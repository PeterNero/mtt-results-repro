"""Audit selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource.candidate.json"
CERT = ROOT / "certificates" / "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource_certificate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource"
ROW = PACKET_DIR / "first_row_kernel_formula_source_packet.packet.json"
DECISION = PACKET_DIR / "kernel_source_promotion_decision.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DifferentiatedPhiFinC1PrimitiveOverlap_or_FirstRowKernelFormulaSource_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    cert = load(CERT)
    row = load(ROW)
    decision = load(DECISION)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_DIFFERENTIATEDPHIFINC1PRIMITIVEOVERLAP_OR_FIRSTROWKERNELFORMULASOURCE_BUILT_FORMULA_PAIRING_SOURCE_ROW_VALUE_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["what_closes_now"]["first_row_kernel_formula_source_specified"] is True, "row formula source not specified")
    require(data["what_closes_now"]["finite_trace_frobenius_pairing_source_attached"] is True, "finite pairing source not attached")
    require(row["row_id"] == "u:phase:r0c0", "row mismatch")
    require("HessianCounterterm_u^phase[0,0]" in row["selected_primitive_kernel_formula"], "formula not specialized")
    require(row["selected_trace_or_pairing_source"]["finite_pairing_source_verified"] is True, "pairing not verified")
    require(row["computed_independent_complex_entry_value"] is False, "row value overclaimed")
    require(row["first_row_independently_executed_now"] is False, "row execution overclaimed")
    require(decision["closed_kernel_clauses_for_first_row"]["selected_primitive_kernel_formula"] is True, "formula clause not closed")
    require(decision["closed_kernel_clauses_for_first_row"]["selected_physical_or_independent_trace_pairing_clause"] is True, "pairing clause not closed")
    require(decision["closed_kernel_clauses_for_first_row"]["computed_independent_complex_entries"] is False, "computed entries overclaimed")
    require(decision["full_72_row_execution_closed"] is False, "72 rows overclaimed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM equivalence overclaimed")
    require(decision["no_knob_closed"] is False, "no-knob closure overclaimed")
    require(cert["first_row_formula_source_specified"] is True, "certificate missing formula")
    require(cert["first_row_value_executed"] is False, "certificate overclaims row execution")
    require("Next artifact" in note, "note missing next artifact")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
