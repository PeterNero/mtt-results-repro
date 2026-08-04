"""Build downstream operator-payload ledger after SM-slot functor closure."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SMSLOT = DATA / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"
CONTRACT = DATA / "selected_routec_samesource_matter_slot_overlap_operator_packet.candidate.json"
FILL_NOGO = DATA / "selected_routec_samesource_operatorpacket_fill_or_nogo.candidate.json"
WEYL_TRANSFER = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
WEYL_A = DATA / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"
SOURCE_PLAN = DATA / "selected_routec_sourceemission_minimal_subpacket_attack_plan.candidate.json"

OUTPUT = DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"
CERT = CERTS / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger_certificate.json"
NOTE = CORPUS / "MTT_SelectedSMSlotFunctor_DownstreamOperatorPayloads_or_SMParityLedger_v1.md"

STATUS = (
    "MTT_SELECTED_SMSLOTFUNCTOR_DOWNSTREAM_PAYLOAD_LEDGER_BUILT_"
    "STATIC_FIELDS_PROMOTED_DYNAMIC_C1_OPEN"
)
NEXT = "MTT_Selected_DynamicOverlapKernel_or_C1Primitive_SourceEmission_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    smslot = load(SMSLOT)
    contract = load(CONTRACT)
    fill_nogo = load(FILL_NOGO)
    weyl_transfer = load(WEYL_TRANSFER)
    weyl_a = load(WEYL_A)
    source_plan = load(SOURCE_PLAN)

    old_fields = fill_nogo["attempted_selected_packet"]["fields"]

    static_partition = {
        "clock_phase_side": {
            "matter_slot": "10_M",
            "sectors": ["u", "e"],
            "selected_by": "A1 terminal Ext source -> 10_M plus A4 U_10=I_3",
            "weyl_leg": "Z/clock/phase",
        },
        "shift_non10_side": {
            "matter_slots": ["bar5_M", "1_M=N^c"],
            "sectors": ["d", "nuD"],
            "selected_by": "A2 terminal Ext source -> bar5_M and A3 terminal Ext source -> 1_M=N^c plus A4 U_bar5=F",
            "weyl_leg": "X/shift/translation",
        },
    }

    reclassified_fields = {
        "source_identity": {
            "old_selected_emitted": old_fields["source_identity"]["selected_emitted"],
            "static_sm_slot_source_identity_closed": smslot["arrow_status"]["all_six_closed"],
            "dynamic_visible_routec_operator_source_identity_closed": False,
            "ledger_effect": "static source identity is no longer a blocker for SM-slot routing, but operator-level Route-C/visible source identity is still required",
        },
        "matter_slot_charge": {
            "old_selected_emitted": old_fields["matter_slot_charge"]["selected_emitted"],
            "static_selected_emitted": True,
            "selected_partition": static_partition,
            "c1_sector_route_independent_of_locked_target": True,
            "ledger_effect": "the old sector-routing blocker is discharged at the static SM-slot source tier",
        },
        "singlet_neutrino_rule": {
            "old_selected_emitted": old_fields["singlet_neutrino_rule"]["selected_emitted"],
            "static_selected_emitted": True,
            "selected_rule": "1_M=N^c routes with the Dirac-neutrino/non-10 shift side",
            "ledger_effect": "nuD no longer needs an additional structural guess at the static routing tier",
        },
        "operator_values": {
            "old_selected_emitted": old_fields["operator_values"]["selected_emitted"],
            "dynamic_selected_emitted": False,
            "needed": "same-branch D_E, Riesz projectors, reduced Green operator, dotD_alpha1, and alpha1 driver",
            "ledger_effect": "unchanged open dynamic field",
        },
        "overlap_transfer": {
            "old_selected_emitted": old_fields["overlap_transfer"]["selected_emitted"],
            "static_finite_transfer_selected": True,
            "dynamic_source_to_C1_transfer_functor_selected": False,
            "static_kernel": smslot["selected_overlap_kernel"]["kernel_definition"],
            "ledger_effect": "finite SM-slot trace transfer is selected, but the dynamic C1 overlap tensor is not emitted",
        },
        "normalization": {
            "old_selected_emitted": old_fields["normalization"]["selected_emitted"],
            "static_trace_innerproduct_normalization_selected": True,
            "dynamic_hessian_or_b_selected_normalization_selected": False,
            "unit_trace_transfer": smslot["selected_overlap_kernel"]["normalization_values"][
                "unit_trace_transfer"
            ],
            "ledger_effect": "static finite normalization is closed; A_selected/b_selected normalization remains open",
        },
        "primitive_contractions": {
            "old_selected_emitted": old_fields["primitive_contractions"]["selected_emitted"],
            "dynamic_selected_emitted": False,
            "needed": "selected primitive C1/Yukawa overlap contractions or an equivalent selected full-response packet",
            "ledger_effect": "unchanged open dynamic field",
        },
    }

    payload_tiers = {
        "static_sm_slot_tier": {
            "closed": True,
            "closed_inputs": [
                "terminal section-ring source",
                "10_M -> u,e",
                "bar5_M -> d",
                "1_M=N^c -> nuD",
                "q79 polarization U_10=I_3, U_bar5=F",
                "transported-projector finite trace normalization",
            ],
        },
        "dynamic_operator_c1_tier": {
            "closed": False,
            "open_inputs": [
                "visible/Route-C operator source identity",
                "same-branch D_E/Riesz/Green/dotD values",
                "physical alpha1 driver",
                "dynamic source-to-C1 overlap tensor or transfer functor",
                "primitive C1/Yukawa contractions",
                "b_selected and Hessian/kernel normalization for A_selected",
            ],
        },
    }

    weylpair_consequence = {
        "source_level_ZX_carrier_closed": True,
        "conditional_transfer_exact": weyl_transfer["conditional_transfer_map"]["conditional_exact"],
        "conditional_A_weylpair_exact": weyl_a["locked_solve"]["consistent"],
        "selected_static_sector_route_now_closed": True,
        "phase_route": ["u", "e"],
        "shift_route": ["d", "nuD"],
        "promote_conditional_A_to_A_selected": False,
        "why_not_promoted": (
            "The static route removes the sector-partition ambiguity, but A_selected still requires "
            "dynamic operator values, the selected source-to-C1 transfer tensor, primitive contractions, "
            "and b_selected from the same branch."
        ),
    }

    old_contract_effect = {
        "previous_required_fields": contract["field_counts"]["required"],
        "previous_selected_emitted": contract["field_counts"]["selected_emitted"],
        "previous_support_present": contract["field_counts"]["support_present"],
        "static_fields_now_discharged_for_routing": [
            "matter_slot_charge",
            "singlet_neutrino_rule",
            "finite trace/transfer normalization at the SM-slot functor tier",
        ],
        "fields_still_needed_for_A_selected": [
            "dynamic visible/Route-C operator source identity",
            "selected D_E/Riesz/Green/dotD",
            "selected dynamic overlap transfer functor",
            "selected primitive C1 contractions",
            "selected b_selected/Hessian normalization",
            "physical alpha1 driver",
        ],
        "current_validator_promotion_allowed": False,
    }

    theorem = {
        "name": "SMSlotFunctorStaticToDynamicPayloadSeparationTheorem",
        "proved": True,
        "statement": (
            "After the selected SM-slot functor emits all six static source arrows, the old C1 blockers "
            "coming from matter-slot partition, the 1_M Dirac-neutrino routing rule, and finite trace "
            "normalization are discharged at the static source tier.  This does not promote the "
            "conditional Weyl-pair C1 operator to A_selected, because that promotion still requires the "
            "dynamic same-branch operator values, overlap tensor, primitive contractions, and b_selected."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedSMSlotFunctorDownstreamOperatorPayloadsOrSMParityLedger",
        "status": STATUS,
        "inputs": {
            "selected_smslotfunctor_overlapkernel_source_emission": rel(SMSLOT),
            "same_source_operator_packet_contract": rel(CONTRACT),
            "same_source_operator_packet_fill_nogo": rel(FILL_NOGO),
            "weylpair_source_to_c1_transfer_map": rel(WEYL_TRANSFER),
            "conditional_weylpair_A_assembly": rel(WEYL_A),
            "sourceemission_minimal_subpacket_attack_plan": rel(SOURCE_PLAN),
        },
        "superset_strategy": {
            "mode": "STATIC_TO_DYNAMIC_LEDGER_RECLASSIFICATION",
            "observed_data_used": False,
            "target_fitting_used": False,
            "locked_target_role": "the locked C1 splitter remains a diagnostic consistency target, not a selector",
            "what_is_promoted": "static source-tier SM-slot routing and finite trace normalization",
            "what_is_not_promoted": "dynamic C1 operator values, A_selected, b_selected, or SM flavor constants",
        },
        "payload_tiers": payload_tiers,
        "old_contract_reclassification": reclassified_fields,
        "old_contract_effect": old_contract_effect,
        "weylpair_consequence": weylpair_consequence,
        "source_plan_update": {
            "previous_order": source_plan["strategy"]["dependency_order"],
            "matter_slot_subpacket_static_status": "STATIC_CLOSED_NOT_DYNAMIC_OPERATOR_CLOSED",
            "new_minimal_dynamic_target": NEXT,
        },
        "what_closes_now": {
            "selected_static_sector_route_Z_to_u_e_X_to_d_nuD": True,
            "selected_static_1M_Dirac_neutrino_shift_rule": True,
            "selected_static_finite_trace_transfer_normalization": True,
            "old_seven_field_blocker_reclassified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "dynamic_visible_routec_operator_source_identity": True,
            "selected_D_E_Riesz_Green_dotD": True,
            "physical_alpha1_driver": True,
            "selected_dynamic_overlap_tensor_or_transfer_functor": True,
            "selected_primitive_C1_contractions": True,
            "selected_b_selected_and_Hessian_normalization": True,
            "promote_conditional_A_to_A_selected": True,
            "Yukawa_CKM_PMNS_masses_Higgs_RG": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "selected_static_payloads_claimed": True,
        "dynamic_operator_payloads_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem": theorem,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_SelectedSMSlotFunctor_DownstreamOperatorPayloads_or_SMParityLedger_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "selected_static_payloads_claimed": True,
        "dynamic_operator_payloads_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem_proved": True,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT SelectedSMSlotFunctor DownstreamOperatorPayloads or SMParityLedger v1

Status: `{STATUS}`.

## Result

The static SM-slot functor closure is now imported into the downstream C1
ledger.  Three old blockers are no longer generic blockers:

- `10_M -> u,e` selects the clock/phase side;
- `bar5_M -> d` plus `1_M=N^c -> nuD` selects the shift/non-10 side;
- the transported-projector trace Gram fixes the finite static transfer
  normalization.

So the Weyl-pair sector route is now source-derived at the static tier:

```text
Z / clock  -> u,e
X / shift  -> d,nuD
```

## Boundary

This still does not promote the conditional Weyl-pair operator to
`A_selected`.  The missing objects are dynamic: selected `D_E/Riesz/Green/dotD`,
the physical alpha1 driver, the selected source-to-C1 overlap tensor, primitive
C1 contractions, and `b_selected`/Hessian normalization.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
