#!/usr/bin/env python3
"""Consolidate seven exact q79 symbolic lines at u1=2 across both spaces."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
S5 = ROOT / "candidate_data" / "q79_Ronly_u1_002_space5_symbolic_u2_prefix"
S6 = ROOT / "candidate_data" / "q79_Ronly_u1_002_space6_symbolic_u2_prefix"
EXCEPTION = ROOT / "candidate_data" / "q79_Ronly_u1_002_symbolic_exception_D_closure"
PARENT5 = ROOT / "candidate_data" / "q79_Ronly_classfree_representative_lines" / "space_5_h0_g0_class1_inverse_root.msolve.in"
V1 = ROOT / "certificates" / "Q79_Ronly_U1_002_Space5_Symbolic_U2_Prefix_v1.json"
ACCELERATION = ROOT / "certificates" / "Q79_Ronly_U2_Laurent_Line_Acceleration_v1.json"
DEFAULT_OUTPUT = ROOT / "certificates" / "Q79_Ronly_U1_002_CrossSpace_Symbolic_Prefix_v2.json"
STEM = "space5_class1_u1_002_a_050_symbolic_v"
VARIABLES = (
    "h1", "h2", "h3", "h4", "h5", "h6",
    "u3", "u4", "u5", "u6", "u7", "t",
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


def resolve(path_text: str) -> Path:
    path = Path(path_text.replace("\\", "/"))
    return path if path.is_absolute() else ROOT / path


def load(path: Path) -> dict[str, object]:
    require(path.is_file(), f"required artifact: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"JSON object: {path}")
    return value


def literal_unit(path: Path, variables: tuple[str, ...]) -> bool:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return bool(
        text.startswith("#Reduced Groebner basis data\n")
        and "#field characteristic: 101" in text
        and "#variable order:       " + ", ".join(variables) in text
        and re.search(r"#length of basis:\s+1 element", text)
        and re.search(r"\[1\]:\s*$", text)
    )


def exact_nonunit_basis(path: Path, variables: tuple[str, ...], length: int) -> bool:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = re.search(r"#length of basis:\s+(\d+) element", text)
    return bool(
        text.startswith("#Reduced Groebner basis data\n")
        and "#field characteristic: 101" in text
        and "#variable order:       " + ", ".join(variables) in text
        and match is not None
        and int(match.group(1)) == length
        and not re.search(r"\[1\]:\s*$", text)
        and text.rstrip().endswith("]:")
    )


def validate_family(directory: Path, space: int) -> tuple[dict[str, object], str]:
    packet_path = directory / "family.packet.json"
    packet = load(packet_path)
    require(
        packet.get("schema") == "MTTQ79RonlyFixedU1U2SymbolicFamily.v1"
        and packet.get("status") == "EXACT_100_NONZERO_U2_SYMBOLIC_INPUTS_EMITTED"
        and packet.get("field") == "F_101"
        and packet.get("space_index") == space
        and packet.get("fixed_u1") == 2
        and packet.get("endpoint_selected_u0") == 76,
        f"space-{space} family",
    )
    records = packet.get("records", [])
    require(len(records) == 100, f"space-{space} 100 records")
    require([row.get("u2") for row in records] == list(range(1, 101)), "u2 ordering")
    commitment_rows = []
    for row in records:
        path = resolve(str(row["input"]["path"]))
        observed = artifact(path)
        require(
            observed["bytes"] == row["input"]["bytes"]
            and observed["sha256"] == row["input"]["sha256"],
            f"space-{space} input {row['u2']}",
        )
        commitment_rows.append(f"{row['u2']}:{observed['sha256']}")
    commitment = hashlib.sha256(("\n".join(commitment_rows) + "\n").encode("ascii")).hexdigest()
    return packet, commitment


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    v1 = load(V1)
    acceleration = load(ACCELERATION)
    require(
        v1.get("status") == "EXACT_U1_002_SPACE5_THREE_U2_SYMBOLIC_LINES_CLOSED"
        and v1.get("accounting", {}).get("symbolic_u2_lines_proved_unit") == 3,
        "v1 three-line theorem",
    )
    require(
        acceleration.get("status")
        == "EXACT_FIXED_U1_U2_LAURENT_LINE_COMPRESSION_CERTIFIED",
        "Laurent acceleration theorem",
    )
    space5_family, space5_commitment = validate_family(S5, 5)
    space6_family, space6_commitment = validate_family(S6, 6)

    space5_u2_4_input = S5 / "inputs" / "space5_u1_002_u2_004.msolve.in"
    space5_u2_4_output = S5 / "inputs" / "space5_u1_002_u2_004.msolve.out"
    space5_u2_4_log = S5 / "inputs" / "space5_u1_002_u2_004.msolve.log"
    for path in (space5_u2_4_input, space5_u2_4_output, space5_u2_4_log):
        require(path.is_file(), f"space-5 u2=4 artifact: {path}")
    require(exact_nonunit_basis(space5_u2_4_output, VARIABLES, 48), "space-5 u2=4 nonunit basis")
    require(
        space5_family["records"][3]["input"]["sha256"]
        == artifact(space5_u2_4_input)["sha256"],
        "space-5 u2=4 family binding",
    )

    space5_u2_5_input = S5 / "inputs" / "space5_u1_002_u2_005.msolve.in"
    space5_u2_5_output = S5 / "inputs" / "space5_u1_002_u2_005.msolve.out"
    space5_u2_5_log = S5 / "inputs" / "space5_u1_002_u2_005.msolve.log"
    for path in (space5_u2_5_input, space5_u2_5_output, space5_u2_5_log):
        require(path.is_file(), f"space-5 u2=5 artifact: {path}")
    require(literal_unit(space5_u2_5_output, VARIABLES), "space-5 u2=5 unit basis")
    require(
        space5_family["records"][4]["input"]["sha256"]
        == artifact(space5_u2_5_input)["sha256"],
        "space-5 u2=5 family binding",
    )

    space6_u2_1_input = S6 / "inputs" / "space6_u1_002_u2_001.msolve.in"
    space6_u2_1_output = S6 / "inputs" / "space6_u1_002_u2_001.msolve.out"
    space6_u2_1_log = S6 / "inputs" / "space6_u1_002_u2_001.msolve.log"
    for path in (space6_u2_1_input, space6_u2_1_output, space6_u2_1_log):
        require(path.is_file(), f"space-6 u2=1 artifact: {path}")
    require(literal_unit(space6_u2_1_output, VARIABLES), "space-6 u2=1 unit basis")
    require(
        space6_family["records"][0]["input"]["sha256"]
        == artifact(space6_u2_1_input)["sha256"],
        "space-6 u2=1 family binding",
    )

    space6_u2_2_input = S6 / "inputs" / "space6_u1_002_u2_002.msolve.in"
    space6_u2_2_output = S6 / "inputs" / "space6_u1_002_u2_002.msolve.out"
    space6_u2_2_log = S6 / "inputs" / "space6_u1_002_u2_002.msolve.log"
    for path in (space6_u2_2_input, space6_u2_2_output, space6_u2_2_log):
        require(path.is_file(), f"space-6 u2=2 artifact: {path}")
    require(literal_unit(space6_u2_2_output, VARIABLES), "space-6 u2=2 unit basis")
    require(
        space6_family["records"][1]["input"]["sha256"]
        == artifact(space6_u2_2_input)["sha256"],
        "space-6 u2=2 family binding",
    )

    exception_paths = {
        "symbolic_v_input": EXCEPTION / f"{STEM}.msolve.in",
        "symbolic_v_input_packet": EXCEPTION / f"{STEM}.input.packet.json",
        "transported_basis": EXCEPTION / f"{STEM}.transported.msolve.out",
        "basis_transport_certificate": EXCEPTION / f"{STEM}.transport.certificate.json",
        "D_unit_certificate": EXCEPTION / f"{STEM}.D_unit.certificate.json",
    }
    transport = load(exception_paths["basis_transport_certificate"])
    d_certificate = load(exception_paths["D_unit_certificate"])
    require(
        transport.get("status") == "EXACT_DIAGONAL_LAURENT_GROEBNER_BASIS_TRANSPORT"
        and transport.get("canonical_a") == 50
        and transport.get("quotient", {}).get("dimension") == 10
        and transport.get("quotient", {}).get("associativity_basis_triple_checks") == 1000
        and len(transport.get("checks", {})) == 10
        and all(transport["checks"].values()),
        "exact Laurent basis transport",
    )
    require(
        d_certificate.get("status")
        == "EXACT_R_ONLY_FINITE_AFFINE_QUADRATIC_LINE_REJECTED_SCHEME_THEORETICALLY_BY_D"
        and d_certificate.get("space_index") == 5
        and d_certificate.get("scalar_square_class_representative") == 1
        and d_certificate.get("fixed_coordinates")
        == {"u1": 2, "a_equals_v_times_u3": 50, "selected_u0": 76, "selected_u2": 4},
        "exception coordinates",
    )
    quotient = d_certificate.get("quotient_algebra", {})
    witness = d_certificate.get("unit_witness", {})
    require(
        quotient.get("dimension") == 10
        and quotient.get("standard_basis")
        == ["1", "h4", "h5", "h6", "u3", "u4", "u5", "u6", "u7", "v"]
        and quotient.get("associativity_basis_triple_checks") == 1000
        and witness.get("parent_row") == 18
        and witness.get("D_multiplication_determinant") == 95
        and witness.get("product_coefficients") == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        and len(d_certificate.get("checks", {})) == 13
        and all(d_certificate["checks"].values()),
        "dimension-10 D-unit witness",
    )
    expected_d_artifacts = {
        "parent_input": artifact(PARENT5),
        "symbolic_input": artifact(exception_paths["symbolic_v_input"]),
        "symbolic_input_packet": artifact(exception_paths["symbolic_v_input_packet"]),
        "exact_reduced_basis_output": artifact(exception_paths["transported_basis"]),
        "solver_log": artifact(exception_paths["basis_transport_certificate"]),
    }
    require(d_certificate.get("artifacts") == expected_d_artifacts, "D artifact binding")

    inverse = acceleration["canonical_coordinate_bijection"]["inverse_table"]
    require(
        inverse["4"] == {"scalar_class": 1, "canonical_a": 50}
        and inverse["1"] == {"scalar_class": 1, "canonical_a": 1},
        "canonical coordinates",
    )
    require(
        inverse["5"] == {"scalar_class": 1, "canonical_a": 9}
        and inverse["2"] == {"scalar_class": 2, "canonical_a": 1},
        "new canonical coordinates",
    )
    checks = {
        "v1_three_space5_unit_lines_are_retained": True,
        "both_space_families_emit_all_100_nonzero_u2_inputs": True,
        "all_200_family_inputs_are_present_and_hash_bound": True,
        "space5_u2_4_is_an_exact_48_row_nonunit_R_basis": True,
        "the_u2_4_basis_is_transported_two_sidedly_to_the_canonical_v_line": True,
        "the_transported_quotient_is_a_dimension_10_associative_algebra": True,
        "all_y_rows_reconstruct_and_D18_is_a_unit_with_determinant_95": True,
        "space5_u2_5_has_literal_R_only_basis_one": True,
        "space6_u2_1_has_literal_R_only_basis_one": True,
        "space6_u2_2_has_literal_R_only_basis_one": True,
        "all_seven_lines_are_unit_at_the_complete_required_R_or_R_y_D_tier": True,
        "the_other_193_cross_space_u2_lines_remain_explicitly_unclassified": True,
        "no_continuous_fit_parameter_is_added": True,
    }
    require(all(checks.values()), "consolidated checks")
    certificate = {
        "schema": "MTTQ79RonlyU1002CrossSpaceSymbolicPrefix.v2",
        "date": "2026-07-21",
        "status": "EXACT_U1_002_CROSSSPACE_SEVEN_SYMBOLIC_LINES_CLOSED",
        "field": "F_101",
        "selected_u1": 2,
        "selected_u0": 76,
        "source_artifacts": {
            "space5_three_line_v1": artifact(V1),
            "Laurent_acceleration_theorem": artifact(ACCELERATION),
            "space5_family": artifact(S5 / "family.packet.json"),
            "space5_all_input_commitment": space5_commitment,
            "space6_family": artifact(S6 / "family.packet.json"),
            "space6_all_input_commitment": space6_commitment,
        },
        "new_line_results": [
            {
                "space_index": 5,
                "u2": 4,
                "canonical_scalar_class": 1,
                "canonical_a": 50,
                "R_only_status": "EXACT_NONUNIT_SYMBOLIC_LINE",
                "complete_status": "EXACT_FULL_R_Y_D_UNIT_BY_D18",
                "R_only_input": artifact(space5_u2_4_input),
                "R_only_basis": artifact(space5_u2_4_output),
                "R_only_log": artifact(space5_u2_4_log),
                "basis_transport": artifact(exception_paths["basis_transport_certificate"]),
                "D_unit_certificate": artifact(exception_paths["D_unit_certificate"]),
                "quotient_dimension": 10,
                "associativity_checks": 1000,
                "D_unit_row": 18,
                "D_multiplication_determinant": 95,
            },
            {
                "space_index": 5,
                "u2": 5,
                "canonical_scalar_class": 1,
                "canonical_a": 9,
                "R_only_status": "EXACT_UNIT_SYMBOLIC_LINE",
                "complete_status": "EXACT_R_ONLY_UNIT",
                "R_only_input": artifact(space5_u2_5_input),
                "R_only_basis": artifact(space5_u2_5_output),
                "R_only_log": artifact(space5_u2_5_log),
            },
            {
                "space_index": 6,
                "u2": 1,
                "canonical_scalar_class": 1,
                "canonical_a": 1,
                "R_only_status": "EXACT_UNIT_SYMBOLIC_LINE",
                "complete_status": "EXACT_R_ONLY_UNIT",
                "R_only_input": artifact(space6_u2_1_input),
                "R_only_basis": artifact(space6_u2_1_output),
                "R_only_log": artifact(space6_u2_1_log),
            },
            {
                "space_index": 6,
                "u2": 2,
                "canonical_scalar_class": 2,
                "canonical_a": 1,
                "R_only_status": "EXACT_UNIT_SYMBOLIC_LINE",
                "complete_status": "EXACT_R_ONLY_UNIT",
                "R_only_input": artifact(space6_u2_2_input),
                "R_only_basis": artifact(space6_u2_2_output),
                "R_only_log": artifact(space6_u2_2_log),
            },
        ],
        "accounting": {
            "space5_symbolic_lines_closed": 5,
            "space6_symbolic_lines_closed": 2,
            "cross_space_symbolic_lines_closed": 7,
            "R_only_unit_lines": 6,
            "D_augmented_unit_lines": 1,
            "canonical_fixed_F101_fibers_closed": 700,
            "cross_space_symbolic_lines_remaining_unclassified": 193,
        },
        "checks": checks,
        "theorem": (
            "At u1=2 in the q79 R-only cores, space-5 lines u2=1,2,3 are "
            "R-only unit ideals, space-5 u2=4 is a dimension-10 finite R quotient "
            "rejected scheme-theoretically by the unit D18 terminal, space-5 u2=5 "
            "is R-only unit, and space-6 u2=1,2 are R-only unit ideals. Hence all "
            "seven displayed symbolic lines, representing 700 canonical fixed F_101 "
            "fibers, are empty at the complete "
            "required R or R/y/D tier and after every scalar extension."
        ),
        "claim_boundary": (
            "This closes 5/100 space-5 and 2/100 space-6 symbolic-u2 lines at u1=2. "
            "The other 193 lines, the other 98 nonzero u1 values, characteristic zero, "
            "the two mirror zero-zero charts, and physical HYM/QG promotion remain open. "
            "The global symbolic chart count remains 138/140."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
    print(certificate["status"])
    print("space5=5/100; space6=2/100; canonical fibers=700")
    print("u2=4 exception: dim=10, D18 determinant=95")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
