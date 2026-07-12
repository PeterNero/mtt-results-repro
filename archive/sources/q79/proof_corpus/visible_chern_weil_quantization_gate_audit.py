"""Audit the visible Chern-Weil quantization gate."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "analyze_visible_chern_weil_quantization_gate.py"
CANDIDATE = REPO / "candidate_data" / "visible_chern_weil_quantization_gate.candidate.json"
CERT = REPO / "certificates" / "visible_chern_weil_quantization_gate_certificate.json"
PAPER = ROOT / "Visible_Chern_Weil_Quantization_Gate_v1.md"


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
    split = cert.get("row_normalization_split", {})
    gate = cert.get("period_quantization_gate", {})
    flux = cert.get("existing_flux_row_consistency", {})
    calc = cert.get("calculation_results", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status reduced to quantization gate",
            "PASS"
            if cert.get("status")
            == "VISIBLE_CHERN_WEIL_QUANTIZATION_REDUCED_TO_PERIOD_SOURCE_SELECTION_OPEN"
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
            "absorbed/unabsorbed split recorded",
            "PASS"
            if split.get("alpha_prime_over_4_absorbed") is True
            and split.get("absorbed_visible_alpha1_coefficient")
            == "8*r3^2/(r1^2*r2^2) + 4*r3^2"
            and split.get("restored_unabsorbed_bianchi_component")
            == "8*r3^2/(r1^2*r2^2) + (16/alpha_prime)*r3^2"
            else "FAIL",
            str(split),
        ),
        Gate(
            "period gate blocks integrality claim",
            "OPEN"
            if gate.get("integrality_proved_now") is False
            and "selected alpha_1 period normalization" in gate.get("minimal_missing_inputs", [])
            and "selected trace convention for Tr_F" in gate.get("minimal_missing_inputs", [])
            else "FAIL",
            str(gate),
        ),
        Gate(
            "existing flux row only conditional",
            "OPEN"
            if flux.get("conditional_integer_label_if_period_unit_is_2pi_squared") == 8
            and flux.get("conditional_integer_label_if_unit_is_8pi_squared") == 4
            and flux.get("usable_as_visible_source_now") is False
            else "FAIL",
            str(flux),
        ),
        Gate(
            "calculation scoped",
            "PASS"
            if calc.get("no_quantization_contradiction_found") is True
            and calc.get("integral_visible_bundle_or_sheaf_constructed") is False
            and closes.get("no_current_integrality_contradiction") is True
            else "FAIL",
            str({"calc": calc, "closes": closes}),
        ),
        Gate(
            "remaining source data open",
            "OPEN"
            if still_open.get("selected_visible_integral_Chern_character_or_K_theory_class") is True
            and still_open.get("HYM_or_Route_C_residual") is True
            and still_open.get("same_source_D_E_dotD_Riesz_Green") is True
            else "FAIL",
            str(still_open),
        ),
        Gate("guardrails", "PASS" if all(value is False for value in guardrails.values()) else "FAIL", str(guardrails)),
        Gate(
            "paper records exact scope",
            "PASS"
            if contains_all(
                paper,
                [
                    "absorbed Green-Schwarz normalization",
                    "unabsorbed Chern-Weil normalization",
                    "period normalization",
                    "not a selected visible bundle",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible Chern-Weil quantization gate audit")
    print("==========================================")
    width = max(len(gate_item.label) for gate_item in gates)
    status_width = max(len(gate_item.status) for gate_item in gates)
    failures: list[Gate] = []
    for gate_item in gates:
        print(f"{gate_item.label:{width}s}  {gate_item.status:{status_width}s}  {gate_item.detail}")
        if gate_item.status == "FAIL":
            failures.append(gate_item)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
