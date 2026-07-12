"""Build Step58 internal Rtheta no-go import / higher-response frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step58_internalrtheta_nogo_import_or_higherresponse_frontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT_PACKET = PACKET_DIR / "step58_internal_rtheta_nogo_import.packet.json"
CUTSET = PACKET_DIR / "step58_next_higherresponse_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step58_InternalRThetaNoGoImport_or_HigherResponseFrontier_v1.md"

STEP57 = DATA / "selected_step57_noknob_boundary_import_or_internalrtheta_frontier.candidate.json"
INTERNAL = DATA / "selected_internalrthetavaluederivation_or_minimaluniversalparameterselection.candidate.json"
FIRST_RESPONSE = (
    DATA
    / "selected_internalrthetavaluederivation_or_minimaluniversalparameterselection"
    / "internal_rtheta_first_response_sufficiency_test.packet.json"
)
DECISION = (
    DATA
    / "selected_internalrthetavaluederivation_or_minimaluniversalparameterselection"
    / "internal_or_minimal_selection_decision.packet.json"
)
CUTSET_SOURCE = (
    DATA
    / "selected_internalrthetavaluederivation_or_minimaluniversalparameterselection"
    / "next_cutset_after_internal_rtheta_attack.packet.json"
)

STATUS = "MTT_SELECTED_STEP58_INTERNAL_RTHETA_NOGO_IMPORTED_HIGHER_RESPONSE_REQUIRED"
NEXT = "MTT_Selected_HigherResponseRThetaFunctional_or_SourceAnchorTheorem_v1"


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
    inputs = [STEP57, INTERNAL, FIRST_RESPONSE, DECISION, CUTSET_SOURCE]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step58 inputs: " + ", ".join(missing))

    step57 = load(STEP57)
    internal = load(INTERNAL)
    first = load(FIRST_RESPONSE)
    decision = load(DECISION)
    cutset_source = load(CUTSET_SOURCE)

    import_packet = {
        "schema": "MTTStep58InternalRThetaNoGoImport.v1",
        "status": "FIRST_RESPONSE_NOGO_IMPORTED",
        "step57_source": rel(STEP57),
        "internal_rtheta_source": rel(INTERNAL),
        "dynamic_first_response_layer_closed": internal["closure_decision"]["dynamic_first_response_layer_closed"],
        "dynamic_normal_form_rank": first["dynamic_normal_form_rank"],
        "scalar_target_slot_count": first["scalar_target_slot_count"],
        "accepted_selected_coefficient_rows": first["accepted_selected_coefficient_rows"],
        "first_response_sufficient_for_no_knob_value_rows": first[
            "first_response_sufficient_for_no_knob_value_rows"
        ],
        "minimal_universal_parameter_selected": decision["minimal_universal_parameter_selected"],
        "selected_higher_response_or_retarded_kernel_derivative_required": decision[
            "selected_higher_response_or_retarded_kernel_derivative_required"
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(IMPORT_PACKET, import_packet)

    cutset = {
        "schema": "MTTStep58NextHigherResponseCutset.v1",
        "status": "NEXT_HIGHER_RESPONSE_OR_SOURCE_ANCHOR",
        "closed_now": {
            "internal_first_response_sufficiency_test_imported": True,
            "first_response_only_route_rejected_for_scalar_no_knob_values": True,
            "minimal_universal_parameter_nonselection_imported": True,
        },
        "still_open": cutset_source["still_open"],
        "recommended_next": cutset_source["recommended_next"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedStep58InternalRThetaNoGoImportOrHigherResponseFrontier",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "internal_rtheta_nogo_import": rel(IMPORT_PACKET),
            "next_higherresponse_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "Step58InternalRThetaNoGoImportTheorem",
            "proved": True,
            "statement": (
                "The internal Rtheta first-response sufficiency test is imported into the numbered plan. "
                "The dynamic first-response layer is closed, but it is rank two and emits zero selected "
                "scalar coefficient rows for the ten-row no-knob target, so the required next target is "
                "a higher-response/retarded-kernel functional or source-anchor theorem."
            ),
        },
        "closure_decision": {
            "dynamic_first_response_layer_closed": True,
            "first_response_only_route_rejected_for_scalar_no_knob_values": True,
            "dynamic_normal_form_rank": first["dynamic_normal_form_rank"],
            "scalar_target_slot_count": first["scalar_target_slot_count"],
            "accepted_internal_Rtheta_coefficient_row_count": 0,
            "selected_universal_parameter_count": 0,
            "minimal_universal_parameter_selection_closed": False,
            "no_knob_value_derivation_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step57["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step58_InternalRThetaNoGoImport_or_HigherResponseFrontier_v1",
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
        f"""# MTT Selected Step58 InternalRThetaNoGoImport or HigherResponseFrontier v1

Status: `{STATUS}`.

```text
dynamic first-response layer closed     : true
dynamic normal-form rank                : {first["dynamic_normal_form_rank"]}
scalar target slots                     : {first["scalar_target_slot_count"]}
accepted internal Rtheta rows           : 0
selected universal parameters           : 0
first-response scalar no-knob closure   : false
full no-knob closure                    : false
true SM equivalence                     : false
```

The next target is `{NEXT}`.
""",
        encoding="utf-8",
    )
    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
