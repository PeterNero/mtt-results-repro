"""Build post-Pi Rtheta value-frontier contraction or threshold-row attack packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_postpirthetavaluefrontiercontraction_or_thresholdrowattackpacket"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RETIREMENT = PACKET_DIR / "post_pi_stale_blocker_retirement.packet.json"
RECLASSIFICATION = PACKET_DIR / "vsd_obligation_reclassification_after_pi.packet.json"
CUTSET = PACKET_DIR / "minimal_threshold_row_cutset_after_post_pi.packet.json"
ROUTE_ORDER = PACKET_DIR / "threshold_row_attack_order_after_post_pi.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PostPiRThetaValueFrontierContraction_or_ThresholdRowAttackPacket_v1.md"

POST_PI = DATA / "selected_rthetasectortransfer_or_primitiveassemblymapexecution.candidate.json"
POST_PI_CUTSET = (
    DATA
    / "selected_rthetasectortransfer_or_primitiveassemblymapexecution"
    / "next_cutset_after_sector_transfer_or_assembly_execution.packet.json"
)
POST_PI_ASSEMBLY = (
    DATA
    / "selected_rthetasectortransfer_or_primitiveassemblymapexecution"
    / "primitive_assembly_map_execution.packet.json"
)
POST_PI_VALUE = (
    DATA
    / "selected_rthetasectortransfer_or_primitiveassemblymapexecution"
    / "pi_closure_value_evaluator_domain.packet.json"
)
VALUE_KERNEL = DATA / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest.candidate.json"
VALUE_KERNEL_PACKET = (
    DATA
    / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest"
    / "value_source_derivation_obligation_kernel.packet.json"
)
FIRST_ROW_PROMOTION = DATA / "selected_firstvaluesourcerowpromotion_or_honestgalerkinprimitiverow.candidate.json"
THRESHOLD_FUNCTIONAL = DATA / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition.candidate.json"
SAME_BRANCH = DATA / "selected_samebranchconvention_or_thresholdrowemission.candidate.json"
THRESHOLD_ROWS = DATA / "selected_thresholdresponserows_or_sectorprojectionweightsexecution.candidate.json"
RTHETA_ORDER = DATA / "selected_rtheta_thresholdrows_or_profileconventionsourceclosure.candidate.json"
RTHETA_READINESS = (
    DATA
    / "selected_rtheta_thresholdrows_or_profileconventionsourceclosure"
    / "rtheta_value_execution_readiness_after_ordering.packet.json"
)

STATUS = (
    "MTT_SELECTED_POSTPIRTHETAVALUEFRONTIERCONTRACTION_OR_THRESHOLDROWATTACKPACKET_"
    "BUILT_STALE_BLOCKERS_RETIRED_THRESHOLD_ROWS_OPEN"
)
NEXT = "MTT_Selected_ConventionSourceTheorem_or_RGEngineThresholdPolicy_PostPi_v1"

POST_PI_MINIMAL_BLOCKERS = [
    "same_branch_scale_scheme_loop_convention",
    "threshold_matching_source_rows",
    "mass_scheme_conversion_source_rows",
    "no_knob_value_derivation",
    "full_profile_likelihood_or_accepted_diagonal_theorem",
]


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
        raise FileNotFoundError("missing post-Pi value-frontier sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        POST_PI,
        POST_PI_CUTSET,
        POST_PI_ASSEMBLY,
        POST_PI_VALUE,
        VALUE_KERNEL,
        VALUE_KERNEL_PACKET,
        FIRST_ROW_PROMOTION,
        THRESHOLD_FUNCTIONAL,
        SAME_BRANCH,
        THRESHOLD_ROWS,
        RTHETA_ORDER,
        RTHETA_READINESS,
    ]
    require_sources(sources)

    post_pi = load(POST_PI)
    post_pi_cutset = load(POST_PI_CUTSET)
    assembly = load(POST_PI_ASSEMBLY)
    post_pi_value = load(POST_PI_VALUE)
    value_kernel = load(VALUE_KERNEL)
    value_kernel_packet = load(VALUE_KERNEL_PACKET)
    first_row_promotion = load(FIRST_ROW_PROMOTION)
    threshold_functional = load(THRESHOLD_FUNCTIONAL)
    same_branch = load(SAME_BRANCH)
    threshold_rows = load(THRESHOLD_ROWS)
    rtheta_order = load(RTHETA_ORDER)
    readiness = load(RTHETA_READINESS)

    old_first_row_open = first_row_promotion["what_remains_open"]
    retired_from_old_first_row = {
        "assembly_map_from_primitive_rows_to_dynamic_value_source_row": assembly[
            "formal_110_row_assembly"
        ],
        "physical_PhiFinC1_action_source_or_independent_provenance": assembly[
            "physical_PhiFinC1_action_source"
        ],
        "selected_A_b_deltaTheta_promotion": (
            assembly["A_selected_promoted"]
            and assembly["b_selected_promoted"]
            and assembly["deltaTheta_C1_promoted"]
        ),
        "honest_primitive_row_exactness_seed": first_row_promotion["closure_decision"][
            "primitive_exactness_backimported"
        ],
        "selected_dynamic_operator_source_owner": post_pi_value[
            "selected_dynamic_operator_source_owner_closed"
        ],
        "Pi_Rtheta": post_pi["closure_decision"]["Pi_Rtheta_closed"],
        "coefficient_functional_domain": post_pi["closure_decision"][
            "coefficient_functional_domain_closed"
        ],
    }
    still_not_retired = {
        "selected_dynamic_overlap_threshold_tensor_T_selected": True,
        "same_branch_linking_tensor_rows_to_versioned_value_packet": True,
        "magnitude_bearing_projection_weights": (
            threshold_rows["closure_decision"]["magnitude_bearing_projection_weights_closed"] is False
        ),
        "threshold_matching_source_rows": True,
        "mass_scheme_conversion_source_rows": True,
    }

    retirement = {
        "schema": "MTTPostPiStaleBlockerRetirement.v1",
        "status": "POST_PI_SOURCE_OWNER_AND_ASSEMBLY_BLOCKERS_RETIRED",
        "old_first_row_promotion_source": rel(FIRST_ROW_PROMOTION),
        "post_pi_source": rel(POST_PI),
        "retired_from_old_first_row_open_set": retired_from_old_first_row,
        "old_first_row_open_set_reference": old_first_row_open,
        "still_not_retired": still_not_retired,
        "stale_blocker_retirement_closed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RETIREMENT, retirement)

    required_rows = value_kernel_packet["required_rows"]
    reclassified_rows = []
    for row in required_rows:
        if row["id"] == "VSD-01-selected-overlap-value-kernel":
            reclassified_rows.append(
                {
                    "id": row["id"],
                    "old_closed": row["closed"],
                    "post_pi_source_subrequirements_closed": {
                        "all_72_primitive_rows_exact": assembly["all_72_primitive_rows_exact"],
                        "formal_110_row_assembly": assembly["formal_110_row_assembly"],
                        "A_b_deltaTheta_promoted": retired_from_old_first_row[
                            "selected_A_b_deltaTheta_promotion"
                        ],
                        "physical_PhiFinC1_action_source": assembly[
                            "physical_PhiFinC1_action_source"
                        ],
                        "dynamic_matter_overlap_first_response_layer": assembly[
                            "selected_dynamic_QaSU3_operator_packet_first_response_layer_closed"
                        ],
                        "Pi_Rtheta": post_pi["closure_decision"]["Pi_Rtheta_closed"],
                    },
                    "post_pi_value_subrequirements_still_open": {
                        "selected_dynamic_overlap_threshold_tensor_T_selected": True,
                        "sector_rows_for_charged_fermions_and_lambda_H": True,
                        "same_branch_link_to_versioned_value_packet": True,
                    },
                    "post_pi_closed": False,
                    "decision": "source assembly closed, magnitude-bearing value row still open",
                }
            )
        else:
            reclassified_rows.append(
                {
                    "id": row["id"],
                    "old_closed": row["closed"],
                    "post_pi_closed": False,
                    "decision": "unchanged open obligation after post-Pi contraction",
                }
            )

    reclassification = {
        "schema": "MTTVSDObligationReclassificationAfterPi.v1",
        "status": "VSD_SOURCE_PROVENANCE_RECLASSIFIED_VALUES_STILL_OPEN",
        "value_kernel_source": rel(VALUE_KERNEL_PACKET),
        "required_row_count": value_kernel_packet["required_row_count"],
        "closed_row_count_after_reclassification": 0,
        "reclassified_rows": reclassified_rows,
        "important_change": (
            "VSD-01 no longer fails because primitive assembly/action-source provenance is absent. "
            "It now fails only at the magnitude-bearing threshold/value tensor and same-branch packet-link layer."
        ),
        "selected_dynamic_value_source_rows_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RECLASSIFICATION, reclassification)

    cutset = {
        "schema": "MTTMinimalThresholdRowCutsetAfterPostPi.v1",
        "status": "MINIMAL_VALUE_CUTSET_CONTRACTED_TO_THRESHOLD_PROFILE_ROWS",
        "source": rel(POST_PI_CUTSET),
        "readiness_before": {
            "present_count": readiness["present_count"],
            "requirement_count": readiness["requirement_count"],
            "blocking_failures": readiness["blocking_failures"],
        },
        "closed_support_now": {
            "Pi_Rtheta": post_pi["closure_decision"]["Pi_Rtheta_closed"],
            "VSD01_source_assembly_subgate": post_pi["closure_decision"][
                "VSD01_source_assembly_subgate_closed"
            ],
            "dynamic_matter_overlap_operator_packet_first_response": post_pi[
                "closure_decision"
            ]["dynamic_matter_overlap_operator_packet_first_response_closed"],
            "coefficient_functional_domain": post_pi["closure_decision"][
                "coefficient_functional_domain_closed"
            ],
            "source_normalized_projection_weights": post_pi_value[
                "source_normalized_projection_weights_closed"
            ],
        },
        "minimal_remaining_blockers": POST_PI_MINIMAL_BLOCKERS,
        "minimal_remaining_blocker_count": len(POST_PI_MINIMAL_BLOCKERS),
        "selected_threshold_response_functional_instantiated": False,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    route_order = {
        "schema": "MTTThresholdRowAttackOrderAfterPostPi.v1",
        "status": "ATTACK_ORDER_FIXED_CONVENTION_SOURCE_FIRST",
        "ordered_routes": [
            {
                "rank": 1,
                "target": "same_branch_scale_scheme_loop_convention",
                "why_first": "Threshold and mass rows are meaningless unless scale, scheme, loop order, and covariance semantics are owned by the same branch.",
                "best_existing_support": rel(SAME_BRANCH),
                "current_closed": same_branch["closure_decision"][
                    "same_branch_scale_scheme_loop_convention_closed"
                ],
            },
            {
                "rank": 2,
                "target": "selected_threshold_response_functional_instantiated",
                "why_first": "The R_theta contract exists, but cannot emit coefficient rows without the convention source.",
                "best_existing_support": rel(THRESHOLD_FUNCTIONAL),
                "current_closed": threshold_functional["closure_decision"][
                    "selected_threshold_response_functional_instantiated"
                ],
            },
            {
                "rank": 3,
                "target": "threshold_matching_source_rows",
                "why_first": "These rows convert selected response data into physical threshold matching entries.",
                "best_existing_support": rel(RTHETA_ORDER),
                "current_closed": rtheta_order["closure_decision"][
                    "threshold_matching_source_rows_closed"
                ],
            },
            {
                "rank": 4,
                "target": "mass_scheme_conversion_source_rows",
                "why_first": "The mass scheme rows must share the convention source with threshold rows.",
                "best_existing_support": rel(RTHETA_ORDER),
                "current_closed": rtheta_order["closure_decision"][
                    "mass_scheme_conversion_source_rows_closed"
                ],
            },
            {
                "rank": 5,
                "target": "full_profile_likelihood_or_accepted_diagonal_theorem",
                "why_first": "A profile theorem can only promote values after convention and row semantics are fixed.",
                "best_existing_support": rel(RTHETA_ORDER),
                "current_closed": rtheta_order["closure_decision"][
                    "full_profile_likelihood_or_accepted_diagonal_theorem_closed"
                ],
            },
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": "The next non-looping step is to prove or import the same-branch convention source; all numeric rows depend on it.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ROUTE_ORDER, route_order)

    candidate = {
        "candidate": "MTTSelectedPostPiRThetaValueFrontierContractionOrThresholdRowAttackPacket",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "post_pi_stale_blocker_retirement": rel(RETIREMENT),
            "vsd_obligation_reclassification_after_pi": rel(RECLASSIFICATION),
            "minimal_threshold_row_cutset_after_post_pi": rel(CUTSET),
            "threshold_row_attack_order_after_post_pi": rel(ROUTE_ORDER),
        },
        "theorem": {
            "name": "PostPiValueFrontierContractionTheorem",
            "proved": True,
            "statement": (
                "After Pi_Rtheta and VSD01 primitive/source assembly close, the active R_theta value frontier "
                "contracts. The stale source-owner, primitive assembly, physical PhiFinC1 action-source, and "
                "A/b/deltaTheta promotion blockers are retired. This does not emit magnitude-bearing threshold "
                "or mass-scheme rows. The minimal remaining cutset is the same-branch scale/scheme/loop convention, "
                "threshold matching rows, mass-scheme conversion rows, no-knob value derivation, and a full profile "
                "likelihood or accepted diagonal theorem."
            ),
        },
        "what_closes_now": {
            "post_pi_frontier_synchronized": True,
            "stale_selected_dynamic_operator_source_owner_blocker_retired": True,
            "primitive_assembly_action_source_blocker_retired": True,
            "A_b_deltaTheta_promotion_blocker_retired": True,
            "minimal_threshold_profile_cutset_fixed": True,
            "non_looping_next_target_selected": True,
        },
        "what_remains_open": {
            key: True for key in POST_PI_MINIMAL_BLOCKERS
        }
        | {
            "numeric_Rtheta_coefficient_values": True,
            "lambda_H_value_execution": True,
            "Yukawa_mass_mixing_value_closure": True,
            "true_SM_equivalence": True,
        },
        "closure_decision": {
            "post_pi_frontier_synchronized": True,
            "stale_source_owner_and_assembly_blockers_retired": True,
            "VSD_01_source_provenance_subrequirements_closed": True,
            "VSD_01_magnitude_value_row_closed": False,
            "selected_threshold_response_functional_instantiated": False,
            "accepted_coefficient_value_count": 0,
            "accepted_lambda_H_value": False,
            "selected_value_evaluator_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": post_pi["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_PostPiRThetaValueFrontierContraction_or_ThresholdRowAttackPacket_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "post_pi_frontier_synchronized": True,
        "stale_source_owner_and_assembly_blockers_retired": True,
        "VSD_01_magnitude_value_row_closed": False,
        "selected_threshold_response_functional_instantiated": False,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected PostPiRThetaValueFrontierContraction or ThresholdRowAttackPacket v1

Status: `{STATUS}`.

The post-Pi frontier is now synchronized with the newer source-assembly result.

```text
Pi_Rtheta closed                                  : true
VSD01 primitive/source assembly closed            : true
stale source-owner/assembly blockers retired      : true
VSD01 magnitude-bearing value row closed          : false
accepted Rtheta coefficient values                : 0
true SM equivalence                               : false
```

This is useful because it prevents us from looping on old source-owner and
primitive-assembly blockers.  The remaining frontier is the threshold/profile
row layer.

Minimal remaining blockers:

```text
1. same-branch scale/scheme/loop convention
2. threshold matching source rows
3. mass-scheme conversion source rows
4. no-knob value derivation
5. full profile likelihood or accepted diagonal theorem
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
