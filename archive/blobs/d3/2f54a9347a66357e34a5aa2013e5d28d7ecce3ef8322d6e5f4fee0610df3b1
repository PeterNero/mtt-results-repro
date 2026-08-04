"""Audit Bergman/HYM coefficient and heat-zeta radial dual attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_bergmanhymcoefficient_or_heatzetaradialoperator_dualattempt"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BERGMAN = PACKET_DIR / "bergman_hym_window_coefficient_attempt.packet.json"
HEAT = PACKET_DIR / "heat_zeta_radial_operator_proxy_attempt.packet.json"
DECISION = PACKET_DIR / "dual_route_decision_and_next_theorem.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_BergmanHYMCoefficient_or_HeatZetaRadialOperator_DualAttempt_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_BERGMANHYMCOEFFICIENT_OR_HEATZETARADIALOPERATOR_DUALATTEMPT_"
    "BERGMAN_WINDOW_SHARP_HEAT_PROXY_REJECTED_SOURCE_THEOREM_REQUIRED"
)
NEXT = "MTT_Selected_BergmanHYMCoefficientSourceRule_or_ExactRadialOperator_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    bergman = load(BERGMAN)
    heat = load(HEAT)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("bergman", bergman),
        ("heat", heat),
        ("decision", decision),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(decision["next_required_artifact"] == NEXT, "decision next")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    best_b = bergman["best_candidate"]
    require(best_b["name"] == "(2*theta_cutoff+1)/(CY_dim+End0_rank+trace_unit)", "best bergman")
    require(abs(best_b["k_value"] - 25 / 7) < 1e-15, "bergman k")
    require(best_b["relative_residual"] < 1e-7, "bergman residual")
    require(bergman["accepted_bergman_coefficient_source_count"] == 0, "bergman accepted")
    require(bergman["denominator_source_theorem_proved"] is False, "denominator overproved")
    require(bergman["exact_tau_H_equality_proved"] is False, "exact overproved")

    best_h = heat["best_candidate"]
    require(best_h["name"] == "4", "best heat")
    require(best_h["relative_residual"] > best_b["relative_residual"], "heat unexpectedly stronger")
    require(heat["accepted_heat_zeta_radial_source_count"] == 0, "heat accepted")
    require("flat theta-window Laplacian" in heat["why_rejected"][0], "heat rejection")

    require(decision["best_route_now"] == "Bergman/HYM finite coefficient source rule", "route")
    require(decision["accepted_source_rows_total"] == 0, "decision accepted")
    require(data["closure_decision"]["bergman_route_prioritized"] is True, "bergman priority")
    require(data["closure_decision"]["heat_proxy_rejected_as_final"] is True, "heat rejection")
    require(data["closure_decision"]["strict_tau_H_promoted"] is False, "tau overpromoted")
    require(data["closure_decision"]["strict_r_H_promoted"] is False, "r overpromoted")

    for phrase in [
        "BergmanHYMCoefficientAndHeatZetaDualAttemptTheorem",
        "25/7",
        "Accepted source rows: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: Bergman/HYM route gives the sharp 25/7 theorem target; "
        "flat heat/zeta proxy is rejected; no source row accepted."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
