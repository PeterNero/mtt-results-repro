from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutraloverlapkernelphysicalunitoractioncompleteness"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
PACKET = ROOT / "candidate_data" / SLUG / "neutral_overlap_physical_action_gate.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralOverlapKernelPhysicalUnitOrActionCompleteness_v1.md"

STATUS = "MTT_SELECTED_NEUTRALOVERLAP_PHYSICALUNIT_ACTIONCOMPLETENESS_GATE_EXECUTED_VALUES_OPEN"
NEXT = "MTT_Selected_NeutralOverlapKernelValueSourceOrPhysicalUnitTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    packet = load(PACKET)
    candidate = load(CANDIDATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == STATUS, "packet status changed")
    require(cert["status"] == STATUS, "certificate status changed")
    require(packet["next_required_artifact"] == NEXT, "packet next changed")
    require(cert["next_required_artifact"] == NEXT, "cert next changed")
    require(packet["observed_data_used_as_selector"] is False, "observed selector used")
    require(packet["target_fitting_used"] is False, "target fitting used")
    require(cert["observed_data_used_as_selector"] is False, "cert observed selector used")
    require(cert["target_fitting_used"] is False, "cert target fitting used")

    closes = packet["what_closes_here"]
    for key in [
        "three_exit_gate_executed",
        "overlap_schema_imported_but_not_promoted",
        "physical_unit_bridge_imported_as_conditional_only",
        "action_completeness_not_derived",
        "exact_next_value_source_contract_named",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    corpus = packet["corpus_diagnostics"]
    for key, value in corpus.items():
        require(value is True, f"corpus diagnostic missing: {key}")

    ok = packet["neutral_overlap_OK_gate_acceptance"]
    require(packet["neutral_overlap_OK_gates_total"] == 9, "OK gate total changed")
    require(packet["neutral_overlap_OK_gates_closed"] == 3, "OK gate closed count changed")
    for key in [
        "OK1_selected_geometry_and_charge_sector",
        "OK2_SM_representation_spaces",
        "OK9_no_measured_selector",
    ]:
        require(ok[key] is True, f"closed OK gate lost: {key}")
    for key in [
        "OK3_normalized_zero_mode_bases",
        "OK4_kinetic_metrics_positive",
        "OK5_finite_neutral_overlap_channel_sets",
        "OK6_action_costs_prefactors_characters_retarded_signs",
        "OK7_nil_coherence_anchor_projectors",
        "OK8_RG_threshold_matching_map",
    ]:
        require(ok[key] is False, f"OK value gate overclosed: {key}")

    routes = packet["route_exit_screen"]
    require(set(routes) == {
        "A_dirac_dimensionful_MD",
        "B_majorana_or_seesaw_blocks",
        "C_nil_boundary_effective_spectrum",
    }, "route set changed")
    require(packet["route_exit_count"] == 3, "route count changed")
    require(packet["accepted_route_exit_count"] == 0, "route overaccepted")
    require(cert["accepted_route_exit_count"] == 0, "cert route overaccepted")
    for route_id, row in routes.items():
        require(row["accepted"] is False, f"route accepted: {route_id}")
        require(row["failed_gates"], f"failed gates empty: {route_id}")
        require(row["can_be_reopened_by"], f"reopen contract empty: {route_id}")

    require(packet["physical_unit_status"] == "CONDITIONAL_MAP_CLOSED_PHYSICAL_UNIT_COEFFICIENT_OPEN", "physical unit status changed")
    require(packet["physical_unit_selected"] is False, "physical unit overselected")
    require(packet["Dirac_only_completeness_closed"] is False, "Dirac action completeness overclosed")
    require(packet["separate_Majorana_operator_excluded"] is False, "Majorana operator overexcluded")
    require(packet["new_value_fields_closed_here"] == 0, "value fields overclosed")
    require(packet["required_fields_closed"] == 4, "required field count changed")
    require(packet["required_fields_total"] == 8, "required field total changed")
    require(packet["selected_neutral_operator_accepted"] is False, "neutral operator overaccepted")
    require(packet["U5_closed"] is False, "U5 overclosed")

    for field in [
        "dimensionful_M_D_3x3",
        "dimensionful_M_L_3x3",
        "dimensionful_M_R_3x3",
        "absolute_normalization_and_scheme",
    ]:
        require(packet["required_field_acceptance"][field] is False, f"value field overclosed: {field}")
        require(cert[f"{field}_closed"] is False, f"cert value field overclosed: {field}")

    contract = packet["next_value_source_contract"]
    require(len(contract["must_emit"]) == 5, "next contract changed")
    require("at least one accepted lawful exit" in contract["minimum_success"], "minimum success guard missing")

    for phrase in [
        "neutral operator at `4/8`",
        "schema/support source",
        "`omega_gap_phys` is not",
        "Dirac-only action",
        "all three lawful exits remain unaccepted",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(json.dumps({
        "neutral_OK_gates": f"{packet['neutral_overlap_OK_gates_closed']}/{packet['neutral_overlap_OK_gates_total']}",
        "accepted_routes": packet["accepted_route_exit_count"],
        "new_value_fields_closed": packet["new_value_fields_closed_here"],
        "next": NEXT,
    }, indent=2))
    print("selected neutral overlap/physical-unit/action-completeness audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
