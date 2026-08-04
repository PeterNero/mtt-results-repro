"""Audit H scalar functional on finite projected HYM algebra."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hscalarfunctionalonfiniteprojectedhymalgebra_or_halfdensitysourcerule"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FUNCTIONAL = PACKET_DIR / "h_scalar_finite_trace_functional.packet.json"
VALUE = PACKET_DIR / "tauh_rh_source_value_execution.packet.json"
COMPARISON = PACKET_DIR / "downstream_tauh_comparison_certificate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_hlambda_or_fullsm_closure_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HScalarFunctionalOnFiniteProjectedHYMAlgebra_or_HalfDensitySourceRule_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HSCALARFUNCTIONALONFINITEPROJECTEDHYMALGEBRA_OR_HALFDENSITYSOURCERULE_"
    "FINITE_TRACE_HSCALAR_SOURCE_ROW_EMITTED"
)
NEXT = "MTT_Selected_HLambdaThresholdPayload_from_FiniteHScalarSource_or_FullSMClosureAudit_v1"


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
    functional = load(FUNCTIONAL)
    value = load(VALUE)
    comparison = load(COMPARISON)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("functional", functional),
        ("value", value),
        ("comparison", comparison),
        ("next", next_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(next_packet["next_required_artifact"] == NEXT, "next packet")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    require(functional["accepted_as_H_scalar_source_rule"] is True, "functional source rule")
    for field in ["base_denominator7", "angular_term", "halfdensity_term", "interaction_term"]:
        require(functional["source_ownership"][field]["accepted"] is True, f"{field} not accepted")
    require(functional["operations_used"]["star_N_exact"] is True, "star exact")
    require(functional["operations_used"]["exp_N_exact"] is True, "exp exact")
    require(functional["operations_used"]["Delta_N_Green_N_exact"] is True, "green exact")

    require(value["accepted_H_scalar_source_rows"] == 1, "accepted H scalar count")
    require(value["strict_tau_H_promoted"] is True, "tau not promoted")
    require(value["strict_r_H_promoted"] is True, "rH not promoted")
    require(abs(value["source_values"]["k_H_A_N"] - 3.5795828145988784) < 1e-15, "k value")
    require(abs(value["source_values"]["tau_H_A_N"] - 4.018017196377423) < 1e-15, "tau value")

    require(comparison["comparison_only"] is True, "comparison boundary")
    require(comparison["comparison_did_not_select_source"] is True, "comparison selector")
    require(comparison["tau_residual_below_replay_floor"] is True, "replay floor")
    require(abs(comparison["tau_H_absolute_residual"]) < 5e-14, "tau residual")

    decision = data["closure_decision"]
    require(decision["H_scalar_functional_on_A_N_closed"] is True, "decision H functional")
    require(decision["half_density_interaction_source_rule_closed"] is True, "decision halfdensity")
    require(decision["accepted_H_scalar_source_rows"] == 1, "decision row count")
    require(decision["strict_tau_H_promoted"] is True, "decision tau")
    require(decision["strict_r_H_promoted"] is True, "decision rH")
    require(decision["lambda_H_threshold_payload_closed"] is False, "lambda overclosed")
    require(decision["full_no_knob_closed"] is False, "full no-knob overclosed")

    for phrase in [
        "HScalarFunctionalOnFiniteProjectedHYMAlgebraTheorem",
        "Accepted H scalar source rows: `1`",
        "Strict `tau_H` source promoted: `true`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: H scalar finite trace source row emitted; "
        "tau_H/r_H promoted; lambda threshold payload remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
