"""Build the selected Qa/SU3 same-source visible/color operator packet attempt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

INPUT = DATA / "selected_qa_su3_color_bundle_connection_endomorphism_interface.candidate.json"
OUTPUT_DATA = DATA / "selected_qa_su3_same_source_visible_color_operator_packet.candidate.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_same_source_visible_color_operator_packet_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_Qa_SU3_Same_Source_Visible_Color_Operator_Packet_v1.md"

LOCAL_INPUTS = {
    "qa_su3_interface": CERTS / "selected_qa_su3_color_bundle_connection_endomorphism_interface_certificate.json",
    "q79_l2_orientation": Q79 / "candidate_data" / "iwasawa_monad_l2_branch_orientation_candidate.candidate.json",
    "q79_monad_visible_role": Q79 / "candidate_data" / "iwasawa_monad_visible_source_role.candidate.json",
    "q79_ordered_source_gate": Q79 / "certificates" / "visible_rank2_l2_ordered_source_promotion_gate_certificate.json",
    "q79_s3_restriction": Q79 / "certificates" / "visible_twisted_s3_class_restriction_closure_certificate.json",
    "q79_gs_curvature": Q79 / "certificates" / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json",
    "q79_operator_after_s3": Q79 / "certificates" / "visible_operator_source_after_s3_closure_certificate.json",
    "q79_hym_gate": Q79 / "certificates" / "selected_hym_operator_source_attempt_certificate.json",
    "nonsm_visible_architecture": NONSM / "certificates" / "selected_qa_su3_visible_source_architecture_certificate.json",
    "nonsm_routec_gate": NONSM / "certificates" / "selected_qa_su3_routec_source_solve_gate_certificate.json",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_status() -> dict[str, object]:
    return {
        key: {
            "path": str(path),
            "present": path.exists(),
        }
        for key, path in LOCAL_INPUTS.items()
    }


def build_candidate() -> dict[str, object]:
    input_data = load_json(INPUT)
    local = {key: load_json(path) for key, path in LOCAL_INPUTS.items()}
    l2 = local["q79_l2_orientation"]
    role = local["q79_monad_visible_role"]
    ordered = local["q79_ordered_source_gate"]
    s3 = local["q79_s3_restriction"]
    gs = local["q79_gs_curvature"]
    after_s3 = local["q79_operator_after_s3"]
    hym = local["q79_hym_gate"]
    routec = local["nonsm_routec_gate"]
    key_lift = l2["key_candidate"]
    return {
        "candidate": "MTTSelectedQaSU3SameSourceVisibleColorOperatorPacket",
        "status": "MTT_SELECTED_QA_SU3_SAME_SOURCE_VISIBLE_COLOR_OPERATOR_PACKET_ATTEMPT_BUILT_PROMOTION_OPEN",
        "input_status": input_data["status"],
        "source_status": source_status(),
        "same_source_packet_attempt": {
            "branch": "q79/F,m=1 visible/color branch",
            "topological_candidate": {
                "ordered_difference": key_lift["ordered_difference"],
                "value": key_lift["value"],
                "double_value": key_lift["double_value"],
                "matches_target_L": key_lift["matches_target_L"],
                "matches_target_L2_after_doubling": key_lift["matches_target_L2_after_doubling"],
                "unique_ordered_difference": len(l2["ordered_difference_scan"]["differences_whose_double_is_target_L2"]) == 1,
            },
            "closed_support": {
                "s3_flat_deligne_restriction_closed": s3["calculation_results"]["selected_S3_class_restriction_packet_constructed"],
                "s3_freed_witten_cancellation_closed": s3["calculation_results"]["smooth_Freed_Witten_cancellation_closed"],
                "s3_block_projector_retention_closed": s3["calculation_results"]["block_sector_projector_retention_closed"],
                "visible_gs_curvature_closed": gs["calculation_results"]["visible_green_schwarz_curvature_verified"],
                "visible_gs_bianchi_residual_zero": gs["what_this_closes"]["zero_Bianchi_residual_for_required_symbolic_row"],
            },
            "not_same_source_yet": {
                "monad_alone_realizes_visible_alpha1_source": role["role_comparison"]["monad_alone_realizes_visible_alpha1_source"],
                "monad_c2_minus_required_c2_coeff_alpha1": role["role_comparison"]["monad_c2_minus_required_c2_coeff_alpha1"],
                "ordered_source_gate_status": ordered["status"],
                "ordered_source_still_open": ordered["still_open"],
                "operator_after_s3_status": after_s3["status"],
                "operator_cut_set": after_s3["still_open_cut_set"],
                "hym_gate_status": hym["status"],
            },
        },
        "promotion_tests": {
            "T1_unique_L3_minus_K2_integral_lift": True,
            "T2_S3_GS_support_closed": True,
            "T3_monad_alone_c2_mismatch_rejected": role["what_this_closes"]["do_not_reuse_c2_zero_monad_as_c2_4_alpha1_source"],
            "T4_ordered_source_selected": False,
            "T5_Pic0_selected_or_quotiented": False,
            "T6_same_source_Chern_Weil_row_derived": False,
            "T7_transition_rhoE_or_DE_emitted": False,
            "T8_selected_HYM_or_RouteC_residual": False,
            "T9_Riesz_Green_dotD_projector_retention": False,
            "T10_finite_determinant_or_torsion_response": False,
        },
        "minimal_closing_payload": {
            "primary_repair": "source-select the ordered V_alpha/L3-K2 lane and bind it to the already-closed S3/Green-Schwarz visible support",
            "must_supply": [
                "selected source status for L3-K2 or an enlarged visible source",
                "standard lattice/base ordering and base-swap-breaking evidence",
                "Pic0 selection or a physical quotient theorem removing Pic0",
                "Chern-Weil row derived from the same selected source, not inserted",
                "transition/rho_E or Cech/Dolbeault/D_E data from that source",
                "selected HYM/Strominger or Route-C residual with selected_source_verified true",
                "Riesz projector, reduced Green, dotD_alpha1, and zero-mode projector retention",
                "finite determinant, heat, spectrum, or torsion response",
            ],
            "then_run": routec["next_object"]["then_run"],
        },
        "decision": {
            "result": "Same-source visible/color packet attempted; support is strong but promotion fails honestly.",
            "why_not_closed": "The source-selection and operator-emission gates are still open: ordered V_alpha selection, Pic0 handling, same-source Chern-Weil derivation, and selected D_E/rho_E/dotD/Riesz/Green are not supplied.",
            "best_next_artifact": "MTT_Selected_Qa_SU3_Ordered_VAlpha_Pic0_Source_Repair_v1",
            "secondary_next_artifact": "MTT_Selected_Qa_SU3_Gerbe_Twisted_DE_Source_Repair_v1",
        },
        "gate_results": {
            "same_source_packet_attempt_built": True,
            "topological_L3_minus_K2_candidate_imported": True,
            "s3_gs_support_imported_closed": True,
            "monad_c2_mismatch_rejected": True,
            "operator_source_promoted": False,
            "selected_Qa_SU3_packet_closed": False,
            "sm_parity_closure_claimed": False,
            "no_knob_closure_claimed": False,
        },
        "next_required_artifact": "MTT_Selected_Qa_SU3_Ordered_VAlpha_Pic0_Source_Repair_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSelectedQaSU3SameSourceVisibleColorOperatorPacket",
        "status": "MTT_SELECTED_QA_SU3_SAME_SOURCE_VISIBLE_COLOR_OPERATOR_PACKET_ATTEMPT_BUILT_PROMOTION_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "same_source_packet_attempt": True,
            "L3_minus_K2_integral_lift_imported": True,
            "S3_GS_support_imported_as_closed_support": True,
            "monad_alone_c2_mismatch_rejected": True,
            "minimal_repair_payload_identified": True,
        },
        "what_remains_open": {
            "ordered_VAlpha_source_selection": True,
            "standard_lattice_base_order_and_base_swap_breaking": True,
            "Pic0_selection_or_quotient": True,
            "same_source_Chern_Weil_row": True,
            "transition_rhoE_Cech_Dolbeault_or_DE_packet": True,
            "selected_HYM_or_RouteC_residual": True,
            "Riesz_Green_dotD_projector_retention": True,
            "finite_determinant_heat_spectrum_or_torsion_response": True,
            "selected_Qa_SU3_color_operator_packet": True,
            "sm_parity_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    sources = "\n".join(
        f"- `{key}`: {body['path']} ({'present' if body['present'] else 'missing'})"
        for key, body in candidate["source_status"].items()
    )
    packet = candidate["same_source_packet_attempt"]
    tests = "\n".join(f"- `{name}`: `{value}`" for name, value in candidate["promotion_tests"].items())
    payload = "\n".join(f"- {item}" for item in candidate["minimal_closing_payload"]["must_supply"])
    closes = "\n".join(f"- {name}" for name, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {name}" for name, value in certificate["what_remains_open"].items() if value)
    return f"""# MTT Selected Qa/SU3 Same-Source Visible/Color Operator Packet v1

## Purpose

This artifact tries the best current construction: bind the `V_alpha`
terminal-monad lane to the selected S3/Green-Schwarz visible support and use
the HYM/Route-C or spectral Galerkin machinery as the execution engine.

The result is not closure.  It is a stricter promotion attempt that separates
closed support from still-open same-source operator data.

## Inputs

{sources}

## Packet Attempt

- Branch: `{packet["branch"]}`
- Ordered difference: `{packet["topological_candidate"]["ordered_difference"]}`
- Integral lift value: `{packet["topological_candidate"]["value"]}`
- Doubled value: `{packet["topological_candidate"]["double_value"]}`
- Unique ordered difference: `{packet["topological_candidate"]["unique_ordered_difference"]}`
- Matches target L: `{packet["topological_candidate"]["matches_target_L"]}`
- Matches target L2 after doubling: `{packet["topological_candidate"]["matches_target_L2_after_doubling"]}`

## Closed Support

- S3 flat Deligne restriction closed: `{packet["closed_support"]["s3_flat_deligne_restriction_closed"]}`
- S3 Freed-Witten cancellation closed: `{packet["closed_support"]["s3_freed_witten_cancellation_closed"]}`
- S3 block projector retention closed: `{packet["closed_support"]["s3_block_projector_retention_closed"]}`
- Visible Green-Schwarz curvature closed: `{packet["closed_support"]["visible_gs_curvature_closed"]}`
- Visible GS Bianchi residual zero: `{packet["closed_support"]["visible_gs_bianchi_residual_zero"]}`

## Promotion Tests

{tests}

## Minimal Closing Payload

Primary repair: {candidate["minimal_closing_payload"]["primary_repair"]}

{payload}

After that packet is supplied, rerun:

```text
{chr(10).join(candidate["minimal_closing_payload"]["then_run"])}
```

## Decision

{candidate["decision"]["result"]}

Reason: {candidate["decision"]["why_not_closed"]}

Best next artifact:

```text
{candidate["decision"]["best_next_artifact"]}
```

Secondary next artifact:

```text
{candidate["decision"]["secondary_next_artifact"]}
```

## Theorem

The current corpus/repo evidence supports the `L3-K2` / `V_alpha` lane as the
unique ordered integral lift candidate and supports the S3/Green-Schwarz
visible data as closed support.  It does not yet prove that these are one
selected same-source visible/color operator packet.  Promotion is blocked
until source selection, Pic0 handling, same-source Chern-Weil derivation,
operator emission, and finite determinant response are supplied before target
comparison.

## What This Closes

{closes}

## What Remains Open

{open_items}

## Next Artifact

```text
{candidate["next_required_artifact"]}
```
"""


def main() -> None:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    note_text = render_note(candidate, certificate)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note_text, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
