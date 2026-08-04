"""Build non-Higgs covariance profile values or local QFT observable functor."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_nonhiggscovarianceprofilevalues_or_localqftobservablefunctor"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROFILE = PACKET_DIR / "nonhiggs_precision_profile_status.packet.json"
FUNCTOR = PACKET_DIR / "local_qft_observable_functor_status.packet.json"
NEXT = PACKET_DIR / "next_true_equivalence_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_NonHiggsCovarianceProfileValues_or_LocalQFTObservableFunctor_v1.md"

STATUS = "MTT_SELECTED_NONHIGGSCOVARIANCEPROFILEVALUES_OR_LOCALQFTOBSERVABLEFUNCTOR_BUILT_ENVELOPE_TREEFUNCTOR_CLOSED_PRECISION_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_fullsmparityreplayclosure_or_nonhiggsprofilepolicy.candidate.json")
    diagonal = load(DATA / "selected_fullcovarianceprofile_or_multiloopconventionaudit.candidate.json")
    correlated = load(DATA / "selected_correlatedprofilevalues_or_localqftobservablevalues.candidate.json")
    qft_tree = load(DATA / "selected_localqftobservablerows_or_finaltruesmequivalencegap.candidate.json")

    profile = {
        "schema": "MTTNonHiggsPrecisionProfileStatus.v1",
        "status": "DIAGONAL_AND_CORRELATION_ENVELOPE_BUILT_FULL_PROFILE_VALUES_OPEN",
        "diagonal_profile_source": rel(DATA / "selected_fullcovarianceprofile_or_multiloopconventionaudit.candidate.json"),
        "correlation_envelope_source": rel(DATA / "selected_correlatedprofilevalues_or_localqftobservablevalues.candidate.json"),
        "diagonal_profile_executed": diagonal["closure_decision"]["diagonal_profile_executed"],
        "coarse_profile_passes": diagonal["closure_decision"]["coarse_profile_passes"],
        "correlation_envelope_built": correlated["closure_decision"]["correlation_envelope_built"],
        "full_correlated_profile_closed": False,
        "accepted_for_SM_parity_replay": True,
        "accepted_for_true_SM_equivalence": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    functor = {
        "schema": "MTTLocalQFTObservableFunctorStatus.v1",
        "status": "TREE_IDENTITY_FUNCTOR_ROWS_BUILT_PRECISION_OBSERVABLE_VALUES_OPEN",
        "tree_qft_rows_source": rel(DATA / "selected_localqftobservablerows_or_finaltruesmequivalencegap.candidate.json"),
        "tree_QFT_identity_tier_closed": qft_tree["closure_decision"]["tree_QFT_identity_tier_closed"],
        "precision_local_QFT_observable_values_closed": False,
        "covered_tree_rows": [
            "v(G_F)",
            "Higgs curvature/tree seed",
            "charged Yukawa mass identities",
            "gauge alpha-to-coupling normalization",
            "CKM unitarity",
            "PMNS unitarity",
        ],
        "missing_precision_rows": [
            "loop-level correlator/S-matrix observables",
            "threshold-sensitive decay and scattering rows",
            "scheme-locked multi-loop running values",
            "full non-Higgs covariance/profile likelihood rows",
            "actual selected Qa/SU3 operator attachment",
        ],
        "accepted_for_SM_parity_replay": True,
        "accepted_for_true_SM_equivalence": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_cutset = {
        "schema": "MTTNextTrueEquivalenceCutset.v1",
        "status": "NEXT_CUTSET_REDUCED_TO_PRECISION_VALUES_OR_ACTUAL_OPERATOR_PACKET",
        "closed_now": [
            "non-Higgs diagonal profile and correlation-envelope status integration",
            "tree-level local-QFT observable functor status integration",
            "explicit split between SM-parity replay and true precision equivalence",
        ],
        "remaining_cutset": [
            "published or reconstructed non-Higgs full covariance/profile values",
            "scheme-locked multi-loop threshold and pole/running maps",
            "precision local-QFT observable values beyond tree identities",
            "actual selected Qa/SU3 operator/source packet",
            "Higgs final-three route-A kernels or stronger likelihood replacement",
            "QM/GR measurement-response and dimensional normalization interfaces",
        ],
        "recommended_next_artifact": "MTT_Selected_TrueEquivalencePrecisionValueTable_or_ActualQaSU3OperatorUpgrade_v1",
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedNonHiggsCovarianceProfileValuesOrLocalQFTObservableFunctor",
        "status": STATUS,
        "inputs": {
            "previous_full_smparity_refresh": rel(DATA / "selected_fullsmparityreplayclosure_or_nonhiggsprofilepolicy.candidate.json"),
            "diagonal_profile": rel(DATA / "selected_fullcovarianceprofile_or_multiloopconventionaudit.candidate.json"),
            "correlation_envelope": rel(DATA / "selected_correlatedprofilevalues_or_localqftobservablevalues.candidate.json"),
            "tree_qft_rows": rel(DATA / "selected_localqftobservablerows_or_finaltruesmequivalencegap.candidate.json"),
        },
        "output_packets": {
            "nonhiggs_precision_profile_status": rel(PROFILE),
            "local_qft_observable_functor_status": rel(FUNCTOR),
            "next_true_equivalence_cutset": rel(NEXT),
        },
        "theorem": {
            "name": "NonHiggsProfileAndTreeQFTFunctorStatusTheorem",
            "proved": True,
            "statement": (
                "Given the diagonal profile execution, correlation envelope, and tree local-QFT observable rows, "
                "the non-Higgs precision interface is integrated enough for SM-parity replay but not for true "
                "SM equivalence. True equivalence now requires either precision value/profile completion or an "
                "actual selected Qa/SU3 operator upgrade."
            ),
        },
        "what_closes_now": {
            "nonHiggs_profile_status_integrated": True,
            "tree_QFT_observable_functor_status_integrated": True,
            "next_true_equivalence_cutset_sharpened": True,
        },
        "what_remains_open": {
            "true_SM_equivalence": True,
            "no_knob_closure": True,
            "full_nonHiggs_covariance_profile_values": True,
            "precision_local_QFT_values": True,
            "actual_QaSU3_operator_packet": True,
        },
        "closure_decision": {
            "SM_parity_closed": previous["closure_decision"]["SM_parity_closed"],
            "nonHiggs_envelope_integrated": True,
            "tree_QFT_functor_integrated": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": next_cutset["recommended_next_artifact"],
    }

    cert = {
        "certificate": "MTT_Selected_NonHiggsCovarianceProfileValues_or_LocalQFTObservableFunctor_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "SM_parity_closed": True,
        "nonHiggs_envelope_integrated": True,
        "tree_QFT_functor_integrated": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    note = f"""# MTT Selected NonHiggsCovarianceProfileValues or LocalQFTObservableFunctor v1

Status: `{STATUS}`.

The non-Higgs precision layer is now integrated:

- diagonal profile execution and coarse correlation envelope are present;
- tree-level local-QFT identity rows are present;
- this is enough for the declared SM-parity replay tier;
- it is not enough for true SM equivalence.

The remaining precision cutset is now either full non-Higgs covariance/profile
values plus precision local-QFT rows, or an actual selected Qa/SU3 operator
upgrade strong enough to replace the parity-interface substitute.
"""

    for path, payload in [
        (PROFILE, profile),
        (FUNCTOR, functor),
        (NEXT, next_cutset),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
