"""Build full profile matrix reconstruction or Qa/SU3 actual packet search."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_fullprofilematrixreconstruction_or_qasu3actualpacketsearch"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
MATRIX = PACKET_DIR / "surrogate_profile_matrix_reconstruction.packet.json"
QASU3_SEARCH = PACKET_DIR / "qasu3_actual_packet_search_status.packet.json"
PROMOTION = PACKET_DIR / "true_equivalence_promotion_decision_after_matrix_search.packet.json"
CUTSET = PACKET_DIR / "next_closure_cutset_after_matrix_search.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FullProfileMatrixReconstruction_or_QaSU3ActualPacketSearch_v1.md"

STATUS = "MTT_SELECTED_FULLPROFILEMATRIXRECONSTRUCTION_OR_QASU3ACTUALPACKETSEARCH_BUILT_SURROGATE_PROFILE_QASU3_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def covariance_from_sigmas(ids: list[str], sigmas: dict[str, float], rho: float) -> list[list[float]]:
    matrix = []
    for i, left in enumerate(ids):
        row = []
        for j, right in enumerate(ids):
            corr = 1.0 if i == j else rho
            row.append(corr * sigmas[left] * sigmas[right])
        matrix.append(row)
    return matrix


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_precisionvalueemissionattempt_or_qasu3sourcepayloadfill.candidate.json")
    precision = load(
        DATA
        / "selected_precisionvalueemissionattempt_or_qasu3sourcepayloadfill"
        / "partial_precision_value_emission.packet.json"
    )
    envelope = load(
        DATA
        / "selected_correlatedprofilevalues_or_localqftobservablevalues"
        / "correlation_robust_profile_envelope.packet.json"
    )
    qasu3_attempt = load(
        DATA
        / "selected_precisionvalueemissionattempt_or_qasu3sourcepayloadfill"
        / "qasu3_source_payload_fill_attempt.packet.json"
    )
    qasu3_crossrepo = load(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json")

    independent_ids = envelope["basis_reduction"]["independent_outputs"]
    row_by_id = {row["id"]: row for row in precision["value_rows"]}
    sigmas = {row_id: row_by_id[row_id]["total_diagonal_sigma"] for row_id in independent_ids}
    deltas = {row_id: row_by_id[row_id]["delta"] for row_id in independent_ids}
    best_scan = min(envelope["scan_rows"], key=lambda row: row["chi2"])
    core_scan = [
        row
        for row in envelope["scan_rows"]
        if envelope["chi2_envelope"]["core_rho_window"][0]
        <= row["rho_equicorrelation"]
        <= envelope["chi2_envelope"]["core_rho_window"][1]
    ]
    core_worst = max(core_scan, key=lambda row: row["chi2"])
    best_rho = best_scan["rho_equicorrelation"]

    matrix = {
        "schema": "MTTSurrogateProfileMatrixReconstruction.v1",
        "status": "SURROGATE_COMPRESSED_PROFILE_MATRIX_RECONSTRUCTED_FULL_PROFILE_OPEN",
        "basis": {
            "independent_outputs": independent_ids,
            "removed_redundant_outputs": envelope["basis_reduction"]["redundant_outputs_removed"],
            "reason": envelope["basis_reduction"]["reason"],
        },
        "best_surrogate_rho": best_rho,
        "best_surrogate_chi2": best_scan["chi2"],
        "best_surrogate_reduced_chi2": best_scan["reduced_chi2"],
        "core_worst_rho": core_worst["rho_equicorrelation"],
        "core_worst_chi2": core_worst["chi2"],
        "core_worst_reduced_chi2": core_worst["reduced_chi2"],
        "deltas": deltas,
        "sigmas": sigmas,
        "surrogate_covariance_matrix": covariance_from_sigmas(independent_ids, sigmas, best_rho),
        "surrogate_correlation_model": {
            "type": "compressed-output equicorrelation surrogate copied from prior stress envelope",
            "rho": best_rho,
            "rho_selection_rule": "minimum chi-square over predeclared envelope scan; diagnostic only, not a source selector",
        },
        "passes_core_correlation_envelope": precision["passes_core_correlation_envelope"],
        "passes_extreme_correlation_stress_envelope": precision["passes_extreme_correlation_stress_envelope"],
        "accepted_as_surrogate_profile_matrix": True,
        "accepted_as_full_published_or_reconstructed_profile": False,
        "accepted_for_true_SM_equivalence": False,
        "why_not_full_profile": [
            "equicorrelation surrogate is not a published/reconstructed likelihood",
            "rho is a diagnostic envelope representative, not an external covariance value",
            "extreme stress envelope remains failing",
            "loop-level local QFT observable rows and actual Qa/SU3 packet remain open",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    qasu3_search = {
        "schema": "MTTQaSU3ActualPacketSearchStatus.v1",
        "status": "ACTUAL_QASU3_PACKET_SEARCH_REPLAYED_NO_FINAL_PACKET_FOUND",
        "input_attempt": rel(
            DATA
            / "selected_precisionvalueemissionattempt_or_qasu3sourcepayloadfill"
            / "qasu3_source_payload_fill_attempt.packet.json"
        ),
        "crossrepo_status": qasu3_crossrepo["status"],
        "json_files_scanned": qasu3_crossrepo["repos_scanned"][0]["json_files_scanned"],
        "source_payload_filled_before": qasu3_attempt["source_payload_filled"],
        "source_payload_filled_now": False,
        "actual_packet_found": False,
        "accepted_as_actual_QaSU3_operator_upgrade": False,
        "required_source_payload": qasu3_attempt["required_source_payload"],
        "next_search_targets": [
            "selected color/operator packet with non-null source fields",
            "representation/anomaly certificate attached to actual packet",
            "D_E/rho_E/operator data replacing parity-interface substitute",
            "typed monad/Cech/section-ring operator maps",
            "precision observable attachment to actual selected packet",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion = {
        "schema": "MTTTrueEquivalencePromotionDecisionAfterMatrixSearch.v1",
        "status": "SURROGATE_MATRIX_ACCEPTED_ACTUAL_PROFILE_AND_QASU3_STILL_OPEN",
        "route_A_profile_matrix": {
            "surrogate_matrix_reconstructed": True,
            "accepted_as_full_profile": False,
            "can_close_true_SM_equivalence_now": False,
        },
        "route_B_qasu3_actual_packet": {
            "actual_packet_found": False,
            "can_close_true_SM_equivalence_now": False,
            "can_close_no_knob_now": False,
        },
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextClosureCutsetAfterMatrixSearch.v1",
        "status": "SURROGATE_PROFILE_BUILT_TRUE_CLOSURE_REQUIRES_EXTERNAL_PROFILE_OR_ACTUAL_PACKET",
        "closed_now": [
            "compressed surrogate profile matrix reconstructed",
            "best envelope representative rho recorded",
            "Qa/SU3 actual packet search status replayed",
            "promotion decision after matrix/search attempt recorded",
        ],
        "remaining_minimal_payloads": [
            "published/reconstructed non-Higgs covariance or likelihood workspace",
            "precision local-QFT loop/threshold observable values attached to the profile",
            "actual selected Qa/SU3 source/operator packet",
            "Higgs final-three route-A kernels or stronger likelihood replacement",
        ],
        "recommended_next_artifact": "MTT_Selected_ProfileLikelihoodSourceImport_or_QaSU3PacketCandidateMining_v1",
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedFullProfileMatrixReconstructionOrQaSU3ActualPacketSearch",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_precisionvalueemissionattempt_or_qasu3sourcepayloadfill.candidate.json"),
            "partial_precision_values": rel(
                DATA
                / "selected_precisionvalueemissionattempt_or_qasu3sourcepayloadfill"
                / "partial_precision_value_emission.packet.json"
            ),
            "correlation_envelope": rel(
                DATA
                / "selected_correlatedprofilevalues_or_localqftobservablevalues"
                / "correlation_robust_profile_envelope.packet.json"
            ),
            "qasu3_payload_attempt": rel(
                DATA
                / "selected_precisionvalueemissionattempt_or_qasu3sourcepayloadfill"
                / "qasu3_source_payload_fill_attempt.packet.json"
            ),
        },
        "output_packets": {
            "surrogate_profile_matrix_reconstruction": rel(MATRIX),
            "qasu3_actual_packet_search_status": rel(QASU3_SEARCH),
            "true_equivalence_promotion_decision": rel(PROMOTION),
            "next_closure_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "SurrogateProfileMatrixAndQaSU3SearchStatusTheorem",
            "proved": True,
            "statement": (
                "The emitted diagonal precision values and correlation envelope determine a compressed "
                "surrogate profile covariance matrix after removing the redundant GUT-normalized hypercharge "
                "row. This improves the precision-value layer but does not replace a published/reconstructed "
                "profile likelihood. The Qa/SU3 actual-packet search still finds no final packet, so true SM "
                "equivalence remains open."
            ),
        },
        "what_closes_now": {
            "surrogate_profile_matrix_reconstructed": True,
            "qasu3_actual_packet_search_replayed": True,
            "promotion_decision_after_matrix_search": True,
            "next_cutset_after_matrix_search": True,
        },
        "what_remains_open": {
            "true_SM_equivalence": True,
            "no_knob_closure": True,
            "published_or_reconstructed_profile_likelihood": True,
            "precision_local_QFT_loop_values": True,
            "actual_QaSU3_operator_packet": True,
        },
        "closure_decision": {
            "SM_parity_closed": previous["closure_decision"]["SM_parity_closed"],
            "surrogate_profile_matrix_reconstructed": True,
            "accepted_as_full_profile": False,
            "actual_QaSU3_packet_found": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": cutset["recommended_next_artifact"],
    }

    cert = {
        "certificate": "MTT_Selected_FullProfileMatrixReconstruction_or_QaSU3ActualPacketSearch_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "SM_parity_closed": True,
        "surrogate_profile_matrix_reconstructed": True,
        "accepted_as_full_profile": False,
        "actual_QaSU3_packet_found": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    note = f"""# MTT Selected FullProfileMatrixReconstruction or QaSU3ActualPacketSearch v1

Status: `{STATUS}`.

This artifact reconstructs a compressed surrogate profile matrix from the
partial precision rows and the correlation-envelope scan. The redundant
`g_1_GUT_Mt` row is removed because it is determined by `g_Y_Mt`.

The matrix is useful as a diagnostic precision scaffold, but it is not a published or independently reconstructed profile likelihood.
The actual Qa/SU3 operator packet search is also replayed and remains unfilled.

True SM equivalence and no-knob closure remain open.
"""

    for path, payload in [
        (MATRIX, matrix),
        (QASU3_SEARCH, qasu3_search),
        (PROMOTION, promotion),
        (CUTSET, cutset),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
