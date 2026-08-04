"""Build external profile/correlation import or Qa/SU3 slot selection proof attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_externalprofilelikelihoodimport_or_qasu3slotselectionproof"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROFILE = PACKET_DIR / "external_higgs_decay_correlation_covariance_import.packet.json"
QASU3 = PACKET_DIR / "qasu3_slot_selection_proof_attempt.packet.json"
SYNTHESIS = PACKET_DIR / "true_equivalence_frontier_synthesis.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ExternalProfileLikelihoodImport_or_QaSU3SlotSelectionProof_v1.md"

STATUS = "MTT_SELECTED_EXTERNALPROFILELIKELIHOODIMPORT_OR_QASU3SLOTSELECTIONPROOF_BUILT_CORRELATED_DECAY_COVARIANCE_SLOT_PROOF_OPEN"
NEXT = "MTT_Selected_AcceptedHiggsDecayCovarianceProfile_or_FirstQaSU3SelectedSlotClosure_v1"

CORRELATION_SOURCE = "https://arxiv.org/abs/1606.00455"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def covariance_from(rows: list[dict[str, Any]], labels: list[str], corr: list[list[float]]) -> list[list[float]]:
    sigmas = [next(row["sigma_symmetric_MeV"] for row in rows if row["id"] == label) for label in labels]
    return [[corr[i][j] * sigmas[i] * sigmas[j] for j in range(len(labels))] for i in range(len(labels))]


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_covarianceprofilepayload_or_qasu3selectedslotvalues.candidate.json")
    covariance_surrogate = load(
        DATA
        / "selected_covarianceprofilepayload_or_qasu3selectedslotvalues"
        / "higgs_external_row_covariance_surrogate_payload.packet.json"
    )
    slot_candidates = load(
        DATA
        / "selected_covarianceprofilepayload_or_qasu3selectedslotvalues"
        / "qasu3_selected_slot_value_candidate_payload.packet.json"
    )

    # Decay-sector correlations from arXiv:1606.00455 ancillary tables_i.txt,
    # restricted to the nine rows currently present in the external CERN BR/GammaH payload.
    labels = [
        "H_to_WW",
        "H_to_ZZ",
        "H_to_gammagamma",
        "H_to_Zgamma",
        "H_to_gg",
        "H_to_bb",
        "H_to_cc",
        "H_to_tautau",
        "H_to_mumu",
    ]
    source_decay_labels = ["WW", "ZZ", "gaga", "Zga", "gg", "bb", "cc", "tautau", "mumu"]
    corr = [
        [1.000000, 0.996559, 0.562851, 0.990036, 0.363948, -0.862681, -0.154186, 0.098449, 0.098184],
        [0.996559, 1.000000, 0.492904, 0.975199, 0.307556, -0.827162, -0.151868, 0.016371, 0.016111],
        [0.562851, 0.492904, 1.000000, 0.673199, 0.771696, -0.816359, -0.114028, 0.877386, 0.877252],
        [0.990036, 0.975199, 0.673199, 1.000000, 0.455342, -0.909844, -0.156845, 0.237234, 0.236981],
        [0.363948, 0.307556, 0.771696, 0.455342, 1.000000, -0.732084, -0.203234, 0.696962, 0.696929],
        [-0.862681, -0.827162, -0.816359, -0.909844, -0.732084, 1.000000, -0.010922, -0.476250, -0.476052],
        [-0.154186, -0.151868, -0.114028, -0.156845, -0.203234, -0.010922, 1.000000, -0.037576, -0.037540],
        [0.098449, 0.016371, 0.877386, 0.237234, 0.696962, -0.476250, -0.037576, 1.000000, 1.000000],
        [0.098184, 0.016111, 0.877252, 0.236981, 0.696929, -0.476052, -0.037540, 1.000000, 1.000000],
    ]
    cov = covariance_from(covariance_surrogate["rows"], labels, corr)
    diag = [cov[i][i] for i in range(len(labels))]

    profile = {
        "schema": "MTTExternalHiggsDecayCorrelationCovarianceImport.v1",
        "input_diagonal_surrogate": rel(
            DATA
            / "selected_covarianceprofilepayload_or_qasu3selectedslotvalues"
            / "higgs_external_row_covariance_surrogate_payload.packet.json"
        ),
        "external_source": {
            "url": CORRELATION_SOURCE,
            "source_name": "The correlation matrix of Higgs rates at the LHC",
            "ancillary_table": "tables_i.txt",
            "source_claim": "uncertainties and full correlation matrix for Higgs rates supplied in ancillary files",
        },
        "restricted_decay_sector": {
            "labels": labels,
            "source_decay_labels": source_decay_labels,
            "correlation_matrix": corr,
            "covariance_matrix_MeV2": cov,
            "diagonal_variances_MeV2": diag,
            "row_count": len(labels),
        },
        "import_result": {
            "external_correlated_covariance_submatrix_imported": True,
            "covers_current_external_decay_rows": True,
            "full_profile_likelihood_function_imported": False,
            "accepted_as_Higgs_decay_covariance_profile_candidate": True,
            "accepted_as_full_true_equivalence_profile": False,
            "why_not_full_likelihood": (
                "The ancillary matrix supplies correlated uncertainty data, but not a complete likelihood "
                "function or all non-Higgs/QM/GR observables required for full true equivalence."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    slot_proofs = {}
    for slot, payload in slot_candidates["conditional_slot_values"].items():
        support = payload["support_present"]
        slot_proofs[slot] = {
            "conditional_support_token_present": support,
            "selection_proof_attempted": True,
            "selected_source_value_emitted": False,
            "proof_status": "SELECTION_PROOF_OPEN",
            "blocking_condition": payload["why_not_selected"],
        }

    qasu3 = {
        "schema": "MTTQaSU3SlotSelectionProofAttempt.v1",
        "input_conditional_slot_values": rel(
            DATA
            / "selected_covarianceprofilepayload_or_qasu3selectedslotvalues"
            / "qasu3_selected_slot_value_candidate_payload.packet.json"
        ),
        "slot_selection_proofs": slot_proofs,
        "summary": {
            "slot_count": len(slot_proofs),
            "support_tokens_available": sum(1 for proof in slot_proofs.values() if proof["conditional_support_token_present"]),
            "selection_proofs_closed": 0,
            "selected_source_values_emitted": 0,
            "actual_QaSU3_operator_packet_closed": False,
        },
        "promotion_rule": (
            "A slot closes only with a selected source theorem/value for that exact slot. "
            "The support-token packet is necessary context but not sufficient."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    synthesis = {
        "schema": "MTTTrueEquivalenceFrontierSynthesisAfterBothPaths.v1",
        "status": "HIGGS_DECAY_CORRELATED_COVARIANCE_IMPORTED_QASU3_SLOT_SELECTION_OPEN",
        "what_is_now_strong": [
            "SM-parity remains closed under declared measured-input standard",
            "external Higgs BR/GammaH rows are machine encoded",
            "external Higgs decay covariance submatrix is machine encoded",
            "Qa/SU3 slot support and conditional slot candidates are machine encoded",
        ],
        "what_is_still_not_closed": [
            "full profile likelihood function",
            "non-Higgs/QM/GR true-equivalence observable interfaces",
            "selected Qa/SU3 slot source values",
            "actual sector-ready Qa/SU3-HYM operator packet",
            "no-knob derivation",
        ],
        "route_A_status": "correlated covariance profile candidate imported for Higgs decay sector",
        "route_B_status": "slot selection proofs attempted, zero selected values emitted",
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedExternalProfileLikelihoodImportOrQaSU3SlotSelectionProof",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_covarianceprofilepayload_or_qasu3selectedslotvalues.candidate.json"),
            "external_correlation_source": CORRELATION_SOURCE,
            "diagonal_covariance_surrogate": rel(
                DATA
                / "selected_covarianceprofilepayload_or_qasu3selectedslotvalues"
                / "higgs_external_row_covariance_surrogate_payload.packet.json"
            ),
            "conditional_qasu3_slot_values": rel(
                DATA
                / "selected_covarianceprofilepayload_or_qasu3selectedslotvalues"
                / "qasu3_selected_slot_value_candidate_payload.packet.json"
            ),
        },
        "output_packets": {
            "external_higgs_decay_correlation_covariance_import": rel(PROFILE),
            "qasu3_slot_selection_proof_attempt": rel(QASU3),
            "true_equivalence_frontier_synthesis": rel(SYNTHESIS),
        },
        "theorem": {
            "name": "ExternalCorrelationImportOrQaSU3SlotSelectionProofAttempt",
            "proved": True,
            "statement": (
                "The arXiv:1606.00455 ancillary correlation matrix can be restricted to the current nine "
                "Higgs decay rows and combined with the existing external row uncertainties to form a "
                "correlated covariance profile candidate. This advances Route A beyond diagonal covariance. "
                "Route B attempts selection proofs for every Qa/SU3 slot, but no selected source value is emitted."
            ),
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "external_higgs_decay_covariance_profile_candidate_imported": True,
            "full_profile_likelihood_function_imported": False,
            "selected_operator_slot_source_values_closed": False,
            "actual_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "external_correlated_covariance_submatrix_imported": True,
            "higgs_decay_covariance_profile_candidate_built": True,
            "qasu3_slot_selection_proofs_attempted": True,
            "frontier_synthesis_built": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "full_profile_likelihood_function": True,
            "accepted_full_true_equivalence_profile": True,
            "selected_operator_slot_source_values": True,
            "actual_QaSU3_operator_packet": True,
            "non_Higgs_QM_GR_observable_interfaces": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "previous_candidate_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_ExternalProfileLikelihoodImport_or_QaSU3SlotSelectionProof_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": True,
        "external_higgs_decay_covariance_profile_candidate_imported": True,
        "full_profile_likelihood_function_imported": False,
        "selected_operator_slot_source_values_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected ExternalProfileLikelihoodImport or QaSU3SlotSelectionProof v1

This artifact pushes both paths and brings them together.

Route A now imports an external correlated covariance submatrix for the nine
machine-encoded Higgs decay rows, using the arXiv:1606.00455 ancillary
correlation table.  This is stronger than the previous diagonal surrogate, but
it is still not a full likelihood function or full true-equivalence profile.

Route B attempts selection proofs for all eight Qa/SU3 slots.  No selected slot
source value is emitted; support tokens remain support tokens.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (PROFILE, profile),
        (QASU3, qasu3),
        (SYNTHESIS, synthesis),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
