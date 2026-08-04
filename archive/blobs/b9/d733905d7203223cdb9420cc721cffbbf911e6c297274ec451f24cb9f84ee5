"""Build CONST-GR-01 G4 Omega0 physical-unit or one-metrology primitive packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
GR_REPO = TEXPAPERS / "mtt-protospinor-gr-response-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_gr_01_absolute_scale_g4_omega0_physical_unit_or_one_metrology_primitive"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STRICT_ATTEMPT = BASE / "strict_same_branch_metrology_attempt.packet.json"
PRIMITIVE_CONTRACT = BASE / "one_metrology_primitive_contract.packet.json"
DOWNSTREAM = BASE / "downstream_formulae_and_falsification.packet.json"
PORTFOLIO = BASE / "portfolio_handoff.packet.json"
BOUNDARY = BASE / "g4_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_GR_01_AbsoluteScale_G4_Omega0PhysicalUnitOrOneMetrologyPrimitive_v1.md"

STATUS = "MTT_CONST_GR_01_G4_OMEGA0_OR_ONE_METROLOGY_PRIMITIVE_BUILT"


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

    g3_path = DATA / "const_gr_01_absolute_scale_g3_cuv_qtau_omega0_source_data.candidate.json"
    g3_boundary_path = DATA / "const_gr_01_absolute_scale_g3_cuv_qtau_omega0_source_data" / "g3_boundary.packet.json"
    alpha_primitive_path = DATA / "const_em_01_alpha1_universal_primitive_or_nogo" / "one_universal_primitive.packet.json"
    weak_b42_path = DATA / "const_ew_02_weak_mixing_b42_one_primitive_physical_bridge.candidate.json"
    weak_b45_path = DATA / "const_ew_02_weak_mixing_b45_universal_primitive_portfolio_handoff.candidate.json"
    targets_path = DATA / "constant_frontier_ledger" / "individual_constant_targets.packet.json"

    metrology_no_go_path = GR_REPO / "certificates" / "dimensional_metrology_no_go_and_relative_closure_theorem_certificate.json"
    same_branch_path = GR_REPO / "certificates" / "same_branch_physical_clock_or_length_source_search_certificate.json"
    omega0_path = GR_REPO / "certificates" / "selected_physical_omega0_source_theorem_certificate.json"
    omega_convention_path = GR_REPO / "certificates" / "selected_omega_convention_theorem_certificate.json"
    semigroup_path = GR_REPO / "certificates" / "selected_sharp_semigroup_bound_theorem_certificate.json"
    one_anchor_gr_path = GR_REPO / "certificates" / "one_anchor_gr_normalization_propagation_certificate.json"

    g3 = load(g3_path)
    g3_boundary = load(g3_boundary_path)
    alpha_primitive = load(alpha_primitive_path)
    weak_b42 = load(weak_b42_path)
    weak_b45 = load(weak_b45_path)
    targets = load(targets_path)
    metrology_no_go = load(metrology_no_go_path)
    same_branch = load(same_branch_path)
    omega0 = load(omega0_path)
    omega_convention = load(omega_convention_path)
    semigroup = load(semigroup_path)
    one_anchor_gr = load(one_anchor_gr_path)

    strict_attempt = {
        "schema": "MTTConstGR01G4StrictSameBranchMetrologyAttempt.v1",
        "status": "STRICT_SAME_BRANCH_METROLOGY_DERIVATION_BLOCKED_BY_SCALE_SYMMETRY",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G4-STRICT-SAME-BRANCH-METROLOGY-ATTEMPT",
        "inputs": {
            "G3_candidate": rel(g3_path),
            "dimensional_metrology_no_go": rel(metrology_no_go_path),
            "same_branch_clock_or_length_source": rel(same_branch_path),
            "selected_physical_omega0_source": rel(omega0_path),
            "selected_sharp_semigroup_bound": rel(semigroup_path),
        },
        "strict_evidence_closed": {
            "same_branch_tau_role_sourced": same_branch["verdict"]["same_branch_physical_clock_or_length_source_found"],
            "relative_physical_scale_solution_closed": metrology_no_go["closure_result"]["relative_physical_closure"],
            "C_Q_equals_1_on_selected_exact_branch": semigroup["omega0_formula"]["C_Q"] == 1.0,
            "epsilon_adm_equals_1_over_448": semigroup["closed_inputs"]["epsilon_is_one_over_448"],
            "chi_omega_convention_closed": omega_convention["convention_selection"]["chi_omega"] == 1.0,
            "internal_CUV_Qtau_ratio_imported": g3["internal_CUV_Qtau_ratio_accepted_for_shared_scale_data"],
        },
        "current_no_go": metrology_no_go["no_go"],
        "reason_no_strict_promotion": "All current same-branch data fix dimensionless ratios and the physical role of tau, but the positive scaling symmetry leaves the absolute physical unit unidentified.",
        "strict_no_knob_Omega0_derived": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    solution_family = metrology_no_go["solution_family"]
    primitive_contract = {
        "schema": "MTTConstGR01G4OneMetrologyPrimitiveContract.v1",
        "status": "ONE_UNIVERSAL_METROLOGY_PRIMITIVE_TIER_DEFINED_NOT_NO_KNOB",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G4-ONE-METROLOGY-PRIMITIVE-CONTRACT",
        "primitive_names": {
            "length": "L0",
            "energy": "E0",
            "proper_time_width": "T0",
            "inverse_length": "Omega0",
        },
        "omega0_convention_reconciliation": {
            "selected_convention": "Omega0 := Lambda_eff,phys",
            "selected_source": "Selected_Omega_Convention_Theorem_v1",
            "legacy_factor_warning": "Some imported one-anchor packets write Omega0=sqrt(tau_int)/L0 or sqrt(tau_int)*E0. G4 keeps those as legacy coordinate formulae and uses the selected convention Omega0=1/L0=E0 for the active physical-unit gate.",
            "reconciled": True,
        },
        "legacy_coordinate_choices_from_imported_metrology_no_go": solution_family,
        "equivalent_coordinate_choices": {
            "length_anchor": {
                "anchor": "choose a physical coherent length L0, not fitted to the target being predicted",
                "alpha_phys": "tau_int / L0^2",
                "tau_phys": "L0^2",
                "ell_coh": "L0",
                "Lambda_eff": "1 / L0",
                "Omega0": "1 / L0",
            },
            "energy_anchor": {
                "anchor": "choose a physical coherent energy E0, not fitted to the target being predicted",
                "alpha_phys": "tau_int * E0^2",
                "tau_phys": "1 / E0^2",
                "ell_coh": "1 / E0",
                "Lambda_eff": "E0",
                "Omega0": "E0",
            },
            "tau_anchor": {
                "anchor": "choose a physical proper-time/coherent-width T0 with units L^2=E^-2",
                "alpha_phys": "tau_int / T0",
                "tau_phys": "T0",
                "ell_coh": "sqrt(T0)",
                "Lambda_eff": "1 / sqrt(T0)",
                "Omega0": "1 / sqrt(T0)",
            },
            "omega0_anchor": {
                "anchor": "choose a physical damping/admissibility inverse-length Omega0, not fitted to any target",
                "Omega0": "Omega0",
                "alpha_phys": "Omega0^2 * tau_int",
                "tau_phys": "tau_int / alpha_phys = 1 / Omega0^2",
                "ell_coh": "1 / Omega0",
                "Lambda_eff": "Omega0",
                "L0": "1 / Omega0",
                "E0": "Omega0",
            },
        },
        "acceptance_policy": {
            "allowed_if": [
                "declared exactly once as a universal metrology primitive",
                "selected before comparison to measured constants",
                "not adjusted per sector, per constant, or per observable",
                "all downstream results state dependence on the primitive unless a later theorem derives it",
                "can be falsified by cross-constant disagreement after one external metrology selection",
            ],
            "forbidden_if": [
                "chosen from alpha, weak angle, G_N, M_Pl, masses, cosmology, TeV, or any target being predicted",
                "renamed as strict no-knob closure",
                "varied between alpha, weak mixing, GR, Higgs, or cosmology",
                "hidden inside a unit convention while claiming physical prediction",
            ],
        },
        "parameter_budget": {
            "new_sector_specific_parameters": 0,
            "new_universal_metrology_primitives": 1,
            "strict_no_knob_primitives": 0,
            "accepted_tier": "ONE_UNIVERSAL_PRIMITIVE_TIER_ONLY",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    omega_factor = omega_convention["reduced_formula"]["Omega0_over_sqrt_alpha_phys"]
    downstream = {
        "schema": "MTTConstGR01G4DownstreamFormulaeAndFalsification.v1",
        "status": "DOWNSTREAM_FORMULAE_AND_FALSIFICATION_RULES_BUILT",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G4-DOWNSTREAM-FORMULAE-AND-FALSIFICATION",
        "inputs": {
            "alpha_one_primitive": rel(alpha_primitive_path),
            "weak_mixing_B42": rel(weak_b42_path),
            "one_anchor_GR": rel(one_anchor_gr_path),
        },
        "shared_formulae": {
            "tau_int": metrology_no_go["closure_result"]["numeric_coefficients"]["tau_int"],
            "sqrt_tau_int": metrology_no_go["closure_result"]["numeric_coefficients"]["sqrt_tau_int"],
            "Omega0_over_sqrt_alpha_phys": omega_factor,
            "alpha_from_L0": "alpha_phys = tau_int / L0^2",
            "alpha_from_E0": "alpha_phys = tau_int * E0^2",
            "Omega0_from_L0_selected_convention": "Omega0 = 1 / L0",
            "Omega0_from_E0_selected_convention": "Omega0 = E0",
            "legacy_imported_Omega0_from_L0": "sqrt(tau_int) / L0",
            "legacy_imported_Omega0_from_E0": "sqrt(tau_int) * E0",
            "GR_G_eff_from_L0": one_anchor_gr["solution"]["length_anchor_family"]["G_eff_phys"],
            "GR_G_eff_from_E0": one_anchor_gr["solution"]["energy_anchor_family"]["G_eff_phys"],
            "weak_mixing_bridge": "K_phys, alpha_phys, and mu_match collapse to the same E0/L0 primitive in the B42 tier",
        },
        "falsification_rules": [
            "After one allowed metrology primitive is selected, alpha, weak mixing, and GR cannot independently retune it.",
            "A mismatch in any downstream sector falsifies the one-primitive branch or one of its source maps.",
            "Measured constants may be used for comparison after selection, not to choose the primitive.",
            "A later strict source theorem may replace the primitive with a derived value; until then the tier remains non-no-knob.",
        ],
        "physical_predictions_now": {
            "alpha_numeric": False,
            "weak_angle_numeric": False,
            "Newton_or_Planck_numeric": False,
            "conditional_relations": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    target_rows = {row["label"]: row for row in targets["targets"]}
    portfolio = {
        "schema": "MTTConstGR01G4PortfolioHandoff.v1",
        "status": "ABSOLUTE_SCALE_REDUCED_TO_ONE_METROLOGY_PRIMITIVE_MOVE_TO_NEXT_TEST",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G4-PORTFOLIO-HANDOFF",
        "portfolio_state": {
            "alpha": "down to same E0/L0 primitive or strict source upgrade",
            "weak_mixing": weak_b45["status"],
            "GR_absolute_scale": "relative scale closed; one metrology primitive tier defined; strict physical unit source open",
            "shared_primitive_count": 1,
            "sector_specific_new_parameters": 0,
        },
        "next_constant_candidates": [
            {
                "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD",
                "why": "Tests whether the same action/metrology primitive and threshold-kernel normalization can propagate into the Higgs sector without adding a Higgs-specific knob.",
                "priority": 1,
                "target_row": target_rows["CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD"],
            },
            {
                "label": "CONST-CP-01 / FINITE-PHASE-ORIENTATION",
                "why": "Likely probes a different universal primitive class; useful after the metrology primitive is frozen or if we want an independent primitive-family check.",
                "priority": 2,
                "target_row": target_rows["CONST-CP-01 / FINITE-PHASE-ORIENTATION"],
            },
            {
                "label": "CONST-COSMO-01 / BOUNDARY-ADMISSIBILITY",
                "why": "Potentially sensitive to absolute scale, but current readiness is lower and target-backsolve risk is higher.",
                "priority": 3,
                "target_row": target_rows["CONST-COSMO-01 / BOUNDARY-ADMISSIBILITY"],
            },
        ],
        "selected_next": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD",
        "reason": "Alpha, weak mixing, and GR are already all waiting on the same metrology primitive. The strongest anti-cycle move is to test a new sector that may reuse the primitive without selecting it from the target.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstGR01G4Boundary.v1",
        "status": "G4_METROLOGY_TIER_FROZEN_STRICT_SOURCE_OPEN",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G4-BOUNDARY",
        "closed_or_decided_now": {
            "strict_same_branch_metrology_attempt_evaluated": True,
            "relative_physical_scale_solution_confirmed_closed": True,
            "absolute_scale_no_go_confirmed_current_formalization": True,
            "Omega0_convention_reconciled": True,
            "one_universal_metrology_primitive_contract_defined": True,
            "downstream_falsification_rules_defined": True,
            "portfolio_handoff_selected": True,
        },
        "still_open": {
            "strict_same_branch_physical_unit_theorem": True,
            "physical_Omega0_selected": True,
            "selected_physical_E0_or_L0_value": True,
            "Newton_or_Planck_prediction": True,
            "strict_no_knob_absolute_scale_closure": True,
            "one_primitive_cross_constant_validation": True,
        },
        "anti_cycle_delta_from_G3": {
            "G3": "split source-data provenance from the active physical unit gate",
            "G4": "evaluates the physical unit gate and freezes the one-metrology-primitive tier with falsification rules",
            "not_repeated": [
                "not reopening C_UV/Q_tau as active physical blocker",
                "not pretending one primitive is no-knob closure",
                "not selecting the primitive from alpha, weak angle, Newton, Planck, masses, cosmology, or TeV calibration",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstGR01G4NextWork.v1",
        "status": "NEXT_WORKORDER_CONST_HIGGS_01_SHARED_METROLOGY_TEST",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G5-NEXT",
        "primary": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H1-SHARED-METROLOGY-PRIMITIVE-TEST",
            "task": "Attack the Higgs quartic/threshold sector as the next cross-constant test of the same E0/L0/action-normalization primitive, without using measured Higgs mass or quartic as a selector.",
        },
        "parking_lot": {
            "label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G4B-SAME-BRANCH-PHYSICAL-ROD-CLOCK-THEOREM",
            "task": "Return here if the corpus emits an internally constructed physical rod/clock process that selects Omega0/E0/L0 without target data.",
        },
    }

    candidate = {
        "candidate": "MTTConstGR01AbsoluteScaleG4Omega0PhysicalUnitOrOneMetrologyPrimitive",
        "status": STATUS,
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G4-OMEGA0-PHYSICAL-UNIT-OR-ONE-METROLOGY-PRIMITIVE",
        "output_packets": {
            "strict_same_branch_metrology_attempt": rel(STRICT_ATTEMPT),
            "one_metrology_primitive_contract": rel(PRIMITIVE_CONTRACT),
            "downstream_formulae_and_falsification": rel(DOWNSTREAM),
            "portfolio_handoff": rel(PORTFOLIO),
            "g4_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTGR01G4Omega0OrOneMetrologyPrimitiveTheorem",
            "proved": True,
            "statement": (
                "In the current corpus, strict same-branch derivation of the absolute physical unit Omega0/E0/L0 is blocked by a one-dimensional scale symmetry, while the relative physical scale solution is closed. The correct non-cyclic move is to define a one-universal-metrology-primitive tier with explicit guardrails and falsification rules, keep strict no-knob metrology as an open upgrade, and move to another constant to test the same primitive."
            ),
        },
        "relative_physical_scale_solution_closed": True,
        "Omega0_convention_reconciled": True,
        "strict_same_branch_Omega0_derived": False,
        "one_universal_metrology_primitive_tier_defined": True,
        "selected_metrology_primitive_value": False,
        "selected_next_constant": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD",
        "measured_Newton_or_Planck_derived": False,
        "strict_no_knob_absolute_scale_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_GR_01_AbsoluteScale_G4_Omega0PhysicalUnitOrOneMetrologyPrimitive_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "relative_physical_scale_solution_closed": True,
        "Omega0_convention_reconciled": True,
        "strict_same_branch_Omega0_derived": False,
        "one_universal_metrology_primitive_tier_defined": True,
        "selected_metrology_primitive_value": False,
        "selected_next_constant": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD",
        "strict_no_knob_absolute_scale_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST GR 01 Absolute Scale G4 Omega0 Physical Unit or One Metrology Primitive v1

Status: `{STATUS}`

Label: `CONST-GR-01 / ABSOLUTE-SCALE-GN / G4-OMEGA0-PHYSICAL-UNIT-OR-ONE-METROLOGY-PRIMITIVE`

## Result

```text
relative physical scale solution closed          True
strict same-branch Omega0/E0/L0 derived          False
one-universal-metrology primitive tier defined   True
selected primitive value                         False
Newton/Planck prediction                         False
selected next constant                           CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD
```

The strict current-corpus result is the dimensional metrology no-go:

```text
alpha_phys -> s^2 alpha_phys
Lambda_eff -> s Lambda_eff
ell_coh    -> ell_coh/s
```

leaves all selected dimensionless branch data invariant.  So there is no
honest arithmetic step that turns the relative scale solution into an absolute
physical number without either:

```text
1. an internally constructed physical rod/clock theorem, or
2. one explicitly declared universal metrology primitive.
```

## One-Primitive Tier

The allowed primitive may be written as `L0`, `E0`, `T0`, or `Omega0`; these are
coordinate choices for the same physical metrology slot.

It is allowed only if selected once, before target comparison, and reused
unchanged across sectors.  It is forbidden to choose it from alpha, weak angle,
Newton, Planck, masses, cosmology, TeV calibration, or any target being
predicted.  This tier is not strict no-knob closure.

## Next

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H1-SHARED-METROLOGY-PRIMITIVE-TEST`
"""

    for path, payload in [
        (STRICT_ATTEMPT, strict_attempt),
        (PRIMITIVE_CONTRACT, primitive_contract),
        (DOWNSTREAM, downstream),
        (PORTFOLIO, portfolio),
        (BOUNDARY, boundary),
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
