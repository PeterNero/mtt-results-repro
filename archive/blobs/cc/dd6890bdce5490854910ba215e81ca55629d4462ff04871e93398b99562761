"""Validate a selected visible Green-Schwarz source packet for q79/F,m=1.

The packet must do two things at once:

1. realize the exact visible gauge-curvature row derived by the previous
   requirement certificate;
2. carry selected-source evidence, not merely a copied coefficient row.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REQUIREMENT_CERT = ROOT / "certificates" / "time_oriented_m1_visible_green_schwarz_requirement_certificate.json"
SCHEMA = "TimeOrientedM1VisibleGreenSchwarzSource.v1"
REQUIREMENT_CERT_NAME = "time_oriented_m1_visible_green_schwarz_requirement_certificate.json"
SOURCE_KINDS = {
    "finite_HYM_Strominger_solve",
    "route_c_visible_solve",
    "typed_Cech_monad_transition_data",
}


class IncompleteData(ValueError):
    """Raised when the packet is deliberately open."""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, failures: list[str], message: str) -> None:
    if not condition:
        failures.append(message)


def requirement_data() -> dict[str, Any]:
    cert = load_json(REQUIREMENT_CERT)
    if cert.get("status") != "TIME_ORIENTED_M1_VISIBLE_GS_REQUIREMENT_DERIVED_SOURCE_OPEN":
        raise ValueError("visible Green-Schwarz requirement certificate is not in the expected state")
    return cert


def validate(packet: dict[str, Any]) -> tuple[int, list[str], dict[str, Any]]:
    if packet.get("status") == "OPEN":
        raise IncompleteData("visible Green-Schwarz source packet is OPEN")
    if packet.get("schema") != SCHEMA:
        raise ValueError(f"schema must be {SCHEMA}")

    req = requirement_data()
    required_row = req.get("derived_required_visible_row", {}).get("Tr_F_visible_squared")
    required_residual = req.get("derived_required_visible_row", {}).get("residual_if_supplied")
    known_rows = req.get("known_rows", {})

    failures: list[str] = []
    require(
        packet.get("requirement_certificate") == REQUIREMENT_CERT_NAME,
        failures,
        f"requirement_certificate must be {REQUIREMENT_CERT_NAME}",
    )
    require(packet.get("selected_by_mtt") is True, failures, "selected_by_mtt must be true")
    require(packet.get("same_branch_as_q79_m1") is True, failures, "same_branch_as_q79_m1 must be true")
    require(packet.get("fixture_only") is False, failures, "fixture_only must be false")
    require(
        packet.get("uses_observed_flavor_data") is False,
        failures,
        "uses_observed_flavor_data must be false",
    )
    require(
        packet.get("uses_benchmark_flavor_entries") is False,
        failures,
        "uses_benchmark_flavor_entries must be false",
    )

    rows = packet.get("curvature_rows")
    if not isinstance(rows, dict):
        raise IncompleteData("MISSING curvature_rows")
    require(
        rows.get("dH") == known_rows.get("dH"),
        failures,
        "curvature_rows.dH must match the requirement certificate",
    )
    require(
        rows.get("Tr_R_plus_squared") == known_rows.get("Tr_R_plus_squared"),
        failures,
        "curvature_rows.Tr_R_plus_squared must match the requirement certificate",
    )
    require(
        rows.get("Tr_F_visible_squared") == required_row,
        failures,
        "curvature_rows.Tr_F_visible_squared must equal the derived required visible row",
    )
    require(
        rows.get("residual") == required_residual,
        failures,
        "curvature_rows.residual must be zero as derived by the requirement certificate",
    )

    source = packet.get("visible_source_evidence")
    if not isinstance(source, dict):
        raise IncompleteData("MISSING visible_source_evidence")
    require(source.get("source_kind") in SOURCE_KINDS, failures, "visible_source_evidence.source_kind is not allowed")
    require(
        source.get("selected_visible_bundle_model") is True,
        failures,
        "selected visible bundle model must be supplied",
    )
    require(
        source.get("same_branch_q79_f_m1") is True,
        failures,
        "visible source must be on the q79/F,m=1 branch",
    )
    require(
        source.get("chern_weil_row_from_source") is True,
        failures,
        "Chern-Weil row must be derived from the selected visible source",
    )
    require(
        source.get("hym_or_route_c_residual_verified") is True,
        failures,
        "HYM/Route-C source residual must be verified",
    )
    require(
        isinstance(source.get("source_certificate"), str)
        and source.get("source_certificate", "").endswith(".json"),
        failures,
        "visible_source_evidence.source_certificate must name a source certificate",
    )

    report = {
        "required_row": required_row,
        "packet_row": rows.get("Tr_F_visible_squared"),
        "row_matches_requirement": rows.get("Tr_F_visible_squared") == required_row,
        "source_kind": source.get("source_kind"),
        "selected_visible_bundle_model": source.get("selected_visible_bundle_model"),
        "green_schwarz_source_verified": not failures,
    }
    return (0 if not failures else 1), failures, report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        packet = load_json(args.packet)
        code, failures, report = validate(packet)
    except IncompleteData as exc:
        print(str(exc))
        return 2
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID visible Green-Schwarz source packet: {exc}")
        return 1

    print(f"visible_gs_source_report={json.dumps(report, sort_keys=True)}")
    if failures:
        print("visible Green-Schwarz source FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("visible Green-Schwarz source PASS")
    print("selected visible source realizes the required q79/F,m=1 curvature row")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
