"""Audit selected Weyl-pair source provenance lemma attempt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_weylpair_source_provenance_lemma.candidate.json"
CERT = REPO / "certificates" / "selected_routec_weylpair_source_provenance_lemma_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_SOURCE_PROVENANCE_REDUCED_SOURCE_LEVEL_CARRIER_CLOSED_C1_TRANSFER_OPEN"
NEXT = "MTT_Selected_RouteC_WeylPair_SourceToC1_Transfer_Map_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    strategy = data["superset_strategy"]
    carrier = data["source_level_weyl_carrier"]
    active = data["active_shift_provenance"]
    transfer = data["c1_transfer_map"]
    lemma = data["lemma_attempt"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "superset guardrails",
            strategy["mode"] == "CONSTRAINED_SUPERSET_WITH_LOCKED_TARGET"
            and strategy["observed_data_used"] is False
            and strategy["lifted_flags_used_as_proof"] is False
            and strategy["target_fitting_used"] is False,
            strategy,
        ),
        check(
            "source-level Weyl carrier closed",
            carrier["proved"] is True
            and carrier["carrier_check"]["g1_equals_phase_Z_residual"] <= 1e-10
            and carrier["carrier_check"]["g2_equals_shift_X_residual"] <= 1e-10
            and carrier["source_level_flags"]["selected_s3_gerbe_source_level_promoted"] is True
            and carrier["source_level_flags"]["source_level_projective_class_selected"] is True,
            carrier,
        ),
        check(
            "operator-level still not promoted",
            carrier["source_level_flags"]["operator_level_projective_rhoE_promoted"] is False
            and carrier["source_level_flags"]["operator_level_projective_class_selected"] is False,
            carrier["source_level_flags"],
        ),
        check(
            "active shift provenance closed",
            active["proved"] is True and active["nonzero_active_shifts"] == [[1, 1]],
            active,
        ),
        check(
            "transfer map open",
            transfer["selected_source_to_C1_response_map_emitted"] is False
            and transfer["phase_Z_routed_to_u_e_I_plus_Z_column"] is False
            and transfer["shift_X_routed_to_d_nuD_I_plus_X_column"] is False
            and transfer["selected_A_selected_currently_emitted"] is False,
            transfer,
        ),
        check(
            "lemma reduced not overclaimed",
            lemma["fully_proved"] is False
            and lemma["proved_sublemma"] == "SelectedSourceLevelQutritWeylCarrierAndActiveShiftLemma"
            and lemma["open_sublemma"] == "SelectedWeylPairSourceToC1TransferMapLemma",
            lemma,
        ),
        check(
            "what closes/remains",
            data["what_closes_now"]["source_level_phase_Z_carrier_provenance"] is True
            and data["what_closes_now"]["source_level_shift_X_carrier_provenance"] is True
            and data["what_remains_open"]["emit_selected_source_to_C1_transfer_map"] is True
            and data["what_remains_open"]["promote_conditional_A_to_A_selected"] is True,
            {"closes": data["what_closes_now"], "open": data["what_remains_open"]},
        ),
        check(
            "no closure or fitting",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records reduction",
            "source-level qutrit Weyl carrier is closed" in note
            and "full provenance lemma is not yet proved" in note
            and "SelectedWeylPairSourceToC1TransferMapLemma" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C Weyl-pair source provenance audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
