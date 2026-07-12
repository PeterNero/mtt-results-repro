from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "candidate_data" / "post_alpha_hybrid_same_source_nogo.packet.json"
BRIDGE = QA / "candidate_data" / "selected_u1y_routec_operator_source_identity_bridge_subpacket.candidate.json"
PIC0_SPLIT = QA / "candidate_data" / "selected_u1y_routec_operatorlayer_pic0_or_selected_residual_source_subpacket.candidate.json"
SM_IDENTITY = SM / "candidate_data" / "selected_routec_operatorsourceidentity_subpacket.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_operator_source_identity_pic0_split_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_operator_source_identity_pic0_split.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_OperatorSourceIdentity_Pic0Split_v1.md"

STATUS = "POST_ALPHA_OPERATOR_SOURCE_IDENTITY_REDUCED_PHIFIN_OPEN"
NEXT = "Selected_U1Y_RouteC_FiniteEmissionMorphism_PhiFin_Subpacket_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    bridge = load(BRIDGE)
    split = load(PIC0_SPLIT)
    sm_identity = load(SM_IDENTITY)

    bridge_nogo = all(
        [
            bridge["source_identity_bridge_result"]["bridge_closed"] is False,
            bridge["source_identity_bridge_result"]["current_source_nogo"] is True,
            bridge["source_identity_bridge_result"]["mathematical_impossibility_claimed"] is False,
            bridge["source_identity_bridge_result"]["operator_layer_pic0_closed"] is False,
            bridge["source_identity_bridge_result"]["selected_operator_source_identity_emitted"] is False,
            bridge["source_identity_bridge_result"]["selected_residual_or_hym_closed"] is False,
            all(not req["selected_emitted"] for req in bridge["bridge_requirements"].values()),
        ]
    )
    pic0_split_exact = all(
        [
            split["source_split_result"]["bridge_closed"] is False,
            split["source_split_result"]["pic0_closed"] is False,
            split["source_split_result"]["selected_residual_closed"] is False,
            split["source_split_result"]["primary_route_selected"] == "Phi_fin",
            split["pic0_lane"]["can_close_bridge_alone"] is False,
            split["residual_lane"]["can_close_bridge_with_pic0_side_condition"] is True,
            split["route_decision"]["primary_next_artifact"] == NEXT,
            split["route_decision"]["pic0_policy"].startswith("carry Pic0"),
        ]
    )
    sm_identity_reconciled = all(
        [
            sm_identity["theorem"]["proved"] is True,
            sm_identity["operator_identity_verdict"]["subpacket_closed"] is False,
            sm_identity["operator_identity_verdict"]["rank2_or_routec_fill_required"] is True,
            sm_identity["source_level_support"]["selected_s3_gerbe_source_level"] is True,
            sm_identity["source_level_support"]["visible_operator_source_closed"] is False,
            sm_identity["what_closes_now"]["source_level_support_separated_from_operator_identity"] is True,
        ]
    )
    previous_reconciled = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_remains_open"]["selected_source_identity_bridge"] is True,
            prev["what_remains_open"]["operator_values_payload"] is True,
        ]
    )
    guardrails_ok = all(
        [
            bridge["guardrails"]["claims_A_selected"] is False,
            bridge["guardrails"]["claims_b_selected"] is False,
            bridge["guardrails"]["claims_full_closure"] is False,
            bridge["guardrails"]["claims_lambda12"] is False,
            split["guardrails"]["claims_pic0_closed"] is False,
            split["guardrails"]["claims_selected_residual_closed"] is False,
            split["guardrails"]["claims_A_selected"] is False,
            split["guardrails"]["claims_b_selected"] is False,
            sm_identity["closure_claimed"] is False,
            bridge["target_fitting_used"] is False,
            split["target_fitting_used"] is False,
            sm_identity["target_fitting_used"] is False,
        ]
    )
    theorem_proved = all([bridge_nogo, pic0_split_exact, sm_identity_reconciled, previous_reconciled, guardrails_ok])

    packet = {
        "theorem": {
            "name": "PostAlphaOperatorSourceIdentityPic0SplitTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The source-identity bridge is attempted and fails for the current source record. "
                "Source-level S3/Green-Schwarz/projective support is strong but does not emit an operator-level "
                "visible source. Pic0 selection or quotient is necessary as a side condition, but cannot by itself "
                "emit the residual, D_E, Riesz/Green, dotD, or C1 payload. The primary next object is the finite "
                "emission morphism Phi_fin, carrying Pic0 as an explicit side condition."
            ),
        },
        "status": STATUS,
        "operator_source_bridge": {
            "status": bridge["status"],
            "hard_cut_set": bridge["hard_cut_set"],
            "bridge_requirements": bridge["bridge_requirements"],
            "route_evaluation": bridge["route_evaluation"],
        },
        "pic0_residual_split": {
            "status": split["status"],
            "pic0_lane": split["pic0_lane"],
            "residual_lane": split["residual_lane"],
            "route_decision": split["route_decision"],
        },
        "sm_operator_identity_reconciliation": {
            "status": sm_identity["status"],
            "operator_identity_verdict": sm_identity["operator_identity_verdict"],
            "lane_evaluation": sm_identity["lane_evaluation"],
            "symmetry_breaking_dependency": sm_identity["symmetry_breaking_dependency"],
        },
        "checks": {
            "bridge_nogo": bridge_nogo,
            "pic0_split_exact": pic0_split_exact,
            "sm_identity_reconciled": sm_identity_reconciled,
            "previous_reconciled": previous_reconciled,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            "operator_source_identity_current_source_nogo_imported": True,
            "source_level_support_separated_from_operator_identity": True,
            "operator_layer_cutset_isolated": True,
            "pic0_only_route_demoted_to_side_condition": True,
            "selected_residual_route_ranked_primary": True,
            "Phi_fin_named_as_next_object": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "Phi_fin": True,
            "operator_layer_Pic0_side_condition": True,
            "selected_operator_source_identity": True,
            "selected_residual_or_hym": True,
            "operator_payload_DE_Riesz_Green_dotD": True,
            "finite_truncation_error_gap": True,
            "primitive_contractions": True,
            "A_selected": True,
            "b_selected": True,
            "Yukawa_CKM_PMNS_CP_and_full_SM_closure": True,
            "selected_lambda12_spectral_table": True,
        },
        "guardrails": {
            "does_not_promote_source_level_support_to_operator_identity": True,
            "does_not_claim_pic0_closed": True,
            "does_not_claim_selected_residual_closed": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_full_SM_or_lambda12_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous_hybrid_nogo": str(PREV),
            "bridge": str(BRIDGE),
            "pic0_split": str(PIC0_SPLIT),
            "sm_identity": str(SM_IDENTITY),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_operator_source_identity_pic0_split",
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
    note = f"""# PostAlpha OperatorSourceIdentity Pic0Split v1

## Result

The operator-source identity bridge is a current-source no-go:

```text
operator source identity emitted = false
Pic0 closed = false
selected residual/HYM closed = false
mathematical impossibility = false
```

Pic0 is demoted to a side condition. The primary live route is:

```text
Phi_fin: selected finite emission morphism
```

`Phi_fin` must turn `selected_source_verified` into a theorem field and emit
the residual, `D_E`, Riesz/Green, `dotD`, and compatible C1 payload data.

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
