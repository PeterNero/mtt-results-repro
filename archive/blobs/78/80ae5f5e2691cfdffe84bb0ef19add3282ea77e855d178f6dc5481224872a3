"""Audit decisive dynamic-C1 source-leaf attack."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_decisive_dynamicc1_sourceleaf_attack_or_sourceowner_theorem"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_sixfield_phifinc1_source_attack.packet.json"
ROUTE_B = PACKET_DIR / "route_b_independent_row_export_attack.packet.json"
QASU3 = PACKET_DIR / "qasu3_bn27_source_support_attack.packet.json"
OWNER = PACKET_DIR / "minimal_dynamic_c1_source_owner_theorem.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DecisiveDynamicC1_SourceLeafAttack_or_SourceOwnerTheorem_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_DECISIVE_DYNAMICC1_SOURCELEAF_ATTACK_BUILT_SOURCE_OWNER_OPEN"
NEXT = "MTT_Selected_DynamicC1_SourceOwnerTheorem_or_IndependentConnectionTables_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    qasu3 = load(QASU3)
    owner = load(OWNER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_decision"]["SM_parity_closed"] is True, "SM parity should remain closed")
    require(data["closure_decision"]["route_A_closed_now"] is False, "Route A overclosed")
    require(data["closure_decision"]["route_B_closed_now"] is False, "Route B overclosed")
    require(data["closure_decision"]["qasu3_source_route_closed_now"] is False, "Qa/SU3 route overclosed")
    require(data["closure_decision"]["any_route_closes_now"] is False, "route closure overclaimed")
    require(data["closure_decision"]["dynamic_C1_source_owner_theorem_supplied"] is False, "source owner overclaimed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(data["closure_decision"]["no_knob_closed"] is False, "no-knob overclosed")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(route_a["passes_strict_source_validator"] is False, "Route A validator should fail")
    require(route_a["required_fields"]["physical_trace_frobenius_measure"] is True, "measure clause should be closed")
    for key in [
        "physical_first_variation",
        "phase_R_Z_source",
        "shift_R_X_source",
        "same_source_b_selected",
        "no_extra_boundary_or_source",
    ]:
        require(route_a["required_fields"][key] is False, f"Route A field overclosed: {key}")

    require(route_b["passes_strict_source_validator"] is False, "Route B validator should fail")
    require(route_b["required_fields"]["stationary_basis_rows_selected"] is True, "stationary basis not imported")
    require(route_b["required_fields"]["primitive_row_ids_locked"] is True, "primitive row ids not locked")
    require(route_b["required_fields"]["formal_110_rows_executed"] is True, "formal rows not executed")
    require(route_b["required_fields"]["dynamic_dotd_trace_binding_selected"] is True, "dynamic trace import not recorded")
    require(route_b["required_fields"]["residual_projector_independent_source"] is False, "residual independence overclosed")
    require(route_b["required_fields"]["selected_row_kernel_source"] is False, "row kernel source overclosed")

    require(qasu3["passes_strict_source_validator"] is False, "Qa/SU3 route should fail")
    require(qasu3["required_fields"]["nonidentity_rho_E_interface_built"] is True, "nonidentity rhoE interface missing")
    require(qasu3["required_fields"]["quotient_valid_B_N_required"] is True, "quotient-valid BN requirement missing")
    require(qasu3["required_fields"]["selected_values_all_open"] is True, "Qa/SU3 selected values not open")
    require(qasu3["required_fields"]["selected_correction_source_closed"] is False, "correction source overclosed")
    require(qasu3["required_fields"]["selected_full_response_emission_closed"] is False, "full response overclosed")
    require(qasu3["required_fields"]["actual_operator_payload_promoted"] is False, "actual payload overpromoted")

    require(owner["status"] == "MINIMAL_SOURCE_OWNER_THEOREM_REQUIRED", "owner theorem status mismatch")
    require(owner["currently_supplied"] is False, "owner theorem overclaimed")
    require(len(owner["minimal_fields"]) == 7, "owner theorem field count changed")
    require("Route A physical Phi_fin^C1 action/source theorem" in owner["legal_exports"], "Route A export missing")
    require("Route B independent selected Galerkin row-kernel theorem" in owner["legal_exports"], "Route B export missing")
    require(
        "Qa/SU3 nonidentity rho_E plus quotient-valid B_N selected connection table export" in owner["legal_exports"],
        "Qa/SU3 export missing",
    )

    require(data["what_closes_now"]["decisive_three_route_attack_executed"] is True, "three-route attack not executed")
    require(data["what_closes_now"]["cross_repo_basis_and_row_progress_imported"] is True, "cross-repo progress not imported")
    require(data["what_closes_now"]["qasu3_nonidentity_bn_contract_imported"] is True, "Qa/SU3 contract not imported")
    require(data["what_closes_now"]["minimal_source_owner_theorem_emitted"] is True, "owner theorem not emitted")
    require(data["superset_strategy"]["paths_used_as_knobs"] is False, "superset used as knobs")
    require("No route closes with the current packets." in note, "note missing failed route result")

    for packet in [data, route_a, route_b, qasu3, owner, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
