"""Audit DynamicC1 source-owner theorem object."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_dynamicc1_sourceowner_theorem_or_independentconnectiontables"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STRICT_TEMPLATE = PACKET_DIR / "dynamic_c1_source_owner_theorem.strict_template.json"
CURRENT_ATTEMPT = PACKET_DIR / "current_source_owner_fill_attempt.packet.json"
CONNECTION_SCHEMA = PACKET_DIR / "independent_connection_tables_export_schema.packet.json"
IMPLICATION = PACKET_DIR / "source_owner_promotion_implication.packet.json"
PAPER_TEXT = PACKET_DIR / "paper_ready_theorem_text.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicC1_SourceOwnerTheorem_or_IndependentConnectionTables_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_DYNAMICC1_SOURCEOWNER_THEOREM_BUILT_TEMPLATE_OPEN"
NEXT = "MTT_Selected_DynamicC1_SourceOwnerTheorem_Fill_or_ConnectionTablesExport_Run_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    strict = load(STRICT_TEMPLATE)
    current = load(CURRENT_ATTEMPT)
    connection = load(CONNECTION_SCHEMA)
    implication = load(IMPLICATION)
    paper = load(PAPER_TEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(data["closure_decision"]["SM_parity_closed"] is True, "SM parity should remain closed")
    require(data["closure_decision"]["strict_source_owner_template_built"] is True, "strict template not built")
    require(data["closure_decision"]["independent_connection_export_schema_built"] is True, "connection schema not built")
    require(data["closure_decision"]["current_fill_attempt_passes"] is False, "current fill overaccepted")
    require(data["closure_decision"]["dynamic_C1_source_owner_theorem_proved_as_hypothesis"] is False, "hypothesis overproved")
    require(data["closure_decision"]["unpatched_dynamic_C1_packet_closed"] is False, "dynamic C1 overclosed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(data["closure_decision"]["no_knob_closed"] is False, "no-knob overclosed")

    required_fields = strict["required_fields"]
    require(len(required_fields) == 7, "strict field count changed")
    for key, field in required_fields.items():
        require(field["selected_emitted"] is False, f"{key} selected too early")
        require(field["same_branch"] is False, f"{key} same-branch overclaimed")
        require(field["theorem_derived"] is False, f"{key} theorem-derived overclaimed")
        require(field["source_owner_verified"] is False, f"{key} owner verified too early")
        require(field["forbidden_provenance_excluded"] is True, f"{key} missing provenance guard")
    require(len(strict["accepted_exports"]) == 3, "accepted export count changed")
    require("residual-projector replay used as source" in strict["forbidden_provenance"], "residual shortcut not forbidden")

    require(current["status"] == "CURRENT_FILL_REJECTED_SOURCE_OWNER_OPEN", "current attempt status mismatch")
    require(current["route_A_import"]["measure_clause_closed"] is True, "Route A measure import missing")
    require(current["route_A_import"]["passes"] is False, "Route A current attempt passed unexpectedly")
    require(current["route_B_import"]["stationary_basis_rows_selected"] is True, "Route B basis import missing")
    require(current["route_B_import"]["primitive_row_ids_locked"] is True, "Route B row ids missing")
    require(current["route_B_import"]["formal_110_rows_executed"] is True, "Route B formal rows missing")
    require(current["route_B_import"]["passes"] is False, "Route B current attempt passed unexpectedly")
    require(current["qasu3_import"]["nonidentity_rho_E_interface_built"] is True, "Qa/SU3 rhoE import missing")
    require(current["qasu3_import"]["quotient_valid_B_N_required"] is True, "Qa/SU3 BN import missing")
    require(current["qasu3_import"]["passes"] is False, "Qa/SU3 current attempt passed unexpectedly")
    require(all(value is False for value in current["strict_template_field_results"].values()), "strict fields should be unfilled")

    table_families = connection["required_table_families"]
    require(len(table_families) == 8, "connection table family count changed")
    require(connection["if_all_present_then_fills_source_owner_template"] is True, "connection implication missing")
    for key, family in table_families.items():
        require(family["present"] is False, f"connection table overfilled: {key}")

    require(implication["status"] == "CONDITIONAL_PROMOTION_IMPLICATION_PROVED", "implication status mismatch")
    require(implication["consequences"]["selected_A_selected_promotes"] is True, "A implication missing")
    require(implication["consequences"]["selected_b_selected_promotes"] is True, "b implication missing")
    require(implication["consequences"]["selected_deltaTheta_C1_promotes"] is True, "delta implication missing")
    require(implication["consequences"]["unpatched_dynamic_C1_packet_closes"] is True, "closure implication missing")
    require(implication["uses_formal_values"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A mismatch")
    require(implication["uses_formal_values"]["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(implication["uses_formal_values"]["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")

    require(paper["theorem_title"] == "Selected Dynamic C1 Source-Owner Theorem", "paper theorem title mismatch")
    require(len(paper["proof_skeleton"]) == 6, "proof skeleton count changed")
    require("template ready" in paper["current_status"], "paper status missing open marker")
    require("not a closure claim" in note, "note missing non-closure guardrail")

    require(data["what_closes_now"]["DynamicC1SourceOwnerTheorem_created_as_strict_object"] is True, "object not created")
    require(data["what_closes_now"]["conditional_promotion_implication_proved"] is True, "conditional implication not proved")
    require(data["what_remains_open"]["or_export_independent_connection_tables"] is True, "connection export not open")
    require(data["superset_strategy"]["paths_used_as_knobs"] is False, "superset used as knobs")

    for packet in [data, strict, current, connection, implication, paper, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
