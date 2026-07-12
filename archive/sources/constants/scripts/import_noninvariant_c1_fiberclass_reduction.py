"""Import the non-invariant C1 primitive search and fiber-class reduction."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CERTS = ROOT / "certificates"
SM = TEXPAPERS / "mtt-sm-parity-closure"

PREFIX = CERTS / "routec_rhoe_bn_operator_prefix_import_certificate.json"
LOCAL_FIBER = CERTS / "c1_fiberclass_invariance_and_flavor_split_gate_certificate.json"
SEARCH_CERT = SM / "certificates" / "selected_routec_noninvariant_c1_primitive_search_certificate.json"
SEARCH_CANDIDATE = SM / "candidate_data" / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
FIBER_CERT = SM / "certificates" / "selected_routec_primitive_source_selection_audit_certificate.json"
FIBER_CANDIDATE = SM / "candidate_data" / "selected_routec_primitive_source_selection_audit.candidate.json"

OUTPUT = CERTS / "noninvariant_c1_fiberclass_reduction_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prefix = load(PREFIX)
    local_fiber = load(LOCAL_FIBER)
    search_cert = load(SEARCH_CERT)
    search = load(SEARCH_CANDIDATE)
    fiber_cert = load(FIBER_CERT)
    fiber = load(FIBER_CANDIDATE)

    active = fiber["active_shift_theorem"]["enumeration"]
    fixed = fiber["fiber_class_theorem"]["fixed_fiber_shifts"]
    envelope = fiber["fiber_class_theorem"]["all_fiber_envelope"]

    output = {
        "certificate": "NonInvariantC1FiberClassReduction",
        "status": "NONINVARIANT_C1_FIBERCLASS_REDUCTION_IMPORTED_SELECTED_SOURCE_OPEN",
        "inputs": {
            "local_routec_prefix": str(PREFIX.relative_to(ROOT)),
            "local_current_fiber_invariance_gate": str(LOCAL_FIBER.relative_to(ROOT)),
            "sm_noninvariant_c1_search": str(SEARCH_CERT),
            "sm_noninvariant_c1_candidate": str(SEARCH_CANDIDATE),
            "sm_primitive_source_selection": str(FIBER_CERT),
            "sm_primitive_source_candidate": str(FIBER_CANDIDATE),
        },
        "closed_now": {
            "canonical_zero_repaired_at_candidate_level": search_cert["what_closes"][
                "canonical_zero_repaired_at_candidate_level"
            ],
            "finite_noninvariant_C1_candidate_matrices_emitted": search_cert["what_closes"][
                "finite_noninvariant_C1_candidate_matrices_emitted"
            ],
            "active_shift_1_1_forced_by_finite_support": fiber_cert["what_closes"][
                "active_shift_1_1_forced_by_finite_support"
            ],
            "fixed_fiber_shifts_one_qutrit_gauge_class": fiber_cert["what_closes"][
                "fixed_fiber_shifts_reduced_to_one_qutrit_gauge_class"
            ],
            "all_fiber_envelope_retired": fiber_cert["what_closes"][
                "all_fiber_envelope_retired_as_fixed_single_charge_candidate"
            ],
            "no_observed_flavor_data_used": search["target_fitting_used"] is False
            and fiber["target_fitting_used"] is False,
            "local_current_C1_fiber_invariance_agrees": local_fiber["closed_now"][
                "fixed_fiber_shifts_one_gauge_class"
            ],
        },
        "finite_result": {
            "nonzero_unselected_candidates_found": search["calculation_results"][
                "nonzero_unselected_candidates_found"
            ],
            "all_four_tested_candidates_nonzero": search["calculation_results"][
                "all_four_tested_candidates_nonzero"
            ],
            "minimal_active_shift_required": search["search_rule"]["minimal_active_shift_required"],
            "all_active_shifts_tested": active["all_active_shifts_tested"],
            "nonzero_active_shifts": active["nonzero_active_shifts"],
            "active_shift_necessary_and_sufficient_for_nonzero": active[
                "active_shift_necessary_and_sufficient_for_nonzero"
            ],
            "fixed_fiber_ranks": fixed["ranks"],
            "fixed_fiber_frobenius_norms": fixed["frobenius_norms"],
            "all_fiber_rank": envelope["rank"],
            "all_fiber_frobenius_norms": envelope["frobenius_norms"],
            "representative_max_abs_entry": search["candidate_primitives"][0]["summary"]["u"][
                "max_abs_entry"
            ],
        },
        "meaning": {
            "source_has_period_three_projective_class": fiber["source_implication"]["qutrit_source_support"][
                "source_level_projective_class_selected"
            ],
            "operator_level_projective_class_selected": fiber["source_implication"]["qutrit_source_support"][
                "operator_level_projective_class_selected"
            ],
            "selected_noninvariant_primitive_source_proved": fiber["source_implication"][
                "selected_noninvariant_primitive_source_proved"
            ],
            "absolute_fiber_shift_selected": fiber["source_implication"]["absolute_fiber_shift_selected"],
            "observable_invariance_under_fiber_class_proved": fiber["source_implication"][
                "observable_invariance_under_fiber_class_proved"
            ],
        },
        "not_closed": {
            "selected_noninvariant_C1_primitive_or_vertex_source": fiber_cert["what_remains_open"][
                "selected_noninvariant_C1_primitive_or_vertex_source"
            ],
            "observable_invariance_under_fixed_fiber_class": fiber_cert["what_remains_open"][
                "observable_invariance_under_fixed_fiber_class"
            ],
            "absolute_fiber_origin_gauge_fix": fiber_cert["what_remains_open"][
                "absolute_fiber_origin_gauge_fix"
            ],
            "selected_basis_transport_theorem": fiber_cert["what_remains_open"][
                "selected_basis_transport_theorem"
            ],
            "selected_dotD_source_verified": fiber_cert["what_remains_open"][
                "selected_dotD_source_verified"
            ],
            "alpha1_driver_verified": fiber_cert["what_remains_open"]["alpha1_driver_verified"],
            "honest_replay_without_lifted_flags": fiber_cert["what_remains_open"][
                "honest_replay_without_lifted_flags"
            ],
            "yukawa_CKM_PMNS_magnitudes": fiber_cert["what_remains_open"][
                "yukawa_CKM_PMNS_magnitudes"
            ],
            "full_SM_closure": fiber_cert["what_remains_open"]["full_SM_or_no_knob_closure"],
        },
        "next_closing_object": {
            "name": "Selected_C1_Response_Operator_Emission_or_FiberClass_Invariant_Observable_v1",
            "must_prove": [
                "derive the active-shift (1,1) primitive, vertex, or basis transport from the selected q79/F,m=1 source",
                "prove downstream C1/Yukawa observables are invariant under the fixed qutrit fiber gauge class, or select a physical fiber origin",
                "promote selected dotD and alpha1 source flags without formal lift",
                "emit nonzero selected C1 matrices before claiming flavor closure",
            ],
        },
        "guardrails": {
            "claims_selected_C1_source": False,
            "claims_physical_fiber_origin": False,
            "claims_nonzero_selected_C1_response": False,
            "claims_yukawa_CKM_PMNS_magnitudes": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
        },
        "honest_answer": (
            "The finite C1 obstruction is now reduced to source selection: active shift "
            "(1,1) is forced, fixed qutrit fiber shifts are one gauge class, and the "
            "all-fiber envelope is not a fixed single-charge primitive. What remains "
            "is proving selected source emission or fiber-class-invariant downstream observables."
        ),
        "previous_prefix_status": prefix["status"],
    }

    if "--write-certificate" in sys.argv:
        OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
