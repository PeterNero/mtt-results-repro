"""Import q79 alpha1 retarded-kernel formula and test N_MTT bridge."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

RAW_NMTT = CERTS / "raw_nmtt_terminal_source_operator_certificate.json"
LOCAL_RETARDED_ATTEMPT = (
    CERTS / "selected_alpha1_tangent_or_retarded_overlap_kernel_attempt_certificate.json"
)
Q79_KERNEL = Q79 / "certificates" / "q79_selected_alpha1_tangent_or_retarded_overlap_kernel_certificate.json"
Q79_VALUE_FILL = (
    Q79
    / "certificates"
    / "q79_selected_physical_alpha1_source_normalization_or_end0_sector_routing_value_fill_certificate.json"
)
Q79_MATTERSLOT = (
    Q79 / "certificates" / "q79_selected_matter_slot_charge_and_overlap_normalization_theorem_certificate.json"
)

OUTPUT_PACKET = DATA / "q79_alpha1_retarded_kernel_formula_nmtt_bridge.candidate.json"
OUTPUT_CERT = CERTS / "q79_alpha1_retarded_kernel_formula_nmtt_bridge_certificate.json"
OUTPUT_NOTE = CORPUS / "Q79_Alpha1_Retarded_Kernel_Formula_NMTT_Bridge_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    nmtt = load(RAW_NMTT)
    local = load(LOCAL_RETARDED_ATTEMPT)
    q79_kernel = load(Q79_KERNEL)
    value_fill = load(Q79_VALUE_FILL)
    matterslot = load(Q79_MATTERSLOT)

    analytic = q79_kernel["analytic_variational_kernel_formula"]
    route_a = value_fill["route_A_source_normalization"]
    route_b = value_fill["route_B_end0_to_sector_routing"]

    bridge_checks = {
        "B0_finite_raw_NMTT_terminal_operator_closed": nmtt["verdict"][
            "finite_terminal_raw_operator_closed"
        ],
        "B1_NMTT_selects_L3_K2_and_c2_400": nmtt["operator_definition"][
            "kernel_basis"
        ]
        == ["L3-K2"]
        and nmtt["operator_definition"]["target_c2"] == [4, 0, 0],
        "B2_q79_analytic_retarded_kernel_formula_proved": q79_kernel["theorem"][
            "proved"
        ]
        and analytic["what_the_formula_closes"][
            "analytic_riesz_projection_derivative_formula"
        ]
        and analytic["what_the_formula_closes"][
            "duhamel_retarded_kernel_derivative_formula"
        ],
        "B3_q79_selected_tangent_values_still_open": q79_kernel[
            "what_remains_open"
        ]["selected_alpha1_tangent_parameter_or_kernel_values"],
        "B4_naive_ext_scale_to_alpha1_rejected": route_a[
            "naive_Ext_scale_to_alpha1_source_normalization_rejected"
        ],
        "B5_End0_sector_route_is_remaining_legal_route": value_fill["decision"][
            "sector_routing_route_remains_primary"
        ]
        and not route_b["closed"],
        "B6_raw_NMTT_does_not_emit_End0_sector_functor_values": False,
        "B7_raw_NMTT_does_not_emit_selected_transfer_normalization": False,
        "B8_raw_NMTT_does_not_emit_primitive_C1_contractions": False,
    }

    theorem_proved = (
        bridge_checks["B0_finite_raw_NMTT_terminal_operator_closed"]
        and bridge_checks["B1_NMTT_selects_L3_K2_and_c2_400"]
        and bridge_checks["B2_q79_analytic_retarded_kernel_formula_proved"]
        and bridge_checks["B3_q79_selected_tangent_values_still_open"]
        and bridge_checks["B4_naive_ext_scale_to_alpha1_rejected"]
        and bridge_checks["B5_End0_sector_route_is_remaining_legal_route"]
    )

    return {
        "packet": "Q79_Alpha1_Retarded_Kernel_Formula_NMTT_Bridge_v1",
        "status": "Q79_ALPHA1_RETARDED_KERNEL_FORMULA_IMPORTED_NMTT_BRIDGE_VALUES_OPEN",
        "inputs": {
            "raw_nmtt": str(RAW_NMTT.relative_to(ROOT)),
            "local_retarded_attempt": str(LOCAL_RETARDED_ATTEMPT.relative_to(ROOT)),
            "q79_kernel": str(Q79_KERNEL),
            "q79_value_fill": str(Q79_VALUE_FILL),
            "q79_matterslot": str(Q79_MATTERSLOT),
        },
        "theorem": {
            "name": "Q79Alpha1RetardedKernelNMTTBridgeTheorem",
            "proved": theorem_proved,
            "statement": (
                "The finite raw N_MTT terminal source selects the L3-K2 "
                "Chern/source row c2=(4,0,0), and the q79 repo proves the "
                "analytic Riesz/Duhamel retarded-kernel formula on the locked "
                "B_N gap layer.  Together these close the terminal-source plus "
                "analytic-response frame, but they do not emit selected alpha1 "
                "tangent values, End0-to-sector functor values, selected "
                "transfer normalization, or primitive C1 contractions."
            ),
        },
        "bridge_checks": bridge_checks,
        "raw_nmtt_contribution": {
            "selected_terminal_lane": nmtt["operator_definition"]["kernel_basis"][0],
            "selected_c2_row": nmtt["operator_definition"]["target_c2"],
            "finite_spectral_gap": nmtt["operator_definition"]["spectral_gap"],
            "closes": [
                "finite terminal source operator",
                "unique terminal Chern/source row",
                "positive finite heat-kernel selection gap",
            ],
            "does_not_close": [
                "smooth continuum N_MTT operator",
                "selected alpha1 tangent/source-normalization values",
                "selected End0-to-sector routing functor",
                "selected transfer normalization",
                "primitive C1 contractions",
            ],
        },
        "q79_kernel_contribution": {
            "status": q79_kernel["status"],
            "formula_status": analytic["status"],
            "response_formula": q79_kernel["selected_tangent_value_fill_contract"][
                "response_formula_to_use_once_values_exist"
            ],
            "selected_gap_lower_bound": analytic["selected_gap_layer"][
                "selected_gap_lower_bound"
            ],
            "selected_green_norm_bound": analytic["selected_gap_layer"][
                "selected_green_norm_bound"
            ],
            "closes": analytic["what_the_formula_closes"],
            "does_not_close": analytic["what_the_formula_does_not_close"],
        },
        "value_gate": {
            "route_A_naive_source_normalization_rejected": route_a[
                "naive_Ext_scale_to_alpha1_source_normalization_rejected"
            ],
            "why_route_A_fails": route_a["reason"],
            "shared_circle_guardrail": route_a["shared_circle_guardrail"],
            "route_B_primary": value_fill["decision"][
                "sector_routing_route_remains_primary"
            ],
            "route_B_next_contract": value_fill[
                "next_end0_sector_functor_value_packet_contract"
            ],
            "matter_slot_same_source_reduction_status": matterslot["status"],
        },
        "frontier_update": {
            "old_local_next": local["verdict"]["next_required_artifact"],
            "q79_imported_next": q79_kernel["next_required_artifact"],
            "current_next": value_fill["next_required_artifact"],
            "why": (
                "The analytic retarded-kernel formula is now proven in q79, "
                "so the remaining blocker moves from formula construction to "
                "selected value emission: either a selected alpha1 source "
                "normalization or the End0-to-sector functor/source/value packet."
            ),
        },
        "guardrails": {
            "does_not_claim_smooth_N_MTT": True,
            "does_not_claim_selected_alpha1_values": True,
            "does_not_claim_selected_dotD_replay": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_C1_response": True,
            "does_not_claim_Yukawa_or_full_SM_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "The constants repo imports the q79 analytic retarded/Riesz "
                "formula and binds it to the new finite raw N_MTT terminal "
                "source row.  The response frame is now clean: source row and "
                "analytic Green response are closed at their respective scopes."
            ),
            "what_remains": (
                "Emit the selected End0-to-sector functor/source/value packet "
                "or an equivalent selected alpha1 source-normalization, then "
                "replay dotD and primitive C1 without lifted flags."
            ),
            "next_required_artifact": "Q79_Selected_End0_to_SectorFunctor_Source_and_Value_Packet_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "Q79Alpha1RetardedKernelFormulaNMTTBridge",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "bridge_checks": packet["bridge_checks"],
        "frontier_update": packet["frontier_update"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# Q79 Alpha1 Retarded Kernel Formula NMTT Bridge v1

## Result

Status: `{cert["status"]}`

The q79 analytic retarded/Riesz formula is now imported and bound to the finite
raw `N_MTT` terminal source operator.

This closes the response frame, not the response values.  The finite
`N_MTT_terminal_q79` operator selects `L3-K2` and `c2=(4,0,0)`, while q79 proves
the analytic formula

```text
dotPsi_i = - G Q dotD_alpha1 Psi_i, with P dotPsi_i=0
```

on the locked `B_N` gap layer.  The missing object is no longer the Riesz or
Duhamel formula; it is selected value emission.

## Bridge Checks

```json
{json.dumps(packet["bridge_checks"], indent=2, sort_keys=True)}
```

## Raw NMTT Contribution

```json
{json.dumps(packet["raw_nmtt_contribution"], indent=2, sort_keys=True)}
```

## Q79 Kernel Contribution

```json
{json.dumps(packet["q79_kernel_contribution"], indent=2, sort_keys=True)}
```

## Value Gate

```json
{json.dumps(packet["value_gate"], indent=2, sort_keys=True)}
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
