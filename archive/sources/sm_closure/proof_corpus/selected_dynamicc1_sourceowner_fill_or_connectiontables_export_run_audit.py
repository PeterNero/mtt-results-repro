"""Audit DynamicC1 source-owner fill/export run after back-import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_dynamicc1_sourceowner_fill_or_connectiontables_export_run"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FIELD_MATRIX = PACKET_DIR / "source_owner_field_matrix_after_backimport.packet.json"
CONNECTION_STATUS = PACKET_DIR / "independent_connection_export_status_after_backimport.packet.json"
FIX_DECISION = PACKET_DIR / "dynamic_c1_sourceowner_fix_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicC1_SourceOwnerTheorem_Fill_or_ConnectionTablesExport_Run_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_DYNAMICC1_SOURCEOWNER_FILLRUN_STATIC_FIELDS_IMPORTED_DYNAMIC_VALUES_OPEN"
NEXT = "MTT_Selected_DynamicC1_SourceOwner_DynamicTransferHessian_or_HonestGalerkinValues_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    fields = load(FIELD_MATRIX)
    connection = load(CONNECTION_STATUS)
    decision = load(FIX_DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(data["theorem"]["proved"] is True, "backimport theorem not recorded")

    require(fields["closed_field_count"] == 3, "closed field count mismatch")
    require(fields["open_field_count"] == 4, "open field count mismatch")
    results = fields["field_results"]
    for key in ["source_owner_id", "admissible_c1_variation_space", "independence_guard"]:
        field = results[key]
        require(field["closed_for_source_owner_template"] is True, f"{key} should close")
        require(field["selected_emitted"] is True, f"{key} selected flag missing")
        require(field["same_branch"] is True, f"{key} same-branch flag missing")
        require(field["theorem_derived"] is True, f"{key} theorem flag missing")
        require(field["source_owner_verified"] is True, f"{key} owner flag missing")
    for key in ["phase_R_Z_source", "shift_R_X_source", "b_selected_source", "sector_row_assembly"]:
        field = results[key]
        require(field["closed_for_source_owner_template"] is False, f"{key} overclosed")
        require(field["selected_emitted"] is False, f"{key} selected too early")
        require(field["same_branch"] is False, f"{key} same-branch overclaimed")
        require(field["theorem_derived"] is False, f"{key} theorem-derived overclaimed")
        require(field["source_owner_verified"] is False, f"{key} owner verified too early")

    require(connection["present_count"] == 5, "connection present count mismatch")
    require(connection["missing_count"] == 3, "connection missing count mismatch")
    families = connection["required_table_families"]
    for key in [
        "selected_connection_or_transition_data",
        "rho_E_or_nonidentity_projective_transition",
        "quotient_valid_B_N_or_BN27_carrier",
        "D_E_Riesz_Green_dotD_payload",
        "source_independence_certificate",
    ]:
        require(families[key]["present"] is True, f"{key} should be present")
    for key in ["primitive_C1_row_kernel_tables", "hessian_bselected_tables", "sector_response_tables"]:
        require(families[key]["present"] is False, f"{key} overexported")

    closure = decision["closure_decision"]
    require(closure["source_owner_id_closed"] is True, "source owner id not closed")
    require(closure["admissible_c1_variation_space_closed"] is True, "variation target not closed")
    require(closure["independence_guard_closed"] is True, "independence guard not closed")
    require(closure["phase_R_Z_source_closed"] is False, "R_Z overclosed")
    require(closure["shift_R_X_source_closed"] is False, "R_X overclosed")
    require(closure["b_selected_source_closed"] is False, "b overclosed")
    require(closure["sector_row_assembly_closed"] is False, "sector rows overclosed")
    require(closure["dynamic_C1_source_owner_closed"] is False, "dynamic source owner overclosed")
    require(closure["true_SM_equivalence_closed"] is False, "true SM equivalence overclosed")
    require(closure["no_knob_closed"] is False, "no-knob overclosed")

    exact = decision["exact_conditional_values_retained"]
    require(exact["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A mismatch")
    require(exact["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(exact["b_norm_sq"] == 24.0, "b norm mismatch")
    require(exact["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")
    require(exact["linear_algebra_obstruction_removed"] is True, "linear algebra not imported")

    require(data["what_closes_now"]["old_template_backimport_fixed"] is True, "backimport fix missing")
    require(data["what_closes_now"]["static_sector_routing_imported"] is True, "static routing not imported")
    require(data["what_closes_now"]["alpha1_dotd_imported"] is True, "alpha1/dotD not imported")
    require(data["what_closes_now"]["dynamic_value_blocker_is_precisely_identified"] is True, "blocker not sharp")
    require(data["not_used_as_closure"]["conditional_values"] is True, "conditional values used as closure")
    require(data["not_used_as_closure"]["source_map_candidate"] is True, "source map candidate used as closure")
    require(data["not_used_as_closure"]["primitive_candidate"] is True, "primitive candidate used as closure")
    require(data["closure_claimed"] is False, "closure claimed")

    require("not a closure claim" in note, "note missing closure guardrail")
    require("dynamic C1 value emission" in note, "note missing dynamic blocker")

    for packet in [data, fields, connection, decision, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
