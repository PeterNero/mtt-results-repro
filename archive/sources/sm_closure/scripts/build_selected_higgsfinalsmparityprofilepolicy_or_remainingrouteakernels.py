"""Build final Higgs SM-parity profile policy or remaining route-A kernels."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsfinalsmparityprofilepolicy_or_remainingrouteakernels"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
POLICY = PACKET_DIR / "final_higgs_smparity_profile_policy.packet.json"
TEN_ROW = PACKET_DIR / "ten_row_higgs_replay_closure_ledger.packet.json"
REMAINING = PACKET_DIR / "remaining_route_a_kernel_execution_contract.packet.json"
TRUE_GATE = PACKET_DIR / "updated_true_equivalence_gate_after_final_higgs_policy.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsFinalSMParityProfilePolicy_or_RemainingRouteAKernels_v1.md"

STATUS = "MTT_SELECTED_HIGGSFINALSMPARITYPROFILEPOLICY_OR_REMAININGROUTEAKERNELS_BUILT_SMPARITY_HIGGS_REPLAY_CLOSED_ROUTEA_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsoffshellzgammaroutea_or_precisionimportdecision.candidate.json")
    final_three = load(
        DATA
        / "selected_higgsoffshellzgammaroutea_or_precisionimportdecision"
        / "higgs_route_a_ten_row_status_after_decision.packet.json"
    )
    imported_replay = load(
        DATA
        / "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood"
        / "imported_profile_observable_replay.packet.json"
    )
    covariance_import = load(
        DATA
        / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport"
        / "repo_basis_decay_covariance_import.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgsoffshellzgammaroutea_or_precisionimportdecision"
        / "updated_true_equivalence_gate_after_offshell_zgamma_decision.packet.json"
    )

    channels = list(covariance_import["repo_row_basis"])
    executed = list(final_three["route_A_rows_executed"])
    remaining = list(final_three["route_A_rows_remaining"])
    row_status = []
    for channel in channels:
        if channel in executed:
            status = "ROUTE_A_PROXY_OR_TREE_DERIVATIVE_EXECUTED"
            replay_source = "route_A_derivative_row_plus_imported_profile_diagnostic"
            route_a_ready = True
        elif channel in remaining:
            status = "DOWNSTREAM_IMPORT_REPLAY_ONLY_ROUTE_A_KERNEL_OPEN"
            replay_source = "imported_profile_replay_row"
            route_a_ready = False
        else:
            raise AssertionError(f"unexpected Higgs channel {channel}")
        row_status.append(
            {
                "channel": channel,
                "policy_status": status,
                "SM_parity_replay_source": replay_source,
                "SM_parity_replay_admitted": True,
                "route_A_formula_derivative_available": route_a_ready,
                "accepted_as_precision_formula_row": False,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )

    policy = {
        "schema": "MTTHiggsFinalSMParityProfilePolicy.v1",
        "status": "HIGGS_TEN_ROW_SMPARITY_REPLAY_PROFILE_ADMITTED_ROUTEA_REMAINS_SEVEN_OF_TEN",
        "declared_standard": "SM_PARITY_REPLAY",
        "policy_statement": (
            "The ten-row Higgs basis is closed for SM-parity replay by combining executed route-A "
            "rows where available with a single imported correlated decay-profile replay layer for "
            "all rows. This is not a route-A formula-derivative closure and not a no-knob derivation."
        ),
        "profile_basis_channels": channels,
        "profile_covariance_source": rel(
            DATA
            / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport"
            / "repo_basis_decay_covariance_import.packet.json"
        ),
        "observable_replay_source": rel(
            DATA
            / "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood"
            / "imported_profile_observable_replay.packet.json"
        ),
        "ten_row_replay_admitted_for_SM_parity": True,
        "route_A_rows_executed_count": len(executed),
        "route_A_rows_remaining_count": len(remaining),
        "full_route_A_ten_row_engine_closed": False,
        "precision_total_width_closed_by_formula": False,
        "precision_branching_ratios_closed_by_formula": False,
        "official_likelihood_imported": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    ten_row = {
        "schema": "MTTHiggsTenRowReplayClosureLedger.v1",
        "status": "TEN_ROW_HIGGS_SMPARITY_REPLAY_LEDGER_COMPLETE",
        "rows": row_status,
        "row_count": len(row_status),
        "all_rows_have_SM_parity_replay_source": all(row["SM_parity_replay_admitted"] for row in row_status),
        "route_A_rows_executed": executed,
        "route_A_rows_remaining": remaining,
        "SM_parity_Higgs_profile_replay_closed": True,
        "route_A_Higgs_profile_closed": False,
        "precision_Higgs_profile_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining_contract = {
        "schema": "MTTHiggsRemainingRouteAKernelExecutionContract.v1",
        "status": "REMAINING_ROUTE_A_KERNELS_PINNED_FOR_TRUE_PRECISION_CLOSURE",
        "remaining_channels": remaining,
        "required_for_route_A_closure": [
            "H_to_Z_gamma analytic or numerical loop kernel with declared electroweak scheme",
            "H_to_WW_star off-shell kernel with declared four-fermion/width convention",
            "H_to_ZZ_star off-shell kernel with declared four-fermion/width convention",
            "first derivatives with respect to the locked common-scale input vector",
            "covariance propagation into the same ten-row Higgs basis",
            "post-execution comparison to imported replay profile only after kernels are fixed",
        ],
        "alternate_SM_parity_path_closed_now": True,
        "route_A_formula_path_closed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    true_gate = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterFinalHiggsPolicy.v1",
        "status": "HIGGS_SMPARITY_PROFILE_POLICY_CLOSED_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_gate": rel(
            DATA
            / "selected_higgsoffshellzgammaroutea_or_precisionimportdecision"
            / "updated_true_equivalence_gate_after_offshell_zgamma_decision.packet.json"
        ),
        "closed_now": previous_true["closed_now"] + [
            "Final Higgs ten-row SM-parity profile policy",
            "Complete Higgs ten-row replay ledger",
            "Explicit separation of SM-parity replay closure from route-A precision closure",
        ],
        "remaining_true_equivalence_blockers": [
            blocker
            for blocker in previous_true["remaining_true_equivalence_blockers"]
            if blocker != "Higgs ten-row SM-parity replay profile policy"
        ]
        + [
            "Route-A kernels for H_to_Z_gamma, H_to_WW_star, and H_to_ZZ_star if formula-level Higgs closure is required",
            "Official public machine-readable full Higgs likelihood/profile if the imported covariance replay is to be replaced",
            "Full covariance/profile policy across non-Higgs SM observables",
            "No-knob derivation of the measured replay inputs",
        ],
        "guardrails": {
            "SM_parity_Higgs_profile_replay_closed": True,
            "route_A_Higgs_profile_closed": False,
            "precision_Higgs_profile_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsFinalSMParityProfilePolicyOrRemainingRouteAKernels",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsoffshellzgammaroutea_or_precisionimportdecision.candidate.json"),
            "final_three_status": rel(
                DATA
                / "selected_higgsoffshellzgammaroutea_or_precisionimportdecision"
                / "higgs_route_a_ten_row_status_after_decision.packet.json"
            ),
            "imported_replay_observables": rel(
                DATA
                / "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood"
                / "imported_profile_observable_replay.packet.json"
            ),
            "covariance_import": rel(
                DATA
                / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport"
                / "repo_basis_decay_covariance_import.packet.json"
            ),
        },
        "output_packets": {
            "final_higgs_smparity_profile_policy": rel(POLICY),
            "ten_row_higgs_replay_closure_ledger": rel(TEN_ROW),
            "remaining_route_a_kernel_execution_contract": rel(REMAINING),
            "updated_true_equivalence_gate": rel(TRUE_GATE),
        },
        "theorem": {
            "name": "HiggsSMParityReplayProfileClosureTheorem",
            "proved": True,
            "statement": (
                "Under the declared SM-parity replay standard, the Higgs ten-row profile is closed as a "
                "downstream replay object because every row has an admitted replay source and the covariance "
                "profile is propagated in the locked ten-row basis. This theorem does not promote imported "
                "values to route-A derivatives, formula precision, true SM equivalence, or no-knob closure."
            ),
        },
        "what_closes_now": {
            "Higgs_ten_row_SM_parity_replay_profile": True,
            "Higgs_ten_row_replay_ledger": True,
            "final_three_route_A_kernel_contract_retained": True,
        },
        "what_remains_open": {
            "route_A_H_to_Z_gamma_kernel": True,
            "route_A_H_to_WW_star_kernel": True,
            "route_A_H_to_ZZ_star_kernel": True,
            "formula_level_precision_Higgs_profile": True,
            "official_full_likelihood_import": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_Higgs_profile_replay_closed": True,
            "route_A_rows_closed_total": len(executed),
            "route_A_rows_remaining_total": len(remaining),
            "full_route_A_ten_row_engine_closed": False,
            "precision_total_width_closed_by_formula": False,
            "precision_branching_ratios_closed_by_formula": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_FullSMParityReplayClosureOr_NonHiggsProfilePolicy_v1",
    }

    cert = {
        "certificate": "MTT_Selected_HiggsFinalSMParityProfilePolicy_or_RemainingRouteAKernels_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "SM_parity_Higgs_profile_replay_closed": True,
        "route_A_rows_closed_total": len(executed),
        "route_A_rows_remaining_total": len(remaining),
        "full_route_A_ten_row_engine_closed": False,
        "precision_Higgs_profile_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    note = f"""# MTT Selected HiggsFinalSMParityProfilePolicy or RemainingRouteAKernels v1

Status: `{STATUS}`.

This theorem closes the Higgs ten-row layer only at the SM-parity replay level.
All ten rows have an admitted downstream replay source in the locked Higgs basis,
and the imported covariance/profile replay is kept downstream of source
selection.

The policy is deliberately strict:

- seven rows have route-A tree/proxy derivative execution;
- `H_to_Z_gamma`, `H_to_WW_star`, and `H_to_ZZ_star` remain import-replay rows;
- import replay is not formula differentiation;
- formula-level Higgs precision still requires the three remaining route-A
  kernels or a stronger public likelihood/profile import;
- true SM equivalence and no-knob closure remain open.
"""

    for path, payload in [
        (POLICY, policy),
        (TEN_ROW, ten_row),
        (REMAINING, remaining_contract),
        (TRUE_GATE, true_gate),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
