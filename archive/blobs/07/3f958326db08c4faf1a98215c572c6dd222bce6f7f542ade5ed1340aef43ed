"""Audit the imported PSM-C1-02 source-identity frontier."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
JSON_PATH = ROOT / "selected_psm_c1_02_sourceidentity_unpatched_frontier.import.json"
MD_PATH = ROOT / "PSM_C1_02_SourceIdentity_Unpatched_Frontier_Import_v1.md"

EXPECTED_STATUS = "IMPORTED_LOCAL_SOURCE_IDENTITY_CLOSED_UNPATCHED_THREE_FIELD_CERTIFICATE_OPEN"
EXPECTED_NEXT = "MTT_Selected_PSM_C1_02_PhysicalActionRestrictionSourceActualFill_or_RouteBIndependentRun_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    text = MD_PATH.read_text(encoding="utf-8", errors="ignore")

    require(data["status"] == EXPECTED_STATUS, "unexpected import status")
    require(data["next_required_artifact"] == EXPECTED_NEXT, "unexpected next artifact")
    require(data["closure_claimed"] is False, "unpatched closure must not be claimed")
    require(data["observed_data_used_as_selector"] is False, "observed data selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    statuses = data["imported_status_chain"]
    require(len(statuses) >= 14, "status chain is incomplete")
    require(any("LOCAL_PRINCIPLE_SOURCE_PACKET_VALIDATES" in s for s in statuses), "missing local packet validation")
    require(any("MEASURE_SUBLEMMA_DERIVED" in s for s in statuses), "missing derived measure sublemma")
    require(any("THREE_FIELD_PHYSICAL_SOURCE_CERTIFICATE_READY_NOT_FILLED" in s for s in statuses), "missing three-field frontier")
    require(any("PHYSICAL_ACTION_RESTRICTION_SOURCE_PROBED" in s for s in statuses), "missing A1a support-only probe")

    closes = data["what_closes_now"]
    require(closes["local_principle_source_promotion_packet_validates_all_named_blockers"], "local source packet not recorded closed")
    require(closes["finite_trace_frobenius_measure_normalization_derived"], "measure sublemma not recorded derived")
    require(closes["SI1u_A1a_support_only_probe_rejected_by_strict_validator"], "A1a support-only probe not recorded")

    remains = data["what_remains_open"]
    require(remains["unpatched_SelectedFiniteC1SourceIdentityTheorem"], "unpatched theorem should remain open")
    require(remains["SI1u_A1a_physical_action_restricts_to_selected_finite_Weyl_quotient"], "missing A1a frontier")
    require(remains["SI1u_A1b_no_extra_physical_boundary_or_source_term"], "missing A1b frontier")
    require(remains["SI1u_A1c_same_source_R_Z_R_X_b_selected_emission"], "missing A1c frontier")

    for phrase in [
        "local/premise-conditioned source-identity spine",
        "three-field certificate",
        "restriction row is emitted",
        "does not mean the unpatched theorem is proved",
    ]:
        require(phrase in text, f"missing markdown phrase: {phrase}")

    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    print("PASS psm_c1_02_sourceidentity_unpatched_frontier.import.json")


if __name__ == "__main__":
    main()
