"""Audit selected End0-to-sector functor source/value packet attempt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_end0_to_sector_functor_source_and_value_packet.candidate.json"
CERT = ROOT / "certificates" / "selected_end0_to_sector_functor_source_and_value_packet_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_End0_to_SectorFunctor_Source_and_Value_Packet_v1.md"

STATUS = "MTT_SELECTED_END0_TO_SECTOR_FUNCTOR_PACKET_ATTEMPTED_EXISTING_VALUES_REJECTED_FUNCTOR_OBJECT_OPEN"
NEXT = "MTT_Selected_SectorZeroMode_Realization_Functor_or_End0TensorProduct_Construction_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    test = data["existing_value_tests"]
    nogo = data["scalar_normalization_no_go"]
    contract = data["minimal_functor_contract"]
    decision = data["decision"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "selected End0 domain retained",
            data["selected_End0_domain"]["basis"] == ["T1", "T2", "T3"]
            and data["selected_End0_domain"]["basis_selected"] is True
            and data["selected_End0_domain"]["adT3_matrix"] == [[0, -1, 0], [1, 0, 0], [0, 0, 0]],
            data["selected_End0_domain"],
        ),
        check(
            "existing values rejected",
            test["passes"] is False
            and test["bn_rejected_as_selected_End0_basis"] is True
            and test["honest_bn_validator_fails_only_by_source_flags"] is True
            and test["all_compact_sector_flags_false"] is True
            and test["conditional_weyl_transfer_exact_but_unselected"] is True,
            test,
        ),
        check(
            "scalar normalization no-go",
            nogo["closed"] is True
            and nogo["requires_tensor_product_or_realization_functor"] is True
            and "No scalar normalization" in nogo["statement"],
            nogo,
        ),
        check(
            "functor contract emitted",
            contract["status"] == "OPEN"
            and len(contract["must_emit"]) >= 6
            and "selected sector zero-mode realization for Q,u,d,L,e,N,H" in contract["must_emit"]
            and "set selected flags from diagnostic lifted packet" in contract["forbidden_shortcuts"],
            contract,
        ),
        check(
            "decision honest",
            decision["selected_End0_to_sector_functor_values_extracted"] is False
            and decision["existing_BN_or_compact_values_promoted"] is False
            and decision["scalar_normalization_sufficient"] is False
            and decision["functor_contract_specified"] is True
            and decision["next_required_artifact"] == NEXT,
            decision,
        ),
        check(
            "sector summaries preserve flags",
            all(
                slot["selected_dotD_source_verified"] is False and slot["alpha1_driver_verified"] is False
                for slot in data["sector_value_summaries"]["compact_dotd_response"].values()
            ),
            data["sector_value_summaries"]["compact_dotd_response"],
        ),
        check(
            "no closure or target fitting",
            data["closure_claimed"] is False
            and data["target_fitting_used"] is False
            and cert["closure_claimed"] is False
            and cert["target_fitting_used"] is False,
            {"closure": data["closure_claimed"], "target_fitting": data["target_fitting_used"]},
        ),
        check(
            "next artifact",
            data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT,
            data["next_required_artifact"],
        ),
        check(
            "note records no-go",
            "The obstruction is not a missing scalar" in note
            and "Existing Values Rejected" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected End0-to-sector functor packet audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
