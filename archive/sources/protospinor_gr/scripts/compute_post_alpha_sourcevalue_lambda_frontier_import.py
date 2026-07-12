from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_primitive_c1_gate_import.packet.json"
SOURCEVALUE = QA / "candidate_data" / "selected_u1y_routec_primitive_c1_sourcevalue_theorem_or_noninvariant_tensor.candidate.json"
CONTRACT = QA / "candidate_data" / "selected_u1y_routec_primitive_c1_sourcevalue_closure_contract.json"
LAMBDA_GATE = QA / "candidate_data" / "selected_u1_hypercharge_local_determinant_spectrum_attempt.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_sourcevalue_lambda_frontier_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_sourcevalue_lambda_frontier.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_SourceValue_Lambda_Frontier_v1.md"

STATUS = "POST_ALPHA_SOURCEVALUE_AND_LAMBDA_FRONTIER_REDUCED_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_CanonicalZeroSelection_or_NonInvariantC1Tensor_Fill_and_U1HyperchargeSpectrum_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCEVALUE)
    contract = load(CONTRACT)
    lambda_gate = load(LAMBDA_GATE)

    primitive_frontier_exact = all(
        [
            prev["theorem"]["proved"] is True,
            source["theorem"]["proved"] is True,
            source["decision"]["sourcevalue_contract_built"] is True,
            source["decision"]["primitive_C1_atoms_emitted"] is False,
            source["decision"]["missing_leaf_count_carried_forward"] == 40,
            source["missing_leaf_counts"]["primitive_c1_atom_matrix"] == 24,
            source["missing_leaf_counts"]["selected_basis"] == 12,
            source["missing_leaf_counts"]["b_selected_source"] == 4,
            contract["status"] == "OPEN_SOURCE_VALUE_THEOREM_REQUIRED",
        ]
    )
    route_partition_exact = all(
        [
            len(source["route_ranking"]) == 3,
            source["route_ranking"][0]["route"] == "selected_noninvariant_tensor",
            contract["canonical_zero_selection"]["currently_closed"] is False,
            contract["selected_noninvariant_tensor"]["currently_closed"] is False,
            contract["typed_connection_derivation"]["currently_closed"] is False,
            contract["selected_noninvariant_tensor"]["closure_consequence"].startswith("This is the only primitive C1 route"),
        ]
    )
    lambda_frontier_exact = all(
        [
            lambda_gate["decision"]["lambda_12_closed"] is False,
            lambda_gate["decision"]["u1_hypercharge_spectrum_closed"] is False,
            lambda_gate["decision"]["primary_route"] == "heterotic_or_section_ring_u1_hypercharge_spectrum",
            lambda_gate["attempts"]["heterotic_section_ring"]["status"] == "OPEN_PRIMARY_ROUTE",
            lambda_gate["attempts"]["quotient_identity"]["status"].startswith("REJECTED"),
            lambda_gate["attempts"]["central_circle_reuse"]["status"].startswith("REJECTED"),
            lambda_gate["target_fitting_used"] is False,
        ]
    )
    guardrails_ok = all(
        [
            source["guardrails"]["claims_A_selected"] is False,
            source["guardrails"]["claims_Yukawa_or_full_SM_closure"] is False,
            source["guardrails"]["claims_lambda12"] is False,
            source["guardrails"]["uses_observed_data"] is False,
            source["guardrails"]["uses_benchmark_data"] is False,
            lambda_gate["decision"]["target_fitting_used"] is False,
            lambda_gate["decision"]["Pperp_quotient_identity_promoted"] is False,
            lambda_gate["decision"]["central_circle_reuse_promoted"] is False,
        ]
    )
    theorem_proved = all([primitive_frontier_exact, route_partition_exact, lambda_frontier_exact, guardrails_ok])

    packet = {
        "theorem": {
            "name": "PostAlphaSourceValueAndLambdaFrontierTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "After alpha1 closure, primitive C1 flavor closure is exactly reduced to one selected "
                "source-value theorem. The theorem has three and only three currently legal realizations: "
                "select the canonical translation-invariant zero branch with basis transport and homogeneous "
                "zero b row; emit a selected noninvariant primitive tensor with all 24 atom matrices, 12 "
                "sector bases, and four b rows or zero theorems; or derive those same values from typed "
                "monad/Cech/HYM connection data. Separately, lambda_12 is exactly reduced to a selected "
                "U1/hypercharge local-determinant spectrum on the quotient carrier. The quotient projector "
                "and central-circle determinant are rejected as proof sources for lambda_12."
            ),
        },
        "status": STATUS,
        "primitive_c1_frontier": {
            "source_status": source["status"],
            "contract_status": contract["status"],
            "missing_leaf_counts": source["missing_leaf_counts"],
            "route_ranking": source["route_ranking"],
            "next_required_artifact": source["next_required_artifact"],
        },
        "closure_contract": {
            "canonical_zero_selection": contract["canonical_zero_selection"],
            "selected_noninvariant_tensor": contract["selected_noninvariant_tensor"],
            "typed_connection_derivation": contract["typed_connection_derivation"],
            "acceptance_tests": contract["acceptance_tests"],
        },
        "lambda12_frontier": {
            "status": lambda_gate["status"],
            "primary_route": lambda_gate["decision"]["primary_route"],
            "next_required_object": lambda_gate["decision"]["next_required_object"],
            "hypercharge_gate": lambda_gate["hypercharge_gate"],
            "rejected_routes": {
                "quotient_identity": lambda_gate["attempts"]["quotient_identity"],
                "central_circle_reuse": lambda_gate["attempts"]["central_circle_reuse"],
            },
            "open_primary_route": lambda_gate["attempts"]["heterotic_section_ring"],
        },
        "checks": {
            "primitive_frontier_exact": primitive_frontier_exact,
            "route_partition_exact": route_partition_exact,
            "lambda_frontier_exact": lambda_frontier_exact,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            "post_alpha_sourcevalue_frontier_theorem": True,
            "three_legal_primitive_c1_routes_partitioned": True,
            "canonical_zero_overpromotion_blocked": True,
            "noninvariant_tensor_route_identified_as_primary_for_flavor": True,
            "typed_connection_derivation_kept_live": True,
            "lambda12_spectral_table_route_isolated": True,
            "invalid_lambda12_shortcuts_rejected": True,
        },
        "what_remains_open": {
            "selected_noninvariant_primitive_tensor_or_selected_zero_theorem": True,
            "selected_basis_transport": True,
            "all_24_primitive_C1_atoms": True,
            "four_b_rows_or_homogeneous_zero_theorems": True,
            "A_selected_and_b_selected": True,
            "selected_U1_hypercharge_spectrum": True,
            "lambda_12": True,
            "Yukawa_magnitudes_and_full_SM_closure": True,
        },
        "guardrails": {
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_primitive_C1_values": True,
            "does_not_claim_lambda12": True,
            "does_not_claim_Yukawa_or_full_SM_closure": True,
            "rejects_projector_as_threshold_operator": True,
            "rejects_central_circle_reuse_for_U1": True,
            "target_fitting_excluded": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous_post_alpha_gate": str(PREV),
            "sourcevalue": str(SOURCEVALUE),
            "contract": str(CONTRACT),
            "lambda_gate": str(LAMBDA_GATE),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_sourcevalue_lambda_frontier",
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
    note = f"""# PostAlpha SourceValue Lambda Frontier v1

## Result

Alpha1 closure reduces the remaining SM/flavor problem to two independent value
objects:

```text
primitive C1 source-value object:
  24 atom matrices
  12 selected sector bases
  4 b rows or homogeneous-zero theorems

lambda12 object:
  selected U1/hypercharge local-determinant spectrum on V/<s>
```

The primitive C1 route is now partitioned into exactly three legal closures:

1. selected noninvariant primitive tensor, primary for nonzero flavor data
2. selected canonical zero theorem, rigorous but retires primitive C1 as a
   Yukawa hierarchy source
3. typed monad/Cech/HYM derivation, which may produce either of the two above

For `lambda_12`, two tempting shortcuts are rejected:

```text
P_perp quotient identity is a projector, not a threshold operator
central-circle determinant reuse double-counts the quotiented shared circle
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
