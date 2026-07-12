"""Audit the Bergman/HYM next-correction superset attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_bergmanhymnextcorrection_or_exactradialoperator_supersetattempt"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SEARCH = PACKET_DIR / "source_native_correction_candidates.packet.json"
SELECTED = PACKET_DIR / "selected_halfdensity_interaction_candidate.packet.json"
EXACTNESS = PACKET_DIR / "numerical_exactness_certificate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_theorem_or_operator_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_BergmanHYMNextCorrection_or_ExactRadialOperator_SupersetAttempt_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_BERGMANHYMNEXTCORRECTION_OR_EXACTRADIALOPERATOR_SUPERSETATTEMPT_"
    "HALFDENSITY_INTERACTION_NUMERICALLY_CLOSE_SOURCE_THEOREM_REQUIRED"
)
NEXT = "MTT_Selected_BergmanHYMHalfDensityInteractionSourceRule_or_AnalyticRadialOperator_v1"


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
    search = load(SEARCH)
    selected = load(SELECTED)
    exactness = load(EXACTNESS)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("search", search),
        ("selected", selected),
        ("exactness", exactness),
        ("next", next_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(next_packet["next_required_artifact"] == NEXT, "next packet")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["target_residual_used_for_diagnostic_ranking"] is True, "diagnostic ranking not recorded")

    best = search["best_candidate"]
    require(
        best["name"] == "sqrt(CY_dim)*s_beta + log_skew_2/2^CY_dim - s_beta*exp_skew_1/2",
        "unexpected best candidate",
    )
    require(search["accepted_strict_source_rows"] == 0, "search source overclaim")
    require(search["conditional_source_candidates"] == 1, "conditional candidate")

    require(selected["accepted_as_strict_source"] is False, "selected overpromoted")
    require(selected["conditional_if_source_rule_proved"] is True, "conditional witness missing")
    require(selected["components"]["base_denominator7"] == 25 / 7, "base coefficient")
    require(abs(selected["components"]["k_error_against_comparison_target"]) < 2e-9, "k error too large")

    require(exactness["tau_error_below_solver_residual_floor"] is True, "solver floor certificate")
    require(exactness["tau_error_below_metric_replay_residual_floor"] is True, "metric floor certificate")
    require(exactness["strict_exactness_closed"] is False, "strict exactness overclosed")
    require(abs(exactness["tau_H_absolute_residual"]) < 5e-14, "tau residual")
    require(exactness["tau_H_relative_residual"] < 1e-14, "relative tau residual")

    decision = data["closure_decision"]
    require(decision["source_native_correction_candidate_found"] is True, "source candidate not found")
    require(decision["tau_error_below_selected_galerkin_floor"] is True, "floor decision")
    require(decision["analytic_source_rule_proved"] is False, "analytic overproof")
    require(decision["accepted_source_rows_total"] == 0, "accepted source rows")

    for phrase in [
        "BergmanHYMHalfDensityInteractionSupersetAttemptTheorem",
        "sqrt(CY_dim)*s_beta",
        "below the selected Galerkin replay residual",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: half-density interaction correction reaches the Galerkin floor; "
        "analytic source-rule derivation remains required."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
