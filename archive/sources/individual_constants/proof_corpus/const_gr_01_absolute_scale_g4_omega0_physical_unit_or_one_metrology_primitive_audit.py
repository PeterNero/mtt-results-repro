"""Audit CONST-GR-01 G4 Omega0 physical-unit or one-metrology primitive packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_gr_01_absolute_scale_g4_omega0_physical_unit_or_one_metrology_primitive"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
STRICT_ATTEMPT = BASE / "strict_same_branch_metrology_attempt.packet.json"
PRIMITIVE_CONTRACT = BASE / "one_metrology_primitive_contract.packet.json"
DOWNSTREAM = BASE / "downstream_formulae_and_falsification.packet.json"
PORTFOLIO = BASE / "portfolio_handoff.packet.json"
BOUNDARY = BASE / "g4_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_GR_01_AbsoluteScale_G4_Omega0PhysicalUnitOrOneMetrologyPrimitive_v1.md"

STATUS = "MTT_CONST_GR_01_G4_OMEGA0_OR_ONE_METROLOGY_PRIMITIVE_BUILT"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    strict_attempt = load(STRICT_ATTEMPT)
    primitive_contract = load(PRIMITIVE_CONTRACT)
    downstream = load(DOWNSTREAM)
    portfolio = load(PORTFOLIO)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("strict_attempt", strict_attempt),
        ("primitive_contract", primitive_contract),
        ("downstream", downstream),
        ("portfolio", portfolio),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["relative_physical_scale_solution_closed"] is True, "relative closure")
    require(candidate["Omega0_convention_reconciled"] is True, "Omega0 convention")
    require(candidate["strict_same_branch_Omega0_derived"] is False, "Omega0 overderived")
    require(candidate["one_universal_metrology_primitive_tier_defined"] is True, "primitive tier")
    require(candidate["selected_metrology_primitive_value"] is False, "primitive value")
    require(candidate["selected_next_constant"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD", "next constant")
    require(candidate["measured_Newton_or_Planck_derived"] is False, "Newton overclosed")
    require(candidate["strict_no_knob_absolute_scale_closure"] is False, "strict overclosed")

    require(strict_attempt["status"] == "STRICT_SAME_BRANCH_METROLOGY_DERIVATION_BLOCKED_BY_SCALE_SYMMETRY", "strict status")
    evidence = strict_attempt["strict_evidence_closed"]
    require(evidence["same_branch_tau_role_sourced"] is True, "tau source")
    require(evidence["relative_physical_scale_solution_closed"] is True, "relative")
    require(evidence["C_Q_equals_1_on_selected_exact_branch"] is True, "C_Q")
    require(evidence["epsilon_adm_equals_1_over_448"] is True, "epsilon")
    require(evidence["chi_omega_convention_closed"] is True, "chi")
    require(evidence["internal_CUV_Qtau_ratio_imported"] is True, "internal ratio")
    require(strict_attempt["current_no_go"]["free_parameter_count_for_absolute_units"] == 1, "free count")
    require(strict_attempt["strict_no_knob_Omega0_derived"] is False, "strict Omega0")

    require(primitive_contract["status"] == "ONE_UNIVERSAL_METROLOGY_PRIMITIVE_TIER_DEFINED_NOT_NO_KNOB", "contract status")
    require(primitive_contract["omega0_convention_reconciliation"]["reconciled"] is True, "omega convention")
    require(primitive_contract["equivalent_coordinate_choices"]["length_anchor"]["Omega0"] == "1 / L0", "length Omega0")
    require(primitive_contract["equivalent_coordinate_choices"]["energy_anchor"]["Omega0"] == "E0", "energy Omega0")
    require(primitive_contract["equivalent_coordinate_choices"]["omega0_anchor"]["Omega0"] == "Omega0", "Omega anchor")
    require(primitive_contract["parameter_budget"]["new_sector_specific_parameters"] == 0, "sector params")
    require(primitive_contract["parameter_budget"]["new_universal_metrology_primitives"] == 1, "primitive count")
    require(primitive_contract["parameter_budget"]["strict_no_knob_primitives"] == 0, "strict count")
    require("renamed as strict no-knob closure" in primitive_contract["acceptance_policy"]["forbidden_if"], "no-knob guard")
    require("chosen from alpha, weak angle, G_N, M_Pl, masses, cosmology, TeV, or any target being predicted" in primitive_contract["acceptance_policy"]["forbidden_if"], "target guard")
    require(primitive_contract["equivalent_coordinate_choices"]["omega0_anchor"]["Omega0"] if "Omega0" in primitive_contract["equivalent_coordinate_choices"]["omega0_anchor"] else True, "omega0 anchor shape")

    require(downstream["status"] == "DOWNSTREAM_FORMULAE_AND_FALSIFICATION_RULES_BUILT", "downstream status")
    formulae = downstream["shared_formulae"]
    require(formulae["tau_int"] == 0.40698621549433234, "tau")
    require(formulae["Omega0_over_sqrt_alpha_phys"] == 1.5675093859261626, "omega factor")
    require(formulae["Omega0_from_L0_selected_convention"] == "Omega0 = 1 / L0", "Omega0 L0 selected")
    require(formulae["Omega0_from_E0_selected_convention"] == "Omega0 = E0", "Omega0 E0 selected")
    require(formulae["legacy_imported_Omega0_from_L0"] == "sqrt(tau_int) / L0", "legacy L0")
    require(formulae["GR_G_eff_from_L0"] == "0.29759362932431804 * L0^2", "GR L0")
    require(formulae["GR_G_eff_from_E0"] == "0.29759362932431804 / E0^2", "GR E0")
    require(downstream["physical_predictions_now"]["conditional_relations"] is True, "conditional")
    require(downstream["physical_predictions_now"]["Newton_or_Planck_numeric"] is False, "Newton numeric")
    require("A mismatch in any downstream sector falsifies the one-primitive branch or one of its source maps." in downstream["falsification_rules"], "falsification")

    require(portfolio["status"] == "ABSOLUTE_SCALE_REDUCED_TO_ONE_METROLOGY_PRIMITIVE_MOVE_TO_NEXT_TEST", "portfolio status")
    require(portfolio["portfolio_state"]["shared_primitive_count"] == 1, "portfolio primitive count")
    require(portfolio["portfolio_state"]["sector_specific_new_parameters"] == 0, "portfolio sector params")
    require(portfolio["selected_next"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD", "portfolio next")
    require(portfolio["next_constant_candidates"][0]["label"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD", "candidate priority")

    closed = boundary["closed_or_decided_now"]
    open_ = boundary["still_open"]
    require(closed["strict_same_branch_metrology_attempt_evaluated"] is True, "boundary strict")
    require(closed["Omega0_convention_reconciled"] is True, "boundary convention")
    require(closed["one_universal_metrology_primitive_contract_defined"] is True, "boundary primitive")
    require(closed["portfolio_handoff_selected"] is True, "boundary handoff")
    require(open_["strict_same_branch_physical_unit_theorem"] is True, "strict open")
    require(open_["one_primitive_cross_constant_validation"] is True, "validation open")
    require("not pretending one primitive is no-knob closure" in boundary["anti_cycle_delta_from_G3"]["not_repeated"], "anti-cycle")

    require(next_work["primary"]["label"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H1-SHARED-METROLOGY-PRIMITIVE-TEST", "primary")
    require(next_work["parking_lot"]["label"] == "CONST-GR-01 / ABSOLUTE-SCALE-GN / G4B-SAME-BRANCH-PHYSICAL-ROD-CLOCK-THEOREM", "parking")

    require(cert["status"] == STATUS, "cert status")
    require(cert["relative_physical_scale_solution_closed"] is True, "cert relative")
    require(cert["Omega0_convention_reconciled"] is True, "cert convention")
    require(cert["strict_same_branch_Omega0_derived"] is False, "cert strict")
    require(cert["one_universal_metrology_primitive_tier_defined"] is True, "cert primitive")
    require(cert["selected_metrology_primitive_value"] is False, "cert value")
    require("G4-OMEGA0-PHYSICAL-UNIT" in note and "H1-SHARED-METROLOGY-PRIMITIVE-TEST" in note, "note")

    print("CONST-GR-01 G4 Omega0/one-metrology primitive audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
