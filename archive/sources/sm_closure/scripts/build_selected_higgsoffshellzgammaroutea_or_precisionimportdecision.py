"""Build Higgs off-shell/Zgamma route-A or precision import decision."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsoffshellzgammaroutea_or_precisionimportdecision"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DECISION = PACKET_DIR / "offshell_zgamma_route_a_vs_import_decision.packet.json"
IMPORT_REPLAY = PACKET_DIR / "offshell_zgamma_import_replay_status.packet.json"
REMAINING = PACKET_DIR / "remaining_three_route_a_kernel_contract.packet.json"
FINAL_STATUS = PACKET_DIR / "higgs_route_a_ten_row_status_after_decision.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_offshell_zgamma_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsOffshellZGammaRouteA_or_PrecisionImportDecision_v1.md"

STATUS = "MTT_SELECTED_HIGGSOFFSHELLZGAMMAROUTEA_OR_PRECISIONIMPORTDECISION_BUILT_REMAINING_THREE_IMPORT_REPLAY_ROUTEA_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsloopoffshellrouteaderivativerows_or_precisiondecision.candidate.json")
    readiness = load(
        DATA
        / "selected_higgsewformulakernelexecution_or_precisionimportrows"
        / "ew_formula_kernel_execution_readiness.packet.json"
    )
    import_contract = load(
        DATA
        / "selected_higgsewformulakernelexecution_or_precisionimportrows"
        / "ew_precision_import_row_contract.packet.json"
    )
    imported_profile = load(
        DATA
        / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport"
        / "repo_basis_decay_covariance_import.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgsloopoffshellrouteaderivativerows_or_precisiondecision"
        / "updated_true_equivalence_gate_after_loop_offshell_rows.packet.json"
    )

    open_basis = ["H_to_Z_gamma", "H_to_WW_star", "H_to_ZZ_star"]
    readiness_by_channel = {row["channel"]: row for row in readiness["rows"]}
    import_by_channel = {row["channel"]: row for row in import_contract["rows"]}

    decision_rows = []
    replay_rows = []
    remaining_rows = []
    for channel in open_basis:
        ready = readiness_by_channel[channel]
        imported = import_by_channel[channel]
        profile_width = imported_profile["central_widths_GeV"][channel]
        profile_sigma = imported_profile["relative_uncertainties"][channel] * profile_width
        current_external = float(imported["current_external_width_GeV"])
        decision_rows.append(
            {
                "channel": channel,
                "route_A_kernel_executable_now": ready["formula_kernel_executable_now"],
                "route_A_kernel_filled": ready["formula_kernel_filled"],
                "precision_import_available_as_replay_input": imported["external_value_replayed"],
                "precision_import_accepted_as_formula_derivative": False,
                "decision": "KEEP_IMPORT_FOR_SM_PARITY_REPLAY_AND_KEEP_ROUTE_A_KERNEL_OPEN",
                "reason": (
                    "The row has replay/import central data but no executable route-A formula kernel. "
                    "Import identity cannot count as formula differentiation."
                ),
            }
        )
        replay_rows.append(
            {
                "channel": channel,
                "current_external_width_GeV": current_external,
                "published_profile_width_GeV": profile_width,
                "published_profile_sigma_GeV": profile_sigma,
                "delta_external_minus_profile_GeV": current_external - profile_width,
                "relative_delta_external_minus_profile": (current_external - profile_width) / profile_width,
                "accepted_as_SM_parity_downstream_replay_value": True,
                "accepted_as_precision_total_width_row": False,
                "accepted_as_route_A_formula_value": False,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )
        remaining_rows.append(
            {
                "channel": channel,
                "formula_family": ready["formula_family"],
                "minimum_kernel_inputs": ready["minimum_kernel_inputs"],
                "operator_attachment_required": ready["operator_attachment_required"],
                "required_next_for_route_A_closure": [
                    "executable analytic or numerical formula kernel",
                    "declared electroweak input and mass scheme",
                    "derivatives with respect to declared inputs",
                    "covariance propagation into ten-row Higgs basis",
                    "comparison to imported profile after execution only",
                ],
            }
        )

    decision = {
        "schema": "MTTHiggsOffshellZGammaRouteAImportDecision.v1",
        "status": "REMAINING_THREE_ROWS_IMPORT_REPLAY_ALLOWED_ROUTE_A_KERNELS_OPEN",
        "rows": decision_rows,
        "route_A_rows_closed_total": previous["closure_decision"]["route_A_rows_closed_total_including_previous"],
        "route_A_rows_remaining": open_basis,
        "import_replay_allowed_for_SM_parity": True,
        "import_replay_counts_as_route_A_derivative": False,
        "full_route_A_ten_row_engine_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    import_replay = {
        "schema": "MTTHiggsOffshellZGammaImportReplayStatus.v1",
        "status": "REMAINING_THREE_EXTERNAL_ROWS_REPLAYED_BUT_NOT_PROMOTED",
        "rows": replay_rows,
        "accepted_as_SM_parity_downstream_replay_layer": True,
        "accepted_as_precision_profile_closure": False,
        "accepted_as_route_A_derivative_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = {
        "schema": "MTTHiggsRemainingThreeRouteAKernelContract.v1",
        "status": "REMAINING_THREE_ROUTE_A_KERNEL_CONTRACT_BUILT",
        "rows": remaining_rows,
        "row_count": len(remaining_rows),
        "route_A_kernel_contract_complete": True,
        "route_A_kernel_values_filled": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    final_status = {
        "schema": "MTTHiggsRouteATenRowStatusAfterDecision.v1",
        "status": "SEVEN_OF_TEN_ROUTE_A_ROWS_EXECUTED_THREE_IMPORT_REPLAY_ROWS_OPEN",
        "route_A_rows_executed": [
            "H_to_tau_tau",
            "H_to_mu_mu",
            "H_to_bb",
            "H_to_cc",
            "H_to_ss",
            "H_to_gg",
            "H_to_gamma_gamma",
        ],
        "route_A_rows_remaining": open_basis,
        "route_A_rows_executed_count": 7,
        "route_A_rows_remaining_count": 3,
        "SM_parity_import_replay_available_for_remaining_three": True,
        "full_route_A_ten_row_engine_closed": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterOffshellZGammaDecision.v1",
        "status": "REMAINING_THREE_IMPORT_REPLAY_DECISION_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_gate": rel(
            DATA
            / "selected_higgsloopoffshellrouteaderivativerows_or_precisiondecision"
            / "updated_true_equivalence_gate_after_loop_offshell_rows.packet.json"
        ),
        "closed_now": previous_true["closed_now"] + [
            "Remaining three Higgs row route-A/import decision",
            "SM-parity import replay status for H_to_Z_gamma, H_to_WW_star, H_to_ZZ_star",
            "Route-A kernel contract for the remaining three rows",
            "Seven-of-ten route-A Higgs status after decision",
        ],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "construct executable route-A kernels for Zgamma/WW*/ZZ* or declare final SM-parity Higgs import profile policy",
        "guardrails": {
            "remaining_three_import_replay_built": True,
            "remaining_three_route_A_kernels_open": True,
            "full_route_A_ten_row_engine_closed": False,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsOffshellZGammaRouteAOrPrecisionImportDecision",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsloopoffshellrouteaderivativerows_or_precisiondecision.candidate.json"),
            "ew_formula_kernel_readiness": rel(
                DATA
                / "selected_higgsewformulakernelexecution_or_precisionimportrows"
                / "ew_formula_kernel_execution_readiness.packet.json"
            ),
            "ew_precision_import_row_contract": rel(
                DATA
                / "selected_higgsewformulakernelexecution_or_precisionimportrows"
                / "ew_precision_import_row_contract.packet.json"
            ),
            "imported_profile": rel(
                DATA
                / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport"
                / "repo_basis_decay_covariance_import.packet.json"
            ),
        },
        "output_packets": {
            "offshell_zgamma_route_a_vs_import_decision": rel(DECISION),
            "offshell_zgamma_import_replay_status": rel(IMPORT_REPLAY),
            "remaining_three_route_a_kernel_contract": rel(REMAINING),
            "higgs_route_a_ten_row_status_after_decision": rel(FINAL_STATUS),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsOffshellZGammaImportReplayDecisionTheorem",
            "proved": True,
            "statement": (
                "For H_to_Z_gamma, H_to_WW_star, and H_to_ZZ_star, the repo has downstream import/replay rows "
                "but no executable route-A formula kernels. Therefore these rows may be retained as SM-parity "
                "replay inputs, while route-A ten-row derivative closure remains open at seven of ten rows."
            ),
        },
        "what_closes_now": {
            "remaining_three_import_vs_route_A_decision": True,
            "SM_parity_import_replay_status_for_remaining_three": True,
            "remaining_three_route_A_kernel_contract": True,
            "seven_of_ten_route_A_status": True,
        },
        "what_remains_open": {
            "route_A_H_to_Z_gamma_kernel": True,
            "route_A_H_to_WW_star_kernel": True,
            "route_A_H_to_ZZ_star_kernel": True,
            "precision_total_width": True,
            "precision_branching_ratios": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "remaining_three_import_replay_accepted_for_SM_parity": True,
            "remaining_three_import_replay_accepted_as_route_A": False,
            "route_A_rows_closed_total": 7,
            "full_route_A_ten_row_engine_closed": False,
            "accepted_as_full_Higgs_precision": False,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsFinalSMParityProfilePolicy_or_RemainingRouteAKernels_v1",
    }

    cert = {
        "certificate": "MTT_Selected_HiggsOffshellZGammaRouteA_or_PrecisionImportDecision_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "remaining_three_import_replay_accepted_for_SM_parity": True,
        "remaining_three_import_replay_accepted_as_route_A": False,
        "route_A_rows_closed_total": 7,
        "full_route_A_ten_row_engine_closed": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    note = f"""# MTT Selected HiggsOffshellZGammaRouteA or PrecisionImportDecision v1

Status: `{STATUS}`.

This artifact handles the last three Higgs rows: `H_to_Z_gamma`, `H_to_WW_star`,
and `H_to_ZZ_star`.

The decision is explicit:

- their external/import rows may be used as downstream SM-parity replay inputs;
- imported central values do not count as route-A formula derivatives;
- route-A ten-row derivative closure remains open at seven of ten rows;
- the remaining three rows need executable kernels or a final Higgs import-profile
  policy.

No observed value is used to select source structure.
"""

    for path, payload in [
        (DECISION, decision),
        (IMPORT_REPLAY, import_replay),
        (REMAINING, remaining),
        (FINAL_STATUS, final_status),
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
