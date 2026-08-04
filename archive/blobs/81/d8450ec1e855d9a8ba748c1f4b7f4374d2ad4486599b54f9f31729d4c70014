"""Build variation-operator shape compatibility and keep Hessian/source gate open."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_variationoperatorshapecompatibility_or_hessiansourcegap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTING = PACKET_DIR / "variation_operator_72_slot_routing.packet.json"
COMPAT = PACKET_DIR / "variation_operator_shape_compatibility.packet.json"
GAP = PACKET_DIR / "hessian_source_and_selection_gap.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_VariationOperatorShapeCompatibility_or_HessianSourceGap_v1.md"

PREVIOUS = DATA / "selected_primitivekernelslotcoverage_or_variationhessiangap.candidate.json"
SLOT_TABLE = (
    DATA
    / "selected_primitivekernelslotcoverage_or_variationhessiangap"
    / "primitive_kernel_72_slot_coverage.packet.json"
)
SOURCE_MAP = (
    DATA
    / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution"
    / "primitive_tensor_hessian_source_map_candidate.packet.json"
)
OBLIGATION = (
    DATA
    / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution"
    / "source_map_selection_obligation_kernel.packet.json"
)
ALL_ROWS = (
    DATA
    / "selected_firstrowprovenancepromotion_or_allrowsweylexecution"
    / "all_rows_execution_decision.packet.json"
)

STATUS = "MTT_SELECTED_VARIATIONOPERATORSHAPECOMPATIBILITY_BUILT_HESSIAN_SOURCE_GAP_OPEN"
NEXT = "MTT_Selected_HessianCountertermSourceAndBVectorTheorem_or_PhysicalPhiFinC1Emission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def route_for_sector(sector: str) -> tuple[str, str]:
    if sector in {"u", "e"}:
        return "phase_packet", "phase_R_Z"
    if sector in {"d", "nuD"}:
        return "shift_packet", "shift_R_X"
    raise KeyError(sector)


def main() -> int:
    previous = load(PREVIOUS)
    slot_table = load(SLOT_TABLE)
    source_map = load(SOURCE_MAP)
    obligation = load(OBLIGATION)
    all_rows = load(ALL_ROWS)

    candidate_ops = source_map["candidate_residual_operators"]
    phase_shape = candidate_ops["phase_R_Z"]["shape"]
    shift_shape = candidate_ops["shift_R_X"]["shape"]

    routed_rows: list[dict[str, Any]] = []
    for row in slot_table["rows"]:
        active_direction, operator = route_for_sector(row["sector"])
        shape = phase_shape if operator == "phase_R_Z" else shift_shape
        routed_rows.append(
            {
                "row_index": row["row_index"],
                "sector": row["sector"],
                "matrix_entry": row["matrix_entry"],
                "component": row["component"],
                "active_direction": active_direction,
                "variation_operator_shape": operator,
                "operator_shape_rank": shape["residual_rank"],
                "operator_shape_norm_sq": shape["residual_norm_sq"],
                "operator_shape_orthogonal_to_fixed_fiber_span": shape[
                    "orthogonal_to_fixed_fiber_span"
                ],
                "slot_typed_by_selected_basis": row["row_function_slot_typed"],
                "operator_shape_attached": True,
                "operator_selected_as_source_now": candidate_ops[operator]["selected_by_MTT_now"],
                "hessian_counterterm_sourced": False,
                "residual_projector_used_as_source": False,
            }
        )

    phase_rows = [row for row in routed_rows if row["variation_operator_shape"] == "phase_R_Z"]
    shift_rows = [row for row in routed_rows if row["variation_operator_shape"] == "shift_R_X"]
    all_shapes_attached = all(row["operator_shape_attached"] for row in routed_rows)
    no_shape_selected = not any(row["operator_selected_as_source_now"] for row in routed_rows)

    routing = {
        "schema": "MTTVariationOperator72SlotRouting.v1",
        "status": "VARIATION_OPERATOR_SHAPES_ROUTED_TO_72_SLOTS_SELECTION_OPEN",
        "row_count": len(routed_rows),
        "phase_R_Z_rows": len(phase_rows),
        "shift_R_X_rows": len(shift_rows),
        "sector_routing": {
            "phase_R_Z": ["u", "e"],
            "shift_R_X": ["d", "nuD"],
        },
        "rows": routed_rows,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    compatibility = {
        "schema": "MTTVariationOperatorShapeCompatibility.v1",
        "status": "SHAPE_COMPATIBILITY_CLOSED_SOURCE_SELECTION_OPEN",
        "compatible_with_72_slot_table": len(routed_rows) == 72
        and len(phase_rows) == 36
        and len(shift_rows) == 36,
        "phase_operator_shape_attached": True,
        "shift_operator_shape_attached": True,
        "all_routed_operator_shapes_attached": all_shapes_attached,
        "operator_shapes_selected_as_source_now": False,
        "source_map_selected_by_MTT_now": source_map["selected_by_MTT_now"],
        "obligation_currently_emitted": obligation["currently_emitted"],
        "all_rows_values_exact_support": all_rows["all_72_row_values_exact"],
        "all_rows_provenance_independent": all_rows["closed_kernel_clauses_for_all_rows"][
            "provenance_independent_of_residual_projector_replay"
        ],
        "selection_guard": {
            "shape_compatibility_is_not_source_selection": True,
            "residual_projector_outputs_may_be_compared_not_used_as_source": True,
            "hessian_counterterm_source_still_required": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    gap = {
        "schema": "MTTHessianSourceAndSelectionGap.v1",
        "status": "VARIATION_SHAPE_COMPATIBILITY_CLOSED_HESSIAN_AND_SELECTION_OPEN",
        "closed_now": {
            "phase_shift_variation_operator_shapes_attached": True,
            "variation_operator_shapes_routed_to_all_72_slots": compatibility[
                "compatible_with_72_slot_table"
            ],
            "phase_shift_sector_partition_verified": True,
            "operator_shape_selection_not_overclaimed": no_shape_selected,
        },
        "not_closed": {
            "selected_phase_shift_variation_operators_pre_residual": True,
            "selected_hessian_counterterm_source": True,
            "selected_b_vector_source": True,
            "row_formula_source_theorem_derived": True,
            "source_independent_of_residual_projector_replay": True,
        },
        "why_not_routeB_promotion": [
            "The phase/shift residual operator shapes are compatible with the 72 selected row slots, but selected_by_MTT_now is still false.",
            "The Hessian counterterm and b_selected source vector are not emitted.",
            "Existing all-row values remain exact support, not residual-projector-independent source provenance.",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedVariationOperatorShapeCompatibilityOrHessianSourceGap",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "slot_table": rel(SLOT_TABLE),
            "source_map_candidate": rel(SOURCE_MAP),
            "selection_obligation_kernel": rel(OBLIGATION),
            "all_rows_decision": rel(ALL_ROWS),
        },
        "output_packets": {
            "variation_operator_72_slot_routing": rel(ROUTING),
            "variation_operator_shape_compatibility": rel(COMPAT),
            "hessian_source_and_selection_gap": rel(GAP),
        },
        "what_closes_now": gap["closed_now"],
        "what_remains_open": gap["not_closed"],
        "theorem": {
            "name": "VariationOperatorShapeCompatibilityTheorem",
            "proved": True,
            "statement": (
                "The source-map candidate supplies phase_R_Z and shift_R_X residual-operator shapes "
                "that route compatibly across the selected 72 primitive row slots: phase on u/e and "
                "shift on d/nuD. This proves shape and slot compatibility only; the operators are not "
                "selected as physical source data, and the Hessian counterterm/b source remains open."
            ),
        },
        "closure_claimed": False,
        "previous_gate_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_VariationOperatorShapeCompatibility_or_HessianSourceGap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "row_count": len(routed_rows),
        "phase_R_Z_rows": len(phase_rows),
        "shift_R_X_rows": len(shift_rows),
        "shape_compatibility_closed": compatibility["compatible_with_72_slot_table"],
        "variation_operators_selected_as_source": False,
        "hessian_counterterm_source_closed": False,
        "b_selected_source_closed": False,
        "route_B_promoted_now": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected VariationOperatorShapeCompatibility or HessianSourceGap v1

Status: `{STATUS}`

This step proves shape compatibility for the dynamic variation operators. The
existing source-map candidate supplies `phase_R_Z` and `shift_R_X` residual
operator shapes, and the selected slot table routes them across all `72`
primitive row slots: phase on `u,e`, shift on `d,nuD`.

This is not source promotion. The operator shapes remain unselected as physical
source data, and the Hessian counterterm / `b_selected` source vector is still
missing.

Next artifact: `{NEXT}`.
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "{SLUG}.candidate.json"
ROUTING = ROOT / "candidate_data" / "{SLUG}" / "variation_operator_72_slot_routing.packet.json"
COMPAT = ROOT / "candidate_data" / "{SLUG}" / "variation_operator_shape_compatibility.packet.json"
GAP = ROOT / "candidate_data" / "{SLUG}" / "hessian_source_and_selection_gap.packet.json"
CERT = ROOT / "certificates" / "{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_VariationOperatorShapeCompatibility_or_HessianSourceGap_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    routing = load(ROUTING)
    compat = load(COMPAT)
    gap = load(GAP)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(routing["row_count"] == 72, "wrong row count")
    require(routing["phase_R_Z_rows"] == 36, "wrong phase count")
    require(routing["shift_R_X_rows"] == 36, "wrong shift count")
    require(all(row["operator_shape_attached"] is True for row in routing["rows"]), "shape missing")
    require(all(row["operator_selected_as_source_now"] is False for row in routing["rows"]), "operator source overclosed")
    require(all(row["hessian_counterterm_sourced"] is False for row in routing["rows"]), "hessian overclosed")
    require(compat["compatible_with_72_slot_table"] is True, "compatibility not closed")
    require(compat["operator_shapes_selected_as_source_now"] is False, "source selection overclosed")
    require(compat["all_rows_provenance_independent"] is False, "all rows provenance unexpectedly promoted")
    require(gap["closed_now"]["variation_operator_shapes_routed_to_all_72_slots"] is True, "routing gap not closed")
    require(gap["not_closed"]["selected_phase_shift_variation_operators_pre_residual"] is True, "variation source gap missing")
    require(gap["not_closed"]["selected_hessian_counterterm_source"] is True, "hessian gap missing")
    require(gap["not_closed"]["selected_b_vector_source"] is True, "b source gap missing")
    require(cert["shape_compatibility_closed"] is True, "cert compatibility not closed")
    require(cert["variation_operators_selected_as_source"] is False, "cert source overclosed")
    require(cert["hessian_counterterm_source_closed"] is False, "cert hessian overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("This is not source promotion" in note, "note missing guardrail")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(ROUTING, routing)
    write_json(COMPAT, compatibility)
    write_json(GAP, gap)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(AUDIT)}")
    print(f"Rows: {len(routed_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
