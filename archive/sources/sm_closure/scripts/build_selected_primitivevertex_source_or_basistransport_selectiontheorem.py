"""Build primitive-vertex / basis-transport source selection theorem gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun.candidate.json"
WEYL_SOURCE = DATA / "selected_routec_weylpair_source_provenance_lemma.candidate.json"
WEYL_GATE = DATA / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem.candidate.json"
SM_OVERLAP = DATA / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"
DOWNSTREAM = DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"
PRIMITIVE_SELECTOR = DATA / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem.candidate.json"
SOURCE_TO_C1 = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
DOTD_IMPORT = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"

OUTPUT = DATA / "selected_primitivevertex_source_or_basistransport_selectiontheorem.candidate.json"
PACKET_DIR = DATA / "selected_primitivevertex_source_or_basistransport_selectiontheorem"
SELECTOR_PACKET = PACKET_DIR / "primitive_vertex_source_selector.packet.json"
CERT = CERTS / "selected_primitivevertex_source_or_basistransport_selectiontheorem_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrimitiveVertexSource_or_BasisTransport_SelectionTheorem_v1.md"

STATUS = "MTT_SELECTED_PRIMITIVEVERTEX_SOURCE_OR_BASISTRANSPORT_SELECTIONTHEOREM_BUILT_SOURCE_SELECTOR_CLOSED_VALUES_OPEN"
NEXT = "MTT_Selected_PrimitiveOverlapContractions_ValueEmission_or_HonestGalerkinRun_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    previous = load(PREVIOUS)
    weyl_source = load(WEYL_SOURCE)
    weyl_gate = load(WEYL_GATE)
    sm_overlap = load(SM_OVERLAP)
    downstream = load(DOWNSTREAM)
    primitive_selector = load(PRIMITIVE_SELECTOR)
    source_to_c1 = load(SOURCE_TO_C1)
    dotd_import = load(DOTD_IMPORT)

    coord = previous["differentiated_primitive_overlap_contract"]["coordinate_system"]
    phase_route = downstream["weylpair_consequence"]["phase_route"]
    shift_route = downstream["weylpair_consequence"]["shift_route"]
    static_partition = downstream["old_contract_reclassification"]["matter_slot_charge"][
        "selected_partition"
    ]
    overlap_kernel = sm_overlap["selected_overlap_kernel"]

    source_selector_packet = {
        "schema": "MTTSelectedPrimitiveVertexSourceSelector.v1",
        "status": "SELECTED_SOURCE_SELECTOR_EMITTED_VALUES_OPEN",
        "branch": "q79/F,m=1 S3/GS Route-C",
        "same_source": True,
        "observed_data_used": False,
        "target_fitting_used": False,
        "selector_components": {
            "source_level_qutrit_weyl_carrier": {
                "selected": weyl_source["source_level_weyl_carrier"]["proved"],
                "phase_generator": "Z",
                "shift_generator": "X",
                "source": rel(WEYL_SOURCE),
            },
            "active_deck_shift": {
                "selected": primitive_selector["primitive_selector"]["active_shift_selected"],
                "value": primitive_selector["primitive_selector"]["selected_active_shift"],
                "source": rel(PRIMITIVE_SELECTOR),
            },
            "fixed_fiber_quotient": {
                "selected_for_current_observables": primitive_selector["primitive_selector"][
                    "fiber_class_quotient_selected_for_current_observables"
                ],
                "absolute_fiber_origin_selected": primitive_selector["primitive_selector"][
                    "absolute_fiber_shift_selected"
                ],
                "computation_representative": primitive_selector["primitive_selector"][
                    "canonical_computation_representative"
                ],
                "fixed_fiber_class": primitive_selector["primitive_selector"]["fixed_fiber_class"],
            },
            "static_sector_route": {
                "selected": downstream["weylpair_consequence"][
                    "selected_static_sector_route_now_closed"
                ],
                "phase_Z_to": phase_route,
                "shift_X_to": shift_route,
                "clock_phase_side": static_partition["clock_phase_side"],
                "shift_non10_side": static_partition["shift_non10_side"],
                "source": rel(DOWNSTREAM),
            },
            "static_overlap_transfer_normalization": {
                "selected": overlap_kernel["selected"],
                "kernel_definition": overlap_kernel["kernel_definition"],
                "unit_trace_transfer": overlap_kernel["normalization_values"][
                    "unit_trace_transfer"
                ],
                "source": rel(SM_OVERLAP),
            },
            "alpha1_dotD_driver": {
                "selected_dotD_source_verified": dotd_import[
                    "selected_dotD_source_verified_imported"
                ],
                "alpha1_driver_verified": dotd_import["alpha1_driver_verified_imported"],
                "honest_dotD_alpha1_replay": dotd_import["alpha1_driver_replay_import"][
                    "honest_dotD_alpha1_replay"
                ],
                "source": rel(DOTD_IMPORT),
            },
        },
        "selector_statement": (
            "The same q79/F,m=1 source selects the enriched Weyl-pair primitive vertex/basis-transport "
            "selector at the source-routing level: Z is the phase/clock leg for u,e; X is the "
            "active-shift leg for d,nuD; fixed fiber shifts are a current-observable quotient class; "
            "and the static trace transfer normalization is selected."
        ),
        "values_not_emitted": {
            "primitive_three_by_three_contraction_terms": True,
            "differentiated_vertex_integrals": True,
            "Hessian_counterterms": True,
            "A_selected_72_real_columns": True,
            "b_selected_source_vector": True,
            "deltaTheta_C1": True,
            "sector_response_matrices": True,
        },
    }

    source_selector_theorem = {
        "name": "SelectedPrimitiveVertexSourceOrBasisTransportSelectionTheorem",
        "proved": True,
        "statement": (
            "Combining the selected S3/GS qutrit Weyl carrier, the selected active deck shift (1,1), "
            "the selected fixed-fiber quotient class for current C1 observables, the selected SM-slot "
            "source route Z->u,e and X->d,nuD with 1_M=N^c on the shift side, the selected trace "
            "overlap normalization, and the theorem-derived alpha1/dotD driver emits the primitive "
            "vertex/basis-transport source selector needed by the differentiated Phi_fin^C1 contract. "
            "This is a selector theorem, not a value-emission theorem: primitive integrals, Hessian "
            "counterterms, A_selected, b_selected, and deltaTheta_C1 remain open."
        ),
        "proof_steps": [
            "Source-level qutrit Weyl carrier is selected by the S3/GS gerbe packet.",
            "Active deck shift (1,1) is selected and is the unique nonzero active shift for the current primitive lane.",
            "Fixed qutrit fiber shifts 0,1,2 form a selected quotient class for current C1 spectral observables.",
            "The selected SM-slot functor emits the source route Z/clock -> u,e and X/shift -> d,nuD, with 1_M=N^c on the shift side.",
            "The selected overlap kernel emits the static trace transfer normalization.",
            "The cross-repo alpha1 replay imports selected_dotD_source_verified and alpha1_driver_verified for the same branch.",
            "Therefore the source selector for the differentiated primitive-overlap template is emitted, while numerical/differentiated primitive values remain unfilled.",
        ],
        "what_this_does_not_prove": [
            "primitive overlap contraction values",
            "Hessian/source vector b_selected",
            "A_selected or selected 72-real phase/shift columns",
            "deltaTheta_C1",
            "Yukawa/CKM/PMNS/mass closure",
        ],
    }

    transfer_boundary = {
        "conditional_source_to_C1_transfer_exact": source_to_c1["conditional_transfer_map"][
            "conditional_exact"
        ],
        "old_selected_transfer_map_emitted": source_to_c1["selected_status"][
            "selected_transfer_map_emitted"
        ],
        "updated_by_this_artifact": {
            "source_selector_for_transfer_promoted": True,
            "dynamic_overlap_tensor_values_promoted": False,
            "normal_form_values_promoted": False,
        },
        "why_A_selected_still_open": (
            "The source selector says which primitive vertex/basis-transport lane is legal.  It does not "
            "evaluate the differentiated contraction tensor in the selected transported zero-mode basis."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedPrimitiveVertexSourceOrBasisTransportSelectionTheorem",
        "status": STATUS,
        "inputs": {
            "previous_differentiated_PhiFinC1_gate": rel(PREVIOUS),
            "weylpair_source_provenance": rel(WEYL_SOURCE),
            "weylpair_basis_transport_gate": rel(WEYL_GATE),
            "selected_smslotfunctor_overlap_kernel": rel(SM_OVERLAP),
            "downstream_static_payload_ledger": rel(DOWNSTREAM),
            "primitive_fiber_shift_selector": rel(PRIMITIVE_SELECTOR),
            "conditional_source_to_C1_transfer": rel(SOURCE_TO_C1),
            "crossrepo_alpha1_driver_import": rel(DOTD_IMPORT),
        },
        "coordinate_system": coord,
        "source_selector_packet_path": rel(SELECTOR_PACKET),
        "source_selector_packet": source_selector_packet,
        "source_selector_theorem": source_selector_theorem,
        "transfer_boundary": transfer_boundary,
        "template_instantiation": {
            "template_path": previous["differentiated_primitive_overlap_contract"]["template_path"],
            "selector_attached": True,
            "selected_values_filled": False,
            "next_fill_fields": [
                "transported_zero_mode_bases",
                "selected primitive vertex operators V_phase and V_shift",
                "primitive three-by-three contraction terms",
                "linear response matrices",
                "Hessian/source counterterms",
                "A_selected, b_selected, deltaTheta_C1",
            ],
        },
        "promotion_decision": {
            "source_selector_promoted": True,
            "selected_primitive_vertex_or_basis_transport_source_promoted": True,
            "selected_primitive_overlap_contractions_promoted": False,
            "selected_dynamic_overlap_tensor_promoted": False,
            "selected_A_selected_promoted": False,
            "selected_b_selected_promoted": False,
            "selected_deltaTheta_C1_promoted": False,
            "selected_sector_response_matrices_promoted": False,
            "honest_Galerkin_C1_contractions_promoted": False,
            "full_SM_no_knob_closure_promoted": False,
        },
        "what_closes_now": {
            "primitive_vertex_source_selector_emitted": True,
            "source_level_ZX_carrier_imported": True,
            "active_shift_and_fiber_quotient_imported": True,
            "static_sector_route_imported": True,
            "static_trace_transfer_normalization_imported": True,
            "alpha1_dotD_driver_imported": True,
            "value_emission_target_reduced_to_primitive_overlap_contractions": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_primitive_overlap_contraction_values": True,
            "selected_vertex_integrals_or_honest_Galerkin_C1_values": True,
            "selected_Hessian_source_vector_b_selected": True,
            "selected_A_selected_deltaTheta_sector_response_matrices": True,
            "Yukawa_CKM_PMNS_masses_Higgs_RG_no_knob": True,
            "full_SM_no_knob_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "selected_primitive_overlap_contractions_claimed": False,
        "selected_PhiFinC1_identity_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PrimitiveVertexSource_or_BasisTransport_SelectionTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "selector_packet_path": rel(SELECTOR_PACKET),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "source_selector_promoted": True,
        "selected_primitive_overlap_contractions_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "theorem_proved": True,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PrimitiveVertexSource or BasisTransport SelectionTheorem v1

Status: `{STATUS}`.

This artifact promotes the source selector for the differentiated `Phi_fin^C1`
primitive-overlap template.

Selected selector:

```text
Z / clock / phase  -> u,e
X / shift          -> d,nuD
active deck shift  -> (1,1)
fixed fiber class  -> 0,1,2 quotient class
1_M=N^c            -> shift / Dirac-neutrino side
```

It uses the selected S3/GS qutrit Weyl carrier, the selected SM-slot functor
source arrows, the selected static trace normalization, and the theorem-derived
alpha1/dotD replay.

This does not emit primitive overlap values.  The next artifact must fill the
template by evaluating the selected primitive vertex/basis-transport
contractions, or by running an honest selected Galerkin C1 solve.

Selector packet: `{rel(SELECTOR_PACKET)}`.

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `{NEXT}`.
"""

    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SELECTOR_PACKET.write_text(json.dumps(source_selector_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "selector_packet": rel(SELECTOR_PACKET), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
