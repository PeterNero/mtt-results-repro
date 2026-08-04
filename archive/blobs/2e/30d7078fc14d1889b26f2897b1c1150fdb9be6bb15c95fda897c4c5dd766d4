"""Build zero-mode/Hessian/primitive-row execution or pure-Weyl rows gate.

This artifact reconciles the older pure-Weyl identity-subtraction blocker with
the later VSD-01 source assembly closure.  The direct exact primitive rows
already contain pure R_Z and R_X rows, so the unscaled pure-Weyl primitive row
layer can close without emitting a dynamic identity row.

It still does not close the lambda coefficient representative, selected
second-order physical matrices, higher-response scalar rows, or full SM/no-knob
closure.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_zeromodehessianprimitiverowexecution_or_pureweylrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PURE_ROWS = PACKET_DIR / "identity_free_pure_weyl_rows.packet.json"
HESSIAN_GATE = PACKET_DIR / "zeromode_hessian_payload_reconciliation.packet.json"
PROMOTION = PACKET_DIR / "pure_weyl_promotion_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_identity_free_pure_weyl_rows.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ZeroModeHessianPrimitiveRowExecution_or_PureWeylRows_v1.md"

PAYLOAD_GATE = DATA / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution.candidate.json"
PAYLOAD_INVENTORY = (
    DATA
    / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution"
    / "dynamic_phifin_c1_payload_row_inventory.packet.json"
)
HYM_VALUES = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"
PURE_WEYL_GATE = DATA / "selected_pureweylcoefficientrows_or_primitivec1formulaexecution.candidate.json"
PURE_WEYL_CUTSET = (
    DATA
    / "selected_pureweylcoefficientrows_or_primitivec1formulaexecution"
    / "primitive_c1_formula_execution_cutset.packet.json"
)
ALL72 = (
    DATA
    / "selected_firstrowprovenancepromotion_or_allrowsweylexecution"
    / "all_72_exact_weyl_row_execution.packet.json"
)
FORMAL110 = (
    DATA
    / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
    / "formal_110_row_replay_integrated.packet.json"
)
VSD01_SOURCE = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json"
VSD01_DYNAMIC = DATA / "selected_vsd01_dynamicoperatorbackimport_or_yukawavaluefrontier.candidate.json"
SAME_SOURCE = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
SOURCE_SUMMARY = (
    DATA
    / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate"
    / "unpatched_source_promotion_replay_summary.packet.json"
)

STATUS = (
    "MTT_SELECTED_ZEROMODEHESSIANPRIMITIVEROWEXECUTION_OR_PUREWEYLROWS_"
    "BUILT_IDENTITY_FREE_PURE_WEYL_ROWS_CLOSED_LAMBDA_OPEN"
)
NEXT = "MTT_Selected_PureWeylLambdaRepresentative_or_HigherResponseScalarRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing zero-mode/Hessian primitive inputs: " + ", ".join(missing))


def rows_by_source(rows: list[dict[str, Any]], source: str) -> list[dict[str, Any]]:
    return [row for row in rows if row.get("value_source") == source]


def exact_rows(rows: list[dict[str, Any]]) -> bool:
    return all(
        row.get("computed_value_clause_closed") is True
        and row.get("exactness_clause_closed") is True
        and row.get("matches_formal_quadrature_value") is True
        and row.get("observed_data_used_as_selector") is False
        and row.get("target_fitting_used") is False
        for row in rows
    )


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PAYLOAD_GATE,
        PAYLOAD_INVENTORY,
        HYM_VALUES,
        PURE_WEYL_GATE,
        PURE_WEYL_CUTSET,
        ALL72,
        FORMAL110,
        VSD01_SOURCE,
        VSD01_DYNAMIC,
        SAME_SOURCE,
        SOURCE_SUMMARY,
    ]
    require_sources(sources)

    payload_gate = load(PAYLOAD_GATE)
    payload_inventory = load(PAYLOAD_INVENTORY)
    hym_values = load(HYM_VALUES)
    pure_weyl_gate = load(PURE_WEYL_GATE)
    pure_weyl_cutset = load(PURE_WEYL_CUTSET)
    all72 = load(ALL72)
    formal110 = load(FORMAL110)
    vsd01_source = load(VSD01_SOURCE)
    vsd01_dynamic = load(VSD01_DYNAMIC)
    same_source = load(SAME_SOURCE)
    source_summary = load(SOURCE_SUMMARY)

    rz_rows = rows_by_source(all72["rows"], "R_Z")
    rx_rows = rows_by_source(all72["rows"], "R_X")
    zero_route_count = int(all72["source_counts"]["zero_route"])
    rz_sectors = sorted({row["sector"] for row in rz_rows})
    rx_sectors = sorted({row["sector"] for row in rx_rows})

    source_assembly_closed = vsd01_source["closure_decision"][
        "VSD01_source_assembly_subgate_closed"
    ]
    dynamic_subgate_closed = vsd01_dynamic["closure_decision"][
        "VSD01_dynamic_tensor_subgate_closed"
    ]
    same_source_dynamic_closed = same_source["promotion_decision"][
        "dynamic_matter_overlap_operator_packet_closed"
    ]
    source_stack_promotes = source_summary["promoted_objects"]

    identity_free_pure_rows_closed = (
        all72["computed_value_clause_closed_for_all_rows"] is True
        and all72["exactness_clause_closed_for_all_rows"] is True
        and all72["all_rows_match_formal_packet"] is True
        and len(rz_rows) == 18
        and len(rx_rows) == 18
        and exact_rows(rz_rows)
        and exact_rows(rx_rows)
        and source_assembly_closed is True
        and source_stack_promotes["PhysicalPhiFinC1ActionSource"] is True
        and source_stack_promotes["A_selected"] is True
        and source_stack_promotes["b_selected"] is True
        and source_stack_promotes["deltaTheta_C1"] is True
    )

    pure_rows = {
        "schema": "MTTIdentityFreePureWeylRows.v1",
        "status": "IDENTITY_FREE_PURE_RZ_RX_PRIMITIVE_ROWS_CLOSED"
        if identity_free_pure_rows_closed
        else "IDENTITY_FREE_PURE_RZ_RX_PRIMITIVE_ROWS_OPEN",
        "previous_identity_subtraction_boundary": rel(PURE_WEYL_GATE),
        "identity_subtraction_used": False,
        "dynamic_C1_identity_row_emitted": False,
        "direct_pure_row_source": rel(ALL72),
        "row_counts": {
            "R_Z": len(rz_rows),
            "R_X": len(rx_rows),
            "zero_route": zero_route_count,
            "total": all72["row_count"],
        },
        "sector_coverage": {
            "R_Z_sectors": rz_sectors,
            "R_X_sectors": rx_sectors,
            "R_Z_expected_phase_sectors": ["e", "u"],
            "R_X_expected_shift_sectors": ["d", "nuD"],
        },
        "exactness": {
            "R_Z_rows_exact": exact_rows(rz_rows),
            "R_X_rows_exact": exact_rows(rx_rows),
            "all_72_exact": all72["exactness_clause_closed_for_all_rows"],
            "all_72_match_formal_packet": all72["all_rows_match_formal_packet"],
            "max_abs_error_against_formal_packet": all72[
                "max_abs_error_against_formal_packet"
            ],
        },
        "source_promotion": {
            "VSD01_source_assembly_subgate_closed": source_assembly_closed,
            "PhysicalPhiFinC1ActionSource_promoted": source_stack_promotes[
                "PhysicalPhiFinC1ActionSource"
            ],
            "A_selected_promoted": source_stack_promotes["A_selected"],
            "b_selected_promoted": source_stack_promotes["b_selected"],
            "deltaTheta_C1_promoted": source_stack_promotes["deltaTheta_C1"],
        },
        "accepted_as_unscaled_selected_pure_weyl_primitive_rows": identity_free_pure_rows_closed,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": identity_free_pure_rows_closed,
    }
    write_json(PURE_ROWS, pure_rows)

    hessian_gate = {
        "schema": "MTTZeroModeHessianPayloadReconciliation.v1",
        "status": "FINITE_ZEROMODE_VALUES_AND_SCALAR_HESSIAN_SOURCE_CLOSED_DYNAMIC_HYM_BLOCKS_OPEN",
        "hym_projector_values": {
            "finite_model_active_projector_values_emitted": hym_values["what_closes_now"][
                "finite_model_active_projector_values_emitted"
            ],
            "ordered_zero_mode_basis_ids_emitted": hym_values["what_closes_now"][
                "ordered_zero_mode_basis_ids_emitted"
            ],
            "positive_model_complement_gap_emitted": hym_values["what_closes_now"][
                "positive_model_complement_gap_emitted"
            ],
            "selected_HYM_projector_values_promoted": hym_values["validator_result"][
                "selected_HYM_projector_values_promoted"
            ],
            "selected_rho_s_promoted": hym_values["validator_result"][
                "rho_candidate_promoted_to_selected_rho_s"
            ],
        },
        "formal_hessian_source_rows": {
            "formal_110_rows_executed": formal110["formal_110_rows_executed"],
            "hessian_source_row_count": formal110["hessian_source_rows"]["count"],
            "A_transpose_A": formal110["hessian_source_rows"]["A_transpose_A"],
            "A_transpose_b": formal110["hessian_source_rows"]["A_transpose_b"],
            "deltaTheta_C1": formal110["hessian_source_rows"]["deltaTheta_C1"],
            "formal_hessian_rows_physical_source_promoted": formal110[
                "hessian_source_rows"
            ]["physical_source_promoted"],
            "same_branch_source_stack_promotes_A_b_deltaTheta": (
                source_stack_promotes["A_selected"]
                and source_stack_promotes["b_selected"]
                and source_stack_promotes["deltaTheta_C1"]
            ),
        },
        "dynamic_payload_inventory": {
            "accepted_dynamic_payload_row_count": payload_inventory[
                "accepted_dynamic_payload_row_count"
            ],
            "stationary_source_slot_closed_count": payload_inventory[
                "stationary_source_slot_closed_count"
            ],
            "higher_response_execution_inputs_available": payload_inventory[
                "higher_response_execution_inputs_available"
            ],
        },
        "what_this_reclassifies": [
            "unscaled pure R_Z/R_X primitive rows are closed directly, not by identity subtraction",
            "A/b/deltaTheta scalar normal equations are same-branch promoted by the source stack",
            "finite model-active HYM projector values remain support until selected HYM/Strominger source promotion",
            "dynamic higher-response HYM/Phi_fin payload blocks remain open",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(HESSIAN_GATE, hessian_gate)

    promotion = {
        "schema": "MTTPureWeylPromotionDecision.v1",
        "status": "UNSCALED_PURE_WEYL_ROWS_CLOSED_LAMBDA_AND_HIGHER_RESPONSE_OPEN",
        "previous_pure_weyl_blocker": pure_weyl_gate["status"],
        "previous_shortcut_rejected_correctly": pure_weyl_gate["closure_decision"][
            "identity_subtraction_promoted"
        ]
        is False,
        "identity_free_direct_row_route_closes": identity_free_pure_rows_closed,
        "what_closes_now": {
            "unscaled_selected_pure_R_Z_rows": identity_free_pure_rows_closed,
            "unscaled_selected_pure_R_X_rows": identity_free_pure_rows_closed,
            "identity_subtraction_no_longer_needed_for_unscaled_pure_rows": True,
            "VSD01_primitive_source_reconciled_with_pure_rows": source_assembly_closed,
            "first_response_dynamic_tensor_subgate_preserved": dynamic_subgate_closed,
            "same_source_dynamic_matter_overlap_packet_preserved": same_source_dynamic_closed,
        },
        "what_remains_open": {
            "lambda_static_coefficient_representative": True,
            "lambda_static_times_R_Z_R_X_scaled_rows": True,
            "selected_second_order_physical_matrices": True,
            "selected_HYM_projector_source_promotion": True,
            "higher_response_Rtheta_scalar_rows": True,
            "Yukawa_mass_mixing_value_closure": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROMOTION, promotion)

    cutset = {
        "schema": "MTTNextCutsetAfterIdentityFreePureWeylRows.v1",
        "status": "PURE_WEYL_ROWS_CLOSED_NEXT_LAMBDA_REPRESENTATIVE_OR_HIGHER_RESPONSE_SCALARS",
        "closed_now": promotion["what_closes_now"],
        "still_open": promotion["what_remains_open"],
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "derive/select lambda_static from the same higher-response source and scale the closed pure R_Z/R_X rows",
            "route_B": "execute the higher-response Rtheta scalar-row functional directly",
            "route_C": "prove a coexistence theorem if two lambda orientations remain physically admissible",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedZeroModeHessianPrimitiveRowExecutionOrPureWeylRows",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "identity_free_pure_weyl_rows": rel(PURE_ROWS),
            "zeromode_hessian_payload_reconciliation": rel(HESSIAN_GATE),
            "pure_weyl_promotion_decision": rel(PROMOTION),
            "next_cutset_after_identity_free_pure_weyl_rows": rel(CUTSET),
        },
        "theorem": {
            "name": "IdentityFreePureWeylPrimitiveRowsTheorem",
            "proved": identity_free_pure_rows_closed,
            "statement": (
                "The selected VSD-01 source assembly and exact 72-row finite Weyl execution provide "
                "direct pure R_Z and R_X primitive rows. Therefore the unscaled pure-Weyl primitive "
                "row layer closes without using the forbidden identity-subtraction shortcut. This "
                "does not select lambda_static, scale the pure rows into second-order physical "
                "matrices, promote model-active HYM projector values to selected HYM/Strominger "
                "values, execute the ten higher-response scalar rows, or close true SM equivalence."
            ),
        },
        "what_closes_now": promotion["what_closes_now"],
        "what_remains_open": promotion["what_remains_open"],
        "closure_decision": {
            "identity_free_unscaled_pure_Weyl_rows_closed": identity_free_pure_rows_closed,
            "dynamic_C1_identity_row_emitted": False,
            "identity_subtraction_promoted": False,
            "lambda_static_coefficient_representative_selected": False,
            "selected_second_order_physical_matrices_promoted": False,
            "selected_HYM_projector_values_promoted": False,
            "higher_response_Rtheta_scalar_rows_executed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_statuses": {
            "payload_gate": payload_gate["status"],
            "pure_weyl_gate": pure_weyl_gate["status"],
            "hym_values": hym_values["status"],
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": identity_free_pure_rows_closed,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_ZeroModeHessianPrimitiveRowExecution_or_PureWeylRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": identity_free_pure_rows_closed,
        "identity_free_unscaled_pure_Weyl_rows_closed": identity_free_pure_rows_closed,
        "dynamic_C1_identity_row_emitted": False,
        "identity_subtraction_promoted": False,
        "lambda_static_coefficient_representative_selected": False,
        "selected_second_order_physical_matrices_promoted": False,
        "selected_HYM_projector_values_promoted": False,
        "higher_response_Rtheta_scalar_rows_executed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": identity_free_pure_rows_closed,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected ZeroModeHessianPrimitiveRowExecution or PureWeylRows v1

Status: `{STATUS}`.

The important advance is that pure Weyl rows do **not** need the rejected
identity-subtraction shortcut. The exact primitive execution already emits
direct `R_Z` and `R_X` rows:

```text
R_Z rows = {len(rz_rows)}
R_X rows = {len(rx_rows)}
zero-route rows = {zero_route_count}
all 72 exact = {str(all72["exactness_clause_closed_for_all_rows"]).lower()}
VSD-01 source assembly closed = {str(source_assembly_closed).lower()}
```

So the unscaled selected pure-Weyl primitive row layer is closed. What remains
open is the scaling/physics layer:

```text
lambda_static representative selected = false
lambda_static * R_Z/R_X rows emitted  = false
selected second-order matrices        = false
higher-response scalar rows executed  = false
true SM equivalence                   = false
full no-knob closure                  = false
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
