"""Validate a selected HYM/Strominger operator-source packet.

This gate sits between the closed Fu-Yau/Strominger charge sector and the
selected matter-slot source gate.  It asks whether the selected background has
actually supplied the finite operator data D_E, dotD, Riesz/Green, and projector
retention needed downstream.

Exit codes:
  0: complete packet verifies the selected HYM/Strominger operator source;
  1: complete packet fails a selected-source/operator check;
  2: packet is explicitly open/incomplete.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCHEMA = "SelectedHYMOperatorSource.v1"
SOURCE_KIND = "finite_HYM_Strominger_solve"


class IncompleteData(ValueError):
    """Raised when a packet is still open."""


def resolve_path(value: Any, packet_path: Path, label: str) -> Path:
    if not isinstance(value, str) or not value:
        raise IncompleteData(f"MISSING {label}")
    raw = Path(value)
    candidates = [raw] if raw.is_absolute() else [packet_path.parent / raw, ROOT / raw]
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved.exists():
            return resolved
    raise IncompleteData(f"MISSING file for {label}: {value}")


def run_validator(script_name: str, path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / script_name), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "script": script_name,
        "path": str(path),
        "exit_code": proc.returncode,
        "stdout": proc.stdout,
        "pass": proc.returncode == 0,
    }


def require(condition: bool, failures: list[str], message: str) -> None:
    if not condition:
        failures.append(message)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_source(data: dict[str, Any], failures: list[str]) -> dict[str, Any]:
    source = data.get("source")
    if not isinstance(source, dict):
        raise IncompleteData("MISSING source")
    require(source.get("source_kind") == SOURCE_KIND, failures, f"source.source_kind must be {SOURCE_KIND}")
    require(source.get("selected_by_mtt") is True, failures, "source.selected_by_mtt must be true")
    require(source.get("fixture_only") is False, failures, "source.fixture_only must be false")
    require(
        isinstance(source.get("source_certificate"), str) and bool(source.get("source_certificate")),
        failures,
        "source.source_certificate is required",
    )
    require(
        source.get("uses_observed_flavor_inputs") is False,
        failures,
        "source must not use observed flavor inputs",
    )
    require(
        source.get("uses_benchmark_flavor_inputs") is False,
        failures,
        "source must not use benchmark flavor inputs",
    )
    return {
        "source_kind": source.get("source_kind"),
        "selected_by_mtt": source.get("selected_by_mtt"),
        "fixture_only": source.get("fixture_only"),
    }


def validate_background(
    data: dict[str, Any],
    packet_path: Path,
    failures: list[str],
) -> dict[str, Any]:
    background = data.get("background")
    if not isinstance(background, dict):
        raise IncompleteData("MISSING background")
    cert_report: dict[str, Any] = {}
    if isinstance(background.get("certificate_path"), str) and background.get("certificate_path"):
        cert_path = resolve_path(background.get("certificate_path"), packet_path, "background.certificate_path")
        cert = load_json(cert_path)
        cert_report = {
            "path": str(cert_path),
            "status": cert.get("status"),
            "strominger_selection_applies": cert.get("selection", {}).get("strominger_selection_applies"),
            "green_schwarz_bianchi_identity_verified": cert.get("geometry", {}).get(
                "green_schwarz_bianchi_identity_verified"
            ),
        }
        require(cert.get("status") == "CLOSED_CHARGE_SECTOR", failures, "background certificate must be CLOSED_CHARGE_SECTOR")
        require(
            cert.get("selection", {}).get("strominger_selection_applies") is True,
            failures,
            "background certificate must have strominger_selection_applies true",
        )
        require(
            cert.get("geometry", {}).get("green_schwarz_bianchi_identity_verified") is True,
            failures,
            "background certificate must verify Green-Schwarz Bianchi identity",
        )
    else:
        raise IncompleteData("MISSING background.certificate_path")

    require(
        background.get("fuyau_strominger_charge_sector_closed") is True,
        failures,
        "background.fuyau_strominger_charge_sector_closed must be true",
    )
    require(
        background.get("green_schwarz_bianchi_identity_verified") is True,
        failures,
        "background.green_schwarz_bianchi_identity_verified must be true",
    )
    require(
        background.get("strominger_selection_applies") is True,
        failures,
        "background.strominger_selection_applies must be true",
    )
    require(
        background.get("charge_sector_only") is False,
        failures,
        "background.charge_sector_only must be false for operator-source closure",
    )
    require(
        background.get("visible_sm_bundle_model_selected") is True,
        failures,
        "background.visible_sm_bundle_model_selected must be true",
    )
    require(
        background.get("matter_operator_source_constructed") is True,
        failures,
        "background.matter_operator_source_constructed must be true",
    )
    return {
        "fuyau_strominger_charge_sector_closed": background.get(
            "fuyau_strominger_charge_sector_closed"
        ),
        "charge_sector_only": background.get("charge_sector_only"),
        "visible_sm_bundle_model_selected": background.get("visible_sm_bundle_model_selected"),
        "matter_operator_source_constructed": background.get("matter_operator_source_constructed"),
        "certificate": cert_report,
    }


def validate_branch(data: dict[str, Any], failures: list[str]) -> dict[str, Any]:
    branch = data.get("branch")
    if not isinstance(branch, dict):
        raise IncompleteData("MISSING branch")
    require(branch.get("q") == 79, failures, "branch.q must be 79")
    require(branch.get("orientation") == "F", failures, "branch.orientation must be F")
    require(
        branch.get("retarded_q79_branch_selected") is True,
        failures,
        "branch.retarded_q79_branch_selected must be true",
    )
    require(
        branch.get("antiunitary_conjugate_retained") is True,
        failures,
        "branch.antiunitary_conjugate_retained must be true",
    )
    require(
        isinstance(branch.get("branch_packet_reference"), str)
        and bool(branch.get("branch_packet_reference")),
        failures,
        "branch.branch_packet_reference is required",
    )
    return {
        "q": branch.get("q"),
        "orientation": branch.get("orientation"),
        "retarded_q79_branch_selected": branch.get("retarded_q79_branch_selected"),
    }


def validate_operator_source(
    data: dict[str, Any],
    packet_path: Path,
    failures: list[str],
) -> dict[str, Any]:
    operator = data.get("operator_source")
    if not isinstance(operator, dict):
        raise IncompleteData("MISSING operator_source")

    route_c_path = resolve_path(
        operator.get("route_c_residual_packet"),
        packet_path,
        "operator_source.route_c_residual_packet",
    )
    promotion_path = resolve_path(
        operator.get("selected_source_promotion_packet"),
        packet_path,
        "operator_source.selected_source_promotion_packet",
    )
    route_c_result = run_validator("validate_iwasawa_route_c_residuals.py", route_c_path)
    promotion_result = run_validator("validate_iwasawa_selected_source_promotion.py", promotion_path)

    if not route_c_result["pass"]:
        failures.append(
            "Route C residual validator failed with exit "
            f"{route_c_result['exit_code']}"
        )
    if not promotion_result["pass"]:
        failures.append(
            "selected-source promotion validator failed with exit "
            f"{promotion_result['exit_code']}"
        )

    require(operator.get("same_branch_dotd") is True, failures, "operator_source.same_branch_dotd must be true")
    require(
        operator.get("selected_D_E_constructed") is True,
        failures,
        "operator_source.selected_D_E_constructed must be true",
    )
    require(
        operator.get("selected_dotD_constructed") is True,
        failures,
        "operator_source.selected_dotD_constructed must be true",
    )
    require(
        operator.get("selected_riesz_green_constructed") is True,
        failures,
        "operator_source.selected_riesz_green_constructed must be true",
    )
    require(
        operator.get("projector_retention_selected") is True,
        failures,
        "operator_source.projector_retention_selected must be true",
    )

    return {
        "same_branch_dotd": operator.get("same_branch_dotd"),
        "selected_D_E_constructed": operator.get("selected_D_E_constructed"),
        "selected_dotD_constructed": operator.get("selected_dotD_constructed"),
        "selected_riesz_green_constructed": operator.get("selected_riesz_green_constructed"),
        "projector_retention_selected": operator.get("projector_retention_selected"),
        "route_c_residual_validator": route_c_result,
        "selected_source_promotion_validator": promotion_result,
    }


def validate_packet(packet_path: Path, data: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    if data.get("status") == "OPEN":
        raise IncompleteData("selected HYM operator-source packet is OPEN")
    if data.get("schema") != SCHEMA:
        raise ValueError(f"schema must be {SCHEMA}")
    failures: list[str] = []
    report = {
        "schema": data.get("schema"),
        "source": validate_source(data, failures),
        "background": validate_background(data, packet_path, failures),
        "branch": validate_branch(data, failures),
        "operator_source": validate_operator_source(data, packet_path, failures),
    }
    report["selected_hym_operator_source_verified"] = not failures
    return failures, report


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_hym_operator_source.py <packet.json>")
        return 1

    packet_path = Path(argv[1]).resolve()
    try:
        data = json.loads(packet_path.read_text(encoding="utf-8"))
        failures, report = validate_packet(packet_path, data)
    except IncompleteData as exc:
        print(str(exc))
        return 2
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID selected HYM operator-source packet: {exc}")
        return 1

    print(f"hym_operator_source_validation_report={json.dumps(report, sort_keys=True)}")
    if failures:
        print("selected HYM operator-source validation FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("selected HYM operator-source validation PASS")
    print("selected Fu-Yau/HYM/Strominger source promotes to finite D_E/dotD operator data")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
