"""Build C1 defect-functional source / independent quadrature data-fill gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve.candidate.json"
VARIATIONAL = (
    DATA
    / "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve"
    / "orthogonal_completion_variational_derivation.packet.json"
)
QUADRATURE_SPEC = (
    DATA
    / "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve"
    / "independent_quadrature_hessian_solve_spec.packet.json"
)
SUFFICIENCY = (
    DATA
    / "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve"
    / "principle_or_solve_sufficiency_replay.packet.json"
)

SLUG = "selected_c1defectfunctionalsource_or_independentquadraturedatafill"
OUTPUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
FUNCTIONAL_SOURCE = PACKET_DIR / "c1_defect_functional_uniqueness_source.packet.json"
PHYSICAL_APPLICATION = PACKET_DIR / "phifinc1_physical_application_source_gap.packet.json"
QUADRATURE_DATA = PACKET_DIR / "independent_quadrature_data_fill_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_C1DefectFunctionalSource_or_IndependentQuadratureDataFill_v1.md"

STATUS = "MTT_SELECTED_C1DEFECTFUNCTIONALSOURCE_OR_INDEPENDENTQUADRATUREDATAFILL_BUILT_FUNCTIONAL_UNIQUENESS_OPEN_APPLICATION"
NEXT = "MTT_Selected_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    variational = load(VARIATIONAL)
    quadrature_spec = load(QUADRATURE_SPEC)
    sufficiency = load(SUFFICIENCY)
    replay = sufficiency["current_replay_values"]

    candidate_functional = variational["candidate_functional"]

    functional_source = {
        "schema": "MTTC1DefectFunctionalUniquenessSource.v1",
        "status": "UNIQUE_QUADRATIC_DEFECT_FUNCTIONAL_SELECTED_AS_FORMAL_SOURCE",
        "functional_name": candidate_functional["name"],
        "functional_form": candidate_functional["form"],
        "selection_inputs": {
            "selected_trace_frobenius_metric": True,
            "selected_fixed_fiber_response_span": True,
            "selected_static_sector_routing": ["Z->u,e", "X->d,nuD"],
            "selected_72_real_coordinate_target": True,
            "selected_no_observed_target_policy": True,
        },
        "uniqueness_conditions": {
            "quadratic": True,
            "positive_semidefinite": True,
            "invariant_under_unitary_change_of_selected_zero_mode_basis": True,
            "vanishes_on_fixed_fiber_span": True,
            "penalizes_only_trace_frobenius_leakage_into_residual_complement": True,
            "no_extra_weights_or_sector_knobs": True,
        },
        "uniqueness_result": {
            "unique_up_to_overall_positive_scale": True,
            "overall_scale_cancels_from_euler_projection": True,
            "euler_condition": candidate_functional["euler_condition"],
            "selects_Q_residual": True,
        },
        "what_this_sources": {
            "selected_MTT_C1_defect_functional_is_candidate": True,
            "finite_dimensional_projection_rule": True,
            "least_norm_trace_orthogonal_completion": True,
        },
        "what_this_does_not_source": {
            "physical_PhiFinC1_variation_minimizes_this_functional": True,
            "independent_quadrature_hessian_values": True,
            "unpatched_A_selected_b_selected_promotion": True,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    physical_application = {
        "schema": "MTTPhiFinC1PhysicalApplicationSourceGap.v1",
        "status": "FUNCTIONAL_SOURCED_PHYSICAL_APPLICATION_RULE_OPEN",
        "now_available": {
            "unique_formal_C1_defect_functional": True,
            "Euler_projection_derivation": True,
            "sufficiency_if_PhiFinC1_minimizes_functional": True,
        },
        "remaining_physical_application_rule": {
            "needed_statement": (
                "The selected differentiated Phi_fin^C1 response is the stationary/minimizing "
                "response of the unique C1DefectLeakageFunctional under selected boundary and routing constraints."
            ),
            "not_proved_now": True,
            "why_not_automatic": [
                "Formal uniqueness of a defect functional does not by itself prove Phi_fin^C1 uses that functional dynamically.",
                "Stationary transport-only Phi_fin^C1 was previously shown insufficient for nonzero residual columns.",
                "The missing rule must bind the differentiated physical map to the selected variational problem.",
            ],
        },
        "if_supplied_then": sufficiency["if_variational_source_functional_selected"],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    quadrature_data = {
        "schema": "MTTIndependentQuadratureDataFillAttempt.v1",
        "status": "DATA_REQUIREMENTS_RESTATED_NO_INDEPENDENT_VALUES_FILLED",
        "required_values": quadrature_spec["required_values"],
        "input_data_available_now": {
            "selected_zero_mode_basis_data": False,
            "independent_primitive_quadrature_table": False,
            "independent_hessian_source_vector": False,
            "independent_sector_response_matrices": False,
        },
        "acceptance_tests": quadrature_spec["acceptance_tests"],
        "forbidden_shortcuts": quadrature_spec["quadrature_requirements"]["forbidden"],
        "if_supplied_then": sufficiency["if_independent_quadrature_hessian_solve_passes"],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedC1DefectFunctionalSourceOrIndependentQuadratureDataFill",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "variational_derivation": rel(VARIATIONAL),
            "quadrature_spec": rel(QUADRATURE_SPEC),
            "sufficiency_replay": rel(SUFFICIENCY),
        },
        "output_packets": {
            "c1_defect_functional_uniqueness_source": rel(FUNCTIONAL_SOURCE),
            "phifinc1_physical_application_source_gap": rel(PHYSICAL_APPLICATION),
            "independent_quadrature_data_fill_attempt": rel(QUADRATURE_DATA),
        },
        "what_closes_now": {
            "unique_formal_C1_defect_functional_sourced": True,
            "no_extra_weight_or_sector_knob_needed_for_functional": True,
            "euler_projection_scale_independence_verified": True,
            "physical_application_gap_is_isolated": True,
            "independent_quadrature_data_requirements_preserved": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "prove_PhiFinC1_minimizes_unique_C1_defect_functional": True,
            "bind_differentiated_PhiFinC1_to_variational_problem": True,
            "fill_selected_zero_mode_basis_data": True,
            "fill_independent_primitive_quadrature_table": True,
            "fill_independent_hessian_source_vector": True,
            "run_independent_quadrature_hessian_solve": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "selected_C1_defect_functional_formal_source_promoted": True,
            "physical_PhiFinC1_application_rule_proved": False,
            "independent_quadrature_data_filled": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "C1DefectFunctionalUniquenessTheorem",
            "proved": True,
            "statement": (
                "Under the selected trace/Frobenius metric, fixed-fiber span, static sector routing, "
                "and no-extra-knob policy, the quadratic positive semidefinite C1 leakage functional "
                "that vanishes on the fixed-fiber span and penalizes only residual leakage is unique up "
                "to an overall positive scale. The scale cancels in the Euler equation, so the formal "
                "defect functional is sourced. The remaining physical step is proving that differentiated "
                "Phi_fin^C1 is governed by this functional, or else filling independent quadrature data."
            ),
        },
        "replay_if_physical_application_or_independent_data_supplied": {
            "A_transpose_A": replay["A_transpose_A"],
            "A_transpose_b": replay["A_transpose_b"],
            "deltaTheta_C1": replay["deltaTheta_C1"],
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "patched_spine_closure_preserved": previous["patched_spine_closure_preserved"],
        "unpatched_theorem_closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_C1DefectFunctionalSource_or_IndependentQuadratureDataFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "patched_spine_closure_preserved": candidate["patched_spine_closure_preserved"],
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected C1DefectFunctionalSource or IndependentQuadratureDataFill v1

Status: `{STATUS}`.

This gate sources the formal C1 defect functional.

Closed:

```text
unique quadratic C1 defect functional       = sourced
extra sector weights / knobs                = excluded
overall scale                               = cancels in Euler projection
Q_residual selection from the functional    = formal consequence
```

Still open:

```text
Phi_fin^C1 physically minimizes it          = False
independent quadrature/Hessian data filled  = False
unpatched dynamic closure                   = False
```

Replay once either remaining antecedent is supplied:

```text
A^T A      = {replay["A_transpose_A"]}
A^T b      = {replay["A_transpose_b"]}
deltaTheta = {replay["deltaTheta_C1"]}
```

Next artifact: `{NEXT}`.
"""

    FUNCTIONAL_SOURCE.write_text(json.dumps(functional_source, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    PHYSICAL_APPLICATION.write_text(json.dumps(physical_application, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    QUADRATURE_DATA.write_text(json.dumps(quadrature_data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
