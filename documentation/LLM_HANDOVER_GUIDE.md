# LILA v3 — Master LLM Handover Guide 🛰️🧠💎

This guide defines the protocol for an external LLM (Orchestrator) to manage the **CGAlpha v3** system following the **North Star 3.0.0** canon.

## 1. Orchestration API Endpoints (v3.0.0)

Lila v3 is now controllable via the following authenticated REST endpoints:

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/lila/execute-cycle` | `POST` | Triggers a full learning cycle (Harvest -> Oracle Training). |
| `/api/lila/command` | `POST` | Executes technical modifications (TechnicalSpec). |
| `/api/vault/status` | `GET` | Returns full system state, metrics, and DNA inventory. |
| `/api/vault/promote` | `POST` | Promotes a validated component to Layer 2 (DNA). |

## 2. Command Schema (Lila Orchestrator)

The external LLM should send instruction objects to `/api/lila/command` using the following schema:

```json
{
  "action": "update_param",
  "component": "oracle_v3",
  "parameter": "confidence_threshold",
  "value": 0.85,
  "reason": "Adjustment requested due to OOS drift detection."
}
```

## 3. Mandatory Invariants (The Canon)

The Orchestrator MUST NEVER bypass these gates:
1. **Nexus Gate**: All code promotions to Layer 2 require **ΔCausal > 0** in OOS data.
2. **Binary Promotion**: A component is either in **Layer 1 (Provisional)** or **Layer 2 (Permanent)**. Layer 2 is immutable.
3. **Trinity First**: All strategy logic must rely on **VWAP, OBI, and Cumulative Delta**. ATR is for normalization only.

## 4. Operational Flow

1. **Observe**: Fetch `/api/vault/status`.
2. **Analyze**: Identify performance gaps or parameter drift.
3. **Act**: Send `/api/lila/command` or trigger `/api/lila/execute-cycle`.
4. **Validate**: Monitor the **Nexus Gate** decision.

---
**Lila v3 is ready for handoff. Causal Immortalization: ACHIEVED.** 💎🚀🏆
