"""Audit selected R_theta Route-C Galerkin solve / diagonal profile theorem gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_rtheta_selectedroutecgalerkinsolve_or_diagonalprofiletheorem"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
EXTERNAL = PACKET_DIR / "external_strominger_galerkin_inspiration.packet.json"
SOLVE_CONTRACT = PACKET_DIR / "selected_routec_galerkin_solve_acceptance_contract.packet.json"
READINESS = PACKET_DIR / "current_selected_routec_solve_readiness.packet.json"
DIAGONAL = PACKET_DIR / "diagonal_profile_theorem_attempt.packet.json"
DECISION = PACKET_DIR / "selected_solve_or_diagonal_profile_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_selected_solve_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RThetaSelectedRouteCGalerkinSolve_or_DiagonalProfileTheorem_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_RTHETASELECTEDROUTECGALERKINSOLVE_OR_DIAGONALPROFILETHEOREM_"
    "BUILT_SOLVE_CONTRACT_DIAGONAL_LIMITATION_OPEN"
)
NEXT = "MTT_Selected_RThetaSelectedRouteCSolveExecution_or_ProfileWorkspaceIngest_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    external = load(EXTERNAL)
    contract = load(SOLVE_CONTRACT)
    readiness = load(READINESS)
    diagonal = load(DIAGONAL)
    decision = load(DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")

    require(
        external["status"] == "EXTERNAL_INSPIRATION_IMPORTED_AS_ACCEPTANCE_SHAPE_ONLY",
        "external inspiration status mismatch",
    )
    require(len(external["references"]) == 4, "external reference count mismatch")
    for ref in external["references"]:
        require(ref["url"].startswith("https://"), f"external reference URL invalid: {ref['id']}")
    require(external["closure_claimed"] is False, "external inspiration overclaimed")
    require(external["observed_data_used_as_selector"] is False, "external selector guard missing")
    require(external["target_fitting_used"] is False, "external target-fitting guard missing")

    require(
        contract["status"] == "SELECTED_ROUTEC_GALERKIN_SOLVE_CONTRACT_EMITTED",
        "solve contract status mismatch",
    )
    require(contract["contract_closed"] is True, "solve contract not closed")
    require(contract["closure_claimed"] is True, "solve contract should claim local contract closure")
    require(len(contract["must_emit"]) >= 7, "solve contract obligations too weak")
    for needle in ["selected_source_verified", "coherent spectral", "primitive C1", "no observed masses"]:
        require(
            any(needle in row for row in contract["must_emit"]),
            f"solve contract missing obligation fragment: {needle}",
        )
    require(contract["observed_data_used_as_selector"] is False, "contract selector guard missing")
    require(contract["target_fitting_used"] is False, "contract target-fitting guard missing")

    require(
        readiness["status"] == "CURRENT_SOLVE_READINESS_AUDITED_SUPPORT_STRONG_VALUES_OPEN",
        "readiness status mismatch",
    )
    require(readiness["present_count"] == 4, "readiness present count changed unexpectedly")
    require(readiness["required_count"] == 7, "readiness required count mismatch")
    require(readiness["selected_routec_galerkin_solve_closed"] is False, "readiness overclosed solve")
    rows = {row["id"]: row for row in readiness["readiness_rows"]}
    for key in [
        "q79_polarization",
        "block_projector_retention",
        "sector_projector_matrices",
        "stationary_projector_source",
    ]:
        require(rows[key]["present"] is True, f"readiness positive row missing: {key}")
    for key in [
        "coherent_spectral_projector_retention",
        "selected_DE_Riesz_Green_dotD",
        "honest_dotD_replay_without_lifted_flags",
    ]:
        require(rows[key]["present"] is False, f"readiness blocker overclosed: {key}")
    require(readiness["closure_claimed"] is False, "readiness overclaimed")

    require(
        diagonal["status"]
        == "DIAGONAL_PROFILE_LIMITATION_THEOREM_ATTEMPTED_NOT_ACCEPTED_FOR_TRUE_EQUIVALENCE",
        "diagonal attempt status mismatch",
    )
    require(diagonal["coarse_diagonal_profile_available"] is True, "coarse diagonal profile should be available")
    require(diagonal["full_correlated_profile_imported"] is False, "full correlated profile overimported")
    require(
        diagonal["accepted_diagonal_limitation_theorem_for_true_equivalence"] is False,
        "diagonal theorem overaccepted for true equivalence",
    )
    require(
        diagonal["accepted_as_diagnostic_or_SM_parity_limited_profile"] is True,
        "diagonal diagnostic profile should remain usable",
    )
    require(diagonal["closure_claimed"] is False, "diagonal attempt overclaimed")

    require(decision["status"] == "SOLVE_CONTRACT_CLOSED_SOLVE_AND_PROFILE_STILL_OPEN", "decision status mismatch")
    require(decision["selected_routec_galerkin_solve_contract_closed"] is True, "decision contract not closed")
    for key in [
        "selected_routec_galerkin_solve_closed",
        "diagonal_profile_theorem_accepted_for_true_equivalence",
        "Pi_Rtheta_closed",
        "profile_response_closed",
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(len(decision["minimal_next_actions"]) == 4, "decision next-action count mismatch")
    require(decision["closure_claimed"] is False, "decision overclaimed")

    require(cutset["status"] == "NEXT_ATTACK_SOLVE_EXECUTION_OR_PROFILE_WORKSPACE_INGEST", "cutset status mismatch")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    for key in [
        "external_inspiration_imported_as_contract_shape",
        "selected_routec_solve_acceptance_contract",
        "current_readiness_audited",
        "diagonal_profile_theorem_attempt_scoped",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset missing local closure: {key}")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")

    final = data["closure_decision"]
    require(final["selected_routec_galerkin_solve_contract_closed"] is True, "candidate final contract not closed")
    for key in [
        "selected_routec_galerkin_solve_closed",
        "diagonal_profile_theorem_accepted_for_true_equivalence",
        "Pi_Rtheta_closed",
        "profile_response_closed",
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(final[key] is False, f"candidate final overclosed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(cert["selected_routec_galerkin_solve_contract_closed"] is True, "certificate contract missing")
    require(cert["selected_routec_galerkin_solve_closed"] is False, "certificate solve overclosed")
    require(cert["diagonal_profile_true_equivalence_closed"] is False, "certificate diagonal overclosed")
    require("readiness rows present      : 4/7" in note, "note missing readiness count")
    require("selected solve closed       : false" in note, "note missing solve-open guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
