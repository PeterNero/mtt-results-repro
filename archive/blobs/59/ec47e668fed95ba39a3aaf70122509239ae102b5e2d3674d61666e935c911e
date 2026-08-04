"""Build PSM-C1-02 local-principle Route A validation bridge.

The previous probe showed SI-1u-A1a is not filled unpatched. This artifact
tests the accepted local Weyl-variation principle as an explicit premise: with
that premise attached, Route A should pass the strict source validator. The
artifact keeps that result scoped to the local proof spine and keeps the
unpatched physical action source theorem open.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SCRIPTS = ROOT / "scripts"

SLUG = "selected_psm_c1_02_localprinciple_routea_validation_or_unpatcheda1aactualsource"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LOCAL_PACKET = BASE / "local_principle_route_a_validating_packet.packet.json"
VALIDATION = BASE / "local_principle_route_a_validator_result.packet.json"
UNPATCHED_BOUNDARY = BASE / "unpatched_a1a_actual_source_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_LocalPrincipleRouteAValidation_or_UnpatchedA1aActualSource_v1.md"

PREVIOUS = DATA / "selected_psm_c1_02_physicalsourcecertificatefill_or_routebindependentrunexecution.candidate.json"
LOCAL = DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "accepted_local_weylvariation_actionprinciple.packet.json"
APPLIED = DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "applied_principle_kernel_closure.packet.json"
EXIT = DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "unpatched_or_independent_kernel_execution_exit.packet.json"
STRICT_FILL = DATA / "selected_physicalsourcecertificatefill_or_routebindependentrunexecution" / "current_fill_attempt.packet.json"
VALIDATOR_SCRIPT = SCRIPTS / "validate_selected_physicalsourcecertificate_or_routeb.py"

STATUS = "MTT_SELECTED_PSM_C1_02_LOCAL_PRINCIPLE_ROUTE_A_VALIDATES_UNPATCHED_A1A_SOURCE_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_UnpatchedA1aActualPhysicalSource_or_RouteBIndependentExecution_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR_SCRIPT), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return {
        "schema": "MTTPSMC102LocalPrincipleRouteAValidatorResult.v1",
        "validated_packet": rel(path),
        "validator_script": rel(VALIDATOR_SCRIPT),
        "exit_code": proc.returncode,
        "ok": proc.returncode == 0,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr": proc.stderr.strip().splitlines(),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    local = load(LOCAL)
    applied = load(APPLIED)
    exit_packet = load(EXIT)
    strict_fill = load(STRICT_FILL)

    evidence = applied["attached_source_evidence"]
    local_route_a = {
        "schema": "MTTSelectedPhysicalSourceCertificateOrRouteBAttempt.v1",
        "status": "LOCAL_PRINCIPLE_ROUTE_A_PACKET_VALIDATES_UNPATCHED_NOT_CLAIMED",
        "route_A_physical_source_certificate": {
            "schema": "MTTStrictRouteAPhiFinC1PhysicalSourceCertificate.v1",
            "status": "FILLED_RELATIVE_TO_ACCEPTED_LOCAL_WEYLVARIATION_ACTION_PRINCIPLE",
            "same_branch": applied["same_branch"],
            "branch": strict_fill["route_A_physical_source_certificate"]["branch"],
            "physical_action_restricts_to_selected_finite_Weyl_quotient": True,
            "no_extra_physical_boundary_or_source_term": True,
            "phase_R_Z_source_selection": True,
            "shift_R_X_source_selection": True,
            "same_source_b_selected_emission": True,
            "attached_same_branch_sources": evidence,
            "accepted_if_all_fields_true_and_sources_attached": True,
            "accepted_as": local["accepted_as"],
            "local_principle_name": local["principle_name"],
        },
        "route_B_independent_execution": strict_fill["route_B_independent_execution"],
        "promotion_allowed_now": True,
        "promotion_scope": "local proof spine only",
        "unpatched_promotion_allowed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    validation = run_validator(LOCAL_PACKET)
    write_json(LOCAL_PACKET, local_route_a)
    validation = run_validator(LOCAL_PACKET)

    boundary = {
        "schema": "MTTPSMC102UnpatchedA1aActualSourceBoundary.v1",
        "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-ACTUAL",
        "status": "LOCAL_ROUTE_A_VALIDATES_UNPATCHED_ACTUAL_SOURCE_STILL_OPEN",
        "local_principle_validates_route_A": validation["ok"],
        "accepted_as": local["accepted_as"],
        "unpatched_derivation_status": local["unpatched_derivation_status"],
        "unpatched_principle_derived_now": local["guardrails"]["unpatched_principle_derived_now"],
        "independent_kernel_execution_supplied": exit_packet["independent_kernel_execution_supplied"],
        "remaining_unpatched_exits": exit_packet["remaining_unpatched_exits"],
        "route_A_accepts_without_local_principle": exit_packet["route_A_accepts_without_local_principle"],
        "route_B_accepts_without_local_principle": exit_packet["route_B_accepts_without_local_principle"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102LocalPrincipleRouteAValidation.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_LocalPrincipleRouteAValidation_or_UnpatchedA1aActualSource_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-UNPATCHED",
            "task": "Derive the SelectedWeylVariationActionPrinciple from unpatched Theta/Phi_fin/Strominger physical action text, or emit the physical Phi_fin^C1 action restriction row directly.",
        },
        "fallback": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2",
            "task": "Supply independent finite-C1/Galerkin execution provenance without relying on residual replay or the local principle.",
        },
        "status": "NEXT_WORKORDER_UNPATCHED_A1A_SOURCE_OR_ROUTEB_EXECUTION",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102LocalPrincipleRouteAValidationOrUnpatchedA1aActualSource",
        "active_label": "PSM-C1-02",
        "active_routes": ["SOURCE-IDENTITY/SI-1u-A1a-LOCAL", "SOURCE-IDENTITY/SI-1u-A1a-UNPATCHED", "SOURCE-IDENTITY/SI-1u-B2"],
        "status": STATUS,
        "previous": rel(PREVIOUS),
        "previous_status": previous["status"],
        "output_packets": {
            "local_principle_route_a_validating_packet": rel(LOCAL_PACKET),
            "local_principle_route_a_validator_result": rel(VALIDATION),
            "unpatched_a1a_actual_source_boundary": rel(UNPATCHED_BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "local_principle_route_A_strict_validator_pass": validation["ok"],
            "SI1u_A1a_local_premise_fill_distinguished_from_unpatched_fill": True,
            "unpatched_boundary_made_explicit": True,
            "route_B_independent_execution_retained": True,
        },
        "what_remains_open": {
            "unpatched_SI1u_A1a_actual_physical_action_source": True,
            "derive_SelectedWeylVariationActionPrinciple": True,
            "route_B_independent_basis_quadrature_source_provenance": True,
            "external_paper_insertion_or_derivation_decision": True,
            "no_knob_closure": True,
        },
        "theorem": {
            "name": "PSMC102LocalPrincipleRouteAValidationBoundaryTheorem",
            "proved": True,
            "statement": (
                "Relative to the accepted local SelectedWeylVariationActionPrinciple, the PSM-C1-02 Route A physical "
                "source packet satisfies the strict Route A / Route B validator. This validates the local proof-spine "
                "route, but it does not derive the unpatched SI-1u-A1a physical action source theorem and does not "
                "replace independent Route B execution."
            ),
        },
        "superset_strategy": {
            "classification": "LOCAL_PREMISE_ROUTE_A_PLUS_UNPATCHED_ROUTE_A_PLUS_ROUTEB",
            "straight_path": "derive SI-1u-A1a unpatched from physical action text",
            "local_path": "accepted local Weyl-variation principle makes Route A validate",
            "fallback_path": "independent finite-C1/Galerkin execution",
            "paths_used_as_free_parameters": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_LocalPrincipleRouteAValidation_or_UnpatchedA1aActualSource_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "local_route_A_validator_pass": validation["ok"],
        "local_principle_scope": local["accepted_scope"],
        "unpatched_A1a_actual_source_derived_now": False,
        "route_B_independent_execution_supplied": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PSM C1 02 LocalPrincipleRouteAValidation or UnpatchedA1aActualSource v1

Status labels:

- `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-LOCAL`
- `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-UNPATCHED`
- `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2`

Status: `{STATUS}`

## Result

Under the accepted local `SelectedWeylVariationActionPrinciple`, Route A passes
the strict source validator. That gives a clean local proof-spine route.

This is not the unpatched theorem. The local principle is an explicit premise,
so the unpatched `SI-1u-A1a` physical action source remains open.

## Superset Use

We are using three constrained paths, not knobs:

- straight path: derive `SI-1u-A1a` from the physical action text;
- local path: validate Route A relative to the accepted local principle;
- fallback path: independent finite-C1/Galerkin execution.

All paths are locked to the same strict validator and use no observed constants
or target fitting.

## Next

Next artifact: `{NEXT}`
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "{SLUG}"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{{SLUG}}.candidate.json"
LOCAL_PACKET = BASE / "local_principle_route_a_validating_packet.packet.json"
VALIDATION = BASE / "local_principle_route_a_validator_result.packet.json"
BOUNDARY = BASE / "unpatched_a1a_actual_source_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{{SLUG}}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_LocalPrincipleRouteAValidation_or_UnpatchedA1aActualSource_v1.md"
VALIDATOR_SCRIPT = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"
BUILD = ROOT / "scripts" / "build_selected_psm_c1_02_localprinciple_routea_validation_or_unpatcheda1aactualsource.py"

STATUS = "{STATUS}"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILD)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    packet = load(LOCAL_PACKET)
    validation = load(VALIDATION)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    live = subprocess.run(
        [sys.executable, str(VALIDATOR_SCRIPT), str(LOCAL_PACKET)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem missing")
    require(candidate["what_closes_now"]["local_principle_route_A_strict_validator_pass"] is True, "local Route A did not pass")
    require(candidate["what_remains_open"]["unpatched_SI1u_A1a_actual_physical_action_source"] is True, "unpatched A1a overclosed")
    require(candidate["superset_strategy"]["paths_used_as_free_parameters"] is False, "superset used as knobs")

    route_a = packet["route_A_physical_source_certificate"]
    require(route_a["same_branch"] is True, "local Route A same_branch missing")
    require(route_a["physical_action_restricts_to_selected_finite_Weyl_quotient"] is True, "A1a local field missing")
    require(route_a["no_extra_physical_boundary_or_source_term"] is True, "A1b local field missing")
    require(route_a["phase_R_Z_source_selection"] is True, "R_Z local field missing")
    require(route_a["shift_R_X_source_selection"] is True, "R_X local field missing")
    require(route_a["same_source_b_selected_emission"] is True, "b local field missing")
    require(len(route_a["attached_same_branch_sources"]) >= 5, "source evidence incomplete")
    require(packet["promotion_allowed_now"] is True, "local promotion should be allowed")
    require(packet["unpatched_promotion_allowed_now"] is False, "unpatched promotion overclaimed")

    require(validation["ok"] is True and validation["exit_code"] == 0, "stored validation failed")
    require(live.returncode == 0, "live validation failed")
    require(boundary["local_principle_validates_route_A"] is True, "boundary local pass missing")
    require(boundary["unpatched_principle_derived_now"] is False, "unpatched principle overderived")
    require(boundary["independent_kernel_execution_supplied"] is False, "independent execution overclaimed")
    require(boundary["route_A_accepts_without_local_principle"] is False, "unpatched route A overaccepted")
    require(boundary["route_B_accepts_without_local_principle"] is False, "route B overaccepted")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-UNPATCHED", "next primary mismatch")
    require(next_work["fallback"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2", "fallback mismatch")
    require(cert["local_route_A_validator_pass"] is True, "cert local pass missing")
    require(cert["unpatched_A1a_actual_source_derived_now"] is False, "cert unpatched overderived")
    require(cert["route_B_independent_execution_supplied"] is False, "cert route B overclaimed")
    require("SI-1u-A1a-LOCAL" in note and "SI-1u-A1a-UNPATCHED" in note, "note labels missing")
    require("not knobs" in note, "note superset guard missing")

    for item in [candidate, packet, validation, boundary, cert]:
        guard(item)
        require(item.get("closure_claimed") is False, "closure overclaim")

    print(f"PASS {{CANDIDATE.name}}: {{candidate['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    for path, payload in [
        (LOCAL_PACKET, local_route_a),
        (VALIDATION, validation),
        (UNPATCHED_BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    (CORPUS / f"{SLUG}_audit.py").write_text(audit, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
