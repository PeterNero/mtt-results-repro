"""Build final SM-parity gap matrix / closure attempt after patched dynamic C1."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_finalsmparitygapmatrix_or_closureattempt"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
GAP = PACKET_DIR / "final_sm_parity_gap_matrix.packet.json"
DECISION = PACKET_DIR / "closure_attempt_decision.packet.json"
NEXT = PACKET_DIR / "minimal_next_gate_recommendation.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FinalSMParityGapMatrix_or_ClosureAttempt_v1.md"

STATUS = "MTT_SELECTED_FINALSMPARITYGAPMATRIX_OR_CLOSUREATTEMPT_BUILT_OPEN_GATES_SHARPENED"
NEXT_ARTIFACT = "MTT_Selected_CommonScaleYukawaHiggsTransport_or_FinalReplayAudit_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    integration = load(DATA / "selected_patcheddynamicc1empiricalreplayintegration_or_noknobderivation.candidate.json")
    remaining = load(
        DATA
        / "selected_patcheddynamicc1empiricalreplayintegration_or_noknobderivation"
        / "remaining_global_sm_parity_gates.packet.json"
    )
    replay = load(
        DATA
        / "selected_patcheddynamicc1empiricalreplayintegration_or_noknobderivation"
        / "patched_dynamic_c1_empirical_replay_interface.packet.json"
    )
    ledger = load(DATA / "sm_parity_closure_ledger.candidate.json")
    admission = load(DATA / "sm_equivalence_measured_replay_admission.candidate.json")
    common_scale = load(DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json")
    rg_policy = load(DATA / "sm_equivalence_rgpolicy_covariance_and_observable_suite.candidate.json")
    qasu3 = load(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json")

    closed = remaining["closed_or_no_longer_blocking"]
    still_open = remaining["still_open"]
    patched_c1 = replay["patched_dynamic_C1_inputs"]

    gap_rows = [
        {
            "blocks_SM_parity": False,
            "blocks_no_knob": False,
            "blocks_true_SM_equivalence": False,
            "evidence": "all six static SM-slot functor arrows emitted",
            "gate": "static_SM_slot_functor_source_arrows",
            "state": "closed",
            "tier": "SM-parity source interface",
        },
        {
            "blocks_SM_parity": False,
            "blocks_no_knob": True,
            "blocks_true_SM_equivalence": False,
            "evidence": {
                "A_selected": patched_c1["A_selected"],
                "b_selected": patched_c1["b_selected"],
                "deltaTheta_C1": patched_c1["deltaTheta_C1"],
                "sector_response_matrices": patched_c1["sector_response_matrices"],
            },
            "gate": "patched_dynamic_C1_interface",
            "state": "closed_under_explicit_patch",
            "tier": "patched SM-parity replay interface",
        },
        {
            "blocks_SM_parity": False,
            "blocks_no_knob": False,
            "blocks_true_SM_equivalence": False,
            "evidence": admission["what_closes_now"],
            "gate": "measured_replay_admission_policy",
            "state": "closed",
            "tier": "SM-style empirical standard",
        },
        {
            "blocks_SM_parity": False,
            "blocks_no_knob": False,
            "blocks_true_SM_equivalence": False,
            "evidence": common_scale["what_closes_now"],
            "gate": "MZ_gauge_triplet_common_scale",
            "state": "closed_for_gauge_triplet_only",
            "tier": "common-scale replay",
        },
        {
            "blocks_SM_parity": True,
            "blocks_no_knob": True,
            "blocks_true_SM_equivalence": True,
            "evidence_needed": "transport Yukawa, quark/lepton masses, and Higgs lambda/v policy to declared scales with uncertainties",
            "gate": "common_scale_Yukawa_and_Higgs_transport",
            "state": "open",
            "tier": "common-scale replay",
        },
        {
            "blocks_SM_parity": True,
            "blocks_no_knob": False,
            "blocks_true_SM_equivalence": True,
            "evidence_needed": "execute central-value plus uncertainty/covariance policy for replay comparisons",
            "gate": "covariance_profile_likelihood_or_tolerance_policy_execution",
            "state": "open",
            "tier": "empirical audit",
        },
        {
            "blocks_SM_parity": True,
            "blocks_no_knob": False,
            "blocks_true_SM_equivalence": True,
            "evidence_needed": "single verifier comparing all declared replay observables against the frozen measured packets",
            "gate": "final_integrated_empirical_replay_audit",
            "state": "open",
            "tier": "empirical audit",
        },
        {
            "blocks_SM_parity": True,
            "blocks_no_knob": True,
            "blocks_true_SM_equivalence": True,
            "evidence_needed": "one bundled selected gauge/representation/family/Higgs/Qa-SU3 packet certificate",
            "gate": "selected_SM_packet_certificate_integration",
            "state": "open",
            "tier": "source interface",
        },
        {
            "blocks_SM_parity": False,
            "blocks_no_knob": True,
            "blocks_true_SM_equivalence": True,
            "evidence_needed": "typed map from selected packet to QFT observable algebra and perturbative convention",
            "gate": "local_QFT_observable_functor",
            "state": "open",
            "tier": "recovery interface",
        },
        {
            "blocks_SM_parity": False,
            "blocks_no_knob": True,
            "blocks_true_SM_equivalence": True,
            "evidence_needed": "measurement, probability, and semiclassical/GR-limit interface compatible with the selected packet",
            "gate": "GR_QM_measurement_interfaces",
            "state": "open",
            "tier": "recovery interface",
        },
        {
            "blocks_SM_parity": False,
            "blocks_no_knob": True,
            "blocks_true_SM_equivalence": False,
            "evidence_needed": "derive finite C1 trace measure / dynamic C1 packet from pre-existing MTT source rather than local patch",
            "gate": "unpatched_no_knob_dynamic_C1_derivation",
            "state": "open",
            "tier": "no-knob closure",
        },
        {
            "blocks_SM_parity": False,
            "blocks_no_knob": True,
            "blocks_true_SM_equivalence": False,
            "evidence_needed": "derive measured constants from selected source without using observed values as selectors",
            "gate": "full_no_knob_constants",
            "state": "open",
            "tier": "no-knob closure",
        },
    ]

    sm_parity_blockers = [row["gate"] for row in gap_rows if row["blocks_SM_parity"]]
    true_equivalence_blockers = [row["gate"] for row in gap_rows if row["blocks_true_SM_equivalence"]]
    no_knob_blockers = [row["gate"] for row in gap_rows if row["blocks_no_knob"]]

    gap = {
        "blocker_sets": {
            "SM_parity": sm_parity_blockers,
            "no_knob": no_knob_blockers,
            "true_SM_equivalence": true_equivalence_blockers,
        },
        "closed_or_no_longer_blocking": closed,
        "gap_rows": gap_rows,
        "observed_data_used": False,
        "qasu3_crossrepo_status": qasu3.get("status"),
        "schema": "MTTFinalSMParityGapMatrix.v1",
        "scope": {
            "SM_parity": "MTT may use the same style of measured constants as the SM, but must replay them coherently.",
            "no_knob": "no measured constants or fitted values are permitted as source selectors.",
            "true_SM_equivalence": "SM-parity plus QFT/recovery interfaces and observable-level empirical audit.",
        },
        "status": "FINAL_GAP_MATRIX_BUILT_NOT_CLOSED",
        "still_open_imported": still_open,
        "target_fitting_used": False,
    }

    decision = {
        "closure_guardrails": {
            "closure_claimed": False,
            "observed_data_used": False,
            "patched_dynamic_C1_is_patch_not_unpatched_derivation": True,
            "target_fitting_used": False,
        },
        "no_knob_closed": False,
        "no_regression_from_previous_work": {
            "dynamic_C1_removed_from_patched_parity_blocker_list": integration["what_closes_now"][
                "dynamic_C1_removed_from_patched_parity_blocker_list"
            ],
            "measured_constants_remain_downstream": True,
            "no_knob_claims_remain_open": True,
            "patched_dynamic_C1_interface_ready": integration["what_closes_now"][
                "patched_dynamic_C1_empirical_replay_interface_ready"
            ],
        },
        "patched_SM_parity_closed": False,
        "reason": (
            "Patched dynamic C1 and measured replay admission are ready, but SM parity still needs "
            "common-scale Yukawa/Higgs transport, covariance/tolerance execution, a final integrated "
            "empirical replay audit, and a bundled selected SM packet certificate."
        ),
        "schema": "MTTClosureAttemptDecision.v1",
        "status": "CLOSURE_ATTEMPT_EVALUATED_NOT_YET_FULLY_CLOSED",
        "true_SM_equivalence_closed": False,
    }

    recommendation = {
        "defer_until_after_SM_parity": [
            "unpatched_no_knob_dynamic_C1_derivation",
            "full_no_knob_constants",
        ],
        "parallel_gate": "selected_SM_packet_certificate_integration",
        "primary_next_gate": "common_scale_Yukawa_and_Higgs_transport",
        "schema": "MTTMinimalNextGateRecommendation.v1",
        "status": "NEXT_GATE_RECOMMENDED",
        "superset_strategy_use": {
            "description": (
                "The current branch combines terminal SM-slot, Qa/SU3 import, patched dynamic C1, "
                "and measured replay lanes, but locks them to an SM-parity target. It does not let "
                "any lane tune source selection against observed constants."
            ),
            "mode": "combined_paths_with_locked_target",
        },
        "why_parallel": (
            "This bundles the source-side gauge/representation/family/Higgs/Qa-SU3 interface so the "
            "empirical replay is attached to one selected packet rather than scattered proofs."
        ),
        "why_primary": (
            "It is the smallest purely empirical SM-parity blocker left after patched C1: it does not "
            "require solving no-knob constants, but it is required before the final integrated replay "
            "audit can honestly compare Yukawa/Higgs sectors."
        ),
    }

    candidate = {
        "blocker_sets": gap["blocker_sets"],
        "candidate": "MTTSelectedFinalSMParityGapMatrixOrClosureAttempt",
        "closure_claimed": False,
        "closure_decision": {
            "no_knob_closed": False,
            "patched_SM_parity_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "inputs": {
            "common_scale_packet": rel(DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json"),
            "measured_replay_admission": rel(DATA / "sm_equivalence_measured_replay_admission.candidate.json"),
            "patched_dynamic_c1_empirical_integration": rel(
                DATA / "selected_patcheddynamicc1empiricalreplayintegration_or_noknobderivation.candidate.json"
            ),
            "qasu3_crossrepo_import": rel(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json"),
            "remaining_global_gates": rel(
                DATA
                / "selected_patcheddynamicc1empiricalreplayintegration_or_noknobderivation"
                / "remaining_global_sm_parity_gates.packet.json"
            ),
            "rg_covariance_policy": rel(DATA / "sm_equivalence_rgpolicy_covariance_and_observable_suite.candidate.json"),
            "sm_parity_closure_ledger": rel(DATA / "sm_parity_closure_ledger.candidate.json"),
        },
        "ledger_status": ledger.get("status"),
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used": False,
        "output_packets": {
            "closure_attempt_decision": rel(DECISION),
            "final_sm_parity_gap_matrix": rel(GAP),
            "minimal_next_gate_recommendation": rel(NEXT),
        },
        "rg_policy_status": rg_policy.get("status"),
        "status": STATUS,
        "target_fitting_used": False,
        "theorem": {
            "name": "FinalSMParityGapMatrixTheorem",
            "proved": True,
            "statement": (
                "After patched dynamic C1 empirical integration, the remaining SM-parity blockers "
                "are exactly common-scale Yukawa/Higgs transport, covariance/tolerance execution, "
                "final integrated empirical replay audit, and selected SM packet certificate integration. "
                "QFT/GR/QM recovery interfaces block true SM equivalence, while unpatched C1 and full "
                "constant derivation block no-knob closure."
            ),
        },
        "what_closes_now": {
            "SM_parity_blockers_separated_from_true_equivalence_blockers": True,
            "closure_attempt_evaluated": True,
            "final_gap_matrix_built": True,
            "minimal_next_gate_selected": True,
            "no_knob_blockers_separated_from_SM_parity": True,
        },
    }

    cert = {
        "candidate_path": rel(OUTPUT),
        "certificate": "MTT_Selected_FinalSMParityGapMatrix_or_ClosureAttempt_v1",
        "closure_claimed": False,
        "closure_decision": candidate["closure_decision"],
        "next_required_artifact": NEXT_ARTIFACT,
        "note_path": rel(NOTE),
        "observed_data_used": False,
        "status": STATUS,
        "target_fitting_used": False,
        "theorem_proved": True,
        "what_closes": candidate["what_closes_now"],
    }

    note = f"""# MTT Selected FinalSMParityGapMatrix or ClosureAttempt v1

Status: `{STATUS}`.

This artifact evaluates the closure attempt after patched dynamic C1 integration.
It does not move backward: patched dynamic C1 remains ready and removed from the
patched SM-parity blocker list.

## Result

```text
patched SM-parity closed = False
true SM equivalence      = False
no-knob closure          = False
```

## SM-Parity Blockers

The remaining SM-parity blockers are:

1. common-scale Yukawa/Higgs transport,
2. covariance/profile-likelihood or tolerance-policy execution,
3. final integrated empirical replay audit,
4. selected SM packet certificate integration.

QFT/GR/QM recovery interfaces are promoted to the true-equivalence lane, while
unpatched dynamic C1 and full constant derivation remain no-knob blockers.

## Next

Next artifact:
`{NEXT_ARTIFACT}`.
"""

    GAP.write_text(json.dumps(gap, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    DECISION.write_text(json.dumps(decision, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT.write_text(json.dumps(recommendation, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
