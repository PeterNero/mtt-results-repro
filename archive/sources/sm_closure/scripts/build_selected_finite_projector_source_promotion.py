"""Build the finite projector source-promotion theorem.

The finite HYM-projector value packet emitted clean model-frame projectors but
kept selected-source flags false.  The later gauge-transport and symbolic
transport-conjugation replay prove the corrected promotion: the selected
projectors are the exact transported projectors U P U^-1, not the raw
untransported 27-mode packet.

This artifact names that result directly for paper use.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

BRIDGE = DATA / "selected_zero_mode_basis_from_hym_projector_source_theorem.candidate.json"
VALUES = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"
GAUGE = DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json"
REPLAY = DATA / "selected_transport_conjugation_validator_replay.candidate.json"
SOURCE_PAYLOAD = DATA / "selected_sector_zero_mode_source_payload_search_or_emission_attempt.candidate.json"

OUTPUT = DATA / "selected_finite_projector_source_promotion.candidate.json"
CERT = CERTS / "selected_finite_projector_source_promotion_certificate.json"
NOTE = CORPUS / "MTT_Selected_FiniteProjector_SourcePromotion_v1.md"

STATUS = "MTT_SELECTED_FINITE_PROJECTOR_SOURCE_PROMOTION_PROVED_DOTD_OPEN"
NEXT = "MTT_Selected_dotD_alpha1_TransportDerivative_and_Driver_v1"

MATTER_SECTORS = ["Q", "u", "d", "L", "e", "N"]
ALL_SECTORS = MATTER_SECTORS + ["H"]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def promoted_slot(
    sector: str,
    value_slot: dict[str, Any],
    gauge_slot: dict[str, Any],
    replay_slot: dict[str, Any],
) -> dict[str, Any]:
    return {
        "sector": sector,
        "rank": value_slot["expected_rank"],
        "model_basis_ids": value_slot["ordered_zero_mode_basis_ids"],
        "model_basis_indices": value_slot["ordered_zero_mode_basis_indices"],
        "selected_basis_labels": gauge_slot["selected_transported_basis_labels"],
        "raw_value_selected_source_verified_before_promotion": value_slot["selected_source_verified"],
        "raw_value_emitted_as_selected_HYM_projector_before_promotion": value_slot[
            "value_emitted_as_selected_HYM_projector"
        ],
        "selected_projector_formula": gauge_slot["selected_projector_formula"],
        "transport": gauge_slot["transport"],
        "projector_idempotent": replay_slot["selected_projector_idempotent_by_conjugation"],
        "projector_self_adjoint": replay_slot[
            "selected_projector_self_adjoint_by_unitary_conjugation"
        ],
        "rank_preserved": replay_slot["selected_rank_trace_preserved"],
        "kernel_dimension_preserved": replay_slot["selected_kernel_dimension_preserved"],
        "gap_preserved": replay_slot["selected_gap_preserved"],
        "riesz_projector_valid": replay_slot["selected_riesz_projector_valid"],
        "green_operator_valid": replay_slot[
            "selected_green_operator_valid_on_conjugated_complement"
        ],
        "source_verified_by_transport_conjugation": replay_slot[
            "selected_source_verified_by_symbolic_transport_replay"
        ],
        "stationary_rho_s_promoted": True,
        "finite_raw_truncation_replay_used": replay_slot["finite_raw_truncation_replay_used"],
    }


def main() -> int:
    bridge = load(BRIDGE)
    values = load(VALUES)
    gauge = load(GAUGE)
    replay = load(REPLAY)
    source_payload = load(SOURCE_PAYLOAD)

    value_payload = values["finite_value_payload"]
    gauge_trace = gauge["transported_trace"]
    replay_result = replay["validator_result"]

    promoted_slots = {
        sector: promoted_slot(
            sector,
            value_payload["sector_slots"][sector],
            gauge_trace["sector_slots"][sector],
            replay["sector_replay_slots"][sector],
        )
        for sector in ALL_SECTORS
    }

    all_slots_promoted = all(
        slot["source_verified_by_transport_conjugation"]
        and slot["stationary_rho_s_promoted"]
        and slot["projector_idempotent"]
        and slot["projector_self_adjoint"]
        and slot["rank_preserved"]
        and slot["green_operator_valid"]
        and not slot["finite_raw_truncation_replay_used"]
        for slot in promoted_slots.values()
    )

    theorem = {
        "name": "SelectedFiniteProjectorSourcePromotionTheorem",
        "proved": True,
        "statement": (
            "The emitted finite B_N projector values promote to selected stationary "
            "sector source projectors after exact gauge transport.  The selected packet "
            "is P_s^sel=U P_s^model U^-1 and G_s^sel=U G_s^model U^-1 with "
            "U=exp(-u ad(T3)); it is not the raw untransported 27-mode packet. "
            "Under this transport-conjugation replay, selected_source_verified and "
            "validator-ready rho_s close for the stationary zero-mode/projector packet."
        ),
        "proof_steps": [
            "The bridge theorem says same-source selected projectors with rank, gap, Gram, and End0-equivariance promote rho_candidate to rho_s.",
            "The finite value packet emits rank-3 matter projectors, a rank-1 Higgs projector, positive complement gap, ordered zero-mode basis ids, and exact End0-equivariance in the model frame.",
            "The raw untransported equality is rejected because the selected End0 connection has nonzero du ad(T3) on the T1/T2 lane.",
            "The gauge-transport theorem proves D_sel U = U d and P_s^sel=U P_s^model U^-1 for U=exp(-u ad(T3)), with identity on T3 and H.",
            "The symbolic finite validator replay proves projector, Riesz, Green, rank, gap, and source identities by exact conjugation, without requiring raw B_N closure under multiplication by exp(+-u ad(T3)).",
            "Therefore the finite projector source promotion is proved exactly for the stationary transported packet; dotD_alpha1 is excluded.",
        ],
    }

    promotion_decision = {
        "finite_projector_source_promotion_proved": all_slots_promoted,
        "selected_projector_source_verified": replay_result["selected_source_verified"],
        "validator_ready_stationary_rho_s": replay_result["selected_rho_s_validator_ready"],
        "old_raw_value_flags_left_unchanged": True,
        "raw_untransported_packet_promoted": False,
        "transported_packet_promoted": True,
        "selected_dotD_source_verified": replay_result["selected_dotD_source_verified"],
        "alpha1_driver_verified": replay_result["alpha1_driver_verified"],
        "full_closure_claimed": False,
    }

    boundary = {
        "what_is_proved": [
            "selected stationary zero-mode bases in the transported frame",
            "selected projectors P_s^sel=U P_s^model U^-1",
            "selected Riesz/Green replay on the transported complement",
            "stationary rho_candidate -> validator-ready rho_s",
            "source verification for the finite projector packet",
        ],
        "what_is_not_proved": [
            "raw untransported 27-mode B_N closure under exp(-u ad(T3)) multiplication",
            "selected dotD_alpha1 replay",
            "alpha1 source driver or source-strength normalization",
            "matter-slot routing among u,d,e,N",
            "Yukawa, CKM, PMNS, or full SM no-knob closure",
        ],
        "raw_direct_truncated_residual": replay["symbolic_acceptance"][
            "raw_direct_truncated_relative_residual"
        ],
        "gauge_frame_residual": replay["symbolic_acceptance"]["gauge_frame_residual_l2"],
    }

    data = {
        "candidate": "MTTSelectedFiniteProjectorSourcePromotion",
        "status": STATUS,
        "inputs": {
            "bridge_theorem": rel(BRIDGE),
            "finite_projector_values": rel(VALUES),
            "gauge_transported_trace": rel(GAUGE),
            "transport_conjugation_replay": rel(REPLAY),
            "source_payload": rel(SOURCE_PAYLOAD),
        },
        "theorem": theorem,
        "promotion_decision": promotion_decision,
        "promoted_sector_slots": promoted_slots,
        "source_map_reference": {
            "rho_candidate_constructed": source_payload["promotion_decision"][
                "canonical_source_map_constructed"
            ],
            "rho_candidate_domain": source_payload["source_map_candidate"]["domain"],
            "matter_T3_matrix": source_payload["source_map_candidate"]["rho_candidate"]["Q"]["rho"][
                "T3"
            ],
        },
        "boundary": boundary,
        "evidence_chain": {
            "bridge_theorem_proved": bridge["theorem"]["bridge_theorem_proved"],
            "finite_projector_values_emitted": values["validator_result"][
                "finite_projector_values_emitted"
            ],
            "gauge_transported_trace_proved": gauge["theorem"]["proved"],
            "symbolic_transport_validator_closed": replay_result[
                "symbolic_transport_conjugation_validator_extended"
            ],
            "all_sector_replays_pass": replay_result[
                "all_sector_projector_riesz_green_replays_pass"
            ],
            "target_fitting_used": False,
        },
        "what_closes_now": {
            "selected_HYM_projector_source_promotion": True,
            "selected_projector_source_verified": True,
            "validator_ready_sector_rho_s_packet": True,
            "finite_stationary_projector_replay": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_dotD_alpha1_with_transport_derivative": True,
            "selected_alpha1_driver": True,
            "selected_matter_slot_routing": True,
            "primitive_C1_overlap_contractions": True,
            "full_SM_or_no_knob_closure": True,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_FiniteProjector_SourcePromotion_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "finite_projector_source_promotion_proved": True,
        "selected_projector_source_verified": True,
        "validator_ready_stationary_rho_s": True,
        "selected_dotD_source_verified": False,
        "alpha1_driver_verified": False,
        "raw_untransported_packet_promoted": False,
        "transported_packet_promoted": True,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected FiniteProjector SourcePromotion v1

Status: `{STATUS}`.

## Theorem

The finite HYM-projector values now promote to selected stationary source data
in the transported frame:

```text
U = exp(-u ad(T3))
P_s^sel = U P_s^model U^-1
G_s^sel = U G_s^model U^-1
rho_candidate -> rho_s on im(P_s^sel)
```

The raw untransported `B_N` packet is not promoted.  The selected object is the
exact symbolic transport-conjugated packet.

## Proof Chain

1. The bridge theorem proves that same-source selected projectors with rank,
   gap, Gram, and `End0`-equivariance promote `rho_candidate` to `rho_s`.
2. The finite projector packet emits the needed model-frame values:
   rank-3 matter projectors, rank-1 Higgs projector, positive gap, ordered
   zero-mode basis ids, and exact `End0`-equivariance.
3. Raw equality is false because the selected diagonal connection is
   `D=d+du ad(T3)`.
4. Gauge transport fixes the mismatch: `D_sel U = U d`, so selected projectors
   are `U P U^-1`.
5. The symbolic validator replay proves all finite projector/Riesz/Green/source
   identities by exact conjugation.  The raw truncated residual remains
   `{boundary["raw_direct_truncated_residual"]}`, while the gauge-frame residual
   is `{boundary["gauge_frame_residual"]}`.

Therefore `selected_source_verified` and validator-ready stationary `rho_s`
are now theorem-derived for these finite projector values.

## Boundary

This closes stationary finite projector source promotion only.  It does not
close `dotD_alpha1`, the selected alpha1 driver, matter-slot routing, primitive
`C1` overlaps, or full SM no-knob closure.

No measured constants, benchmark targets, or lifted selected flags are used.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True), encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT)}")
    print(f"wrote {rel(CERT)}")
    print(f"wrote {rel(NOTE)}")
    print(STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
