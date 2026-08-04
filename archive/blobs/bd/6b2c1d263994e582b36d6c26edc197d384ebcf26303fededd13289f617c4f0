"""Audit CONST-EW-02 B34 RA-1/RB-1 input-basis artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b34_ra1_or_rb1_input_basis"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
RA1 = BASE / "route_a_ra1_physical_c1_variation_import.packet.json"
RB1 = BASE / "route_b_rb1_zero_mode_basis_input_import.packet.json"
BOUNDARY = BASE / "weak_mixing_b34_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B34_RA1_or_RB1_InputBasis_v1.md"

STATUS = "MTT_CONST_EW_02_B34_RA1_OR_RB1_INPUT_BASIS_BUILT"


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
    ra1 = load(RA1)
    rb1 = load(RB1)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("ra1", ra1),
        ("rb1", rb1),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["RA1_closed_now"] is False, "RA1 overclosed")
    require(candidate["RB1_input_filled_now"] is True, "RB1 input not filled")
    require(candidate["RB1_selected_source_promoted_now"] is False, "RB1 source overpromoted")
    require(candidate["remaining_route_b_input_count_after_rb1"] == 3, "remaining input count")
    require(candidate["source_promotion_closed_now"] is False, "source promotion overclosed")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")

    require(ra1["clause_id"] == "RA-1", "RA1 id")
    require(ra1["closed_now"] is False, "RA1 packet overclosed")
    require(ra1["conditional_witness_value"] is True, "RA1 conditional missing")
    require(ra1["free_axiom_patch_used"] is False, "RA1 patch")
    require("unpatched physical action equality" in " ".join(ra1["why_not_proved"]), "RA1 reason")

    require(rb1["input_id"] == "RB-1", "RB1 id")
    require(rb1["input_file_exists_now"] is True, "RB1 file")
    require(rb1["basis_dimension"] == 9, "RB1 basis dimension")
    require(rb1["selected_emitted"] is False, "RB1 selected emitted overclosed")
    require(rb1["theorem_derived"] is False, "RB1 theorem overclosed")
    require(rb1["source_owner_verified"] is False, "RB1 owner overclosed")
    require(rb1["remaining_route_b_input_count_after_rb1"] == 3, "RB1 remaining")
    require(rb1["hym_projector_bridge"]["bridge_theorem_proved"] is True, "HYM bridge")
    require(rb1["hym_projector_bridge"]["selected_values_emitted"] is False, "HYM values overemitted")

    require(boundary["closed_or_sharpened_now"]["ROUTE_B_RB1_zero_mode_basis_input_file_filled"] is True, "boundary RB1")
    require(boundary["still_open"]["ROUTE_A_RA1_unpatched_physical_C1_variation_derivation"] is True, "boundary RA1 open")
    require(boundary["still_open"]["ROUTE_B_RB1_selected_HYM_projector_basis_value_emission"] is True, "boundary RB1 source open")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "boundary weak angle open")
    require("not a patched/local-axiom closure claim" in boundary["anti_cycle_delta_from_B33"]["not_repeated"], "anti-cycle patch guard")

    require(cert["status"] == STATUS, "cert status")
    require(cert["RA1_closed_now"] is False, "cert RA1")
    require(cert["RB1_input_filled_now"] is True, "cert RB1")
    require(cert["RB1_selected_source_promoted_now"] is False, "cert RB1 source")
    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B35-ROUTEA-RA1-DERIVATION-ATTACK", "next primary")
    require(next_work["parallel"]["label"] == "CONST-EW-02 / WEAK-MIXING / B35-ROUTEB-RB2-PRIMITIVE-TERMS-FILL", "next parallel")
    require("RB-1 zero-mode basis input file filled" in note, "note result")
    require("B35" in note, "note next")

    print("CONST-EW-02 B34 RA1/RB1 input-basis audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
