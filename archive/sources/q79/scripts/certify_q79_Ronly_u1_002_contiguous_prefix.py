#!/usr/bin/env python3
"""Certify the maximal currently closed contiguous q79 u1=2 line prefixes."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
S5 = ROOT / "candidate_data" / "q79_Ronly_u1_002_space5_symbolic_u2_prefix"
S6 = ROOT / "candidate_data" / "q79_Ronly_u1_002_space6_symbolic_u2_prefix"
D_DIRECTORY = ROOT / "candidate_data" / "q79_Ronly_u1_002_symbolic_exception_D_closure"
V3 = ROOT / "certificates" / "Q79_Ronly_U1_002_CrossSpace_Symbolic_Prefix_v3.json"
SOLVER_BASELINE = ROOT / "certificates" / "Q79_Ronly_U1_002_Space5_Symbolic_U2_Prefix_v1.json"
ACCELERATION = ROOT / "certificates" / "Q79_Ronly_U2_Laurent_Line_Acceleration_v1.json"
DEFAULT_OUTPUT = ROOT / "certificates" / "Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1.json"
BATCH_RESULT = (
    ROOT
    / "candidate_data"
    / "q79_Ronly_u1_002_remaining_029_100_batch"
    / "q79_Ronly_u1_002_remaining_029_100.result.packet.json"
)
BATCH_MANIFEST = (
    ROOT
    / "candidate_data"
    / "q79_Ronly_u1_002_remaining_029_100_batch"
    / "input_manifest.json"
)
BATCH_CONTRACT = (
    ROOT
    / "proof_corpus"
    / "Q79_Ronly_U1_002_Remaining_029_100_Batch_Execution_Contract_v1.md"
)
VARIABLES = (
    "h1", "h2", "h3", "h4", "h5", "h6",
    "u3", "u4", "u5", "u6", "u7", "t",
)
ACCEPTED_D_STATUSES = {
    "EXACT_R_ONLY_FINITE_AFFINE_QUADRATIC_LINE_REJECTED_SCHEME_THEORETICALLY_BY_D",
    "EXACT_R_ONLY_FINITE_GROEBNER_LINE_REJECTED_SCHEME_THEORETICALLY_BY_D",
    "EXACT_R_ONLY_DOUBLE_POINT_LINE_REJECTED_SCHEME_THEORETICALLY_BY_D",
}


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


def artifact_entry_is_valid(entry: dict[str, object]) -> bool:
    path = resolve(str(entry.get("path", "")))
    return bool(
        path.is_file()
        and path.stat().st_size == entry.get("bytes")
        and hashlib.sha256(path.read_bytes()).hexdigest() == entry.get("sha256")
    )


def classify_basis(path: Path) -> str | None:
    if not path.is_file() or path.stat().st_size == 0:
        return None
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if not (
        text.startswith("#Reduced Groebner basis data\n")
        and "#field characteristic: 101" in text
        and "#variable order:       " + ", ".join(VARIABLES) in text
        and text.rstrip().endswith("]:")
    ):
        return None
    length = re.search(r"#length of basis:\s+(\d+) element", text)
    require(length is not None and int(length.group(1)) >= 1, f"basis length: {path}")
    return "R_ONLY_UNIT" if re.search(r"\[1\]:\s*$", text) else "R_ONLY_NONUNIT"


def validate_solver_log(path: Path, classification: str) -> None:
    require(path.is_file() and path.stat().st_size > 0, f"solver log: {path}")
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    required = (
        r"field characteristic\s+101",
        r"monomial order\s+DRL",
        r"#threads\s+1",
        r"reduce gb\s+1",
        r"#invalid equations\s+0",
        r"msolve overall time",
    )
    require(all(re.search(pattern, text) for pattern in required), f"exact solver mode: {path}")
    if classification == "R_ONLY_UNIT":
        require(
            "Grobner basis has a single element" in text and "No solution" in text,
            f"unit-basis solver verdict: {path}",
        )


def valid_d_certificate(path: Path, packet: dict[str, object]) -> bool:
    coordinates = packet.get("fixed_coordinates", {})
    witness = packet.get("unit_witness", {})
    checks = packet.get("checks", {})
    artifacts = packet.get("artifacts", {})
    product = witness.get("product_coefficients", [])
    return bool(
        packet.get("status") in ACCEPTED_D_STATUSES
        and coordinates.get("u1") == 2
        and coordinates.get("selected_u0") == 76
        and isinstance(checks, dict)
        and checks
        and all(checks.values())
        and isinstance(artifacts, dict)
        and artifacts
        and all(
            isinstance(entry, dict) and artifact_entry_is_valid(entry)
            for entry in artifacts.values()
        )
        and witness.get("D_multiplication_determinant", 0) % 101 != 0
        and isinstance(product, list)
        and product
        and product[0] == 1
        and all(value == 0 for value in product[1:])
        and path.is_file()
    )


def d_certificates() -> dict[tuple[int, int], tuple[Path, dict[str, object]]]:
    result: dict[tuple[int, int], tuple[Path, dict[str, object]]] = {}
    if not D_DIRECTORY.is_dir():
        return result
    for path in sorted(D_DIRECTORY.glob("*.D_unit.certificate.json")):
        packet = load(path)
        if not valid_d_certificate(path, packet):
            continue
        coordinates = packet["fixed_coordinates"]
        key = (int(packet["space_index"]), int(coordinates["selected_u2"]))
        require(key not in result, f"unique D certificate: {key}")
        result[key] = (path, packet)
    return result


def scan_space(
    directory: Path,
    family: dict[str, object],
    space: int,
    inverse: dict[str, object],
    d_map: dict[tuple[int, int], tuple[Path, dict[str, object]]],
) -> tuple[list[dict[str, object]], dict[str, object]]:
    records = []
    stop: dict[str, object] = {"next_u2": 101, "reason": "ALL_100_LINES_CLOSED"}
    for u2 in range(1, 101):
        stem = f"space{space}_u1_002_u2_{u2:03d}.msolve"
        input_path = directory / "inputs" / f"{stem}.in"
        output_path = directory / "inputs" / f"{stem}.out"
        log_path = directory / "inputs" / f"{stem}.log"
        family_row = family["records"][u2 - 1]
        require(family_row["u2"] == u2, f"space-{space} family ordering")
        family_input = resolve(str(family_row["input"]["path"]))
        require(
            artifact(input_path)["sha256"] == family_row["input"]["sha256"]
            and hashlib.sha256(family_input.read_bytes()).hexdigest() == family_row["input"]["sha256"],
            f"space-{space} u2={u2} family binding",
        )
        classification = classify_basis(output_path)
        if classification is None:
            stop = {"next_u2": u2, "reason": "NO_EXACT_REDUCED_BASIS"}
            break
        validate_solver_log(log_path, classification)
        canonical = inverse[str(u2)]
        row = {
            "space_index": space,
            "u2": u2,
            "canonical_scalar_class": canonical["scalar_class"],
            "canonical_a": canonical["canonical_a"],
            "R_only_classification": classification,
            "R_only_input": artifact(input_path),
            "R_only_basis": artifact(output_path),
            "R_only_log": artifact(log_path),
        }
        if classification == "R_ONLY_UNIT":
            row["complete_status"] = "EXACT_R_ONLY_UNIT"
        else:
            d_entry = d_map.get((space, u2))
            if d_entry is None:
                stop = {
                    "next_u2": u2,
                    "reason": "EXACT_NONUNIT_R_LINE_REQUIRES_D_CLOSURE",
                    "R_only_basis": artifact(output_path),
                }
                break
            d_path, d_packet = d_entry
            require(
                d_packet["scalar_square_class_representative"] == canonical["scalar_class"]
                and d_packet["fixed_coordinates"]["a_equals_v_times_u3"] == canonical["canonical_a"],
                f"space-{space} u2={u2} D coordinates",
            )
            row["complete_status"] = "EXACT_FULL_R_Y_D_UNIT"
            row["D_unit_certificate"] = artifact(d_path)
            row["quotient_dimension"] = d_packet["quotient_algebra"]["dimension"]
            row["D_unit_row"] = d_packet["unit_witness"]["parent_row"]
            row["D_multiplication_determinant"] = d_packet["unit_witness"]["D_multiplication_determinant"]
        records.append(row)
    return records, stop


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    predecessor = load(V3)
    solver_baseline = load(SOLVER_BASELINE)
    acceleration = load(ACCELERATION)
    batch = load(BATCH_RESULT)
    family5 = load(S5 / "family.packet.json")
    family6 = load(S6 / "family.packet.json")
    require(
        predecessor.get("status") == "EXACT_U1_002_CROSSSPACE_NINE_SYMBOLIC_LINES_CLOSED"
        and predecessor.get("accounting", {}).get("cross_space_symbolic_lines_closed") == 9,
        "nine-line predecessor",
    )
    require(
        acceleration.get("status") == "EXACT_FIXED_U1_U2_LAURENT_LINE_COMPRESSION_CERTIFIED",
        "Laurent acceleration",
    )
    require(
        batch.get("status") == "EXACT_U1_002_REMAINING_R_ONLY_LINES_CLASSIFIED"
        and batch.get("accounting", {}).get("requested_lines") == 144
        and batch.get("accounting", {}).get("R_only_unit_lines") == 138
        and batch.get("accounting", {}).get("R_only_nonunit_lines") == 6
        and len(batch.get("results", [])) == 144,
        "completed remaining-line batch",
    )
    require(
        {
            (int(row["space_index"]), int(row["u2"]))
            for row in batch["results"]
            if row["classification"] == "R_ONLY_NONUNIT"
        }
        == {(5, 31), (6, 53), (6, 59), (5, 73), (5, 75), (6, 91)},
        "six exact remaining R-only exceptions",
    )
    solver_provenance = solver_baseline.get("solver_provenance", {})
    require(
        solver_provenance.get("engine") == "msolve 0.10.1"
        and solver_provenance.get("binary_sha256")
        == "a4c2beb9a7d186394af6bb21e235f76e3bfb3d0e6fdf872c27b517b8a6e87e13"
        and solver_provenance.get("mode")
        == "one thread, exact F_101 reduced Groebner basis",
        "solver provenance",
    )
    for space, family in ((5, family5), (6, family6)):
        require(
            family.get("status") == "EXACT_100_NONZERO_U2_SYMBOLIC_INPUTS_EMITTED"
            and family.get("space_index") == space
            and family.get("fixed_u1") == 2
            and len(family.get("records", [])) == 100,
            f"space-{space} family",
        )
    inverse = acceleration["canonical_coordinate_bijection"]["inverse_table"]
    d_map = d_certificates()
    space5, stop5 = scan_space(S5, family5, 5, inverse, d_map)
    space6, stop6 = scan_space(S6, family6, 6, inverse, d_map)
    require(len(space5) >= 6 and len(space6) >= 3, "predecessor lines retained")
    lines = space5 + space6
    r_units = sum(row["complete_status"] == "EXACT_R_ONLY_UNIT" for row in lines)
    d_units = sum(row["complete_status"] == "EXACT_FULL_R_Y_D_UNIT" for row in lines)
    closed = len(lines)
    remaining = 200 - closed
    complete_cover = len(space5) == 100 and len(space6) == 100
    checks = {
        "nine_line_predecessor_is_retained": len(space5) >= 6 and len(space6) >= 3,
        "both_source_families_are_complete_and_hash_bound": True,
        "solver_binary_version_hash_and_exact_mode_are_bound": True,
        "every_counted_solver_log_matches_the_exact_mode": True,
        "every_counted_output_is_a_complete_reduced_Groebner_basis": True,
        "every_R_only_unit_output_is_literal_basis_one": True,
        "every_counted_nonunit_R_line_has_an_exact_coordinate_matched_D_unit_certificate": d_units == sum(row["R_only_classification"] == "R_ONLY_NONUNIT" for row in lines),
        "every_D_certificate_transitively_hash_binds_its_source_artifacts": True,
        "the_closed_prefix_in_each_space_stops_before_the_first_unproved_line": True,
        "canonical_labels_are_read_from_the_proved_u2_bijection": True,
        "closed_line_accounting_is_exact": r_units + d_units == closed,
        "completed_batch_is_hash_bound_and_its_six_nonunit_rows_are_exactly_the_D_augmented_rows": (
            all(
                next(
                    row
                    for row in lines
                    if row["space_index"] == batch_row["space_index"]
                    and row["u2"] == batch_row["u2"]
                )["R_only_classification"]
                == batch_row["classification"]
                for batch_row in batch["results"]
            )
        ),
        "both_contiguous_prefixes_exhaust_the_nonzero_F101_u2_torus": complete_cover,
        "no_continuous_fit_parameter_is_added": True,
    }
    require(all(checks.values()), "checks")
    certificate = {
        "schema": "MTTQ79RonlyU1002ContiguousCrossSpacePrefix.v1",
        "date": "2026-07-24",
        "status": "EXACT_U1_002_CONTIGUOUS_CROSSSPACE_PREFIX_CLOSED",
        "coverage_status": (
            "COMPLETE_NONZERO_U2_CROSSSPACE_COVER"
            if complete_cover
            else "CONTIGUOUS_PREFIX_ONLY"
        ),
        "field": "F_101",
        "selected_u1": 2,
        "selected_u0": 76,
        "source_artifacts": {
            "nine_line_predecessor": artifact(V3),
            "solver_provenance_baseline": artifact(SOLVER_BASELINE),
            "Laurent_acceleration_theorem": artifact(ACCELERATION),
            "space5_family": artifact(S5 / "family.packet.json"),
            "space6_family": artifact(S6 / "family.packet.json"),
            "remaining_batch_manifest": artifact(BATCH_MANIFEST),
            "remaining_batch_contract": artifact(BATCH_CONTRACT),
            "remaining_batch_result": artifact(BATCH_RESULT),
        },
        "solver_provenance": solver_provenance,
        "space5_closed_lines": space5,
        "space6_closed_lines": space6,
        "first_unproved_line": {"space5": stop5, "space6": stop6},
        "accounting": {
            "space5_contiguous_symbolic_lines_closed": len(space5),
            "space6_contiguous_symbolic_lines_closed": len(space6),
            "cross_space_symbolic_lines_closed": closed,
            "R_only_unit_lines": r_units,
            "D_augmented_unit_lines": d_units,
            "canonical_fixed_F101_fibers_closed": 100 * closed,
            "cross_space_symbolic_lines_remaining_unclassified": remaining,
        },
        "checks": checks,
        "theorem": (
            f"At u1=2, all {len(space5)} nonzero symbolic-u2 lines in space 5 and "
            f"all {len(space6)} in space 6 are empty at the complete required R or "
            f"R/y/D tier over F_101 and every scalar extension. This closes "
            f"{closed}/200 lines and represents {100 * closed} canonical fixed F_101 "
            "fibers."
        ),
        "claim_boundary": (
            "All nonzero-u2 lines at selected u1=2 are classified. The other 98 "
            "nonzero u1 values, characteristic zero, the two mirror zero-zero charts, "
            "and physical HYM/QG promotion remain open. The global symbolic chart "
            "count remains 138/140."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
    print(certificate["status"])
    print(
        f"space5={len(space5)}/100; space6={len(space6)}/100; "
        f"closed={closed}/200; fibers={100 * closed}"
    )
    print(f"next: space5={stop5}; space6={stop6}")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
