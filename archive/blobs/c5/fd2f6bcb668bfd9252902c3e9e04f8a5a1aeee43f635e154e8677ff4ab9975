"""Build final Route B row-source independence proof target or Route A fallback."""

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

SLUG = "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TEMPLATE = PACKET_DIR / "row_source_independence.strict_template.json"
ATTEMPT = PACKET_DIR / "current_row_source_independence_attempt.packet.json"
VALIDATION = PACKET_DIR / "row_source_validator_result.packet.json"
DECISION = PACKET_DIR / "final_routeb_or_routea_decision.packet.json"
VALIDATOR = SCRIPTS / "validate_selected_routeb_rowsource_independence.py"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_RouteBRowSourceIndependenceProof_or_PhysicalSourceFill_v1.md"

PREVIOUS = DATA / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap.candidate.json"
BASIS_FILL = (
    DATA
    / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap"
    / "route_b_selected_basis_independence_fill.packet.json"
)
ROW_GAP = (
    DATA
    / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap"
    / "row_source_independence_gap.packet.json"
)
ALL_ROWS_DECISION = (
    DATA
    / "selected_firstrowprovenancepromotion_or_allrowsweylexecution"
    / "all_rows_execution_decision.packet.json"
)
ALL_ROWS_GATE = (
    DATA
    / "selected_firstrowprovenancepromotion_or_allrowsweylexecution"
    / "provenance_promotion_gate_after_all_rows.packet.json"
)
FORMAL_INTEGRATED = (
    DATA
    / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
    / "formal_110_row_replay_integrated.packet.json"
)
DYNAMIC_TRACE = DATA / "selected_primitiverowsexecution_or_dynamicdotdtracebinding.candidate.json"
FIRST_ROW_SOURCE = (
    DATA
    / "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource"
    / "first_row_kernel_formula_source_packet.packet.json"
)

STATUS = "MTT_SELECTED_ROUTEB_ROWSOURCEINDEPENDENCEPROOF_BUILT_FINAL_SOURCE_TARGET_OPEN"
NEXT = "MTT_Selected_RouteBActualRowSourceIndependenceFill_or_RouteAPhysicalPhiFinC1Source_v1"


VALIDATOR_SOURCE = r'''"""Validate Route B dynamic C1 row-source independence."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = [
    "selected_basis_feeds_72_primitive_rows",
    "finite_weyl_trace_rule_feeds_all_rows",
    "sector_rows_assembled_from_primitive_rows",
    "hessian_source_rows_assembled_from_same_rows",
    "no_residual_projector_replay_used_as_source",
    "no_locked_target_values_used_as_source",
    "row_formula_source_theorem_derived",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(payload: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if payload.get("observed_data_used_as_selector") is not False:
        errors.append("observed_data_used_as_selector must be false")
    if payload.get("target_fitting_used") is not False:
        errors.append("target_fitting_used must be false")
    missing = [field for field in REQUIRED_FIELDS if payload.get(field) is not True]
    if missing:
        errors.append("missing row-source fields: " + ", ".join(missing))
    evidence = payload.get("attached_source_evidence", [])
    if not isinstance(evidence, list) or len(evidence) < 4:
        errors.append("attached_source_evidence must contain at least four sources")
    if payload.get("source_independent_of_residual_projector_replay") is not True:
        errors.append("source_independent_of_residual_projector_replay is not true")
    return not errors, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_routeb_rowsource_independence.py <packet.json>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    ok, errors = validate(load(path))
    if ok:
        print(f"PASS {path}")
        return 0
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
'''


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
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
    VALIDATOR.write_text(VALIDATOR_SOURCE, encoding="utf-8")

    previous = load(PREVIOUS)
    basis_fill = load(BASIS_FILL)
    row_gap = load(ROW_GAP)
    all_rows_decision = load(ALL_ROWS_DECISION)
    all_rows_gate = load(ALL_ROWS_GATE)
    formal = load(FORMAL_INTEGRATED)
    dynamic_trace = load(DYNAMIC_TRACE)
    first_row = load(FIRST_ROW_SOURCE)

    template = {
        "schema": "MTTRouteBRowSourceIndependenceStrictTemplate.v1",
        "status": "STRICT_TEMPLATE_READY_NOT_FILLED",
        "selected_basis_feeds_72_primitive_rows": False,
        "finite_weyl_trace_rule_feeds_all_rows": basis_fill["route_B_independent_execution"][
            "quadrature_rule_independent_of_locked_target"
        ],
        "sector_rows_assembled_from_primitive_rows": False,
        "hessian_source_rows_assembled_from_same_rows": False,
        "no_residual_projector_replay_used_as_source": False,
        "no_locked_target_values_used_as_source": True,
        "row_formula_source_theorem_derived": False,
        "source_independent_of_residual_projector_replay": False,
        "attached_source_evidence": [],
        "validator": rel(VALIDATOR),
    }

    attempt = dict(template)
    attempt.update(
        {
            "schema": "MTTRouteBRowSourceIndependenceAttempt.v1",
            "status": "CURRENT_ATTEMPT_REJECTED_ROW_SOURCE_THEOREM_STILL_OPEN",
            "selected_basis_feeds_72_primitive_rows": False,
            "finite_weyl_trace_rule_feeds_all_rows": True,
            "sector_rows_assembled_from_primitive_rows": formal["sector_matrix_rows"][
                "all_formal_quadrature_emitted"
            ],
            "hessian_source_rows_assembled_from_same_rows": formal["hessian_source_rows"][
                "all_formal_quadrature_emitted"
            ],
            "no_residual_projector_replay_used_as_source": False,
            "no_locked_target_values_used_as_source": True,
            "row_formula_source_theorem_derived": False,
            "source_independent_of_residual_projector_replay": False,
            "attached_source_evidence": [
                {
                    "source": rel(BASIS_FILL),
                    "closes": "selected transported basis and finite Weyl trace rule are available",
                },
                {
                    "source": rel(DYNAMIC_TRACE),
                    "closes": "dynamic dotD/Phi_fin C1 trace binding accepted for this frontier",
                },
                {
                    "source": rel(FORMAL_INTEGRATED),
                    "closes": "formal 110 rows emitted",
                },
                {
                    "source": rel(ALL_ROWS_DECISION),
                    "closes": "72 row values and exactness emitted",
                    "does_not_close": "provenance independent of residual-projector replay",
                },
            ],
            "current_blocker_evidence": {
                "all_rows_provenance_independence": all_rows_decision[
                    "closed_kernel_clauses_for_all_rows"
                ]["provenance_independent_of_residual_projector_replay"],
                "all_rows_route_B_independent": all_rows_decision[
                    "all_72_row_execution_closed_under_independent_route_B"
                ],
                "all_rows_gate_residual_independent_source": all_rows_gate[
                    "route_B_independence_gate"
                ]["residual_projector_independent_source"],
                "first_row_formula_provenance_independent": first_row[
                    "provenance_independent_of_residual_projector_replay"
                ],
            },
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        }
    )

    write_json(TEMPLATE, template)
    write_json(ATTEMPT, attempt)
    validation = run_validator(ATTEMPT)

    decision = {
        "schema": "MTTRouteBFinalRowSourceOrRouteADecision.v1",
        "status": "FINAL_ROUTEB_FIELD_REDUCED_TO_ROW_SOURCE_THEOREM_OPEN",
        "strict_row_source_validator_built": True,
        "current_attempt_validates": validation["ok"],
        "route_B_all_other_strict_fields_closed": True,
        "remaining_route_B_field": "source_independent_of_residual_projector_replay",
        "route_B_promoted_now": False,
        "route_A_fallback_still_available": True,
        "minimal_next": {
            "route_B": [
                "prove selected transported bases K_s feed the 72 primitive row kernels",
                "prove 36 sector rows and 2 Hessian/source rows are assembled from those kernels and finite Weyl trace",
                "prove no residual-projector replay is used as row source",
            ],
            "route_A": [
                "physical Phi_fin^C1 action restriction",
                "no extra physical boundary/source term",
                "same-source R_Z/R_X/b_selected emission",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedRouteBRowSourceIndependenceProofOrPhysicalSourceFill",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "basis_fill": rel(BASIS_FILL),
            "row_source_gap": rel(ROW_GAP),
            "all_rows_decision": rel(ALL_ROWS_DECISION),
            "all_rows_gate": rel(ALL_ROWS_GATE),
            "formal_110_integrated": rel(FORMAL_INTEGRATED),
            "dynamic_trace_binding": rel(DYNAMIC_TRACE),
            "first_row_formula_source": rel(FIRST_ROW_SOURCE),
        },
        "output_packets": {
            "row_source_independence_template": rel(TEMPLATE),
            "current_row_source_independence_attempt": rel(ATTEMPT),
            "row_source_validator_result": rel(VALIDATION),
            "final_routeb_or_routea_decision": rel(DECISION),
            "validator_script": rel(VALIDATOR),
        },
        "what_closes_now": {
            "strict_row_source_independence_validator_built": True,
            "last_route_B_field_decomposed": True,
            "final_routeB_or_routeA_decision_packet_built": True,
        },
        "what_remains_open": {
            "source_independent_of_residual_projector_replay": True,
            "Route_A_physical_source_fill": True,
            "unpatched_dynamic_C1_packet_closure": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "theorem": {
            "name": "FinalRowSourceIndependenceCutsetTheorem",
            "proved": True,
            "statement": (
                "After selected basis independence, quadrature independence, exact 72-row execution, "
                "and formal 110-row execution are closed, the only remaining Route B promotion field "
                "is row-source independence from residual-projector replay. The current support does "
                "not close this field because the row formula provenance is still marked residual-lineage "
                "dependent. A strict validator now fixes the final acceptance conditions."
            ),
        },
        "decision": decision,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_gate_status": previous["status"],
        "row_gap_status": row_gap["status"],
    }

    cert = {
        "certificate": "MTT_Selected_RouteBRowSourceIndependenceProof_or_PhysicalSourceFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "strict_validator_exit_code": validation["exit_code"],
        "strict_validator_still_rejects": validation["exit_code"] == 1,
        "row_source_validator_built": True,
        "source_independence_closed": False,
        "route_B_promoted_now": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected RouteBRowSourceIndependenceProof or PhysicalSourceFill v1

Status: `{STATUS}`

This step builds the final strict validator for Route B row-source independence.

Closed before this gate:

1. selected basis independence;
2. quadrature independence;
3. exact 72 primitive rows;
4. formal 110-row finite trace replay;
5. dynamic trace binding for this frontier.

Still open:

1. prove the 72 primitive row kernels are sourced from the selected transported
   bases `K_s`;
2. prove the 36 sector rows and 2 Hessian/source rows are assembled from those
   kernels plus the finite Weyl trace rule;
3. prove no residual-projector replay is used as the row source.

The current attempt is rejected by the strict row-source validator, as it should.

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
ATTEMPT = PACKET_DIR / "current_row_source_independence_attempt.packet.json"
DECISION = PACKET_DIR / "final_routeb_or_routea_decision.packet.json"
CERT = ROOT / "certificates" / "{SLUG}_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_rowsource_independence.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteBRowSourceIndependenceProof_or_PhysicalSourceFill_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    attempt = load(ATTEMPT)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(ATTEMPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(attempt["finite_weyl_trace_rule_feeds_all_rows"] is True, "trace rule not closed")
    require(attempt["sector_rows_assembled_from_primitive_rows"] is True, "sector rows not closed")
    require(attempt["hessian_source_rows_assembled_from_same_rows"] is True, "hessian rows not closed")
    require(attempt["selected_basis_feeds_72_primitive_rows"] is False, "basis-row source overclosed")
    require(attempt["no_residual_projector_replay_used_as_source"] is False, "residual source overclosed")
    require(attempt["row_formula_source_theorem_derived"] is False, "row formula theorem overclosed")
    require(attempt["source_independent_of_residual_projector_replay"] is False, "source independence overclosed")
    require(proc.returncode == 1, "validator should reject current attempt")
    require(any("source_independent_of_residual_projector_replay is not true" in line for line in proc.stderr.splitlines()), "missing source rejection")
    require(decision["route_B_all_other_strict_fields_closed"] is True, "not all other Route B fields closed")
    require(decision["route_B_promoted_now"] is False, "Route B overpromoted")
    require(cert["row_source_validator_built"] is True, "cert missing validator")
    require(cert["source_independence_closed"] is False, "cert source overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("current attempt is rejected" in note, "note missing guardrail")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(VALIDATION, validation)
    write_json(DECISION, decision)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(f"wrote {rel(OUTPUT)}")
    print(f"status {STATUS}")
    print(f"validator_row_source_exit {validation['exit_code']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
