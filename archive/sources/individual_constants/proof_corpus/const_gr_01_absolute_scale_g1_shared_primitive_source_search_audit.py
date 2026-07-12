"""Audit CONST-GR-01 G1 shared-primitive source-search packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_gr_01_absolute_scale_g1_shared_primitive_source_search"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
SHARED_IMPORT = BASE / "shared_primitive_import.packet.json"
GR_SCAN = BASE / "gr_modal_gap_source_scan.packet.json"
ABS_GATE = BASE / "absolute_scale_gate.packet.json"
SUPERSET = BASE / "superset_strategy_status.packet.json"
PORTFOLIO = BASE / "portfolio_status.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_GR_01_AbsoluteScale_G1_SharedPrimitiveSourceSearch_v1.md"

STATUS = "MTT_CONST_GR_01_G1_SHARED_PRIMITIVE_SOURCE_SEARCH_BUILT"


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
    shared_import = load(SHARED_IMPORT)
    gr_scan = load(GR_SCAN)
    absolute_gate = load(ABS_GATE)
    superset = load(SUPERSET)
    portfolio = load(PORTFOLIO)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("shared_import", shared_import),
        ("gr_scan", gr_scan),
        ("absolute_gate", absolute_gate),
        ("superset", superset),
        ("portfolio", portfolio),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["one_anchor_GR_family_closed"] is True, "one-anchor GR")
    require(candidate["shared_primitive_portfolio_extended_to_GR"] is True, "GR portfolio")
    require(candidate["selected_physical_E0_or_L0_value"] is False, "primitive value overclosed")
    require(candidate["measured_Newton_or_Planck_derived"] is False, "Newton overclosed")
    require(candidate["strict_no_knob_absolute_scale_closure"] is False, "strict overclosed")

    require(shared_import["status"] == "SHARED_E0_L0_PRIMITIVE_IMPORTED_FROM_ALPHA_WEAK_AND_GR", "shared status")
    require("energy" in shared_import["shared_primitive_options"], "energy primitive missing")
    require("length" in shared_import["shared_primitive_options"], "length primitive missing")
    require(shared_import["gr_selected_internal_row"]["N"] == 448, "selected row N")
    require(abs(shared_import["gr_selected_internal_row"]["tau_int"] - 0.40698621549433234) < 1e-15, "tau")
    require(shared_import["gr_one_anchor_family"]["length_anchor"]["G_eff_over_L0_squared"] == 0.29759362932431804, "G/L0")
    require(shared_import["gr_one_anchor_family"]["energy_anchor"]["G_eff_times_E0_squared"] == 0.29759362932431804, "G*E0")

    require(gr_scan["best_structural_route"]["id"] == "m_theory_modal_gap_planck_anchor", "best route")
    require(gr_scan["best_structural_route"]["classification"] == "BEST_STRUCTURAL_ROUTE_PACKET_REQUIRED", "route class")
    require(gr_scan["anchor_template"]["status"] == "TEMPLATE_UNFILLED", "template should remain unfilled")
    require(gr_scan["anchor_template"]["selected_by_mtt"] is False, "template selected too early")
    require(gr_scan["modal_gate_open_tests"]["selected_modal_gap_in_eV_or_inverse_meters_computed"] is False, "modal gap overclosed")
    require(gr_scan["blocked_shortcuts"]["use_mu_theta_5TeV_as_prediction"] is True, "TeV guard")

    closed = absolute_gate["closed_now"]
    open_ = absolute_gate["still_open"]
    require(closed["shared_E0_L0_formulas_imported"] is True, "closed import")
    require(closed["one_anchor_GR_normalization_family_closed"] is True, "closed one-anchor")
    require(closed["conditional_low_energy_TT_response_closed"] is True, "closed TT")
    require(closed["no_new_GR_knob_introduced"] is True, "new knob")
    require(open_["selected_physical_E0_or_L0_value"] is True, "E0/L0 should remain open")
    require(open_["measured_Newton_value_derived"] is True, "Newton should remain open")
    require(open_["strict_no_knob_absolute_scale_closure"] is True, "strict should remain open")
    require("use observed G_N or M_Pl to select L0/E0" in absolute_gate["forbidden_promotions"], "Newton guard")

    paths = superset["paths"]
    require(paths["straight_source_path"]["current_status"] == "STRUCTURAL_SLOT_FOUND_VALUE_OPEN", "straight path")
    require(paths["cross_sector_one_primitive_path"]["current_status"] == "CONDITIONAL_FAMILY_CLOSED", "cross path")
    require(paths["strict_no_knob_upgrade_path"]["current_status"] == "OPEN", "strict path")
    require(superset["strategy_decision"]["one_universal_primitive_tier_remains_allowed_but_labeled"] is True, "primitive tier label")

    require(portfolio["portfolio"]["sector_specific_new_parameters_added_here"] == 0, "sector knobs")
    require(portfolio["portfolio"]["selected_numeric_primitive_value_now"] is False, "selected numeric")
    require(len(portfolio["portfolio"]["constants_currently_waiting_on_same_primitive"]) == 3, "portfolio size")

    require(next_work["primary"]["label"] == "CONST-GR-01 / ABSOLUTE-SCALE-GN / G2-MODAL-GAP-DIMENSIONAL-ANCHOR-PACKET-FILL", "primary")
    require(next_work["secondary"]["label"] == "CONST-GR-01 / ABSOLUTE-SCALE-GN / G2B-ONE-PRIMITIVE-CROSS-CONSTANT-TEST", "secondary")

    require(cert["status"] == STATUS, "cert status")
    require(cert["one_anchor_GR_family_closed"] is True, "cert one-anchor")
    require(cert["selected_physical_E0_or_L0_value"] is False, "cert primitive")
    require(cert["strict_no_knob_absolute_scale_closure"] is False, "cert strict")
    require("G1-SHARED-PRIMITIVE-SOURCE-SEARCH" in note and "G2-MODAL-GAP" in note, "note")

    print("CONST-GR-01 G1 shared-primitive source-search audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
