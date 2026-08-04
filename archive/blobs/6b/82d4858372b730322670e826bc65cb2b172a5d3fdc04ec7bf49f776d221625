"""Import conditional dynamic-transfer/Hessian/b-selected value-fill theorem."""

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

PREVIOUS = CERTS / "weylpairdynamicoverlap_sourcepromotion_or_honestgalerkinc1_valuefill_import_certificate.json"
SM_PACKET = SM / "candidate_data" / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json"
SM_CERT = SM / "certificates" / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill_certificate.json"

OUTPUT_PACKET = DATA / "dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill_import.candidate.json"
OUTPUT_CERT = CERTS / "dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill_import_certificate.json"
OUTPUT_NOTE = CORPUS / "DynamicTransferHessian_bSelected_or_HonestGalerkinC1_ValueFill_Import_v1.md"

STATUS = "DYNAMIC_TRANSFER_HESSIAN_BSELECTED_VALUEFILL_IMPORTED_CONDITIONAL_GRAM_EXACT_SOURCE_OPEN"
PREVIOUS_STATUS = "WEYLPAIR_DYNAMIC_OVERLAP_PROMOTION_CUTSET_IMPORTED_OPEN"
SM_STATUS = (
    "MTT_SELECTED_DYNAMICTRANSFERHESSIAN_BSELECTED_OR_HONESTGALERKINC1_"
    "VALUEFILL_BUILT_CONDITIONAL_GRAM_EXACT_SOURCE_OPEN"
)
NEXT = "Selected_U1Y_RouteC_SameSourceDynamicTransferIdentity_or_GalerkinC1Contractions_Emission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    sm_packet = load(SM_PACKET)
    sm_cert = load(SM_CERT)
    coord_packet = sm_packet["conditional_dynamic_transfer_coordinate_packet"]
    hessian = sm_packet["hessian_bselected_fill_attempt"]
    galerkin = sm_packet["honest_Galerkin_C1_value_fill_attempt"]
    gate = sm_packet["promotion_gate"]

    checks = {
        "G0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "G1_upstream_theorem_proved": sm_cert["status"] == SM_STATUS
        and sm_cert["theorem_proved"] is True
        and sm_packet["theorem"]["proved"] is True,
        "G2_coordinate_system_fixed": coord_packet["coordinate_system"]["codomain_real_dimension"] == 72
        and coord_packet["coordinate_system"]["sector_order"] == ["u", "d", "e", "nuD"]
        and coord_packet["coordinate_system"]["coordinates_per_sector"] == 18
        and coord_packet["A_conditional_shape"] == [72, 2],
        "G3_conditional_Gram_exact": coord_packet["Gram_A_transpose_A"]
        == [[12.0, 0.0], [0.0, 12.0]]
        and coord_packet["phase_column_norm_sq"] == 12.0
        and coord_packet["shift_column_norm_sq"] == 12.0
        and coord_packet["cross_inner_product"] == 0.0
        and coord_packet["rank"] == 2
        and coord_packet["condition_number"] == 1.0,
        "G4_conditional_b_and_deltaTheta_exact": coord_packet["A_transpose_b_conditional"]
        == [12.0, 12.0]
        and coord_packet["b_conditional_norm_sq"] == 24.0
        and coord_packet["b_conditional_sector_norm_sq"] == {"u": 6.0, "d": 6.0, "e": 6.0, "nuD": 6.0}
        and coord_packet["deltaTheta_conditional_from_Gram_solve"] == [1.0, 1.0]
        and coord_packet["residual_norm"] == 0.0
        and coord_packet["matches_splitter_target_norm_sq"] is True
        and coord_packet["matches_prior_weylpair_assembly"] is True,
        "G5_Hessian_bselected_attempt_not_promoted": hessian["attempted"] is True
        and hessian["conditional_Hessian_Gram_candidate"]["orthogonal_equal_norm_columns"] is True
        and hessian["conditional_Hessian_Gram_candidate"]["selected_by_MTT"] is False
        and hessian["conditional_b_candidate"]["selected_b_selected"] is False
        and hessian["promoted"] is False
        and all(value is False for value in hessian["selected_value_slots_from_C1_response_audit"].values()),
        "G6_honest_galerkin_attempt_still_open": galerkin["attempted"] is True
        and galerkin["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING"
        and galerkin["selected_source_verified"] is False
        and galerkin["required_coordinate_compatibility"]["codomain_real_dimension"] == 72
        and galerkin["promoted"] is False,
        "G7_promotion_gate_exactly_source_open": gate["conditional_dynamic_value_packet_built"] is True
        and gate["no_linear_algebra_obstruction"] is True
        and all(gate["qualitative_flavor_tests_pass_conditionally"].values())
        and gate["selected_dynamic_transfer_identity_emitted"] is False
        and gate["selected_Hessian_bselected_emitted"] is False
        and gate["honest_Galerkin_C1_contractions_emitted"] is False
        and gate["promote_to_selected_A_selected"] is False
        and gate["promote_to_selected_b_selected"] is False
        and gate["promote_to_selected_deltaTheta_C1"] is False,
        "G8_no_target_or_closure_overclaim": sm_packet["closure_claimed"] is False
        and sm_packet["selected_dynamic_transfer_identity_claimed"] is False
        and sm_packet["selected_Hessian_blocks_claimed"] is False
        and sm_packet["A_selected_claimed"] is False
        and sm_packet["b_selected_claimed"] is False
        and sm_packet["deltaTheta_C1_claimed"] is False
        and sm_packet["Galerkin_C1_contractions_claimed"] is False
        and sm_packet["observed_data_used"] is False
        and sm_packet["target_fitting_used"] is False,
    }

    return {
        "packet": "DynamicTransferHessian_bSelected_or_HonestGalerkinC1_ValueFill_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "sm_dynamic_transfer_packet": str(SM_PACKET),
            "sm_dynamic_transfer_certificate": str(SM_CERT),
        },
        "theorem": {
            "name": "ConditionalDynamicTransferHessianBselectedValueFillImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "In the fixed 72-real C1 coordinate system, the conditional "
                "Weyl-pair dynamic transfer has A^T A = 12 I_2, "
                "A^T b = (12,12), ||b||^2 = 24, condition number 1, and "
                "deltaTheta = (1,1) with zero residual. Thus no linear-algebra "
                "obstruction remains. The only open gate is selected-source "
                "emission of the same dynamic transfer/Hessian/b_selected "
                "identity or honest selected Galerkin C1 contractions."
            ),
        },
        "checks": checks,
        "conditional_dynamic_transfer_coordinate_packet": coord_packet,
        "hessian_bselected_fill_attempt": hessian,
        "honest_Galerkin_C1_value_fill_attempt": galerkin,
        "promotion_gate": gate,
        "what_closes_now": sm_packet["what_closes_now"],
        "what_remains_open": sm_packet["what_remains_open"],
        "frontier_update": {
            "old_next": previous["next_required_artifact"],
            "current_next": NEXT,
            "why": (
                "The conditional finite value problem is solved exactly. "
                "Only same-source dynamic-transfer identity or honest Galerkin "
                "C1 contraction emission can promote it."
            ),
        },
        "guardrails": {
            "conditional_dynamic_value_packet_built": True,
            "no_linear_algebra_obstruction": True,
            "selected_dynamic_transfer_identity_claimed": False,
            "selected_Hessian_blocks_claimed": False,
            "selected_A_selected_claimed": False,
            "selected_b_selected_claimed": False,
            "selected_deltaTheta_C1_claimed": False,
            "honest_Galerkin_C1_contractions_claimed": False,
            "observed_data_used": False,
            "target_fitting_used": False,
            "full_SM_closure_claimed": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "DynamicTransferHessianBselectedOrHonestGalerkinC1ValueFillImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "frontier_update": packet["frontier_update"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    c = packet["conditional_dynamic_transfer_coordinate_packet"]
    return f"""# DynamicTransferHessian bSelected or HonestGalerkinC1 ValueFill Import v1

Status: `{cert["status"]}`.

## Exact Conditional Gram

The conditional Weyl-pair packet is now fixed in a 72-real coordinate system:

```text
A^T A = {c["Gram_A_transpose_A"]}
A^T b = {c["A_transpose_b_conditional"]}
||b||^2 = {c["b_conditional_norm_sq"]}
deltaTheta = {c["deltaTheta_conditional_from_Gram_solve"]}
residual norm = {c["residual_norm"]}
condition number = {c["condition_number"]}
```

This removes the linear-algebra obstruction.

## Boundary

The packet is still conditional. Promotion requires same-source dynamic
transfer/Hessian/`b_selected` identity or honest selected Galerkin C1
contractions in this 72-real coordinate system.

No observed masses, CKM/PMNS values, CP phase, benchmark matrices, or lifted
flags are used as selectors.

Next artifact: `{packet["next_required_artifact"]}`.
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
