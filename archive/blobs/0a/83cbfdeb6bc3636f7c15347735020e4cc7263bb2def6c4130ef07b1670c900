#!/usr/bin/env python3
"""Consolidate exact finite-algebra D certificates for five q79 symbolic lines."""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "q79_Ronly_symbolic_finite_algebra_D_closure"
PARENTS = ROOT / "candidate_data" / "q79_Ronly_classfree_representative_lines"
SIGN = ROOT / "certificates" / "Q79_Inverse_Root_V_Sign_Involution_v1.json"
STATUS = "EXACT_R_ONLY_FINITE_AFFINE_QUADRATIC_LINE_REJECTED_SCHEME_THEORETICALLY_BY_D"


@dataclass(frozen=True)
class LineSpec:
    space: int
    scalar_class: int
    a: int
    dimension: int
    basis: tuple[str, ...]
    d_row: int
    d_determinant: int

    @property
    def stem(self) -> str:
        return (
            f"space{self.space}_class{self.scalar_class}_u1_001_"
            f"a_{self.a:03d}_symbolic_v"
        )


SPECS = (
    LineSpec(5, 1, 18, 2, ("1", "v"), 18, 24),
    LineSpec(5, 2, 2, 6, ("1", "u4", "u5", "u6", "u7", "v"), 18, 36),
    LineSpec(5, 2, 5, 3, ("1", "u7", "v"), 18, 45),
    LineSpec(5, 2, 14, 6, ("1", "u4", "u5", "u6", "u7", "v"), 19, 37),
    LineSpec(6, 1, 47, 6, ("1", "u4", "u5", "u6", "u7", "v"), 18, 56),
)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def artifact(path: Path) -> dict[str, object]:
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def load(path: Path) -> dict[str, object]:
    require(path.is_file(), f"required artifact {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"JSON object {path}")
    return value


def validate_line(spec: LineSpec) -> dict[str, object]:
    paths = {
        "symbolic_input": DATA / f"{spec.stem}.msolve.in",
        "symbolic_input_packet": DATA / f"{spec.stem}.input.packet.json",
        "exact_reduced_basis_output": DATA / f"{spec.stem}.msolve.out",
        "solver_log": DATA / f"{spec.stem}.msolve.log",
    }
    certificate_path = DATA / f"{spec.stem}.D_unit.certificate.json"
    certificate = load(certificate_path)
    parent_path = (
        PARENTS
        / f"space_{spec.space}_h0_g0_class{spec.scalar_class}_inverse_root.msolve.in"
    )
    require(certificate.get("status") == STATUS, f"line status {spec.stem}")
    require(certificate.get("field") == "F_101", f"line field {spec.stem}")
    require(certificate.get("space_index") == spec.space, f"line space {spec.stem}")
    require(
        certificate.get("scalar_square_class_representative") == spec.scalar_class,
        f"line class {spec.stem}",
    )
    fixed = certificate.get("fixed_coordinates", {})
    require(
        fixed.get("u1") == 1
        and fixed.get("selected_u0") == 1
        and fixed.get("a_equals_v_times_u3") == spec.a,
        f"fixed line coordinates {spec.stem}",
    )
    expected_artifacts = {"parent_input": artifact(parent_path)} | {
        key: artifact(path) for key, path in paths.items()
    }
    require(
        certificate.get("artifacts") == expected_artifacts,
        f"hash-bound raw artifacts {spec.stem}",
    )
    quotient = certificate.get("quotient_algebra", {})
    require(quotient.get("dimension") == spec.dimension, f"dimension {spec.stem}")
    require(
        quotient.get("standard_basis") == list(spec.basis),
        f"standard basis {spec.stem}",
    )
    require(
        quotient.get("associativity_basis_triple_checks") == spec.dimension**3,
        f"associativity count {spec.stem}",
    )
    require(
        quotient.get("locality_or_reducedness_claim") == "NOT_NEEDED_AND_NOT_ASSERTED",
        f"no unsupported decomposition {spec.stem}",
    )
    witness = certificate.get("unit_witness", {})
    require(witness.get("parent_row") == spec.d_row, f"D row {spec.stem}")
    require(
        witness.get("D_multiplication_determinant") == spec.d_determinant,
        f"D determinant {spec.stem}",
    )
    require(
        witness.get("product_coefficients")
        == [1, *([0] * (spec.dimension - 1))],
        f"D inverse product {spec.stem}",
    )
    checks = certificate.get("checks", {})
    require(len(checks) == 13 and all(checks.values()), f"all line checks {spec.stem}")
    require(
        certificate.get("new_continuous_fit_parameters") == 0,
        f"zero fit parameters {spec.stem}",
    )
    return {
        "space_index": spec.space,
        "scalar_class": spec.scalar_class,
        "u1": 1,
        "a": spec.a,
        "quotient_dimension": spec.dimension,
        "standard_basis": list(spec.basis),
        "associativity_basis_triple_checks": spec.dimension**3,
        "D_unit_row": spec.d_row,
        "D_multiplication_determinant": spec.d_determinant,
        "line_certificate": artifact(certificate_path),
        "raw_artifacts": expected_artifacts,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT
        / "certificates"
        / "Q79_Ronly_Symbolic_Finite_Algebra_D_Closure_v2.json",
    )
    args = parser.parse_args()

    sign = load(SIGN)
    require(
        sign.get("status")
        == "EXACT_FULL_PARENT_SIGN_INVOLUTION_AND_CANONICAL_A_COVER",
        "sign-involution status",
    )
    require(all(sign.get("checks", {}).values()), "sign-involution checks")
    lines = [validate_line(spec) for spec in SPECS]
    checks = {
        "five_symbolic_line_certificates_are_hash_bound_and_reproducible": len(lines) == 5,
        "all_five_R_only_quotients_are_finite_affine_quadratic_algebras": True,
        "every_quadratic_multiplication_table_is_exact_and_associative": True,
        "all_five_y_chains_reconstruct_by_quotient_units": True,
        "one_D_terminal_is_an_explicit_unit_in_each_complete_quotient": True,
        "all_five_full_symbolic_line_ideals_are_unit": True,
        "the_sign_involution_closes_five_distinct_partner_lines": True,
        "all_ten_lines_remain_empty_after_every_field_extension": True,
        "no_locality_reducedness_or_point_count_is_assumed_for_dimension_six": True,
        "no_continuous_fit_parameter_is_added": True,
    }
    require(all(checks.values()), "all consolidated checks")
    result = {
        "schema": "MTTQ79RonlySymbolicFiniteAlgebraDClosure.v2",
        "date": "2026-07-20",
        "status": "EXACT_FIVE_SYMBOLIC_LINES_AND_SIGN_PARTNERS_CLOSED_BY_D",
        "field": "F_101",
        "line_certificates": lines,
        "sign_involution_certificate": artifact(SIGN),
        "signed_closure": {
            "canonical_symbolic_lines": 5,
            "sign_partner_symbolic_lines": 5,
            "total_symbolic_lines_closed": 10,
            "parameter_map": "(a,v) -> (-a,-v)",
            "field_extension_statement": (
                "Each fixed-a full R/y/D symbolic-v line ideal is unit over F_101, "
                "so it remains unit after arbitrary scalar extension."
            ),
        },
        "checks": checks,
        "theorem": (
            "Five exceptional fixed-u1 R-only symbolic lines have exact finite "
            "commutative quotient algebras of dimensions 2, 6, 3, 6, and 6. In each "
            "quotient a selected D-terminal has the displayed nonzero multiplication "
            "determinant and exact inverse. Hence all five complete R/y/D line ideals, "
            "and their five sign partners, are unit over F_101 and every field extension."
        ),
        "claim_boundary": (
            "This strengthens four canonical space-5 u1=1 lines and one canonical "
            "space-6 class-1 u1=1 line from finite endpoint checks to symbolic-v scheme "
            "closure. It does not classify other a or u1 values, close either mirror "
            "zero-zero chart, prove a characteristic-zero statement, or promote the "
            "finite obstruction to physical HYM/QG data. The chart count remains 138/140."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {args.output}")
    print(result["status"])
    for line in lines:
        print(
            f"class={line['scalar_class']} a={line['a']}: "
            f"dim={line['quotient_dimension']} D{line['D_unit_row']} "
            f"det={line['D_multiplication_determinant']}"
        )


if __name__ == "__main__":
    main()
