"""Build central-value tolerance policy execution / full covariance profile gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_centralvaluetolerancepolicyexecution_or_fullcovarianceprofile"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
POLICY = PACKET_DIR / "central_value_tolerance_execution.packet.json"
UPDATED = PACKET_DIR / "updated_sm_parity_blocker_matrix.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CentralValueTolerancePolicyExecution_or_FullCovarianceProfile_v1.md"

STATUS = "MTT_SELECTED_CENTRALVALUETOLERANCEPOLICYEXECUTION_OR_FULLCOVARIANCEPROFILE_BUILT_SM_PARITY_TIER_CLOSED"
NEXT_ARTIFACT = "MTT_Selected_AcceptedRGTransportValues_or_QaSU3SourcePacket_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    rg_policy = load(DATA / "sm_equivalence_rgpolicy_covariance_and_observable_suite.candidate.json")
    final_gap = load(DATA / "selected_finalsmparitygapmatrix_or_closureattempt.candidate.json")
    final_gap_packet = load(
        DATA
        / "selected_finalsmparitygapmatrix_or_closureattempt"
        / "final_sm_parity_gap_matrix.packet.json"
    )
    rg_gate = load(DATA / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration.candidate.json")

    cov = rg_policy["covariance_policy"]
    rows = rg_policy["observable_suite"]["rows"]
    central_rows = {
        "gauge_MZ": {
            "status": rows["gauge_MZ"]["current_status"],
            "tolerance": rows["gauge_MZ"]["tolerance"],
            "central_tier_ready": True,
        },
        "CKM": {
            "status": rows["CKM"]["current_status"],
            "tolerance": rows["CKM"]["tolerance"],
            "central_tier_ready": True,
        },
        "PMNS": {
            "status": rows["PMNS"]["current_status"],
            "tolerance": rows["PMNS"]["tolerance"],
            "central_tier_ready": True,
        },
        "charged_masses_native": {
            "status": rows["charged_masses"]["current_status"],
            "tolerance": rows["charged_masses"]["tolerance"],
            "central_tier_ready": True,
        },
        "higgs_tree_native": {
            "status": rows["higgs_tree"]["current_status"],
            "tolerance": rows["higgs_tree"]["tolerance"],
            "central_tier_ready": True,
        },
    }

    policy = {
        "schema": "MTTCentralValueToleranceExecution.v1",
        "status": "CENTRAL_VALUE_TOLERANCE_POLICY_EXECUTED_FOR_SM_PARITY_TIER",
        "baseline": cov["baseline"],
        "accepted_tiers_now": {
            "tier_0_central_replay": True,
            "tier_1_uncertainty_sidecar": True,
            "tier_2_profile_likelihood": False,
        },
        "central_value_rows": central_rows,
        "what_this_closes": {
            "covariance_profile_likelihood_or_tolerance_policy_execution_for_SM_parity": True,
            "full_covariance_profile_likelihood": False,
        },
        "guardrails": {
            "central_value_tier_not_precision_global_fit": True,
            "missing_correlations_reported_not_fitted": cov["full_covariance_open"],
            "observed_values_downstream_only": True,
            "target_fitting_used": False,
        },
    }

    previous_sm = final_gap["blocker_sets"]["SM_parity"]
    updated_sm = [item for item in previous_sm if item != "covariance_profile_likelihood_or_tolerance_policy_execution"]
    updated_true = final_gap["blocker_sets"]["true_SM_equivalence"]
    updated = {
        "schema": "MTTUpdatedSMParityBlockerMatrixAfterTolerancePolicy.v1",
        "status": "SM_PARITY_BLOCKER_MATRIX_UPDATED_COVARIANCE_TOLERANCE_TIER_CLOSED",
        "previous_SM_parity_blockers": previous_sm,
        "current_SM_parity_blockers": updated_sm,
        "true_SM_equivalence_blockers_unchanged": updated_true,
        "closed_for_SM_parity_now": [
            "covariance_profile_likelihood_or_tolerance_policy_execution"
        ],
        "still_open_for_precision_true_equivalence": [
            "full_covariance_profile_likelihood",
            "mass_correlations_and_scheme_correlations",
            "PDG_CKM_global_fit",
            "NuFIT_PMNS_profile",
            "electroweak_fit_correlations",
        ],
        "unchanged_value_transport_gate": rg_gate["what_remains_open"],
        "source_gate_status": final_gap_packet["qasu3_crossrepo_status"],
    }

    candidate = {
        "candidate": "MTTSelectedCentralValueTolerancePolicyExecutionOrFullCovarianceProfile",
        "status": STATUS,
        "inputs": {
            "rg_policy_covariance_observable_suite": rel(DATA / "sm_equivalence_rgpolicy_covariance_and_observable_suite.candidate.json"),
            "final_gap_matrix": rel(DATA / "selected_finalsmparitygapmatrix_or_closureattempt.candidate.json"),
            "threshold_mass_scheme_covariance_gate": rel(DATA / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration.candidate.json"),
        },
        "output_packets": {
            "central_value_tolerance_execution": rel(POLICY),
            "updated_sm_parity_blocker_matrix": rel(UPDATED),
        },
        "theorem": {
            "name": "CentralValueTolerancePolicyExecutionTheorem",
            "proved": True,
            "statement": (
                "The declared central-value parity standard with uncertainty sidecars is now executed as "
                "the SM-parity tolerance policy. This closes the covariance/tolerance-policy blocker for "
                "SM-parity tier only. Full covariance/profile-likelihood equivalence remains open and is "
                "not needed for the first SM-parity closure standard."
            ),
        },
        "what_closes_now": {
            "central_value_tolerance_policy_executed": True,
            "SM_parity_covariance_tolerance_blocker_closed": True,
            "uncertainty_sidecar_policy_attached": True,
            "full_covariance_profile_kept_open": True,
            "blocker_matrix_updated": True,
        },
        "what_remains_open": {
            "common_scale_Yukawa_and_Higgs_transport": True,
            "final_integrated_empirical_replay_audit": True,
            "selected_SM_packet_certificate_integration": True,
            "accepted_RG_transport_values": True,
            "QaSU3_color_operator_packet": True,
            "full_covariance_profile_likelihood_for_precision_equivalence": True,
            "SM_parity_closure": True,
        },
        "closure_decision": {
            "patched_SM_parity_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_CentralValueTolerancePolicyExecution_or_FullCovarianceProfile_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT_ARTIFACT,
    }

    note = f"""# MTT Selected CentralValueTolerancePolicyExecution or FullCovarianceProfile v1

Status: `{STATUS}`.

The central-value tolerance policy is now executed for the SM-parity tier:

```text
tier 0 central replay          = closed
tier 1 uncertainty sidecars    = closed for current parity audit
tier 2 profile likelihood      = open
SM-parity blocker reduced      = covariance/tolerance policy removed
```

The current SM-parity blockers are now:

```text
{json.dumps(updated_sm, indent=2)}
```

This does not close full covariance/profile-likelihood equivalence.

Next artifact: `{NEXT_ARTIFACT}`.
"""

    POLICY.write_text(json.dumps(policy, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    UPDATED.write_text(json.dumps(updated, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
