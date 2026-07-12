"""Audit R_theta support re-evaluation / source promotion attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_rtheta_supportreevaluation_or_sourcepromotionattempt"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SUPPORT_REEVALUATION = PACKET_DIR / "support_rows_under_rtheta_contract.packet.json"
NON_SOURCE_CLOSURES = PACKET_DIR / "accepted_non_source_support_closures.packet.json"
PROMOTION_ATTEMPT = PACKET_DIR / "source_promotion_attempt_after_support_reevaluation.packet.json"
DECISION = PACKET_DIR / "rtheta_support_reevaluation_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_rtheta_support_reevaluation.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RThetaSupportReevaluation_or_SourcePromotionAttempt_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_RTHETA_SUPPORTREEVALUATION_OR_SOURCEPROMOTIONATTEMPT_"
    "BUILT_SUPPORT_ROLES_CLOSED_SOURCE_PROMOTION_OPEN"
)
NEXT = "MTT_Selected_RThetaSourceOwnerAndRowCoefficientPacket_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    support = load(SUPPORT_REEVALUATION)
    non_source = load(NON_SOURCE_CLOSURES)
    promotion = load(PROMOTION_ATTEMPT)
    decision = load(DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")

    require(
        support["status"] == "SUPPORT_ROWS_REEVALUATED_UNDER_RTHETA_CONTRACT",
        "support status mismatch",
    )
    require(support["reevaluated_row_count"] == 10, "wrong support row count")
    require(support["accepted_non_source_role_count"] >= 8, "non-source roles not accepted")
    require(support["accepted_rtheta_source_row_count"] == 0, "source rows overaccepted")
    require(support["support_ambiguity_closed"] is True, "support ambiguity not closed")
    for row in support["reevaluated_rows"]:
        require(row["accepted_as_rtheta_source_row"] is False, f"row overpromoted: {row['support_id']}")
        require(row["decision"], f"row decision missing: {row['support_id']}")
    rows = {row["support_id"]: row for row in support["reevaluated_rows"]}
    require(
        rows["residual_value_table"]["accepted_non_source_role"]
        == "finite_residual_validation_support",
        "residual row not promoted to validation support",
    )
    require(
        rows["residual_value_table"]["satisfies_rtheta_requirements"]
        == ["finite_residual_validation_support"],
        "residual validation requirement mismatch",
    )
    require(
        rows["qasu3_sm_parity_source_rows"]["accepted_non_source_role"]
        == "SM_parity_domain_interface_candidate",
        "Qa/SU3 role mismatch",
    )
    require(
        rows["versioned_value_packet"]["accepted_non_source_role"] == "value_replay_payload",
        "value packet role mismatch",
    )
    require(support["closure_claimed"] is False, "support packet overclaimed")

    require(
        non_source["status"] == "NON_SOURCE_SUPPORT_ROLES_ACCEPTED_SOURCE_ROWS_STILL_EMPTY",
        "non-source closure status mismatch",
    )
    require(non_source["accepted_validation_support"] == ["residual_value_table"], "validation support mismatch")
    require(non_source["accepted_source_rows"] == [], "non-source packet accepted source rows")
    for key in [
        "finite_residual_validation_support",
        "support_row_role_classification",
        "proxy_rows_rejected_as_sources",
        "same_branch_support_reused_without_overclaim",
    ]:
        require(non_source["what_this_closes"][key] is True, f"non-source close flag missing: {key}")
    for key in [
        "selected_dynamic_operator_source_owner",
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
    ]:
        require(non_source["what_this_does_not_close"][key] is True, f"open blocker missing: {key}")
    require(non_source["closure_claimed"] is False, "non-source closure overclaimed")

    require(
        promotion["status"] == "SOURCE_PROMOTION_ATTEMPT_EXECUTED_NO_RTHETA_SOURCE_ROWS_ACCEPTED",
        "promotion status mismatch",
    )
    require(promotion["current_accepted_source_rows"] == [], "promotion accepted source rows")
    require(promotion["promoted_from_support_count"] == 0, "support overpromoted")
    require(promotion["accepted_source_owner_theorem"] is None, "source owner overaccepted")
    require(promotion["accepted_scale_scheme_loop_convention"] is None, "precision convention overaccepted")
    require(promotion["accepted_profile_likelihood_or_diagonal_theorem"] is None, "profile response overaccepted")
    require(promotion["no_knob_value_derivation_closed"] is False, "no-knob derivation overclosed")
    require(promotion["external_likelihood_imported"] is False, "external likelihood overimported")
    require(promotion["closure_claimed"] is False, "promotion overclaimed")

    require(
        decision["status"] == "SUPPORT_REEVALUATION_CLOSED_SOURCE_PROMOTION_REMAINS_OPEN",
        "decision status mismatch",
    )
    require(decision["support_ambiguity_closed"] is True, "decision support ambiguity not closed")
    require(decision["accepted_non_source_support_closed"] is True, "decision non-source not closed")
    require(decision["source_promotion_attempt_executed"] is True, "promotion not attempted")
    require(decision["accepted_rtheta_source_row_count"] == 0, "decision overaccepted source rows")
    for key in [
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(len(decision["remaining_rtheta_blockers"]) == 6, "wrong blocker count")
    require(decision["closure_claimed"] is False, "decision overclaimed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(len(cutset["recommended_next"]["must_emit"]) == 5, "next payload too small")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")

    final = data["closure_decision"]
    require(final["support_ambiguity_closed"] is True, "candidate final support not closed")
    require(final["accepted_non_source_support_closed"] is True, "candidate final non-source not closed")
    for key in [
        "accepted_rtheta_source_rows_closed",
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(final[key] is False, f"candidate final overclosed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(cert["accepted_rtheta_source_row_count"] == 0, "certificate overaccepted rows")
    require("accepted R_theta source rows    : 0" in note, "note missing zero-source guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
