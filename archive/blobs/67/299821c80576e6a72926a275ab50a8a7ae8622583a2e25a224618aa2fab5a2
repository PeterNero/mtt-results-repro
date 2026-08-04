"""Audit oriented Phi_fin source-leaf source-amendment/corpus-discovery gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_sourceleaf_sourceamendment_or_corpusdiscovery.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceleaf_sourceamendment_or_corpusdiscovery.candidate.json"
DISCOVERY = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceleaf_corpus_discovery_report.json"
PLAN = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceleaf_minimal_source_amendment_plan.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_sourceleaf_sourceamendment_or_corpusdiscovery_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_SourceLeaf_SourceAmendment_or_CorpusDiscovery_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCELEAF_CORPUS_DISCOVERY_NO_EXISTING_SOURCE_PACKET_AMENDMENT_PLAN_BUILT"
NEXT = "Selected_Heterotic_OrientedPhiFin_DirectCarrier_SourceTheorem_ConstructiveAttempt_v1"


def check(label: str, condition: bool, detail: object) -> None:
    if not condition:
        print(f"FAIL: {label} -- {detail}")
        sys.exit(1)
    print(f"PASS: {label} -- {detail}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    check("script reruns", proc.returncode == 0, proc.stdout + proc.stderr)

    data = load(DATA)
    discovery = load(DISCOVERY)
    plan = load(PLAN)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("discovery status", discovery["status"] == "NO_EXISTING_SOURCE_PACKET_FOUND", discovery["status"])
    check("repo scanned", discovery["repo_scan"]["exists"] is True and discovery["repo_scan"]["files_scanned"] > 0, discovery["repo_scan"])
    check("corpus scan attempted", "exists" in discovery["mtt_corpus_scan"] and "files_scanned" in discovery["mtt_corpus_scan"], discovery["mtt_corpus_scan"].keys())
    check("no source packet found", decision["direct_existing_packet_found"] is False and decision["smooth_existing_packet_found"] is False and cert["direct_existing_packet_found"] is False and cert["smooth_existing_packet_found"] is False, decision)
    check("support matches allowed", discovery["classification"]["support_only_matches_found"] is True, discovery["classification"])
    check("plan built", plan["status"] == "DIRECT_CARRIER_CONSTRUCTIVE_ATTEMPT_SELECTED_NEXT" and cert["minimal_source_amendment_plan_built"] is True, plan["status"])
    check("plan uses exact logdet as required theorem target", plan["next_direct_packet"]["prove_finitepart_trace_identity"] == "log(92160000)", plan["next_direct_packet"])
    check("smooth lane fallback", "R+ geometry exists" in plan["smooth_lane_kept_as_fallback"]["why"], plan["smooth_lane_kept_as_fallback"])
    check("no closure", decision["closure_claimed"] is False and data["closure_claimed"] is False and cert["closure_claimed"] is False, decision)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records outputs", str(DISCOVERY.relative_to(ROOT)) in note and str(PLAN.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin source-leaf corpus-discovery audit passed")


if __name__ == "__main__":
    main()
