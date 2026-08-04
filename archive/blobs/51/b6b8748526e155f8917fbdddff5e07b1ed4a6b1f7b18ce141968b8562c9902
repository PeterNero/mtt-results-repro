from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "sector_zeromode_source_payload_stationary_promotion_certificate.json"
STATUS = "SECTOR_ZEROMODE_STATIONARY_RHO_S_PROMOTED_DOTD_ALPHA1_AND_ROUTING_OPEN"
NEXT = "MTT_Selected_dotD_alpha1_TransportDerivative_and_Driver_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim full closure")
    require(all(cert["checks"].values()), "all checks should pass")
    require(packet["theorem"]["proved"] is True, "theorem should be proved")
    require(packet["proof_chain"]["target_fitting_used"] is False, "target fitting must be excluded")
    require(packet["what_closes_now"]["validator_ready_sector_rho_s_packet"] is True, "rho_s packet not promoted")
    require(packet["what_closes_now"]["raw_untransported_packet_not_promoted"] is True, "raw packet must not promote")
    require(all(packet["what_remains_open"].values()), "open flags should remain open")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    slots = packet["stationary_sector_packet"]["promoted_sector_slots"]
    require(slots["H"]["rank"] == 1, "H rank should be one")
    for sector in ["Q", "u", "d", "L", "e", "N"]:
        require(slots[sector]["rank"] == 3, f"{sector} rank should be three")
        require(slots[sector]["stationary_rho_s_promoted"] is True, f"{sector} stationary rho_s not promoted")
        require(slots[sector]["source_verified_by_transport_conjugation"] is True, f"{sector} source not transport verified")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "P_s^sel = U P_s^model U^-1" in note, "note missing essentials")
    print("AUDIT_PASS: stationary sector rho_s promoted; dotD alpha1 and routing remain open")


if __name__ == "__main__":
    main()
