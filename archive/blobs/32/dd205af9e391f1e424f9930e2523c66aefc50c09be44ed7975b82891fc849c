"""Audit Route-C/Strominger source-flag consolidation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_routec_strominger_sourceflags_or_samesource_visibleoperator.py"

SLUG = "selected_routec_strominger_sourceflags_or_samesource_visibleoperator"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteCStromingerSourceFlags_or_SameSourceVisibleOperatorPacket_v1.md"
FLAG_PACKET = PACKET_DIR / "routec_strominger_source_flag_consolidation.packet.json"
DE_PACKET = PACKET_DIR / "symbolic_de_transport_source_replay.packet.json"
GATE_PACKET = PACKET_DIR / "bn27_finalrow_remaining_gate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_fullsector_visible_offdiag_source.packet.json"

STATUS = "MTT_SELECTED_ROUTEC_STROMINGER_SOURCEFLAGS_CONSOLIDATED_VISIBLE_OFFDIAG_FULLSOURCE_OPEN"
NEXT = "MTT_Selected_FullSectorVisibleOffDiagonalSource_or_BN27FinalRowAcceptance_v1"
FINAL_ROW = "selected_HYM_or_projective_connection_coefficients"
SECTORS = ["Q", "u", "d", "L", "e", "N", "H"]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    flags = load(FLAG_PACKET)
    de = load(DE_PACKET)
    gate = load(GATE_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "cert theorem not proved")

    for payload in [candidate, cert, flags, de, gate, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    for key in [
        "D_E_selected_source_verified_by_symbolic_transport",
        "selected_dotD_source_verified",
        "alpha1_driver_verified",
        "selected_HYM_projector_values_promoted",
        "stationary_rho_s_validator_ready",
        "finite_projected_symbolic_transport_exactness_closed",
    ]:
        require(decision[key] is True, f"closed source flag missing: {key}")
    for key in [
        "selected_visible_operator_source_closed",
        "global_full_selected_strominger_operator_provenance_closed",
        "full_sector_offdiagonal_End0_control_selected",
        "BN27_final_row_accepted",
        "strict_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"overclaim: {key}")
    require(decision["two_premise_AH_equivalent_final_connection_tables_accepted"] == 7, "AH lane")

    consolidated = flags["consolidated_source_flags"]
    require(flags["source_flags_closed_count"] == 6, "closed source count")
    require(flags["source_flags_required_count"] == 10, "required source count")
    for key in [
        "D_E_selected_source_verified_by_symbolic_transport",
        "dotD_selected_dotD_source_verified_by_step40",
        "alpha1_driver_verified_by_step40",
        "selected_HYM_projector_values_promoted_by_transport",
        "stationary_rho_s_validator_ready",
        "finite_projected_symbolic_transport_exactness_closed",
    ]:
        require(consolidated[key] is True, f"consolidated flag false: {key}")
    for key in [
        "selected_visible_operator_source_closed",
        "visible_green_schwarz_same_source_operator_constructed",
        "full_sector_offdiagonal_End0_control_selected",
        "global_full_selected_strominger_operator_provenance_closed",
    ]:
        require(consolidated[key] is False, f"remaining blocker overclosed: {key}")
        require(key in flags["remaining_blockers"], f"remaining blocker not recorded: {key}")

    for sector in SECTORS:
        row = flags["sectorwise_flags"][sector]
        require(row["D_E_selected_source_verified_by_symbolic_transport"] is True, f"D_E {sector}")
        require(row["selected_dotD_source_verified_by_step40"] is True, f"dotD {sector}")
        require(row["alpha1_driver_verified_by_step40"] is True, f"alpha {sector}")
        require(row["selected_projector_value_promoted_by_transport"] is True, f"projector {sector}")

    require(de["D_E_source_verified_symbolically_for_all_sectors"] is True, "D_E symbolic replay")
    require(de["raw_honest_de_packet_left_unmodified"] is True, "raw packet should remain unmodified")
    require(de["source_identity"]["D_selected_U_equals_U_d"] is True, "transport identity")
    require(de["source_identity"]["model_active_diagnostic_validator_passes"] is True, "D_E diagnostic")
    require(
        de["source_identity"]["honest_validator_fails_only_by_missing_source_flags"] is True,
        "honest D_E fail reason",
    )

    require(gate["row"] == FINAL_ROW, "gate row")
    require(gate["accepted_now"] is False, "gate overaccepted")
    require(gate["BN27_final_row_accepted"] is False, "final row overaccepted")
    require(gate["current_connection_table_lanes"]["two_premise_AH_equivalent_lane"] == "7/8", "gate AH lane")
    require(len(gate["would_accept_if"]) == 3, "remaining acceptance conditions")

    for key in [
        "stationary transported projector/rho_s source promotion",
        "same-branch dotD/alpha1 Step40 import",
        "symbolic D_E transport replay",
        "model-active 27-mode matrix construction",
    ]:
        require(key in next_packet["do_not_reopen"], f"do-not-reopen missing: {key}")
    require(next_packet["current_lanes"]["two_premise_AH_equivalent_lane"] == "7/8", "next AH lane")

    require(cert["source_flags_closed_count"] == 6, "cert closed count")
    require(cert["source_flags_required_count"] == 10, "cert required count")
    require(cert["BN27_final_row_accepted"] is False, "cert final row")
    require(cert["strict_no_knob_closed"] is False, "cert no-knob")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    require("not a lifted-flag replay" in note, "note lifted flag guard")
    require("The counted AH-equivalent lane therefore remains `7/8`" in note, "note AH lane")
    require(NEXT in note, "note next")

    print("Route-C/Strominger source-flag consolidation audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
