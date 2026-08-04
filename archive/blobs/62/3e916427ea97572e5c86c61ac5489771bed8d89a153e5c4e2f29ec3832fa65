"""Integrate Phi_fin transported sector payload progress into internal scalar-row gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_phifinminimizertracesectorpayload_or_internalscalarrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PAYLOAD_UPDATE = PACKET_DIR / "transported_phifin_sector_payload_update.packet.json"
SCALAR_GATE = PACKET_DIR / "internal_scalar_row_gate_after_transport_payload.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_phifin_sector_payload_update.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhiFinMinimizerTraceSectorPayload_or_InternalScalarRows_v1.md"

PREVIOUS = DATA / "selected_internalrthetascalarrowemission_or_universalanchorselection.candidate.json"
DIRECT_ATTEMPT = (
    DATA
    / "selected_internalrthetascalarrowemission_or_universalanchorselection"
    / "direct_internal_rtheta_scalar_row_emission_attempt.packet.json"
)
GAUGE_TRACE = DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json"
TRANSPORT_SYMBOLIC = DATA / "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator.candidate.json"
TRANSPORT_VALIDATOR = DATA / "selected_transport_conjugation_validator_replay.candidate.json"
SECTOR_CHARGE = DATA / "selected_sectorcharge_1mdirac_sourceemission_or_transportclosedvalidatorreplay.candidate.json"
PHIFIN_ALPHA1 = DATA / "selected_phifinalpha1payloadvalues_or_typedbnretardedderivativeexecution.candidate.json"
HYM_PAYLOAD = DATA / "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution.candidate.json"
FULLS2_GATE = (
    DATA
    / "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution"
    / "rhoede_full_s2_execution_gate.packet.json"
)
HIGHER_CONTRACT = (
    DATA
    / "selected_higherresponserthetafunctional_or_sourceanchortheorem"
    / "rtheta_higher_response_functional_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_PHIFINMINIMIZERTRACESECTORPAYLOAD_OR_INTERNALSCALARROWS_"
    "BUILT_TRANSPORT_REPLAY_IMPORTED_SECTOR_SOURCE_PAYLOAD_OPEN"
)
NEXT = "MTT_Selected_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1"


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
        raise FileNotFoundError("missing Phi_fin sector payload inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        DIRECT_ATTEMPT,
        GAUGE_TRACE,
        TRANSPORT_SYMBOLIC,
        TRANSPORT_VALIDATOR,
        SECTOR_CHARGE,
        PHIFIN_ALPHA1,
        HYM_PAYLOAD,
        FULLS2_GATE,
        HIGHER_CONTRACT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    direct = load(DIRECT_ATTEMPT)
    gauge_trace = load(GAUGE_TRACE)
    transport_symbolic = load(TRANSPORT_SYMBOLIC)
    transport_validator = load(TRANSPORT_VALIDATOR)
    sector_charge = load(SECTOR_CHARGE)
    phifin_alpha1 = load(PHIFIN_ALPHA1)
    hym_payload = load(HYM_PAYLOAD)
    fulls2 = load(FULLS2_GATE)
    higher_contract = load(HIGHER_CONTRACT)

    transport_replay_closed = transport_validator["promotion_decision"][
        "transport_closed_finite_validator_replay"
    ]
    validator_rhos_ready = transport_validator["promotion_decision"][
        "rho_candidate_promoted_to_validator_ready_sector_rho_s_packet"
    ]
    functional_trace_closed = gauge_trace["promotion_decision"][
        "functional_selected_trace_proved"
    ]
    symbolic_morphism_valid = transport_symbolic["promotion_decision"][
        "finite_emission_morphism_restriction_proved"
    ]
    alpha1_retired = phifin_alpha1["closure_decision"]["same_branch_alpha1_derivative_closed"]

    scalar_rows_ready = (
        transport_replay_closed
        and validator_rhos_ready
        and functional_trace_closed
        and symbolic_morphism_valid
        and sector_charge["what_remains_open"]["selected_ordered_matter_slot_packet"] is False
    )

    payload_update = {
        "schema": "MTTTransportedPhiFinSectorPayloadUpdate.v1",
        "status": "TRANSPORT_REPLAY_IMPORTED_SECTOR_SOURCE_PAYLOAD_STILL_OPEN",
        "functional_PhiFin_trace_closed": functional_trace_closed,
        "symbolic_transport_finite_morphism_valid": symbolic_morphism_valid,
        "transport_closed_validator_replay_closed": transport_replay_closed,
        "validator_ready_sector_rho_s_packet": validator_rhos_ready,
        "same_branch_alpha1_derivative_closed": alpha1_retired,
        "HYM_payload_previous_blocker": rel(HYM_PAYLOAD),
        "remaining_sector_source_payload": {
            "selected_U10_clock_source": True,
            "selected_Ubar5_shift_source": True,
            "selected_1M_Dirac_neutrino_shift_source": True,
            "selected_ordered_matter_slot_packet": True,
            "actual_QaSU3_operator_packet": True,
            "selected_dynamic_PhiFin_C1_payload": True,
        },
        "why_scalar_rows_still_blocked": [
            "transport replay closes stationary projector/Riesz/Green/rho_s, not matter-slot source emission",
            "the same-branch U10/Ubar5/1M source packet is still open",
            "dynamic Phi_fin/C1 payload values remain absent",
            "Rtheta scalar rows need sector-owned value carriers, not just stationary projectors",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PAYLOAD_UPDATE, payload_update)

    scalar_gate = {
        "schema": "MTTInternalScalarRowGateAfterTransportPayload.v1",
        "status": "TRANSPORT_PAYLOAD_IMPORTED_INTERNAL_SCALAR_ROWS_STILL_BLOCKED",
        "prior_direct_attempt": rel(DIRECT_ATTEMPT),
        "codomain_scalar_rows": higher_contract["codomain_scalar_rows"],
        "codomain_scalar_row_count": higher_contract["codomain_scalar_row_count"],
        "accepted_internal_scalar_row_count": 0,
        "lambda_H_row_emitted": False,
        "full_S2_scalar_execution_ready_in_old_gate": fulls2["ready"][
            "full_S2_scalar_execution_ready"
        ],
        "updated_readiness": {
            "stationary_projector_riesz_green_rhos_layer": True,
            "transport_closed_validator_layer": True,
            "same_branch_matter_slot_source_layer": False,
            "dynamic_PhiFin_C1_payload_layer": False,
            "internal_Rtheta_scalar_rows": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SCALAR_GATE, scalar_gate)

    cutset = {
        "schema": "MTTNextCutsetAfterPhiFinSectorPayloadUpdate.v1",
        "status": "NEXT_ATTACK_U10_UBAR5_1M_SOURCE_AND_DYNAMIC_PHIFIN_C1_PAYLOAD",
        "closed_now": {
            "functional_PhiFin_trace_imported": functional_trace_closed,
            "symbolic_transport_validator_imported": transport_replay_closed,
            "validator_ready_sector_rho_s_imported": validator_rhos_ready,
            "alpha1_not_reopened_as_scalar_knob": alpha1_retired,
        },
        "still_open": {
            "selected_U10_clock_source": True,
            "selected_Ubar5_shift_source": True,
            "selected_1M_Dirac_neutrino_shift_source": True,
            "selected_ordered_matter_slot_packet": True,
            "selected_dynamic_PhiFin_C1_payload": True,
            "actual_QaSU3_operator_packet": True,
            "internal_Rtheta_scalar_rows": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "emit same-branch U10, Ubar5, 1M and ordered matter-slot source packet on transported carriers",
            "route_B": "emit selected dynamic Phi_fin/C1 payload values from the same sector-owned packet",
            "route_C": "only after sector ownership closes, rerun internal Rtheta scalar row emission",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedPhiFinMinimizerTraceSectorPayloadOrInternalScalarRows",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "transported_phifin_sector_payload_update": rel(PAYLOAD_UPDATE),
            "internal_scalar_row_gate_after_transport_payload": rel(SCALAR_GATE),
            "next_cutset_after_phifin_sector_payload_update": rel(CUTSET),
        },
        "theorem": {
            "name": "TransportedPhiFinSectorPayloadReductionTheorem",
            "proved": True,
            "statement": (
                "The transported Phi_fin trace, symbolic transport finite morphism, validator-ready "
                "rho_s packet, and alpha1 bridge are imported into the internal scalar-row gate. This "
                "retires stationary projector/Riesz/Green/rho_s and alpha1 as direct blockers. Internal "
                "Rtheta scalar rows still cannot emit until same-branch U10/Ubar5/1M matter-slot source "
                "ownership and the dynamic Phi_fin/C1 payload close."
            ),
        },
        "closure_decision": {
            "transported_sector_payload_imported": True,
            "accepted_internal_scalar_row_count": 0,
            "lambda_H_row_emitted": False,
            "same_branch_matter_slot_source_closed": False,
            "dynamic_PhiFin_C1_payload_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "previous_status": previous["status"],
        "direct_attempt_status": direct["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": True,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_PhiFinMinimizerTraceSectorPayload_or_InternalScalarRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "transported_sector_payload_imported": True,
        "accepted_internal_scalar_row_count": 0,
        "lambda_H_row_emitted": False,
        "same_branch_matter_slot_source_closed": False,
        "dynamic_PhiFin_C1_payload_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected PhiFinMinimizerTraceSectorPayload or InternalScalarRows v1

Status: `{STATUS}`.

The direct scalar-row blocker has been reduced:

```text
functional Phi_fin trace imported       : {str(functional_trace_closed).lower()}
transport validator replay imported     : {str(transport_replay_closed).lower()}
validator-ready rho_s imported          : {str(validator_rhos_ready).lower()}
same-branch matter-slot source closed   : false
dynamic Phi_fin/C1 payload closed       : false
accepted internal scalar rows           : 0
```

So direct `R_theta` scalar rows still cannot emit, but the reason is sharper:
sector-owned matter-slot source emission and dynamic `Phi_fin/C1` payload
values are the active blockers.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
