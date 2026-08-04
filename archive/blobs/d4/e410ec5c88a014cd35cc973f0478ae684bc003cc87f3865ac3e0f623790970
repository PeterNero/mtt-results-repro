from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_operator_source_identity_pic0_split.packet.json"
PHIFIN = QA / "candidate_data" / "selected_u1y_routec_finite_emission_morphism_phifin_subpacket.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_phifin_subpacket_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_phifin_subpacket.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_PhiFin_Subpacket_v1.md"

STATUS = "POST_ALPHA_PHIFIN_SUBPACKET_BUILT_SELECTED_FINITE_TRACE_OPEN"
NEXT = "Selected_U1Y_RouteC_SelectedFiniteTrace_SourceOrNoGo_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    phifin = load(PHIFIN)

    contract_bound = all(
        [
            phifin["theorem"]["proved"] is True,
            phifin["decision"]["domain_lock_closed"] is True,
            phifin["decision"]["finite_trace_scaffold_constructed"] is True,
            phifin["what_closes_now"]["Phi_fin_contract_bound_to_actual_payloads"] is True,
            phifin["what_closes_now"]["selected_smoke_promotion_rejected"] is True,
        ]
    )
    no_promotion = all(
        [
            phifin["decision"]["Phi_fin_constructed"] is False,
            phifin["decision"]["commuting_projection_proved"] is False,
            phifin["decision"]["selected_basis_B_N_emitted"] is False,
            phifin["decision"]["selected_error_gap_certificate_emitted"] is False,
            phifin["decision"]["selected_operator_payload_emitted"] is False,
            phifin["decision"]["primitive_C1_tensors_emitted"] is False,
            phifin["acceptance_tests"]["selected_source_verified_theorem_derived"] is False,
            phifin["acceptance_tests"]["validators_pass_honestly"] is False,
        ]
    )
    stage_status_exact = all(
        [
            phifin["stage_checks"][0]["stage"] == "domain_lock" and phifin["stage_checks"][0]["passes"] is True,
            all(stage["passes"] is False for stage in phifin["stage_checks"][1:]),
            phifin["stage_checks"][1]["stage"] == "finite_basis",
            phifin["stage_checks"][2]["stage"] == "projection_commuting_square",
            phifin["stage_checks"][3]["stage"] == "finite_operator_payload",
            phifin["stage_checks"][4]["stage"] == "error_gap_certificate",
        ]
    )
    previous_reconciled = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_remains_open"]["Phi_fin"] is True,
            prev["what_remains_open"]["operator_payload_DE_Riesz_Green_dotD"] is True,
        ]
    )
    guardrails_ok = all(
        [
            phifin["guardrails"]["claims_A_selected"] is False,
            phifin["guardrails"]["claims_b_selected"] is False,
            phifin["guardrails"]["claims_Phi_fin_closed"] is False,
            phifin["guardrails"]["claims_lambda12"] is False,
            phifin["guardrails"]["promotes_smoke_data"] is False,
            phifin["guardrails"]["uses_observed_data"] is False,
            phifin["target_fitting_used"] is False,
        ]
    )
    theorem_proved = all([contract_bound, no_promotion, stage_status_exact, previous_reconciled, guardrails_ok])

    packet = {
        "theorem": {
            "name": "PostAlphaPhiFinSubpacketImportTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The Phi_fin contract is bound to the current finite Route-C payloads and the fixed q79/F,m=1 "
                "domain support is closed. The present finite trace is validator-ready support only: selected "
                "finite basis emission, commuting projection proof, theorem-derived source verification, selected "
                "operator payload, selected gap/error certificate, and primitive C1 tensors remain absent. "
                "Therefore Phi_fin is not constructed, and the next gate is the selected finite-trace source/no-go."
            ),
        },
        "status": STATUS,
        "phifin_contract": phifin["contract"],
        "decision": phifin["decision"],
        "finite_trace_attempt": phifin["finite_trace_attempt"],
        "stage_checks": phifin["stage_checks"],
        "acceptance_tests": phifin["acceptance_tests"],
        "checks": {
            "contract_bound": contract_bound,
            "no_promotion": no_promotion,
            "stage_status_exact": stage_status_exact,
            "previous_reconciled": previous_reconciled,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            "Phi_fin_contract_bound_to_actual_payloads": True,
            "domain_lock_confirmed": True,
            "finite_trace_scaffold_summarized": True,
            "first_missing_selected_objects_named": True,
            "selected_smoke_promotion_rejected": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_finite_trace_source_or_nogo": True,
            "source_selected_basis_B_N_from_M_star": True,
            "commuting_projection_square": True,
            "theorem_derived_selected_source_verified": True,
            "selected_D_E_Riesz_Green_dotD": True,
            "selected_rhoE_metric_sector_maps": True,
            "selected_error_gap_certificate": True,
            "primitive_C1_overlap_tensors": True,
            "A_selected": True,
            "b_selected": True,
            "Yukawa_CKM_PMNS_CP_and_full_SM_closure": True,
            "selected_lambda12_spectral_table": True,
        },
        "guardrails": {
            "does_not_claim_Phi_fin_constructed": True,
            "does_not_promote_smoke_data": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_full_SM_or_lambda12_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {"previous_pic0_split": str(PREV), "phifin": str(PHIFIN)},
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_phifin_subpacket",
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
    note = f"""# PostAlpha PhiFin Subpacket v1

## Result

`Phi_fin` is bound to the current finite Route-C payloads, but it is not
constructed:

```text
domain lock = closed
finite trace scaffold = built
selected finite basis = open
commuting projection proof = open
theorem-derived selected_source_verified = open
primitive C1 tensors = open
```

The current payload is validator-ready support, not selected source data.

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
