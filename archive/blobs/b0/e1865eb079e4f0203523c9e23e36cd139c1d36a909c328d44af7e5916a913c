"""Audit terminal admissible-section principle promotion into active MTT spine."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "promote_terminal_admissible_section_principle_to_spine.py"
PACKET = ROOT / "candidate_data" / "terminal_admissible_section_principle_spine_promotion.candidate.json"
CERT = ROOT / "certificates" / "terminal_admissible_section_principle_spine_promotion_certificate.json"
NOTE = ROOT / "proof_corpus" / "Terminal_Admissible_Section_Principle_Spine_Promotion_v1.md"

STATUS = "TERMINAL_ADMISSIBLE_SECTION_PRINCIPLE_PROMOTED_TO_ACTIVE_MTT_SPINE_RELATIVE_THEOREM"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load(PACKET)
    cert = load(CERT)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("script runs", proc.returncode == 0, proc.stdout)
    script_packet = json.loads(proc.stdout)

    check("packet and cert match", packet == cert, {"packet": PACKET, "cert": CERT})
    check("script agrees", script_packet["status"] == packet["status"], script_packet["status"])
    check("status", packet["status"] == STATUS, packet["status"])
    check("all promotion checks pass", all(packet["promotion_checks"].values()), packet["promotion_checks"])

    axiom = packet["axiom_schema"]
    check(
        "axiom promoted but not derived from older corpus",
        axiom["status"] == "PROMOTED_TO_ACTIVE_MTT_SPINE_AS_EXPLICIT_AXIOM_SCHEMA"
        and axiom["not_derived_from_older_corpus"] is True,
        axiom,
    )
    check(
        "axiom has failure modes",
        set(axiom["failure_modes"]) == {"no_survivor", "multiple_survivors", "holonomy_sensitive_layer"},
        axiom["failure_modes"],
    )

    q79 = packet["q79_application"]
    check(
        "q79 selects L3-K2 relative to active spine",
        q79["spine_relative_source_status"] == "SELECTED_BY_ACTIVE_MTT_SPINE_AXIOM"
        and q79["selected_source_label"] == "g3 / L3-K2"
        and q79["selected_L"] == [1, -2, 0]
        and q79["selected_L2"] == [2, -4, 0]
        and q79["selected_c2"] == [4, 0, 0],
        q79,
    )
    check(
        "relative theorem not old-corpus theorem",
        packet["theorem"]["proved"] is True
        and packet["theorem"]["relative_to_active_spine"] is True
        and packet["theorem"]["derived_from_prior_corpus_alone"] is False,
        packet["theorem"],
    )
    check(
        "remaining derivation and operator gates retained",
        packet["what_remains_open"]["derive_terminal_axiom_from_deeper_projection_dynamics"] is True
        and packet["what_remains_open"]["selected_dotD_alpha1_first_variation"] is True
        and packet["what_remains_open"]["primitive_C1_response_matrices"] is True,
        packet["what_remains_open"],
    )
    check(
        "guardrails all negative",
        all(v is False for v in packet["guardrails"].values()),
        packet["guardrails"],
    )
    check(
        "verdict distinguishes relative and old corpus closure",
        packet["verdict"]["spine_promotion_complete"] is True
        and packet["verdict"]["q79_source_unconditional_relative_to_active_spine"] is True
        and packet["verdict"]["q79_source_unconditional_from_old_corpus_alone"] is False,
        packet["verdict"],
    )

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "active MTT spine",
        "not a derivation",
        "`g3 / L3-K2`",
        "fail-fast",
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nTerminal admissible-section principle spine promotion audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
