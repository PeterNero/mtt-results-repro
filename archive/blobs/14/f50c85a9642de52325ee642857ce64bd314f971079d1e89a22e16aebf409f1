"""Audit finite C1 source-identity principle insertion or selected-action derivation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DERIVATION = PACKET_DIR / "selected_action_derivation_attempt.packet.json"
INSERTION = PACKET_DIR / "local_source_identity_principle_insertion.packet.json"
PROMOTED = PACKET_DIR / "local_principle_promoted_110row_source_packet.packet.json"
VALIDATION = PACKET_DIR / "local_principle_promoted_110row_validator_result.packet.json"
REPLAY = PACKET_DIR / "patched_source_identity_dynamic_c1_replay.packet.json"
GUARDRAIL = PACKET_DIR / "unpatched_no_knob_guardrail.packet.json"
DECISION = PACKET_DIR / "principle_insertion_or_action_derivation_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteC1SourceIdentityPrincipleInsertion_or_SelectedActionDerivation_v1.md"

STATUS = "MTT_SELECTED_FINITEC1SOURCEIDENTITYPRINCIPLEINSERTION_OR_SELECTEDACTIONDERIVATION_BUILT_PATCHED_SOURCE_IDENTITY_CLOSED_UNPATCHED_OPEN"
NEXT = "MTT_Selected_SourceIdentityPatchedDynamicC1Ledger_or_UnpatchedActionProof_v1"


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
    derivation = load(DERIVATION)
    insertion = load(INSERTION)
    promoted = load(PROMOTED)
    validation = load(VALIDATION)
    replay = load(REPLAY)
    guardrail = load(GUARDRAIL)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")

    require(derivation["status"] == "SELECTED_ACTION_DERIVATION_ATTEMPTED_STILL_OPEN", "derivation status mismatch")
    require(derivation["unpatched_principle_derived_now"] is False, "derivation overclosed")
    for key, value in derivation["derivation_result"].items():
        require(value is False, f"unpatched derivation overclaimed: {key}")
    require(derivation["closure_claimed"] is False, "derivation closure overclaimed")

    require(insertion["status"] == "LOCAL_SOURCE_IDENTITY_PRINCIPLE_INSERTED_IN_SM_PARITY_SPINE", "insertion status mismatch")
    require(insertion["inserted_into_local_proof_spine"] is True, "local insertion missing")
    require(insertion["inserted_into_external_obsidian_papers"] is False, "external corpus modified")
    require(insertion["derived_from_prior_axioms"] is False, "insertion claims derivation")
    require(len(insertion["minimal_axioms"]) == 7, "minimal axiom count mismatch")
    require(all(value is True for value in insertion["scope"].values()), "scope guard missing")

    require(promoted["status"] == "PROMOTED_UNDER_LOCAL_SELECTED_FINITEC1_SOURCE_IDENTITY_PRINCIPLE", "promoted packet status mismatch")
    require(promoted["local_principle_inserted"] is True, "promoted packet missing local insertion")
    require(promoted["derived_unpatched"] is False, "promoted packet overclaims unpatched derivation")
    require(promoted["closure_claimed"] is False, "promoted packet overclaims global closure")

    require(validation["ok"] is True and validation["exit_code"] == 0, "strict source id validator should pass")
    require(replay["status"] == "PATCHED_SOURCE_IDENTITY_DYNAMIC_C1_REPLAY_CLOSED", "replay status mismatch")
    require(replay["validator_ok"] is True, "replay validator flag mismatch")
    require(replay["row_counts"]["primitive_rows"] == 72, "primitive row count mismatch")
    require(replay["row_counts"]["sector_rows"] == 36, "sector row count mismatch")
    require(replay["row_counts"]["hessian_source_rows"] == 2, "hessian row count mismatch")
    require(replay["row_counts"]["total_source_rows"] == 110, "total row count mismatch")
    for key, value in replay["promoted_under_local_principle"].items():
        require(value is True, f"patched promotion missing: {key}")
    for key, value in replay["not_promoted_unpatched"].items():
        require(value is False, f"unpatched overclaim: {key}")
    require(replay["superset_strategy"]["free_parameters_used"] is False, "superset path used free parameters")
    require(replay["closure_claimed"] is False, "replay global closure overclaimed")
    require(replay["patched_spine_closure_claimed"] is True, "patched closure not claimed")

    require(guardrail["status"] == "PATCHED_SOURCE_IDENTITY_SEPARATED_FROM_UNPATCHED_THEOREM", "guardrail status mismatch")
    for key, value in guardrail["unpatched_open_items"].items():
        require(value is True, f"unpatched item not open: {key}")
    require("unpatched no-knob derivation" in guardrail["patched_closure_not_allowed_for"], "guardrail missing no-knob exclusion")

    require(decision["selected_action_derivation_succeeded"] is False, "decision overderives selected action")
    require(decision["local_principle_inserted"] is True, "decision missing insertion")
    require(decision["strict_source_id_validator_ok"] is True, "decision missing validator")
    require(decision["patched_dynamic_C1_source_identity_closed"] is True, "decision missing patched closure")
    require(decision["unpatched_no_knob_dynamic_C1_closed"] is False, "decision overclaims no-knob closure")
    require(decision["closure_claimed"] is False, "decision global closure overclaimed")

    require(candidate["theorem"]["proved"] is True and candidate["theorem"]["patched"] is True, "candidate theorem metadata mismatch")
    require(cert["theorem_proved"] is True and cert["theorem_patched"] is True, "cert theorem metadata mismatch")
    require(candidate["closure_claimed"] is False and cert["closure_claimed"] is False, "global closure overclaimed")
    require(candidate["patched_spine_closure_claimed"] is True and cert["patched_spine_closure_claimed"] is True, "patched closure missing")
    require("passes the strict source-id validator" in note, "note missing validator result")
    require("not a no-knob theorem" in note, "note missing no-knob guardrail")

    for packet in [candidate, derivation, insertion, replay, guardrail, decision, cert]:
        guard(packet)

    print(proc.stdout.strip())
    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
