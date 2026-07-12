"""Audit the visible rank-two L^2 branch-selection reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "reduce_visible_rank2_l2_branch_selection.py"
CANDIDATE = REPO / "candidate_data" / "visible_rank2_l2_branch_selection_reduction.candidate.json"
CERT = REPO / "certificates" / "visible_rank2_l2_branch_selection_reduction_certificate.json"
PAPER = ROOT / "Visible_Rank2_L2_Branch_Selection_Reduction_v1.md"


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

    selectors = cert.get("selector_evaluation", {})
    slope = selectors.get("slope_chamber", {})
    time = selectors.get("time_oriented_q79_F", {})
    s3 = selectors.get("s3_twisted_orientation", {})
    flat = selectors.get("flat_character", {})
    flux = selectors.get("abelian_alpha1_flux_row", {})
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
            if cert.get("status")
            == "VISIBLE_RANK2_L2_BRANCH_SELECTION_REDUCED_TO_ORIENTATION_SOURCE"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("selector_evaluation") == cert.get("selector_evaluation")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "topology and h1 not unique",
            "OPEN"
            if selectors.get("topology_c2", {}).get("selects_unique_branch") is False
            and selectors.get("h1_dimension", {}).get("selects_unique_branch") is False
            and selectors.get("h1_dimension", {}).get("h1_values") == [8]
            else "FAIL",
            str(selectors),
        ),
        Gate(
            "slope chamber reduces only to pairs",
            "OPEN"
            if slope.get("generic_chamber_selects_unique_branch") is False
            and slope.get("generic_chamber_selects_two_negative_branches") is True
            and slope.get("symmetric_shared_base_chamber_conditional_survivors")
            == [[-2, 1, 0], [1, -2, 0]]
            else "FAIL",
            str(slope),
        ),
        Gate(
            "q79/F real but unmapped",
            "OPEN"
            if time.get("q79_F_selected") is True
            and time.get("maps_q79_F_to_L_branch") is False
            and s3.get("q79_F_orientation_in_twisted_sector") is True
            and s3.get("maps_to_visible_L2_line_bundle") is False
            else "FAIL",
            str({"time": time, "s3": s3}),
        ),
        Gate(
            "flux row rejected as selector",
            "PASS"
            if flux.get("supports_alpha1_row") is True
            and flux.get("split_source_retired_as_selector") is True
            and flux.get("maps_to_non_split_L_branch") is False
            else "FAIL",
            str(flux),
        ),
        Gate(
            "flat character still open",
            "OPEN"
            if flat.get("flat_Pic0_characters_preserve_c1") is True
            and flat.get("hidden_flat_or_torsion_twist_ruled_out_by_current_data")
            is False
            else "FAIL",
            str(flat),
        ),
        Gate(
            "closes exact selector reduction",
            "PASS"
            if closes.get("c2_and_h1_do_not_select_unique_branch") is True
            and closes.get("slope_sign_alone_does_not_select_unique_branch") is True
            and closes.get("q79_F_orientation_not_yet_mapped_to_base_L_branch")
            is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if still_open.get("selected_base_factor_ordering_or_branch_orientation_source")
            is True
            and still_open.get("map_q79_F_or_other_orientation_datum_to_L_equals_1_minus2_0")
            is True
            and still_open.get("promote_L2_packet_to_SELECTED_DATA") is True
            else "FAIL",
            str(still_open),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_unique_L_branch_selected") is False
            and guardrails.get("claims_q79_F_selects_L_branch") is False
            and guardrails.get("claims_flat_character_eliminated") is False
            and guardrails.get("uses_observed_flavor_data") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper records reduction",
            "PASS"
            if contains_all(
                paper,
                [
                    "four branches",
                    "two negative-slope branches",
                    "q79/F",
                    "not mapped to the base line",
                    "Selected_Pullback_L2_Branch_Orientation_Source",
                    "flat Pic0",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible rank-two L2 branch-selection reduction audit")
    print("====================================================")
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
