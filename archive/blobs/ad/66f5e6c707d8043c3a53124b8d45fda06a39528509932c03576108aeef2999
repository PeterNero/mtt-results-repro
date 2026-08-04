"""Audit conditional Weyl-pair A assembly / source proof reduction."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"
CERT = REPO / "certificates" / "selected_routec_weylpair_aselected_assembly_or_source_proof_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_WeylPair_Aselected_Assembly_or_Source_Proof_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_ASELECTED_ASSEMBLY_BUILT_CONDITIONAL_SOLVE_EXACT_SOURCE_PROOF_OPEN"
NEXT = "MTT_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    strategy = data["superset_strategy"]
    operator = data["conditional_operator"]
    solve = data["locked_solve"]
    selected = data["selected_emission_status"]
    provenance = data["provenance_reduction"]

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
            "conditional operator assembled but not selected",
            operator["shape"] == [72, 2]
            and operator["columns"] == ["phase_packet", "shift_packet"]
            and operator["is_A_selected"] is False,
            operator,
        ),
        check(
            "locked solve exact",
            solve["rank"] == 2
            and solve["consistent"] is True
            and solve["residual_norm"] <= 1e-10
            and abs(solve["deltaTheta_conditional"][0] - 1.0) <= 1e-10
            and abs(solve["deltaTheta_conditional"][1] - 1.0) <= 1e-10,
            solve,
        ),
        check(
            "selected emission still open",
            selected["A_selected_currently_emitted"] is False
            and selected["b_selected_currently_emitted"] is False
            and selected["rank_test_now_computable_for_selected_A"] is False
            and selected["least_squares_now_computable_for_selected_A"] is False,
            selected,
        ),
        check(
            "provenance lemma selected",
            provenance["name"] == "SelectedWeylPairSourceProvenanceLemma"
            and provenance["status"] == "NEXT_LEMMA_REQUIRED"
            and len(provenance["must_prove"]) == 4,
            provenance,
        ),
        check(
            "theorem closes algebra only",
            data["theorem"]["proved"] is True
            and data["what_closes_now"]["remaining_gap_reduced_to_source_provenance"] is True
            and data["what_remains_open"]["prove_selected_weylpair_source_provenance"] is True,
            {"theorem": data["theorem"], "open": data["what_remains_open"]},
        ),
        check(
            "no closure or fitting",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records conditional status",
            "does not promote `A_weylpair_conditional` to `A_selected`" in note
            and "SelectedWeylPairSourceProvenanceLemma" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C Weyl-pair A assembly audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
