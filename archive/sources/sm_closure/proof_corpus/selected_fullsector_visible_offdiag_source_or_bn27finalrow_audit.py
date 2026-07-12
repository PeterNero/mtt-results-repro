"""Audit full-sector offdiagonal control after source-flag consolidation."""

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
BUILDER = ROOT / "scripts" / "build_selected_fullsector_visible_offdiag_source_or_bn27finalrow.py"

SLUG = "selected_fullsector_visible_offdiag_source_or_bn27finalrow"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FullSectorVisibleOffDiagonalSource_or_BN27FinalRowAcceptance_v1.md"
OFFDIAG_PACKET = PACKET_DIR / "projected_routec_fullsector_offdiag_control.packet.json"
VISIBLE_PACKET = PACKET_DIR / "visible_global_provenance_gate.packet.json"
FINAL_PACKET = PACKET_DIR / "bn27_finalrow_acceptance_after_offdiag.packet.json"
NEXT_PACKET = PACKET_DIR / "next_visible_global_strominger_provenance.packet.json"

STATUS = "MTT_SELECTED_FULLSECTOR_OFFDIAGONAL_ROUTEC_SCOPE_CLOSED_VISIBLE_GLOBAL_PROVENANCE_OPEN"
NEXT = "MTT_Selected_VisibleGlobalStromingerProvenance_or_BN27FinalRowAcceptance_v1"
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
    offdiag = load(OFFDIAG_PACKET)
    visible = load(VISIBLE_PACKET)
    final = load(FINAL_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for payload in [candidate, cert, offdiag, visible, final, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["projected_RouteC_fullsector_offdiag_control_closed"] is True, "projected offdiag not closed")
    require(decision["literal_global_AH_Cech_offdiag_closed"] is False, "global AH/Cech offdiag overclosed")
    require(decision["selected_visible_operator_source_closed"] is False, "visible source overclosed")
    require(decision["visible_GS_same_source_closed"] is False, "visible GS overclosed")
    require(
        decision["global_full_selected_strominger_operator_provenance_closed"] is False,
        "global provenance overclosed",
    )
    require(decision["BN27_final_row_accepted"] is False, "BN27 final row overaccepted")
    require(decision["two_premise_AH_equivalent_final_connection_tables_accepted"] == 7, "AH lane")
    require(decision["strict_no_knob_closed"] is False, "strict no-knob overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclaim")

    require(offdiag["full_sector_offdiagonal_End0_control_selected_at_projected_RouteC_scope"] is True, "offdiag scope")
    require(offdiag["literal_global_AH_Cech_scope_closed"] is False, "global scope overclosed")
    for key in [
        "row_model_offdiag_closed",
        "Ext_source_has_no_T1_T2_component",
        "stationary_End0_to_sector_routing_values_closed",
        "transported_projectors_closed",
        "symbolic_transport_conjugation_closed",
        "same_branch_dotD_alpha1_closed",
        "selected_diagonal_End0_D_E_closed",
    ]:
        require(offdiag["proof_inputs"][key] is True, f"offdiag proof input missing: {key}")
    for sector in SECTORS:
        row = offdiag["sectorwise_control"][sector]
        require(row["selected_projector_transport_preserves_End0_decomposition"] is True, f"transport {sector}")
        require(row["offdiagonal_T1_T2_leakage"] == 0.0, f"leakage {sector}")
        require(row["Cartan_T3_lane_retained"] is True, f"T3 {sector}")
        require(row["same_branch_dynamic_driver_available"] is True, f"driver {sector}")

    require(visible["selected_visible_operator_source_closed"] is False, "visible source")
    require(visible["visible_green_schwarz_same_source_operator_constructed"] is False, "visible GS")
    require(
        visible["global_full_selected_strominger_operator_provenance_closed"] is False,
        "global provenance",
    )
    require(visible["support_available"]["projected_RouteC_replacement_for_local_D_E_dotD_projectors_offdiag"] is True, "support")
    require(len(visible["remaining_global_clauses"]) == 2, "remaining global clauses")

    require(final["row"] == FINAL_ROW, "final row")
    require(final["projected_RouteC_fullsector_offdiag_closed"] is True, "final projected offdiag")
    require(final["visible_global_provenance_closed"] is False, "final visible")
    require(final["global_full_selected_strominger_operator_provenance_closed"] is False, "final provenance")
    require(final["accepted_now"] is False, "final overaccepted")
    require(final["BN27_final_row_accepted"] is False, "BN27 overaccepted")
    require(final["current_connection_table_lanes"]["two_premise_AH_equivalent_lane"] == "7/8", "final AH lane")
    require(len(final["remaining_to_reach_8_of_8"]) == 2, "remaining final clauses")

    for key in [
        "transported stationary projectors/rho_s",
        "same-branch dotD/alpha1 Step40 import",
        "symbolic D_E transport replay",
        "projected Route-C full-sector offdiagonal control",
    ]:
        require(key in next_packet["do_not_reopen"], f"do-not-reopen missing: {key}")
    require(next_packet["current_lanes"]["two_premise_AH_equivalent_lane"] == "7/8", "next AH lane")

    require(cert["projected_RouteC_fullsector_offdiag_control_closed"] is True, "cert projected offdiag")
    require(cert["literal_global_AH_Cech_offdiag_closed"] is False, "cert global overclosed")
    require(cert["BN27_final_row_accepted"] is False, "cert final row")
    require(cert["strict_no_knob_closed"] is False, "cert no-knob")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    require("projected Route-C full-sector offdiagonal control is now closed" in note, "note closure")
    require("not literal global AH/Cech visible-source closure" in note, "note boundary")
    require(NEXT in note, "note next")

    print("Full-sector visible/offdiag source audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
