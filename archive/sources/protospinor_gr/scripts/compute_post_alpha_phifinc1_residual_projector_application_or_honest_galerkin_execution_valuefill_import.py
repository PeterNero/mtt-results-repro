from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_canonical_residual_projector_or_honest_galerkin_c1_valuefill_certificate.json"
SLUG = "selected_phifinc1_residualprojectorapplication_or_honestgalerkinexecution_valuefill"
SM_CERT = SM_ROOT / "certificates" / f"{SLUG}_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / f"{SLUG}.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / SLUG
APPLICATION_AUDIT = SM_DIR / "phifinc1_projector_application_audit.packet.json"
DECISION_PACKET = SM_DIR / "application_or_execution_decision.packet.json"
EXECUTION_CONTRACT = SM_DIR / "honest_galerkin_execution_contract.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_phifinc1_residual_projector_application_or_honest_galerkin_execution_valuefill_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_phifinc1_residual_projector_application_or_honest_galerkin_execution_valuefill.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_PhiFinC1ResidualProjectorApplication_or_HonestGalerkinExecution_ValueFill_Import_v1.md"

STATUS = "POST_ALPHA_PHIFINC1_RESIDUAL_PROJECTOR_APPLICATION_OR_HONEST_GALERKIN_EXECUTION_IMPORTED_NOGO_OPEN"
NEXT = "MTT_Selected_DifferentiatedResidualProjectorSourceRule_or_HonestGalerkinC1Execution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    application_audit = load(APPLICATION_AUDIT)
    decision = load(DECISION_PACKET)
    execution_contract = load(EXECUTION_CONTRACT)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"][
                "frontier_is_PhiFinC1_residual_projector_application_or_honest_galerkin_execution_value_fill"
            ]
            is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_PhiFinC1ResidualProjectorApplication_or_HonestGalerkinExecution_ValueFill_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_PhiFinC1ResidualProjectorApplication_or_HonestGalerkinExecution_ValueFill_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["SM_parity_dynamic_packet_closure_claimed"] is False,
            cert["no_knob_closure_claimed"] is False,
            cert["true_SM_equivalence_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "PhiFinC1ResidualProjectorApplicationGuardrailTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["promotion_decision"]["PhiFinC1_projector_application_promoted"] is False,
            candidate["promotion_decision"]["honest_Galerkin_C1_execution_promoted"] is False,
            candidate["promotion_decision"]["SM_parity_dynamic_packet_closed"] is False,
            candidate["promotion_decision"]["no_knob_flavor_constants_closed"] is False,
            candidate["promotion_decision"]["true_SM_equivalence_closed"] is False,
        ]
    )

    audit_ok = all(
        [
            application_audit["schema"] == "MTTPhiFinC1ResidualProjectorApplicationAudit.v1",
            application_audit["status"] == "PROJECTOR_APPLICATION_NOT_DERIVED_BY_EXISTING_PHIFINC1_ARTIFACTS",
            application_audit["canonical_projector_available"] is True,
            application_audit["canonical_projector_mathematically_selected"] is True,
            application_audit["blocking_no_go"]["name"] == "DifferentiatedPhiFinC1TransportOnlyNoGo",
            application_audit["blocking_no_go"]["proved"] is True,
            application_audit["blocking_no_go"]["all_sector_matrices_verified_zero"] is True,
            application_audit["blocking_no_go"]["canonical_all_zero"] is True,
            application_audit["existing_PhiFinC1_support"]["alpha1_dotD_driver_attached"] is True,
            application_audit["existing_PhiFinC1_support"]["selected_dotD_source_verified"] is True,
            application_audit["existing_PhiFinC1_support"]["selected_PhiFinC1_identity_claimed"] is False,
            application_audit["promotion_decision"]["PhiFinC1_projector_application_promoted"] is False,
            application_audit["promotion_decision"]["SM_parity_dynamic_packet_closed"] is False,
            application_audit["observed_data_used"] is False,
            application_audit["target_fitting_used"] is False,
        ]
    )

    conditional = application_audit["conditional_value_if_new_application_rule_is_proved"]
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
            decision["observed_data_used"] is False,
            decision["target_fitting_used"] is False,
            "using stationary transport-only Phi_fin^C1 as the dynamic C1 application rule"
            in decision["what_is_now_ruled_out"],
            "selected differentiated residual-projector source rule" in decision["what_would_close_next"],
        ]
    )

    execution_ok = all(
        [
            execution_contract["schema"] == "MTTHonestGalerkinC1ExecutionContract.v1",
            execution_contract["status"] == "HONEST_GALERKIN_EXECUTION_VALUES_OPEN",
            execution_contract["current_manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
            execution_contract["selected_source_verified_now"] is False,
            execution_contract["target_fitting_forbidden"] is True,
            execution_contract["observed_flavor_data_forbidden"] is True,
            execution_contract["promotion_decision"]["honest_Galerkin_C1_execution_promoted"] is False,
            execution_contract["promotion_decision"]["SM_parity_dynamic_packet_closed"] is False,
            "sector response matrices M_u, M_d, M_e, M_nuD emitted" in execution_contract["acceptance_checks"],
            "CP-odd invariant test" in execution_contract["acceptance_checks"],
        ]
    )

    what_closes_now = {
        "canonical_projector_gate_consumed": prev_ok,
        "PhiFinC1_application_guardrail_imported": imported_ok,
        "transport_only_no_go_verified": audit_ok,
        "conditional_value_if_new_application_rule_is_proved_recorded": conditional_ok,
        "application_or_execution_decision_imported": decision_ok,
        "honest_galerkin_execution_contract_reemitted": execution_ok,
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
        "name": "PostAlphaPhiFinC1ResidualProjectorApplicationGuardrailImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The existing stationary Phi_fin^C1 transport and canonical mode-conserving "
            "primitive tensor do not derive the physical application of the canonical "
            "residual projector: their one-response C1 sector matrices vanish. The route "
            "therefore advances by proving a selected differentiated residual-projector "
            "source rule, by supplying a basis-transport/vertex/Hessian source, or by "
            "running an honest selected Galerkin C1 execution."
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
            "what_closes_now": candidate["what_closes_now"],
            "what_remains_open": candidate["what_remains_open"],
        },
        "phifinc1_projector_application_audit": application_audit,
        "application_or_execution_decision": decision,
        "honest_galerkin_execution_contract": execution_contract,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "stationary_transport_only_no_go_closed": True,
            "frontier_is_differentiated_residual_projector_source_rule_or_honest_galerkin_execution": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "phifinc1_projector_application_audit": str(APPLICATION_AUDIT),
            "application_or_execution_decision": str(DECISION_PACKET),
            "honest_galerkin_execution_contract": str(EXECUTION_CONTRACT),
        },
    }

    note = f"""# PostAlpha PhiFinC1ResidualProjectorApplication or HonestGalerkinExecution ValueFill Import v1

## Result

The canonical residual projector is available, but existing stationary
`Phi_fin^C1` artifacts do not prove its physical C1 application.

Closed guardrail:

```text
DifferentiatedPhiFinC1TransportOnlyNoGo = proved
all emitted one-response C1 sector matrices = zero
```

The conditional value remains available only if a new selected application rule
is proved:

```text
A^T A          = [[12, 0], [0, 12]]
A^T b          = [12, 12]
deltaTheta_C1  = [1, 1]
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
        "certificate": "post_alpha_phifinc1_residual_projector_application_or_honest_galerkin_execution_valuefill",
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
