from __future__ import annotations

import json

from flint import acb, acb_mat, arb

import certify_q79_selected_alignment_single_E32_thimble_nodal_factor as legacy


def certify_node_with_deep_pair_seed(
    system,
    critical: complex,
    *,
    epsilon: float,
    initial_parameter_radius: float,
    initial_root_radius: float,
    iterations: int,
):
    base = 0.25 + 0.25j
    critical_parameter_center = -1j * (critical - base)
    # Some rays have a nonvanishing pair closer than the true vanishing pair at
    # the 1e-5 integration cutoff. Use a deeper point only to identify and seed
    # the unique colliding pair; all final claims come from interval Newton.
    pair_seed_epsilon = min(1.0e-9, epsilon * 1.0e-4)
    seed_parameter = (1.0 - pair_seed_epsilon) * critical_parameter_center
    roots = legacy.roots_at(system, seed_parameter)
    pair = legacy.closest_pair(roots)
    root_center = legacy.midpoint((roots[pair[0]] + roots[pair[1]]) / acb(2))
    parameter_center = acb(
        format(critical_parameter_center.real, ".17g"),
        format(critical_parameter_center.imag, ".17g"),
    )
    point_newton_rows = []
    for iteration in range(8):
        values, jacobian, diagnostics = legacy.node_equations_and_jacobian(
            system, parameter_center, root_center
        )
        correction = jacobian.solve(acb_mat([[values[0]], [values[1]]]))
        parameter_center -= correction[0, 0]
        root_center -= correction[1, 0]
        point_newton_rows.append(
            {
                "iteration": iteration + 1,
                "parameter_correction_absolute_upper": legacy.validated.upper(
                    abs(correction[0, 0])
                ),
                "root_correction_absolute_upper": legacy.validated.upper(
                    abs(correction[1, 0])
                ),
                **diagnostics,
            }
        )

    parameter_box = acb(
        arb(str(parameter_center.real.mid()), str(initial_parameter_radius)),
        arb(str(parameter_center.imag.mid()), str(initial_parameter_radius)),
    )
    root_box = acb(
        arb(str(root_center.real.mid()), str(initial_root_radius)),
        arb(str(root_center.imag.mid()), str(initial_root_radius)),
    )
    rows = []
    for iteration in range(iterations):
        parameter_midpoint = legacy.midpoint(parameter_box)
        root_midpoint = legacy.midpoint(root_box)
        values_midpoint, _jacobian_midpoint, _ = legacy.node_equations_and_jacobian(
            system, parameter_midpoint, root_midpoint
        )
        _values_box, jacobian_box, diagnostics = legacy.node_equations_and_jacobian(
            system, parameter_box, root_box
        )
        correction = system.verified_solve(
            jacobian_box,
            acb_mat([[values_midpoint[0]], [values_midpoint[1]]]),
        )
        new_parameter = parameter_midpoint - correction[0, 0]
        new_root = root_midpoint - correction[1, 0]
        parameter_interior = parameter_box.contains_interior(new_parameter)
        root_interior = root_box.contains_interior(new_root)
        rows.append(
            {
                "iteration": iteration + 1,
                "parameter_radius_before": legacy.validated.radius_upper(
                    parameter_box
                ),
                "root_radius_before": legacy.validated.radius_upper(root_box),
                "parameter_newton_radius": legacy.validated.radius_upper(
                    new_parameter
                ),
                "root_newton_radius": legacy.validated.radius_upper(new_root),
                "parameter_interior_inclusion": bool(parameter_interior),
                "root_interior_inclusion": bool(root_interior),
                **diagnostics,
            }
        )
        if not parameter_interior or not root_interior:
            raise ArithmeticError(
                "deep-seed interval Newton inclusion failed at iteration "
                f"{iteration + 1}: {json.dumps(rows[-1], sort_keys=True)}"
            )
        parameter_box = legacy.inflated(new_parameter)
        root_box = legacy.inflated(new_root)

    values, jacobian, diagnostics = legacy.node_equations_and_jacobian(
        system, parameter_box, root_box
    )
    if not values[0].contains(0) or not values[1].contains(0):
        raise AssertionError("certified deep-seed node boxes exclude F=F_t=0")
    if diagnostics["jacobian_determinant_absolute_lower"] <= 0:
        raise AssertionError("deep-seed node Jacobian is not separated")
    return parameter_box, root_box, {
        "pair_seed_method": "unique closest pair at a deeper radial seed",
        "pair_seed_epsilon": pair_seed_epsilon,
        "integration_cutoff_epsilon": epsilon,
        "incoming_closest_pair_zero_based": list(pair),
        "point_newton_refinement": point_newton_rows,
        "iterations": rows,
        "final_F_interval": legacy.encoded_acb(values[0]),
        "final_F_t_interval": legacy.encoded_acb(values[1]),
        "final_jacobian_determinant": legacy.encoded_acb(jacobian.det()),
        **diagnostics,
    }


if __name__ == "__main__":
    wrapper_file = __file__
    legacy.certify_node = certify_node_with_deep_pair_seed
    # The legacy packet builder reads its module __file__ when recording source
    # authority. Point it at this wrapper so the emitted hash names the method
    # that was actually executed.
    legacy.__file__ = wrapper_file
    raise SystemExit(legacy.main())
