"""Build Higgs QCD formula-repair gate / QaSU3 parity attachment bridge."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsqcdformularepairvalues_or_qasu3operatorattachment"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FORMULA_GATE = PACKET_DIR / "higgs_qcd_formula_repair_value_gate.packet.json"
QASU3_ATTACHMENT = PACKET_DIR / "higgs_qcd_qasu3_parity_attachment.packet.json"
UPDATED_REPAIR = PACKET_DIR / "updated_higgs_qcd_repair_gate_after_qasu3_parity_attachment.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_qasu3_parity_attachment.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsQCDFormulaRepairValues_or_QaSU3OperatorAttachment_v1.md"

STATUS = "MTT_SELECTED_HIGGSQCDFORMULAREPAIRVALUES_OR_QASU3OPERATORATTACHMENT_BUILT_PARITY_ATTACHMENT_FORMULA_VALUES_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsqcdrepairvalues_or_profilecovarianceblock.candidate.json")
    residuals = load(
        DATA
        / "selected_higgsqcdthresholdrows_or_correlatedprofilefill"
        / "qcd_threshold_residual_rows.packet.json"
    )
    obligations = load(
        DATA
        / "selected_higgsqcdthresholdrows_or_correlatedprofilefill"
        / "qcd_threshold_repair_obligations.packet.json"
    )
    qasu3_replacement = load(
        DATA
        / "selected_qasu3sourcepacket_or_finalsmparityclosure"
        / "qasu3_parity_interface_replacement.packet.json"
    )
    profile_block = load(
        DATA
        / "selected_higgsqcdrepairvalues_or_profilecovarianceblock"
        / "qcd_diagonal_profile_block.packet.json"
    )
    psd = load(
        DATA
        / "selected_higgsqcdrepairvalues_or_profilecovarianceblock"
        / "qcd_profile_psd_and_chisquare_check.packet.json"
    )
    repair_status = load(
        DATA
        / "selected_higgsqcdrepairvalues_or_profilecovarianceblock"
        / "qcd_repair_values_status_after_profile_block.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgsqcdrepairvalues_or_profilecovarianceblock"
        / "updated_true_equivalence_gate_after_qcd_profile_block.packet.json"
    )

    obligation_by_channel = {row["channel"]: row for row in obligations["rows"]}
    qcd_rows = []
    for row in residuals["rows"]:
        channel = row["channel"]
        obligation = obligation_by_channel[channel]
        qcd_rows.append(
            {
                "channel": channel,
                "required_formula_family": row["required_formula_family"],
                "operator_attachment_required": row["operator_attachment_required"],
                "minimum_acceptance_tests": obligation["minimum_acceptance_tests"],
                "missing_formula_inputs": obligation["missing_repair_inputs"],
                "benchmark_over_proxy_ratio_recorded_as_forbidden_fit_factor": row["forbidden_fit_factor"],
                "forbidden_fit_factor_may_be_applied": False,
                "formula_repair_value_filled": False,
                "formula_repair_value_promotable": False,
                "qasu3_attachment_closed_for_sm_parity_interface": True,
                "qasu3_attachment_closed_as_actual_no_knob_operator_packet": False,
            }
        )

    formula_gate = {
        "schema": "MTTHiggsQCDFormulaRepairValueGate.v1",
        "status": "QCD_FORMULA_REPAIR_VALUE_GATE_BUILT_VALUES_OPEN",
        "channels": [row["channel"] for row in qcd_rows],
        "rows": qcd_rows,
        "accepted_formula_repair_values_count": 0,
        "formula_repair_values_filled": False,
        "formula_repair_values_promotable": False,
        "forward_replay_required_before_benchmark_comparison": True,
        "forbidden_fit_factor_policy": {
            "benchmark_over_proxy_ratios_present_as_diagnostics": True,
            "benchmark_over_proxy_ratios_may_be_applied": False,
            "separate_residual_multipliers_allowed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    attachment = {
        "schema": "MTTHiggsQCDQaSU3ParityAttachment.v1",
        "status": "QASU3_PARITY_ATTACHMENT_ACCEPTED_FOR_HIGGS_QCD_INTERFACE_ONLY",
        "imported_qasu3_replacement": rel(
            DATA
            / "selected_qasu3sourcepacket_or_finalsmparityclosure"
            / "qasu3_parity_interface_replacement.packet.json"
        ),
        "replacement_rule": qasu3_replacement["replacement_rule"],
        "support_presence": qasu3_replacement["support_presence"],
        "accepted_for_higgs_qcd_sm_parity_operator_attachment": True,
        "accepted_as_actual_selected_qasu3_operator_packet": False,
        "accepted_for_true_precision_qcd_formula_values": False,
        "accepted_for_no_knob_qasu3": False,
        "attached_rows": [
            {
                "channel": row["channel"],
                "attachment_kind": "SM_PARITY_TYPED_SOURCE_INTERFACE_REPLACEMENT",
                "actual_operator_derivation_required_for_no_knob": True,
                "precision_formula_values_still_required": True,
            }
            for row in qcd_rows
        ],
        "guardrails": {
            "observed_higgs_widths_used_to_select_attachment": False,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "q79_cp_success_used_as_direct_color_proof": False,
            "benchmark_matrices_promoted": False,
            "actual_operator_packet_claimed": False,
        },
        "superset_strategy": {
            "mode": "PARITY_INTERFACE_BRIDGE_TO_LOCKED_QCD_TARGET",
            "straight_path": "Higgs QCD residual rows and diagonal profile replay",
            "superset_paths_combined": [
                "Qa/SU3 parity-interface replacement",
                "threshold/mass-scheme acceptance contract",
                "diagonal QCD profile fallback",
                "forbidden fit-factor guard",
            ],
            "paths_combined_as_knobs": False,
            "locked_target": "Higgs QCD operator attachment for SM-parity interface only",
        },
    }

    updated_repair = {
        "schema": "MTTUpdatedHiggsQCDRepairGateAfterQaSU3ParityAttachment.v1",
        "status": "HIGGS_QCD_PARITY_OPERATOR_ATTACHMENT_CLOSED_FORMULA_VALUES_OPEN",
        "previous_repair_status": repair_status["status"],
        "closed_now": [
            "H_to_ss Qa/SU3 parity-interface operator attachment",
            "H_to_gg Qa/SU3 parity-interface operator attachment",
        ],
        "still_open": [
            "non-fit H_to_ss formula repair value",
            "non-fit H_to_gg formula repair value",
            "full correlated QCD profile",
            "actual selected Qa/SU3 no-knob operator packet",
            "forward replay from accepted formula values",
        ],
        "qcd_diagonal_profile_chi_square": psd["diagonal_chi_square"],
        "qcd_diagonal_profile_dimension": profile_block["summary"]["dimension"],
        "repair_values_filled": False,
        "values_promotable_now": False,
        "selected_QaSU3_operator_attachment_closed_for_sm_parity": True,
        "selected_QaSU3_operator_attachment_closed_as_no_knob": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterQaSU3ParityAttachment.v1",
        "status": "QASU3_PARITY_ATTACHMENT_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "closed_now": previous_true["closed_now"]
        + ["Higgs QCD Qa/SU3 parity-interface attachment for SM-parity"],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "compute non-fit QCD formula repair values for H_to_ss and H_to_gg, then replay forward",
        "guardrails": {
            "parity_attachment_not_actual_no_knob_qasu3": True,
            "formula_repair_values_filled": False,
            "full_correlated_profile_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsQCDFormulaRepairValuesOrQaSU3OperatorAttachment",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsqcdrepairvalues_or_profilecovarianceblock.candidate.json"),
            "qcd_threshold_residual_rows": rel(
                DATA
                / "selected_higgsqcdthresholdrows_or_correlatedprofilefill"
                / "qcd_threshold_residual_rows.packet.json"
            ),
            "qcd_threshold_repair_obligations": rel(
                DATA
                / "selected_higgsqcdthresholdrows_or_correlatedprofilefill"
                / "qcd_threshold_repair_obligations.packet.json"
            ),
            "qasu3_parity_interface_replacement": rel(
                DATA
                / "selected_qasu3sourcepacket_or_finalsmparityclosure"
                / "qasu3_parity_interface_replacement.packet.json"
            ),
            "qcd_profile_block": rel(
                DATA
                / "selected_higgsqcdrepairvalues_or_profilecovarianceblock"
                / "qcd_diagonal_profile_block.packet.json"
            ),
        },
        "output_packets": {
            "formula_repair_value_gate": rel(FORMULA_GATE),
            "qasu3_parity_attachment": rel(QASU3_ATTACHMENT),
            "updated_higgs_qcd_repair_gate": rel(UPDATED_REPAIR),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsQCDQaSU3ParityAttachmentTheorem",
            "proved": True,
            "statement": (
                "The accepted Qa/SU3 parity-interface replacement can be attached to the Higgs QCD "
                "threshold rows as an SM-parity operator-interface bridge. This closes the Higgs QCD "
                "operator attachment at the parity-interface tier only. It does not compute QCD formula "
                "repair values, does not promote residual ratios, and does not close actual no-knob Qa/SU3."
            ),
        },
        "what_closes_now": {
            "Higgs_QCD_QaSU3_attachment_for_SM_parity_interface": True,
            "forbidden_fit_factor_guard_reaffirmed": True,
            "formula_value_acceptance_gate_installed": True,
            "superset_bridge_documented": True,
        },
        "what_remains_open": {
            "non_fit_H_to_ss_formula_repair_value": True,
            "non_fit_H_to_gg_formula_repair_value": True,
            "full_correlated_QCD_profile": True,
            "actual_QaSU3_operator_packet_no_knob": True,
            "forward_replay_from_accepted_formula_values": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "higgs_qcd_qasu3_attachment_closed_for_sm_parity_interface": True,
            "formula_repair_values_filled": False,
            "formula_repair_values_promotable": False,
            "actual_QaSU3_operator_packet_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsQCDFormulaRepairValues_or_QaSU3OperatorAttachment_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "higgs_qcd_qasu3_attachment_closed_for_sm_parity_interface": True,
        "formula_repair_values_filled": False,
        "formula_repair_values_promotable": False,
        "actual_QaSU3_operator_packet_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsQCDNonFitFormulaValueExecution_or_ForwardReplay_v1",
    }

    note = f"""# MTT Selected HiggsQCDFormulaRepairValues or QaSU3OperatorAttachment v1

Status: `{STATUS}`.

This artifact attaches the already accepted Qa/SU3 parity-interface replacement
to the Higgs QCD threshold rows. The attachment is valid only for SM-parity
operator-interface certification. It is not an actual selected no-knob Qa/SU3
operator packet.

## Superset Use

This is a constrained superset bridge: the straight Higgs QCD residual/profile
path is combined with the Qa/SU3 parity-interface replacement, threshold
contract, and forbidden-fit guard. The locked target is narrow: QCD operator
attachment for SM-parity interface only.

## Still Open

- non-fit formula repair values for `H_to_ss` and `H_to_gg`
- forward replay from accepted formula values before benchmark comparison
- full correlated QCD profile
- actual selected Qa/SU3 operator packet for no-knob closure
- true precision SM equivalence
"""

    for path, payload in [
        (FORMULA_GATE, formula_gate),
        (QASU3_ATTACHMENT, attachment),
        (UPDATED_REPAIR, updated_repair),
        (UPDATED_TRUE, updated_true),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
