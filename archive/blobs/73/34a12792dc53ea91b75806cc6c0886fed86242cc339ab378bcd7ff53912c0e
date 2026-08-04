"""Build CONST-HIGGS-01 H7B1U source-bound metric and finite-reduction gate."""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1u_source_bound_metric_and_finite_reduction"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_BINDING = BASE / "source_bound_metric_attempt.packet.json"
FINITE_REDUCTION = BASE / "conditional_finite_reduction_execution.packet.json"
DIRECT_HERM2 = BASE / "direct_herm2_payload_attempt.packet.json"
NO_CYCLE = BASE / "non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1U_SourceBoundMetricAndFiniteReduction_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1U_CONDITIONAL_REDUCTION_EXECUTED_SOURCE_REDUCTION_OPEN"


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


def import_hym_replay_module() -> Any:
    script = SM_PARITY / "scripts" / "build_selected_full_exps_hym_newton_replay.py"
    spec = importlib.util.spec_from_file_location("selected_full_exps_hym_newton_replay", script)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import {script}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def replay_diagonal_hym_grid() -> dict[str, Any]:
    replay = import_hym_replay_module()
    overlap = load(SM_PARITY / "candidate_data" / "selected_ext_overlap_hym_hodge_projector_table.candidate.json")

    mesh = 24
    relaxation = 0.6
    tolerance = 1e-12
    max_iterations = 60
    axis = (np.arange(mesh) + 0.5) / mesh
    x1, y1, x2, y2 = np.meshgrid(axis, axis, axis, axis, indexing="ij")

    unit_rescale = overlap["selected_row"]["unit_rescale_factor"]
    rho1 = replay.weighted_theta_density(2, 0, x1[:, :, 0, 0], y1[:, :, 0, 0])
    rho2 = replay.weighted_theta_density(4, 0, x2[0, 0, :, :], y2[0, 0, :, :])
    rho = (unit_rescale**2) * rho1[:, :, None, None] * rho2[None, None, :, :]

    solve_poisson, laplacian = replay.poisson_solver(rho.shape)
    u = np.zeros_like(rho)
    iterations = []
    residual_l2 = math.inf
    for step in range(max_iterations):
        exp_weighted_density = rho * np.exp(-2.0 * u)
        source = exp_weighted_density - exp_weighted_density.mean()
        residual = laplacian(u) - source
        residual_l2 = float(np.linalg.norm(residual.ravel()) / math.sqrt(residual.size))
        iterations.append(
            {
                "iteration": step,
                "residual_l2": residual_l2,
                "u_min": float(u.min()),
                "u_max": float(u.max()),
                "mean_exp_weighted_density": float(exp_weighted_density.mean()),
            }
        )
        if residual_l2 < tolerance:
            break
        next_u = solve_poisson(source)
        u = relaxation * next_u + (1.0 - relaxation) * u

    exp_density = rho * np.exp(-2.0 * u)
    local_s_beta = np.tanh(2.0 * u) ** 2
    contraction_ratios = [
        iterations[i + 1]["residual_l2"] / iterations[i]["residual_l2"]
        for i in range(len(iterations) - 1)
        if iterations[i]["residual_l2"] > 0
    ]
    tail = contraction_ratios[-8:] if len(contraction_ratios) >= 8 else contraction_ratios

    return {
        "mesh": mesh,
        "theta_series_cutoff": 12,
        "relaxation": relaxation,
        "tolerance": tolerance,
        "iterations_run": len(iterations),
        "residual_l2": residual_l2,
        "tail_contraction_ratios": tail,
        "u_min": float(u.min()),
        "u_max": float(u.max()),
        "u_l2": float(np.linalg.norm(u.ravel()) / math.sqrt(u.size)),
        "u_mean_abs": float(abs(u.mean())),
        "mean_exp_weighted_density": float(exp_density.mean()),
        "s_beta_uniform_mean": float(local_s_beta.mean()),
        "s_beta_uniform_l2": float(np.linalg.norm(local_s_beta.ravel()) / math.sqrt(local_s_beta.size)),
        "s_beta_uniform_min": float(local_s_beta.min()),
        "s_beta_uniform_max": float(local_s_beta.max()),
        "s_beta_rho_weighted_mean": float((rho * local_s_beta).mean() / rho.mean()),
        "s_beta_exp_density_weighted_mean": float((exp_density * local_s_beta).mean() / exp_density.mean()),
    }


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    h7b1t_path = DATA / "const_higgs_01_h7b1t_uv_higgs_plane_binding_or_minimal_lift_theorem.candidate.json"
    h7b1t_binding_path = DATA / "const_higgs_01_h7b1t_uv_higgs_plane_binding_or_minimal_lift_theorem" / "actual_source_binding_attempt.packet.json"
    h7b1t_lift_path = DATA / "const_higgs_01_h7b1t_uv_higgs_plane_binding_or_minimal_lift_theorem" / "conditional_metric_minimal_lift_formula.packet.json"
    h7b1d_import_path = DATA / "const_higgs_01_h7b1d_diagonal_hym_rank2_metric_candidate" / "diagonal_hym_rank2_import.packet.json"
    h7b1f_functor_path = DATA / "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet" / "basis_invariant_huv_functor_theorem.packet.json"
    h7b1g_bhuv_path = DATA / "const_higgs_01_h7b1g_fill_bhuv_or_msource" / "bhuv_minimal_lift_payload_request.packet.json"
    h7b1g_msource_path = DATA / "const_higgs_01_h7b1g_fill_bhuv_or_msource" / "msource_minimal_operator_payload_request.packet.json"
    hym_first_solve_path = SM_PARITY / "candidate_data" / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor" / "selected_hym_first_solve_payload.packet.json"
    full_replay_path = SM_PARITY / "candidate_data" / "selected_full_exps_hym_newton_replay.candidate.json"
    zero_mode_path = SM_PARITY / "candidate_data" / "selected_zero_mode_basis_from_hym_projector_source_theorem.candidate.json"

    h7b1t = load(h7b1t_path)
    h7b1t_binding = load(h7b1t_binding_path)
    h7b1t_lift = load(h7b1t_lift_path)
    h7b1d_import = load(h7b1d_import_path)
    h7b1f_functor = load(h7b1f_functor_path)
    bhuv_request = load(h7b1g_bhuv_path)
    msource_request = load(h7b1g_msource_path)
    hym_first_solve = load(hym_first_solve_path)
    full_replay = load(full_replay_path)
    zero_mode = load(zero_mode_path)

    replay = replay_diagonal_hym_grid()
    replay_matches_stored = all(
        [
            abs(replay["residual_l2"] - full_replay["solution_summary"]["final_residual_l2"]) < 1e-15,
            abs(replay["u_min"] - full_replay["solution_summary"]["u_min"]) < 1e-14,
            abs(replay["u_max"] - full_replay["solution_summary"]["u_max"]) < 1e-14,
            abs(replay["mean_exp_weighted_density"] - full_replay["solution_summary"]["mean_exp_weighted_density"]) < 1e-14,
        ]
    )

    source_metric_bound_to_E_H_UV = False
    selected_minimal_lift_policy_emitted = False
    selected_finite_reduction_policy_emitted = False
    direct_herm2_payload_emitted = False
    selected_s_beta_promoted = False
    numeric_lambda_H_derived = False

    source_binding = {
        "schema": "MTTConstHiggs01H7B1USourceBoundMetricAttempt.v1",
        "status": "SOURCE_BOUND_METRIC_ATTEMPT_FAILS_UV_HIGGS_BINDING",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1U-A-SOURCE-BOUND-METRIC",
        "input_sources": {
            "H7B1T_candidate": rel(h7b1t_path),
            "H7B1T_binding_attempt": rel(h7b1t_binding_path),
            "H7B1D_diagonal_HYM_import": rel(h7b1d_import_path),
            "selected_HYM_first_solve_payload": rel(hym_first_solve_path),
            "selected_zero_mode_basis_theorem": rel(zero_mode_path),
        },
        "closed_support": {
            "formal_UV_exact_sequence_scaffold_closed": h7b1t["formal_UV_exact_sequence_scaffold_closed"],
            "conditional_G_minimal_lift_formula_proved": h7b1t["conditional_G_minimal_lift_formula_proved"],
            "diagonal_HYM_first_solve_source_payload_emitted": hym_first_solve["A_HYM_payload"]["emitted"],
            "diagonal_HYM_metric_candidate_available": h7b1t["diagonal_HYM_metric_candidate_available"],
            "grid_replay_matches_stored_certificate": replay_matches_stored,
            "zero_mode_H_rank_one_support_available": zero_mode["finite_acceptance_validator"]["required_slots"]["H"]["required_rank"] == 1,
        },
        "blocked_binding": {
            "same_source_identifies_two_diagonal_HYM_lines_with_Hu_Hddagger": source_metric_bound_to_E_H_UV,
            "H_sector_currently_rank_one_not_UV_twoHiggs": zero_mode["finite_acceptance_validator"]["required_slots"]["H"]["required_rank"] == 1,
            "H_rho_is_trivial_singlet_not_twoHiggs_action": zero_mode["rho_candidate_reference"]["H_rho"] == {
                "T1": [[0.0]],
                "T2": [[0.0]],
                "T3": [[0.0]],
            },
            "selected_zero_mode_H_values_emitted": zero_mode["finite_acceptance_validator"]["required_slots"]["H"]["current_value_emitted"],
            "selected_minimal_lift_policy_emitted": selected_minimal_lift_policy_emitted,
            "selected_projector_phase_covariance_emitted": False,
        },
        "decision": {
            "source_metric_bound_to_E_H_UV": source_metric_bound_to_E_H_UV,
            "selected_G_minimal_lift_policy_promoted": selected_minimal_lift_policy_emitted,
            "reason": "The selected diagonal HYM lane is source-owned as an End0 T3 metric, but the available selected H carrier remains rank-one H with trivial singlet action; no packet identifies the two diagonal lines with (H_u,H_d^dagger).",
        },
        **clean_flags(),
    }

    finite_reduction = {
        "schema": "MTTConstHiggs01H7B1UConditionalFiniteReductionExecution.v1",
        "status": "CONDITIONAL_FINITE_REDUCTION_EXECUTED_SELECTION_POLICY_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1U-B-CONDITIONAL-FINITE-REDUCTION",
        "input_sources": {
            "H7B1T_minimal_lift_formula": rel(h7b1t_lift_path),
            "selected_full_expS_HYM_replay": rel(full_replay_path),
            "selected_HYM_first_solve_payload": rel(hym_first_solve_path),
        },
        "replay_certificate": {
            "mesh": replay["mesh"],
            "theta_series_cutoff": replay["theta_series_cutoff"],
            "iterations_run": replay["iterations_run"],
            "residual_l2": replay["residual_l2"],
            "tail_contraction_ratios": replay["tail_contraction_ratios"],
            "u_min": replay["u_min"],
            "u_max": replay["u_max"],
            "u_l2": replay["u_l2"],
            "u_mean_abs": replay["u_mean_abs"],
            "matches_stored_replay": replay_matches_stored,
        },
        "conditional_local_formula": h7b1t_lift["diagonal_HYM_specialization_if_bound_to_E_H_UV"]["conditional_local_s_beta"],
        "conditional_reduction_candidates_not_selected": {
            "uniform_mean": replay["s_beta_uniform_mean"],
            "uniform_l2": replay["s_beta_uniform_l2"],
            "uniform_min": replay["s_beta_uniform_min"],
            "uniform_max": replay["s_beta_uniform_max"],
            "rho_weighted_mean": replay["s_beta_rho_weighted_mean"],
            "exp_density_weighted_mean": replay["s_beta_exp_density_weighted_mean"],
        },
        "promotion_requirements": {
            "source_metric_bound_to_E_H_UV": source_metric_bound_to_E_H_UV,
            "selected_minimal_lift_policy_emitted": selected_minimal_lift_policy_emitted,
            "selected_finite_reduction_policy_emitted": selected_finite_reduction_policy_emitted,
            "finite_reduction_exactness_certificate_emitted": replay_matches_stored,
            "observed_Higgs_or_beta_selector_forbidden": True,
        },
        "decision": {
            "conditional_finite_reduction_executable": True,
            "selected_finite_reduction_policy_promoted": selected_finite_reduction_policy_emitted,
            "selected_s_beta_promoted": selected_s_beta_promoted,
            "reason": "The grid can now replay conditional reductions from the selected HYM recipe, but no same-source rule chooses uniform, rho-weighted, exp-density-weighted, or another finite reduction as the physical Higgs projection.",
        },
        **clean_flags(),
    }

    direct_herm2 = {
        "schema": "MTTConstHiggs01H7B1UDirectHerm2PayloadAttempt.v1",
        "status": "DIRECT_HERM2_HUV_PAYLOAD_ATTEMPT_STILL_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1U-C-DIRECT-HERM2-PAYLOAD",
        "input_sources": {
            "H7B1F_basis_invariant_Huv_functor": rel(h7b1f_functor_path),
            "H7B1G_BHuv_payload_request": rel(h7b1g_bhuv_path),
            "H7B1G_Msource_payload_request": rel(h7b1g_msource_path),
        },
        "conditional_functor_ready": h7b1f_functor["theorem"]["proved"],
        "payload_requests_ready": {
            "B_Huv_request_ready": bhuv_request["status"] == "BHUV_MINIMAL_LIFT_PAYLOAD_REQUESTED_NOT_EMITTED",
            "M_source_request_ready": msource_request["status"] == "MSOURCE_MINIMAL_OPERATOR_PAYLOAD_REQUESTED_NOT_EMITTED",
        },
        "actual_outputs": {
            "B_Huv": None,
            "M_source": None,
            "Huu": None,
            "Hud": None,
            "Hdd": None,
            "Delta": None,
            "Omega": None,
            "P_L": None,
            "s_beta": None,
            "lambda_H": None,
        },
        "decision": {
            "direct_Herm2_Huv_payload_emitted": direct_herm2_payload_emitted,
            "B_Huv_value_emitted": False,
            "M_source_value_emitted": False,
            "direct_Huv_entries_emitted": False,
        },
        **clean_flags(),
    }

    no_cycle = {
        "schema": "MTTConstHiggs01H7B1UNonCirculationLedger.v1",
        "status": "NO_CIRCULATION_LEDGER_UPDATED_H7B1U",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1U-NO-CYCLE",
        "retired_or_do_not_reopen": {
            "formal_UV_sequence_as_source_binding": True,
            "conditional_G_lift_formula_as_selected_lift": True,
            "conditional_reduction_candidate_as_selected_s_beta": True,
            "rank_one_H_zero_mode_as_twoHiggs_metric": True,
        },
        "new_information_added": [
            "the selected HYM grid is replayed inside the Higgs gate and matches the stored certificate",
            "conditional finite reductions of tanh(2u)^2 are computed for multiple plausible measures",
            "the absence of a selected finite-reduction policy is now separated from replay availability",
            "direct Herm(2) Huv payloads remain the alternative legal exit",
        ],
        "active_not_retired": {
            "source_metric_binding_to_E_H_UV": True,
            "selected_finite_reduction_policy": True,
            "direct_Herm2_Huv_rows": True,
            "EW_boundary_RG_after_selected_s_beta": True,
        },
        "circulation_test": {
            "is_reopening_H7B1T_formula": False,
            "is_promoting_conditional_number_as_Higgs_value": False,
            "is_using_measured_Higgs_mass_or_tan_beta": False,
            "is_reusing_rank_one_H_as_B_Huv": False,
        },
        **clean_flags(),
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1UNextWork.v1",
        "status": "NEXT_WORKORDER_H7B1V_REDUCTION_SELECTOR_OR_DIRECT_HERM2_HUV_SOURCE",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1U-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1V-REDUCTION-SELECTOR-OR-DIRECT-HERM2-HUV-SOURCE",
            "task": "Prove a same-source finite reduction policy for the conditional s_beta grid, or emit direct Herm(2) Huv rows/B_Huv+M_source from the selected source.",
        },
        "legal_exits": [
            {
                "id": "H7B1V-A",
                "label": "selected reduction selector",
                "must_emit": "same-source choice of uniform, rho-weighted, exp-density-weighted, or another finite measure plus proof it is the Higgs projection measure",
            },
            {
                "id": "H7B1V-B",
                "label": "direct Herm2 Huv source",
                "must_emit": "B_Huv+M_source or direct Huu,Hud,Hdd with exactness/residual certificate",
            },
        ],
        "superset_strategy": {
            "using_one_straight_way": False,
            "combining_paths": True,
            "straight_path": "selected diagonal HYM grid replay and conditional G-minimal lift",
            "support_path": "H7B1F/H7B1G direct Herm(2) functor kept as alternative source exit",
            "locked_target": "source-selected finite reduction or direct Huv payload, not a chosen-to-match Higgs quartic",
        },
        **clean_flags(),
    }

    theorem = {
        "name": "H7B1UConditionalReductionExecutionAndSourceSelectorBoundaryTheorem",
        "proved": True,
        "statement": (
            "H7B1U replays the selected q79/F,m=1 diagonal HYM grid and evaluates the conditional H7B1T local invariant s_beta(u)=tanh(2u)^2 under several finite reduction candidates. The replay matches the stored diagonal HYM certificate, giving uniform mean 0.004701083905943647, rho-weighted mean 0.01175427147946371, and exp-density-weighted mean 0.012349317823559027. These are conditional reduction diagnostics, not selected Higgs values, because no same-source policy binds the End0 T3 metric to E_H^UV and selects the physical finite reduction measure. Direct B_Huv/M_source/Huv rows also remain un-emitted."
        ),
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1USourceBoundMetricAndFiniteReduction",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1U-SOURCE-BOUND-METRIC-AND-FINITE-REDUCTION",
        "output_packets": {
            "source_bound_metric_attempt": rel(SOURCE_BINDING),
            "conditional_finite_reduction_execution": rel(FINITE_REDUCTION),
            "direct_herm2_payload_attempt": rel(DIRECT_HERM2),
            "non_circulation_ledger": rel(NO_CYCLE),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": theorem,
        "H7B1T_imported": h7b1t["status"] == "MTT_CONST_HIGGS_01_H7B1T_FORMAL_SEQUENCE_AND_MINIMAL_LIFT_FORMULA_CLOSED_SOURCE_BINDING_OPEN",
        "formal_UV_exact_sequence_scaffold_closed": h7b1t["formal_UV_exact_sequence_scaffold_closed"],
        "conditional_G_minimal_lift_formula_proved": h7b1t["conditional_G_minimal_lift_formula_proved"],
        "diagonal_HYM_grid_replayed": True,
        "grid_replay_matches_stored_certificate": replay_matches_stored,
        "conditional_finite_reduction_executable": True,
        "source_metric_bound_to_E_H_UV": source_metric_bound_to_E_H_UV,
        "selected_minimal_lift_policy_emitted": selected_minimal_lift_policy_emitted,
        "selected_finite_reduction_policy_emitted": selected_finite_reduction_policy_emitted,
        "direct_Herm2_Huv_payload_emitted": direct_herm2_payload_emitted,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "direct_Huv_entries_emitted": False,
        "selected_s_beta_value_found": selected_s_beta_promoted,
        "numeric_lambda_H_derived": numeric_lambda_H_derived,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1V_ReductionSelectorOrDirectHerm2HuvSource_v1",
        **clean_flags(),
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1U_SourceBoundMetricAndFiniteReduction_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "diagonal_HYM_grid_replayed": True,
        "grid_replay_matches_stored_certificate": replay_matches_stored,
        "conditional_finite_reduction_executable": True,
        "uniform_mean_conditional_s_beta": replay["s_beta_uniform_mean"],
        "rho_weighted_mean_conditional_s_beta": replay["s_beta_rho_weighted_mean"],
        "exp_density_weighted_mean_conditional_s_beta": replay["s_beta_exp_density_weighted_mean"],
        "source_metric_bound_to_E_H_UV": source_metric_bound_to_E_H_UV,
        "selected_finite_reduction_policy_emitted": selected_finite_reduction_policy_emitted,
        "selected_s_beta_value_found": selected_s_beta_promoted,
        "numeric_lambda_H_derived": numeric_lambda_H_derived,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    note = f"""# MTT CONST HIGGS 01 H7B1U Source Bound Metric And Finite Reduction v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1U-SOURCE-BOUND-METRIC-AND-FINITE-REDUCTION`

## Result

```text
formal UV exact-sequence scaffold closed        {h7b1t["formal_UV_exact_sequence_scaffold_closed"]}
conditional G-minimal lift formula proved       {h7b1t["conditional_G_minimal_lift_formula_proved"]}
diagonal HYM grid replayed                      True
grid replay matches stored certificate          {replay_matches_stored}
conditional finite reduction executable         True
source metric bound to E_H^UV                   {source_metric_bound_to_E_H_UV}
selected finite reduction policy emitted        {selected_finite_reduction_policy_emitted}
B_Huv / M_source / direct Huv emitted           False
s_beta / lambda_H promoted                      False
```

## Conditional Reduction Diagnostics

Using the H7B1T local formula `s_beta(u)=tanh(2u)^2` and replaying the selected
diagonal HYM grid gives:

```text
uniform mean                       {replay["s_beta_uniform_mean"]:.18g}
rho-weighted mean                  {replay["s_beta_rho_weighted_mean"]:.18g}
exp-density-weighted mean          {replay["s_beta_exp_density_weighted_mean"]:.18g}
uniform max                        {replay["s_beta_uniform_max"]:.18g}
residual L2                        {replay["residual_l2"]:.3e}
```

These are conditional diagnostics only.  No observed Higgs mass, `tan_beta`, or
quartic target is used, and no reduction candidate is promoted.

## What Moved Forward

H7B1U proves that the finite reduction can now be executed from the selected
HYM recipe.  The remaining issue is not numerical availability; it is source
selection of the finite measure/reduction and source binding of the metric to
`E_H^UV`.

## Remaining Boundary

The next theorem is:

`SelectedReductionSelectorOrDirectHerm2HuvSourceTheorem`

It must either select the finite reduction policy for the conditional
`s_beta(u)` grid, or emit direct `Herm(2)` Huv data via `B_Huv+M_source` or
`Huu,Hud,Hdd`.

Next label:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1V-REDUCTION-SELECTOR-OR-DIRECT-HERM2-HUV-SOURCE`
"""

    for path, payload in [
        (SOURCE_BINDING, source_binding),
        (FINITE_REDUCTION, finite_reduction),
        (DIRECT_HERM2, direct_herm2),
        (NO_CYCLE, no_cycle),
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
