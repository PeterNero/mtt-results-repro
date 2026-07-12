"""Audit Step 41 single-branch first-response solution assembly."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step41_singlebranch_solution_assembly_or_valuefunctionalfrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOLUTION = PACKET_DIR / "step41_q79_f_m1_first_response_solution.packet.json"
FRONTIER = PACKET_DIR / "step41_value_functional_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step41_SingleBranchSolutionAssembly_or_ValueFunctionalFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP41_SINGLE_BRANCH_FIRST_RESPONSE_SOLUTION_ASSEMBLED_VALUE_ROWS_OPEN"
NEXT = "MTT_Selected_ValueFunctionalRows_From_AssembledFirstResponseSolution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    solution = load(SOLUTION)
    frontier = load(FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")

    for packet in [data, solution, frontier, cert]:
        require(packet.get("target_fitting_used") is False, "target fitting violation")
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")

    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(solution["theorem"]["proved"] is True, "solution theorem not proved")
    require(solution["status"] == "SINGLE_Q79_F_M1_FIRST_RESPONSE_SOLUTION_ASSEMBLED", "solution status mismatch")

    branch = solution["selected_branch"]
    require(branch["q"] == 79, "wrong q branch")
    require(branch["orientation"] == "F", "wrong orientation branch")
    require(branch["torsion_m"] == 1, "wrong torsion branch")
    require("Heisenberg-Weyl" in branch["finite_source"], "rho_E source not named")
    require("D_E = d + du ad(T3)" in branch["covariant"], "selected covariant not named")

    for key, value in solution["closed_checks"].items():
        require(value is True, f"closed check failed: {key}")

    decision = data["closure_decision"]
    for key in [
        "single_branch_first_response_solution_assembled",
        "selected_q79_F_m1_branch_fixed",
        "selected_S3_source_chain_closed",
        "selected_operator_transport_chain_closed",
        "primitive_C1_first_response_layer_closed",
        "selected_A_selected_promoted",
        "selected_b_selected_promoted",
        "selected_deltaTheta_C1_promoted",
        "selected_dynamic_overlap_tensor_closed",
        "selected_source_to_C1_transfer_map_closed",
        "selected_Rtheta_scalar_value_functional_source_domain_closed",
    ]:
        require(decision[key] is True, f"decision close missing: {key}")
        require(cert[key] is True, f"certificate close missing: {key}")

    require(decision["accepted_internal_scalar_row_count"] == 0, "candidate scalar rows overaccepted")
    require(cert["accepted_internal_scalar_row_count"] == 0, "certificate scalar rows overaccepted")
    for key in [
        "accepted_value_functional_rows_closed",
        "accepted_Yukawa_magnitudes_closed",
        "CKM_PMNS_measured_value_closure_closed",
        "lambda_H_row_emitted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")

    closed_now = frontier["closed_now"]
    for key in [
        "single_branch_first_response_solution_assembled",
        "primitive_C1_first_response_layer_closed",
        "selected_A_selected_promoted",
        "selected_b_selected_promoted",
        "selected_deltaTheta_C1_promoted",
        "selected_dynamic_overlap_tensor_closed",
        "selected_source_to_C1_transfer_map_closed",
        "selected_Rtheta_scalar_value_functional_source_domain_closed",
    ]:
        require(closed_now[key] is True, f"frontier close missing: {key}")

    still_open = frontier["still_open"]
    require(still_open["accepted_internal_scalar_row_count"] == 0, "frontier scalar rows overaccepted")
    for key in [
        "accepted_value_functional_rows_closed",
        "accepted_Yukawa_magnitudes_closed",
        "CKM_PMNS_measured_value_closure_closed",
        "lambda_H_row_emitted",
        "threshold_matching_internal_rows_closed",
        "mass_scheme_internal_rows_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(still_open[key] is False, f"frontier overclosed: {key}")

    for key, value in frontier["open_checks"].items():
        require(value is True, f"open-boundary check failed: {key}")
    require(frontier["next_required_payload"]["target"] == NEXT, "frontier next mismatch")

    for phrase in [
        "q=79",
        "orientation `F`",
        "torsion `m=1`",
        "first-response/operator-source branch is now assembled",
        "superseded at this layer by the later Step24/VSD01 packets",
        "accepted internal scalar rows",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
