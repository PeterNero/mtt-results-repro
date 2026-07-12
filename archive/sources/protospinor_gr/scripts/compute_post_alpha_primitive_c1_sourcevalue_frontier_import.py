from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_dotd_alpha1_c1_response.packet.json"
GATE = QA / "candidate_data" / "selected_u1y_routec_primitive_c1_contractions_or_lambda12_gate.candidate.json"
INTERFACE = QA / "candidate_data" / "selected_u1y_routec_primitive_c1_atom_emission_interface.candidate.json"
FILL = QA / "candidate_data" / "selected_u1y_routec_primitive_c1_atom_payload_fill_or_nogo.candidate.json"
FRONTIER = QA / "candidate_data" / "selected_u1y_routec_primitive_c1_sourcevalue_theorem_or_noninvariant_tensor.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_primitive_c1_sourcevalue_frontier_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_primitive_c1_sourcevalue_frontier.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_PrimitiveC1_SourceValue_Frontier_v1.md"

STATUS = "POST_ALPHA_PRIMITIVE_C1_SOURCEVALUE_FRONTIER_BUILT_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_CanonicalZeroSelection_or_NonInvariantC1Tensor_Fill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    gate = load(GATE)
    interface = load(INTERFACE)
    fill = load(FILL)
    frontier = load(FRONTIER)

    post_alpha_prefix_closed = all(
        [
            prev["decision"]["same_branch_alpha1_driver_proved"] is True,
            prev["decision"]["selected_dotD_source_theorem_proved"] is True,
            prev["decision"]["honest_dotD_replay_without_lifted_flags"] is True,
            gate["decision"]["alpha1_and_honest_dotD_prefix_closed"] is True,
            gate["post_alpha_prefix"]["alpha1_driver_verified"] is True,
            gate["post_alpha_prefix"]["honest_dotD_validator_closed"] is True,
        ]
    )
    atom_contract_built = all(
        [
            interface["theorem"]["proved"] is True,
            interface["decision"]["assembly_theorem_proved"] is True,
            interface["decision"]["atom_payload_template_written"] is True,
            interface["decision"]["missing_atom_count"] == 24,
            interface["decision"]["emitted_atom_count"] == 0,
            interface["decision"]["A_selected_computable"] is False,
            interface["decision"]["b_selected_computable"] is False,
        ]
    )
    current_fill_nogo = all(
        [
            fill["theorem"]["proved"] is True,
            fill["decision"]["fill_attempt_executed"] is True,
            fill["decision"]["canonical_zero_branch_tested"] is True,
            fill["decision"]["canonical_zero_branch_rejected_as_closure"] is True,
            fill["decision"]["current_corpus_supplies_selected_atom_payload"] is False,
            fill["decision"]["missing_atom_count"] == 24,
            fill["decision"]["missing_leaf_count"] == 40,
            fill["fill_attempt"]["filled_atom_matrices"] == 0,
            fill["canonical_zero_branch"]["accepted_as_selected_atom_payload"] is False,
        ]
    )
    sourcevalue_frontier_built = all(
        [
            frontier["theorem"]["proved"] is True,
            frontier["decision"]["sourcevalue_contract_built"] is True,
            frontier["decision"]["canonical_zero_selection_closed"] is False,
            frontier["decision"]["noninvariant_tensor_route_kept_primary"] is True,
            frontier["decision"]["typed_connection_derivation_route_kept_live"] is True,
            frontier["decision"]["primitive_C1_atoms_emitted"] is False,
            frontier["missing_leaf_counts"]["primitive_c1_atom_matrix"] == 24,
            frontier["missing_leaf_counts"]["selected_basis"] == 12,
            frontier["missing_leaf_counts"]["b_selected_source"] == 4,
        ]
    )
    lambda12_separated = all(
        [
            gate["what_closes_now"]["lambda12_separated_from_alpha1_and_C1"] is True,
            gate["lambda12_status"]["lambda_12_closed"] is False,
            gate["lambda12_status"]["lambda_12_computable_from_this_gate"] is False,
            frontier["decision"]["lambda_12_computable"] is False,
        ]
    )
    guardrails_ok = all(
        [
            all(prev["guardrails"].values()),
            all(gate["guardrails"].values()) is False,
            all(interface["guardrails"].values()) is False,
            all(fill["guardrails"].values()) is False,
            all(frontier["guardrails"].values()) is False,
            gate["target_fitting_used"] is False,
            interface["target_fitting_used"] is False,
            fill["target_fitting_used"] is False,
            frontier["target_fitting_used"] is False,
        ]
    )
    # The source guardrail dictionaries intentionally encode forbidden claims as false.
    forbidden_claims_absent = all(
        [
            gate["guardrails"]["claims_primitive_C1_contractions"] is False,
            interface["guardrails"]["claims_primitive_C1_values"] is False,
            fill["guardrails"]["claims_primitive_C1_values"] is False,
            frontier["guardrails"]["claims_primitive_C1_values"] is False,
            frontier["guardrails"]["claims_noninvariant_tensor_emitted"] is False,
            frontier["guardrails"]["claims_canonical_zero_selected"] is False,
            frontier["guardrails"]["uses_observed_data"] is False,
            frontier["guardrails"]["uses_benchmark_data"] is False,
        ]
    )
    theorem_proved = all(
        [
            post_alpha_prefix_closed,
            atom_contract_built,
            current_fill_nogo,
            sourcevalue_frontier_built,
            lambda12_separated,
            guardrails_ok,
            forbidden_claims_absent,
        ]
    )

    packet = {
        "theorem": {
            "name": "PostAlphaPrimitiveC1SourceValueFrontierImportTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "After local alpha1/dotD replay closure, primitive C1 closure reduces to a selected "
                "source-value theorem. The atom interface fixes the six required terms for each of "
                "u,d,e,nuD. Applying the current corpus fills zero of twenty-four atom matrices and "
                "leaves forty source leaves missing. The canonical translation-invariant zero branch "
                "is finitely tested but not selected as the primitive C1 payload. Thus the next legal "
                "gate is either canonical-zero selection with homogeneous b row, selected non-invariant "
                "C1 tensor/basis transport, or typed monad/Cech/HYM connection values."
            ),
        },
        "status": STATUS,
        "post_alpha_prefix": gate["post_alpha_prefix"],
        "atom_table": gate["atom_table"],
        "assembly_rules": interface["assembly_rules"],
        "canonical_zero_branch": fill["canonical_zero_branch"],
        "missing_leaf_counts": frontier["missing_leaf_counts"],
        "route_ranking": frontier["route_ranking"],
        "checks": {
            "post_alpha_prefix_closed": post_alpha_prefix_closed,
            "atom_contract_built": atom_contract_built,
            "current_fill_nogo": current_fill_nogo,
            "sourcevalue_frontier_built": sourcevalue_frontier_built,
            "lambda12_separated": lambda12_separated,
            "guardrails_ok": guardrails_ok,
            "forbidden_claims_absent": forbidden_claims_absent,
        },
        "what_closes_now": {
            "primitive_C1_atom_contract_imported": True,
            "all_24_required_atoms_identified": True,
            "current_corpus_fill_nogo_imported": True,
            "canonical_zero_overpromotion_blocked": True,
            "sourcevalue_closure_contract_imported": True,
            "three_legal_routes_ranked": True,
            "lambda12_kept_separate_as_spectral_table_problem": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_same_source_atom_payload": True,
            "all_24_primitive_C1_atom_matrices": True,
            "selected_basis_transport": True,
            "selected_basis_order_and_zero_mode_bases": True,
            "inhomogeneous_row_or_homogeneous_zero_theorem": True,
            "canonical_zero_selection_theorem": True,
            "selected_noninvariant_primitive_tensor": True,
            "typed_connection_derivation_values": True,
            "A_selected": True,
            "b_selected": True,
            "sector_response_matrices": True,
            "lambda_12": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "does_not_claim_primitive_C1_values": True,
            "does_not_claim_canonical_zero_selected": True,
            "does_not_claim_noninvariant_tensor_emitted": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_lambda12_or_full_SM": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous": str(PREV),
            "primitive_gate": str(GATE),
            "atom_interface": str(INTERFACE),
            "fill_or_nogo": str(FILL),
            "sourcevalue_frontier": str(FRONTIER),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_primitive_c1_sourcevalue_frontier",
        "status": STATUS,
        "closure_claimed": False,
        "missing_atom_count": 24,
        "missing_leaf_count": 40,
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
    note = f"""# PostAlpha PrimitiveC1 SourceValue Frontier v1

## Result

Primitive C1 closure is reduced to a selected source-value theorem.

Current corpus fill:

```text
required atom matrices = 24
filled atom matrices = 0
missing source leaves = 40
canonical zero branch tested = true
canonical zero selected = false
```

The legal routes are:

```text
1. selected non-invariant primitive C1 tensor
2. canonical zero selection plus homogeneous b row
3. typed monad/Cech/HYM connection derivation values
```

`lambda_12` is separated from this C1 atom gate: it still needs a selected
local determinant/spectral table.

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
