"""Audit H radial transport-map / dynamic Phi_fin C1 consumer frontier."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hradialtransportmap_or_dynamicphifinc1consumer"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TRANSPORT = PACKET_DIR / "d211_pi2_radial_transport_contract.packet.json"
COEFF = PACKET_DIR / "radial_transport_coefficient_isolation.packet.json"
CONSUMER = PACKET_DIR / "dynamic_phifinc1_consumer_retest_after_pi2.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HRadialTransportMap_or_DynamicPhiFinC1Consumer_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HRADIALTRANSPORTMAP_OR_DYNAMICPHIFINC1CONSUMER_"
    "PI4_TAU_ISOLATED_CONSUMER_OPEN"
)
NEXT = "MTT_Selected_TauHTransportCoefficientSource_or_UnpatchedPhiFinC1Consumer_v1"


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
    transport = load(TRANSPORT)
    coeff = load(COEFF)
    consumer = load(CONSUMER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("transport", transport),
        ("coeff", coeff),
        ("consumer", consumer),
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

    law = transport["candidate_transport_law"]
    require(law["law"] == "r_H = pi^4 * tau_H", "transport law")
    require(math.isclose(transport["required_values"]["tau_H_required"], 4.018017196377461, rel_tol=0, abs_tol=1e-12), "tau required")
    require(transport["accepted_radial_transport_map_count"] == 0, "transport overaccepted")
    require(transport["accepted_tau_H_source_count"] == 0, "tau overaccepted")

    require(coeff["accepted_tau_H_source_count"] == 0, "coeff overaccepted")
    require(coeff["tau_candidates"][0]["name"] == "tau_required", "tau candidate")
    require(coeff["tau_candidates"][1]["accepted_as_source"] is False, "logdet overaccepted")
    require(coeff["tau_candidates"][2]["accepted_as_source"] is False, "integer overaccepted")

    require(consumer["dynamic_values_ready"] is True, "dynamic values")
    require(consumer["patched_local_axiom_closure_available"] is True, "patched local axiom")
    require(consumer["unpatched_source_rule_derived"] is False, "unpatched overclaim")
    require(consumer["honest_galerkin_tables_exported"] is False, "galerkin overclaim")
    require(consumer["selected_dynamic_phi_fin_c1_payload_emitted"] is False, "payload overclaim")
    require(consumer["typed_HRG_consumer_map_emitted"] is False, "consumer overclaim")
    require(consumer["D211_pi2_clue_closes_consumer_map"] is False, "pi2 consumer overclaim")
    require(consumer["accepted_HRG_consumer_count"] == 0, "consumer count")

    decision = data["closure_decision"]
    require(decision["D211_pi2_transport_contract_built"] is True, "decision transport")
    require(decision["tau_H_required_isolated"] is True, "decision tau")
    require(decision["accepted_tau_H_source_count"] == 0, "decision tau source")
    require(decision["accepted_radial_transport_map_count"] == 0, "decision transport source")
    require(decision["typed_HRG_consumer_map_emitted"] is False, "decision consumer")
    require(decision["strict_r_H_promoted"] is False, "decision rH")
    require(decision["strict_N_H_promoted"] is False, "decision NH")

    for phrase in [
        "HRadialTransportCoefficientIsolationTheorem",
        "r_H = pi^4 * tau_H",
        "tau_H required",
        "selected_dynamic_phi_fin_c1_payload_emitted = false",
        "typed_HRG_consumer_map_emitted",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print("AUDIT_PASS: radial transport contract isolates tau_H; dynamic Phi_fin/C1 consumer remains open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
