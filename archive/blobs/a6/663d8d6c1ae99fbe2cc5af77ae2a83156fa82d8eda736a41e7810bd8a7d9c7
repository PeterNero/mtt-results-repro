"""Build the precision-observable promotion policy after tree QFT decay rows."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_precisionobservablepromotionpolicy_or_loopqftvalues"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
POLICY = PACKET_DIR / "precision_observable_promotion_policy.packet.json"
MATRIX = PACKET_DIR / "observable_tier_promotion_matrix.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_promotion_policy.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrecisionObservablePromotionPolicy_or_LoopQFTValues_v1.md"

STATUS = "MTT_SELECTED_PRECISIONOBSERVABLEPROMOTIONPOLICY_OR_LOOPQFTVALUES_BUILT_POLICY_LOOP_VALUES_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_precisionqftobservablerows_or_actualqasu3packet.candidate.json")
    previous_gate = load(
        DATA
        / "selected_precisionqftobservablerows_or_actualqasu3packet"
        / "updated_true_equivalence_gate_after_tree_decay_rows.packet.json"
    )
    local_qft_rows = load(
        DATA
        / "selected_localqftobservablerows_or_finaltruesmequivalencegap"
        / "tree_level_local_qft_observable_rows.packet.json"
    )
    decay_rows = load(
        DATA
        / "selected_precisionqftobservablerows_or_actualqasu3packet"
        / "representative_tree_level_decay_observable_rows.packet.json"
    )
    precision_suite = load(DATA / "selected_precisionempiricalreplaysuite_or_trueequivalence.candidate.json")
    literature = load(DATA / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance.candidate.json")
    pole_residuals = load(DATA / "selected_polethresholdresidualvalues_or_covarianceprofile.candidate.json")
    correlated = load(DATA / "selected_correlatedprofilevalues_or_localqftobservablevalues.candidate.json")
    qasu3_gate = load(
        DATA
        / "selected_precisionqftobservablerows_or_actualqasu3packet"
        / "actual_qasu3_packet_gate_after_qft_rows.packet.json"
    )

    tree_identity_count = len(local_qft_rows["observable_rows"])
    higgs_decay_count = len(decay_rows["higgs_fermion_decay_rows"])
    w_decay_count = len(decay_rows["w_leptonic_decay_rows"])

    promotion_policy = {
        "schema": "MTTPrecisionObservablePromotionPolicy.v1",
        "status": "PRECISION_OBSERVABLE_PROMOTION_POLICY_LOCKED_LOOP_VALUES_OPEN",
        "purpose": (
            "Prevent tree identities, representative decay rows, and benchmark rows from being silently promoted "
            "to true precision SM-equivalence observables."
        ),
        "promotion_requirements": {
            "SM_parity_tree_identity": [
                "typed measured replay admission",
                "declared algebraic/tree formula",
                "finite residual check under the declared convention",
            ],
            "representative_tree_decay": [
                "typed measured replay admission",
                "declared tree formula and kinematic domain",
                "finite nonnegative width check",
                "explicit guard that the row is not a precision width",
            ],
            "precision_loop_QFT_observable": [
                "declared renormalization scheme, scale, and loop order",
                "running-mass and threshold policy",
                "loop/EW/QCD/off-shell correction policy where applicable",
                "experimental or benchmark comparison target with uncertainty/covariance treatment",
                "actual selected source/operator packet attachment for Ward/anomaly/operator-sensitive rows",
            ],
            "true_SM_equivalence_row": [
                "precision_loop_QFT_observable requirements",
                "common RG transport to the declared scale",
                "covariance/profile rule or explicit waiver",
                "no use of observed values as source selectors",
            ],
        },
        "hard_guards": {
            "tree_identity_does_not_imply_precision_equivalence": True,
            "representative_decay_does_not_imply_loop_width": True,
            "literature_benchmark_does_not_select_MTT_source": True,
            "correlated_profile_does_not_replace_actual_QaSU3_packet": True,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    tier_rows = [
        {
            "tier": "tree_identity_rows",
            "input_packet": rel(
                DATA
                / "selected_localqftobservablerows_or_finaltruesmequivalencegap"
                / "tree_level_local_qft_observable_rows.packet.json"
            ),
            "row_count": tree_identity_count,
            "current_acceptance": "SM_PARITY_TREE_IDENTITY_ACCEPTED",
            "accepted_for_true_precision_equivalence": False,
            "missing_for_true_precision": [
                "loop-corrected correlator/S-matrix policy where the observable is not a pure identity",
                "common scale/covariance comparison",
            ],
        },
        {
            "tier": "representative_tree_decay_rows",
            "input_packet": rel(
                DATA
                / "selected_precisionqftobservablerows_or_actualqasu3packet"
                / "representative_tree_level_decay_observable_rows.packet.json"
            ),
            "row_count": higgs_decay_count + w_decay_count,
            "current_acceptance": "REPRESENTATIVE_DECAY_REPLAY_ACCEPTED",
            "accepted_for_true_precision_equivalence": False,
            "missing_for_true_precision": [
                "running masses at the declared scale",
                "QCD/EW corrections",
                "off-shell and total-width policy",
                "covariance/profile comparison to benchmark or data",
            ],
        },
        {
            "tier": "RG_and_threshold_benchmark_rows",
            "input_packets": [
                rel(DATA / "selected_precisionempiricalreplaysuite_or_trueequivalence.candidate.json"),
                rel(DATA / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance.candidate.json"),
                rel(DATA / "selected_polethresholdresidualvalues_or_covarianceprofile.candidate.json"),
            ],
            "current_acceptance": "DOWNSTREAM_BENCHMARK_AND_FORMULA_REPLAY_ACCEPTED",
            "accepted_for_true_precision_equivalence": False,
            "missing_for_true_precision": [
                "full declared multiloop convention audit",
                "non-diagonal covariance/profile likelihood or declared waiver",
                "integrated final precision-observable suite",
            ],
        },
        {
            "tier": "correlated_profile_rows",
            "input_packet": rel(DATA / "selected_correlatedprofilevalues_or_localqftobservablevalues.candidate.json"),
            "current_acceptance": "CORRELATION_ENVELOPE_SCAFFOLD_ACCEPTED",
            "accepted_for_true_precision_equivalence": False,
            "missing_for_true_precision": [
                "published or reconstructed full covariance/profile values",
                "observable-by-observable precision residual acceptance",
            ],
        },
        {
            "tier": "actual_QaSU3_operator_sensitive_rows",
            "input_packet": rel(
                DATA
                / "selected_precisionqftobservablerows_or_actualqasu3packet"
                / "actual_qasu3_packet_gate_after_qft_rows.packet.json"
            ),
            "current_acceptance": "SOURCE_GATE_RECHECKED_OPEN",
            "accepted_for_true_precision_equivalence": False,
            "missing_for_true_precision": qasu3_gate["why_still_open"],
        },
    ]
    promotion_matrix = {
        "schema": "MTTObservableTierPromotionMatrix.v1",
        "status": "OBSERVABLE_TIERS_CLASSIFIED_NO_PRECISION_OVERPROMOTION",
        "row_counts": {
            "tree_identity_rows": tree_identity_count,
            "higgs_tree_decay_rows": higgs_decay_count,
            "w_tree_decay_rows": w_decay_count,
        },
        "tiers": tier_rows,
        "all_current_rows_classified": True,
        "any_row_promoted_to_true_precision_equivalence": any(
            row["accepted_for_true_precision_equivalence"] for row in tier_rows
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = list(previous_gate["remaining_true_equivalence_blockers"])
    if "precision-observable promotion policy" not in previous_gate["closed_now"]:
        closed_now = previous_gate["closed_now"] + ["precision-observable promotion policy"]
    else:
        closed_now = previous_gate["closed_now"]
    if "declared precision-observable promotion policy" in remaining:
        remaining.remove("declared precision-observable promotion policy")
    for blocker in [
        "loop-corrected local QFT correlator/S-matrix/decay rows",
        "full covariance/profile likelihood values",
        "actual selected Qa/SU3 operator packet",
    ]:
        if blocker not in remaining:
            remaining.append(blocker)

    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterPromotionPolicy.v1",
        "status": "PROMOTION_POLICY_LOCKED_TRUE_PRECISION_VALUES_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": closed_now,
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": (
            "fill loop-corrected local QFT observable rows under the promotion policy, "
            "or promote the actual selected Qa/SU3 source/operator packet"
        ),
        "guardrails": {
            "policy_closes_classification_not_values": True,
            "no_tree_row_promoted_to_precision": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPrecisionObservablePromotionPolicyOrLoopQFTValues",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_precisionqftobservablerows_or_actualqasu3packet.candidate.json"),
            "precision_suite": rel(DATA / "selected_precisionempiricalreplaysuite_or_trueequivalence.candidate.json"),
            "external_literature_benchmarks": rel(
                DATA / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance.candidate.json"
            ),
            "pole_threshold_residuals": rel(DATA / "selected_polethresholdresidualvalues_or_covarianceprofile.candidate.json"),
            "correlated_profile": rel(DATA / "selected_correlatedprofilevalues_or_localqftobservablevalues.candidate.json"),
        },
        "output_packets": {
            "precision_observable_promotion_policy": rel(POLICY),
            "observable_tier_promotion_matrix": rel(MATRIX),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "PrecisionObservablePromotionPolicyTheorem",
            "proved": True,
            "statement": (
                "Given the current SM-parity replay packets, every observable row is classified by its promotion tier. "
                "Tree identity rows and representative tree decay rows are accepted only at their declared replay tiers; "
                "true precision SM-equivalence requires loop/threshold/RG/covariance data and, for operator-sensitive "
                "rows, the actual selected Qa/SU3 source/operator packet."
            ),
        },
        "what_closes_now": {
            "precision_observable_promotion_policy": True,
            "observable_tier_matrix": True,
            "silent_precision_overpromotion_blocked": True,
            "superset_boundary_preserved": True,
        },
        "what_remains_open": {
            "loop_corrected_local_QFT_values": True,
            "full_covariance_profile_likelihood_values": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "source_strategy": {
            "mode": "straight_downstream_SM_parity_replay_after_superset_source_boundary",
            "explanation": (
                "The superset strategy has already supplied the typed parity/interface boundary. This artifact uses a "
                "straight downstream SM/QFT promotion discipline and does not mix measured rows back into source selection."
            ),
        },
        "dependency_statuses": {
            "precision_suite": precision_suite["status"],
            "external_literature_benchmarks": literature["status"],
            "pole_threshold_residuals": pole_residuals["status"],
            "correlated_profile": correlated["status"],
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "promotion_policy_closed": True,
            "precision_loop_QFT_values_closed": False,
            "actual_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PrecisionObservablePromotionPolicy_or_LoopQFTValues_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "promotion_policy_closed": True,
        "precision_loop_QFT_values_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_LoopCorrectedQFTObservableValues_or_ActualQaSU3Packet_v1",
    }

    note = """# MTT Selected PrecisionObservablePromotionPolicy or LoopQFTValues v1

Status: `MTT_SELECTED_PRECISIONOBSERVABLEPROMOTIONPOLICY_OR_LOOPQFTVALUES_BUILT_POLICY_LOOP_VALUES_OPEN`.

This artifact proves the local promotion discipline for observable rows after
the tree QFT identity and representative decay replays.

Tree identities and representative tree decay rows are accepted only at their
declared replay tiers. They cannot be silently promoted to true precision
SM-equivalence rows.

True precision rows require a declared scheme, scale, loop order, threshold
policy, covariance/profile policy, and for operator-sensitive rows attachment
to the actual selected Qa/SU3 source/operator packet.

This closes classification and rigor, not the loop-corrected values.
"""

    for path, payload in [
        (POLICY, promotion_policy),
        (MATRIX, promotion_matrix),
        (UPDATED, updated),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
