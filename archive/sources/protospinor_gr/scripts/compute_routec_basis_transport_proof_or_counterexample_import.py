from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

REDUCTION_CERT = ROOT / "certificates" / "routec_basis_transport_gate_reduction_import_certificate.json"
COUNTER_CERT = SM / "certificates" / "selected_routec_basis_transport_primitive_source_proof_or_counterexample_certificate.json"
COUNTER_DATA = SM / "candidate_data" / "selected_routec_basis_transport_primitive_source_proof_or_counterexample.candidate.json"
FLAVOR_CERT = SM / "certificates" / "selected_routec_higherorder_fullresponse_flavor_splitting_certificate.json"
FLAVOR_DATA = SM / "candidate_data" / "selected_routec_higherorder_fullresponse_flavor_splitting.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_basis_transport_proof_or_counterexample_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_basis_transport_proof_or_counterexample_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_BasisTransport_Proof_or_Counterexample_Import_v1.md"
OUT_INSERTION = ROOT / "proof_corpus" / "paper_insertions" / "RouteC_WeylPair_BasisTransport_Refinement_for_Strominger_and_Theta_Papers.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    reduction = load(REDUCTION_CERT)
    counter_cert = load(COUNTER_CERT)
    counter = load(COUNTER_DATA)
    flavor_cert = load(FLAVOR_CERT)
    flavor = load(FLAVOR_DATA)

    span = counter["span_tests"]
    primitive_span = span["fixed_fiber_primitives"]
    primitive_plus_all = span["fixed_plus_all_fiber_envelope"]
    higher = flavor["path_A_higher_order_criterion"]
    full = flavor["path_B_full_response_criterion"]

    closed_now = {
        "previous_basis_transport_gate_reduced": reduction["verdict"]["basis_transport_gate_reduced"],
        "primitive_only_counterexample_built": counter_cert["what_closes"]["primitive_only_counterexample_built"],
        "locked_splitter_span_test_run": counter_cert["what_closes"]["locked_splitter_span_test_run"],
        "primitive_fixed_fiber_span_rejects_target": primitive_span["target_in_span"] is False,
        "primitive_plus_all_fiber_span_rejects_target": primitive_plus_all["target_in_span"] is False,
        "I7_refined_to_weyl_pair_source_theorem": counter_cert["what_closes"]["I7_refined_to_weyl_pair_source_theorem"],
        "current_scalar_permutation_layer_no_go_proved": flavor_cert["what_closes"]["current_scalar_permutation_layer_no_go_proved"],
        "higher_order_splitting_criterion_proved": flavor_cert["what_closes"]["higher_order_splitting_criterion_proved"],
        "full_response_acceptance_tests_locked": flavor_cert["what_closes"]["full_response_acceptance_tests_locked"],
        "target_fitting_excluded": (
            counter_cert["what_closes"]["target_fitting_excluded"] is True
            and flavor_cert["what_closes"]["target_fitting_excluded"] is True
            and counter["superset_strategy"]["observed_data_used"] is False
        ),
    }

    still_open = {
        "prove_selected_weyl_pair_basis_transport_or_vertex_source": counter_cert["what_remains_open"]["prove_selected_weyl_pair_basis_transport_or_vertex_source"],
        "emit_enriched_A_selected": counter_cert["what_remains_open"]["emit_enriched_A_selected"],
        "emit_b_selected": counter_cert["what_remains_open"]["emit_b_selected"],
        "solve_or_reject_splitter_equation": counter_cert["what_remains_open"]["solve_or_reject_splitter_equation"],
        "selected_higher_order_correction_matrices": flavor_cert["what_remains_open"]["selected_higher_order_correction_matrices"],
        "selected_full_response_matrices": flavor_cert["what_remains_open"]["selected_full_response_matrices"],
        "finite_C1_Hessian_and_deltaTheta": flavor_cert["what_remains_open"]["finite_C1_Hessian_and_deltaTheta"],
        "alpha1_driver_verified": flavor_cert["what_remains_open"]["alpha1_driver_verified"],
        "selected_dotD_source_verified": flavor_cert["what_remains_open"]["selected_dotD_source_verified"],
        "nondegenerate_yukawa_hierarchy": flavor_cert["what_remains_open"]["nondegenerate_yukawa_hierarchy"],
        "CKM_PMNS_CP_from_selected_matrices": flavor_cert["what_remains_open"]["CKM_PMNS_CP_from_selected_matrices"],
        "full_SM_or_no_knob_closure": flavor_cert["what_remains_open"]["full_SM_or_no_knob_closure"],
    }

    theorem = {
        "name": "RouteCBasisTransportProofOrCounterexampleImportTheorem",
        "proved": all(closed_now.values()),
        "statement": (
            "The primitive-only I7 source theorem is refuted as sufficient: the "
            "real span of the fixed-fiber primitive responses, even after adding "
            "the all-fiber envelope, does not contain the locked qutrit/Weyl "
            "splitter target. The next source theorem must emit an enriched "
            "Weyl-pair basis-transport or vertex response with both phase-like "
            "and shift-like qutrit directions. Independently, the current "
            "scalar-permutation C1 layer is proved flavor-degenerate, so flavor "
            "closure requires selected higher-order or full-response matrices."
        ),
    }

    refined_next = counter["refined_next_theorem"]
    acceptance_tests = {
        "mass_splitting": higher["mass_splitting_condition"],
        "mixing": higher["mixing_condition"],
        "CP": higher["cp_condition"],
        "full_response_required_outputs": full["required_outputs"],
        "full_response_required_stages": full["required_stages"],
    }

    verdict = {
        "primitive_only_route_closed_as_insufficient": True,
        "weyl_pair_basis_transport_or_vertex_source_required": True,
        "current_layer_flavor_no_go_proved": True,
        "selected_source_emission_proved": False,
        "selected_enriched_A_or_b_emitted": False,
        "selected_correction_values_computed": False,
        "full_SM_or_no_knob_closure": False,
        "next_required_artifact": "MTT_Selected_RouteC_WeylPair_BasisTransport_or_Vertex_Source_Theorem_v1",
        "next_value_artifact_after_source": "MTT_Selected_RouteC_First_Selected_Correction_Matrix_Search_or_Galerkin_Run_v1",
    }

    guardrails = {
        "does_not_claim_selected_source_emission": True,
        "does_not_claim_A_selected_or_b_selected": True,
        "does_not_claim_deltaTheta_solution": True,
        "does_not_claim_flavor_or_SM_closure": True,
        "does_not_use_observed_or_benchmark_inputs": True,
        "does_not_lift_flags_by_hand": True,
    }

    packet = {
        "theorem": theorem,
        "span_tests": span,
        "refined_next_theorem": refined_next,
        "current_layer_no_go": flavor["current_layer_no_go"],
        "acceptance_tests": acceptance_tests,
        "closed_now": closed_now,
        "still_open": still_open,
        "verdict": verdict,
    }

    note = f"""# Route-C BasisTransport Proof or Counterexample Import v1

## Result

The primitive-only source theorem is not sufficient.

Even under conditional promotion of the current non-invariant primitive family,
the finite real span of the fixed-fiber primitive responses does not contain the
locked qutrit/Weyl splitter target:

```text
fixed-fiber target_in_span = {primitive_span["target_in_span"]}
fixed-fiber relative residual = {primitive_span["relative_residual"]:.6f}
fixed + all-fiber target_in_span = {primitive_plus_all["target_in_span"]}
fixed + all-fiber relative residual = {primitive_plus_all["relative_residual"]:.6f}
target dimension = {span["target_dimension"]}
```

So the I7 theorem has been sharpened. The next source theorem must emit an
enriched Weyl-pair basis-transport or vertex response containing both:

```text
phase-like qutrit Z component or equivalent basis holonomy
shift-like qutrit X component tied to active shift (1,1)
```

## Flavor Boundary

The current scalar-permutation C1 layer is also a no-go for flavor splitting:
`Y0 Y0*` is scalar identity in every sector. It can provide a scaffold and a
diagnostic splitter, but it cannot by itself produce nondegenerate masses,
CKM/PMNS mixing, or CP violation.

## Next Gate

```text
MTT_Selected_RouteC_WeylPair_BasisTransport_or_Vertex_Source_Theorem_v1
```

After that source theorem exists, the next value artifact is:

```text
MTT_Selected_RouteC_First_Selected_Correction_Matrix_Search_or_Galerkin_Run_v1
```
"""

    insertion = """# Route-C Weyl-Pair BasisTransport Refinement Insert

Target papers:

```text
Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md
Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v2.md
Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps.md
```

## Refinement

The primitive-only Route-C C1 source theorem is insufficient. The finite span of
the current fixed-fiber non-invariant primitive family, even with the all-fiber
envelope added, does not contain the locked qutrit/Weyl splitter target.

Therefore the selected source theorem must be strengthened:

```text
SelectedWeylPairBasisTransportOrVertexSourceTheorem
```

The selected `q79/F,m=1` `S3`/Green-Schwarz Route-C source must emit a
basis-transport or vertex response whose projected response contains both
shift-like and phase-like qutrit Weyl directions. The active deck shift `(1,1)`
remains forced, but the phase/basis-holonomy component is necessary before
`A_selected` can reach the splitter.

## Guardrail

This is not a Standard Model closure theorem. The current C1 layer remains
flavor-degenerate because `Y0 Y0*` is scalar identity in each sector. Selected
higher-order or full-response matrices must still be emitted before Yukawa,
CKM/PMNS, or CP claims can be tested.
"""

    OUT_INSERTION.parent.mkdir(parents=True, exist_ok=True)
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_basis_transport_proof_or_counterexample_import",
                "status": "ROUTEC_PRIMITIVE_ONLY_COUNTEREXAMPLE_IMPORTED_WEYL_PAIR_SOURCE_OPEN",
                "input_certificates": {
                    "routec_basis_transport_gate_reduction_import": str(REDUCTION_CERT),
                    "selected_routec_basis_transport_primitive_source_proof_or_counterexample": str(COUNTER_CERT),
                    "selected_routec_higherorder_fullresponse_flavor_splitting": str(FLAVOR_CERT),
                },
                "theorem": theorem,
                "span_tests": span,
                "refined_next_theorem": refined_next,
                "acceptance_tests": acceptance_tests,
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
    print("STATUS: ROUTEC_PRIMITIVE_ONLY_COUNTEREXAMPLE_IMPORTED_WEYL_PAIR_SOURCE_OPEN")


if __name__ == "__main__":
    main()
