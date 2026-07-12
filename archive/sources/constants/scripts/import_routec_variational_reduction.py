"""Import Route-C differentiated C1 variational reduction gate."""

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

PREVIOUS = CERTS / "routec_dependency_cutset_import_certificate.json"
UPSTREAM_SLUG = "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve"
UPSTREAM_PACKET = SM / "candidate_data" / f"{UPSTREAM_SLUG}.candidate.json"
UPSTREAM_CERT = SM / "certificates" / f"{UPSTREAM_SLUG}_certificate.json"
UPSTREAM_NOTE = SM / "proof_corpus" / "MTT_Selected_DifferentiatedC1OrthogonalCompletionPrinciple_or_IndependentQuadratureHessianSolve_v1.md"
UPSTREAM_DIR = SM / "candidate_data" / UPSTREAM_SLUG
VARIATIONAL = UPSTREAM_DIR / "orthogonal_completion_variational_derivation.packet.json"
QUADRATURE = UPSTREAM_DIR / "independent_quadrature_hessian_solve_spec.packet.json"
SUFFICIENCY = UPSTREAM_DIR / "principle_or_solve_sufficiency_replay.packet.json"

OUTPUT_PACKET = DATA / "routec_variational_reduction_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_variational_reduction_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_VariationalReduction_Import_v1.md"

STATUS = "ROUTEC_VARIATIONAL_REDUCTION_IMPORTED_C1_DEFECT_SOURCE_OPEN"
PREVIOUS_STATUS = "ROUTEC_DEPENDENCY_CUTSET_IMPORTED_ORTHOGONAL_COMPLETION_OR_INDEPENDENT_SOLVE_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_DIFFERENTIATEDC1ORTHOGONALCOMPLETIONPRINCIPLE_OR_INDEPENDENTQUADRATUREHESSIANSOLVE_BUILT_VARIATIONAL_REDUCTION_OPEN"
NEXT = "MTT_Selected_C1DefectFunctionalSource_or_IndependentQuadratureDataFill_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    cert = load(UPSTREAM_CERT)
    variational = load(VARIATIONAL)
    quadrature = load(QUADRATURE)
    sufficiency = load(SUFFICIENCY)
    note = UPSTREAM_NOTE.read_text(encoding="utf-8")

    derived = variational["derived_inside_this_gate"]
    not_derived = variational["not_derived_inside_this_gate"]
    replay = sufficiency["current_replay_values"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_DifferentiatedC1OrthogonalCompletionPrinciple_or_IndependentQuadratureHessianSolve_v1",
        "F1_upstream_variational_reduction_proved_open": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["patched_spine_closure_preserved"] is True
        and upstream["unpatched_theorem_closure_claimed"] is False
        and upstream["observed_data_used"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": cert["status"] == UPSTREAM_STATUS
        and cert["theorem_proved"] is True
        and cert["patched_spine_closure_preserved"] is True
        and cert["unpatched_theorem_closure_claimed"] is False
        and cert["next_required_artifact"] == NEXT,
        "F3_variational_euler_projection_derived": variational["status"] == "EULER_PROJECTION_DERIVED_SELECTED_FUNCTIONAL_OPEN"
        and derived["finite_dimensional_projection_euler_equation"] is True
        and derived["least_norm_trace_orthogonal_completion_selects_Q_residual"] is True
        and derived["if_selected_C1_defect_functional_equals_candidate_then_PhiFinC1_applies_Q_residual"] is True
        and not_derived["selected_MTT_C1_defect_functional_is_candidate"] is True
        and not_derived["physical_PhiFinC1_variation_minimizes_this_functional"] is True
        and len(variational["proof_reduction"]) == 4,
        "F4_independent_solve_spec_ready_not_run": quadrature["status"] == "NUMERICAL_SOLVE_SPEC_READY_DATA_MISSING"
        and quadrature["acceptance_tests"]["A_shape"] == [72, 2]
        and quadrature["acceptance_tests"]["b_shape"] == [72]
        and len(quadrature["required_values"]) == 6
        and quadrature["run_now"] is False
        and len(quadrature["why_not_run_now"]) == 3
        and "copying R_Z/R_X from the residual-projector axiom contract" in quadrature["quadrature_requirements"]["forbidden"],
        "F5_sufficiency_replay_antecedent_open": sufficiency["status"] == "SUFFICIENCY_PROVED_ANTECEDENT_OPEN"
        and sufficiency["if_variational_source_functional_selected"]["SM_parity_dynamic_packet_closes"] is True
        and sufficiency["if_independent_quadrature_hessian_solve_passes"]["SM_parity_dynamic_packet_closes"] is True
        and replay["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]]
        and replay["A_transpose_b"] == [12.0, 12.0]
        and replay["deltaTheta_C1"] == [1.0, 1.0]
        and sufficiency["antecedent_met_now"] is False,
        "F6_remaining_gates_preserved": all(
            upstream["what_remains_open"][key] is True
            for key in [
                "select_C1_defect_leakage_functional_from_MTT",
                "prove_physical_PhiFinC1_minimizes_selected_defect_functional",
                "fill_selected_zero_mode_basis_data",
                "fill_independent_primitive_quadrature_table",
                "fill_independent_hessian_source_vector",
                "run_independent_quadrature_hessian_solve",
                "unpatched_SM_parity_dynamic_packet_closure",
                "true_SM_equivalence_closure",
            ]
        ),
        "F7_promotion_guardrails_preserved": upstream["promotion_decision"]["variational_euler_projection_derived"] is True
        and upstream["promotion_decision"]["selected_C1_defect_functional_proved"] is False
        and upstream["promotion_decision"]["physical_PhiFinC1_application_rule_proved"] is False
        and upstream["promotion_decision"]["independent_quadrature_hessian_solve_run"] is False
        and upstream["promotion_decision"]["unpatched_SM_parity_dynamic_packet_closed"] is False
        and "variational reduction" in note,
    }

    summary = {
        "finite_euler_projection_derived": True,
        "orthogonal_completion_reduced_to_C1_defect_functional": True,
        "selected_C1_defect_functional_proved": False,
        "physical_PhiFinC1_application_rule_proved": False,
        "independent_quadrature_hessian_solve_run": False,
        "A_transpose_A": replay["A_transpose_A"],
        "A_transpose_b": replay["A_transpose_b"],
        "deltaTheta_C1": replay["deltaTheta_C1"],
        "next_two_exits": [
            "select_C1_defect_leakage_functional_from_MTT",
            "fill_and_run_independent_quadrature_hessian_solve",
        ],
    }

    return {
        "packet": "RouteC_VariationalReduction_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
            "upstream_variational_derivation": str(VARIATIONAL),
            "upstream_quadrature_solve_spec": str(QUADRATURE),
            "upstream_sufficiency_replay": str(SUFFICIENCY),
        },
        "theorem": {
            "name": "RouteCVariationalReductionImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The differentiated C1 orthogonal-completion rule is reduced "
                "to the Euler equation of a finite least-Frobenius C1 defect "
                "functional.  The remaining source gate is to select that "
                "functional from MTT, prove PhiFinC1 minimizes it, or supply "
                "independent quadrature/Hessian data."
            ),
        },
        "checks": checks,
        "variational_reduction_summary": summary,
        "upstream_candidate": upstream,
        "upstream_packets": {
            "orthogonal_completion_variational_derivation": variational,
            "independent_quadrature_hessian_solve_spec": quadrature,
            "principle_or_solve_sufficiency_replay": sufficiency,
        },
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_selected_C1_defect_functional": False,
            "claims_physical_PhiFinC1_application_rule": False,
            "claims_independent_quadrature_hessian_solve": False,
            "claims_unpatched_SM_dynamic_closure": False,
            "claims_true_SM_equivalence": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCVariationalReductionImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "variational_reduction_summary": packet["variational_reduction_summary"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    s = cert["variational_reduction_summary"]
    return f"""# RouteC Variational Reduction Import v1

Status: `{cert["status"]}`.

The unpatched C1 route has advanced from an axiom-shaped gap to a variational
source gap.  The finite Euler projection is derived, and the orthogonal
completion rule is reduced to selection of the C1 defect/leakage functional.

Current replay remains:

```text
A^T A = {s["A_transpose_A"]}
A^T b = {s["A_transpose_b"]}
deltaTheta_C1 = {s["deltaTheta_C1"]}
```

Still not claimed: selected C1 defect functional, physical `Phi_fin^C1`
application rule, independent quadrature/Hessian solve, unpatched SM dynamic
closure, or true SM equivalence.

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
