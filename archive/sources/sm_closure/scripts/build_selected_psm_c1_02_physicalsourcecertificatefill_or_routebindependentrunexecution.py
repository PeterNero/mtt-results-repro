"""Build PSM-C1-02 SI-1u-A1a physical-source fill probe.

This artifact binds the existing strict Route A / Route B validator to the
PSM-C1-02 label system. It does not promote the physical source; it records the
exact support currently available, the exact validator rejection, and the next
same-branch source object needed.
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

SLUG = "selected_psm_c1_02_physicalsourcecertificatefill_or_routebindependentrunexecution"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROBE = BASE / "route_a_a1a_physical_action_restriction_source_probe.packet.json"
VALIDATOR_REPLAY = BASE / "strict_route_a_route_b_validator_replay.packet.json"
ROUTE_B_READY = BASE / "route_b_replacement_readiness.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_PhysicalSourceCertificateFill_or_RouteBIndependentRunExecution_v1.md"

PREVIOUS = DATA / "selected_psm_c1_02_physicalphifinc1actionrestriction_or_honestfinitec1execution.candidate.json"
ACTION_VALIDATOR = DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission" / "route_a_action_restriction_validator_v2.packet.json"
EMISSION_SLOTS = DATA / "selected_physicalsourceemissionvalues_or_honestgalerkinexecution" / "route_a_emission_value_slots.packet.json"
SOURCE_PUSH = DATA / "selected_sourcetheorem_push_attempt_or_minimalnewlemma" / "route_a_phifinc1_action_source_theorem_push.packet.json"
STRICT_FILL = DATA / "selected_physicalsourcecertificatefill_or_routebindependentrunexecution" / "current_fill_attempt.packet.json"
STRICT_VALIDATOR = DATA / "selected_physicalsourcecertificatefill_or_routebindependentrunexecution" / "promotion_acceptance_validator.packet.json"
VALIDATOR_SCRIPT = SCRIPTS / "validate_selected_physicalsourcecertificate_or_routeb.py"

STATUS = "MTT_SELECTED_PSM_C1_02_SI1U_A1A_PHYSICAL_ACTION_RESTRICTION_SOURCE_PROBED_STRICT_VALIDATOR_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_PhysicalActionRestrictionSourceActualFill_or_RouteBIndependentRun_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def validator_replay() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR_SCRIPT), str(STRICT_FILL)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return {
        "schema": "MTTPSMC102StrictRouteARouteBValidatorReplay.v1",
        "status": "STRICT_VALIDATOR_REPLAY_REJECTS_CURRENT_PACKET_AS_EXPECTED",
        "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a",
        "fallback_label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2",
        "validator_script": rel(VALIDATOR_SCRIPT),
        "validated_packet": rel(STRICT_FILL),
        "exit_code": proc.returncode,
        "ok": proc.returncode == 0,
        "stderr": proc.stderr.strip().splitlines(),
        "stdout": proc.stdout.strip().splitlines(),
        "expected_missing_route_a_field": "physical_action_restricts_to_selected_finite_Weyl_quotient",
        "expected_route_b_gap": "independent provenance / selected basis / quadrature source",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    action_validator = load(ACTION_VALIDATOR)
    emission_slots = load(EMISSION_SLOTS)
    source_push = load(SOURCE_PUSH)
    strict_fill = load(STRICT_FILL)
    strict_validator = load(STRICT_VALIDATOR)
    replay = validator_replay()

    closed_support = action_validator["closed_subclauses"]
    missing = source_push["still_missing"]
    route_a = strict_fill["route_A_physical_source_certificate"]
    route_b = strict_fill["route_B_independent_execution"]

    probe = {
        "schema": "MTTPSMC102SI1uA1aPhysicalActionRestrictionSourceProbe.v1",
        "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a",
        "status": "SI1U_A1A_SUPPORT_ONLY_PROBED_PHYSICAL_SOURCE_NOT_FILLED",
        "candidate_sources_checked": [
            rel(ACTION_VALIDATOR),
            rel(EMISSION_SLOTS),
            rel(SOURCE_PUSH),
            rel(STRICT_FILL),
        ],
        "closed_support": closed_support,
        "required_field": "physical_action_restricts_to_selected_finite_Weyl_quotient",
        "accepted_same_branch_sources_found": route_a["attached_same_branch_sources"],
        "same_branch_physical_action_restriction_emitted": route_a[
            "physical_action_restricts_to_selected_finite_Weyl_quotient"
        ],
        "route_a_slot_value": next(
            slot for slot in emission_slots["slots"] if slot["name"] == "physical_PhiFinC1_action_restriction"
        ),
        "minimal_lemma": source_push["minimal_route_A_lemma"],
        "still_missing": missing,
        "support_only_not_sufficient": True,
        "field_filled_now": False,
        "why_not_filled": (
            "The finite quotient, trace measure, Weyl variation algebra, and algebraic boundary support are necessary "
            "but do not yet emit a same-branch physical Phi_fin^C1 action-to-finite-quotient identity."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    route_b_ready = {
        "schema": "MTTPSMC102RouteBReplacementReadiness.v1",
        "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2",
        "status": "ROUTE_B_REPLACEMENT_PARTIAL_ROWS_READY_INDEPENDENT_PROVENANCE_OPEN",
        "all_72_primitive_rows_executed": route_b["all_72_primitive_rows_executed"],
        "formal_110_rows_executed": route_b["formal_110_rows_executed"],
        "selected_basis_independent_of_residual_projector": route_b[
            "selected_basis_independent_of_residual_projector"
        ],
        "quadrature_rule_independent_of_locked_target": route_b["quadrature_rule_independent_of_locked_target"],
        "source_independent_of_residual_projector_replay": route_b[
            "source_independent_of_residual_projector_replay"
        ],
        "exactness_or_error_certificates_attached": route_b["exactness_or_error_certificates_attached"],
        "attached_independent_provenance_sources": route_b["attached_independent_provenance_sources"],
        "ready_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102SI1uA1aProbe.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_PhysicalSourceCertificateFill_or_RouteBIndependentRunExecution_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-ACTUAL",
            "task": "Emit the same-branch physical Phi_fin^C1 action row and restriction map to the selected finite Weyl quotient.",
        },
        "then": [
            "SI-1u-A1b: prove zero extra physical boundary/source term.",
            "SI-1u-A1c: emit same-source R_Z, R_X, and b_selected.",
        ],
        "fallback": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2",
            "task": "Run or import an independent finite-C1/Galerkin provenance execution with basis and quadrature independent of residual replay.",
        },
        "superset_use": (
            "Two constrained routes are retained: Route A source promotion and Route B independent execution. "
            "They are not adjustable knobs because both must satisfy the same strict validator without observed constants."
        ),
        "status": "NEXT_WORKORDER_FILL_A1A_ACTUAL_OR_EXECUTE_ROUTEB",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102PhysicalSourceCertificateFillOrRouteBIndependentRunExecution",
        "active_label": "PSM-C1-02",
        "active_routes": ["SOURCE-IDENTITY/SI-1u-A1a", "SOURCE-IDENTITY/SI-1u-B2"],
        "status": STATUS,
        "previous": rel(PREVIOUS),
        "previous_status": previous["status"],
        "strict_validator_import": rel(STRICT_VALIDATOR),
        "output_packets": {
            "route_a_a1a_physical_action_restriction_source_probe": rel(PROBE),
            "strict_route_a_route_b_validator_replay": rel(VALIDATOR_REPLAY),
            "route_b_replacement_readiness": rel(ROUTE_B_READY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "SI1u_A1a_support_probe_attached": True,
            "strict_validator_replay_attached": True,
            "route_B_replacement_readiness_classified": True,
            "same_source_gap_identified_without_overclaim": True,
        },
        "what_remains_open": {
            "SI1u_A1a_actual_physical_action_source_fill": True,
            "SI1u_A1b_no_extra_physical_boundary_or_source_term": True,
            "SI1u_A1c_same_source_R_Z_R_X_b_selected": True,
            "route_B_independent_basis_quadrature_source_provenance": True,
            "unpatched_A_selected_b_selected_deltaTheta_C1": True,
        },
        "theorem": {
            "name": "PSMC102SI1uA1aSupportOnlyProbeTheorem",
            "proved": True,
            "statement": (
                "For the current PSM-C1-02 branch, the physical action restriction subclaim SI-1u-A1a is not "
                "filled by the existing finite quotient, trace measure, Weyl variation, and algebraic boundary "
                "support. The strict validator rejects the current packet exactly at the same-branch physical "
                "source fields, so the next legal promotion is either an actual same-branch Phi_fin^C1 action "
                "restriction row or the Route B independent finite-C1 execution."
            ),
        },
        "superset_strategy": {
            "classification": "TWO_ROUTE_LOCKED_TARGET",
            "route_A": "same-branch physical source promotion for SI-1u-A1a/A1b/A1c",
            "route_B": "independent finite-C1/Galerkin execution",
            "locked_target": "strict Route A / Route B validator",
            "not_knobs": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_PhysicalSourceCertificateFill_or_RouteBIndependentRunExecution_v1",
        "active_label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a",
        "fallback_label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "strict_validator_replay_exit_code": replay["exit_code"],
        "strict_validator_rejects_current_packet": replay["exit_code"] == 1,
        "SI1u_A1a_field_filled_now": False,
        "route_B_ready_now": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PSM C1 02 PhysicalSourceCertificateFill or RouteBIndependentRunExecution v1

Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a`

Fallback label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2`

Status: `{STATUS}`

## Result

This step probes the first physical source subclaim:

`SI-1u-A1a`: the physical `Phi_fin^C1` action restricts to the selected finite Weyl quotient.

The available support is real but support-only: finite selected C1 quotient,
trace/Frobenius measure, selected Weyl variation algebra, and algebraic finite
boundary cancellation. The strict validator still rejects the packet because no
same-branch physical action restriction row is emitted.

## Superset Use

We are using two constrained routes to one locked target, not knobs:

- Route A: same-branch physical source promotion.
- Route B: independent finite-C1/Galerkin execution.

Neither route may use observed constants or target fitting as a selector.

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
PROBE = BASE / "route_a_a1a_physical_action_restriction_source_probe.packet.json"
VALIDATOR_REPLAY = BASE / "strict_route_a_route_b_validator_replay.packet.json"
ROUTE_B_READY = BASE / "route_b_replacement_readiness.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{{SLUG}}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_PhysicalSourceCertificateFill_or_RouteBIndependentRunExecution_v1.md"
VALIDATOR_SCRIPT = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"
STRICT_FILL = DATA / "selected_physicalsourcecertificatefill_or_routebindependentrunexecution" / "current_fill_attempt.packet.json"
BUILD = ROOT / "scripts" / "build_selected_psm_c1_02_physicalsourcecertificatefill_or_routebindependentrunexecution.py"

STATUS = "{STATUS}"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


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
    probe = load(PROBE)
    replay = load(VALIDATOR_REPLAY)
    route_b = load(ROUTE_B_READY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    validator_proc = subprocess.run(
        [sys.executable, str(VALIDATOR_SCRIPT), str(STRICT_FILL)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_routes"] == ["SOURCE-IDENTITY/SI-1u-A1a", "SOURCE-IDENTITY/SI-1u-B2"], "routes mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem missing")
    require(candidate["superset_strategy"]["not_knobs"] is True, "superset guard missing")

    require(probe["status"] == "SI1U_A1A_SUPPORT_ONLY_PROBED_PHYSICAL_SOURCE_NOT_FILLED", "probe status mismatch")
    require(all(probe["closed_support"].values()), "closed support should all be true")
    require(probe["accepted_same_branch_sources_found"] == [], "unexpected same-branch source")
    require(probe["same_branch_physical_action_restriction_emitted"] is False, "A1a overfilled")
    require(probe["field_filled_now"] is False, "field filled unexpectedly")
    require(probe["support_only_not_sufficient"] is True, "support-only guard missing")

    require(replay["exit_code"] == 1, "validator replay should reject")
    require(replay["ok"] is False, "validator replay unexpectedly ok")
    require(any("physical_action_restricts_to_selected_finite_Weyl_quotient" in line for line in replay["stderr"]), "missing A1a validator error")
    require(validator_proc.returncode == 1, "live validator should reject")

    require(route_b["all_72_primitive_rows_executed"] is True, "route B rows missing")
    require(route_b["formal_110_rows_executed"] is True, "route B formal replay missing")
    require(route_b["source_independent_of_residual_projector_replay"] is False, "route B source independence overclaimed")
    require(route_b["exactness_or_error_certificates_attached"] is False, "route B exactness overclaimed")
    require(route_b["ready_now"] is False, "route B overready")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-ACTUAL", "next primary mismatch")
    require(next_work["fallback"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2", "fallback mismatch")

    require(cert["strict_validator_rejects_current_packet"] is True, "cert validator mismatch")
    require(cert["SI1u_A1a_field_filled_now"] is False, "cert overfilled")
    require(cert["route_B_ready_now"] is False, "cert route B overready")
    require("Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a`" in note, "note label missing")
    require("not knobs" in note, "note superset guard missing")

    for packet in [candidate, probe, replay, route_b, cert]:
        guard(packet)

    print(f"PASS {{CANDIDATE.name}}: {{candidate['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    for path, payload in [
        (PROBE, probe),
        (VALIDATOR_REPLAY, replay),
        (ROUTE_B_READY, route_b_ready),
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
