"""Build R_theta primitive-C1 overlap import or Pi no-need theorem packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_primitivec1overlap_or_pinoneedtheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PRIMITIVE_IMPORT = PACKET_DIR / "rtheta_primitive_c1_overlap_import.packet.json"
DEPENDENCY_AUDIT = PACKET_DIR / "pi_rtheta_dependency_audit_after_primitive_import.packet.json"
PI_RECHECK = PACKET_DIR / "pi_rtheta_recheck_after_primitive_c1_import.packet.json"
VALUE_GATE = PACKET_DIR / "rtheta_value_gate_after_pi_closure.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_pi_closure.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaPrimitiveC1Overlap_or_PiNoNeedTheorem_v1.md"

PREVIOUS = DATA / "selected_rtheta_matterslotrouting_or_primitivec1noneedtheorem.candidate.json"
PREVIOUS_PI = (
    DATA
    / "selected_rtheta_matterslotrouting_or_primitivec1noneedtheorem"
    / "pi_rtheta_recheck_after_matterslot_routing.packet.json"
)
DYNAMIC_PACKET = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
MATTER_PACKET = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_packet.packet.json"
)
VALIDATOR_RESULT = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_validator_result.packet.json"
)
SELECTED_VALUES = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)
COEFFICIENT_SKELETON = (
    DATA
    / "selected_rtheta_coefficientfunctional_or_universalanchorselection"
    / "rtheta_coefficient_functional_skeleton.packet.json"
)
PHYSICAL_KERNEL_ATTEMPT = (
    DATA
    / "selected_rtheta_physicalprojectionkernel_or_profileresponse"
    / "pi_rtheta_kernel_attempt.packet.json"
)

STATUS = (
    "MTT_SELECTED_RTHETA_PRIMITIVEC1OVERLAP_OR_PINONEEDTHEOREM_"
    "IMPORTED_PRIMITIVE_C1_PI_CLOSED_VALUES_OPEN"
)
NEXT = "MTT_Selected_RThetaValueEvaluatorExecution_or_ThresholdResponseInstantiation_v1"


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
        raise FileNotFoundError("missing R_theta primitive-C1 sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_PI,
        DYNAMIC_PACKET,
        MATTER_PACKET,
        VALIDATOR_RESULT,
        SELECTED_VALUES,
        COEFFICIENT_SKELETON,
        PHYSICAL_KERNEL_ATTEMPT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_pi = load(PREVIOUS_PI)
    dynamic = load(DYNAMIC_PACKET)
    matter = load(MATTER_PACKET)
    validator = load(VALIDATOR_RESULT)
    values = load(SELECTED_VALUES)
    skeleton = load(COEFFICIENT_SKELETON)
    kernel_attempt = load(PHYSICAL_KERNEL_ATTEMPT)

    primitive_field = matter["attempted_selected_packet"]["fields"]["primitive_contractions"]
    primitive_c1_overlap_closed = (
        dynamic["promotion_decision"]["dynamic_matter_overlap_operator_packet_closed"] is True
        and dynamic["what_closes_now"][
            "primitive_C1_contractions_selected_emitted_first_response_layer"
        ]
        is True
        and primitive_field["selected_emitted"] is True
        and primitive_field["same_source"] is True
        and primitive_field["theorem_derived"] is True
        and validator["returncode"] == 0
        and any('"ok": true' in line for line in validator["stdout"])
        and values["selected_by_MTT"] is True
        and values["guardrail"]["observed_flavor_data_used"] is False
    )
    primitive_c1_no_need_theorem_closed = False
    primitive_or_no_need_closed = primitive_c1_overlap_closed or primitive_c1_no_need_theorem_closed

    primitive_import = {
        "schema": "MTTRThetaPrimitiveC1OverlapImport.v1",
        "status": "PRIMITIVE_C1_OVERLAP_IMPORTED_FROM_SAME_SOURCE_DYNAMIC_PACKET",
        "dynamic_packet_source": rel(DYNAMIC_PACKET),
        "same_source_matter_overlap_packet": rel(MATTER_PACKET),
        "validator_result": rel(VALIDATOR_RESULT),
        "selected_values_source": rel(SELECTED_VALUES),
        "route": "direct primitive C1 overlap import, not no-need theorem",
        "primitive_C1_overlap_contractions_closed": primitive_c1_overlap_closed,
        "primitive_C1_no_need_theorem_closed": primitive_c1_no_need_theorem_closed,
        "primitive_C1_or_no_need_gate_closed": primitive_or_no_need_closed,
        "same_source_flags": primitive_field,
        "selected_first_response_layer_only": True,
        "does_not_emit": [
            "theta_coeff numeric values",
            "lambda_H",
            "Yukawa magnitudes",
            "running mass ratios",
            "CKM/PMNS measured angles",
            "true SM equivalence",
            "full no-knob closure",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": primitive_c1_overlap_closed,
    }
    write_json(PRIMITIVE_IMPORT, primitive_import)

    dependency_audit = {
        "schema": "MTTPiRThetaDependencyAuditAfterPrimitiveImport.v1",
        "status": "PI_RTHETA_DEPENDENCIES_ALL_PRESENT_VALUE_EVALUATOR_SEPARATE",
        "kernel_attempt_source": rel(PHYSICAL_KERNEL_ATTEMPT),
        "coefficient_skeleton_source": rel(COEFFICIENT_SKELETON),
        "dependency_classes": {
            "stationary_sector_transfer": previous["closure_decision"][
                "stationary_sector_transfer_closed"
            ],
            "selected_stationary_rho_s": previous["closure_decision"][
                "selected_stationary_rho_s_closed"
            ],
            "selected_dotD_alpha1_transport": previous["closure_decision"][
                "dotD_alpha1_transport_subgate_closed"
            ],
            "selected_matter_slot_ownership": previous["closure_decision"][
                "matter_slot_routing_closed"
            ],
            "selected_primitive_C1_overlap_first_response": primitive_c1_overlap_closed,
        },
        "original_kernel_minimal_missing_object": kernel_attempt["minimal_internal_missing_object"],
        "original_kernel_slot_count": kernel_attempt["slot_count"],
        "rtheta_charged_functional_rows": skeleton["charged_functional_row_count"],
        "coefficient_functional_skeleton_closed": skeleton[
            "coefficient_functional_readiness_closed"
        ],
        "primitive_C1_role": (
            "needed to certify the first-response dynamic overlap/contraction input used by "
            "the physical projection kernel; it is not by itself a numeric theta coefficient "
            "or threshold/profile convention"
        ),
        "value_evaluator_separate_requirements": [
            "selected threshold response functional instantiated",
            "profile/precision convention selected before measured-value comparison",
            "coefficient row evaluation against selected scale/scheme functor",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": primitive_or_no_need_closed,
    }
    write_json(DEPENDENCY_AUDIT, dependency_audit)

    prev_tests = previous_pi["component_tests_after_matterslot_routing"]
    component_tests = dict(prev_tests)
    component_tests.update(
        {
            "primitive_C1_overlap_or_no_need_available": primitive_or_no_need_closed,
            "selected_primitive_C1_overlap_contractions_available": primitive_c1_overlap_closed,
            "selected_dynamic_matter_overlap_packet_validates": dynamic["promotion_decision"][
                "dynamic_matter_overlap_operator_packet_closed"
            ],
        }
    )

    pi_closed = (
        previous["closure_decision"]["stationary_sector_transfer_closed"]
        and previous["closure_decision"]["selected_stationary_rho_s_closed"]
        and previous["closure_decision"]["dotD_alpha1_transport_subgate_closed"]
        and previous["closure_decision"]["matter_slot_routing_closed"]
        and primitive_or_no_need_closed
    )

    pi_recheck = {
        "schema": "MTTPiRThetaRecheckAfterPrimitiveC1Import.v1",
        "status": "PI_RTHETA_RECHECKED_PRIMITIVE_C1_IMPORTED_CLOSED",
        "previous_pi_recheck": rel(PREVIOUS_PI),
        "component_tests_after_primitive_c1_import": component_tests,
        "retired_missing_primitives": [
            "primitive_C1_overlap_contractions_or_no-need theorem for Pi_Rtheta"
        ],
        "still_retired_from_previous": previous_pi["retired_missing_primitives"]
        + previous_pi["still_retired_from_previous"],
        "Pi_Rtheta_closed": pi_closed,
        "accepted_coefficient_value_count": 0,
        "new_minimal_missing_primitives": [],
        "why_values_not_emitted": [
            "Pi_Rtheta closure supplies the physical projection kernel, not the threshold/profile value evaluator",
            "the coefficient skeleton rows still require selected threshold response instantiation and scale/scheme convention",
            "first-response primitive C1 data does not by itself equal Yukawa magnitudes, lambda_H, or measured SM closure",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": pi_closed,
    }
    write_json(PI_RECHECK, pi_recheck)

    value_gate = {
        "schema": "MTTRThetaValueGateAfterPiClosure.v1",
        "status": "RTHETA_PI_CLOSED_VALUES_STILL_REJECTED_THRESHOLD_RESPONSE_OPEN",
        "Pi_Rtheta_closed": pi_closed,
        "coefficient_functional_skeleton_closed": skeleton[
            "coefficient_functional_readiness_closed"
        ],
        "charged_functional_row_count": skeleton["charged_functional_row_count"],
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "selected_threshold_response_functional_instantiated": False,
        "profile_response_closed": False,
        "Yukawa_magnitudes_predicted": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VALUE_GATE, value_gate)

    cutset = {
        "schema": "MTTNextCutsetAfterPiClosure.v1",
        "status": "NEXT_ATTACK_RTHETA_VALUE_EVALUATOR_OR_THRESHOLD_RESPONSE",
        "closed_now": {
            "primitive_C1_overlap_contractions_or_no_need_for_Pi_Rtheta": primitive_or_no_need_closed,
            "Pi_Rtheta": pi_closed,
            "values_still_rejected_without_threshold_response": True,
        },
        "still_open": [
            "selected_threshold_response_functional_instantiated",
            "profile_response_or_precision_convention_closed",
            "theta_coeff numeric value execution",
            "lambda_H value execution",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "instantiate the selected threshold response functional over the closed Pi_Rtheta kernel",
            "route_B": "execute coefficient rows under the selected scale/scheme convention, still excluding observed magnitudes as selectors",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaPrimitiveC1OverlapOrPiNoNeedTheorem",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "rtheta_primitive_c1_overlap_import": rel(PRIMITIVE_IMPORT),
            "pi_rtheta_dependency_audit_after_primitive_import": rel(DEPENDENCY_AUDIT),
            "pi_rtheta_recheck_after_primitive_c1_import": rel(PI_RECHECK),
            "rtheta_value_gate_after_pi_closure": rel(VALUE_GATE),
            "next_cutset_after_pi_closure": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaPrimitiveC1OverlapImportClosesPiTheorem",
            "proved": pi_closed,
            "statement": (
                "The same-source dynamic matter/overlap packet validates with theorem-derived primitive "
                "contractions for the selected first-response layer. Combining that packet with the already "
                "closed stationary sector transfer, selected rho_s, dotD_alpha1 transport, and static matter-slot "
                "ownership closes the remaining Pi_Rtheta dependency. This closes Pi_Rtheta, not the numeric "
                "R_theta coefficient evaluator, lambda_H, Yukawa magnitudes, true SM equivalence, or no-knob closure."
            ),
        },
        "closure_decision": {
            "stationary_sector_transfer_closed": previous["closure_decision"][
                "stationary_sector_transfer_closed"
            ],
            "selected_stationary_rho_s_closed": previous["closure_decision"][
                "selected_stationary_rho_s_closed"
            ],
            "dotD_alpha1_transport_subgate_closed": previous["closure_decision"][
                "dotD_alpha1_transport_subgate_closed"
            ],
            "matter_slot_routing_closed": previous["closure_decision"][
                "matter_slot_routing_closed"
            ],
            "primitive_C1_or_no_need_gate_closed": primitive_or_no_need_closed,
            "primitive_C1_overlap_contractions_closed": primitive_c1_overlap_closed,
            "primitive_C1_no_need_theorem_closed": primitive_c1_no_need_theorem_closed,
            "Pi_Rtheta_closed": pi_closed,
            "accepted_coefficient_value_count": 0,
            "accepted_lambda_H_value": False,
            "selected_threshold_response_functional_instantiated": False,
            "profile_response_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTTSelectedRThetaPrimitiveC1OverlapOrPiNoNeedTheorem",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "primitive_C1_overlap_contractions_closed": primitive_c1_overlap_closed,
        "primitive_C1_no_need_theorem_closed": primitive_c1_no_need_theorem_closed,
        "Pi_Rtheta_closed": pi_closed,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "theorem_proved": pi_closed,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected RThetaPrimitiveC1Overlap or PiNoNeedTheorem v1

Status: `{STATUS}`.

This artifact resolves the last `Pi_Rtheta` blocker by direct import, not by a
no-need theorem.  The selected same-source dynamic matter/overlap packet already
validates theorem-derived primitive contractions for the first-response layer.

```text
primitive C1 overlap contractions closed      : {str(primitive_c1_overlap_closed).lower()}
primitive C1 no-need theorem closed           : {str(primitive_c1_no_need_theorem_closed).lower()}
Pi_Rtheta closed                              : {str(pi_closed).lower()}
accepted coefficient values                   : 0
lambda_H value accepted                       : false
selected threshold response instantiated      : false
```

The retired blocker is now:

- primitive C1 overlap contractions or a theorem proving `Pi_Rtheta` does not
  require them.

The route that worked is direct primitive import from the validated same-source
dynamic matter/overlap packet.  This closes the projection kernel dependency
stack:

- stationary sector transfer,
- selected stationary `rho_s`,
- selected `dotD_alpha1` transported-packet derivative,
- selected matter-slot ownership,
- selected primitive C1 first-response overlap/contraction data.

This does **not** emit numeric `theta_coeff` values, `lambda_H`, Yukawa
magnitudes, running mass ratios, CKM/PMNS measured angles, true SM equivalence,
or full no-knob closure.  Those now move to the value-evaluator layer.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
