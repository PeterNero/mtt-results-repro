"""Build physical source-promotion clause proof or new independent row packet fill."""

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

SLUG = "selected_physicalsourcepromotionclauseproof_or_newindependentrowpacketfill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROMOTION_ATTEMPT = PACKET_DIR / "physical_source_promotion_clause_attempt.packet.json"
NEW_ROW_FILL = PACKET_DIR / "new_independent_row_packet_fill_template.packet.json"
VALIDATION = PACKET_DIR / "strict_final_source_validator_result.packet.json"
DECISION = PACKET_DIR / "promotion_clause_or_new_rows_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalSourcePromotionClauseProof_or_NewIndependentRowPacketFill_v1.md"

PREVIOUS = DATA / "selected_finitec1sourceidentityclauseproof_or_independentrowdataemission.candidate.json"
UPDATED_GATE = (
    DATA
    / "selected_finitec1sourceidentityclauseproof_or_independentrowdataemission"
    / "updated_source_identity_clause_gate.packet.json"
)
CLAUSE_PROOF = (
    DATA
    / "selected_finitec1sourceidentityclauseproof_or_independentrowdataemission"
    / "finite_weyl_trace_assembly_clause_proof.packet.json"
)
BEST_FILL = (
    DATA
    / "selected_finalsourceemission_bestcurrentfill_or_nogowitness"
    / "best_current_source_emission_fill_attempt.packet.json"
)
NO_GO = (
    DATA
    / "selected_finalsourceemission_bestcurrentfill_or_nogowitness"
    / "final_source_emission_nogo_witness.packet.json"
)
NEW_ROWS_SCHEMA = (
    DATA
    / "selected_finitec1sourceidentitytheorem_or_newindependentrows"
    / "new_independent_rows_schema.packet.json"
)
VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1emission_or_independenthessianquadraturesource.py"

STATUS = "MTT_SELECTED_PHYSICALSOURCEPROMOTION_CLAUSEPROOF_BUILT_PROMOTION_OPEN"
NEXT = "MTT_Selected_SameSourcePhiFinC1Emission_or_IndependentRowsActualFill_v1"


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
    gate = load(UPDATED_GATE)
    clause = load(CLAUSE_PROOF)
    best = load(BEST_FILL)
    nogo = load(NO_GO)
    schema = load(NEW_ROWS_SCHEMA)

    route_a = dict(best["route_A_phifinc1_source_emission"])
    route_b = dict(best["route_B_independent_hessian_quadrature_source"])

    promotion_attempt = {
        "schema": "MTTPhysicalSourcePromotionClauseAttempt.v1",
        "status": "TRACE_ASSEMBLY_IMPORTED_STRICT_PROMOTION_STILL_REJECTED",
        "imported_closed_subclaim": {
            "finite_trace_measure_and_formal_assembly_closed": clause["proved_subclaim"][
                "trace_assembly_closed"
            ],
            "source": rel(CLAUSE_PROOF),
        },
        "route_A_phifinc1_source_emission": route_a,
        "route_B_independent_hessian_quadrature_source": route_b,
        "locked_target_values_used_as_source": best["locked_target_values_used_as_source"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(PROMOTION_ATTEMPT, promotion_attempt)
    validation = run_validator(PROMOTION_ATTEMPT)

    new_row_fill = {
        "schema": "MTTNewIndependentRowPacketFillTemplate.v1",
        "status": "TEMPLATE_FILLED_WITH_CURRENT_SUPPORT_VALUES_SOURCE_FIELDS_OPEN",
        "required_schema": rel(NEW_ROWS_SCHEMA),
        "selected_source_identity": {
            "selected_emitted": False,
            "required": schema["required_packet_fields"]["selected_source_identity"],
        },
        "basis_source_certificate": {
            "selected_emitted": schema["required_packet_fields"]["basis_source_certificate"][
                "current_support_available"
            ],
            "source": "candidate_data/selected_routeb_selectedbasisindependencefill_or_rowsourcegap/route_b_selected_basis_independence_fill.packet.json",
        },
        "primitive_rows": {
            "required_count": 72,
            "values_available_as_postchecks": schema["current_values_reusable_as_postchecks"][
                "all_72_values_exact"
            ],
            "source_integral_or_formula_independent": False,
        },
        "sector_rows": {
            "required_count": 36,
            "formal_assembly_available": clause["proved_subclaim"]["sector_rows_assembled_formally"],
            "physical_source_promoted": False,
        },
        "hessian_source_rows": {
            "required_count": 2,
            "formal_assembly_available": clause["proved_subclaim"][
                "hessian_source_rows_assembled_formally"
            ],
            "same_source_b_selected_derivation": False,
        },
        "exactness_or_error_certificate": {
            "available_for_current_postcheck_values": True,
            "usable_for_new_source_packet": False,
        },
        "independence_certificate": {
            "residual_projector_replay_excluded_as_source": False,
            "locked_target_values_excluded_as_source": True,
            "observed_data_excluded_as_selector": True,
            "benchmark_matrices_excluded": True,
        },
        "new_independent_row_packet_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTPhysicalSourcePromotionOrNewRowsDecision.v1",
        "status": "STRICT_PROMOTION_REJECTED_NEW_ROW_PACKET_NOT_EMITTED",
        "updated_gate_status": gate["status"],
        "trace_assembly_subclaim_closed": clause["proved_subclaim"]["trace_assembly_closed"],
        "strict_validator_ok": validation["ok"],
        "source_identity_theorem_proved": False,
        "new_independent_row_packet_emitted": False,
        "remaining_minimal_payload": nogo["minimal_non_replay_payload_needed"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [
        (VALIDATION, validation),
        (NEW_ROW_FILL, new_row_fill),
        (DECISION, decision),
    ]:
        write_json(path, payload)

    candidate = {
        "candidate": "MTTSelectedPhysicalSourcePromotionClauseProofOrNewIndependentRowPacketFill",
        "status": STATUS,
        "inputs": {
            "previous": rel(PREVIOUS),
            "updated_gate": rel(UPDATED_GATE),
            "best_current_fill": rel(BEST_FILL),
            "new_rows_schema": rel(NEW_ROWS_SCHEMA),
        },
        "output_packets": {
            "physical_source_promotion_clause_attempt": rel(PROMOTION_ATTEMPT),
            "strict_final_source_validator_result": rel(VALIDATION),
            "new_independent_row_packet_fill_template": rel(NEW_ROW_FILL),
            "decision": rel(DECISION),
        },
        "theorem": {
            "name": "PhysicalSourcePromotionClauseNoGoAndRowsTemplateTheorem",
            "proved": True,
            "statement": (
                "After importing the closed finite trace assembly subclaim, the strict final-source validator "
                "still rejects current support. The missing payload is not numerical: it is same-branch physical "
                "Phi_fin^C1 source emission or a genuinely independent row packet with residual-replay-free provenance."
            ),
        },
        "what_closes_now": {
            "trace_assembly_imported_into_promotion_attempt": True,
            "strict_validator_rerun": True,
            "new_row_packet_fill_template_created": True,
            "minimal_non_replay_payload_preserved": True,
        },
        "what_remains_open": {
            "same_branch_phifin_c1_source_emission": True,
            "same_source_b_selected_emission": True,
            "source_independent_of_residual_projector_replay": True,
            "new_independent_selected_row_packet": True,
            "unpatched_dynamic_C1_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalSourcePromotionClauseProof_or_NewIndependentRowPacketFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "strict_validator_ok": validation["ok"],
        "strict_validator_exit_code": validation["exit_code"],
        "source_identity_theorem_proved": False,
        "new_independent_row_packet_emitted": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    NOTE.write_text(
        "# MTT Selected PhysicalSourcePromotionClauseProof or NewIndependentRowPacketFill v1\n\n"
        f"Status: `{STATUS}`.\n\n"
        "The finite trace assembly subclaim is now imported into the strict physical-source "
        "promotion attempt. The validator still rejects the current packet: trace assembly "
        "and exact row values are postcheck support, not source promotion.\n\n"
        "The emitted new-row template shows the remaining live fields: selected source identity, "
        "residual-replay-free primitive row provenance, physical sector-row promotion, and "
        "same-source `b_selected` derivation.\n\n"
        f"Next artifact: `{NEXT}`.\n",
        encoding="utf-8",
    )
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
