"""Validate promotion of a projective Iwasawa twist to selected source data.

This is the twisted analogue of validate_iwasawa_selected_source_promotion.py.
It prevents a projective rho_E table from being promoted merely because its
corner failures are scalar central phases.  A passing packet must supply a
selected gerbe/B-field/discrete-torsion source, map it to the finite zeta_3
cocycle, verify Bianchi/Freed-Witten/projector gates, and pass the projective
rho_E, metric, and sector validators.

Exit codes:
  0: packet passes the implemented twisted-source promotion gate
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

SCHEMA = "IwasawaTwistedSourcePromotionPacket.v1"
SOURCE_KINDS = {
    "Deligne_Cech_gerbe",
    "B_field_period_table",
    "discrete_torsion_class",
    "finite_HYM_Strominger_twisted_solve",
}
TRUE_FLAGS = (
    "selected_twist_verified",
    "fixed_topological_sector",
    "no_observed_flavor_inputs",
)
FALSE_FLAGS = (
    "uses_execution_ii_benchmarks",
    "uses_observed_masses_or_mixings",
    "uses_projective_prototype_as_selected",
    "uses_zeta3_twist_as_q79_replacement",
)
GERBE_TRUE_FLAGS = (
    "selected_by_mtt",
    "fixed_differential_cohomology_class",
    "map_to_central_cocycle_verified",
    "green_schwarz_bianchi_verified",
    "freed_witten_verified",
    "twisted_projector_retains_sector",
    "coherent_spectral_projector_verified",
)
PATH_VALIDATORS = {
    "projective_rhoE_mesh": "validate_iwasawa_projective_rhoE_mesh.py",
    "rhoE_metric": "validate_iwasawa_rhoE_metric.py",
    "sector_maps": "validate_iwasawa_sector_maps.py",
}
EXPECTED_COCYCLE = {
    "base_group": "F_3^2",
    "omega_order": 3,
    "commutator_rank_over_F3": 2,
    "finite_heisenberg_extension_order": 27,
    "center_order": 3,
}


class IncompleteData(ValueError):
    """Raised when a promotion packet is still open."""


def resolve_path(value: Any, packet_path: Path, label: str) -> Path:
    if not isinstance(value, str) or not value:
        raise IncompleteData(f"MISSING paths.{label}")
    raw = Path(value)
    candidates = []
    if raw.is_absolute():
        candidates.append(raw)
    else:
        candidates.append((packet_path.parent / raw).resolve())
        candidates.append((ROOT / raw).resolve())
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise IncompleteData(f"MISSING file for paths.{label}: {value}")


def run_validator(script_name: str, data_path: Path) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / script_name), str(data_path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def parse_projective_report(output: str) -> dict[str, Any]:
    match = re.search(r"projective_report=(\{.*\})", output)
    if not match:
        raise ValueError(f"missing projective_report in validator output: {output}")
    return json.loads(match.group(1))


def validate_top_flags(data: dict[str, Any]) -> list[str]:
    failures = []
    for key in TRUE_FLAGS:
        if data.get(key) is not True:
            failures.append(f"{key} must be true")
    for key in FALSE_FLAGS:
        if data.get(key) is not False:
            failures.append(f"{key} must be false")
    return failures


def validate_gerbe_source(data: dict[str, Any]) -> list[str]:
    source = data.get("gerbe_source")
    if not isinstance(source, dict):
        raise IncompleteData("MISSING gerbe_source object")
    if source.get("source_kind") not in SOURCE_KINDS:
        raise ValueError(f"gerbe_source.source_kind must be one of {sorted(SOURCE_KINDS)}")

    failures = []
    for key in GERBE_TRUE_FLAGS:
        if key not in source:
            raise IncompleteData(f"MISSING gerbe_source.{key}")
        if source.get(key) is not True:
            failures.append(f"gerbe_source.{key} must be true")

    denominator = source.get("period_denominator")
    if denominator != 3:
        failures.append("gerbe_source.period_denominator must equal 3 for the certified zeta_3 route")

    phase = source.get("central_phase_label")
    if phase not in {"zeta_3^1", "zeta_3^2", "omega^1", "omega^2"}:
        failures.append("gerbe_source.central_phase_label must be a nontrivial third-root label")

    return failures


def validate_cocycle(data: dict[str, Any]) -> list[str]:
    cocycle = data.get("central_cocycle")
    if not isinstance(cocycle, dict):
        raise IncompleteData("MISSING central_cocycle object")
    failures = []
    for key, expected in EXPECTED_COCYCLE.items():
        if key not in cocycle:
            raise IncompleteData(f"MISSING central_cocycle.{key}")
        if cocycle.get(key) != expected:
            failures.append(f"central_cocycle.{key} must be {expected!r}")
    if cocycle.get("ordinary_bundle_coboundary_possible") is not False:
        failures.append("central_cocycle.ordinary_bundle_coboundary_possible must be false")
    return failures


def validate_paths(
    packet_path: Path,
    paths: dict[str, Any],
) -> tuple[list[str], dict[str, Any]]:
    failures = []
    reports: dict[str, Any] = {}
    for key, script_name in PATH_VALIDATORS.items():
        resolved = resolve_path(paths.get(key), packet_path, key)
        code, output = run_validator(script_name, resolved)
        reports[key] = {"exit": code, "path": str(resolved)}
        if key == "projective_rhoE_mesh" and code == 0:
            projective_report = parse_projective_report(output)
            reports[key]["projective_report"] = projective_report
            if projective_report.get("central_twist_is_nontrivial") is not True:
                failures.append("nontrivial central twist required for twisted-source promotion")
            if projective_report.get("projective_gerbe_gluing_passes") is not True:
                failures.append("projective rho_E mesh gluing must pass")
        if code == 2:
            raise IncompleteData(f"{key} validator incomplete: {output.strip()}")
        if code != 0:
            failures.append(f"{key} validator failed with exit {code}: {output.strip()}")
    return failures, reports


def validate_packet(packet_path: Path, data: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    if data.get("status") == "OPEN":
        raise IncompleteData("twisted-source promotion packet is OPEN")
    if data.get("schema") != SCHEMA:
        raise ValueError(f"schema must be {SCHEMA}")

    failures = validate_top_flags(data)
    if failures:
        return failures, {"guardrail_failures": failures}

    failures.extend(validate_gerbe_source(data))
    failures.extend(validate_cocycle(data))

    paths = data.get("paths")
    if not isinstance(paths, dict):
        raise IncompleteData("MISSING paths object")
    path_failures, path_reports = validate_paths(packet_path, paths)
    failures.extend(path_failures)

    report = {
        "schema": data.get("schema"),
        "source_kind": data.get("gerbe_source", {}).get("source_kind"),
        "central_cocycle": data.get("central_cocycle"),
        "path_reports": path_reports,
        "selected_twist_verified": data.get("selected_twist_verified") is True,
        "fixed_topological_sector": data.get("fixed_topological_sector") is True,
        "no_observed_flavor_inputs": data.get("no_observed_flavor_inputs") is True,
    }
    return failures, report


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_iwasawa_twisted_source_promotion.py <packet.json>")
        return 1

    packet_path = Path(argv[1]).resolve()
    try:
        data = json.loads(packet_path.read_text(encoding="utf-8"))
        failures, report = validate_packet(packet_path, data)
    except IncompleteData as exc:
        print(str(exc))
        return 2
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID twisted-source promotion packet: {exc}")
        return 1

    print(f"twisted_promotion_report={json.dumps(report, sort_keys=True)}")
    if failures:
        print("twisted-source promotion FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("twisted-source promotion PASS")
    print("selected projective twist source, Bianchi/Freed-Witten/projector gates, and finite validators pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
