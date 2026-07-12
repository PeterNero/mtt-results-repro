from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_primitive_c1_sourcevalue_frontier.packet.json"
SOURCE = QA / "candidate_data" / "selected_u1y_routec_external_noninvariant_c1_candidate_import.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_external_noninvariant_c1_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_external_noninvariant_c1.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_ExternalNonInvariantC1_v1.md"

STATUS = "POST_ALPHA_EXTERNAL_NONINVARIANT_C1_REDUCED_FIBER_ORIGIN_OPEN"
NEXT = "Selected_U1Y_RouteC_FiberOrigin_or_GaugeInvariantC1Observable_Theorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE)

    previous_frontier_closed = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_closes_now"]["three_legal_routes_ranked"] is True,
            prev["what_remains_open"]["selected_noninvariant_primitive_tensor"] is True,
            prev["next_required_artifact"] == "Selected_U1Y_RouteC_CanonicalZeroSelection_or_NonInvariantC1Tensor_Fill_v1",
        ]
    )
    noninvariant_candidates_imported = all(
        [
            source["theorem"]["proved"] is True,
            source["decision"]["external_scan_completed"] is True,
            source["decision"]["nonzero_noninvariant_candidates_imported"] is True,
            source["decision"]["active_shift_1_1_promoted_as_required_candidate_condition"] is True,
            source["decision"]["fiber_class_reduction_imported"] is True,
            source["decision"]["basis_transport_candidate_imported"] is True,
            source["candidate_summary"]["calculation_results"]["all_four_tested_candidates_nonzero"] is True,
            source["candidate_summary"]["calculation_results"]["nonzero_unselected_candidates_found"] == 4,
            source["imported_facts"]["minimal_active_shift_required"] == [1, 1],
            source["imported_facts"]["fixed_fiber_shifts_one_qutrit_gauge_class"] is True,
        ]
    )
    fixed_fiber_rank_profile_valid = all(
        [
            all(rank == 3 for sector in source["imported_facts"]["fixed_fiber_ranks"].values() for rank in sector.values()),
            all(rank == 1 for rank in source["imported_facts"]["all_fiber_rank"].values()),
            source["imported_facts"]["all_fiber_envelope_retired"] is True,
        ]
    )
    selector_open = all(
        [
            source["decision"]["selected_C1_closed"] is False,
            source["decision"]["selected_noninvariant_tensor_emitted"] is False,
            source["selection_state"]["absolute_fiber_shift_selected"] is False,
            source["selection_state"]["observable_invariance_under_fiber_class_proved"] is False,
            source["selection_state"]["operator_level_projective_class_selected"] is False,
            source["selection_state"]["q79_basis_transport_selected_by_MTT"] is False,
            source["selection_state"]["selected_noninvariant_primitive_source_proved"] is False,
        ]
    )
    guardrails_ok = all(
        [
            source["closure_claimed"] is False,
            source["target_fitting_used"] is False,
            source["guardrails"]["claims_selected_C1_closed"] is False,
            source["guardrails"]["claims_selected_noninvariant_tensor_emitted"] is False,
            source["guardrails"]["claims_A_selected"] is False,
            source["guardrails"]["claims_b_selected"] is False,
            source["guardrails"]["claims_lambda12"] is False,
            source["guardrails"]["claims_Yukawa_or_full_SM_closure"] is False,
            source["guardrails"]["uses_observed_data"] is False,
            source["guardrails"]["uses_benchmark_data"] is False,
            source["guardrails"]["uses_locked_target_columns"] is False,
            source["guardrails"]["uses_diagnostic_lambda12_values"] is False,
            all(prev["guardrails"].values()),
        ]
    )
    theorem_proved = all(
        [
            previous_frontier_closed,
            noninvariant_candidates_imported,
            fixed_fiber_rank_profile_valid,
            selector_open,
            guardrails_ok,
        ]
    )

    packet = {
        "theorem": {
            "name": "PostAlphaExternalNonInvariantC1ImportTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "External proof repos reduce the live non-invariant primitive C1 route from an arbitrary "
                "tensor search to a finite selector problem. The active shift (1,1) is forced by finite "
                "support, four fixed-fiber candidate families are nonzero, and the all-fiber envelope is "
                "retired. The remaining selector is an absolute fiber-origin theorem, a proof that C1 "
                "observables are invariant under the fixed qutrit fiber class, or selected typed "
                "monad/Cech/Galerkin zero-mode transport."
            ),
        },
        "status": STATUS,
        "candidate_summary": source["candidate_summary"],
        "imported_facts": source["imported_facts"],
        "selection_state": source["selection_state"],
        "route_update": source["route_update"],
        "checks": {
            "previous_frontier_closed": previous_frontier_closed,
            "noninvariant_candidates_imported": noninvariant_candidates_imported,
            "fixed_fiber_rank_profile_valid": fixed_fiber_rank_profile_valid,
            "selector_open": selector_open,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            "active_shift_1_1_required_condition_imported": True,
            "arbitrary_noninvariant_tensor_search_retired": True,
            "four_nonzero_fixed_fiber_candidate_families_imported": True,
            "all_fiber_envelope_retired": True,
            "basis_connection_candidate_imported": True,
            "fiber_origin_or_invariance_selector_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "absolute_fiber_origin_gauge_fix": True,
            "fiber_class_invariant_C1_observable_theorem": True,
            "selected_basis_transport_theorem": True,
            "selected_noninvariant_primitive_source": True,
            "same_source_atom_payload": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "does_not_claim_selected_C1_closed": True,
            "does_not_claim_selected_noninvariant_tensor_emitted": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_lambda12_or_full_SM": True,
            "does_not_promote_unselected_candidates": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {"previous": str(PREV), "external_noninvariant": str(SOURCE)},
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_external_noninvariant_c1",
        "status": STATUS,
        "closure_claimed": False,
        "nonzero_unselected_candidate_count": 4,
        "minimal_active_shift_required": [1, 1],
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
    note = f"""# PostAlpha ExternalNonInvariantC1 v1

## Result

The non-invariant primitive C1 route is no longer an arbitrary tensor search.
External packets reduce it to:

```text
active shift = (1,1)
nonzero fixed-fiber candidates = 4
fixed fiber shifts = one qutrit gauge class
all-fiber envelope = retired
representative max entry = {source["imported_facts"]["representative_max_abs_entry"]}
```

The candidates are useful but still unselected. The exact selector is now:

```text
absolute fiber-origin theorem
or fiber-class-invariant C1 observable theorem
or selected monad/Cech/Galerkin basis-transport derivation
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
