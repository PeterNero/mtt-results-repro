"""Audit CONST-EW-02 B33 selected source-promotion packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b33_selected_source_promotion_packet"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
PACKET = BASE / "strict_nine_field_source_packet_import.packet.json"
VALIDATORS = BASE / "source_promotion_validator_matrix.packet.json"
REDUCTION = BASE / "unpatched_source_rule_or_honest_export_reduction.packet.json"
BOUNDARY = BASE / "weak_mixing_b33_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B33_SelectedSourcePromotionPacket_v1.md"

STATUS = "MTT_CONST_EW_02_B33_SELECTED_SOURCE_PROMOTION_PACKET_BUILT"


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
    packet = load(PACKET)
    validators = load(VALIDATORS)
    reduction = load(REDUCTION)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("packet", packet),
        ("validators", validators),
        ("reduction", reduction),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["strict_source_promotion_packet_constructed"] is True, "packet not constructed")
    require(candidate["closed_current_field_count"] == 3, "closed field count")
    require(candidate["open_current_field_count"] == 6, "open field count")
    require(candidate["current_unpatched_packet_passes"] is False, "current overpasses")
    require(candidate["conditional_unpatched_packet_passes"] is True, "conditional should pass")
    require(candidate["patched_packet_passes_unpatched_validator"] is False, "patched overpasses")
    require(candidate["source_promotion_closed_now"] is False, "source promotion overclosed")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")

    require(packet["closed_current_field_count"] == 3, "packet closed count")
    require(packet["open_current_field_count"] == 6, "packet open count")
    require("source_owner_id" in packet["closed_current_fields"], "source owner missing")
    require("admissible_c1_variation_space" in packet["closed_current_fields"], "admissible space missing")
    require("independence_guard" in packet["closed_current_fields"], "independence guard missing")
    for field in [
        "selected_measure_pairing",
        "selected_quadrature_rule",
        "phase_R_Z_source",
        "shift_R_X_source",
        "b_selected_source",
        "sector_row_assembly",
    ]:
        require(field in packet["open_current_fields"], f"{field} should be open")
    require(packet["strict_110_row_payload_validator_passes"] is True, "110-row validator")
    require(packet["emitted_before_residual_replay"] is False, "residual replay overclosed")

    require(validators["current_unpatched_packet_passes"] is False, "validator current")
    require(validators["conditional_unpatched_packet_passes"] is True, "validator conditional")
    require(validators["patched_packet_passes_unpatched_validator"] is False, "validator patched")
    require(any("free_axiom_patch_used must be false" in err for err in validators["patched_errors"]), "patched error missing")
    require(validators["honest_galerkin_table_exported"] is False, "honest Galerkin overexported")
    require(validators["unpatched_source_rule_proved"] is False, "source rule overproved")

    require(reduction["what_closes_now"]["ROUTE_A_four_clause_ladder_created"] is True, "Route A ladder")
    require(reduction["what_closes_now"]["ROUTE_B_four_input_manifest_created"] is True, "Route B manifest")
    require(reduction["what_remains_open"]["ROUTE_A_RA_1_physical_C1_variation_principle"] is True, "RA1 open")
    require(reduction["what_remains_open"]["ROUTE_B_selected_zero_mode_basis"] is True, "RB basis open")

    require(boundary["closed_or_sharpened_now"]["strict_selected_source_promotion_packet_constructed"] is True, "boundary packet")
    require(boundary["still_open"]["derive_differentiated_PhiFinC1_source_rule"] is True, "source rule open")
    require(boundary["still_open"]["export_honest_selected_Galerkin_C1_tables"] is True, "export open")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "weak angle open")
    require("not a patched/local-axiom closure claim" in boundary["anti_cycle_delta_from_B32"]["not_repeated"], "anti-cycle patch guard")

    require(cert["status"] == STATUS, "cert status")
    require(cert["closed_current_field_count"] == 3, "cert closed count")
    require(cert["open_current_field_count"] == 6, "cert open count")
    require(cert["conditional_unpatched_packet_passes"] is True, "cert conditional")
    require(cert["patched_packet_passes_unpatched_validator"] is False, "cert patched")
    require(cert["source_promotion_closed_now"] is False, "cert source promotion")
    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B34-ROUTEA-RA1-PHYSICAL-C1-VARIATION", "next primary")
    require(next_work["parallel"]["label"] == "CONST-EW-02 / WEAK-MIXING / B34-ROUTEB-SELECTED-ZERO-MODE-BASIS", "next parallel")
    require("strict nine-field packet" in note, "note packet")
    require("Two Exits" in note, "note exits")

    print("CONST-EW-02 B33 selected source-promotion packet audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
