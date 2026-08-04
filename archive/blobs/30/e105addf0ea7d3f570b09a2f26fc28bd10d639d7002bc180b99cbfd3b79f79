from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

COUNTER_IMPORT = ROOT / "certificates" / "routec_basis_transport_proof_or_counterexample_import_certificate.json"
WEYL_CERT = SM / "certificates" / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem_certificate.json"
WEYL_DATA = SM / "candidate_data" / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_weylpair_source_gate_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_weylpair_source_gate_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_WeylPair_Source_Gate_Import_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    counter = load(COUNTER_IMPORT)
    weyl_cert = load(WEYL_CERT)
    weyl = load(WEYL_DATA)

    span = weyl["span_test"]
    packet = weyl["enriched_weyl_pair_packet"]
    theorem_gate = weyl["theorem_gate"]
    contract = weyl["source_contract"]

    closed_now = {
        "primitive_only_counterexample_imported": counter["verdict"]["primitive_only_route_closed_as_insufficient"],
        "minimal_weyl_pair_packet_defined": weyl_cert["what_closes"]["minimal_weyl_pair_packet_defined"],
        "locked_splitter_reconstructed_by_weyl_pair": weyl_cert["what_closes"]["locked_splitter_reconstructed_by_weyl_pair"],
        "primitive_only_failure_localized_to_missing_phase_like_component": weyl_cert["what_closes"]["primitive_only_failure_localized_to_missing_phase_like_component"],
        "selected_source_contract_for_A_selected_defined": weyl_cert["what_closes"]["selected_source_contract_for_A_selected_defined"],
        "phase_and_shift_packets_present": set(packet["source_directions"]) == {"phase_packet", "shift_packet"},
        "span_test_exact_to_tolerance": span["target_in_span"] is True and span["relative_residual"] < 1.0e-12,
        "target_fitting_excluded": (
            weyl_cert["what_closes"]["target_fitting_excluded"] is True
            and weyl["superset_strategy"]["observed_data_used"] is False
            and weyl["superset_strategy"]["lifted_flags_used_as_proof"] is False
        ),
    }

    still_open = {
        "prove_selected_phase_like_Z_or_basis_holonomy_source": weyl_cert["what_remains_open"]["prove_selected_phase_like_Z_or_basis_holonomy_source"],
        "prove_selected_shift_like_X_vertex_source": weyl_cert["what_remains_open"]["prove_selected_shift_like_X_vertex_source"],
        "assemble_theorem_derived_A_selected": weyl_cert["what_remains_open"]["assemble_theorem_derived_A_selected"],
        "emit_theorem_derived_b_selected": weyl_cert["what_remains_open"]["emit_theorem_derived_b_selected"],
        "solve_or_reject_locked_deltaTheta_C1_equation": weyl_cert["what_remains_open"]["solve_or_reject_locked_deltaTheta_C1_equation"],
        "full_SM_or_no_knob_closure": weyl_cert["what_remains_open"]["full_SM_or_no_knob_closure"],
    }

    theorem = {
        "name": "RouteCWeylPairSourceGateImportTheorem",
        "proved": all(closed_now.values()),
        "statement": (
            "The minimal enriched Weyl-pair packet is imported as an algebraically "
            "sufficient source gate: a phase-like packet on u/e and a shift-like "
            "packet on d/nuD exactly reconstruct the locked qutrit/Weyl splitter "
            "target. This defines the selected-source contract for A_selected, "
            "but does not prove same-branch source provenance or emit A_selected/b_selected."
        ),
    }

    verdict = {
        "weyl_pair_algebraic_gate_built": True,
        "locked_splitter_span_closed_algebraically": True,
        "selected_source_provenance_proved": False,
        "A_selected_emitted": False,
        "b_selected_emitted": False,
        "deltaTheta_C1_solved": False,
        "full_SM_or_no_knob_closure": False,
        "next_required_artifact": "MTT_Selected_RouteC_WeylPair_Aselected_Assembly_or_Source_Proof_v1",
    }

    guardrails = {
        "does_not_claim_source_provenance": True,
        "does_not_claim_A_selected_or_b_selected": True,
        "does_not_claim_deltaTheta_solution": True,
        "does_not_claim_flavor_or_SM_closure": True,
        "does_not_use_observed_or_benchmark_inputs": True,
        "does_not_lift_flags_by_hand": True,
    }

    out_packet = {
        "theorem": theorem,
        "enriched_weyl_pair_packet": packet,
        "span_test": span,
        "source_contract": contract,
        "theorem_gate": theorem_gate,
        "closed_now": closed_now,
        "still_open": still_open,
        "verdict": verdict,
    }

    note = f"""# Route-C WeylPair Source Gate Import v1

## Result

The minimal enriched Weyl-pair packet is algebraically sufficient for the locked
qutrit/Weyl splitter target.

```text
columns = {span["columns"]}
rank = {span["rank"]}
relative residual = {span["relative_residual"]:.3e}
target_in_span = {span["target_in_span"]}
```

The two required directions are:

```text
phase_packet: u,e = I + Z; d,nuD = 0
shift_packet: d,nuD = I + X; u,e = 0
```

This is the precise repair of the primitive-only counterexample: the missing
piece was the phase-like qutrit/basis-holonomy component.

## Boundary

This is still not selected flavor or full SM closure. It defines the algebraic
source contract for `A_selected`, but same-branch provenance remains open:

```text
prove selected phase-like Z or basis holonomy source
prove selected shift-like X vertex source
assemble theorem-derived A_selected
emit theorem-derived b_selected
solve or reject the locked DeltaTheta_C1 equation
```

## Status

```text
ROUTEC_WEYLPAIR_SOURCE_GATE_IMPORTED_ASELECTED_SOURCE_OPEN
```
"""

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "routec_weylpair_source_gate_import",
        "status": "ROUTEC_WEYLPAIR_SOURCE_GATE_IMPORTED_ASELECTED_SOURCE_OPEN",
        "input_certificates": {
            "routec_basis_transport_proof_or_counterexample_import": str(COUNTER_IMPORT),
            "selected_routec_weylpair_basis_transport_or_vertex_source_theorem": str(WEYL_CERT),
        },
        "theorem": theorem,
        "span_test": span,
        "source_contract": contract,
        "theorem_gate": theorem_gate,
        "closed_now": closed_now,
        "still_open": still_open,
        "verdict": verdict,
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    OUT_PACKET.write_text(json.dumps(out_packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print("STATUS: ROUTEC_WEYLPAIR_SOURCE_GATE_IMPORTED_ASELECTED_SOURCE_OPEN")


if __name__ == "__main__":
    main()
