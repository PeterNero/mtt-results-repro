"""Audit selected_i11tracemap_gaugetransportimport_or_dynamicreplaygap."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_i11tracemap_gaugetransportimport_or_dynamicreplaygap"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CURRENT = PACKET_DIR / "current_gauge_transport_import_trace_map_attempt.packet.json"
FUNCTIONAL = PACKET_DIR / "functional_phi_fin_trace_import_sublemma.packet.json"
WITNESS = PACKET_DIR / "conditional_transport_closed_dynamic_trace_map_witness.packet.json"
FRONTIER = PACKET_DIR / "remaining_transport_closed_dynamic_replay_frontier.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_I11TraceMap_GaugeTransportImport_or_DynamicReplayGap_v1.md"
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
    functional = load(FUNCTIONAL)
    witness = load(WITNESS)
    frontier = load(FRONTIER)
    current_result = load(CURRENT_RESULT)
    witness_result = load(WITNESS_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_I11TRACEMAP_GAUGETRANSPORT_IMPORTED_DYNAMIC_REPLAY_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "import theorem not proved")
    require(data["conditional_only"] is True, "candidate should be conditional")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(functional["proved"] is True, "functional trace import should be proved")
    require(functional["imported_closures"]["gauge_transported_phi_fin_trace"] is True, "gauge trace not imported")
    require(functional["not_imported_as_closed"]["alpha1_driver_verified"] is False, "alpha1 overpromoted")
    require(current["selected_minimizer_identifier"] is True, "functional minimizer identifier should close")
    require(current["finite_phi_fin_trace_operator"] is True, "functional Phi_fin operator should close")
    require(current["c1_response_coordinate_map"] is False, "C1 coordinates overpromoted")
    require(current["selected_normalization_boundary_clause"] is False, "boundary overpromoted")
    require(current["dynamic_c1_flags_verified"] is False, "dynamic flags overpromoted")
    require(current["finite_27_mode_validator_replay_closed"] is False, "finite replay overpromoted")
    require(current["free_axiom_patch_used"] is False, "free patch used")

    require(witness["conditional_only"] is True, "witness should be conditional")
    require(witness["selected_minimizer_identifier"] is True, "witness missing minimizer")
    require(witness["dynamic_c1_flags_verified"] is True, "witness missing dynamic flags")
    require(current_result["returncode"] == 1, "recorded current validator should fail")
    require(witness_result["returncode"] == 0, "recorded witness validator should pass")
    require(validator_returncode(CURRENT) == 1, "current validator should fail")
    require(validator_returncode(WITNESS) == 0, "witness validator should pass")

    require(frontier["closed_now"]["functional_selected_minimizer_trace"] is True, "frontier should close functional trace")
    require(frontier["still_open"]["transport_closed_finite_validator_replay"]["current_support"] is False, "transport replay overpromoted")
    require(frontier["still_open"]["selected_normalization_boundary_clause"]["boundary_closed"] is False, "boundary lost")
    require(cert["functional_trace_import_sublemma_proved"] is True, "cert should record functional import")
    require("functional selected trace = proved" in note, "note missing functional trace statement")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
