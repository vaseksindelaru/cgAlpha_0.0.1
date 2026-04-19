## §5 — LA MEMORIA INTELIGENTE v4: ARQUITECTURA

### 5.1 Arquitectura de 7 niveles

La memoria v4 extiende los 6 niveles de v3 con un séptimo nivel inmune a degradación. El cambio no es solo un número: es una separación ontológica entre "lo que el sistema sabe" (niveles 0a-4) y "lo que el sistema es" (nivel 5).

```
╔══════════════════════════════════════════════════════════════════════════╗
║  MEMORIA INTELIGENTE v4 — 7 NIVELES                                     ║
╠════════╦═════════════╦════════╦═══════════╦════════════════╦════════════╣
║ Nivel  ║ Nombre      ║  TTL   ║ Aprobador ║ Auto-degrada   ║ Propósito  ║
╠════════╬═════════════╬════════╬═══════════╬════════════════╬════════════╣
║  0a    ║ RAW         ║ 24h    ║ Auto      ║ No             ║ Ingesta    ║
║        ║             ║        ║           ║                ║ bruta      ║
╠════════╬═════════════╬════════╬═══════════╬════════════════╬════════════╣
║  0b    ║ NORMALIZED  ║ 7d     ║ Auto      ║ No             ║ Datos      ║
║        ║             ║        ║           ║                ║ limpios    ║
╠════════╬═════════════╬════════╬═══════════╬════════════════╬════════════╣
║  1     ║ FACTS       ║ 30d    ║ Lila      ║ No             ║ Hechos     ║
║        ║             ║        ║           ║                ║ confirmados║
╠════════╬═════════════╬════════╬═══════════╬════════════════╬════════════╣
║  2     ║ RELATIONS   ║ 90d    ║ Lila      ║ No             ║ Relaciones,║
║        ║             ║        ║           ║                ║ reflexiones║
║        ║             ║        ║           ║                ║ y pending  ║
║        ║             ║        ║           ║                ║ proposals  ║
╠════════╬═════════════╬════════╬═══════════╬════════════════╬════════════╣
║  3     ║ PLAYBOOKS   ║ indef  ║ Humano    ║ Sí (4→3 por   ║ Estrategias║
║        ║             ║        ║           ║  régimen)      ║ probadas   ║
╠════════╬═════════════╬════════╬═══════════╬════════════════╬════════════╣
║  4     ║ STRATEGY    ║ indef  ║ Humano    ║ Sí (shift →    ║ Estrategia ║
║        ║             ║        ║           ║  degrada a 3)  ║ activa     ║
╠════════╬═════════════╬════════╬═══════════╬════════════════╬════════════╣
║  5     ║ IDENTITY    ║ ∞      ║ Humano    ║ NUNCA          ║ ADN de     ║
║        ║             ║ nunca  ║ + firma   ║ bajo ninguna   ║ Lila v4    ║
║        ║             ║ expira ║ v4        ║ condición      ║ El mantra  ║
╚════════╩═════════════╩════════╩═══════════╩════════════════╩════════════╝
```

> **C34:** Las propuestas pendientes (Cat.2, Cat.3) se guardan en nivel RELATIONS (TTL 90d), no en FACTS (TTL 30d). Esto evita que expiren antes de la escalada Cat.2→Cat.3 a los 14 días.

### 5.2 Cambios al código existente

#### 5.2.1 Nuevo valor en MemoryLevel enum

**Fichero:** `domain/models/signal.py`, línea 162

```python
class MemoryLevel(str, Enum):
    RAW        = "0a"
    NORMALIZED = "0b"
    FACTS      = "1"
    RELATIONS  = "2"
    PLAYBOOKS  = "3"
    STRATEGY   = "4"
    IDENTITY   = "5"   # v4: TTL=∞, inmune a degradación de régimen
```

#### 5.2.2 Actualización de MemoryPolicyEngine

**Fichero:** `learning/memory_policy.py`

Cambios en constantes de clase:

```python
TTL_BY_LEVEL_HOURS = {
    MemoryLevel.RAW: 24,
    MemoryLevel.NORMALIZED: 24 * 7,
    MemoryLevel.FACTS: 24 * 30,
    MemoryLevel.RELATIONS: 24 * 90,
    MemoryLevel.PLAYBOOKS: None,
    MemoryLevel.STRATEGY: None,
    MemoryLevel.IDENTITY: None,       # ← NUEVO
}

APPROVER_BY_LEVEL = {
    MemoryLevel.RAW: "auto",
    MemoryLevel.NORMALIZED: "auto",
    MemoryLevel.FACTS: "Lila",
    MemoryLevel.RELATIONS: "Lila",
    MemoryLevel.PLAYBOOKS: "human",
    MemoryLevel.STRATEGY: "human",
    MemoryLevel.IDENTITY: "human",    # ← NUEVO
}

LEVEL_ORDER = [
    MemoryLevel.RAW,
    MemoryLevel.NORMALIZED,
    MemoryLevel.FACTS,
    MemoryLevel.RELATIONS,
    MemoryLevel.PLAYBOOKS,
    MemoryLevel.STRATEGY,
    MemoryLevel.IDENTITY,             # ← NUEVO (último, el más alto)
]
```

**Nuevos métodos auxiliares (C18, C30):**

```python
# C30: parse_level() — requerido por load_from_disk()
def parse_level(self, value: str) -> MemoryLevel:
    """Convierte string a MemoryLevel. Lanza ValueError si el valor no es válido."""
    try:
        return MemoryLevel(value)
    except ValueError:
        raise ValueError(
            f"Nivel de memoria desconocido: '{value}'. "
            f"Valores válidos: {[m.value for m in MemoryLevel]}"
        )

# C18: _must_get() — requerido por Orchestrator, reflexiones, approve/reject
def _must_get(self, entry_id: str) -> 'MemoryEntry':
    """Retorna un entry por ID. Lanza KeyError si no existe."""
    if entry_id not in self.entries:
        raise KeyError(
            f"Entry '{entry_id}' not found in memory. "
            f"May have expired or not been loaded from disk."
        )
    return self.entries[entry_id]
```

#### 5.2.3 Guard en detect_and_apply_regime_shift()

**Fichero:** `learning/memory_policy.py`, método `detect_and_apply_regime_shift()`, línea ~199

El guard previene que las entradas IDENTITY sean degradadas por cambio de régimen:

```python
affected = 0
for entry in self.entries.values():
    # GUARD v4: nivel IDENTITY nunca se degrada
    if entry.level == MemoryLevel.IDENTITY:
        continue

    if entry.level == MemoryLevel.STRATEGY:
        entry.level = MemoryLevel.PLAYBOOKS
        entry.stale = True
        entry.approved_by = self.APPROVER_BY_LEVEL[MemoryLevel.PLAYBOOKS]
        affected += 1
    elif entry.level == MemoryLevel.PLAYBOOKS:
        entry.level = MemoryLevel.RELATIONS
        # ... resto igual
```

#### 5.2.4 Validación adicional en promote() + dispatch de persistencia

Promoción a IDENTITY requiere validación extra. **C31:** promote() invoca `_persist_identity_entry()` cuando corresponde.

```python
def promote(self, *, entry_id, target_level, approved_by, tags=None, now=None):
    # ... validación existente ...

    # v4: Promoción a IDENTITY requiere aprobación humana explícita
    if target_level == MemoryLevel.IDENTITY:
        if approved_by != "human":
            raise ValueError(
                "Promoción a IDENTITY requiere approved_by='human'. "
                "Lila puede proponer pero no ejecutar esta promoción."
            )

    entry.level = target_level
    # ... resto de lógica existente ...

    # C31: dispatch de persistencia según nivel
    if target_level == MemoryLevel.IDENTITY:
        self._persist_identity_entry(entry)
    else:
        self._persist_memory_entry(entry)
```

### 5.3 Recarga de memoria al inicio de sesión (fix de BUG-7)

#### 5.3.1 Nuevo método en MemoryPolicyEngine

```python
import json
from pathlib import Path

def load_from_disk(self, directory: str) -> dict:
    """
    Carga todas las entradas de memoria desde ficheros JSON en disco.
    Se llama una vez al iniciar el servidor.

    Args:
        directory: Path a la carpeta de memory_entries
                   (ej: "cgalpha_v3/memory/memory_entries")

    Returns:
        dict con conteo de entradas cargadas por nivel
    """
    dir_path = Path(directory)
    if not dir_path.exists():
        return {"loaded": 0, "errors": 0, "reason": "directory_not_found"}

    loaded = 0
    errors = 0
    identity_error = False
    level_counts = {lvl.value: 0 for lvl in self.LEVEL_ORDER}

    for json_file in sorted(dir_path.glob("*.json")):
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            entry = MemoryEntry(
                entry_id=data["entry_id"],
                level=self.parse_level(data["level"]),  # C30: método definido
                content=data["content"],
                source_id=data.get("source_id"),
                source_type=data.get("source_type"),
                created_at=datetime.fromisoformat(data["created_at"]),
                expires_at=(
                    datetime.fromisoformat(data["expires_at"])
                    if data.get("expires_at") else None
                ),
                approved_by=data.get("approved_by", "auto"),
                field=data.get("field", "trading"),
                tags=data.get("tags", []),
                stale=data.get("stale", False),
            )

            # No cargar entradas expiradas
            now_dt = datetime.now(timezone.utc)
            if entry.expires_at and entry.expires_at <= now_dt:
                continue

            self.entries[entry.entry_id] = entry
            level_counts[entry.level.value] += 1
            loaded += 1

        # C32: Logging detallado por tipo de error, no silenciar
        except json.JSONDecodeError as e:
            errors += 1
            logger.warning(f"JSON corrupto en {json_file.name}: {e}")
            if self._might_be_identity(json_file):
                identity_error = True
        except KeyError as e:
            errors += 1
            logger.warning(f"Campo faltante en {json_file.name}: {e}")
            if self._might_be_identity(json_file):
                identity_error = True
        except Exception as e:
            errors += 1
            logger.error(f"Error inesperado cargando {json_file.name}: "
                        f"{type(e).__name__}: {e}")
            if self._might_be_identity(json_file):
                identity_error = True

    # C32: Alerta crítica si una entrada IDENTITY no pudo cargarse
    if identity_error:
        logger.critical(
            "⚠️ IDENTITY entry no pudo cargarse desde disco — "
            "el mantra puede estar perdido. Verificar memory/identity/ "
            "para backup con hash."
        )

    return {
        "loaded": loaded,
        "errors": errors,
        "levels": level_counts,
        "total_on_disk": loaded + errors,
        "identity_error": identity_error,
    }

def _might_be_identity(self, json_file: Path) -> bool:
    """Heurística para detectar si un fichero corrupto era IDENTITY."""
    try:
        text = json_file.read_text(encoding="utf-8", errors="ignore")
        return '"5"' in text or '"IDENTITY"' in text or '"mantra"' in text
    except Exception:
        return False
```

#### 5.3.2 Invocación al iniciar el servidor

**Fichero:** `gui/server.py`, en el bloque de inicialización (cerca de línea 115):

```python
# Después de crear memory_engine:
memory_engine = MemoryPolicyEngine()

# v4: Cargar memoria persistida desde disco
load_result = memory_engine.load_from_disk("cgalpha_v3/memory/memory_entries")
logger.info(f"✓ Memoria cargada desde disco: {load_result['loaded']} entradas, "
            f"{load_result['errors']} errores")

if load_result.get("identity_error"):
    logger.critical("⚠️ No se pudo cargar el mantra IDENTITY — el sistema "
                    "puede estar operando sin instrucciones fundacionales")
```

#### 5.3.3 Persistencia de nuevas entradas (confirmar)

El servidor ya persiste entradas vía `_persist_memory_entry()`. Verificar que:
- Escribe en `cgalpha_v3/memory/memory_entries/{entry_id}.json`
- El formato coincide con el que `load_from_disk()` espera
- Las actualizaciones (promote, degrade) sobreescriben el fichero existente

### 5.4 Persistencia del nivel IDENTITY

Las entradas IDENTITY tienen requisitos especiales de persistencia:

```python
def _persist_identity_entry(self, entry: 'MemoryEntry'):
    """
    Persistencia reforzada para nivel IDENTITY.
    Además del fichero JSON estándar, crea un backup con hash.

    C31: Este método se llama desde promote() cuando
    target_level == MemoryLevel.IDENTITY.
    """
    # 1. Persistencia estándar
    self._persist_memory_entry(entry)

    # 2. Backup con hash para detectar corrupción
    import hashlib
    content_hash = hashlib.sha256(entry.content.encode()).hexdigest()[:16]
    backup_path = Path(f"cgalpha_v3/memory/identity/"
                       f"{entry.entry_id}_{content_hash}.json")
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    with open(backup_path, "w", encoding="utf-8") as f:
        json.dump({
            "entry_id": entry.entry_id,
            "level": entry.level.value,
            "content": entry.content,
            "content_hash": content_hash,
            "created_at": entry.created_at.isoformat(),
            "approved_by": entry.approved_by,
            "field": entry.field,
            "tags": entry.tags,
        }, f, indent=2, ensure_ascii=False)
```

### 5.5 Tipos de contenido por nivel — guía para el Orchestrator

| Nivel | Qué se guarda | Campo (field) típico | Quién escribe |
|---|---|---|---|
| 0a RAW | Métricas brutas del ciclo, logs de AutoProposer | trading | Pipeline automático |
| 0b NORMALIZED | Métricas normalizadas, resultados de experimentos | trading, math | Pipeline + Lila |
| 1 FACTS | Resultados confirmados: "Sharpe del ciclo = X" | trading | Lila (auto-aprobado) |
| 2 RELATIONS | Reflexiones críticas, propuestas pendientes (Cat.2/Cat.3), correlaciones | architect, memory_librarian | Lila (auto-aprobado, TTL 90d) |
| 3 PLAYBOOKS | Estrategias validadas por OOS, parameter landscape consolidado | trading, architect | Humano (aprobación) |
| 4 STRATEGY | Configuración activa del sistema, LLM switcher config | architect | Humano (aprobación) |
| 5 IDENTITY | El prompt fundacional, principios invariantes | architect | Humano + firma v4 |

### 5.6 Búsqueda en memoria — interfaz para el Orchestrator

El `MemoryPolicyEngine` de v3 tiene `list_entries(level, field, limit)`. Para v4, el Orchestrator necesita buscar por contenido:

```python
def search(self, *, query: str, level: MemoryLevel | None = None,
           field: str | None = None, limit: int = 20) -> list['MemoryEntry']:
    """
    Búsqueda por substring en el contenido de las entradas.
    Para v4.1: reemplazar por búsqueda semántica con embeddings.
    """
    results = []
    query_lower = query.lower()
    for entry in self.entries.values():
        if level and entry.level != level:
            continue
        if field and entry.field != field:
            continue
        if query_lower in entry.content.lower():
            results.append(entry)
    results.sort(key=lambda e: e.created_at, reverse=True)
    return results[:limit]


def get_identity_entries(self) -> list['MemoryEntry']:
    """Atajo para obtener todas las entradas IDENTITY."""
    return self.list_entries(level=MemoryLevel.IDENTITY, limit=100)


def get_pending_proposals(self) -> list['MemoryEntry']:
    """Atajo para el Orchestrator: propuestas pendientes de aprobación."""
    entries = self.list_entries(level=MemoryLevel.RELATIONS, limit=200)
    return [e for e in entries if "pending" in e.tags]
```

### 5.7 Snapshot v4 — extensión del dashboard

El método `snapshot()` existente se extiende para incluir el nuevo nivel. **C35 corregido:** se muestra el patrón completo, no una referencia a variable indefinida.

```python
def snapshot(self) -> dict:
    # Calcular conteos existentes (lógica v3 intacta)
    levels = {lvl.value: 0 for lvl in self.LEVEL_ORDER}
    for entry in self.entries.values():
        if not entry.stale:
            levels[entry.level.value] += 1

    # v4: métricas adicionales
    identity_count = levels.get("5", 0)
    pending_count = sum(1 for e in self.entries.values() if "pending" in e.tags)

    return {
        "total_entries": sum(levels.values()),
        "by_level": levels,
        # v4 añade:
        "identity_entries": identity_count,
        "pending_proposals": pending_count,
        "memory_health": "healthy" if identity_count > 0 else "no_identity",
    }
```

### 5.8 Tests mínimos requeridos

```python
# test_memory_v4.py

def test_identity_level_exists():
    assert MemoryLevel.IDENTITY.value == "5"

def test_identity_ttl_is_infinite():
    assert MemoryPolicyEngine.TTL_BY_LEVEL_HOURS[MemoryLevel.IDENTITY] is None

def test_identity_requires_human_approval():
    engine = MemoryPolicyEngine()
    entry = engine.ingest_raw(content="test", field="architect")
    with pytest.raises(ValueError, match="approved_by='human'"):
        engine.promote(
            entry_id=entry.entry_id,
            target_level=MemoryLevel.IDENTITY,
            approved_by="Lila"  # Debe fallar
        )

def test_identity_not_degraded_by_regime_shift():
    engine = MemoryPolicyEngine()
    entry = engine.ingest_raw(content="mantra", field="architect")
    engine.promote(entry_id=entry.entry_id,
                   target_level=MemoryLevel.IDENTITY,
                   approved_by="human")

    # Simular régimen shift con datos suficientes
    vol_series = [1.0] * 40 + [10.0] * 20  # shift extremo
    result = engine.detect_and_apply_regime_shift(vol_series)

    # El entry IDENTITY debe seguir en nivel 5
    assert engine.entries[entry.entry_id].level == MemoryLevel.IDENTITY

def test_load_from_disk(tmp_path):
    # Crear fichero JSON de prueba
    entry_data = {
        "entry_id": "test-uuid",
        "level": "1",
        "content": "test content",
        "source_id": None,
        "source_type": "secondary",
        "created_at": "2026-04-19T00:00:00+00:00",
        "expires_at": "2026-05-19T00:00:00+00:00",
        "approved_by": "auto",
        "field": "trading",
        "tags": ["test"],
        "stale": False
    }
    (tmp_path / "test-uuid.json").write_text(json.dumps(entry_data))

    engine = MemoryPolicyEngine()
    result = engine.load_from_disk(str(tmp_path))

    assert result["loaded"] == 1
    assert "test-uuid" in engine.entries
    assert engine.entries["test-uuid"].level == MemoryLevel.FACTS

def test_expired_entries_not_loaded(tmp_path):
    entry_data = {
        "entry_id": "expired-uuid",
        "level": "0a",
        "content": "old data",
        "created_at": "2025-01-01T00:00:00+00:00",
        "expires_at": "2025-01-02T00:00:00+00:00",  # expirado
        "approved_by": "auto",
        "field": "trading",
        "tags": [],
        "stale": False
    }
    (tmp_path / "expired-uuid.json").write_text(json.dumps(entry_data))

    engine = MemoryPolicyEngine()
    result = engine.load_from_disk(str(tmp_path))

    assert result["loaded"] == 0
    assert "expired-uuid" not in engine.entries

# C33 corregido: test usa el flujo real de persistencia, no escritura manual
def test_identity_survives_full_cycle(tmp_path):
    """Test end-to-end: crear IDENTITY, persistir via promote(), recargar."""
    # El MemoryPolicyEngine necesita memory_dir configurable para este test.
    # Si v3 no lo soporta, el test DEBE usar el método real de persistencia.
    engine = MemoryPolicyEngine()
    # Configurar directorio de persistencia para el test
    engine._memory_dir = str(tmp_path)

    entry = engine.ingest_raw(content="mantra fundacional", field="architect")
    # promote() llama _persist_identity_entry() que escribe a disco (C31)
    engine.promote(entry_id=entry.entry_id,
                   target_level=MemoryLevel.IDENTITY,
                   approved_by="human")

    # Verificar que el fichero se escribió
    json_path = tmp_path / f"{entry.entry_id}.json"
    assert json_path.exists(), "promote() no persistió el entry a disco"

    # Nuevo engine (simula reinicio)
    engine2 = MemoryPolicyEngine()
    result = engine2.load_from_disk(str(tmp_path))

    assert result["loaded"] >= 1
    reloaded = engine2.entries[entry.entry_id]
    assert reloaded.level == MemoryLevel.IDENTITY
    assert reloaded.content == "mantra fundacional"

def test_must_get_raises_on_missing():
    """C18: _must_get() lanza KeyError si el entry no existe."""
    engine = MemoryPolicyEngine()
    with pytest.raises(KeyError, match="not found in memory"):
        engine._must_get("nonexistent-uuid")

def test_must_get_returns_existing():
    """C18: _must_get() retorna el entry si existe."""
    engine = MemoryPolicyEngine()
    entry = engine.ingest_raw(content="test", field="trading")
    result = engine._must_get(entry.entry_id)
    assert result.content == "test"

def test_parse_level_valid():
    """C30: parse_level() convierte strings válidos."""
    engine = MemoryPolicyEngine()
    assert engine.parse_level("5") == MemoryLevel.IDENTITY
    assert engine.parse_level("0a") == MemoryLevel.RAW

def test_parse_level_invalid():
    """C30: parse_level() lanza ValueError con string inválido."""
    engine = MemoryPolicyEngine()
    with pytest.raises(ValueError, match="desconocido"):
        engine.parse_level("99")

# C36: test para get_identity_entries()
def test_get_identity_entries_returns_only_identity():
    engine = MemoryPolicyEngine()
    e1 = engine.ingest_raw(content="fact", field="trading")
    e2 = engine.ingest_raw(content="mantra", field="architect")
    engine.promote(entry_id=e2.entry_id,
                   target_level=MemoryLevel.IDENTITY,
                   approved_by="human")

    identities = engine.get_identity_entries()
    assert len(identities) == 1
    assert identities[0].entry_id == e2.entry_id

def test_load_from_disk_logs_corrupt_identity(tmp_path, caplog):
    """C32: Fichero corrupto con indicios de IDENTITY genera alerta crítica."""
    corrupt_content = '{"level": "5", "entry_id": "bad", CORRUPTED'
    (tmp_path / "bad.json").write_text(corrupt_content)

    engine = MemoryPolicyEngine()
    with caplog.at_level(logging.CRITICAL):
        result = engine.load_from_disk(str(tmp_path))

    assert result["errors"] == 1
    assert result["identity_error"] is True
```
