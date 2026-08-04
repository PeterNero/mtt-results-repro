#!/usr/bin/env python3
"""Certify the first exact symbolic-u2 lines beyond the q79 u1=1 slice."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


PRIME = 101
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "q79_Ronly_u1_002_space5_symbolic_u2_prefix"
FAMILY = DATA / "family.packet.json"
ACCELERATION = ROOT / "certificates" / "Q79_Ronly_U2_Laurent_Line_Acceleration_v1.json"
BUILDER = ROOT / "scripts" / "build_q79_Ronly_fixed_u1_u2_symbolic_family.py"
RUNNER = ROOT / "scripts" / "run_q79_Ronly_fixed_u1_u2_symbolic_cover.py"
DEFAULT_OUTPUT = ROOT / "certificates" / "Q79_Ronly_U1_002_Space5_Symbolic_U2_Prefix_v1.json"
VARIABLES = (
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "u3",
    "u4",
    "u5",
    "u6",
    "u7",
    "t",
)
SELECTED_U2 = (1, 2, 3)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def checksum(path: Path) -> dict[str, object]:
    return {
        "path": relative(path),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def resolve(path_text: str) -> Path:
    path = Path(path_text.replace("\\", "/"))
    return path if path.is_absolute() else ROOT / path


def input_rows(path: Path) -> list[str]:
    lines = path.read_text(encoding="ascii").replace("\r\n", "\n").splitlines()
    require(tuple(lines[0].split(",")) == VARIABLES, f"variable order: {path.name}")
    require(int(lines[1]) == PRIME, f"field: {path.name}")
    rows = "\n".join(lines[2:]).rstrip().removesuffix(",").split(",\n")
    require(len(rows) == 13, f"13 rows: {path.name}")
    require(rows[-1] in {"u3*t + 100", "t*u3 + 100"}, f"Laurent row: {path.name}")
    return rows


def literal_unit_output(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="strict").replace("\r\n", "\n")
    length = re.search(r"#length of basis:\s+(\d+) element", text)
    return bool(
        text.startswith("#Reduced Groebner basis data\n")
        and "#field characteristic: 101" in text
        and "#variable order:       " + ", ".join(VARIABLES) in text
        and length is not None
        and int(length.group(1)) == 1
        and re.search(r"\[1\]:\s*$", text) is not None
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    for path in (FAMILY, ACCELERATION, BUILDER, RUNNER):
        require(path.is_file(), f"required artifact: {path}")
    family = json.loads(FAMILY.read_text(encoding="utf-8"))
    acceleration = json.loads(ACCELERATION.read_text(encoding="utf-8"))
    require(
        family.get("schema") == "MTTQ79RonlyFixedU1U2SymbolicFamily.v1"
        and family.get("status") == "EXACT_100_NONZERO_U2_SYMBOLIC_INPUTS_EMITTED",
        "family packet status",
    )
    require(
        family.get("field") == "F_101"
        and family.get("space_index") == 5
        and family.get("fixed_u1") == 2
        and family.get("endpoint_selected_u0") == 76,
        "selected endpoint",
    )
    require(
        acceleration.get("status")
        == "EXACT_FIXED_U1_U2_LAURENT_LINE_COMPRESSION_CERTIFIED",
        "acceleration theorem",
    )

    records = family.get("records", [])
    require(len(records) == 100, "100 family records")
    require([row.get("u2") for row in records] == list(range(1, PRIME)), "u2 exhaustion")
    input_hash_rows = []
    for row in records:
        path = resolve(str(row["input"]["path"]))
        require(path.is_file(), f"family input: {path}")
        observed = checksum(path)
        require(observed["bytes"] == row["input"]["bytes"], f"input bytes: {path.name}")
        require(observed["sha256"] == row["input"]["sha256"], f"input hash: {path.name}")
        input_rows(path)
        input_hash_rows.append(f"{row['u2']}:{observed['sha256']}")
    family_commitment = hashlib.sha256(("\n".join(input_hash_rows) + "\n").encode("ascii")).hexdigest()

    inverse = acceleration["canonical_coordinate_bijection"]["inverse_table"]
    selected = []
    for u2 in SELECTED_U2:
        stem = f"space5_u1_002_u2_{u2:03d}.msolve"
        input_path = DATA / "inputs" / f"{stem}.in"
        output_path = DATA / "inputs" / f"{stem}.out"
        log_path = DATA / "inputs" / f"{stem}.log"
        require(input_path.is_file() and output_path.is_file() and log_path.is_file(), stem)
        require(literal_unit_output(output_path), f"literal unit output: {stem}")
        coordinate = inverse[str(u2)]
        selected.append(
            {
                "space_index": 5,
                "u1": 2,
                "u2": u2,
                "canonical_scalar_class": coordinate["scalar_class"],
                "canonical_a": coordinate["canonical_a"],
                "input": checksum(input_path),
                "exact_reduced_basis_output": checksum(output_path),
                "solver_log": checksum(log_path),
                "reduced_basis": [1],
                "consequence": (
                    "The saturated R-only ideal is the unit ideal over F_101 and "
                    "after every scalar extension."
                ),
            }
        )

    certificate = {
        "schema": "MTTQ79RonlyU1002Space5SymbolicU2Prefix.v1",
        "date": "2026-07-21",
        "status": "EXACT_U1_002_SPACE5_THREE_U2_SYMBOLIC_LINES_CLOSED",
        "field": "F_101",
        "selected_slice": {"space_index": 5, "u1": 2, "selected_u0": 76},
        "source_artifacts": {
            "parent_family": checksum(FAMILY),
            "Laurent_acceleration_theorem": checksum(ACCELERATION),
            "family_builder": checksum(BUILDER),
            "checkpoint_runner": checksum(RUNNER),
            "all_100_input_hash_commitment": family_commitment,
        },
        "exact_unit_lines": selected,
        "accounting": {
            "symbolic_u2_lines_emitted": 100,
            "symbolic_u2_lines_exactly_classified": 3,
            "symbolic_u2_lines_proved_unit": 3,
            "symbolic_u2_lines_remaining_unclassified": 97,
            "canonical_fixed_F101_fibers_closed": 300,
            "fixed_fibers_per_symbolic_line": 100,
        },
        "solver_provenance": {
            "engine": "msolve 0.10.1",
            "binary_bytes": 70980672,
            "binary_sha256": "a4c2beb9a7d186394af6bb21e235f76e3bfb3d0e6fdf872c27b517b8a6e87e13",
            "mode": "one thread, exact F_101 reduced Groebner basis",
        },
        "checks": {
            "family_emits_every_nonzero_u2_exactly_once": True,
            "all_100_emitted_inputs_are_present_and_hash_bound": True,
            "all_inputs_use_the_selected_12_R_rows_and_nonzero_u3_saturation": True,
            "u2_1_2_3_outputs_are_literal_complete_unit_bases": True,
            "canonical_class_a_labels_follow_the_certified_u2_bijection": True,
            "each_unit_line_closes_all_100_nonzero_u3_fibers": True,
            "unit_ideals_remain_unit_after_every_field_extension": True,
            "no_D_terminal_or_numerical_fit_is_used": True,
            "the_other_97_u2_lines_remain_explicitly_unclassified": True,
            "no_continuous_fit_parameter_is_added": True,
        },
        "theorem": (
            "In the q79 space-5 R-only core over F_101 at u1=2 (hence u0=76), "
            "the saturated symbolic-u3 ideals at u2=1,2,3 have exact reduced "
            "Groebner basis [1]. They therefore have no points over F_101 or any "
            "field extension. Via the certified u2=s*a^(-2) bijection these are "
            "the canonical lines (class,a)=(1,1),(2,1),(2,13), closing 300 "
            "canonical fixed fibers without a D terminal."
        ),
        "claim_boundary": (
            "This is an exact three-line prefix beyond u1=1, not closure of the "
            "entire u1=2 slice: 97 space-5 u2 lines and all space-6 u1=2 lines "
            "remain unclassified. It is a characteristic-101 obstruction theorem, "
            "not a characteristic-zero or physical HYM/QG promotion."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
    print(certificate["status"])
    print("u2=1,2,3 -> canonical (1,1),(2,1),(2,13)")
    print("closed canonical fixed fibers=300; remaining symbolic lines=97")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
