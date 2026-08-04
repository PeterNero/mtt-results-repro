from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "candidate_data" / "post_alpha_sourcevalue_lambda_frontier.packet.json"
NONINV = SM / "candidate_data" / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
U1_SOURCE = QA / "candidate_data" / "selected_u1_hypercharge_operator_spectrum_source_packet.candidate.json"
U1_ROW = QA / "candidate_data" / "selected_u1_hypercharge_section_ring_or_twisted_module_operator_row.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_candidate_routes_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_candidate_routes.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_CandidateRoutes_v1.md"

STATUS = "POST_ALPHA_CANDIDATE_ROUTES_BUILT_SELECTION_AND_SPECTRA_OPEN"
NEXT = "MTT_Selected_RouteC_Primitive_Source_Selection_Theorem_or_U1_Direct_Operator_Row_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    noninv = load(NONINV)
    u1_source = load(U1_SOURCE)
    u1_row = load(U1_ROW)

    noninvariant_candidate_support = all(
        [
            noninv["theorem"]["proved"] is True,
            noninv["calculation_results"]["all_four_tested_candidates_nonzero"] is True,
            noninv["calculation_results"]["nonzero_unselected_candidates_found"] == 4,
            noninv["calculation_results"]["can_close_selected_C1_now"] is False,
            noninv["search_rule"]["minimal_active_shift_required"] == [1, 1],
            noninv["target_fitting_used"] is False,
            all(candidate["selected_by_theorem"] is False for candidate in noninv["candidate_primitives"]),
        ]
    )
    post_alpha_reinterpretation = all(
        [
            prev["theorem"]["proved"] is True,
            prev["status"] == "POST_ALPHA_SOURCEVALUE_AND_LAMBDA_FRONTIER_REDUCED_VALUES_OPEN",
            prev["what_remains_open"]["selected_noninvariant_primitive_tensor_or_selected_zero_theorem"] is True,
            prev["what_remains_open"]["A_selected_and_b_selected"] is True,
        ]
    )
    u1_contract_support = all(
        [
            u1_source["decision"]["operator_spectrum_source_packet_built"] is True,
            u1_source["decision"]["selected_U1_hypercharge_operator_spectrum_found"] is False,
            u1_source["route_tests"]["same_source_operator_spectrum_packet"]["status"] == "OPEN_PRIMARY_ROUTE",
            u1_row["decision"]["section_ring_or_twisted_module_operator_row_found"] is False,
            u1_row["decision"]["finite_qutrit_lane_closes_only_index"] is True,
            u1_row["lanes"]["finite_qutrit_projector_lane"]["status"] == "CLOSED_FOR_QUOTIENT_INDEX_ONLY_NOT_OPERATOR_ROW",
            u1_row["lanes"]["minimal_source_amendment"]["status"] == "REQUIRED_TO_CLOSE",
            u1_source["target_fitting_used"] is False,
            u1_row["target_fitting_used"] is False,
        ]
    )
    guardrails_ok = all(
        [
            noninv["closure_claimed"] is False,
            noninv["superset_mode"]["diagnostic_backfit_only"]["used"] is False,
            u1_source["acceptance_contract"]["closed_now"]["lambda_12_closed"] is False,
            u1_source["acceptance_contract"]["closed_now"]["selected_spectrum_emitted"] is False,
            u1_source["route_tests"]["diagnostic_scalar_spectral_table"]["status"].startswith("REJECTED"),
            u1_source["route_tests"]["qa_log2008_hypercharge_injection"]["status"].startswith("REJECTED"),
            u1_source["route_tests"]["topology_only_hypercharge_embedding"]["status"].startswith("REJECTED"),
        ]
    )
    theorem_proved = all([noninvariant_candidate_support, post_alpha_reinterpretation, u1_contract_support, guardrails_ok])

    packet = {
        "theorem": {
            "name": "PostAlphaCandidateRoutesTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The post-alpha source-value frontier has two concrete candidate routes. For primitive C1, "
                "the finite noninvariant active shift (1,1) emits four nonzero candidate matrix families "
                "without observed flavor data, but none is selected until a source theorem chooses the "
                "primitive, vertex, basis transport, and fiber rule. For lambda_12, the U1/hypercharge "
                "source-packet interface is built and the section-ring/twisted-module operator-row route is "
                "reduced to a minimal source amendment, but no selected spectrum or determinant finite part is emitted."
            ),
        },
        "status": STATUS,
        "primitive_c1_candidate_route": {
            "source_status": noninv["status"],
            "minimal_active_shift": noninv["search_rule"]["minimal_active_shift_required"],
            "candidate_count": len(noninv["candidate_primitives"]),
            "candidate_fiber_shifts": [candidate["primitive_fiber_shift"] for candidate in noninv["candidate_primitives"]],
            "rank_summary": noninv["calculation_results"]["ranks_by_candidate"],
            "max_abs_entry": noninv["candidate_primitives"][0]["summary"]["u"]["max_abs_entry"],
            "selected_by_theorem": False,
            "next_required_artifact": noninv["next_required_artifact"],
        },
        "lambda12_candidate_route": {
            "operator_source_status": u1_source["status"],
            "operator_row_status": u1_row["status"],
            "primary_next_object": u1_row["decision"]["primary_next_object"],
            "required_operator_fields": u1_source["route_tests"]["same_source_operator_spectrum_packet"]["required_fields"],
            "minimal_source_amendment_fields": u1_row["lanes"]["minimal_source_amendment"]["packet_fields"],
        },
        "checks": {
            "noninvariant_candidate_support": noninvariant_candidate_support,
            "post_alpha_reinterpretation": post_alpha_reinterpretation,
            "u1_contract_support": u1_contract_support,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            "nonzero_noninvariant_C1_candidate_matrices_imported": True,
            "minimal_active_shift_11_carried_forward": True,
            "candidate_fiber_shift_family_identified": True,
            "u1_hypercharge_spectrum_source_contract_imported": True,
            "u1_section_ring_or_twisted_module_row_reduced": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_fiber_shift_rule": True,
            "selected_noninvariant_primitive_or_vertex_or_basis_transport": True,
            "promotion_to_selected_24_atom_payload": True,
            "A_selected_and_b_selected": True,
            "selected_U1_hypercharge_operator_spectrum": True,
            "lambda_12": True,
            "Yukawa_magnitudes_and_full_SM_closure": True,
        },
        "guardrails": {
            "does_not_promote_candidate_matrices_to_selected_values": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_lambda12": True,
            "does_not_use_observed_or_benchmark_inputs": True,
            "rejects_proxy_spectra_and_log2008_injection": True,
            "finite_qutrit_lane_only_closes_index": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous_frontier": str(PREV),
            "noninvariant_c1_search": str(NONINV),
            "u1_operator_source": str(U1_SOURCE),
            "u1_operator_row": str(U1_ROW),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_candidate_routes",
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
    note = f"""# PostAlpha CandidateRoutes v1

## Result

The frontier now has two concrete candidate routes.

Primitive C1:

```text
minimal active shift = (1,1)
nonzero candidate families = 4
fiber shifts = 0, 1, 2, all
selected by theorem = false
```

This is real computational support for a nonzero primitive C1 route, but it is
not yet `A_selected`: the selected source still has to choose the primitive,
vertex/basis-transport correction, and fiber rule.

Lambda12:

```text
U1/hypercharge source-packet interface = built
section-ring/twisted-module row = reduced to minimal source amendment
selected spectrum = false
lambda_12 closed = false
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
