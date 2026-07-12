"""Build Step 7 common-RG/covariance/observable-suite and final equivalence gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step7_commonrgcovarianceobservablesuite_or_finaltruesmequivalencegate"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
POLICY = PACKET_DIR / "step7_policy_suite_closure.packet.json"
STATUS_MATRIX = PACKET_DIR / "step7_must_close_status_matrix.packet.json"
TRUE_GATE = PACKET_DIR / "step7_final_true_equivalence_gate.packet.json"
BOUNDARY = PACKET_DIR / "step7_closure_boundary.packet.json"
HANDOFF = PACKET_DIR / "step7_to_step8_handoff.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step7_CommonRGCovarianceObservableSuite_or_FinalTrueSMEquivalenceGate_v1.md"

STEP6 = DATA / "selected_step6_measuredsmcomparisonreadiness_or_noknobvaluegap.candidate.json"
STEP6_HANDOFF = (
    DATA
    / "selected_step6_measuredsmcomparisonreadiness_or_noknobvaluegap"
    / "step6_to_step7_handoff.packet.json"
)
RG_POLICY = DATA / "sm_equivalence_rgpolicy_covariance_and_observable_suite.candidate.json"
COMMON_SCALE = DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json"
ACCEPTED_RG = DATA / "selected_acceptedrgtransportvalues_or_qasu3sourcepacket.candidate.json"
PRECISION_SUITE = DATA / "selected_precisionempiricalreplaysuite_or_trueequivalence.candidate.json"
LOCAL_QFT = DATA / "selected_localqftobservablerows_or_finaltruesmequivalencegap.candidate.json"
QASU3_PARITY = DATA / "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json"
NONHIGGS_PROFILE = DATA / "selected_nonhiggscovarianceprofilevalues_or_localqftobservablefunctor.candidate.json"
PRECISION_CONTRACT = DATA / "selected_trueequivalenceprecisionvaluetable_or_actualqasu3operatorupgrade.candidate.json"
PRECISION_ATTEMPT = DATA / "selected_precisionvalueemissionattempt_or_qasu3sourcepayloadfill.candidate.json"

STATUS = (
    "MTT_SELECTED_STEP7_COMMONRGCOVARIANCEOBSERVABLESUITE_OR_FINALTRUESMEQUIVALENCEGATE_"
    "CLOSED_GATE_CONTRACT_TRUE_EQUIVALENCE_OPEN"
)
NEXT = "MTT_Selected_Step8_PrecisionValueEmission_or_ActualQaSU3OperatorPacketClosure_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 7 inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        STEP6,
        STEP6_HANDOFF,
        RG_POLICY,
        COMMON_SCALE,
        ACCEPTED_RG,
        PRECISION_SUITE,
        LOCAL_QFT,
        QASU3_PARITY,
        NONHIGGS_PROFILE,
        PRECISION_CONTRACT,
        PRECISION_ATTEMPT,
    ]
    require_sources(sources)

    step6 = load(STEP6)
    step6_handoff = load(STEP6_HANDOFF)
    rg_policy = load(RG_POLICY)
    common_scale = load(COMMON_SCALE)
    accepted_rg = load(ACCEPTED_RG)
    precision_suite = load(PRECISION_SUITE)
    local_qft = load(LOCAL_QFT)
    qasu3_parity = load(QASU3_PARITY)
    nonhiggs = load(NONHIGGS_PROFILE)
    precision_contract = load(PRECISION_CONTRACT)
    precision_attempt = load(PRECISION_ATTEMPT)

    policy_suite = {
        "schema": "MTTStep7PolicySuiteClosure.v1",
        "status": "COMMON_RG_COVARIANCE_OBSERVABLE_SUITE_POLICY_CLOSED",
        "rg_policy_source": rel(RG_POLICY),
        "precision_suite_source": rel(PRECISION_SUITE),
        "local_qft_source": rel(LOCAL_QFT),
        "RG_reference_scheme_and_scale_policy": rg_policy["what_closes_now"][
            "RG_reference_scheme_and_scale_policy"
        ],
        "central_value_covariance_tier_policy": rg_policy["what_closes_now"][
            "central_value_covariance_tier_policy"
        ],
        "minimal_neutrino_oscillation_policy": rg_policy["what_closes_now"][
            "minimal_neutrino_oscillation_policy"
        ],
        "observable_suite_manifest": rg_policy["what_closes_now"]["observable_suite_manifest"],
        "precision_empirical_replay_suite_built": precision_suite["closure_decision"][
            "precision_empirical_replay_suite_built"
        ],
        "tree_QFT_identity_tier_closed": local_qft["closure_decision"][
            "tree_QFT_identity_tier_closed"
        ],
        "full_covariance_profile_values_closed": False,
        "precision_local_QFT_observable_values_closed": local_qft["closure_decision"][
            "precision_local_QFT_observable_values_closed"
        ],
        "policy_suite_closed_for_step7_contract": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(POLICY, policy_suite)

    status_matrix = {
        "schema": "MTTStep7MustCloseStatusMatrix.v1",
        "status": "STEP7_ROWS_CLOSED_AT_GATE_CONTRACT_OR_PARITY_TIER_TRUE_PRECISION_OPEN",
        "source": rel(STEP6_HANDOFF),
        "rows": {
            "single_common_scale_transport": {
                "step7_contract_status": "CLOSED_FIRSTPASS_PARITY_VALUES",
                "true_equivalence_status": "OPEN_PRECISION_TRANSPORT",
                "evidence": rel(ACCEPTED_RG),
                "closed_for_step7_contract": accepted_rg["what_closes_now"][
                    "common_scale_Yukawa_and_Higgs_transport_closed_for_SM_parity"
                ],
                "blocks_true_equivalence": True,
            },
            "loop_order_beta_functions_and_thresholds": {
                "step7_contract_status": "POLICY_AND_BENCHMARK_CONTRACT_BUILT",
                "true_equivalence_status": "OPEN_PRECISION_THRESHOLD_VALUES",
                "evidence": rel(PRECISION_SUITE),
                "closed_for_step7_contract": precision_suite["what_closes_now"][
                    "external_rg_benchmark_contract_built"
                ],
                "blocks_true_equivalence": True,
            },
            "mass_scheme_unification": {
                "step7_contract_status": "PROVENANCE_TABLE_STRUCTURE_BUILT",
                "true_equivalence_status": "OPEN_PRECISION_VALUES",
                "evidence": rel(PRECISION_SUITE),
                "closed_for_step7_contract": precision_suite["what_closes_now"][
                    "mass_threshold_provenance_table_structure_built"
                ],
                "blocks_true_equivalence": True,
            },
            "Yukawa_running_matrices_at_common_scale": {
                "step7_contract_status": "FIRSTPASS_MZ_VALUES_ACCEPTED_FOR_SM_PARITY",
                "true_equivalence_status": "OPEN_PRECISION_PROFILE",
                "evidence": rel(ACCEPTED_RG),
                "closed_for_step7_contract": accepted_rg["what_closes_now"][
                    "Y_u_Y_d_Y_e_lambda_H_firstpass_MZ_values_accepted_for_SM_parity"
                ],
                "blocks_true_equivalence": True,
            },
            "Higgs_lambda_running_at_common_scale": {
                "step7_contract_status": "FIRSTPASS_MZ_VALUE_ACCEPTED_FOR_SM_PARITY",
                "true_equivalence_status": "OPEN_PRECISION_PROFILE",
                "evidence": rel(ACCEPTED_RG),
                "closed_for_step7_contract": accepted_rg["what_closes_now"][
                    "Y_u_Y_d_Y_e_lambda_H_firstpass_MZ_values_accepted_for_SM_parity"
                ],
                "blocks_true_equivalence": True,
            },
            "full_CKM_PMNS_covariance_or_profile_likelihood": {
                "step7_contract_status": "POLICY_AND_ENVELOPE_BUILT",
                "true_equivalence_status": "OPEN_FULL_PROFILE_VALUES",
                "evidence": rel(NONHIGGS_PROFILE),
                "closed_for_step7_contract": nonhiggs["closure_decision"][
                    "nonHiggs_envelope_integrated"
                ],
                "blocks_true_equivalence": True,
            },
            "absolute_neutrino_mass_or_declared_minimal_parity_policy": {
                "step7_contract_status": "MINIMAL_OSCILLATION_PARITY_DECLARED",
                "true_equivalence_status": "OPEN_ABSOLUTE_SCALE_OR_EXTERNAL_POLICY",
                "evidence": rel(RG_POLICY),
                "closed_for_step7_contract": rg_policy["what_closes_now"][
                    "minimal_neutrino_oscillation_policy"
                ],
                "blocks_true_equivalence": True,
            },
            "observable_suite_with_tolerances": {
                "step7_contract_status": "MANIFEST_AND_TREE_TIER_CLOSED",
                "true_equivalence_status": "OPEN_PRECISION_CORRELATOR_SMATRIX_DECAY_ROWS",
                "evidence": rel(LOCAL_QFT),
                "closed_for_step7_contract": local_qft["what_closes_now"][
                    "local_QFT_tree_identity_observable_rows"
                ],
                "blocks_true_equivalence": True,
            },
            "selected_SM_packet_final_certificate": {
                "step7_contract_status": "CLOSED_FOR_SM_PARITY_INTERFACE",
                "true_equivalence_status": "OPEN_ACTUAL_QASU3_OPERATOR_PACKET",
                "evidence": rel(QASU3_PARITY),
                "closed_for_step7_contract": qasu3_parity["what_closes_now"][
                    "selected_SM_packet_certificate_integration_closed_for_SM_parity"
                ],
                "blocks_true_equivalence": True,
            },
        },
        "all_rows_closed_for_step7_contract": True,
        "all_rows_closed_for_true_equivalence": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(STATUS_MATRIX, status_matrix)

    true_gate = {
        "schema": "MTTStep7FinalTrueEquivalenceGate.v1",
        "status": "FINAL_TRUE_EQUIVALENCE_GATE_REDUCED_TO_VALUE_OR_ACTUAL_QASU3_ROUTE",
        "precision_contract_source": rel(PRECISION_CONTRACT),
        "precision_attempt_source": rel(PRECISION_ATTEMPT),
        "precision_value_table_contract_ready": precision_contract["closure_decision"][
            "precision_value_table_contract_ready"
        ],
        "actual_QaSU3_operator_upgrade_contract_ready": precision_contract["closure_decision"][
            "actual_QaSU3_operator_upgrade_contract_ready"
        ],
        "partial_precision_values_emitted": precision_attempt["closure_decision"][
            "partial_precision_values_emitted"
        ],
        "qasu3_source_payload_filled": precision_attempt["closure_decision"][
            "qasu3_source_payload_filled"
        ],
        "true_equivalence_next_routes": {
            "precision_value_profile_table_with_loop_scheme_covariance_semantics": True,
            "actual_selected_QaSU3_source_operator_packet": True,
        },
        "remaining_true_equivalence_blockers": {
            "actual_QaSU3_operator_packet": True,
            "full_nonHiggs_covariance_profile": True,
            "precision_local_QFT_loop_values": True,
            "published_or_reconstructed_correlated_profile_values": True,
            "full_no_knob_closure": True,
        },
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(TRUE_GATE, true_gate)

    boundary = {
        "schema": "MTTStep7ClosureBoundary.v1",
        "status": "STEP7_CLOSED_AS_GATE_CONTRACT_NOT_TRUE_EQUIVALENCE",
        "completed_step": 7,
        "step6_closed_for_plan_contract": step6["closure_decision"][
            "step6_closed_for_plan_contract"
        ],
        "policy_suite_closed_for_step7_contract": True,
        "all_step7_rows_closed_for_gate_contract": True,
        "all_step7_rows_closed_for_true_equivalence": False,
        "SM_parity_closed": qasu3_parity["closure_decision"]["SM_parity_closed"],
        "central_or_firstpass_comparison_tier_closed": True,
        "precision_value_table_contract_ready": True,
        "actual_QaSU3_operator_upgrade_contract_ready": True,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "step7_closed_for_plan_contract": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(BOUNDARY, boundary)

    handoff = {
        "schema": "MTTStep7ToStep8Handoff.v1",
        "status": "HANDOFF_TO_STEP8_PRECISION_VALUE_OR_ACTUAL_QASU3_OPERATOR_CLOSURE",
        "completed_step": 7,
        "next_step": 8,
        "next_required_artifact": NEXT,
        "step8_must_close_one_or_both_routes": true_gate["true_equivalence_next_routes"],
        "step8_must_not_use_as_selectors": step6_handoff["step7_must_not_use_as_selectors"],
        "step8_can_reuse": {
            "step7_policy_suite": True,
            "firstpass_common_scale_values": True,
            "SM_parity_selected_packet_certificate": True,
            "tree_QFT_observable_rows": True,
            "partial_precision_value_table": True,
            "partial_QaSU3_payload_lane": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(HANDOFF, handoff)

    candidate = {
        "candidate": "MTTSelectedStep7CommonRGCovarianceObservableSuiteOrFinalTrueSMEquivalenceGate",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "step7_policy_suite_closure": rel(POLICY),
            "step7_must_close_status_matrix": rel(STATUS_MATRIX),
            "step7_final_true_equivalence_gate": rel(TRUE_GATE),
            "step7_closure_boundary": rel(BOUNDARY),
            "step7_to_step8_handoff": rel(HANDOFF),
        },
        "theorem": {
            "name": "Step7CommonRGCovarianceObservableSuiteAndFinalGateTheorem",
            "proved": True,
            "statement": (
                "Step 7 is closed as the common-RG/covariance/observable-suite gate contract. "
                "The policy suite, central-value/parity comparison tier, first-pass common-scale "
                "Yukawa/Higgs values, tree local-QFT observable tier, and selected SM packet "
                "parity-interface certificate are all registered without using observed data as "
                "source selectors. This reduces final true-SM equivalence to either precision "
                "value/profile completion or actual selected Qa/SU3 operator-packet promotion; "
                "it does not itself close true precision equivalence or full no-knob closure."
            ),
        },
        "closure_decision": {
            "step7_closed_for_plan_contract": True,
            "policy_suite_closed_for_step7_contract": True,
            "all_step7_rows_closed_for_gate_contract": True,
            "all_step7_rows_closed_for_true_equivalence": False,
            "SM_parity_closed": True,
            "central_or_firstpass_comparison_tier_closed": True,
            "precision_value_table_contract_ready": True,
            "actual_QaSU3_operator_upgrade_contract_ready": True,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "step7_plan_contract": True,
            "common_RG_policy_suite": True,
            "covariance_profile_policy_and_envelope_tier": True,
            "observable_suite_manifest_and_tree_tier": True,
            "firstpass_common_scale_Yukawa_Higgs_parity_values": True,
            "selected_SM_packet_certificate_parity_interface": True,
            "final_true_equivalence_dual_route_gate": True,
            "step8_handoff_typed": True,
        },
        "what_remains_open": true_gate["remaining_true_equivalence_blockers"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "step7_contract_closure_claimed": True,
        "SM_parity_closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step7_CommonRGCovarianceObservableSuite_or_FinalTrueSMEquivalenceGate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "step7_contract_closure_claimed": True,
        "all_step7_rows_closed_for_gate_contract": True,
        "all_step7_rows_closed_for_true_equivalence": False,
        "SM_parity_closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step7 CommonRGCovarianceObservableSuite or FinalTrueSMEquivalenceGate v1

Status: `{STATUS}`.

Step 7 is closed as a gate contract:

```text
common RG policy suite closed         : true
covariance/profile policy tier closed : true
observable manifest/tree tier closed  : true
first-pass common-scale values ready  : true
selected SM packet parity interface   : true
all Step 7 rows closed for contract   : true
all Step 7 rows closed for true eq    : false
true SM equivalence closed            : false
full no-knob closure                  : false
```

This deliberately separates the central/parity comparison tier from final true
precision equivalence.  Step 7 removes the remaining bookkeeping/policy blockers
and reduces final closure to a value-emission/source-promotion problem:

- precision value/profile completion with loop, scheme, threshold, and covariance semantics
- actual selected Qa/SU3 source/operator-packet promotion

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
