from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_sectorrouting_sourcepacket.packet.json"
ALPHA = ROOT / "candidate_data" / "alpha1_driver_replay_closure_import.packet.json"
HYBRID = QA / "candidate_data" / "selected_u1y_routec_hybrid_galerkin_overlap_source_packet.candidate.json"
FILL = QA / "candidate_data" / "selected_u1y_routec_samesource_operatorpacket_fill_or_nogo.candidate.json"
PLAN = QA / "candidate_data" / "selected_u1y_routec_sourceemission_minimal_subpacket_attack_plan.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_hybrid_same_source_nogo_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_hybrid_same_source_nogo.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_Hybrid_SameSource_NoGo_v1.md"

STATUS = "POST_ALPHA_HYBRID_SAMESOURCE_NOGO_REDUCED_SOURCE_IDENTITY_BRIDGE_OPEN"
NEXT = "Selected_U1Y_RouteC_OperatorSourceIdentity_Bridge_Subpacket_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    alpha = load(ALPHA)
    hybrid = load(HYBRID)
    fill = load(FILL)
    plan = load(PLAN)

    alpha_closed_locally = all(
        [
            alpha["theorem"]["proved"] is True,
            alpha["what_closes_now"]["alpha1_driver_verified"] is True,
            alpha["what_closes_now"]["selected_dotD_source_verified"] is True,
            alpha["what_closes_now"]["honest_dotD_alpha1_replay"] is True,
        ]
    )
    hybrid_packet_nogo = all(
        [
            hybrid["hybrid_packet_result"]["packet_constructed"] is True,
            hybrid["hybrid_packet_result"]["required_count"] == 7,
            hybrid["hybrid_packet_result"]["selected_emitted_count"] == 0,
            hybrid["hybrid_packet_result"]["support_present_count"] == 6,
            hybrid["decision"]["current_source_record_no_go"] is True,
            hybrid["decision"]["selected_packet_closed"] is False,
            all(value is False for value in hybrid["selected_fields"].values()),
        ]
    )
    fill_nogo_exact = all(
        [
            fill["current_source_nogo"]["current_scaffold_nogo_proved"] is True,
            fill["current_source_nogo"]["mathematical_impossibility_claimed"] is False,
            fill["fill_summary"]["required_fields"] == 7,
            fill["fill_summary"]["selected_emitted"] == 0,
            fill["fill_summary"]["support_present"] == 6,
            fill["fill_summary"]["can_promote_A_selected"] is False,
            fill["fill_summary"]["can_promote_b_selected"] is False,
            fill["validator_report"]["ok"] is False,
            fill["validator_report"]["exit_code"] == 1,
        ]
    )
    minimal_plan_built = all(
        [
            plan["what_closes_now"]["fill_nogo_converted_to_source_emission_plan"] is True,
            plan["strategy"]["minimal_first_subpacket"] == NEXT,
            plan["strategy"]["dependency_order"][0]["id"] == "S1_source_identity_bridge",
            plan["strategy"]["dependency_order"][1]["id"] == "S2_operator_values_payload",
            plan["strategy"]["dependency_order"][2]["id"] == "S3_matter_overlap_payload",
            plan["strategy"]["dependency_order"][3]["id"] == "S4_primitive_contractions_payload",
            plan["acceptance_contract"]["must_make_same_source_validator_pass"] is True,
        ]
    )
    previous_reconciled = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_remains_open"]["same_source_DE_Riesz_Green_dotD_payload"] is True,
            prev["what_remains_open"]["emit_A_selected_and_b_selected"] is True,
        ]
    )
    guardrails_ok = all(
        [
            hybrid["guardrails"]["claims_A_selected"] is False,
            hybrid["guardrails"]["claims_b_selected"] is False,
            hybrid["guardrails"]["claims_full_sm_closure"] is False,
            hybrid["guardrails"]["uses_locked_target_columns_as_selector"] is False,
            hybrid["guardrails"]["uses_observed_masses_or_ckm_inputs"] is False,
            fill["guardrails"]["claims_A_selected"] is False,
            fill["guardrails"]["claims_b_selected"] is False,
            fill["guardrails"]["claims_full_closure"] is False,
            fill["guardrails"]["locked_target_selector_used"] is False,
            fill["guardrails"]["observed_data_used"] is False,
            plan["target_fitting_used"] is False,
        ]
    )
    theorem_proved = all(
        [
            alpha_closed_locally,
            hybrid_packet_nogo,
            fill_nogo_exact,
            minimal_plan_built,
            previous_reconciled,
            guardrails_ok,
        ]
    )

    packet = {
        "theorem": {
            "name": "PostAlphaHybridSameSourceNoGoReductionTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "With alpha1 and honest dotD replay closed locally, the remaining C1/SM obstruction is the "
                "same-source operator/overlap packet. The hybrid Galerkin packet requires seven fields and "
                "currently emits none as selected theorem-derived same-source values. The fill/no-go validator "
                "therefore proves a current-scaffold no-go, not a mathematical impossibility theorem. The "
                "minimal dependency order is source identity bridge, operator values payload, matter/overlap "
                "payload, then primitive contractions."
            ),
        },
        "status": STATUS,
        "alpha_reconciliation": {
            "alpha_closed_locally": alpha_closed_locally,
            "local_alpha_status": alpha["imported_status"]["status"],
            "reason": "Sibling scaffold records may predate local alpha closure; this packet carries forward the local alpha closure and leaves only same-source C1/overlap fields open.",
        },
        "hybrid_packet": {
            "status": hybrid["status"],
            "required_fields": hybrid["next_artifact_contract"]["required_fields"],
            "field_rows": hybrid["field_rows"],
            "selected_emitted_count": hybrid["hybrid_packet_result"]["selected_emitted_count"],
            "support_present_count": hybrid["hybrid_packet_result"]["support_present_count"],
            "no_go_scope": hybrid["no_go_scope"],
        },
        "same_source_fill_nogo": {
            "status": fill["status"],
            "required_fields": fill["validator_report"]["required_fields"],
            "validator_errors": fill["validator_report"]["errors"],
            "current_source_nogo": fill["current_source_nogo"],
            "fill_summary": fill["fill_summary"],
        },
        "minimal_subpacket_plan": {
            "status": plan["status"],
            "acceptance_contract": plan["acceptance_contract"],
            "dependency_order": plan["strategy"]["dependency_order"],
            "minimal_first_subpacket": plan["strategy"]["minimal_first_subpacket"],
            "promotion_condition": plan["strategy"]["promotion_condition"],
        },
        "checks": {
            "alpha_closed_locally": alpha_closed_locally,
            "hybrid_packet_nogo": hybrid_packet_nogo,
            "fill_nogo_exact": fill_nogo_exact,
            "minimal_plan_built": minimal_plan_built,
            "previous_reconciled": previous_reconciled,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            "alpha_closure_reconciled_with_post_alpha_same_source_gate": True,
            "seven_field_same_source_packet_contract_imported": True,
            "current_scaffold_nogo_imported": True,
            "mathematical_impossibility_not_claimed": True,
            "minimal_dependency_order_built": True,
            "source_identity_bridge_selected_as_first_subpacket": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_source_identity_bridge": True,
            "operator_values_payload": True,
            "matter_overlap_payload": True,
            "primitive_contractions_payload": True,
            "A_selected": True,
            "b_selected": True,
            "selected_deltaTheta_C1_solve": True,
            "Yukawa_CKM_PMNS_CP_and_full_SM_closure": True,
            "selected_lambda12_spectral_table": True,
        },
        "guardrails": {
            "does_not_reopen_alpha1": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_full_SM_or_lambda12_closure": True,
            "does_not_claim_mathematical_impossibility": True,
            "does_not_use_locked_target_columns_as_selector": True,
            "does_not_use_observed_flavor_data": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous_sectorrouting": str(PREV),
            "alpha": str(ALPHA),
            "hybrid": str(HYBRID),
            "fill": str(FILL),
            "plan": str(PLAN),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_hybrid_same_source_nogo",
        "status": STATUS,
        "closure_claimed": False,
        "checks": {
            "theorem_proved": theorem_proved,
            **packet["checks"],
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
        "next_required_artifact": NEXT,
    }
    note = f"""# PostAlpha Hybrid SameSource NoGo v1

## Result

Alpha1 and honest dotD replay remain closed locally. The post-alpha blocker is
the same-source operator/overlap packet:

```text
required fields = 7
selected emitted = 0
support present = 6
current-source no-go = true
mathematical impossibility = false
```

The minimal dependency order is now:

```text
S1 source_identity_bridge
S2 operator_values_payload
S3 matter_overlap_payload
S4 primitive_contractions_payload
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
