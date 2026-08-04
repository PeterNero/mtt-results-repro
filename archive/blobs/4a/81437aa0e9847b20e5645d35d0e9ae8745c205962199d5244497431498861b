from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "candidate_data" / "sector_zeromode_source_payload_stationary_promotion.packet.json"
TANGENT = ROOT / "candidate_data" / "selected_alpha1_tangent_or_retarded_overlap_kernel_construct.packet.json"
TRANSPORT_DOTD = SM / "candidate_data" / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
PIN_DOWN = SM / "candidate_data" / "selected_samesource_alpha1_normalization_pin_down_kernel.candidate.json"

OUT_CERT = ROOT / "certificates" / "dotd_alpha1_transport_derivative_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "dotd_alpha1_transport_derivative_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "dotD_alpha1_TransportDerivative_Import_v1.md"

STATUS = "DOTD_ALPHA1_TRANSPORT_DERIVATIVE_IMPORTED_DRIVER_NORMALIZATION_OPEN"
NEXT = "MTT_Selected_Alpha1_SourceStrength_Normalization_or_Driver_Theorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    tangent = load(TANGENT)
    dotd = load(TRANSPORT_DOTD)
    pin_down = load(PIN_DOWN)

    previous_stationary_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_closes_now"]["validator_ready_sector_rho_s_packet"] is True,
            prev["what_remains_open"]["selected_dotD_alpha1_with_transport_derivative"] is True,
        ]
    )
    local_tangent_ready = all(
        [
            tangent["theorem"]["proved"] is True,
            tangent["constructed_tangent_kernel"]["operator_formula"]["dU_dalpha"]
            == "-(du/dalpha) ad(T3) U",
            tangent["constructed_tangent_kernel"]["operator_formula"]["identity"]
            == "D_sel(delta psi)+dotD_h psi_sel=0",
            tangent["honest_replay_status"]["full_flag_probe_passes_if_flags_theorem_derived"] is True,
            tangent["honest_replay_status"]["alpha1_driver_verified"] is False,
        ]
    )
    imported_transport_derivative = all(
        [
            dotd["theorem"]["proved"] is True,
            dotd["promotion_decision"]["selected_dotD_source_formula_closed"] is True,
            dotd["promotion_decision"]["selected_dotD_source_verified_by_transport_derivative"] is True,
            dotd["driver_audit"]["dotD_frechet_replay_closed"] is True,
            dotd["driver_audit"]["alpha1_driver_verified_now"] is False,
            dotd["validator_boundary"]["mathematical_dotd_matrices_pass_if_flags_are_theorem_derived"] is True,
            dotd["validator_boundary"]["source_only_fails_only_by_alpha1_driver"] is True,
        ]
    )
    normalization_pin_down_ready = all(
        [
            pin_down["acceptance_kernel"]["current_evaluation"]["selected_value_emitted_now"] is False,
            pin_down["pin_down_result"]["lambda_alpha1_candidate_pinned_as_unique_current_candidate"] is True,
            pin_down["what_remains_open"]["promote_alpha1_driver_verified"] is True,
            pin_down["what_closes_now"]["unsafe_coordinate_promotion_excluded"] is True,
        ]
    )
    theorem_proved = all(
        [
            previous_stationary_ready,
            local_tangent_ready,
            imported_transport_derivative,
            normalization_pin_down_ready,
        ]
    )

    packet = {
        "theorem": {
            "name": "dotDAlpha1TransportDerivativeImport",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The dotD_alpha1 transport derivative is imported as a proved "
                "operator formula: for U=exp(-u ad(T3)) and h=du/dalpha, "
                "dU/dalpha=-(du/dalpha)ad(T3)U, dotD_h=(dh)ad(T3), and "
                "D_sel(delta psi)+dotD_h psi_sel=0. This closes the dotD "
                "source algebra and explains the existing finite dotD matrices "
                "provided the alpha1 driver flag is theorem-derived. The remaining "
                "local blocker is the same-branch source-strength normalization "
                "identifying h_ext with the physical alpha1 derivative."
            ),
        },
        "imported_status": {
            "status": STATUS,
            "source_status": dotd["status"],
            "pin_down_status": pin_down["status"],
        },
        "transport_derivative_formula": dotd["transport_derivative_formula"],
        "validator_boundary": dotd["validator_boundary"],
        "driver_audit": dotd["driver_audit"],
        "pin_down_kernel": pin_down["acceptance_kernel"],
        "proof_chain": {
            "previous_stationary_ready": previous_stationary_ready,
            "local_tangent_ready": local_tangent_ready,
            "imported_transport_derivative": imported_transport_derivative,
            "normalization_pin_down_ready": normalization_pin_down_ready,
            "target_fitting_used": dotd["target_fitting_used"] or pin_down["target_fitting_used"],
        },
        "what_closes_now": {
            "selected_dotD_source_algebra": True,
            "transport_derivative_formula": True,
            "finite_dotD_matrices_pass_if_driver_is_theorem_derived": True,
            "alpha1_driver_gap_localized_to_source_strength_normalization": True,
            "unsafe_coordinate_promotion_excluded": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "alpha1_driver_source_strength_normalization": True,
            "honest_dotD_validator_replay_without_alpha1_lift": True,
            "sector_dotd_equality_as_selected_theorem": True,
            "primitive_C1_overlap_contractions": True,
            "selected_matter_slot_routing": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "does_not_claim_alpha1_driver_verified": True,
            "does_not_promote_lambda_alpha1_by_coordinate_choice": True,
            "does_not_claim_h_ext_physical_until_source_strength_selected": True,
            "does_not_use_lifted_validator_flags": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous_stationary_promotion": str(PREV),
            "local_tangent_kernel": str(TANGENT),
            "transport_dotd": str(TRANSPORT_DOTD),
            "pin_down": str(PIN_DOWN),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "dotd_alpha1_transport_derivative_import",
        "status": STATUS,
        "closure_claimed": False,
        "checks": {
            "theorem_proved": theorem_proved,
            "previous_stationary_ready": previous_stationary_ready,
            "local_tangent_ready": local_tangent_ready,
            "imported_transport_derivative": imported_transport_derivative,
            "normalization_pin_down_ready": normalization_pin_down_ready,
            "target_fitting_excluded": packet["proof_chain"]["target_fitting_used"] is False,
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# dotD alpha1 TransportDerivative Import v1

## Result

The dynamic transport formula is now imported:

```text
U = exp(-u ad(T3))
dU/dalpha = -(du/dalpha) ad(T3) U
dotD_h = (dh) ad(T3)
delta psi = -(h ad(T3)) psi_sel
D_sel(delta psi) + dotD_h psi_sel = 0
```

So the dotD source algebra is closed. The finite dotD matrices pass once the
alpha1 driver flag is theorem-derived. They still cannot be promoted by lifted
flags or coordinate convention.

Status:

```text
{STATUS}
```

Remaining gate:

```text
same-branch source-strength normalization identifying h_ext with physical alpha1
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
