"""Audit CONST-EW-02 B35 RA-1 derivation/RB-2 primitive terms artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b35_ra1_derivation_or_rb2_primitive_terms"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
RA1 = BASE / "route_a_ra1_derivation_attack_import.packet.json"
RB2 = BASE / "route_b_rb2_primitive_terms_fill_import.packet.json"
ALIGNMENT = BASE / "superset_external_alignment_import.packet.json"
BOUNDARY = BASE / "weak_mixing_b35_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B35_RA1_Derivation_or_RB2_PrimitiveTerms_v1.md"

STATUS = "MTT_CONST_EW_02_B35_RA1_DERIVATION_OR_RB2_PRIMITIVE_TERMS_BUILT"


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
    rb2 = load(RB2)
    alignment = load(ALIGNMENT)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("ra1", ra1),
        ("rb2", rb2),
        ("alignment", alignment),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["RA1_physical_action_equality_proved_now"] is False, "RA1 overclosed")
    require(candidate["RB2_primitive_terms_input_filled_now"] is True, "RB2 not filled")
    require(candidate["RB2_primitive_row_count"] == 72, "RB2 row count")
    require(candidate["RB2_selected_source_promoted_now"] is False, "RB2 source overpromoted")
    require(candidate["external_sources_used_as_MTT_source_proof"] is False, "external proof misuse")
    require(candidate["remaining_route_b_input_count_after_rb2"] == 2, "remaining Route-B count")
    require(candidate["source_promotion_closed_now"] is False, "source promotion overclosed")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")

    require(ra1["clause_id"] == "RA-1", "RA1 id")
    require(ra1["closed_now"] is False, "RA1 packet overclosed")
    require(ra1["external_used_as_source_proof"] is False, "RA1 external proof")
    require("RA1b" in ra1["refined_RA1_target"], "RA1 refined target")
    require("unpatched equality" in " ".join(ra1["why_still_open"]), "RA1 reason")

    require(rb2["input_id"] == "RB-2", "RB2 id")
    require(rb2["input_file_exists_now"] is True, "RB2 file")
    require(rb2["primitive_row_count"] == 72, "RB2 rows")
    require(rb2["selected_emitted"] is False, "RB2 selected overemitted")
    require(rb2["theorem_derived"] is False, "RB2 theorem overderived")
    require(rb2["source_owner_verified"] is False, "RB2 owner oververified")
    require(rb2["remaining_route_b_input_count_after_rb2"] == 2, "RB2 remaining")

    require(alignment["paths_used_as_knobs"] is False, "paths used as knobs")
    require(all(ref["used_as_source_proof"] is False for ref in alignment["external_references"]), "external source proof imported")
    require("same PSM-C1-02 selected source-promotion packet" in alignment["locked_target"], "locked target")

    require(boundary["closed_or_sharpened_now"]["ROUTE_B_RB2_primitive_terms_input_file_filled"] is True, "boundary RB2")
    require(boundary["closed_or_sharpened_now"]["all_72_primitive_support_rows_materialized"] is True, "boundary rows")
    require(boundary["still_open"]["ROUTE_A_RA1_unpatched_physical_action_equality"] is True, "boundary RA1")
    require(boundary["still_open"]["ROUTE_B_RB2_selected_source_promotion"] is True, "boundary RB2 promotion")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "boundary weak angle")
    require("not using external literature as MTT source proof" in boundary["anti_cycle_delta_from_B34"]["not_repeated"], "anti-cycle external guard")

    require(cert["status"] == STATUS, "cert status")
    require(cert["RB2_primitive_terms_input_filled_now"] is True, "cert RB2")
    require(cert["RB2_primitive_row_count"] == 72, "cert row count")
    require(cert["RB2_selected_source_promoted_now"] is False, "cert RB2 source")
    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B36-ROUTEA-RA1-PHYSICAL-ACTION-EQUALITY", "next primary")
    require(next_work["parallel"]["label"] == "CONST-EW-02 / WEAK-MIXING / B36-ROUTEB-RB3-HESSIAN-SOURCE-FILL", "next parallel")
    require("RB-2 primitive terms input filled" in note, "note result")
    require("B36" in note, "note next")

    print("CONST-EW-02 B35 RA1 derivation/RB2 primitive terms audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
