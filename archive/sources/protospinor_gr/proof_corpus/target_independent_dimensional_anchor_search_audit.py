from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "target_independent_dimensional_anchor_search_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    routes = cert["route_table"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "DIMENSIONAL_ANCHOR_SEARCH_EXHAUSTED_PACKET_GATE_READY",
        "unexpected dimensional anchor search status",
    )
    require(all(cert["closed_inputs"].values()), "all dimensional anchor search inputs must be ready")
    require(cert["verdict"]["current_corpus_closes_alpha_phys"] is False, "alpha_phys must not close here")
    require(cert["verdict"]["best_route"] == "m_theory_modal_gap_planck_anchor", "best route changed")
    require(
        routes["m_theory_modal_gap_planck_anchor"]["classification"] == "BEST_STRUCTURAL_ROUTE_PACKET_REQUIRED",
        "M-theory route classification changed",
    )
    require(routes["theta_matching_scale"]["classification"] == "REJECTED_AS_NO_KNOB_ANCHOR", "Theta route must be rejected")
    require(routes["observed_target_backsolve"]["classification"] == "FORBIDDEN", "backsolve must be forbidden")
    require(routes["unit_convention"]["classification"] == "FORBIDDEN_AS_PHYSICAL_PREDICTION", "unit convention must be forbidden")

    require(packet["packet"] == "SelectedDimensionalAnchorPacket", "packet schema changed")
    require(packet["status"] == "TEMPLATE_UNFILLED", "packet must remain unfilled")
    require(packet["source_certification"]["selected_by_mtt"] is False, "template must not preselect a source")
    require(packet["map_to_alpha_phys"]["alpha_phys_value"] is None, "template must not prefill alpha")

    require(guards["claims_alpha_phys_closed_now"] is False, "must not claim alpha closure")
    require(guards["claims_physical_Newton_or_Planck_now"] is False, "must not claim Newton/Planck")
    require(guards["uses_target_backsolve"] is False, "must not backsolve")
    require(guards["uses_Theta_5TeV_as_prediction"] is False, "must not use TeV calibration")
    require(guards["uses_unit_convention_as_prediction"] is False, "must not use unit convention")

    require("alpha_phys is not numerically closed" in note, "note must state nonclosure")
    require("candidate_data/selected_dimensional_anchor_packet.template.json" in note, "note must point to packet")
    print("AUDIT_PASS: dimensional anchor search exhausted; packet gate ready for any future alpha_phys closure claim")


if __name__ == "__main__":
    main()
