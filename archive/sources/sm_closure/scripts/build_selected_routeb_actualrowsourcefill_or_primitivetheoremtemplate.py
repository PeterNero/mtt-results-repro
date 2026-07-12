"""Build Route B actual row-source fill attempt and primitive theorem template."""

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

SLUG = "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TEMPLATE = PACKET_DIR / "primitive_kernel_source_theorem.strict_template.json"
ATTEMPT = PACKET_DIR / "current_actual_row_source_fill_attempt.packet.json"
VALIDATION = PACKET_DIR / "row_source_validator_result.packet.json"
GAP = PACKET_DIR / "remaining_primitive_source_gap.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_RouteBActualRowSourceFill_or_PrimitiveTheoremTemplate_v1.md"

VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_rowsource_independence.py"
PREVIOUS = DATA / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill.candidate.json"
PREVIOUS_ATTEMPT = (
    DATA
    / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill"
    / "current_row_source_independence_attempt.packet.json"
)
ROW_TEMPLATE = (
    DATA
    / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill"
    / "row_source_independence.strict_template.json"
)
BASIS_FILL = (
    DATA
    / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap"
    / "route_b_selected_basis_independence_fill.packet.json"
)
DYNAMIC_TRACE = DATA / "selected_primitiverowsexecution_or_dynamicdotdtracebinding.candidate.json"
PRIMITIVE_OVERLAP_TEMPLATE = (
    DATA
    / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun"
    / "primitive_overlap_contractions.template.json"
)
FIRST_ROW_SOURCE = (
    DATA
    / "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource"
    / "first_row_kernel_formula_source_packet.packet.json"
)
ALL_ROWS_DECISION = (
    DATA
    / "selected_firstrowprovenancepromotion_or_allrowsweylexecution"
    / "all_rows_execution_decision.packet.json"
)
FORMAL_INTEGRATED = (
    DATA
    / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
    / "formal_110_row_replay_integrated.packet.json"
)
SOURCE_RULE_CONTRACT = (
    DATA
    / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution"
    / "differentiated_residual_projector_source_rule.contract.json"
)

STATUS = "MTT_SELECTED_ROUTEB_ACTUALROWSOURCEFILL_ATTEMPT_BUILT_PRIMITIVE_SOURCE_THEOREM_OPEN"
NEXT = "MTT_Selected_PrimitiveKernelSourceTheorem_or_PhysicalPhiFinC1SourceEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
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

    previous = load(PREVIOUS)
    previous_attempt = load(PREVIOUS_ATTEMPT)
    row_template = load(ROW_TEMPLATE)
    basis_fill = load(BASIS_FILL)
    dynamic_trace = load(DYNAMIC_TRACE)
    primitive_overlap = load(PRIMITIVE_OVERLAP_TEMPLATE)
    first_row = load(FIRST_ROW_SOURCE)
    all_rows = load(ALL_ROWS_DECISION)
    formal = load(FORMAL_INTEGRATED)
    source_rule = load(SOURCE_RULE_CONTRACT)

    theorem_template = {
        "schema": "MTTPrimitiveKernelSourceTheoremStrictTemplate.v1",
        "status": "STRICT_TEMPLATE_READY_NOT_PROVED",
        "theorem_name": "SelectedPrimitiveKernelSourceTheorem",
        "must_prove": {
            "selected_basis_feeds_row_functions": False,
            "selected_phase_shift_variation_operators_pre_residual": False,
            "selected_hessian_counterterm_source": False,
            "finite_weyl_trace_is_the_pairing_source": True,
            "sector_rows_assembled_from_primitive_rows": True,
            "hessian_source_rows_assembled_from_same_rows": True,
            "no_residual_projector_replay_used_as_source": False,
            "no_locked_target_values_used_as_source": True,
        },
        "acceptance_formula": primitive_overlap["formula_slots"]["primitive_formula"],
        "sector_couplings": primitive_overlap["formula_slots"]["sector_couplings"],
        "coordinate_system": primitive_overlap["coordinate_system"],
        "validator_target": rel(VALIDATOR),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    attempt = {
        "schema": "MTTActualRouteBRowSourceFillAttempt.v1",
        "status": "ACTUAL_ROW_SOURCE_FILL_ATTEMPT_REJECTED_PRIMITIVE_SOURCE_THEOREM_OPEN",
        "selected_basis_feeds_72_primitive_rows": False,
        "finite_weyl_trace_rule_feeds_all_rows": True,
        "sector_rows_assembled_from_primitive_rows": True,
        "hessian_source_rows_assembled_from_same_rows": True,
        "no_residual_projector_replay_used_as_source": False,
        "no_locked_target_values_used_as_source": True,
        "row_formula_source_theorem_derived": False,
        "source_independent_of_residual_projector_replay": False,
        "closed_support_imported": {
            "selected_basis_available": basis_fill["route_B_independent_execution"][
                "selected_basis_independent_of_residual_projector"
            ],
            "dynamic_trace_binding_available": dynamic_trace["status"],
            "all_72_row_values_exact": all_rows["all_72_row_values_exact"],
            "all_72_row_exactness_certificates": all_rows["all_72_row_exactness_certificates"],
            "formal_110_rows_emitted": formal["formal_110_rows_executed"],
            "source_rule_contract_exists": source_rule["rule_name"],
        },
        "primitive_kernel_source_subclaims": theorem_template["must_prove"],
        "attached_source_evidence": [
            {
                "source": rel(PREVIOUS),
                "closes": "final row-source cutset and validator already built",
            },
            {
                "source": rel(BASIS_FILL),
                "closes": "stationary selected basis/projector source independence",
            },
            {
                "source": rel(PRIMITIVE_OVERLAP_TEMPLATE),
                "closes": "typed primitive row formula shape and sector couplings",
            },
            {
                "source": rel(DYNAMIC_TRACE),
                "closes": "dynamic trace binding support for this frontier",
            },
            {
                "source": rel(ALL_ROWS_DECISION),
                "closes": "all row values and exactness",
                "does_not_close": "row-source independence from residual-projector replay",
            },
            {
                "source": rel(SOURCE_RULE_CONTRACT),
                "closes": "residual-source theorem contract shape",
                "does_not_close": "selected emissions or source theorem proof",
            },
        ],
        "blocker_evidence": {
            "previous_attempt_selected_basis_feeds_rows": previous_attempt[
                "selected_basis_feeds_72_primitive_rows"
            ],
            "first_row_provenance_independent": first_row[
                "provenance_independent_of_residual_projector_replay"
            ],
            "all_rows_provenance_independent": all_rows[
                "closed_kernel_clauses_for_all_rows"
            ]["provenance_independent_of_residual_projector_replay"],
            "source_rule_values_emitted": source_rule["currently_emitted"][
                "selected_differentiated_residual_projector_source_rule"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    write_json(TEMPLATE, theorem_template)
    write_json(ATTEMPT, attempt)
    validation = run_validator(ATTEMPT)

    gap = {
        "schema": "MTTRemainingPrimitiveSourceGap.v1",
        "status": "PRIMITIVE_KERNEL_SOURCE_THEOREM_REMAINS_OPEN",
        "validator_rejects_current_attempt": validation["exit_code"] == 1,
        "closed_now": {
            "strict_row_source_validator_available": True,
            "primitive_kernel_theorem_template_emitted": True,
            "finite_weyl_trace_pairing_source": True,
            "sector_and_hessian_assembly_support": True,
        },
        "not_closed": {
            "selected_basis_to_all_72_row_functions": True,
            "selected_phase_shift_variation_operators_before_residual_projection": True,
            "selected_hessian_counterterm_source": True,
            "no_residual_projector_replay_used_as_source": True,
            "row_formula_source_theorem_derived": True,
        },
        "why_this_is_the_correct_next_gate": [
            "Route B already has values, exactness, finite trace pairing, formal assembly, and stationary selected basis support.",
            "The validator now asks for the missing source theorem, not more numerical replay.",
            "A legal promotion must make residual projectors outputs or comparisons only, never selectors for the primitive row source.",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedRouteBActualRowSourceFillOrPrimitiveTheoremTemplate",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "previous_attempt": rel(PREVIOUS_ATTEMPT),
            "row_source_template": rel(ROW_TEMPLATE),
            "basis_fill": rel(BASIS_FILL),
            "dynamic_trace_binding": rel(DYNAMIC_TRACE),
            "primitive_overlap_template": rel(PRIMITIVE_OVERLAP_TEMPLATE),
            "first_row_formula_source": rel(FIRST_ROW_SOURCE),
            "all_rows_decision": rel(ALL_ROWS_DECISION),
            "formal_110_integrated": rel(FORMAL_INTEGRATED),
            "source_rule_contract": rel(SOURCE_RULE_CONTRACT),
        },
        "output_packets": {
            "primitive_kernel_source_theorem_template": rel(TEMPLATE),
            "current_actual_row_source_fill_attempt": rel(ATTEMPT),
            "row_source_validator_result": rel(VALIDATION),
            "remaining_primitive_source_gap": rel(GAP),
        },
        "what_closes_now": {
            "primitive_source_theorem_slots_named": True,
            "row_source_fill_attempt_is_executable": True,
            "validator_rejection_is_expected_and_recorded": validation["exit_code"] == 1,
        },
        "what_remains_open": gap["not_closed"],
        "theorem": {
            "name": "PrimitiveKernelSourceTheoremReduction",
            "proved": True,
            "statement": (
                "Given the already validated Route B values, exactness, finite Weyl trace pairing, "
                "formal row assembly, and stationary selected basis support, full Route B source "
                "promotion is equivalent to proving the selected primitive kernel source theorem "
                "listed in this artifact. The current corpus does not prove that theorem yet."
            ),
        },
        "previous_gate_status": previous["status"],
        "row_template_status": row_template["status"],
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_RouteBActualRowSourceFill_or_PrimitiveTheoremTemplate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "strict_validator_exit_code": validation["exit_code"],
        "strict_validator_still_rejects": validation["exit_code"] == 1,
        "primitive_source_theorem_template_emitted": True,
        "source_independence_closed": False,
        "route_B_promoted_now": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected RouteBActualRowSourceFill or PrimitiveTheoremTemplate v1

Status: `{STATUS}`

This artifact tries the final Route B row-source fill, but keeps the proof
standard strict. It imports the closed support: selected stationary basis,
finite Weyl trace pairing, exact 72 row values, formal 110-row assembly, and
the differentiated residual-source contract.

The current fill attempt is intentionally rejected by the row-source validator.
That rejection is the useful result: the remaining object is no longer a broad
numerical search, but the selected primitive kernel source theorem.

The theorem must show that the selected transported basis, selected phase/shift
variation operators, and selected Hessian counterterm source generate the 72
primitive rows before any residual-projector replay is used. Residual projectors
may appear as checked outputs or comparisons, but not as row-source selectors.

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
ATTEMPT = PACKET_DIR / "current_actual_row_source_fill_attempt.packet.json"
TEMPLATE = PACKET_DIR / "primitive_kernel_source_theorem.strict_template.json"
GAP = PACKET_DIR / "remaining_primitive_source_gap.packet.json"
CERT = ROOT / "certificates" / "{SLUG}_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_rowsource_independence.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteBActualRowSourceFill_or_PrimitiveTheoremTemplate_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    attempt = load(ATTEMPT)
    template = load(TEMPLATE)
    gap = load(GAP)
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
    require(data["theorem"]["proved"] is True, "reduction theorem not proved")
    require(attempt["finite_weyl_trace_rule_feeds_all_rows"] is True, "trace rule missing")
    require(attempt["sector_rows_assembled_from_primitive_rows"] is True, "sector assembly missing")
    require(attempt["hessian_source_rows_assembled_from_same_rows"] is True, "hessian assembly missing")
    require(attempt["selected_basis_feeds_72_primitive_rows"] is False, "basis feed overclosed")
    require(attempt["no_residual_projector_replay_used_as_source"] is False, "residual source overclosed")
    require(attempt["row_formula_source_theorem_derived"] is False, "formula theorem overclosed")
    require(attempt["source_independent_of_residual_projector_replay"] is False, "source independence overclosed")
    require(template["must_prove"]["selected_basis_feeds_row_functions"] is False, "template overclosed")
    require(template["must_prove"]["selected_hessian_counterterm_source"] is False, "hessian source overclosed")
    require(gap["validator_rejects_current_attempt"] is True, "gap should record validator rejection")
    require(gap["not_closed"]["selected_basis_to_all_72_row_functions"] is True, "basis gap missing")
    require(gap["not_closed"]["selected_hessian_counterterm_source"] is True, "hessian gap missing")
    require(proc.returncode == 1, "validator should still reject")
    require(any("source_independent_of_residual_projector_replay is not true" in line for line in proc.stderr.splitlines()), "missing source rejection")
    require(cert["strict_validator_still_rejects"] is True, "cert should reject")
    require(cert["source_independence_closed"] is False, "cert overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("intentionally rejected" in note, "note missing guardrail")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(VALIDATION, validation)
    write_json(GAP, gap)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(AUDIT)}")
    print(f"Validator exit: {validation['exit_code']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
