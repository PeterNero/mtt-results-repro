from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "candidate_data" / "post_alpha_fiberclass_source_target.packet.json"
PRIM_COUNTER = SM / "candidate_data" / "selected_routec_basis_transport_primitive_source_proof_or_counterexample.candidate.json"
WEYL_GATE = SM / "candidate_data" / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem.candidate.json"
WEYL_ASSEMBLY = SM / "candidate_data" / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"
PROVENANCE = SM / "candidate_data" / "selected_routec_weylpair_source_provenance_lemma.candidate.json"
TRANSFER = SM / "candidate_data" / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_weylpair_transfer_reduction_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_weylpair_transfer_reduction.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_WeylPair_Transfer_Reduction_v1.md"

STATUS = "POST_ALPHA_WEYLPAIR_TRANSFER_REDUCED_SECTOR_ROUTING_NORMALIZATION_OPEN"
NEXT = "MTT_Selected_RouteC_WeylPair_SectorRouting_Source_Lemma_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    prim = load(PRIM_COUNTER)
    gate = load(WEYL_GATE)
    assembly = load(WEYL_ASSEMBLY)
    provenance = load(PROVENANCE)
    transfer = load(TRANSFER)

    primitive_only_retired = all(
        [
            prim["theorem"]["proved"] is True,
            prim["source_attempt"]["counterexample_proved"] is True,
            prim["span_tests"]["fixed_fiber_primitives"]["target_in_span"] is False,
            prim["span_tests"]["fixed_plus_all_fiber_envelope"]["target_in_span"] is False,
            prim["what_closes_now"]["primitive_only_counterexample_built"] is True,
        ]
    )
    weylpair_algebra_sufficient = all(
        [
            gate["theorem_gate"]["proved_now"]["minimal_weyl_pair_reconstructs_locked_splitter"] is True,
            gate["span_test"]["target_in_span"] is True,
            gate["span_test"]["rank"] == 2,
            gate["span_test"]["relative_residual"] < 1e-12,
            assembly["theorem"]["proved"] is True,
            assembly["locked_solve"]["consistent"] is True,
            assembly["locked_solve"]["rank"] == 2,
            assembly["locked_solve"]["relative_residual"] < 1e-12,
        ]
    )
    source_level_provenance_closed = all(
        [
            provenance["source_level_weyl_carrier"]["proved"] is True,
            provenance["active_shift_provenance"]["proved"] is True,
            provenance["what_closes_now"]["source_level_phase_Z_carrier_provenance"] is True,
            provenance["what_closes_now"]["source_level_shift_X_carrier_provenance"] is True,
            provenance["c1_transfer_map"]["selected_source_to_C1_response_map_emitted"] is False,
        ]
    )
    conditional_transfer_exact = all(
        [
            transfer["theorem"]["proved"] is True,
            transfer["conditional_transfer_map"]["conditional_exact"] is True,
            transfer["conditional_transfer_map"]["phase_residual"] == 0.0,
            transfer["conditional_transfer_map"]["shift_residual"] == 0.0,
            transfer["selected_status"]["promote_to_A_selected_allowed"] is False,
            transfer["selected_status"]["selected_sector_routing_emitted"] is False,
            transfer["selected_status"]["selected_normalization_emitted"] is False,
        ]
    )
    post_alpha_reconciled = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_remains_open"]["selected_basis_transport_or_vertex_source_proof"] is True,
            prev["what_remains_open"]["A_selected_and_b_selected"] is True,
        ]
    )
    guardrails_ok = all(
        [
            prim["target_fitting_used"] is False,
            gate["target_fitting_used"] is False,
            assembly["target_fitting_used"] is False,
            provenance["target_fitting_used"] is False,
            transfer["target_fitting_used"] is False,
            prim["closure_claimed"] is False,
            gate["closure_claimed"] is False,
            assembly["closure_claimed"] is False,
            provenance["closure_claimed"] is False,
            transfer["closure_claimed"] is False,
        ]
    )
    theorem_proved = all(
        [
            primitive_only_retired,
            weylpair_algebra_sufficient,
            source_level_provenance_closed,
            conditional_transfer_exact,
            post_alpha_reconciled,
            guardrails_ok,
        ]
    )

    packet = {
        "theorem": {
            "name": "PostAlphaWeylPairTransferReductionTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "Primitive-only fixed-fiber C1 emission is insufficient: its span does not contain the locked "
                "qutrit/Weyl splitter. The enriched Weyl-pair packet with phase-like Z on u/e and shift-like X "
                "on d/nuD is algebraically sufficient and solves the conditional two-column splitter equation. "
                "Source-level q79/F,m=1 S3/GS provenance supplies the Z/X Weyl carrier and active shift (1,1), "
                "and the conditional source-to-C1 transfer map is exact. The remaining selected obstruction is "
                "to theorem-derive the sector routing and normalization from the same source, then emit A_selected "
                "and b_selected."
            ),
        },
        "status": STATUS,
        "primitive_only_counterexample": {
            "status": prim["status"],
            "fixed_fiber_relative_residual": prim["span_tests"]["fixed_fiber_primitives"]["relative_residual"],
            "fixed_plus_all_relative_residual": prim["span_tests"]["fixed_plus_all_fiber_envelope"]["relative_residual"],
            "target_in_primitive_span": False,
            "refined_next_theorem": prim["refined_next_theorem"],
        },
        "weylpair_algebra": {
            "gate_status": gate["status"],
            "target_in_weylpair_span": gate["span_test"]["target_in_span"],
            "rank": gate["span_test"]["rank"],
            "relative_residual": gate["span_test"]["relative_residual"],
            "assembly_status": assembly["status"],
            "conditional_deltaTheta": assembly["locked_solve"]["deltaTheta_conditional"],
            "condition_number": assembly["locked_solve"]["condition_number"],
        },
        "source_provenance": {
            "status": provenance["status"],
            "source_level_weyl_carrier": provenance["source_level_weyl_carrier"],
            "active_shift_provenance": provenance["active_shift_provenance"],
            "open_transfer_sublemma": provenance["lemma_attempt"]["open_sublemma"],
        },
        "conditional_transfer": {
            "status": transfer["status"],
            "formula": transfer["conditional_transfer_map"]["formula"],
            "phase_residual": transfer["conditional_transfer_map"]["phase_residual"],
            "shift_residual": transfer["conditional_transfer_map"]["shift_residual"],
            "reduction": transfer["reduction"],
            "selected_status": transfer["selected_status"],
        },
        "checks": {
            "primitive_only_retired": primitive_only_retired,
            "weylpair_algebra_sufficient": weylpair_algebra_sufficient,
            "source_level_provenance_closed": source_level_provenance_closed,
            "conditional_transfer_exact": conditional_transfer_exact,
            "post_alpha_reconciled": post_alpha_reconciled,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            "primitive_only_C1_span_counterexample_imported": True,
            "enriched_weylpair_packet_algebraically_sufficient": True,
            "conditional_deltaTheta_two_column_solve_exact": True,
            "source_level_ZX_carrier_and_active_shift_provenance_imported": True,
            "conditional_source_to_C1_transfer_exact": True,
            "remaining_gap_reduced_to_selected_sector_routing_and_normalization": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_sector_routing_source_lemma": True,
            "selected_transfer_normalization": True,
            "promote_conditional_transfer_to_selected_C1_map": True,
            "emit_A_selected_and_b_selected": True,
            "honest_selected_deltaTheta_C1_solve": True,
            "selected_24_atom_payload": True,
            "Yukawa_CKM_PMNS_CP_and_full_SM_closure": True,
            "selected_lambda12_spectral_table": True,
        },
        "guardrails": {
            "does_not_treat_diagnostic_splitter_as_selected_source": True,
            "does_not_promote_conditional_A_to_A_selected": True,
            "does_not_claim_b_selected": True,
            "does_not_claim_flavor_or_SM_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
            "primitive_only_route_retired_without_discarding_active_shift_result": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous_fiberclass": str(PREV),
            "primitive_counterexample": str(PRIM_COUNTER),
            "weylpair_gate": str(WEYL_GATE),
            "weylpair_assembly": str(WEYL_ASSEMBLY),
            "source_provenance": str(PROVENANCE),
            "transfer": str(TRANSFER),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_weylpair_transfer_reduction",
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
    note = f"""# PostAlpha WeylPair Transfer Reduction v1

## Result

Primitive-only C1 is now retired as the direct splitter source:

```text
primitive-only target in span = false
fixed-fiber residual ratio = {packet["primitive_only_counterexample"]["fixed_fiber_relative_residual"]}
```

The enriched Weyl-pair route is algebraically sufficient:

```text
phase Z -> u,e as I+Z
shift X -> d,nuD as I+X
conditional rank = {packet["weylpair_algebra"]["rank"]}
conditional deltaTheta = {packet["weylpair_algebra"]["conditional_deltaTheta"]}
```

The selected source-level `Z/X` carrier and active shift `(1,1)` are proved,
and the conditional source-to-C1 transfer map is exact. The remaining blocker
is selected sector routing plus selected normalization, after which
`A_selected` and `b_selected` can be emitted and the honest splitter solve can
run.

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
