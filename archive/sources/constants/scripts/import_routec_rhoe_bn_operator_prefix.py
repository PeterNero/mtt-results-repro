"""Import the Route-C rho_E/B_N/operator prefix and C1 zero-response frontier."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CERTS = ROOT / "certificates"
SM = TEXPAPERS / "mtt-sm-parity-closure"

PREVIOUS = CERTS / "selected_correction_emission_gate_certificate.json"
SM_CERTS = {
    "rhoe_bn": SM / "certificates" / "selected_routec_nonidentity_rhoe_bn_construction_certificate.json",
    "smooth_bn": SM / "certificates" / "selected_routec_smooth_bn_galerkin_lift_certificate.json",
    "de_action": SM / "certificates" / "selected_routec_de_action_on_smooth_bn_certificate.json",
    "dotd": SM / "certificates" / "selected_routec_sector_projectors_dotd_on_smooth_bn_certificate.json",
    "c1": SM / "certificates" / "selected_routec_c1_primitive_response_on_smooth_bn_certificate.json",
}
SM_CANDIDATES = {
    "rhoe_bn": SM / "candidate_data" / "selected_routec_nonidentity_rhoe_bn_construction.candidate.json",
    "smooth_bn": SM / "candidate_data" / "selected_routec_smooth_bn_galerkin_lift.candidate.json",
    "de_action": SM / "candidate_data" / "selected_routec_de_action_on_smooth_bn.candidate.json",
    "dotd": SM / "candidate_data" / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json",
    "c1": SM / "candidate_data" / "selected_routec_c1_primitive_response_on_smooth_bn.candidate.json",
}

OUTPUT = CERTS / "routec_rhoe_bn_operator_prefix_import_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREVIOUS)
    certs = {name: load(path) for name, path in SM_CERTS.items()}
    candidates = {name: load(path) for name, path in SM_CANDIDATES.items()}

    rhoe = candidates["rhoe_bn"]["rho_E_candidate"]["numeric_gates"]
    smooth = candidates["smooth_bn"]["B_N_lift"]
    de_validation = candidates["de_action"]["validation"]["matrix_consistency"]
    dotd_validation = candidates["dotd"]["validation"]
    c1 = candidates["c1"]

    output = {
        "certificate": "RouteCRhoEBNOperatorPrefixImport",
        "status": "ROUTEC_RHOE_BN_OPERATOR_PREFIX_IMPORTED_NONINVARIANT_C1_PRIMITIVE_OPEN",
        "inputs": {
            "local_selected_correction_emission_gate": str(PREVIOUS.relative_to(ROOT)),
            "sm_certificates": {name: str(path) for name, path in SM_CERTS.items()},
            "sm_candidates": {name: str(path) for name, path in SM_CANDIDATES.items()},
        },
        "closed_now": {
            "nonidentity_projective_rhoE_candidate_built": certs["rhoe_bn"]["what_closes"][
                "nonidentity_projective_rhoE_candidate_built"
            ],
            "identity_smoke_replaced_by_nonidentity_candidate": certs["rhoe_bn"]["what_closes"][
                "identity_smoke_replaced_by_nonidentity_candidate"
            ],
            "smooth_BN_27_mode_scaffold_built": certs["smooth_bn"]["what_closes"][
                "smooth_scalar_basis_functions_phi_m_emitted"
            ],
            "Gram_stiffness_eigenpairs_and_model_Green_emitted": all(
                certs["smooth_bn"]["what_closes"][key]
                for key in (
                    "Gram_matrix_entries_emitted",
                    "stiffness_matrix_entries_emitted_for_model_active_laplacian",
                    "generalized_eigenpairs_emitted",
                    "Riesz_and_reduced_Green_emitted_for_model_active_laplacian",
                )
            ),
            "D_E_matrix_on_27_mode_BN_emitted": certs["de_action"]["what_closes"][
                "D_E_matrix_on_27_mode_BN_emitted"
            ],
            "sector_projectors_and_dotD_same_basis_emitted": certs["dotd"]["what_closes"][
                "sector_projectors_on_27_mode_BN_emitted"
            ]
            and certs["dotd"]["what_closes"]["dotD_alpha1_matrix_in_same_basis_emitted"],
            "canonical_C1_contraction_engine_built": certs["c1"]["what_closes"][
                "primitive_C1_contraction_engine_built"
            ],
            "canonical_C1_zero_response_no_go_proved": certs["c1"]["what_closes"][
                "canonical_tensor_zero_response_result_proved_finitely"
            ],
            "target_fitting_excluded_through_prefix": all(
                cert["what_closes"].get("target_fitting_excluded") is True for cert in certs.values()
            ),
        },
        "finite_prefix_summary": {
            "rho_E": {
                "rank": candidates["rhoe_bn"]["rho_E_candidate"]["rank"],
                "active_deck_rank_over_F3": rhoe["active_deck_rank_over_F3"],
                "nonidentity_norm": rhoe["nonidentity_norm"],
                "unitary_residual_max": rhoe["unitary_residual_max"],
                "order3_residual_max": rhoe["order3_residual_max"],
                "projective_commutator_residual": rhoe["projective_commutator_residual"],
                "selected_by_mtt": candidates["rhoe_bn"]["rho_E_candidate"]["selected_by_mtt"],
            },
            "B_N": {
                "basis_id": smooth["basis_id"],
                "dimension": smooth["dimension"],
                "zero_cluster_dimension": smooth["zero_cluster"]["dimension"],
                "complement_gap": smooth["complement_gap"],
                "projective_equivariance_up_to_central_phase": smooth["bundle_equivariance"][
                    "projective_equivariance_up_to_central_phase"
                ],
            },
            "D_E": {
                "domain_dimension": de_validation["domain_dimension"],
                "family_kernel_dimension": de_validation["family_kernel_dimension"],
                "higgs_kernel_dimension": de_validation["higgs_kernel_dimension"],
                "honest_validator_fails_only_by_selected_source_flags": de_validation[
                    "honest_validator_fails_only_by_selected_source_flags"
                ],
            },
            "dotD": {
                "diagnostic_lift_validator_passes": dotd_validation["diagnostic_lift_validator_passes"],
                "honest_validator_fails_only_by_source_driver_flags": dotd_validation[
                    "honest_validator_fails_only_by_source_driver_flags"
                ],
                "projector_ranks": {
                    sector: values["rank_trace"]
                    for sector, values in dotd_validation["projector_residuals"].items()
                },
            },
            "C1": {
                "primitive_tensor": c1["primitive_tensor"]["name"],
                "nonzero_tensor_slots": c1["primitive_tensor"]["nonzero_tensor_slots"],
                "all_c1_matrices_zero_for_canonical_tensor": c1["diagnostics"][
                    "all_c1_matrices_zero_for_canonical_tensor"
                ],
                "why_zero": c1["diagnostics"]["why_zero"],
            },
        },
        "not_closed": {
            "R1_selected_source_certificate": certs["de_action"]["what_remains_open"][
                "R1_selected_source_certificate"
            ],
            "R2_source_promotion_for_rhoE": certs["de_action"]["what_remains_open"][
                "R2_source_promotion_for_rhoE"
            ],
            "full_iwasawa_strominger_DE_not_only_model_active": certs["dotd"]["what_remains_open"][
                "full_iwasawa_strominger_DE_not_only_model_active"
            ],
            "full_iwasawa_truncation_error_certificate": certs["dotd"]["what_remains_open"][
                "full_iwasawa_truncation_error_certificate"
            ],
            "selected_dotD_source_verified": certs["c1"]["what_remains_open"][
                "selected_dotD_source_verified"
            ],
            "alpha1_driver_verified": certs["c1"]["what_remains_open"]["alpha1_driver_verified"],
            "selected_noninvariant_C1_primitive_or_vertex": certs["c1"]["what_remains_open"][
                "selected_noninvariant_C1_primitive_or_vertex"
            ],
            "selected_basis_transport_between_zero_and_response_modes": certs["c1"]["what_remains_open"][
                "selected_basis_transport_between_zero_and_response_modes"
            ],
            "nonzero_C1_response_matrices": certs["c1"]["what_remains_open"][
                "nonzero_C1_response_matrices"
            ],
            "yukawa_CKM_PMNS_magnitudes": certs["c1"]["what_remains_open"][
                "yukawa_CKM_PMNS_magnitudes"
            ],
            "full_SM_closure": certs["c1"]["what_remains_open"]["full_SM_or_no_knob_closure"],
        },
        "next_closing_object": {
            "name": "Selected_RouteC_NonInvariant_C1_Primitive_or_BasisTransport_Search_v1",
            "must_prove": [
                "derive a non-invariant C1 primitive, vertex correction, or basis transport from selected source data",
                "break the active-mode conservation zero-response obstruction without target fitting",
                "keep the same q79/F,m=1 branch and 27-mode B_N/dotD source chain",
                "produce nonzero C1 response matrices before claiming Yukawa, CKM, PMNS, or CP closure",
            ],
        },
        "guardrails": {
            "claims_selected_source_flags_promoted": False,
            "claims_nonzero_C1_response": False,
            "claims_yukawa_CKM_PMNS_magnitudes": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "honest_answer": (
            "A large finite Route-C prefix now exists: non-identity projective rho_E, "
            "27-mode smooth B_N, model D_E, same-basis dotD/projectors, and a C1 "
            "contraction engine. The canonical translation-invariant C1 primitive "
            "provably gives zero one-response matrices, so the next real gate is a "
            "selected non-invariant primitive, vertex correction, or basis transport."
        ),
        "previous_gate_status": previous["status"],
    }

    if "--write-certificate" in sys.argv:
        OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
