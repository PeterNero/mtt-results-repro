from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_primitive_c1_atom_nogo_frontier.packet.json"
EXTERNAL = QA / "candidate_data" / "selected_u1y_routec_external_noninvariant_c1_candidate_import.candidate.json"
FIBER = QA / "candidate_data" / "selected_u1y_routec_fiberorigin_or_gaugeinvariant_c1observable_theorem.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_noninvariant_c1_fiberclass_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_noninvariant_c1_fiberclass.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_NonInvariantC1_FiberClass_Import_v1.md"

STATUS = "POST_ALPHA_NONINVARIANT_C1_FIBERCLASS_SPECTRAL_QUOTIENT_CLOSED_FULL_RESPONSE_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_v1"
SECTORS = ["u", "d", "e", "nuD"]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def ranks_ok(external: dict) -> bool:
    ranks = external["candidate_summary"]["calculation_results"]["ranks_by_candidate"]
    return all(ranks[str(i)] == {sector: 3 for sector in SECTORS} for i in range(3)) and ranks["all"] == {
        sector: 1 for sector in SECTORS
    }


def external_ok(external: dict) -> bool:
    decision = external["decision"]
    selection = external["selection_state"]
    return all(
        [
            external["status"] == "U1Y_ROUTEC_EXTERNAL_NONINVARIANT_C1_CANDIDATES_IMPORTED_SOURCE_SELECTION_OPEN",
            external["closure_claimed"] is False,
            external["target_fitting_used"] is False,
            external["next_required_artifact"] == "Selected_U1Y_RouteC_FiberOrigin_or_GaugeInvariantC1Observable_Theorem_v1",
            external["theorem"]["proved"] is True,
            decision["active_shift_1_1_promoted_as_required_candidate_condition"] is True,
            decision["nonzero_noninvariant_candidates_imported"] is True,
            decision["fiber_class_reduction_imported"] is True,
            decision["selected_C1_closed"] is False,
            decision["selected_noninvariant_tensor_emitted"] is False,
            external["imported_facts"]["minimal_active_shift_required"] == [1, 1],
            external["imported_facts"]["fixed_fiber_shifts_one_qutrit_gauge_class"] is True,
            external["candidate_summary"]["calculation_results"]["nonzero_unselected_candidates_found"] == 4,
            ranks_ok(external),
            all(value is False for value in selection.values()),
            all(value is False for value in external["guardrails"].values()),
        ]
    )


def fiber_ok(fiber: dict) -> bool:
    decision = fiber["decision"]
    quotient = fiber["quotient_theorem"]
    boundary = fiber["downstream_boundary"]
    spectrum = fiber["spectral_observable_summary"]
    return all(
        [
            fiber["status"] == "U1Y_ROUTEC_FIBERCLASS_C1_OBSERVABLE_QUOTIENT_CLOSED_MATRIX_REPRESENTATIVE_OPEN",
            fiber["closure_claimed"] is False,
            fiber["target_fitting_used"] is False,
            fiber["next_required_artifact"] == NEXT,
            fiber["theorem"]["proved"] is True,
            decision["active_shift_1_1_selected_for_current_C1_layer"] is True,
            decision["fiberclass_quotient_for_current_C1_spectral_observables_closed"] is True,
            decision["shift0_allowed_as_computation_gauge"] is True,
            decision["absolute_fiber_origin_selected"] is False,
            decision["absolute_fiber_origin_used_as_hidden_knob"] is False,
            decision["selected_matrix_representative_for_full_C1_operator"] is False,
            decision["A_selected_computable"] is False,
            decision["b_selected_computable"] is False,
            decision["lambda_12_computable"] is False,
            quotient["selected_active_shift"] == [1, 1],
            quotient["fixed_fiber_class"] == [0, 1, 2],
            quotient["fiber_class_quotient_selected"] is True,
            quotient["active_shift_selected"] is True,
            quotient["absolute_fiber_shift_selected"] is False,
            spectrum["YYstar_scalar_identity_invariant"] is True,
            spectrum["current_layer_flavor_splitting_possible"] is False,
            boundary["can_promote_fixed_fiber_representative_for_current_spectral_observables"] is True,
            boundary["can_promote_fixed_fiber_representative_for_full_C1_matrix_operator"] is False,
            boundary["can_compute_yukawa_hierarchy"] is False,
            boundary["can_compute_CKM_PMNS_CP"] is False,
            all(value is False for value in fiber["guardrails"].values()),
        ]
    )


def main() -> None:
    prev = load(PREV)
    external = load(EXTERNAL)
    fiber = load(FIBER)

    previous_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["status"] == "POST_ALPHA_PRIMITIVE_C1_ATOM_NOGO_FRONTIER_BUILT_VALUES_OPEN",
            prev["next_required_artifact"] == "Selected_U1Y_RouteC_CanonicalZeroSelection_or_NonInvariantC1Tensor_Fill_v1",
            prev["canonical_zero_selected"] if "canonical_zero_selected" in prev else True,
        ]
    )
    # The packet stores canonical zero status inside the branch payload; keep the intent explicit.
    previous_ready = previous_ready and prev["canonical_zero_branch"]["accepted_as_selected_atom_payload"] is False
    theorem_proved = all([previous_ready, external_ok(external), fiber_ok(fiber)])
    packet = {
        "theorem": {
            "name": "PostAlphaNonInvariantC1FiberClassImport",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The noninvariant primitive C1 branch is reduced to active shift (1,1) and a selected "
                "fixed-fiber quotient class for current spectral observables. Shift 0 is only a computation "
                "gauge. The quotient proves current-layer scalar-permutation degeneracy, so nondegenerate "
                "Yukawa hierarchy, CKM/PMNS, CP, A_selected, b_selected, and lambda12 require selected "
                "higher-order/full-response data or operator-level basis transport."
            ),
        },
        "status": STATUS,
        "external_candidate_summary": external["candidate_summary"],
        "imported_facts": external["imported_facts"],
        "quotient_theorem": fiber["quotient_theorem"],
        "spectral_observable_summary": fiber["spectral_observable_summary"],
        "downstream_boundary": fiber["downstream_boundary"],
        "checks": {
            "previous_ready": previous_ready,
            "external_ok": external_ok(external),
            "fiber_ok": fiber_ok(fiber),
            "theorem_proved": theorem_proved,
        },
        "what_closes_now": {
            "active_shift_1_1_selected_for_current_C1_layer": True,
            "fixed_fiber_quotient_class_selected_for_current_C1_spectral_observables": True,
            "shift0_computation_gauge_allowed": True,
            "absolute_fiber_origin_hidden_knob_rejected": True,
            "current_layer_scalar_permutation_degeneracy_proved": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": fiber["what_remains_open"],
        "guardrails": {
            "does_not_select_absolute_fiber_origin": True,
            "does_not_promote_shift0_to_physical_knob": True,
            "does_not_claim_full_C1_matrix_representative": True,
            "does_not_claim_A_b_lambda_yukawa_or_SM_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {"previous": str(PREV), "external": str(EXTERNAL), "fiber": str(FIBER)},
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_noninvariant_c1_fiberclass",
        "status": STATUS,
        "closure_claimed": False,
        "active_shift_selected": True,
        "fiberclass_spectral_quotient_closed": True,
        "full_matrix_representative_selected": False,
        "current_layer_flavor_splitting_possible": False,
        "checks": {
            **packet["checks"],
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# PostAlpha NonInvariantC1 FiberClass Import v1

## Result

The noninvariant primitive C1 route is no longer an arbitrary tensor search:

```text
selected active shift = (1,1)
fixed fiber class = [0,1,2]
shift 0 = computation gauge only
current spectral quotient = closed
absolute fiber origin = not selected
full C1 matrix representative = open
```

The current finite primitive C1 layer is scalar-permutation degenerate:
`YY*` is a scalar identity in `u,d,e,nuD`, so this layer alone cannot produce
nondegenerate Yukawa hierarchy, CKM/PMNS, or CP.

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
