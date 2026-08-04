"""Import C1 fiber-class invariance and sharpen the flavor-splitting gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CERTS = ROOT / "certificates"
SM_CERTS = TEXPAPERS / "mtt-sm-parity-closure" / "certificates"

CW_ATTEMPT = CERTS / "selected_qa_su3_m1_cw_operator_source_proof_attempt_certificate.json"
FIBER_INV = SM_CERTS / "selected_routec_fiberclass_observable_invariance_or_gaugefix_certificate.json"
PRIM_AUDIT = SM_CERTS / "selected_routec_primitive_source_selection_audit_certificate.json"
C1_RESPONSE = SM_CERTS / "selected_routec_c1_primitive_response_on_smooth_bn_certificate.json"

OUTPUT = CERTS / "c1_fiberclass_invariance_and_flavor_split_gate_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    cw = load(CW_ATTEMPT)
    fiber = load(FIBER_INV)
    primitive = load(PRIM_AUDIT)
    c1 = load(C1_RESPONSE)

    output = {
        "certificate": "C1FiberClassInvarianceAndFlavorSplitGate",
        "status": "C1_FIBERCLASS_INVARIANCE_IMPORTED_FLAVOR_SPLIT_OPEN",
        "inputs": {
            "cw_prefix": str(CW_ATTEMPT.relative_to(ROOT)),
            "fiber_invariance": str(FIBER_INV),
            "primitive_source_selection": str(PRIM_AUDIT),
            "c1_response": str(C1_RESPONSE),
        },
        "closed_now": {
            "cw_prefix_was_closed": all(cw["closed_prefix"].values()),
            "active_shift_1_1_forced_by_finite_support": primitive["what_closes"][
                "active_shift_1_1_forced_by_finite_support"
            ],
            "fixed_fiber_shifts_one_gauge_class": primitive["what_closes"][
                "fixed_fiber_shifts_reduced_to_one_qutrit_gauge_class"
            ],
            "observable_invariance_under_fixed_fiber_class_for_current_C1_spectrum": fiber[
                "what_closes"
            ]["observable_invariance_under_fixed_fiber_class_for_current_C1_spectrum"],
            "absolute_fiber_origin_not_needed_for_current_spectral_invariants": fiber[
                "what_closes"
            ]["absolute_fiber_origin_not_needed_for_current_spectral_invariants"],
            "canonical_shift0_computation_gauge_allowed": fiber["what_closes"][
                "canonical_shift0_computation_gauge_allowed"
            ],
            "canonical_tensor_zero_response_result_proved_finitely": c1["what_closes"][
                "canonical_tensor_zero_response_result_proved_finitely"
            ],
        },
        "meaning": {
            "what_this_removes": (
                "For the current finite C1 spectral layer, absolute qutrit fiber "
                "origin is not a physical observable: fixed fiber shifts have "
                "identical ranks, singular spectra, traces, and determinant magnitudes."
            ),
            "what_this_does_not_remove": (
                "It does not select a physical fiber origin, prove dotD source "
                "flags, or produce nondegenerate Yukawa/CKM/PMNS data."
            ),
        },
        "not_closed": {
            "selected_noninvariant_C1_primitive_or_vertex_source": fiber["what_remains_open"][
                "selected_noninvariant_C1_primitive_or_vertex_source"
            ],
            "operator_level_basis_transport": fiber["what_remains_open"][
                "operator_level_basis_transport"
            ],
            "higher_order_or_full_strominger_response_support": fiber["what_remains_open"][
                "higher_order_or_full_strominger_response_support"
            ],
            "nondegenerate_yukawa_hierarchy": fiber["what_remains_open"][
                "nondegenerate_yukawa_hierarchy"
            ],
            "CKM_PMNS_CP_from_selected_matrices": fiber["what_remains_open"][
                "CKM_PMNS_CP_from_selected_matrices"
            ],
            "selected_dotD_source_verified": fiber["what_remains_open"][
                "selected_dotD_source_verified"
            ],
            "honest_replay_without_lifted_flags": fiber["what_remains_open"][
                "honest_replay_without_lifted_flags"
            ],
            "full_SM_closure": fiber["what_remains_open"]["full_SM_or_no_knob_closure"],
        },
        "next_closing_object": {
            "name": "Selected_Higher_Order_or_Full_Response_Flavor_Splitting_v1",
            "must_prove": [
                "construct selected corrections that break scalar-permutation degeneracy",
                "derive the non-invariant C1 primitive or full Strominger response support from source data",
                "keep fixed-fiber gauge invariance for observables",
                "replay dotD/C1/Yukawa matrices without observed masses, CKM, PMNS, CP, or benchmark entries",
            ],
        },
        "guardrails": {
            "claims_fiber_origin_physically_selected": False,
            "claims_nonzero_flavor_hierarchy": False,
            "claims_CKM_PMNS_CP_closure": False,
            "claims_selected_dotD_source_verified": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "honest_answer": (
            "The current C1 fixed-fiber ambiguity is harmless for present spectral "
            "observables, so shift 0 is allowed as a computation gauge. But the "
            "same theorem proves the current C1 layer is degenerate. The next "
            "real gate is selected higher-order or full-response flavor splitting."
        ),
    }

    if "--write-certificate" in __import__("sys").argv:
        OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
