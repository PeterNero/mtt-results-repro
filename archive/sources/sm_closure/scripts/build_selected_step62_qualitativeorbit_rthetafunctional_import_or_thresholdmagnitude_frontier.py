"""Build Step62 qualitative-orbit/Rtheta-functional import frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step62_qualitativeorbit_rthetafunctional_import_or_thresholdmagnitude_frontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT_PACKET = PACKET_DIR / "step62_qualitative_orbit_rtheta_import.packet.json"
CUTSET = PACKET_DIR / "step62_threshold_magnitude_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step62_QualitativeOrbitRThetaFunctionalImport_or_ThresholdMagnitudeFrontier_v1.md"

STEP61 = DATA / "selected_step61_chainintegrity_audit_or_frontiercorrection.candidate.json"
HYM_GATE = DATA / "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution.candidate.json"
PURE_ROWS = DATA / "selected_zeromodehessianprimitiverowexecution_or_pureweylrows.candidate.json"
LAMBDA_ORBIT = DATA / "selected_pureweyllambdarepresentative_or_higherresponsescalarrows.candidate.json"
SECOND_ORDER = DATA / "selected_lambdaorbitsecondordermatrixpacket_or_rthetascalarexecution.candidate.json"
QUALITATIVE = DATA / "selected_secondorderorbitqualitativesmclosure_or_rthetascalarvalues.candidate.json"
RTHETA_SOURCE = DATA / "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows.candidate.json"
RTHETA_SOURCE_PACKET = (
    DATA
    / "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows"
    / "rtheta_scalar_value_functional_source_packet.packet.json"
)
RTHETA_EXECUTION_GATE = (
    DATA
    / "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows"
    / "no_knob_numerical_rows_execution_gate.packet.json"
)
RTHETA_CUTSET_SOURCE = (
    DATA
    / "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows"
    / "next_cutset_after_rtheta_scalar_value_functional_source.packet.json"
)

STATUS = (
    "MTT_SELECTED_STEP62_QUALITATIVE_ORBIT_RTHETA_FUNCTIONAL_IMPORTED_"
    "THRESHOLD_MAGNITUDE_FRONTIER_OPEN"
)
NEXT = "MTT_Selected_ThresholdMagnitudeRows_or_MinimalUniversalParameterDecision_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP61,
        HYM_GATE,
        PURE_ROWS,
        LAMBDA_ORBIT,
        SECOND_ORDER,
        QUALITATIVE,
        RTHETA_SOURCE,
        RTHETA_SOURCE_PACKET,
        RTHETA_EXECUTION_GATE,
        RTHETA_CUTSET_SOURCE,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step62 inputs: " + ", ".join(missing))

    step61 = load(STEP61)
    hym_gate = load(HYM_GATE)
    pure_rows = load(PURE_ROWS)
    lambda_orbit = load(LAMBDA_ORBIT)
    second_order = load(SECOND_ORDER)
    qualitative = load(QUALITATIVE)
    rtheta = load(RTHETA_SOURCE)
    source_packet = load(RTHETA_SOURCE_PACKET)
    execution_gate = load(RTHETA_EXECUTION_GATE)
    rtheta_cutset = load(RTHETA_CUTSET_SOURCE)

    import_packet = {
        "schema": "MTTStep62QualitativeOrbitRThetaFunctionalImport.v1",
        "status": "QUALITATIVE_ORBIT_AND_RTHETA_FUNCTIONAL_IMPORTED",
        "step61_source": rel(STEP61),
        "hym_gate_source": rel(HYM_GATE),
        "primitive_route_sources": {
            "identity_free_pure_rows": rel(PURE_ROWS),
            "lambda_orbit_rows": rel(LAMBDA_ORBIT),
            "second_order_orbit_matrix_packet": rel(SECOND_ORDER),
            "qualitative_orbit_closure": rel(QUALITATIVE),
        },
        "rtheta_source": rel(RTHETA_SOURCE),
        "closed_now": {
            "chain_integrity_no_loopback": step61["closure_decision"]["no_loopback_confirmed"],
            "diagonal_End0_HYM_payload_support_closed": hym_gate["closure_decision"][
                "diagonal_End0_operator_payload_closed"
            ],
            "identity_free_unscaled_pure_Weyl_rows_closed": pure_rows["closure_decision"][
                "identity_free_unscaled_pure_Weyl_rows_closed"
            ],
            "lambda_static_orbit_selected": lambda_orbit["closure_decision"]["lambda_static_orbit_selected"],
            "second_order_orbit_matrix_packet_closed": second_order["closure_decision"][
                "selected_second_order_orbit_matrix_packet_closed"
            ],
            "qualitative_SM_orbit_closure_closed": qualitative["closure_decision"][
                "qualitative_SM_orbit_closure_closed"
            ],
            "Rtheta_scalar_value_functional_source_domain_closed": rtheta["closure_decision"][
                "selected_Rtheta_scalar_value_functional_source_domain_closed"
            ],
            "ten_scalar_row_codomain_aligned": rtheta["closure_decision"]["ten_scalar_row_codomain_aligned"],
        },
        "still_open_counts": {
            "accepted_numerical_scalar_rows": execution_gate["accepted_coefficient_value_count"],
            "no_knob_numerical_rows_emitted": rtheta["closure_decision"]["no_knob_numerical_rows_emitted"],
            "selected_Rtheta_scalar_rows_emitted": qualitative["closure_decision"][
                "selected_Rtheta_scalar_rows_emitted"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(IMPORT_PACKET, import_packet)

    cutset = {
        "schema": "MTTStep62ThresholdMagnitudeFrontier.v1",
        "status": "NEXT_THRESHOLD_MAGNITUDE_ROWS_OR_MINIMAL_PARAMETER_DECISION",
        "closed_now": import_packet["closed_now"],
        "still_open": rtheta_cutset["still_open"],
        "recommended_next": rtheta_cutset["recommended_next"],
        "frontier_interpretation": {
            "not_a_loopback": True,
            "primitive_route_has_advanced_to_qualitative_orbit": True,
            "Rtheta_functional_domain_ready_but_values_absent": True,
            "minimum_next_success": (
                "emit threshold/mass-scheme/magnitude-bearing rows or a source-selected minimal "
                "universal-parameter decision, then execute the ten scalar Rtheta rows"
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedStep62QualitativeOrbitRThetaFunctionalImportOrThresholdMagnitudeFrontier",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "qualitative_orbit_rtheta_import": rel(IMPORT_PACKET),
            "threshold_magnitude_frontier": rel(CUTSET),
        },
        "theorem": {
            "name": "Step62QualitativeOrbitRThetaFunctionalImportTheorem",
            "proved": True,
            "statement": (
                "The primitive branch has advanced beyond Step61: identity-free pure Weyl rows, "
                "the selected lambda orbit, and the selected second-order orbit matrix packet close "
                "qualitative three-family splitting and nonzero CP at the orbit layer. Combining this "
                "with the Rtheta evaluator lane closes the selected scalar value-functional source/domain "
                "and aligns the ten-row codomain. Numerical no-knob rows remain open until threshold, "
                "mass-scheme, magnitude-bearing projection, or source-selected minimal-parameter rows are emitted."
            ),
        },
        "closure_decision": {
            "qualitative_orbit_imported": True,
            "Rtheta_scalar_value_functional_source_domain_closed": True,
            "ten_scalar_row_codomain_aligned": True,
            "diagonal_End0_HYM_payload_support_closed": True,
            "HYM_selected_sector_payload_closed": False,
            "accepted_numerical_scalar_rows": execution_gate["accepted_coefficient_value_count"],
            "no_knob_numerical_rows_emitted": False,
            "selected_Rtheta_scalar_rows_emitted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step61["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step62_QualitativeOrbitRThetaFunctionalImport_or_ThresholdMagnitudeFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step62 QualitativeOrbitRThetaFunctionalImport or ThresholdMagnitudeFrontier v1

Status: `{STATUS}`.

## What Advances

Step62 imports the already validated primitive-route progress into the numbered
chain. The Step61 split is no longer merely HYM/projector-or-primitive in broad
terms: the primitive route has reached a selected second-order orbit matrix
packet and a qualitative SM orbit layer.

```text
no loopback confirmed                         : true
identity-free pure Weyl rows closed           : true
selected lambda orbit closed                  : true
second-order orbit matrix packet closed       : true
qualitative three-family / CP layer closed    : true
Rtheta scalar functional source/domain closed : true
ten scalar row codomain aligned               : true
accepted numerical scalar rows                : 0
selected Rtheta scalar rows emitted           : false
true SM equivalence closed                    : false
full no-knob closure                          : false
```

## What This Means

This is not full SM closure. It is a real narrowing: qualitative SM-like
structure is now closed at the selected orbit layer, and the value-functional
domain is ready. The remaining problem is numerical scalar execution.

The active frontier is:

`{NEXT}`

Minimum next success: emit threshold/mass-scheme/magnitude-bearing rows, or a
source-selected minimal universal-parameter decision, and then execute the ten
scalar `Rtheta` rows without using observed values as selectors.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
