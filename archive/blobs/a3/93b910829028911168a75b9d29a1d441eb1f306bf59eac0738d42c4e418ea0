"""Attempt the selected Phi_fin dotD/alpha1/C1 response emission gate."""

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

GAP_LOCK = DATA / "selected_phifin_s2_gap_layer_honest_replay_lock.candidate.json"
C1_PACKET = DATA / "selected_phifin_c1_emission_packet.template.json"
C1_TEMPLATE = CERTS / "selected_routec_c1_operator_source_rebuild.payload.template.json"
DOTD_CERT = SM / "candidate_data" / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
DOTD_HONEST = (
    SM
    / "candidate_data"
    / "selected_routec_sector_projectors_dotd_on_smooth_bn"
    / "sector_projectors_dotd_on_smooth_bn.honest.json"
)

OUTPUT_PACKET = DATA / "selected_phifin_dotd_alpha1_c1_response_emission_attempt.candidate.json"
OUTPUT_CERT = CERTS / "selected_phifin_dotd_alpha1_c1_response_emission_attempt_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_PhiFin_dotD_alpha1_C1_Response_Emission_Attempt_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matrix_shape(matrix: list[Any]) -> list[int]:
    if not matrix:
        return [0, 0]
    first = matrix[0]
    return [len(matrix), len(first) if isinstance(first, list) else 1]


def count_nonzero(matrix: list[list[float]]) -> int:
    return sum(1 for row in matrix for value in row if abs(float(value)) > 1e-12)


def summarize_dotd_slots(dotd_honest: dict[str, Any], dotd_cert: dict[str, Any]) -> dict[str, Any]:
    summaries: dict[str, Any] = {}
    residuals = dotd_cert["validation"]["projector_residuals"]
    projectors = dotd_honest["sector_projectors_on_BN"]
    for sector, slot in dotd_honest["dotd_response_slots"].items():
        summaries[sector] = {
            "dimension": slot["dimension"],
            "expected_kernel_dimension": slot["expected_kernel_dimension"],
            "dotD_alpha1_matrix_shape": matrix_shape(slot["dotD_alpha1_matrix"]),
            "dotD_alpha1_nonzero_entries": count_nonzero(slot["dotD_alpha1_matrix"]),
            "projector_matrix_shape": matrix_shape(projectors[sector]["projector_matrix"]),
            "complement_projector_shape": matrix_shape(slot["complement_projector"]),
            "projector_rank_trace": residuals[sector]["rank_trace"],
            "projector_idempotence_residual": residuals[sector]["idempotence_residual"],
            "projector_hermitian_residual": residuals[sector]["hermitian_residual"],
            "green_operator_verified": slot["green_operator_verified"],
            "horizontal_gauge_verified": slot["horizontal_gauge_verified"],
            "selected_dotD_source_verified": slot["selected_dotD_source_verified"],
            "alpha1_driver_verified": slot["alpha1_driver_verified"],
        }
    return summaries


def build_packet() -> dict[str, Any]:
    gap_lock = load_json(GAP_LOCK)
    c1_packet = load_json(C1_PACKET)
    c1_template = load_json(C1_TEMPLATE)
    dotd_cert = load_json(DOTD_CERT)
    dotd_honest = load_json(DOTD_HONEST)

    dotd_slots = summarize_dotd_slots(dotd_honest, dotd_cert)
    all_same_basis = (
        gap_lock["locked_contract"]["basis_id"] == dotd_honest["basis_id"]
        and c1_packet["selected_branch"] == "q79/F,m=1 S3/GS Route-C"
    )
    all_projectors_clean = all(
        slot["projector_idempotence_residual"] == 0.0
        and slot["projector_hermitian_residual"] == 0.0
        for slot in dotd_slots.values()
    )
    any_dotd_nonzero = any(slot["dotD_alpha1_nonzero_entries"] > 0 for slot in dotd_slots.values())
    selected_dotd_source_closed = all(
        slot["selected_dotD_source_verified"] for slot in dotd_slots.values()
    )
    alpha1_driver_closed = all(slot["alpha1_driver_verified"] for slot in dotd_slots.values())

    can_emit_c1_response = (
        gap_lock["locked_contract"]["Riesz_Green_layer_closes"]
        and selected_dotd_source_closed
        and alpha1_driver_closed
        and c1_template["alpha1"]["source_vector_b_selected"] is not None
        and c1_template["Hess_Xi"]["finite_blocks_emitted"] is True
        and c1_template["primitive_C1"]["selected_contractions_emitted"] is True
        and c1_template["sector_response_matrices"]["emitted"] is True
    )

    return {
        "packet": "Selected_PhiFin_dotD_alpha1_C1_Response_Emission_Attempt_v1",
        "status": (
            "SELECTED_PHIFIN_DOTD_ALPHA1_C1_RESPONSE_EMITTED"
            if can_emit_c1_response
            else "SELECTED_PHIFIN_DOTD_ALPHA1_C1_RESPONSE_FRONTIER_SHARPENED"
        ),
        "inputs": {
            "gap_lock": str(GAP_LOCK.relative_to(ROOT)),
            "c1_packet": str(C1_PACKET.relative_to(ROOT)),
            "c1_template": str(C1_TEMPLATE.relative_to(ROOT)),
            "dotD_certificate": str(DOTD_CERT),
            "dotD_honest_payload": str(DOTD_HONEST),
        },
        "closed_prefix": {
            "selected_D_E_gap_Riesz_Green_locked": gap_lock["locked_contract"][
                "Riesz_Green_layer_closes"
            ],
            "same_basis_as_locked_D_E": all_same_basis,
            "dotD_alpha1_value_matrices_emitted": True,
            "sector_projectors_clean": all_projectors_clean,
            "finite_horizontal_response_diagnostic_passes": dotd_cert["validation"][
                "diagnostic_lift_validator_passes"
            ],
            "dotD_alpha1_has_nonzero_entries": any_dotd_nonzero,
            "target_fitting_excluded": dotd_cert["target_fitting_used"] is False,
        },
        "dotD_value_packet": {
            "basis_id": dotd_honest["basis_id"],
            "candidate_kind": dotd_honest["candidate_kind"],
            "sector_slots": dotd_slots,
            "honest_replay": dotd_cert["validation"]["honest"],
            "honest_replay_fails_only_by_source_driver_flags": dotd_cert["validation"][
                "honest_validator_fails_only_by_source_driver_flags"
            ],
        },
        "c1_response_emission": {
            "A_selected_emitted": False,
            "b_selected_emitted": False,
            "sector_response_matrices_emitted": False,
            "can_emit_c1_response_now": can_emit_c1_response,
            "reason_not_emitted": (
                "Selected dotD source flags, alpha1 driver, b_selected, finite "
                "Hess_Xi blocks, selected zero modes, primitive C1 contractions, "
                "and sector response matrices are still absent as selected payloads."
            ),
        },
        "remaining_gates": {
            "selected_dotD_source_theorem": not selected_dotd_source_closed,
            "same_branch_alpha1_driver_theorem": not alpha1_driver_closed,
            "retarded_overlap_source_vector_b_selected": c1_template["alpha1"][
                "source_vector_b_selected"
            ]
            is None,
            "finite_Hess_Xi_blocks": c1_template["Hess_Xi"]["finite_blocks_emitted"]
            is not True,
            "selected_zero_mode_bases": c1_template["zero_modes"][
                "selected_bases_emitted"
            ]
            is not True,
            "primitive_C1_contractions": c1_template["primitive_C1"][
                "selected_contractions_emitted"
            ]
            is not True,
            "sector_response_matrices": c1_template["sector_response_matrices"][
                "emitted"
            ]
            is not True,
        },
        "guardrails": {
            "does_not_promote_dotD_flags": True,
            "does_not_claim_alpha1_driver": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_Yukawa_or_SM_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
            "uses_locked_D_E_only_as_gap_layer_input": True,
        },
        "verdict": {
            "what_closes_now": (
                "The dotD/C1 frontier is reduced to source/driver/primitive "
                "emission: selected D_E and Green are locked, and same-basis "
                "dotD value matrices with clean projectors are available."
            ),
            "what_remains": (
                "Prove selected dotD source and same-branch alpha1 driver, then "
                "emit b_selected, Hess_Xi, zero modes, primitive C1 contractions, "
                "and sector response matrices."
            ),
            "next_required_artifact": "Selected_dotD_alpha1_Source_and_Driver_Theorem_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedPhiFinDotDAlpha1C1ResponseEmissionAttempt",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "closed_prefix": packet["closed_prefix"],
        "c1_response_emission": packet["c1_response_emission"],
        "remaining_gates": packet["remaining_gates"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# Selected PhiFin dotD alpha1 C1 Response Emission Attempt v1

## Result

Status: `{cert["status"]}`

The selected `D_E` gap/Riesz/Green layer is consumed as locked input.  The
same-basis finite `dotD_alpha1` value packet and sector projectors are present,
but selected `dotD` source flags and the same-branch alpha1 driver are still
open.  Therefore `A_selected` and `b_selected` are not emitted.

## Closed Prefix

```json
{json.dumps(packet["closed_prefix"], indent=2, sort_keys=True)}
```

## Remaining Gates

```json
{json.dumps(packet["remaining_gates"], indent=2, sort_keys=True)}
```

## Boundary

This artifact does not promote `dotD` flags, does not claim the alpha1 driver,
and does not claim `A_selected`, `b_selected`, Yukawa data, or SM closure.

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
