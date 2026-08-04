"""Audit Weyl variation action-principle derivation or insertion gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DERIVATION = PACKET_DIR / "unpatched_weylvariation_actionprinciple_derivation_attempt.packet.json"
INSERTION = PACKET_DIR / "explicit_weylvariation_actionprinciple_insertion_package.packet.json"
IF_INSERTED = PACKET_DIR / "if_inserted_kernel_closure_witness.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "conditional_kernel_validator_result.packet.json"
DECISION = PACKET_DIR / "derivation_or_insertion_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_WeylVariationActionPrinciple_Derivation_or_ExplicitInsertion_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_WEYLVARIATION_ACTIONPRINCIPLE_DERIVATION_OPEN_INSERTION_READY"
NEXT = "MTT_Selected_WeylVariationActionPrinciple_Apply_or_IndependentKernelExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    derivation = load(DERIVATION)
    insertion = load(INSERTION)
    if_inserted = load(IF_INSERTED)
    validator = load(VALIDATOR_RESULT)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")

    require(
        derivation["status"] == "UNPATCHED_DERIVATION_SUPPORT_CLOSED_PHYSICAL_SELECTION_OPEN",
        "derivation status mismatch",
    )
    require(derivation["unpatched_principle_derived_now"] is False, "unpatched principle overderived")
    for key, value in derivation["closed_support"].items():
        require(value is True, f"closed support missing: {key}")
    require(len(derivation["unpatched_requirements"]) == 4, "unpatched requirement count mismatch")

    require(insertion["status"] == "EXPLICIT_PRINCIPLE_INSERTION_READY_NOT_ACCEPTED", "insertion status mismatch")
    require(insertion["accepted_here"] is False, "principle accepted accidentally")
    require(insertion["must_not_be_used_as_free_patch"] is True, "free patch guard missing")
    for key, value in insertion["would_close"].items():
        require(value is True, f"insertion would-close missing: {key}")
    require(insertion["external_papers_modified"] is False, "external papers modified")

    require(if_inserted["status"] == "CONDITIONAL_WITNESS_VALIDATES_IF_PRINCIPLE_ACCEPTED_OR_DERIVED", "conditional status mismatch")
    for key in ["same_branch", "selected_variation_functional", "same_source_hessian", "sector_functor", "independence_certificate"]:
        require(if_inserted[key] is True, f"conditional kernel field missing: {key}")
    require(if_inserted["locked_target_values_used_as_source"] is False, "locked target used as source")
    require(if_inserted["residual_projector_replay_used_as_source"] is False, "residual replay used as source")
    require(len(if_inserted["attached_source_evidence"]) >= 4, "conditional evidence too thin")

    require(validator["ok"] is True, "conditional kernel validator should pass")
    require(validator["exit_code"] == 0, "conditional validator exit mismatch")

    require(
        decision["status"] == "DERIVATION_OPEN_EXPLICIT_INSERTION_READY_CONDITIONAL_KERNEL_VALIDATES",
        "decision status mismatch",
    )
    require(decision["unpatched_principle_derived_now"] is False, "decision overderived principle")
    require(decision["explicit_principle_accepted_now"] is False, "decision accepted principle")
    require(decision["conditional_kernel_validator_ok"] is True, "decision lost conditional validation")
    require(decision["current_kernel_closed_without_principle"] is False, "current kernel overclosed")
    require(decision["route_A_accepts_now"] is False, "Route A overaccepted")
    require(decision["route_B_accepts_now"] is False, "Route B overaccepted")
    require(decision["superset_strategy"]["locked_target_used_only_as_postcheck"] is True, "locked target misuse")
    require(decision["superset_strategy"]["paths_used_as_free_parameters"] is False, "paths treated as knobs")

    require(data["theorem"]["proved"] is True, "gate theorem missing")
    closure = data["closure_decision"]
    require(closure["unpatched_principle_derived_now"] is False, "candidate overderived principle")
    require(closure["explicit_principle_accepted_now"] is False, "candidate accepted principle")
    require(closure["conditional_kernel_validator_ok"] is True, "candidate lost conditional validator")
    require(closure["unpatched_dynamic_C1_closed"] is False, "candidate overclosed dynamic C1")
    require(closure["global_closure_claimed"] is False, "global closure overclaimed")
    for key in [
        "derivation_attempt_recorded",
        "explicit_principle_insertion_package_created",
        "conditional_kernel_closure_validated",
        "paper_ready_principle_text_created",
    ]:
        require(data["what_closes_now"][key] is True, f"achievement missing: {key}")

    require("not accepted here" in note, "note missing acceptance guard")
    require(NEXT in note, "note missing next target")

    for packet in [data, derivation, insertion, if_inserted, decision, cert]:
        guard(packet)

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
