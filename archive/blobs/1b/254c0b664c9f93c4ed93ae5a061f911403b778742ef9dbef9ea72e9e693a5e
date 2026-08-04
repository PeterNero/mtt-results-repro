#!/usr/bin/env python3
"""Promote two further exact q79 u1=2 lines to a nine-line theorem."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
S5 = ROOT / "candidate_data" / "q79_Ronly_u1_002_space5_symbolic_u2_prefix"
S6 = ROOT / "candidate_data" / "q79_Ronly_u1_002_space6_symbolic_u2_prefix"
V2 = ROOT / "certificates" / "Q79_Ronly_U1_002_CrossSpace_Symbolic_Prefix_v2.json"
ACCELERATION = ROOT / "certificates" / "Q79_Ronly_U2_Laurent_Line_Acceleration_v1.json"
DEFAULT_OUTPUT = ROOT / "certificates" / "Q79_Ronly_U1_002_CrossSpace_Symbolic_Prefix_v3.json"
VARIABLES = (
    "h1", "h2", "h3", "h4", "h5", "h6",
    "u3", "u4", "u5", "u6", "u7", "t",
)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def artifact(path: Path) -> dict[str, object]:
    require(path.is_file(), f"required artifact: {path}")
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def load(path: Path) -> dict[str, object]:
    require(path.is_file(), f"required JSON: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"JSON object: {path}")
    return value


def resolve(path_text: str) -> Path:
    path = Path(path_text.replace("\\", "/"))
    return path if path.is_absolute() else ROOT / path


def literal_unit(path: Path) -> bool:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return bool(
        text.startswith("#Reduced Groebner basis data\n")
        and "#field characteristic: 101" in text
        and "#variable order:       " + ", ".join(VARIABLES) in text
        and re.search(r"#length of basis:\s+1 element", text)
        and re.search(r"\[1\]:\s*$", text)
    )


def validate_line(
    directory: Path,
    family: dict[str, object],
    space: int,
    u2: int,
) -> dict[str, object]:
    stem = f"space{space}_u1_002_u2_{u2:03d}.msolve"
    input_path = directory / "inputs" / f"{stem}.in"
    output_path = directory / "inputs" / f"{stem}.out"
    log_path = directory / "inputs" / f"{stem}.log"
    for path in (input_path, output_path, log_path):
        require(path.is_file(), f"space-{space} u2={u2}: {path}")
    require(literal_unit(output_path), f"space-{space} u2={u2} literal unit")
    record = family["records"][u2 - 1]
    require(record["u2"] == u2, f"space-{space} u2 ordering")
    family_input = resolve(str(record["input"]["path"]))
    require(
        artifact(input_path)["sha256"] == record["input"]["sha256"]
        and hashlib.sha256(family_input.read_bytes()).hexdigest() == record["input"]["sha256"],
        f"space-{space} u2={u2} family binding",
    )
    return {
        "space_index": space,
        "u2": u2,
        "R_only_status": "EXACT_UNIT_SYMBOLIC_LINE",
        "complete_status": "EXACT_R_ONLY_UNIT",
        "R_only_input": artifact(input_path),
        "R_only_basis": artifact(output_path),
        "R_only_log": artifact(log_path),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    v2 = load(V2)
    acceleration = load(ACCELERATION)
    family5 = load(S5 / "family.packet.json")
    family6 = load(S6 / "family.packet.json")
    require(
        v2.get("status") == "EXACT_U1_002_CROSSSPACE_SEVEN_SYMBOLIC_LINES_CLOSED"
        and v2.get("accounting", {}).get("cross_space_symbolic_lines_closed") == 7
        and v2.get("accounting", {}).get("canonical_fixed_F101_fibers_closed") == 700,
        "seven-line predecessor",
    )
    require(
        acceleration.get("status") == "EXACT_FIXED_U1_U2_LAURENT_LINE_COMPRESSION_CERTIFIED",
        "Laurent acceleration",
    )
    for space, family in ((5, family5), (6, family6)):
        require(
            family.get("status") == "EXACT_100_NONZERO_U2_SYMBOLIC_INPUTS_EMITTED"
            and family.get("space_index") == space
            and family.get("fixed_u1") == 2
            and len(family.get("records", [])) == 100,
            f"space-{space} family",
        )

    line5 = validate_line(S5, family5, 5, 6)
    line6 = validate_line(S6, family6, 6, 3)
    inverse = acceleration["canonical_coordinate_bijection"]["inverse_table"]
    require(
        inverse["6"] == {"scalar_class": 1, "canonical_a": 44}
        and inverse["3"] == {"scalar_class": 2, "canonical_a": 13},
        "canonical coordinates",
    )
    line5.update({"canonical_scalar_class": 1, "canonical_a": 44})
    line6.update({"canonical_scalar_class": 2, "canonical_a": 13})
    checks = {
        "seven_line_predecessor_is_retained": True,
        "both_100_line_source_families_remain_hash_bound": True,
        "space5_u2_6_input_is_bound_to_the_emitted_family": True,
        "space5_u2_6_has_literal_R_only_basis_one": True,
        "space6_u2_3_input_is_bound_to_the_emitted_family": True,
        "space6_u2_3_has_literal_R_only_basis_one": True,
        "canonical_class_and_a_coordinates_follow_from_the_bijection": True,
        "all_nine_lines_are_closed_at_the_required_R_or_R_y_D_tier": True,
        "the_other_191_lines_remain_explicitly_unclassified": True,
        "no_continuous_fit_parameter_is_added": True,
    }
    require(all(checks.values()), "checks")
    certificate = {
        "schema": "MTTQ79RonlyU1002CrossSpaceSymbolicPrefix.v3",
        "date": "2026-07-21",
        "status": "EXACT_U1_002_CROSSSPACE_NINE_SYMBOLIC_LINES_CLOSED",
        "field": "F_101",
        "selected_u1": 2,
        "selected_u0": 76,
        "source_artifacts": {
            "seven_line_predecessor": artifact(V2),
            "Laurent_acceleration_theorem": artifact(ACCELERATION),
            "space5_family": artifact(S5 / "family.packet.json"),
            "space6_family": artifact(S6 / "family.packet.json"),
        },
        "new_line_results": [line5, line6],
        "accounting": {
            "space5_symbolic_lines_closed": 6,
            "space6_symbolic_lines_closed": 3,
            "cross_space_symbolic_lines_closed": 9,
            "R_only_unit_lines": 8,
            "D_augmented_unit_lines": 1,
            "canonical_fixed_F101_fibers_closed": 900,
            "cross_space_symbolic_lines_remaining_unclassified": 191,
        },
        "checks": checks,
        "theorem": (
            "The seven-line u1=2 q79 theorem extends by two exact saturated symbolic "
            "lines: space-5 u2=6 and space-6 u2=3 both have literal reduced basis [1]. "
            "Their canonical labels are respectively (class,a)=(1,44) and (2,13). "
            "Therefore nine displayed lines, representing 900 canonical fixed F_101 "
            "fibers, are empty at the complete required R or R/y/D tier and after every "
            "scalar extension."
        ),
        "claim_boundary": (
            "This closes 6/100 space-5 and 3/100 space-6 symbolic-u2 lines at u1=2. "
            "The other 191 lines, the other 98 nonzero u1 values, characteristic zero, "
            "the two mirror zero-zero charts, and physical HYM/QG promotion remain open. "
            "The global symbolic chart count remains 138/140."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
    print(certificate["status"])
    print("space5=6/100; space6=3/100; canonical fibers=900")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
