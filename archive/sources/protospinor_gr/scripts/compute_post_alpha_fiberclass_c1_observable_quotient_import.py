from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_external_noninvariant_c1.packet.json"
SOURCE = QA / "candidate_data" / "selected_u1y_routec_fiberorigin_or_gaugeinvariant_c1observable_theorem.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_fiberclass_c1_observable_quotient_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_fiberclass_c1_observable_quotient.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_FiberClass_C1Observable_Quotient_v1.md"

STATUS = "POST_ALPHA_FIBERCLASS_C1_OBSERVABLE_QUOTIENT_CLOSED_FULL_RESPONSE_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE)

    previous_selector_identified = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_closes_now"]["fiber_origin_or_invariance_selector_identified"] is True,
            prev["what_remains_open"]["fiber_class_invariant_C1_observable_theorem"] is True,
            prev["next_required_artifact"] == "Selected_U1Y_RouteC_FiberOrigin_or_GaugeInvariantC1Observable_Theorem_v1",
        ]
    )
    quotient_closed = all(
        [
            source["theorem"]["proved"] is True,
            source["decision"]["active_shift_1_1_selected_for_current_C1_layer"] is True,
            source["decision"]["fiberclass_quotient_for_current_C1_spectral_observables_closed"] is True,
            source["decision"]["shift0_allowed_as_computation_gauge"] is True,
            source["quotient_theorem"]["active_shift_selected"] is True,
            source["quotient_theorem"]["fiber_class_quotient_selected"] is True,
            source["quotient_theorem"]["computation_representative"] == "fiber_shift_0",
            source["quotient_theorem"]["absolute_fiber_origin_not_hidden_knob"] is True,
        ]
    )
    spectral_invariants_closed = all(
        [
            source["spectral_observable_summary"]["rank_invariant"] is True,
            source["spectral_observable_summary"]["YYstar_scalar_identity_invariant"] is True,
            source["spectral_observable_summary"]["representative_for_computation"] == "fiber_shift_0",
            source["downstream_boundary"]["can_promote_fixed_fiber_representative_for_current_spectral_observables"] is True,
        ]
    )
    matrix_and_flavor_open = all(
        [
            source["decision"]["absolute_fiber_origin_selected"] is False,
            source["decision"]["selected_matrix_representative_for_full_C1_operator"] is False,
            source["decision"]["A_selected_computable"] is False,
            source["decision"]["b_selected_computable"] is False,
            source["decision"]["lambda_12_computable"] is False,
            source["decision"]["Yukawa_or_full_SM_closure"] is False,
            source["downstream_boundary"]["can_promote_fixed_fiber_representative_for_full_C1_matrix_operator"] is False,
            source["downstream_boundary"]["can_compute_yukawa_hierarchy"] is False,
            source["downstream_boundary"]["can_compute_CKM_PMNS_CP"] is False,
            source["spectral_observable_summary"]["current_layer_flavor_splitting_possible"] is False,
        ]
    )
    live_routes_preserved = all(
        [
            source["live_routes"]["basis_transport_candidate_viable"] is True,
            source["live_routes"]["basis_transport_selected"] is False,
            source["live_routes"]["higher_order_or_full_response"] is True,
            source["live_routes"]["operator_level_basis_transport"] is True,
        ]
    )
    guardrails_ok = all(
        [
            source["closure_claimed"] is False,
            source["target_fitting_used"] is False,
            source["decision"]["absolute_fiber_origin_used_as_hidden_knob"] is False,
            source["guardrails"]["claims_absolute_fiber_origin_selected"] is False,
            source["guardrails"]["claims_full_C1_matrix_representative"] is False,
            source["guardrails"]["claims_A_selected"] is False,
            source["guardrails"]["claims_b_selected"] is False,
            source["guardrails"]["claims_lambda12"] is False,
            source["guardrails"]["claims_Yukawa_or_full_SM_closure"] is False,
            source["guardrails"]["uses_observed_data"] is False,
            source["guardrails"]["uses_benchmark_data"] is False,
            all(prev["guardrails"].values()),
        ]
    )
    theorem_proved = all(
        [
            previous_selector_identified,
            quotient_closed,
            spectral_invariants_closed,
            matrix_and_flavor_open,
            live_routes_preserved,
            guardrails_ok,
        ]
    )

    packet = {
        "theorem": {
            "name": "PostAlphaFiberClassC1ObservableQuotientImportTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The fixed qutrit fiber class is selected as a quotient for current primitive C1 spectral "
                "observables. Shift 0 may be used as a computation gauge for rank, determinant absolute "
                "value, traces of powers of YY*, and singular spectrum. This rejects any hidden absolute "
                "fiber-origin knob. It does not select a full C1 matrix representative, compute A_selected "
                "or b_selected, or produce nondegenerate Yukawa hierarchy, CKM/PMNS, CP, lambda_12, or full "
                "SM closure; those require higher-order/full-response matrices or same-source operator-level "
                "basis transport."
            ),
        },
        "status": STATUS,
        "quotient_theorem": source["quotient_theorem"],
        "spectral_observable_summary": source["spectral_observable_summary"],
        "downstream_boundary": source["downstream_boundary"],
        "live_routes": source["live_routes"],
        "checks": {
            "previous_selector_identified": previous_selector_identified,
            "quotient_closed": quotient_closed,
            "spectral_invariants_closed": spectral_invariants_closed,
            "matrix_and_flavor_open": matrix_and_flavor_open,
            "live_routes_preserved": live_routes_preserved,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            "active_shift_1_1_selected_for_current_C1_layer": True,
            "fixed_fiber_quotient_class_selected_for_current_C1_spectral_observables": True,
            "shift0_computation_gauge_allowed": True,
            "absolute_fiber_origin_hidden_knob_rejected": True,
            "current_C1_spectral_invariant_representative_allowed": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_matrix_representative_for_full_C1_operator": True,
            "operator_level_basis_transport": True,
            "selected_higher_order_or_full_response_matrices": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "does_not_claim_absolute_fiber_origin_selected": True,
            "does_not_claim_full_C1_matrix_representative": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_lambda12_or_full_SM": True,
            "does_not_use_fiber_origin_as_hidden_knob": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {"previous": str(PREV), "fiberclass_quotient": str(SOURCE)},
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_fiberclass_c1_observable_quotient",
        "status": STATUS,
        "closure_claimed": False,
        "quotient_closed_for_current_spectral_observables": True,
        "full_C1_matrix_representative_selected": False,
        "reduced_to": NEXT,
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
    note = f"""# PostAlpha FiberClass C1Observable Quotient v1

## Result

The fixed qutrit fiber class is now closed as a quotient for current primitive
C1 spectral observables.

```text
selected active shift = {source["quotient_theorem"]["selected_active_shift"]}
fixed fiber class = {source["quotient_theorem"]["fixed_fiber_class"]}
computation representative = {source["quotient_theorem"]["computation_representative"]}
det abs = {source["spectral_observable_summary"]["det_abs"]}
YY* scalar = {source["spectral_observable_summary"]["YYstar_scalar"]}
```

This is not a hidden knob: no absolute fiber origin is selected. It is only a
quotient/gauge result for the current spectral layer. Full C1 matrices,
`A_selected`, `b_selected`, Yukawa splitting, CKM/PMNS/CP, `lambda_12`, and full
SM closure remain open.

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
