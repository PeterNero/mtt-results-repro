"""Audit projected Route-C equivalence acceptance for the BN27 HYM row."""

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
BUILDER = ROOT / "scripts" / "build_selected_visibleglobalstromingerprovenance_or_bn27finalrowacceptance.py"

SLUG = "selected_visibleglobalstromingerprovenance_or_bn27finalrowacceptance"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_VisibleGlobalStromingerProvenance_or_BN27FinalRowAcceptance_v1.md"
GLOBAL_PACKET = PACKET_DIR / "literal_visible_global_provenance_recheck.packet.json"
EQUIV_PACKET = PACKET_DIR / "projected_routec_bn27_hymrow_equivalence.packet.json"
LANE_PACKET = PACKET_DIR / "bn27_ah_equivalent_lane_acceptance.packet.json"
NEXT_PACKET = PACKET_DIR / "next_strict_global_or_truesm_after_ah8.packet.json"

STATUS = "MTT_SELECTED_BN27_HYMROW_PROJECTED_ROUTEC_EQUIVALENCE_ACCEPTED_AH8_STRICT_GLOBAL_OPEN"
NEXT = "MTT_Selected_StrictGlobalCechHYMProvenance_or_TrueSMClosureAfterAH8_v1"
FINAL_ROW = "selected_HYM_or_projective_connection_coefficients"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    global_packet = load(GLOBAL_PACKET)
    equiv = load(EQUIV_PACKET)
    lane = load(LANE_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "cert theorem not proved")

    for payload in [candidate, cert, global_packet, equiv, lane, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["projected_RouteC_equivalence_for_BN27_HYM_row_accepted"] is True, "projected row not accepted")
    require(decision["two_premise_AH_equivalent_final_connection_tables_accepted"] == 8, "AH count")
    require(decision["two_premise_AH_equivalent_lane_closed"] is True, "AH lane not closed")
    require(decision["literal_visible_global_provenance_closed"] is False, "literal visible overclosed")
    require(decision["literal_good_cover_Cech_HYM_closed"] is False, "literal good-cover overclosed")
    require(decision["strict_no_knob_closed"] is False, "strict no-knob overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclaim")

    require(global_packet["selected_visible_operator_source_closed"] is False, "global visible overclosed")
    require(global_packet["visible_GS_same_source_closed"] is False, "global GS overclosed")
    require(global_packet["literal_good_cover_cech_closed"] is False, "literal Cech overclosed")
    require(global_packet["literal_HYM_connection_coefficients_accepted"] is False, "literal HYM overclosed")

    require(equiv["row"] == FINAL_ROW, "equiv row")
    require(equiv["accepted_as_equivalent_BN27_HYM_projective_connection_row"] is True, "equiv not accepted")
    require("AH-equivalent" in equiv["accepted_scope"], "equiv scope")
    require(equiv["literal_global_scope_closed"] is False, "equiv global overclosed")
    for key in [
        "finite_projected_HYM_source_principle_closed",
        "automatic_finite_cutoff_exactness_for_A_N_closed",
        "D_E_dotD_alpha_projector_source_flags_closed",
        "projected_fullsector_offdiag_control_closed",
        "literal_row_was_not_previously_accepted",
    ]:
        require(equiv["proof_inputs"][key] is True, f"equiv proof input missing: {key}")
    require(equiv["theorem"]["proved"] is True, "equiv theorem")

    require(lane["two_premise_AH_equivalent_lane"] == "8/8", "lane 8/8")
    require(lane["accepted_final_row"] is True, "lane final row")
    require(lane["literal_global_Cech_HYM_lane_closed"] is False, "lane global overclosed")
    require(lane["strict_no_knob_closed"] is False, "lane no-knob")
    require(lane["true_SM_equivalence_closed"] is False, "lane true SM")

    for key in [
        "finite projected A_N exactness",
        "transported D_E/dotD/projector/rho_s source flags",
        "projected Route-C full-sector offdiagonal control",
        "AH-equivalent BN27 HYM row acceptance",
    ]:
        require(key in next_packet["do_not_reopen"], f"do-not-reopen missing: {key}")

    require(cert["projected_RouteC_equivalence_for_BN27_HYM_row_accepted"] is True, "cert projected row")
    require(cert["two_premise_AH_equivalent_final_connection_tables_accepted"] == 8, "cert AH count")
    require(cert["two_premise_AH_equivalent_lane_closed"] is True, "cert AH lane")
    require(cert["literal_visible_global_provenance_closed"] is False, "cert global")
    require(cert["strict_no_knob_closed"] is False, "cert no-knob")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    require("AH-equivalent BN27 connection-table lane reaches `8/8`" in note, "note AH8")
    require("not literal global AH/Cech/HYM provenance" in note, "note boundary")
    require(NEXT in note, "note next")

    print("Visible/global provenance or BN27 final-row acceptance audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
