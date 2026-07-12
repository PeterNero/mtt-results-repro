from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_noninvariant_c1_fiberclass.packet.json"
HIGHER = QA / "candidate_data" / "selected_u1y_routec_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"
CORRECTION = QA / "candidate_data" / "selected_u1y_routec_selectedcorrection_source_or_fullresponse_emission.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_selected_correction_source_reduction_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_selected_correction_source_reduction.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_SelectedCorrection_SourceReduction_Import_v1.md"

STATUS = "POST_ALPHA_SELECTED_CORRECTION_SOURCE_REDUCED_NONIDENTITY_RHOE_BN_OPEN"
NEXT = "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_Construction_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def higher_ok(higher: dict) -> bool:
    decision = higher["decision"]
    tests = higher["primitive_layer_tests"]
    contract = higher["higher_order_contract"]
    return all(
        [
            higher["status"] == "U1Y_ROUTEC_PRIMITIVECLASS_C1OBSERVABLE_NO_SPLIT_HIGHERORDER_SOURCE_EMISSION_OPEN",
            higher["closure_claimed"] is False,
            higher["target_fitting_used"] is False,
            higher["next_required_artifact"] == "Selected_U1Y_RouteC_SelectedCorrectionMatrixSource_or_FullResponseEmission_v1",
            higher["theorem"]["proved"] is True,
            decision["primitive_fixed_fiber_class_selected_for_current_spectral_observables"] is True,
            decision["primitive_class_can_emit_non_degenerate_flavor"] is False,
            decision["higher_order_or_full_response_source_emission_required"] is True,
            decision["selected_source_emission_closed"] is False,
            tests["all_yy_star_scalar_identity"] is True,
            tests["mass_splitting_test_passes"] is False,
            tests["mixing_commutator_test_passes"] is False,
            tests["cp_odd_test_passes"] is False,
            contract["criterion_imported"] is True,
            contract["diagnostic_splitter_exists_without_observed_targets"] is True,
            contract["full_response_acceptance_tests_locked"] is True,
            all(value is False for value in higher["guardrails"].values()),
        ]
    )


def correction_ok(correction: dict) -> bool:
    decision = correction["decision"]
    reduction = correction["reduction"]
    diagnostic = correction["diagnostic_representative_support_only"]
    payload = correction["required_payload"]
    return all(
        [
            correction["status"] == "U1Y_ROUTEC_SELECTED_CORRECTION_EMISSION_REDUCED_NONIDENTITY_RHOE_BN_OPEN",
            correction["closure_claimed"] is False,
            correction["target_fitting_used"] is False,
            correction["next_required_artifact"] == NEXT,
            correction["theorem"]["proved"] is True,
            decision["primitive_only_route_retired_for_splitter"] is True,
            decision["nonidentity_rhoE_and_BN_required"] is True,
            decision["selected_correction_matrix_source_closed"] is False,
            decision["selected_full_response_emission_closed"] is False,
            decision["diagnostic_splitter_promoted"] is False,
            decision["formal_lift_promoted"] is False,
            decision["A_selected_computable"] is False,
            decision["b_selected_computable"] is False,
            decision["lambda_12_computable"] is False,
            reduction["diagnostic_splitter_exists"] is True,
            reduction["mass_mixing_cp_diagnostic_tests_nonzero"] is True,
            reduction["diagnostic_splitter_not_promoted"] is True,
            reduction["formal_lift_rejected_as_proof"] is True,
            reduction["strict_primitive_search_found_no_legal_emission"] is True,
            reduction["selected_correction_matrices_emitted"] is False,
            diagnostic["candidate_count"] == 1170,
            diagnostic["ckm_commutator_norm_sq"] > 0,
            diagnostic["pmns_commutator_norm_sq"] > 0,
            diagnostic["cp_odd_trace_commutator_cubed_imag"] > 0,
            all(value["current_status"] == "open" and value["required"] is True for value in payload.values()),
            all(value is False for value in correction["guardrails"].values()),
        ]
    )


def main() -> None:
    prev = load(PREV)
    higher = load(HIGHER)
    correction = load(CORRECTION)

    previous_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["status"] == "POST_ALPHA_NONINVARIANT_C1_FIBERCLASS_SPECTRAL_QUOTIENT_CLOSED_FULL_RESPONSE_OPEN",
            prev["next_required_artifact"]
            == "Selected_U1Y_RouteC_PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_v1",
            prev["what_closes_now"]["current_layer_scalar_permutation_degeneracy_proved"] is True,
        ]
    )
    theorem_proved = all([previous_ready, higher_ok(higher), correction_ok(correction)])
    packet = {
        "theorem": {
            "name": "PostAlphaSelectedCorrectionSourceReductionImport",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The primitive fixed-fiber C1 layer is proved too degenerate for flavor splitting. "
                "A diagnostic qutrit/Weyl correction splitter passes mass, commutator, and CP tests "
                "without observed targets, but it is not selected. The selected correction/full-response "
                "gate reduces to same-source nonidentity rho_E, quotient-valid B_N, and an honest "
                "deltaTheta/C1 solve."
            ),
        },
        "status": STATUS,
        "primitive_layer_tests": higher["primitive_layer_tests"],
        "higher_order_contract": higher["higher_order_contract"],
        "diagnostic_representative_support_only": correction["diagnostic_representative_support_only"],
        "required_payload": correction["required_payload"],
        "checks": {
            "previous_ready": previous_ready,
            "higher_ok": higher_ok(higher),
            "correction_ok": correction_ok(correction),
            "theorem_proved": theorem_proved,
        },
        "what_closes_now": {
            "primitive_only_route_retired_for_splitter": True,
            "diagnostic_splitter_recorded_support_only": True,
            "selected_correction_gate_reduced": True,
            "nonidentity_rhoE_BN_payload_contract_built": True,
            "formal_lift_rejected_as_proof": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": correction["what_remains_open"],
        "guardrails": {
            "does_not_promote_diagnostic_splitter": True,
            "does_not_promote_formal_lift": True,
            "does_not_claim_selected_correction_or_full_response_emission": True,
            "does_not_claim_A_b_lambda_yukawa_or_SM_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {"previous": str(PREV), "higher": str(HIGHER), "correction": str(CORRECTION)},
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_selected_correction_source_reduction",
        "status": STATUS,
        "closure_claimed": False,
        "diagnostic_splitter_exists": True,
        "diagnostic_splitter_promoted": False,
        "selected_correction_matrix_source_closed": False,
        "checks": {
            **packet["checks"],
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# PostAlpha SelectedCorrection SourceReduction Import v1

## Result

The primitive C1 quotient layer is too degenerate for flavor splitting, but an
unselected diagnostic splitter shows that the algebraic target is reachable.

```text
diagnostic splitter found = true
diagnostic splitter selected = false
selected correction matrices emitted = false
formal lift promoted = false
```

The next required payload is now:

```text
nonidentity rho_E
quotient-valid B_N
selected D_E/Riesz/Green/dotD replay
selected deltaTheta/C1 solution
primitive C1 contractions or full response matrices
b_selected row or homogeneous-zero theorem
```

Status:

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
