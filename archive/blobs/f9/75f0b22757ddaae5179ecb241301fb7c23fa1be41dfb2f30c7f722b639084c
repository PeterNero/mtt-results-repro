"""Audit tau_H coefficient source routes / one-parameter reparam."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_tauhtransportcoefficientsource_or_unpatchedphifinc1consumer"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTES = PACKET_DIR / "tauh_source_route_evaluation.packet.json"
REPARAM = PACKET_DIR / "source_normalized_oneparameter_reparam_ledger.packet.json"
NEXT_PACKET = PACKET_DIR / "next_unpatched_or_galerkin_clause_after_tauh.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TauHTransportCoefficientSource_or_UnpatchedPhiFinC1Consumer_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_TAUHTRANSPORTCOEFFICIENTSOURCE_OR_UNPATCHEDPHIFINC1CONSUMER_"
    "TAUH_ROUTES_EXECUTED_SOURCE_OPEN_ONEPARAM_REPARAM_READY"
)
NEXT = "MTT_Selected_UnpatchedPhiFinC1SourceRule_or_HonestGalerkinTauHExport_v1"


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
    routes = load(ROUTES)
    reparam = load(REPARAM)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("routes", routes),
        ("reparam", reparam),
        ("next", next_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    require(math.isclose(routes["tau_H_required"], 4.018017196377461, rel_tol=0, abs_tol=1e-12), "tau required")
    require(routes["accepted_tau_H_source_count"] == 0, "routes accepted count")
    for item in routes["routes"]:
        require(item["accepted_as_tau_H_source"] is False, f"route overaccepted {item['route']}")
    require(routes["radial_predictions"]["tau_H_4_relative_r_residual"] > 0.004, "tau 4 residual")
    require(routes["radial_predictions"]["minus_logdet_D211_relative_r_residual"] > 0.0003, "logdet residual")

    require(reparam["new_parameterization"]["parameter_count"] == 1, "parameter count")
    require(reparam["strict_no_knob_upgrade"]["tau_H_source_selected"] is False, "tau overselected")
    require(reparam["strict_no_knob_upgrade"]["strict_no_knob_closed"] is False, "strict overclosed")

    require(next_packet["next_required_artifact"] == NEXT, "next packet artifact")
    require("pi^4 transport scale tied to D_211/pi^2 clue" in next_packet["closed_here"], "closed pi4")
    require(any("derive tau_H" in item for item in next_packet["still_open"]), "tau still open")

    decision = data["closure_decision"]
    require(decision["tau_H_source_routes_evaluated"] is True, "decision routes")
    require(decision["accepted_tau_H_source_count"] == 0, "decision tau count")
    require(decision["integer_tau_H_4_rejected"] is True, "decision int")
    require(decision["minus_logdet_D211_rejected"] is True, "decision logdet")
    require(decision["one_parameter_H_reparametrized_as_pi4_tauH"] is True, "decision reparam")
    require(decision["H_parameter_count_preserved"] == 1, "decision count")
    require(decision["strict_r_H_promoted"] is False, "decision rH")

    for phrase in [
        "TauHSourceRouteAndOneParameterReparamTheorem",
        "r_H = pi^4 * tau_H",
        "parameter count: 1",
        "tau_H = -logdet(D_211)",
        "Both are diagnostics only",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print("AUDIT_PASS: tau_H source routes rejected; one-parameter H reparametrization is ready.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
