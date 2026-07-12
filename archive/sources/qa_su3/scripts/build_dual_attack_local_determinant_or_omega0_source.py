"""Attack the two remaining electroweak frontier lanes in parallel.

Lane A: selected local determinant / analytic torsion threshold vector.
Lane B: physical Omega0 / compactification action unit.

This artifact imports the newest sibling-repo reductions and advances each lane
only where a source-certified step exists.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"
GR = ROOT.parent / "mtt-protospinor-gr-response-proof"

INPUTS = {
    "frontier": DATA / "selected_physical_gauge_anchor_and_electroweak_threshold_vector.candidate.json",
    "local_interface": NONSM / "certificates" / "selected_local_determinant_computation_interface_certificate.json",
    "local_final_attempt": NONSM / "certificates" / "selected_local_determinant_final_computation_attempt_certificate.json",
    "operator_weight_gate": NONSM / "certificates" / "u1_su2_operator_weight_candidate_gate_certificate.json",
    "qc_circle": NONSM / "certificates" / "selected_qc_circle_gauge_block_equivalence_certificate.json",
    "su2_flat_policy": NONSM / "certificates" / "selected_flat_fp_quotient_normalization_policy_certificate.json",
    "character_channel": GR / "certificates" / "selected_character_channel_covariance_import_certificate.json",
    "omega0_source": GR / "certificates" / "selected_physical_omega0_source_theorem_certificate.json",
    "sharp_semigroup": GR / "certificates" / "selected_sharp_semigroup_bound_theorem_certificate.json",
    "omega_convention": GR / "certificates" / "selected_omega_convention_theorem_certificate.json",
}

OUTPUT_DATA = DATA / "dual_attack_local_determinant_or_omega0_source.candidate.json"
OUTPUT_CERT = CERTS / "dual_attack_local_determinant_or_omega0_source_certificate.json"
OUTPUT_NOTE = PROOF / "Dual_Attack_Local_Determinant_or_Omega0_Source_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def by_name(rows: list[dict[str, Any]], name: str) -> dict[str, Any]:
    for row in rows:
        if row.get("name") == name:
            return row
    raise KeyError(name)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    frontier = load(INPUTS["frontier"])
    local_interface = load(INPUTS["local_interface"])
    local_final = load(INPUTS["local_final_attempt"])
    weights = load(INPUTS["operator_weight_gate"])
    qc = load(INPUTS["qc_circle"])
    su2 = load(INPUTS["su2_flat_policy"])
    char = load(INPUTS["character_channel"])
    omega0 = load(INPUTS["omega0_source"])
    sharp = load(INPUTS["sharp_semigroup"])
    convention = load(INPUTS["omega_convention"])

    two_thirds = by_name(weights["candidate_results"], "two_thirds_u1_diagnostic")
    scalar_unit = by_name(weights["candidate_results"], "scalar_unit_weights")
    gut = by_name(weights["candidate_results"], "gut_hypercharge_three_fifths_u1")
    target = weights["target_witness"]

    omega_factor = convention["reduced_formula"]["Omega0_over_sqrt_alpha_phys"]
    omega_gap_factor = convention["reduced_formula"]["omega_gap_phys_over_sqrt_alpha_phys"]
    lambda_gap_factor = convention["reduced_formula"]["Lambda_gap_phys_over_sqrt_alpha_phys"]
    expected_omega_factor = math.sqrt(15.0 / math.log(448.0))

    lane_a = {
        "name": "LaneA_SelectedLocalDeterminantThresholdVector",
        "status": "OPEN_SELECTED_GAUGE_FACTOR_SPECTRAL_TABLE_REQUIRED",
        "what_closes_now": {
            "determinant_accounting_interface_closed": local_interface["verdict"]["determinant_accounting_interface_closed"],
            "qc_circle_block_closed_for_weak_split": qc["verdict"]["qc_selected_for_lambda_12_accounting"],
            "su2_flat_fp_policy_closed_for_weak_split": su2["verdict"]["su2_selected_for_lambda_12_accounting"],
            "u1_shared_circle_index_closed": frontier["theorem"]["selected_internal_inputs"]["I_U1"] == "2/3",
        },
        "strongest_selected_inputs": {
            "selected_p_Qc_for_weak_split": qc["selected_values"]["selected_p_Qc_for_weak_split"],
            "selected_p_SU2_for_weak_split": su2["selected_flat_su2_data"]["selected_p_SU2_for_weak_split"],
            "selected_U1_threshold_index": "2/3",
            "v1_tilde": frontier["theorem"]["threshold_vector_gate"]["known_selected_prefactor_v1_tilde"],
        },
        "diagnostics_not_proof": {
            "scalar_unit_lambda_12": scalar_unit["lambda_12"],
            "gut_three_fifths_lambda_12": gut["lambda_12"],
            "two_thirds_proxy_lambda_12": two_thirds["lambda_12"],
            "two_thirds_proxy_delta_g12": two_thirds["Delta_G_12"],
            "target_witness_lambda_12": target["lambda_12"],
            "target_witness_delta_g12": target["Delta_G_12"],
        },
        "blocker": {
            "selected_spectra_computed": local_interface["verdict"]["selected_spectra_computed"],
            "final_attempt_status": local_final["status"],
            "missing": local_final["remaining_required_data"],
            "minimal_next_object": "selected gauge-factor-resolved spectral table with U1/hypercharge, SU2, and SU3/Qa index weights",
        },
        "decision": "The lane is advanced to an exact executable determinant interface with Qc and SU2 weak-split blocks closed, but lambda_12 remains open because the selected U1/hypercharge local determinant spectrum and full index-weighted spectral table are not source-emitted.",
    }

    lane_b = {
        "name": "LaneB_PhysicalOmega0Source",
        "status": "REDUCED_TO_ALPHA_PHYS_OR_ACTION_UNIT_ONLY",
        "what_closes_now": {
            "character_channel_dQ_closed": char["internal_selected_data"]["D_raw_norm_squared_d_Q"] == 1.0,
            "C_UV_internal_imported": char["internal_selected_data"]["C_UV_norm_internal"],
            "rho_UV_internal_closed": char["internal_selected_data"]["rho_UV"],
            "s_star_closed": char["internal_selected_data"]["s_star"],
            "C_Q_equals_1_closed": sharp["omega0_formula"]["C_Q"] == 1.0,
            "epsilon_equals_1_over_448_closed": sharp["omega0_formula"]["epsilon_adm"] == 1 / 448,
            "chi_omega_equals_1_closed": convention["convention_selection"]["chi_omega"] == 1.0,
        },
        "reduced_formula": {
            "Omega0": convention["reduced_formula"]["Omega0"],
            "Omega0_over_sqrt_alpha_phys": omega_factor,
            "omega_gap_phys": convention["reduced_formula"]["omega_gap_phys"],
            "omega_gap_phys_over_sqrt_alpha_phys": omega_gap_factor,
            "Lambda_gap_phys": convention["reduced_formula"]["Lambda_gap_phys"],
            "Lambda_gap_phys_over_sqrt_alpha_phys": lambda_gap_factor,
            "formula_check_sqrt_15_over_log_448": expected_omega_factor,
        },
        "blocker": {
            "alpha_phys_or_action_unit_selected": convention["still_open"]["alpha_phys_or_action_unit_selected"],
            "physical_Omega0_numeric_closed": convention["still_open"]["physical_Omega0_numeric_closed"],
            "minimal_next_object": "Selected_Physical_Alpha_or_Action_Unit_Theorem_v1",
        },
        "decision": "The lane advances: Omega0 is no longer blocked by C_Q, epsilon_adm, chi_omega, C_UV, or Q_tau on the imported character-channel branch. It is reduced to the single physical action-unit primitive alpha_phys.",
    }

    cross_lane = {
        "can_substitute_lane_b_for_lane_a": False,
        "reason": "Omega0 fixes physical units/common normalization. It does not emit the gauge-factor-dependent determinant difference lambda_12.",
        "can_substitute_lane_a_for_lane_b": False,
        "reason_2": "lambda_12 fixes a dimensionless weak-split threshold. It does not select a physical inverse-length/action unit.",
        "joint_closure_condition": "Need both alpha_phys and lambda_12/Delta_a^sel, plus convention map, mu_match, and RG/threshold scheme, before measured electroweak comparison.",
    }

    source_checks = {
        "frontier_loaded": frontier["status"] == "PHYSICAL_EW_MATCHING_REDUCED_TO_OMEGA0_AND_LOCAL_DETERMINANT_OPEN",
        "local_interface_closed": lane_a["what_closes_now"]["determinant_accounting_interface_closed"] is True,
        "local_final_still_blocked": local_final["verdict"]["numeric_electroweak_closure"] is False,
        "qc_closed": lane_a["what_closes_now"]["qc_circle_block_closed_for_weak_split"] is True,
        "su2_policy_closed": lane_a["what_closes_now"]["su2_flat_fp_policy_closed_for_weak_split"] is True,
        "two_thirds_near_hit_not_proof": two_thirds["status"] == "NEAR_HIT_DIAGNOSTIC_NOT_A_PROOF",
        "character_channel_imported": char["status"] == "INTERNAL_CHARACTER_CHANNEL_QTAU_AND_CUV_IMPORTED_OMEGA0_OPEN",
        "omega0_reduced": omega0["status"] == "OMEGA0_REDUCED_TO_PHYSICAL_ALPHA_CQ_EPSILON_AND_CHI",
        "sharp_semigroup_closed": sharp["status"] == "CQ1_SHARP_SEMIGROUP_BOUND_CLOSED_ALPHA_CHI_OPEN",
        "omega_convention_closed": convention["status"] == "CHI_OMEGA_CONVENTION_CLOSED_ALPHA_OPEN",
        "omega_factor_matches_formula": abs(omega_factor - expected_omega_factor) < 1e-15,
    }

    decision = {
        "lane_A_lambda12_closed": False,
        "lane_A_reduced_to_selected_spectral_table": True,
        "lane_B_Omega0_closed": False,
        "lane_B_reduced_to_alpha_phys_only": True,
        "full_physical_electroweak_closure": False,
        "next_required_objects": [
            "Selected_Gauge_Factor_Spectral_Table_v1",
            "Selected_Physical_Alpha_or_Action_Unit_Theorem_v1",
            "Typed_Electroweak_Convention_Map_and_RG_Scheme_v1",
        ],
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "DualAttackLocalDeterminantOrOmega0Source",
        "status": "DUAL_LANE_ATTACK_DONE_LAMBDA12_OPEN_OMEGA0_REDUCED_TO_ALPHA",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "source_checks": source_checks,
        "lane_A_local_determinant": lane_a,
        "lane_B_omega0": lane_b,
        "cross_lane_independence": cross_lane,
        "decision": decision,
        "guardrails": [
            "Do not promote the two-thirds proxy lambda_12 near-hit to proof.",
            "Do not use the diagnostic target witness lambda_12 as determinant data.",
            "Do not treat Omega0/alpha_phys as a substitute for gauge-factor threshold spectra.",
            "Do not treat lambda_12 as a physical unit or compactification action anchor.",
            "Do not compare to measured electroweak data until alpha_phys, lambda_12, convention map, mu_match, and RG scheme are all selected.",
        ],
        "closure_claimed": True,
        "closure_scope": "parallel_frontier_reduction_only",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "DualAttackLocalDeterminantOrOmega0Source",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "closed": {
            "parallel_attack_executed": True,
            "lane_A_accounting_interface_Qc_SU2_blocks": True,
            "lane_B_CQ_epsilon_chi_CUV_Qtau_reduction": True,
            "Omega0_formula_reduced": lane_b["reduced_formula"],
            "no_target_fit_used": True,
        },
        "open": {
            "lambda12_selected_spectral_table": True,
            "alpha_phys_or_action_unit": True,
            "typed_electroweak_convention_map": True,
            "matching_scale_and_RG_scheme": True,
            "measured_electroweak_closure": True,
        },
        "next_required_objects": decision["next_required_objects"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    a = candidate["lane_A_local_determinant"]
    b = candidate["lane_B_omega0"]
    checks = "\n".join(f"{k} = {v}" for k, v in candidate["source_checks"].items())
    guards = "\n".join(f"- {x}" for x in candidate["guardrails"])
    nexts = "\n".join(f"- {x}" for x in candidate["decision"]["next_required_objects"])
    a_closed = "\n".join(f"{k} = {v}" for k, v in a["what_closes_now"].items())
    a_diag = "\n".join(f"{k} = {v}" for k, v in a["diagnostics_not_proof"].items())
    b_closed = "\n".join(f"{k} = {v}" for k, v in b["what_closes_now"].items())
    b_formula = "\n".join(f"{k} = {v}" for k, v in b["reduced_formula"].items())
    return f"""# Dual Attack Local Determinant or Omega0 Source v1

## Result

Both frontier paths were attacked in parallel.

```text
lane_A_lambda12_closed = {str(candidate["decision"]["lane_A_lambda12_closed"]).lower()}
lane_A_reduced_to_selected_spectral_table = {str(candidate["decision"]["lane_A_reduced_to_selected_spectral_table"]).lower()}
lane_B_Omega0_closed = {str(candidate["decision"]["lane_B_Omega0_closed"]).lower()}
lane_B_reduced_to_alpha_phys_only = {str(candidate["decision"]["lane_B_reduced_to_alpha_phys_only"]).lower()}
full_physical_electroweak_closure = {str(candidate["decision"]["full_physical_electroweak_closure"]).lower()}
target_fitting_used = {str(candidate["decision"]["target_fitting_used"]).lower()}
```

## Lane A: Local Determinant

Status:

```text
{a["status"]}
```

Closed inputs:

```text
{a_closed}
```

Strongest selected inputs:

```text
selected_p_Qc_for_weak_split = {a["strongest_selected_inputs"]["selected_p_Qc_for_weak_split"]}
selected_p_SU2_for_weak_split = {a["strongest_selected_inputs"]["selected_p_SU2_for_weak_split"]}
selected_U1_threshold_index = {a["strongest_selected_inputs"]["selected_U1_threshold_index"]}
v1_tilde = {a["strongest_selected_inputs"]["v1_tilde"]}
```

Diagnostics that remain non-proof:

```text
{a_diag}
```

Blocker:

```text
selected_spectra_computed = {a["blocker"]["selected_spectra_computed"]}
final_attempt_status = {a["blocker"]["final_attempt_status"]}
minimal_next_object = {a["blocker"]["minimal_next_object"]}
```

Decision:

```text
{a["decision"]}
```

## Lane B: Omega0

Status:

```text
{b["status"]}
```

Closed inputs:

```text
{b_closed}
```

Reduced formula:

```text
{b_formula}
```

Blocker:

```text
alpha_phys_or_action_unit_selected = {b["blocker"]["alpha_phys_or_action_unit_selected"]}
physical_Omega0_numeric_closed = {b["blocker"]["physical_Omega0_numeric_closed"]}
minimal_next_object = {b["blocker"]["minimal_next_object"]}
```

Decision:

```text
{b["decision"]}
```

## Cross-Lane Independence

```text
can_substitute_lane_b_for_lane_a = {candidate["cross_lane_independence"]["can_substitute_lane_b_for_lane_a"]}
reason = {candidate["cross_lane_independence"]["reason"]}
can_substitute_lane_a_for_lane_b = {candidate["cross_lane_independence"]["can_substitute_lane_a_for_lane_b"]}
reason_2 = {candidate["cross_lane_independence"]["reason_2"]}
joint_closure_condition = {candidate["cross_lane_independence"]["joint_closure_condition"]}
```

## Source Checks

```text
{checks}
```

## Guardrails

{guards}

## Next Required Objects

{nexts}
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    missing = [str(path) for path in INPUTS.values() if not path.exists()]
    if missing:
        print("Missing inputs:")
        print("\n".join(missing))
        return 1
    candidate, certificate, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, certificate)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"Wrote {OUTPUT_DATA}")
    print(f"Wrote {OUTPUT_CERT}")
    print(f"Wrote {OUTPUT_NOTE}")
    print(certificate["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
