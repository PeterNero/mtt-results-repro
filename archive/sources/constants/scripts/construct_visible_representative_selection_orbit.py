"""Construct Visible_Representative_Selection_in_Antiunitary_q79_q369_Orbit_v1."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"

ANTIUNITARY_CERT = CERTS / "antiunitary_dedotd_equivalence_test_certificate.json"
SOURCE_ORIGIN_CERT = CERTS / "selected_source_origin_or_antiunitary_dedotd_equivalence_attempt_certificate.json"
OUTPUT_CERT = CERTS / "visible_representative_selection_orbit_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    anti = load(ANTIUNITARY_CERT)
    source = load(SOURCE_ORIGIN_CERT)
    anti_closed = anti["closed_now"]
    source_closed = source["closed_now"]

    orbit_is_selected_object = (
        source_closed["C6_branch_space_reduced_to_global_conjugate_pair"]
        and source_closed["not_two_unrelated_universes"]
        and source_closed["independent_channel_phase_knobs_removed"]
        and anti_closed["operator_level_antiunitary_equivalence_for_current_finite_packets"]
    )
    visible_rep_is_not_selected_yet = (
        anti["source_flags"]["still_open_on_both_branches"]
        and anti["not_closed"]["selected_source_origin"]
        and anti["not_closed"]["retarded_or_source_boundary_selector_for_one_representative"]
    )

    output = {
        "certificate": "VisibleRepresentativeSelectionInAntiunitaryQ79Q369Orbit",
        "status": "ANTIUNITARY_ORBIT_RETAINED_VISIBLE_REPRESENTATIVE_SELECTION_OPEN",
        "inputs": {
            "antiunitary_dedotd_equivalence": str(ANTIUNITARY_CERT.relative_to(ROOT)),
            "source_origin_or_antiunitary_attempt": str(SOURCE_ORIGIN_CERT.relative_to(ROOT)),
        },
        "interpretation": {
            "full_universe_object": "{q79, q369} antiunitary orbit",
            "visible_sector_question": "which representative is seen by the selected retarded/source sector",
            "not_the_interpretation": [
                "q79 true and q369 false",
                "q369 retired from the full theory",
                "q79 and q369 as two independent tunable universes",
            ],
        },
        "closed_now": {
            "antiunitary_orbit_is_the_correct_current_object": orbit_is_selected_object,
            "q79_and_q369_both_retained_in_full_orbit": orbit_is_selected_object,
            "q79_q369_not_independent_knobs": orbit_is_selected_object,
            "q369_not_retired_from_full_universe_object": orbit_is_selected_object,
            "visible_representative_selection_identified_as_next_gate": visible_rep_is_not_selected_yet,
        },
        "still_open": {
            "which_representative_is_visible": True,
            "selected_retarded_source_functional_on_orbit": True,
            "selected_source_origin_flags": True,
            "primitive_C1_contractions_on_selected_visible_representative": True,
            "selected_Yukawa_matrices": True,
            "full_SM_closure": True,
        },
        "visible_representative_policy": {
            "allowed": [
                "prove the orbit is selected first",
                "then prove a retarded/source functional selects the visible representative",
                "retain the antiunitary partner as the conjugate presentation of the same full object",
            ],
            "forbidden": [
                "delete q369 as physically wrong",
                "count q79 and q369 as separate parameter choices",
                "choose visible q79 by observed CP sign or measured flavor data",
                "turn selected-source flags on without a source theorem",
            ],
        },
        "next_closing_object": {
            "name": "Selected_Visible_Source_Functional_on_Antiunitary_Orbit_v1",
            "must_prove": [
                "construct a non-observed selected source or retarded-boundary functional on the antiunitary orbit",
                "show the functional acts on the orbit rather than adding a new branch knob",
                "derive which representative is visible, or prove only conjugation-invariant observables are selected at this stage",
                "propagate the selected representative into primitive C1/Yukawa contractions without observed masses or CP inputs",
            ],
        },
        "guardrails": {
            "claims_q79_visible_selected": False,
            "claims_q369_false_or_retired": False,
            "claims_two_independent_universes": False,
            "claims_selected_source_origin": False,
            "claims_full_SM_closure": False,
            "uses_observed_cp_sign_or_masses": False,
            "uses_benchmark_flavor_entries": False,
        },
        "honest_answer": (
            "Yes: the present evidence supports treating q79 and q369 as the "
            "same selected antiunitary orbit of the full theory, not as a "
            "winner and loser. What remains open is the visible-sector "
            "representative selection: a non-observed MTT source or retarded "
            "boundary functional must explain why our visible presentation is "
            "one representative rather than the other, or why only "
            "conjugation-invariant data are visible at this layer."
        ),
    }

    if "--write-certificate" in __import__("sys").argv:
        OUTPUT_CERT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
