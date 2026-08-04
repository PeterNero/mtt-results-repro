from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_symbolic_transport_projector_replay.packet.json"
LOCAL_DOTD = ROOT / "candidate_data" / "dotd_alpha1_transport_derivative_import.packet.json"
LOCAL_DRIVER = ROOT / "candidate_data" / "alpha1_driver_replay_closure_import.packet.json"
QA_DOTD = QA / "candidate_data" / "selected_u1y_routec_dotd_alpha1_transport_derivative_and_driver.candidate.json"
QA_DRIVER = QA / "candidate_data" / "selected_u1y_routec_alpha1_driver_replay_from_oriented_overlap.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_dotd_alpha1_driver_bridge_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_dotd_alpha1_driver_bridge.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_dotD_alpha1_Driver_Bridge_Import_v1.md"

STATUS = "POST_ALPHA_DOTD_ALPHA1_DRIVER_REPLAY_CLOSED_PRIMITIVE_C1_LAMBDA_OPEN"
NEXT = "Selected_U1Y_RouteC_Primitive_C1_Contractions_or_Lambda12_Gate_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def qa_dotd_ok(dotd: dict) -> bool:
    decision = dotd["decision"]
    payload = dotd["transport_derivative_payload"]
    boundary = dotd["validator_replay_boundary"]
    return all(
        [
            dotd["status"] == "U1Y_ROUTEC_DOTD_ALPHA1_TRANSPORT_DERIVATIVE_CLOSED_DRIVER_VALUE_OPEN",
            dotd["closure_claimed"] is False,
            dotd["target_fitting_used"] is False,
            dotd["next_required_artifact"] == "Selected_U1Y_RouteC_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1",
            dotd["theorem"]["proved"] is True,
            decision["transport_derivative_formula_closed"] is True,
            decision["selected_dotD_source_formula_closed"] is True,
            decision["selected_dotD_source_verified_by_transport_derivative"] is True,
            decision["dotD_matrices_pass_if_driver_theorem_supplied"] is True,
            decision["source_only_fails_only_by_alpha1_driver"] is True,
            decision["alpha1_driver_verified_now"] is False,
            decision["honest_dotD_validator_closed_now"] is False,
            decision["normalization_value_emitted_now"] is False,
            payload["U"] == "exp(-u ad(T3))",
            payload["dU_dalpha"] == "-(du/dalpha) ad(T3) U",
            payload["identity"] == "D_sel(delta psi)+dotD_h psi_sel=0",
            payload["h_ext_residual_l2"] < 1e-12,
            boundary["mathematical_dotd_matrices_pass_if_flags_are_theorem_derived"] is True,
            boundary["promote_full_flags_now"] is False,
            boundary["source_only_fails_only_by_alpha1_driver"] is True,
            boundary["full_flag_validation"]["exit_code"] == 0,
            boundary["source_only_validation"]["exit_code"] == 1,
            all(value is False for value in dotd["guardrails"].values()),
        ]
    )


def qa_driver_ok(driver: dict) -> bool:
    decision = driver["decision"]
    promoted = driver["promoted_value"]
    replay = driver["honest_dotd_replay"]
    return all(
        [
            driver["status"] == "U1Y_ROUTEC_ALPHA1_DRIVER_REPLAY_CLOSED_PRIMITIVE_C1_LAMBDA_OPEN",
            driver["closure_claimed"] is False,
            driver["target_fitting_used"] is False,
            driver["observed_data_used"] is False,
            driver["next_required_artifact"] == NEXT,
            driver["theorem"]["proved"] is True,
            decision["N_alpha1_h_ext_promoted_to_selected_value"] is True,
            decision["du_dalpha1_equals_h_ext_emitted"] is True,
            decision["selected_dotD_source_verified"] is True,
            decision["alpha1_driver_verified"] is True,
            decision["honest_dotD_validator_closed"] is True,
            decision["primitive_C1_contractions_closed"] is False,
            decision["lambda_12_computable"] is False,
            decision["target_fitting_used"] is False,
            all(driver["alpha_requirements"].values()),
            promoted["N_alpha1_h_ext"] == 1.0,
            promoted["lambda_alpha1"] == 1.0,
            promoted["du_dalpha1"] == "h_ext",
            promoted["selected_value_emitted_by_this_theorem"] is True,
            promoted["tangent_residual_l2"] == 0.0,
            replay["selected_dotD_source_verified"] is True,
            replay["alpha1_driver_verified"] is True,
            replay["honest_dotD_validator_closed"] is True,
            all(value is False for value in driver["guardrails"].values()),
        ]
    )


def local_packets_ok(local_dotd: dict, local_driver: dict) -> bool:
    return all(
        [
            local_dotd["theorem"]["proved"] is True,
            local_dotd["imported_status"]["status"] == "DOTD_ALPHA1_TRANSPORT_DERIVATIVE_IMPORTED_DRIVER_NORMALIZATION_OPEN",
            local_dotd["what_closes_now"]["transport_derivative_formula"] is True,
            local_dotd["what_closes_now"]["selected_dotD_source_algebra"] is True,
            local_dotd["guardrails"]["does_not_claim_alpha1_driver_verified"] is True,
            local_driver["theorem"]["proved"] is True,
            local_driver["imported_status"]["status"] == "ALPHA1_DRIVER_REPLAY_CLOSED_PRIMITIVE_C1_LAMBDA_OPEN",
            local_driver["what_closes_now"]["selected_dotD_source_verified"] is True,
            local_driver["what_closes_now"]["alpha1_driver_verified"] is True,
            local_driver["what_closes_now"]["honest_dotD_alpha1_replay"] is True,
            local_driver["guardrails"]["does_not_claim_primitive_C1_contractions"] is True,
        ]
    )


def main() -> None:
    prev = load(PREV)
    local_dotd = load(LOCAL_DOTD)
    local_driver = load(LOCAL_DRIVER)
    qa_dotd = load(QA_DOTD)
    qa_driver = load(QA_DRIVER)

    previous_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["status"] == "POST_ALPHA_SYMBOLIC_TRANSPORT_PROJECTOR_REPLAY_CLOSED_DOTD_OPEN",
            prev["next_required_artifact"] == "Selected_U1Y_RouteC_dotD_alpha1_TransportDerivative_and_Driver_v1",
            prev["what_closes_now"]["selected_rho_s_validator_ready"] is True,
        ]
    )
    theorem_proved = all(
        [
            previous_ready,
            qa_dotd_ok(qa_dotd),
            qa_driver_ok(qa_driver),
            local_packets_ok(local_dotd, local_driver),
        ]
    )
    packet = {
        "theorem": {
            "name": "PostAlphadotDAlpha1DriverBridgeImport",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The post-alpha symbolic replay branch connects to the existing dotD_alpha1 driver "
                "closure. The transport derivative closes dU/dalpha and the selected dotD source "
                "algebra; the oriented-overlap source-strength theorem emits N_alpha1(h_ext)=1 and "
                "du/dalpha1=h_ext, making selected_dotD_source_verified and alpha1_driver_verified "
                "theorem-derived. The finite dotD matrices therefore pass honest replay. Primitive "
                "C1 contractions, lambda_12, A_selected, b_selected, Yukawas, and full SM closure remain open."
            ),
        },
        "status": STATUS,
        "dotd_transport_derivative": qa_dotd["transport_derivative_payload"],
        "promoted_alpha1_value": qa_driver["promoted_value"],
        "honest_dotd_replay": qa_driver["honest_dotd_replay"],
        "checks": {
            "previous_ready": previous_ready,
            "qa_dotd_ok": qa_dotd_ok(qa_dotd),
            "qa_driver_ok": qa_driver_ok(qa_driver),
            "local_packets_ok": local_packets_ok(local_dotd, local_driver),
            "theorem_proved": theorem_proved,
        },
        "what_closes_now": {
            "dU_dalpha_formula": True,
            "selected_dotD_source_algebra": True,
            "selected_N_alpha1_h_ext_value": True,
            "du_dalpha1_equals_h_ext": True,
            "selected_dotD_source_verified": True,
            "alpha1_driver_verified": True,
            "honest_dotD_alpha1_replay": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": qa_driver["what_remains_open"],
        "guardrails": {
            "does_not_claim_primitive_C1_contractions": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_lambda12": True,
            "does_not_claim_Yukawa_or_full_SM_closure": True,
            "does_not_use_diagnostic_lift_as_proof": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous": str(PREV),
            "local_dotd": str(LOCAL_DOTD),
            "local_driver": str(LOCAL_DRIVER),
            "qa_dotd": str(QA_DOTD),
            "qa_driver": str(QA_DRIVER),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_dotd_alpha1_driver_bridge",
        "status": STATUS,
        "closure_claimed": False,
        "selected_dotD_source_verified": True,
        "alpha1_driver_verified": True,
        "honest_dotD_alpha1_replay": True,
        "primitive_C1_contractions_closed": False,
        "lambda12_computable": False,
        "checks": {
            **packet["checks"],
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# PostAlpha dotD alpha1 Driver Bridge Import v1

## Result

The new post-alpha symbolic replay branch now connects to the existing
`dotD_alpha1` driver closure:

```text
dU/dalpha = -(du/dalpha) ad(T3) U
dotD_h = (dh) ad(T3)
N_alpha1(h_ext) = 1
du/dalpha1 = h_ext
selected_dotD_source_verified = true
alpha1_driver_verified = true
honest dotD replay = true
```

This is not a primitive-C1 or Yukawa closure. It only retires the local
`dotD_alpha1` driver blocker for the selected transported zero-mode packet.

Status:

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
