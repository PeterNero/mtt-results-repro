"""Audit the sector source-payload search/emission attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_sector_zero_mode_source_payload_search_or_emission_attempt.py"
CANDIDATE = ROOT / "candidate_data" / "selected_sector_zero_mode_source_payload_search_or_emission_attempt.candidate.json"
CERT = ROOT / "certificates" / "selected_sector_zero_mode_source_payload_search_or_emission_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SectorZeroMode_SourcePayload_Search_or_Emission_Attempt_v1.md"

STATUS = "MTT_SELECTED_SECTOR_SOURCEPAYLOAD_ATTEMPT_CANONICAL_RHO_CONSTRUCTED_SELECTION_OPEN"
NEXT = "MTT_Selected_ZeroModeBasis_From_HYM_Projector_Source_Theorem_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    source = data["source_map_candidate"]
    checks = data["construction_checks"]
    decision = data["promotion_decision"]
    chain = data["source_chain"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check("certificate path", cert["candidate_path"].endswith(CANDIDATE.name), cert),
        check(
            "canonical rho candidate emitted",
            decision["canonical_source_map_constructed"] is True
            and source["rho_candidate"]["Q"]["rho"]["T3"] == source["model_matrix_tests"]["model_rho_T3"]
            and checks["all_sector_maps_present"] is True
            and checks["matter_maps_are_adjoint_triplets"] is True
            and checks["H_map_is_trivial_singlet"] is True,
            source["rho_candidate"]["Q"],
        ),
        check(
            "representation tests pass",
            checks["bracket_skew_casimir_tests_pass"] is True
            and data["what_closes_now"]["finite_representation_tests_pass"] is True
            and data["what_closes_now"]["Higgs_singlet_action_zero"] is True,
            source["model_matrix_tests"],
        ),
        check(
            "same-source diagonal End0 support imported",
            chain["selected_End0_adjoint_basis_available"] is True
            and chain["diagonal_End0_DE_formula_extracted"] is True
            and chain["End0_DE_T3_matrix_matches_rho_candidate"] is True
            and chain["eta00_harmonic_row_closed"] is True,
            chain,
        ),
        check(
            "not promoted as selected rho_s",
            decision["selected_source_map_emitted"] is False
            and decision["selected_zero_mode_bases_emitted"] is False
            and decision["can_promote_without_new_theorem"] is False
            and checks["source_flags_remain_false"] is True
            and checks["adjoint_theorem_hypothesis_rho_still_open"] is True,
            decision,
        ),
        check(
            "promotion blocker localized",
            "coherent spectral zero-mode projector retention is still false" in decision["why_not_promoted"]
            and chain["coherent_spectral_zero_mode_retention"] is False
            and chain["zero_mode_slot_values_filled"] is False
            and data["next_required_artifact"] == NEXT,
            decision["why_not_promoted"],
        ),
        check(
            "conditional promotion rule recorded",
            data["conditional_promotion_rule"]["recorded"] is True
            and data["conditional_promotion_rule"]["proved_now"] is False
            and "selected ordered zero-mode bases K_s" in data["conditional_promotion_rule"]["proof_obligation_remaining"],
            data["conditional_promotion_rule"],
        ),
        check(
            "no closure or target fitting",
            data["closure_claimed"] is False
            and data["target_fitting_used"] is False
            and cert["closure_claimed"] is False
            and cert["target_fitting_used"] is False,
            cert,
        ),
        check(
            "note records map and boundary",
            "rho_candidate,s(T_i)=ad(T_i)" in note
            and "not selected physical `rho_s`" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected sector source-payload search/emission attempt audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
