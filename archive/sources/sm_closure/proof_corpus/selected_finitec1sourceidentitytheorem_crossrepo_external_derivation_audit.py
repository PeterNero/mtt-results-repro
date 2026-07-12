"""Audit cross-repo/external derivation attempt for finite C1 source identity."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finitec1sourceidentitytheorem_crossrepo_external_derivation"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SUPPORT = PACKET_DIR / "cross_repo_corpus_external_support.packet.json"
PRINCIPLE = PACKET_DIR / "selected_finite_c1_source_identity_principle_candidate.packet.json"
DERIVATION = PACKET_DIR / "source_identity_derivation_attempt.packet.json"
VALIDATION = PACKET_DIR / "conditional_promoted_source_identity_validator_result.packet.json"
DECISION = PACKET_DIR / "source_identity_theorem_or_principle_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteC1SourceIdentityTheorem_CrossRepoExternalDerivation_v1.md"

STATUS = "MTT_SELECTED_FINITEC1SOURCEIDENTITYTHEOREM_CROSSREPO_EXTERNAL_DERIVATION_PRINCIPLE_READY_THEOREM_OPEN"
NEXT = "MTT_Selected_FiniteC1SourceIdentityPrincipleInsertion_or_SelectedActionDerivation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    support = load(SUPPORT)
    principle = load(PRINCIPLE)
    derivation = load(DERIVATION)
    validation = load(VALIDATION)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "next mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(cert["theorem_proved"] is False, "certificate overproves theorem")
    require(cert["principle_inserted"] is False, "certificate inserts principle")

    require(support["classification"]["cross_repo_proves_theorem"] is False, "cross-repo overproof")
    require(support["classification"]["corpus_proves_theorem"] is False, "corpus overproof")
    require(support["classification"]["external_literature_proves_mtt_theorem"] is False, "external overproof")
    require(support["classification"]["support_suffices_for_principle_candidate"] is True, "principle support missing")
    require(len(support["external_support"]["sources"]) == 3, "external source count mismatch")

    require(principle["principle_name"] == "SelectedFiniteC1SourceIdentityPrinciple", "principle name mismatch")
    require(principle["status"] == "MINIMAL_PRINCIPLE_CANDIDATE_FORMULATED_NOT_INSERTED", "principle status mismatch")
    require(len(principle["minimal_axioms"]) == 7, "minimal axiom count mismatch")
    require(principle["insertion_status"]["accepted_as_axiom_or_derived_theorem"] is False, "principle overinserted")
    require(principle["why_minimal"]["does_not_add_numeric_values"] is True, "principle adds numbers")

    require(derivation["proved_now"] is False, "derivation overproved")
    require(derivation["principle_candidate_ready"] is True, "principle not ready")
    for path in derivation["attempted_paths"].values():
        require(path["success"] is False, "attempt path overclosed")
    require(derivation["closure_claimed"] is False, "derivation overclaims")

    require(validation["ok"] is True and validation["exit_code"] == 0, "conditional validator should pass")
    require(decision["selected_finite_c1_source_identity_theorem_proved"] is False, "decision theorem overproved")
    require(decision["selected_finite_c1_source_identity_principle_inserted"] is False, "decision overinserted")
    require(decision["conditional_promoted_witness_validates"] is True, "decision missing conditional validation")
    require(decision["closure_claimed"] is False, "decision overclaims closure")

    require(candidate["what_closes_now"]["minimal_source_identity_principle_formulated"] is True, "principle formulation missing")
    require(candidate["what_closes_now"]["conditional_promoted_witness_validates"] is True, "conditional witness missing")
    require(candidate["what_remains_open"]["SelectedFiniteC1SourceIdentityTheorem"] is True, "theorem should remain open")
    require("supports the strategy, not the MTT theorem" in note, "note missing external guardrail")
    require("passes the strict validator" in note, "note missing conditional pass")

    for packet in [candidate, support, principle, derivation, decision, cert]:
        guard(packet)

    print(proc.stdout.strip())
    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
