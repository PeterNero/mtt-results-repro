"""Audit selected H-angular/C1 metric search for tau_H."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hangularc1metricsearch_or_hweightedgalerkinpayload"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SEARCH = PACKET_DIR / "hangular_c1_metric_tauh_search.packet.json"
PAYLOAD = PACKET_DIR / "hweighted_galerkin_payload_contract.packet.json"
DECISION = PACKET_DIR / "angular_metric_search_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HAngularC1MetricSearch_or_HWeightedGalerkinPayload_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HANGULARC1METRICSEARCH_OR_HWEIGHTEDGALERKINPAYLOAD_"
    "ANGULAR_C1_NEARMISSES_REJECTED_HWEIGHTED_PAYLOAD_REQUIRED"
)
NEXT = "MTT_Selected_HWeightedGalerkinMetricTauHExport_or_DirectRadialOperator_v1"


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
    payload = load(PAYLOAD)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("search", search),
        ("payload", payload),
        ("decision", decision),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(decision["next_required_artifact"] == NEXT, "decision next")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    require(abs(search["selected_s_beta"]["value"] - 0.004701083905943647) < 1e-18, "s_beta")
    require(search["selected_s_beta"]["observed_higgs_or_beta_used"] is False, "observed beta")
    require(search["accepted_tau_H_source_count"] == 0, "search accepted")
    require(len(search["best_near_misses"]) == 16, "best near miss list")
    require(all(row["accepted_as_tau_H_source"] is False for row in search["best_near_misses"]), "overaccepted")

    required_rows = payload["required_rows"]
    for key in [
        "selected_zero_mode_bases",
        "H_weighted_metric_kernel",
        "primitive_three_by_three_H_contractions",
        "linear_response_matrices",
        "tau_H_export_rule",
        "exactness_error_certificate",
    ]:
        require(key in required_rows, f"payload missing {key}")
        require(required_rows[key]["accepted_now"] is False, f"payload overfilled {key}")

    require("controlled r_H or N_H" in payload["forbidden_sources"], "forbidden radial missing")
    require(decision["accepted_tau_H_source_count"] == 0, "decision accepted")
    require(decision["controlled_H_radial_used_as_input"] is False, "controlled H circularity")
    require(data["closure_decision"]["H_weighted_Galerkin_payload_contract_emitted"] is True, "payload contract")
    require(data["closure_decision"]["strict_r_H_promoted"] is False, "rH overpromoted")

    for phrase in [
        "HAngularC1MetricSearchAndPayloadContractTheorem",
        "Accepted H-angular/C1 source rows: `0`",
        "s_beta` fixes the H angular ray",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print("AUDIT_PASS: H-angular/C1 metric near misses rejected; H-weighted Galerkin payload contract emitted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
