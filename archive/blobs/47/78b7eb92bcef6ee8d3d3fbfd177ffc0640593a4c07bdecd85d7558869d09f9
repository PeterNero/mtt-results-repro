"""Build CONST-EW-02 B33 selected source-promotion packet.

B33 imports the strict PSM-C1-02 selected source-promotion packet and the next
unpatched-source-rule / honest-Galerkin-export reduction.  It records the best
current attempt: current unpatched support fails, conditional unpatched support
passes, patched/local-axiom support is rejected, and the remaining route is a
finite labelled source-rule/export checklist.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b33_selected_source_promotion_packet"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PACKET = BASE / "strict_nine_field_source_packet_import.packet.json"
VALIDATORS = BASE / "source_promotion_validator_matrix.packet.json"
REDUCTION = BASE / "unpatched_source_rule_or_honest_export_reduction.packet.json"
BOUNDARY = BASE / "weak_mixing_b33_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B33_SelectedSourcePromotionPacket_v1.md"

STATUS = "MTT_CONST_EW_02_B33_SELECTED_SOURCE_PROMOTION_PACKET_BUILT"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b32_path = DATA / "const_ew_02_weak_mixing_b32_dual_path_home_stretch.candidate.json"
    b32_boundary_path = DATA / "const_ew_02_weak_mixing_b32_dual_path_home_stretch" / "weak_mixing_b32_boundary.packet.json"

    source_candidate_path = SM / "candidate_data" / "selected_psm_c1_02_selectedsourcepromotionpacket.candidate.json"
    current_packet_path = SM / "candidate_data" / "selected_psm_c1_02_selectedsourcepromotionpacket" / "current_unpatched_selected_source_promotion_packet.packet.json"
    current_validator_path = SM / "candidate_data" / "selected_psm_c1_02_selectedsourcepromotionpacket" / "current_unpatched_source_promotion_validator_result.packet.json"
    conditional_packet_path = SM / "candidate_data" / "selected_psm_c1_02_selectedsourcepromotionpacket" / "conditional_unpatched_selected_source_promotion_packet.packet.json"
    conditional_validator_path = SM / "candidate_data" / "selected_psm_c1_02_selectedsourcepromotionpacket" / "conditional_unpatched_source_promotion_validator_result.packet.json"
    patched_packet_path = SM / "candidate_data" / "selected_psm_c1_02_selectedsourcepromotionpacket" / "patched_local_axiom_source_promotion_packet.packet.json"
    patched_validator_path = SM / "candidate_data" / "selected_psm_c1_02_selectedsourcepromotionpacket" / "patched_local_axiom_source_promotion_validator_result.packet.json"
    promotion_matrix_path = SM / "candidate_data" / "selected_psm_c1_02_selectedsourcepromotionpacket" / "psm_c1_02_source_promotion_matrix.packet.json"
    source_next_path = SM / "candidate_data" / "selected_psm_c1_02_selectedsourcepromotionpacket" / "next_labeled_workorder.packet.json"

    reduction_candidate_path = SM / "candidate_data" / "selected_psm_c1_02_unpatchedsourceruleproof_or_honestgalerkinexport.candidate.json"
    route_a_ladder_path = SM / "candidate_data" / "selected_psm_c1_02_unpatchedsourceruleproof_or_honestgalerkinexport" / "route_a_four_clause_ladder.packet.json"
    route_b_manifest_path = SM / "candidate_data" / "selected_psm_c1_02_unpatchedsourceruleproof_or_honestgalerkinexport" / "route_b_honest_galerkin_export_manifest.packet.json"
    implication_path = SM / "candidate_data" / "selected_psm_c1_02_unpatchedsourceruleproof_or_honestgalerkinexport" / "psm_c1_02_unpatched_closure_implication.packet.json"
    reduction_next_path = SM / "candidate_data" / "selected_psm_c1_02_unpatchedsourceruleproof_or_honestgalerkinexport" / "next_labeled_workorder.packet.json"

    b32 = load(b32_path)
    b32_boundary = load(b32_boundary_path)
    source_candidate = load(source_candidate_path)
    current_packet = load(current_packet_path)
    current_validator = load(current_validator_path)
    conditional_packet = load(conditional_packet_path)
    conditional_validator = load(conditional_validator_path)
    patched_packet = load(patched_packet_path)
    patched_validator = load(patched_validator_path)
    promotion_matrix = load(promotion_matrix_path)
    source_next = load(source_next_path)
    reduction_candidate = load(reduction_candidate_path)
    route_a_ladder = load(route_a_ladder_path)
    route_b_manifest = load(route_b_manifest_path)
    implication = load(implication_path)
    reduction_next = load(reduction_next_path)

    source_fields = current_packet["source_fields"]
    closed_fields = {
        key: value
        for key, value in source_fields.items()
        if value["selected_emitted"] and value["theorem_derived"] and value["source_owner_verified"] and value["same_branch"]
    }
    open_fields = {
        key: value
        for key, value in source_fields.items()
        if key not in closed_fields
    }

    packet = {
        "schema": "MTTConstEW02B33StrictNineFieldSourcePacketImport.v1",
        "status": "STRICT_NINE_FIELD_PACKET_IMPORTED_CURRENT_UNPATCHED_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B33-SELECTED-SOURCE-PROMOTION-PACKET",
        "inputs": {
            "source_candidate": rel(source_candidate_path),
            "current_packet": rel(current_packet_path),
            "conditional_packet": rel(conditional_packet_path),
            "patched_packet": rel(patched_packet_path),
            "promotion_matrix": rel(promotion_matrix_path),
        },
        "row_counts": current_packet["row_counts"],
        "closed_current_fields": sorted(closed_fields.keys()),
        "open_current_fields": sorted(open_fields.keys()),
        "closed_current_field_count": len(closed_fields),
        "open_current_field_count": len(open_fields),
        "strict_110_row_payload_validator_passes": current_packet["strict_110_row_payload_validator_passes"],
        "emitted_before_residual_replay": current_packet["emitted_before_residual_replay"],
        "legal_unpatched_exits": promotion_matrix["legal_unpatched_exits"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    validators = {
        "schema": "MTTConstEW02B33SourcePromotionValidatorMatrix.v1",
        "status": "CURRENT_FAILS_CONDITIONAL_PASSES_PATCHED_REJECTED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B33-VALIDATOR-MATRIX",
        "inputs": {
            "current_validator": rel(current_validator_path),
            "conditional_validator": rel(conditional_validator_path),
            "patched_validator": rel(patched_validator_path),
            "source_next": rel(source_next_path),
        },
        "current_unpatched_packet_passes": current_validator["passes"],
        "conditional_unpatched_packet_passes": conditional_validator["passes"],
        "patched_packet_passes_unpatched_validator": patched_validator["passes"],
        "current_errors": current_validator["stderr"],
        "patched_errors": patched_validator["stderr"],
        "conditional_stdout": conditional_validator["stdout"],
        "source_promotion_matrix_status": promotion_matrix["status"],
        "dynamic_values_ready": promotion_matrix["dynamic_values_ready"],
        "exact_values_ready": promotion_matrix["exact_values_ready"],
        "honest_galerkin_table_exported": promotion_matrix["honest_galerkin_table_exported"],
        "unpatched_source_rule_proved": promotion_matrix["unpatched_source_rule_proved"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    reduction = {
        "schema": "MTTConstEW02B33UnpatchedSourceRuleOrHonestExportReduction.v1",
        "status": "UNPATCHED_SOURCE_RULE_OR_HONEST_EXPORT_CHECKLIST_IMPORTED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B33-ROUTEA-ROUTEB-REDUCTION",
        "inputs": {
            "reduction_candidate": rel(reduction_candidate_path),
            "route_A_ladder": rel(route_a_ladder_path),
            "route_B_manifest": rel(route_b_manifest_path),
            "unpatched_closure_implication": rel(implication_path),
            "reduction_next": rel(reduction_next_path),
        },
        "route_A_four_clause_ladder": route_a_ladder,
        "route_B_four_input_manifest": route_b_manifest,
        "closure_implication": implication,
        "what_closes_now": reduction_candidate["what_closes_now"],
        "what_remains_open": reduction_candidate["what_remains_open"],
        "next_required_artifact": reduction_candidate["next_required_artifact"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B33Boundary.v1",
        "status": "B33_SELECTED_SOURCE_PROMOTION_PACKET_BUILT_UNPATCHED_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B33-BOUNDARY",
        "previous_B32": {
            "candidate": b32["candidate"],
            "status": b32["status"],
            "still_open": b32_boundary["still_open"],
        },
        "closed_or_sharpened_now": {
            "strict_selected_source_promotion_packet_constructed": source_candidate["what_closes_now"]["strict_selected_source_promotion_packet_constructed"],
            "current_unpatched_packet_tested_and_rejected": source_candidate["what_closes_now"]["current_unpatched_packet_tested_and_rejected"],
            "conditional_unpatched_target_packet_validates": source_candidate["what_closes_now"]["conditional_unpatched_target_packet_validates"],
            "local_axiom_patch_separated_from_unpatched_proof": source_candidate["what_closes_now"]["local_axiom_patch_separated_from_unpatched_proof"],
            "ROUTE_A_four_clause_ladder_created": reduction_candidate["what_closes_now"]["ROUTE_A_four_clause_ladder_created"],
            "ROUTE_B_four_input_manifest_created": reduction_candidate["what_closes_now"]["ROUTE_B_four_input_manifest_created"],
        },
        "still_open": {
            "derive_differentiated_PhiFinC1_source_rule": True,
            "export_honest_selected_Galerkin_C1_tables": True,
            "promote_current_unpatched_source_packet": True,
            "ROUTE_A_RA_1_physical_C1_variation_principle": True,
            "ROUTE_A_RA_2_boundary_cancellation": True,
            "ROUTE_A_RA_3_Q_residual_application": True,
            "ROUTE_A_RA_4_b_selected_emission": True,
            "ROUTE_B_selected_zero_mode_basis": True,
            "ROUTE_B_primitive_contraction_terms": True,
            "ROUTE_B_hessian_source_vector": True,
            "ROUTE_B_sector_response_matrices": True,
            "K_phys_or_f_ab": True,
            "mu_match": True,
            "RG_threshold_scheme": True,
            "physical_weak_angle_closure": True,
            "strict_full_no_knob_closure": True,
        },
        "anti_cycle_delta_from_B32": {
            "B32": "verified both conditional exits and table shape, with actual source promotion open",
            "B33": "constructs the strict nine-field source packet and reduces unpatched closure to two four-item exits",
            "not_repeated": [
                "not another table-shape audit",
                "not a patched/local-axiom closure claim",
                "not a numerical weak-angle fit",
            ],
        },
        "allowed_claim": "B33 constructs the strict selected source-promotion packet and proves exactly which source fields remain to close it.",
        "forbidden_claim": "unpatched source promotion, patched closure as unpatched proof, physical weak-angle closure, or no-knob closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B33NextWork.v1",
        "status": "NEXT_WORKORDER_ROUTEA_CLAUSE1_OR_ROUTEB_INPUT_BASIS",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B34-ROUTEA-CLAUSE1-OR-ROUTEB-INPUT-BASIS",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B34-ROUTEA-RA1-PHYSICAL-C1-VARIATION",
            "task": "Prove Route A clause RA-1: the unpatched physical C1 variation principle that starts the Phi_fin^C1 source rule.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B34-ROUTEB-SELECTED-ZERO-MODE-BASIS",
            "task": "Fill Route B input 1: selected zero-mode/Galerkin basis as an honest source input independent of replay and local axiom patch.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB33SelectedSourcePromotionPacket",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B33-SELECTED-SOURCE-PROMOTION-PACKET",
        "output_packets": {
            "strict_nine_field_source_packet_import": rel(PACKET),
            "source_promotion_validator_matrix": rel(VALIDATORS),
            "unpatched_source_rule_or_honest_export_reduction": rel(REDUCTION),
            "weak_mixing_b33_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B33SelectedSourcePromotionPacketReductionTheorem",
            "proved": True,
            "statement": (
                "The weak-mixing C1 source-promotion packet is now explicit as a strict nine-field object. Current unpatched data close three support/provenance fields and pass the downstream 110-row payload validator, but fail the dynamic source fields and are not emitted before residual replay. The conditional unpatched packet validates, while the patched local axiom packet is rejected for unpatched proof. Thus closure is reduced to either the Route-A four-clause unpatched source rule or the Route-B four-input honest Galerkin export."
            ),
        },
        "strict_source_promotion_packet_constructed": True,
        "closed_current_field_count": len(closed_fields),
        "open_current_field_count": len(open_fields),
        "current_unpatched_packet_passes": False,
        "conditional_unpatched_packet_passes": True,
        "patched_packet_passes_unpatched_validator": False,
        "route_A_four_clause_ladder_created": True,
        "route_B_four_input_manifest_created": True,
        "source_promotion_closed_now": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B33_SelectedSourcePromotionPacket_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "strict_source_promotion_packet_constructed": True,
        "closed_current_field_count": len(closed_fields),
        "open_current_field_count": len(open_fields),
        "current_unpatched_packet_passes": False,
        "conditional_unpatched_packet_passes": True,
        "patched_packet_passes_unpatched_validator": False,
        "route_A_four_clause_ladder_created": True,
        "route_B_four_input_manifest_created": True,
        "source_promotion_closed_now": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B33 Selected Source Promotion Packet v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B33-SELECTED-SOURCE-PROMOTION-PACKET`

## Built

The source-promotion target is now a strict nine-field packet.

```text
closed current fields = {len(closed_fields)}
open current fields   = {len(open_fields)}
current unpatched     = fails
conditional unpatched = passes
patched local axiom   = rejected for unpatched proof
```

## Open Dynamic Fields

```text
{chr(10).join(sorted(open_fields.keys()))}
```

## Two Exits

Route A has four clauses:

```text
RA-1 physical C1 variation principle
RA-2 selected dynamic boundary cancellation
RA-3 Phi_fin^C1 application of Q_residual producing R_Z/R_X
RA-4 same-source b_selected emission
```

Route B has four inputs:

```text
selected zero-mode basis
primitive contraction terms
hessian source vector
sector response matrices
```

## Next

`CONST-EW-02 / WEAK-MIXING / B34-ROUTEA-CLAUSE1-OR-ROUTEB-INPUT-BASIS`
"""

    for path, payload in [
        (PACKET, packet),
        (VALIDATORS, validators),
        (REDUCTION, reduction),
        (BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
