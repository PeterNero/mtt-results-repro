"""Audit the canonical theta-ladder attempt for the remaining Yoneda scalar."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "attempt_valpha_remaining_yoneda_scalar.py"
CERT = ROOT / "certificates" / "valpha_remaining_yoneda_scalar_attempt_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "valpha_remaining_yoneda_scalar_attempt.candidate.json"
PACKET = (
    ROOT
    / "candidate_data"
    / "valpha_remaining_yoneda_scalar"
    / "canonical_theta_ladder_scalar.candidate.json"
)
PAPER = CORPUS / "VAlpha_Remaining_Yoneda_Scalar_Attempt_v1.md"


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
        cwd=ROOT,
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
    packet = load(PACKET)
    paper = read(PAPER)

    embedded = cert.get("canonical_theta_ladder_packet", {})
    closed = cert.get("closed_by_this_attempt", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    basis_map = embedded.get("basis_map", {})
    target_vector = embedded.get("target_vector", [])

    expected_status = "VALPHA_REMAINING_YONEDA_SCALAR_CANONICAL_NONZERO_SELECTION_OPEN"
    expected_target = [1, 0, 0, 0, 0, 0, 0, 0, 0]

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1200]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("packet exists", "PASS" if PACKET.exists() else "FAIL", PACKET),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status expected",
            "PASS" if cert.get("status") == expected_status else "FAIL",
            cert.get("status"),
        ),
        Gate("candidate mirrors cert", "PASS" if candidate == cert else "FAIL", candidate.get("status")),
        Gate("packet mirrors embedded", "PASS" if packet == embedded else "FAIL", packet.get("status")),
        Gate(
            "basis dimensions",
            "PASS"
            if len(embedded.get("source_basis", [])) == 8
            and len(embedded.get("target_basis", [])) == 9
            and embedded.get("hom_generator_space") == "H^0(1,1,0)"
            else "FAIL",
            {
                "source": len(embedded.get("source_basis", [])),
                "target": len(embedded.get("target_basis", [])),
            },
        ),
        Gate(
            "canonical ladder map",
            "PASS"
            if basis_map.get("theta_plus_0_tensor_eta_minus_0")
            == "theta_plus3_0_tensor_eta_minus3_0"
            and basis_map.get("theta_plus_0_tensor_eta_minus_3") is None
            and basis_map.get("theta_plus_1_tensor_eta_minus_3") is None
            else "FAIL",
            basis_map,
        ),
        Gate(
            "selected vector maps nonzero",
            "PASS"
            if embedded.get("selected_ext_vector") == [1, 0, 0, 0, 0, 0, 0, 0]
            and target_vector == expected_target
            and embedded.get("target_vector_nonzero") is True
            and embedded.get("distinguished_scalar_value") == 1
            else "FAIL",
            target_vector,
        ),
        Gate(
            "conditional closure only",
            "PASS"
            if closed.get("canonical_ladder_scalar_computed") is True
            and closed.get("canonical_ladder_scalar_nonzero") is True
            and closed.get("selected_ext_label_not_in_ladder_kernel") is True
            and closed.get("remaining_branch_obstruction_would_close_if_ladder_selected") is True
            else "FAIL",
            closed,
        ),
        Gate(
            "selected-source proof still open",
            "OPEN"
            if still_open.get("prove_raw_appell_humbert_cech_multiplication_matches_ladder") is True
            and still_open.get("prove_mtt_selects_canonical_theta_ladder_basis") is True
            and still_open.get("promote_scalar_nonzero_to_selected_source_theorem") is True
            and still_open.get("full_SM_closure") is True
            else "FAIL",
            still_open,
        ),
        Gate(
            "guardrails",
            "PASS" if guardrails and all(value is False for value in guardrails.values()) else "FAIL",
            guardrails,
        ),
        Gate(
            "paper records conditional scalar",
            "PASS"
            if contains_all(
                paper,
                [
                    "VAlpha Remaining Yoneda Scalar Attempt",
                    "canonical theta-ladder basis",
                    "target component",
                    "raw Appell-Humbert/Cech multiplication data",
                    "not yet promoted to a selected theorem",
                    "does not prove full stability",
                    "full SM closure",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("V_alpha remaining Yoneda scalar attempt audit")
    print("============================================")
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:<{width}}  {gate.status:<{status_width}}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        print("\nFailures")
        print("--------")
        for failure in failures:
            print(f"- {failure.label}: {failure.detail}")
        return 1

    print("\nResult: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
