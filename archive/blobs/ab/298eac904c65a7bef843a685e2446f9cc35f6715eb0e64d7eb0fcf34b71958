from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PREV = (
    ROOT
    / "certificates"
    / "post_alpha_phifinc1_minimizes_defect_functional_or_independent_quadrature_table_certificate.json"
)
SOURCE_CERT = ROOT / "certificates" / "post_alpha_minimizer_trace_c1_payload_or_quadrature_values_certificate.json"

OUT_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_minimizer_trace_c1_payload_theorem_or_quadrature_table_values_certificate.json"
)
OUT_PACKET = (
    ROOT
    / "candidate_data"
    / "post_alpha_minimizer_trace_c1_payload_theorem_or_quadrature_table_values.packet.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "PostAlpha_MinimizerTraceC1PayloadTheorem_or_QuadratureTableValues_Import_v1.md"
)

STATUS = "POST_ALPHA_MINIMIZER_TRACE_C1_PAYLOAD_THEOREM_OR_QUADRATURE_TABLE_VALUES_IMPORTED_CONTRACT_OPEN"
NEXT = "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source_cert = load(SOURCE_CERT)
    source_packet = load(Path(source_cert["packet_written"]))

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["unpatched_theorem_closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_minimizer_trace_C1_payload_theorem_or_quadrature_values"]
            is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_MinimizerTraceC1PayloadTheorem_or_QuadratureTableValues_v1",
        ]
    )

    source_ok = all(
        [
            source_cert["theorem"]["proved"] is True,
            source_cert["closure_claimed"] is False,
            source_cert["unpatched_theorem_closure_claimed"] is False,
            source_cert["status"] == "POST_ALPHA_MINIMIZER_TRACE_C1_PAYLOAD_OR_QUADRATURE_VALUES_IMPORTED_CONTRACT_OPEN",
            source_cert["frontier_decision"]["next_required_artifact"] == NEXT,
            source_cert["frontier_decision"]["route_A_payload_certificate_contract_built"] is True,
            source_cert["frontier_decision"]["route_B_quadrature_values_tables_staged"] is True,
            source_cert["frontier_decision"]["closure_acceptance_manifest_built"] is True,
            all(source_cert["what_closes_now"].values()),
            all(source_cert["what_remains_open"].values()),
            all(source_cert["guardrails"].values()),
        ]
    )

    payload = source_packet["i10_minimizer_trace_c1_payload_contract"]
    quadrature = source_packet["quadrature_values_staging_tables"]
    manifest = source_packet["closure_acceptance_manifest"]

    payload_ok = all(
        [
            payload["schema"] == "MTTI10MinimizerTraceC1PayloadContract.v1",
            payload["status"] == "PAYLOAD_CERTIFICATE_CONTRACT_BUILT_VALUES_OPEN",
            payload["theorem_slot"] == "I10_phifinc1_minimizes_c1_defect_functional",
            payload["promotion_rule"]["current_all_payload_certificates_verified"] is False,
            len(payload["payload_certificate_required"]) == 3,
            payload["observed_data_used"] is False,
            payload["target_fitting_used"] is False,
        ]
    )

    quadrature_ok = all(
        [
            quadrature["schema"] == "MTTIndependentQuadratureValuesStagingTables.v1",
            quadrature["status"] == "TABLES_STAGED_VALUES_EMPTY",
            quadrature["values_filled_now"] is False,
            all(len(rows) == 0 for rows in quadrature["tables"].values()),
            quadrature["expected_minimum_counts"]["zero_mode_basis_rows"] == 8,
            quadrature["expected_minimum_counts"]["primitive_contraction_rows"] == 18,
            quadrature["expected_minimum_counts"]["hessian_source_rows"] == 2,
            quadrature["expected_minimum_counts"]["sector_matrix_rows"] == 18,
            quadrature["would_close_if_filled"]["SM_parity_dynamic_packet_closes"] is True,
            quadrature["observed_data_used"] is False,
            quadrature["target_fitting_used"] is False,
        ]
    )

    manifest_ok = all(
        [
            manifest["schema"] == "MTTPhiFinC1ClosureAcceptanceManifest.v1",
            manifest["status"] == "DUAL_ROUTE_ACCEPTANCE_MANIFEST_BUILT_OPEN",
            manifest["closure_claimed_now"] is False,
            manifest["route_A_i10_payload_certificate"]["accepted_now"] is False,
            manifest["route_B_independent_quadrature_values"]["accepted_now"] is False,
            manifest["replay_target_if_accepted"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            manifest["replay_target_if_accepted"]["A_transpose_b"] == [12.0, 12.0],
            manifest["replay_target_if_accepted"]["deltaTheta_C1"] == [1.0, 1.0],
        ]
    )

    what_closes_now = {
        "long_name_PhiFinC1_binding_gate_consumed": prev_ok,
        "audited_payload_or_quadrature_contract_bridged": source_ok,
        "I10_payload_certificate_schema_fixed": payload_ok,
        "independent_quadrature_value_tables_staged": quadrature_ok,
        "dual_route_acceptance_manifest_built": manifest_ok,
    }

    what_remains_open = {
        "selected_minimizer_trace_payload_verified": True,
        "selected_c1_response_payload_verified": True,
        "defect_functional_minimizer_payload_verified": True,
        "independent_quadrature_values_filled": True,
        "unpatched_SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "does_not_claim_I10_payload_certificate_accepted": True,
        "does_not_claim_quadrature_values_filled": True,
        "does_not_claim_dual_route_acceptance": True,
        "does_not_promote_unpatched_A_b_or_deltaTheta": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_true_SM_or_no_knob_closure": True,
    }

    theorem = {
        "name": "PostAlphaMinimizerTraceC1PayloadTheoremOrQuadratureTableValuesBridge",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "The long-name chain now imports the executable I10 payload or quadrature "
            "values contract. Route A requires selected minimizer trace, C1 response, "
            "and defect-functional minimizer payloads. Route B requires independent "
            "quadrature tables. Neither route is accepted here."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_contract_certificate": source_cert,
        "i10_minimizer_trace_c1_payload_contract": payload,
        "quadrature_values_staging_tables": quadrature,
        "closure_acceptance_manifest": manifest,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "route_A_payload_certificate_contract_built": True,
            "route_B_quadrature_values_tables_staged": True,
            "closure_acceptance_manifest_built": True,
            "frontier_is_I10_payload_certificate_or_independent_quadrature_values_fill": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_long_name_certificate": str(PREV),
            "source_contract_certificate": str(SOURCE_CERT),
            "source_contract_packet": source_cert["packet_written"],
        },
    }

    note = f"""# PostAlpha MinimizerTraceC1PayloadTheorem or QuadratureTableValues Import v1

## Result

The remaining unpatched closure route is now machine-checkable.

Route A requires:

```text
selected minimizer trace payload
selected C1 response payload
defect-functional minimizer payload
```

Route B requires independent quadrature tables:

```text
zero-mode basis rows >= 8
primitive contraction rows >= 18
hessian/source rows >= 2
sector matrix rows >= 18
```

Neither route is accepted yet.

Next:

```text
{NEXT}
```
"""

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_minimizer_trace_c1_payload_theorem_or_quadrature_table_values",
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
