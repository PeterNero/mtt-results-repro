"""Audit selected_primitivekernelslotcoverage_or_variationhessiangap."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_primitivekernelslotcoverage_or_variationhessiangap.candidate.json"
SLOT_TABLE = ROOT / "candidate_data" / "selected_primitivekernelslotcoverage_or_variationhessiangap" / "primitive_kernel_72_slot_coverage.packet.json"
GAP = ROOT / "candidate_data" / "selected_primitivekernelslotcoverage_or_variationhessiangap" / "variation_hessian_source_gap.packet.json"
CERT = ROOT / "certificates" / "selected_primitivekernelslotcoverage_or_variationhessiangap_certificate.json"
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

    require(data["status"] == "MTT_SELECTED_PRIMITIVEKERNELSLOTCOVERAGE_BUILT_VARIATION_HESSIAN_GAP_OPEN", "status mismatch")
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
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
