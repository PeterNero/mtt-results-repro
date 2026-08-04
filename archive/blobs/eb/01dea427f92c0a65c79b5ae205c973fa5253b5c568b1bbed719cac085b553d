"""Audit the visible rank-two L^2 cohomology source hunt."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "hunt_visible_rank2_l2_cohomology_source.py"
CANDIDATE = REPO / "candidate_data" / "visible_rank2_l2_cohomology_source_hunt.candidate.json"
CERT = REPO / "certificates" / "visible_rank2_l2_cohomology_source_hunt_certificate.json"
PAPER = ROOT / "Visible_Rank2_L2_Cohomology_Source_Hunt_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


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

    routes = cert.get("route_evaluation", {})
    calc = cert.get("calculation_results", {})
    closes = cert.get("what_this_closes", {})
    open_items = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    flux_hits = cert.get("flux_source_hits", {})
    target = cert.get("source_targets", {})
    vector_scan = (
        routes.get("R3_typed_monad_or_line_table_reuse", {})
        .get("evidence", {})
        .get("vector_scan", {})
    )

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status source hunt blocked",
            "PASS"
            if cert.get("status")
            == "VISIBLE_RANK2_L2_COHOMOLOGY_SOURCE_HUNT_BLOCKED_SELECTED_DATA_ABSENT"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("calculation_results") == cert.get("calculation_results")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "target is preferred L2",
            "PASS"
            if target.get("l_vector_abc") == [1, -2, 0]
            and target.get("l2_vector_abc") == [2, -4, 0]
            else "FAIL",
            str(target),
        ),
        Gate(
            "flux adjacent data found",
            "PASS"
            if flux_hits.get("flux_source_exists") is True
            and flux_hits.get("explicit_left_invariant_barpartial_E_section") is True
            and flux_hits.get("H1_X_L2_literal_present") is False
            else "FAIL",
            str(flux_hits),
        ),
        Gate(
            "direct L2 packet absent",
            "OPEN"
            if routes.get("R1_direct_selected_L2_cochain_packet", {}).get("status")
            == "BLOCKED_NOT_FOUND"
            and calc.get("selected_L2_cochain_packet_found") is False
            else "FAIL",
            str(routes.get("R1_direct_selected_L2_cochain_packet", {})),
        ),
        Gate(
            "flux A01 rejected for L2",
            "PASS"
            if routes.get("R2_flux_explicit_barpartial_E", {}).get("status")
            == "BLOCKED_WRONG_OBJECT_AND_LITERAL_A01_FAILS"
            and calc.get("external_flux_section_can_fill_L2") is False
            else "FAIL",
            str(routes.get("R2_flux_explicit_barpartial_E", {})),
        ),
        Gate(
            "monad reuse rejected for L2",
            "PASS"
            if routes.get("R3_typed_monad_or_line_table_reuse", {}).get("status")
            == "BLOCKED_TYPED_MAPS_AND_NO_L2_MATCH"
            and vector_scan.get("direct_target_matches") == []
            and calc.get("monad_line_or_typed_slot_matches_L2_vector") is False
            else "FAIL",
            str(vector_scan),
        ),
        Gate(
            "diagnostic h1 rejected",
            "PASS"
            if routes.get("R4_corrected_A01_or_diagnostic_h1", {}).get("status")
            == "BLOCKED_UNSELECTED_WRONG_OBJECT"
            and calc.get("diagnostic_h1_candidates_selected") is False
            else "FAIL",
            str(routes.get("R4_corrected_A01_or_diagnostic_h1", {})),
        ),
        Gate(
            "next construction named",
            "OPEN"
            if routes.get("R5_construct_selected_L2_from_geometry", {}).get("status")
            == "NEXT_REQUIRED_CONSTRUCTION"
            and "SelectedVisibleL2LineBundleCohomologyPacket.v1"
            in routes.get("R5_construct_selected_L2_from_geometry", {}).get(
                "required_packet", ""
            )
            else "FAIL",
            str(routes.get("R5_construct_selected_L2_from_geometry", {})),
        ),
        Gate(
            "closes shortcut hunt",
            "PASS"
            if closes.get("corpus_hunt_for_hidden_L2_packet") is True
            and closes.get("flux_A01_shortcut_rejected_for_L2") is True
            and closes.get("typed_monad_reuse_rejected_for_L2") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if open_items.get("construct_selected_L2_transition_or_Dolbeault_data")
            is True
            and open_items.get("compute_actual_h1_for_L_squared") is True
            and open_items.get("full_SM_closure") is True
            else "FAIL",
            str(open_items),
        ),
        Gate("guardrails", "PASS" if all(value is False for value in guardrails.values()) else "FAIL", str(guardrails)),
        Gate(
            "paper records source hunt",
            "PASS"
            if contains_all(
                paper,
                [
                    "SelectedVisibleL2LineBundleCohomologyPacket.v1",
                    "flux A01 does not fill L^2",
                    "typed monad data do not contain the L^2 packet",
                    "H^1(X,L^2)",
                    "closed non-exact eta",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible rank-two L2 cohomology source hunt audit")
    print("================================================")
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
