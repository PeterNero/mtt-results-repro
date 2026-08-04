"""Audit Higgs precision-row gate and full correlated-profile readiness."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsprecisionrows_or_fullcorrelatedprofile"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROWS = PACKET_DIR / "higgs_precision_row_promotion_gate.packet.json"
PROFILE = PACKET_DIR / "full_correlated_profile_readiness_matrix.packet.json"
BLOCKERS = PACKET_DIR / "minimal_precision_closure_blocker_set.packet.json"
DECISION = PACKET_DIR / "precision_rows_or_full_profile_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsPrecisionRows_or_FullCorrelatedProfile_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSPRECISIONROWS_OR_FULLCORRELATEDPROFILE_BUILT_PROMOTION_GATE_VALUES_OPEN"
NEXT = "MTT_Selected_HiggsPrecisionValueFill_or_ProfileConventionImport_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    rows = load(ROWS)
    profile = load(PROFILE)
    blockers = load(BLOCKERS)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    require(rows["summary"]["row_count"] == 10, "precision row count mismatch")
    require(rows["summary"]["accepted_precision_row_count"] == 0, "precision rows overpromoted")
    require(rows["summary"]["proxy_row_count"] == 7, "proxy row count mismatch")
    require(rows["summary"]["external_import_identity_row_count"] == 3, "external import identity count mismatch")
    require(rows["summary"]["all_rows_have_precision_route"] is True, "missing precision routes")
    require(rows["summary"]["all_rows_have_operator_source_requirement"] is True, "missing operator requirements")
    require(all(row["accepted_as_precision_formula_or_import_row"] is False for row in rows["rows"]), "row overaccepted")
    require(any(row["channel"] == "H_to_gg" and "Qa/SU3" in row["operator_source_requirement"] for row in rows["rows"]), "Qa/SU3 gg requirement missing")
    require(any(row["channel"] == "H_to_WW_star" and "off-shell" in row["precision_route"] for row in rows["rows"]), "EW offshell route missing")

    require(profile["summary"]["block_count"] == 4, "profile block count mismatch")
    require(profile["summary"]["available_stress_or_diagonal_blocks"] == 3, "available profile blocks mismatch")
    require(profile["summary"]["full_empirical_profile_filled"] is False, "full profile overfilled")
    require(profile["summary"]["cross_block_correlations_filled"] is False, "cross-block correlations overfilled")
    require(profile["summary"]["accepted_as_full_correlated_profile"] is False, "full profile overaccepted")
    require(any(block["block"] == "cross_block_shared_inputs" and block["status"].startswith("OPEN") for block in profile["blocks"]), "cross-block blocker missing")

    require(len(blockers["blockers"]) == 3, "minimal blocker count mismatch")
    require(blockers["minimal_for_sm_parity_precision_replay"] == ["accepted_precision_row_values", "full_correlated_profile"], "SM-parity precision blocker set mismatch")
    require("source_operator_upgrade" in blockers["minimal_for_no_knob_source_closure"], "no-knob source blocker missing")

    require(decision["precision_row_promotion_gate_built"] is True, "decision row gate missing")
    require(decision["full_correlated_profile_readiness_built"] is True, "decision profile readiness missing")
    require(decision["accepted_precision_row_count"] == 0, "decision row promotion mismatch")
    require(decision["full_correlated_profile_filled"] is False, "decision profile overfilled")
    require(decision["precision_total_width_closed"] is False, "precision total width overclosed")
    require(decision["precision_branching_ratios_closed"] is False, "precision branching overclosed")

    require(data["closure_decision"]["accepted_precision_row_count"] == 0, "candidate rows overpromoted")
    require(data["closure_decision"]["full_correlated_profile_filled"] is False, "candidate profile overfilled")
    require(data["closure_decision"]["precision_total_width_closed"] is False, "candidate total width overclosed")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("promotes zero" in note, "note missing zero-promotion guard")
    require("No benchmark value is used as a source selector" in note, "note missing selector guard")

    for packet in [rows, profile, blockers, decision, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
