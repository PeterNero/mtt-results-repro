"""Audit the HRG value-map / complex-rotated H phase certificate attempt."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hrgvaluemapforh_or_complexrotatedhphasecertificate"


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    candidate = read_json(f"candidate_data/{SLUG}.candidate.json")
    hrg = read_json(f"candidate_data/{SLUG}/hrg_value_source_map_attempt.packet.json")
    phase = read_json(f"candidate_data/{SLUG}/complex_rotated_h_phase_certificate_attempt.packet.json")
    combined = read_json(f"candidate_data/{SLUG}/combined_frontier_after_two_gate_attack.packet.json")
    cert = read_json(f"certificates/{SLUG}_certificate.json")

    require(candidate["theorem"]["proved"] is True, "theorem must be proved")
    require(candidate["decision"]["strict_r_H_promoted"] is False, "r_H must remain unpromoted")
    require(candidate["decision"]["controlled_r_H_retained"] is True, "controlled r_H must be retained")
    require(candidate["decision"]["phi_axis_promoted"] is True, "phase axis should be promoted")
    require(candidate["decision"]["phi_sign_promoted"] is False, "phase sign must remain open")
    require(candidate["decision"]["strict_phi_Omega_promoted"] is False, "strict phi must remain open")

    require(hrg["strict_status"]["typed_HRG_consumer_map_emitted"] is False, "typed HRG map unexpectedly emitted")
    require(hrg["strict_status"]["accepted_strict_source_count"] == 0, "strict HRG source count must be zero")
    require(hrg["expanded_diagnostic_invariant_scan"]["accepted_as_source_identity_count"] == 0, "diagnostic scan must not promote")
    require(hrg["expanded_diagnostic_invariant_scan"]["best_candidates"][0]["accepted_as_source_identity"] is False, "best near miss must not promote")

    require(phase["decision"]["phi_axis_promoted"] is True, "phase axis decision mismatch")
    require(phase["decision"]["phase_continuum_reduced_to_binary_orientation"] is True, "phase must reduce to binary orientation")
    require(phase["promoted_now"]["phase_reduced_to"] == ["pi/2", "-pi/2"], "phase options mismatch")
    require(phase["not_promoted_now"]["plus_i_orientation"]["promoted"] is False, "plus i must remain open")
    require(phase["not_promoted_now"]["period_or_finite_quotient"]["period_selector_found"] is False, "period selector must remain open")

    require(
        combined["next_frontier"] == "MTT_Selected_HRGValueSourceMap_or_HPhaseSignSelector_v1",
        "next frontier mismatch",
    )
    require(cert["checks"]["diagnostic_near_misses_not_promoted"] is True, "cert diagnostic guard mismatch")

    print("selected_hrgvaluemapforh_or_complexrotatedhphasecertificate audit: PASS")


if __name__ == "__main__":
    main()
