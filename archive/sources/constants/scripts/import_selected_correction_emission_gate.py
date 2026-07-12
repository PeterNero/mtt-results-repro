"""Import the selected correction-emission gate frontier."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CERTS = ROOT / "certificates"
SM = TEXPAPERS / "mtt-sm-parity-closure"

HIGHER_ORDER = CERTS / "higher_order_flavor_splitting_criterion_import_certificate.json"
FIRST_SEARCH_CERT = SM / "certificates" / "selected_routec_first_correction_search_or_galerkin_run_certificate.json"
FIRST_SEARCH_CANDIDATE = SM / "candidate_data" / "selected_routec_first_correction_search_or_galerkin_run.candidate.json"
PRIMITIVE_CERT = SM / "certificates" / "selected_routec_selected_primitive_emission_search_certificate.json"

OUTPUT = CERTS / "selected_correction_emission_gate_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    higher = load(HIGHER_ORDER)
    first_cert = load(FIRST_SEARCH_CERT)
    first_candidate = load(FIRST_SEARCH_CANDIDATE)
    primitive = load(PRIMITIVE_CERT)

    lane_a = first_candidate["parallel_lanes"]["lane_A_qutrit_weyl_correction_search"]
    lane_b = first_candidate["parallel_lanes"]["lane_B_galerkin_replay"]
    representative = lane_a["representative"]

    output = {
        "certificate": "SelectedCorrectionEmissionGate",
        "status": "SELECTED_CORRECTION_EMISSION_GATE_REDUCED_NONIDENTITY_RHOE_AND_BN_CONSTRUCTION_OPEN",
        "inputs": {
            "higher_order_flavor_gate": str(HIGHER_ORDER.relative_to(ROOT)),
            "sm_first_search_certificate": str(FIRST_SEARCH_CERT),
            "sm_first_search_candidate": str(FIRST_SEARCH_CANDIDATE),
            "sm_primitive_emission_search": str(PRIMITIVE_CERT),
        },
        "closed_now": {
            "higher_order_flavor_gate_imported": higher["status"]
            == "HIGHER_ORDER_FLAVOR_SPLITTING_CRITERION_IMPORTED_SELECTED_EMISSION_OPEN",
            "diagnostic_qutrit_splitter_exists": lane_a["diagnostic_splitter_found"],
            "diagnostic_splitter_not_promoted": lane_a["selected_by_mtt"] is False
            and lane_a["promotion_allowed"] is False,
            "diagnostic_splitter_uses_no_observed_targets": first_candidate["target_fitting_used"] is False
            and first_cert["what_closes"]["target_fitting_excluded"] is True,
            "mass_mixing_cp_diagnostic_tests_nonzero": all(
                value > 0.0 for value in representative["mass_split_traceless_norm_sq"].values()
            )
            and representative["ckm_commutator_norm_sq"] > 0.0
            and representative["pmns_commutator_norm_sq"] > 0.0
            and representative["cp_odd_trace_commutator_cubed_imag"] != 0.0,
            "first_galerkin_replay_executed": first_cert["what_closes"]["first_galerkin_replay_executed"],
            "formal_lift_rejected_as_proof": primitive["what_closes"]["formal_lift_rejected_as_proof"],
            "identity_rhoE_rejected_as_selected_payload": primitive["what_closes"][
                "identity_rhoE_rejected_as_selected_payload"
            ],
            "strict_primitive_search_found_no_legal_emission": primitive["status"]
            == "MTT_SELECTED_ROUTEC_PRIMITIVE_EMISSION_SEARCH_EXECUTED_NO_LEGAL_EMISSION_FOUND",
            "selected_deck_scaffold_identified": primitive["what_closes"]["selected_deck_scaffold_identified"],
        },
        "diagnostic_representative": {
            "candidate_count": lane_a["candidate_count"],
            "mass_split_traceless_norm_sq": representative["mass_split_traceless_norm_sq"],
            "ckm_commutator_norm_sq": representative["ckm_commutator_norm_sq"],
            "pmns_commutator_norm_sq": representative["pmns_commutator_norm_sq"],
            "cp_odd_trace_commutator_cubed_imag": representative[
                "cp_odd_trace_commutator_cubed_imag"
            ],
            "sector_labels": {
                "u": representative["u_correction_label"],
                "d": representative["d_correction_label"],
                "e": representative["e_correction_label"],
                "nuD": representative["nuD_correction_label"],
            },
        },
        "reduction": {
            "selected_emission_not_found_in_current_artifacts": True,
            "why_current_artifacts_do_not_close": [
                "Lane A is an algebraic diagnostic search, not a selected MTT emission.",
                "Lane B has a formal-lift diagnostic, but the honest root still fails selected-source, selected dotD, and alpha1-driver gates.",
                "The strict primitive search found no legal emission in the current identity-rhoE/current-BN artifacts.",
            ],
            "next_construction": "Selected_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_Construction_v1",
            "construction_requirements": [
                "construct non-identity selected projective or twisted rho_E from q79/F,m=1 data",
                "construct quotient-valid non-invariant Galerkin B_N from the same selected branch",
                "emit finite correction matrices or Galerkin values from those selected data",
                "replay mass splitting, CKM/PMNS noncommutation, and CP tests without lifted flags",
            ],
        },
        "not_closed": {
            "selected_correction_matrix_source": first_cert["what_remains_open"][
                "selected_correction_matrix_source"
            ],
            "selected_galerkin_values": first_cert["what_remains_open"]["selected_galerkin_values"],
            "honest_replay_without_lifted_flags": first_cert["what_remains_open"][
                "honest_replay_without_lifted_flags"
            ],
            "selected_dotD_source_verified": first_cert["what_remains_open"][
                "selected_dotD_source_verified"
            ],
            "alpha1_driver_verified": first_cert["what_remains_open"]["alpha1_driver_verified"],
            "finite_C1_Hessian_and_deltaTheta": first_cert["what_remains_open"][
                "finite_C1_Hessian_and_deltaTheta"
            ],
            "promoted_non_degenerate_yukawa_hierarchy": first_cert["what_remains_open"][
                "promoted_non_degenerate_yukawa_hierarchy"
            ],
            "promoted_CKM_PMNS_CP": first_cert["what_remains_open"]["promoted_CKM_PMNS_CP"],
            "full_SM_closure": primitive["what_remains_open"]["full_SM_or_no_knob_closure"],
        },
        "guardrails": {
            "claims_selected_flavor_hierarchy": False,
            "claims_selected_CKM_PMNS_CP": False,
            "claims_selected_correction_emission": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "honest_answer": (
            "The algebraic obstruction has moved: a nondegenerate, noncommuting, CP-odd "
            "finite correction pattern exists without target fitting, and existing primitive "
            "artifacts have been searched strictly. What remains is selected emission: build "
            "non-identity rho_E and quotient-valid B_N from the same q79/F,m=1 branch and let "
            "them emit the correction matrices or Galerkin values."
        ),
    }

    if "--write-certificate" in sys.argv:
        OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
