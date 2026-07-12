"""Build CONST-HIGGS-01 H7B1N H-sector dynamic extension / Huv rows gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY_REPO = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1n_hsector_dynamic_extension_or_honest_huv_rows"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
HSECTOR_EXTENSION = BASE / "hsector_dynamic_extension_attempt.packet.json"
HUV_ROWS = BASE / "honest_huv_row_export_attempt.packet.json"
CUTSET = BASE / "nonlinear_hym_huv_payload_cutset.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1N_HSectorDynamicExtensionOrHonestHuvRows_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1N_TWO_ROUTE_TEST_BUILT_NONLINEAR_HYM_HUV_PAYLOAD_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def clean_flags() -> dict[str, bool]:
    return {
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    h7b1m_path = DATA / "const_higgs_01_h7b1m_c1_to_huv_projection_or_honest_huv_row_export.candidate.json"
    h7b1m_audit_path = DATA / "const_higgs_01_h7b1m_c1_to_huv_projection_or_honest_huv_row_export" / "c1_target_sector_support_audit.packet.json"
    h7b1c_request_path = DATA / "const_higgs_01_h7b1c_selected_two_higgs_mass_strain_hessian" / "minimal_two_by_two_hessian_payload_request.packet.json"
    h7b1d_conditional_path = DATA / "const_higgs_01_h7b1d_diagonal_hym_rank2_metric_candidate" / "conditional_huv_readout.packet.json"
    h7b1f_contract_path = DATA / "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet" / "nonsplit_to_huv_reduction_contract.packet.json"
    h7b1f_functor_path = DATA / "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet" / "basis_invariant_huv_functor_theorem.packet.json"
    h7b1g_support_path = DATA / "const_higgs_01_h7b1g_fill_bhuv_or_msource" / "support_split_theorem.packet.json"
    h7b1g_attempt_path = DATA / "const_higgs_01_h7b1g_fill_bhuv_or_msource" / "current_fill_attempt.packet.json"
    h7b1h_decision_path = DATA / "const_higgs_01_h7b1h_nearhit_source_export_audit" / "source_export_route_decision.packet.json"
    h7b1h_valpha_rejection_path = DATA / "const_higgs_01_h7b1h_nearhit_source_export_audit" / "conditional_valpha_msource_rejection.packet.json"
    ext_overlap_path = SM_PARITY_REPO / "candidate_data" / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"

    h7b1m = load(h7b1m_path)
    h7b1m_audit = load(h7b1m_audit_path)
    h7b1c_request = load(h7b1c_request_path)
    h7b1d_conditional = load(h7b1d_conditional_path)
    h7b1f_contract = load(h7b1f_contract_path)
    h7b1f_functor = load(h7b1f_functor_path)
    h7b1g_support = load(h7b1g_support_path)
    h7b1g_attempt = load(h7b1g_attempt_path)
    h7b1h_decision = load(h7b1h_decision_path)
    h7b1h_valpha_rejection = load(h7b1h_valpha_rejection_path)
    ext_overlap = load(ext_overlap_path)

    c1_target = h7b1m_audit["c1_response_target"]
    c1_sectors = c1_target["sector_norm_sq_keys"]
    h_required_basis = h7b1c_request["basis_required"]["ordered_basis"]

    hsector_extension = {
        "schema": "MTTConstHiggs01H7B1NHSectorDynamicExtensionAttempt.v1",
        "status": "HSECTOR_DYNAMIC_C1_EXTENSION_NOT_EMITTED_CURRENT_CORPUS",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1N-A-HSECTOR-DYNAMIC-EXTENSION",
        "input_sources": {
            "H7B1M_candidate": rel(h7b1m_path),
            "H7B1M_C1_target_audit": rel(h7b1m_audit_path),
            "H7B1C_Huv_payload_request": rel(h7b1c_request_path),
            "H7B1F_Huv_reduction_contract": rel(h7b1f_contract_path),
        },
        "current_dynamic_c1_target": {
            "sector_set": c1_sectors,
            "inferred_real_dimension": c1_target["inferred_real_dimension"],
            "contains_H_sector": c1_target["contains_H_sector"],
            "contains_Hu_sector": c1_target["contains_Hu_sector"],
            "contains_Hd_dagger_sector": c1_target["contains_Hd_dagger_sector"],
            "selected_A_selected_emitted": c1_target["selected_A_selected_emitted"],
            "selected_b_selected_emitted": c1_target["selected_b_selected_emitted"],
            "conditional_Gram_exact": c1_target["conditional_Gram_exact"],
        },
        "required_extension_payload": {
            "extend_target_with_H_or_Huv_rows": True,
            "ordered_UV_basis": h_required_basis,
            "emit_Pi_Huv_or_R_H": True,
            "emit_H_response_on_Huv": True,
            "emit_Hermitian_Huv_mass_strain_entries": True,
            "emit_exactness_or_error_certificate": True,
            "emit_coefficient_normalization_convention": True,
        },
        "attempt_decision": {
            "H_sector_dynamic_extension_found": False,
            "selected_Pi_Huv_or_R_H_found": False,
            "H_response_found": False,
            "route_A_passes": False,
            "reason": "The available dynamic C1 target remains the matter-sector u,d,e,nuD target. No current packet extends it with H/Huv rows or emits a C1-to-Huv codomain map.",
        },
        **clean_flags(),
    }

    honest_huv_rows = {
        "schema": "MTTConstHiggs01H7B1NHonestHuvRowExportAttempt.v1",
        "status": "HONEST_HUV_ROW_EXPORT_NOT_EMITTED_CURRENT_CORPUS",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1N-B-HONEST-HUV-ROW-EXPORT",
        "input_sources": {
            "H7B1C_Huv_payload_request": rel(h7b1c_request_path),
            "H7B1D_conditional_diagonal_readout": rel(h7b1d_conditional_path),
            "H7B1F_Huv_reduction_contract": rel(h7b1f_contract_path),
            "H7B1F_basis_invariant_functor": rel(h7b1f_functor_path),
            "H7B1G_support_split": rel(h7b1g_support_path),
            "H7B1G_current_fill_attempt": rel(h7b1g_attempt_path),
            "H7B1H_source_export_route_decision": rel(h7b1h_decision_path),
            "H7B1H_conditional_valpha_rejection": rel(h7b1h_valpha_rejection_path),
            "selected_ext_overlap_hym_hodge_projector_table": rel(ext_overlap_path),
        },
        "B_Huv_side": {
            "support_closed": h7b1g_support["bhuv_support"]["support_closed"],
            "value_emitted": h7b1g_support["bhuv_support"]["value_emitted"],
            "still_missing_for_B_Huv": h7b1g_support["bhuv_support"]["still_missing_for_B_Huv"],
            "current_attempt_value_emitted": h7b1g_attempt["attempted_routes"]["route_A_fill_B_Huv"]["value_emitted"],
        },
        "M_source_side": {
            "support_closed": h7b1g_support["msource_support"]["support_closed"],
            "value_emitted": h7b1g_support["msource_support"]["value_emitted"],
            "still_missing_for_M_source": h7b1g_support["msource_support"]["still_missing_for_M_source"],
            "current_attempt_value_emitted": h7b1g_attempt["attempted_routes"]["route_B_fill_M_source"]["value_emitted"],
            "conditional_valpha_promoted_to_M_source": h7b1h_valpha_rejection["promotion_decision"]["conditional_valpha_promoted_to_M_source"],
        },
        "direct_Huv_rows": {
            "basis_labels_currently_emitted": h7b1c_request["basis_required"]["basis_labels_currently_emitted"],
            "matrix_values_currently_emitted": h7b1c_request["matrix_required"]["values_currently_emitted"],
            "Huu": h7b1c_request["matrix_required"]["Huu"],
            "Hud": h7b1c_request["matrix_required"]["Hud"],
            "Hdd": h7b1c_request["matrix_required"]["Hdd"],
            "current_packet_passes": h7b1c_request["current_packet_passes"],
        },
        "conditional_diagonal_HYM_support": {
            "conditional_endpoint_s_beta": h7b1d_conditional["conditional_endpoint_if_future_nonzero_diagonal_reduction_is_selected"]["s_beta"],
            "currently_promoted": h7b1d_conditional["conditional_endpoint_if_future_nonzero_diagonal_reduction_is_selected"]["currently_promoted"],
            "requires_binding_and_reduction": True,
            "raw_mean_log_strain_fails_non_scalar_test": h7b1d_conditional["why_naive_reductions_do_not_close"]["raw_mean_log_strain_fails_non_scalar_test"],
        },
        "nonlinear_HYM_support": {
            "row_level_harmonic_seed_closed": ext_overlap["HYM_correction_status"]["row_level_harmonic_seed_closed"],
            "transition_overlap_table_closed": ext_overlap["transition_overlap_table"]["closed"],
            "Hodge_Lambda_row_table_closed": ext_overlap["newton_readiness"]["Hodge_Lambda_row_table_closed"],
            "gauge_projector_row_closed": ext_overlap["newton_readiness"]["gauge_projector_row_closed"],
            "nonlinear_HYM_connection_correction_closed": ext_overlap["HYM_correction_status"]["nonlinear_non_split_HYM_metric_correction_closed"],
            "next_equation": ext_overlap["HYM_correction_status"]["next_equation"],
        },
        "attempt_decision": {
            "B_Huv_emitted": False,
            "M_source_emitted": False,
            "direct_Huv_entries_emitted": False,
            "route_B_passes": False,
            "reason": "Current support closes labels, quotient contracts, Ext/Hodge/projector rows, and conditional diagonal readout, but no same-source B_Huv, M_source, or direct Huv entries are emitted.",
        },
        **clean_flags(),
    }

    cutset = {
        "schema": "MTTConstHiggs01H7B1NNonlinearHYMHuvPayloadCutset.v1",
        "status": "MINIMAL_CUTSET_NONLINEAR_HYM_CORRECTION_OR_DIRECT_HUV_ROWS",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1N-CUTSET",
        "cutset_theorem": {
            "name": "H7B1NTwoRouteCutsetTheorem",
            "proved": True,
            "statement": (
                "Given H7B1M, the existing 72-real C1 target cannot supply Huv rows. "
                "Given H7B1G/H7B1H and the Ext/Hodge table, the current V_alpha/Route-C branch supplies support and a nonlinear HYM equation but not B_Huv, M_source, or direct Huv entries. "
                "Therefore the broad H7B1N gate is closed to a minimal cutset: solve the selected nonlinear HYM/Huv row payload or emit direct source-owned Huv rows."
            ),
        },
        "minimal_payload_to_close": {
            "route_A_Hsector_dynamic_extension": [
                "selected H/Huv response rows extending the current C1 target",
                "Pi_Huv or R_H codomain map to ordered (H_u,H_d^dagger)",
                "Huv Hermitian mass-strain entries and exactness certificate",
            ],
            "route_B_nonlinear_HYM_or_direct_rows": [
                "solve Lambda(F_{A_split + eta_00^unit + a_HYM})_0=0 with Coulomb gauge d_A^* a_HYM=0 in the selected End0 basis",
                "emit nonlinear HYM correction coefficients or an equivalent Hermitian M_source",
                "emit B_Huv or direct Huv entries in ordered (H_u,H_d^dagger)",
                "attach finite residual/truncation/source certificate",
            ],
        },
        "closed_as_nonstarters": {
            "existing_72_real_C1_target_as_Huv_source": True,
            "rank_one_H_projector_as_B_Huv": True,
            "conditional_diagonal_readout_as_value": True,
            "conditional_valpha_validator_as_M_source": True,
            "raw_mean_log_strain_reduction": True,
            "observed_lambda_beta_threshold_backsolve": True,
        },
        "strict_outputs": {
            "H_response": None,
            "Pi_Huv": None,
            "R_H": None,
            "B_Huv": None,
            "M_source": None,
            "Huv": None,
            "Delta": None,
            "Omega": None,
            "s_beta": None,
            "lambda_H": None,
        },
        "passes": False,
        **clean_flags(),
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1NNextWork.v1",
        "status": "NEXT_WORKORDER_H7B1O_NONLINEAR_HYM_CORRECTION_OR_DIRECT_HUV_ROWS",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1N-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1O-NONLINEAR-HYM-CORRECTION-OR-DIRECT-HUV-ROWS",
            "task": "Build the selected nonlinear HYM correction coefficient solve for the V_alpha/eta_00 branch, or emit direct source-owned Huv rows with exactness.",
        },
        "two_legal_exits": [
            {
                "id": "H7B1O-A",
                "label": "nonlinear HYM correction to Huv",
                "must_emit": "a_HYM coefficients or equivalent M_source plus B_Huv/direct Huv entries and residual certificate",
            },
            {
                "id": "H7B1O-B",
                "label": "direct honest Huv rows",
                "must_emit": "Huu,Hud,Hdd in the ordered (H_u,H_d^dagger) basis with source ids and exactness/error certificate",
            },
        ],
        "do_not_repeat": [
            "Do not reuse the current 72-real matter-sector C1 target as Huv.",
            "Do not promote conditional diagonal HYM readout or V_alpha validator success as selected rows.",
            "Do not use rank-one H:h0 as B_Huv.",
            "Do not backsolve from Higgs mass, lambda_H, beta, threshold residual, Yukawas, CKM, or PMNS.",
        ],
        **clean_flags(),
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1NHSectorDynamicExtensionOrHonestHuvRows",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1N-HSECTOR-DYNAMIC-EXTENSION-OR-HONEST-HUV-ROWS",
        "output_packets": {
            "hsector_dynamic_extension_attempt": rel(HSECTOR_EXTENSION),
            "honest_huv_row_export_attempt": rel(HUV_ROWS),
            "nonlinear_hym_huv_payload_cutset": rel(CUTSET),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": cutset["cutset_theorem"],
        "H7B1M_gate_imported": h7b1m["plain_C1_to_Huv_projection_route_retired_current_target"],
        "Hsector_dynamic_extension_found": False,
        "honest_Huv_row_export_found": False,
        "nonlinear_HYM_seed_support_closed": True,
        "nonlinear_HYM_correction_closed": False,
        "broad_H7B1N_gate_reduced_to_minimal_cutset": True,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "direct_Huv_entries_emitted": False,
        "selected_offdiagonal_Omega_found": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1O_NonlinearHYMCorrectionOrDirectHuvRows_v1",
        **clean_flags(),
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1N_HSectorDynamicExtensionOrHonestHuvRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "Hsector_dynamic_extension_found": False,
        "honest_Huv_row_export_found": False,
        "nonlinear_HYM_seed_support_closed": True,
        "nonlinear_HYM_correction_closed": False,
        "broad_H7B1N_gate_reduced_to_minimal_cutset": True,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "direct_Huv_entries_emitted": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    note = f"""# MTT CONST HIGGS 01 H7B1N H-Sector Dynamic Extension Or Honest Huv Rows v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1N-HSECTOR-DYNAMIC-EXTENSION-OR-HONEST-HUV-ROWS`

## Result

```text
H-sector dynamic C1 extension found       False
honest Huv row export found              False
nonlinear HYM seed support closed         True
nonlinear HYM correction closed           False
broad H7B1N gate reduced to cutset        True
Huv / Omega / s_beta / lambda_H           False
```

## What Closed

The broad H7B1N search is now closed to a minimal cutset.  The existing C1
target has no Huv codomain, and the direct Huv route has no emitted `B_Huv`,
`M_source`, or direct `Huu,Hud,Hdd` rows.

The strongest live support is the selected `V_alpha/eta_00` Ext/Hodge row:
the harmonic row, transition overlap table, Hodge/Lambda row, and gauge
projector row are closed.  The nonlinear HYM correction coefficients are not.

## Remaining Exact Payload

Either:

- solve the selected nonlinear HYM correction and reduce it to `M_source` /
  `B_Huv` / `Huv`, or
- emit direct source-owned Huv rows with exactness certificates.

Next label:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1O-NONLINEAR-HYM-CORRECTION-OR-DIRECT-HUV-ROWS`
"""

    for path, payload in [
        (HSECTOR_EXTENSION, hsector_extension),
        (HUV_ROWS, honest_huv_rows),
        (CUTSET, cutset),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
