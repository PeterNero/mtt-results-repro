"""Audit selected_i11tracemap_transportdotdimport_or_boundaryc1gap."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_i11tracemap_transportdotdimport_or_boundaryc1gap"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TRANSPORT_DOTD = PACKET_DIR / "transport_closed_dotd_trace_import_sublemma.packet.json"
CURRENT = PACKET_DIR / "current_transport_dotd_import_trace_map_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_boundary_c1_trace_map_witness.packet.json"
FRONTIER = PACKET_DIR / "remaining_boundary_c1_firstvariation_frontier.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_I11TraceMap_TransportDotDImport_or_BoundaryC1Gap_v1.md"
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
    transport_dotd = load(TRANSPORT_DOTD)
    current = load(CURRENT)
    witness = load(WITNESS)
    frontier = load(FRONTIER)
    current_result = load(CURRENT_RESULT)
    witness_result = load(WITNESS_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_I11TRACEMAP_TRANSPORT_DOTD_IMPORTED_BOUNDARY_C1_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "import theorem not proved")
    require(data["conditional_only"] is True, "candidate should be conditional")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(transport_dotd["proved"] is True, "transport/dotD sublemma should be proved")
    require(transport_dotd["transport_closed_finite_validator_replay"] is True, "transport replay should close")
    require(transport_dotd["dynamic_dotd_trace_binding_accepted"] is True, "dynamic dotD binding should close")
    require("primitive overlap contraction values" in transport_dotd["not_accepted_scope"], "scope should exclude primitive contractions")

    require(current["selected_minimizer_identifier"] is True, "minimizer should stay closed")
    require(current["finite_phi_fin_trace_operator"] is True, "Phi_fin trace should stay closed")
    require(current["transport_closed_finite_validator_replay"] is True, "transport replay not imported")
    require(current["dynamic_dotd_trace_binding_imported"] is True, "dotD binding not imported")
    require(current["c1_response_coordinate_map"] is False, "C1 coordinates overpromoted")
    require(current["selected_normalization_boundary_clause"] is False, "boundary overpromoted")
    require(current["dynamic_c1_flags_verified"] is False, "dynamic C1 flags overpromoted")
    require(current["physical_first_variation_identity"] is False, "physical first variation overpromoted")
    require(current["free_axiom_patch_used"] is False, "free patch used")

    require(witness["conditional_only"] is True, "witness should be conditional")
    require(witness["dynamic_c1_flags_verified"] is True, "witness missing dynamic flags")
    require(current_result["returncode"] == 1, "recorded current validator should fail")
    require(witness_result["returncode"] == 0, "recorded witness validator should pass")
    require(validator_returncode(CURRENT) == 1, "current validator should fail")
    require(validator_returncode(WITNESS) == 0, "witness validator should pass")

    require(frontier["closed_now"]["transport_closed_finite_validator_replay"] is True, "frontier should close transport replay")
    require(frontier["closed_now"]["dynamic_dotd_trace_binding"] is True, "frontier should close dotD binding")
    require(frontier["still_open"]["physical_boundary_cancellation"]["physical_verified"] is False, "boundary overpromoted")
    require(frontier["still_open"]["physical_first_variation_identity"]["current_support"] == "formal finite-dimensional projection only", "first variation support mismatch")
    require(cert["transport_dotd_import_sublemma_proved"] is True, "cert should record sublemma")
    require("dynamic dotD trace binding accepted   = True" in note, "note missing dotD statement")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
