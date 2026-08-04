"""Audit the selected Gauduchon wall radius gate."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "analyze_selected_gauduchon_wall_radius_gate.py"
CANDIDATE = REPO / "candidate_data" / "selected_gauduchon_wall_radius_gate.candidate.json"
CERT = REPO / "certificates" / "selected_gauduchon_wall_radius_gate_certificate.json"
PAPER = ROOT / "Selected_Gauduchon_Wall_Radius_Gate_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> int:
    proc = run([sys.executable, str(SCRIPT)])
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    paper = read(PAPER)

    source_clues = cert.get("source_clues", {})
    slope = cert.get("slope_radius_map", {})
    walls = cert.get("wall_dictionary", {})
    current = cert.get("current_source_status", {})
    routes = {route.get("id"): route for route in cert.get("route_evaluation", [])}
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status reduced",
            "PASS"
            if cert.get("status") == "GAUDUCHON_WALL_REDUCED_TO_RADIUS_RATIO_SOURCE_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("wall_dictionary") == cert.get("wall_dictionary")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "slope-radius map",
            "PASS"
            if slope.get("p1_over_p2") == "r2^2/r1^2"
            and slope.get("matches_split_no_go_p_vector") is True
            else "FAIL",
            str(slope),
        ),
        Gate(
            "target wall radius",
            "OPEN"
            if walls.get("target_wall", {}).get("equivalent_radius_ratio")
            == "r1:r2 = sqrt(2):1"
            and walls.get("target_wall", {}).get("selects_target_as_unique_negative")
            is True
            else "FAIL",
            str(walls.get("target_wall", {})),
        ),
        Gate(
            "symmetric source not enough",
            "OPEN"
            if walls.get("symmetric_source", {}).get("radius_condition") == "r1 = r2"
            and walls.get("symmetric_source", {}).get("selects_unique_branch") is False
            and current.get("rplus_equal_radius_assumption") == "r1 = r2 = R"
            else "FAIL",
            str({"walls": walls.get("symmetric_source", {}), "current": current}),
        ),
        Gate(
            "corpus leaves Iwasawa shape open",
            "OPEN"
            if source_clues.get("iwasawa_shape_modulus_open_in_flux_source") is True
            and source_clues.get("selection_source_iwasawa_fixes_r3_not_r1_over_r2")
            is True
            else "FAIL",
            str(source_clues),
        ),
        Gate(
            "bad shortcuts rejected",
            "PASS"
            if routes.get("derive_target_wall_from_existing_iwasawa_flux_packets", {}).get(
                "status"
            )
            == "BLOCKED"
            and routes.get("derive_target_wall_from_split_line_hym_primitivity", {}).get(
                "status"
            )
            == "REJECTED_AS_VISIBLE_SOURCE_SELECTOR"
            else "FAIL",
            str(routes),
        ),
        Gate(
            "live routes remain",
            "OPEN"
            if routes.get("construct_new_nonabelian_or_route_c_wall_source", {}).get(
                "status"
            )
            == "LIVE"
            and routes.get("integral_cech_de_lift_of_finite_qutrit_class", {}).get(
                "status"
            )
            == "LIVE"
            else "FAIL",
            str(routes),
        ),
        Gate(
            "closes radius reduction",
            "PASS"
            if closes.get("abstract_p_wall_translated_to_iwasawa_radii") is True
            and closes.get("target_wall_requires_r1_over_r2_sqrt2") is True
            and closes.get("current_equal_radius_sources_do_not_select_target_wall")
            is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if still_open.get("source_certified_r1_over_r2_sqrt2_wall") is True
            and still_open.get("integral_cech_or_de_lift_selecting_L_1_minus2_0")
            is True
            and still_open.get("same_source_D_E_dotD_Riesz_Green") is True
            else "FAIL",
            str(still_open),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_target_wall_selected") is False
            and guardrails.get("claims_L_branch_selected") is False
            and guardrails.get("claims_split_line_hym_source_reopened") is False
            and guardrails.get("uses_observed_flavor_data") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper records theorem",
            "PASS"
            if contains_all(
                paper,
                [
                    "p1:p2 = 1:2",
                    "r1:r2 = sqrt(2):1",
                    "r1 = r2",
                    "shape modulus",
                    "integral Cech/D_E lift",
                    "full SM closure",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Selected Gauduchon wall radius gate audit")
    print("=========================================")
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
