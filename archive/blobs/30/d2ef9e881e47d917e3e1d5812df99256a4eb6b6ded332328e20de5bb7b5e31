"""Build CONST-HIGGS-01 H6F symbolic D-term boundary replay."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h6f_symbolic_dterm_boundary_replay"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BOUNDARY_REPLAY = BASE / "symbolic_boundary_replay_functor.packet.json"
RG_CONTRACT = BASE / "higgs_rg_transport_contract.packet.json"
SOURCE_GATE = BASE / "source_input_gate_ledger.packet.json"
SUPERSET_MAP = BASE / "superset_path_map.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H6F_SymbolicDTermBoundaryReplay_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H6F_SYMBOLIC_DTERM_REPLAY_BUILT_VALUES_OPEN"


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

    h6e_path = DATA / "const_higgs_01_h6e_uv_two_higgs_projection_angle_or_primitive_beta_policy.candidate.json"
    h6e_symbolic_path = DATA / "const_higgs_01_h6e_uv_two_higgs_projection_angle_or_primitive_beta_policy" / "symbolic_dterm_boundary_packet.packet.json"
    h6e_policy_path = DATA / "const_higgs_01_h6e_uv_two_higgs_projection_angle_or_primitive_beta_policy" / "primitive_beta_policy.packet.json"
    h6d_contract_path = DATA / "const_higgs_01_h6d_selected_dterm_boundary_or_beta_source" / "dterm_boundary_acceptance_contract.packet.json"
    ew_b41_path = DATA / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching" / "rg_matching_threshold_scheme_status.packet.json"
    ew_b43_policy_path = DATA / "const_ew_02_weak_mixing_b43_threshold_vector_or_minimal_policy" / "minimal_threshold_replay_policy.packet.json"
    ew_b44_execution_path = DATA / "const_ew_02_weak_mixing_b44_conditional_profile_execution" / "conditional_profile_execution.packet.json"

    h6e = load(h6e_path)
    h6e_symbolic = load(h6e_symbolic_path)
    h6e_policy = load(h6e_policy_path)
    h6d_contract = load(h6d_contract_path)
    ew_b41 = load(ew_b41_path)
    ew_b43_policy = load(ew_b43_policy_path)
    ew_b44_execution = load(ew_b44_execution_path)

    boundary_formula = h6e_symbolic["symbolic_boundary"]["formula"]
    potential_convention = h6e_symbolic["symbolic_boundary"]["potential_convention"]

    boundary_replay = {
        "schema": "MTTConstHiggs01H6FSymbolicBoundaryReplayFunctor.v1",
        "status": "SYMBOLIC_DTERM_REPLAY_FUNCTOR_DEFINED_VALUES_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6F-SYMBOLIC-DTERM-BOUNDARY-REPLAY-FUNCTOR",
        "inputs": {
            "H6E_symbolic_Dterm_boundary": rel(h6e_symbolic_path),
            "H6D_Dterm_boundary_contract": rel(h6d_contract_path),
        },
        "boundary_functor": {
            "name": "Lambda_H_boundary_from_selected_EW_Higgs_data",
            "domain": [
                "selected gauge boundary pair (g_2, g_Y)",
                "selected beta_H or selected intrinsic no-beta replacement",
                "selected matching scale mu_match",
                "declared threshold/RG policy",
            ],
            "codomain": "symbolic lambda_H(mu_match) plus transport contract",
            "tree_boundary": boundary_formula,
            "potential_convention": potential_convention,
            "cos2beta_square_identity": h6e_symbolic["symbolic_boundary"]["equivalent_cos2beta_from_tanbeta"],
            "same_formula_rewritten_with_tan_beta": "lambda(mu_match) = (g_2^2 + g_Y^2) * ((tan_beta_H^2 - 1)/(tan_beta_H^2 + 1))^2 / 8",
        },
        "strict_replay_guards": {
            "uses_measured_mH_or_v_to_choose_beta": False,
            "uses_measured_lambda_to_choose_threshold": False,
            "promotes_tan_beta_10": False,
            "promotes_single_Higgs_projection_to_UV_angle": False,
            "declares_beta_primitive": False,
        },
        "output_status": {
            "symbolic_boundary_defined": True,
            "numeric_boundary_value_emitted": False,
            "numeric_low_scale_lambda_emitted": False,
            "strict_no_knob_Higgs_closure": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    rg_contract = {
        "schema": "MTTConstHiggs01H6FHiggsRGTransportContract.v1",
        "status": "HIGGS_RG_TRANSPORT_OPERATOR_DECLARED_INPUTS_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6F-HIGGS-RG-TRANSPORT-CONTRACT",
        "inputs": {
            "EW_B41_RG_matching_scaffold": rel(ew_b41_path),
            "EW_B43_minimal_threshold_policy": rel(ew_b43_policy_path),
            "EW_B44_conditional_profile_execution": rel(ew_b44_execution_path),
        },
        "transport_operator": {
            "name": "R_Higgs",
            "formal_action": "lambda_H(mu_obs) = R_Higgs[lambda_H(mu_match), gauge(mu), Yukawa(mu), threshold_vector, scheme, loop_order]",
            "boundary_value": "lambda_H(mu_match) = (g_2(mu_match)^2 + g_Y(mu_match)^2) cos^2(2 beta_H) / 8",
            "declared_minimum_policy": "one-loop/threshold replay is admissible only as a labeled conditional lane until precision source values are selected",
            "exact_numeric_algorithm_filled": False,
            "accepted_external_benchmark_values_used_as_selectors": ew_b41["decision"]["precision_benchmark_values_imported_as_selectors"],
        },
        "current_imported_support": {
            "rg_policy_scaffold_declared": ew_b41["decision"]["RG_policy_scaffold_declared"],
            "one_loop_diagnostic_engine_available": ew_b41["decision"]["one_loop_diagnostic_engine_available"],
            "minimal_threshold_replay_policy_available": ew_b43_policy["decision"]["minimal_threshold_replay_policy_closed"],
            "weak_mixing_conditional_profile_executable": ew_b44_execution["checks"]["finite_value"],
        },
        "required_before_numerical_Higgs_comparison": {
            "selected_gauge_boundary_values": False,
            "selected_beta_or_intrinsic_no_beta_replacement": False,
            "selected_matching_scale": False,
            "selected_Higgs_threshold_vector": False,
            "selected_Yukawa_boundary_or_replay_policy": False,
            "declared_loop_order_and_scheme": False,
            "covariance_or_uncertainty_policy": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    source_gate = {
        "schema": "MTTConstHiggs01H6FSourceInputGateLedger.v1",
        "status": "NUMERICAL_SOURCE_GATES_EXPLICITLY_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6F-SOURCE-INPUT-GATE-LEDGER",
        "closed_inputs": {
            "low_energy_single_Higgs_projection": h6e["low_energy_single_Higgs_projection_closed"],
            "standard_Dterm_factor": h6d_contract["current_filled_fields"]["correct_formula_factor"],
            "symbolic_boundary_formula": h6e["symbolic_Dterm_boundary_ready"],
            "primitive_beta_policy_written": h6e["beta_primitive_policy_built"],
        },
        "open_strict_inputs": {
            "selected_UV_beta_source_found": h6e["selected_UV_beta_source_found"],
            "beta_primitive_declared_now": h6e["beta_primitive_declared_now"],
            "new_Higgs_specific_parameters_now": h6e["new_Higgs_specific_parameters"],
            "selected_gauge_boundary_values_filled": h6e_symbolic["numeric_status"]["selected_gauge_boundary_values_filled"],
            "matching_scale_policy_filled": h6e_symbolic["numeric_status"]["matching_scale_policy_filled"],
            "threshold_RG_transport_filled": h6e_symbolic["numeric_status"]["threshold_RG_transport_filled"],
            "numeric_lambda_H_derived": h6e_symbolic["numeric_status"]["numeric_lambda_H_derived"],
        },
        "acceptance_policy": {
            "strict_no_knob_accepts": [
                "selected intrinsic K_H^(4)[12,12,12,12] row with coefficient convention",
                "or selected UV beta/theta plus selected gauge boundary and selected RG/threshold policy",
            ],
            "one_primitive_tier_accepts": [
                "a single explicit beta_H primitive only if declared before Higgs comparison",
                "or a shared universal physical primitive reused unchanged from other constants",
            ],
            "rejects": [
                "Higgs mass backsolve",
                "lambda_H target fit",
                "tan_beta=10 representative promotion",
                "threshold residual scan against measured lambda",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    superset_map = {
        "schema": "MTTConstHiggs01H6FSupersetPathMap.v1",
        "status": "SUPERSET_PATHS_SEPARATED_LOCKED_TARGET_DECLARED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6F-SUPERSET-PATH-MAP",
        "locked_target": "source-selected Higgs quartic boundary/replay without measured Higgs lambda as selector",
        "paths": {
            "route_A_intrinsic_row": {
                "object": "K_H^(4)[12,12,12,12]",
                "tier": "strict no-knob if emitted by selected action",
                "current_status": "OPEN",
            },
            "route_B_Dterm_boundary": {
                "object": "lambda = (g_2^2 + g_Y^2) cos^2(2 beta_H) / 8",
                "tier": "strict no-knob only after beta/gauge/RG source gates close",
                "current_status": "SYMBOLIC_REPLAY_READY_VALUES_OPEN",
            },
            "route_C_explicit_beta_primitive": {
                "object": "beta_H or tan_beta_H",
                "tier": h6e_policy["policy"]["allowed_tier"],
                "current_status": "POLICY_READY_NOT_DECLARED",
            },
            "route_D_shared_universal_primitive": {
                "object": "shared action/metrology primitive reused across constants",
                "tier": "conditional universal-primitive portfolio, not strict no-knob",
                "current_status": "AVAILABLE_AS_LATER_PORTFOLIO_LANE",
            },
        },
        "combination_rule": {
            "may_compare_paths": True,
            "may_reuse_a_declared_universal_primitive_across_paths": True,
            "may_sum_independent_path_residuals_to_fit_lambda": False,
            "must_label_tier_before_numeric_comparison": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H6FNextWork.v1",
        "status": "NEXT_WORKORDER_H7_STRICT_SOURCE_OR_PORTFOLIO_REPLAY",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6F-NEXT",
        "strict_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7-INTRINSIC-H-SECTOR-K4-ROW-OR-UV-BETA-THEOREM",
            "task": "Try to emit either the intrinsic fourth row K_H^(4)[12,12,12,12] or a selected UV beta/tan_beta theorem.",
        },
        "portfolio_next": {
            "label": "CONST-HIGGS-01 / UNIVERSAL-PRIMITIVE-PORTFOLIO / H7P-BETA-OR-SHARED-ACTION-PRIMITIVE-REPLAY",
            "task": "If strict H7 remains open, test whether one already-declared universal primitive can fix the remaining Higgs replay without adding a Higgs-only knob.",
        },
        "paper_insert_section": {
            "label": "CONST-HIGGS-01 / PAPER-INSERT / SYMBOLIC-DTERM-REPLAY-AND-SOURCE-GATES",
            "task": "Add the H6F functor, the source gate ledger, and the strict versus one-primitive tier distinction.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H6FSymbolicDTermBoundaryReplay",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6F-SYMBOLIC-DTERM-BOUNDARY-REPLAY",
        "output_packets": {
            "symbolic_boundary_replay_functor": rel(BOUNDARY_REPLAY),
            "higgs_rg_transport_contract": rel(RG_CONTRACT),
            "source_input_gate_ledger": rel(SOURCE_GATE),
            "superset_path_map": rel(SUPERSET_MAP),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H6FSymbolicDTermBoundaryReplayTheorem",
            "proved": True,
            "statement": (
                "H6F turns the H6E symbolic D-term boundary into a replay functor. The functor maps selected gauge data, beta_H or an intrinsic no-beta replacement, matching scale, and threshold/RG policy to a symbolic lambda_H boundary and formal RG transport contract. It emits no numerical lambda_H, declares no beta primitive, uses no observed Higgs data as a selector, and keeps strict no-knob, one-primitive, and diagnostic replay tiers separated."
            ),
        },
        "symbolic_boundary_replay_functor_defined": True,
        "Higgs_RG_transport_contract_declared": True,
        "source_input_gate_ledger_built": True,
        "superset_paths_separated": True,
        "selected_UV_beta_source_found": False,
        "beta_primitive_declared_now": False,
        "new_Higgs_specific_parameters": 0,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7_IntrinsicHSectorK4RowOrUVBetaTheorem_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H6F_SymbolicDTermBoundaryReplay_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "symbolic_boundary_replay_functor_defined": True,
        "Higgs_RG_transport_contract_declared": True,
        "source_input_gate_ledger_built": True,
        "superset_paths_separated": True,
        "selected_UV_beta_source_found": False,
        "beta_primitive_declared_now": False,
        "new_Higgs_specific_parameters": 0,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H6F Symbolic DTerm Boundary Replay v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6F-SYMBOLIC-DTERM-BOUNDARY-REPLAY`

## Result

```text
symbolic D-term replay functor             True
Higgs RG transport contract                True
source input gate ledger                   True
superset paths separated                   True
selected UV beta source                    False
beta primitive declared now                False
new Higgs-specific parameters now          0
numeric lambda_H                           False
strict no-knob Higgs closure               False
```

## Functor

```text
lambda_H(mu_match) = (g_2(mu_match)^2 + g_Y(mu_match)^2) cos^2(2 beta_H) / 8
lambda_H(mu_obs)   = R_Higgs[lambda_H(mu_match), gauge, Yukawa, thresholds, scheme]
```

This is a replay object, not a numerical prediction yet.

## Superset Use

H6F uses one straight symbolic D-term lane and compares it against the
intrinsic-row and one-primitive lanes.  The paths are not combined as fitting
knobs.  A later declared universal primitive may be reused, but it must be
declared before any Higgs comparison and remain fixed across constants.

## Next

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7-INTRINSIC-H-SECTOR-K4-ROW-OR-UV-BETA-THEOREM`
"""

    for path, payload in [
        (BOUNDARY_REPLAY, boundary_replay),
        (RG_CONTRACT, rg_contract),
        (SOURCE_GATE, source_gate),
        (SUPERSET_MAP, superset_map),
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
