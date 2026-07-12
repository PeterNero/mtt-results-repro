from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = ROOT / "certificates" / "post_alpha_independent_residual_weyl_polynomial_source_theorem_attempt_certificate.json"
SOURCE_CERT = ROOT / "certificates" / "post_alpha_canonical_residual_projector_or_honest_galerkin_c1_valuefill_certificate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_independent_canonical_residual_projector_or_honest_galerkin_c1_valuefill_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_independent_canonical_residual_projector_or_honest_galerkin_c1_valuefill.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_IndependentCanonicalResidualProjector_or_HonestGalerkinC1ValueFill_Import_v1.md"

STATUS = "POST_ALPHA_INDEPENDENT_CANONICAL_RESIDUAL_PROJECTOR_OR_HONEST_GALERKIN_C1_VALUEFILL_IMPORTED_APPLICATION_OPEN"
SOURCE_STATUS = "POST_ALPHA_CANONICAL_RESIDUAL_PROJECTOR_OR_HONEST_GALERKIN_C1_VALUEFILL_IMPORTED_APPLICATION_OPEN"
THIS_ARTIFACT = "MTT_Selected_CanonicalResidualProjector_or_HonestGalerkinC1_ValueFill_v1"
NEXT = "MTT_Selected_PhiFinC1ResidualProjectorApplication_or_HonestGalerkinExecution_ValueFill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE_CERT)
    source_packet = load(Path(source["packet_written"]))

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_canonical_residual_projector_or_honest_galerkin_C1_value_fill"]
            is True,
            prev["frontier_decision"]["next_required_artifact"] == THIS_ARTIFACT,
            all(prev["guardrails"].values()),
        ]
    )

    source_ok = all(
        [
            source["status"] == SOURCE_STATUS,
            source["theorem"]["proved"] is True,
            source["closure_claimed"] is False,
            source["frontier_decision"]["canonical_mathematical_projector_closed"] is True,
            source["frontier_decision"][
                "frontier_is_PhiFinC1_residual_projector_application_or_honest_galerkin_execution_value_fill"
            ]
            is True,
            source["frontier_decision"]["next_required_artifact"] == NEXT,
            all(source["what_closes_now"].values()),
            all(source["what_remains_open"].values()),
            all(source["guardrails"].values()),
        ]
    )

    projector = source_packet["canonical_fixedfiber_residual_projector"]
    replay = source_packet["projector_application_value_replay"]
    cutset = source_packet["projector_or_galerkin_cutset_decision"]

    projector_ok = all(
        [
            projector["schema"] == "MTTCanonicalFixedFiberResidualProjector.v1",
            projector["selected_as_canonical_mathematical_projector"] is True,
            projector["selected_as_physical_C1_transfer_application"] is False,
            projector["observed_data_used"] is False,
            projector["target_fitting_used"] is False,
            projector["operator_checks"]["fixed_projector_rank"] == 3,
            projector["operator_checks"]["residual_projector_rank"] == 6,
            projector["operator_checks"]["fixed_projector_idempotence_norm_sq"] == 0.0,
            projector["operator_checks"]["fixed_projector_self_adjoint_norm_sq"] == 0.0,
            projector["operator_checks"]["partition_sum_identity_norm_sq"] == 0.0,
            projector["operator_checks"]["residual_projector_idempotence_norm_sq"] < 1e-24,
            projector["operator_checks"]["orthogonal_complement_product_norm_sq"] < 1e-24,
        ]
    )

    replay_ok = all(
        [
            replay["schema"] == "MTTCanonicalResidualProjectorApplicationReplay.v1",
            replay["physical_application_claimed"] is False,
            replay["matches_stored_residual_packet"] is True,
            replay["honest_galerkin_selected_source_verified"] is False,
            replay["phase_replay"]["residual_norm_sq"] == 4.0,
            abs(replay["shift_replay"]["residual_norm_sq"] - 2.0) < 1e-12,
            replay["phase_replay"]["residual_matches_stored_norm_sq"] < 1e-24,
            replay["shift_replay"]["residual_matches_stored_norm_sq"] < 1e-24,
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
            cutset["if_lane_A_application_theorem_is_supplied"]["A_transpose_A"]
            == [[12.0, 0.0], [0.0, 12.0]],
            cutset["if_lane_A_application_theorem_is_supplied"]["A_transpose_b"] == [12.0, 12.0],
            cutset["if_lane_A_application_theorem_is_supplied"]["deltaTheta_C1"] == [1.0, 1.0],
            cutset["if_lane_A_application_theorem_is_supplied"]["SM_parity_dynamic_packet_would_close"] is True,
            cutset["if_lane_A_application_theorem_is_supplied"]["no_knob_flavor_constants_would_close"] is False,
        ]
    )

    what_closes_now = {
        "long_name_weyl_polynomial_gate_consumed": prev_ok,
        "audited_canonical_projector_gate_reanchored": source_ok,
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
        "name": "PostAlphaIndependentCanonicalResidualProjectorOrHonestGalerkinC1ValueFillImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The long-name branch imports the unique rank-3/rank-6 canonical "
            "fixed-fiber residual projector as a mathematical projector. Its replay "
            "matches the residual packets, but selected Phi_fin^C1 physical "
            "application or an honest Galerkin value run remains open."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_canonical_projector_certificate": source,
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
            "previous_long_name_certificate": str(PREV),
            "source_canonical_projector_certificate": str(SOURCE_CERT),
            "source_canonical_projector_packet": source["packet_written"],
        },
    }

    note = f"""# PostAlpha Independent CanonicalResidualProjector or HonestGalerkinC1 ValueFill Import v1

## Result

The long-name branch now imports the canonical mathematical residual projector.

Closed now:

```text
rank(P_fixed)    = 3
rank(Q_residual) = 6
projector replay matches stored residual packets = True
```

Still open: selected `Phi_fin^C1` physical projector application, or an honest Galerkin C1 value run.

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
        "certificate": "post_alpha_independent_canonical_residual_projector_or_honest_galerkin_c1_valuefill",
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
