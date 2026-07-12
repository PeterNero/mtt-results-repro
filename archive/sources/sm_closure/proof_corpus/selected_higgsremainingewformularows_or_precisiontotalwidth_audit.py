"""Audit remaining electroweak Higgs formula-row gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsremainingewformularows_or_precisiontotalwidth"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
EW_GATE = PACKET_DIR / "remaining_ew_formula_or_precision_import_gate.packet.json"
TEN_CHANNEL = PACKET_DIR / "refreshed_ten_channel_formula_status.packet.json"
TOTAL_DECISION = PACKET_DIR / "precision_total_width_decision_after_ew_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsRemainingEWFormulaRows_or_PrecisionTotalWidth_v1.md"

STATUS = "MTT_SELECTED_HIGGSREMAININGEWFORMULAROWS_OR_PRECISIONTOTALWIDTH_BUILT_EW_GATE_TOTAL_WIDTH_OPEN"
NEXT = "MTT_Selected_HiggsEWFormulaKernelExecution_or_PrecisionImportRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    ew_gate = load(EW_GATE)
    ten = load(TEN_CHANNEL)
    total = load(TOTAL_DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["target_fitting_used"] is False, "target fitting guard missing")
    require(data["observed_data_used_as_selector"] is False, "observed selector guard missing")
    require(ew_gate["summary"]["remaining_external_fill_count"] == 3, "remaining EW count mismatch")
    require(set(ew_gate["summary"]["remaining_external_fill_channels"]) == {"H_to_WW_star", "H_to_ZZ_star", "H_to_Z_gamma"}, "remaining EW channels mismatch")
    require(ew_gate["summary"]["all_remaining_rows_have_formula_or_import_route"] is True, "route gate incomplete")
    require(ew_gate["summary"]["all_formula_kernels_filled"] is False, "formula kernels overfilled")
    require(ew_gate["summary"]["all_rows_precision_accepted"] is False, "precision rows overaccepted")
    require(ten["summary"]["channel_count"] == 10, "ten-channel count mismatch")
    require(ten["summary"]["computed_or_proxy_row_count"] == 7, "computed/proxy count mismatch")
    require(ten["summary"]["external_fill_row_count"] == 3, "external fill count mismatch")
    require(ten["summary"]["all_channels_have_width_rows"] is True, "width row coverage missing")
    require(ten["summary"]["all_channels_have_formula_or_proxy_rows"] is False, "formula row overclaimed")
    require(total["precision_total_width_closed"] is False, "precision total width overclosed")
    require(total["branching_ratios_closed"] is False, "branching ratios overclosed")
    require(total["values_promotable_to_precision_now"] is False, "values overpromoted")
    require(data["closure_decision"]["remaining_EW_gate_built"] is True, "candidate gate closure missing")
    require(data["closure_decision"]["precision_total_width_closed"] is False, "candidate precision overclosed")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("only `H_to_WW_star`, `H_to_ZZ_star`, and" in note, "note missing remaining rows")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
