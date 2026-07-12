"""Audit PEW gauge-action normalization source packet or direct-K certificate payload."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_pewgaugeactionnormalizationsourcepacket_or_directkcertificatepayload"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_PACKET = PACKET_DIR / "pew_gauge_action_source_payload.packet.json"
DIRECT_K_CERT = PACKET_DIR / "direct_k_certificate_payload.packet.json"
CROSSUSE_PACKET = PACKET_DIR / "nonhiggs_crossuse_payload.packet.json"
NEXT_PACKET = PACKET_DIR / "next_payload_after_pew_source_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PEWGaugeActionNormalizationSourcePacket_or_DirectKCertificatePayload_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
STATUS = "MTT_SELECTED_PEWGAUGEACTIONNORMALIZATIONSOURCEPACKET_OR_DIRECTKCERTIFICATEPAYLOAD_PAYLOAD_CONTRACT_LOCKED_VALUES_OPEN"
NEXT = "MTT_Selected_FirstPEWGaugeActionNormalizationValue_or_DirectKCertificateRun_v1"


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
    source = load(SOURCE_PACKET)
    direct = load(DIRECT_K_CERT)
    cross = load(CROSSUSE_PACKET)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [("candidate", data), ("source", source), ("direct", direct), ("cross", cross), ("next", next_packet), ("cert", cert)]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(next_packet["next_required_artifact"] == NEXT, "next packet")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["payload_contract_locked"] is True, "contract")
    require(data["strict_P_EW_source_theorem_closed"] is False, "PEW overclaim")
    require(data["direct_K_threshold_Omega_H_lambda_closed"] is False, "K overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    decision = data["closure_decision"]
    require(decision["source_required_field_count"] == 8, "field count")
    require(decision["source_filled_field_count"] == 0, "filled fields")
    require(decision["accepted_strict_P_EW_source_rows"] == 0, "PEW rows")
    require(decision["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "K rows")
    require(decision["best_A_EW_expression_formula"] == "8*Delta_G12/pi^2", "best formula")
    require(decision["physical_gauge_action_anchor_closed"] is False, "physical anchor")
    require(decision["matching_scale_closed"] is False, "mu match")
    require(decision["RG_scheme_closed"] is False, "RG scheme")
    require(decision["threshold_operator_or_torsion_finite_part_emitted"] is False, "finite part")
    require(decision["same_source_connection_value_count"] == 0, "connection values")
    require(decision["minimal_one_primitive_lane_preserved"] is True, "primitive lane")

    require(source["required_field_count"] == 8, "source count")
    require(source["filled_field_count"] == 0, "source filled")
    require(source["accepted_strict_P_EW_source_rows"] == 0, "source rows")
    require(source["best_internal_clue"]["accepted_as_source"] is False, "clue promoted")
    require(direct["filled_certificate_count"] == 0, "direct cert filled")
    require(direct["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct rows")
    require(direct["strict_H_K_threshold_row_emitted"] is False, "direct emitted")
    require(cross["accepted_nonHiggs_HRG_source_map_count"] == 0, "crossuse count")
    require(cross["same_prefactor_prediction_target_emitted"] is False, "crossuse target")

    for phrase in [
        "PEWGaugeActionNormalizationSourcePayloadTheorem",
        "source required fields: `8`",
        "source fields filled as final values: `0`",
        "accepted strict `P_EW` source rows: `0`",
        "accepted direct `K_threshold.Omega_H.lambda` rows: `0`",
        "not strict source rows",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print("AUDIT_PASS: PEW gauge/action payload contract locked; zero final source rows and direct-K certificates emitted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
