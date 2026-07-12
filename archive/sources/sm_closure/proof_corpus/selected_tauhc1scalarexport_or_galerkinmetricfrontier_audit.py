"""Audit finite C1 scalar export attempt for tau_H."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_tauhc1scalarexport_or_galerkinmetricfrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SCALARS = PACKET_DIR / "finite_c1_scalar_inventory.packet.json"
SEARCH = PACKET_DIR / "tauh_c1_expression_search.packet.json"
FRONTIER = PACKET_DIR / "galerkin_metric_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TauHC1ScalarExport_or_GalerkinMetricFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_TAUHC1SCALAREXPORT_OR_GALERKINMETRICFRONTIER_"
    "C1_SCALARS_REJECTED_GALERKIN_METRIC_REQUIRED"
)
NEXT = "MTT_Selected_GalerkinMetricTauHExport_or_HWeightedC1KernelValues_v1"


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
    scalars = load(SCALARS)
    search = load(SEARCH)
    frontier = load(FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("scalars", scalars),
        ("search", search),
        ("frontier", frontier),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(frontier["next_required_artifact"] == NEXT, "frontier next")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    require(scalars["scalars"]["b_norm_sq"] == 24.0, "b norm")
    require(scalars["scalars"]["total_four_sector_norm_sq"] == 12.0, "total norm")
    require(search["accepted_tau_H_source_count"] == 0, "search accepted")
    require(len(search["best_near_misses"]) == 12, "best list")
    require(all(row["accepted_as_tau_H_source"] is False for row in search["best_near_misses"]), "near miss overaccepted")

    decision = data["closure_decision"]
    require(decision["C1_scalar_only_tau_H_export_rejected"] is True, "C1 rejection")
    require(decision["honest_Galerkin_metric_payload_required"] is True, "metric frontier")
    require(decision["strict_r_H_promoted"] is False, "rH overpromoted")

    for key in [
        "zero_mode_bases",
        "primitive_three_by_three_contraction_terms",
        "linear_response_matrices",
        "tau_H_export_rule",
    ]:
        require(key in frontier["remaining_required_payload"], f"missing payload key {key}")

    for phrase in [
        "TauHC1ScalarRejectionAndGalerkinMetricFrontierTheorem",
        "Accepted C1-only source rows: `0`",
        "H-weighted Galerkin/metric data",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print("AUDIT_PASS: finite C1 scalars reject tau_H source export; Galerkin metric payload is the next frontier.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
