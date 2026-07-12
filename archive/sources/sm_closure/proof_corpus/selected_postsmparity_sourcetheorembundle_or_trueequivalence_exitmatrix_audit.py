"""Audit post-SM-parity source-theorem bundle and true-equivalence exit matrix."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_postsmparity_sourcetheorembundle_or_trueequivalence_exitmatrix"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BUNDLE = PACKET_DIR / "post_smparity_source_theorem_bundle.packet.json"
EXIT_MATRIX = PACKET_DIR / "true_equivalence_exit_matrix.packet.json"
PAPER_CHECKLIST = PACKET_DIR / "paper_insertion_and_guardrail_checklist.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PostSMParity_SourceTheoremBundle_or_TrueEquivalenceExitMatrix_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_POSTSMPARITY_SOURCETHEOREMBUNDLE_OR_TRUEEQUIVALENCE_EXITMATRIX_BUILT"
NEXT = "MTT_Selected_HYMNewtonGalerkin_FirstSolve_or_Rank2SectorFunctor_v1"
PARALLEL_NEXT = "MTT_Selected_ProfileLikelihoodSourceImport_or_QaSU3PacketCandidateMining_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    bundle = load(BUNDLE)
    exit_matrix = load(EXIT_MATRIX)
    checklist = load(PAPER_CHECKLIST)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem not proved")
    require(data["closure_decision"]["SM_parity_closed"] is True, "SM parity should be closed")
    require(data["closure_decision"]["source_theorem_bundle_built"] is True, "source bundle missing")
    require(data["closure_decision"]["true_equivalence_exit_matrix_built"] is True, "exit matrix missing")
    require(data["closure_decision"]["actual_QaSU3_operator_packet_promoted"] is False, "Qa/SU3 overpromoted")
    require(data["closure_decision"]["precision_profile_complete"] is False, "precision profile overpromoted")
    require(data["closure_decision"]["unpatched_dynamic_C1_closed"] is False, "unpatched dynamic C1 overclosed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(data["closure_decision"]["no_knob_closed"] is False, "no-knob overclosed")
    require(data["next_required_artifact"] == NEXT, "wrong source next artifact")
    require(data["parallel_next_artifact"] == PARALLEL_NEXT, "wrong precision next artifact")

    closed = bundle["closed_for_SM_parity"]
    require(closed["SM_parity_under_declared_interface_standard"] is True, "SM parity closure not imported")
    require(closed["Higgs_replay_policy_refresh"] is True, "Higgs replay refresh not imported")
    require(closed["static_matter_slot_readout"] is True, "static matter-slot readout not imported")
    require(closed["patched_dynamic_C1_value_packet"] is True, "patched dynamic C1 packet not imported")
    require(closed["patched_A_b_deltaTheta_replay"] is True, "patched A/b/delta replay not imported")
    require(closed["final_replay_refresh_keeps_SM_parity_closed"] is True, "replay refresh reopened parity")

    support = bundle["support_only_not_promoted"]
    require(support["actual_QaSU3_operator_packet"] is False, "actual Qa/SU3 promoted unexpectedly")
    require(support["visible_operator_payload"] is False, "visible operator payload promoted unexpectedly")
    require(support["unpatched_dynamic_C1_packet"] is False, "unpatched C1 promoted unexpectedly")
    require(support["full_profile_likelihood"] is False, "full profile promoted unexpectedly")

    frontier = bundle["source_theorem_frontier"]
    require(frontier["actual_QaSU3_operator_packet"] is True, "Qa/SU3 frontier missing")
    require(frontier["selected_HYM_Newton_Galerkin_first_solve"] is True, "HYM frontier missing")
    require(frontier["rank2_to_sector_transfer_functor"] is True, "rank2 transfer frontier missing")
    require(frontier["selected_rho_E_metric_D_E_Riesz_Green_dotD_C1"] is True, "operator payload frontier missing")
    require(frontier["unpatched_dynamic_C1_derivation"] is True, "unpatched C1 frontier missing")

    require(exit_matrix["status"] == "TWO_LEGAL_EXITS_EXPLICIT", "exit matrix status mismatch")
    require(exit_matrix["exit_A_actual_source_theorem"]["primary_next"] == NEXT, "exit A next mismatch")
    require(exit_matrix["exit_B_precision_profile_values"]["primary_next"] == PARALLEL_NEXT, "exit B next mismatch")
    require(exit_matrix["exit_A_actual_source_theorem"]["closed_now"] is False, "exit A overclosed")
    require(exit_matrix["exit_B_precision_profile_values"]["closed_now"] is False, "exit B overclosed")
    require(exit_matrix["superset_use"]["using_one_straight_path"] is False, "superset marked straight-only")
    require(exit_matrix["superset_use"]["combines_multiple_paths"] is True, "superset combination not recorded")
    require(exit_matrix["true_SM_equivalence_closed"] is False, "exit matrix true equivalence overclosed")
    require(exit_matrix["no_knob_closed"] is False, "exit matrix no-knob overclosed")

    require(checklist["status"] == "READY_FOR_PAPER_DRAFT_INSERTION_WITH_OPEN_GATES", "checklist status mismatch")
    require(len(checklist["sections_to_add"]) == 4, "paper checklist section count changed")
    require("SM-parity is closed" in checklist["current_paper_ready_theorem"], "paper theorem missing parity claim")
    require("No observed constant" in checklist["current_paper_ready_theorem"], "paper theorem missing selector guard")

    require("SM-parity is closed under the declared parity-interface standard." in note, "note missing parity sentence")
    require("observed replay residuals cannot" in note, "note missing residual guardrail")

    for packet in [data, bundle, exit_matrix, checklist, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
