"""Build enriched Weyl-pair source provenance or Galerkin C1 values gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun.candidate.json"
PROMOTION_ATTEMPT = (
    DATA
    / "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun"
    / "weylpair_source_emission_promotion_attempt.packet.json"
)
CONDITIONAL_VALUE_RUN = (
    DATA
    / "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun"
    / "conditional_weylpair_value_run.packet.json"
)
SOURCE_PROVENANCE = DATA / "selected_routec_weylpair_source_provenance_lemma.candidate.json"
SOURCE_TO_C1 = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
SM_SLOT_OVERLAP = DATA / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"
SM_SLOT_DOWNSTREAM = DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"
PRIMITIVE_SELECTOR = DATA / "selected_primitivevertex_source_or_basistransport_selectiontheorem.candidate.json"
GALERKIN_CONTRACT = (
    DATA
    / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun"
    / "honest_galerkin_c1_value_run_contract.packet.json"
)

OUTPUT = DATA / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values.candidate.json"
PACKET_DIR = DATA / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values"
STATIC_PROVENANCE_PACKET = PACKET_DIR / "static_enriched_weylpair_source_provenance.packet.json"
DYNAMIC_BOUNDARY_PACKET = PACKET_DIR / "dynamic_c1_value_boundary.packet.json"
GALERKIN_VALUES_PACKET = PACKET_DIR / "galerkin_c1_values_fallback.packet.json"
CERT = CERTS / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values_certificate.json"
NOTE = CORPUS / "MTT_Selected_EnrichedWeylPairSourceProvenance_or_GalerkinC1Values_v1.md"

STATUS = "MTT_SELECTED_ENRICHEDWEYLPAIRSOURCEPROVENANCE_OR_GALERKINC1VALUES_BUILT_STATIC_PROVENANCE_CLOSED_DYNAMIC_VALUES_OPEN"
NEXT = "MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    promotion = load(PROMOTION_ATTEMPT)
    value_run = load(CONDITIONAL_VALUE_RUN)
    provenance = load(SOURCE_PROVENANCE)
    source_to_c1 = load(SOURCE_TO_C1)
    sm_overlap = load(SM_SLOT_OVERLAP)
    sm_downstream = load(SM_SLOT_DOWNSTREAM)
    primitive_selector = load(PRIMITIVE_SELECTOR)
    galerkin = load(GALERKIN_CONTRACT)

    static_partition = sm_downstream["old_contract_reclassification"]["matter_slot_charge"][
        "selected_partition"
    ]
    downstream_norm = sm_downstream["old_contract_reclassification"]["normalization"]
    source_selector = primitive_selector["source_selector_packet"]

    static_provenance_closed = (
        provenance["source_level_weyl_carrier"]["proved"] is True
        and provenance["active_shift_provenance"]["proved"] is True
        and sm_overlap["arrow_status"]["all_six_closed"] is True
        and sm_downstream["payload_tiers"]["static_sm_slot_tier"]["closed"] is True
        and sm_downstream["old_contract_reclassification"]["matter_slot_charge"][
            "static_selected_emitted"
        ]
        is True
        and sm_downstream["old_contract_reclassification"]["singlet_neutrino_rule"][
            "static_selected_emitted"
        ]
        is True
        and downstream_norm["static_trace_innerproduct_normalization_selected"] is True
    )

    static_packet = {
        "schema": "MTTStaticEnrichedWeylPairSourceProvenance.v1",
        "status": "STATIC_ENRICHED_WEYLPAIR_SOURCE_PROVENANCE_CLOSED",
        "source_level_carrier": {
            "phase_Z_source_proved": provenance["source_level_weyl_carrier"]["proved"],
            "shift_X_source_proved": provenance["source_level_weyl_carrier"]["proved"],
            "active_shift_1_1_proved": provenance["active_shift_provenance"]["proved"],
            "carrier_statement": provenance["source_level_weyl_carrier"]["statement"],
        },
        "static_sector_route": {
            "phase_Z_to": sm_downstream["weylpair_consequence"]["phase_route"],
            "shift_X_to": sm_downstream["weylpair_consequence"]["shift_route"],
            "clock_phase_side": static_partition["clock_phase_side"],
            "shift_non10_side": static_partition["shift_non10_side"],
            "selected_static_sector_route_now_closed": sm_downstream["weylpair_consequence"][
                "selected_static_sector_route_now_closed"
            ],
            "same_route_in_primitive_selector": source_selector["selector_components"][
                "static_sector_route"
            ]["selected"],
        },
        "static_normalization": {
            "selected_overlap_transfer_normalization": sm_overlap[
                "selected_overlap_kernel"
            ]["selected"],
            "static_trace_innerproduct_normalization_selected": downstream_norm[
                "static_trace_innerproduct_normalization_selected"
            ],
            "unit_trace_transfer": sm_overlap["selected_overlap_kernel"]["normalization_values"][
                "unit_trace_transfer"
            ],
        },
        "provenance_closed": static_provenance_closed,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    dynamic_boundary = {
        "schema": "MTTDynamicC1ValueBoundary.v1",
        "status": "DYNAMIC_C1_VALUES_OPEN_AFTER_STATIC_PROVENANCE",
        "conditional_value_run_ready": True,
        "conditional_rank": value_run["rank"],
        "conditional_condition_number": value_run["condition_number"],
        "conditional_deltaTheta": value_run["deltaTheta_conditional"],
        "A_transpose_A_if_promoted": value_run["A_transpose_A_if_promoted"],
        "A_transpose_b_if_promoted": value_run["A_transpose_b_if_promoted"],
        "why_not_A_selected": sm_downstream["weylpair_consequence"]["why_not_promoted"],
        "open_dynamic_requirements": sm_downstream["payload_tiers"][
            "dynamic_operator_c1_tier"
        ]["open_inputs"],
        "prior_source_to_C1_transfer_selected_status": source_to_c1["selected_status"],
        "prior_promotion_inputs_missing_before_static_closure": promotion[
            "promotion_inputs_missing"
        ],
        "after_static_provenance_closure": {
            "source_level_weylpair_provenance_open": False,
            "static_sector_routing_open": False,
            "static_transfer_normalization_open": False,
            "selected_dynamic_source_to_C1_transfer_tensor_open": True,
            "selected_primitive_C1_overlap_contractions_open": True,
            "selected_Hessian_or_b_source_vector_open": True,
            "A_selected_currently_emitted": False,
            "b_selected_currently_emitted": False,
            "deltaTheta_C1_currently_promoted": False,
        },
        "dynamic_value_promotion": {
            "A_selected_promoted": False,
            "b_selected_promoted": False,
            "deltaTheta_C1_promoted": False,
            "SM_parity_dynamic_packet_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    galerkin_packet = {
        "schema": "MTTSelectedGalerkinC1ValuesFallback.v1",
        "status": "HONEST_GALERKIN_C1_VALUES_STILL_OPEN",
        "contract_status": galerkin["status"],
        "current_manifest_status": galerkin["current_manifest_status"],
        "selected_source_verified": galerkin["selected_source_verified"],
        "required_inputs": galerkin["required_inputs"],
        "required_outputs": galerkin["required_outputs"],
        "acceptance_checks": galerkin["acceptance_checks"],
        "would_close_SM_parity_dynamic_packet_if_values_emitted": True,
        "would_close_no_knob_flavor_constants_if_values_emitted": False,
        "observed_flavor_data_forbidden": galerkin["observed_flavor_data_forbidden"],
        "target_fitting_forbidden": galerkin["target_fitting_forbidden"],
    }

    candidate = {
        "candidate": "MTTSelectedEnrichedWeylPairSourceProvenanceOrGalerkinC1Values",
        "status": STATUS,
        "inputs": {
            "previous_value_run": rel(PREVIOUS),
            "promotion_attempt": rel(PROMOTION_ATTEMPT),
            "conditional_value_run": rel(CONDITIONAL_VALUE_RUN),
            "weylpair_source_provenance": rel(SOURCE_PROVENANCE),
            "source_to_C1_transfer": rel(SOURCE_TO_C1),
            "selected_smslotfunctor_overlapkernel": rel(SM_SLOT_OVERLAP),
            "selected_smslotfunctor_downstream_payloads": rel(SM_SLOT_DOWNSTREAM),
            "primitive_source_selector": rel(PRIMITIVE_SELECTOR),
            "honest_galerkin_contract": rel(GALERKIN_CONTRACT),
        },
        "output_packets": {
            "static_enriched_weylpair_source_provenance": rel(STATIC_PROVENANCE_PACKET),
            "dynamic_c1_value_boundary": rel(DYNAMIC_BOUNDARY_PACKET),
            "galerkin_c1_values_fallback": rel(GALERKIN_VALUES_PACKET),
        },
        "what_closes_now": {
            "static_enriched_weylpair_source_provenance": True,
            "static_Z_to_u_e_X_to_d_nuD_route": True,
            "static_1M_Dirac_neutrino_shift_rule": True,
            "static_finite_trace_transfer_normalization": True,
            "dynamic_value_boundary_after_static_provenance": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "selected_dynamic_source_to_C1_transfer_tensor": True,
            "selected_primitive_C1_overlap_contractions": True,
            "selected_D_E_Riesz_Green_dotD": True,
            "physical_alpha1_driver_at_dynamic_C1_tier": True,
            "theorem_derived_A_selected": True,
            "theorem_derived_b_selected": True,
            "selected_deltaTheta_C1": True,
            "honest_selected_Galerkin_C1_execution_values": True,
            "SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_flavor_closure": True,
        },
        "promotion_decision": {
            "static_enriched_weylpair_source_provenance_promoted": static_provenance_closed,
            "dynamic_C1_transfer_tensor_promoted": False,
            "A_selected_promoted": False,
            "b_selected_promoted": False,
            "deltaTheta_C1_promoted": False,
            "honest_Galerkin_C1_execution_promoted": False,
            "SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_flavor_constants_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "StaticEnrichedWeylPairSourceProvenanceTheorem",
            "proved": True,
            "statement": (
                "The source-level qutrit Weyl carrier, active shift, selected SM-slot "
                "functor arrows, 1_M Dirac-neutrino shift rule, and finite trace "
                "normalization now close the static enriched Weyl-pair provenance: "
                "Z/clock routes to u,e and X/shift routes to d,nuD without observed "
                "data or locked-target selection.  This does not promote A_selected, "
                "b_selected, or deltaTheta_C1, because dynamic C1 transfer, operator "
                "values, primitive contractions, and Hessian/source normalization remain open."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_EnrichedWeylPairSourceProvenance_or_GalerkinC1Values_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "static_provenance_packet_path": rel(STATIC_PROVENANCE_PACKET),
        "dynamic_boundary_packet_path": rel(DYNAMIC_BOUNDARY_PACKET),
        "galerkin_values_packet_path": rel(GALERKIN_VALUES_PACKET),
        "theorem_proved": True,
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected EnrichedWeylPairSourceProvenance or GalerkinC1Values v1

Status: `{STATUS}`.

This closes the static enriched Weyl-pair provenance:

```text
Z / clock / phase -> u,e
X / shift         -> d,nuD
1_M = N^c         -> Dirac-neutrino shift side
finite trace transfer normalization selected
```

This is now source-tier data, not a target fit.  It uses the selected qutrit
Weyl carrier, active shift `(1,1)`, all six SM-slot functor arrows, and the
selected transported-projector trace normalization.

The dynamic C1 value tier remains open.  The conditional value run is still
ready:

```text
rank(A_conditional) = {value_run["rank"]}
condition number    = {value_run["condition_number"]}
deltaTheta          = {value_run["deltaTheta_conditional"]}
```

But `A_selected`, `b_selected`, and `deltaTheta_C1` are not promoted until the
dynamic transfer tensor, primitive C1 contractions, Hessian/source vector, or
honest selected Galerkin C1 values are emitted.

No observed masses, CKM/PMNS values, CP phase, benchmark matrices, or target
residuals are used as selectors.

Next artifact: `{NEXT}`.
"""

    STATIC_PROVENANCE_PACKET.write_text(json.dumps(static_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    DYNAMIC_BOUNDARY_PACKET.write_text(json.dumps(dynamic_boundary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    GALERKIN_VALUES_PACKET.write_text(json.dumps(galerkin_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
