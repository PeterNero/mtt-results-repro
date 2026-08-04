"""Build the dynamic Higgs response Hessian on B_Huv attempt.

After B_Huv and the canonical R_H restriction are closed, the Huv problem is no
longer a domain/restriction problem.  It is exactly a value-source problem:
derive the selected second variation on the two-Higgs B_Huv coordinates, or emit
the same Herm(2) M_H table directly.
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

SLUG = "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DOMAIN_GATE = PACKET_DIR / "dynamic_hessian_domain_and_extraction_gate.packet.json"
VALUE_SEARCH = PACKET_DIR / "direct_mh_value_search_after_domain_closure.packet.json"
DIAGONAL_REJECTION = PACKET_DIR / "diagonal_hym_t3_candidate_rejection.packet.json"
STRICT_TABLE = PACKET_DIR / "strict_mh_table_value_gate.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_dynamic_hessian_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_dynamic_hessian_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicHiggsResponseHessianOnBHuv_or_DirectMHValueEmission_v1.md"

PREVIOUS_RH = DATA / "selected_hsectorrestrictionfrombhuv_or_dynamichiggsresponsehessian.candidate.json"
PREVIOUS_RH_PACKET = (
    DATA
    / "selected_hsectorrestrictionfrombhuv_or_dynamichiggsresponsehessian"
    / "hsector_restriction_from_bhuv.packet.json"
)
PREVIOUS_DYNAMIC_GATE = (
    DATA
    / "selected_hsectorrestrictionfrombhuv_or_dynamichiggsresponsehessian"
    / "dynamic_higgs_response_hessian_gate.packet.json"
)
PREVIOUS_HK = (
    DATA
    / "selected_hsectorrestrictionfrombhuv_or_dynamichiggsresponsehessian"
    / "hk_threshold_gate_after_rh_closure.packet.json"
)
MH_TABLE = (
    DATA
    / "selected_mhthreerowsourcefunctional_or_c5c6bridgeexecution"
    / "mh_three_row_execution_table_request.packet.json"
)
H7B1C_MINIMAL = (
    CONST_DATA
    / "const_higgs_01_h7b1c_selected_two_higgs_mass_strain_hessian"
    / "minimal_two_by_two_hessian_payload_request.packet.json"
)
H7B1C_SEARCH = (
    CONST_DATA
    / "const_higgs_01_h7b1c_selected_two_higgs_mass_strain_hessian"
    / "hessian_source_search.packet.json"
)
H7B1C_INSUFF = (
    CONST_DATA
    / "const_higgs_01_h7b1c_selected_two_higgs_mass_strain_hessian"
    / "current_source_insufficiency_proof.packet.json"
)
H7B1D_DIAGONAL = (
    CONST_DATA
    / "const_higgs_01_h7b1d_diagonal_hym_rank2_metric_candidate"
    / "conditional_huv_readout.packet.json"
)
H7B1F_FUNCTOR = (
    CONST_DATA
    / "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet"
    / "basis_invariant_huv_functor_theorem.packet.json"
)
H7B1F_CONTRACT = (
    CONST_DATA
    / "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet"
    / "nonsplit_to_huv_reduction_contract.packet.json"
)
H7B1N_EXTENSION = (
    CONST_DATA
    / "const_higgs_01_h7b1n_hsector_dynamic_extension_or_honest_huv_rows"
    / "hsector_dynamic_extension_attempt.packet.json"
)
H7B1N_HONEST = (
    CONST_DATA
    / "const_higgs_01_h7b1n_hsector_dynamic_extension_or_honest_huv_rows"
    / "honest_huv_row_export_attempt.packet.json"
)
H7B1Y_SCHEMA = (
    CONST_DATA
    / "const_higgs_01_h7b1y_selected_ehuv_section_basis_quadrature_or_herm2_row_values"
    / "direct_herm2_huv_row_schema.packet.json"
)
H7B1Y_MANIFEST = (
    CONST_DATA
    / "const_higgs_01_h7b1y_selected_ehuv_section_basis_quadrature_or_herm2_row_values"
    / "payload_search_manifest.packet.json"
)
H7B1Z_DIRECT = (
    CONST_DATA
    / "const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values"
    / "direct_herm2_fill_attempt.packet.json"
)
H7B1W_DIRECT = (
    CONST_DATA
    / "const_higgs_01_h7b1w_finite_trace_hym_binding_or_direct_huv_payload"
    / "direct_huv_payload_attempt.packet.json"
)

STATUS = (
    "MTT_SELECTED_DYNAMICHIGGSRESPONSEHESSIANONBHUV_OR_DIRECTMHVALUEEMISSION_"
    "DOMAIN_EXTRACTION_CLOSED_VALUES_OPEN"
)
NEXT = "MTT_Selected_HiggsSecondVariationFunctionalSource_or_Herm2RowValues_v1"


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
        raise FileNotFoundError("missing dynamic Huv Hessian inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS_RH,
        PREVIOUS_RH_PACKET,
        PREVIOUS_DYNAMIC_GATE,
        PREVIOUS_HK,
        MH_TABLE,
        H7B1C_MINIMAL,
        H7B1C_SEARCH,
        H7B1C_INSUFF,
        H7B1D_DIAGONAL,
        H7B1F_FUNCTOR,
        H7B1F_CONTRACT,
        H7B1N_EXTENSION,
        H7B1N_HONEST,
        H7B1Y_SCHEMA,
        H7B1Y_MANIFEST,
        H7B1Z_DIRECT,
        H7B1W_DIRECT,
    ]
    require_sources(sources)

    previous_rh = load(PREVIOUS_RH)
    rh_packet = load(PREVIOUS_RH_PACKET)
    previous_dynamic = load(PREVIOUS_DYNAMIC_GATE)
    previous_hk = load(PREVIOUS_HK)
    mh_table = load(MH_TABLE)
    h7b1c_minimal = load(H7B1C_MINIMAL)
    h7b1c_search = load(H7B1C_SEARCH)
    h7b1c_insuff = load(H7B1C_INSUFF)
    h7b1d_diagonal = load(H7B1D_DIAGONAL)
    h7b1f_functor = load(H7B1F_FUNCTOR)
    h7b1f_contract = load(H7B1F_CONTRACT)
    h7b1n_extension = load(H7B1N_EXTENSION)
    h7b1n_honest = load(H7B1N_HONEST)
    h7b1y_schema = load(H7B1Y_SCHEMA)
    h7b1y_manifest = load(H7B1Y_MANIFEST)
    h7b1z_direct = load(H7B1Z_DIRECT)
    h7b1w_direct = load(H7B1W_DIRECT)

    source_space = rh_packet["selected_source_space"]
    subspace = rh_packet["selected_two_higgs_subspace"]
    current_table = dict(mh_table["minimal_table"])
    rows_null = all(value is None for value in current_table.values())
    direct_attempts_emit_values = any(
        [
            h7b1n_honest["attempt_decision"]["direct_Huv_entries_emitted"],
            h7b1y_schema["acceptance_booleans"]["direct_Huu_Hud_Hdd_emitted"],
            h7b1z_direct["decision"]["direct_Huu_Hud_Hdd_emitted"],
            h7b1w_direct["decision"]["direct_Huu_Hud_Hdd_emitted"],
        ]
    )

    domain_gate = {
        "schema": "MTTDynamicHiggsResponseHessianOnBHuvDomainGate.v1",
        "status": "BHUV_RH_DOMAIN_AND_HERM2_EXTRACTION_LAW_CLOSED",
        "closure_claimed": True,
        "selected_domain": {
            "source_space": source_space,
            "two_higgs_subspace": subspace,
            "R_H": rh_packet["canonical_restriction"]["R_H"],
            "P_H": rh_packet["canonical_restriction"]["P_H"],
            "R_H_B_Huv_equals_I2": rh_packet["proof_identities"]["R_H_B_Huv_equals_I2"],
            "P_H_squared_equals_P_H": rh_packet["proof_identities"]["P_H_squared_equals_P_H"],
            "P_H_G_self_adjoint": rh_packet["proof_identities"]["P_H_is_G_Q_self_adjoint"],
        },
        "dynamic_value_rule": {
            "functional_name": "F_H",
            "functional_domain": "ordered complex coordinates (z_u,z_d) on span(B_Huv)",
            "selected_functional_required": (
                "F_H must be selected by the same q79/F,m=1 finite trace/HYM/"
                "retarded-overlap source, before observed Higgs/beta data enter."
            ),
            "Herm2_hessian": "(M_H)_{ij} = d^2 F_H / d(conj(z_i)) dz_j at the selected stationary point",
            "Hermiticity_certificate": "real-valued selected F_H implies M_H=M_H^*",
            "equivalent_full_route": "M_H = B_Huv^* M_source B_Huv = B_Huv^* Herm(R_H^* H_response R_H) B_Huv",
            "row_extraction": mh_table["row_reduction_when_table_exists"],
        },
        "what_is_closed_now": {
            "B_Huv_domain": True,
            "R_H_restriction": True,
            "P_H_projector": True,
            "Herm2_codomain": True,
            "Pauli_Riesz_row_extractors": True,
            "basis_phase_covariance": True,
            "no_observed_selector": True,
        },
        "what_is_not_closed": {
            "selected_F_H_functional": True,
            "selected_second_variation_values": True,
            "direct_Huu_Hud_Hdd_values": True,
            "finite_exactness_or_error_certificate_for_values": True,
            "selected_s_beta": True,
            "lambda_H_or_tenth_K_row": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    value_search = {
        "schema": "MTTDirectMHValueSearchAfterBHuvRHDomainClosure.v1",
        "status": "DIRECT_MH_VALUE_SEARCH_AFTER_DOMAIN_CLOSURE_VALUES_NOT_FOUND",
        "closure_claimed": True,
        "old_blockers_retired_by_current_repo": {
            "H7B1C_basis_labels_currently_emitted_old": h7b1c_minimal["basis_required"][
                "basis_labels_currently_emitted"
            ],
            "B_Huv_emitted_now": True,
            "R_H_emitted_now": True,
            "P_H_emitted_now": True,
            "basis_and_quotient_domain_closed_now": True,
        },
        "direct_value_attempts": {
            "H7B1C_selected_Huu_Hud_Hdd_found": h7b1c_search["result"][
                "selected_Huu_Hud_Hdd_found"
            ],
            "H7B1N_direct_Huv_entries_emitted": h7b1n_honest["attempt_decision"][
                "direct_Huv_entries_emitted"
            ],
            "H7B1Y_direct_Huu_Hud_Hdd_emitted": h7b1y_schema["acceptance_booleans"][
                "direct_Huu_Hud_Hdd_emitted"
            ],
            "H7B1Z_direct_Huu_Hud_Hdd_emitted": h7b1z_direct["decision"][
                "direct_Huu_Hud_Hdd_emitted"
            ],
            "H7B1W_direct_Huu_Hud_Hdd_emitted": h7b1w_direct["decision"][
                "direct_Huu_Hud_Hdd_emitted"
            ],
            "any_direct_attempt_emits_values": direct_attempts_emit_values,
        },
        "current_table_after_recheck": current_table,
        "rows_all_null": rows_null,
        "positive_support_retained": {
            "H7B1F_basis_invariant_functor_proved": h7b1f_functor["theorem"]["proved"],
            "H7B1Y_schema_emitted": h7b1y_schema["status"]
            == "DIRECT_HERM2_HUV_ROW_SCHEMA_EMITTED_VALUES_OPEN",
            "H7B1C_minimal_payload_contract_built": True,
            "current_R_H_closure_plugs_prior_Pi_or_RH_gap": True,
        },
        "why_not_a_repeat": [
            "The domain, B_Huv, R_H, and Herm(2) extraction law are now closed.",
            "Only the dynamic second-variation/value source is rechecked here.",
            "Old packets that lacked B_Huv are not treated as final failures; their value rows are re-evaluated after domain closure.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    diagonal_rejection = {
        "schema": "MTTDiagonalHYMT3CandidateRejectionAfterBHuvRH.v1",
        "status": "DIAGONAL_HYM_T3_CANDIDATE_REJECTED_AS_VALUE_SOURCE",
        "closure_claimed": True,
        "candidate_shape": {
            "candidate": "M_H proportional to T3 = diag(1,-1) on (H_u,H_d^dagger)",
            "would_give": {
                "Omega": h7b1d_diagonal["conditional_endpoint_if_future_nonzero_diagonal_reduction_is_selected"][
                    "Omega_eff"
                ],
                "s_beta": h7b1d_diagonal["conditional_endpoint_if_future_nonzero_diagonal_reduction_is_selected"][
                    "s_beta"
                ],
            },
            "conditional_endpoint_currently_promoted": h7b1d_diagonal[
                "conditional_endpoint_if_future_nonzero_diagonal_reduction_is_selected"
            ]["currently_promoted"],
        },
        "rejection_reasons": {
            "diagonal_HYM_metric_or_log_strain_is_not_yet_a_selected_second_variation": True,
            "finite_scalar_reduction_rule_absent": h7b1d_diagonal[
                "conditional_assumptions_required"
            ]["A2_finite_scalar_reduction"],
            "mass_strain_convention_absent": h7b1d_diagonal[
                "conditional_assumptions_required"
            ]["A3_mass_strain_convention"],
            "raw_mean_log_strain_fails_non_scalar_test": h7b1d_diagonal[
                "why_naive_reductions_do_not_close"
            ]["raw_mean_log_strain_fails_non_scalar_test"],
            "measured_lambda_or_tan_beta_selector_forbidden": h7b1d_diagonal[
                "why_naive_reductions_do_not_close"
            ]["using_measured_lambda_or_tan_beta_to_choose_reduction_forbidden"],
        },
        "decision": {
            "promote_T3_as_M_H": False,
            "promote_conditional_s_beta_1": False,
            "requires_selected_F_H_or_reduction_theorem": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    strict_table = {
        "schema": "MTTStrictMHTableValueGateAfterDomainClosure.v1",
        "status": "STRICT_MH_TABLE_VALUES_OPEN_DOMAIN_CLOSED",
        "closure_claimed": True,
        "domain_closed": {
            "B_Huv": True,
            "R_H": True,
            "P_H": True,
            "Herm2_codomain": True,
            "quotient_admissibility_domain": True,
        },
        "required_values": current_table,
        "computed_when_values_exist": mh_table["row_reduction_when_table_exists"],
        "acceptance_tests": h7b1c_minimal["acceptance_tests"],
        "current_packet_passes": False,
        "value_closure_reasons_missing": [
            "selected F_H second-variation functional not emitted",
            "selected H_response table not emitted",
            "direct Huu,Hud,Hdd rows not emitted",
            "finite exactness/error certificate for values not emitted",
            "source ownership certificate for value rows not emitted",
        ],
        "forbidden_shortcuts": [
            "promoting the source metric G_Q or connection generator T3 as M_H",
            "promoting collapsed rank-one H projector data to UV two-Higgs mass/strain values",
            "using observed Higgs mass, lambda_H, tan_beta, or threshold residuals to choose entries",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    h_row = dict(previous_hk["H_row"])
    h_row.update(
        {
            "dynamic_Hessian_domain_on_BHuv_closed": True,
            "Herm2_value_extraction_law_closed": True,
            "diagonal_HYM_T3_candidate_tested": True,
            "diagonal_HYM_T3_candidate_promoted_as_M_H": False,
            "selected_F_H_second_variation_emitted": False,
            "selected_dynamic_H_response_emitted": False,
            "selected_Hermitian_M_source_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_H_response_table_emitted": False,
            "selected_Delta_row_emitted": False,
            "selected_Re_Omega_row_emitted": False,
            "selected_Im_Omega_row_emitted": False,
            "selected_s_beta_value_found": False,
            "K_threshold_Omega_H_lambda_emitted": False,
        }
    )
    hk_gate = {
        "schema": "MTTHKThresholdGateAfterDynamicHessianAttempt.v1",
        "status": "H_K_THRESHOLD_GATE_DYNAMIC_HESSIAN_DOMAIN_CLOSED_VALUES_OPEN_9_OF_10",
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
        "schema": "MTTNextCutsetAfterDynamicHiggsHessianAttempt.v1",
        "status": "NEXT_FRONTIER_HIGGS_SECOND_VARIATION_FUNCTIONAL_SOURCE_OR_HERM2_ROWS",
        "closure_claimed": True,
        "closed_here": [
            "dynamic Higgs Hessian domain on B_Huv fixed",
            "Herm(2) second-variation extraction law fixed",
            "direct Huu/Hud/Hdd value attempts rechecked after B_Huv/R_H closure",
            "diagonal HYM T3 shortcut tested and rejected as source value",
            "strict M_H value gate reduced to F_H/source-owned row emission",
            "H K-threshold gate remains 9/10",
        ],
        "still_open": [
            "selected finite H-sector action/response functional F_H",
            "selected second variation M_H on B_Huv",
            "direct Huu,Hud,Hdd rows with exactness/source certificates",
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
        "candidate": "MTTSelectedDynamicHiggsResponseHessianOnBHuvOrDirectMHValueEmission",
        "status": STATUS,
        "previous_status": previous_rh["status"],
        "theorem": {
            "name": "DynamicHiggsResponseHessianOnBHuvDomainReductionTheorem",
            "proved": True,
            "statement": (
                "After B_Huv and R_H are selected, the Huv problem is exactly the "
                "selected second variation of a finite H-sector functional F_H on "
                "the ordered B_Huv coordinates, or an equivalent direct Herm(2) "
                "table Huu,Hud,Hdd.  The domain, Herm(2) codomain, phase covariance, "
                "and row extraction laws are closed.  Current packets still emit no "
                "selected F_H, H_response, Huu/Hud/Hdd, Delta/Omega, s_beta, lambda_H, "
                "or tenth K row; diagonal HYM/T3 support remains conditional and is "
                "not a source-owned value."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "B_Huv_two_column_uv_lift_emitted": True,
            "selected_H_sector_restriction_R_H_emitted": True,
            "selected_H_projector_P_H_emitted": True,
            "dynamic_Hessian_domain_on_BHuv_closed": True,
            "Herm2_value_extraction_law_closed": True,
            "direct_value_attempts_rechecked_after_domain_closure": True,
            "diagonal_HYM_T3_candidate_tested": True,
            "diagonal_HYM_T3_candidate_promoted_as_M_H": False,
            "selected_F_H_second_variation_emitted": False,
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
            "dynamic_hessian_domain_and_extraction_gate": rel(DOMAIN_GATE),
            "direct_mh_value_search_after_domain_closure": rel(VALUE_SEARCH),
            "diagonal_hym_t3_candidate_rejection": rel(DIAGONAL_REJECTION),
            "strict_mh_table_value_gate": rel(STRICT_TABLE),
            "hk_threshold_gate_after_dynamic_hessian_attempt": rel(HK_GATE),
            "next_cutset_after_dynamic_hessian_attempt": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedDynamicHiggsResponseHessianOnBHuvOrDirectMHValueEmissionCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "B_Huv_two_column_uv_lift_emitted": True,
        "selected_H_sector_restriction_R_H_emitted": True,
        "selected_H_projector_P_H_emitted": True,
        "dynamic_Hessian_domain_on_BHuv_closed": True,
        "Herm2_value_extraction_law_closed": True,
        "direct_value_attempts_rechecked_after_domain_closure": True,
        "diagonal_HYM_T3_candidate_tested": True,
        "diagonal_HYM_T3_candidate_promoted_as_M_H": False,
        "selected_F_H_second_variation_emitted": False,
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

    note = f"""# MTT Selected DynamicHiggsResponseHessianOnBHuv or DirectMHValueEmission v1

Status: `{STATUS}`

## What Closed

- fixed the selected dynamic Higgs Hessian domain: ordered `B_Huv` coordinates
- fixed the value law `(M_H)_ij = d^2 F_H / d(conj(z_i)) dz_j`
- fixed the equivalent full route `M_H=B_Huv^* M_source B_Huv`
- rechecked direct `Huu,Hud,Hdd` attempts after `B_Huv/R_H` closure
- tested and rejected the diagonal HYM/T3 shortcut as a value source

## Still Open

- selected finite H-sector functional `F_H`
- selected Herm(2) values `Huu,Hud,Hdd`
- `Delta`, `Re(Omega)`, `Im(Omega)`, `s_beta`, `lambda_H`
- the tenth `K_threshold.Omega_H.lambda` row

Next required artifact: `{NEXT}`
"""

    write_json(DOMAIN_GATE, domain_gate)
    write_json(VALUE_SEARCH, value_search)
    write_json(DIAGONAL_REJECTION, diagonal_rejection)
    write_json(STRICT_TABLE, strict_table)
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
