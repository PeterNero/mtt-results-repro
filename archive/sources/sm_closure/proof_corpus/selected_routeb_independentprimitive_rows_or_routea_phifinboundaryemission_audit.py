"""Audit reduced primitive-row execution preconditions after alpha1/dotD retirement."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_routeb_independentprimitive_rows_or_routea_phifinboundaryemission"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PRECONDITIONS = PACKET_DIR / "primitive_row_precondition_reduction.packet.json"
ROUTE_A = PACKET_DIR / "route_a_phifin_boundary_emission_target.packet.json"
ROUTE_B = PACKET_DIR / "route_b_independent_primitive_row_kernel_contract.packet.json"
DECISION = PACKET_DIR / "primitive_row_execution_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteBIndependentPrimitiveRows_or_RouteAPhiFinBoundaryEmission_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_routeb_independentprimitive_rows_or_routea_phifinboundaryemission.py"

STATUS = "MTT_SELECTED_ROUTEB_INDEPENDENTPRIMITIVEROWS_OR_ROUTEA_PHIFINBOUNDARYEMISSION_BUILT_PRECONDITIONS_REDUCED"
NEXT = "MTT_Selected_DynamicPhiFinTraceBinding_or_PrimitiveRowFormulaExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    preconditions = load(PRECONDITIONS)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("Alpha1/dotD transport is no longer an active blocker" in note, "note misses retired blocker")

    retired = preconditions["retired_preconditions"]
    for key in [
        "selected_dotD_source_verified",
        "alpha1_driver_verified",
        "same_branch_alpha1_derivative_closed",
        "honest_dotD_replay_closed",
    ]:
        require(retired[key] is True, f"retired precondition missing: {key}")
    require(preconditions["basis_stage_accepted"] is True, "basis stage should be accepted")
    require(preconditions["primitive_row_count"] == 72, "primitive row count mismatch")
    require(preconditions["can_execute_rows_now"] is False, "primitive rows overexecutable")
    for key, value in preconditions["reduced_remaining_preconditions"].items():
        require(value is True, f"remaining precondition missing: {key}")

    require(route_a["status"] == "ROUTE_A_DYNAMIC_PHIFIN_BOUNDARY_EMISSION_OPEN", "Route A status mismatch")
    require(route_a["currently_emitted"]["stationary_source_identity"] is True, "stationary identity missing")
    require(route_a["currently_emitted"]["same_branch_alpha1_derivative"] is True, "alpha1 derivative missing")
    for key in ["dynamic_PhiFin_C1_payload", "boundary_source_R_Z_R_X", "physical_b_selected"]:
        require(route_a["currently_emitted"][key] is False, f"Route A overemitted {key}")
    require(route_a["lane_closes_now"] is False, "Route A overclosed")
    require(len(route_a["required_emissions"]) == 5, "Route A requirements mismatch")

    require(route_b["status"] == "ROUTE_B_PRIMITIVE_ROW_KERNEL_CONTRACT_REDUCED_NOT_EXECUTED", "Route B status mismatch")
    require(route_b["primitive_stage_row_count"] == 72, "Route B primitive count mismatch")
    require(len(route_b["primitive_stage_rows"]) == 72, "Route B primitive row list mismatch")
    require(len(route_b["required_kernel_fields_per_row"]) == 6, "Route B kernel fields mismatch")
    require(route_b["independent_rows_executed_now"] is False, "Route B rows overexecuted")
    require(route_b["independent_rows_emitted_count"] == 0, "Route B rows overemitted")
    require(route_b["replay_rows_allowed_as_acceptance_oracle_only"] is True, "replay oracle guardrail missing")
    require(route_b["lane_closes_now"] is False, "Route B overclosed")
    require(all(route_b["replay_diagnostics_available"].values()), "replay diagnostics not all available")

    require(decision["alpha1_dotD_is_no_longer_blocker"] is True, "decision did not retire alpha1/dotD")
    require(decision["route_b_replay_target_structurally_nondegenerate"] is True, "nondegenerate target missing")
    require(decision["route_a_dynamic_phifin_boundary_emission_closed"] is False, "Route A overclosed in decision")
    require(decision["route_b_independent_primitive_rows_executed"] is False, "Route B overexecuted in decision")
    require(decision["unpatched_dynamic_C1_packet_closed"] is False, "dynamic C1 overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")

    closure = data["closure_decision"]
    require(closure["alpha1_dotD_retired"] is True, "candidate alpha1/dotD not retired")
    require(closure["primitive_row_preconditions_reduced"] is True, "candidate preconditions not reduced")
    require(closure["route_a_dynamic_phifin_boundary_emission_closed"] is False, "candidate Route A overclosed")
    require(closure["route_b_independent_primitive_rows_executed"] is False, "candidate Route B overexecuted")
    require(closure["unpatched_dynamic_C1_packet_closed"] is False, "candidate dynamic C1 overclosed")

    for label, payload in [
        ("candidate", data),
        ("preconditions", preconditions),
        ("route_a", route_a),
        ("route_b", route_b),
        ("decision", decision),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
