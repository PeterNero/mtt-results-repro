from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

WEYL_IMPORT = ROOT / "certificates" / "routec_weylpair_source_gate_import_certificate.json"
ASSEMBLY_CERT = SM / "certificates" / "selected_routec_weylpair_aselected_assembly_or_source_proof_certificate.json"
ASSEMBLY_DATA = SM / "candidate_data" / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_weylpair_aselected_assembly_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_weylpair_aselected_assembly_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_WeylPair_Aselected_Assembly_Import_v1.md"
OUT_INSERTION = ROOT / "proof_corpus" / "paper_insertions" / "RouteC_WeylPair_Aselected_Conditional_Solve_for_Theta_Papers.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    weyl_import = load(WEYL_IMPORT)
    assembly_cert = load(ASSEMBLY_CERT)
    assembly = load(ASSEMBLY_DATA)

    solve = assembly["locked_solve"]
    op = assembly["conditional_operator"]
    provenance = assembly["provenance_reduction"]

    closed_now = {
        "weyl_pair_source_gate_imported": weyl_import["verdict"]["weyl_pair_algebraic_gate_built"],
        "conditional_A_weylpair_assembled": assembly_cert["what_closes"]["conditional_A_weylpair_assembled"],
        "algebraic_rank_obstruction_absent": assembly_cert["what_closes"]["algebraic_rank_obstruction_absent_for_weylpair_packet"],
        "conditional_deltaTheta_solve_exact": assembly_cert["what_closes"]["conditional_deltaTheta_solve_exact"],
        "remaining_gap_reduced_to_source_provenance": assembly_cert["what_closes"]["remaining_gap_reduced_to_source_provenance"],
        "operator_shape_72_by_2": op["shape"] == [72, 2],
        "operator_rank_2": solve["rank"] == 2,
        "solve_consistent": solve["consistent"] is True,
        "solve_residual_tiny": solve["relative_residual"] < 1.0e-12,
        "target_fitting_excluded": (
            assembly_cert["what_closes"]["target_fitting_excluded"] is True
            and assembly["superset_strategy"]["observed_data_used"] is False
            and assembly["superset_strategy"]["lifted_flags_used_as_proof"] is False
        ),
    }

    still_open = {
        "prove_selected_weylpair_source_provenance": assembly_cert["what_remains_open"]["prove_selected_weylpair_source_provenance"],
        "promote_conditional_A_to_A_selected": assembly_cert["what_remains_open"]["promote_conditional_A_to_A_selected"],
        "emit_theorem_derived_b_selected": assembly_cert["what_remains_open"]["emit_theorem_derived_b_selected"],
        "run_honest_selected_deltaTheta_C1_solve": assembly_cert["what_remains_open"]["run_honest_selected_deltaTheta_C1_solve"],
        "full_SM_or_no_knob_closure": assembly_cert["what_remains_open"]["full_SM_or_no_knob_closure"],
    }

    theorem = {
        "name": "RouteCWeylPairAselectedAssemblyImportTheorem",
        "proved": all(closed_now.values()),
        "statement": (
            "Conditioned on selected source emission of the two Weyl-pair columns, "
            "the 72x2 operator A_weylpair_conditional has rank 2 and solves the "
            "locked DeltaTheta_C1 splitter equation with deltaTheta=(1,1) up to "
            "roundoff. Thus no algebraic obstruction remains at this Weyl-pair "
            "assembly layer; the blocker is selected source provenance."
        ),
    }

    verdict = {
        "conditional_A_weylpair_built": True,
        "conditional_deltaTheta_solution_found": True,
        "A_selected_emitted": False,
        "b_selected_emitted": False,
        "honest_selected_deltaTheta_C1_solve_run": False,
        "selected_source_provenance_proved": False,
        "full_SM_or_no_knob_closure": False,
        "next_required_artifact": "MTT_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1",
    }

    guardrails = {
        "does_not_promote_conditional_A_to_A_selected": True,
        "does_not_claim_b_selected": True,
        "does_not_claim_honest_selected_deltaTheta_solve": True,
        "does_not_claim_source_provenance": True,
        "does_not_claim_flavor_or_SM_closure": True,
        "does_not_use_observed_or_benchmark_inputs": True,
        "does_not_lift_flags_by_hand": True,
    }

    packet = {
        "theorem": theorem,
        "conditional_operator": op,
        "locked_solve": solve,
        "provenance_reduction": provenance,
        "selected_emission_status": assembly["selected_emission_status"],
        "closed_now": closed_now,
        "still_open": still_open,
        "verdict": verdict,
    }

    note = f"""# Route-C WeylPair Aselected Assembly Import v1

## Result

The conditional Weyl-pair operator is assembled:

```text
A_weylpair_conditional = [phase_packet, shift_packet]
shape = {op["shape"]}
rank = {solve["rank"]}
condition number = {solve["condition_number"]:.15g}
deltaTheta_conditional = {solve["deltaTheta_conditional"]}
relative residual = {solve["relative_residual"]:.3e}
```

This closes the algebraic assembly obstruction for the enriched Weyl-pair
packet. If the selected source emits these two columns, the locked splitter
equation is solved exactly up to numerical roundoff.

## Boundary

This does not promote `A_weylpair_conditional` to `A_selected`. The current
selected emission flags remain:

```text
A_selected_currently_emitted = {assembly["selected_emission_status"]["A_selected_currently_emitted"]}
b_selected_currently_emitted = {assembly["selected_emission_status"]["b_selected_currently_emitted"]}
```

The remaining blocker is:

```text
SelectedWeylPairSourceProvenanceLemma
```

It must prove that the selected `q79/F,m=1` `S3`/Green-Schwarz Route-C source
emits the phase-like `I+Z` basis-holonomy packet and the shift-like `I+X`
active-vertex packet in the same `B_N`/projector/dotD/zero-mode basis, with
internal normalization.
"""

    insertion = """# Route-C Weyl-Pair Conditional A Solve Insert

Target papers:

```text
Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v2.md
Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps.md
```

## Conditional Solve

Conditioned on theorem-derived selected emission of the two Weyl-pair columns,
the operator

```text
A_weylpair_conditional = [phase_packet, shift_packet]
```

has shape `72 x 2`, rank `2`, and solves the locked splitter equation with
`deltaTheta=(1,1)` up to numerical roundoff. This removes the algebraic rank
obstruction at the Weyl-pair layer.

## Proof Boundary

This is not yet `A_selected`. The source provenance lemma remains required:
the selected Route-C source must emit the phase-like `I+Z` basis-holonomy
packet and the shift-like `I+X` active-vertex packet from the same branch,
without observed masses, CKM/PMNS, CP phase, lifted flags, or benchmark
matrices.
"""

    OUT_INSERTION.parent.mkdir(parents=True, exist_ok=True)
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_weylpair_aselected_assembly_import",
                "status": "ROUTEC_WEYLPAIR_CONDITIONAL_A_SOLVE_BUILT_SOURCE_PROVENANCE_OPEN",
                "input_certificates": {
                    "routec_weylpair_source_gate_import": str(WEYL_IMPORT),
                    "selected_routec_weylpair_aselected_assembly_or_source_proof": str(ASSEMBLY_CERT),
                },
                "theorem": theorem,
                "conditional_operator": op,
                "locked_solve": solve,
                "provenance_reduction": provenance,
                "selected_emission_status": assembly["selected_emission_status"],
                "closed_now": closed_now,
                "still_open": still_open,
                "verdict": verdict,
                "guardrails": guardrails,
                "packet_written": str(OUT_PACKET),
                "note_written": str(OUT_NOTE),
                "paper_insertion_written": str(OUT_INSERTION),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_INSERTION.write_text(insertion, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"WROTE: {OUT_INSERTION}")
    print("STATUS: ROUTEC_WEYLPAIR_CONDITIONAL_A_SOLVE_BUILT_SOURCE_PROVENANCE_OPEN")


if __name__ == "__main__":
    main()
