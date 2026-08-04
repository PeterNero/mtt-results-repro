from __future__ import annotations

import json
import tempfile
import types
from pathlib import Path
from typing import Callable

import numpy as np

import compute_q79genus2normalfunction as normal_function_module
from compute_q79genus2normalfunction import Q79DeltaNormalFunction
from explore_q79_pgl3_beta_zero import (
    PGL3BetaEvaluator,
    complex_pair,
    complex_value,
)


def evaluate_deformed_beta_path(
    evaluator: PGL3BetaEvaluator,
    alignment: np.ndarray,
    *,
    path_offset: Callable[[float], complex],
    path_offset_derivative: Callable[[float], complex],
    path_model: str,
    line_chart: str = "z",
    base_lift_source_chart: str | None = None,
    rtol: float,
    atol: float,
    base_rtol: float | None = None,
    base_atol: float | None = None,
    winding_reference: complex | None = None,
    high_precision_condition_threshold: float | None = None,
) -> tuple[np.ndarray, dict]:
    """Evaluate the frozen beta engine on an endpoint-fixed deformed path."""
    alignment = np.asarray(alignment, dtype=np.complex128)
    if alignment.shape != (3, 3):
        raise ValueError("alignment must be 3x3")
    if abs(np.linalg.det(alignment)) < 1.0e-8:
        raise ValueError("alignment is singular")
    start_offset = complex(path_offset(0.0))
    end_offset = complex(path_offset(1.0))
    if abs(start_offset) > 1.0e-13 or abs(end_offset - 1j) > 1.0e-13:
        raise ValueError("deformed beta path must retain the selected endpoints")

    source_chart = (
        line_chart if base_lift_source_chart is None else base_lift_source_chart
    )
    packet = evaluator.fibration_packet(alignment, line_chart=line_chart)
    original_fibration = normal_function_module.FIBRATION
    with tempfile.TemporaryDirectory(prefix="q79-pgl3-deformed-") as directory:

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
            lambda _self, periods, a_value, b_value: evaluator.residue_rows(
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
            source_packet = evaluator.fibration_packet(
                alignment, line_chart=source_chart
            )
            source_engine = engine_for(source_packet, source_chart)
        source_lift, base_diagnostics = evaluator.base_abel_jacobi_lift(
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
        base_lift, transition_residual = evaluator.transform_base_lift(
            alignment,
            source_lift,
            source_chart=source_chart,
            target_chart=line_chart,
        )
        if source_chart != line_chart:
            source_wound = complex_value(base_diagnostics["wound_branch_point"])
            base_diagnostics.update(
                {
                    "base_lift_source_chart": source_chart,
                    "execution_line_chart": line_chart,
                    "target_chart_wound_branch_point": complex_pair(
                        evaluator.transform_fiber_coordinate(
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
            lambda parameter: engine.root_transport.base
            + path_offset(float(parameter)),
            lambda parameter: path_offset_derivative(float(parameter)),
            rtol=rtol,
            atol=atol,
        )
    return relative_periods, {
        "path_model": path_model,
        "path_start_offset": complex_pair(start_offset),
        "path_end_offset": complex_pair(end_offset),
        "alignment_determinant": complex_pair(np.linalg.det(alignment)),
        "base_abel_jacobi_lift": [complex_pair(value) for value in base_lift],
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
