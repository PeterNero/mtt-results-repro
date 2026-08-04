"""Import alpha1 source-strength value gate reduction."""

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

PREVIOUS = CERTS / "projector_source_promotion_dotd_transport_reduction_certificate.json"
VALUE_ATTEMPT = SM / "certificates" / "selected_alpha1_source_strength_value_emission_attempt_certificate.json"
PIN_DOWN = SM / "certificates" / "selected_samesource_alpha1_normalization_pin_down_kernel_certificate.json"
PACKET_FILL = SM / "certificates" / "selected_samesource_alpha1_normalization_packet_fill_attempt_certificate.json"
SOURCE_ID_PARTIAL = SM / "certificates" / "selected_samesource_alpha1_normalization_sourceidentity_partial_fill_certificate.json"
SOURCE_OR_RETARDED = SM / "certificates" / "selected_alpha1_sourceidentity_or_retardedkernel_value_attempt_certificate.json"
VISIBLE_CONTRACT = SM / "certificates" / "visible_routec_sourceidentity_or_typedbn_derivative_contract_certificate.json"
VISIBLE_PARTIAL = SM / "certificates" / "visible_routec_sourceidentity_or_typedbn_derivative_partial_fill_certificate.json"
C1_PRIMITIVE = SM / "certificates" / "selected_routec_c1_primitive_response_on_smooth_bn_certificate.json"

OUTPUT_PACKET = DATA / "alpha1_sourcestrength_value_gate_reduction.candidate.json"
OUTPUT_CERT = CERTS / "alpha1_sourcestrength_value_gate_reduction_certificate.json"
OUTPUT_NOTE = CORPUS / "Alpha1_SourceStrength_Value_Gate_Reduction_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    value = load(VALUE_ATTEMPT)
    pin = load(PIN_DOWN)
    packet_fill = load(PACKET_FILL)
    source_partial = load(SOURCE_ID_PARTIAL)
    source_or_retarded = load(SOURCE_OR_RETARDED)
    visible_contract = load(VISIBLE_CONTRACT)
    visible_partial = load(VISIBLE_PARTIAL)
    c1 = load(C1_PRIMITIVE)

    checks = {
        "A0_previous_frontier_is_alpha1_value_or_transfer": previous["verdict"][
            "next_required_artifacts"
        ]
        == [
            "MTT_Selected_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1",
            "MTT_Selected_SectorCharge_GramTransferNormalization_Packet_v1",
        ],
        "A1_unit_candidate_isolated_but_unselected": value[
            "candidate_unit_source_strength_isolated"
        ]
        and value["conditional_value_candidate"]["lambda_alpha1_candidate"] == 1.0
        and not value["selected_value_emitted"]
        and not value["alpha1_driver_verified"],
        "A2_pin_down_kernel_built_but_values_open": pin[
            "promotion_acceptance_kernel_built"
        ]
        and pin["minimal_packet_schema_built"]
        and pin["lambda_alpha1_candidate"] == 1.0
        and not pin["lambda_alpha1_selected_now"],
        "A3_packet_fill_failed_final_validation": packet_fill["lambda_alpha1"] == 1.0
        and packet_fill["N_alpha1_h_ext"] == 1.0
        and not packet_fill["validator_ok"]
        and not packet_fill["selected_value_emitted"],
        "A4_source_identity_partial_fill_closes_identity_only": source_partial[
            "source_identity_selected"
        ]
        and not source_partial["validator_ok"]
        and "tangent_equality" in source_partial["remaining_fields"],
        "A5_source_or_retarded_attempt_reduces_to_visible_fill": not source_or_retarded[
            "lane_A_selected_source_identity_emitted"
        ]
        and not source_or_retarded["lane_B_typed_bn_retarded_derivative_emitted"]
        and source_or_retarded["next_required_artifact"]
        == "MTT_Selected_Visible_RouteC_SourceIdentity_Certificate_or_TypedBNRetardedDerivative_v1",
        "A6_visible_contract_built_values_open": visible_contract["contract_built"]
        and visible_contract["lambda_alpha1"] == 1.0
        and not visible_contract["template_validates_now"]
        and not visible_contract["selected_value_emitted"],
        "A7_visible_partial_closes_routec_source_identity_not_derivative": visible_partial[
            "lane_A_source_identity_closed"
        ]
        and visible_partial["lane_A_visible_routec_operator_source_closed"]
        and not visible_partial["lane_B_closed"]
        and not visible_partial["validator_ok"]
        and "same_branch_alpha1_derivative" in visible_partial[
            "remaining_lane_A_blockers"
        ],
        "A8_c1_engine_built_but_selected_primitive_open": c1["what_closes"][
            "primitive_C1_contraction_engine_built"
        ]
        and c1["what_closes"]["canonical_tensor_zero_response_result_proved_finitely"]
        and c1["what_remains_open"]["selected_noninvariant_C1_primitive_or_vertex"],
    }

    theorem_proved = all(checks.values())

    return {
        "packet": "Alpha1_SourceStrength_Value_Gate_Reduction_v1",
        "status": "ALPHA1_SOURCESTRENGTH_VALUE_GATE_REDUCED_TO_PHIFIN_DERIVATIVE_FILL_OPEN",
        "inputs": {
            "previous": str(PREVIOUS.relative_to(ROOT)),
            "value_attempt": str(VALUE_ATTEMPT),
            "pin_down_kernel": str(PIN_DOWN),
            "packet_fill": str(PACKET_FILL),
            "source_identity_partial": str(SOURCE_ID_PARTIAL),
            "source_or_retarded": str(SOURCE_OR_RETARDED),
            "visible_contract": str(VISIBLE_CONTRACT),
            "visible_partial": str(VISIBLE_PARTIAL),
            "c1_primitive": str(C1_PRIMITIVE),
        },
        "theorem": {
            "name": "Alpha1SourceStrengthValueGateReductionTheorem",
            "proved": theorem_proved,
            "statement": (
                "The alpha1 source-strength value gate has a unique current "
                "unit candidate lambda_alpha1=1 with N_alpha1(h_ext)=1, but "
                "the candidate is not selected.  The same-source normalization "
                "packet and the visible Route-C source-identity/typed-B_N "
                "contract reduce the blocker to the same-branch Phi_fin "
                "alpha1 derivative or an equivalent typed B_N retarded "
                "derivative.  C1 machinery exists only as an engine and "
                "finite zero-response test until a selected primitive/vertex "
                "and honest alpha1 driver are emitted."
            ),
        },
        "checks": checks,
        "unit_candidate": {
            "lambda_alpha1_candidate": value["conditional_value_candidate"][
                "lambda_alpha1_candidate"
            ],
            "symbolic_value": value["conditional_value_candidate"]["symbolic_value"],
            "h_ext_l2": value["conditional_value_candidate"]["h_ext_l2"],
            "residual_l2": value["conditional_value_candidate"]["h_ext_residual_l2"],
            "selected_value_emitted": value["selected_value_emitted"],
            "alpha1_driver_verified": value["alpha1_driver_verified"],
        },
        "source_identity_state": {
            "same_source_identity_selected": source_partial["source_identity_selected"],
            "same_source_remaining_fields": source_partial["remaining_fields"],
            "visible_routec_operator_source_closed": visible_partial[
                "lane_A_visible_routec_operator_source_closed"
            ],
            "visible_remaining_lane_A_blockers": visible_partial[
                "remaining_lane_A_blockers"
            ],
            "typed_BN_derivative_closed": visible_partial["lane_B_closed"],
        },
        "c1_state": {
            "status": c1["status"],
            "primitive_C1_contraction_engine_built": c1["what_closes"][
                "primitive_C1_contraction_engine_built"
            ],
            "canonical_tensor_zero_response_result_proved_finitely": c1[
                "what_closes"
            ]["canonical_tensor_zero_response_result_proved_finitely"],
            "selected_noninvariant_C1_primitive_or_vertex_open": c1[
                "what_remains_open"
            ]["selected_noninvariant_C1_primitive_or_vertex"],
            "nonzero_C1_response_matrices_open": c1["what_remains_open"][
                "nonzero_C1_response_matrices"
            ],
        },
        "frontier_update": {
            "old_next": previous["frontier_update"]["current_next"],
            "value_attempt_next": value["next_required_artifact"],
            "pin_down_next": pin["next_required_artifact"],
            "packet_fill_next": packet_fill["next_required_artifact"],
            "visible_contract_next": visible_contract["next_required_artifact"],
            "current_next": visible_partial["next_required_artifact"],
            "why": (
                "The source-strength scalar itself is not mysterious: the only "
                "available candidate is the unit source-strength lambda=1.  "
                "What remains missing is the theorem that this coordinate is "
                "the selected same-branch Phi_fin alpha1 derivative, or a typed "
                "B_N retarded derivative replacing it."
            ),
        },
        "guardrails": {
            "does_not_select_lambda_alpha1_candidate": True,
            "does_not_claim_alpha1_driver": True,
            "does_not_claim_honest_dotD_replay": True,
            "does_not_claim_selected_transfer_normalization": True,
            "does_not_claim_nonzero_C1_response": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_Yukawa_or_full_SM_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "The alpha1 value gate is reduced to a very small object: "
                "prove the already-isolated unit source-strength candidate is "
                "the selected same-branch Phi_fin alpha1 derivative, or emit "
                "an equivalent typed B_N retarded derivative."
            ),
            "what_remains": (
                "Fill MTT_Visible_RouteC_PhiFinAlpha1Derivative_v1, then rerun "
                "the same-source alpha1 normalization validator and the honest "
                "dotD/C1 response chain."
            ),
            "next_required_artifact": "MTT_Visible_RouteC_PhiFinAlpha1Derivative_Fill_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "Alpha1SourceStrengthValueGateReduction",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "checks": packet["checks"],
        "frontier_update": packet["frontier_update"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# Alpha1 SourceStrength Value Gate Reduction v1

## Result

Status: `{cert["status"]}`

The alpha1 source-strength scalar is now isolated but not selected.  The only
current candidate is

```text
lambda_alpha1 = 1, du/dalpha1 = h_ext
```

with `N_alpha1(h_ext)=1`.  The final same-source normalization packet still
fails validation, because the selected same-branch `Phi_fin` alpha1 derivative
or an equivalent typed `B_N` retarded derivative has not been emitted.

## Checks

```json
{json.dumps(packet["checks"], indent=2, sort_keys=True)}
```

## Unit Candidate

```json
{json.dumps(packet["unit_candidate"], indent=2, sort_keys=True)}
```

## Source Identity State

```json
{json.dumps(packet["source_identity_state"], indent=2, sort_keys=True)}
```

## C1 State

```json
{json.dumps(packet["c1_state"], indent=2, sort_keys=True)}
```

## Frontier Update

```json
{json.dumps(packet["frontier_update"], indent=2, sort_keys=True)}
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
