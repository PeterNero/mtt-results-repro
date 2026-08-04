from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_minimizer_trace_c1_payload_or_quadrature_values_certificate.json"
SM_CERT = SM_ROOT / "certificates" / "selected_i10_payloadcertificate_or_independentquadraturevaluesfill_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_i10_payloadcertificate_or_independentquadraturevaluesfill.candidate.json"
SM_NOTE = SM_ROOT / "proof_corpus" / "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1.md"
SM_DIR = SM_ROOT / "candidate_data" / "selected_i10_payloadcertificate_or_independentquadraturevaluesfill"
ROUTE_A = SM_DIR / "route_a_i10_payload_certificate_fill_attempt.packet.json"
ROUTE_B = SM_DIR / "route_b_independent_quadrature_values_fill_attempt.packet.json"
CUTSET = SM_DIR / "minimal_next_cutset.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_i10_payload_certificate_or_quadrature_values_fill_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_i10_payload_certificate_or_quadrature_values_fill.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_I10PayloadCertificate_or_QuadratureValuesFill_Import_v1.md"

STATUS = "POST_ALPHA_I10_PAYLOAD_CERTIFICATE_OR_QUADRATURE_VALUES_FILL_IMPORTED_CUTSET_OPEN"
NEXT = "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    cutset = load(CUTSET)
    source_note = SM_NOTE.read_text(encoding="utf-8")

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_I10_payload_certificate_or_independent_quadrature_values_fill"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["unpatched_theorem_closure_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["route_A_accepted"] is False,
            cert["route_B_accepted"] is False,
            cert["next_required_artifact"] == NEXT,
            candidate["theorem"]["name"] == "I10PayloadFillAttemptCutsetTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["promotion_decision"]["I10_proved"] is False,
            candidate["promotion_decision"]["route_A_i10_payload_certificate_accepted"] is False,
            candidate["promotion_decision"]["route_B_independent_quadrature_values_accepted"] is False,
            candidate["promotion_decision"]["unpatched_SM_parity_dynamic_packet_closed"] is False,
            candidate["promotion_decision"]["true_SM_equivalence_closed"] is False,
            candidate["replay_if_route_A_or_B_accepted"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            candidate["replay_if_route_A_or_B_accepted"]["A_transpose_b"] == [12.0, 12.0],
            candidate["replay_if_route_A_or_B_accepted"]["deltaTheta_C1"] == [1.0, 1.0],
            NEXT in source_note,
        ]
    )

    route_a_ok = all(
        [
            route_a["schema"] == "MTTRouteAI10PayloadCertificateFillAttempt.v1",
            route_a["status"] == "ATTEMPTED_NOT_ACCEPTED_SELECTED_PAYLOADS_OPEN",
            route_a["accepted_now"] is False,
            route_a["observed_data_used"] is False,
            route_a["target_fitting_used"] is False,
            route_a["payload_checks"]["no_observed_data_as_selector"]["value"] is True,
            route_a["payload_checks"]["selected_minimizer_trace_payload_verified"]["value"] is False,
            route_a["payload_checks"]["selected_c1_response_payload_verified"]["value"] is False,
            route_a["payload_checks"]["defect_functional_minimizer_payload_verified"]["value"] is False,
        ]
    )

    route_b_ok = all(
        [
            route_b["schema"] == "MTTRouteBIndependentQuadratureValuesFillAttempt.v1",
            route_b["status"] == "ATTEMPTED_VALUES_EMPTY_NOT_ACCEPTED",
            route_b["accepted_now"] is False,
            route_b["observed_data_used"] is False,
            route_b["target_fitting_used"] is False,
            route_b["acceptance_checks"]["no_patched_replay_copying"] is True,
            route_b["acceptance_checks"]["deltaTheta_solve_matches_replay"] is False,
            route_b["table_counts"]["zero_mode_basis_rows"] == 0,
            route_b["table_counts"]["primitive_contraction_rows"] == 0,
            route_b["table_counts"]["hessian_source_rows"] == 0,
            route_b["table_counts"]["sector_matrix_rows"] == 0,
            route_b["expected_minimum_counts"]["zero_mode_basis_rows"] == 8,
            route_b["expected_minimum_counts"]["primitive_contraction_rows"] == 18,
            route_b["expected_minimum_counts"]["hessian_source_rows"] == 2,
            route_b["expected_minimum_counts"]["sector_matrix_rows"] == 18,
        ]
    )

    cutset_ok = all(
        [
            cutset["schema"] == "MTTI10PayloadMinimalCutset.v1",
            cutset["status"] == "NEXT_CUTSET_SELECTED",
            cutset["recommended_next"]["artifact"] == NEXT,
            cutset["recommended_next"]["superset_strategy"]["locked_target"]["A_transpose_A"]
            == [[12.0, 0.0], [0.0, 12.0]],
            cutset["recommended_next"]["superset_strategy"]["locked_target"]["A_transpose_b"] == [12.0, 12.0],
            cutset["recommended_next"]["superset_strategy"]["locked_target"]["deltaTheta_C1"] == [1.0, 1.0],
            cutset["route_A_minimal_cutset"]
            == [
                "selected_minimizer_trace_payload_verified",
                "selected_c1_response_payload_verified",
                "defect_functional_minimizer_payload_verified",
            ],
            cutset["route_B_minimal_cutset"]
            == [
                "zero_mode_basis_rows",
                "primitive_contraction_rows",
                "hessian_source_rows",
                "sector_matrix_rows",
            ],
        ]
    )

    what_closes_now = {
        "previous_I10_payload_or_quadrature_frontier_consumed": prev_ok,
        "I10_fill_attempt_theorem_imported": imported_ok,
        "route_A_payload_certificate_attempt_evaluated_not_accepted": route_a_ok,
        "route_B_quadrature_value_attempt_evaluated_empty_not_accepted": route_b_ok,
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
    }

    guardrails = {
        "does_not_claim_I10_proved": True,
        "does_not_claim_route_A_accepted": True,
        "does_not_claim_route_B_accepted": True,
        "does_not_promote_replay_A_b_or_deltaTheta_as_selected_values": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_unpatched_SM_closure": True,
        "does_not_claim_true_SM_equivalence_closure": True,
    }

    theorem = {
        "name": "PostAlphaI10PayloadCertificateOrQuadratureValuesFillImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "The selected I10 fill attempt is evaluated without observed or target inputs. "
            "Route A remains blocked because the minimizer trace, selected C1 response, "
            "and defect-functional minimizer payloads are not verified. Route B remains "
            "blocked because the independent quadrature tables contain zero rows. The "
            "next exact frontier is the selected Strominger trace/C1 first-variation "
            "theorem or an executed quadrature plan."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_candidate_summary": {
            "status": candidate["status"],
            "theorem": candidate["theorem"],
            "promotion_decision": candidate["promotion_decision"],
            "replay_if_route_A_or_B_accepted": candidate["replay_if_route_A_or_B_accepted"],
            "what_closes_now": candidate["what_closes_now"],
            "what_remains_open": candidate["what_remains_open"],
        },
        "route_A_i10_payload_certificate_fill_attempt": route_a,
        "route_B_independent_quadrature_values_fill_attempt": route_b,
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
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "route_A_fill_attempt": str(ROUTE_A),
            "route_B_fill_attempt": str(ROUTE_B),
            "minimal_next_cutset": str(CUTSET),
        },
    }

    note = f"""# PostAlpha I10 Payload Certificate or Quadrature Values Fill Import v1

## Result

The selected I10 fill attempt has been evaluated. It does not close I10.

Route A is not accepted because the three required selected payload certificates remain unverified:

```text
selected minimizer trace payload
selected C1 response payload
defect-functional minimizer payload
```

Route B is not accepted because the independent quadrature tables remain empty:

```text
zero-mode basis rows = 0
primitive contraction rows = 0
hessian/source rows = 0
sector matrix rows = 0
```

The replay target is fixed but not promoted as selected data:

```text
A^T A = [[12, 0], [0, 12]]
A^T b = [12, 12]
deltaTheta_C1 = [1, 1]
```

## Status

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_i10_payload_certificate_or_quadrature_values_fill",
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
