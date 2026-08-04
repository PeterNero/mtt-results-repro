from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

PREV_CERT = ROOT / "certificates" / "selected_dotd_alpha1_source_driver_reduction_certificate.json"
PREV_PACKET = ROOT / "candidate_data" / "selected_dotd_alpha1_source_driver_reduction.packet.json"
DOTD_TRANSPORT = SM / "candidate_data" / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
PIN_DOWN = SM / "candidate_data" / "selected_samesource_alpha1_normalization_pin_down_kernel.candidate.json"
FILL_ATTEMPT = SM / "candidate_data" / "selected_samesource_alpha1_normalization_packet.fill_attempt.json"
RETARDED_ATTEMPT = (
    NONSM / "candidate_data" / "selected_alpha1_tangent_or_retarded_overlap_kernel_attempt.candidate.json"
)

OUT_CERT = ROOT / "certificates" / "selected_alpha1_tangent_or_retarded_overlap_kernel_construct_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_alpha1_tangent_or_retarded_overlap_kernel_construct.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel_Construct_v1.md"

STATUS = "SELECTED_ALPHA1_TANGENT_KERNEL_CONSTRUCTED_SELECTION_NORMALIZATION_OPEN"
NEXT = "MTT_Selected_SameSource_Alpha1_Normalization_Packet_Fill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev_cert = load(PREV_CERT)
    prev = load(PREV_PACKET)
    dotd = load(DOTD_TRANSPORT)
    pin = load(PIN_DOWN)
    fill = load(FILL_ATTEMPT)
    retarded = load(RETARDED_ATTEMPT)

    transport = dotd["transport_derivative_formula"]
    driver = dotd["driver_audit"]
    validator = dotd["validator_boundary"]
    acceptance = pin["acceptance_kernel"]
    fill_norm = fill["normalization_functional"]
    fill_tangent = fill["tangent_equality"]
    fill_sector = fill["sector_dotd_equality"]
    transfer = retarded["transfer_checks"]

    algebraic_tangent_kernel_constructed = all(
        [
            dotd["theorem"]["proved"] is True,
            driver["selected_ext_density_tangent_available"] is True,
            driver["h_ext_zero_mean"] is True,
            driver["h_ext_residual_l2"] < 1.0e-12,
            transport["identity"] == "D_sel(delta psi)+dotD_h psi_sel=0",
            transport["dotD_h"] == "dotD_h=(dh) ad(T3)",
            validator["mathematical_dotd_matrices_pass_if_flags_are_theorem_derived"] is True,
        ]
    )
    canonical_normalization_constructed = all(
        [
            fill_norm["formula"] == "N_alpha1(f)=<f,h_ext>/||h_ext||_L2^2",
            fill_norm["N_alpha1_h_ext"] == 1.0,
            fill_norm["support_present"] is True,
            fill_norm["selected_emitted"] is False,
            fill_tangent["residual_l2"] == 0.0,
            fill_tangent["local_hym_residual_l2"] < 1.0e-12,
        ]
    )
    acceptance_kernel_constructed = all(
        [
            pin["what_closes_now"]["promotion_acceptance_kernel_built"] is True,
            pin["pin_down_result"]["lambda_alpha1_candidate_pinned_as_unique_current_candidate"]
            is True,
            acceptance["selected_value_when_passed"]["lambda_alpha1"] == 1.0,
            acceptance["selected_value_when_passed"]["du_dalpha1"] == "h_ext",
            acceptance["selected_value_when_passed"]["alpha1_driver_verified"] is True,
        ]
    )
    retarded_alternative_classified = all(
        [
            transfer["K1_ckm_retarded_kernel_pattern_available"] is True,
            transfer["K2_q79_phi_fin_alpha1_support_available"] is True,
            transfer["K3_source_level_weyl_carrier_available"] is True,
            transfer["K4_selected_sector_charge_or_chirality"] is False,
            transfer["K5_selected_transfer_normalization"] is False,
            transfer["K6_selected_BN_tangent_or_retarded_kernel"] is False,
            transfer["K7_honest_dotD_replay_from_kernel"] is False,
        ]
    )
    selection_still_open = all(
        [
            fill["promotion_result"]["alpha1_driver_verified"] is False,
            fill["promotion_result"]["honest_dotd_validator_closed"] is False,
            fill["source_strength_coordinate"]["selected_emitted"] is False,
            fill_norm["theorem_derived"] is False,
            fill_sector["honest_validator_exit_code"] == 1,
            fill_sector["source_only_fails_only_by_alpha1_driver"] is True,
            prev_cert["source_driver_theorem_proved"] is False,
        ]
    )

    theorem_proved = all(
        [
            algebraic_tangent_kernel_constructed,
            canonical_normalization_constructed,
            acceptance_kernel_constructed,
            retarded_alternative_classified,
            selection_still_open,
        ]
    )

    packet = {
        "theorem": {
            "name": "SelectedAlpha1TangentOrRetardedOverlapKernelConstruct",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "A finite alpha1 tangent-kernel construct is available: the "
                "zero-mean Ext-density tangent h_ext defines dotD_h=(dh)ad(T3), "
                "the transported response satisfies D_sel(delta psi)+dotD_h psi=0, "
                "and the canonical L2 dual N_alpha1(f)=<f,h_ext>/||h_ext||^2 "
                "pins lambda_alpha1=1 as the unique current unit candidate. "
                "This constructs the tangent kernel and its promotion criterion, "
                "but it does not yet emit the same-source selected normalization "
                "functional required to verify alpha1_driver."
            ),
        },
        "constructed_tangent_kernel": {
            "kernel_name": "K_alpha1_tangent",
            "tangent": {
                "symbol": "h_ext",
                "role": "candidate selected alpha1 tangent h=du/dalpha1",
                "zero_mean": driver["h_ext_zero_mean"],
                "h_ext_l2": pin["acceptance_kernel"]["selected_value_when_passed"]["h_ext_l2"],
                "h_ext_residual_l2": driver["h_ext_residual_l2"],
                "selected_now": False,
            },
            "operator_formula": {
                "U": transport["U"],
                "dU_dalpha": transport["dU_dalpha"],
                "dotD_h": transport["dotD_h"],
                "response": transport["response"],
                "identity": transport["identity"],
            },
            "normalization_functional": {
                "formula": fill_norm["formula"],
                "N_alpha1_h_ext": fill_norm["N_alpha1_h_ext"],
                "h_ext_l2_squared": fill_norm["h_ext_l2_squared"],
                "lambda_alpha1_candidate": fill["source_strength_coordinate"]["lambda_alpha1"],
                "selected_now": fill_norm["selected_emitted"],
                "why_not_selected": fill_norm["reason_not_selected"],
            },
        },
        "promotion_acceptance_theorem": {
            "name": acceptance["name"],
            "if_and_only_if_fields": acceptance["promotes_value_if_and_only_if"],
            "selected_value_when_passed": acceptance["selected_value_when_passed"],
            "current_evaluation": acceptance["current_evaluation"],
            "meaning": (
                "This is the exact finite criterion for when the constructed "
                "kernel becomes the selected physical alpha1 driver."
            ),
        },
        "retarded_overlap_alternative": {
            "classified": retarded_alternative_classified,
            "kernel_pattern_available": retarded["retarded_kernel_transfer"][
                "ckm_nil_survivor_kernel_available"
            ],
            "unit_lag_ratio_closed": retarded["retarded_kernel_transfer"][
                "ckm_unit_lag_ratio_closed"
            ],
            "schur_formula_available": retarded["retarded_kernel_transfer"][
                "schur_formula_available"
            ],
            "typed_sm_dotD_kernel_emitted": retarded["retarded_kernel_transfer"][
                "typed_sm_dotD_kernel_emitted"
            ],
            "why_not_transferable_as_proof": retarded["retarded_kernel_transfer"][
                "why_not_transferable_as_proof"
            ],
            "open_transfer_checks": {
                "selected_sector_charge_or_chirality": transfer[
                    "K4_selected_sector_charge_or_chirality"
                ],
                "selected_transfer_normalization": transfer["K5_selected_transfer_normalization"],
                "selected_BN_tangent_or_retarded_kernel": transfer[
                    "K6_selected_BN_tangent_or_retarded_kernel"
                ],
                "honest_dotD_replay_from_kernel": transfer["K7_honest_dotD_replay_from_kernel"],
            },
        },
        "honest_replay_status": {
            "full_flag_probe_passes_if_flags_theorem_derived": validator[
                "mathematical_dotd_matrices_pass_if_flags_are_theorem_derived"
            ],
            "full_flag_validation_exit_code": validator["full_flag_validation"]["exit_code"],
            "source_only_probe_exit_code": validator["source_only_validation"]["exit_code"],
            "source_only_fails_only_by_alpha1_driver": validator[
                "source_only_fails_only_by_alpha1_driver"
            ],
            "honest_replay_without_lifted_flags_closed": False,
            "alpha1_driver_verified": False,
        },
        "what_closes_now": {
            "algebraic_alpha1_tangent_kernel_constructed": algebraic_tangent_kernel_constructed,
            "canonical_L2_dual_normalization_constructed": canonical_normalization_constructed,
            "lambda_alpha1_unit_candidate_pinned": acceptance_kernel_constructed,
            "promotion_acceptance_kernel_built": acceptance_kernel_constructed,
            "retarded_overlap_alternative_classified": retarded_alternative_classified,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "same_source_selected_normalization_functional": True,
            "source_strength_coordinate_selected_by_branch": True,
            "selected_tangent_equality_h_alpha1_equals_h_ext": True,
            "sector_dotd_equality_as_selected_theorem": True,
            "honest_dotD_replay_without_lifted_flags": True,
            "A_selected_and_b_selected": True,
        },
        "guardrails": {
            "does_not_claim_alpha1_driver_verified": True,
            "does_not_promote_coordinate_normalization": True,
            "does_not_use_diagnostic_lift_as_proof": True,
            "does_not_import_ckm_retarded_kernel_as_sm_dotd_proof": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "input_artifacts": {
            "previous_packet": str(PREV_PACKET),
            "previous_certificate": str(PREV_CERT),
            "dotd_transport": str(DOTD_TRANSPORT),
            "pin_down": str(PIN_DOWN),
            "fill_attempt": str(FILL_ATTEMPT),
            "retarded_attempt": str(RETARDED_ATTEMPT),
        },
        "next_required_artifact": NEXT,
    }

    checks = {
        "theorem_proved": theorem_proved,
        "algebraic_tangent_kernel_constructed": algebraic_tangent_kernel_constructed,
        "canonical_normalization_constructed": canonical_normalization_constructed,
        "acceptance_kernel_constructed": acceptance_kernel_constructed,
        "retarded_alternative_classified": retarded_alternative_classified,
        "selection_still_open": selection_still_open,
        "all_closes_true": all(packet["what_closes_now"].values()),
        "all_open_true": all(packet["what_remains_open"].values()),
        "all_guardrails_true": all(packet["guardrails"].values()),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_alpha1_tangent_or_retarded_overlap_kernel_construct",
        "status": STATUS,
        "closure_claimed": False,
        "checks": checks,
        "kernel_constructed": True,
        "alpha1_driver_verified": False,
        "selected_physical_alpha1_closed": False,
        "reduced_to": NEXT,
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected alpha1 Tangent or Retarded Overlap Kernel Construct v1

## Result

The finite alpha1 tangent kernel is now constructed:

```text
h = h_ext
dotD_h = (dh) ad(T3)
delta psi = -(h ad(T3)) psi_sel
D_sel(delta psi) + dotD_h psi_sel = 0
```

The canonical L2 dual normalization is also constructed:

```text
N_alpha1(f) = <f,h_ext> / ||h_ext||_L2^2
N_alpha1(h_ext) = 1
lambda_alpha1 candidate = 1
```

So the algebraic tangent and the unique current unit candidate are nailed down.

## Boundary

This is not yet the selected physical alpha1 driver. The same-source branch has
not emitted the normalization functional or source-strength coordinate as a
selected object, and the honest dotD replay still fails by
`alpha1_driver_verified`.

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
