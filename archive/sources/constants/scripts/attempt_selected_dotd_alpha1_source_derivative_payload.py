"""Attempt Selected_dotD_alpha1_Source_Derivative_Payload_v1."""

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

DRIVER_GATE = DATA / "selected_dotd_alpha1_source_and_driver_theorem_attempt.candidate.json"
FRONTIER = DATA / "selected_phifin_dotd_alpha1_c1_response_emission_attempt.candidate.json"
GAP_LOCK = DATA / "selected_phifin_s2_gap_layer_honest_replay_lock.candidate.json"

ALPHA1_PAYLOAD = SM / "candidate_data" / "selected_phifin_alpha1_payload.candidate.json"
SOURCE_ORIGIN = SM / "candidate_data" / "selected_source_origin_and_alpha1_driver.candidate.json"
OPERATOR_IDENTITY = SM / "candidate_data" / "selected_routec_operatorsourceidentity_subpacket.candidate.json"
PRIMITIVE_SELECTION = SM / "candidate_data" / "selected_routec_primitive_source_selection_audit.candidate.json"
ORIENTATION_SOURCE = SM / "candidate_data" / "selected_orientation_carrying_de_dotd_source.candidate.json"
MATTER_SLOT_PACKET = (
    SM
    / "candidate_data"
    / "selected_routec_samesource_matter_slot_overlap_operator_packet.candidate.json"
)
OPERATOR_PACKET_NOGO = (
    SM / "candidate_data" / "selected_routec_samesource_operatorpacket_fill_or_nogo.candidate.json"
)
DOTD_CERT = SM / "candidate_data" / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"

OUTPUT_PACKET = DATA / "selected_dotd_alpha1_source_derivative_payload_attempt.candidate.json"
OUTPUT_CERT = CERTS / "selected_dotd_alpha1_source_derivative_payload_attempt_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_dotD_alpha1_Source_Derivative_Payload_Attempt_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    driver_gate = load_json(DRIVER_GATE)
    frontier = load_json(FRONTIER)
    gap_lock = load_json(GAP_LOCK)
    alpha1 = load_json(ALPHA1_PAYLOAD)
    source_origin = load_json(SOURCE_ORIGIN)
    operator_identity = load_json(OPERATOR_IDENTITY)
    primitive = load_json(PRIMITIVE_SELECTION)
    orientation = load_json(ORIENTATION_SOURCE)
    matter_slot = load_json(MATTER_SLOT_PACKET)
    operator_nogo = load_json(OPERATOR_PACKET_NOGO)
    dotd = load_json(DOTD_CERT)

    local_prefix = {
        "selected_D_E_gap_layer_locked": gap_lock["locked_contract"][
            "Riesz_Green_layer_closes"
        ],
        "same_basis_dotD_value_matrices_emitted": frontier["closed_prefix"][
            "dotD_alpha1_value_matrices_emitted"
        ]
        and frontier["closed_prefix"]["same_basis_as_locked_D_E"],
        "diagnostic_horizontal_response_passes": frontier["closed_prefix"][
            "finite_horizontal_response_diagnostic_passes"
        ],
        "driver_gate_reduced_to_derivative_payload": driver_gate["verdict"][
            "next_required_artifact"
        ]
        == "Selected_dotD_alpha1_Source_Derivative_Payload_v1",
    }

    external_source_audit = {
        "source_origin_reduction": {
            "status": source_origin["status"],
            "reduced_to_selected_phifin_alpha1_payload": source_origin[
                "next_required_artifact"
            ]
            == "MTT_Selected_PhiFin_Alpha1_Payload_v1",
            "same_branch_dotD_alpha1_derivative_open": source_origin[
                "what_remains_open"
            ]["same_branch_dotD_alpha1_derivative"],
        },
        "alpha1_payload_attempt": {
            "status": alpha1["status"],
            "dotD_support_present": alpha1["payload_summary"][
                "support_candidate_present"
            ]["dotD_alpha1"],
            "dotD_selected_payload_flag": alpha1["payload_summary"][
                "selected_payload_flags"
            ]["dotD_alpha1"],
            "finite_hessian_c1_selected_payload_flag": alpha1["payload_summary"][
                "selected_payload_flags"
            ]["finite_Hessian_C1_source"],
            "operator_level_projective_rhoE_promoted": alpha1[
                "projective_gerbe_support"
            ]["operator_level_projective_rhoE_promoted"],
            "selected_twist_verified_in_attempt": alpha1[
                "projective_gerbe_support"
            ]["selected_twist_verified_in_attempt"],
        },
        "operator_identity_subpacket": {
            "status": operator_identity["status"],
            "closure_claimed": operator_identity["closure_claimed"],
            "source_level_not_operator_level": operator_identity[
                "operator_identity_verdict"
            ]["source_level_not_operator_level"],
            "selected_visible_operator_source_closed": operator_identity[
                "operator_identity_verdict"
            ]["selected_visible_operator_source_closed"],
            "same_branch_derivative_open": operator_identity[
                "symmetry_breaking_dependency"
            ]["primary_route"]["open"]["same_branch_derivative_verified"],
            "actual_selected_dotD_alpha1_operator_open": operator_identity[
                "symmetry_breaking_dependency"
            ]["primary_route"]["open"]["actual_selected_dotD_alpha1_operator"],
        },
        "orientation_carrying_de_dotd_source": {
            "status": orientation["status"],
            "reduced_to_source_origin_and_alpha1_driver": orientation[
                "next_required_artifact"
            ]
            == "MTT_Selected_Source_Origin_and_Alpha1_Driver_v1",
            "same_branch_derivative_verified_open": orientation["what_remains_open"][
                "same_branch_derivative_verified"
            ],
            "selected_dotD_source_flags_open": orientation["what_remains_open"][
                "selected_dotD_source_flags"
            ],
        },
        "primitive_source_selection": {
            "status": primitive["status"],
            "active_shift_forced": primitive["what_closes_now"][
                "active_shift_1_1_forced_by_finite_support"
            ],
            "selected_dotD_source_verified_open": primitive["what_remains_open"][
                "selected_dotD_source_verified"
            ],
            "alpha1_driver_verified_open": primitive["what_remains_open"][
                "alpha1_driver_verified"
            ],
            "absolute_fiber_shift_selected": primitive["source_implication"][
                "absolute_fiber_shift_selected"
            ],
        },
        "same_source_matter_slot_packet": {
            "status": matter_slot["status"],
            "closure_claimed": matter_slot["closure_claimed"],
            "selected_DE_dotD_Riesz_Green_values_open": matter_slot[
                "what_remains_open"
            ]["emit_selected_DE_dotD_Riesz_Green"],
            "selected_normalization_and_b_selected_open": matter_slot[
                "what_remains_open"
            ]["emit_selected_normalization_and_b_selected"],
        },
        "same_source_operatorpacket_fill_or_nogo": {
            "status": operator_nogo["status"],
            "closure_claimed": operator_nogo["closure_claimed"],
            "current_scaffolds_support_only": operator_nogo["what_closes_now"][
                "current_scaffold_nogo_proved"
            ],
            "selected_DE_dotD_Riesz_Green_values_open": operator_nogo[
                "what_remains_open"
            ]["selected_DE_dotD_Riesz_Green_values"],
            "selected_trace_hessian_normalization_open": operator_nogo[
                "what_remains_open"
            ]["selected_trace_hessian_normalization"],
        },
        "dotD_honest_replay": {
            "status": dotd["status"],
            "closure_claimed": dotd["closure_claimed"],
            "same_basis_matrix_emitted": dotd["what_closes_now"][
                "dotD_alpha1_matrix_in_same_basis_emitted"
            ],
            "honest_fails_only_by_source_driver_flags": dotd["validation"][
                "honest_validator_fails_only_by_source_driver_flags"
            ],
            "honest_replay_without_lifted_flags_open": dotd["what_remains_open"][
                "honest_replay_without_lifted_flags"
            ],
        },
    }

    derivative_payload_checks = {
        "D0_locked_basis_and_D_E_gap_available": local_prefix[
            "selected_D_E_gap_layer_locked"
        ],
        "D1_same_basis_dotD_values_available": local_prefix[
            "same_basis_dotD_value_matrices_emitted"
        ],
        "D2_diagnostic_horizontal_response_available": local_prefix[
            "diagnostic_horizontal_response_passes"
        ],
        "D3_source_level_projective_support_available": alpha1[
            "projective_gerbe_support"
        ]["source_level_promoted"],
        "D4_operator_level_selected_projector_retention_for_dotD": False,
        "D5_selected_alpha1_tangent_parameter": False,
        "D6_retarded_overlap_derivative_formula": False,
        "D7_sector_equality_from_selected_derivative_to_dotD_matrices": False,
        "D8_honest_dotD_replay_without_lifted_flags": False,
    }

    proved = all(derivative_payload_checks.values())
    return {
        "packet": "Selected_dotD_alpha1_Source_Derivative_Payload_Attempt_v1",
        "status": (
            "SELECTED_DOTD_ALPHA1_SOURCE_DERIVATIVE_PAYLOAD_PROVED"
            if proved
            else "SELECTED_DOTD_ALPHA1_SOURCE_DERIVATIVE_PAYLOAD_ATTEMPT_BUILT_SOURCE_TANGENT_OPEN"
        ),
        "inputs": {
            "driver_gate": str(DRIVER_GATE.relative_to(ROOT)),
            "frontier": str(FRONTIER.relative_to(ROOT)),
            "gap_lock": str(GAP_LOCK.relative_to(ROOT)),
            "alpha1_payload": str(ALPHA1_PAYLOAD),
            "source_origin": str(SOURCE_ORIGIN),
            "operator_identity": str(OPERATOR_IDENTITY),
            "primitive_selection": str(PRIMITIVE_SELECTION),
            "orientation_source": str(ORIENTATION_SOURCE),
            "matter_slot_packet": str(MATTER_SLOT_PACKET),
            "operatorpacket_fill_or_nogo": str(OPERATOR_PACKET_NOGO),
            "dotD_certificate": str(DOTD_CERT),
        },
        "theorem": {
            "name": "Selected_dotD_alpha1_Source_Derivative_Payload",
            "proved": proved,
            "statement": (
                "There is a selected first-variation source in the locked "
                "q79/F,m=1 F3xF3 B_N basis whose retarded-overlap derivative "
                "equals the emitted sector dotD_alpha1 matrices without using "
                "diagnostic source lifts."
            ),
        },
        "local_prefix": local_prefix,
        "external_source_audit": external_source_audit,
        "derivative_payload_checks": derivative_payload_checks,
        "classification": {
            "not_missing_finite_values": True,
            "not_missing_D_E_gap_or_Green": True,
            "not_missing_source_level_S3_gerbe_support": True,
            "missing_selected_tangent_object": True,
            "missing_variational_identity": True,
            "missing_honest_replay_without_lift": True,
            "why_external_packets_do_not_close": (
                "The SM-parity packets reduce the source-origin and alpha1 "
                "driver problem to a selected PhiFin alpha1 payload, but the "
                "available payload records support shapes with selected flags "
                "false.  The matter-slot and operator-packet files define "
                "contracts or no-go current scaffolds, not selected derivative "
                "matrices derived from an operator-level tangent."
            ),
        },
        "minimal_closure_contract": {
            "name": "Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel_v1",
            "must_emit": [
                "selected tangent vector or deformation parameter alpha1 in the locked B_N basis",
                "operator-level projector retention proof for q79/F,m=1 sectors",
                "retarded-overlap derivative formula d/d alpha1 Phi_fin(alpha1)|selected",
                "sector-by-sector matrix equality to the existing dotD_alpha1 value packet",
                "honest replay certificate setting selected_dotD_source_verified and alpha1_driver_verified by theorem",
            ],
        },
        "guardrails": {
            "does_not_promote_dotD_flags": True,
            "does_not_use_diagnostic_lift_as_proof": True,
            "does_not_treat_support_level_gerbe_as_operator_derivative": True,
            "does_not_claim_alpha1_driver": True,
            "does_not_claim_C1_or_b_selected": True,
            "does_not_claim_Yukawa_or_SM_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "The derivative-payload search is narrowed to one exact "
                "operator-level tangent/retarded-kernel theorem.  Existing "
                "cross-repo packets are classified as support, reduction, "
                "contract, or diagnostic-value data, not proof of the selected "
                "dotD source."
            ),
            "what_remains": (
                "Build the selected alpha1 tangent or retarded-overlap kernel "
                "and replay dotD honestly from that source."
            ),
            "next_required_artifact": "Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedDotDAlpha1SourceDerivativePayloadAttempt",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "derivative_payload_checks": packet["derivative_payload_checks"],
        "classification": packet["classification"],
        "minimal_closure_contract": packet["minimal_closure_contract"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# Selected dotD alpha1 Source Derivative Payload Attempt v1

## Result

Status: `{cert["status"]}`

The derivative payload is not proved yet.  The current repository now has the
locked selected `D_E`/Green layer and same-basis finite `dotD_alpha1` value
matrices.  The sibling SM packets add source-level S3/gerbe support and several
Route-C contracts, but they do not emit the selected alpha1 tangent or
retarded-overlap derivative that would make `dotD_alpha1` theorem-derived.

## Derivative Payload Checks

```json
{json.dumps(packet["derivative_payload_checks"], indent=2, sort_keys=True)}
```

## External Source Audit

```json
{json.dumps(packet["external_source_audit"], indent=2, sort_keys=True)}
```

## Minimal Closure Contract

```json
{json.dumps(packet["minimal_closure_contract"], indent=2, sort_keys=True)}
```

## Guardrails

```json
{json.dumps(packet["guardrails"], indent=2, sort_keys=True)}
```
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_CERT.write_text(
            json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
