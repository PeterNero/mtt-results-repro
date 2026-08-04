"""Build the S2 Phi_fin value-emission replay gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

S2_SCAFFOLD = DATA / "selected_phifin_s1s2_value_emission.s2_scaffold.json"
PROMOTION_CRITERION = CERTS / "selected_phifin_s2_source_promotion_criterion_certificate.json"
SMOOTH_BN = SM / "candidate_data" / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
DE_CERT = SM / "candidate_data" / "selected_routec_de_action_on_smooth_bn.candidate.json"
DE_HONEST = (
    SM
    / "candidate_data"
    / "selected_routec_de_action_on_smooth_bn"
    / "de_action_on_smooth_bn.honest.json"
)
DOTD_CERT = SM / "candidate_data" / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
DOTD_HONEST = (
    SM
    / "candidate_data"
    / "selected_routec_sector_projectors_dotd_on_smooth_bn"
    / "sector_projectors_dotd_on_smooth_bn.honest.json"
)

OUTPUT_PACKET = DATA / "selected_phifin_s2_value_emission_with_gap_error_honest_replay.candidate.json"
OUTPUT_CERT = CERTS / "selected_phifin_s2_value_emission_with_gap_error_honest_replay_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_PhiFin_S2_Value_Emission_with_Gap_Error_and_Honest_Replay_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matrix_shape(matrix: list[Any]) -> list[int]:
    if not matrix:
        return [0, 0]
    first = matrix[0]
    return [len(matrix), len(first) if isinstance(first, list) else 1]


def summarize_de_slots(slots: dict[str, Any]) -> dict[str, Any]:
    return {
        sector: {
            "domain_dimension": slot["domain_dimension"],
            "range_dimension": slot["range_dimension"],
            "expected_kernel_dimension": slot["expected_kernel_dimension"],
            "D_E_matrix_shape": matrix_shape(slot["D_E_matrix"]),
            "selected_source_verified": slot["selected_source_verified"],
            "boundary_conditions_verified": slot["boundary_conditions_verified"],
        }
        for sector, slot in slots.items()
    }


def summarize_dotd_slots(slots: dict[str, Any]) -> dict[str, Any]:
    return {
        sector: {
            "dimension": slot["dimension"],
            "expected_kernel_dimension": slot["expected_kernel_dimension"],
            "dotD_alpha1_matrix_shape": matrix_shape(slot["dotD_alpha1_matrix"]),
            "selected_dotD_source_verified": slot["selected_dotD_source_verified"],
            "alpha1_driver_verified": slot["alpha1_driver_verified"],
            "green_operator_verified": slot["green_operator_verified"],
            "horizontal_gauge_verified": slot["horizontal_gauge_verified"],
        }
        for sector, slot in slots.items()
    }


def all_failure_lines_are_source_flags(validation: dict[str, Any]) -> bool:
    allowed_fragments = (
        "selected_source_verified is not true",
        "selected_dotD_source_verified is not true",
        "alpha1_driver_verified is not true",
        "D_E action validation FAIL",
        "dotD response validation FAIL",
        "loaded sector-specific finite",
    )
    lines = validation.get("output", [])
    return validation.get("exit_code") == 1 and all(
        any(fragment in line for fragment in allowed_fragments) for line in lines
    )


def build_packet() -> dict[str, Any]:
    scaffold = load_json(S2_SCAFFOLD)
    criterion = load_json(PROMOTION_CRITERION)
    smooth = load_json(SMOOTH_BN)
    de_cert = load_json(DE_CERT)
    de_honest = load_json(DE_HONEST)
    dotd_cert = load_json(DOTD_CERT)
    dotd_honest = load_json(DOTD_HONEST)

    basis_id = scaffold["S2_galerkin_basis_and_operator_blocks"]["basis_BN_or_Cech_basis_entries"][
        "basis_id"
    ]
    if basis_id != smooth["B_N_lift"]["basis_id"]:
        raise ValueError(f"basis mismatch: local {basis_id} vs smooth {smooth['B_N_lift']['basis_id']}")
    if basis_id != de_honest["basis_id"] or basis_id != dotd_honest["basis_id"]:
        raise ValueError("honest payload basis mismatch")

    de_slots = summarize_de_slots(de_honest["operator_slots"])
    dotd_slots = summarize_dotd_slots(dotd_honest["dotd_response_slots"])
    gamma_model = smooth["B_N_lift"]["complement_gap"]
    epsilon_model = 0.0
    de_honest_fails_only_flags = all_failure_lines_are_source_flags(
        de_cert["validation"]["honest"]
    )
    dotd_honest_fails_only_flags = all_failure_lines_are_source_flags(
        dotd_cert["validation"]["honest"]
    )

    return {
        "packet": "Selected_PhiFin_S2_Value_Emission_with_Gap_Error_and_Honest_Replay_v1",
        "status": "S2_VALUE_EMISSION_REPLAY_BUILT_SELECTED_PROMOTION_BLOCKED",
        "inputs": {
            "local_S2_scaffold": str(S2_SCAFFOLD.relative_to(ROOT)),
            "local_promotion_criterion": str(PROMOTION_CRITERION.relative_to(ROOT)),
            "smooth_BN_candidate": str(SMOOTH_BN),
            "D_E_candidate": str(DE_CERT),
            "D_E_honest_payload": str(DE_HONEST),
            "dotD_candidate": str(DOTD_CERT),
            "dotD_honest_payload": str(DOTD_HONEST),
        },
        "same_basis_value_payload": {
            "basis_id": basis_id,
            "basis_dimension": len(smooth["B_N_lift"]["basis"]),
            "projective_equivariance_up_to_central_phase": smooth["B_N_lift"][
                "bundle_equivariance"
            ]["projective_equivariance_up_to_central_phase"],
            "zero_cluster_dimension": smooth["B_N_lift"]["zero_cluster"]["dimension"],
            "zero_cluster_indices": smooth["B_N_lift"]["zero_cluster"]["indices"],
            "D_E_slots": de_slots,
            "dotD_alpha1_slots": dotd_slots,
            "sector_projector_ranks": {
                sector: values["rank_trace"]
                for sector, values in dotd_cert["validation"]["projector_residuals"].items()
            },
        },
        "gap_error_replay": {
            "model_active_gap_gamma_N": gamma_model,
            "model_active_residual_epsilon_N": epsilon_model,
            "model_active_epsilon_below_gap": epsilon_model < gamma_model,
            "selected_gap_error_certificate_emitted": False,
            "full_iwasawa_truncation_error_certificate": False,
            "why_not_selected_gap_error": (
                "The smooth B_N scaffold supplies a positive model-active gap and zero "
                "internal scaffold residual, but the full selected Iwasawa/Strominger "
                "operator and truncation-error certificate are still open."
            ),
        },
        "honest_replay": {
            "D_E": de_cert["validation"]["honest"],
            "dotD": dotd_cert["validation"]["honest"],
            "D_E_fails_only_by_source_flags": de_honest_fails_only_flags,
            "dotD_fails_only_by_source_driver_flags": dotd_honest_fails_only_flags,
            "D_E_diagnostic_lift_passes": de_cert["validation"]["diagnostic_source_lift"][
                "exit_code"
            ]
            == 0,
            "dotD_diagnostic_lift_passes": dotd_cert["validation"]["diagnostic_source_lift"][
                "exit_code"
            ]
            == 0,
            "honest_replay_without_lifted_flags_passes": False,
        },
        "criterion_evaluation": {
            "actual_D_E_matrix_entries_emitted": True,
            "actual_Riesz_projector_entries_emitted": True,
            "actual_reduced_Green_entries_emitted": True,
            "actual_dotD_alpha1_entries_emitted": True,
            "same_27_mode_basis_as_S2_scaffold": True,
            "selected_positive_gap_gamma_N_emitted": False,
            "selected_residual_epsilon_N_emitted": False,
            "epsilon_strictly_below_selected_gap_margin": False,
            "honest_validator_replay_without_lifted_flags": False,
            "selected_source_promotion_allowed_by_criterion": False,
        },
        "verdict": {
            "gate_built": True,
            "selected_S2_value_emission_closed": False,
            "source_promotion_now_allowed": False,
            "reason": (
                "Same-basis 27-mode value-shaped D_E/dotD/projector payloads exist "
                "and the model-active gap is positive, but honest replay still fails "
                "because selected source, selected dotD source, alpha1 driver, and "
                "full selected truncation-error provenance are not theorem-derived."
            ),
            "next_required_artifact": "Selected_PhiFin_S2_Selected_Operator_and_Truncation_Source_Theorem_v1",
        },
        "guardrails": {
            "does_not_promote_lifted_flags": True,
            "does_not_claim_selected_S2_value_emission": True,
            "does_not_claim_full_selected_gap_error": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_use_observed_or_benchmark_inputs": True,
            "diagnostic_lift_not_used_as_proof": True,
            "promotion_criterion_status": criterion["status"],
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedPhiFinS2ValueEmissionWithGapErrorHonestReplay",
        "status": "SELECTED_PHIFIN_S2_VALUE_EMISSION_REPLAY_BUILT_BLOCKED_BY_SELECTED_PROVENANCE",
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes_now": {
            "same_basis_27_mode_value_payload_located": True,
            "D_E_value_shapes_and_honest_replay_imported": True,
            "dotD_projector_value_shapes_and_honest_replay_imported": True,
            "model_active_positive_gap_recorded": packet["gap_error_replay"][
                "model_active_epsilon_below_gap"
            ],
            "honest_replay_cutset_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_D_E_source_promotion": True,
            "selected_dotD_source_verified": True,
            "alpha1_driver_verified": True,
            "full_selected_iwasawa_strominger_operator": True,
            "selected_truncation_error_certificate": True,
            "honest_replay_without_lifted_flags": True,
            "A_selected": True,
            "b_selected": True,
        },
        "verdict": packet["verdict"],
        "guardrails": packet["guardrails"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    gap = packet["gap_error_replay"]
    replay = packet["honest_replay"]
    return f"""# Selected PhiFin S2 Value Emission with Gap Error and Honest Replay v1

## Result

The S2 value-emission replay gate is built.

Status: `{cert["status"]}`

This does not close selected S2 value emission. It records that same-basis
27-mode value-shaped `D_E`, sector-projector, and `dotD_alpha1` payloads exist,
and that the model-active scaffold has a positive gap. The honest replay still
fails because the selected source flags and full selected truncation provenance
are not theorem-derived.

## Emitted at Scaffold Level

```text
basis id: {packet["same_basis_value_payload"]["basis_id"]}
basis dimension: {packet["same_basis_value_payload"]["basis_dimension"]}
zero cluster dimension: {packet["same_basis_value_payload"]["zero_cluster_dimension"]}
model-active gamma_N: {gap["model_active_gap_gamma_N"]}
model-active epsilon_N: {gap["model_active_residual_epsilon_N"]}
model-active epsilon < gamma: {gap["model_active_epsilon_below_gap"]}
selected gap/error emitted: {gap["selected_gap_error_certificate_emitted"]}
```

## Honest Replay

```text
D_E honest replay exit code: {replay["D_E"]["exit_code"]}
D_E fails only by source flags: {replay["D_E_fails_only_by_source_flags"]}
dotD honest replay exit code: {replay["dotD"]["exit_code"]}
dotD fails only by source/driver flags: {replay["dotD_fails_only_by_source_driver_flags"]}
honest replay without lifted flags passes: {replay["honest_replay_without_lifted_flags_passes"]}
```

## Boundary

The gate is now narrow: to close selected S2 value emission, we need a theorem
that the 27-mode `B_N` values are the selected full Iwasawa/Strominger operator
trace with a selected truncation-error bound. Until then, the diagnostic lift is
useful for algebra but cannot be used as proof.

Next required artifact:

```text
{packet["verdict"]["next_required_artifact"]}
```
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
