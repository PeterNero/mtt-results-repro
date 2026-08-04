"""Audit selected_i11_sourcepromotion_backimport_or_boundaryfirstvariation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_i11_sourcepromotion_backimport_or_boundaryfirstvariation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CURRENT = PACKET_DIR / "current_i11_sourcepromotion_backimport_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_boundary_firstvariation_witness.packet.json"
FRONTIER = PACKET_DIR / "remaining_boundary_firstvariation_source_frontier.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_i11_trace_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_i11_trace_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_I11_SourcePromotionBackimport_or_BoundaryFirstVariation_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_i11_trace_map.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validator_returncode(path: Path) -> int:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return proc.returncode


def main() -> int:
    data = load(DATA)
    current = load(CURRENT)
    witness = load(WITNESS)
    frontier = load(FRONTIER)
    current_result = load(CURRENT_RESULT)
    witness_result = load(WITNESS_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_I11_SOURCEPROMOTION_BACKIMPORT_BUILT_BOUNDARY_FIRSTVARIATION_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "backimport theorem not proved")
    require(data["conditional_only"] is True, "candidate should be conditional")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(current["same_branch"] is True, "current should be same branch")
    require(current["selected_minimizer_identifier"] is True, "selected minimizer not imported")
    require(current["finite_phi_fin_trace_operator"] is True, "finite Phi_fin trace not imported")
    require(current["c1_response_coordinate_map"] is True, "C1 coordinate chart not imported")
    require(current["selected_normalization_boundary_clause"] is False, "current overclosed boundary")
    require(current["dynamic_c1_flags_verified"] is False, "current overclosed dynamic flags")
    require(len(current["attached_certificate_evidence"]) >= 6, "current evidence too short")

    require(witness["selected_normalization_boundary_clause"] is True, "witness boundary missing")
    require(witness["dynamic_c1_flags_verified"] is True, "witness dynamic flags missing")
    require(witness["conditional_only"] is True, "witness should be conditional")
    require(len(witness["attached_certificate_evidence"]) >= 7, "witness evidence too short")

    require(current_result["returncode"] == 1, "recorded current validator should fail")
    require(witness_result["returncode"] == 0, "recorded witness validator should pass")
    require(validator_returncode(CURRENT) == 1, "current validator should still fail")
    require(validator_returncode(WITNESS) == 0, "witness validator should pass")

    require(frontier["closed_now"]["c1_response_coordinate_chart_imported"] is True, "frontier missing C1 chart import")
    require(frontier["closed_now"]["transport_dotd_trace_binding_imported"] is True, "frontier missing dotD import")
    require(frontier["closed_now"]["normalization_compatibility_proved"] is True, "frontier missing normalization")
    require("physical_first_variation_identity" in frontier["remaining_physical_fields"], "frontier missing first variation")
    require("physical_boundary_cancellation" in frontier["remaining_physical_fields"], "frontier missing boundary")
    require("same_source_RZ_RX_bselected_emission" in frontier["remaining_physical_fields"], "frontier missing source emission")
    require(frontier["superset_strategy"]["uses_observed_constants"] is False, "frontier uses observed constants")

    require(cert["current_i11_attempt_rejected"] is True, "cert missing current rejection")
    require(cert["conditional_i11_witness_passes"] is True, "cert missing witness pass")
    require(cert["boundary_firstvariation_source_frontier_identified"] is True, "cert missing frontier")
    require("What remains is physical, not numerical" in note, "note missing physical frontier")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
