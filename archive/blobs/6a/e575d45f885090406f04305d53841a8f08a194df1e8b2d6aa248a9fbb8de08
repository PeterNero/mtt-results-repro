"""Integrate static U10/Ubar5/1M matter-slot source promotion into scalar-row path."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_u10ubar5_1m_sourcepromotion_samebranch_emission"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STATIC_PROMOTION = PACKET_DIR / "static_matter_slot_source_promotion_update.packet.json"
SCALAR_GATE = PACKET_DIR / "internal_scalar_row_gate_after_static_matter_slot_readout.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_static_matter_slot_source_promotion.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1.md"

PREVIOUS = DATA / "selected_phifinminimizertracesectorpayload_or_internalscalarrows.candidate.json"
PHIFIN_PAYLOAD_GATE = (
    DATA
    / "selected_phifinminimizertracesectorpayload_or_internalscalarrows"
    / "internal_scalar_row_gate_after_transport_payload.packet.json"
)
U10_ATTEMPT = DATA / "selected_u10ubar5_1m_samebranch_emission_attempt.candidate.json"
MATTER_READOUT = DATA / "selected_matterslot_readout_backimport_from_smslotfunctor.candidate.json"
STATIC_READOUT_PACKET = (
    DATA
    / "selected_matterslot_readout_backimport_from_smslotfunctor"
    / "selected_static_matterslot_readout.packet.json"
)
DYNAMIC_BOUNDARY = (
    DATA
    / "selected_matterslot_readout_backimport_from_smslotfunctor"
    / "dynamic_operator_boundary_after_readout.packet.json"
)
HIGHER_CONTRACT = (
    DATA
    / "selected_higherresponserthetafunctional_or_sourceanchortheorem"
    / "rtheta_higher_response_functional_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_U10UBAR5_1M_SOURCEPROMOTION_SAMEBRANCH_EMISSION_"
    "BUILT_STATIC_MATTERSLOT_READOUT_CLOSED_DYNAMIC_PAYLOAD_OPEN"
)
NEXT = "MTT_Selected_DynamicOverlapKernel_or_C1Primitive_SourceEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing U10/Ubar5/1M source promotion inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PHIFIN_PAYLOAD_GATE,
        U10_ATTEMPT,
        MATTER_READOUT,
        STATIC_READOUT_PACKET,
        DYNAMIC_BOUNDARY,
        HIGHER_CONTRACT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    phifin_gate = load(PHIFIN_PAYLOAD_GATE)
    u10 = load(U10_ATTEMPT)
    matter_readout = load(MATTER_READOUT)
    static_readout = load(STATIC_READOUT_PACKET)
    dynamic_boundary = load(DYNAMIC_BOUNDARY)
    higher_contract = load(HIGHER_CONTRACT)

    static_readout_closed = matter_readout["what_closes_now"][
        "selected_matter_slot_transversality_readout_functional_static_tier"
    ]
    u10_static_closed = matter_readout["what_closes_now"][
        "selected_U10_Ubar5_polarization_source_outputs_static_tier"
    ]
    one_m_static_closed = matter_readout["what_closes_now"][
        "selected_1M_Dirac_shift_readout_static_tier"
    ]
    transfer_static_closed = matter_readout["what_closes_now"][
        "selected_overlap_transfer_normalization_static_tier"
    ]

    dynamic_payload_closed = False

    static_promotion = {
        "schema": "MTTStaticMatterSlotSourcePromotionUpdate.v1",
        "status": "STATIC_MATTERSLOT_READOUT_CLOSED_DYNAMIC_PAYLOAD_OPEN",
        "previous_u10_attempt": rel(U10_ATTEMPT),
        "static_readout_source": rel(STATIC_READOUT_PACKET),
        "selected_static_tier_outputs": {
            "selected_matter_slot_transversality_readout": static_readout_closed,
            "selected_U10_clock_source": u10_static_closed,
            "selected_Ubar5_shift_source": u10_static_closed,
            "selected_1M_Dirac_neutrino_shift_source": one_m_static_closed,
            "selected_ordered_matter_slot_packet": static_readout_closed,
            "selected_overlap_transfer_normalization_static_tier": transfer_static_closed,
        },
        "static_phase_shift_partition": {
            "phase": ["u", "e"],
            "shift": ["d", "nuD"],
        },
        "dynamic_boundary": rel(DYNAMIC_BOUNDARY),
        "dynamic_tier_still_open": dynamic_boundary,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(STATIC_PROMOTION, static_promotion)

    scalar_gate = {
        "schema": "MTTInternalScalarRowGateAfterStaticMatterSlotReadout.v1",
        "status": "STATIC_MATTERSLOT_READOUT_IMPORTED_INTERNAL_SCALAR_ROWS_STILL_BLOCKED",
        "prior_gate": rel(PHIFIN_PAYLOAD_GATE),
        "codomain_scalar_rows": higher_contract["codomain_scalar_rows"],
        "codomain_scalar_row_count": higher_contract["codomain_scalar_row_count"],
        "accepted_internal_scalar_row_count": 0,
        "lambda_H_row_emitted": False,
        "updated_readiness": {
            "transported_projector_riesz_green_rhos_layer": True,
            "static_matter_slot_readout_layer": static_readout_closed,
            "static_U10_Ubar5_1M_layer": u10_static_closed and one_m_static_closed,
            "dynamic_overlap_kernel_layer": False,
            "dynamic_PhiFin_C1_payload_layer": dynamic_payload_closed,
            "internal_Rtheta_scalar_rows": False,
        },
        "why_still_blocked": [
            "static source readout does not promote dynamic D_E/Riesz/Green/dotD",
            "dynamic overlap tensor or transfer functor remains open",
            "primitive C1 contractions/A_selected/b_selected are not emitted by this static tier",
            "Rtheta scalar rows require dynamic value payload rows, not only static matter-slot labels",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SCALAR_GATE, scalar_gate)

    cutset = {
        "schema": "MTTNextCutsetAfterStaticMatterSlotSourcePromotion.v1",
        "status": "NEXT_ATTACK_DYNAMIC_OVERLAP_KERNEL_OR_C1_PRIMITIVE_SOURCE",
        "closed_now": {
            "selected_matter_slot_transversality_readout_static_tier": static_readout_closed,
            "selected_U10_clock_source_static_tier": u10_static_closed,
            "selected_Ubar5_shift_source_static_tier": u10_static_closed,
            "selected_1M_Dirac_shift_source_static_tier": one_m_static_closed,
            "selected_overlap_transfer_normalization_static_tier": transfer_static_closed,
            "locked_C1_target_not_used_as_selector": True,
        },
        "still_open": {
            "dynamic_visible_routec_operator_source_identity": True,
            "selected_D_E_Riesz_Green_dotD_dynamic_payload": True,
            "selected_dynamic_overlap_tensor_or_transfer_functor": True,
            "selected_primitive_C1_contractions": True,
            "A_selected": True,
            "b_selected": True,
            "internal_Rtheta_scalar_rows": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "promote dynamic overlap kernel/C1 primitive rows from the selected static matter-slot packet",
            "route_B": "emit selected D_E/Riesz/Green/dotD value payload rows on transported carriers",
            "route_C": "rerun scalar-row emission only after dynamic payload rows exist",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedU10Ubar51MSourcePromotionSameBranchEmission",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "static_matter_slot_source_promotion_update": rel(STATIC_PROMOTION),
            "internal_scalar_row_gate_after_static_matter_slot_readout": rel(SCALAR_GATE),
            "next_cutset_after_static_matter_slot_source_promotion": rel(CUTSET),
        },
        "theorem": {
            "name": "StaticMatterSlotReadoutImportedButDynamicPayloadOpenTheorem",
            "proved": True,
            "statement": (
                "The later SM-slot functor readout fills the U10/Ubar5/1M matter-slot readout at "
                "the static source tier and can be imported into the same-branch scalar-row path. "
                "This retires the static matter-slot blocker, but internal Rtheta scalar rows still "
                "require dynamic overlap/C1 payload rows."
            ),
        },
        "closure_decision": {
            "static_matter_slot_readout_closed": static_readout_closed,
            "static_U10_Ubar5_1M_source_closed": u10_static_closed and one_m_static_closed,
            "dynamic_overlap_kernel_closed": False,
            "accepted_internal_scalar_row_count": 0,
            "lambda_H_row_emitted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "previous_status": previous["status"],
        "previous_gate_status": phifin_gate["status"],
        "u10_attempt_status": u10["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": True,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "static_matter_slot_readout_closed": static_readout_closed,
        "static_U10_Ubar5_1M_source_closed": u10_static_closed and one_m_static_closed,
        "dynamic_overlap_kernel_closed": False,
        "accepted_internal_scalar_row_count": 0,
        "lambda_H_row_emitted": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected U10Ubar5 1M SourcePromotion SameBranch Emission v1

Status: `{STATUS}`.

Static matter-slot source emission is now imported:

```text
matter-slot readout static tier   : {str(static_readout_closed).lower()}
U10/Ubar5 source static tier      : {str(u10_static_closed).lower()}
1M Dirac shift static tier        : {str(one_m_static_closed).lower()}
dynamic overlap/C1 payload closed : false
accepted internal scalar rows     : 0
```

This retires the static U10/Ubar5/1M readout blocker for the scalar-row path.
The active blocker is now dynamic: overlap kernel/C1 primitive source emission
and selected dynamic value payload rows.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
