from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_end0_sector_model_values_certificate.json"
STATUS = "POST_ALPHA_END0_SECTOR_MODEL_VALUES_CONSTRUCTED_SELECTED_ZEROMODES_OPEN"
NEXT = "Selected_U1Y_RouteC_ZeroModeBasis_From_HYM_Projector_Source_Theorem_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["selected_zero_mode_bases_emitted"] is False, "selected zero modes should remain open")
    require(cert["physical_dotD_alpha1_payload_extracted"] is False, "physical dotD payload should remain open")
    require(all(cert["checks"].values()), "all certificate checks should pass")

    values = packet["value_packet"]
    require(values["domain"]["basis"] == ["T1", "T2", "T3"], "wrong End0 basis")
    require(values["sector_carrier_model"]["total_dimension"] == 19, "wrong carrier dimension")
    require(values["sector_carrier_model"]["rank_match"]["six_matter_triplets_plus_H_singlet"] == "6*3+1", "wrong rank structure")
    require(values["sector_carrier_model"]["validation"]["all_lie_checks_pass"] is True, "Lie checks must pass")
    require(values["sector_carrier_model"]["validation"]["all_projectors_idempotent"] is True, "projectors must be idempotent")
    require(values["sector_carrier_model"]["validation"]["all_distinct_projectors_orthogonal"] is True, "projectors must be orthogonal")
    require(values["sector_carrier_model"]["validation"]["projectors_sum_to_identity"] is True, "projectors must sum to identity")
    require(values["sector_carrier_model"]["validation"]["all_projectors_commute_with_End0_action"] is True, "projectors should commute")
    require(values["sector_carrier_model"]["validation"]["H_T3_response_zero"] is True, "H should be T3-trivial")

    dims = values["sector_projector_model"]["sector_dimensions"]
    require(dims == {"H": 1, "L": 3, "N": 3, "Q": 3, "d": 3, "e": 3, "u": 3}, "sector dimensions changed")
    require(values["sector_projector_model"]["sector_order"] == ["Q", "u", "d", "L", "e", "N", "H"], "sector order changed")

    support = packet["b_support_dictionary_interpretation"]
    require(
        support["dictionary_status"] == "RECORDED_AS_USER_SUPPLIED_SUPPORT_INTERPRETATION_NOT_USED_AS_PROOF_INPUT",
        "dictionary should be recorded as support, not proof",
    )
    require(support["interpretation_status"] == "SUPPORT_MATCH_ONLY_SELECTED_ZEROMODE_SOURCE_OPEN", "support should not promote")
    require(support["support_labels_by_sector"]["Q"] == ["B3", "B2", "B1"], "Q support changed")
    require(support["support_labels_by_sector"]["N"] == [], "N should remain sterile in dictionary")
    require("full SM closure" in support["not_claimed"], "must not claim SM closure")

    blocker = packet["promotion_blocker"]
    require(blocker["minimal_new_theorem_needed"] == "MTT_Selected_ZeroModeBasis_From_HYM_Projector_Source_Theorem_v1", "wrong blocker theorem")
    require("selected ordered zero-mode bases K_s" in blocker["proof_obligation_remaining"], "missing K_s obligation")

    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "Q -> B3+B2+B1" in note, "note missing essentials")

    print("AUDIT_PASS: End0 sector model values imported; B-support dictionary matched without promotion")


if __name__ == "__main__":
    main()
