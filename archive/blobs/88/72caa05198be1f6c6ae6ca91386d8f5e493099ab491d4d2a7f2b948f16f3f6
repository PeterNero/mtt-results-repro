"""Audit selected Route-C correction source-emission attempt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_correction_source_emission_or_selected_galerkin_values.candidate.json"
CERT = REPO / "certificates" / "selected_routec_correction_source_emission_or_selected_galerkin_values_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Correction_Source_Emission_or_Selected_Galerkin_Values_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_CORRECTION_SOURCE_EMISSION_AUDITED_DIAGNOSTIC_SPLITTER_NOT_SOURCE_EMITTED_VALUES_OPEN"
NEXT = "MTT_Selected_RouteC_Splitter_Source_Emission_Contract_or_Selected_DeltaTheta_C1_Solve_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")

    emission = data["source_emission_attempt"]
    payload = data["selected_payload_audit"]
    source = data["source_origin_alpha1_audit"]
    galerkin = data["selected_galerkin_values_audit"]
    contract = data["source_emission_contract"]

    emitted_flags = [
        emitted
        for sector in emission["label_emission_search"].values()
        for emitted in sector["emitted_by_selected_inputs"].values()
    ]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "diagnostic splitter not promoted",
            emission["attempted"] is True
            and emission["diagnostic_splitter_found"] is True
            and emission["diagnostic_splitter_selected_by_mtt"] is False
            and emission["diagnostic_splitter_promotion_allowed"] is False
            and emission["selected_source_emits_splitter"] is False,
            emission,
        ),
        check(
            "representative labels not emitted by selected inputs",
            emission["any_representative_label_emitted_by_selected_inputs"] is False
            and not any(emitted_flags),
            emission["label_emission_search"],
        ),
        check(
            "Phi_fin selected values still absent",
            payload["all_support_shapes_present"] is True
            and payload["all_selected_payload_flags_true"] is False
            and payload["selected_deltaTheta_C1_solution_present"] is False
            and payload["sector_response_matrices_present"] is False
            and payload["selected_values_emitted"] is False,
            payload,
        ),
        check(
            "source origin alpha1 still values-open",
            source["support_converges"] is True
            and source["all_source_flags_true"] is False
            and source["all_alpha1_values_present"] is False,
            source,
        ),
        check(
            "Galerkin honest values not promoted",
            galerkin["manifest_filled"] is True
            and galerkin["honest_root_all_pass"] is False
            and galerkin["selected_correction_matrices_emitted"] is False
            and galerkin["formal_lift_lower_validators_all_pass"] is True
            and galerkin["formal_lift_is_diagnostic_only"] is True
            and galerkin["formal_lift_promotable_as_proof"] is False,
            galerkin,
        ),
        check(
            "contract locks allowed paths and no target fit",
            contract["name"] == "RouteCSelectedSplitterSourceEmissionContract"
            and contract["minimum_acceptance_tests"]["target_fitting_used"] is False
            and contract["minimum_acceptance_tests"]["selected_source_flags_not_lifted"] is True,
            contract,
        ),
        check(
            "no closure claim",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check(
            "remaining exact gates",
            data["what_remains_open"]["selected_deltaTheta_C1_solution"] is True
            and data["what_remains_open"]["sector_response_matrices_M_u_M_d_M_e_M_nuD"] is True
            and data["what_remains_open"]["promoted_yukawa_hierarchy_CKM_PMNS_CP"] is True,
            data["what_remains_open"],
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records non-emission",
            "not source-emitted" in note
            and "diagnostic splitter" in note
            and "selected source emission" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C correction source-emission audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
