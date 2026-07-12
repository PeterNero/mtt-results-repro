"""Audit finite C1 source-identity theorem gate or new independent rows schema."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finitec1sourceidentitytheorem_or_newindependentrows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
THEOREM_GATE = PACKET_DIR / "selected_finite_c1_source_identity_theorem_gate.packet.json"
ANCESTOR_RECONCILIATION = PACKET_DIR / "ancestor_lemma_reconciliation.packet.json"
NEW_ROWS_SCHEMA = PACKET_DIR / "new_independent_rows_schema.packet.json"
DECISION = PACKET_DIR / "source_identity_or_new_rows_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteC1SourceIdentityTheorem_or_NewIndependentRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_FINITEC1SOURCEIDENTITYTHEOREM_OR_NEWINDEPENDENTROWS_BUILT_THEOREM_OPEN"
NEXT = "MTT_Selected_FiniteC1SourceIdentityClauseProof_or_IndependentRowDataEmission_v1"


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
    gate = load(THEOREM_GATE)
    ancestor = load(ANCESTOR_RECONCILIATION)
    rows = load(NEW_ROWS_SCHEMA)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next mismatch")

    require(gate["status"] == "THEOREM_GATE_BUILT_CLAUSES_OPEN", "gate status mismatch")
    require(gate["theorem_name"] == "SelectedFiniteC1SourceIdentityTheorem", "theorem name mismatch")
    require(gate["proved_now"] is False, "gate overproved")
    require(len(gate["clause_status"]) == 6, "clause count mismatch")
    require(gate["clause_status"]["finite_weyl_trace_rule_assembles_sector_and_hessian_rows"]["status"] == "PARTIAL", "expected partial finite trace clause")
    require(gate["clause_status"]["no_residual_projector_replay_as_source_provenance"]["proved"] is False, "residual provenance overproved")
    require(gate["current_route_A_accepts"] is False, "route A overaccepted")
    require(gate["current_route_B_accepts"] is False, "route B overaccepted")

    require(ancestor["status"] == "SOURCE_IDENTITY_STRICTLY_STRENGTHENS_PRIOR_MINIMAL_LEMMA", "ancestor status mismatch")
    require(ancestor["relation"]["new_theorem_implies_prior_route_B_lemma"] is True, "implication missing")
    require(ancestor["relation"]["prior_route_B_lemma_does_not_imply_route_A_physical_action_clauses"] is True, "strictness missing")
    require(ancestor["countermodel_summary"]["full_minimal_lemma_proved"] is False, "countermodel mismatch")

    require(rows["status"] == "NEW_INDEPENDENT_ROWS_SCHEMA_BUILT_VALUES_NOT_EMITTED", "rows status mismatch")
    require(rows["required_packet_fields"]["primitive_rows"]["required_count"] == 72, "primitive count mismatch")
    require(rows["required_packet_fields"]["sector_rows"]["required_count"] == 36, "sector count mismatch")
    require(rows["required_packet_fields"]["hessian_source_rows"]["required_count"] == 2, "hessian count mismatch")
    require(rows["current_values_reusable_as_postchecks"]["all_72_values_exact"] is True, "postcheck rows missing")
    require(rows["current_values_reusable_as_postchecks"]["all_72_source_independence"] is False, "source independence overclosed")
    require(rows["emitted_now"] is False, "new rows overemitted")

    require(decision["status"] == "THEOREM_NOT_PROVED_NEW_ROWS_NOT_EMITTED_NEXT_CLAUSE_PROOF", "decision status mismatch")
    require(decision["source_identity_theorem_proved"] is False, "decision theorem overproved")
    require(decision["new_independent_rows_emitted"] is False, "decision rows overemitted")
    require(decision["unpatched_dynamic_C1_closed"] is False, "unpatched overclosed")
    require(decision["next_required_artifact"] == NEXT, "decision next mismatch")

    require(data["closure_claimed"] is False, "closure overclaimed")
    for key in [
        "source_identity_clause_gate_built",
        "prior_minimal_lemma_reconciled",
        "new_independent_rows_schema_built",
        "next_clause_proof_target_selected",
    ]:
        require(data["what_closes_now"][key] is True, f"missing achievement: {key}")
    require("stronger than the older Route-B" in note, "note missing strictness")
    require("independence certificate excluding residual-projector replay" in note, "note missing rows guard")

    for packet in [data, gate, ancestor, rows, decision, cert]:
        guard(packet)

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
