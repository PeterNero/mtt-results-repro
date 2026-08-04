"""Audit the HYM projector source-promotion implication packet."""

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
BUILDER = ROOT / "scripts" / "build_selected_hym_projector_sourcepromotion_or_fullstrominger_operator_value.py"

SLUG = "selected_hym_projector_sourcepromotion_or_fullstrominger_operator_value"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HYM_Projector_SourcePromotion_or_FullStrominger_Operator_Value_Theorem_v1.md"
CONTRACT_PACKET = PACKET_DIR / "selected_source_promotion_contract.packet.json"
IMPLICATION_PACKET = PACKET_DIR / "bn27_final_row_implication_replay.packet.json"
FLAG_PACKET = PACKET_DIR / "routec_strominger_source_flag_manifest.packet.json"
NEXT_PACKET = PACKET_DIR / "next_routec_strominger_sourceflags_or_samesource_visibleoperator.packet.json"

STATUS = "MTT_SELECTED_HYM_PROJECTOR_SOURCEPROMOTION_IMPLICATION_PROVED_SOURCE_FLAGS_OPEN"
NEXT = "MTT_Selected_RouteCStromingerSourceFlags_or_SameSourceVisibleOperatorPacket_v1"
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
    contract = load(CONTRACT_PACKET)
    implication = load(IMPLICATION_PACKET)
    flags = load(FLAG_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for payload in [candidate, cert, contract, implication, flags, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["source_promotion_implication_proved"] is True, "implication not proved")
    require(decision["model_active_payload_sufficient_conditionally"] is True, "conditional sufficiency missing")
    require(decision["source_theorem_antecedent_closed"] is False, "source antecedent overclosed")
    require(decision["selected_source_flags_closed"] is False, "selected flags overclosed")
    require(decision["accepted_now"] is False, "accepted now overclaim")
    require(decision["BN27_final_row_accepted"] is False, "BN27 row overaccepted")
    require(decision["two_premise_AH_equivalent_final_connection_tables_accepted"] == 7, "AH lane count")
    require(decision["strict_no_knob_closed"] is False, "strict no-knob overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclaim")
    require(decision["missing_flag_groups"] == 6, "missing flag group count")

    snapshot = candidate["source_flag_snapshot"]
    for key in [
        "de_action_selected_source_verified",
        "dotd_selected_dotD_source_verified",
        "dotd_alpha1_driver_verified",
        "selected_HYM_projector_values_promoted",
        "selected_visible_operator_source_closed",
        "full_sector_offdiagonal_control_selected",
    ]:
        require(snapshot[key] is False, f"source flag unexpectedly true: {key}")

    require(contract["contract_name"] == "SelectedHYMProjectorSourcePromotionTheorem", "contract name")
    require(len(contract["selected_source_axioms_needed"]) == 7, "contract axiom count")
    require(contract["source_flags_required"]["de_action_selected_source_verified"] == SECTORS, "D_E sectors")
    require(contract["source_flags_required"]["dotd_selected_dotD_source_verified"] == SECTORS, "dotD sectors")
    require(contract["source_flags_required"]["dotd_alpha1_driver_verified"] == SECTORS, "alpha sectors")
    require(contract["source_flags_required"]["selected_projector_values"] == SECTORS, "projector sectors")
    require("finite 27-mode D_E matrix" in contract["do_not_rebuild"], "D_E no-rebuild missing")

    require(implication["row"] == FINAL_ROW, "implication row")
    require(implication["antecedent_currently_true"] is False, "antecedent overclosed")
    require(implication["model_active_payload_sufficient_if_antecedent_true"] is True, "conditional payload")
    require(implication["conditional_final_row_acceptance"] is True, "conditional final row")
    require(implication["accepted_now"] is False, "implication overaccepted")
    require(implication["current_connection_table_lanes"]["two_premise_AH_equivalent_lane"] == "7/8", "AH lane")
    require(implication["would_promote_to"]["two_premise_AH_equivalent_lane"] == "8/8", "conditional target")

    require(flags["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3", "basis id")
    require(flags["ambient_dimension"] == 27, "ambient dimension")
    require(flags["sectors"] == SECTORS, "sectors")
    for sector in SECTORS:
        require(flags["D_E_flags"][sector] is False, f"D_E flag overclosed {sector}")
        require(flags["dotD_alpha1_flags"][sector]["selected_dotD_source_verified"] is False, f"dotD flag {sector}")
        require(flags["dotD_alpha1_flags"][sector]["alpha1_driver_verified"] is False, f"alpha flag {sector}")
        require(flags["projector_flags"][sector]["selected_source_verified"] is False, f"projector source {sector}")
        require(
            flags["projector_flags"][sector]["value_emitted_as_selected_HYM_projector"] is False,
            f"projector value {sector}",
        )
    require(flags["honest_validators_fail_only_by_missing_flags"]["D_E"] is True, "D_E fail reason")
    require(flags["honest_validators_fail_only_by_missing_flags"]["dotD_alpha1"] is True, "dotD fail reason")
    require(flags["diagnostic_validators_pass"]["D_E"] is True, "D_E diagnostic")
    require(flags["diagnostic_validators_pass"]["dotD_alpha1"] is True, "dotD diagnostic")
    require(flags["diagnostic_validators_pass"]["projectors"] is True, "projector diagnostic")
    require(flags["visible_source_roots"]["visible_cw_selected_source_closed"] is False, "visible CW overclosed")
    require(
        flags["visible_source_roots"]["visible_gs_selected_operator_source_constructed"] is False,
        "visible GS overclosed",
    )
    require(flags["offdiagonal_scope"]["row_model_ext_control_closed"] is True, "row-model offdiag")
    require(flags["offdiagonal_scope"]["full_sector_validator_ready"] is False, "full-sector offdiag overclosed")

    require("recompute the same 27-mode D_E matrix" in next_packet["not_allowed_next"], "no-loop D_E")
    require("accept lifted selected_source flags without source provenance" in next_packet["not_allowed_next"], "no lifted flags")
    require("RouteC_full_strominger_operator" in next_packet["allowed_next_routes"], "RouteC next route")
    require("Visible_same_source_packet" in next_packet["allowed_next_routes"], "visible next route")
    require(next_packet["current_lanes"]["two_premise_AH_equivalent_lane"] == "7/8", "next AH lane")

    require(cert["source_promotion_implication_proved"] is True, "cert implication")
    require(cert["source_theorem_antecedent_closed"] is False, "cert antecedent")
    require(cert["BN27_final_row_accepted"] is False, "cert final row")
    require(cert["strict_no_knob_closed"] is False, "cert no-knob")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    require("conditionally sufficient" in note, "note conditional")
    require("The antecedent is still open" in note, "note open antecedent")
    require(NEXT in note, "note next")

    print("HYM projector source-promotion implication audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
