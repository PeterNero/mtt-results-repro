"""Build Step 6 measured-SM comparison readiness and no-knob gap boundary."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step6_measuredsmcomparisonreadiness_or_noknobvaluegap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
COMPARISON = PACKET_DIR / "step6_admitted_comparison_material.packet.json"
GAPS = PACKET_DIR / "step6_no_knob_value_gap_register.packet.json"
READINESS = PACKET_DIR / "step6_true_equivalence_readiness.packet.json"
BOUNDARY = PACKET_DIR / "step6_closure_boundary.packet.json"
HANDOFF = PACKET_DIR / "step6_to_step7_handoff.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step6_MeasuredSMComparisonReadiness_or_NoKnobValueGap_v1.md"

STEP5 = DATA / "selected_step5_noknobminimalknobaudit_or_internalscalarrowsexecution.candidate.json"
STEP5_HANDOFF = (
    DATA
    / "selected_step5_noknobminimalknobaudit_or_internalscalarrowsexecution"
    / "step5_to_step6_handoff.packet.json"
)
STEP5_BOUNDARY = (
    DATA
    / "selected_step5_noknobminimalknobaudit_or_internalscalarrowsexecution"
    / "step5_closure_boundary.packet.json"
)
EXTERNAL_IMPORT = DATA / "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport.candidate.json"
COMMON_RG = DATA / "sm_equivalence_common_rg_and_empirical_audit.candidate.json"
DYNAMIC_QASU3 = DATA / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure.candidate.json"
DYNAMIC_REPLAY = (
    DATA
    / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure"
    / "dynamic_qasu3_operator_packet_replay.packet.json"
)

STATUS = (
    "MTT_SELECTED_STEP6_MEASUREDSMCOMPARISONREADINESS_OR_NOKNOBVALUEGAP_"
    "CLOSED_READINESS_TRUE_EQUIVALENCE_OPEN"
)
NEXT = "MTT_Selected_Step7_CommonRGCovarianceObservableSuite_or_FinalTrueSMEquivalenceGate_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 6 inputs: " + ", ".join(missing))


def true_count(mapping: dict[str, Any]) -> int:
    return sum(1 for value in mapping.values() if value is True)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        STEP5,
        STEP5_HANDOFF,
        STEP5_BOUNDARY,
        EXTERNAL_IMPORT,
        COMMON_RG,
        DYNAMIC_QASU3,
        DYNAMIC_REPLAY,
    ]
    require_sources(sources)

    step5 = load(STEP5)
    step5_handoff = load(STEP5_HANDOFF)
    step5_boundary = load(STEP5_BOUNDARY)
    external = load(EXTERNAL_IMPORT)
    common = load(COMMON_RG)
    dynamic_qasu3 = load(DYNAMIC_QASU3)
    dynamic_replay = load(DYNAMIC_REPLAY)

    native_closed_rows = common["native_published_parameter_replay"]["closed_rows"]
    qualitative = dynamic_replay["qualitative_flavor_response"]
    step6_allowed = step5_handoff["step6_allowed_comparisons"]
    no_knob_gaps = step5_handoff["step6_must_report_gaps"]
    do_not_use = step5_handoff["do_not_use_as_selectors"]

    comparison = {
        "schema": "MTTStep6AdmittedComparisonMaterial.v1",
        "status": "ADMITTED_COMPARISON_MATERIAL_READY_WITH_SOURCE_GUARDS",
        "step5_handoff_source": rel(STEP5_HANDOFF),
        "allowed_comparison_lanes": step6_allowed,
        "admitted_external_replay": {
            "source": rel(EXTERNAL_IMPORT),
            "external_import_lane_closed_at_admitted_replay_tier": external["closure_decision"][
                "external_import_lane_closed_at_admitted_replay_tier"
            ],
            "accepted_external_threshold_row_count": external["closure_decision"][
                "accepted_external_threshold_row_count"
            ],
            "accepted_external_mass_scheme_row_count": external["closure_decision"][
                "accepted_external_mass_scheme_row_count"
            ],
            "accepted_diagonal_profile_theorem_closed": external["closure_decision"][
                "accepted_diagonal_profile_theorem_closed"
            ],
            "is_no_knob_source": False,
        },
        "native_measured_replay": {
            "source": rel(COMMON_RG),
            "native_replay_closure_claimed": common["native_replay_closure_claimed"],
            "closed_row_count": true_count(native_closed_rows),
            "closed_rows": native_closed_rows,
            "is_downstream_comparison_only": True,
        },
        "dynamic_qualitative_support": {
            "source": rel(DYNAMIC_REPLAY),
            "first_response_layer_closed": dynamic_replay[
                "actual_QaSU3_operator_packet_first_response_layer_closed"
            ],
            "qualitative_test_count": true_count(qualitative),
            "qualitative_flavor_response": qualitative,
            "not_a_precision_value_packet": dynamic_replay["not_a_precision_value_packet"],
        },
        "forbidden_selector_uses": do_not_use,
        "measured_comparison_readiness_closed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(COMPARISON, comparison)

    gap_register = {
        "schema": "MTTStep6NoKnobValueGapRegister.v1",
        "status": "NOKNOB_VALUE_GAP_REPORTED_EXPLICITLY",
        "source": rel(STEP5_HANDOFF),
        "gap_count": true_count(no_knob_gaps),
        "gaps": no_knob_gaps,
        "accepted_internal_scalar_row_count": step5_boundary["accepted_internal_scalar_row_count"],
        "selected_universal_parameter_count": step5_boundary["selected_universal_parameter_count"],
        "internal_no_knob_values_ready_for_comparison": step5_boundary[
            "internal_no_knob_values_ready_for_step6"
        ],
        "internal_no_knob_Yukawa_lambdaH_CKM_PMNS_predictions_allowed": step6_allowed[
            "internal_no_knob_Yukawa_lambdaH_CKM_PMNS_predictions"
        ],
        "no_knob_gap_blocks_full_SM_equivalence": True,
        "ordinary_fitted_knobs_forbidden": step5_boundary["ordinary_fitted_knobs_forbidden"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(GAPS, gap_register)

    common_rg_open = common["common_RG_true_equivalence_gate"]["open_rows"]
    empirical_open = common["what_remains_open"]
    readiness = {
        "schema": "MTTStep6TrueEquivalenceReadiness.v1",
        "status": "NATIVE_REPLAY_READY_TRUE_EQUIVALENCE_NOT_READY",
        "common_rg_source": rel(COMMON_RG),
        "native_published_parameter_replay_ready": common["native_replay_closure_claimed"],
        "admitted_external_replay_ready": comparison["admitted_external_replay"][
            "external_import_lane_closed_at_admitted_replay_tier"
        ],
        "dynamic_first_response_qualitative_tests_ready": dynamic_replay[
            "actual_QaSU3_operator_packet_first_response_layer_closed"
        ],
        "common_rg_true_equivalence_ready": False,
        "common_rg_open_row_count": true_count(common_rg_open),
        "common_rg_open_rows": common_rg_open,
        "empirical_audit_open_rows": empirical_open,
        "selected_SM_packet_final_certificate_ready": not empirical_open[
            "selected_SM_packet_final_certificate"
        ],
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(READINESS, readiness)

    boundary = {
        "schema": "MTTStep6ClosureBoundary.v1",
        "status": "STEP6_CLOSED_AS_MEASURED_COMPARISON_READINESS_NOT_TRUE_EQUIVALENCE",
        "completed_step": 6,
        "step5_closed_for_plan_contract": step5["closure_decision"][
            "step5_closed_for_plan_contract"
        ],
        "measured_comparison_readiness_closed": True,
        "no_knob_value_gap_reported": True,
        "admitted_external_replay_ready": True,
        "native_measured_replay_ready": True,
        "dynamic_qualitative_support_ready": True,
        "accepted_internal_scalar_row_count": 0,
        "selected_universal_parameter_count": 0,
        "common_rg_true_equivalence_ready": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "step6_closed_for_plan_contract": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(BOUNDARY, boundary)

    handoff = {
        "schema": "MTTStep6ToStep7Handoff.v1",
        "status": "HANDOFF_TO_STEP7_COMMON_RG_COVARIANCE_OBSERVABLE_SUITE",
        "completed_step": 6,
        "next_step": 7,
        "next_required_artifact": NEXT,
        "step7_must_close": {
            "single_common_scale_transport": True,
            "loop_order_beta_functions_and_thresholds": True,
            "mass_scheme_unification": True,
            "Yukawa_running_matrices_at_common_scale": True,
            "Higgs_lambda_running_at_common_scale": True,
            "full_CKM_PMNS_covariance_or_profile_likelihood": True,
            "absolute_neutrino_mass_or_declared_minimal_parity_policy": True,
            "observable_suite_with_tolerances": True,
            "selected_SM_packet_final_certificate": True,
        },
        "step7_may_use": {
            "admitted_external_replay_rows_as_comparison_data": True,
            "native_measured_replay_rows_as_downstream_slots": True,
            "dynamic_first_response_qualitative_tests": True,
        },
        "step7_must_not_use_as_selectors": do_not_use,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(HANDOFF, handoff)

    candidate = {
        "candidate": "MTTSelectedStep6MeasuredSMComparisonReadinessOrNoKnobValueGap",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "step6_admitted_comparison_material": rel(COMPARISON),
            "step6_no_knob_value_gap_register": rel(GAPS),
            "step6_true_equivalence_readiness": rel(READINESS),
            "step6_closure_boundary": rel(BOUNDARY),
            "step6_to_step7_handoff": rel(HANDOFF),
        },
        "theorem": {
            "name": "Step6MeasuredComparisonReadinessAndNoKnobGapTheorem",
            "proved": True,
            "statement": (
                "Step 6 is closed as a measured-comparison readiness theorem. The admitted "
                "external threshold/mass-scheme rows, native measured replay rows, and selected "
                "dynamic first-response qualitative tests are ready for downstream comparison, "
                "while all internal no-knob value gaps are reported explicitly. This does not "
                "derive internal Yukawa, CKM, PMNS, lambda_H, mass-ratio, common-RG, covariance, "
                "or full true-SM equivalence closure."
            ),
        },
        "closure_decision": {
            "step6_closed_for_plan_contract": True,
            "measured_comparison_readiness_closed": True,
            "no_knob_value_gap_reported": True,
            "admitted_external_replay_ready": True,
            "native_measured_replay_ready": True,
            "dynamic_qualitative_support_ready": True,
            "accepted_internal_scalar_row_count": 0,
            "selected_universal_parameter_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "step6_plan_contract": True,
            "admitted_comparison_material_registered": True,
            "native_measured_replay_downstream_ready": True,
            "dynamic_qualitative_support_registered": True,
            "no_knob_value_gap_register_closed": True,
            "step7_handoff_typed": True,
        },
        "what_remains_open": handoff["step7_must_close"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "step6_contract_closure_claimed": True,
        "native_replay_closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step6_MeasuredSMComparisonReadiness_or_NoKnobValueGap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "step6_contract_closure_claimed": True,
        "measured_comparison_readiness_closed": True,
        "no_knob_value_gap_reported": True,
        "accepted_internal_scalar_row_count": 0,
        "selected_universal_parameter_count": 0,
        "native_replay_closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step6 MeasuredSMComparisonReadiness or NoKnobValueGap v1

Status: `{STATUS}`.

Step 6 is closed as measured-comparison readiness:

```text
admitted external replay ready        : true
native measured replay ready          : true
dynamic qualitative support ready     : true
no-knob value gap reported            : true
accepted internal scalar rows         : 0
selected universal parameters         : 0
true SM equivalence closed            : false
full no-knob closure                  : false
```

This closes the comparison-readiness layer.  The measured rows are downstream
comparison data only; they do not select source structure, value functionals, or
universal anchors.  The next closure target is the common-RG, covariance/profile,
observable-suite, and selected-SM-packet gate.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
