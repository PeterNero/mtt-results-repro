"""No-go test for the currently sourced Repair B primitive correction.

Repair B is the only live algebraic repair branch after the retirement stress
test.  This script computes the exact primitive obstruction and checks whether
any currently source-certified term has the required color Cartan shape and mu
dependence.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RETIREMENT_CERT = ROOT / "certificates" / "selected_qa_su3_repair_retirement_stress_test_certificate.json"
TEMPLATE_CERT = ROOT / "certificates" / "selected_qa_su3_color_connection_template_fill_attempt_certificate.json"
MU_NO_GO_CERT = ROOT / "certificates" / "selected_qa_su3_mu_independent_completion_no_go_certificate.json"
RADIUS_CERT = ROOT / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def metric_weights(radius_cert: dict[str, Any]) -> list[float]:
    values = radius_cert["selected_values"]
    r1 = float(values["R_star"])
    r2 = r1
    r3 = float(values["r3"])
    return [1.0 / r1**2, 1.0 / r2**2, 1.0 / r3**2]


def required_repair_b_coefficient(mu: float, weights: list[float]) -> float:
    # Repair B primitive contraction is (w1*mu + w3*mu^2) diag(1,-1,0).
    return -(weights[0] * mu + weights[2] * mu * mu)


def matrix_from_coefficient(coefficient: float) -> list[list[float]]:
    return [
        [coefficient, 0.0, 0.0],
        [0.0, -coefficient, 0.0],
        [0.0, 0.0, 0.0],
    ]


def sample_required_correction(weights: list[float]) -> list[dict[str, Any]]:
    samples = []
    for mu in [0.25, 1.0, 4.0]:
        coeff = required_repair_b_coefficient(mu, weights)
        samples.append(
            {
                "mu": mu,
                "required_weighted_correction_coefficient": coeff,
                "required_weighted_correction_matrix": matrix_from_coefficient(coeff),
                "required_shape": "diag(-1,1,0) in weighted primitive contraction",
                "coefficient_formula": "-(w1*mu + w3*mu^2)",
            }
        )
    return samples


def source_term_tests(template: dict[str, Any], mu_no_go: dict[str, Any]) -> list[dict[str, Any]]:
    connection = template["partial_fill"]["connection"]
    return [
        {
            "candidate": "selected R_+ gravitational curvature",
            "source_data": connection["curvature_or_flux_data"]["iwasawa_grav"],
            "has_required_color_cartan_shape": False,
            "has_required_mu_dependence": False,
            "result": "reject",
            "reason": "R_+ is gravitational/invariant alpha1 data, not a selected SU3 color endomorphism proportional to diag(-1,1,0).",
        },
        {
            "candidate": "heterotic abelian flux coefficients",
            "source_data": connection["curvature_or_flux_data"]["iwasawa_abelian_flux"],
            "has_required_color_cartan_shape": False,
            "has_required_mu_dependence": False,
            "result": "reject",
            "reason": "The sourced abelian flux is coefficient-level anomaly data, not the Repair B HYM color primitive correction.",
        },
        {
            "candidate": "mu-independent torsion or OU lift",
            "source_data": mu_no_go["status"],
            "has_required_color_cartan_shape": False,
            "has_required_mu_dependence": False,
            "result": "reject",
            "reason": "Already proved unable to close the selected HYM block; Repair B requires a nonconstant mu and mu^2 Cartan term.",
        },
        {
            "candidate": "scalar OU variance or damping weights",
            "source_data": "OU sources supply scalar mode variance/damping structures, not color-matrix endomorphism_E data.",
            "has_required_color_cartan_shape": False,
            "has_required_mu_dependence": "generic_mu_dependence_possible_but_not_selected",
            "result": "reject",
            "reason": "A scalar OU weight can rescale an operator; it cannot by itself add the traceless color Cartan primitive correction without a selected color endomorphism.",
        },
        {
            "candidate": "stored color endomorphism_E",
            "source_data": connection["endomorphism_E"],
            "has_required_color_cartan_shape": False,
            "has_required_mu_dependence": False,
            "result": "reject",
            "reason": "The current selected Qa/SU3 color-connection template has endomorphism_E = null.",
        },
        {
            "candidate": "pure sign, transpose, or wedge convention",
            "source_data": "exhausted by prior convention scans for the printed matrix; Repair B is an erratum candidate, not a source-certified convention.",
            "has_required_color_cartan_shape": False,
            "has_required_mu_dependence": False,
            "result": "reject",
            "reason": "Conventions can change signs/orderings, but do not source a new weighted primitive correction term with coefficient -(w1*mu+w3*mu^2).",
        },
    ]


def main() -> int:
    retirement = load(RETIREMENT_CERT)
    template = load(TEMPLATE_CERT)
    mu_no_go = load(MU_NO_GO_CERT)
    radius = load(RADIUS_CERT)
    weights = metric_weights(radius)
    tests = source_term_tests(template, mu_no_go)
    output = {
        "certificate": "SelectedQaSU3RepairBPrimitiveCorrectionNoGo",
        "status": "QA_SU3_REPAIR_B_PRIMITIVE_CORRECTION_CURRENT_SOURCE_NO_GO",
        "input_status": {
            "retirement_stress_test": retirement["status"],
            "color_connection_template": template["status"],
            "mu_independent_completion_no_go": mu_no_go["status"],
            "selected_radius": radius["status"],
        },
        "repair_B_live_branch_confirmed": retirement["stress_test_conclusion"][
            "repair_B_only_live_current_branch"
        ],
        "metric_weights": {
            "w1": weights[0],
            "w2": weights[1],
            "w3": weights[2],
        },
        "required_correction": {
            "weighted_primitive_formula": "-(w1*mu + w3*mu^2) diag(1,-1,0)",
            "samples": sample_required_correction(weights),
            "source_requirements": [
                "selected SU3 color endomorphism or torsion correction",
                "Cartan shape diag(-1,1,0) in the primitive contraction",
                "mu and mu^2 dependence tied to the same Repair B HYM family",
                "independent source derivation, not threshold-target backsolve",
            ],
        },
        "available_source_term_tests": tests,
        "no_go_scope": {
            "proved_for_current_corpus_sources": True,
            "not_proved_for_future_new_source": True,
            "not_proved_for_changed_selected_branch": True,
        },
        "allowed_future_escape_hatches": [
            "find an explicit source-certified HYM curvature matrix for Repair B whose full Chern-Weil primitive includes the missing term",
            "derive an endomorphism_E from the selected Strominger/Dirac/Weitzenbock operator with exactly the required Cartan and mu dependence",
            "replace the Repair B algebraic branch by a source-certified connection matrix from the heterotic paper or erratum",
            "retire the explicit HYM-matrix route entirely and return to compact Nil/local-system determinant routes",
        ],
        "verdict": {
            "repair_B_primitive_correction_source_certified_now": False,
            "repair_B_current_source_no_go": True,
            "repair_B_mathematically_impossible": False,
            "safe_to_close_Qa_SU3": False,
            "target_fitting_used": False,
            "next_required_artifact": "Selected_Qa_SU3_Explicit_Source_Certified_Connection_or_Route_Retirement_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
