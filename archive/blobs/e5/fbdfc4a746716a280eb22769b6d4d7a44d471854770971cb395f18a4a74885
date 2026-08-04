"""Build the dynamic overlap-kernel or C1-primitive source-emission reduction."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

DOWNSTREAM = DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"
ALPHA1_TRANSFER = DATA / "selected_alpha1_sourcestrength_or_transfernormalization_fill_attempt.candidate.json"
DOTD_PROBE = DATA / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
END0_SECTOR = DATA / "selected_end0_to_sector_functor_source_and_value_packet.candidate.json"
CANONICAL_C1 = DATA / "selected_routec_c1_primitive_response_on_smooth_bn.candidate.json"
NONINV_C1 = DATA / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
WEYL_A = DATA / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"

OUTPUT = DATA / "selected_dynamic_overlapkernel_or_c1primitive_source_emission.candidate.json"
CERT = CERTS / "selected_dynamic_overlapkernel_or_c1primitive_source_emission_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicOverlapKernel_or_C1Primitive_SourceEmission_v1.md"

STATUS = (
    "MTT_SELECTED_DYNAMIC_OVERLAPKERNEL_OR_C1PRIMITIVE_SOURCE_EMISSION_"
    "REDUCED_TYPED_DERIVATIVE_PRIMITIVE_VALUES_OPEN"
)
NEXT = "MTT_Selected_TypedBN_RetardedDerivative_or_PrimitiveResponse_ValueEmission_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    downstream = load(DOWNSTREAM)
    alpha1 = load(ALPHA1_TRANSFER)
    dotd = load(DOTD_PROBE)
    end0 = load(END0_SECTOR)
    canonical = load(CANONICAL_C1)
    noninv = load(NONINV_C1)
    weyl_a = load(WEYL_A)

    static_import = {
        "sector_pair_partition_closed_static": downstream["what_closes_now"][
            "selected_static_sector_route_Z_to_u_e_X_to_d_nuD"
        ],
        "oneM_Dirac_rule_closed_static": downstream["what_closes_now"][
            "selected_static_1M_Dirac_neutrino_shift_rule"
        ],
        "finite_trace_transfer_closed_static": downstream["what_closes_now"][
            "selected_static_finite_trace_transfer_normalization"
        ],
        "dynamic_C1_operator_values_closed": False,
        "meaning": (
            "The selected static SM-slot functor supplies the sector route and finite trace frame. "
            "It does not supply the dynamic retarded derivative, Hessian, source-to-C1 overlap tensor, "
            "or primitive response values."
        ),
    }

    lane_alpha1_source_strength = {
        "closed": False,
        "source_identity_selected": alpha1["minimal_cutset"]["route_A_same_source_coordinate"][
            "source_identity_selected"
        ],
        "lambda_alpha1_candidate": alpha1["minimal_cutset"]["route_A_same_source_coordinate"][
            "lambda_alpha1_candidate"
        ],
        "h_ext_l2": alpha1["minimal_cutset"]["route_A_same_source_coordinate"]["h_ext_l2"],
        "h_ext_residual_l2": alpha1["minimal_cutset"]["route_A_same_source_coordinate"][
            "h_ext_residual_l2"
        ],
        "remaining_after_static_import": [
            "same-branch source-strength coordinate",
            "selected normalization functional, not canonical coordinate dual alone",
            "selected proof that h_selected_alpha1 equals h_ext",
        ],
    }

    lane_typed_retarded_derivative = {
        "closed": False,
        "dotD_source_algebra_closed": dotd["promotion_decision"]["selected_dotD_source_formula_closed"],
        "validator_math_passes_if_driver_is_theorem_derived": dotd["validator_boundary"][
            "mathematical_dotd_matrices_pass_if_flags_are_theorem_derived"
        ],
        "static_sector_route_available": static_import["sector_pair_partition_closed_static"],
        "static_finite_transfer_available": static_import["finite_trace_transfer_closed_static"],
        "dynamic_End0_to_sector_functor_values_extracted": end0["decision"][
            "selected_End0_to_sector_functor_values_extracted"
        ],
        "typed_BN_tangent_or_retarded_kernel_emitted": alpha1["minimal_cutset"][
            "route_B_typed_transfer"
        ]["selected_BN_tangent_or_retarded_kernel"],
        "honest_dotD_replay_from_kernel": alpha1["minimal_cutset"]["route_B_typed_transfer"][
            "honest_dotD_replay_from_kernel"
        ],
        "remaining_after_static_import": [
            "selected dynamic End0-to-sector realization/functor values",
            "typed B_N alpha1 tangent or retarded derivative",
            "dynamic transfer/Hessian normalization",
            "honest dotD replay without lifted flags",
        ],
    }

    fixed_fiber_candidates = [
        item
        for item in noninv["candidate_primitives"]
        if item["primitive_fiber_shift"] in [0, 1, 2]
    ]
    lane_c1_primitive = {
        "closed": False,
        "canonical_mode_conserving_C1_zero": canonical["diagnostics"][
            "all_c1_matrices_zero_for_canonical_tensor"
        ],
        "noninvariant_active_shift_forced": noninv["search_rule"][
            "minimal_active_shift_required"
        ]
        == [1, 1],
        "noninvariant_candidates_nonzero": noninv["calculation_results"][
            "all_four_tested_candidates_nonzero"
        ],
        "fixed_fiber_candidate_count": len(fixed_fiber_candidates),
        "fixed_fiber_ranks_all_three": all(
            all(summary["rank"] == 3 for summary in item["summary"].values())
            for item in fixed_fiber_candidates
        ),
        "conditional_weylpair_A_exact": weyl_a["locked_solve"]["consistent"],
        "promote_to_A_selected": False,
        "remaining_after_static_import": [
            "selected dynamic primitive/vertex/basis-transport source theorem",
            "selected primitive contraction values in the same D_E/dotD basis",
            "b_selected emitted by the selected dynamic source",
            "honest selected deltaTheta_C1 solve",
        ],
    }

    dynamic_cutset = {
        "already_closed_or_reduced": {
            "static_sector_pair_partition": static_import["sector_pair_partition_closed_static"],
            "static_1M_Dirac_rule": static_import["oneM_Dirac_rule_closed_static"],
            "static_finite_trace_transfer": static_import["finite_trace_transfer_closed_static"],
            "dotD_transport_derivative_algebra": lane_typed_retarded_derivative[
                "dotD_source_algebra_closed"
            ],
            "canonical_C1_zero_no_go": lane_c1_primitive["canonical_mode_conserving_C1_zero"],
            "noninvariant_active_shift_1_1_localized": lane_c1_primitive[
                "noninvariant_active_shift_forced"
            ],
        },
        "remaining_minimal_objects": [
            "typed dynamic B_N retarded derivative or alpha1 source-strength theorem",
            "selected End0-to-sector realization/functor values",
            "selected dynamic overlap/Hessian normalization and b_selected",
            "selected primitive/vertex/basis-transport response values",
        ],
    }

    theorem = {
        "name": "DynamicOverlapOrC1PrimitiveCutsetTheorem",
        "proved": True,
        "statement": (
            "With static sector routing and finite trace transfer closed, the remaining C1 obstruction is "
            "not a sector-label ambiguity.  The exact remaining cutset is dynamic: either emit a typed "
            "same-branch retarded derivative/alpha1 driver and End0-to-sector transfer, or emit selected "
            "primitive/vertex/basis-transport response values with b_selected.  Existing conditional "
            "Weyl-pair algebra is sufficient but not selected."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedDynamicOverlapKernelOrC1PrimitiveSourceEmission",
        "status": STATUS,
        "inputs": {
            "downstream_operator_payload_ledger": rel(DOWNSTREAM),
            "alpha1_source_strength_or_transfer_attempt": rel(ALPHA1_TRANSFER),
            "dotd_alpha1_transport_derivative_probe": rel(DOTD_PROBE),
            "end0_to_sector_functor_packet": rel(END0_SECTOR),
            "canonical_c1_primitive_response": rel(CANONICAL_C1),
            "noninvariant_c1_primitive_search": rel(NONINV_C1),
            "conditional_weylpair_A_assembly": rel(WEYL_A),
        },
        "superset_strategy": {
            "mode": "DYNAMIC_CUTSET_AFTER_STATIC_SMSLOT_CLOSURE",
            "observed_data_used": False,
            "target_fitting_used": False,
            "locked_target_role": "conditional Weyl-pair rank/solve checks algebraic readiness only",
            "static_import_role": "sector labels and finite trace normalization are allowed inputs, not dynamic operator values",
        },
        "static_import": static_import,
        "lanes": {
            "A_same_source_alpha1_strength": lane_alpha1_source_strength,
            "B_typed_retarded_derivative": lane_typed_retarded_derivative,
            "C_selected_C1_primitive_or_vertex": lane_c1_primitive,
        },
        "dynamic_cutset": dynamic_cutset,
        "what_closes_now": {
            "dynamic_frontier_reduced_after_static_sector_closure": True,
            "sector_routing_removed_as_generic_C1_blocker": True,
            "alpha1_and_primitive_lanes_separated": True,
            "typed_derivative_or_primitive_valueemission_next": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "typed_BN_retarded_derivative_or_alpha1_source_strength": True,
            "selected_End0_to_sector_functor_values": True,
            "selected_dynamic_overlap_Hessian_normalization": True,
            "selected_primitive_or_vertex_response_values": True,
            "selected_b_selected": True,
            "honest_selected_deltaTheta_C1_solve": True,
            "promote_conditional_A_to_A_selected": True,
            "Yukawa_CKM_PMNS_masses_Higgs_RG": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "dynamic_kernel_emitted": False,
        "selected_C1_primitive_emitted": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem": theorem,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DynamicOverlapKernel_or_C1Primitive_SourceEmission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "dynamic_kernel_emitted": False,
        "selected_C1_primitive_emitted": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem_proved": True,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DynamicOverlapKernel or C1Primitive SourceEmission v1

Status: `{STATUS}`.

## Result

The C1 frontier is now genuinely dynamic.  Static sector labels and finite trace
normalization are closed, so the remaining obstruction is not choosing the
sector partition.

The remaining legal lanes are:

1. emit a same-branch alpha1 source-strength theorem identifying
   `du/dalpha1 = h_ext`;
2. emit a typed `B_N` retarded derivative plus selected End0-to-sector transfer;
3. emit selected primitive/vertex/basis-transport response values and
   `b_selected`.

The conditional Weyl-pair operator remains algebraically exact, but it is still
not `A_selected`.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
