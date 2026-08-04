#!/usr/bin/env python3
"""Glue the currently closed q79 u1=2 lines by explicit F_101 CRT idempotents."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULUS = 101
PREFIX = ROOT / "certificates" / "Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1.json"
DEFAULT_OUTPUT = ROOT / "certificates" / "Q79_Ronly_U1_002_Partial_CRT_Gluing_v1.json"
ACCEPTED = {"EXACT_R_ONLY_UNIT", "EXACT_FULL_R_Y_D_UNIT"}


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def artifact(path: Path) -> dict[str, object]:
    require(path.is_file(), f"artifact: {path}")
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def trim(poly: list[int]) -> list[int]:
    value = [coefficient % MODULUS for coefficient in poly]
    while len(value) > 1 and value[-1] == 0:
        value.pop()
    return value


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ])


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * coefficient for coefficient in poly])


def multiply(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % MODULUS
    return trim(result)


def evaluate(poly: list[int], value: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % MODULUS
    return result


def divide_by_linear(poly: list[int], root: int) -> list[int]:
    degree = len(poly) - 1
    require(degree >= 1 and poly[-1] == 1, "monic polynomial")
    quotient = [0] * degree
    quotient[-1] = 1
    for index in range(degree - 1, 0, -1):
        quotient[index - 1] = (poly[index] + root * quotient[index]) % MODULUS
    require((poly[0] + root * quotient[0]) % MODULUS == 0, "linear division remainder")
    return trim(quotient)


def reduce_mod(poly: list[int], modulus_poly: list[int]) -> list[int]:
    result = trim(poly)
    degree = len(modulus_poly) - 1
    require(modulus_poly[-1] == 1, "monic modulus")
    while len(result) - 1 >= degree:
        shift = len(result) - len(modulus_poly)
        leading = result[-1]
        for index, coefficient in enumerate(modulus_poly):
            result[index + shift] = (
                result[index + shift] - leading * coefficient
            ) % MODULUS
        result = trim(result)
    return result + [0] * (degree - len(result))


def build_space(rows: list[dict[str, object]], space: int) -> dict[str, object]:
    roots = [int(row["u2"]) for row in rows]
    require(roots == list(range(1, len(roots) + 1)), f"space-{space} contiguous roots")
    require(all(row.get("complete_status") in ACCEPTED for row in rows), f"space-{space} statuses")

    polynomial = [1]
    for root in roots:
        polynomial = multiply(polynomial, [(-root) % MODULUS, 1])
    require(len(polynomial) == len(roots) + 1 and polynomial[-1] == 1, f"space-{space} P")
    field_roots = [value for value in range(MODULUS) if evaluate(polynomial, value) == 0]
    require(field_roots == roots, f"space-{space} exact root set")

    idempotents = []
    sum_idempotents = [0]
    for root in roots:
        quotient = divide_by_linear(polynomial, root)
        denominator = evaluate(quotient, root)
        require(denominator != 0, f"space-{space} square-free denominator")
        inverse = pow(denominator, -1, MODULUS)
        coefficients = scale(quotient, inverse)
        evaluations = [evaluate(coefficients, value) for value in roots]
        require(
            evaluations == [int(value == root) for value in roots],
            f"space-{space} idempotent evaluations at {root}",
        )
        padded = coefficients + [0] * (len(roots) - len(coefficients))
        require(
            reduce_mod(multiply(coefficients, coefficients), polynomial) == padded,
            f"space-{space} idempotence at {root}",
        )
        sum_idempotents = add(sum_idempotents, coefficients)
        idempotents.append({
            "u2": root,
            "P_divided_by_u2_minus_root_coefficients_ascending": quotient,
            "derivative_denominator": denominator,
            "derivative_denominator_inverse": inverse,
            "idempotent_coefficients_ascending": coefficients,
        })
    require(
        sum_idempotents == [1],
        f"space-{space} partition of unity",
    )
    counts = Counter(str(row["complete_status"]) for row in rows)
    return {
        "space_index": space,
        "closed_u2_values": roots,
        "projector_polynomial": {
            "variable": "u2",
            "factorization": [f"u2-{root}" for root in roots],
            "coefficients_ascending_mod_101": polynomial,
            "degree": len(roots),
        },
        "CRT_idempotents": idempotents,
        "component_status_counts": dict(sorted(counts.items())),
        "coordinate_algebra": f"F_101[u2]/(P_{space}) ~= product_{{a=1}}^{len(roots)} F_101",
        "glued_full_ideal_quotient": "ZERO_RING_ON_THIS_FINITE_PROJECTED_SUBSCHEME",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    prefix = json.loads(PREFIX.read_text(encoding="utf-8"))
    require(
        prefix.get("status") == "EXACT_U1_002_CONTIGUOUS_CROSSSPACE_PREFIX_CLOSED",
        "contiguous-prefix source",
    )
    space5 = build_space(prefix["space5_closed_lines"], 5)
    space6 = build_space(prefix["space6_closed_lines"], 6)
    total = len(space5["closed_u2_values"]) + len(space6["closed_u2_values"])
    full_torus_polynomial = [100, *([0] * 99), 1]
    full_torus = (
        len(space5["closed_u2_values"]) == 100
        and len(space6["closed_u2_values"]) == 100
        and space5["projector_polynomial"]["coefficients_ascending_mod_101"]
        == full_torus_polynomial
        and space6["projector_polynomial"]["coefficients_ascending_mod_101"]
        == full_torus_polynomial
    )
    require(full_torus, "complete nonzero-u2 torus")
    checks = {
        "source_prefix_is_exact_and_hash_bound": True,
        "closed_components_are_contiguous_and_distinct": True,
        "projector_polynomials_are_monic_and_have_exactly_the_listed_F101_roots": True,
        "all_Lagrange_denominators_are_units_in_F101": True,
        "idempotent_evaluation_matrices_are_identity": True,
        "every_projector_is_idempotent_modulo_its_space_polynomial": True,
        "the_projectors_sum_to_one": True,
        "componentwise_zero_quotients_glue_to_zero_over_the_finite_base": True,
        "both_projector_polynomials_are_exactly_u2_to_100_minus_1": full_torus,
        "both_nonzero_F101_u2_tori_are_exhausted": full_torus,
        "no_new_line_is_classified_by_the_gluing_step": True,
        "no_continuous_fit_parameter_is_added": True,
    }
    certificate = {
        "schema": "MTTQ79RonlyU1002PartialCRTGlue.v1",
        "date": "2026-07-24",
        "status": "EXACT_FULL_NONZERO_U2_CRT_GLUE_CERTIFIED",
        "coverage_status": "COMPLETE_F101_NONZERO_U2_TORUS_IN_BOTH_SPACES",
        "field": "F_101",
        "selected_u1": 2,
        "selected_u0": 76,
        "source_artifact": artifact(PREFIX),
        "spaces": [space5, space6],
        "accounting": {
            "cross_space_components_glued": total,
            "canonical_fixed_F101_fibers_represented": 100 * total,
            "new_symbolic_lines_classified": 0,
        },
        "checks": checks,
        "theorem": (
            "For each independent q79 core, the explicitly displayed 100 Lagrange "
            "idempotents split F_101[u2]/(u2^100-1) into its 100 nonzero-field "
            "components. Since the full selected ideal quotient is zero on every "
            "component, it is zero over the complete nonzero F_101 u2 torus."
        ),
        "claim_boundary": (
            "This exact CRT theorem glues already-closed components and introduces "
            "no new line classification. It closes the selected u1=2 nonzero-u2 "
            "finite torus only. It does not emit expanded global Nullstellensatz "
            "coefficients, address the other 98 u1 values or mirror zero-zero "
            "charts, lift to characteristic zero, or promote to physical HYM/QG."
        ),
        "new_continuous_fit_parameters": 0,
    }
    require(all(checks.values()), "certificate checks")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
    print(certificate["status"])
    print(
        f"space5={len(space5['closed_u2_values'])}; "
        f"space6={len(space6['closed_u2_values'])}; total={total}"
    )
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
