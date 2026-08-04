"""Build pure Weyl coefficient rows / primitive C1 formula execution gate.

The second-order coefficient gate identified the rows lambda_static*Z and
lambda_static*X as the missing object.  Algebraically one might try to extract
pure Z and X from first-response rows by subtracting a dynamic identity row:

    Z = (I+Z) - I,   X = (I+X) - I.

This artifact records why that shortcut is not currently a selected proof: the
repo has selected static trace/unit normalizations, but not an emitted dynamic
C1 identity row or executed primitive C1 row formula.  The next executable
target is therefore zero-mode/Hessian/primitive-row execution, not identity
subtraction by convention.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_pureweylcoefficientrows_or_primitivec1formulaexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DECOMP = PACKET_DIR / "pure_weyl_row_algebraic_decomposition.packet.json"
IDENTITY_BOUNDARY = PACKET_DIR / "dynamic_identity_row_source_boundary.packet.json"
PRIMITIVE_CUTSET = PACKET_DIR / "primitive_c1_formula_execution_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PureWeylCoefficientRows_or_PrimitiveC1FormulaExecution_v1.md"

SECOND_ORDER = DATA / "selected_secondorderdynamiccoefficientemission_or_lambdarepresentativeselection.candidate.json"
REQUIRED_ROWS = (
    DATA
    / "selected_secondorderdynamiccoefficientemission_or_lambdarepresentativeselection"
    / "second_order_coefficient_required_rows.packet.json"
)
FORMAL110 = (
    DATA
    / "selected_postsourceformal110_observableaudit_or_fullsmgap"
    / "formal110_sector_matrix_observables.packet.json"
)
PAYLOAD_INVENTORY = (
    DATA
    / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution"
    / "dynamic_phifin_c1_payload_row_inventory.packet.json"
)
PAYLOAD_RECONCILIATION = (
    DATA
    / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution"
    / "support_vs_selected_payload_reconciliation.packet.json"
)
HIGHER_ATTEMPT = (
    DATA
    / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution"
    / "higher_response_execution_attempt_after_payload_inventory.packet.json"
)
SMSLOT_OVERLAP = DATA / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"
EXT_HODGE = DATA / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"

STATUS = "MTT_SELECTED_PURE_WEYL_COEFFICIENT_ROWS_BUILT_IDENTITY_SUBTRACTION_BLOCKED_PRIMITIVE_EXECUTION_OPEN"
NEXT = "MTT_Selected_ZeroModeHessianPrimitiveRowExecution_or_PureWeylRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    second_order = load(SECOND_ORDER)
    required_rows = load(REQUIRED_ROWS)
    formal110 = load(FORMAL110)
    inventory = load(PAYLOAD_INVENTORY)
    reconciliation = load(PAYLOAD_RECONCILIATION)
    higher_attempt = load(HIGHER_ATTEMPT)
    smslot = load(SMSLOT_OVERLAP)
    ext_hodge = load(EXT_HODGE)

    dynamic_identity_row_emitted = any(
        row["row_id"] in {"identity_C1", "unit_C1", "dynamic_identity"}
        and row.get("accepted_as_dynamic_phifin_c1_payload_row") is True
        for row in inventory["rows"]
    )

    decomposition = {
        "schema": "MTTPureWeylRowAlgebraicDecomposition.v1",
        "status": "ALGEBRAIC_DECOMPOSITION_AVAILABLE_SELECTED_SOURCE_NOT_YET",
        "algebraic_identities": {
            "phase_pure_Z": "Z = (I + Z) - I",
            "shift_pure_X": "X = (I + X) - I",
            "phase_second_order": "lambda_static * Z on u,e",
            "shift_second_order": "lambda_static * X on d,nuD",
        },
        "first_response_rows_available": {
            "phase_first_response": formal110["sector_observables"]["u"]["source_direction"],
            "shift_first_response": formal110["sector_observables"]["d"]["source_direction"],
            "non_scalar_first_splitting_emitted": formal110["global_observable_decision"][
                "first_non_scalar_family_splitting_emitted"
            ],
        },
        "dynamic_identity_row_required": True,
        "dynamic_identity_row_emitted": dynamic_identity_row_emitted,
        "identity_subtraction_promoted_as_selected_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECOMP, decomposition)

    identity_boundary = {
        "schema": "MTTDynamicIdentityRowSourceBoundary.v1",
        "status": "STATIC_UNIT_NORMALIZATION_DOES_NOT_EMIT_DYNAMIC_C1_IDENTITY_ROW",
        "static_support_closed": {
            "smslot_all_six_arrows_closed": smslot["arrow_status"]["all_six_closed"],
            "selected_static_overlap_kernel": smslot["selected_overlap_kernel"]["selected"],
            "selected_ext_unit_row_closed": smslot["selected_overlap_kernel"]["preconditions"][
                "selected_ext_unit_row_closed"
            ],
            "selected_hodge_projector_row_closed": ext_hodge["gauge_projector_table"][
                "closed_for_eta_row"
            ],
        },
        "dynamic_payload_status": {
            "accepted_dynamic_payload_row_count": inventory["accepted_dynamic_payload_row_count"],
            "same_source_dynamic_payload_closed": reconciliation["same_source_dynamic_payload_closed"],
            "primitive_row_formula_executed": reconciliation["primitive_row_formula_executed"],
            "selected_functional_executed": higher_attempt["selected_functional_executed"],
            "dynamic_identity_row_emitted": dynamic_identity_row_emitted,
        },
        "decision": (
            "Static unit/trace normalization may normalize selected rows, but it cannot be used as a "
            "dynamic C1 identity row for source-level subtraction until the dynamic Phi_fin/C1 payload "
            "or primitive C1 formula emits that row."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(IDENTITY_BOUNDARY, identity_boundary)

    primitive_cutset = {
        "schema": "MTTPrimitiveC1FormulaExecutionCutsetForPureWeylRows.v1",
        "status": "PRIMITIVE_EXECUTION_REQUIRED_FOR_SELECTED_PURE_WEYL_ROWS",
        "must_emit": [
            "selected dynamic C1 identity/unit row or an identity-free formula for pure Z/X",
            "selected zero-mode basis values",
            "selected finite Hessian C1 source blocks",
            "primitive C1 contractions isolating pure Z and pure X coefficient rows",
        ],
        "forbidden_shortcuts": [
            "subtract static identity or trace normalization as if it were a dynamic C1 row",
            "choose lambda representative from observed Yukawa/CKM/PMNS data",
            "reuse first-response VSD packet as second-order coefficient emission",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The algebraic extraction is clear, but source promotion requires a dynamic identity "
                "row or primitive formula execution that directly emits pure Z/X coefficient rows."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PRIMITIVE_CUTSET, primitive_cutset)

    candidate = {
        "candidate": "MTTSelectedPureWeylCoefficientRowsOrPrimitiveC1FormulaExecution",
        "status": STATUS,
        "inputs": {
            "second_order_dynamic_coefficient_gate": rel(SECOND_ORDER),
            "second_order_required_rows": rel(REQUIRED_ROWS),
            "formal110_observables": rel(FORMAL110),
            "dynamic_payload_inventory": rel(PAYLOAD_INVENTORY),
            "support_vs_selected_payload_reconciliation": rel(PAYLOAD_RECONCILIATION),
            "higher_response_execution_attempt": rel(HIGHER_ATTEMPT),
            "smslot_overlap_kernel_source": rel(SMSLOT_OVERLAP),
            "ext_hodge_projector_table": rel(EXT_HODGE),
        },
        "output_packets": {
            "pure_weyl_row_algebraic_decomposition": rel(DECOMP),
            "dynamic_identity_row_source_boundary": rel(IDENTITY_BOUNDARY),
            "primitive_c1_formula_execution_cutset": rel(PRIMITIVE_CUTSET),
        },
        "theorem": {
            "name": "PureWeylRowsRequireDynamicIdentityOrPrimitiveFormulaTheorem",
            "proved": (
                decomposition["first_response_rows_available"]["non_scalar_first_splitting_emitted"]
                is True
                and dynamic_identity_row_emitted is False
                and reconciliation["primitive_row_formula_executed"] is False
            ),
            "statement": (
                "Pure Weyl rows are algebraically Z=(I+Z)-I and X=(I+X)-I, but the current selected "
                "source does not emit a dynamic C1 identity row.  Static trace/unit normalization and "
                "the selected Ext unit row are not dynamic C1 identity rows.  Therefore pure Z/X "
                "coefficient rows cannot be promoted by identity subtraction now; they require dynamic "
                "identity emission or primitive C1 formula execution."
            ),
        },
        "what_closes_now": {
            "pure_Z_X_algebraic_decomposition_recorded": True,
            "identity_subtraction_shortcut_rejected": True,
            "static_unit_vs_dynamic_identity_boundary_built": True,
            "primitive_execution_cutset_for_pure_weyl_rows_built": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_dynamic_C1_identity_or_identity_free_pure_weyl_formula": True,
            "selected_zero_mode_basis_values": True,
            "selected_finite_Hessian_C1_source_blocks": True,
            "primitive_C1_contractions": True,
            "pure_Weyl_coefficient_rows_lambda_Z_lambda_X": True,
            "individual_lambda_representative_selection_or_coexistence": True,
            "selected_second_order_physical_matrix_promotion": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "closure_decision": {
            "pure_Weyl_rows_emitted": False,
            "identity_subtraction_promoted": False,
            "primitive_C1_formula_executed": False,
            "individual_lambda_value_selected": False,
            "selected_second_order_physical_matrices_promoted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": second_order["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_PureWeylCoefficientRows_or_PrimitiveC1FormulaExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": candidate["theorem"]["proved"],
        "pure_Z_X_algebraic_decomposition_recorded": True,
        "identity_subtraction_shortcut_rejected": True,
        "dynamic_identity_row_emitted": dynamic_identity_row_emitted,
        "primitive_C1_formula_executed": False,
        "pure_Weyl_rows_emitted": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected PureWeylCoefficientRows or PrimitiveC1FormulaExecution v1

Status: `{STATUS}`.

Algebraically, the pure Weyl rows are simple:

```text
Z = (I + Z) - I
X = (I + X) - I
```

But this is not yet a selected dynamic-source proof:

```text
static unit/trace normalization closed : true
dynamic C1 identity row emitted        : {str(dynamic_identity_row_emitted).lower()}
primitive C1 formula executed          : {str(reconciliation["primitive_row_formula_executed"]).lower()}
identity subtraction promoted          : false
pure Weyl coefficient rows emitted     : false
full SM closure                        : false
```

So the shortcut is rejected.  The next proof must emit a dynamic C1 identity
row, or execute an identity-free primitive C1 formula that directly produces
pure `Z` and pure `X` coefficient rows.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
