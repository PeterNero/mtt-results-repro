from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_first_correction_search_galerkin_import_certificate.json"
STATUS = "ROUTEC_FIRST_CORRECTION_SEARCH_GALERKIN_IMPORTED_DIAGNOSTIC_SPLITTER_VALUES_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_Correction_Source_Emission_or_Selected_Galerkin_Values_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "first correction/Galerkin import theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["diagnostic_checks"].values()), "all diagnostic checks should pass")
    require(all(cert["galerkin_checks"].values()), "all Galerkin checks should pass")
    require(all(cert["open_gate_checks"].values()), "all open-gate checks should pass")
    require(all(cert["still_open_checks"].values()), "all still-open checks should pass")
    require(cert["verdict"]["diagnostic_splitter_found"] is True, "diagnostic splitter should be found")
    require(cert["verdict"]["diagnostic_candidate_count"] > 0, "candidate count should be positive")
    require(cert["verdict"]["mass_split_traceless_positive"] is True, "mass split should be positive")
    require(cert["verdict"]["ckm_commutator_norm_sq"] > 0, "CKM commutator should be positive")
    require(cert["verdict"]["pmns_commutator_norm_sq"] > 0, "PMNS commutator should be positive")
    require(abs(cert["verdict"]["cp_odd_trace_commutator_cubed_imag"]) > 0, "CP odd invariant nonzero")
    require(cert["verdict"]["selected_correction_promoted"] is False, "diagnostic must not promote")
    require(
        cert["verdict"]["honest_galerkin_selected_values_emit_correction"] is False,
        "honest Galerkin must remain values-open",
    )
    require(cert["verdict"]["observed_flavor_data_used"] is False, "observed flavor data must not be used")
    require(cert["verdict"]["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    lane_a = packet["parallel_lanes"]["lane_A_qutrit_weyl_correction_search"]
    lane_b = packet["parallel_lanes"]["lane_B_galerkin_replay"]
    require(lane_a["selected_by_mtt"] is False, "lane A must remain unselected")
    require(lane_b["selected_correction_matrices_emitted"] is False, "lane B must not emit selected matrices")
    require("not promoted as selected MTT data" in note, "note must state non-promotion")
    require("diagnostic only" in note, "note must state formal-lift boundary")

    print("AUDIT_PASS: diagnostic correction splitter imported; selected correction values remain open")


if __name__ == "__main__":
    main()
