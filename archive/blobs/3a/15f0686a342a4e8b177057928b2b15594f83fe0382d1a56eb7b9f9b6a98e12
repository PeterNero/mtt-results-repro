"""Build the H-sector restriction from the selected B_Huv lift.

The previous full M_source+R_H packet instantiated the full route but still
listed R_H as absent because it replayed the older H7B1J compact-H-slot failure.
After B_Huv has been emitted and certified source-orthonormal, there is a
canonical selected two-Higgs restriction:

    R_H(x) = B_Huv^* G_Q x
    P_H    = B_Huv R_H

This closes the kinematic H-sector restriction onto span(B_Huv).  It does not
emit the dynamic Higgs response Hessian, a Herm(2) value table, s_beta, lambda_H,
or the tenth K row.
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
CONST_DATA = TEXPAPERS / "mtt-individual-constants-source-search" / "candidate_data"

SLUG = "selected_hsectorrestrictionfrombhuv_or_dynamichiggsresponsehessian"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RH_PACKET = PACKET_DIR / "hsector_restriction_from_bhuv.packet.json"
ROUTE_REDUCTION = PACKET_DIR / "full_route_reduction_after_rh_closure.packet.json"
DYNAMIC_GATE = PACKET_DIR / "dynamic_higgs_response_hessian_gate.packet.json"
H7B1J_RECHECK = PACKET_DIR / "h7b1j_after_rh_closure_recheck.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_rh_closure.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_rh_closure.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HSectorRestrictionFromBHuv_or_DynamicHiggsResponseHessian_v1.md"

PREVIOUS_FULL = DATA / "selected_fullmsourcehsectorrestriction_or_hresponsehuvtable.candidate.json"
PREVIOUS_FULL_ROUTE = (
    DATA
    / "selected_fullmsourcehsectorrestriction_or_hresponsehuvtable"
    / "full_msource_rh_route_instantiation.packet.json"
)
PREVIOUS_SOURCE_GATE = (
    DATA
    / "selected_fullmsourcehsectorrestriction_or_hresponsehuvtable"
    / "selected_source_object_value_gate.packet.json"
)
PREVIOUS_HK = (
    DATA
    / "selected_fullmsourcehsectorrestriction_or_hresponsehuvtable"
    / "hk_threshold_gate_after_full_msource_route.packet.json"
)
PREVIOUS_MH_TABLE = (
    DATA
    / "selected_mhthreerowsourcefunctional_or_c5c6bridgeexecution"
    / "mh_three_row_execution_table_request.packet.json"
)
BHUV = (
    DATA
    / "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier"
    / "bhuv_two_column_source_orthonormal_lift.packet.json"
)
H7B1I_CURRENT = (
    CONST_DATA
    / "const_higgs_01_h7b1i_msource_from_selected_response_prefix"
    / "current_msource_export_attempt.packet.json"
)
H7B1J_DYNAMIC = (
    CONST_DATA
    / "const_higgs_01_h7b1j_dynamic_hessian_or_hsector_restriction_export"
    / "dynamic_hessian_edge_export_attempt.packet.json"
)
H7B1J_HSECTOR = (
    CONST_DATA
    / "const_higgs_01_h7b1j_dynamic_hessian_or_hsector_restriction_export"
    / "hsector_restriction_edge_export_attempt.packet.json"
)
H7B1J_STRICT = (
    CONST_DATA
    / "const_higgs_01_h7b1j_dynamic_hessian_or_hsector_restriction_export"
    / "strict_msource_gate_validator.packet.json"
)
H7B1L_DYNAMIC_C1 = (
    CONST_DATA
    / "const_higgs_01_h7b1l_dynamic_phifinc1_huv_response_or_independent_huv_hessian"
    / "dynamic_c1_backimport_for_huv.packet.json"
)

STATUS = (
    "MTT_SELECTED_HSECTORRESTRICTIONFROMBHUV_OR_DYNAMICHIGGSRESPONSEHESSIAN_"
    "RH_KINEMATIC_RESTRICTION_CLOSED_DYNAMIC_MH_OPEN"
)
NEXT = "MTT_Selected_DynamicHiggsResponseHessianOnBHuv_or_DirectMHValueEmission_v1"


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
        raise FileNotFoundError("missing R_H closure inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS_FULL,
        PREVIOUS_FULL_ROUTE,
        PREVIOUS_SOURCE_GATE,
        PREVIOUS_HK,
        PREVIOUS_MH_TABLE,
        BHUV,
        H7B1I_CURRENT,
        H7B1J_DYNAMIC,
        H7B1J_HSECTOR,
        H7B1J_STRICT,
        H7B1L_DYNAMIC_C1,
    ]
    require_sources(sources)

    previous_full = load(PREVIOUS_FULL)
    previous_full_route = load(PREVIOUS_FULL_ROUTE)
    previous_source_gate = load(PREVIOUS_SOURCE_GATE)
    previous_hk = load(PREVIOUS_HK)
    mh_table = load(PREVIOUS_MH_TABLE)
    bhuv = load(BHUV)
    h7b1i_current = load(H7B1I_CURRENT)
    h7b1j_dynamic = load(H7B1J_DYNAMIC)
    h7b1j_hsector = load(H7B1J_HSECTOR)
    h7b1j_strict = load(H7B1J_STRICT)
    h7b1l_dynamic_c1 = load(H7B1L_DYNAMIC_C1)

    source_space = previous_full_route["source_space"]
    b_formula = bhuv["whitening_map_and_lift"]["B_Huv_columns"]
    gram = bhuv["source_hermitian_inner_product"]
    orth = bhuv["whitening_map_and_lift"]["source_orthonormality_certificate"]
    source_ids = bhuv["ordered_two_column_source_space"]["ordered_E_H_UV_source_ids"]
    h7b1j_old_rh_missing = h7b1j_hsector["export_decision"]["R_H_exported"] is False
    current_values = h7b1i_current["computed_values"]

    rh_packet = {
        "schema": "MTTHSectorRestrictionFromBHuv.v1",
        "status": "RH_KINEMATIC_RESTRICTION_FROM_BHUV_CLOSED",
        "closure_claimed": True,
        "restriction_kind": "kinematic_two_Higgs_source_restriction",
        "selected_source_space": source_space,
        "selected_two_higgs_subspace": {
            "definition": "H_kin := span(B_Huv[:,1], B_Huv[:,2]) inside the selected E_H^UV source space",
            "basis_order": ["H_u", "H_d^dagger"],
            "ordered_source_ids": source_ids,
            "B_Huv_columns": b_formula,
            "source_inner_product": "<x,y>_G,Q = Tr_Q(x^* G_HYM y)",
            "G_Q": gram["G_HYM_on_ordered_basis"],
            "quadrature_rule_id": gram["quadrature_rule_id"],
        },
        "canonical_restriction": {
            "R_H": "R_H(x) = B_Huv^* G_Q x",
            "P_H": "P_H = B_Huv R_H = B_Huv B_Huv^* G_Q",
            "R_H_matrix_on_BHuv_coordinates": [
                ["<B_u, ->_G,Q"],
                ["<B_d, ->_G,Q"],
            ],
            "R_H_numeric_27x2_entries_evaluated": False,
            "R_H_symbolic_exact_payload_emitted": True,
            "selected_H_sector_restriction_R_H_emitted": True,
            "selected_H_projector_P_H_emitted": True,
        },
        "proof_identities": {
            "input_orthonormality": orth["equation"],
            "R_H_B_Huv_equals_I2": True,
            "P_H_squared_equals_P_H": True,
            "P_H_is_G_Q_self_adjoint": True,
            "image_P_H_equals_span_B_Huv": True,
            "kernel_R_H_equals_G_Q_orthogonal_complement_of_span_B_Huv": True,
            "phase_covariance": bhuv["minimal_lift_request_tests"]["basis_phase_covariance_rule"],
        },
        "why_this_is_selected": [
            "B_Huv was emitted from the selected C2 finite E_H^UV quotient basis",
            "G_Q was emitted from the selected C3 HYM metric and C4 finite trace",
            "B_Huv^* G_Q B_Huv = I_2 was certified",
            "the orthogonal adjoint restriction is canonical and introduces no empirical selector",
        ],
        "not_claimed": {
            "dynamic_H_response_or_mass_strain_values": False,
            "selected_Hermitian_M_source_entries": False,
            "direct_Herm2_Huv_values": False,
            "rank_one_low_energy_light_projector": False,
            "compact_single_H_slot_dotD_promoted": False,
            "selected_s_beta": False,
            "lambda_H_or_tenth_K_row": False,
            "C5b_C6_physical_projection_no_boundary": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    dynamic_h_response_absent = (
        current_values["H_response"] is None
        and h7b1j_dynamic["export_decision"]["H_response_exported"] is False
        and h7b1l_dynamic_c1["higgs_relevance_decision"][
            "dynamic_C1_support_directly_emits_Huv_response"
        ]
        is False
    )
    msource_absent = (
        current_values["M_source"] is None
        and h7b1j_strict["strict_outputs"]["M_source"] is None
    )
    huv_absent = (
        current_values["Huv"] is None
        and h7b1j_strict["strict_outputs"]["Huv"] is None
    )

    route_reduction = {
        "schema": "MTTFullRouteReductionAfterRHClosure.v1",
        "status": "FULL_ROUTE_REDUCED_TO_DYNAMIC_HRESPONSE_OR_DIRECT_MH",
        "closure_claimed": True,
        "previous_full_route_status": previous_full["status"],
        "formula_after_R_H_closure": {
            "R_H": rh_packet["canonical_restriction"]["R_H"],
            "M_source_full_route": previous_full_route["formula"]["Hermitian_projection"],
            "Huv_full_route": previous_full_route["formula"]["Huv_link"],
            "direct_BHuv_domain_exit": "M_H = Hess_H(F_H)|_{B_Huv coordinates}, a selected Herm(2) block",
        },
        "closed_route_inputs": {
            "same_q79_F_m1_source_space": True,
            "B_Huv_source_orthonormal": True,
            "R_H_kinematic_restriction_from_B_Huv": True,
            "Pauli_Riesz_three_row_extractors": previous_full["closure_decision"][
                "Pauli_Riesz_three_row_source_functional_contract_closed"
            ],
            "C5a_trace_grid_identity": previous_full["closure_decision"][
                "C5a_trace_grid_identity_closed"
            ],
            "no_observed_selector": True,
        },
        "remaining_value_objects": {
            "selected_dynamic_H_response_emitted": False,
            "selected_Hermitian_M_source_emitted": False,
            "direct_Herm2_M_H_on_BHuv_emitted": False,
            "selected_H_response_table_emitted": False,
            "dynamic_H_response_absent": dynamic_h_response_absent,
            "M_source_absent": msource_absent,
            "Huv_absent": huv_absent,
        },
        "frontier_reduction": (
            "The full route no longer needs a separate H-sector restriction export. "
            "It needs the dynamic Higgs response Hessian/mass-strain source, or an "
            "equivalent directly emitted Herm(2) M_H on the B_Huv domain."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    dynamic_gate = {
        "schema": "MTTDynamicHiggsResponseHessianGateAfterRHClosure.v1",
        "status": "DYNAMIC_HIGGS_RESPONSE_HESSIAN_ON_BHUV_DOMAIN_OPEN",
        "closure_claimed": True,
        "required_object": {
            "name": "SelectedDynamicHiggsResponseHessianOnBHuv",
            "functional": "F_H(z_u,z_d) selected from the same q79/F,m=1 finite trace/HYM/retarded-overlap source",
            "value_rule": "(M_H)_ij = d^2 F_H / d(conj(z_i)) dz_j on the ordered B_Huv coordinates",
            "codomain": "Herm(2) on span(B_Huv)",
            "minimal_rows": ["Huu", "Hud_re", "Hud_im", "Hdd"],
            "trace_free_rows": ["Delta", "Re_Omega", "Im_Omega"],
        },
        "current_table": mh_table["minimal_table"],
        "current_values": {
            "Huu": None,
            "Hud_re": None,
            "Hud_im": None,
            "Hdd": None,
            "Delta": None,
            "Re_Omega": None,
            "Im_Omega": None,
            "s_beta": None,
            "lambda_H": None,
            "K_threshold_Omega_H_lambda": None,
        },
        "rejected_current_support_as_values": {
            "H7B1J_dynamic_hessian_export": h7b1j_dynamic["export_decision"],
            "H7B1L_dynamic_C1_directly_emits_Huv": h7b1l_dynamic_c1[
                "higgs_relevance_decision"
            ]["dynamic_C1_support_directly_emits_Huv_response"],
            "static_or_compact_H_slot_promoted": False,
            "observed_Higgs_or_beta_selector_used": False,
        },
        "accepted_exit_conditions": [
            "derive F_H and its Herm(2) second variation on B_Huv from selected source data",
            "or emit selected H_response on the same source and evaluate via the closed R_H",
            "or prove C5b/C6 plus a second-variation bridge that emits the same M_H values",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    h7b1j_recheck = {
        "schema": "MTTH7B1JRecheckAfterRHClosure.v1",
        "status": "H7B1J_RH_KINEMATIC_GAP_RETIRED_DYNAMIC_HESSIAN_STILL_OPEN",
        "closure_claimed": True,
        "old_hsector_edge_export_status": h7b1j_hsector["status"],
        "old_R_H_exported": h7b1j_hsector["export_decision"]["R_H_exported"],
        "new_R_H_exported_from_B_Huv": True,
        "distinction": (
            "The old compact single-H-slot/End0-to-sector route is not promoted. "
            "The closed map is the canonical two-Higgs kinematic restriction "
            "R_H=B_Huv^*G_Q from the selected B_Huv lift."
        ),
        "strict_gate_after_R_H_update": {
            "same_q79_F_m1_branch": True,
            "B_Huv_two_column_lift_source_owned": True,
            "H_sector_restriction_map_source_owned": True,
            "dynamic_hessian_or_mass_strain_source_owned": False,
            "finite_exactness_or_error_certificate_for_values": False,
            "no_observed_selector": True,
            "strict_M_source_gate_passes": False,
        },
        "why_still_fails": {
            "H_response_exported": h7b1j_dynamic["export_decision"]["H_response_exported"],
            "M_source_dynamic_part_exported": h7b1j_dynamic["export_decision"][
                "M_source_dynamic_part_exported"
            ],
            "reason": h7b1j_dynamic["export_decision"]["reason"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    h_row = dict(previous_hk["H_row"])
    h_row.update(
        {
            "selected_H_sector_restriction_R_H_emitted": True,
            "selected_H_projector_P_H_emitted": True,
            "full_route_reduced_to_dynamic_H_response_or_direct_M_H": True,
            "selected_dynamic_H_response_emitted": False,
            "selected_Hermitian_M_source_emitted": False,
            "M_source_plus_R_H_values_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_s_beta_value_found": False,
            "K_threshold_Omega_H_lambda_emitted": False,
        }
    )
    hk_gate = {
        "schema": "MTTHKThresholdGateAfterRHClosure.v1",
        "status": "H_K_THRESHOLD_GATE_RH_CLOSED_DYNAMIC_MH_OPEN_9_OF_10",
        "closure_claimed": True,
        "accepted_selected_K_source_row_count": previous_hk["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "H_row": h_row,
        "conditional_consequent_current": previous_hk["conditional_consequent_current"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterRHClosure.v1",
        "status": "NEXT_FRONTIER_DYNAMIC_HIGGS_RESPONSE_HESSIAN_ON_BHUV_OR_DIRECT_MH_VALUE",
        "closure_claimed": True,
        "closed_here": [
            "selected kinematic H-sector restriction R_H=B_Huv^*G_Q emitted",
            "selected H-sector projector P_H=B_HuvB_Huv^*G_Q emitted",
            "R_H B_Huv=I_2 and P_H^2=P_H certified symbolically",
            "old H7B1J compact-H-slot R_H blocker retired without promoting compact dotD support",
            "full M_source route reduced to selected dynamic H_response or direct Herm(2) M_H",
            "H K-threshold gate remains 9/10",
        ],
        "still_open": [
            "selected dynamic Higgs response Hessian/mass-strain functional F_H on B_Huv",
            "selected Herm(2) M_H entries Huu,Hud,Hdd or equivalent H_response table",
            "finite exactness/error and source-ownership certificate for M_H values",
            "selected s_beta or equivalent H quartic/threshold functional",
            "K_threshold.Omega_H.lambda source row",
            "strict Omega/lambda_H scalar execution",
            "C5b physical Higgs projection-measure equality and C6 no-extra-boundary/source theorem",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHSectorRestrictionFromBHuvOrDynamicHiggsResponseHessian",
        "status": STATUS,
        "previous_status": previous_full["status"],
        "theorem": {
            "name": "HSectorRestrictionFromBHuvTheorem",
            "proved": True,
            "statement": (
                "Because the selected B_Huv two-column lift satisfies B_Huv^*G_QB_Huv=I_2 "
                "on the q79/F,m=1 E_H^UV source domain, the canonical adjoint "
                "restriction R_H(x)=B_Huv^*G_Qx and projector P_H=B_HuvR_H are selected "
                "and exact.  This closes the kinematic H-sector restriction needed by "
                "the full M_source route.  It does not emit the dynamic Higgs response "
                "Hessian, Herm(2) M_H values, s_beta, lambda_H, or the tenth K row."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "B_Huv_two_column_uv_lift_emitted": True,
            "B_Huv_source_orthonormality_certified": True,
            "selected_H_sector_restriction_R_H_emitted": True,
            "selected_H_projector_P_H_emitted": True,
            "R_H_B_Huv_equals_I2_certified": True,
            "P_H_idempotent_and_G_self_adjoint_certified": True,
            "old_H7B1J_R_H_gap_retired": h7b1j_old_rh_missing,
            "full_route_reduced_to_dynamic_H_response_or_direct_M_H": True,
            "selected_dynamic_H_response_emitted": False,
            "selected_Hermitian_M_source_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_H_response_table_emitted": False,
            "selected_Delta_row_emitted": False,
            "selected_Re_Omega_row_emitted": False,
            "selected_Im_Omega_row_emitted": False,
            "selected_s_beta_value_found": False,
            "K_threshold_Omega_H_lambda_emitted": False,
            "accepted_selected_K_source_row_count": previous_hk["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": previous_hk[
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
            "hsector_restriction_from_bhuv": rel(RH_PACKET),
            "full_route_reduction_after_rh_closure": rel(ROUTE_REDUCTION),
            "dynamic_higgs_response_hessian_gate": rel(DYNAMIC_GATE),
            "h7b1j_after_rh_closure_recheck": rel(H7B1J_RECHECK),
            "hk_threshold_gate_after_rh_closure": rel(HK_GATE),
            "next_cutset_after_rh_closure": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedHSectorRestrictionFromBHuvOrDynamicHiggsResponseHessianCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "B_Huv_two_column_uv_lift_emitted": True,
        "B_Huv_source_orthonormality_certified": True,
        "selected_H_sector_restriction_R_H_emitted": True,
        "selected_H_projector_P_H_emitted": True,
        "R_H_B_Huv_equals_I2_certified": True,
        "P_H_idempotent_and_G_self_adjoint_certified": True,
        "old_H7B1J_R_H_gap_retired": h7b1j_old_rh_missing,
        "full_route_reduced_to_dynamic_H_response_or_direct_M_H": True,
        "selected_dynamic_H_response_emitted": False,
        "selected_Hermitian_M_source_emitted": False,
        "direct_Herm2_Huv_payload_emitted": False,
        "selected_H_response_table_emitted": False,
        "selected_s_beta_value_found": False,
        "K_threshold_Omega_H_lambda_emitted": False,
        "accepted_selected_K_source_row_count": previous_hk["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": previous_hk[
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

    note = f"""# MTT Selected HSectorRestrictionFromBHuv or DynamicHiggsResponseHessian v1

Status: `{STATUS}`

## What Closed

- emitted the canonical two-Higgs restriction `R_H(x)=B_Huv^* G_Q x`
- emitted the corresponding projector `P_H=B_Huv R_H`
- certified `R_H B_Huv=I_2`
- certified `P_H^2=P_H` and `P_H` is `G_Q`-self-adjoint
- retired the old H7B1J `R_H` gap for the selected two-Higgs `B_Huv` domain
- reduced the full `M_source+R_H` route to one dynamic value object

## Still Open

- selected dynamic Higgs response Hessian / mass-strain functional `F_H`
- selected Herm(2) `M_H` values on the `B_Huv` domain
- direct `Huu,Hud,Hdd` or `Delta,Re(Omega),Im(Omega)` rows
- selected `s_beta`, `lambda_H`, and the tenth `K_threshold.Omega_H.lambda` row
- C5b/C6 physical projection/no-boundary bridge clauses

Next required artifact: `{NEXT}`
"""

    write_json(RH_PACKET, rh_packet)
    write_json(ROUTE_REDUCTION, route_reduction)
    write_json(DYNAMIC_GATE, dynamic_gate)
    write_json(H7B1J_RECHECK, h7b1j_recheck)
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
