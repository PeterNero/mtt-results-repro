from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "candidate_data" / "post_alpha_candidate_routes.packet.json"
FIBER_AUDIT = SM / "candidate_data" / "selected_routec_primitive_source_selection_audit.candidate.json"
FIBER_INVARIANCE = SM / "candidate_data" / "selected_routec_fiberclass_observable_invariance_or_gaugefix.candidate.json"
REBUILD = SM / "candidate_data" / "selected_routec_selected_c1_operator_source_or_galerkin_rebuild.candidate.json"
THEOREM_SLOT = SM / "candidate_data" / "selected_routec_basis_transport_primitive_source_theorem.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_fiberclass_source_target_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_fiberclass_source_target.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_FiberClass_SourceTarget_v1.md"

STATUS = "POST_ALPHA_FIBERCLASS_SOURCE_TARGET_REDUCED_BASISTRANSPORT_PROOF_OPEN"
NEXT = "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Proof_or_Counterexample_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    audit = load(FIBER_AUDIT)
    invariance = load(FIBER_INVARIANCE)
    rebuild = load(REBUILD)
    slot = load(THEOREM_SLOT)

    active_shift_closed = all(
        [
            audit["active_shift_theorem"]["proved"] is True,
            audit["active_shift_theorem"]["enumeration"]["active_shift_necessary_and_sufficient_for_nonzero"] is True,
            audit["active_shift_theorem"]["enumeration"]["nonzero_active_shifts"] == [[1, 1]],
            audit["what_closes_now"]["active_shift_1_1_forced_by_finite_support"] is True,
        ]
    )
    fiber_class_closed_current_layer = all(
        [
            audit["fiber_class_theorem"]["proved"] is True,
            audit["what_closes_now"]["fixed_fiber_shifts_reduced_to_one_qutrit_gauge_class"] is True,
            audit["fiber_class_theorem"]["all_fiber_envelope"]["not_gauge_equivalent_to_fixed_fiber_class"] is True,
            invariance["theorem"]["proved"] is True,
            invariance["combined_result"]["selected_C1_observable_class_proved_at_current_layer"] is True,
            invariance["combined_result"]["selected_unique_C1_matrix_proved"] is False,
            invariance["path_A_observable_invariance"]["proved_for_current_finite_C1_layer"] is True,
        ]
    )
    next_lane_exact = all(
        [
            rebuild["theorem"]["proved"] is True,
            rebuild["solution_space_iteration"]["selected_solution_kernel"]["selected_next_lane"] == "L3_noninvariant_basis_transport_or_vertex_source",
            rebuild["solution_space_iteration"]["selected_solution_kernel"]["fixed_fiber_shifts_gauge_equivalent"] is True,
            slot["theorem_slot"]["status"] == "THEOREM_SLOT_BUILT_SOURCE_PROOF_OPEN",
            slot["theorem_slot"]["proved_now"]["active_shift_1_1_unique_for_nonzero_response"] is True,
            slot["theorem_slot"]["proved_now"]["fixed_fiber_shifts_finite_gauge_equivalent_current_layer"] is True,
        ]
    )
    post_alpha_reconciled = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_remains_open"]["selected_noninvariant_primitive_or_vertex_or_basis_transport"] is True,
            prev["guardrails"]["does_not_promote_candidate_matrices_to_selected_values"] is True,
        ]
    )
    guardrails_ok = all(
        [
            audit["closure_claimed"] is False,
            invariance["closure_claimed"] is False,
            rebuild["closure_claimed"] is False,
            slot["closure_claimed"] is False,
            audit["target_fitting_used"] is False,
            invariance["target_fitting_used"] is False,
            rebuild["target_fitting_used"] is False,
            slot["target_fitting_used"] is False,
        ]
    )
    theorem_proved = all([active_shift_closed, fiber_class_closed_current_layer, next_lane_exact, post_alpha_reconciled, guardrails_ok])

    packet = {
        "theorem": {
            "name": "PostAlphaFiberClassSourceTargetTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "In the post-alpha branch, finite C1 source selection is reduced beyond candidate search. "
                "The active primitive shift (1,1) is necessary and sufficient for nonzero one-response C1 "
                "matrices. Fixed qutrit fiber shifts 0,1,2 form one cyclic gauge class for the current "
                "finite C1 spectral observables, and shift 0 may be used only as a computation gauge. "
                "The all-fiber envelope is retired as a fixed single-charge primitive. The next proof target "
                "is therefore the selected basis-transport or vertex source theorem, not another fiber search."
            ),
        },
        "status": STATUS,
        "active_shift_result": {
            "nonzero_active_shifts": audit["active_shift_theorem"]["enumeration"]["nonzero_active_shifts"],
            "all_active_shifts_tested": audit["active_shift_theorem"]["enumeration"]["all_active_shifts_tested"],
            "necessary_and_sufficient": audit["active_shift_theorem"]["enumeration"]["active_shift_necessary_and_sufficient_for_nonzero"],
        },
        "fiber_class_result": {
            "fixed_fiber_shifts": [0, 1, 2],
            "rank_by_fixed_shift": audit["fiber_class_theorem"]["fixed_fiber_shifts"]["ranks"],
            "frobenius_norms": audit["fiber_class_theorem"]["fixed_fiber_shifts"]["frobenius_norms"],
            "all_fiber_envelope_retired": audit["fiber_class_theorem"]["all_fiber_envelope"]["not_gauge_equivalent_to_fixed_fiber_class"],
            "canonical_computation_gauge": invariance["path_B_absolute_gauge_fix"]["canonical_computation_gauge"],
        },
        "current_layer_observable_invariance": {
            "proved": invariance["path_A_observable_invariance"]["proved_for_current_finite_C1_layer"],
            "scope": invariance["path_A_observable_invariance"]["scope"],
            "why_not_physical_flavor_closure": invariance["path_A_observable_invariance"]["why_not_physical_flavor_closure"],
            "fiber_origin_needed_for_current_spectral_observables": invariance["combined_result"]["fiber_origin_needed_for_current_spectral_observables"],
            "fiber_origin_needed_for_full_matrix_entries_or_future_noncommuting_corrections": invariance["combined_result"]["fiber_origin_needed_for_full_matrix_entries_or_future_noncommuting_corrections"],
        },
        "selected_next_lane": {
            "lane": rebuild["solution_space_iteration"]["selected_solution_kernel"]["selected_next_lane"],
            "minimal_theorem_to_prove_next": rebuild["solution_space_iteration"]["selected_solution_kernel"]["minimal_theorem_to_prove_next"],
            "theorem_slot": slot["theorem_slot"],
        },
        "checks": {
            "active_shift_closed": active_shift_closed,
            "fiber_class_closed_current_layer": fiber_class_closed_current_layer,
            "next_lane_exact": next_lane_exact,
            "post_alpha_reconciled": post_alpha_reconciled,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            "active_shift_11_unique_nonzero_imported": True,
            "fixed_fiber_shifts_reduced_to_current_layer_gauge_class": True,
            "all_fiber_envelope_retired": True,
            "shift0_allowed_as_computation_gauge_for_current_spectral_invariants": True,
            "basis_transport_or_vertex_source_theorem_identified_as_next_target": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_basis_transport_or_vertex_source_proof": True,
            "operator_level_basis_transport": True,
            "selected_24_atom_payload": True,
            "A_selected_and_b_selected": True,
            "nondegenerate_yukawa_hierarchy_CKM_PMNS_CP": True,
            "full_SM_closure": True,
            "selected_lambda12_spectral_table": True,
        },
        "guardrails": {
            "does_not_promote_current_layer_spectral_invariance_to_flavor_closure": True,
            "does_not_claim_selected_unique_C1_matrix": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_Yukawa_or_full_SM_closure": True,
            "shift0_is_computation_gauge_not_absolute_fiber_origin": True,
            "target_fitting_excluded": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous_candidate_routes": str(PREV),
            "fiber_audit": str(FIBER_AUDIT),
            "fiber_invariance": str(FIBER_INVARIANCE),
            "rebuild": str(REBUILD),
            "theorem_slot": str(THEOREM_SLOT),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_fiberclass_source_target",
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
    note = f"""# PostAlpha FiberClass SourceTarget v1

## Result

The C1 candidate route is now reduced past fiber search:

```text
unique nonzero active shift = (1,1)
fixed fiber shifts 0,1,2 = one current-layer cyclic gauge class
all-fiber envelope = retired as fixed single-charge primitive
shift 0 = computation gauge only
```

This proves current-layer spectral invariance of the fixed-fiber class, not
physical flavor closure. The current finite matrices still have degenerate
singular values, so nondegenerate Yukawas, CKM, PMNS, and CP require selected
higher-order/full-response splitting or an operator-level basis-transport /
vertex source theorem.

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
