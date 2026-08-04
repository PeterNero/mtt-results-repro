"""Validate promotion of Iwasawa rho_E/D_E data to selected proof evidence.

This is a guardrail validator.  It does not construct the selected bundle or
operator data.  Instead it prevents finite validator prototypes from being
promoted unless they pass the relevant lower-level validators and, at the
response level, carry a nonzero selected dotD response.

Exit codes:
  0: promotion packet passes the implemented gate for its target level
  1: complete packet fails an implemented mathematical/schema check
  2: packet is incomplete/open rather than mathematically failed
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"

SCHEMA = "IwasawaSelectedSourcePromotionPacket.v1"
SOURCE_KINDS = {
    "typed_Cech_monad_transition_data",
    "finite_HYM_Strominger_solve",
}
TARGET_LEVELS = {"rhoE_source", "de_response"}
TRUE_FLAGS = ("selected_source_verified", "no_observed_flavor_inputs")
FALSE_FLAGS = (
    "uses_execution_ii_benchmarks",
    "uses_observed_masses_or_mixings",
    "uses_diagnostic_h1_three_as_selected",
    "uses_pure_gauge_prototype_as_selected",
)
SOURCE_VALIDATORS = {
    "rhoE_mesh": "validate_iwasawa_rhoE_mesh.py",
    "rhoE_metric": "validate_iwasawa_rhoE_metric.py",
    "sector_maps": "validate_iwasawa_sector_maps.py",
}
RESPONSE_VALIDATORS = {
    "route_c_residuals": "validate_iwasawa_route_c_residuals.py",
    "de_action": "validate_iwasawa_de_action.py",
    "riesz_gap": "validate_iwasawa_riesz_gap.py",
    "reduced_green": "validate_iwasawa_reduced_green.py",
    "dotd_response": "validate_iwasawa_dotd_response.py",
}
TOL = 1e-12


class IncompleteData(ValueError):
    """Raised when a promotion packet is still open."""


def parse_complex(value: Any) -> complex:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return complex(float(value), 0.0)
    if (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(part, (int, float)) and not isinstance(part, bool) for part in value)
    ):
        return complex(float(value[0]), float(value[1]))
    raise ValueError(f"invalid complex entry {value!r}")


def max_abs_nested(value: Any) -> float:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return abs(float(value))
    if (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(part, (int, float)) and not isinstance(part, bool) for part in value)
    ):
        return abs(parse_complex(value))
    if isinstance(value, list):
        return max((max_abs_nested(part) for part in value), default=0.0)
    if isinstance(value, dict):
        if "matrix" in value:
            return max_abs_nested(value["matrix"])
        return max((max_abs_nested(part) for part in value.values()), default=0.0)
    return 0.0


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


def detect_coboundary(rho_path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [
            sys.executable,
            str(SCRIPTS / "detect_iwasawa_face_graph_coboundary.py"),
            str(rho_path),
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        raise ValueError(f"face-graph coboundary diagnostic failed: {proc.stdout}")
    return json.loads(proc.stdout)


def require_float(value: Any, label: str, default: float) -> float:
    if value is None:
        return default
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValueError(f"{label} must be numeric")
    parsed = float(value)
    if parsed < 0:
        raise ValueError(f"{label} must be nonnegative")
    return parsed


def dotd_response_norms(dotd_path: Path) -> dict[str, Any]:
    data = json.loads(dotd_path.read_text(encoding="utf-8"))
    slots = data.get("dotd_response_slots")
    if not isinstance(slots, dict):
        raise IncompleteData("MISSING dotd_response_slots object for norm check")

    max_source_norm = 0.0
    max_response_norm = 0.0
    nonzero_response_sectors: list[str] = []
    for sector, slot in sorted(slots.items()):
        if not isinstance(slot, dict):
            raise IncompleteData(f"MISSING {sector} dotD response slot object")
        source_norm = max_abs_nested(slot.get("source_vectors"))
        response_norm = max_abs_nested(slot.get("horizontal_response_vectors"))
        max_source_norm = max(max_source_norm, source_norm)
        max_response_norm = max(max_response_norm, response_norm)
        if response_norm > TOL:
            nonzero_response_sectors.append(sector)

    return {
        "max_source_norm": max_source_norm,
        "max_response_norm": max_response_norm,
        "nonzero_response_sectors": nonzero_response_sectors,
    }


def validate_flags(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    for key in TRUE_FLAGS:
        if data.get(key) is not True:
            failures.append(f"{key} must be true")
    for key in FALSE_FLAGS:
        if data.get(key) is not False:
            failures.append(f"{key} must be false")
    return failures


def validate_paths(
    packet_path: Path,
    paths: dict[str, Any],
    validators: dict[str, str],
) -> tuple[list[str], dict[str, Path]]:
    failures: list[str] = []
    resolved: dict[str, Path] = {}
    for key, script_name in validators.items():
        path = resolve_path(paths.get(key), packet_path, key)
        resolved[key] = path
        code, output = run_validator(script_name, path)
        if code == 2:
            raise IncompleteData(f"{key} validator incomplete: {output.strip()}")
        if code != 0:
            failures.append(f"{key} validator failed with exit {code}: {output.strip()}")
    return failures, resolved


def validate_packet(packet_path: Path, data: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    if data.get("status") == "OPEN":
        raise IncompleteData("selected-source promotion packet is OPEN")
    if data.get("schema") != SCHEMA:
        raise ValueError(f"schema must be {SCHEMA}")
    target_level = data.get("target_level")
    if target_level not in TARGET_LEVELS:
        raise ValueError(f"target_level must be one of {sorted(TARGET_LEVELS)}")
    if data.get("source_kind") not in SOURCE_KINDS:
        raise ValueError(f"source_kind must be one of {sorted(SOURCE_KINDS)}")

    paths = data.get("paths")
    if not isinstance(paths, dict):
        raise IncompleteData("MISSING paths object")

    failures = validate_flags(data)
    source_failures, resolved = validate_paths(packet_path, paths, SOURCE_VALIDATORS)
    failures.extend(source_failures)

    rho_path = resolved["rhoE_mesh"]
    coboundary = detect_coboundary(rho_path)
    face_graph_coboundary = coboundary.get("face_graph_coboundary") is True

    if target_level == "rhoE_source" and face_graph_coboundary:
        failures.append(
            "rhoE_source promotion requires a non-coboundary finite face graph; "
            "pure-gauge finite tables cannot be promoted from rho_E data alone"
        )

    response_norms: dict[str, Any] | None = None
    if target_level == "de_response":
        response_failures, response_paths = validate_paths(packet_path, paths, RESPONSE_VALIDATORS)
        failures.extend(response_failures)
        resolved.update(response_paths)

        response_gate = data.get("response_gate", {})
        if response_gate is None:
            response_gate = {}
        if not isinstance(response_gate, dict):
            raise ValueError("response_gate must be an object when supplied")
        min_source = require_float(
            response_gate.get("minimum_source_norm"),
            "response_gate.minimum_source_norm",
            TOL,
        )
        min_response = require_float(
            response_gate.get("minimum_response_norm"),
            "response_gate.minimum_response_norm",
            TOL,
        )
        response_norms = dotd_response_norms(resolved["dotd_response"])
        if response_norms["max_source_norm"] <= min_source:
            failures.append(
                "dotD source norm "
                f"{response_norms['max_source_norm']:.3e} <= required {min_source:.3e}"
            )
        if response_norms["max_response_norm"] <= min_response:
            failures.append(
                "horizontal response norm "
                f"{response_norms['max_response_norm']:.3e} <= required {min_response:.3e}"
            )

    report = {
        "target_level": target_level,
        "rhoE_face_graph_coboundary": face_graph_coboundary,
        "coboundary_diagnostic": coboundary,
        "resolved_paths": {key: str(value) for key, value in resolved.items()},
        "dotd_response_norms": response_norms,
    }
    return failures, report


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_iwasawa_selected_source_promotion.py <promotion-packet.json>")
        return 1

    packet_path = Path(argv[1]).resolve()
    try:
        data = json.loads(packet_path.read_text(encoding="utf-8"))
        failures, report = validate_packet(packet_path, data)
    except IncompleteData as exc:
        print(str(exc))
        return 2
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID selected-source promotion packet: {exc}")
        return 1

    print("Iwasawa selected-source promotion gate")
    print(f"target_level={report['target_level']}")
    print(f"rhoE_face_graph_coboundary={report['rhoE_face_graph_coboundary']}")
    if report["dotd_response_norms"] is not None:
        print(f"dotd_response_norms={json.dumps(report['dotd_response_norms'], sort_keys=True)}")

    if failures:
        print("selected-source promotion FAIL")
        for failure in failures[:50]:
            print(f"- {failure}")
        if len(failures) > 50:
            print(f"- ... {len(failures) - 50} more failures")
        return 1

    print("selected-source promotion PASS")
    print("candidate may be used at the requested promotion level")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
