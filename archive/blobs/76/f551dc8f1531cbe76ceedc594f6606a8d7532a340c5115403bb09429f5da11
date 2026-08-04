"""Validate block-factorized sector maps for the qutrit twisted route.

The ordinary sector-map validator assumes every SM slot is a projector inside
one rank-three bundle.  That is the wrong architecture for the qutrit twisted
route because the Higgs line must be separated from the irreducible qutrit
family block.  This validator checks the corrected architecture:

* Q,u,d,L,e,N occupy the full rank-three projective family block;
* H occupies a separate ordinary rank-one Higgs line;
* the family block passes projective rho_E and metric validators;
* sector maps are projectors on their own blocks, not a fake rank-one Higgs
  projector inside the irreducible qutrit block.

Exit codes:
  0: packet passes finite block-factorized sector-map checks
  1: complete packet fails a mathematical/schema/guardrail check
  2: packet is incomplete/open rather than mathematically failed
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCHEMA = "IwasawaBlockFactorizedSectorMaps.v1"
FAMILY_SECTORS = ("Q", "u", "d", "L", "e", "N")
GENERATORS = ("g1", "g2", "g3", "g4", "g5", "g6")
TOL = 1e-9

Matrix = list[list[complex]]


class IncompleteData(ValueError):
    """Raised when required finite data are absent."""


def resolve_path(value: Any, packet_path: Path, label: str) -> Path:
    if not isinstance(value, str) or not value:
        raise IncompleteData(f"MISSING {label}")
    raw = Path(value)
    candidates = [raw] if raw.is_absolute() else [
        (packet_path.parent / raw).resolve(),
        (ROOT / raw).resolve(),
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise IncompleteData(f"MISSING file for {label}: {value}")


def run_validator(script_name: str, path: Path) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / script_name), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def parse_projective_report(output: str) -> dict[str, Any]:
    match = re.search(r"projective_report=(\{.*\})", output)
    if not match:
        raise ValueError("missing projective_report in projective validator output")
    return json.loads(match.group(1))


def parse_complex(value: Any) -> complex:
    if isinstance(value, bool):
        raise ValueError(f"invalid complex entry {value!r}")
    if isinstance(value, (int, float)):
        return complex(float(value), 0.0)
    if (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(part, (int, float)) and not isinstance(part, bool) for part in value)
    ):
        return complex(float(value[0]), float(value[1]))
    raise ValueError(f"invalid complex entry {value!r}")


def parse_matrix(value: Any, size: int, label: str) -> Matrix:
    matrix_data = value.get("matrix") if isinstance(value, dict) else value
    if not isinstance(matrix_data, list) or len(matrix_data) != size:
        raise ValueError(f"{label} must have {size} rows")
    matrix: Matrix = []
    for row in matrix_data:
        if not isinstance(row, list) or len(row) != size:
            raise ValueError(f"{label} must be {size}x{size}")
        matrix.append([parse_complex(entry) for entry in row])
    return matrix


def matmul(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return [
        [sum(left[row][mid] * right[mid][col] for mid in range(size)) for col in range(size)]
        for row in range(size)
    ]


def adjoint(matrix: Matrix) -> Matrix:
    size = len(matrix)
    return [[matrix[col][row].conjugate() for col in range(size)] for row in range(size)]


def max_abs_diff(left: Matrix, right: Matrix) -> float:
    size = len(left)
    return max(abs(left[row][col] - right[row][col]) for row in range(size) for col in range(size))


def matrix_rank(matrix: Matrix) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = None
        for row in range(rank, rows):
            if abs(work[row][col]) > TOL:
                pivot = row
                break
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][col]
        work[rank] = [value / scale for value in work[rank]]
        for row in range(rows):
            if row == rank or abs(work[row][col]) <= TOL:
                continue
            factor = work[row][col]
            work[row] = [work[row][idx] - factor * work[rank][idx] for idx in range(cols)]
        rank += 1
    return rank


def identity(size: int) -> Matrix:
    return [[1.0 + 0j if row == col else 0j for col in range(size)] for row in range(size)]


def validate_projector(projector: Matrix, rank: int, label: str) -> list[str]:
    failures: list[str] = []
    if max_abs_diff(projector, adjoint(projector)) > TOL:
        failures.append(f"{label} projector is not Hermitian")
    if max_abs_diff(matmul(projector, projector), projector) > TOL:
        failures.append(f"{label} projector is not idempotent")
    actual_rank = matrix_rank(projector)
    if actual_rank != rank:
        failures.append(f"{label} projector rank {actual_rank} != {rank}")
    return failures


def load_generator_data(path: Path) -> dict[str, Matrix]:
    data = json.loads(path.read_text(encoding="utf-8"))
    generator_data = data.get("generator_data")
    if not isinstance(generator_data, dict):
        raise IncompleteData("MISSING generator_data in family rhoE path")
    matrices: dict[str, Matrix] = {}
    for generator in GENERATORS:
        if generator_data.get(generator) is None:
            raise IncompleteData(f"MISSING generator_data.{generator}")
        matrices[generator] = parse_matrix(generator_data[generator], 3, f"generator {generator}")
    return matrices


def validate_family_block(packet_path: Path, data: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    block = data.get("family_block")
    if not isinstance(block, dict):
        raise IncompleteData("MISSING family_block")

    rho_path = resolve_path(block.get("projective_rhoE_mesh"), packet_path, "family_block.projective_rhoE_mesh")
    metric_path = resolve_path(block.get("rhoE_metric"), packet_path, "family_block.rhoE_metric")
    sectors = block.get("sector_projectors")
    if not isinstance(sectors, dict):
        raise IncompleteData("MISSING family_block.sector_projectors")

    failures: list[str] = []
    projective_code, projective_output = run_validator("validate_iwasawa_projective_rhoE_mesh.py", rho_path)
    if projective_code != 0:
        failures.append(f"projective family rhoE validator failed with exit {projective_code}: {projective_output.strip()}")
        projective_report: dict[str, Any] = {}
    else:
        projective_report = parse_projective_report(projective_output)
        if projective_report.get("projective_gerbe_gluing_passes") is not True:
            failures.append("family projective gerbe gluing must pass")
        if projective_report.get("central_twist_is_nontrivial") is not True:
            failures.append("family central twist must be nontrivial")

    metric_code, metric_output = run_validator("validate_iwasawa_rhoE_metric.py", metric_path)
    if metric_code != 0:
        failures.append(f"family metric validator failed with exit {metric_code}: {metric_output.strip()}")

    generator_matrices = load_generator_data(rho_path)
    for sector in FAMILY_SECTORS:
        entry = sectors.get(sector)
        if not isinstance(entry, dict):
            raise IncompleteData(f"MISSING family sector {sector}")
        if entry.get("kind") != "family":
            failures.append(f"family sector {sector} kind must be family")
        if entry.get("dimension") != 3:
            failures.append(f"family sector {sector} dimension must be 3")
        projector = parse_matrix(entry.get("projector"), 3, f"family sector {sector}")
        failures.extend(validate_projector(projector, 3, f"family sector {sector}"))
        for generator, rho in generator_matrices.items():
            if max_abs_diff(matmul(projector, rho), matmul(rho, projector)) > TOL:
                failures.append(f"family sector {sector} projector does not commute with {generator}")

    return failures, {
        "projective_rhoE_mesh": str(rho_path),
        "rhoE_metric": str(metric_path),
        "projective_validator_exit": projective_code,
        "metric_validator_exit": metric_code,
        "projective_report": projective_report,
        "family_sectors": list(FAMILY_SECTORS),
    }


def validate_higgs_line(data: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    block = data.get("higgs_line_block")
    if not isinstance(block, dict):
        raise IncompleteData("MISSING higgs_line_block")

    failures: list[str] = []
    if block.get("kind") != "ordinary_trivial_line":
        failures.append("higgs_line_block.kind must be ordinary_trivial_line")
    if block.get("dimension") != 1:
        failures.append("higgs_line_block.dimension must be 1")
    projector = parse_matrix(block.get("projector"), 1, "higgs line projector")
    failures.extend(validate_projector(projector, 1, "higgs line"))

    transitions = block.get("transition_scalars")
    if not isinstance(transitions, dict):
        raise IncompleteData("MISSING higgs_line_block.transition_scalars")
    for generator in GENERATORS:
        if generator not in transitions:
            raise IncompleteData(f"MISSING higgs transition {generator}")
        scalar = parse_complex(transitions[generator])
        if abs(scalar - 1.0) > TOL:
            failures.append(f"higgs transition {generator} must be trivial identity")

    return failures, {
        "kind": block.get("kind"),
        "dimension": block.get("dimension"),
        "transition_scalars_trivial": True,
    }


def validate_packet(packet_path: Path, data: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    if data.get("status") == "OPEN":
        raise IncompleteData("block-factorized sector-map packet is OPEN")
    failures: list[str] = []
    if data.get("schema") != SCHEMA:
        failures.append(f"schema must be {SCHEMA}")
    if data.get("selected_by_mtt") is not False:
        failures.append("selected_by_mtt must be false for this finite candidate")
    if data.get("no_observed_flavor_inputs") is not True:
        failures.append("no_observed_flavor_inputs must be true")
    for key in ("uses_execution_ii_benchmarks", "uses_observed_masses_or_mixings"):
        if data.get(key) is not False:
            failures.append(f"{key} must be false")

    family_failures, family_report = validate_family_block(packet_path, data)
    higgs_failures, higgs_report = validate_higgs_line(data)
    failures.extend(family_failures)
    failures.extend(higgs_failures)

    report = {
        "schema": data.get("schema"),
        "status": data.get("status"),
        "family_block": family_report,
        "higgs_line_block": higgs_report,
        "finite_block_factorized_sector_maps_valid": not failures,
        "selected_source_ready": False,
    }
    return failures, report


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_iwasawa_block_factorized_sector_maps.py <packet.json>")
        return 1

    packet_path = Path(argv[1]).resolve()
    try:
        data = json.loads(packet_path.read_text(encoding="utf-8"))
        failures, report = validate_packet(packet_path, data)
    except IncompleteData as exc:
        print(str(exc))
        return 2
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID block-factorized sector-map packet: {exc}")
        return 1

    print(f"block_factorized_sector_report={json.dumps(report, sort_keys=True)}")
    if failures:
        print("block-factorized sector-map validation FAIL")
        for failure in failures[:50]:
            print(f"- {failure}")
        if len(failures) > 50:
            print(f"- ... {len(failures) - 50} more failures")
        return 1

    print("block-factorized sector-map validation PASS")
    print("family sectors and separate Higgs line validate; selected source remains separate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
