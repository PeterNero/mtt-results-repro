"""Audit Higgs QCD formula-repair gate / QaSU3 parity attachment bridge."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsqcdformularepairvalues_or_qasu3operatorattachment"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FORMULA_GATE = PACKET_DIR / "higgs_qcd_formula_repair_value_gate.packet.json"
QASU3_ATTACHMENT = PACKET_DIR / "higgs_qcd_qasu3_parity_attachment.packet.json"
UPDATED_REPAIR = PACKET_DIR / "updated_higgs_qcd_repair_gate_after_qasu3_parity_attachment.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsQCDFormulaRepairValues_or_QaSU3OperatorAttachment_v1.md"

STATUS = "MTT_SELECTED_HIGGSQCDFORMULAREPAIRVALUES_OR_QASU3OPERATORATTACHMENT_BUILT_PARITY_ATTACHMENT_FORMULA_VALUES_OPEN"
NEXT = "MTT_Selected_HiggsQCDNonFitFormulaValueExecution_or_ForwardReplay_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    formula = load(FORMULA_GATE)
    attachment = load(QASU3_ATTACHMENT)
    updated = load(UPDATED_REPAIR)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["target_fitting_used"] is False, "target fitting guard missing")
    require(data["observed_data_used_as_selector"] is False, "observed selector guard missing")
    require(formula["channels"] == ["H_to_ss", "H_to_gg"], "formula channels mismatch")
    require(formula["accepted_formula_repair_values_count"] == 0, "formula values overfilled")
    require(formula["formula_repair_values_filled"] is False, "formula values filled too early")
    require(formula["formula_repair_values_promotable"] is False, "formula values overpromoted")
    require(formula["forward_replay_required_before_benchmark_comparison"] is True, "forward replay guard missing")
    require(
        formula["forbidden_fit_factor_policy"]["benchmark_over_proxy_ratios_may_be_applied"] is False,
        "fit factors allowed",
    )
    require(attachment["accepted_for_higgs_qcd_sm_parity_operator_attachment"] is True, "attachment not accepted")
    require(attachment["accepted_as_actual_selected_qasu3_operator_packet"] is False, "actual Qa/SU3 overclaimed")
    require(attachment["accepted_for_true_precision_qcd_formula_values"] is False, "precision overclaimed")
    require(attachment["accepted_for_no_knob_qasu3"] is False, "no-knob overclaimed")
    require(attachment["guardrails"]["actual_operator_packet_claimed"] is False, "operator packet overclaimed")
    require(attachment["superset_strategy"]["paths_combined_as_knobs"] is False, "superset knobs overclaimed")
    require(updated["selected_QaSU3_operator_attachment_closed_for_sm_parity"] is True, "SM-parity attachment not closed")
    require(updated["selected_QaSU3_operator_attachment_closed_as_no_knob"] is False, "no-knob attachment overclaimed")
    require(updated["repair_values_filled"] is False, "repair values overfilled")
    require(updated["values_promotable_now"] is False, "values overpromoted")
    require(data["closure_decision"]["higgs_qcd_qasu3_attachment_closed_for_sm_parity_interface"] is True, "closure missing")
    require(data["closure_decision"]["formula_repair_values_filled"] is False, "candidate formulas overfilled")
    require(data["closure_decision"]["actual_QaSU3_operator_packet_no_knob_closed"] is False, "candidate Qa/SU3 overclosed")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("not an actual selected no-knob Qa/SU3" in note, "note missing no-knob guard")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
