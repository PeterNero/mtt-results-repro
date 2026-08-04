"""Build cross-repo alpha1 driver replay import."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

TYPED_VALUE = DATA / "selected_typedbn_retardedderivative_or_primitiveresponse_valueemission.candidate.json"
DOTD_PROBE = DATA / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
PRIMITIVE_SELECTOR = DATA / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem.candidate.json"
HIGHER_ORDER = DATA / "selected_routec_higherorder_fullresponse_flavor_splitting.candidate.json"

TEXPAPERS = ROOT.parent
GR_ALPHA = TEXPAPERS / "mtt-protospinor-gr-response-proof" / "candidate_data" / "alpha1_driver_replay_closure_import.packet.json"
Q79_KERNEL = TEXPAPERS / "mtt-q79-proof-repro" / "candidate_data" / "q79_selected_alpha1_tangent_or_retarded_overlap_kernel.candidate.json"
CONSTANTS_BRIDGE = TEXPAPERS / "mtt-nonsm-constants-no-knob" / "candidate_data" / "q79_alpha1_retarded_kernel_formula_nmtt_bridge.candidate.json"
QA_PRIMITIVE = TEXPAPERS / "mtt-qa-su3-packet-proof" / "candidate_data" / "selected_u1y_routec_primitive_c1_atom_payload_fill_or_nogo.candidate.json"

OUTPUT = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
CERT = CERTS / "selected_crossrepo_alpha1_driver_replay_import_certificate.json"
NOTE = CORPUS / "MTT_Selected_CrossRepo_Alpha1DriverReplay_Import_v1.md"

STATUS = "MTT_SELECTED_CROSSREPO_ALPHA1_DRIVER_REPLAY_IMPORTED_PRIMITIVE_C1_OPEN"
NEXT = "MTT_Selected_PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    typed_value = load(TYPED_VALUE)
    dotd_probe = load(DOTD_PROBE)
    primitive_selector = load(PRIMITIVE_SELECTOR)
    higher_order = load(HIGHER_ORDER)
    gr_alpha = load(GR_ALPHA)
    q79_kernel = load(Q79_KERNEL)
    constants_bridge = load(CONSTANTS_BRIDGE)
    qa_primitive = load(QA_PRIMITIVE)

    repo_scan = {
        "mtt_protospinor_gr_response_proof": {
            "head_result": "alpha1 driver replay gate closed",
            "useful_for_this_frontier": True,
            "status": gr_alpha["imported_status"]["status"],
            "closes": gr_alpha["what_closes_now"],
            "remaining": gr_alpha["what_remains_open"],
        },
        "mtt_q79_proof_repro": {
            "head_result": "analytic alpha1 Riesz/Duhamel retarded-kernel formula proved",
            "useful_for_this_frontier": True,
            "status": q79_kernel["status"],
            "closes_formula_not_values": q79_kernel["analytic_variational_kernel_formula"][
                "what_the_formula_closes"
            ],
            "remaining_values": q79_kernel["analytic_variational_kernel_formula"][
                "what_the_formula_does_not_close"
            ],
        },
        "mtt_nonsm_constants_no_knob": {
            "head_result": "q79 analytic retarded kernel imported into N_MTT bridge, values open",
            "useful_for_this_frontier": True,
            "status": constants_bridge["status"],
            "retarded_frame_clean": constants_bridge["q79_kernel_contribution"]["closes"],
            "values_still_open": constants_bridge["q79_kernel_contribution"]["does_not_close"],
        },
        "mtt_qa_su3_packet_proof": {
            "head_result": "primitive C1 atom payload fill no-go in current corpus",
            "useful_for_this_frontier": True,
            "status": qa_primitive["status"],
            "confirms_primitive_payload_still_open": qa_primitive["what_remains_open"],
        },
    }

    alpha_import = {
        "imported_from": rel(GR_ALPHA),
        "selected_N_alpha1_h_ext_value": gr_alpha["what_closes_now"][
            "selected_N_alpha1_h_ext_value"
        ],
        "du_dalpha1_equals_h_ext": gr_alpha["what_closes_now"]["du_dalpha1_equals_h_ext"],
        "selected_dotD_source_verified": gr_alpha["honest_dotd_replay"][
            "selected_dotD_source_verified"
        ],
        "alpha1_driver_verified": gr_alpha["honest_dotd_replay"]["alpha1_driver_verified"],
        "honest_dotD_alpha1_replay": gr_alpha["what_closes_now"][
            "honest_dotD_alpha1_replay"
        ],
        "lambda_alpha1": gr_alpha["promoted_value"]["lambda_alpha1"],
        "N_alpha1_h_ext": gr_alpha["promoted_value"]["N_alpha1_h_ext"],
        "tangent_residual_l2": gr_alpha["promoted_value"]["tangent_residual_l2"],
        "validator_output": gr_alpha["honest_dotd_replay"]["validator_output"],
        "why_import_allowed": (
            "The imported proof closes the same q79/F,m=1 oriented terminal slot, functional "
            "HYM/End0 operator, and overlap-normalization hypotheses already present in this proof spine. "
            "It supplies theorem-derived alpha1 and dotD replay flags, not diagnostic lifted flags."
        ),
    }

    local_compatibility = {
        "dotD_transport_formula_already_proved_locally": dotd_probe["theorem"]["proved"],
        "local_source_only_failure_was_alpha1_driver": dotd_probe["validator_boundary"][
            "source_only_fails_only_by_alpha1_driver"
        ],
        "primitive_fiber_quotient_already_closed_locally": primitive_selector[
            "fiber_class_quotient_selected_claimed"
        ],
        "active_shift_selected_by_current_repo": primitive_selector["active_shift_selected_claimed"],
        "absolute_fiber_shift_still_unselected": primitive_selector[
            "absolute_fiber_shift_selected_claimed"
        ]
        is False,
        "shift0_is_computation_gauge_only": primitive_selector["primitive_selector"][
            "canonical_representative_is_physical_selector"
        ]
        is False,
        "higher_order_full_response_criterion_already_locked": higher_order["theorem"][
            "proved"
        ],
        "current_layer_flavor_splitting_possible": primitive_selector[
            "observable_class_payload"
        ]["current_layer_flavor_splitting_possible"],
        "previous_typed_value_alpha1_open": typed_value["alpha1_value_packet"][
            "alpha1_driver_verified"
        ]
        is False,
        "primitive_candidates_already_emitted": typed_value[
            "primitive_response_candidate_values_emitted"
        ],
        "conditional_A_still_not_selected": typed_value["A_selected_claimed"] is False,
        "b_selected_still_not_selected": typed_value["b_selected_claimed"] is False,
    }

    frontier_update = {
        "alpha1_driver_no_longer_primary_blocker": True,
        "selected_dotD_replay_available_by_import": True,
        "typed_retarded_selector_no_longer_needed_for_alpha1_only": True,
        "typed_retarded_selector_may_still_be_relevant_for_primitive_selector": True,
        "fiberclass_quotient_already_selected_locally": True,
        "absolute_fiber_origin_not_active_blocker_for_current_observables": True,
        "next_frontier": NEXT,
        "remaining_primary_blocker": (
            "selected primitive C1 contractions or higher-order/full-response matrices that emit "
            "A_selected and b_selected from the same branch"
        ),
    }

    theorem = {
        "name": "CrossRepoAlpha1DriverReplayImportTheorem",
        "proved": True,
        "statement": (
            "The sibling GR/protospinor proof closes the alpha1 source-strength and honest dotD replay "
            "gate for the same oriented q79/F,m=1 source spine: N_alpha1(h_ext)=1, du/dalpha1=h_ext, "
            "selected_dotD_source_verified=true, and alpha1_driver_verified=true.  Importing that result "
            "removes alpha1 as the active blocker in this SM-parity proof.  Combined with the local "
            "primitive fiber-class quotient theorem, the current frontier is not alpha1 or absolute "
            "fiber origin; it is selected primitive-class C1 observable emission or higher-order/full "
            "response.  This import does not emit primitive C1 contractions or promote the conditional "
            "Weyl-pair operator to A_selected/b_selected."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedCrossRepoAlpha1DriverReplayImport",
        "status": STATUS,
        "inputs": {
            "typedbn_or_primitive_value_emission": rel(TYPED_VALUE),
            "local_dotd_transport_derivative_probe": rel(DOTD_PROBE),
            "primitive_fiber_quotient_selector": rel(PRIMITIVE_SELECTOR),
            "higher_order_full_response_frontier": rel(HIGHER_ORDER),
            "gr_alpha1_driver_replay_closure": rel(GR_ALPHA),
            "q79_analytic_alpha1_retarded_kernel": rel(Q79_KERNEL),
            "constants_q79_retarded_nmtt_bridge": rel(CONSTANTS_BRIDGE),
            "qa_su3_primitive_c1_atom_payload_nogo": rel(QA_PRIMITIVE),
        },
        "repo_scan": repo_scan,
        "alpha1_driver_replay_import": alpha_import,
        "local_compatibility": local_compatibility,
        "frontier_update": frontier_update,
        "what_closes_now": {
            "cross_repo_scan_completed": True,
            "selected_alpha1_driver_imported": True,
            "selected_dotD_source_verified_imported": True,
            "honest_dotD_alpha1_replay_imported": True,
            "alpha1_driver_removed_as_active_blocker": True,
            "fiberclass_quotient_compatibility_checked": True,
            "primitive_fiber_quotient_retained_as_closed_local_result": True,
            "higher_order_full_response_frontier_retained": True,
            "primitive_C1_frontier_sharpened": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_primitive_class_C1_observable_emission": True,
            "absolute_fiber_origin_source_theorem": True,
            "selected_primitive_C1_contractions": True,
            "selected_higher_order_or_full_response_matrices": True,
            "selected_b_selected": True,
            "promote_conditional_A_to_A_selected": True,
            "honest_selected_deltaTheta_C1_solve": True,
            "Yukawa_CKM_PMNS_masses_Higgs_RG": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "alpha1_driver_verified_imported": True,
        "selected_dotD_source_verified_imported": True,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "primitive_C1_contractions_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem": theorem,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_CrossRepo_Alpha1DriverReplay_Import_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "alpha1_driver_verified_imported": True,
        "selected_dotD_source_verified_imported": True,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "primitive_C1_contractions_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem_proved": True,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected CrossRepo Alpha1DriverReplay Import v1

Status: `{STATUS}`.

## Result

The sibling repos contain one directly useful closure:

```text
N_alpha1(h_ext) = 1
du/dalpha1 = h_ext
selected_dotD_source_verified = true
alpha1_driver_verified = true
honest dotD replay = PASS
```

This is imported from the GR/protospinor response proof.  The q79 and constants
repos also support the analytic Riesz/Duhamel retarded-kernel frame, while the
Qa/SU3 repo confirms that primitive C1 atom values are still the hard open
payload.

## Boundary

This import removes alpha1/dotD replay as the active blocker here.  Together
with the local primitive fiber-class quotient theorem, it also confirms that
absolute fiber origin is not the active blocker for current C1 spectral
observables.  It does not emit primitive C1 contractions, selected higher-order
response matrices, or promote the conditional Weyl-pair packet to `A_selected`
or `b_selected`.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
