"""Import Route-C Weyl-pair conditional A solve and source-provenance frontier."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = CERTS / "differentiated_phifinc1_primitiveoverlap_or_galerkinrun_import_certificate.json"
SM_COUNTEREXAMPLE = SM / "candidate_data" / "selected_routec_basis_transport_primitive_source_proof_or_counterexample.candidate.json"
SM_WEYL_GATE = SM / "candidate_data" / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem.candidate.json"
SM_ASSEMBLY = SM / "candidate_data" / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"
Q79_ASSEMBLY = Q79 / "candidate_data" / "q79_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"

OUTPUT_PACKET = DATA / "routec_weylpair_conditional_a_solve_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_weylpair_conditional_a_solve_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_WeylPair_Conditional_A_Solve_Import_v1.md"

STATUS = "ROUTEC_WEYLPAIR_CONDITIONAL_A_SOLVE_IMPORTED_SOURCE_PROVENANCE_OPEN"
PREVIOUS_STATUS = "DIFFERENTIATED_PHIFINC1_PRIMITIVE_OVERLAP_IMPORTED_TRANSPORT_NOGO_TEMPLATE_OPEN"
NEXT = "Q79_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    counterexample = load(SM_COUNTEREXAMPLE)
    gate = load(SM_WEYL_GATE)
    assembly = load(SM_ASSEMBLY)
    q79 = load(Q79_ASSEMBLY)

    sm_solve = assembly["locked_solve"]
    q79_solve = q79["conditional_solve"]["locked_solve"]
    q79_operator = q79["conditional_solve"]["conditional_operator"]

    checks = {
        "I0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "I1_primitive_only_counterexample_proved": counterexample["source_attempt"][
            "counterexample_proved"
        ]
        is True
        and counterexample["source_attempt"]["selected_source_emission_proved"] is False
        and counterexample["span_tests"]["fixed_fiber_primitives"]["target_in_span"] is False
        and counterexample["span_tests"]["fixed_plus_all_fiber_envelope"]["target_in_span"] is False,
        "I2_weyl_pair_gate_algebraically_sufficient": gate["span_test"]["target_in_span"] is True
        and gate["span_test"]["rank"] == 2
        and gate["span_test"]["relative_residual"] < 1e-12
        and gate["source_contract"]["operator_emission_status_imported"]["A_selected_currently_emitted"]
        is False
        and gate["source_contract"]["operator_emission_status_imported"]["b_selected_currently_emitted"]
        is False,
        "I3_sm_conditional_solve_exact": assembly["conditional_operator"]["is_A_selected"] is False
        and assembly["selected_emission_status"]["A_selected_currently_emitted"] is False
        and assembly["selected_emission_status"]["b_selected_currently_emitted"] is False
        and sm_solve["rank"] == 2
        and sm_solve["consistent"] is True
        and sm_solve["relative_residual"] < 1e-12
        and sm_solve["deltaTheta_conditional"] == [1.0, 1.0000000000000002],
        "I4_q79_conditional_solve_exact": q79_operator["is_A_selected"] is False
        and q79["decision"]["conditional_A_weylpair_assembled"] is True
        and q79["decision"]["conditional_deltaTheta_solve_exact"] is True
        and q79["decision"]["conditional_A_promoted_to_A_selected"] is False
        and q79["decision"]["A_selected_emitted"] is False
        and q79["decision"]["b_selected_emitted"] is False
        and q79_solve["rank"] == 2
        and q79_solve["consistent"] is True
        and q79_solve["relative_residual"] < 1e-12,
        "I5_remaining_gap_is_source_provenance": assembly["provenance_reduction"]["status"]
        == "NEXT_LEMMA_REQUIRED"
        and q79["conditional_solve"]["provenance_reduction"]["status"] == "NEXT_LEMMA_REQUIRED"
        and q79["next_required_artifact"] == NEXT,
        "I6_no_target_or_selected_overclaim": assembly["closure_claimed"] is False
        and assembly["target_fitting_used"] is False
        and q79["closure_claimed"] is False
        and q79["target_fitting_used"] is False
        and q79["guardrails"]["claims_A_selected_emitted"] is False
        and q79["guardrails"]["claims_b_selected_emitted"] is False
        and q79["guardrails"]["claims_conditional_A_is_A_selected"] is False
        and q79["guardrails"]["claims_selected_source_provenance_proved"] is False
        and q79["guardrails"]["uses_observed_flavor_data"] is False
        and q79["guardrails"]["uses_benchmark_flavor_entries"] is False,
    }

    return {
        "packet": "RouteC_WeylPair_Conditional_A_Solve_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "sm_primitive_only_counterexample": str(SM_COUNTEREXAMPLE),
            "sm_weylpair_gate": str(SM_WEYL_GATE),
            "sm_weylpair_assembly": str(SM_ASSEMBLY),
            "q79_weylpair_assembly": str(Q79_ASSEMBLY),
        },
        "theorem": {
            "name": "RouteCWeylPairConditionalASolveImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "Primitive-only basis transport is insufficient for the locked "
                "72-real splitter target, but the enriched Weyl-pair packet is "
                "algebraically sufficient. Conditioned on selected source "
                "provenance, the two-column Weyl-pair operator has rank 2 and "
                "solves the locked DeltaTheta_C1 equation with deltaTheta=(1,1). "
                "The remaining blocker is not linear algebra; it is proving that "
                "the selected q79/Route-C source emits those two columns and the "
                "corresponding b_selected without target fitting."
            ),
        },
        "checks": checks,
        "primitive_only_counterexample": counterexample,
        "weylpair_source_gate": gate,
        "sm_conditional_assembly": assembly,
        "q79_conditional_assembly": q79,
        "conditional_solve_summary": {
            "operator_name": q79_operator["name"],
            "operator_shape": q79_operator["shape"],
            "operator_is_A_selected": False,
            "columns": q79_operator["columns"],
            "rank": q79_solve["rank"],
            "condition_number": q79_solve["condition_number"],
            "deltaTheta_conditional": q79_solve["deltaTheta_conditional"],
            "relative_residual": q79_solve["relative_residual"],
            "residual_norm": q79_solve["residual_norm"],
            "exact_to_tolerance": q79["conditional_solve"]["exact_to_tolerance"],
        },
        "source_provenance_obligations": q79["conditional_solve"]["provenance_reduction"]["must_prove"],
        "what_closes_now": {
            "primitive_only_span_counterexample_imported": True,
            "weylpair_packet_algebraically_sufficient": True,
            "conditional_A_weylpair_assembled": True,
            "conditional_deltaTheta_solve_exact": True,
            "rank_and_consistency_obstruction_removed": True,
            "remaining_gap_reduced_to_source_provenance": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "prove_selected_weylpair_source_provenance": True,
            "promote_conditional_A_to_A_selected": True,
            "emit_theorem_derived_b_selected": True,
            "run_honest_selected_deltaTheta_C1_solve": True,
            "selected_PhiFin_alpha1_payload_values": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "conditional_A_is_A_selected": False,
            "A_selected_emitted": False,
            "b_selected_emitted": False,
            "selected_source_provenance_proved": False,
            "honest_selected_deltaTheta_solve_run": False,
            "observed_flavor_data_used": False,
            "benchmark_flavor_entries_used": False,
            "target_fitting_used": False,
            "full_SM_closure_claimed": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCWeylPairConditionalASolveImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "conditional_solve_summary": packet["conditional_solve_summary"],
        "source_provenance_obligations": packet["source_provenance_obligations"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    solve = cert["conditional_solve_summary"]
    return f"""# RouteC WeylPair Conditional A Solve Import v1

Status: `{cert["status"]}`.

Primitive-only basis transport is now a counterexample branch: its span does
not contain the locked 72-real qutrit/Weyl splitter target.  The enriched
Weyl-pair packet fixes that algebraic obstruction.

Conditioned on source provenance, the imported operator has:

```text
shape                 = {solve["operator_shape"]}
rank                  = {solve["rank"]}
condition_number      = {solve["condition_number"]}
deltaTheta_conditional = {solve["deltaTheta_conditional"]}
relative_residual     = {solve["relative_residual"]}
```

This operator is not promoted to `A_selected`: the source-provenance lemma still
has to prove that the selected q79/Route-C branch emits the phase-like and
shift-like Weyl-pair columns, and then emit `b_selected`.

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
