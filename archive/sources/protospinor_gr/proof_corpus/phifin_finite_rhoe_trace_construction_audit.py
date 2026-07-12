from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "phifin_finite_rhoe_trace_construction_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    insertion = Path(cert["paper_insertion_written"]).read_text(encoding="utf-8")
    checks = cert["numeric_checks"]
    verdict = cert["verdict"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "PHIFIN_FINITE_RHOE_TRACE_CONSTRUCTED_FULL_PAYLOAD_OPEN",
        "unexpected Phi_fin finite rhoE trace status",
    )
    require(cert["theorem"]["proved"] is True, "finite rhoE theorem should be proved")
    require(verdict["finite_rhoE_trace_piece_constructed"] is True, "finite rhoE piece should close")
    require(verdict["identity_rhoE_smoke_retired_for_phi_fin"] is True, "identity smoke should be retired")
    require(verdict["phi_fin_full_selected_payload_emitted"] is False, "full payload must remain open")
    require(verdict["selected_matter_stress_coefficients_closed"] is False, "matter stress must remain open")
    require(verdict["selected_source_flags_may_be_set_true"] is False, "selected flags must not be set")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["still_open"].values()), "all remaining gates should remain open")

    tolerance = 1.0e-9
    for key in [
        "g1_unitary_residual",
        "g2_unitary_residual",
        "g1_order3_residual",
        "g2_order3_residual",
        "g3_identity_residual",
        "projective_commutator_residual",
    ]:
        require(checks[key] < tolerance, f"{key} too large")
    require(checks["nonidentity_norm_g1_minus_I"] > 1.0, "g1 should be nonidentity")
    require(checks["nonidentity_norm_g2_minus_I"] > 1.0, "g2 should be nonidentity")

    require(packet["partial_phi_fin"]["codomain_piece"] == "rank-3 Heisenberg/Weyl projective rho_E packet", "packet codomain changed")
    require("identity-smoke obstacle" in note, "note must mention identity-smoke closure")
    require("not the full selected `Phi_fin`" in insertion or "not the full selected `Phi_fin`" in note, "must preserve full-payload caveat")
    require("No observed masses" in insertion, "paper insertion must include no-target guardrail")
    require(all(guards.values()), "all guardrails must hold")

    print("AUDIT_PASS: Phi_fin finite rhoE trace constructed; full selected payload remains open")


if __name__ == "__main__":
    main()
