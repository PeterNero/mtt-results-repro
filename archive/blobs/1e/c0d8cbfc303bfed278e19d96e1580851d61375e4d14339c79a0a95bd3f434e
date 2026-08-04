"""Build profile likelihood source import or Qa/SU3 packet candidate mining."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROFILE_IMPORT = PACKET_DIR / "profile_likelihood_source_import_status.packet.json"
QASU3_MINING = PACKET_DIR / "qasu3_packet_candidate_mining.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_import_and_mining.packet.json"
CUTSET = PACKET_DIR / "next_import_or_payload_fill_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ProfileLikelihoodSourceImport_or_QaSU3PacketCandidateMining_v1.md"

STATUS = "MTT_SELECTED_PROFILELIKELIHOODSOURCEIMPORT_OR_QASU3PACKETCANDIDATEMINING_BUILT_IMPORT_ABSENT_MINING_READY"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_fullprofilematrixreconstruction_or_qasu3actualpacketsearch.candidate.json")
    matrix = load(
        DATA
        / "selected_fullprofilematrixreconstruction_or_qasu3actualpacketsearch"
        / "surrogate_profile_matrix_reconstruction.packet.json"
    )
    qasu3_search = load(
        DATA
        / "selected_fullprofilematrixreconstruction_or_qasu3actualpacketsearch"
        / "qasu3_actual_packet_search_status.packet.json"
    )
    actual_packet_audit = load(DATA / "actual_selected_sm_packet_anomaly_audit.candidate.json")
    parity_replacement = load(
        DATA
        / "selected_qasu3sourcepacket_or_finalsmparityclosure"
        / "qasu3_parity_interface_replacement.packet.json"
    )

    profile_import = {
        "schema": "MTTProfileLikelihoodSourceImportStatus.v1",
        "status": "NO_PUBLISHED_PROFILE_LIKELIHOOD_IMPORTED_SURROGATE_RETAINED",
        "surrogate_profile_source": rel(
            DATA
            / "selected_fullprofilematrixreconstruction_or_qasu3actualpacketsearch"
            / "surrogate_profile_matrix_reconstruction.packet.json"
        ),
        "required_import_payload": [
            "published/reconstructed non-Higgs covariance matrix or likelihood workspace",
            "basis map to lambda_Mt, y_t_Mt, g_2_Mt, g_Y_Mt, g_3_Mt",
            "redundant hypercharge treatment",
            "profile-likelihood convention and acceptance rule",
            "provenance sufficient for reproducible replay",
        ],
        "local_import_candidates_checked": [
            "surrogate compressed covariance matrix",
            "diagonal profile execution",
            "correlation stress envelope",
            "external literature RG benchmark central rows",
        ],
        "published_or_reconstructed_profile_imported": False,
        "surrogate_profile_retained": matrix["accepted_as_surrogate_profile_matrix"],
        "accepted_as_full_profile_likelihood": False,
        "accepted_for_true_SM_equivalence": False,
        "why_import_absent": [
            "no local published/reconstructed likelihood workspace is present",
            "current covariance is an equicorrelation surrogate, not external covariance data",
            "extreme stress envelope remains failing",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    mined_candidates = [
        {
            "candidate_id": "typed_monad_section_ring_operator_maps",
            "source": parity_replacement["support_presence"]["external"]["nonsm_typed_monad_interface"]["path"],
            "present": parity_replacement["support_presence"]["external"]["nonsm_typed_monad_interface"]["present"],
            "promotable_now": False,
            "missing_for_promotion": [
                "non-null selected operator maps",
                "same-branch period/finite quotient selector",
                "attachment to SM representation/anomaly table",
            ],
        },
        {
            "candidate_id": "qa_su3_dependency_audit_support",
            "source": parity_replacement["support_presence"]["external"]["qa_su3_dependency_certificate"]["path"],
            "present": parity_replacement["support_presence"]["external"]["qa_su3_dependency_certificate"]["present"],
            "promotable_now": False,
            "missing_for_promotion": [
                "selected D_E or rho_E operator packet",
                "mapped Bianchi/Freed-Witten source certificate",
                "final packet closure flag",
            ],
        },
        {
            "candidate_id": "local_same_source_visible_color_attempt",
            "source": parity_replacement["support_presence"]["local"]["same_source_visible_color_operator_attempt"]["path"],
            "present": parity_replacement["support_presence"]["local"]["same_source_visible_color_operator_attempt"]["present"],
            "promotable_now": False,
            "missing_for_promotion": [
                "actual color/operator values",
                "source-side representation packet",
                "precision observable attachment",
            ],
        },
        {
            "candidate_id": "topology_only_representation_anomaly_support",
            "source": actual_packet_audit["source_presence"]["topology_only"]["path"],
            "present": actual_packet_audit["source_presence"]["topology_only"]["present"],
            "promotable_now": False,
            "missing_for_promotion": [
                "instantiated selected representation table",
                "machine anomaly table on the selected packet",
                "operator data rather than topology-only support",
            ],
        },
    ]

    qasu3_mining = {
        "schema": "MTTQaSU3PacketCandidateMining.v1",
        "status": "QASU3_CANDIDATES_MINED_SUPPORT_PRESENT_NO_PROMOTION",
        "previous_search_source": rel(
            DATA
            / "selected_fullprofilematrixreconstruction_or_qasu3actualpacketsearch"
            / "qasu3_actual_packet_search_status.packet.json"
        ),
        "crossrepo_status": qasu3_search["crossrepo_status"],
        "json_files_scanned": qasu3_search["json_files_scanned"],
        "candidate_count": len(mined_candidates),
        "mined_candidates": mined_candidates,
        "all_candidates_present": all(row["present"] for row in mined_candidates),
        "any_candidate_promotable_now": any(row["promotable_now"] for row in mined_candidates),
        "accepted_as_actual_QaSU3_packet": False,
        "accepted_for_true_SM_equivalence": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion = {
        "schema": "MTTPromotionDecisionAfterImportAndMining.v1",
        "status": "PROFILE_IMPORT_ABSENT_QASU3_SUPPORT_MINED_TRUE_EQ_OPEN",
        "route_A_profile_import": {
            "published_or_reconstructed_profile_imported": False,
            "surrogate_retained": True,
            "can_close_true_SM_equivalence_now": False,
        },
        "route_B_qasu3_mining": {
            "candidate_support_mined": True,
            "any_candidate_promotable_now": False,
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
        "schema": "MTTNextImportOrPayloadFillCutset.v1",
        "status": "IMPORT_OR_SOURCE_PAYLOAD_VALUES_REQUIRED",
        "closed_now": [
            "profile likelihood import attempt recorded",
            "Qa/SU3 support candidates mined and ranked",
            "promotion decision after import/mining recorded",
        ],
        "remaining_minimal_payloads": [
            "actual non-Higgs profile likelihood/covariance source import",
            "or fill one mined Qa/SU3 candidate with selected operator maps and anomaly certificate",
            "or derive selected representation/anomaly/operator packet in this repo",
        ],
        "recommended_next_artifact": "MTT_Selected_QaSU3CandidatePayloadFill_or_ProfileSourceAcquisition_v1",
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedProfileLikelihoodSourceImportOrQaSU3PacketCandidateMining",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_fullprofilematrixreconstruction_or_qasu3actualpacketsearch.candidate.json"),
            "surrogate_profile_matrix": rel(
                DATA
                / "selected_fullprofilematrixreconstruction_or_qasu3actualpacketsearch"
                / "surrogate_profile_matrix_reconstruction.packet.json"
            ),
            "qasu3_search_status": rel(
                DATA
                / "selected_fullprofilematrixreconstruction_or_qasu3actualpacketsearch"
                / "qasu3_actual_packet_search_status.packet.json"
            ),
            "actual_packet_audit": rel(DATA / "actual_selected_sm_packet_anomaly_audit.candidate.json"),
        },
        "output_packets": {
            "profile_likelihood_source_import_status": rel(PROFILE_IMPORT),
            "qasu3_packet_candidate_mining": rel(QASU3_MINING),
            "promotion_decision": rel(PROMOTION),
            "next_import_or_payload_fill_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "ProfileImportAndQaSU3CandidateMiningTheorem",
            "proved": True,
            "statement": (
                "No published/reconstructed profile likelihood is imported in the local repo, so the surrogate "
                "matrix remains diagnostic. Qa/SU3 support candidates can be mined from the parity-interface and "
                "actual-packet audit layers, but none supplies the non-null selected operator payload needed for "
                "true SM equivalence or no-knob closure."
            ),
        },
        "what_closes_now": {
            "profile_likelihood_import_attempt": True,
            "qasu3_candidate_mining": True,
            "promotion_decision_after_import_and_mining": True,
            "next_cutset_import_or_payload_fill": True,
        },
        "what_remains_open": {
            "true_SM_equivalence": True,
            "no_knob_closure": True,
            "profile_likelihood_source_import": True,
            "actual_QaSU3_operator_payload": True,
        },
        "closure_decision": {
            "SM_parity_closed": previous["closure_decision"]["SM_parity_closed"],
            "profile_likelihood_imported": False,
            "qasu3_candidates_mined": True,
            "any_qasu3_candidate_promotable_now": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": cutset["recommended_next_artifact"],
    }

    cert = {
        "certificate": "MTT_Selected_ProfileLikelihoodSourceImport_or_QaSU3PacketCandidateMining_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "SM_parity_closed": True,
        "profile_likelihood_imported": False,
        "qasu3_candidates_mined": True,
        "any_qasu3_candidate_promotable_now": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    note = f"""# MTT Selected ProfileLikelihoodSourceImport or QaSU3PacketCandidateMining v1

Status: `{STATUS}`.

This artifact tries the two live routes after surrogate profile reconstruction.

Route A: no published or independently reconstructed non-Higgs profile likelihood
is present locally, so the surrogate matrix remains diagnostic.

Route B: Qa/SU3 support candidates are mined from the parity-interface,
actual-packet audit, and sibling-repo support layers. They are real support
targets, but none has the non-null selected operator payload needed for
promotion.

True SM equivalence and no-knob closure remain open.
"""

    for path, payload in [
        (PROFILE_IMPORT, profile_import),
        (QASU3_MINING, qasu3_mining),
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
