"""Audit CONST-EW-02 B25 internal lambda12 / physical frontier import."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b25_internal_lambda12_physical_frontier"
DATA = ROOT / "candidate_data"
BASE = DATA / SLUG
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(DATA / f"{SLUG}.candidate.json")
    lam = load(BASE / "internal_lambda12_import.packet.json")
    physical = load(BASE / "physical_anchor_rg_frontier.packet.json")
    c1 = load(BASE / "primitive_c1_atom_cutset_import.packet.json")
    boundary = load(BASE / "weak_mixing_b25_boundary.packet.json")
    next_work = load(BASE / "next_labeled_workorder.packet.json")
    cert = load(CERT)

    for name, packet in [
        ("candidate", candidate),
        ("lambda", lam),
        ("physical", physical),
        ("c1", c1),
        ("boundary", boundary),
        ("cert", cert),
    ]:
        require(packet["observed_data_used_as_selector"] is False, f"{name} used observed selector")
        require(packet["target_fitting_used"] is False, f"{name} used target fitting")
        require(packet["closure_claimed"] is False, f"{name} claimed closure")

    require(candidate["theorem"]["proved"] is True, "B25 theorem did not prove")
    require(candidate["internal_lambda_12_closed"] is True, "internal lambda12 not closed")
    require(abs(candidate["internal_lambda_12_value"] - 2.6179362173268497) < 1e-15, "lambda12 value drifted")
    require(candidate["u_dyn_source_derived"] is True, "u_dyn not preserved")
    require(candidate["physical_weak_angle_closure"] is False, "physical weak angle overclosed")
    require(candidate["strict_full_no_knob_closure"] is False, "strict closure overclosed")

    require(lam["closure_scope"] == "dimensionless_internal_weaksplit_threshold_only", "lambda scope wrong")
    require(lam["what_closes"]["internal_lambda_12"] is True, "lambda import not closed")
    require(abs(lam["what_closes"]["internal_lambda_12_value"] - 2.6179362173268497) < 1e-15, "lambda import value wrong")
    require(abs(lam["what_closes"]["internal_Delta_G12_value"] - 0.08450302790361214) < 1e-15, "Delta import value wrong")
    require(lam["guardrails"]["uses_observed_electroweak_data"] is False, "lambda import used observed EW")
    require(lam["guardrails"]["claims_measured_electroweak_closure"] is False, "lambda import overclaims measured EW")
    require(lam["not_closed"]["physical_K_gauge_anchor_closed"] is False, "lambda import closes physical anchor")
    require(lam["not_closed"]["matching_scale_and_RG_scheme_closed"] is False, "lambda import closes RG/matching")

    require(physical["decision"]["internal_lambda_12_closed"] is True, "physical frontier lost internal lambda")
    require(physical["decision"]["physical_gauge_action_anchor_closed"] is False, "physical anchor overclosed")
    require(physical["decision"]["matching_scale_closed"] is False, "matching scale overclosed")
    require(physical["decision"]["RG_scheme_closed"] is False, "RG scheme overclosed")
    require(physical["decision"]["measured_electroweak_closure"] is False, "measured EW overclosed")
    require(physical["u_phys_status"]["u_phys_source_derived"] is False, "u_phys overderived")
    require(physical["u_phys_status"]["single_calibration_allowed_under_B23"] is True, "B23 calibration lane not preserved")

    require(c1["interface"]["assembly_theorem_proved"] is True, "C1 assembly theorem missing")
    require(c1["interface"]["primitive_C1_atoms_emitted"] is False, "C1 atoms overemitted")
    require(c1["interface"]["missing_atom_count"] == 24, "C1 missing atom count wrong")
    require(c1["interface"]["A_selected_computable"] is False, "A_selected overcomputable")
    require(c1["interface"]["b_selected_computable"] is False, "b_selected overcomputable")
    require(c1["fill_attempt"]["fill_attempt_executed"] is True, "C1 fill attempt not executed")
    require(c1["fill_attempt"]["current_corpus_supplies_selected_atom_payload"] is False, "C1 payload overclaimed")
    require(c1["fill_attempt"]["canonical_zero_branch_selected"] is False, "zero branch overselected")
    require(c1["fill_attempt"]["missing_leaf_count"] == 40, "C1 missing leaf count wrong")

    require(boundary["closed_now"]["internal_lambda_12_closed"] is True, "boundary lambda not closed")
    require(boundary["closed_now"]["physical_frontier_reduced_to_anchor_mu_RG"] is True, "boundary physical frontier not reduced")
    require(boundary["still_open"]["physical_gauge_action_anchor_or_u_phys"] is True, "boundary u_phys not open")
    require(boundary["still_open"]["matching_scale_mu_match"] is True, "boundary mu not open")
    require(boundary["still_open"]["RG_and_threshold_scheme"] is True, "boundary RG not open")
    require(boundary["still_open"]["all_24_primitive_C1_atoms"] is True, "boundary C1 atoms not open")
    require(boundary["forbidden_claim"] == "measured/physical weak angle, alpha, or full electroweak closure", "forbidden claim wrong")

    require(next_work["active_label"] == "CONST-EW-02 / WEAK-MIXING / B26-PHYSICAL-GAUGE-ANCHOR-OR-C1-ATOMS", "wrong B26 label")
    require("GAUGEKINETIC-NORMALIZATION" in next_work["primary"]["label"], "primary B26 route wrong")
    require("PRIMITIVE-C1-SOURCEVALUE" in next_work["parallel"]["label"], "parallel B26 route wrong")

    require(cert["internal_lambda_12_closed"] is True, "certificate lambda not closed")
    require(cert["physical_gauge_action_anchor_closed"] is False, "certificate physical anchor overclosed")
    require(cert["primitive_C1_atoms_emitted"] is False, "certificate C1 atoms overemitted")
    require(cert["missing_atom_count"] == 24, "certificate C1 count wrong")
    require(cert["physical_weak_angle_closure"] is False, "certificate weak angle overclosed")

    print("CONST-EW-02 B25 internal lambda12 / physical frontier audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
