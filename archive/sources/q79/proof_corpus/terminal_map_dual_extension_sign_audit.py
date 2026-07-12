"""Audit the terminal-map dual extension sign theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "prove_terminal_map_dual_extension_sign.py"
CERT = REPO / "certificates" / "terminal_map_dual_extension_sign_certificate.json"
CANDIDATE = REPO / "candidate_data" / "terminal_map_dual_extension_sign.candidate.json"
PAPER = ROOT / "Terminal_Map_Dual_Extension_Sign_Theorem_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: object


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def run_script() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> int:
    proc = run_script()
    cert = load(CERT)
    candidate = load(CANDIDATE)
    paper = read(PAPER)

    duality = cert.get("terminal_map_duality", {})
    binding = cert.get("rank2_extension_binding", {})
    matrix = cert.get("ordered_base_matrix_binding", {})
    closes = cert.get("what_this_closes", {})
    not_closed = cert.get("what_this_does_not_close", {})
    guardrails = cert.get("guardrails", {})
    remaining = cert.get("remaining_packet", {})

    expected_matrix = [
        [0, 2, 0, 0, 0, 0],
        [-2, 0, 0, 0, 0, 0],
        [0, 0, 0, -4, 0, 0],
        [0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status proved selector open",
            "PASS"
            if cert.get("status") == "TERMINAL_MAP_DUAL_EXTENSION_SIGN_PROVED_SELECTOR_OPEN"
            else "FAIL",
            cert.get("status"),
        ),
        Gate(
            "candidate mirrors cert",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("terminal_map_duality") == duality
            else "FAIL",
            candidate.get("status"),
        ),
        Gate(
            "terminal duality",
            "PASS"
            if duality.get("computed_L3_minus_K2") == [1, -2, 0]
            and duality.get("printed_terminal_g3_type_K2_minus_L3") == [-1, 2, 0]
            and duality.get("dual_of_printed_g3_type") == [1, -2, 0]
            and duality.get("physical_L_is_dual_of_printed_g3_terminal_map_type") is True
            and duality.get("physical_L_squared") == [2, -4, 0]
            else "FAIL",
            duality,
        ),
        Gate(
            "rank2 extension convention",
            "PASS"
            if binding.get("sequence") == "0 -> L -> V_alpha -> L^{-1} -> 0"
            and binding.get("formula_c2") == "c2(V_alpha)=-l^2"
            and binding.get("physical_L_in_rank2_candidate_list") is True
            else "FAIL",
            binding,
        ),
        Gate(
            "ordered matrix bound",
            "PASS"
            if matrix.get("L") == [1, -2, 0]
            and matrix.get("L_squared") == [2, -4, 0]
            and matrix.get("matrix_order_g1_to_g6") == expected_matrix
            and matrix.get("pullback_matrix_matches") is True
            and matrix.get("appell_humbert_matrix_matches") is True
            and matrix.get("central_shared_circle_degree_zero") is True
            else "FAIL",
            matrix,
        ),
        Gate(
            "closes only sign/order",
            "PASS"
            if closes.get("terminal_g3_dual_sign_convention") is True
            and closes.get("rank2_extension_physical_L_is_L3_minus_K2_not_printed_Hom_type")
            is True
            and closes.get("target_L2_matrix_order_binding_conditional_on_terminal_g3") is True
            and not_closed.get("actual_terminal_map_source_selector") is True
            and not_closed.get("selected_pullback_representative") is True
            else "FAIL",
            {"closes": closes, "not_closed": not_closed},
        ),
        Gate(
            "remaining packet reduced",
            "PASS"
            if remaining.get("name") == "Selected_Terminal_Map_Source_Principle.v1"
            and len(remaining.get("now_reduced_to", [])) == 3
            else "FAIL",
            remaining,
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails and all(value is False for value in guardrails.values())
            else "FAIL",
            guardrails,
        ),
        Gate(
            "paper records theorem and guardrail",
            "PASS"
            if contains_all(
                paper,
                [
                    "physical L is the dual of the printed g3 terminal map type",
                    "L=L3-K2=(1,-2,0)",
                    "L^2=(2,-4,0)",
                    "does not prove that MTT selects g3",
                    "Selected_Terminal_Map_Source_Principle.v1",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("Terminal-map dual extension sign audit")
    print("======================================")
    width = max(len(gate.label) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
