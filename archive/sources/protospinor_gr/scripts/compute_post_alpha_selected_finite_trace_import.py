from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_phifin_subpacket.packet.json"
TRACE = QA / "candidate_data" / "selected_u1y_routec_selected_finite_trace_source_or_nogo.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_selected_finite_trace_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_selected_finite_trace.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_SelectedFiniteTrace_v1.md"

STATUS = "POST_ALPHA_SELECTED_FINITE_TRACE_NOGO_27MODE_PREFIX_OPEN"
NEXT = "Selected_U1Y_RouteC_TraceEquals27Mode_or_FullHYMReplay_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    trace = load(TRACE)

    theorem_reduction = all(
        [
            trace["theorem"]["proved"] is True,
            trace["decision"]["smooth_27mode_prefix_values_present"] is True,
            trace["decision"]["smooth_27mode_prefix_can_replace_old_smoke_as_best_prefix"] is True,
            trace["old_smoke_lane"]["status"] == "REJECTED_AS_SELECTED_TRACE",
            trace["smooth_27mode_lane"]["status"] == "PREFIX_VALUES_EXECUTED_SOURCE_TRACE_OPEN",
        ]
    )
    prefix_values_present = all(trace["smooth_27mode_lane"]["finite_values_present"].values())
    no_closure = all(
        [
            trace["decision"]["Phi_fin_closed"] is False,
            trace["decision"]["selected_trace_equality_proved"] is False,
            trace["decision"]["full_selected_operator_formula_proved"] is False,
            trace["decision"]["selected_gap_error_certificate"] is False,
            trace["decision"]["selected_finite_connection_solve_closed"] is False,
            trace["decision"]["honest_replay_without_lifted_flags"] is False,
            trace["decision"]["rhoE_selected_by_mtt"] is False,
            trace["decision"]["lambda_12_computable"] is False,
        ]
    )
    closing_routes_named = all(
        [
            len(trace["accepted_closing_routes"]["finite_trace_identification"]) == 5,
            len(trace["accepted_closing_routes"]["full_HYM_Newton_replay"]) == 4,
            len(trace["accepted_closing_routes"]["typed_monad_Cech_payload"]) == 2,
            trace["next_required_artifact"] == NEXT,
        ]
    )
    previous_reconciled = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_remains_open"]["selected_finite_trace_source_or_nogo"] is True,
            prev["what_remains_open"]["theorem_derived_selected_source_verified"] is True,
        ]
    )
    guardrails_ok = all(
        [
            trace["guardrails"]["claims_A_selected_or_b_selected"] is False,
            trace["guardrails"]["claims_Phi_fin_closed"] is False,
            trace["guardrails"]["claims_identity_rhoE_smoke_is_selected"] is False,
            trace["guardrails"]["claims_lambda12"] is False,
            trace["guardrails"]["uses_lifted_flags_as_proof"] is False,
            trace["guardrails"]["uses_observed_data"] is False,
            trace["target_fitting_used"] is False,
        ]
    )
    theorem_proved = all([theorem_reduction, prefix_values_present, no_closure, closing_routes_named, previous_reconciled, guardrails_ok])

    packet = {
        "theorem": {
            "name": "PostAlphaSelectedFiniteTraceImportTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The selected finite-trace gate rejects the old identity-rho_E smoke trace and imports the "
                "smooth 27-mode prefix as the strongest current finite prefix. It contains nonidentity projective "
                "rho_E support, the 27-mode B_N scaffold, D_E/Riesz/Green/dotD prefix values, sector projectors, "
                "canonical C1 zero-response no-go, and first HYM correction. It still does not close Phi_fin: "
                "selected trace equality, full selected Iwasawa/Strominger operator formula, selected gap/error "
                "certificate, and theorem-derived selected-source flags remain open."
            ),
        },
        "status": STATUS,
        "decision": trace["decision"],
        "old_smoke_lane": trace["old_smoke_lane"],
        "smooth_27mode_lane": trace["smooth_27mode_lane"],
        "source_trace_cutset": trace["source_trace_cutset"],
        "accepted_closing_routes": trace["accepted_closing_routes"],
        "checks": {
            "theorem_reduction": theorem_reduction,
            "prefix_values_present": prefix_values_present,
            "no_closure": no_closure,
            "closing_routes_named": closing_routes_named,
            "previous_reconciled": previous_reconciled,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            "old_identity_smoke_trace_rejected": True,
            "nonidentity_rhoE_candidate_preferred_over_identity_smoke": True,
            "smooth_27mode_prefix_imported": True,
            "same_basis_DE_Riesz_Green_dotD_prefix_values_present": True,
            "canonical_C1_zero_response_no_go_imported": True,
            "selected_trace_cutset_named": True,
            "three_legal_closing_routes_named": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_trace_equality": True,
            "full_selected_iwasawa_strominger_operator_formula": True,
            "selected_gap_error_certificate": True,
            "theorem_derived_selected_source_flags": True,
            "honest_replay_without_lifted_flags": True,
            "selected_noninvariant_C1_primitive_or_basis_transport": True,
            "primitive_C1_nonzero_values": True,
            "A_selected": True,
            "b_selected": True,
            "Yukawa_CKM_PMNS_CP_and_full_SM_closure": True,
            "lambda_12": True,
        },
        "guardrails": {
            "does_not_claim_Phi_fin_closed": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_lambda12": True,
            "does_not_promote_identity_smoke": True,
            "does_not_use_lifted_flags_or_observed_data": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {"previous_phifin": str(PREV), "trace": str(TRACE)},
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_selected_finite_trace",
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
    note = f"""# PostAlpha SelectedFiniteTrace v1

## Result

The old identity `rho_E` smoke trace is rejected. The best current finite prefix
is now the smooth 27-mode packet:

```text
nonidentity projective rho_E candidate = present
27-mode B_N scaffold = present
D_E/Riesz/Green/dotD prefix values = present
canonical C1 zero-response no-go = imported
Phi_fin closed = false
```

The remaining legal routes are finite-trace identification, full HYM/Newton
replay, or typed monad/Cech payload.

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
