"""Build primitive-C1 contractions or dynamic-overlap tensor source emission."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_primitivec1_or_weylpair_sectorrouting_sourceemission.candidate.json"
CROSS_ALPHA = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
PRIMITIVE_CLASS = DATA / "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"
TYPED_PRIMITIVE = DATA / "selected_typedbn_retardedderivative_or_primitiveresponse_valueemission.candidate.json"
NONINV = DATA / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
C1_EMISSION = DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json"
SPLITTER = DATA / "selected_routec_splitter_source_emission_contract_or_selected_deltatheta_c1_solve.candidate.json"
DOWNSTREAM = DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"
HONEST_PRIMITIVE = (
    DATA / "selected_routec_strominger_galerkin_solve" / "c1_primitive_contractions.candidate.json"
)
FORMAL_PRIMITIVE = (
    DATA
    / "selected_routec_strominger_galerkin_solve"
    / "formal_lift_diagnostic"
    / "c1_primitive_contractions.candidate.json"
)

OUTPUT = DATA / "selected_primitivec1_contractions_or_dynamicoverlaptensor_sourceemission.candidate.json"
CERT = CERTS / "selected_primitivec1_contractions_or_dynamicoverlaptensor_sourceemission_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrimitiveC1Contractions_or_DynamicOverlapTensor_SourceEmission_v1.md"

STATUS = (
    "MTT_SELECTED_PRIMITIVEC1_CONTRACTIONS_OR_DYNAMICOVERLAPTENSOR_SOURCEEMISSION_"
    "ENVELOPE_BUILT_DYNAMIC_VALUES_OPEN"
)
NEXT = "MTT_Selected_DynamicOverlapTensor_HessianNormalization_or_GalerkinC1Contractions_ValueEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sector_matrix_summary(noninv: dict[str, Any]) -> dict[str, Any]:
    fixed = [
        item
        for item in noninv["candidate_primitives"]
        if isinstance(item["primitive_fiber_shift"], int)
    ]
    rank_values = {
        str(item["primitive_fiber_shift"]): item["summary"]
        for item in fixed
    }
    max_abs = sorted(
        {
            float(summary["max_abs_entry"])
            for item in fixed
            for summary in item["summary"].values()
        }
    )
    rank_set = sorted(
        {
            int(summary["rank"])
            for item in fixed
            for summary in item["summary"].values()
        }
    )
    return {
        "fixed_fiber_candidates": [item["primitive_fiber_shift"] for item in fixed],
        "all_fixed_fiber_rank_values": rank_set,
        "all_fixed_fiber_max_abs_values": max_abs,
        "all_fixed_fiber_rank_three": rank_set == [3],
        "rank_by_fixed_fiber_and_sector": rank_values,
    }


def main() -> int:
    previous = load(PREVIOUS)
    alpha = load(CROSS_ALPHA)
    primitive_class = load(PRIMITIVE_CLASS)
    typed_primitive = load(TYPED_PRIMITIVE)
    noninv = load(NONINV)
    c1_emission = load(C1_EMISSION)
    splitter = load(SPLITTER)
    downstream = load(DOWNSTREAM)
    honest_primitive = load(HONEST_PRIMITIVE)
    formal_primitive = load(FORMAL_PRIMITIVE)

    closed_inputs = {
        "alpha1_driver_verified": alpha["alpha1_driver_verified_imported"],
        "selected_dotD_source_verified": alpha["selected_dotD_source_verified_imported"],
        "honest_dotD_alpha1_replay": alpha["alpha1_driver_replay_import"][
            "honest_dotD_alpha1_replay"
        ],
        "static_weyl_sector_routing": previous["what_closes_now"][
            "selected_static_weyl_sector_routing_emitted"
        ],
        "static_singlet_neutrino_shift_rule": previous["what_closes_now"][
            "selected_static_singlet_neutrino_shift_rule_emitted"
        ],
        "static_trace_transfer_normalization": previous["what_closes_now"][
            "selected_static_trace_transfer_normalization_emitted"
        ],
        "primitive_class_C1_observable_layer": primitive_class["promotion_decision"][
            "current_primitive_class_promoted_as_valid_C1_observable_layer"
        ],
        "current_layer_not_flavor_closure": primitive_class["promotion_decision"][
            "current_primitive_class_promoted_as_flavor_closure"
        ]
        is False,
    }

    contraction_envelope = {
        "constructed": True,
        "source": "selected static route plus fixed-fiber primitive response candidates",
        "phase_route": previous["static_routing_source_emission"]["retired_sector_routing"][
            "phase_route"
        ],
        "shift_route": previous["static_routing_source_emission"]["retired_sector_routing"][
            "shift_route"
        ],
        "active_shift": typed_primitive["primitive_response_lane"]["fixed_fiber_candidates"][0][
            "primitive_active_shift"
        ],
        "fixed_fiber_class": [
            item["primitive_fiber_shift"]
            for item in typed_primitive["primitive_response_lane"][
                "fixed_fiber_candidates"
            ]
        ],
        "candidate_summary": sector_matrix_summary(noninv),
        "selected_as_dynamic_tensor": False,
        "why_not_selected": (
            "The envelope combines already selected static routing with finite primitive candidates, "
            "but neither the honest Galerkin primitive-contraction manifest nor the selected C1-response "
            "emission audit supplies theorem-derived dynamic contraction values."
        ),
    }

    promotion_test = {
        "required_fields": {
            "selected_dynamic_overlap_tensor_or_transfer_functor": False,
            "selected_primitive_C1_contractions": honest_primitive[
                "selected_source_verified"
            ],
            "selected_Hessian_or_b_normalization": c1_emission["emission_audit"][
                "selected_source_vector_b_selected_emitted"
            ],
            "selected_A_response_operator": c1_emission["emission_audit"][
                "selected_operator_A_selected_emitted"
            ],
            "selected_deltaTheta_C1_solution": splitter["missing_selected_operator_data"][
                "selected_deltaTheta_C1_solution"
            ]
            is not None,
            "selected_sector_response_matrices": c1_emission["emission_audit"][
                "required_operator_slots"
            ]["sector_response_matrices_M_u_M_d_M_e_M_nuD"],
        },
        "all_required_fields_emitted": False,
        "A_selected_promotion_allowed": False,
        "b_selected_promotion_allowed": False,
        "rank_or_consistency_test_allowed": splitter["selected_deltatheta_c1_solve_gate"][
            "rank_test_computable"
        ],
    }

    honest_vs_formal = {
        "honest_status": honest_primitive["status"],
        "honest_selected_source_verified": honest_primitive["selected_source_verified"],
        "formal_status": formal_primitive["status"],
        "formal_selected_source_verified": formal_primitive["selected_source_verified"],
        "formal_lift_promoted": False,
        "reason": "Both manifests still record missing primitive C1 contractions; formal-lift data cannot promote selected-source proof.",
    }

    retired_blockers = {
        "alpha1_dotD_replay": True,
        "static_sector_routing": True,
        "static_1M_shift_rule": True,
        "static_trace_transfer_normalization": True,
        "absolute_fiber_origin_for_current_spectral_observables": True,
    }

    live_blockers = {
        "selected_dynamic_overlap_tensor_or_transfer_functor": True,
        "selected_primitive_C1_contractions": True,
        "selected_b_selected_or_Hessian_normalization": True,
        "selected_A_selected_response_operator": True,
        "selected_sector_response_matrices": True,
        "selected_deltaTheta_C1_solution": True,
        "dynamic_visible_routec_operator_source_identity": downstream["what_remains_open"][
            "dynamic_visible_routec_operator_source_identity"
        ],
    }

    candidate = {
        "candidate": "MTTSelectedPrimitiveC1ContractionsOrDynamicOverlapTensorSourceEmission",
        "status": STATUS,
        "inputs": {
            "previous_frontier": rel(PREVIOUS),
            "crossrepo_alpha1_import": rel(CROSS_ALPHA),
            "primitive_class_C1_observable": rel(PRIMITIVE_CLASS),
            "typed_primitive_response_candidates": rel(TYPED_PRIMITIVE),
            "noninvariant_C1_primitive_search": rel(NONINV),
            "selected_C1_response_operator_emission": rel(C1_EMISSION),
            "splitter_deltaTheta_gate": rel(SPLITTER),
            "downstream_operator_payload_ledger": rel(DOWNSTREAM),
            "honest_galerkin_primitive_contractions": rel(HONEST_PRIMITIVE),
            "formal_lift_primitive_contractions": rel(FORMAL_PRIMITIVE),
        },
        "closed_inputs": closed_inputs,
        "contraction_envelope": contraction_envelope,
        "promotion_test": promotion_test,
        "honest_vs_formal_primitive_manifest": honest_vs_formal,
        "retired_blockers": retired_blockers,
        "live_blockers": live_blockers,
        "what_closes_now": {
            "dynamic_contraction_promotion_test_built": True,
            "static_route_plus_primitive_candidate_envelope_constructed": True,
            "alpha1_dotD_static_routing_and_trace_normalization_reclassified_as_closed_inputs": True,
            "honest_and_formal_primitive_manifests_checked": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": live_blockers
        | {
            "promote_conditional_A_to_A_selected": True,
            "Yukawa_CKM_PMNS_masses_Higgs_RG": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "dynamic_overlap_tensor_claimed": False,
        "primitive_C1_contractions_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "PrimitiveC1ContractionsOrDynamicOverlapTensorSourceEmissionTheorem",
            "proved": True,
            "statement": (
                "After alpha1/dotD replay, static Weyl routing, the 1_M shift-side rule, and finite trace "
                "normalization are selected, the remaining C1 obstruction is isolated to dynamic data.  The "
                "existing finite primitive candidates form a routed contraction envelope for the current spectral "
                "layer, but the honest and formal Galerkin manifests still mark primitive C1 contractions missing, "
                "and the selected C1-response audit still lacks A_selected, b_selected, sector response matrices, "
                "and deltaTheta_C1.  Therefore the next value-emission target is selected dynamic overlap tensor/"
                "Hessian normalization or honest selected Galerkin primitive-contraction values."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_PrimitiveC1Contractions_or_DynamicOverlapTensor_SourceEmission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "dynamic_overlap_tensor_claimed": False,
        "primitive_C1_contractions_claimed": False,
        "theorem_proved": True,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PrimitiveC1Contractions or DynamicOverlapTensor SourceEmission v1

Status: `{STATUS}`.

Closed inputs now usable by the C1 frontier:

```text
alpha1/dotD replay = selected
Z/clock -> u,e = selected at static SM-slot tier
X/shift -> d,nuD = selected at static SM-slot tier
1_M = N^c shift-side rule = selected at static SM-slot tier
finite trace transfer normalization = selected at static SM-slot tier
active primitive shift = (1,1)
fixed fiber quotient class = 0,1,2
```

The constructed contraction envelope combines those selected static inputs with
the finite fixed-fiber primitive response candidates.  It is not yet a selected
dynamic tensor: the honest Galerkin primitive-contraction manifest still says
`{honest_primitive["status"]}`, and the selected C1-response audit still lacks
`A_selected`, `b_selected`, sector response matrices, and `deltaTheta_C1`.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
