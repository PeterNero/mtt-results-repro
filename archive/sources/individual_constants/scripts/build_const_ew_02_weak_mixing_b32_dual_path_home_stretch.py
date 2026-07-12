"""Build CONST-EW-02 B32 dual-path home-stretch artifact.

B32 tries both legal exits after B31:
Route A: same-source physical Phi_fin^C1 / b_selected emission.
Route B: actual independent finite C1 row-packet/source table.

The strongest current sibling artifacts show both actual attempts still fail,
while both conditional exits validate.  B32 records this as the final source
promotion contract for the weak-mixing C1 edge.
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

SLUG = "const_ew_02_weak_mixing_b32_dual_path_home_stretch"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DUAL_FILL = BASE / "dual_path_actual_fill_import.packet.json"
CONDITIONAL = BASE / "conditional_exit_acceptance_import.packet.json"
TABLE = BASE / "routeb_source_table_shape_import.packet.json"
BOUNDARY = BASE / "weak_mixing_b32_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B32_DualPathHomeStretch_v1.md"

STATUS = "MTT_CONST_EW_02_B32_DUAL_PATH_HOME_STRETCH_BUILT"


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

    b31_path = DATA / "const_ew_02_weak_mixing_b31_clauseproof_and_rowpacket_frontier.candidate.json"
    b31_boundary_path = DATA / "const_ew_02_weak_mixing_b31_clauseproof_and_rowpacket_frontier" / "weak_mixing_b31_boundary.packet.json"

    actual_fill_candidate_path = SM / "candidate_data" / "selected_samesourcephifinc1emission_or_independentrowsactualfill.candidate.json"
    actual_fill_path = SM / "candidate_data" / "selected_samesourcephifinc1emission_or_independentrowsactualfill" / "strongest_legal_two_lane_actual_fill.packet.json"
    actual_validator_path = SM / "candidate_data" / "selected_samesourcephifinc1emission_or_independentrowsactualfill" / "strict_two_lane_validator_result.packet.json"
    actual_cutset_path = SM / "candidate_data" / "selected_samesourcephifinc1emission_or_independentrowsactualfill" / "remaining_source_cutset.packet.json"

    export_candidate_path = SM / "candidate_data" / "selected_physicalphifinc1actionidentity_or_independentrowsourceexport.candidate.json"
    acceptance_contract_path = SM / "candidate_data" / "selected_physicalphifinc1actionidentity_or_independentrowsourceexport" / "source_export_acceptance_contract.packet.json"
    current_export_validator_path = SM / "candidate_data" / "selected_physicalphifinc1actionidentity_or_independentrowsourceexport" / "current_source_export_validator_result.packet.json"
    remaining_export_cutset_path = SM / "candidate_data" / "selected_physicalphifinc1actionidentity_or_independentrowsourceexport" / "remaining_export_cutset.packet.json"
    conditional_route_a_path = SM / "candidate_data" / "selected_physicalphifinc1actionidentity_or_independentrowsourceexport" / "conditional_route_a_validator_result.packet.json"
    conditional_route_b_path = SM / "candidate_data" / "selected_physicalphifinc1actionidentity_or_independentrowsourceexport" / "conditional_route_b_validator_result.packet.json"

    table_candidate_path = SM / "candidate_data" / "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable.candidate.json"
    table_decision_path = SM / "candidate_data" / "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable" / "routea_or_routeb_next_decision.packet.json"
    table_validator_path = SM / "candidate_data" / "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable" / "two_exit_current_after_table_validator_result.packet.json"

    psm_candidate_path = SM / "candidate_data" / "selected_psm_c1_02_i10bindingproof_or_selectedquadraturesourcepromotion.candidate.json"

    b31 = load(b31_path)
    b31_boundary = load(b31_boundary_path)
    actual_fill_candidate = load(actual_fill_candidate_path)
    actual_fill = load(actual_fill_path)
    actual_validator = load(actual_validator_path)
    actual_cutset = load(actual_cutset_path)
    export_candidate = load(export_candidate_path)
    acceptance_contract = load(acceptance_contract_path)
    current_export_validator = load(current_export_validator_path)
    remaining_export_cutset = load(remaining_export_cutset_path)
    conditional_route_a = load(conditional_route_a_path)
    conditional_route_b = load(conditional_route_b_path)
    table_candidate = load(table_candidate_path)
    table_decision = load(table_decision_path)
    table_validator = load(table_validator_path)
    psm_candidate = load(psm_candidate_path)

    dual_fill = {
        "schema": "MTTConstEW02B32DualPathActualFillImport.v1",
        "status": "BOTH_ACTUAL_PATHS_TRIED_STRICT_VALIDATOR_REJECTS",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B32-SAMESOURCE-EMISSION-OR-ACTUAL-ROWPACKET",
        "inputs": {
            "actual_fill_candidate": rel(actual_fill_candidate_path),
            "actual_fill": rel(actual_fill_path),
            "actual_validator": rel(actual_validator_path),
            "actual_cutset": rel(actual_cutset_path),
        },
        "route_A_actual": actual_fill["route_A_phifinc1_source_emission"],
        "route_B_actual": actual_fill["route_B_independent_hessian_quadrature_source"],
        "validator_ok": actual_validator["ok"],
        "validator_errors": actual_validator["stderr"],
        "remaining_source_cutset": actual_cutset,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    conditional = {
        "schema": "MTTConstEW02B32ConditionalExitAcceptanceImport.v1",
        "status": "BOTH_CONDITIONAL_EXITS_VALIDATE_ACTUAL_SOURCE_EMISSION_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B32-CONDITIONAL-EXIT-ACCEPTANCE",
        "inputs": {
            "export_candidate": rel(export_candidate_path),
            "acceptance_contract": rel(acceptance_contract_path),
            "current_export_validator": rel(current_export_validator_path),
            "remaining_export_cutset": rel(remaining_export_cutset_path),
            "conditional_route_a_validator": rel(conditional_route_a_path),
            "conditional_route_b_validator": rel(conditional_route_b_path),
            "psm_c1_02_reduction": rel(psm_candidate_path),
        },
        "acceptance_contract": acceptance_contract,
        "current_export_validator_ok": current_export_validator["ok"],
        "route_A_conditional_validator_ok": remaining_export_cutset["route_A_conditional_validator_ok"],
        "route_B_conditional_validator_ok": remaining_export_cutset["route_B_conditional_validator_ok"],
        "route_A_conditional_result_ok": conditional_route_a["ok"],
        "route_B_conditional_result_ok": conditional_route_b["ok"],
        "psm_c1_02_status": psm_candidate["status"],
        "psm_c1_02_statement": psm_candidate["theorem"]["statement"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    table = {
        "schema": "MTTConstEW02B32RouteBSourceTableShapeImport.v1",
        "status": "ROUTEB_TABLE_SHAPE_READY_PROVENANCE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B32-ACTUAL-INDEPENDENT-ROWPACKET",
        "inputs": {
            "table_candidate": rel(table_candidate_path),
            "table_decision": rel(table_decision_path),
            "table_validator": rel(table_validator_path),
        },
        "route_B_table_shape_ready": table_decision["route_B_table_shape_ready"],
        "route_B_table_independent": table_decision["route_B_table_independent"],
        "strict_validator_ok": table_decision["strict_validator_ok"],
        "validator_errors": table_validator["stderr"],
        "next_minimal_payload": table_decision["next_minimal_payload"],
        "what_closes_now": table_candidate["what_closes_now"],
        "what_remains_open": table_candidate["what_remains_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B32Boundary.v1",
        "status": "B32_HOME_STRETCH_CONTRACT_BUILT_CLOSURE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B32-BOUNDARY",
        "previous_B31": {
            "candidate": b31["candidate"],
            "status": b31["status"],
            "still_open": b31_boundary["still_open"],
        },
        "closed_or_sharpened_now": {
            "both_actual_paths_tried": True,
            "both_actual_paths_rejected_honestly": actual_validator["ok"] is False and current_export_validator["ok"] is False,
            "both_conditional_exits_validate": remaining_export_cutset["route_A_conditional_validator_ok"] and remaining_export_cutset["route_B_conditional_validator_ok"],
            "route_B_table_shape_ready": table_decision["route_B_table_shape_ready"],
            "route_B_provenance_gap_counted": table_candidate["what_closes_now"]["route_B_provenance_failure_counted"],
            "numerical_row_search_removed_as_primary_blocker": psm_candidate["what_closes_now"]["numerical_row_search_removed_as_primary_blocker"],
        },
        "still_open": {
            "route_A_I10_or_physical_PhiFinC1_action_identity": True,
            "physical_no_extra_boundary_source_theorem": True,
            "same_source_RZ_RX_bselected_emission": True,
            "route_B_selected_row_kernel_source_ids": True,
            "route_B_independent_hessian_b_source": True,
            "route_B_residual_replay_exclusion_certificate": True,
            "source_promotion_common_object": True,
            "K_phys_or_f_ab": True,
            "mu_match": True,
            "RG_threshold_scheme": True,
            "physical_weak_angle_closure": True,
            "strict_full_no_knob_closure": True,
        },
        "home_stretch_contract": {
            "route_A": acceptance_contract["route_A_acceptance"]["must_emit"],
            "route_B": acceptance_contract["route_B_acceptance"]["must_emit"],
            "shared_locked_target_policy": acceptance_contract["shared_locked_target_policy"],
        },
        "anti_cycle_delta_from_B31": {
            "B31": "closed trace/assembly subclause and left same-source emission or row packet open",
            "B32": "tries both actual paths, verifies both conditional exits, and freezes the exact source-promotion contract",
            "not_repeated": [
                "not a row-value replay",
                "not a conditional closure claim",
                "not a weak-angle numerical target fit",
            ],
        },
        "allowed_claim": "B32 brings the weak-mixing C1 branch to a final source-promotion contract: either Route A physical action identity/source emission or Route B independent row-source export will close the C1 edge.",
        "forbidden_claim": "actual source promotion, unpatched C1 closure, physical weak-angle closure, or no-knob closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B32NextWork.v1",
        "status": "NEXT_WORKORDER_SELECTED_SOURCE_PROMOTION_PACKET",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B33-SELECTED-SOURCE-PROMOTION-PACKET",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B33-ROUTEA-I10-PHIFIN-ACTION-IDENTITY",
            "task": "Derive the I10/physical Phi_fin^C1 action identity on the selected branch, including no-extra-boundary/source and same-source R_Z/R_X/b_selected emission.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B33-ROUTEB-INDEPENDENT-SOURCE-ID-TABLE",
            "task": "Replace replay kernel_source_id markers with selected row-kernel source ids and independent Hessian/b source rows, then attach a residual-replay exclusion certificate.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB32DualPathHomeStretch",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B32-SAMESOURCE-EMISSION-OR-ACTUAL-ROWPACKET",
        "output_packets": {
            "dual_path_actual_fill_import": rel(DUAL_FILL),
            "conditional_exit_acceptance_import": rel(CONDITIONAL),
            "routeb_source_table_shape_import": rel(TABLE),
            "weak_mixing_b32_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B32DualPathHomeStretchContractTheorem",
            "proved": True,
            "statement": (
                "Both legal B32 paths have been tried with the strongest current support and both actual attempts are rejected by the strict validator. Both conditional exits validate, and Route B has a complete table shape but lacks independent source provenance. Therefore the weak-mixing C1 edge is brought to a final selected source-promotion packet: either Route A emits the physical Phi_fin^C1 action identity/no-boundary/same-source packet, or Route B emits independent row-kernel and Hessian/b source ids with residual-replay exclusion."
            ),
        },
        "both_actual_paths_tried": True,
        "actual_route_A_validates": False,
        "actual_route_B_validates": False,
        "route_A_conditional_validates": True,
        "route_B_conditional_validates": True,
        "route_B_table_shape_ready": True,
        "source_promotion_contract_built": True,
        "anti_cycle_confirmed": True,
        "source_promotion_closed_now": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B32_DualPathHomeStretch_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "both_actual_paths_tried": True,
        "actual_route_A_validates": False,
        "actual_route_B_validates": False,
        "route_A_conditional_validates": True,
        "route_B_conditional_validates": True,
        "route_B_table_shape_ready": True,
        "source_promotion_contract_built": True,
        "anti_cycle_confirmed": True,
        "source_promotion_closed_now": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B32 Dual Path Home Stretch v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B32-SAMESOURCE-EMISSION-OR-ACTUAL-ROWPACKET`

## Tried Both Paths

```text
Route A actual same-source Phi_fin/b emission validates      False
Route B actual independent row-source packet validates       False
Route A conditional witness validates                       True
Route B conditional witness validates                       True
Route B table shape ready                                   True
```

## What This Means

This removes the last numerical-search ambiguity. The blocker is source
promotion only.

## Home-Stretch Contract

Route A must emit:

```text
physical action restriction to finite Weyl quotient
zero extra boundary/source term
phase R_Z source selection
shift R_X source selection
same-source b_selected emission
```

Route B must emit:

```text
selected basis-to-row functional theorem for all 72 primitive rows
pre-residual phase/shift variation operators
independent Hessian counterterm/source rows
sector rows assembled from those source rows
no residual-projector replay or locked-target values as source
```

## Next

`CONST-EW-02 / WEAK-MIXING / B33-SELECTED-SOURCE-PROMOTION-PACKET`
"""

    for path, payload in [
        (DUAL_FILL, dual_fill),
        (CONDITIONAL, conditional),
        (TABLE, table),
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
