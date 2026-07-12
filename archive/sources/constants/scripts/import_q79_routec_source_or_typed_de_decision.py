"""Import q79 Route-C selected source or typed D_E construction decision."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = DATA / "q79_selected_de_green_dotd_source_gate_import.candidate.json"
DE_HUNT = Q79 / "certificates" / "selected_de_source_hunt_certificate.json"
DE_ATTEMPT = Q79 / "certificates" / "iwasawa_selected_de_construction_attempt_certificate.json"
Q79_DE_GATE = Q79 / "certificates" / "q79_selected_de_green_dotd_source_for_primitive_c1_certificate.json"

OUTPUT_PACKET = DATA / "q79_routec_source_or_typed_de_decision_import.candidate.json"
OUTPUT_CERT = CERTS / "q79_routec_source_or_typed_de_decision_import_certificate.json"
OUTPUT_NOTE = CORPUS / "Q79_RouteC_Source_or_Typed_DE_Decision_Import_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load_json(PREVIOUS)
    hunt = load_json(DE_HUNT)
    attempt = load_json(DE_ATTEMPT)
    de_gate = load_json(Q79_DE_GATE)

    checks = {
        "R0_previous_next_matches_routec_or_typed_de": previous["verdict"][
            "next_required_artifact"
        ]
        == "Q79_RouteC_Selected_Source_Certificate_or_Typed_DE_Construction_v1",
        "R1_exact_next_artifact_absent_but_adjacent_hunts_present": hunt["verdict"][
            "source_hunt_closed"
        ]
        is True
        and attempt["verdict"]["diagnostic_pipeline_ready"] is True,
        "R2_selected_de_source_not_found": hunt["hunt_result"][
            "selected_D_E_source_found"
        ]
        is False
        and attempt["verdict"]["selected_D_E_constructed"] is False,
        "R3_first_blocker_is_selected_operator_source": hunt["hunt_result"][
            "first_blocking_layer_confirmed"
        ]
        == "selected_operator_source",
        "R4_route_c_recommended": hunt["hunt_result"]["best_next_route"]
        == "Route C: direct finite HYM/Strominger selected-connection solve scaffold",
        "R5_three_legal_routes_preserved": len(attempt["minimal_new_data_to_close"]["one_of"])
        == 3,
        "R6_de_gate_still_no_closure": de_gate["closure_claimed"] is False
        and de_gate["next_required_artifact"]
        == "Q79_RouteC_Selected_Source_Certificate_or_Typed_DE_Construction_v1",
    }
    proved = all(checks.values())

    legal_routes = {
        "A_typed_monad_cech_package": (
            "typed f_i,g_i sections, transition/Cech data, g o f = 0, "
            "exactness/local freeness, and H1 representatives"
        ),
        "B_corrected_non_invariant_dolbeault_operator": (
            "selected A^(0,1)(x) with integrability, HYM/Strominger residuals, "
            "family count, and sector maps"
        ),
        "C_direct_finite_hym_strominger_solve": (
            "finite rho_E/A_N/H_N solve with cocycle, integrability, HYM, "
            "Bianchi/Strominger residual, MTT selection, gap, and zero modes"
        ),
    }

    return {
        "packet": "Q79_RouteC_Source_or_Typed_DE_Decision_Import_v1",
        "status": (
            "Q79_ROUTEC_SOURCE_OR_TYPED_DE_DECISION_IMPORTED"
            if proved
            else "Q79_ROUTEC_SOURCE_OR_TYPED_DE_DECISION_IMPORT_FAILED"
        ),
        "inputs": {
            "previous": str(PREVIOUS.relative_to(ROOT)),
            "selected_de_source_hunt": str(DE_HUNT),
            "iwasawa_selected_de_construction_attempt": str(DE_ATTEMPT),
            "q79_de_green_dotd_gate": str(Q79_DE_GATE),
        },
        "theorem": {
            "name": "Q79RouteCSourceOrTypedDEDecisionImport",
            "proved": proved,
            "statement": (
                "The exact next q79 source certificate is not already closed in "
                "the corpus. Existing adjacent audits prove the selected D_E "
                "source is still absent, the diagnostic pipeline is ready, and "
                "the legal way forward is one of three concrete construction "
                "routes: typed monad/Cech data, corrected non-invariant A^(0,1), "
                "or direct finite HYM/Strominger Route-C solve."
            ),
        },
        "import_checks": checks,
        "source_hunt": {
            "status": hunt["status"],
            "selected_D_E_source_found": hunt["hunt_result"]["selected_D_E_source_found"],
            "best_next_route": hunt["hunt_result"]["best_next_route"],
            "candidate_results": hunt["candidate_results"],
        },
        "construction_attempt": {
            "status": attempt["status"],
            "route_evaluation": attempt["route_evaluation"],
            "diagnostic_pipeline_ready": attempt["verdict"]["diagnostic_pipeline_ready"],
            "minimal_new_data_to_close": attempt["minimal_new_data_to_close"],
        },
        "legal_routes": legal_routes,
        "decision": {
            "exact_q79_next_artifact_closed": False,
            "selected_D_E_constructed": False,
            "diagnostic_hodge_pipeline_ready": True,
            "recommended_first_build": "C_direct_finite_hym_strominger_solve",
            "why": hunt["hunt_result"]["why_route_c"],
            "next_required_artifact": "Finite_Selected_Connection_Solve_Scaffold_for_q79_v1",
        },
        "guardrails": {
            "does_not_claim_selected_D_E_found": hunt["guardrails"][
                "claims_selected_D_E_found"
            ]
            is False
            and attempt["guardrails"]["claims_selected_D_E_constructed"] is False,
            "does_not_use_diagnostic_candidate_as_selected": hunt["guardrails"][
                "uses_diagnostic_h1_three_as_selected"
            ]
            is False
            and attempt["guardrails"]["uses_diagnostic_candidate_as_selected"] is False,
            "does_not_promote_abstract_HYM_to_matrix": hunt["guardrails"][
                "promotes_abstract_hym_existence_to_matrix"
            ]
            is False
            and attempt["guardrails"]["promotes_abstract_Li_Yau_existence_to_matrix"]
            is False,
            "does_not_use_observed_or_benchmark_inputs": hunt["guardrails"][
                "uses_execution_ii_benchmarks_as_inputs"
            ]
            is False
            and attempt["guardrails"]["uses_observed_flavor_data"] is False,
            "does_not_claim_full_SM_closure": hunt["guardrails"]["claims_full_sm_closure"]
            is False
            and attempt["guardrails"]["claims_full_sm_closure"] is False,
        },
        "verdict": {
            "what_closes_now": (
                "The source-search loop is closed negatively: no selected D_E "
                "source is currently present, and the legal construction routes "
                "are enumerated."
            ),
            "what_remains": (
                "Build the finite selected-connection solve scaffold, or supply "
                "typed monad/Cech data or corrected non-invariant A^(0,1)."
            ),
            "next_required_artifact": "Finite_Selected_Connection_Solve_Scaffold_for_q79_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "Q79RouteCSourceOrTypedDEDecisionImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "import_checks": packet["import_checks"],
        "decision": packet["decision"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# Q79 Route-C Source or Typed D_E Decision Import v1

## Result

Status: `{cert["status"]}`

The exact selected Route-C source certificate is not already closed in q79.
The adjacent q79 source hunt and construction attempt agree: selected `D_E` is
still absent, while the diagnostic Hodge/Galerkin pipeline is ready.

## Import Checks

```json
{json.dumps(packet["import_checks"], indent=2, sort_keys=True)}
```

## Legal Routes

```json
{json.dumps(packet["legal_routes"], indent=2, sort_keys=True)}
```

## Decision

```json
{json.dumps(packet["decision"], indent=2, sort_keys=True)}
```
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_CERT.write_text(
            json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
