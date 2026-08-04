"""Attempt the terminal monad-difference lane selector for Qa/SU3 visible L2."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = CERTS / "selected_qa_su3_monad_difference_l2_source_attempt_certificate.json"
Q79_PROOF_ATTEMPT = Q79_REPO / "certificates" / "selected_monad_difference_l2_source_proof_attempt_certificate.json"
Q79_TYPED_RECOVERY = Q79_REPO / "certificates" / "iwasawa_typed_monad_section_recovery_certificate.json"
Q79_MONAD_MAP_GATE = Q79_REPO / "certificates" / "iwasawa_monad_map_data_gate_certificate.json"
Q79_SPECTRAL_TEMPLATE = Q79_REPO / "certificates" / "iwasawa_spectral_galerkin_data.template.json"

OUTPUT_TEMPLATE = CERTS / "selected_qa_su3_terminal_monad_lane_selector.template.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_terminal_monad_lane_selector_attempt_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def make_template() -> dict[str, Any]:
    return {
        "schema": "SelectedQaSU3TerminalMonadLaneSelector.v1",
        "status": "OPEN_SELECTED_QA_SU3_TERMINAL_MONAD_LANE_SELECTOR_REQUIRED",
        "purpose": (
            "Supply the source-level rule selecting the terminal monad-difference "
            "lane L_i-K2 as the visible ordered L source lane."
        ),
        "conditional_uniqueness_target": {
            "lane": "terminal_monad_differences_L_i_minus_K2",
            "unique_match": "L3-K2",
            "L": [1, -2, 0],
            "L2": [2, -4, 0],
        },
        "must_supply": {
            "source_lane_selector": None,
            "typed_monad_f_sections": None,
            "typed_monad_g_sections": None,
            "transition_or_rhoE_data": None,
            "Pic0_selection_or_quotient": None,
            "binding_to_Appell_Humbert_Cech_order": None,
            "spectral_or_Cech_fallback_if_typed_sections_absent": None,
        },
    }


def main() -> None:
    previous = load(PREVIOUS)
    proof = load(Q79_PROOF_ATTEMPT)
    typed = load(Q79_TYPED_RECOVERY)
    monad_gate = load(Q79_MONAD_MAP_GATE)
    spectral_template = load(Q79_SPECTRAL_TEMPLATE)

    theorem = proof["conditional_uniqueness_theorem"]
    scan = proof["terminal_monad_difference_scan"]
    unconditional = proof["unconditional_selection_attempt"]
    typed_missing = typed["not_recovered_from_corpus"]
    fallback = typed["spectral_fallback_contract"]

    conditional_uniqueness_closed = (
        theorem["proved"] is True
        and scan["target_matches"] == ["L3-K2"]
        and scan["double_target_matches"] == ["L3-K2"]
        and scan["zero_central_terminal_differences"] == ["L3-K2"]
        and theorem["dual_g3_check"]["is_dual_to_selected_L3_minus_K2"] is True
    )
    typed_sections_absent = all(
        typed_missing.get(key) is True
        for key in (
            "explicit_f_i_section_representatives",
            "explicit_g_i_section_representatives",
            "transition_functions_for_L_i_K1_K2",
            "Cech_cover_and_cocycles",
            "g_after_f_zero_certificate",
            "monad_exactness_or_sheaf_singularity_control",
        )
    )
    spectral_fallback_ready_as_next_form = (
        typed["route_decision"]["non_invariant_spectral_galerkin_fallback_triggered"] is True
        and spectral_template["mode"] == "non_invariant_spectral_galerkin"
    )

    output = {
        "certificate": "SelectedQaSU3TerminalMonadLaneSelectorAttempt",
        "status": "QA_SU3_TERMINAL_MONAD_LANE_SELECTOR_ATTEMPT_CONDITIONAL_UNIQUENESS_CLOSED_LANE_SELECTION_OPEN",
        "inputs": {
            "previous_monad_difference_gate": str(PREVIOUS.relative_to(ROOT)),
            "q79_selected_monad_difference_proof_attempt": str(Q79_PROOF_ATTEMPT),
            "q79_typed_monad_section_recovery": str(Q79_TYPED_RECOVERY),
            "q79_monad_map_gate": str(Q79_MONAD_MAP_GATE),
            "q79_spectral_galerkin_template": str(Q79_SPECTRAL_TEMPLATE),
        },
        "template_written": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
        "closed_now": {
            "conditional_uniqueness_inside_terminal_lane": conditional_uniqueness_closed,
            "unique_zero_central_terminal_difference": scan["zero_central_terminal_differences"] == ["L3-K2"],
            "unique_double_target_match": scan["double_target_matches"] == ["L3-K2"],
            "dual_g3_type_identifies_same_line": proof["what_this_closes"][
                "dual_g3_type_identifies_the_same_line_up_to_dual"
            ],
            "proof_frontier_no_longer_arithmetic": proof["what_this_closes"]["proof_frontier_no_longer_arithmetic"],
            "typed_monad_recovery_attempt_closed_negative": typed["verdict"]["closes_corpus_recovery_attempt"],
            "spectral_fallback_identified": spectral_fallback_ready_as_next_form,
        },
        "not_closed": {
            "source_lane_selector_for_terminal_monad_differences": unconditional["open_blockers"][
                "actual_MTT_selection_of_terminal_monad_difference_lane"
            ],
            "typed_sections_or_transition_data": typed_sections_absent,
            "Pic0_selection_or_quotient": unconditional["open_blockers"]["neutral_Pic0_selection_or_quotient"],
            "binding_to_Appell_Humbert_Cech_transitions": previous["not_closed"][
                "bind_monad_difference_to_L2_transitions"
            ],
            "same_source_D_E_dotD_Riesz_Green": proof["what_this_does_not_close"][
                "same_source_D_E_dotD_Riesz_Green"
            ]
            is False,
            "full_SM_closure": True,
        },
        "minimal_next_object": {
            "name": "Selected_Terminal_Monad_Lane_or_Spectral_Galerkin_Source.v1",
            "two_allowed_routes": [
                {
                    "id": "terminal_monad_lane_selector",
                    "must_supply": proof["minimal_success_contract"]["must_supply"],
                },
                {
                    "id": "non_invariant_spectral_galerkin_fallback",
                    "must_supply": fallback["must_supply"],
                    "template": str(Q79_SPECTRAL_TEMPLATE),
                },
            ],
            "reason": (
                "The terminal-lane arithmetic is solved, but the typed monad "
                "sections are absent; the existing q79 recovery gate therefore "
                "triggers the spectral Galerkin fallback as the next executable route."
            ),
        },
        "guardrails": {
            "claims_terminal_lane_selected": False,
            "claims_unconditional_selected_monad_difference_source": False,
            "claims_typed_monad_sections_recovered": False,
            "claims_pic0_resolved": False,
            "claims_full_SM_closure": False,
            "uses_observed_masses_or_mixings": False,
            "uses_benchmark_flavor_entries": False,
        },
        "gate_result": {
            "terminal_monad_lane_selector_closed": False,
            "conditional_uniqueness_closed": conditional_uniqueness_closed,
            "remaining_gate_is_lane_selector_or_spectral_source": True,
            "target_fitting_used": False,
        },
    }

    cert_text = json.dumps(output, indent=2, sort_keys=True)
    template_text = json.dumps(make_template(), indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(template_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
