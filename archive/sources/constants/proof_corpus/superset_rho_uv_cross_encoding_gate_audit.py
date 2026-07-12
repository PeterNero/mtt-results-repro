"""Audit the superset rho_UV cross-encoding gate."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "superset_rho_uv_cross_encoding_gate_certificate.json"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def contains_all(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    return all(needle.lower() in lowered for needle in needles)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    sources = {key: Path(value) for key, value in cert["source_paths"].items()}
    text = {key: read(path) for key, path in sources.items()}
    routes = {item["id"]: item for item in cert["candidate_routes"]}
    verdict = cert["verdict"]

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "SUPERSET_RHO_UV_ROUTE_FORMULATED_NOT_NUMERICALLY_CLOSED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate("sources present", "PASS" if all(path.exists() for path in sources.values()) else "FAIL", str([str(path) for path in sources.values() if not path.exists()])),
        Gate(
            "proof note states rho target",
            "PASS"
            if contains_all(text["proof_note"], ["rho_UV := C_UV^2 / delta", "s_* = (60 rho_UV)^(1/6)"])
            else "FAIL",
            str(sources["proof_note"]),
        ),
        Gate(
            "scale extraction has same remaining ratio",
            "PASS"
            if contains_all(text["scale_extraction"], ["rho_UV := C_UV^2 / delta", "C_UV and delta open"])
            else "FAIL",
            str(sources["scale_extraction"]),
        ),
        Gate(
            "shared ledger supports cross-encoding discipline",
            "PASS"
            if contains_all(text["shared_knob_ledger"], ["selected MTT/MMT data", "encoding dictionary", "remaining open target-specific data"])
            else "FAIL",
            str(sources["shared_knob_ledger"]),
        ),
        Gate(
            "superset supplies harmonic ratio framework",
            "PASS"
            if contains_all(text["superset"], ["alpha_r^{-1}", "K", "zeta_r", "Only ratios"])
            else "FAIL",
            str(sources["superset"]),
        ),
        Gate(
            "theta supplies independent overlap normalization",
            "PASS"
            if contains_all(text["theta_twistor"], ["twistor", "overlap normalization", "Fubini", "I_2", "I_3"])
            else "FAIL",
            str(sources["theta_twistor"]),
        ),
        Gate(
            "C1 response remains primitive-open",
            "PASS"
            if contains_all(text["c1_response"], ["primitive contractions", "does not claim the numerical C1 matrices"])
            else "FAIL",
            str(sources["c1_response"]),
        ),
        Gate(
            "white-noise source leaves finite covariance model open",
            "PASS"
            if contains_all(text["white_noise"], ["finite-memory disturbance", "not proved here", "finite-memory model matters"])
            else "FAIL",
            str(sources["white_noise"]),
        ),
        Gate(
            "theta route not overclaimed",
            "PASS"
            if routes["theta_overlap_normalization"]["classification"] == "FORMULATED_NOT_CLOSED"
            else "FAIL",
            str(routes["theta_overlap_normalization"]),
        ),
        Gate(
            "superset route identified as best structural",
            "PASS"
            if routes["superset_harmonic_weight_ratio"]["classification"] == "BEST_STRUCTURAL_ROUTE_NOT_CLOSED"
            else "FAIL",
            str(routes["superset_harmonic_weight_ratio"]),
        ),
        Gate(
            "threshold delta forbidden",
            "PASS"
            if routes["threshold_delta_import"]["classification"] == "FORBIDDEN_SYMBOL_COLLISION"
            and verdict.get("threshold_delta_forbidden") is True
            else "FAIL",
            str(routes["threshold_delta_import"]),
        ),
        Gate(
            "numeric closure blocked",
            "PASS"
            if verdict.get("superset_route_formulated") is True
            and verdict.get("rho_uv_numerically_closed") is False
            and "U and D" in verdict.get("remaining_gate", "")
            else "FAIL",
            str(verdict),
        ),
    ]

    print("Superset rho_UV cross-encoding gate audit")
    print("==========================================")
    print()
    print(f"status={cert.get('status')}")
    print(f"remaining_gate={verdict.get('remaining_gate')}")
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
