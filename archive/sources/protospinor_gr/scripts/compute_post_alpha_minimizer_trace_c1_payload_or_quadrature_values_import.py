from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_phifinc1_minimizes_defect_or_quadrature_table_certificate.json"
SM_CERT = SM_ROOT / "certificates" / "selected_minimizertracec1payloadtheorem_or_quadraturetablevalues_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_minimizertracec1payloadtheorem_or_quadraturetablevalues.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / "selected_minimizertracec1payloadtheorem_or_quadraturetablevalues"
PAYLOAD = SM_DIR / "i10_minimizer_trace_c1_payload_contract.packet.json"
QUADRATURE = SM_DIR / "quadrature_values_staging_tables.packet.json"
MANIFEST = SM_DIR / "closure_acceptance_manifest.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_minimizer_trace_c1_payload_or_quadrature_values_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_minimizer_trace_c1_payload_or_quadrature_values.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_MinimizerTraceC1Payload_or_QuadratureValues_Import_v1.md"

STATUS = "POST_ALPHA_MINIMIZER_TRACE_C1_PAYLOAD_OR_QUADRATURE_VALUES_IMPORTED_CONTRACT_OPEN"
NEXT = "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    payload = load(PAYLOAD)
    quadrature = load(QUADRATURE)
    manifest = load(MANIFEST)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_minimizer_trace_C1_payload_theorem_or_quadrature_values"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_MinimizerTraceC1PayloadTheorem_or_QuadratureTableValues_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_MinimizerTraceC1PayloadTheorem_or_QuadratureTableValues_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["unpatched_theorem_closure_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "MinimizerTraceC1PayloadOrQuadratureValuesReductionTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["promotion_decision"]["I10_proved"] is False,
            candidate["promotion_decision"]["route_A_i10_payload_certificate_accepted"] is False,
            candidate["promotion_decision"]["route_B_independent_quadrature_values_accepted"] is False,
            candidate["promotion_decision"]["unpatched_SM_parity_dynamic_packet_closed"] is False,
            candidate["replay_if_route_A_or_B_accepted"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            candidate["replay_if_route_A_or_B_accepted"]["A_transpose_b"] == [12.0, 12.0],
            candidate["replay_if_route_A_or_B_accepted"]["deltaTheta_C1"] == [1.0, 1.0],
        ]
    )

    payload_ok = all(
        [
            payload["schema"] == "MTTI10MinimizerTraceC1PayloadContract.v1",
            payload["status"] == "PAYLOAD_CERTIFICATE_CONTRACT_BUILT_VALUES_OPEN",
            payload["theorem_slot"] == "I10_phifinc1_minimizes_c1_defect_functional",
            payload["observed_data_used"] is False,
            payload["target_fitting_used"] is False,
            payload["promotion_rule"]["current_all_payload_certificates_verified"] is False,
            payload["promotion_rule"]["if_all_payload_certificates_verified"]["SM_parity_dynamic_packet_closes"] is True,
            all(item["required"] is True for item in payload["payload_certificate_required"].values()),
            set(payload["payload_certificate_required"].keys())
            == {
                "selected_minimizer_trace_payload",
                "selected_c1_response_payload",
                "defect_functional_minimizer_payload",
            },
        ]
    )

    quadrature_ok = all(
        [
            quadrature["schema"] == "MTTIndependentQuadratureValuesStagingTables.v1",
            quadrature["status"] == "TABLES_STAGED_VALUES_EMPTY",
            quadrature["values_filled_now"] is False,
            quadrature["observed_data_used"] is False,
            quadrature["target_fitting_used"] is False,
            quadrature["acceptance_tests"]["A_shape"] == [72, 2],
            quadrature["acceptance_tests"]["b_shape"] == [72],
            quadrature["expected_minimum_counts"]["zero_mode_basis_rows"] == 8,
            quadrature["expected_minimum_counts"]["primitive_contraction_rows"] == 18,
            quadrature["expected_minimum_counts"]["hessian_source_rows"] == 2,
            quadrature["expected_minimum_counts"]["sector_matrix_rows"] == 18,
            all(len(rows) == 0 for rows in quadrature["tables"].values()),
            quadrature["would_close_if_filled"]["SM_parity_dynamic_packet_closes"] is True,
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
            len(manifest["route_A_i10_payload_certificate"]["required_checks"]) == 4,
            len(manifest["route_B_independent_quadrature_values"]["required_checks"]) == 7,
        ]
    )

    what_closes_now = {
        "previous_binding_reduction_consumed": prev_ok,
        "payload_or_quadrature_contract_imported": imported_ok,
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
    }

    guardrails = {
        "does_not_claim_I10_payload_certificate_accepted": True,
        "does_not_claim_quadrature_values_filled": True,
        "does_not_claim_dual_route_acceptance": True,
        "does_not_promote_unpatched_A_b_or_deltaTheta": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_true_SM_equivalence_closure": True,
    }

    theorem = {
        "name": "PostAlphaMinimizerTraceC1PayloadOrQuadratureValuesImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "The I10 proof obligation is reduced to three explicit selected payload "
            "certificates: minimizer trace, selected C1 response, and defect-functional "
            "stationarity/coercivity; or, independently, to filling staged quadrature "
            "tables that pass the dual-route acceptance manifest. This fixes executable "
            "closure conditions but accepts neither route yet."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
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
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "i10_payload_contract": str(PAYLOAD),
            "quadrature_values_staging_tables": str(QUADRATURE),
            "closure_acceptance_manifest": str(MANIFEST),
        },
    }

    note = f"""# PostAlpha Minimizer Trace C1 Payload or Quadrature Values Import v1

## Result

The closure route is now executable but still open.

Route A requires three selected payload certificates:

```text
selected minimizer trace payload
selected C1 response payload
defect-functional minimizer payload
```

Route B requires independent quadrature values:

```text
zero-mode basis rows >= 8
primitive contraction rows >= 18
hessian/source rows >= 2
sector matrix rows >= 18
```

Neither route is accepted yet.

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
        "certificate": "post_alpha_minimizer_trace_c1_payload_or_quadrature_values",
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
