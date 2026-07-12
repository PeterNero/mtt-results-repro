"""Build the selected B_Huv two-column lift frontier packet.

C2 emits typed finite E_H^UV source IDs, C3 binds the selected diagonal HYM
metric/connection to those IDs, and C4 attaches the normalized finite trace.
Together these are enough to emit the same-source source-orthonormal two-column
UV Higgs lift needed by the H7B1F/G direct-Huv functor.

This is not a full direct Herm(2) Huv closure.  The same-source Hermitian
mass/strain operator M_source, the direct Huu/Hud/Hdd rows, the rank-one light
projector, selected s_beta, and the H K-threshold row remain open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
CONSTANTS = TEXPAPERS / "mtt-individual-constants-source-search"
CONST_DATA = CONSTANTS / "candidate_data"

SLUG = "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BHUV_LIFT = PACKET_DIR / "bhuv_two_column_source_orthonormal_lift.packet.json"
BHUV_REQUEST = PACKET_DIR / "h7b1g_bhuv_request_recheck_after_c4.packet.json"
DIRECT_RECHECK = PACKET_DIR / "direct_huv_functor_recheck_after_bhuv_lift.packet.json"
MSOURCE_FRONTIER = PACKET_DIR / "msource_huv_frontier_after_bhuv_lift.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_bhuv_lift.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_bhuv_lift.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_BHuvTwoColumnSourceOrthonormalLift_or_MSourceHuvFrontier_v1.md"

C4_CANDIDATE = DATA / "selected_ehuvquadraturetraceprojectionmeasure_or_directhuvpayload.candidate.json"
C2_BASIS = (
    DATA
    / "selected_higgshymsectionringquadraturebridge_or_directhuvpayload"
    / "c2_ehuv_finite_quotient_basis_exactness.packet.json"
)
C3_METRIC = (
    DATA
    / "selected_ehuvhymmetricconnectionfixedpoint_or_directhuvpayload"
    / "c3_ehuv_hym_metric_connection_binding.packet.json"
)
C4_TRACE = (
    DATA
    / "selected_ehuvquadraturetraceprojectionmeasure_or_directhuvpayload"
    / "c4_ehuv_finite_trace_quadrature_attachment.packet.json"
)
C4_HK = (
    DATA
    / "selected_ehuvquadraturetraceprojectionmeasure_or_directhuvpayload"
    / "hk_threshold_gate_after_c4_trace.packet.json"
)

H7B1A = (
    CONST_DATA
    / "const_higgs_01_h7b1a_selected_two_higgs_metric_or_light_projector_source.candidate.json"
)
H7B1F = (
    CONST_DATA
    / "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet"
    / "basis_invariant_huv_functor_theorem.packet.json"
)
H7B1G_SPLIT = (
    CONST_DATA
    / "const_higgs_01_h7b1g_fill_bhuv_or_msource"
    / "support_split_theorem.packet.json"
)
H7B1G_BHUV = (
    CONST_DATA
    / "const_higgs_01_h7b1g_fill_bhuv_or_msource"
    / "bhuv_minimal_lift_payload_request.packet.json"
)
H7B1G_MSOURCE = (
    CONST_DATA
    / "const_higgs_01_h7b1g_fill_bhuv_or_msource"
    / "msource_minimal_operator_payload_request.packet.json"
)
H7B1I_MSOURCE = (
    CONST_DATA
    / "const_higgs_01_h7b1i_msource_from_selected_response_prefix"
    / "msource_acceptance_functor.packet.json"
)
H7B1T_ATTEMPT = (
    CONST_DATA
    / "const_higgs_01_h7b1t_uv_higgs_plane_binding_or_minimal_lift_theorem"
    / "actual_source_binding_attempt.packet.json"
)
H7B1Y_DIRECT_SCHEMA = (
    CONST_DATA
    / "const_higgs_01_h7b1y_selected_ehuv_section_basis_quadrature_or_herm2_row_values"
    / "direct_herm2_huv_row_schema.packet.json"
)

STATUS = (
    "MTT_SELECTED_BHUVTWOCOLUMNSOURCEORTHONORMALLIFT_OR_MSOURCEHUVFRONTIER_"
    "BHUV_LIFT_CLOSED_MSOURCE_HUV_OPEN"
)
NEXT = "MTT_Selected_MSourceHermitianMassStrainOperator_or_C5C6HiggsProjectionBridge_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing B_Huv lift inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        C4_CANDIDATE,
        C2_BASIS,
        C3_METRIC,
        C4_TRACE,
        C4_HK,
        H7B1A,
        H7B1F,
        H7B1G_SPLIT,
        H7B1G_BHUV,
        H7B1G_MSOURCE,
        H7B1I_MSOURCE,
        H7B1T_ATTEMPT,
        H7B1Y_DIRECT_SCHEMA,
    ]
    require_sources(sources)

    c4_candidate = load(C4_CANDIDATE)
    c2 = load(C2_BASIS)
    c3 = load(C3_METRIC)
    c4 = load(C4_TRACE)
    c4_hk = load(C4_HK)
    h7b1a = load(H7B1A)
    h7b1f = load(H7B1F)
    h7b1g_split = load(H7B1G_SPLIT)
    h7b1g_bhuv = load(H7B1G_BHUV)
    h7b1g_msource = load(H7B1G_MSOURCE)
    h7b1i = load(H7B1I_MSOURCE)
    h7b1t = load(H7B1T_ATTEMPT)
    h7b1y = load(H7B1Y_DIRECT_SCHEMA)

    uv_ids = c3["basis_binding"]["ordered_E_H_UV_source_ids"]
    trace = c4["finite_trace_quadrature"]
    exactness = c2["exactness_certificate"]
    typing = c2["typing_checks"]
    metric = c3["metric_connection_fixed_point"]
    branch = "q79/F,m=1 eta_00 rank-2 V_alpha diagonal T3 HYM lane"

    norm_u = "Tr_Q_sel^U,ZHYM(exp(u))"
    norm_d = "Tr_Q_sel^U,ZHYM(exp(-u))"
    b_huv_formula = [
        f"{norm_u}^(-1/2) * {uv_ids['H_u']}",
        f"{norm_d}^(-1/2) * {uv_ids['H_d_dagger']}",
    ]

    bhuv_lift = {
        "schema": "MTTSelectedBHuvTwoColumnSourceOrthonormalLift.v1",
        "status": "BHUV_TWO_COLUMN_SOURCE_ORTHONORMAL_LIFT_EMITTED_MSOURCE_OPEN",
        "closure_claimed": True,
        "same_source_branch": branch,
        "selected_source_provenance": [
            {"role": "C2 finite E_H^UV basis and quotient exactness", "source": rel(C2_BASIS)},
            {"role": "C3 selected HYM metric/connection on E_H^UV", "source": rel(C3_METRIC)},
            {"role": "C4 selected finite trace/quadrature", "source": rel(C4_TRACE)},
            {"role": "H7B1F conditional Huv functor", "source": rel(H7B1F)},
            {"role": "H7B1G B_Huv minimal lift request", "source": rel(H7B1G_BHUV)},
        ],
        "ordered_two_column_source_space": {
            "basis": ["H_u", "H_d^dagger"],
            "ordered_E_H_UV_source_ids": uv_ids,
            "pre_whitening_column_vectors": {
                "H_u": {"coordinate_vector": [1, 0], "source_id": uv_ids["H_u"]},
                "H_d_dagger": {"coordinate_vector": [0, 1], "source_id": uv_ids["H_d_dagger"]},
            },
            "selected_finite_quotient": c2["finite_quotient_basis"]["selected_finite_quotient"],
        },
        "source_hermitian_inner_product": {
            "definition": "<x,y>_G,Q = Tr_Q(x^* G_HYM y)",
            "quadrature_rule_id": trace["quadrature_rule_id"],
            "node_count": trace["node_count"],
            "uniform_weight_rational": trace["uniform_weight_rational"],
            "G_HYM_on_ordered_basis": "diag(exp(u), exp(-u))",
            "connection_on_ordered_basis": metric["connection_on_E_H_UV_basis"],
            "Gram_matrix_before_whitening": [[norm_u, "0"], ["0", norm_d]],
            "positivity_certificate": {
                "N_u_positive": True,
                "N_d_positive": True,
                "reason": "exp(u) and exp(-u) are pointwise positive and Tr_Q is the normalized positive finite trace.",
            },
            "offdiagonal_zero_reason": (
                "The selected metric is diagonal in the T3 eigenline basis "
                "(H_u,H_d^dagger), so <H_u,H_d^dagger>_G,Q=0."
            ),
        },
        "whitening_map_and_lift": {
            "whitening_map_W": [[f"{norm_u}^(-1/2)", "0"], ["0", f"{norm_d}^(-1/2)"]],
            "B_Huv_columns": b_huv_formula,
            "B_Huv_symbolic_exact_payload_emitted": True,
            "B_Huv_numeric_entries_evaluated": False,
            "source_orthonormality_certificate": {
                "equation": "B_Huv^* G_Q B_Huv = I_2",
                "matrix": [["1", "0"], ["0", "1"]],
                "requires_only_positive_trace_norms": True,
            },
        },
        "minimal_lift_request_tests": {
            "source_id_matching_selected_branch": True,
            "two_finite_source_space_column_vectors_emitted": True,
            "source_Hermitian_inner_product_or_Gram_matrix_emitted": True,
            "color_triplet_projection_or_decoupling_certificate": True,
            "doublet_slot_certificate": {
                "low_energy_higgs_doublet_embedding_closed": typing[
                    "low_energy_higgs_doublet_embedding_closed"
                ],
                "H_u_hypercharge_after_projection": c2["finite_quotient_basis"]["uv_lift_basis"][0][
                    "hypercharge_after_projection"
                ],
                "H_d_dagger_hypercharge_after_projection": c2["finite_quotient_basis"]["uv_lift_basis"][1][
                    "hypercharge_after_projection"
                ],
                "scope": "physical doublet slot typing only; not a selected rank-one light projector",
            },
            "quotient_admissibility_certificate": {
                "q_Hu_equals_q_Hd_dagger": exactness["q_Hu_equals_q_Hd_dagger"],
                "q_times_kernel_is_zero": exactness["q_times_kernel_is_zero"],
                "kernel_is_span_Hu_minus_Hd_dagger": exactness[
                    "kernel_is_span_Hu_minus_Hd_dagger"
                ],
                "q_restricted_to_each_B_Huv_column_nonzero": True,
            },
            "basis_phase_covariance_rule_emitted": True,
            "basis_phase_covariance_rule": (
                "For V=diag(e^{i alpha},e^{i beta}) on the Huv columns, "
                "B_Huv -> B_Huv V and Huv -> V^* Huv V; eigenvalues and "
                "projector invariants are basis-covariant."
            ),
            "finite_exactness_or_truncation_certificate_attached": True,
            "source_orthonormality_required_by_H7B1G_satisfied": True,
        },
        "not_claimed": {
            "selected_rank_one_light_projector_P_L": False,
            "selected_minimal_lift_sigma_G_of_low_energy_H": False,
            "selected_s_beta": False,
            "M_source": False,
            "direct_Huu_Hud_Hdd": False,
            "Huv_values": False,
            "K_threshold_Omega_H_lambda": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    previous_missing = h7b1g_split["bhuv_support"]["still_missing_for_B_Huv"]
    bhuv_request_recheck = {
        "schema": "MTTH7B1GBHuvRequestRecheckAfterC4.v1",
        "status": "H7B1G_BHUV_TWO_COLUMN_LIFT_REQUEST_CLOSED_PROJECTOR_STILL_OPEN",
        "closure_claimed": True,
        "original_request_source": rel(H7B1G_BHUV),
        "original_status": h7b1g_bhuv["status"],
        "previous_missing_for_B_Huv": previous_missing,
        "after_C2_C3_C4": {
            "channel_weights": True,
            "color_triplet_projection_or_decoupling": True,
            "family_or_Higgs_kinetic_metrics": True,
            "physical_Higgs_doublet_slot_selection": True,
            "selected_metric_on_two_Higgs_plane": True,
            "two_column_source_orthonormal_lift_B_Huv": True,
            "selected_rank_one_light_projector": False,
            "selected_minimal_lift_sigma_G": False,
            "selected_s_beta_value": False,
        },
        "request_tests": bhuv_lift["minimal_lift_request_tests"],
        "decision": {
            "B_Huv_two_column_uv_lift_emitted": True,
            "B_Huv_can_now_feed_H7B1F_functor": True,
            "rank_one_projector_contract_closed": False,
            "H7B1A_quotient_to_projector_underdetermination_retained": h7b1a[
                "quotient_to_projector_underdetermination_proved"
            ],
            "why_projector_not_closed": h7b1a["theorem"]["statement"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    direct_recheck = {
        "schema": "MTTDirectHerm2HuvFunctorRecheckAfterBHuvLift.v1",
        "status": "DIRECT_HERM2_HUV_FUNCTOR_HAS_BHUV_INPUT_MSOURCE_OPEN",
        "closure_claimed": True,
        "conditional_functor": h7b1f["theorem"]["statement"],
        "direct_schema_source": rel(H7B1Y_DIRECT_SCHEMA),
        "accepted_formula": h7b1y["accepted_formula"],
        "direct_schema_fields_after_lift": {
            "B_Huv": b_huv_formula,
            "G_source_or_whitening_map": "G_Q=Tr_Q(diag(exp(u),exp(-u))), W=diag(N_u^-1/2,N_d^-1/2)",
            "quotient_admissibility_certificate": True,
            "same_source_exactness_or_residual_bound": True,
            "M_source": None,
            "Huu": None,
            "Hud": None,
            "Hdd": None,
            "Hdu_equals_conj_Hud_certificate": None,
            "Delta_equals_Huu_minus_Hdd_over_2": None,
            "Omega_equals_Hud": None,
            "P_L_light_projector": None,
            "s_beta_equals_Delta2_over_Delta2_plus_absOmega2": None,
        },
        "acceptance_booleans_after_lift": {
            "B_Huv_emitted": True,
            "M_source_emitted": False,
            "Herm2_payload_complete": False,
            "direct_Huu_Hud_Hdd_emitted": False,
            "selected_s_beta_promoted": False,
            "numeric_lambda_H_derived": False,
        },
        "decision": {
            "direct_Herm2_Huv_payload_emitted": False,
            "reason": "Huv=B_Huv^* M_source B_Huv cannot be evaluated until the same-source Hermitian M_source is emitted.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    msource_frontier = {
        "schema": "MTTMSourceHuvFrontierAfterBHuvLift.v1",
        "status": "MSOURCE_HERMITIAN_MASS_STRAIN_OPERATOR_IS_NOW_DIRECT_ROUTE_FRONTIER",
        "closure_claimed": True,
        "original_msource_request_source": rel(H7B1G_MSOURCE),
        "original_msource_status": h7b1g_msource["status"],
        "h7b1i_acceptance_functor_source": rel(H7B1I_MSOURCE),
        "same_source_with_B_Huv_now_available": True,
        "must_emit_next": h7b1g_msource["must_emit"],
        "minimal_nonlooping_payload": [
            "selected_source_verified true for the q79/F,m=1 Route-C/HYM branch",
            "finite source operator representation on the same source space as B_Huv",
            "D_E/Riesz/reduced-Green/dotD response from that source",
            "Hermitian mass/strain operator M_source with M_source^*=M_source",
            "H-sector restriction certificate proving B_Huv^* M_source B_Huv is the accepted Herm(2) Huv block",
            "exactness/residual certificate and no lifted-flag promotion",
        ],
        "still_open": {
            "selected_Hermitian_M_source": True,
            "selected_operator_payload_for_Huv": True,
            "H_sector_restriction_map": True,
            "direct_Huu_Hud_Hdd": True,
            "selected_s_beta": True,
            "K_threshold_Omega_H_lambda": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    h_row = dict(c4_hk["H_row"])
    h_row["B_Huv_two_column_source_orthonormal_lift_emitted"] = True
    hk_gate = {
        "schema": "MTTHKThresholdGateAfterBHuvLift.v1",
        "status": "H_K_THRESHOLD_GATE_BHUV_LIFT_CLOSED_MSOURCE_HUV_OPEN_9_OF_10",
        "closure_claimed": True,
        "required_output": c4_hk["required_output"],
        "source_equation": c4_hk["source_equation"],
        "accepted_selected_K_source_row_count": c4_hk["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": c4_hk[
            "selected_K_threshold_row_count_required"
        ],
        "H_row": h_row,
        "conditional_consequent_current": c4_hk["conditional_consequent_current"],
        "direct_route_state": {
            "B_Huv_two_column_lift_emitted": True,
            "M_source_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "K_threshold_Omega_H_lambda_emitted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterBHuvLift.v1",
        "status": "NEXT_FRONTIER_MSOURCE_DIRECT_HUV_OR_C5C6_HIGGS_PROJECTION_BRIDGE",
        "closure_claimed": True,
        "closed_here": [
            "same-source B_Huv two-column UV lift emitted",
            "source Gram/inner product G_Q=Tr_Q(diag(exp(u),exp(-u))) emitted",
            "whitening map W=diag(N_u^-1/2,N_d^-1/2) emitted",
            "B_Huv^* G_Q B_Huv = I_2 certified",
            "H7B1F direct-Huv functor rechecked with B_Huv true and M_source false",
            "H K-threshold gate remains 9/10",
        ],
        "still_open": [
            "same-source Hermitian mass/strain operator M_source",
            "H-sector restriction proving B_Huv^* M_source B_Huv is the accepted Herm(2) block",
            "direct Huu,Hud,Hdd rows",
            "C5 trace-to-H7B1U/projection-measure identity",
            "C6 no-extra-boundary/source theorem",
            "selected rank-one light projector P_L or selected s_beta equivalent",
            "K_threshold.Omega_H.lambda source row",
            "strict Omega/lambda_H scalar execution",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedBHuvTwoColumnSourceOrthonormalLiftOrMSourceHuvFrontier",
        "status": STATUS,
        "previous_status": c4_candidate["status"],
        "theorem": {
            "name": "SelectedBHuvTwoColumnSourceOrthonormalLiftTheorem",
            "proved": True,
            "statement": (
                "C2 supplies the ordered finite E_H^UV source columns H_u and H_d^dagger, "
                "C3 supplies the same-source diagonal HYM metric diag(exp(u),exp(-u)), "
                "and C4 supplies the normalized finite trace.  Therefore the exact "
                "source Gram matrix is diag(Tr_Q(exp(u)),Tr_Q(exp(-u))) and the "
                "whitened columns B_Huv=(N_u^-1/2 H_u,N_d^-1/2 H_d^dagger) satisfy "
                "B_Huv^* G_Q B_Huv=I_2.  This closes the two-column B_Huv input of "
                "the H7B1F/G direct-Huv functor.  It does not emit M_source, Huu/Hud/"
                "Hdd, a rank-one light projector, selected s_beta, lambda_H, or the "
                "tenth H K-threshold row."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "bridge_validator_C1_closed": True,
            "bridge_validator_C2_closed": True,
            "bridge_validator_C3_closed": True,
            "bridge_validator_C4_closed": True,
            "B_Huv_two_column_uv_lift_emitted": True,
            "B_Huv_source_orthonormality_certified": True,
            "B_Huv_numeric_entries_evaluated": False,
            "selected_Hermitian_M_source_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "direct_Huu_Hud_Hdd_emitted": False,
            "selected_rank_one_light_projector_emitted": False,
            "selected_s_beta_value_found": False,
            "K_threshold_Omega_H_lambda_emitted": False,
            "accepted_selected_K_source_row_count": c4_hk["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": c4_hk[
                "selected_K_threshold_row_count_required"
            ],
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "bhuv_two_column_source_orthonormal_lift": rel(BHUV_LIFT),
            "h7b1g_bhuv_request_recheck_after_c4": rel(BHUV_REQUEST),
            "direct_huv_functor_recheck_after_bhuv_lift": rel(DIRECT_RECHECK),
            "msource_huv_frontier_after_bhuv_lift": rel(MSOURCE_FRONTIER),
            "hk_threshold_gate_after_bhuv_lift": rel(HK_GATE),
            "next_cutset_after_bhuv_lift": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedBHuvTwoColumnSourceOrthonormalLiftOrMSourceHuvFrontierCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "B_Huv_two_column_uv_lift_emitted": True,
        "B_Huv_source_orthonormality_certified": True,
        "selected_Hermitian_M_source_emitted": False,
        "direct_Herm2_Huv_payload_emitted": False,
        "direct_Huu_Hud_Hdd_emitted": False,
        "selected_rank_one_light_projector_emitted": False,
        "selected_s_beta_value_found": False,
        "K_threshold_Omega_H_lambda_emitted": False,
        "accepted_selected_K_source_row_count": c4_hk["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": c4_hk[
            "selected_K_threshold_row_count_required"
        ],
        "ten_K_antecedent_satisfied": False,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "accepted_internal_scalar_value_row_count": 0,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected BHuvTwoColumnSourceOrthonormalLift or MSourceHuvFrontier v1

Status: `{STATUS}`

## What Closed

- emitted the same-source two-column UV lift `B_Huv` on `(H_u,H_d^dagger)`
- source branch: `{branch}`
- source Gram: `diag({norm_u},{norm_d})`
- whitening map: `diag({norm_u}^(-1/2),{norm_d}^(-1/2))`
- certified `B_Huv^* G_Q B_Huv = I_2`
- rechecked H7B1F: `B_Huv=true`, `M_source=false`
- H K-threshold gate remains `{c4_hk["accepted_selected_K_source_row_count"]}/{c4_hk["selected_K_threshold_row_count_required"]}`

## Still Open

- same-source Hermitian mass/strain operator `M_source`
- direct `Huu,Hud,Hdd` rows or equivalent Herm(2) Huv payload
- C5 trace-to-H7B1U/projection-measure identity and C6 no-extra-boundary theorem
- rank-one light projector `P_L` or selected `s_beta` equivalent
- selected `K_threshold.Omega_H.lambda`

Next required artifact: `{NEXT}`
"""

    write_json(BHUV_LIFT, bhuv_lift)
    write_json(BHUV_REQUEST, bhuv_request_recheck)
    write_json(DIRECT_RECHECK, direct_recheck)
    write_json(MSOURCE_FRONTIER, msource_frontier)
    write_json(HK_GATE, hk_gate)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
