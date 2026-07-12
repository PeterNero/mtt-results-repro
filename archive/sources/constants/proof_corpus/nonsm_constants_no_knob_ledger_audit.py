"""Audit the initial no-knob ledger for non-SM constants."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "nonsm_constants_no_knob_ledger_certificate.json"
PAPER = ROOT / "NonSM_Constants_No_Knob_Ledger_v1.md"

Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
THETA_IV = Q79 / "proof_corpus" / "Theta_Closure_in_Modal_Triplet_Theory_IV__Gravity_and_Cosmology_from_the_Closure_Scale.md"
EXECUTION_I = Q79 / "proof_corpus" / "Execution_of_Modal_Triplet_Theory_I__Gauge__Axion__and_Threshold_Sectors_v2.md"
SHARED_LEDGER = Q79 / "proof_corpus" / "Shared_Knob_Cross_Encoding_Ledger_for_MTT_MMT_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    return all(needle.lower() in lowered for needle in needles)


def target(cert: dict[str, Any], target_id: str) -> dict[str, Any]:
    for item in cert.get("initial_targets", []):
        if item.get("id") == target_id:
            return item
    return {}


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    theta_iv = read(THETA_IV)
    execution_i = read(EXECUTION_I)
    shared_ledger = read(SHARED_LEDGER)
    targets = {item.get("id"): item.get("status") for item in cert.get("initial_targets", [])}
    discipline = cert.get("discipline", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "NONSM_CONSTANTS_NO_KNOB_LEDGER_FORMULATED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "source corpus present",
            "PASS"
            if THETA_IV.exists() and EXECUTION_I.exists() and SHARED_LEDGER.exists()
            else "FAIL",
            str(Q79),
        ),
        Gate(
            "no-knob discipline",
            "PASS" if all(discipline.values()) else "FAIL",
            str(discipline),
        ),
        Gate(
            "status taxonomy",
            "PASS"
            if set(cert.get("claim_statuses", []))
            == {
                "CLOSED",
                "CONDITIONAL",
                "STRUCTURAL",
                "OPEN",
                "FORBIDDEN_AS_UNIT_CONVENTION",
            }
            else "FAIL",
            str(cert.get("claim_statuses", [])),
        ),
        Gate(
            "unit conventions protected",
            "PASS"
            if target(cert, "unit_conventions_c_hbar_kB").get("status")
            == "FORBIDDEN_AS_UNIT_CONVENTION"
            and contains_all(paper, ["c, hbar, k_B", "not prediction targets"])
            else "FAIL",
            str(target(cert, "unit_conventions_c_hbar_kB")),
        ),
        Gate(
            "theta IV tensor bound source",
            "PASS"
            if contains_all(
                theta_iv,
                [
                    "mu_\\Theta",
                    "5~\\mathrm{TeV}",
                    "Lambda_\\Theta",
                    "lesssim",
                    "10^{-30}",
                    "falsifi",
                ],
            )
            and target(cert, "theta_tensor_ratio_bound").get("status") == "CONDITIONAL"
            else "FAIL",
            str(THETA_IV),
        ),
        Gate(
            "theta IV Newton structure source",
            "PASS"
            if contains_all(
                theta_iv,
                [
                    "Vol}(X_{\\mathrm{int}})",
                    "31.8",
                    "G_{10}",
                    "does not attempt to compute",
                ],
            )
            and target(cert, "theta_newton_constant_structure").get("status") == "STRUCTURAL"
            else "FAIL",
            str(target(cert, "theta_newton_constant_structure")),
        ),
        Gate(
            "execution I axion source",
            "PASS"
            if contains_all(
                execution_i,
                [
                    "axion normalizations",
                    "decay constants",
                    "Kähler moduli",
                    "threshold",
                ],
            )
            and target(cert, "execution_i_axion_decay_ratios").get("status") == "STRUCTURAL"
            else "FAIL",
            str(EXECUTION_I),
        ),
        Gate(
            "shared-ledger discipline inherited",
            "PASS"
            if contains_all(
                shared_ledger,
                [
                    "selected MTT/MMT data",
                    "encoding dictionary",
                    "theory-specific observable",
                    "forbidden workflow",
                ],
            )
            else "FAIL",
            str(SHARED_LEDGER),
        ),
        Gate(
            "open cosmology not overclaimed",
            "PASS"
            if targets.get("cosmological_constant_dark_energy") == "OPEN"
            and targets.get("hubble_constant_H0") == "OPEN"
            else "FAIL",
            str(targets),
        ),
        Gate(
            "first executable program",
            "PASS"
            if len(cert.get("first_executable_program", [])) == 4
            and "tensor bound" in cert.get("first_executable_program", [])[0]
            else "FAIL",
            str(cert.get("first_executable_program", [])),
        ),
        Gate(
            "paper records program",
            "PASS"
            if contains_all(
                paper,
                [
                    "Theta IV gives the cleanest current non-SM candidate",
                    "Newton Constant",
                    "Axion Decay Constants",
                    "Late-Time Dark Energy",
                    "First Program",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("ledger_ready") is True
            and verdict.get("closed_new_absolute_constants") is False
            and "Theta IV" in verdict.get("strongest_non_sm_candidate", "")
            else "FAIL",
            str(verdict),
        ),
    ]

    print("Non-SM constants no-knob ledger audit")
    print("=====================================")
    print()
    print(f"target_statuses={targets}")
    print()

    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
