"""Audit corpus paper-revision packet after one-primitive closure adoption."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_corpuspaperrevisionpacket_or_strictnoknobupgradeexecution"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
REVISION_PACKET = PACKET_DIR / "corpus_paper_revision_packet.packet.json"
LEGACY_AUDIT = PACKET_DIR / "legacy_claim_surface_audit.packet.json"
STRICT_ROUTE = PACKET_DIR / "strict_noknob_route01_execution_packet.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CorpusPaperRevisionPacket_or_StrictNoKnobUpgradeExecution_v1.md"

STATUS = (
    "MTT_SELECTED_CORPUSPAPERREVISIONPACKET_OR_STRICTNOKNOBUPGRADEEXECUTION_"
    "BUILT_REVISION_PACKET_AND_ROUTE01_EXECUTION"
)
NEXT = "MTT_Selected_CorpusPaperRevisionExecution_or_StrictNoKnobUpgradeRoute01_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    revision = load(REVISION_PACKET)
    legacy = load(LEGACY_AUDIT)
    route = load(STRICT_ROUTE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["closure_claimed"] is True, "candidate closes this packet")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["target_fitting_used"] is False, "candidate target fitting")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")

    require(revision["status"] == "CORPUS_PAPER_REVISION_PACKET_READY", "revision status")
    require(revision["current_closure_standard"] == "one_shared_physical_primitive", "standard")
    require("one-shared-physical-primitive" in revision["canonical_claim"], "canonical claim")
    require("strict no-knob remains open" in revision["short_claim"], "short claim")
    require(len(revision["allowed_claims"]) == 6, "allowed claims")
    require(len(revision["forbidden_claims"]) == 4, "forbidden claims")
    require(len(revision["required_paper_edits"]) == 5, "paper edits")
    require(len(revision["priority_revision_targets"]) >= 8, "revision targets")
    require(len(revision["replacement_table"]) == 6, "replacement table")
    require(revision["source_boundary_policy"]["observed_data_used_as_selector"] is False, "observed")
    require(revision["source_boundary_policy"]["target_fitting_used"] is False, "fit")
    strict = revision["strict_status_to_preserve"]
    require(strict["strict_no_knob_closure"] is False, "strict status")
    require(strict["accepted_strict_P_EW_source_rows"] == 0, "PEW rows")
    require(strict["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "K rows")
    require(strict["accepted_strict_derivation_route_count"] == 0, "route rows")
    require(len(revision["revision_complete_when"]) == 5, "completion criteria")

    require(legacy["status"] == "LEGACY_SURFACE_AUDITED_FOR_REVISION", "legacy status")
    require(set(legacy["risk_phrase_counts"]) >= {"strict_no_knob_as_current", "zero_primitive_as_current"}, "legacy keys")
    require("not automatic errors" in legacy["interpretation"], "legacy interpretation")

    require(route["status"] == "STRICT_NOKNOB_ROUTE01_READY_TO_ATTACK", "route status")
    require(route["route_id"] == "UPG-01", "route id")
    require(route["blocked_quantities"]["physical_normalization_axiom_derived"] is False, "axiom")
    require(route["blocked_quantities"]["accepted_strict_P_EW_source_rows"] == 0, "route PEW")
    require(route["blocked_quantities"]["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "route K")
    require(len(route["execution_tests"]) == 4, "execution tests")
    require(route["next_artifact"] == NEXT, "route next")

    require(data["theorem"]["name"] == "CorpusPaperRevisionPacketAndRoute01ExecutionTheorem", "theorem")
    require(data["theorem"]["proved"] is True, "theorem proved")
    require(len(data["closed_now"]) == 4, "closed now")
    require(len(data["not_closed"]) == 3, "not closed")
    key = data["key_numbers"]
    require(key["priority_revision_target_count"] >= 8, "key target count")
    require(key["replacement_rule_count"] == 6, "key replacement count")
    require(key["strict_route_execution_test_count"] == 4, "key route tests")
    require(key["strict_P_EW_source_rows"] == 0, "key PEW")
    require(key["strict_direct_K_rows"] == 0, "key K")
    require(key["shared_physical_primitive_count"] == 1, "key primitive")
    require(key["H_specific_parameter_count"] == 0, "key H")

    decision = data["closure_decision"]
    require(decision["corpus_revision_packet_ready"] is True, "decision revision")
    require(decision["legacy_surface_audit_ready"] is True, "decision legacy")
    require(decision["strict_route01_execution_ready"] is True, "decision route")
    require(decision["one_shared_primitive_tier_closed"] is True, "decision tier")
    require(decision["strict_no_knob_closure"] is False, "decision strict")
    require(decision["global_true_SM_no_knob_closure"] is False, "decision global")

    require(cert["corpus_revision_packet_ready"] is True, "cert revision")
    require(cert["legacy_surface_audit_ready"] is True, "cert legacy")
    require(cert["strict_route01_execution_ready"] is True, "cert route")
    require(cert["current_closure_standard"] == "one_shared_physical_primitive", "cert standard")
    require(cert["one_shared_primitive_tier_closed"] is True, "cert tier")
    require(cert["strict_no_knob_closure"] is False, "cert strict")
    require(cert["observed_data_used_as_selector"] is False, "cert observed")
    require(cert["target_fitting_used"] is False, "cert fit")

    for phrase in [
        "What This Closes",
        "one-shared-physical-primitive SM standard",
        "Strict Route 01",
        "strict `P_EW` source rows: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
