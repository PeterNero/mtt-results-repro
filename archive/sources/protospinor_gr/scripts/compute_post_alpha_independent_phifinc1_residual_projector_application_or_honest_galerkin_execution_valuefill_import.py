from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = ROOT / "certificates" / "post_alpha_independent_canonical_residual_projector_or_honest_galerkin_c1_valuefill_certificate.json"
SOURCE_CERT = ROOT / "certificates" / "post_alpha_phifinc1_residual_projector_application_or_honest_galerkin_execution_valuefill_certificate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_independent_phifinc1_residual_projector_application_or_honest_galerkin_execution_valuefill_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_independent_phifinc1_residual_projector_application_or_honest_galerkin_execution_valuefill.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_IndependentPhiFinC1ResidualProjectorApplication_or_HonestGalerkinExecutionValueFill_Import_v1.md"

STATUS = "POST_ALPHA_INDEPENDENT_PHIFINC1_RESIDUAL_PROJECTOR_APPLICATION_OR_HONEST_GALERKIN_EXECUTION_IMPORTED_NOGO_OPEN"
SOURCE_STATUS = "POST_ALPHA_PHIFINC1_RESIDUAL_PROJECTOR_APPLICATION_OR_HONEST_GALERKIN_EXECUTION_IMPORTED_NOGO_OPEN"
THIS_ARTIFACT = "MTT_Selected_PhiFinC1ResidualProjectorApplication_or_HonestGalerkinExecution_ValueFill_v1"
NEXT = "MTT_Selected_DifferentiatedResidualProjectorSourceRule_or_HonestGalerkinC1Execution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE_CERT)
    source_packet = load(Path(source["packet_written"]))

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["canonical_mathematical_projector_closed"] is True,
            prev["frontier_decision"][
                "frontier_is_PhiFinC1_residual_projector_application_or_honest_galerkin_execution_value_fill"
            ]
            is True,
            prev["frontier_decision"]["next_required_artifact"] == THIS_ARTIFACT,
            all(prev["guardrails"].values()),
        ]
    )

    source_ok = all(
        [
            source["status"] == SOURCE_STATUS,
            source["theorem"]["proved"] is True,
            source["closure_claimed"] is False,
            source["frontier_decision"]["stationary_transport_only_no_go_closed"] is True,
            source["frontier_decision"][
                "frontier_is_differentiated_residual_projector_source_rule_or_honest_galerkin_execution"
            ]
            is True,
            source["frontier_decision"]["next_required_artifact"] == NEXT,
            all(source["what_closes_now"].values()),
            all(source["what_remains_open"].values()),
            all(source["guardrails"].values()),
        ]
    )

    application = source_packet["phifinc1_projector_application_audit"]
    decision = source_packet["application_or_execution_decision"]
    contract = source_packet["honest_galerkin_execution_contract"]

    no_go = application["blocking_no_go"]
    application_ok = all(
        [
            application["schema"] == "MTTPhiFinC1ResidualProjectorApplicationAudit.v1",
            application["status"] == "PROJECTOR_APPLICATION_NOT_DERIVED_BY_EXISTING_PHIFINC1_ARTIFACTS",
            application["canonical_projector_available"] is True,
            application["canonical_projector_mathematically_selected"] is True,
            no_go["name"] == "DifferentiatedPhiFinC1TransportOnlyNoGo",
            no_go["proved"] is True,
            no_go["all_sector_matrices_verified_zero"] is True,
            no_go["canonical_all_zero"] is True,
            application["promotion_decision"]["PhiFinC1_projector_application_promoted"] is False,
            application["promotion_decision"]["SM_parity_dynamic_packet_closed"] is False,
            application["observed_data_used"] is False,
            application["target_fitting_used"] is False,
        ]
    )

    conditional = application["conditional_value_if_new_application_rule_is_proved"]
    conditional_ok = all(
        [
            conditional["A_selected_columns_available"] is True,
            conditional["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            conditional["A_transpose_b"] == [12.0, 12.0],
            conditional["deltaTheta_C1"] == [1.0, 1.0],
            conditional["rank"] == 2,
            conditional["SM_parity_dynamic_packet_would_close"] is True,
            conditional["no_knob_flavor_constants_would_close"] is False,
        ]
    )

    decision_ok = all(
        [
            decision["schema"] == "MTTApplicationOrExecutionDecision.v1",
            decision["status"] == "APPLICATION_NOGO_EXECUTION_VALUES_OPEN",
            decision["SM_parity_dynamic_packet_closed"] is False,
            decision["no_knob_flavor_constants_closed"] is False,
            decision["true_SM_equivalence_closed"] is False,
            "selected differentiated residual-projector source rule" in decision["what_would_close_next"],
        ]
    )

    contract_ok = all(
        [
            contract["schema"] == "MTTHonestGalerkinC1ExecutionContract.v1",
            contract["status"] == "HONEST_GALERKIN_EXECUTION_VALUES_OPEN",
            contract["current_manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
            contract["selected_source_verified_now"] is False,
            contract["target_fitting_forbidden"] is True,
            contract["observed_flavor_data_forbidden"] is True,
            contract["promotion_decision"]["honest_Galerkin_C1_execution_promoted"] is False,
            contract["promotion_decision"]["SM_parity_dynamic_packet_closed"] is False,
        ]
    )

    what_closes_now = {
        "long_name_canonical_projector_gate_consumed": prev_ok,
        "audited_PhiFinC1_application_guardrail_reanchored": source_ok,
        "transport_only_no_go_verified": application_ok,
        "conditional_value_if_new_application_rule_is_proved_recorded": conditional_ok,
        "application_or_execution_decision_imported": decision_ok,
        "honest_galerkin_execution_contract_reemitted": contract_ok,
    }

    what_remains_open = {
        "selected_differentiated_residual_projector_source_rule": True,
        "selected_basis_transport_vertex_or_Hessian_source": True,
        "honest_selected_Galerkin_C1_execution_values": True,
        "selected_A_selected": True,
        "selected_b_selected": True,
        "selected_deltaTheta_C1": True,
        "SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "does_not_reinterpret_canonical_projector_as_physical_application": True,
        "does_not_promote_transport_only_PhiFinC1": True,
        "does_not_promote_honest_galerkin_execution": True,
        "does_not_promote_A_b_deltaTheta": True,
        "does_not_claim_SM_parity_dynamic_closure": True,
        "does_not_claim_true_SM_equivalence": True,
        "does_not_claim_no_knob_flavor_closure": True,
        "does_not_use_observed_or_target_inputs": True,
    }

    theorem = {
        "name": "PostAlphaIndependentPhiFinC1ResidualProjectorApplicationGuardrailImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The long-name branch imports the transport-only no-go: existing stationary "
            "Phi_fin^C1 artifacts do not derive physical application of the canonical "
            "residual projector. The next gate is a differentiated residual-projector "
            "source rule or honest Galerkin C1 execution."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_phifinc1_application_certificate": source,
        "phifinc1_projector_application_audit": application,
        "application_or_execution_decision": decision,
        "honest_galerkin_execution_contract": contract,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "stationary_transport_only_no_go_closed": True,
            "frontier_is_differentiated_residual_projector_source_rule_or_honest_galerkin_execution": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_long_name_certificate": str(PREV),
            "source_phifinc1_application_certificate": str(SOURCE_CERT),
            "source_phifinc1_application_packet": source["packet_written"],
        },
    }

    note = f"""# PostAlpha Independent PhiFinC1ResidualProjectorApplication or HonestGalerkinExecution ValueFill Import v1

## Result

The long-name branch imports the transport-only no-go.

Closed guardrail:

```text
DifferentiatedPhiFinC1TransportOnlyNoGo = proved
all emitted one-response C1 sector matrices = zero
```

Still open: selected differentiated residual-projector source rule, or honest Galerkin C1 execution.

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
        "certificate": "post_alpha_independent_phifinc1_residual_projector_application_or_honest_galerkin_execution_valuefill",
        "status": STATUS,
        "closure_claimed": False,
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
