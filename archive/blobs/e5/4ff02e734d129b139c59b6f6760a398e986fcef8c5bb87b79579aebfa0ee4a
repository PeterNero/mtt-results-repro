from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PREV = (
    ROOT
    / "certificates"
    / "post_alpha_independent_long_minimizer_trace_c1_payload_theorem_or_quadrature_table_values_certificate.json"
)
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"
SM_CERT = (
    SM_ROOT
    / "certificates"
    / "selected_i10_payloadcertificate_or_independentquadraturevaluesfill_certificate.json"
)
SM_CANDIDATE = (
    SM_ROOT
    / "candidate_data"
    / "selected_i10_payloadcertificate_or_independentquadraturevaluesfill.candidate.json"
)
SM_PACKET_DIR = SM_ROOT / "candidate_data" / "selected_i10_payloadcertificate_or_independentquadraturevaluesfill"
SM_ROUTE_A = SM_PACKET_DIR / "route_a_i10_payload_certificate_fill_attempt.packet.json"
SM_ROUTE_B = SM_PACKET_DIR / "route_b_independent_quadrature_values_fill_attempt.packet.json"
SM_CUTSET = SM_PACKET_DIR / "minimal_next_cutset.packet.json"

OUT_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_independent_long_i10_payload_certificate_or_independent_quadrature_values_fill_certificate.json"
)
OUT_PACKET = (
    ROOT
    / "candidate_data"
    / "post_alpha_independent_long_i10_payload_certificate_or_independent_quadrature_values_fill.packet.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "PostAlpha_IndependentLongI10PayloadCertificate_or_IndependentQuadratureValuesFill_Import_v1.md"
)

STATUS = (
    "POST_ALPHA_INDEPENDENT_LONG_I10_PAYLOAD_CERTIFICATE_OR_INDEPENDENT_QUADRATURE_VALUES_FILL_"
    "REANCHORED_CUTSET_OPEN"
)
PREV_STATUS = (
    "POST_ALPHA_INDEPENDENT_LONG_MINIMIZER_TRACE_C1_PAYLOAD_THEOREM_OR_QUADRATURE_TABLE_VALUES_"
    "REANCHORED_CONTRACT_OPEN"
)
THIS_ARTIFACT = "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1"
NEXT = "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source_cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    route_a = load(SM_ROUTE_A)
    route_b = load(SM_ROUTE_B)
    cutset = load(SM_CUTSET)

    prev_ok = all(
        [
            prev["status"] == PREV_STATUS,
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["unpatched_theorem_closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_I10_payload_certificate_or_independent_quadrature_values_fill"]
            is True,
            prev["frontier_decision"]["next_required_artifact"] == THIS_ARTIFACT,
            all(prev["what_closes_now"].values()),
            all(prev["what_remains_open"].values()),
            all(prev["guardrails"].values()),
        ]
    )

    source_ok = all(
        [
            source_cert["certificate"] == THIS_ARTIFACT,
            source_cert["theorem_proved"] is True,
            source_cert["closure_claimed"] is False,
            source_cert["unpatched_theorem_closure_claimed"] is False,
            source_cert["status"] == "MTT_SELECTED_I10_PAYLOAD_OR_QUADRATURE_VALUES_FILL_ATTEMPT_BUILT_CUTSET_OPEN",
            source_cert["route_A_accepted"] is False,
            source_cert["route_B_accepted"] is False,
            source_cert["next_required_artifact"] == NEXT,
            all(source_cert["what_closes"].values()),
            all(source_cert["what_remains_open"].values()),
            source_cert["observed_data_used"] is False,
            source_cert["target_fitting_used"] is False,
            candidate["status"] == "MTT_SELECTED_I10_PAYLOAD_OR_QUADRATURE_VALUES_FILL_ATTEMPT_BUILT_CUTSET_OPEN",
            candidate["theorem"]["name"] == "I10PayloadFillAttemptCutsetTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["closure_claimed"] is False,
            candidate["unpatched_theorem_closure_claimed"] is False,
            candidate["promotion_decision"]["route_A_i10_payload_certificate_accepted"] is False,
            candidate["promotion_decision"]["route_B_independent_quadrature_values_accepted"] is False,
            candidate["next_required_artifact"] == NEXT,
            candidate["observed_data_used"] is False,
            candidate["target_fitting_used"] is False,
            all(candidate["what_closes_now"].values()),
            all(candidate["what_remains_open"].values()),
            all(value is False for value in candidate["promotion_decision"].values()),
            candidate["replay_if_route_A_or_B_accepted"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            candidate["replay_if_route_A_or_B_accepted"]["A_transpose_b"] == [12.0, 12.0],
            candidate["replay_if_route_A_or_B_accepted"]["deltaTheta_C1"] == [1.0, 1.0],
        ]
    )

    route_a_ok = all(
        [
            route_a["schema"] == "MTTRouteAI10PayloadCertificateFillAttempt.v1",
            route_a["status"] == "ATTEMPTED_NOT_ACCEPTED_SELECTED_PAYLOADS_OPEN",
            route_a["accepted_now"] is False,
            route_a["payload_checks"]["no_observed_data_as_selector"]["value"] is True,
            route_a["payload_checks"]["selected_minimizer_trace_payload_verified"]["value"] is False,
            route_a["payload_checks"]["selected_c1_response_payload_verified"]["value"] is False,
            route_a["payload_checks"]["defect_functional_minimizer_payload_verified"]["value"] is False,
            route_a["observed_data_used"] is False,
            route_a["target_fitting_used"] is False,
        ]
    )

    route_b_ok = all(
        [
            route_b["schema"] == "MTTRouteBIndependentQuadratureValuesFillAttempt.v1",
            route_b["status"] == "ATTEMPTED_VALUES_EMPTY_NOT_ACCEPTED",
            route_b["accepted_now"] is False,
            route_b["acceptance_checks"]["no_patched_replay_copying"] is True,
            route_b["table_counts"]["zero_mode_basis_rows"] == 0,
            route_b["table_counts"]["primitive_contraction_rows"] == 0,
            route_b["table_counts"]["hessian_source_rows"] == 0,
            route_b["table_counts"]["sector_matrix_rows"] == 0,
            len(route_b["why_values_not_filled"]) == 4,
            route_b["observed_data_used"] is False,
            route_b["target_fitting_used"] is False,
        ]
    )

    cutset_ok = all(
        [
            cutset["schema"] == "MTTI10PayloadMinimalCutset.v1",
            cutset["status"] == "NEXT_CUTSET_SELECTED",
            cutset["recommended_next"]["artifact"] == NEXT,
            len(cutset["route_A_minimal_cutset"]) == 3,
            len(cutset["route_B_minimal_cutset"]) == 4,
            cutset["recommended_next"]["superset_strategy"]["locked_target"]["A_transpose_A"]
            == [[12.0, 0.0], [0.0, 12.0]],
            cutset["recommended_next"]["superset_strategy"]["locked_target"]["A_transpose_b"] == [12.0, 12.0],
            cutset["recommended_next"]["superset_strategy"]["locked_target"]["deltaTheta_C1"] == [1.0, 1.0],
        ]
    )

    what_closes_now = {
        "fresh_long_payload_contract_gate_consumed": prev_ok,
        "audited_I10_fill_attempt_bridged": source_ok,
        "route_A_payload_attempt_evaluated_not_accepted": route_a_ok,
        "route_B_quadrature_attempt_evaluated_empty_not_accepted": route_b_ok,
        "minimal_next_cutset_selected": cutset_ok,
    }

    what_remains_open = {
        "selected_minimizer_trace_payload_verified": True,
        "selected_c1_response_payload_verified": True,
        "defect_functional_minimizer_payload_verified": True,
        "zero_mode_basis_rows_filled": True,
        "primitive_contraction_rows_filled": True,
        "hessian_source_rows_filled": True,
        "sector_matrix_rows_filled": True,
        "unpatched_SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "does_not_claim_I10_proved": True,
        "does_not_claim_route_A_accepted": True,
        "does_not_claim_route_B_accepted": True,
        "does_not_promote_replay_A_b_or_deltaTheta_as_selected_values": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_unpatched_SM_or_true_SM_closure": True,
    }

    theorem = {
        "name": "PostAlphaIndependentLongI10PayloadCertificateOrIndependentQuadratureValuesFillBridge",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "The fresh long-chain branch imports the I10 payload and independent quadrature "
            "fill attempt. Route A is rejected because the selected minimizer trace, C1 "
            "response, and defect-functional minimizer payloads remain unverified. Route B "
            "is rejected because independent quadrature tables are empty. The next frontier "
            "is Strominger trace/C1 first variation or a quadrature execution plan."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "fresh_previous_certificate": prev,
        "source_cutset_certificate": source_cert,
        "route_a_i10_payload_certificate_fill_attempt": route_a,
        "route_b_independent_quadrature_values_fill_attempt": route_b,
        "minimal_next_cutset": cutset,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "route_A_rejected_at_this_gate": True,
            "route_B_rejected_at_this_gate": True,
            "frontier_is_strominger_trace_c1_first_variation_or_quadrature_execution_plan": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "fresh_previous_certificate": str(PREV),
            "source_cutset_certificate": str(SM_CERT),
            "source_candidate": str(SM_CANDIDATE),
            "source_route_a_packet": str(SM_ROUTE_A),
            "source_route_b_packet": str(SM_ROUTE_B),
            "source_minimal_cutset_packet": str(SM_CUTSET),
        },
    }

    note = f"""# PostAlpha IndependentLongI10PayloadCertificate or IndependentQuadratureValuesFill Import v1

## Result

Both closure routes were evaluated on the fresh long-chain branch and remain open.

Route A rejected here:

```text
selected minimizer trace payload = false
selected C1 response payload = false
defect-functional minimizer payload = false
```

Route B rejected here:

```text
zero-mode basis rows = 0
primitive contraction rows = 0
hessian/source rows = 0
sector matrix rows = 0
```

Next frontier:

```text
{NEXT}
```

Status:

```text
{STATUS}
```
"""

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_independent_long_i10_payload_certificate_or_independent_quadrature_values_fill",
        "status": STATUS,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "theorem": theorem,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "frontier_decision": packet["frontier_decision"],
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert_out, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
