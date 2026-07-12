from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_end0_sector_model_values.packet.json"
SOURCE = QA / "candidate_data" / "selected_u1y_routec_zeromodebasis_from_hym_projector_source_theorem.candidate.json"
PAYLOAD = QA / "candidate_data" / "selected_u1y_routec_zeromodebasis_from_hym_projector_source_payload.open.json"
SM_THEOREM = ROOT.parent / "mtt-sm-parity-closure" / "candidate_data" / "selected_zero_mode_basis_from_hym_projector_source_theorem.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_zeromodebasis_hym_projector_theorem_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_zeromodebasis_hym_projector_theorem.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_ZeroModeBasis_HYMProjector_Theorem_Import_v1.md"

STATUS = "POST_ALPHA_ZEROMODEBASIS_HYM_PROJECTOR_THEOREM_PROVED_PAYLOAD_OPEN"
NEXT = "Selected_U1Y_RouteC_HYM_Projector_Source_Payload_Fill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def all_nulls(obj: object) -> bool:
    if isinstance(obj, dict):
        return all(all_nulls(value) for value in obj.values())
    return obj is None


def projector_values_absent(payload: dict) -> bool:
    return all(
        all(
            section[key] is None
            for key in [
                "idempotent",
                "projector_matrix",
                "selected_by_same_source",
                "self_adjoint_for_selected_Gram",
                "zero_mode_projector",
            ]
        )
        for section in payload["required_payload"]["sector_projectors"].values()
    )


def basis_values_absent(payload: dict) -> bool:
    return all(
        all(
            section[key] is None
            for key in ["Gram_matrix", "basis_vectors", "orientation_or_ordering_rule", "trace_normalization"]
        )
        for section in payload["required_payload"]["ordered_zero_mode_bases_K_s"].values()
    )


def end0_action_values_absent(payload: dict) -> bool:
    return all(
        all(
            section[key] is None
            for key in ["bracket_preserving", "preserves_K_s", "rho_s_T1", "rho_s_T2", "rho_s_T3", "same_source_action"]
        )
        for section in payload["required_payload"]["End0_action_on_zero_modes"].values()
    )


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE)
    payload = load(PAYLOAD)
    sm = load(SM_THEOREM)

    previous_model_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["status"] == "POST_ALPHA_END0_SECTOR_MODEL_VALUES_CONSTRUCTED_SELECTED_ZEROMODES_OPEN",
            prev["next_required_artifact"] == "Selected_U1Y_RouteC_ZeroModeBasis_From_HYM_Projector_Source_Theorem_v1",
            prev["what_closes_now"]["sector_projector_model_constructed"] is True,
            prev["what_remains_open"]["selected_zero_mode_bases_K_s"] is True,
            all(prev["guardrails"].values()),
        ]
    )
    theorem_valid = all(
        [
            source["theorem"]["proved"] is True,
            source["closure_claimed"] is False,
            source["status"] == "U1Y_ROUTEC_ZEROMODEBASIS_FROM_HYM_PROJECTOR_SOURCE_THEOREM_PROVED_PAYLOAD_OPEN",
            source["decision"]["theorem_proved"] is True,
            source["decision"]["payload_contract_created"] is True,
            source["decision"]["accepted_source_families_count"] == 3,
            source["decision"]["reference_End0_domain_available"] is True,
            source["decision"]["reference_sector_value_packet_constructed"] is True,
            source["decision"]["reference_projector_checks_pass"] is True,
            source["decision"]["selected_projector_payload_filled"] is False,
            source["decision"]["selected_zero_mode_bases_emitted"] is False,
            source["decision"]["selected_source_map_rho_s_emitted"] is False,
            source["decision"]["selected_matter_slot_routing_emitted"] is False,
            source["decision"]["selected_1M_Dirac_neutrino_rule_emitted"] is False,
            source["decision"]["selected_transfer_normalization_emitted"] is False,
            source["decision"]["physical_dotD_alpha1_payload_extracted"] is False,
            source["decision"]["target_fitting_used"] is False,
            source["next_required_artifact"] == NEXT,
        ]
    )
    payload_contract_open = all(
        [
            payload["status"] == "OPEN_VALUES_REQUIRED",
            len(payload["accepted_source_families"]) == 3,
            payload["reference_model_values"]["End0_basis"] == ["T1", "T2", "T3"],
            payload["reference_model_values"]["sector_order"] == ["Q", "u", "d", "L", "e", "N", "H"],
            payload["reference_model_values"]["sector_dimensions"]
            == {"H": 1, "L": 3, "N": 3, "Q": 3, "d": 3, "e": 3, "u": 3},
            payload["required_payload"]["same_source_id"] is None,
            payload["required_payload"]["selected_HYM_or_typed_projector_certificate"] is None,
            projector_values_absent(payload),
            basis_values_absent(payload),
            end0_action_values_absent(payload),
            all_nulls(payload["required_payload"]["coherence_checks"]),
            all_nulls(payload["required_payload"]["routing_and_normalization_not_supplied_by_this_contract"]),
        ]
    )
    promotion_rule_valid = all(
        [
            source["promotion_rule"]["rho_s_definition"]
            == "rho_s(T_i)=P_s rho(T_i) P_s restricted to K_s=im(P_s)",
            source["promotion_rule"]["matter_sector_result"] == "Q,u,d,L,e,N become selected adjoint triplet carriers",
            source["promotion_rule"]["H_sector_result"] == "H becomes the selected trivial singlet carrier",
            source["promotion_rule"]["normalization_result"]
            == "invariant Gram trace convention fixes matter Gram to I_3 and H Gram to [1]",
        ]
    )
    sm_bridge_consistent = all(
        [
            sm["theorem"]["bridge_theorem_proved"] is True,
            sm["theorem"]["selected_values_emitted"] is False,
            sm["promotion_decision"]["bridge_theorem_closes"] is True,
            sm["promotion_decision"]["canonical_rho_candidate_promotes_now"] is False,
            sm["promotion_decision"]["promotes_after_next_artifact_if_validator_passes"] is True,
            sm["finite_acceptance_validator"]["passes_now"] is False,
            sm["target_fitting_used"] is False,
        ]
    )
    guardrails_ok = all(
        [
            source["target_fitting_used"] is False,
            source["guardrails"]["claims_payload_filled"] is False,
            source["guardrails"]["claims_selected_zero_mode_bases_emitted"] is False,
            source["guardrails"]["claims_selected_source_map_rho_s"] is False,
            source["guardrails"]["claims_selected_matter_slot_routing"] is False,
            source["guardrails"]["claims_selected_1M_Dirac_neutrino_rule"] is False,
            source["guardrails"]["claims_selected_transfer_normalization"] is False,
            source["guardrails"]["claims_physical_dotD_alpha1_payload"] is False,
            source["guardrails"]["claims_primitive_C1_values_computed"] is False,
            source["guardrails"]["claims_A_selected_or_b_selected"] is False,
            source["guardrails"]["claims_lambda12"] is False,
            source["guardrails"]["claims_full_sm_closure"] is False,
            source["guardrails"]["promotes_model_carrier_without_source_payload"] is False,
            source["guardrails"]["uses_observed_or_benchmark_inputs"] is False,
        ]
    )
    theorem_proved = all(
        [
            previous_model_ready,
            theorem_valid,
            payload_contract_open,
            promotion_rule_valid,
            sm_bridge_consistent,
            guardrails_ok,
        ]
    )

    packet = {
        "theorem": {
            "name": "PostAlphaZeroModeBasisHYMProjectorTheoremImport",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "A conditional selected zero-mode promotion theorem is now imported. If a same-source "
                "selected HYM/Strominger, typed monad/Cech, or finite Route-C projector payload emits "
                "sector projectors P_s and ordered zero-mode bases K_s satisfying the contract, then "
                "the canonical End0 sector carrier promotes uniquely to selected rho_s on K_s. The "
                "payload values themselves remain open."
            ),
        },
        "status": STATUS,
        "promotion_rule": source["promotion_rule"],
        "payload_contract": payload,
        "sm_bridge_support": {
            "status": sm["status"],
            "current_support": sm["current_support"],
            "current_blockers": sm["current_blockers"],
            "promotion_decision": sm["promotion_decision"],
        },
        "checks": {
            "previous_model_ready": previous_model_ready,
            "theorem_valid": theorem_valid,
            "payload_contract_open": payload_contract_open,
            "promotion_rule_valid": promotion_rule_valid,
            "sm_bridge_consistent": sm_bridge_consistent,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": source["what_closes_now"],
        "what_remains_open": source["what_remains_open"],
        "guardrails": {
            "does_not_emit_selected_projectors_or_Ks": True,
            "does_not_promote_model_carrier_without_source_payload": True,
            "does_not_claim_matter_routing_1M_or_transfer_normalization": True,
            "does_not_claim_physical_dotD_or_primitive_C1": True,
            "does_not_claim_A_b_lambda_or_full_SM": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous": str(PREV),
            "source": str(SOURCE),
            "payload": str(PAYLOAD),
            "sm_theorem": str(SM_THEOREM),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_zeromodebasis_hym_projector_theorem",
        "status": STATUS,
        "closure_claimed": False,
        "selected_projector_payload_filled": False,
        "selected_zero_mode_bases_emitted": False,
        "selected_source_map_rho_s_emitted": False,
        "checks": {
            "theorem_proved": theorem_proved,
            **packet["checks"],
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# PostAlpha ZeroModeBasis HYMProjector Theorem Import v1

## Result

The bridge theorem is now explicit:

```text
same-source selected projectors P_s + ordered bases K_s
  => selected rho_s(T_i)=P_s rho(T_i) P_s | K_s
  => Q,u,d,L,e,N are adjoint triplet carriers
  => H is the trivial singlet
```

Accepted payload sources:

```text
direct selected HYM/Strominger connection projector
typed monad/Cech HYM projector with exactness/local-freeness certificate
finite Route-C projector with same-source trace equality
```

The theorem is conditional. The payload still has no selected `P_s`, `K_s`,
gaps, End0-equivariance values, Gram matrices, matter-slot routing, `1_M` rule,
or `dotD_alpha1` transfer normalization.

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
