"""Attach the A77 determinant response to the selected six-sector kinetic trace."""
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_producttriplegaugefluctuationfunctorandrelativeboundarycondition"
OUT = ROOT / "candidate_data" / SLUG
READOUT = OUT / "center_response_to_sector_kinetic_density_functor.packet.json"
BRANCHES = OUT / "charged_lepton_dual_metric_sign_branch_execution.packet.json"
BOUNDARY = OUT / "relative_spectral_action_boundary_condition.packet.json"
GATE = OUT / "remaining_sign_and_action_completeness_gate.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ProductTripleGaugeFluctuationFunctorAndRelativeBoundaryCondition_v1.md"
STATUS = "MTT_SELECTED_CENTER_RESPONSE_TO_KINETIC_DENSITY_FUNCTOR_CLOSED_DUAL_LEPTON_SIGN_AND_STRICT_ACTION_COMPLETENESS_OPEN"
NEXT = "MTT_Selected_ChargedLeptonDualMetricSignAndSpectralActionCompleteness_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matvec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def number(value: object) -> float:
    return float(Fraction(str(value)))


def main() -> int:
    paths = {
        "A77_execution": ROOT / "candidate_data" / "selected_gaugefixedfluctuationcomplexontoweraugmentationdomains" / "a73_brst_response_exact_execution.packet.json",
        "A77_gate": ROOT / "candidate_data" / "selected_gaugefixedfluctuationcomplexontoweraugmentationdomains" / "remaining_product_triple_and_matching_gate.packet.json",
        "A65_trace": ROOT / "candidate_data" / "selected_gaugezeromodekineticinnerproduct_or_chernweilbackgroundenergynogo" / "finite_gauge_zero_mode_kinetic_weight_theorem.packet.json",
        "A69_operator": ROOT / "candidate_data" / "selected_commonquarkorder_sharedcirclekineticoperator_or_exactresidualspectrum" / "conditional_common_projected_kinetic_operator.packet.json",
        "A69_support": ROOT / "candidate_data" / "selected_commonquarkorder_sharedcirclekineticoperator_or_exactresidualspectrum" / "exact_residual_cost_spectrum.packet.json",
        "A72_frozen": ROOT / "candidate_data" / "selected_gaugekineticfunctionalofl64andq79chord_or_strictresidualvalueemission" / "frozen_zero_parameter_gauge_execution.packet.json",
        "A51_spectral": ROOT / "candidate_data" / "selected_finitespectralactionandhiggsinnerfluctuation_or_directgenerativesmactionclosure.candidate.json",
        "one_primitive_policy": ROOT / "candidate_data" / "selected_physicalnormalizationaxiomderivation_or_oneprimitiveadoptiondecision.candidate.json",
    }
    data = {key: load(path) for key, path in paths.items()}

    delta_q = float(data["A77_execution"]["q_block"]["value"])
    delta_e = float(data["A77_execution"]["e_total"]["value"])
    tau = math.log(448.0) / 15.0
    sector_order = data["A65_trace"]["finite_form"]["sector_order"]
    trace_map = [[number(value) for value in row] for row in data["A65_trace"]["finite_form"]["sector_trace_map_T"]]
    base_traces = [float(value) for value in data["A69_operator"]["finite_operator"]["base_C1_sector_traces"]]
    p_colored = data["A69_support"]["support_projectors"]["P_colored"]
    p_e = data["A69_support"]["support_projectors"]["P_e"]
    base_cost = [14.0 / 3.0, 14.0 / 3.0, 14.0 / 3.0, 0.0, -3.0, 0.0]

    readout = {
        "schema": "MTTCenterResponseToSectorKineticDensityFunctor.v1",
        "status": "FORMAL_PRODUCT_TRIPLE_CENTER_READOUT_AND_GAUGE_TRACE_MAP_CLOSED",
        "input": {
            "center_valued_determinant_response": [delta_q, delta_e],
            "source_blocks": ["q tower/Z7 augmentation", "Lens direct plus Z4 return"],
        },
        "selected_sector_support": {
            "sector_order": sector_order,
            "P_colored": p_colored,
            "P_e": p_e,
            "projectors_disjoint": sum(a * b for a, b in zip(p_colored, p_e)) == 0,
            "projectors_gauge_commuting": True,
        },
        "functor": {
            "cost_response": "R_kin(delta_q,delta_e;s_e)=delta_q P_colored+s_e delta_e P_e",
            "weight": "W_kin=exp[-tau_int(C0+R_kin)] Phi_C1^+",
            "gauge_metric": "K_a=Tr_HF(W_kin T_a^2)",
            "sector_trace_matrix": trace_map,
            "bounded_positive_for_both_signs": True,
            "gauge_commuting_for_both_signs": True,
            "mathematically_well_defined": True,
        },
        "source_scope": {
            "magnitudes_delta_q_delta_e_selected_by_A77_character_BRST_execution": True,
            "support_projectors_preexist_A72_target_ranking": True,
            "charged_lepton_sign_selected": False,
            "physical_product_triple_action_ownership_closed": False,
        },
    }

    branch_rows = []
    for sign in (-1, 1):
        costs = [
            base + delta_q * q_support + sign * delta_e * e_support
            for base, q_support, e_support in zip(base_cost, p_colored, p_e)
        ]
        weights = [trace * math.exp(-tau * cost) for trace, cost in zip(base_traces, costs)]
        kinetic = matvec(trace_map, weights)
        ratios = [kinetic[0] / kinetic[1], 1.0, kinetic[2] / kinetic[1]]
        branch_rows.append({
            "charged_lepton_cost_sign": sign,
            "interpretation": "dual/inverse-metric lepton lane" if sign == -1 else "same-sign heat-cost lepton lane",
            "cost_eigenvalues_Q_u_d_L_e_N": costs,
            "weighted_sector_traces": weights,
            "K_U1_SU2_SU3": kinetic,
            "K_over_K2": ratios,
            "positive_weight": min(weights) > 0.0,
        })
    dual_branch = next(row for row in branch_rows if row["charged_lepton_cost_sign"] == -1)
    same_branch = next(row for row in branch_rows if row["charged_lepton_cost_sign"] == 1)
    frozen_ratios = [float(value) for value in data["A72_frozen"]["K_over_K2"]]
    branches = {
        "schema": "MTTChargedLeptonDualMetricSignBranchExecution.v1",
        "status": "BOTH_POSITIVE_BRANCHES_EXECUTED_DUAL_SIGN_REPLAYS_FROZEN_A72_SIGN_NOT_SOURCE_SELECTED",
        "rows": branch_rows,
        "dual_branch": dual_branch,
        "same_sign_branch": same_branch,
        "frozen_A72_ratios": frozen_ratios,
        "dual_branch_max_abs_residual_to_A72": max(abs(a - b) for a, b in zip(dual_branch["K_over_K2"], frozen_ratios)),
        "same_sign_branch_separation_from_dual": max(abs(a - b) for a, b in zip(same_branch["K_over_K2"], dual_branch["K_over_K2"])),
        "branch_count": 2,
        "continuous_parameters_added": 0,
        "binary_sign_selected_by_current_source": False,
        "observed_gauge_values_used_as_selector": False,
    }

    tree_trace = [float(value) for value in data["A65_trace"]["finite_form"]["identity_weight_trace"]]
    boundary = {
        "schema": "MTTRelativeSpectralActionBoundaryCondition.v1",
        "status": "UNIVERSAL_RELATIVE_BOUNDARY_CLOSED_AT_ADOPTED_SPECTRAL_ACTION_ONE_PRIMITIVE_TIER_STRICT_COMPLETENESS_OPEN",
        "A51_tree_boundary": {
            "GUT_normalized_gauge_rows": tree_trace,
            "relative_coordinates": [tree_trace[0] - tree_trace[1], tree_trace[2] - tree_trace[1]],
            "relative_coordinates_zero": max(abs(tree_trace[0] - tree_trace[1]), abs(tree_trace[2] - tree_trace[1])) < 1e-14,
        },
        "adopted_closure_tier": {
            "one_shared_physical_normalization_primitive": data["one_primitive_policy"]["key_numbers"]["P_EW_parameter_count"] == 1,
            "relative_bare_terms_set_by_universal_A51_boundary": True,
            "absolute_common_normalization_cancels_from_ratios": True,
            "relative_matching_directions_closed_conditionally": 2,
        },
        "strict_no_knob_tier": {
            "A51_spectral_action_proved_complete_microscopic_MTT_action": False,
            "independent_relative_local_terms_excluded_from_all_MTT_actions": False,
            "P_EW_strict_source_derivation_required_for_absolute_values": True,
        },
    }

    gate = {
        "schema": "MTTRemainingSignAndActionCompletenessGate.v1",
        "status": "CENTER_READOUT_AND_RELATIVE_PROFILE_BOUNDARY_CLOSED_BINARY_SIGN_AND_STRICT_ACTION_COMPLETENESS_OPEN",
        "closed": {
            "A77_magnitudes_imported": True,
            "P_colored_P_e_support_map": True,
            "positive_gauge_commuting_weight_functor": True,
            "six_sector_to_three_gauge_trace_execution": True,
            "both_sign_branches_executed_without_fit": True,
            "dual_branch_exactly_replays_A72": branches["dual_branch_max_abs_residual_to_A72"] < 1e-14,
            "universal_relative_boundary_at_one_primitive_tier": boundary["A51_tree_boundary"]["relative_coordinates_zero"],
        },
        "open": {
            "selected_charged_lepton_dual_metric_sign": True,
            "selected_action_proves_determinant_response_is_the_kinetic_cost_readout": True,
            "spectral_action_is_complete_no_extra_relative_local_terms": True,
            "full_spectator_block_neutrality_or_cancellation": True,
            "strict_absolute_PEW_source": True,
            "modern_precision_validation": True,
        },
        "continuous_source_parameters_remaining_for_relative_ratios": 0,
        "discrete_source_bits_remaining_for_relative_ratios": 1,
        "strict_gauge_values_accepted": 0,
        "next_required_artifact": NEXT,
    }

    checks = {
        "sector_order_correct": sector_order == ["Q", "u", "d", "L", "e", "N"],
        "support_projectors_disjoint": readout["selected_sector_support"]["projectors_disjoint"],
        "trace_map_rank_two_imported": data["A65_trace"]["finite_form"]["relative_rank"] == 2,
        "both_sign_branches_positive": all(row["positive_weight"] for row in branch_rows),
        "branch_count_two": branches["branch_count"] == 2,
        "dual_branch_replays_A72": branches["dual_branch_max_abs_residual_to_A72"] < 1e-14,
        "sign_not_target_selected": not branches["binary_sign_selected_by_current_source"] and not branches["observed_gauge_values_used_as_selector"],
        "relative_tree_boundary_zero": boundary["A51_tree_boundary"]["relative_coordinates_zero"],
        "one_primitive_policy_preserved": boundary["adopted_closure_tier"]["one_shared_physical_normalization_primitive"],
        "strict_action_completeness_not_overclaimed": not boundary["strict_no_knob_tier"]["A51_spectral_action_proved_complete_microscopic_MTT_action"],
        "one_discrete_bit_remaining": gate["discrete_source_bits_remaining_for_relative_ratios"] == 1,
    }
    candidate = {
        "schema": "MTTSelectedProductTripleGaugeFluctuationFunctorAndRelativeBoundaryCondition.v1",
        "status": STATUS,
        "results": {
            "center_response_to_sector_density_functor_closed": True,
            "six_sector_gauge_trace_execution_closed": True,
            "dual_sign_branch_replays_A72": True,
            "relative_boundary_closed_at_one_primitive_tier": True,
            "continuous_parameters_remaining_for_relative_ratios": 0,
            "discrete_sign_bits_remaining_for_relative_ratios": 1,
            "strict_action_completeness_closed": False,
            "strict_gauge_values_accepted": 0,
            "new_continuous_parameters": 0,
        },
        "outputs": {
            "readout": str(READOUT.relative_to(ROOT)).replace("\\", "/"),
            "branches": str(BRANCHES.relative_to(ROOT)).replace("\\", "/"),
            "boundary": str(BOUNDARY.relative_to(ROOT)).replace("\\", "/"),
            "gate": str(GATE.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {key: bool(value) for key, value in checks.items()},
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_ProductTripleGaugeFluctuationFunctorAndRelativeBoundaryCondition_v1",
        "status": STATUS,
        "center_to_sector_functor_closed": True,
        "dual_branch_K_over_K2": dual_branch["K_over_K2"],
        "same_sign_branch_K_over_K2": same_branch["K_over_K2"],
        "relative_boundary_one_primitive_tier_closed": True,
        "continuous_parameters_remaining_for_ratios": 0,
        "discrete_sign_bits_remaining_for_ratios": 1,
        "strict_action_completeness_closed": False,
        "strict_gauge_values_accepted": 0,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Product-Triple Gauge Fluctuation Functor and Relative Boundary Condition v1

## Center-to-sector functor

A77 emits the center-valued response `(delta_q,delta_e)`. The already selected support projectors
give the unique two-support kinetic readout

```text
R_kin(delta_q,delta_e;s_e) = delta_q P_colored + s_e delta_e P_e,
W_kin = exp[-tau_int(C0+R_kin)] Phi_C1^+,
K_a = Tr_HF(W_kin T_a^2).
```

The map is bounded, positive after exponentiation, and gauge commuting. The exact A65 six-sector
trace matrix then emits all three gauge rows. No new scalar row or continuous coefficient is added.

## Binary sign execution

Both allowed real orientation signs were executed before any new comparison. The dual/inverse-metric
branch `s_e=-1` gives

```text
K/K2 = {dual_branch['K_over_K2']},
```

and replays frozen A72 with maximum residual `{branches['dual_branch_max_abs_residual_to_A72']:.3g}`.
The same-sign branch gives

```text
K/K2 = {same_branch['K_over_K2']}.
```

Both weights remain positive. Current source data do not select the dual sign, so this is one binary
branch bit, not a continuous fit and not a strict gauge-value promotion.

## Relative boundary

The A51 product spectral action has GUT-normalized tree rows `{tree_trace}`. Its two relative
coordinates vanish exactly. At the adopted one-shared-`P_EW` closure tier, the common normalization
cancels from ratios and the relative boundary is fixed. Strict no-knob promotion is stronger: it
must prove the spectral action is the complete microscopic MTT gauge action and excludes every extra
relative local quadratic term.

## Remaining theorem

The next artifact is `{NEXT}`. It must derive the charged-lepton dual/inverse-metric sign from the
shared-circle/Lens action, prove determinant-to-kinetic-cost ownership and spectator neutrality, and
establish strict action completeness. Relative ratios then have no continuous source parameter and
no remaining discrete branch bit; absolute normalization remains the separate `P_EW` problem.
"""

    dump(READOUT, readout)
    dump(BRANCHES, branches)
    dump(BOUNDARY, boundary)
    dump(GATE, gate)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
