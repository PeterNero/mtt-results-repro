"""Audit the visible rank-two L2 integral lift source gap."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "analyze_visible_rank2_l2_integral_lift_source_gap.py"
CANDIDATE = REPO / "candidate_data" / "visible_rank2_l2_integral_lift_source_gap.candidate.json"
CERT = REPO / "certificates" / "visible_rank2_l2_integral_lift_source_gap_certificate.json"
PAPER = ROOT / "Visible_Rank2_L2_Integral_Lift_Source_Gap_v1.md"


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

    finite = cert.get("finite_indistinguishability", {})
    deck = cert.get("selected_finite_deck_limit", {})
    h1 = cert.get("existing_h1_packet", {})
    source = cert.get("sufficient_source_contract", {})
    routes = cert.get("route_status", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    original_report = h1.get("original_validation", {}).get("parsed_report") or {}
    promoted_report = h1.get("conditional_promoted_validation", {}).get("parsed_report") or {}

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status source gap",
            "PASS"
            if cert.get("status") == "VISIBLE_RANK2_L2_INTEGRAL_LIFT_REDUCED_TO_SOURCE_CERTIFICATE"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("finite_indistinguishability")
            == cert.get("finite_indistinguishability")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "finite no-go",
            "PASS"
            if finite.get("target_L_mod3_equals_swapped") is True
            and finite.get("target_L2_mod3_equals_swapped") is True
            and finite.get("target_m1_self_period_equals_swapped") is True
            and finite.get(
                "therefore_finite_mod3_data_cannot_select_ordered_integral_branch"
            )
            is True
            else "FAIL",
            str(finite),
        ),
        Gate(
            "finite deck not ordinary lift",
            "PASS"
            if deck.get("g3_g4_in_kernel_of_selected_finite_quotient") is True
            and deck.get("target_integral_c1_requires_g3_g4_degree") == -4
            and deck.get("selected_finite_gerbe_can_be_integral_L2_lift_by_itself")
            is False
            else "FAIL",
            str(deck),
        ),
        Gate(
            "unselected h1 packet algebra",
            "PASS"
            if h1.get("h1") == 8
            and original_report.get("h1") == 8
            and original_report.get("promotes_to_non_split_V_alpha_input") is False
            else "FAIL",
            str(original_report),
        ),
        Gate(
            "conditional source promotion",
            "PASS"
            if promoted_report.get("h1") == 8
            and promoted_report.get("selected_source_promotes") is True
            and promoted_report.get("promotes_to_non_split_V_alpha_input") is True
            and source.get("validator_would_promote_existing_h1_packet_if_source_supplied")
            is True
            else "FAIL",
            str({"promoted": promoted_report, "source": source}),
        ),
        Gate(
            "source contract",
            "PASS"
            if source.get("ordered_integral_c1_matrix_required", [])[0][1] == 2
            and source.get("ordered_integral_c1_matrix_required", [])[2][3] == -4
            and source.get("must_not_be_only_mod3_or_only_torsion") is True
            and source.get("must_select_or_eliminate_flat_pic0_torsion_character")
            is True
            else "FAIL",
            str(source),
        ),
        Gate(
            "route classification",
            "PASS"
            if routes.get("finite_qutrit_only_route", {}).get("status")
            == "NO_GO_FOR_BRANCH_SELECTION"
            and routes.get("integral_lift_route", {}).get("status")
            == "LIVE_SOURCE_CERTIFICATE_ONLY_GAP"
            and routes.get("gauduchon_wall_route", {}).get("status")
            == "LIVE_SOURCE_RATIO_OPEN"
            else "FAIL",
            str(routes),
        ),
        Gate(
            "closes source-gap reduction",
            "PASS"
            if closes.get("finite_mod3_qutrit_data_no_go_for_target_vs_swapped_integral_lift")
            is True
            and closes.get("selected_flat_gerbe_not_same_as_ordinary_integral_c1_lift")
            is True
            and closes.get("existing_h1_8_packet_has_no_remaining_algebraic_obstruction_after_source")
            is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if still_open.get(
                "selected_ordered_integral_Cech_or_automorphy_source_for_L2_2_minus4_0"
            )
            is True
            and still_open.get("same_source_D_E_dotD_Riesz_Green") is True
            and still_open.get("full_SM_closure") is True
            else "FAIL",
            str(still_open),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper records theorem",
            "PASS"
            if contains_all(
                paper,
                [
                    "finite q79/F orientation is real",
                    "ordered integral lift",
                    "E(g1,g2) =  2",
                    "E(g3,g4) = -4",
                    "E(g5,g6)",
                    "source certificate",
                    "Selected_Ordered_L2_Cech_Automorphy_Source_v1",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible rank-two L2 integral lift source gap audit")
    print("==================================================")
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
