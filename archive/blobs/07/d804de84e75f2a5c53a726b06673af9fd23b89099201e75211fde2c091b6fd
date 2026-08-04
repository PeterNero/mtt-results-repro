"""Import higher-order/full-response flavor splitting frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CERTS = ROOT / "certificates"
SM_CERTS = TEXPAPERS / "mtt-sm-parity-closure" / "certificates"

FIBER_GATE = CERTS / "c1_fiberclass_invariance_and_flavor_split_gate_certificate.json"
SPLIT_CRITERION = SM_CERTS / "selected_routec_higherorder_fullresponse_flavor_splitting_certificate.json"
FIRST_SEARCH = SM_CERTS / "selected_routec_first_correction_search_or_galerkin_run_certificate.json"

OUTPUT = CERTS / "higher_order_flavor_splitting_criterion_import_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    fiber = load(FIBER_GATE)
    split = load(SPLIT_CRITERION)
    first = load(FIRST_SEARCH)

    output = {
        "certificate": "HigherOrderFlavorSplittingCriterionImport",
        "status": "HIGHER_ORDER_FLAVOR_SPLITTING_CRITERION_IMPORTED_SELECTED_EMISSION_OPEN",
        "inputs": {
            "local_fiber_gate": str(FIBER_GATE.relative_to(ROOT)),
            "sm_splitting_criterion": str(SPLIT_CRITERION),
            "sm_first_search": str(FIRST_SEARCH),
        },
        "closed_now": {
            "current_scalar_permutation_layer_no_go_proved": split["what_closes"][
                "current_scalar_permutation_layer_no_go_proved"
            ],
            "higher_order_splitting_criterion_proved": split["what_closes"][
                "higher_order_splitting_criterion_proved"
            ],
            "full_response_acceptance_tests_locked": split["what_closes"][
                "full_response_acceptance_tests_locked"
            ],
            "diagnostic_splitter_found_without_observed_targets": first["what_closes"][
                "diagnostic_splitter_found_without_observed_targets"
            ],
            "first_correction_matrix_search_executed": first["what_closes"][
                "first_correction_matrix_search_executed"
            ],
            "first_galerkin_replay_executed": first["what_closes"][
                "first_galerkin_replay_executed"
            ],
            "fiberclass_gate_agrees_flavor_split_open": fiber["not_closed"][
                "nondegenerate_yukawa_hierarchy"
            ],
        },
        "splitting_tests": {
            "mass_splitting": "traceless part of H_s^(r) = correction to Y_s Y_s* is nonzero",
            "CKM_or_PMNS": "sector Hermitian corrections are not simultaneously diagonalizable",
            "CP": "selected complex correction data have nonzero CP-odd invariant",
        },
        "not_closed": {
            "selected_correction_matrix_source": first["what_remains_open"][
                "selected_correction_matrix_source"
            ],
            "selected_galerkin_values": first["what_remains_open"][
                "selected_galerkin_values"
            ],
            "honest_replay_without_lifted_flags": first["what_remains_open"][
                "honest_replay_without_lifted_flags"
            ],
            "selected_dotD_source_verified": first["what_remains_open"][
                "selected_dotD_source_verified"
            ],
            "alpha1_driver_verified": first["what_remains_open"][
                "alpha1_driver_verified"
            ],
            "finite_C1_Hessian_and_deltaTheta": first["what_remains_open"][
                "finite_C1_Hessian_and_deltaTheta"
            ],
            "promoted_non_degenerate_yukawa_hierarchy": first["what_remains_open"][
                "promoted_non_degenerate_yukawa_hierarchy"
            ],
            "promoted_CKM_PMNS_CP": first["what_remains_open"][
                "promoted_CKM_PMNS_CP"
            ],
            "full_SM_closure": first["what_remains_open"]["full_SM_or_no_knob_closure"],
        },
        "next_closing_object": {
            "name": "Selected_Correction_Matrix_Source_or_Galerkin_Value_Emission_v1",
            "must_prove": [
                "derive correction matrices from selected Phi_fin/Galerkin emission, not a diagnostic search",
                "satisfy mass-splitting, commutator, and CP tests on selected data",
                "prove selected dotD and alpha1 driver flags without lifted flags",
                "avoid observed masses, CKM, PMNS, CP, and benchmark matrix entries",
            ],
        },
        "guardrails": {
            "claims_selected_flavor_hierarchy": False,
            "claims_selected_CKM_PMNS_CP": False,
            "claims_diagnostic_splitter_is_selected": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "honest_answer": (
            "The flavor-splitting criterion is now closed and a diagnostic finite "
            "splitter exists without observed targets. The missing step is not "
            "algebraic possibility; it is selected emission of the correction "
            "matrices or Galerkin values with honest source flags."
        ),
    }

    if "--write-certificate" in __import__("sys").argv:
        OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
