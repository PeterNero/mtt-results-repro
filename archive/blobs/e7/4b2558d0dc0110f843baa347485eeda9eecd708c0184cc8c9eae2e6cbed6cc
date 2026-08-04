"""Audit the common-rescaling large-volume repair for Execution I."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "execution_i_large_volume_repair_certificate.json"
PAPER = ROOT / "Execution_I_Large_Volume_Repair_v1.md"


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


def approx_equal(left: float, right: float, rel: float = 1e-12, abs_tol: float = 1e-12) -> bool:
    return abs(left - right) <= max(abs_tol, rel * max(abs(left), abs(right), 1e-300))


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def threshold_direction(taus: list[float]) -> list[float]:
    logs = [math.log(tau) for tau in taus]
    avg = mean(logs)
    return [value - avg for value in logs]


def main() -> None:
    cert = load_json(CERT)
    source_path = Path(cert["source"])
    source = read(source_path)
    paper = read(PAPER)
    base = cert["base_inputs"]
    verdict = cert["verdict"]

    t = [float(base["t1"]), float(base["t2"]), float(base["t3"])]
    taus = [float(base["tau1"]), float(base["tau2"]), float(base["tau3"])]
    base_direction = threshold_direction(taus)
    failures = []
    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "LARGE_VOLUME_RATIO_REPAIR_CERTIFIED_WITH_NORMALIZATION_COST"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "source permits normalization rescaling",
            "PASS"
            if contains_all(
                source,
                [
                    "Different normalization conventions correspond to rescalings",
                    "do not affect ratios or Tier",
                    "Vol}(X_6)}{g_{10}^2}",
                ],
            )
            else "FAIL",
            str(source_path),
        ),
    ]

    for item in cert["example_repairs"]:
        s = float(item["s"])
        scaled_t = [s * value for value in t]
        scaled_tau = [s * s * value for value in taus]
        scaled_volume = (s**3) * float(base["volume"])
        scaled_direction = threshold_direction(scaled_tau)
        required_g10 = s ** 1.5
        gates.extend(
            [
                Gate(
                    f"s={s:g} min_t",
                    "PASS" if approx_equal(min(scaled_t), float(item["min_t"])) else "FAIL",
                    f"{min(scaled_t):.16g}",
                ),
                Gate(
                    f"s={s:g} min_tau",
                    "PASS" if approx_equal(min(scaled_tau), float(item["min_tau"])) else "FAIL",
                    f"{min(scaled_tau):.16g}",
                ),
                Gate(
                    f"s={s:g} volume",
                    "PASS" if approx_equal(scaled_volume, float(item["volume"])) else "FAIL",
                    f"{scaled_volume:.16g}",
                ),
                Gate(
                    f"s={s:g} threshold invariant",
                    "PASS"
                    if all(approx_equal(a, b, abs_tol=1e-11) for a, b in zip(base_direction, scaled_direction))
                    else "FAIL",
                    str(scaled_direction),
                ),
                Gate(
                    f"s={s:g} g10 cost",
                    "PASS" if approx_equal(required_g10, float(item["g10_required_for_fixed_K"])) else "FAIL",
                    f"{required_g10:.16g}",
                ),
            ]
        )

    gates.extend(
        [
            Gate(
                "no absolute overclaim",
                "PASS"
                if verdict.get("repair_algebra_certified") is True
                and verdict.get("ratio_observables_preserved") is True
                and verdict.get("full_absolute_normalization_closed") is False
                else "FAIL",
                str(verdict),
            ),
            Gate(
                "paper records normalization cost",
                "PASS"
                if contains_all(
                    paper,
                    [
                        "g_10 -> s^(3/2) g_10",
                        "not a new absolute prediction",
                        "keep absolute constants behind the normalization gate",
                    ],
                )
                else "FAIL",
                str(PAPER),
            ),
        ]
    )

    print("Execution I large-volume repair audit")
    print("=====================================")
    print()
    print(f"base_threshold_direction={base_direction}")
    print()

    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
