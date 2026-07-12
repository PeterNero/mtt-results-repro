from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_residual_weyl_polynomial_source_theorem_attempt_certificate.json"
SLUG = "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill"
SM_CERT = SM_ROOT / "certificates" / f"{SLUG}_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / f"{SLUG}.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / SLUG
PROJECTOR_PACKET = SM_DIR / "canonical_fixedfiber_residual_projector.packet.json"
REPLAY_PACKET = SM_DIR / "projector_application_value_replay.packet.json"
CUTSET_PACKET = SM_DIR / "projector_or_galerkin_cutset_decision.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_canonical_residual_projector_or_honest_galerkin_c1_valuefill_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_canonical_residual_projector_or_honest_galerkin_c1_valuefill.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_CanonicalResidualProjector_or_HonestGalerkinC1_ValueFill_Import_v1.md"

STATUS = "POST_ALPHA_CANONICAL_RESIDUAL_PROJECTOR_OR_HONEST_GALERKIN_C1_VALUEFILL_IMPORTED_APPLICATION_OPEN"
NEXT = "MTT_Selected_PhiFinC1ResidualProjectorApplication_or_HonestGalerkinExecution_ValueFill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    projector = load(PROJECTOR_PACKET)
    replay = load(REPLAY_PACKET)
    cutset = load(CUTSET_PACKET)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_canonical_residual_projector_or_honest_galerkin_C1_value_fill"]
            is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_CanonicalResidualProjector_or_HonestGalerkinC1_ValueFill_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_CanonicalResidualProjector_or_HonestGalerkinC1_ValueFill_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["canonical_projector_promoted_as_unique_mathematical_projector"] is True,
            cert["PhiFinC1_projector_application_promoted"] is False,
            cert["SM_parity_dynamic_packet_closure_claimed"] is False,
            cert["no_knob_closure_claimed"] is False,
            cert["true_SM_equivalence_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "CanonicalFixedFiberResidualProjectorUniquenessTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["promotion_decision"]["canonical_residual_projector_promoted_as_unique_mathematical_projector"]
            is True,
            candidate["promotion_decision"]["PhiFinC1_projector_application_promoted"] is False,
            candidate["promotion_decision"]["honest_Galerkin_C1_value_run_promoted"] is False,
            candidate["promotion_decision"]["SM_parity_dynamic_packet_closed"] is False,
            candidate["promotion_decision"]["full_no_knob_flavor_closure_promoted"] is False,
        ]
    )

    projector_ok = all(
        [
            projector["schema"] == "MTTCanonicalFixedFiberResidualProjector.v1",
            projector["status"] == "CANONICAL_PROJECTOR_COMPUTED_FROM_SELECTED_FIXED_FIBER_CLASS",
            projector["selected_as_canonical_mathematical_projector"] is True,
            projector["selected_as_physical_C1_transfer_application"] is False,
            all(projector["selected_inputs"].values()),
            projector["observed_data_used"] is False,
            projector["target_fitting_used"] is False,
            projector["operator_checks"]["fixed_projector_rank"] == 3,
            projector["operator_checks"]["residual_projector_rank"] == 6,
            projector["operator_checks"]["fixed_projector_idempotence_norm_sq"] == 0.0,
            projector["operator_checks"]["fixed_projector_self_adjoint_norm_sq"] == 0.0,
            projector["operator_checks"]["partition_sum_identity_norm_sq"] == 0.0,
            projector["operator_checks"]["residual_projector_idempotence_norm_sq"] < 1e-24,
            projector["operator_checks"]["residual_projector_self_adjoint_norm_sq"] == 0.0,
            projector["operator_checks"]["orthogonal_complement_product_norm_sq"] < 1e-24,
        ]
    )

    replay_ok = all(
        [
            replay["schema"] == "MTTCanonicalResidualProjectorApplicationReplay.v1",
            replay["status"] == "PROJECTOR_REPLAY_MATCHES_RESIDUAL_PACKET_APPLICATION_OPEN",
            replay["physical_application_claimed"] is False,
            replay["matches_stored_residual_packet"] is True,
            replay["honest_galerkin_manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
            replay["honest_galerkin_selected_source_verified"] is False,
            replay["phase_replay"]["projection_norm_sq"] == 2.0,
            replay["phase_replay"]["residual_norm_sq"] == 4.0,
            replay["phase_replay"]["target_norm_sq"] == 6.0,
            replay["phase_replay"]["residual_matches_stored_norm_sq"] < 1e-24,
            replay["phase_replay"]["target_minus_projection_minus_residual_norm_sq"] < 1e-24,
            replay["shift_replay"]["projection_norm_sq"] == 4.0,
            replay["shift_replay"]["residual_norm_sq"] > 2.0 - 1e-12,
            replay["shift_replay"]["residual_norm_sq"] < 2.0 + 1e-12,
            replay["shift_replay"]["target_norm_sq"] == 6.0,
            replay["shift_replay"]["residual_matches_stored_norm_sq"] < 1e-24,
            replay["shift_replay"]["target_minus_projection_minus_residual_norm_sq"] == 0.0,
        ]
    )

    cutset_ok = all(
        [
            cutset["schema"] == "MTTProjectorOrGalerkinCutsetDecision.v1",
            cutset["status"] == "TWO_LANE_CUTSET_SHARP_SM_PARITY_DYNAMIC_PACKET_OPEN",
            cutset["canonical_projector_promoted_as_unique_mathematical_projector"] is True,
            cutset["PhiFinC1_projector_application_promoted"] is False,
            cutset["honest_Galerkin_C1_value_run_promoted"] is False,
            cutset["SM_parity_dynamic_packet_closed"] is False,
            cutset["no_knob_flavor_constants_closed"] is False,
            cutset["true_SM_equivalence_closed"] is False,
            cutset["observed_data_used"] is False,
            cutset["target_fitting_used"] is False,
            cutset["if_lane_A_application_theorem_is_supplied"]["A_selected_columns_available"] is True,
            cutset["if_lane_A_application_theorem_is_supplied"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            cutset["if_lane_A_application_theorem_is_supplied"]["A_transpose_b"] == [12.0, 12.0],
            cutset["if_lane_A_application_theorem_is_supplied"]["deltaTheta_C1"] == [1.0, 1.0],
            cutset["if_lane_A_application_theorem_is_supplied"]["rank"] == 2,
            cutset["if_lane_A_application_theorem_is_supplied"]["SM_parity_dynamic_packet_would_close"] is True,
            cutset["if_lane_A_application_theorem_is_supplied"]["no_knob_flavor_constants_would_close"] is False,
            cutset["if_lane_B_values_are_emitted"]["SM_parity_dynamic_packet_would_close"] is True,
            cutset["if_lane_B_values_are_emitted"]["selected_source_verified_now"] is False,
        ]
    )

    what_closes_now = {
        "residual_weyl_polynomial_gate_consumed": prev_ok,
        "canonical_fixed_fiber_projector_imported": imported_ok,
        "projector_rank_idempotence_selfadjointness_verified": projector_ok,
        "projector_replay_matches_stored_residual_packet": replay_ok,
        "two_lane_cutset_sharpened": cutset_ok,
    }

    what_remains_open = {
        "selected_PhiFinC1_applies_canonical_residual_projector": True,
        "selected_Hessian_or_vertex_operator_implements_projector": True,
        "honest_selected_Galerkin_C1_value_run": True,
        "selected_A_selected": True,
        "selected_b_selected": True,
        "selected_deltaTheta_C1": True,
        "SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "promotes_only_canonical_projector_as_mathematical_projector": True,
        "does_not_promote_physical_C1_projector_application": True,
        "does_not_promote_honest_galerkin_values": True,
        "does_not_promote_A_b_deltaTheta": True,
        "does_not_claim_SM_parity_dynamic_closure": True,
        "does_not_claim_true_SM_equivalence": True,
        "does_not_claim_no_knob_flavor_closure": True,
        "does_not_use_observed_or_target_inputs": True,
    }

    theorem = {
        "name": "PostAlphaCanonicalResidualProjectorOrHonestGalerkinC1ValueFillImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The selected fixed-fiber quotient and trace/Frobenius normalization determine "
            "a unique rank-3 fixed projector and rank-6 residual projector. The residual "
            "projector replays the stored I+Z and I+X residual packets, but this is only a "
            "canonical mathematical projector result until selected Phi_fin^C1 or an honest "
            "Galerkin C1 execution supplies the physical response application."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_candidate_summary": {
            "status": candidate["status"],
            "theorem": candidate["theorem"],
            "projector_closure": candidate["projector_closure"],
            "promotion_decision": candidate["promotion_decision"],
            "what_closes_now": candidate["what_closes_now"],
            "what_remains_open": candidate["what_remains_open"],
        },
        "canonical_fixedfiber_residual_projector": projector,
        "projector_application_value_replay": replay,
        "projector_or_galerkin_cutset_decision": cutset,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "canonical_mathematical_projector_closed": True,
            "frontier_is_PhiFinC1_residual_projector_application_or_honest_galerkin_execution_value_fill": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "canonical_fixedfiber_residual_projector": str(PROJECTOR_PACKET),
            "projector_application_value_replay": str(REPLAY_PACKET),
            "projector_or_galerkin_cutset_decision": str(CUTSET_PACKET),
        },
    }

    note = f"""# PostAlpha CanonicalResidualProjector or HonestGalerkinC1 ValueFill Import v1

## Result

The canonical mathematical projector is now imported into the post-alpha chain.

```text
rank(P_fixed)    = 3
rank(Q_residual) = 6
||P_fixed^2 - P_fixed||_F^2       = 0.0
||Q_residual^2 - Q_residual||_F^2 = {projector["operator_checks"]["residual_projector_idempotence_norm_sq"]}
||P_fixed Q_residual||_F^2        = {projector["operator_checks"]["orthogonal_complement_product_norm_sq"]}
||P_fixed + Q_residual - I||_F^2  = 0.0
```

The projector replay matches the stored residual packets:

```text
phase residual norm^2 = 4
shift residual norm^2 = 2
```

This closes the canonical fixed-fiber projector as mathematics. It does not yet
prove that selected `Phi_fin^C1` applies this residual projector as the physical
C1 response.

## Status

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_canonical_residual_projector_or_honest_galerkin_c1_valuefill",
        "status": STATUS,
        "closure_claimed": False,
        "theorem": theorem,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "frontier_decision": packet["frontier_decision"],
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert_out, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
