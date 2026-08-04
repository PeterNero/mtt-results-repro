from __future__ import annotations

import argparse
import json
import math
import tempfile
import types
from pathlib import Path

import numpy as np
import sympy as sp

import compute_q79genus2normalfunction as normal_function_module
from compute_q79genus2normalfunction import Q79DeltaNormalFunction
from q79genus2_period_transport import FORM_NAMES


ROOT = Path(__file__).resolve().parents[1]
MODEL = (
    ROOT
    / "candidate_data"
    / "selected_q79k3perioddomainxihessianexecutionormarkedmodelgerbecertificate"
    / "explicit_splitting_conic_K3_model.packet.json"
)
PRYM = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2lefschetzperiodreduction"
    / "explicit_prym_residues_and_delta_normal_function.packet.json"
)
A121_VECTOR = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "selected_beta_period_vector.floating.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def exact_complex(value: complex) -> sp.Expr:
    return sp.Rational(str(float(value.real))) + sp.I * sp.Rational(
        str(float(value.imag))
    )


def expression_from_terms(table: list[dict], variables: tuple[sp.Symbol, ...]) -> sp.Expr:
    expression = sp.Integer(0)
    for row in table:
        term = sp.Integer(row["coefficient"])
        for variable, exponent in zip(variables, row["powers_xyz"]):
            term *= variable ** int(exponent)
        expression += term
    return sp.expand(expression)


def complex_pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def complex_value(value: dict) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


class PGL3BetaEvaluator:
    def __init__(self) -> None:
        model = load(MODEL)
        prym = load(PRYM)
        x, y, z = sp.symbols("x y z")
        self.xyz = (x, y, z)
        tables = model["coefficient_tables"]
        self.tables = {
            name: tables[name] for name in ["F6", "G3", "Q2", "H4"]
        }
        basis = prym["residue_forms"]["sl3_basis"]
        self.generators = [
            np.asarray(basis[name], dtype=np.complex128) for name in FORM_NAMES
        ]

    @staticmethod
    def base_line(alignment: np.ndarray) -> np.ndarray:
        return np.asarray(alignment, dtype=np.complex128) @ np.asarray(
            [-1j, 1 + 1j, 1 + 0j], dtype=np.complex128
        )

    def transform_fiber_coordinate(
        self,
        alignment: np.ndarray,
        value: complex,
        *,
        source_chart: str,
        target_chart: str,
    ) -> complex:
        if source_chart == target_chart:
            return complex(value)
        line = self.base_line(alignment)
        if source_chart == "z" and target_chart == "y":
            return complex(-(line[0] + line[1] * value) / line[2])
        if source_chart == "y" and target_chart == "z":
            return complex(-(line[0] + line[2] * value) / line[1])
        raise ValueError(
            f"unsupported chart transition {source_chart!r}->{target_chart!r}"
        )

    def transform_base_lift(
        self,
        alignment: np.ndarray,
        lift: np.ndarray,
        *,
        source_chart: str,
        target_chart: str,
    ) -> tuple[np.ndarray, float]:
        lift = np.asarray(lift, dtype=np.complex128)
        if lift.shape != (5,):
            raise ValueError("base lift must contain five reduced periods")
        if source_chart == target_chart:
            return lift.copy(), 0.0
        line = self.base_line(alignment)
        alpha = -line[0] / line[1]
        beta = -line[2] / line[1]
        common = -(line[1] ** 2) / (line[2] ** 2)
        z_from_y = np.zeros((5, 5), dtype=np.complex128)
        for power in range(5):
            for index in range(power + 1):
                z_from_y[power, index] = (
                    common
                    * math.comb(power, index)
                    * alpha ** (power - index)
                    * beta**index
                )
        if source_chart == "z" and target_chart == "y":
            transformed = np.linalg.solve(z_from_y, lift)
            residual = np.max(abs(z_from_y @ transformed - lift))
            return transformed, float(residual)
        if source_chart == "y" and target_chart == "z":
            transformed = z_from_y @ lift
            recovered = np.linalg.solve(z_from_y, transformed)
            return transformed, float(np.max(abs(recovered - lift)))
        raise ValueError(
            f"unsupported chart transition {source_chart!r}->{target_chart!r}"
        )

    def fibration_packet(
        self, alignment: np.ndarray, *, line_chart: str = "z"
    ) -> dict:
        a, b, t = sp.symbols("a b t")
        exact_alignment = sp.Matrix(
            [[exact_complex(value) for value in row] for row in alignment]
        )
        elliptic = sp.Matrix([a, b, 1])
        line = exact_alignment * elliptic

        if line_chart == "z":
            scale = line[2]
            homogeneous_point = (
                scale,
                scale * t,
                -(line[0] + line[1] * t),
            )
            chart_metadata = {
                "name": "z",
                "fixed_coordinate": "x=1",
                "parameter": "t=y/x",
                "eliminated_coordinate": "z",
            }
        elif line_chart == "y":
            scale = line[1]
            homogeneous_point = (
                scale,
                -(line[0] + line[2] * t),
                scale * t,
            )
            chart_metadata = {
                "name": "y",
                "fixed_coordinate": "x=1",
                "parameter": "t=z/x",
                "eliminated_coordinate": "y",
            }
        else:
            raise ValueError(f"unsupported line chart {line_chart!r}")
        if scale == 0:
            raise ValueError(
                f"the selected affine line chart has ell_{line_chart}=0"
            )

        def aligned_polynomial(name: str, degree: int) -> sp.Expr:
            value = sp.Integer(0)
            for row in self.tables[name]:
                x_power, y_power, z_power = row["powers_xyz"]
                if x_power + y_power + z_power != degree:
                    raise AssertionError(f"{name} is not homogeneous")
                value += (
                    sp.Integer(row["coefficient"])
                    * homogeneous_point[0] ** x_power
                    * homogeneous_point[1] ** y_power
                    * homogeneous_point[2] ** z_power
                )
            return sp.expand(value)

        # The homogeneous point is the denominator-free representative of the
        # selected line chart. The hyperelliptic coordinate is U=scale^3*u.
        f_ab = aligned_polynomial("F6", 6)
        g_ab = aligned_polynomial("G3", 3)
        q_ab = aligned_polynomial("Q2", 2)
        h_ab = aligned_polynomial("H4", 4)
        residual = sp.expand(f_ab - g_ab**2 - q_ab * h_ab)
        if residual != 0:
            raise AssertionError("the splitting-conic identity did not survive alignment")
        f_poly = sp.Poly(f_ab, t)
        if f_poly.degree() != 6:
            raise ValueError("the aligned affine fiber is not a sextic in this chart")
        return {
            "schema": "MTTQ79AlignedGenusTwoFibrationDiagnostic.v1",
            "line_chart": {
                **chart_metadata,
                "scale": str(scale),
                "hyperelliptic_rescaling": f"U=ell_{line_chart}^3*u",
                "homogeneous_point": [str(value) for value in homogeneous_point],
            },
            "fiber_chart": {
                "f_coefficients_t_descending": [
                    str(value) for value in f_poly.all_coeffs()
                ]
            },
            "splitting": {
                "g_ab": str(g_ab),
                "q_ab": str(q_ab),
                "h_ab": str(h_ab),
                "identity_residual": "0",
            },
        }

    def residue_rows(
        self,
        alignment: np.ndarray,
        periods: np.ndarray,
        a: complex,
        b: complex,
        *,
        line_chart: str = "z",
    ) -> np.ndarray:
        elliptic = np.asarray([a, b, 1 + 0j], dtype=np.complex128)
        line = alignment @ elliptic
        i0, i1 = periods[0], periods[1]
        rows: list[complex] = []
        for generator in self.generators:
            variation = alignment @ generator @ elliptic
            if line_chart == "z":
                if abs(line[2]) < 1.0e-10:
                    raise ValueError("the moving residue z-chart approaches ell_2=0")
                constant = line[2] * (
                    variation[0] * line[2] - variation[2] * line[0]
                )
                linear = line[2] * (
                    variation[1] * line[2] - variation[2] * line[1]
                )
            elif line_chart == "y":
                if abs(line[1]) < 1.0e-10:
                    raise ValueError("the moving residue y-chart approaches ell_1=0")
                # The minus sign is the orientation change from
                # t=y/x to t=z/x on the same projective line.
                constant = -line[1] * (
                    variation[0] * line[1] - variation[1] * line[0]
                )
                linear = -line[1] * (
                    variation[2] * line[1] - variation[1] * line[2]
                )
            else:
                raise ValueError(f"unsupported line chart {line_chart!r}")
            rows.append(constant * i0 + linear * i1)
        return np.asarray(rows, dtype=np.complex128)

    def base_abel_jacobi_lift(
        self,
        engine: Q79DeltaNormalFunction,
        *,
        rtol: float,
        atol: float,
        winding_reference: complex | None = None,
    ) -> tuple[np.ndarray, dict]:
        a_value = -1j
        b_value = 1 + 1j
        t = engine.t_symbol
        substitutions = {
            engine.a_symbol: -sp.I,
            engine.b_symbol: 1 + sp.I,
        }

        q_expression = sp.sympify(engine.fibration["splitting"]["q_ab"])
        q_coefficients = np.asarray(
            [
                complex(sp.N(value.subs(substitutions), 17))
                for value in sp.Poly(q_expression, t).all_coeffs()
            ],
            dtype=np.complex128,
        )
        q_roots = np.sort_complex(np.roots(q_coefficients))
        if len(q_roots) != 2:
            raise AssertionError("the aligned splitting divisor is not quadratic")

        fiber_coefficients = np.asarray(
            [
                complex(sp.N(sp.sympify(value).subs(substitutions), 17))
                for value in engine.fibration["fiber_chart"][
                    "f_coefficients_t_descending"
                ]
            ],
            dtype=np.complex128,
        )
        branch_points = np.roots(fiber_coefficients)
        branch_order = np.argsort(branch_points.imag)
        if winding_reference is None:
            winding_branch = branch_points[branch_order[-1]]
            selection_route = "maximum imaginary part at the identity carrier"
            reference_distance = 0.0
        else:
            selected_index = int(np.argmin(abs(branch_points - winding_reference)))
            winding_branch = branch_points[selected_index]
            selection_route = "nearest-root continuation from the preceding carrier"
            reference_distance = float(abs(winding_branch - winding_reference))
        branch_separation = min(
            abs(winding_branch - value)
            for value in branch_points
            if value != winding_branch
        )
        winding_clearance = min(
            [
                abs(winding_branch - value)
                for value in np.concatenate([branch_points, q_roots])
                if value != winding_branch
            ]
        )
        winding_radius = min(0.12, 0.2 * winding_clearance)
        if winding_radius <= 1.0e-6 or branch_separation <= 1.0e-6:
            raise ValueError("the selected moving branch winding is not isolated")

        outer = 20 + 7j
        circle_start = winding_branch + winding_radius
        states: list[np.ndarray] = []
        evaluations = 0
        splitting_residual = 0.0
        for root in q_roots:
            g_value = engine.g(a_value, b_value, root)
            splitting_residual = max(
                splitting_residual,
                float(abs(engine.f(a_value, b_value, root) - g_value**2)),
            )
            state = np.concatenate(
                [[g_value], np.zeros(5, dtype=np.complex128)]
            )
            state, count = engine.integrate_line(
                state, root, outer, rtol=rtol, atol=atol
            )
            evaluations += count
            states.append(state)

        direct_same = abs(states[0][0] - states[1][0]) < abs(
            states[0][0] + states[1][0]
        )
        if direct_same:
            state = states[1]
            state, count = engine.integrate_line(
                state, outer, circle_start, rtol=rtol, atol=atol
            )
            evaluations += count
            state, count = engine.integrate_fixed_fiber_segment(
                state,
                lambda parameter: winding_branch
                + winding_radius * np.exp(-2j * np.pi * parameter),
                lambda parameter: -2j
                * np.pi
                * winding_radius
                * np.exp(-2j * np.pi * parameter),
                rtol=rtol,
                atol=atol,
            )
            evaluations += count
            state, count = engine.integrate_line(
                state, circle_start, outer, rtol=rtol, atol=atol
            )
            evaluations += count
            states[1] = state

        outer_sheet_scale = max(abs(states[0][0]), abs(states[1][0]), 1.0)
        outer_sheet_cancellation = abs(states[0][0] + states[1][0]) / outer_sheet_scale
        sheet_gate = max(2.0e-7, 10.0 * rtol)
        if outer_sheet_cancellation >= sheet_gate:
            raise AssertionError(
                "the aligned outer infinity sheets did not cancel: "
                f"direct_same={bool(direct_same)}, "
                f"relative_residual={outer_sheet_cancellation:.6e}"
            )
        lift = -(states[0][1:] + states[1][1:])
        return lift, {
            "construction": (
                "aligned q_A roots on U=g_A, common outer point, and the "
                "continuously selected reversed upper-branch winding"
            ),
            "q_roots": [complex_pair(value) for value in q_roots],
            "maximum_q_root_splitting_residual": format(
                splitting_residual, ".17g"
            ),
            "wound_branch_point": complex_pair(winding_branch),
            "winding_branch_selection_route": selection_route,
            "winding_branch_reference_distance": format(
                reference_distance, ".17g"
            ),
            "winding_branch_separation": format(branch_separation, ".17g"),
            "reversed_branch_winding_applied": bool(direct_same),
            "winding_radius": format(winding_radius, ".17g"),
            "winding_clearance": format(winding_clearance, ".17g"),
            "upper_branch_imaginary_gap": format(
                float(
                    branch_points[branch_order[-1]].imag
                    - branch_points[branch_order[-2]].imag
                ),
                ".17g",
            ),
            "outer_point": complex_pair(outer),
            "outer_sheet_relative_cancellation": format(
                outer_sheet_cancellation, ".17g"
            ),
            "outer_sheet_relative_cancellation_gate": format(
                sheet_gate, ".17g"
            ),
            "function_evaluations": evaluations,
        }

    def evaluate(
        self,
        alignment: np.ndarray,
        *,
        line_chart: str = "z",
        base_lift_source_chart: str | None = None,
        rtol: float,
        atol: float,
        base_rtol: float | None = None,
        base_atol: float | None = None,
        winding_reference: complex | None = None,
        high_precision_condition_threshold: float | None = None,
    ) -> tuple[np.ndarray, dict]:
        alignment = np.asarray(alignment, dtype=np.complex128)
        if alignment.shape != (3, 3):
            raise ValueError("alignment must be 3x3")
        if abs(np.linalg.det(alignment)) < 1.0e-8:
            raise ValueError("alignment is singular")
        source_chart = (
            line_chart
            if base_lift_source_chart is None
            else base_lift_source_chart
        )
        packet = self.fibration_packet(alignment, line_chart=line_chart)
        original_fibration = normal_function_module.FIBRATION
        with tempfile.TemporaryDirectory(prefix="q79-pgl3-") as directory:
            def engine_for(value: dict, name: str) -> Q79DeltaNormalFunction:
                path = Path(directory) / f"aligned_fibration_{name}.json"
                path.write_text(
                    json.dumps(value, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8",
                )
                normal_function_module.FIBRATION = path
                try:
                    return Q79DeltaNormalFunction()
                finally:
                    normal_function_module.FIBRATION = original_fibration

            engine = engine_for(packet, line_chart)
            if high_precision_condition_threshold is not None:
                engine.high_precision_condition_threshold = (
                    high_precision_condition_threshold
                )
            engine.gauss_manin.residue_rows = types.MethodType(
                lambda _self, periods, a_value, b_value: self.residue_rows(
                    alignment,
                    periods,
                    a_value,
                    b_value,
                    line_chart=line_chart,
                ),
                engine.gauss_manin,
            )
            source_engine = engine
            if source_chart != line_chart:
                source_packet = self.fibration_packet(
                    alignment, line_chart=source_chart
                )
                source_engine = engine_for(source_packet, source_chart)
            source_lift, base_diagnostics = self.base_abel_jacobi_lift(
                source_engine,
                rtol=(
                    min(rtol * 0.01, 2.0e-12)
                    if base_rtol is None
                    else base_rtol
                ),
                atol=(
                    min(atol * 0.01, 2.0e-13)
                    if base_atol is None
                    else base_atol
                ),
                winding_reference=winding_reference,
            )
            base_lift, transition_residual = self.transform_base_lift(
                alignment,
                source_lift,
                source_chart=source_chart,
                target_chart=line_chart,
            )
            if source_chart != line_chart:
                source_wound = complex_value(
                    base_diagnostics["wound_branch_point"]
                )
                base_diagnostics.update(
                    {
                        "base_lift_source_chart": source_chart,
                        "execution_line_chart": line_chart,
                        "target_chart_wound_branch_point": complex_pair(
                            self.transform_fiber_coordinate(
                                alignment,
                                source_wound,
                                source_chart=source_chart,
                                target_chart=line_chart,
                            )
                        ),
                        "base_lift_transition_maximum_absolute_residual": format(
                            transition_residual, ".17g"
                        ),
                    }
                )
            _endpoint, relative_periods, evaluations = engine.execute_path(
                base_lift,
                lambda parameter: engine.root_transport.base + 1j * parameter,
                lambda _parameter: 1j,
                rtol=rtol,
                atol=atol,
            )
        return relative_periods, {
            "alignment_determinant": complex_pair(np.linalg.det(alignment)),
            "base_abel_jacobi_lift": [
                complex_pair(value) for value in base_lift
            ],
            "base_lift_diagnostics": base_diagnostics,
            "function_evaluations": evaluations,
            "maximum_raw_reduction_condition_number": format(
                engine.maximum_reduction_condition_number, ".17g"
            ),
            "maximum_equilibrated_reduction_condition_number": format(
                engine.maximum_equilibrated_condition_number, ".17g"
            ),
            "high_precision_reduction_count": engine.high_precision_reduction_count,
            "high_precision_condition_threshold": format(
                engine.high_precision_condition_threshold, ".17g"
            ),
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--rtol", type=float, default=2.0e-9)
    parser.add_argument("--atol", type=float, default=2.0e-11)
    parser.add_argument("--high-precision-condition-threshold", type=float)
    arguments = parser.parse_args()

    evaluator = PGL3BetaEvaluator()
    alignment = np.eye(3, dtype=np.complex128)
    values, diagnostics = evaluator.evaluate(
        alignment,
        rtol=arguments.rtol,
        atol=arguments.atol,
        high_precision_condition_threshold=(
            arguments.high_precision_condition_threshold
        ),
    )
    expected_packet = load(A121_VECTOR)
    expected = np.asarray(
        [complex_value(value) for value in expected_packet["production_values"]],
        dtype=np.complex128,
    )
    maximum_difference = float(np.max(abs(values - expected)))
    result = {
        "schema": "MTTQ79PGL3BetaZeroExploration.v1",
        "status": "IDENTITY_ALIGNMENT_GENERALIZED_EVALUATOR_CROSSCHECK",
        "form_order": FORM_NAMES,
        "alignment": [
            [complex_pair(value) for value in row] for row in alignment
        ],
        "beta_vector": [complex_pair(value) for value in values],
        "A121_identity_vector_maximum_absolute_difference": format(
            maximum_difference, ".17g"
        ),
        "diagnostics": diagnostics,
        "strict_scope": {
            "general_alignment_formula_implemented": True,
            "identity_crosscheck_only": True,
            "PGL3_zero_found": False,
            "interval_certified": False,
        },
    }
    if maximum_difference >= 2.0e-7:
        raise AssertionError("generalized identity evaluator disagrees with A121")
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
