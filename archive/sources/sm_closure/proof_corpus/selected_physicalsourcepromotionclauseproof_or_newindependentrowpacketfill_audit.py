"""Audit physical source-promotion clause proof / new independent row packet fill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalsourcepromotionclauseproof_or_newindependentrowpacketfill"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROMOTION_ATTEMPT = PACKET_DIR / "physical_source_promotion_clause_attempt.packet.json"
NEW_ROW_FILL = PACKET_DIR / "new_independent_row_packet_fill_template.packet.json"
VALIDATION = PACKET_DIR / "strict_final_source_validator_result.packet.json"
DECISION = PACKET_DIR / "promotion_clause_or_new_rows_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalSourcePromotionClauseProof_or_NewIndependentRowPacketFill_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PHYSICALSOURCEPROMOTION_CLAUSEPROOF_BUILT_PROMOTION_OPEN"
NEXT = "MTT_Selected_SameSourcePhiFinC1Emission_or_IndependentRowsActualFill_v1"


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
    attempt = load(PROMOTION_ATTEMPT)
    rows = load(NEW_ROW_FILL)
    validation = load(VALIDATION)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "status mismatch")
    require(cert["status"] == STATUS, "cert status mismatch")
    require(data["next_required_artifact"] == NEXT, "next mismatch")
    require(attempt["imported_closed_subclaim"]["finite_trace_measure_and_formal_assembly_closed"] is True, "trace subclaim missing")
    require(validation["ok"] is False and validation["exit_code"] == 1, "validator should reject")
    require(any("neither narrowed Route A nor narrowed Route B validates" in line for line in validation["stderr"]), "missing strict rejection")
    require(rows["new_independent_row_packet_emitted"] is False, "new rows overemitted")
    require(rows["primitive_rows"]["values_available_as_postchecks"] is True, "postcheck rows unavailable")
    require(rows["primitive_rows"]["source_integral_or_formula_independent"] is False, "primitive provenance overclosed")
    require(rows["hessian_source_rows"]["same_source_b_selected_derivation"] is False, "b source overclosed")
    require(rows["independence_certificate"]["residual_projector_replay_excluded_as_source"] is False, "residual replay overexcluded")
    require(decision["strict_validator_ok"] is False, "decision overaccepted")
    require(decision["source_identity_theorem_proved"] is False, "theorem overproved")
    require(decision["new_independent_row_packet_emitted"] is False, "decision rows overemitted")
    require(decision["next_required_artifact"] == NEXT, "decision next mismatch")
    require(data["closure_claimed"] is False, "closure overclaimed")
    for key in [
        "trace_assembly_imported_into_promotion_attempt",
        "strict_validator_rerun",
        "new_row_packet_fill_template_created",
        "minimal_non_replay_payload_preserved",
    ]:
        require(data["what_closes_now"][key] is True, f"missing achievement: {key}")
    require("validator still rejects" in note, "note missing rejection")
    require("same-source `b_selected`" in note, "note missing b_selected gap")

    for packet in [data, attempt, rows, decision, cert]:
        guard(packet)

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
