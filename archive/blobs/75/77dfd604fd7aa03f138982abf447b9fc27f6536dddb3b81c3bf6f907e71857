"""Build CONST-HIGGS-01 H7B1D diagonal HYM rank-2 metric candidate."""

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

SLUG = "const_higgs_01_h7b1d_diagonal_hym_rank2_metric_candidate"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT_PACKET = BASE / "diagonal_hym_rank2_import.packet.json"
CONDITIONAL_READOUT = BASE / "conditional_huv_readout.packet.json"
NONPROMOTION = BASE / "strict_nonpromotion_proof.packet.json"
PROMOTION_CONTRACT = BASE / "promotion_contract.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1D_DiagonalHYMRank2MetricCandidate_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1D_DIAGONAL_HYM_RANK2_CANDIDATE_CONDITIONAL_NOT_PROMOTED"


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


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    h7b1c_path = DATA / "const_higgs_01_h7b1c_selected_two_higgs_mass_strain_hessian.candidate.json"
    h7b1c_payload_path = DATA / "const_higgs_01_h7b1c_selected_two_higgs_mass_strain_hessian" / "minimal_two_by_two_hessian_payload_request.packet.json"
    diagonal_operator_path = SM_PARITY_REPO / "candidate_data" / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json"
    diagonal_replay_path = SM_PARITY_REPO / "candidate_data" / "selected_full_exps_hym_newton_replay.candidate.json"
    transported_trace_path = SM_PARITY_REPO / "candidate_data" / "selected_gauge_transported_bn_phifin_trace.candidate.json"
    projector_values_path = SM_PARITY_REPO / "candidate_data" / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"

    h7b1c = load(h7b1c_path)
    h7b1c_payload = load(h7b1c_payload_path)
    diagonal_operator = load(diagonal_operator_path)
    diagonal_replay = load(diagonal_replay_path)
    transported_trace = load(transported_trace_path)
    projector_values = load(projector_values_path)

    diag_metric = diagonal_operator["diagonal_metric_payload"]
    diag_connection = diagonal_operator["diagonal_connection_payload"]
    solution = diagonal_replay["solution_summary"]
    h_slot = transported_trace["transported_trace"]["sector_slots"]["H"]
    h_projector_slot = projector_values["finite_value_payload"]["sector_slots"]["H"]

    u_l2 = float(solution["u_l2"])
    u_mean_abs = float(solution["u_mean_abs"])
    u_min = float(solution["u_min"])
    u_max = float(solution["u_max"])
    final_residual = float(solution["final_residual_l2"])

    diagonal_import = {
        "schema": "MTTConstHiggs01H7B1DDiagonalHYMRank2Import.v1",
        "status": "DIAGONAL_HYM_RANK2_METRIC_IMPORTED_NOT_HUV",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1D-DIAGONAL-HYM-RANK2-IMPORT",
        "sources": {
            "h7b1c_minimal_payload": rel(h7b1c_payload_path),
            "diagonal_operator_payload": rel(diagonal_operator_path),
            "diagonal_expS_replay": rel(diagonal_replay_path),
            "gauge_transported_trace": rel(transported_trace_path),
            "projector_value_emission": rel(projector_values_path),
        },
        "rank2_diagonal_HYM_metric": {
            "found": True,
            "metric": diag_metric["H_diagonal"],
            "determinant": diag_metric["determinant"],
            "closed": diag_metric["closed"],
            "selected_end0_direction": diagonal_replay["coefficient_packet"]["selected_end0_direction"],
            "connection_form": diag_connection["connection_form"],
            "residual_l2": final_residual,
            "u_l2": u_l2,
            "u_min": u_min,
            "u_max": u_max,
            "u_mean_abs": u_mean_abs,
            "nonzero_rank2_strain": u_l2 > 0,
            "continuous_parameters_added": diagonal_replay["coefficient_packet"]["continuous_parameters_added"],
        },
        "why_this_is_not_yet_Huv": {
            "H7B1C_requires_ordered_basis": h7b1c_payload["basis_required"]["ordered_basis"],
            "diagonal_payload_basis": "selected End0(V_alpha) rank-2 diagonal HYM lane, not emitted as (H_u,H_d^dagger)",
            "H_sector_currently_rank": h_slot["rank_preserved"],
            "H_sector_model_basis_indices": h_slot["model_basis_indices"],
            "H_sector_transport": h_slot["transport"],
            "H_projector_carrier_kind": h_projector_slot["carrier_kind"],
            "H_projector_selected_source_verified": h_projector_slot["selected_source_verified"],
            "finite_Huv_scalar_reduction_emitted": False,
        },
        "emits_finite_Huv_2x2_block": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    conditional_readout = {
        "schema": "MTTConstHiggs01H7B1DConditionalHuvReadout.v1",
        "status": "CONDITIONAL_DIAGONAL_READOUT_BUILT_REQUIRES_BINDING_AND_REDUCTION",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1D-CONDITIONAL-HUV-READOUT",
        "conditional_assumptions_required": {
            "A1_two_Higgs_basis_binding": "same selected source identifies the two diagonal HYM lines with ordered (H_u,H_d^dagger)",
            "A2_finite_scalar_reduction": "same selected source emits a reduction functional from the pointwise/log metric to scalar Huu,Hud,Hdd",
            "A3_mass_strain_convention": "same selected source says whether the Hessian is the log-strain S=diag(u,-u), the metric H=diag(exp(u),exp(-u)), or a second variation derived from it",
            "A4_global_light_line_policy": "same selected source proves the light line is quotient-admissible and globally selected, including any u sign/zero-set issue",
        },
        "if_log_strain_S_is_selected_pointwise": {
            "S_uv": "diag(u,-u)",
            "Delta_pointwise": "u",
            "Omega_pointwise": 0,
            "u_l2_positive": u_l2 > 0,
            "pointwise_s_beta_where_nonzero": 1,
            "not_a_finite_scalar_packet": True,
        },
        "why_naive_reductions_do_not_close": {
            "raw_zero_mode_mean_of_u": "mean(u)=0 by trace-free constraint",
            "u_mean_abs": u_mean_abs,
            "raw_mean_log_strain_Delta_eff": 0,
            "raw_mean_log_strain_fails_non_scalar_test": True,
            "metric_average_or_norm_reduction_requires_source_rule": True,
            "using_measured_lambda_or_tan_beta_to_choose_reduction_forbidden": True,
        },
        "conditional_endpoint_if_future_nonzero_diagonal_reduction_is_selected": {
            "Omega_eff": 0,
            "Delta_eff_required_nonzero": True,
            "s_beta": 1,
            "interpretation": "oriented two-Higgs split endpoint, not a fitted beta angle",
            "currently_promoted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    nonpromotion = {
        "schema": "MTTConstHiggs01H7B1DStrictNonPromotionProof.v1",
        "status": "STRICT_PROMOTION_TO_HUV_FAILS_CURRENTLY",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1D-STRICT-NONPROMOTION-PROOF",
        "proof_steps": [
            "H7B1C accepts only a same-source finite 2x2 Hermitian packet on the ordered UV basis (H_u,H_d^dagger).",
            "The diagonal HYM replay emits a rank-2 metric diag(exp(u),exp(-u)) in the selected End0(V_alpha) diagonal lane.",
            "The same transported-trace packet still treats the Higgs sector itself as a rank-one trivial Higgs singlet with identity transport.",
            "The projector value packet emits model-active H projectors but leaves selected_source_verified false.",
            "No same-source theorem binds the rank-2 diagonal HYM lines to H_u/H_d^dagger.",
            "No same-source theorem emits a finite scalar reduction from the pointwise diagonal strain u to Huu,Hud,Hdd.",
            "The naive mean of log strain is zero by construction, so it cannot supply a non-scalar H_uv packet.",
        ],
        "conclusion": {
            "diagonal_rank2_support_found": True,
            "selected_Huv_basis_binding_found": False,
            "selected_finite_reduction_found": False,
            "selected_Huu_Hud_Hdd_found": False,
            "selected_Delta_Omega_found": False,
            "selected_s_beta_found": False,
            "numeric_lambda_H_derived": False,
            "strict_no_knob_Higgs_closure": False,
        },
        "no_regression_from_H7B1C": {
            "minimal_payload_still_valid": h7b1c["minimal_Huv_hessian_payload_request_built"],
            "current_source_insufficiency_still_valid": h7b1c["current_source_insufficiency_proved"],
            "new_information_added": "a same-branch diagonal HYM rank-2 candidate is identified, but strict promotion conditions are now explicit",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    promotion_contract = {
        "schema": "MTTConstHiggs01H7B1DPromotionContract.v1",
        "status": "TWO_PROMOTION_EXITS_DEFINED_FOR_H7B1E",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1D-PROMOTION-CONTRACT",
        "legal_exits": [
            {
                "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1E-DIAGONAL-HYM-TO-HUV-BINDING-THEOREM",
                "route": "straight/superset diagonal HYM route",
                "must_emit": [
                    "source binding of the two diagonal HYM lines to (H_u,H_d^dagger)",
                    "finite scalar reduction R_HYM->H_uv",
                    "mass/strain convention",
                    "quotient-admissible global light line",
                ],
                "conditional_readout_if_nonzero_diagonal": "Omega=0 and s_beta=1",
                "currently_closed": False,
            },
            {
                "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1E-OFFDIAGONAL-EXT-OMEGA-SOURCE",
                "route": "off-diagonal extension/Strominger route",
                "must_emit": [
                    "same-source off-diagonal Higgs mixing Omega",
                    "finite Huu/Hdd diagonal terms or proof they cancel",
                    "quotient-admissible light projector P_L",
                ],
                "conditional_readout_if_filled": "s_beta=Delta^2/(Delta^2+|Omega|^2)",
                "currently_closed": False,
            },
            {
                "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B2-SELECTED-EW-BOUNDARY-RG-PACKET",
                "route": "parallel necessary gauge/RG route",
                "must_emit": [
                    "selected gauge boundary values",
                    "matching scale",
                    "threshold policy",
                    "Higgs RG transport",
                ],
                "conditional_readout_if_filled": "lambda_H(mu)=R_Higgs[A_EW*s_beta]",
                "currently_closed": False,
            },
        ],
        "superset_use": {
            "straight_way": "diagonal HYM rank-2 replay from selected eta_00/T3 lane",
            "combined_paths": [
                "H7B1C finite H_uv payload request",
                "SM-parity diagonal HYM exp(S) replay",
                "gauge-transported Phi_fin trace with identity Higgs singlet",
                "HYM projector zero-mode value emission boundary",
            ],
            "locked_target": "same-source finite H_uv packet; no observed Higgs data and no per-Higgs beta knob",
            "combined_as_numeric_knobs": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1DNextWork.v1",
        "status": "NEXT_WORKORDER_H7B1E_BIND_DIAGONAL_HYM_OR_FIND_OFFDIAGONAL_OMEGA",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1D-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1E-DIAGONAL-HYM-TO-HUV-BINDING-THEOREM",
            "task": "Try to prove whether the selected rank-2 diagonal HYM lane is the UV two-Higgs lane or must remain an End0 support object only.",
        },
        "alternate_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1E-OFFDIAGONAL-EXT-OMEGA-SOURCE",
            "task": "Search the selected Ext/Strominger/HYM correction stack for a same-source off-diagonal Omega term on (H_u,H_d^dagger).",
        },
        "parallel_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B2-SELECTED-EW-BOUNDARY-RG-PACKET",
            "task": "Continue gauge boundary, matching-scale, thresholds, and RG transport in parallel.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1DDiagonalHYMRank2MetricCandidate",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1D-DIAGONAL-HYM-RANK2-METRIC-CANDIDATE",
        "output_packets": {
            "diagonal_hym_rank2_import": rel(IMPORT_PACKET),
            "conditional_huv_readout": rel(CONDITIONAL_READOUT),
            "strict_nonpromotion_proof": rel(NONPROMOTION),
            "promotion_contract": rel(PROMOTION_CONTRACT),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H7B1DDiagonalHYMRank2CandidateNonPromotionTheorem",
            "proved": True,
            "statement": (
                "The selected diagonal HYM replay supplies a genuine rank-2 metric/strain candidate diag(exp(u),exp(-u)) with nonzero trace-free strain u, but the current selected Higgs sector is still emitted as a rank-one trivial singlet. Therefore the diagonal HYM packet cannot be promoted to the H7B1C finite H_uv Hessian without an additional same-source theorem binding the rank-2 lines to (H_u,H_d^dagger) and emitting a finite scalar reduction. If such a nonzero diagonal reduction is later source-selected, it would force Omega=0 and the oriented endpoint s_beta=1, but that is conditional and not current Higgs closure."
            ),
        },
        "diagonal_HYM_rank2_metric_found": True,
        "diagonal_HYM_nonzero_strain_found": u_l2 > 0,
        "conditional_Huv_readout_built": True,
        "conditional_endpoint_s_beta_if_nonzero_diagonal_reduction": 1,
        "selected_Huv_basis_binding_found": False,
        "selected_finite_Huv_reduction_found": False,
        "selected_Huu_Hud_Hdd_found": False,
        "selected_Delta_Omega_found": False,
        "selected_rank_one_light_projector_P_L_found": False,
        "selected_s_beta_value_found": False,
        "selected_EW_boundary_RG_packet_closed": False,
        "new_Higgs_specific_parameters": 0,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1E_DiagonalHYMToHuvBinding_or_OffDiagonalOmegaSource_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1D_DiagonalHYMRank2MetricCandidate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "diagonal_HYM_rank2_metric_found": True,
        "diagonal_HYM_nonzero_strain_found": u_l2 > 0,
        "conditional_Huv_readout_built": True,
        "conditional_endpoint_s_beta_if_nonzero_diagonal_reduction": 1,
        "selected_Huv_basis_binding_found": False,
        "selected_finite_Huv_reduction_found": False,
        "selected_Huu_Hud_Hdd_found": False,
        "selected_Delta_Omega_found": False,
        "selected_rank_one_light_projector_P_L_found": False,
        "selected_s_beta_value_found": False,
        "selected_EW_boundary_RG_packet_closed": False,
        "new_Higgs_specific_parameters": 0,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H7B1D Diagonal HYM Rank-2 Metric Candidate v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1D-DIAGONAL-HYM-RANK2-METRIC-CANDIDATE`

## Result

```text
diagonal HYM rank-2 metric found             True
nonzero trace-free strain u                  True
conditional H_uv readout built               True
selected H_u/H_d^dagger basis binding        False
selected finite H_uv reduction               False
selected Huu/Hud/Hdd values                  False
selected Delta/Omega                         False
selected s_beta                              False
numeric lambda_H                             False
strict no-knob Higgs closure                 False
```

## What Was Found

The SM-parity diagonal HYM replay emits a real rank-2 object:

```text
H_diag = diag(exp(u), exp(-u))
S_log  = diag(u, -u)
u_l2   = {u_l2}
u_min  = {u_min}
u_max  = {u_max}
resid  = {final_residual}
```

This is strong same-branch structure: no observed constants or Higgs target
values were used.

## Why It Does Not Close H7B1C

`H7B1C` needs a finite scalar packet on

```text
(H_u, H_d^dagger)
```

with entries `Huu,Hud,Hdd`.  The diagonal replay is currently an
`End0(V_alpha)` rank-2 HYM lane, while the Higgs sector in the transported
trace is still the rank-one trivial singlet with identity transport.

So this cannot be promoted as `H_uv` yet.

## Conditional Readout

If a future same-source theorem binds the two diagonal HYM lines to
`(H_u,H_d^dagger)` and emits a nonzero finite diagonal reduction, then the
readout is forced:

```text
Omega = 0
s_beta = 1
```

That would be an oriented endpoint, not a fitted beta angle.  It is not claimed here because the binding and reduction theorem is still missing.

## Next

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1E-DIAGONAL-HYM-TO-HUV-BINDING-THEOREM`

or

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1E-OFFDIAGONAL-EXT-OMEGA-SOURCE`.
"""

    for path, payload in [
        (IMPORT_PACKET, diagonal_import),
        (CONDITIONAL_READOUT, conditional_readout),
        (NONPROMOTION, nonpromotion),
        (PROMOTION_CONTRACT, promotion_contract),
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
