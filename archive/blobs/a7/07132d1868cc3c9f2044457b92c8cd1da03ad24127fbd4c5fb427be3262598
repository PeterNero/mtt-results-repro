"""Audit full profile matrix reconstruction or Qa/SU3 actual packet search."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_fullprofilematrixreconstruction_or_qasu3actualpacketsearch"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
MATRIX = PACKET_DIR / "surrogate_profile_matrix_reconstruction.packet.json"
QASU3_SEARCH = PACKET_DIR / "qasu3_actual_packet_search_status.packet.json"
PROMOTION = PACKET_DIR / "true_equivalence_promotion_decision_after_matrix_search.packet.json"
CUTSET = PACKET_DIR / "next_closure_cutset_after_matrix_search.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FullProfileMatrixReconstruction_or_QaSU3ActualPacketSearch_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_FULLPROFILEMATRIXRECONSTRUCTION_OR_QASU3ACTUALPACKETSEARCH_BUILT_SURROGATE_PROFILE_QASU3_OPEN"
NEXT = "MTT_Selected_ProfileLikelihoodSourceImport_or_QaSU3PacketCandidateMining_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    matrix = load(MATRIX)
    qasu3 = load(QASU3_SEARCH)
    promotion = load(PROMOTION)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(matrix["accepted_as_surrogate_profile_matrix"] is True, "surrogate matrix not accepted")
    require(matrix["accepted_as_full_published_or_reconstructed_profile"] is False, "full profile overaccepted")
    require(matrix["accepted_for_true_SM_equivalence"] is False, "matrix overaccepted for true equivalence")
    require(matrix["basis"]["independent_outputs"] == ["lambda_Mt", "y_t_Mt", "g_2_Mt", "g_Y_Mt", "g_3_Mt"], "basis mismatch")
    require(matrix["basis"]["removed_redundant_outputs"] == ["g_1_GUT_Mt"], "redundant row not removed")
    require(len(matrix["surrogate_covariance_matrix"]) == 5, "covariance matrix row count mismatch")
    require(all(len(row) == 5 for row in matrix["surrogate_covariance_matrix"]), "covariance matrix column count mismatch")
    require(matrix["passes_core_correlation_envelope"] is True, "core envelope not passing")
    require(matrix["passes_extreme_correlation_stress_envelope"] is False, "extreme envelope unexpectedly passing")

    require(qasu3["actual_packet_found"] is False, "Qa/SU3 packet overfound")
    require(qasu3["source_payload_filled_now"] is False, "Qa/SU3 payload overfilled")
    require(qasu3["accepted_as_actual_QaSU3_operator_upgrade"] is False, "Qa/SU3 overaccepted")
    require(len(qasu3["next_search_targets"]) >= 5, "Qa/SU3 search targets underspecified")

    require(promotion["route_A_profile_matrix"]["surrogate_matrix_reconstructed"] is True, "route A surrogate missing")
    require(promotion["route_A_profile_matrix"]["accepted_as_full_profile"] is False, "route A overaccepted")
    require(promotion["route_A_profile_matrix"]["can_close_true_SM_equivalence_now"] is False, "route A overcloses")
    require(promotion["route_B_qasu3_actual_packet"]["actual_packet_found"] is False, "route B overfound")
    require(promotion["true_SM_equivalence_closed"] is False, "promotion true equivalence overclosed")
    require(promotion["no_knob_closed"] is False, "promotion no-knob overclosed")

    require(cutset["recommended_next_artifact"] == NEXT, "cutset next artifact mismatch")
    require("published/reconstructed non-Higgs covariance or likelihood workspace" in cutset["remaining_minimal_payloads"], "profile payload missing")
    require("actual selected Qa/SU3 source/operator packet" in cutset["remaining_minimal_payloads"], "Qa/SU3 payload missing")

    require(data["closure_decision"]["surrogate_profile_matrix_reconstructed"] is True, "candidate surrogate missing")
    require(data["closure_decision"]["accepted_as_full_profile"] is False, "candidate full profile overaccepted")
    require(data["closure_decision"]["actual_QaSU3_packet_found"] is False, "candidate Qa/SU3 overfound")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true overclosed")
    require(cert["surrogate_profile_matrix_reconstructed"] is True, "certificate surrogate missing")
    require(cert["accepted_as_full_profile"] is False, "certificate full profile overaccepted")
    require("not a published or independently reconstructed profile likelihood" in note, "note missing guardrail")

    for packet in [matrix, qasu3, promotion, cutset, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
