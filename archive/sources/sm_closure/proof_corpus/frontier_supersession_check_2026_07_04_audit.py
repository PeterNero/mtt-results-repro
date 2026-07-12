"""Audit the 2026-07-04 frontier supersession check."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "frontier_supersession_check_2026_07_04.candidate.json"
CERT = ROOT / "certificates" / "frontier_supersession_check_2026_07_04_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Frontier_Supersession_Check_2026_07_04_v1.md"
README = ROOT / "README.md"
VERIFY = ROOT / "scripts" / "verify.py"

STATUS = "MTT_FRONTIER_SUPERSESSION_CHECK_2026_07_04_CURRENT_FRONTIER_CONFIRMED"
FRONTIER = "MTT_Selected_HYMOverlapValueSourceTheorem_or_QutritSpectralTriplePackaging_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    readme = README.read_text(encoding="utf-8")
    verify = VERIFY.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["current_frontier"] == FRONTIER, "candidate frontier mismatch")
    require(cert["current_frontier"] == FRONTIER, "certificate frontier mismatch")
    require(FRONTIER in readme, "README current frontier not updated")
    require(FRONTIER in note, "note missing frontier")

    require(data["superseding_local_artifact_found"] is False, "local supersession overclaimed")
    require(data["superseding_adjacent_repo_artifact_found"] is False, "adjacent supersession overclaimed")
    require(data["superseding_checked_external_result_found"] is False, "external supersession overclaimed")
    require(cert["superseding_artifact_found"] is False, "certificate supersession mismatch")

    promotions = data["active_verifier_promotions"]
    require(promotions["qutrit_weyl_gate_audit_included"] is True, "qutrit audit promotion missing")
    require(promotions["qutrit_weyl_gate_certificate_included"] is True, "qutrit cert promotion missing")
    require(promotions["readme_frontier_updated"] is True, "README promotion missing")
    require(
        "selected_qutritweylcarriertheorem_or_hymoverlapvaluesourcegate_audit.py" in verify,
        "active verifier missing qutrit audit",
    )
    require(
        "selected_qutritweylcarriertheorem_or_hymoverlapvaluesourcegate_certificate.json" in verify,
        "active verifier missing qutrit certificate",
    )

    guardrails = data["guardrails"]
    require(guardrails["claims_full_no_knob_closure"] is False, "full no-knob overclaimed")
    require(guardrails["claims_true_SM_equivalence"] is False, "true SM overclaimed")
    require(guardrails["promotes_conditional_fixture_as_source"] is False, "conditional fixture promoted")
    require(guardrails["uses_observed_values_as_selector"] is False, "observed selector used")
    require(cert["conditional_q79_m1_deresponse_not_promoted"] is True, "q79 conditional guard missing")

    for phrase in [
        "selected_source_still_absent = true",
        "honest_current_hym_source_fails = true",
        "does not supersede the HYM-overlap value-source frontier",
        "fast verifier intentionally not exhaustive",
        "MTT_Selected_HYMOverlapValueSourceTheorem_or_QutritSpectralTriplePackaging_v1",
    ]:
        require(phrase in note_flat, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
