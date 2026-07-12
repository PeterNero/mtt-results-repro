"""Audit the Execution I axion decay-constant ratio claim."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "execution_i_axion_ratio_certificate.json"
PAPER = ROOT / "Execution_I_Axion_Ratio_No_Knob_Certificate_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def contains_all(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    return all(needle.lower() in lowered for needle in needles)


def approx_equal(left: float, right: float, rel: float = 1e-12) -> bool:
    return abs(left - right) <= rel * max(abs(left), abs(right), 1e-300)


def inverse_ratio(value: float) -> float:
    return 1.0 / value


def main() -> None:
    cert = load_json(CERT)
    source_path = Path(cert["source"])
    source = read(source_path)
    paper = read(PAPER)
    selected = cert["selected_inputs"]
    computed = cert["computed_ratios"]
    warning = cert["warning"]
    verdict = cert["verdict"]

    zeta2 = float(selected["zeta2_over_zeta1"])
    zeta3 = float(selected["zeta3_over_zeta1"])
    dzeta3 = float(selected["zeta3_over_zeta1_uncertainty"])
    ratios = {
        "f2_over_f1": inverse_ratio(zeta2),
        "f3_over_f1": inverse_ratio(zeta3),
        "f3_over_f1_low_from_zeta3_plus_uncertainty": inverse_ratio(zeta3 + dzeta3),
        "f3_over_f1_high_from_zeta3_minus_uncertainty": inverse_ratio(zeta3 - dzeta3),
    }

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "AXION_RATIO_CERTIFIED_WITH_EFT_CONTROL_WARNING"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "source present",
            "PASS" if source_path.exists() else "FAIL",
            str(source_path),
        ),
        Gate(
            "source has ratio map",
            "PASS"
            if contains_all(
                source,
                [
                    "zeta_2}{\\zeta_1} = 1",
                    "zeta_3}{\\zeta_1} = 0.229",
                    "tau_2}{\\tau_1}",
                    "tau_3}{\\tau_1}",
                    "f_a \\;\\propto\\; \\frac{1}{\\tau_a}",
                ],
            )
            else "FAIL",
            "Execution I zeta/tau/f_a equations",
        ),
        Gate(
            "numeric f2/f1",
            "PASS" if approx_equal(ratios["f2_over_f1"], computed["f2_over_f1"]) else "FAIL",
            f"{ratios['f2_over_f1']:.16g}",
        ),
        Gate(
            "numeric f3/f1",
            "PASS" if approx_equal(ratios["f3_over_f1"], computed["f3_over_f1"]) else "FAIL",
            f"{ratios['f3_over_f1']:.16g}",
        ),
        Gate(
            "uncertainty lower",
            "PASS"
            if approx_equal(
                ratios["f3_over_f1_low_from_zeta3_plus_uncertainty"],
                computed["f3_over_f1_low_from_zeta3_plus_uncertainty"],
            )
            else "FAIL",
            f"{ratios['f3_over_f1_low_from_zeta3_plus_uncertainty']:.16g}",
        ),
        Gate(
            "uncertainty upper",
            "PASS"
            if approx_equal(
                ratios["f3_over_f1_high_from_zeta3_minus_uncertainty"],
                computed["f3_over_f1_high_from_zeta3_minus_uncertainty"],
            )
            else "FAIL",
            f"{ratios['f3_over_f1_high_from_zeta3_minus_uncertainty']:.16g}",
        ),
        Gate(
            "absolute f_a not claimed",
            "PASS"
            if "absolute axion decay constants" in cert.get("not_claimed", [])
            and verdict.get("absolute_decay_constants_closed") is False
            else "FAIL",
            str(cert.get("not_claimed", [])),
        ),
        Gate(
            "EFT warning recorded",
            "PASS"
            if contains_all(
                warning.get("eft_control_issue", ""),
                ["t_a >> 1", "0.94", "not certified"],
            )
            and verdict.get("eft_control_certified") is False
            else "FAIL",
            str(warning),
        ),
        Gate(
            "paper states caveat",
            "PASS"
            if contains_all(
                paper,
                [
                    "ratio algebra is usable",
                    "large-volume control remains open",
                    "t_1 = t_2 ~= 0.94",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Execution I axion ratio audit")
    print("=============================")
    print()
    for key, value in ratios.items():
        print(f"{key}={value:.16g}")
    print()

    width = max(len(gate.label) for gate in gates)
    failures = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
