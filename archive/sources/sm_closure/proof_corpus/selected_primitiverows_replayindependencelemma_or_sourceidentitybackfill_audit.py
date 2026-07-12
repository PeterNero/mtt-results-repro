"""Audit primitive-row replay-independence lemma gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_primitiverows_replayindependencelemma_or_sourceidentitybackfill"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_AUDIT = PACKET_DIR / "primitive_replay_independence_source_order_audit.packet.json"
HYPOTHETICAL = PACKET_DIR / "hypothetical_source_ordering_validator_payload.packet.json"
LEMMA_GATE = PACKET_DIR / "primitive_replay_independence_lemma_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_rowsource_independence.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrimitiveRows_ReplayIndependenceLemma_or_SourceIdentityBackfill_v1.md"
STATUS = "MTT_SELECTED_PRIMITIVEROWS_REPLAYINDEPENDENCELEMMA_OR_SOURCEIDENTITYBACKFILL_BUILT_SOURCE_ORDERING_GATE_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    audit = load(SOURCE_AUDIT)
    hypothetical = load(HYPOTHETICAL)
    gate = load(LEMMA_GATE)
    cert = load(CERT)
    next_work = load(PACKET_DIR / "next_labeled_workorder.packet.json")
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(HYPOTHETICAL)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    require(data["status"] == STATUS, "status mismatch")
    require(data["active_post_sm_parity_label"] == "PSM-C1-02", "active label mismatch")
    require(data["post_sm_parity_label_context"]["closed_boundary"] == "DONE-PARITY-00", "closed boundary label missing")
    require(data["post_sm_parity_label_context"]["preferred_phrase"] == "post-SM-parity frontier", "preferred phrase missing")
    require(data["post_sm_parity_label_context"]["language_guardrail"].startswith("Do not call"), "language guardrail missing")
    require(data["theorem"]["proved"] is True, "reduction theorem not proved")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["source_ordering_lemma_proved_now"] is False, "source-ordering lemma overclaimed")
    require(data["primitive_replay_independence_closed_now"] is False, "replay independence overclaimed")
    require(audit["row_count"] == 72, "wrong primitive row count")
    require(audit["all_rows_exact"] is True, "primitive rows not exact")
    require(audit["existing_source_ordering_flags"]["provenance_independent_false_rows"] == 72, "expected all rows still provenance-open")
    require(audit["existing_source_ordering_flags"]["physical_source_promoted_rows"] == 0, "physical source overpromoted")
    require(gate["validator_passes_if_two_source_ordering_flags_are_theorem_derived"] is True, "hypothetical validator should pass")
    require(gate["post_sm_parity_label_context"]["active_label"] == "PSM-C1-02", "gate label mismatch")
    require(next_work["active_label"] == "PSM-C1-02", "next work active label mismatch")
    require(next_work["secondary"]["label"] == "PSM-C1-02", "secondary label mismatch")
    require(next_work["secondary"]["route_label"] == "ROUTE-B", "secondary route label mismatch")
    require(gate["lemma_to_prove"]["currently_proved"] is False, "lemma overproved")
    require(hypothetical["hypothetical_only"] is True, "hypothetical guard missing")
    require(proc.returncode == 0, "hypothetical source-ordering validator should pass")
    require(cert["hypothetical_validator_passes"] is True, "cert missing hypothetical pass")
    require(cert["closure_claimed"] is False, "cert overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data selector")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("source-ordering" in note, "note missing source-ordering wording")
    require("Active post-SM-parity label: `PSM-C1-02`" in note, "note missing active label")
    require("Boundary guardrail: `DONE-PARITY-00`" in note, "note missing frozen boundary guardrail")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
