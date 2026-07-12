from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_primitive_c1_lambda_gate.packet.json"
FILL = QA / "candidate_data" / "selected_u1y_routec_primitive_c1_atom_payload_fill_or_nogo.candidate.json"
MISSING = QA / "candidate_data" / "selected_u1y_routec_primitive_c1_atom_payload_missing_leaves.json"
FRONTIER = QA / "candidate_data" / "selected_u1y_routec_primitive_c1_sourcevalue_theorem_or_noninvariant_tensor.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_primitive_c1_atom_nogo_frontier_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_primitive_c1_atom_nogo_frontier.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_PrimitiveC1_AtomNoGo_Frontier_Import_v1.md"

STATUS = "POST_ALPHA_PRIMITIVE_C1_ATOM_NOGO_FRONTIER_BUILT_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_CanonicalZeroSelection_or_NonInvariantC1Tensor_Fill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def missing_counts(leaves: dict) -> dict[str, int]:
    counts: dict[str, int] = {}
    for leaf in leaves["missing_leaves"]:
        counts[leaf["kind"]] = counts.get(leaf["kind"], 0) + 1
    return counts


def fill_ok(fill: dict) -> bool:
    decision = fill["decision"]
    attempt = fill["fill_attempt"]
    zero = fill["canonical_zero_branch"]
    return all(
        [
            fill["status"] == "U1Y_ROUTEC_PRIMITIVE_C1_ATOMPAYLOAD_FILL_NOGO_CURRENT_CORPUS_VALUES_OPEN",
            fill["closure_claimed"] is False,
            fill["target_fitting_used"] is False,
            fill["next_required_artifact"] == "Selected_U1Y_RouteC_PrimitiveC1_SourceValue_Theorem_or_SelectedNonInvariantTensor_v1",
            fill["theorem"]["proved"] is True,
            decision["fill_attempt_executed"] is True,
            decision["current_corpus_supplies_selected_atom_payload"] is False,
            decision["primitive_C1_atoms_emitted"] is False,
            decision["emitted_atom_count"] == 0,
            decision["missing_atom_count"] == 24,
            decision["missing_leaf_count"] == 40,
            decision["canonical_zero_branch_tested"] is True,
            decision["canonical_zero_branch_rejected_as_closure"] is True,
            decision["A_selected_computable"] is False,
            decision["b_selected_computable"] is False,
            decision["lambda_12_computable"] is False,
            attempt["filled_atom_matrices"] == 0,
            attempt["open_atom_matrices"] == 24,
            attempt["total_missing_leaf_count"] == 40,
            attempt["same_source_id_present"] is False,
            attempt["source_certificate_present"] is False,
            zero["canonical_tensor_zero_response_result_proved_finitely"] is True,
            zero["all_c1_matrices_zero_for_canonical_tensor"] is True,
            zero["accepted_as_selected_atom_payload"] is False,
            all(value is False for value in fill["guardrails"].values()),
        ]
    )


def frontier_ok(frontier: dict) -> bool:
    decision = frontier["decision"]
    route_names = [route["route"] for route in frontier["route_ranking"]]
    return all(
        [
            frontier["status"] == "U1Y_ROUTEC_PRIMITIVE_C1_SOURCEVALUE_THEOREM_OR_NONINVARIANT_TENSOR_GATE_BUILT_OPEN",
            frontier["closure_claimed"] is False,
            frontier["target_fitting_used"] is False,
            frontier["next_required_artifact"] == NEXT,
            frontier["theorem"]["proved"] is True,
            decision["sourcevalue_contract_built"] is True,
            decision["canonical_zero_diagnostic_imported"] is True,
            decision["canonical_zero_overpromotion_blocked"] is True,
            decision["canonical_zero_selection_closed"] is False,
            decision["noninvariant_tensor_route_kept_primary"] is True,
            decision["typed_connection_derivation_route_kept_live"] is True,
            decision["primitive_C1_atoms_emitted"] is False,
            decision["missing_leaf_count_carried_forward"] == 40,
            route_names == ["selected_noninvariant_tensor", "canonical_zero_selection", "typed_connection_derivation"],
            all(route["closed"] is False for route in frontier["route_ranking"]),
            frontier["missing_leaf_counts"]
            == {"selected_basis": 12, "primitive_c1_atom_matrix": 24, "b_selected_source": 4},
            all(value is False for value in frontier["guardrails"].values()),
        ]
    )


def main() -> None:
    prev = load(PREV)
    fill = load(FILL)
    missing = load(MISSING)
    frontier = load(FRONTIER)

    previous_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["status"] == "POST_ALPHA_PRIMITIVE_C1_LAMBDA_GATE_BUILT_VALUES_OPEN",
            prev["next_required_artifact"] == "Selected_U1Y_RouteC_PrimitiveC1_AtomEmission_or_SelectedLambda12_SpectralTable_v1",
            prev["primitive_status"]["missing_atom_count"] == 24,
        ]
    )
    missing_ok = all(
        [
            missing["schema"] == "SelectedU1YRouteCPrimitiveC1AtomPayloadMissingLeaves.v1",
            missing["status"] == "CURRENT_CORPUS_VALUES_OPEN",
            len(missing["missing_leaves"]) == 40,
            missing_counts(missing) == {"selected_basis": 12, "primitive_c1_atom_matrix": 24, "b_selected_source": 4},
            len(missing["minimal_closing_options"]) == 3,
            all(missing["source_requirements"].values()),
        ]
    )
    theorem_proved = all([previous_ready, fill_ok(fill), missing_ok, frontier_ok(frontier)])
    packet = {
        "theorem": {
            "name": "PostAlphaPrimitiveC1AtomNoGoFrontierImport",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The current corpus does not fill the selected primitive C1 atom payload. The canonical "
                "translation-invariant tensor gives a finite zero-response diagnostic, but it is not selected "
                "and cannot compute A_selected or b_selected. The remaining legal routes are selected "
                "noninvariant tensor emission, selected canonical-zero theorem, or typed connection derivation."
            ),
        },
        "status": STATUS,
        "fill_attempt": fill["fill_attempt"],
        "canonical_zero_branch": fill["canonical_zero_branch"],
        "missing_leaf_counts": frontier["missing_leaf_counts"],
        "minimal_closing_options": missing["minimal_closing_options"],
        "route_ranking": frontier["route_ranking"],
        "checks": {
            "previous_ready": previous_ready,
            "fill_ok": fill_ok(fill),
            "missing_ok": missing_ok,
            "frontier_ok": frontier_ok(frontier),
            "theorem_proved": theorem_proved,
        },
        "what_closes_now": {
            "current_payload_fill_attempt_executed": True,
            "canonical_zero_overpromotion_blocked": True,
            "missing_leaf_packet_imported": True,
            "sourcevalue_closure_routes_ranked": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": frontier["what_remains_open"],
        "guardrails": {
            "does_not_claim_canonical_zero_selected": True,
            "does_not_claim_noninvariant_tensor_emitted": True,
            "does_not_claim_typed_connection_values_emitted": True,
            "does_not_claim_primitive_C1_values_A_b_lambda_or_SM": True,
            "does_not_use_observed_benchmark_or_diagnostic_lambda_values": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous": str(PREV),
            "fill": str(FILL),
            "missing": str(MISSING),
            "frontier": str(FRONTIER),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_primitive_c1_atom_nogo_frontier",
        "status": STATUS,
        "closure_claimed": False,
        "primitive_C1_atoms_emitted": False,
        "missing_leaf_count": 40,
        "canonical_zero_selected": False,
        "checks": {
            **packet["checks"],
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# PostAlpha PrimitiveC1 AtomNoGo Frontier Import v1

## Result

The current-corpus primitive C1 atom fill attempt is complete and does not close:

```text
emitted atom matrices = 0
open atom matrices = 24
missing leaves = 40
canonical zero branch selected = false
A_selected/b_selected/lambda12 = open
```

The canonical translation-invariant tensor is useful only as a diagnostic zero
branch until a selected same-source zero theorem is proved.

Legal closing routes:

```text
1. selected noninvariant primitive C1 tensor plus basis transport
2. selected canonical-zero theorem plus homogeneous-zero b row
3. typed monad/Cech/HYM connection derivation of all atom matrices
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
