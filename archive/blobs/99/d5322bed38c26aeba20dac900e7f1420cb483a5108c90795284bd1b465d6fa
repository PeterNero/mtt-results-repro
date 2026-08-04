"""Build selected primitive-kernel slot coverage and isolate variation/Hessian gap."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_primitivekernelslotcoverage_or_variationhessiangap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SLOT_TABLE = PACKET_DIR / "primitive_kernel_72_slot_coverage.packet.json"
GAP = PACKET_DIR / "variation_hessian_source_gap.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_PrimitiveKernelSlotCoverage_or_VariationHessianGap_v1.md"

PREVIOUS = DATA / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate.candidate.json"
SOURCE_TEMPLATE = (
    DATA
    / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate"
    / "primitive_kernel_source_theorem.strict_template.json"
)
BASIS_FILL = (
    DATA
    / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap"
    / "route_b_selected_basis_independence_fill.packet.json"
)

STATUS = "MTT_SELECTED_PRIMITIVEKERNELSLOTCOVERAGE_BUILT_VARIATION_HESSIAN_GAP_OPEN"
NEXT = "MTT_Selected_VariationOperatorAndHessianSourceTheorem_or_PhysicalPhiFinC1Emission_v1"


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


def basis_for(summary: dict[str, Any], sector: str) -> list[str]:
    if sector == "Hdagger":
        return [f"conj({label})" for label in summary["H"]["selected_basis_labels"]]
    return summary[sector]["selected_basis_labels"]


def main() -> int:
    previous = load(PREVIOUS)
    source_template = load(SOURCE_TEMPLATE)
    basis_fill = load(BASIS_FILL)

    basis_summary = basis_fill["route_B_independent_execution"][
        "selected_basis_independence_certificate"
    ]["basis_summary"]
    couplings = source_template["sector_couplings"]
    sector_order = source_template["coordinate_system"]["sector_order"]
    components = ["real", "imag"]

    rows: list[dict[str, Any]] = []
    for sector in sector_order:
        coupling = couplings[sector]
        left_basis = basis_for(basis_summary, coupling["left_sector"])
        right_basis = basis_for(basis_summary, coupling["right_sector"])
        higgs_basis = basis_for(basis_summary, coupling["higgs_sector"])
        for i, left_label in enumerate(left_basis):
            for j, right_label in enumerate(right_basis):
                for component in components:
                    rows.append(
                        {
                            "row_index": len(rows),
                            "sector": sector,
                            "matrix_entry": [i, j],
                            "component": component,
                            "left_basis": left_label,
                            "right_basis": right_label,
                            "higgs_basis": higgs_basis[0],
                            "directions_to_evaluate": source_template["coordinate_system"]["columns"],
                            "row_function_slot_typed": True,
                            "dynamic_variation_operator_sourced": False,
                            "hessian_counterterm_sourced": False,
                            "residual_projector_used_as_source": False,
                        }
                    )

    expected_count = source_template["coordinate_system"]["codomain_real_dimension"]
    all_basis_labels_selected = all(
        sector_data["source_verified_by_transport_conjugation"] is True
        for sector, sector_data in basis_summary.items()
        if sector != "Hdagger"
    )
    row_count_ok = len(rows) == expected_count
    sectors_ok = sorted({row["sector"] for row in rows}) == sorted(sector_order)

    slot_table = {
        "schema": "MTTPrimitiveKernel72SlotCoverage.v1",
        "status": "ALL_72_PRIMITIVE_ROW_SLOTS_TYPED_VARIATION_HESSIAN_OPEN",
        "row_count": len(rows),
        "expected_row_count": expected_count,
        "row_count_ok": row_count_ok,
        "sectors_ok": sectors_ok,
        "all_basis_labels_selected_by_transport": all_basis_labels_selected,
        "hdagger_policy": "Hdagger row slots use the conjugate of the selected H basis label.",
        "rows": rows,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    gap = {
        "schema": "MTTVariationHessianSourceGap.v1",
        "status": "ROW_SLOT_COVERAGE_CLOSED_DYNAMIC_SOURCE_STILL_OPEN",
        "closed_now": {
            "selected_basis_slot_coverage_for_72_rows": row_count_ok and sectors_ok,
            "sector_coupling_typing_for_u_d_e_nuD": True,
            "Hdagger_conjugate_basis_policy": True,
            "residual_projector_not_needed_for_slot_typing": True,
        },
        "not_closed": {
            "selected_phase_shift_variation_operators_pre_residual": True,
            "selected_hessian_counterterm_source": True,
            "row_formula_source_theorem_derived": True,
            "source_independent_of_residual_projector_replay": True,
        },
        "validator_field_policy": {
            "selected_basis_feeds_72_primitive_rows_remains_false": (
                "Slot typing is closed, but the strict validator field requires dynamic row-source "
                "evaluation from selected variation/Hessian data, not only basis coverage."
            )
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPrimitiveKernelSlotCoverageOrVariationHessianGap",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "source_template": rel(SOURCE_TEMPLATE),
            "basis_fill": rel(BASIS_FILL),
        },
        "output_packets": {
            "primitive_kernel_72_slot_coverage": rel(SLOT_TABLE),
            "variation_hessian_source_gap": rel(GAP),
        },
        "what_closes_now": gap["closed_now"],
        "what_remains_open": gap["not_closed"],
        "theorem": {
            "name": "SelectedPrimitiveKernelSlotCoverageTheorem",
            "proved": True,
            "statement": (
                "The selected stationary basis packet and primitive sector-coupling schema enumerate "
                "exactly 72 real primitive row-function slots: four sectors, three-by-three entries, "
                "and real/imaginary components. This proves slot coverage only; it does not prove "
                "the selected dynamic variation operators or Hessian counterterm source."
            ),
        },
        "closure_claimed": False,
        "previous_gate_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PrimitiveKernelSlotCoverage_or_VariationHessianGap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "row_count": len(rows),
        "expected_row_count": expected_count,
        "slot_coverage_closed": row_count_ok and sectors_ok and all_basis_labels_selected,
        "dynamic_variation_source_closed": False,
        "hessian_counterterm_source_closed": False,
        "route_B_promoted_now": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PrimitiveKernelSlotCoverage or VariationHessianGap v1

Status: `{STATUS}`

This step closes the combinatorial row-slot question. The selected transported
basis packet and the primitive coupling schema enumerate exactly `72` real row
slots: four sectors, three-by-three entries, and real/imaginary components.
`Hdagger` is handled as the conjugate selected Higgs basis.

This is deliberately weaker than Route B promotion. It proves that the selected
bases can type every row function, but not that the selected phase/shift
variation operators or Hessian counterterm source evaluate those rows.

Next artifact: `{NEXT}`.
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "{SLUG}.candidate.json"
SLOT_TABLE = ROOT / "candidate_data" / "{SLUG}" / "primitive_kernel_72_slot_coverage.packet.json"
GAP = ROOT / "candidate_data" / "{SLUG}" / "variation_hessian_source_gap.packet.json"
CERT = ROOT / "certificates" / "{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrimitiveKernelSlotCoverage_or_VariationHessianGap_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    slot_table = load(SLOT_TABLE)
    gap = load(GAP)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "slot theorem not proved")
    require(slot_table["row_count"] == 72, "wrong row count")
    require(slot_table["expected_row_count"] == 72, "wrong expected count")
    require(slot_table["row_count_ok"] is True, "row count not ok")
    require(slot_table["sectors_ok"] is True, "sectors not ok")
    require(slot_table["all_basis_labels_selected_by_transport"] is True, "basis labels not selected")
    require(all(row["row_function_slot_typed"] is True for row in slot_table["rows"]), "some rows untyped")
    require(all(row["dynamic_variation_operator_sourced"] is False for row in slot_table["rows"]), "variation overclosed")
    require(all(row["hessian_counterterm_sourced"] is False for row in slot_table["rows"]), "hessian overclosed")
    require(gap["closed_now"]["selected_basis_slot_coverage_for_72_rows"] is True, "slot coverage not closed")
    require(gap["not_closed"]["selected_phase_shift_variation_operators_pre_residual"] is True, "variation gap missing")
    require(gap["not_closed"]["selected_hessian_counterterm_source"] is True, "hessian gap missing")
    require(cert["slot_coverage_closed"] is True, "cert slot coverage not closed")
    require(cert["dynamic_variation_source_closed"] is False, "variation source overclosed")
    require(cert["hessian_counterterm_source_closed"] is False, "hessian source overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("deliberately weaker than Route B promotion" in note, "note missing guardrail")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(SLOT_TABLE, slot_table)
    write_json(GAP, gap)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(AUDIT)}")
    print(f"Rows: {len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
