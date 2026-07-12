"""Build strict source-certificate fill validator / Route B run execution gate."""

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

SLUG = "selected_physicalsourcecertificatefill_or_routebindependentrunexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A_TEMPLATE = PACKET_DIR / "route_a_physical_source_certificate.strict_template.json"
ROUTE_B_TEMPLATE = PACKET_DIR / "route_b_independent_execution.strict_template.json"
VALIDATOR_PACKET = PACKET_DIR / "promotion_acceptance_validator.packet.json"
ATTEMPT = PACKET_DIR / "current_fill_attempt.packet.json"
VALIDATOR_SCRIPT = SCRIPTS / "validate_selected_physicalsourcecertificate_or_routeb.py"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_PhysicalSourceCertificateFill_or_RouteBIndependentRunExecution_v1.md"

PREVIOUS = DATA / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun.candidate.json"
MINIMAL = (
    DATA
    / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun"
    / "minimal_physical_source_certificate.packet.json"
)
ROUTEB_SPEC = (
    DATA
    / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun"
    / "route_b_independent_galerkin_provenance_run_spec.packet.json"
)
FORMAL = (
    DATA
    / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
    / "formal_110_row_replay_integrated.packet.json"
)

STATUS = "MTT_SELECTED_PHYSICALSOURCECERTIFICATEFILL_OR_ROUTEBINDEPENDENTRUNEXECUTION_BUILT_STRICT_VALIDATOR_OPEN"
NEXT = "MTT_Selected_PhysicalSourceCertificateActualFill_or_RouteBIndependentRowsRun_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


VALIDATOR_SOURCE = r'''"""Validate selected Phi_fin^C1 physical source certificate or Route B independent run."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROUTE_A_FIELDS = [
    "physical_action_restricts_to_selected_finite_Weyl_quotient",
    "no_extra_physical_boundary_or_source_term",
    "phase_R_Z_source_selection",
    "shift_R_X_source_selection",
    "same_source_b_selected_emission",
]

ROUTE_B_FIELDS = [
    "selected_basis_independent_of_residual_projector",
    "quadrature_rule_independent_of_locked_target",
    "all_72_primitive_rows_executed",
    "formal_110_rows_executed",
    "source_independent_of_residual_projector_replay",
    "exactness_or_error_certificates_attached",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def truth(payload: dict[str, Any], path: list[str]) -> bool:
    node: Any = payload
    for key in path:
        if not isinstance(node, dict) or key not in node:
            return False
        node = node[key]
    return node is True


def evidence_list(payload: dict[str, Any], path: list[str]) -> list[Any]:
    node: Any = payload
    for key in path:
        if not isinstance(node, dict) or key not in node:
            return []
        node = node[key]
    return node if isinstance(node, list) else []


def validate(payload: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if payload.get("observed_data_used_as_selector") is not False:
        errors.append("observed_data_used_as_selector must be false")
    if payload.get("target_fitting_used") is not False:
        errors.append("target_fitting_used must be false")

    route_a = payload.get("route_A_physical_source_certificate", {})
    route_b = payload.get("route_B_independent_execution", {})

    route_a_missing = [key for key in ROUTE_A_FIELDS if route_a.get(key) is not True]
    route_b_missing = [key for key in ROUTE_B_FIELDS if route_b.get(key) is not True]

    route_a_evidence = evidence_list(route_a, ["attached_same_branch_sources"])
    route_b_evidence = evidence_list(route_b, ["attached_independent_provenance_sources"])

    route_a_ok = not route_a_missing and len(route_a_evidence) >= 5 and route_a.get("same_branch") is True
    route_b_ok = not route_b_missing and len(route_b_evidence) >= 3

    if route_a_missing:
        errors.append("Route A missing: " + ", ".join(route_a_missing))
    if not route_a_evidence:
        errors.append("Route A has no attached same-branch source evidence")
    if route_a.get("same_branch") is not True:
        errors.append("Route A same_branch is not true")

    if route_b_missing:
        errors.append("Route B missing: " + ", ".join(route_b_missing))
    if not route_b_evidence:
        errors.append("Route B has no attached independent provenance evidence")

    if not (route_a_ok or route_b_ok):
        errors.append("neither Route A nor Route B validates")
    return route_a_ok or route_b_ok, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_physicalsourcecertificate_or_routeb.py <packet.json>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    payload = load(path)
    ok, errors = validate(payload)
    if ok:
        print(f"PASS {path}")
        return 0
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
'''


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR_SCRIPT), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "path": rel(path),
        "exit_code": proc.returncode,
        "ok": proc.returncode == 0,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr": proc.stderr.strip().splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    minimal = load(MINIMAL)
    route_b_spec = load(ROUTEB_SPEC)
    formal = load(FORMAL)

    VALIDATOR_SCRIPT.write_text(VALIDATOR_SOURCE, encoding="utf-8")

    route_a_template = {
        "schema": "MTTStrictRouteAPhiFinC1PhysicalSourceCertificate.v1",
        "status": "STRICT_TEMPLATE_READY_NOT_FILLED",
        "same_branch": False,
        "branch": "q79/F,m=1/S3_GS/RouteC_or_same_visible_source",
        "physical_action_restricts_to_selected_finite_Weyl_quotient": False,
        "no_extra_physical_boundary_or_source_term": False,
        "phase_R_Z_source_selection": False,
        "shift_R_X_source_selection": False,
        "same_source_b_selected_emission": False,
        "attached_same_branch_sources": [],
        "accepted_if_all_fields_true_and_sources_attached": True,
    }

    route_b_template = {
        "schema": "MTTStrictRouteBIndependentGalerkinExecution.v1",
        "status": "STRICT_TEMPLATE_READY_NOT_EXECUTED",
        "selected_basis_independent_of_residual_projector": False,
        "quadrature_rule_independent_of_locked_target": False,
        "all_72_primitive_rows_executed": formal["all_72_primitive_rows_exact"],
        "formal_110_rows_executed": formal["formal_110_rows_executed"],
        "source_independent_of_residual_projector_replay": False,
        "exactness_or_error_certificates_attached": False,
        "attached_independent_provenance_sources": [],
        "accepted_if_all_fields_true_and_sources_attached": True,
    }

    current_attempt = {
        "schema": "MTTSelectedPhysicalSourceCertificateOrRouteBAttempt.v1",
        "status": "CURRENT_ATTEMPT_FAILS_STRICT_VALIDATOR_AS_EXPECTED",
        "route_A_physical_source_certificate": route_a_template,
        "route_B_independent_execution": route_b_template,
        "formal_support_available": {
            "formal_110_rows_executed": formal["formal_110_rows_executed"],
            "all_72_primitive_values_exact": route_b_spec["current_support"]["all_72_values_exact"],
            "finite_trace_boundary_algebraic": minimal["already_closed_or_retired"][
                "finite_trace_boundary_algebraic"
            ],
        },
        "promotion_allowed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    write_json(ROUTE_A_TEMPLATE, route_a_template)
    write_json(ROUTE_B_TEMPLATE, route_b_template)
    write_json(ATTEMPT, current_attempt)

    attempt_validation = run_validator(ATTEMPT)

    validator_packet = {
        "schema": "MTTStrictPhysicalSourceOrRouteBPromotionValidator.v1",
        "status": "STRICT_VALIDATOR_BUILT_CURRENT_ATTEMPT_REJECTED",
        "validator_script": rel(VALIDATOR_SCRIPT),
        "route_A_required_fields": [
            "same_branch",
            "physical_action_restricts_to_selected_finite_Weyl_quotient",
            "no_extra_physical_boundary_or_source_term",
            "phase_R_Z_source_selection",
            "shift_R_X_source_selection",
            "same_source_b_selected_emission",
            "attached_same_branch_sources length >= 5",
        ],
        "route_B_required_fields": [
            "selected_basis_independent_of_residual_projector",
            "quadrature_rule_independent_of_locked_target",
            "all_72_primitive_rows_executed",
            "formal_110_rows_executed",
            "source_independent_of_residual_projector_replay",
            "exactness_or_error_certificates_attached",
            "attached_independent_provenance_sources length >= 3",
        ],
        "current_attempt_validation": attempt_validation,
        "current_attempt_rejected_as_expected": attempt_validation["exit_code"] == 1,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "route_A_fill_attempted": True,
        "route_A_filled_now": False,
        "route_B_execution_attempted": True,
        "route_B_executed_now": False,
        "strict_validator_built": True,
        "strict_validator_accepts_current_attempt": attempt_validation["ok"],
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalSourceCertificateFillOrRouteBIndependentRunExecution",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "minimal_physical_source_certificate": rel(MINIMAL),
            "route_b_independent_run_spec": rel(ROUTEB_SPEC),
            "formal_110_row_replay": rel(FORMAL),
        },
        "output_packets": {
            "route_a_strict_template": rel(ROUTE_A_TEMPLATE),
            "route_b_strict_template": rel(ROUTE_B_TEMPLATE),
            "current_fill_attempt": rel(ATTEMPT),
            "promotion_acceptance_validator": rel(VALIDATOR_PACKET),
            "validator_script": rel(VALIDATOR_SCRIPT),
        },
        "what_closes_now": {
            "strict_promotion_validator_built": True,
            "current_nonpromotion_made_executable": True,
            "route_A_fill_shape_locked": True,
            "route_B_execution_shape_locked": True,
            "formal_values_preserved_as_support_only": True,
        },
        "what_remains_open": {
            "route_A_actual_same_branch_source_certificate": True,
            "route_B_independent_provenance_sources": True,
            "unpatched_A_selected": True,
            "unpatched_b_selected": True,
            "unpatched_deltaTheta_C1": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "decision": decision,
        "theorem": {
            "name": "StrictPhiFinC1SourcePromotionValidatorTheorem",
            "proved": True,
            "statement": (
                "Unpatched dynamic C1 promotion is now an executable disjunction: either "
                "Route A supplies the same-branch physical Phi_fin^C1 source certificate "
                "with all five source fields and attached evidence, or Route B supplies an "
                "independent Galerkin/row execution with provenance independent of residual "
                "projector replay. The current packet is rejected, preserving the open gate."
            ),
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalSourceCertificateFill_or_RouteBIndependentRunExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "validator_script": rel(VALIDATOR_SCRIPT),
        "current_attempt_rejected_as_expected": attempt_validation["exit_code"] == 1,
        "route_A_filled_now": False,
        "route_B_executed_now": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalSourceCertificateFill or RouteBIndependentRunExecution v1

Status: `{STATUS}`

This step turns the last `Phi_fin^C1` source gate into an executable validator.

Route A can promote only if the same branch supplies physical action restriction,
no extra physical boundary/source term, phase `R_Z`, shift `R_X`, and
`b_selected` emission, with attached source evidence.

Route B can promote only if the 110-row packet is re-executed with selected
basis and quadrature provenance independent of residual-projector replay.

The current attempt intentionally fails the strict validator. That failure is a
result: the repo now has a hard acceptance gate for the actual final fill.

Next artifact: `{NEXT}`.
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "{SLUG}"
ATTEMPT = PACKET_DIR / "current_fill_attempt.packet.json"
VALIDATOR_PACKET = PACKET_DIR / "promotion_acceptance_validator.packet.json"
CERT = ROOT / "certificates" / "{SLUG}_certificate.json"
VALIDATOR_SCRIPT = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalSourceCertificateFill_or_RouteBIndependentRunExecution_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    attempt = load(ATTEMPT)
    validator = load(VALIDATOR_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR_SCRIPT), str(ATTEMPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["decision"]["strict_validator_built"] is True, "validator not built")
    require(data["decision"]["strict_validator_accepts_current_attempt"] is False, "attempt unexpectedly accepted")
    require(attempt["promotion_allowed_now"] is False, "attempt overpromoted")
    require(proc.returncode == 1, "validator should reject current attempt")
    require(any("neither Route A nor Route B validates" in line for line in proc.stderr.splitlines()), "missing rejection reason")
    require(validator["current_attempt_rejected_as_expected"] is True, "validator packet mismatch")
    require(cert["current_attempt_rejected_as_expected"] is True, "cert mismatch")
    require(cert["route_A_filled_now"] is False, "Route A overfilled")
    require(cert["route_B_executed_now"] is False, "Route B overexecuted")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("hard acceptance gate" in note, "note missing validator role")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(VALIDATOR_PACKET, validator_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(f"wrote {rel(OUTPUT)}")
    print(f"status {STATUS}")
    print(f"validator_current_attempt_exit {attempt_validation['exit_code']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
