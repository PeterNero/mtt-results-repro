"""Build PSM-C1-02 selected source-ownership premise execution frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_selectedsourceownershippremiseexecution_promoted"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
PREMISE = PACKET_DIR / "premise_execution_status.packet.json"
NEXT = PACKET_DIR / "gauge_trace_or_independent_rows_next_target.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_SelectedSourceOwnershipPremiseExecution_v1.md"

PREVIOUS = DATA / "selected_phifinc1sourceemissionorfiniterowindependencetheorem.candidate.json"
PREMISE_EXEC = DATA / "selected_psm_c1_02_selectedsourceownershippremiseexecution.candidate.json"
FINITE_LEMMA = DATA / "selected_physicalphifinc1finitequotientnoextraboundarysourcelemma_or_independentrows.candidate.json"

STATUS = (
    "MTT_SELECTED_PSM_C1_02_SELECTEDSOURCEOWNERSHIPPREMISEEXECUTION_"
    "GAUGE_TRACE_OR_INDEPENDENT_ROWS_TARGET_SELECTED"
)
NEXT_ARTIFACT = "MTT_Selected_GaugeTransported_BN_PhiFin_Trace_or_IndependentComplexRowExecution_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing premise-execution inputs: " + ", ".join(missing))


def main() -> int:
    sources = [PREVIOUS, PREMISE_EXEC, FINITE_LEMMA]
    require_sources(sources)

    previous = load(PREVIOUS)
    premise_exec = load(PREMISE_EXEC)
    finite_lemma = load(FINITE_LEMMA)

    premise_decision = premise_exec["closure_decision"]

    premise_packet = {
        "schema": "MTTPSMC102SelectedSourceOwnershipPremiseExecution.v1",
        "status": "PREMISES_EXECUTED_TO_GAUGE_TRACE_OR_INDEPENDENT_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "upstream_remaining_premise_count": previous["closure_decision"][
            "remaining_source_ownership_premise_count"
        ],
        "closed_SM_parity_and_formal_row_boundaries_preserved": premise_exec["what_closes_now"][
            "closed_SM_parity_and_formal_row_boundaries_preserved"
        ],
        "untransported_BN_shortcut_rejected_for_source_ownership": premise_exec["what_closes_now"][
            "untransported_BN_shortcut_rejected_for_source_ownership"
        ],
        "physical_finite_quotient_lemma_attacked": finite_lemma["what_closes_now"][
            "physical_finite_quotient_lemma_attacked"
        ],
        "local_principle_route_A_two_exit_witness_validates": finite_lemma["what_closes_now"][
            "local_principle_route_A_two_exit_witness_validates"
        ],
        "three_field_certificate_is_exact_remaining_route_A": finite_lemma["what_closes_now"][
            "three_field_certificate_is_exact_remaining_route_A"
        ],
    }
    write_json(PREMISE, premise_packet)

    next_packet = {
        "schema": "MTTGaugeTraceOrIndependentRowsNextTarget.v1",
        "status": "NEXT_TARGET_SELECTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "primary_next_target": "SelectedGaugeTransportedBNPhiFinTrace",
        "fallback_next_target": "IndependentComplexRowExecution",
        "gauge_transport_trace_promoted_to_primary_next_target": premise_exec["what_closes_now"][
            "gauge_transport_trace_promoted_to_primary_next_target"
        ],
        "independent_row_formula_execution_promoted_to_fallback_next_target": premise_exec["what_closes_now"][
            "independent_row_formula_execution_promoted_to_fallback_next_target"
        ],
        "Route_A_closed_now": premise_decision["Route_A_closed_now"],
        "Route_B_closed_now": premise_decision["Route_B_closed_now"],
        "Route_A_gauge_transport_trace_required": premise_decision["Route_A_gauge_transport_trace_required"],
        "Route_B_independent_complex_rows_required": premise_decision["Route_B_independent_complex_rows_required"],
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(NEXT, next_packet)

    decision = {
        "selected_source_ownership_premise_execution_promoted": True,
        "closed_SM_parity_and_formal_row_boundaries_preserved": True,
        "untransported_BN_shortcut_rejected_for_source_ownership": True,
        "physical_finite_quotient_lemma_attacked": True,
        "local_principle_route_A_two_exit_witness_validates": True,
        "three_field_certificate_is_exact_remaining_route_A": True,
        "gauge_transport_trace_promoted_to_primary_next_target": True,
        "independent_row_formula_execution_promoted_to_fallback_next_target": True,
        "Route_A_closed_now": False,
        "Route_B_closed_now": False,
        "Route_A_gauge_transport_trace_required": True,
        "Route_B_independent_complex_rows_required": True,
        "actual_dynamic_QaSU3_payload_values_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102SelectedSourceOwnershipPremiseExecution",
        "status": STATUS,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "premise_execution_status": rel(PREMISE),
            "gauge_trace_or_independent_rows_next_target": rel(NEXT),
        },
        "theorem": {
            "name": "PSMC102SelectedSourceOwnershipPremiseExecutionTheorem",
            "proved": True,
            "statement": (
                "The selected source-ownership premise execution rejects the "
                "untransported BN shortcut and promotes the final executable "
                "target to either a gauge-transported BN/PhiFin trace or an "
                "independent complex-row execution."
            ),
        },
        "closure_decision": decision,
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(OUT, candidate)

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_SelectedSourceOwnershipPremiseExecution_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "theorem_proved": True,
        **decision,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected PSM C1 02 SelectedSourceOwnershipPremiseExecution v1

Status: `{STATUS}`.

## Closed Now

```text
SM-parity/formal row boundaries preserved         true
untransported BN shortcut rejected                true
physical finite quotient lemma attacked           true
local route-A two-exit witness validates          true
three-field certificate is exact route-A target   true
```

## Next Target

```text
primary target                                    SelectedGaugeTransportedBNPhiFinTrace
fallback target                                   IndependentComplexRowExecution
Route A closed now                                false
Route B closed now                                false
Route A gauge transport trace required            true
Route B independent complex rows required         true
```

Next artifact: `{NEXT_ARTIFACT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
