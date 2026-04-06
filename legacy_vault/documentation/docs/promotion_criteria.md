# Protocolo de Promoción Labs -> Producción (Sección P3.3)
=====================================================

Este documento define los criterios técnicos y estadísticos obligatorios para que una propuesta (`Proposal`) y sus resultados de experimento (`ExperimentResult`) sean considerados APTOS para operar en el mercado real (Producción).

## 1. Métricas de Rendimiento Fuera de Muestra (OOS)

El sistema CGAlpha v3 exige que los resultados netos (post-fricción) del periodo Out-Of-Sample (OOS) cumplan los siguientes umbrales mínimos:

| Métrica | Umbral Mínimo | Justificación |
|---------|---------------|---------------|
| **Sharpe Ratio OOS** | ≥ 0.8 | Estabilidad de retornos ajustados al riesgo. |
| **Max Drawdown OOS** | ≤ 15.0% | Control de capital y preservación de cuenta. |
| **Calmar Ratio OOS** | ≥ 1.5 | Eficiencia estructural (Retorno / MaxDD). |
| **Profit Factor OOS** | ≥ 1.3 | Ventaja estadística sobre el costo de fricción. |
| **Win Rate OOS** | ≥ 45% | Consistencia operativa (dependiente del R:R). |

## 2. Requerimientos de Integridad Técnica

No se permitirá la promoción si no se validan los siguientes puntos:

1.  **Cero Leakage Temporal**: El experimento debe haber pasado el check de `TemporalLeakageError` sin excepciones en ninguna de las >=3 ventanas.
2.  **SLA de Latencia**: La latencia media de ejecución del experimento debe ser < 60s (SLA P3.5).
3.  **Estado de Salud del Sistema**: El `HealthMonitor` debe reportar estado `healthy`. Si el sistema está `degraded` o `critical`, el Gate de Producción se cierra automáticamente.

## 3. Criterios de Estructura de Datos

1.  **Walk-Forward Windows**: Mínimo de 3 ventanas temporales independientes.
2.  **Continuidad de Datos**: El set de OOS no debe contener gaps masivos (> 4h sin registros) a menos que se justifique por cierre de mercado.
3.  **Inconsistencia de Precios**: El `DataQualityGate` debe haber emitido un reporte `valid` para el dataset utilizado.

## 4. Proceso de Promoción (Workflow)

1.  **Labs**: Desarrollo de hipótesis y entrenamiento inicial.
2.  **Simulation**: Ejecución de Experiment Loop v3 (Walk-forward + Fricción).
3.  **Production Gate**: Llamada al endpoint `POST /api/promotion/validate` con el `experiment_id`.
4.  **Habilitación**: Si el validador retorna `status: approved`, el `ExperimentRunner` marca el modelo como "Deployable".
