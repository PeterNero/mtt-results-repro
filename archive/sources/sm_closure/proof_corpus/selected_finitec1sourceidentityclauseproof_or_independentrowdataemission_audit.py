"""Audit finite C1 source-identity clause proof / independent row data emission."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finitec1sourceidentityclauseproof_or_independentrowdataemission"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CLAUSE_PROOF = PACKET_DIR / "finite_weyl_trace_assembly_clause_proof.packet.json"
UPDATED_GATE = PACKET_DIR / "updated_source_identity_clause_gate.packet.json"
ROW_DATA_ATTEMPT = PACKET_DIR / "independent_row_data_emission_attempt.packet.json"
DECISION = PACKET_DIR / "clause_proof_or_row_data_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteC1SourceIdentityClauseProof_or_IndependentRowDataEmission_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_FINITEC1SOURCEIDENTITY_CLAUSEPROOF_BUILT_TRACEASSEMBLY_CLOSED_SOURCE_OPEN"
NEXT = "MTT_Selected_PhysicalSourcePromotionClauseProof_or_NewIndependentRowPacketFill_v1"


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
    clause = load(CLAUSE_PROOF)
    gate = load(UPDATED_GATE)
    rows = load(ROW_DATA_ATTEMPT)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next mismatch")

    require(clause["status"] == "TRACE_MEASURE_AND_FORMAL_ASSEMBLY_PROVED_PHYSICAL_SOURCE_OPEN", "clause status mismatch")
    proved = clause["proved_subclaim"]
    require(proved["finite_measure_equals_normalized_trace"] is True, "trace measure not proved")
    require(proved["trace_frobenius_pairing_for_finite_quotient"] is True, "trace pairing not proved")
    require(proved["sector_rows_assembled_formally"] is True, "sector formal assembly missing")
    require(proved["hessian_source_rows_assembled_formally"] is True, "hessian formal assembly missing")
    require(proved["trace_assembly_closed"] is True, "trace assembly not closed")
    require(clause["not_proved_subclaim"]["full_source_identity_clause_proved"] is False, "full source clause overproved")

    require(gate["status"] == "THEOREM_GATE_TRACE_ASSEMBLY_SUBCLAUSE_CLOSED_SOURCE_PROMOTION_OPEN", "updated gate status mismatch")
    updated_clause = gate["clause_status"]["finite_weyl_trace_rule_assembles_sector_and_hessian_rows"]
    require(updated_clause["status"] == "SUBCLAUSE_CLOSED_PHYSICAL_SOURCE_PROMOTION_OPEN", "updated clause status mismatch")
    require(updated_clause["proved"] is False, "updated full clause overproved")
    require("same-source b_selected emission" in updated_clause["remaining_open"], "remaining b source missing")
    require(gate["proved_now"] is False, "theorem overproved")

    require(rows["status"] == "CURRENT_SUPPORT_FILLS_POSTCHECK_VALUES_NOT_NEW_INDEPENDENT_SOURCE_DATA", "rows status mismatch")
    require(rows["primitive_rows_available"] == 72, "primitive row count mismatch")
    require(rows["primitive_values_exact"] is True, "primitive exactness missing")
    require(rows["primitive_rows_source_independent"] is False, "primitive source independence overclosed")
    require(rows["new_independent_row_packet_emitted"] is False, "new rows overemitted")

    require(decision["status"] == "TRACE_ASSEMBLY_SUBCLAUSE_CLOSED_FULL_THEOREM_OPEN", "decision status mismatch")
    require(decision["clause_progress"]["finite_weyl_trace_measure_and_formal_assembly"] == "CLOSED", "subclause not closed")
    require(decision["clause_progress"]["physical_source_promotion_for_assembled_rows"] == "OPEN", "source promotion overclosed")
    require(decision["source_identity_theorem_proved"] is False, "source identity overproved")
    require(decision["new_independent_rows_emitted"] is False, "new rows decision overemitted")

    require(data["closure_claimed"] is False, "closure overclaimed")
    for key in [
        "finite_trace_measure_assembly_subclause",
        "formal_sector_and_hessian_row_assembly",
        "current_support_checked_against_new_row_schema",
        "full_clause_boundary_refined",
    ]:
        require(data["what_closes_now"][key] is True, f"missing achievement: {key}")
    require("It does not promote those rows as physical/source data" in note, "note missing guardrail")
    require("36" in note and "2" in note and "110" in note, "note missing row counts")

    for packet in [data, clause, gate, rows, decision, cert]:
        guard(packet)

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
