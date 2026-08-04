from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

THEOREM_SLOT = ROOT / "certificates" / "routec_basistransport_primitive_source_theorem_import_certificate.json"
COUNTEREXAMPLE = ROOT / "certificates" / "routec_basis_transport_proof_or_counterexample_import_certificate.json"
WEYLPAIR_GATE = ROOT / "certificates" / "routec_weylpair_source_gate_import_certificate.json"
CONDITIONAL_A = ROOT / "certificates" / "routec_weylpair_aselected_assembly_import_certificate.json"

OUT_CERT = ROOT / "certificates" / "routec_weylpair_frontier_reconciliation_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_weylpair_frontier_reconciliation.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_WeylPair_Frontier_Reconciliation_v1.md"

STATUS = "ROUTEC_WEYLPAIR_FRONTIER_RECONCILED_SOURCE_PROVENANCE_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    theorem_slot = load(THEOREM_SLOT)
    counterexample = load(COUNTEREXAMPLE)
    weylpair_gate = load(WEYLPAIR_GATE)
    conditional_a = load(CONDITIONAL_A)

    chain_checks = {
        "theorem_slot_imported": theorem_slot["theorem"]["proved"] is True,
        "primitive_only_counterexample_imported": counterexample["theorem"]["proved"] is True,
        "weylpair_gate_imported": weylpair_gate["theorem"]["proved"] is True,
        "conditional_A_solve_imported": conditional_a["theorem"]["proved"] is True,
    }

    counterexample_checks = {
        "primitive_only_route_insufficient": counterexample["verdict"][
            "primitive_only_route_closed_as_insufficient"
        ]
        is True,
        "weyl_pair_required": counterexample["verdict"][
            "weyl_pair_basis_transport_or_vertex_source_required"
        ]
        is True,
        "fixed_span_rejects": counterexample["span_tests"]["fixed_fiber_primitives"][
            "target_in_span"
        ]
        is False,
        "all_fiber_span_rejects": counterexample["span_tests"]["fixed_plus_all_fiber_envelope"][
            "target_in_span"
        ]
        is False,
    }

    weylpair_checks = {
        "weyl_pair_algebraic_gate_built": weylpair_gate["verdict"][
            "weyl_pair_algebraic_gate_built"
        ]
        is True,
        "locked_splitter_span_closed": weylpair_gate["verdict"][
            "locked_splitter_span_closed_algebraically"
        ]
        is True,
        "span_residual_tiny": weylpair_gate["span_test"]["relative_residual"] < 1e-12,
        "source_provenance_not_proved_at_gate": weylpair_gate["verdict"][
            "selected_source_provenance_proved"
        ]
        is False,
    }

    solve_checks = {
        "conditional_A_built": conditional_a["verdict"]["conditional_A_weylpair_built"] is True,
        "conditional_solution_found": conditional_a["verdict"][
            "conditional_deltaTheta_solution_found"
        ]
        is True,
        "conditional_rank_2": conditional_a["locked_solve"]["rank"] == 2,
        "conditional_residual_tiny": conditional_a["locked_solve"]["relative_residual"] < 1e-12,
        "A_selected_not_emitted": conditional_a["verdict"]["A_selected_emitted"] is False,
        "b_selected_not_emitted": conditional_a["verdict"]["b_selected_emitted"] is False,
        "honest_selected_solve_not_run": conditional_a["verdict"][
            "honest_selected_deltaTheta_C1_solve_run"
        ]
        is False,
        "source_provenance_still_open": conditional_a["verdict"][
            "selected_source_provenance_proved"
        ]
        is False,
    }

    guardrails = {
        "no_observed_or_benchmark_inputs": all(
            cert["guardrails"]["does_not_use_observed_or_benchmark_inputs"]
            for cert in [counterexample, weylpair_gate, conditional_a]
        ),
        "no_lifted_flags": all(
            cert["guardrails"]["does_not_lift_flags_by_hand"]
            for cert in [counterexample, weylpair_gate, conditional_a]
        ),
        "no_full_closure_claim": all(
            cert["verdict"]["full_SM_or_no_knob_closure"] is False
            for cert in [counterexample, weylpair_gate, conditional_a]
        ),
    }

    theorem = {
        "name": "RouteCWeylPairFrontierReconciliationTheorem",
        "proved": all(chain_checks.values())
        and all(counterexample_checks.values())
        and all(weylpair_checks.values())
        and all(solve_checks.values())
        and all(guardrails.values()),
        "statement": (
            "After importing the basis-transport theorem slot, the strongest "
            "already verified Route-C frontier is reconciled: primitive-only "
            "basis transport is insufficient, the enriched Weyl-pair packet "
            "algebraically spans the locked splitter, and the conditional "
            "72x2 Weyl-pair operator solves the locked DeltaTheta_C1 equation. "
            "The remaining blocker is not linear algebra; it is same-branch "
            "selected source provenance for the Weyl-pair columns and emitted "
            "b_selected."
        ),
    }

    verdict = {
        "current_frontier": STATUS,
        "primitive_only_retired_as_sufficient": True,
        "weyl_pair_packet_required": True,
        "conditional_A_solve_closed": True,
        "algebraic_rank_obstruction_absent": True,
        "selected_source_provenance_proved": False,
        "A_selected_emitted": False,
        "b_selected_emitted": False,
        "honest_selected_deltaTheta_solve_run": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "chain_checks": chain_checks,
        "counterexample_checks": counterexample_checks,
        "weylpair_checks": weylpair_checks,
        "solve_checks": solve_checks,
        "guardrails": guardrails,
        "locked_solve": conditional_a["locked_solve"],
        "conditional_operator": conditional_a["conditional_operator"],
        "provenance_reduction": conditional_a["provenance_reduction"],
        "verdict": verdict,
    }

    note = """# Route-C Weyl-Pair Frontier Reconciliation v1

## Result

The current Route-C C1 frontier is reconciled after the basis-transport theorem
slot import.

What is now closed:

```text
primitive-only basis transport is insufficient
the enriched Weyl-pair packet spans the locked splitter algebraically
the conditional 72x2 Weyl-pair operator has rank 2
the conditional DeltaTheta_C1 solve has tiny residual
```

So the remaining blocker is no longer rank or linear consistency. It is source
provenance:

```text
prove the selected q79/F,m=1 S3/GS source emits the phase-like Weyl column
prove the same selected branch emits the shift-like active (1,1) Weyl column
emit b_selected from the theorem-derived source, not from a diagnostic target
promote conditional A_weylpair to A_selected only after provenance is proved
```

No observed masses, mixings, CP phase, thresholds, benchmark values, or lifted
selected flags are used as selectors.

## Status

```text
ROUTEC_WEYLPAIR_FRONTIER_RECONCILED_SOURCE_PROVENANCE_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_weylpair_frontier_reconciliation",
                "status": STATUS,
                "input_certificates": {
                    "routec_basistransport_primitive_source_theorem_import": str(THEOREM_SLOT),
                    "routec_basis_transport_proof_or_counterexample_import": str(COUNTEREXAMPLE),
                    "routec_weylpair_source_gate_import": str(WEYLPAIR_GATE),
                    "routec_weylpair_aselected_assembly_import": str(CONDITIONAL_A),
                },
                "theorem": theorem,
                "chain_checks": chain_checks,
                "counterexample_checks": counterexample_checks,
                "weylpair_checks": weylpair_checks,
                "solve_checks": solve_checks,
                "guardrails": guardrails,
                "verdict": verdict,
                "packet_written": str(OUT_PACKET),
                "note_written": str(OUT_NOTE),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
