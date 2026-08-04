"""Audit the q79 same-source operator-packet fill/no-go theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP_SCRIPT = ROOT / "scripts" / "analyze_q79_selected_matter_slot_charge_and_overlap_normalization_theorem.py"
SCRIPT = ROOT / "scripts" / "analyze_q79_samesource_operatorpacket_fill_or_nogo.py"
CERT = ROOT / "certificates" / "q79_samesource_operatorpacket_fill_or_nogo_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_samesource_operatorpacket_fill_or_nogo.candidate.json"
TABLE = ROOT / "candidate_data" / "q79_samesource_operatorpacket_fill_or_nogo" / "field_validation_table.json"
PAPER = ROOT / "proof_corpus" / "Q79_Selected_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1.md"

STATUS = "Q79_SAMESOURCE_OPERATORPACKET_FILL_ATTEMPT_NOGO_CURRENT_SCAFFOLDS_SUPPORT_ONLY"
NEXT = "Q79_Selected_RouteC_Stability_HYM_or_RouteC_Residual_Source_v1"

EXPECTED_SM = {
    "fill_or_nogo_candidate": "MTT_SELECTED_ROUTEC_SAMESOURCE_OPERATORPACKET_FILL_ATTEMPT_NOGO_CURRENT_SCAFFOLDS_SUPPORT_ONLY",
    "minimal_subpacket_plan_candidate": "MTT_SELECTED_ROUTEC_SOURCEEMISSION_MINIMAL_SUBPACKET_ATTACK_PLAN_BUILT",
    "operator_source_identity_candidate": "MTT_SELECTED_ROUTEC_OPERATOR_SOURCE_IDENTITY_SUBPACKET_REDUCED_TO_RANK2_OR_ROUTEC_FILL_VALUES_OPEN",
    "rank2_l2_or_routec_residual_candidate": "MTT_SELECTED_ROUTEC_RANK2_L2_COHOMOLOGY_FILL_CLOSED_STABILITY_OR_ROUTEC_RESIDUAL_OPEN",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def run(script: Path, failures: list[str]) -> None:
    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    require(proc.returncode == 0, f"{script.name} failed:\n{proc.stdout}", failures)


def main() -> int:
    failures: list[str] = []
    run(DEP_SCRIPT, failures)
    run(SCRIPT, failures)
    for path in (CERT, CANDIDATE, TABLE, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)
    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    table = load(TABLE)
    paper = PAPER.read_text(encoding="utf-8")

    require(cert == candidate, "certificate and candidate JSON differ", failures)
    require(table == cert["fill_or_nogo_result"]["field_table"], "field table mismatch", failures)
    require(cert["status"] == STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure must stay false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)

    for name, expected in EXPECTED_SM.items():
        require(
            cert["sm_input_statuses"][name]["status"] == expected,
            f"unexpected SM status for {name}: {cert['sm_input_statuses'][name]['status']}",
            failures,
        )

    fill = cert["fill_or_nogo_result"]
    summary = fill["fill_summary"]
    fields = fill["field_table"]["rows"]
    validator = fill["validator_report"]
    flags = fill["packet_flags"]
    decision = cert["q79_decision"]
    frontier = cert["downstream_frontier_import"]
    rank2 = frontier["rank2_l2_checkpoint"]
    remaining = cert["what_remains_open"]

    require(summary["required_fields"] == 7, "expected seven required fields", failures)
    require(summary["support_present"] == 6, "expected six support fields", failures)
    require(summary["selected_emitted"] == 0, "expected zero selected emissions", failures)
    require(summary["nogo_for_current_scaffolds"] is True, "no-go flag missing", failures)
    require(fill["field_table"]["same_source_emitted"] == 0, "same-source emission overclaim", failures)
    require(fill["field_table"]["theorem_derived"] == 0, "theorem-derived emission overclaim", failures)
    require(all(row["selected_emitted"] is False for row in fields.values()), "field selected unexpectedly", failures)
    require(fields["singlet_neutrino_rule"]["support_present"] is False, "singlet support should be absent", failures)
    require(fields["overlap_transfer"]["provenance"] == "locked_target_selection", "overlap provenance changed", failures)
    require(fields["normalization"]["provenance"] == "locked_target_selection", "normalization provenance changed", failures)

    require(validator["exit_code"] == 1 and validator["ok"] is False, "validator should reject", failures)
    require(validator["error_count"] >= 7, "validator errors too small", failures)
    require(flags["one_same_source"] is False, "one_same_source overclaim", failures)
    require(flags["promote_to_A_selected"] is False, "A_selected overclaim", failures)
    require(flags["promote_to_b_selected"] is False, "b_selected overclaim", failures)

    require(decision["validator_rejects_current_scaffold"] is True, "validator decision missing", failures)
    require(decision["same_source_packet_values_emitted"] is False, "values emitted overclaim", failures)
    require(decision["promote_conditional_A_to_A_selected"] is False, "A promotion overclaim", failures)
    require(decision["emit_b_selected"] is False, "b emission overclaim", failures)

    require(
        frontier["minimal_attack_plan"]["next_required_artifact"]
        == "MTT_Selected_RouteC_OperatorSourceIdentity_Subpacket_v1",
        "wrong imported attack-plan next",
        failures,
    )
    require(
        frontier["operator_source_identity_subpacket"]["operator_identity_closed"] is False
        and frontier["operator_source_identity_subpacket"]["rank2_or_routec_fill_required"] is True,
        "operator identity overclosed",
        failures,
    )
    require(rank2["rank2_l2_validator_exit_code"] == 0, "rank2 L2 validator not closed", failures)
    require(rank2["ordered_source_validator_exit_code"] == 0, "ordered-source validator not closed", failures)
    require(rank2["h1"] == 8, "rank2 h1 changed", failures)
    require(rank2["nonzero_ext_class_selected"] is True, "nonzero Ext not selected", failures)
    require(rank2["selected_operator_identity_closed"] is False, "operator identity closed unexpectedly", failures)
    require(
        rank2["next_required_artifact"] == "MTT_Selected_RouteC_Stability_HYM_or_RouteC_Residual_Source_v1",
        "wrong imported rank2 next",
        failures,
    )

    for key in (
        "non_split_stability_or_hym_proved",
        "selected_route_c_residual_pass",
        "operator_layer_pic0_recheck",
        "same_source_D_E_rhoE_Riesz_Green_dotD",
        "primitive_C1_contractions",
        "full_SM_or_no_knob_closure",
    ):
        require(remaining[key] is True, f"open flag false: {key}", failures)

    for key, value in cert["guardrails"].items():
        require(value is False, f"guardrail violated: {key}", failures)
    require(cert["theorem"]["proved"] is True, "theorem must be proved", failures)
    require(cert["theorem"]["closure_claimed"] is False, "theorem closure must stay false", failures)

    for phrase in (
        "validator-backed no-go",
        "zero selected-emitted fields",
        "not `A_selected`",
        "rank-two L2 checkpoint",
        "nonzero Ext class selected",
        "Q79SelectedRouteCSameSourceOperatorPacketFillOrNoGoTheorem",
        NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 same-source operator-packet fill/no-go audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 same-source operator-packet fill/no-go audit PASS")
    print(f"status: {cert['status']}")
    print(f"field counts: {summary}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
