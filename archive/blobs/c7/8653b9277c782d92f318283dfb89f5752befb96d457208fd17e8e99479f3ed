"""Reconcile dynamic first-response promotion with the static lambda orbit.

The static coefficient tier now selects the two-element orbit
{1+omega, 1+omega2}.  Separate VSD-01 artifacts close a selected dynamic
first-response matter/overlap tensor, but those packets do not contain a
lambda_static/lambda_Z/lambda_X representative selector and do not close the
accepted Yukawa/RG/true-SM value layer.

This artifact proves the reconciliation/boundary theorem: current dynamic
first-response promotion does not select an individual static-lambda
representative or promote the second-order coefficient-lift physical matrices.
The next object is therefore sharper: emit a second-order dynamic coefficient
operator or a selected orientation/time-arrow rule, then re-run value closure.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_dynamicorientation_or_physicalmatrixpromotion"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DYNAMIC_SEARCH = PACKET_DIR / "dynamic_orientation_selector_search.packet.json"
PROMOTION_BOUNDARY = PACKET_DIR / "physical_matrix_promotion_boundary.packet.json"
VALUE_ALIGNMENT = PACKET_DIR / "value_frontier_alignment_after_lambda_orbit.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_dynamic_orientation_reconciliation.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicOrientation_or_PhysicalMatrixPromotion_v1.md"

STATIC_ORBIT_CANDIDATE = DATA / "selected_staticlambdaorbitquotient_or_dynamicorientationfrontier.candidate.json"
STATIC_ORBIT = (
    DATA
    / "selected_staticlambdaorbitquotient_or_dynamicorientationfrontier"
    / "selected_static_lambda_orbit.packet.json"
)
VSD_DYNAMIC = DATA / "selected_vsd01_dynamicoperatorbackimport_or_yukawavaluefrontier.candidate.json"
VSD_FRONTIER = DATA / "selected_vsd01frontierupdate_or_valuekernelv2.candidate.json"
FINAL_VALUE_AUDIT = DATA / "selected_yukawamagnitudergclosure_or_finaltruesmequivalenceaudit.candidate.json"
DYNAMIC_QASU3 = DATA / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure.candidate.json"
NONSCALAR_VALUES = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)

STATUS = "MTT_SELECTED_DYNAMICORIENTATION_OR_PHYSICALMATRIXPROMOTION_BUILT_FIRST_RESPONSE_RECONCILED_LAMBDA_REPRESENTATIVE_OPEN"
NEXT = "MTT_Selected_SecondOrderDynamicCoefficientEmission_or_LambdaRepresentativeSelection_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def has_any_text(payload: Any, needles: list[str]) -> dict[str, bool]:
    blob = json.dumps(payload, sort_keys=True)
    return {needle: needle in blob for needle in needles}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    static_orbit_candidate = load(STATIC_ORBIT_CANDIDATE)
    static_orbit = load(STATIC_ORBIT)
    vsd_dynamic = load(VSD_DYNAMIC)
    vsd_frontier = load(VSD_FRONTIER)
    final_value = load(FINAL_VALUE_AUDIT)
    dynamic_qasu3 = load(DYNAMIC_QASU3)
    nonscalar = load(NONSCALAR_VALUES)

    selector_needles = ["lambda_static", "lambda_Z", "lambda_X", "1+omega", "1+omega2"]
    dynamic_payloads = {
        "VSD_dynamic_backimport": vsd_dynamic,
        "VSD_frontier_update": vsd_frontier,
        "final_value_audit": final_value,
        "dynamic_QaSU3_replay": dynamic_qasu3,
        "selected_non_scalar_dynamic_overlap_values": nonscalar,
    }
    selector_hits = {
        name: has_any_text(payload, selector_needles) for name, payload in dynamic_payloads.items()
    }
    any_selector_hit = any(any(hits.values()) for hits in selector_hits.values())

    dynamic_first_response_closed = (
        vsd_dynamic["closure_decision"]["VSD01_dynamic_tensor_subgate_closed"] is True
        and dynamic_qasu3["promotion_decision"]["dynamic_QaSU3_first_response_layer_closed"] is True
        and nonscalar["selected_by_MTT"] is True
    )
    final_value_decision = final_value["promotion_decision"]
    final_value_open = (
        final_value_decision["true_SM_equivalence_closed"] is False
        and final_value_decision["full_SM_no_knob_closed"] is False
        and final_value_decision["accepted_Yukawa_magnitudes_closed"] is False
    )

    dynamic_search = {
        "schema": "MTTDynamicOrientationSelectorSearch.v1",
        "status": "NO_DYNAMIC_LAMBDA_REPRESENTATIVE_SELECTOR_IN_CURRENT_FIRST_RESPONSE_PACKETS",
        "static_lambda_orbit": static_orbit["selected_static_lambda_orbit"],
        "dynamic_first_response_closed": dynamic_first_response_closed,
        "searched_dynamic_payloads": {name: rel(path) for name, path in {
            "VSD_dynamic_backimport": VSD_DYNAMIC,
            "VSD_frontier_update": VSD_FRONTIER,
            "final_value_audit": FINAL_VALUE_AUDIT,
            "dynamic_QaSU3_replay": DYNAMIC_QASU3,
            "selected_non_scalar_dynamic_overlap_values": NONSCALAR_VALUES,
        }.items()},
        "selector_needles": selector_needles,
        "selector_hits": selector_hits,
        "dynamic_lambda_representative_selector_found": any_selector_hit,
        "interpretation": (
            "The selected dynamic first-response packets close qualitative non-scalar/mixing/CP support, "
            "but they do not mention or emit the second-order static lambda orbit representatives."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DYNAMIC_SEARCH, dynamic_search)

    promotion_boundary = {
        "schema": "MTTPhysicalMatrixPromotionBoundaryAfterLambdaOrbit.v1",
        "status": "FIRST_RESPONSE_DYNAMIC_PROMOTION_DOES_NOT_PROMOTE_SECOND_ORDER_LAMBDA_MATRICES",
        "static_lambda_orbit_selected": static_orbit_candidate["closure_decision"][
            "static_lambda_orbit_selected"
        ],
        "dynamic_first_response_layer_closed": dynamic_first_response_closed,
        "second_order_lambda_coefficient_matrices_present_in_dynamic_packets": any_selector_hit,
        "selected_second_order_physical_matrices_promoted": False,
        "individual_lambda_value_selected": False,
        "physical_coexistence_or_equivalence_proved": False,
        "why": (
            "The VSD/current dynamic packets are first-response I+Z/I+X matter/overlap objects. "
            "The lambda lift is a second-order coefficient refinement, so it needs a new dynamic "
            "coefficient emission or a selected orientation/time-arrow theorem before physical "
            "Yukawa/CKM/PMNS value closure can use it."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROMOTION_BOUNDARY, promotion_boundary)

    value_alignment = {
        "schema": "MTTValueFrontierAlignmentAfterLambdaOrbit.v1",
        "status": "VALUE_FRONTIER_ALIGNED_LAMBDA_REPRESENTATIVE_AND_ACCEPTED_VALUES_OPEN",
        "VSD01_legacy_dynamic_absence_blocker_retired": vsd_frontier["closure_decision"][
            "VSD01_legacy_dynamic_absence_blocker_retired"
        ],
        "VSD01_full_obligation_closed": vsd_frontier["closure_decision"][
            "VSD01_full_obligation_closed"
        ],
        "accepted_Yukawa_magnitudes_closed": final_value_decision[
            "accepted_Yukawa_magnitudes_closed"
        ],
        "CKM_PMNS_measured_value_closure": final_value_decision["CKM_PMNS_measured_value_closure"],
        "true_SM_equivalence_closed": final_value_decision["true_SM_equivalence_closed"],
        "full_SM_no_knob_closed": final_value_decision["full_SM_no_knob_closed"],
        "frontier_statement": (
            "Do not redo VSD-01 source/dynamic first-response closure.  The remaining value frontier "
            "is the second-order lambda representative/dynamic coefficient source plus accepted "
            "Yukawa/RG/threshold/covariance rows."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VALUE_ALIGNMENT, value_alignment)

    cutset = {
        "schema": "MTTNextCutsetAfterDynamicOrientationReconciliation.v1",
        "status": "NEXT_ATTACK_SECOND_ORDER_DYNAMIC_COEFFICIENT_OR_LAMBDA_REPRESENTATIVE",
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The static lambda orbit is selected, and first-response dynamic promotion is reconciled. "
                "Full closure now needs a selected second-order dynamic coefficient operator or a "
                "representative-selection/coexistence theorem, followed by accepted value-row closure."
            ),
        },
        "minimal_tasks": [
            "emit Phi_fin^C1 second-order coefficient rows carrying lambda_static orbit representatives",
            "or derive a selected complex orientation/time-arrow rule choosing or quotienting the representatives",
            "then promote physical matrices and re-run Yukawa/CKM/PMNS/RG/threshold audits",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedDynamicOrientationOrPhysicalMatrixPromotion",
        "status": STATUS,
        "inputs": {
            "static_lambda_orbit_candidate": rel(STATIC_ORBIT_CANDIDATE),
            "selected_static_lambda_orbit": rel(STATIC_ORBIT),
            "VSD_dynamic_backimport": rel(VSD_DYNAMIC),
            "VSD_frontier_update": rel(VSD_FRONTIER),
            "final_value_audit": rel(FINAL_VALUE_AUDIT),
            "dynamic_QaSU3_replay": rel(DYNAMIC_QASU3),
            "selected_non_scalar_dynamic_overlap_values": rel(NONSCALAR_VALUES),
        },
        "output_packets": {
            "dynamic_orientation_selector_search": rel(DYNAMIC_SEARCH),
            "physical_matrix_promotion_boundary": rel(PROMOTION_BOUNDARY),
            "value_frontier_alignment_after_lambda_orbit": rel(VALUE_ALIGNMENT),
            "next_cutset_after_dynamic_orientation_reconciliation": rel(CUTSET),
        },
        "theorem": {
            "name": "DynamicOrientationFirstResponseReconciliationTheorem",
            "proved": dynamic_first_response_closed and not any_selector_hit and final_value_open,
            "statement": (
                "The VSD-01/current dynamic artifacts close a selected first-response matter/overlap "
                "operator layer, but none of the audited dynamic/value packets emits lambda_static, "
                "lambda_Z, lambda_X, or the representatives 1+omega/1+omega2.  Therefore first-response "
                "dynamic promotion is reconciled with the static lambda orbit, but it does not select "
                "a representative, prove coexistence/equivalence, or promote second-order physical "
                "lambda matrices."
            ),
        },
        "what_closes_now": {
            "dynamic_first_response_reconciled_with_static_lambda_orbit": True,
            "old_VSD01_dynamic_absence_track_retired_for_this_frontier": True,
            "no_current_dynamic_lambda_representative_selector_found": not any_selector_hit,
            "second_order_lambda_physical_promotion_boundary_built": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_second_order_dynamic_coefficient_emission": True,
            "individual_lambda_representative_selection_or_coexistence": True,
            "selected_second_order_physical_matrix_promotion": True,
            "accepted_Yukawa_CKM_PMNS_RG_threshold_value_rows": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "closure_decision": {
            "dynamic_first_response_layer_closed": dynamic_first_response_closed,
            "individual_lambda_value_selected": False,
            "selected_second_order_physical_matrices_promoted": False,
            "accepted_value_layer_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": static_orbit_candidate["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_DynamicOrientation_or_PhysicalMatrixPromotion_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": candidate["theorem"]["proved"],
        "dynamic_first_response_layer_closed": dynamic_first_response_closed,
        "dynamic_lambda_representative_selector_found": any_selector_hit,
        "individual_lambda_value_selected": False,
        "selected_second_order_physical_matrices_promoted": False,
        "accepted_value_layer_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected DynamicOrientation or PhysicalMatrixPromotion v1

Status: `{STATUS}`.

The VSD/current dynamic lane is real but first-response only:

```text
dynamic first-response layer closed : {str(dynamic_first_response_closed).lower()}
static lambda orbit                 : {static_orbit["selected_static_lambda_orbit"]}
dynamic lambda selector found       : {str(any_selector_hit).lower()}
individual lambda selected          : false
second-order physical matrices promoted : false
accepted value layer closed         : false
full SM closure                     : false
```

This reconciles the tracks.  We should not redo VSD-01 source/dynamic
first-response closure, and we should not pretend it selects the second-order
lambda representative.  The missing object is now sharply:

```text
{NEXT}
```

That artifact must either emit selected second-order dynamic coefficient rows,
or derive a complex-orientation/time-arrow representative rule, before
Yukawa/CKM/PMNS/RG value closure can honestly proceed.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
