from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
TEXPAPERS = Path(os.environ.get("MTT_TEXPAPERS_ROOT", ROOT.parent))
REPOSITORIES = {
    "20 Mathematical Language Discovery Program": ROOT,
    "mtt-sm-parity-closure": Path(
        os.environ.get(
            "MTT_SM_CLOSURE_ROOT",
            TEXPAPERS / "mtt-sm-parity-closure",
        )
    ),
    "mtt-protospinor-gr-response-proof": Path(
        os.environ.get(
            "MTT_PROTOSPINOR_GR_ROOT",
            TEXPAPERS / "mtt-protospinor-gr-response-proof",
        )
    ),
    "mtt-qm-source-proof": Path(
        os.environ.get(
            "MTT_QM_SOURCE_ROOT",
            TEXPAPERS / "mtt-qm-source-proof",
        )
    ),
}
PACKET = ROOT / "q79_hodge_action_axiom_selection_audit.packet.json"
NOTE = ROOT / "Q79_HODGE_ACTION_AXIOM_SELECTION_AND_SCALE_RIGIDITY_v1.md"


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix(
    values: list[list[object]],
    extra_locals: dict[str, object] | None = None,
) -> sp.Matrix:
    local_symbols: dict[str, object] = {"I": sp.I}
    if extra_locals:
        local_symbols.update(extra_locals)
    return sp.Matrix(
        [
            [sp.sympify(value, locals=local_symbols) for value in row]
            for row in values
        ]
    )


def is_zero(value: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in value)


def block_diag_twice(value: sp.MatrixBase) -> sp.Matrix:
    zero = sp.zeros(value.rows)
    return sp.Matrix.vstack(
        sp.Matrix.hstack(value, zero),
        sp.Matrix.hstack(zero, value),
    )


def verify_inputs(packet: dict) -> dict[str, Path]:
    resolved: dict[str, Path] = {}
    for label, record in packet["inputs"].items():
        repository = record["repository"]
        require(repository in REPOSITORIES, f"unknown repository: {repository}")
        path = REPOSITORIES[repository] / Path(record["relative_path"])
        require(path.is_file(), f"missing input: {label}")
        require(sha256(path) == record["sha256"], f"stale input hash: {label}")
        resolved[label] = path
    return resolved


def main() -> None:
    packet = load(PACKET)
    require(
        packet["schema"] == "MTTQ79HodgeActionAxiomSelectionAudit.v1",
        "schema",
    )
    require(
        packet["status"].startswith(
            "HODGE_CLOSURE_REPAIR_SHAPE_REDUCED_TO_ONE_POSITIVE_RAY"
        ),
        "status",
    )
    require(NOTE.is_file(), "theorem note")
    paths = verify_inputs(packet)

    prior_hodge = load(paths["prior_minimal_Hodge_action"])
    physical_seed = load(paths["physical_gauge_pair_deformation_seed"])
    upstairs_automorphism = load(paths["upstairs_automorphism_transfer"])
    shared_circle = load(paths["shared_circle_gauge_stack"])
    action_independence = load(
        paths["closure_cost_physical_action_independence"]
    )
    fixed_point_gradient = load(
        paths["fixed_point_gradient_to_Hessian_bridge"]
    )
    action_unit = load(paths["physical_action_unit"])
    nonlinear_nogo = load(paths["quadratic_nonlinear_action_nogo"])
    finite_bv_hodge = load(paths["finite_BV_Hodge_shell"])
    mixed_order_nogo = load(paths["mixed_order_BV_Hodge_no_go"])

    require(
        prior_hodge["theorem"]["tier"].endswith(
            "PHYSICAL_Q79_ACTION_NOT_SELECTED"
        ),
        "prior theorem boundary",
    )
    require(
        physical_seed["status"].startswith(
            "Q79_TRACEFREE_HETEROTIC_DEFORMATION_COMPLEX"
        ),
        "physical seed tier",
    )
    require(
        upstairs_automorphism["physical_readiness"]["gates"][
            "physical_upstairs_action"
        ]["closed"]
        is False,
        "physical upper action boundary",
    )
    require(
        shared_circle["theorem"]["tier"]
        == "CLOSED_EXACT_CIRCLE_MAPPING_STACK_AND_LINEARIZED_HODGE_THEOREM",
        "shared circle source",
    )
    require(
        action_independence["theorem"]["proved"] is True,
        "action independence source",
    )
    require(
        fixed_point_gradient["status"]
        == "CLOSURE_HESSIAN_GENERATES_UNIQUE_SELECTED_TIME_DAMPED_OVERLAP_KERNEL",
        "fixed-point gradient source",
    )
    require(
        fixed_point_gradient["theorem"][
            "proved_at_fixed_point_gradient_flow_tier"
        ]
        is True,
        "fixed-point gradient theorem",
    )
    require(
        action_unit["theorem_result"]["physical_numeric_alpha_selected"]
        is False,
        "physical scale source",
    )
    require(
        nonlinear_nogo["claim_tiers"][
            "quadratic_TT_data_select_unique_nonlinear_action"
        ]
        == "CLOSED_NO_GO",
        "nonlinear no-go source",
    )
    require(
        "uniform interacting regulator removal and fixed-coupling Cstar completion"
        in finite_bv_hodge["claim_boundary"]["open"],
        "finite BV boundary",
    )
    require(
        mixed_order_nogo["naive_adjoint_Hodge_no_go"]["checks"][
            "naive_adjoint_Hodge_scales_quartically_not_quadratically"
        ]
        is True,
        "mixed-order no-go source",
    )

    witness = packet["finite_Hodge_witness"]
    differential = matrix(witness["D"])
    adjoint = matrix(witness["D_adjoint"])
    exact_projector = matrix(witness["P_exact"])
    coexact_projector = matrix(witness["P_coexact"])
    harmonic_projector = matrix(witness["P_harmonic"])
    hodge_laplacian = matrix(witness["Delta_D"])
    adjoint_reversal = matrix(witness["adjoint_reversal"])
    identity3 = sp.eye(3)

    require(differential**2 == sp.zeros(3), "D^2")
    require(adjoint == differential.T, "D adjoint")
    require(adjoint**2 == sp.zeros(3), "(D*)^2")
    require(exact_projector == adjoint * differential, "exact projector")
    require(coexact_projector == differential * adjoint, "coexact projector")
    require(
        harmonic_projector
        == identity3 - exact_projector - coexact_projector,
        "harmonic projector",
    )
    require(
        hodge_laplacian == exact_projector + coexact_projector,
        "Hodge Laplacian",
    )
    require(exact_projector**2 == exact_projector, "exact idempotent")
    require(coexact_projector**2 == coexact_projector, "coexact idempotent")
    require(harmonic_projector**2 == harmonic_projector, "harmonic idempotent")
    require(is_zero(exact_projector * coexact_projector), "exact/coexact")
    require(is_zero(exact_projector * harmonic_projector), "exact/harmonic")
    require(is_zero(coexact_projector * harmonic_projector), "coexact/harmonic")

    x, y, z = sp.symbols("x y z", real=True)
    general_hessian = (
        x * exact_projector
        + y * coexact_projector
        + z * harmonic_projector
    )
    harmonic_equations = list(general_hessian * harmonic_projector)
    reversal_equations = list(
        adjoint_reversal.T
        * general_hessian
        * adjoint_reversal
        - general_hessian
    )
    require(
        sp.solve(harmonic_equations, [z], dict=True) == [{z: 0}],
        "harmonic weight",
    )
    require(
        adjoint_reversal * differential * adjoint_reversal == adjoint,
        "adjoint reversal",
    )
    require(
        sp.solve(
            harmonic_equations + reversal_equations,
            [x, z],
            dict=True,
        )
        == [{x: y, z: 0}],
        "positive ray equations",
    )
    require(
        packet["Hodge_sector_classification"]["positive_ray"]
        == "(x,y,z)=(kappa,kappa,0), kappa>0",
        "serialized positive ray",
    )

    b1 = differential + adjoint
    b2 = sp.I * (differential - adjoint)
    p, q = sp.symbols("p q", real=True)
    b_pq = p * b1 + q * b2
    require(b1.H == b1, "B1 self-adjoint")
    require(b2.H == b2, "B2 self-adjoint")
    require(b1**2 == hodge_laplacian, "B1 square")
    require(b2**2 == hodge_laplacian, "B2 square")
    require(is_zero(b1 * b2 + b2 * b1), "B1/B2 anticommutator")
    require(
        sp.simplify(b_pq**2)
        == (p**2 + q**2) * hodge_laplacian,
        "general closure-charge square",
    )
    closure_charge = packet["closure_supercharge_square_theorem"]
    require(matrix(closure_charge["B1"]) == b1, "serialized B1")
    require(matrix(closure_charge["B2"]) == b2, "serialized B2")
    require(
        closure_charge["tier"]
        == "CLOSED_EXACT_UNIVERSAL_SINGLE_SHARED_COEFFICIENT_"
        "CLOSURE_CHARGE_CLASS",
        "closure-charge tier",
    )

    state_symbols = sp.symbols("state_0 state_1 state_2", real=True)
    state = sp.Matrix(state_symbols)
    nonlinear_plus = sp.Matrix([state_symbols[0] ** 2, 0, 0])
    nonlinear_minus = sp.Matrix([0, state_symbols[1] ** 2, 0])
    defect_plus = differential * state + nonlinear_plus
    defect_minus = adjoint * state + nonlinear_minus
    defect_map = sp.Matrix.vstack(defect_plus, defect_minus)
    origin_substitution = {symbol: 0 for symbol in state_symbols}
    defect_jacobian = defect_map.jacobian(state).subs(origin_substitution)
    defect_cost = sp.expand(
        (defect_plus.dot(defect_plus) + defect_minus.dot(defect_minus)) / 2
    )
    defect_hessian = sp.hessian(
        defect_cost,
        state_symbols,
    ).subs(origin_substitution)
    repair_field = -sp.Matrix(
        [sp.diff(defect_cost, symbol) for symbol in state_symbols]
    )
    repair_jacobian = repair_field.jacobian(state).subs(origin_substitution)
    require(
        defect_map.subs(origin_substitution) == sp.zeros(6, 1),
        "nonlinear defect fixed point",
    )
    require(
        defect_jacobian == sp.Matrix.vstack(differential, adjoint),
        "nonlinear defect Jacobian",
    )
    require(
        defect_hessian == defect_jacobian.T * defect_jacobian,
        "zero-defect Gram Hessian",
    )
    require(defect_hessian == hodge_laplacian, "defect Hodge Hessian")
    require(
        repair_jacobian == -hodge_laplacian,
        "defect repair linearization",
    )
    defect_theorem = packet["nonlinear_closure_defect_linearization_theorem"]
    defect_witness = defect_theorem["finite_nonlinear_witness"]
    state_locals = {
        str(symbol): symbol
        for symbol in state_symbols
    }
    require(
        matrix(defect_witness["Phi_plus"], state_locals) == defect_plus,
        "serialized positive defect",
    )
    require(
        matrix(defect_witness["Phi_minus"], state_locals) == defect_minus,
        "serialized negative defect",
    )
    require(
        matrix(defect_witness["Phi_Jacobian_at_origin"])
        == defect_jacobian,
        "serialized defect Jacobian",
    )
    require(
        matrix(defect_witness["cost_Hessian_at_origin"]) == defect_hessian,
        "serialized defect Hessian",
    )
    require(
        matrix(defect_witness["repair_Jacobian_at_origin"])
        == repair_jacobian,
        "serialized repair Jacobian",
    )
    require(
        defect_theorem["tier"]
        == "CLOSED_EXACT_UNIVERSAL_ZERO_DEFECT_GAUSS_NEWTON_"
        "LINEARIZATION_PHYSICAL_Q79_DEFECT_MAP_OPEN",
        "defect theorem tier",
    )

    circle = packet["shared_circle_insufficiency_theorem"]
    j_circle = matrix(circle["J"])
    differential6 = matrix(circle["D_realified"])
    exact6 = matrix(circle["P_exact_realified"])
    coexact6 = matrix(circle["P_coexact_realified"])
    harmonic6 = matrix(circle["P_harmonic_realified"])
    symmetric_hessian6 = matrix(circle["symmetric_Hessian"])
    asymmetric_hessian6 = matrix(circle["asymmetric_Hessian"])
    reversal6 = block_diag_twice(adjoint_reversal)
    identity6 = sp.eye(6)

    require(differential6 == block_diag_twice(differential), "realified D")
    require(exact6 == block_diag_twice(exact_projector), "realified exact")
    require(coexact6 == block_diag_twice(coexact_projector), "realified coexact")
    require(
        harmonic6 == block_diag_twice(harmonic_projector),
        "realified harmonic",
    )
    require(j_circle.T * j_circle == identity6, "circle orthogonal")
    require(j_circle**2 == -identity6, "circle square")
    require(j_circle**4 == identity6, "circle return")
    require(
        is_zero(j_circle * differential6 - differential6 * j_circle),
        "circle/D compatibility",
    )
    require(
        symmetric_hessian6 == exact6 + coexact6,
        "symmetric Hessian",
    )
    require(
        asymmetric_hessian6 == 2 * exact6 + coexact6,
        "asymmetric Hessian",
    )
    require(
        is_zero(
            j_circle * asymmetric_hessian6
            - asymmetric_hessian6 * j_circle
        ),
        "circle/asymmetric Hessian compatibility",
    )
    require(
        is_zero(asymmetric_hessian6 * harmonic6),
        "asymmetric harmonic kernel",
    )
    require(
        asymmetric_hessian6.rank() == symmetric_hessian6.rank(),
        "same kernel dimension",
    )
    require(
        not is_zero(
            reversal6.T
            * asymmetric_hessian6
            * reversal6
            - asymmetric_hessian6
        ),
        "asymmetric Hessian distinction",
    )
    require(
        circle["tier"] == "CLOSED_EXACT_FINITE_COUNTEREXAMPLE",
        "circle no-go tier",
    )

    kappa, scalar, lam = sp.symbols(
        "kappa scalar lambda",
        real=True,
    )
    nonlinear_family = (
        kappa * scalar**2 / 2
        + lam * scalar**4 / 4
    )
    derivatives = {
        order: sp.simplify(
            sp.diff(nonlinear_family, scalar, order).subs(scalar, 0)
        )
        for order in range(5)
    }
    require(derivatives[0] == 0, "nonlinear value")
    require(derivatives[1] == 0, "nonlinear gradient")
    require(derivatives[2] == kappa, "nonlinear Hessian")
    require(derivatives[4] == 6 * lam, "nonlinear fourth derivative")
    serialized_derivatives = packet["nonlinear_nonuniqueness_theorem"][
        "derivatives_at_origin"
    ]
    require(serialized_derivatives["2"] == "kappa", "serialized Hessian")
    require(serialized_derivatives["4"] == "6*lambda", "serialized quartic")

    source_audit = packet["q79_source_audit"]
    primitive_rows = physical_seed["minimal_source_reduction_theorem"][
        "primitive_geometric_rows"
    ]
    require(len(primitive_rows) == 4, "physical source row count")
    require(not any(primitive_rows.values()), "physical source rows open")
    require(
        source_audit["accepted_physical_source_rows"] == 0
        and source_audit["required_physical_source_rows"] == 4,
        "serialized source rows",
    )
    require(
        source_audit["single_shared_coefficient_closure_charge_selected"]
        is False,
        "closure-charge source boundary",
    )
    require(
        source_audit["physical_repair_linearization_to_minus_kappa_Delta_Q"]
        is False,
        "repair linearization boundary",
    )
    require(
        source_audit["physical_nonlinear_closure_defect_map_emitted"] is False,
        "physical defect map boundary",
    )
    require(
        source_audit["physical_defect_Jacobian_equals_sqrt_kappa_B_Q"]
        is False,
        "physical defect Jacobian boundary",
    )
    require(
        source_audit["closure_cost_identified_with_physical_action"] is False,
        "physical action boundary",
    )
    require(
        source_audit["physical_action_scale_selected"] is False,
        "physical scale boundary",
    )
    require(
        source_audit["nonlinear_action_selected"] is False,
        "nonlinear action boundary",
    )

    parameters = packet["parameter_ledger"]
    require(parameters["sector_weights_before_structure"] == 3, "three weights")
    require(
        parameters["weights_after_harmonic_preservation"] == 2,
        "two weights",
    )
    require(
        parameters["positive_scales_after_closure_charge_factorization"] == 1,
        "one scale",
    )
    require(
        parameters["remaining_dimensionless_Hodge_shape_ratios"] == 0,
        "zero shape ratios",
    )
    require(
        parameters["physical_absolute_scale_selected"] is False,
        "absolute scale open",
    )
    require(parameters["new_observed_inputs"] == 0, "no observed inputs")
    require(parameters["new_fitted_parameters"] == 0, "no fitted parameters")

    require(
        packet["next_required_object"]["name"]
        == "q79SelectedClosureDefectJacobianToHodgeOperator.v1",
        "next object",
    )
    for blocker in ("B.HS.01", "B.GEO.01", "B.OP.01"):
        require(
            packet["blocker_assessment"][blocker].startswith("OPEN:"),
            f"{blocker} boundary",
        )
    require(
        packet["blocker_assessment"]["B.ACTION.01"].startswith(
            "OPEN BUT NARROWED:"
        ),
        "B.ACTION.01 boundary",
    )
    require(all(packet["checks"].values()), "serialized checks")
    require(
        not any(
            value
            for key, value in packet["guardrails"].items()
            if key.startswith("claims_")
        ),
        "claim guardrails",
    )
    require(
        packet["guardrails"]["uses_observed_physics_values"] is False,
        "observed-value guardrail",
    )
    require(
        packet["guardrails"]["adds_fitted_parameter"] is False,
        "fit guardrail",
    )

    print("Q79_HODGE_ACTION_AXIOM_SELECTION_AUDIT_VERIFY_PASS")
    print("shared circle no-go and closure-charge square theorem verified")
    print("one shape ray remains; physical q79 source, scale and action stay open")


if __name__ == "__main__":
    main()
