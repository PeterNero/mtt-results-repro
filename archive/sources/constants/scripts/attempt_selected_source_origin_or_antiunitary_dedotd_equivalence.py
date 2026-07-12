"""Attempt Selected_Source_Origin_or_Antiunitary_DEDotD_Equivalence_v1."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CERTS = Q79 / "certificates"

IMPORT_GATE = CERTS / "selected_qa_su3_orientation_dedotd_source_attempt_import_certificate.json"
TERMINAL_SOURCE = CERTS / "selected_terminal_monad_lane_source_selector_attempt_certificate.json"

C6_REDUCTION = Q79_CERTS / "iwasawa_c6_orientation_branch_reduction_certificate.json"
C6_COMMON = Q79_CERTS / "iwasawa_c6_common_holonomy_branch_pair_certificate.json"
C6_PHASE = Q79_CERTS / "iwasawa_c6_global_phase_block_certificate.json"
ORIENTATION = Q79_CERTS / "iwasawa_orientation_de_dotd_bridge_certificate.json"

OUTPUT_CERT = CERTS / "selected_source_origin_or_antiunitary_dedotd_equivalence_attempt_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    import_gate = load(IMPORT_GATE)
    terminal = load(TERMINAL_SOURCE)
    c6_reduction = load(C6_REDUCTION)
    c6_common = load(C6_COMMON)
    c6_phase = load(C6_PHASE)
    orientation = load(ORIENTATION)

    c6_global_pair_closed = (
        c6_reduction["what_this_closes"]["independent_channel_signs_removed"] is True
        and c6_common["what_this_closes"]["C6_orientation_reduced_to_global_conjugate_pair"] is True
        and c6_phase["calculation_results"]["global_pair_are_complex_conjugates"] is True
        and c6_phase["what_this_closes"]["per_channel_C6_phase_knobs_removed"] is True
    )
    operator_equivalence_open = (
        orientation["still_open"]["antiunitary_equivalence_or_retarded_branch_selection_proof"] is True
        and import_gate["not_closed"]["selected_D_E_or_dotD_source_flags"] is True
        and import_gate["not_closed"]["unique_m1_vs_m2_selection"] is True
    )
    source_origin_route_open = (
        import_gate["not_closed"]["selected_source_origin"] is True
        and terminal["not_closed"]["same_source_D_E_dotD_Riesz_Green"] is True
    )

    output = {
        "certificate": "SelectedSourceOriginOrAntiunitaryDEDotDEquivalenceAttempt",
        "status": "SOURCE_ORIGIN_OR_ANTIUNITARY_DEDOTD_EQUIVALENCE_REDUCED_OPERATOR_EQUIVALENCE_OPEN",
        "inputs": {
            "orientation_dedotd_import": str(IMPORT_GATE.relative_to(ROOT)),
            "terminal_lane_source_reduction": str(TERMINAL_SOURCE.relative_to(ROOT)),
            "q79_c6_orientation_reduction": str(C6_REDUCTION),
            "q79_c6_common_holonomy_pair": str(C6_COMMON),
            "q79_c6_global_phase_block": str(C6_PHASE),
            "q79_orientation_de_dotd_bridge": str(ORIENTATION),
        },
        "closed_now": {
            "C6_branch_space_reduced_to_global_conjugate_pair": c6_global_pair_closed,
            "independent_channel_phase_knobs_removed": c6_phase["what_this_closes"][
                "per_channel_C6_phase_knobs_removed"
            ],
            "q79_q369_labels_are_complex_conjugates_at_C6_phase_level": c6_phase[
                "calculation_results"
            ]["global_pair_are_complex_conjugates"],
            "not_two_unrelated_universes": orientation["what_this_closes"][
                "two_unrelated_universe_interpretation_rejected"
            ],
            "finite_DE_dotD_branch_packets_reach_validator_layer": import_gate["closed_now"][
                "finite_branch_data_reaches_DE_Green_dotD_layer"
            ],
        },
        "route_A_selected_source_origin": {
            "status": "OPEN",
            "first_missing": [
                "selected visible bundle/twisted-gerbe/Route-C source origin",
                "selected D_E action source flags",
                "selected dotD alpha1 same-branch driver",
                "projector retention and operator Pic0 rule",
            ],
            "would_close": [
                "turn q79 or q369 orientation packet validator to PASS for exactly one branch",
                "supply same-source base-order breaker for L3-K2",
                "feed primitive C1/Yukawa contractions",
            ],
        },
        "route_B_antiunitary_then_retarded_selection": {
            "status": "OPEN",
            "what_is_already_closed": [
                "C6 phase pair is global conjugate",
                "mixed quark/lepton C6 choices are rejected",
                "per-channel C6 phase knobs are removed",
            ],
            "first_missing": [
                "operator-level antiunitary map between q79 and q369 D_E domains",
                "proof Green/Riesz/projectors transform under the same antiunitary map",
                "proof dotD_alpha1 and primitive C1 contractions transform by conjugation",
                "non-observed retarded/source boundary selector for one representative",
            ],
        },
        "not_closed": {
            "selected_source_origin": source_origin_route_open,
            "operator_level_antiunitary_equivalence": operator_equivalence_open,
            "retarded_boundary_selector_for_orientation": True,
            "selected_D_E_dotD_source_flags": True,
            "same_source_base_order_breaker": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "next_executable_artifact": {
            "name": "Antiunitary_DEDotD_Equivalence_Test_v1",
            "must_compare": [
                "q79 and q369 D_E action slots sector by sector",
                "Gram/stiffness/projector/Green packets under conjugation",
                "dotD_alpha1 source vectors and horizontal responses under conjugation",
                "primitive C1 contractions once available",
            ],
            "acceptance": [
                "PASS if all operator packets are related by one antiunitary branch map and no observed CP/mass input is used",
                "otherwise route A selected-source origin remains mandatory",
            ],
        },
        "guardrails": {
            "claims_selected_source_origin": False,
            "claims_operator_antiunitary_equivalence_proved": False,
            "claims_retarded_orientation_selected": False,
            "claims_selected_D_E_dotD": False,
            "claims_full_SM_closure": False,
            "uses_observed_cp_sign_or_masses": False,
            "uses_benchmark_flavor_entries": False,
        },
        "honest_answer": (
            "C6 phase data already reduce q79/q369 to one global conjugate pair, "
            "not independent knobs.  What remains open is stronger: operator-level "
            "antiunitary equivalence for D_E, Green/Riesz, dotD, and later C1 "
            "contractions, or a selected source origin that directly chooses one branch."
        ),
    }

    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
