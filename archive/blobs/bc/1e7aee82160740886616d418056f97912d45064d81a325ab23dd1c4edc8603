"""Audit the H polar-field numerical completion attempt packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hpolarfieldnumericalcompletionattempt_or_directfinitehactionrows"


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    candidate = read_json(f"candidate_data/{SLUG}.candidate.json")
    enumeration = read_json(f"candidate_data/{SLUG}/controlled_polar_completion_enumeration.packet.json")
    clues = read_json(f"candidate_data/{SLUG}/source_clue_map_for_discrete_choices.packet.json")
    numeric = read_json(f"candidate_data/{SLUG}/controlled_hpolar_numeric_candidate.packet.json")
    cutset = read_json(f"candidate_data/{SLUG}/next_cutset_after_controlled_numeric_candidate.packet.json")
    cert = read_json(f"certificates/{SLUG}_certificate.json")

    require(candidate["theorem"]["proved"] is True, "theorem must be proved")
    require(candidate["decision"]["strict_no_knob_numeric_solution_found"] is False, "strict solution must remain open")
    require(candidate["decision"]["controlled_numeric_candidate_found"] is True, "controlled candidate must be emitted")
    require(candidate["key_numbers"]["strict_accepted_row_count"] == 0, "strict row count must remain zero")
    require(abs(candidate["key_numbers"]["s_beta_residual"]) <= 1e-15, "s_beta residual too large")

    require(enumeration["strict_acceptance"]["accepted_count"] == 0, "enumeration must accept zero strict candidates")
    require(len(enumeration["enumerated_candidates"]) == 8, "expected eight controlled phase/sign candidates")
    require(clues["clues"]["T3_orientation"]["available"] is True, "T3 orientation clue missing")
    require(clues["clues"]["complex_rotated_phase"]["available"] is True, "complex phase clue missing")
    require(clues["external_diagnostic_guard"]["used_to_select_rows_here"] is False, "external diagnostic must not select rows")

    tests = numeric["acceptance_tests"]
    require(tests["Hermitian"] is True, "controlled candidate must be Hermitian")
    require(tests["tracefree"] is True, "controlled candidate must be trace-free")
    require(tests["non_scalar"] is True, "controlled candidate must be non-scalar")
    require(tests["s_beta_recovered"] is True, "controlled candidate must recover selected s_beta")
    require(tests["strict_source_owned_rows"] is False, "controlled candidate must not be strict source-owned rows")
    require(numeric["candidate"]["phi_Omega_label"] == "pi/2", "selected controlled phase mismatch")
    require(numeric["candidate"]["sigma_D"] == 1, "selected controlled sigma mismatch")
    require(numeric["candidate"]["m0"] == 0.0, "selected controlled trace mismatch")

    require(
        cutset["next_frontier"] == "MTT_Selected_HPolarFieldPromotion_or_FiniteHActionDerivation_v1",
        "next frontier mismatch",
    )
    require(cert["checks"]["controlled_not_counted_as_strict"] is True, "certificate tier check failed")

    print("selected_hpolarfieldnumericalcompletionattempt_or_directfinitehactionrows audit: PASS")


if __name__ == "__main__":
    main()
