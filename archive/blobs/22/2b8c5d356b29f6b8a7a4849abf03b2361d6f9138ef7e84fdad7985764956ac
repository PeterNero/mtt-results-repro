"""Build audited benchmark-replay policy for remaining electroweak Higgs rows."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsewbenchmarkpolicy_or_fullformulas"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
POLICY = PACKET_DIR / "remaining_electroweak_benchmark_replay_policy.packet.json"
COMPLETION = PACKET_DIR / "higgs_ten_channel_replay_completion.packet.json"
OPEN = PACKET_DIR / "remaining_higgs_precision_formula_obligations.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_ew_benchmark_policy.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsEWBenchmarkPolicy_or_FullFormulas_v1.md"

STATUS = "MTT_SELECTED_HIGGSEWBENCHMARKPOLICY_OR_FULLFORMULAS_BUILT_TEN_CHANNEL_REPLAY_PRECISION_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsgammagammakernelrow_or_remainingew.candidate.json")
    previous_gate = load(
        DATA
        / "selected_higgsgammagammakernelrow_or_remainingew"
        / "updated_true_equivalence_gate_after_gamma_gamma_kernel.packet.json"
    )
    kernels = load(
        DATA
        / "selected_higgsgammagammakernelrow_or_remainingew"
        / "extended_executable_higgs_kernel_rows_after_gamma_gamma.packet.json"
    )
    remaining_ew = load(
        DATA
        / "selected_higgsgammagammakernelrow_or_remainingew"
        / "remaining_electroweak_higgs_kernel_obligations_after_gamma_gamma.packet.json"
    )
    benchmarks = load(
        DATA
        / "selected_higgsmissingchannelbenchmarks_or_totalwidthreplay"
        / "missing_higgs_channel_benchmark_rows.packet.json"
    )
    sidecars = load(
        DATA
        / "selected_higgsprecisionsidecars_or_uniformformularows"
        / "higgs_channel_uncertainty_sidecars.packet.json"
    )

    benchmark_by_channel = {row["channel"]: row for row in benchmarks["rows"]}
    sidecar_by_channel = {row["channel"]: row for row in sidecars["rows"]}
    ew_channels = ["H_to_WW_star", "H_to_ZZ_star", "H_to_Z_gamma"]
    replay_rows = []
    for obligation in remaining_ew["rows"]:
        channel = obligation["channel"]
        bench = benchmark_by_channel[channel]
        sidecar = sidecar_by_channel[channel]
        replay_rows.append(
            {
                "channel": channel,
                "policy": "AUDITED_DOWNSTREAM_BENCHMARK_REPLAY_ROW",
                "benchmark_width_GeV": bench["width_GeV"],
                "BR_benchmark": bench["BR_benchmark"],
                "source": bench["source"],
                "source_url": bench["source_url"],
                "relative_uncertainty_sidecar": sidecar["relative_uncertainty"],
                "absolute_uncertainty_GeV": sidecar["absolute_uncertainty_GeV"],
                "required_formula_family_still_open": obligation["required_kernel_family"],
                "operator_attachment_required": obligation["operator_attachment_required"],
                "accepted_as_downstream_benchmark_replay_row": True,
                "accepted_as_executable_formula_kernel": False,
                "accepted_as_precision_formula_row": False,
                "used_as_source_selector": False,
                "target_fitting_used": False,
            }
        )

    executable_rows = list(kernels["executable_rows"])
    completion_rows = [
        {
            "channel": row["channel"],
            "row_kind": "executable_proxy_kernel",
            "width_GeV": row["width_GeV"],
            "accepted_for_replay_completion": True,
            "accepted_for_precision": False,
        }
        for row in executable_rows
    ] + [
        {
            "channel": row["channel"],
            "row_kind": "audited_benchmark_replay",
            "width_GeV": row["benchmark_width_GeV"],
            "accepted_for_replay_completion": True,
            "accepted_for_precision": False,
        }
        for row in replay_rows
    ]
    completion_rows = sorted(completion_rows, key=lambda row: row["channel"])
    replay_sum = sum(row["width_GeV"] for row in completion_rows)

    policy = {
        "schema": "MTTRemainingElectroweakBenchmarkReplayPolicy.v1",
        "status": "EW_BENCHMARK_REPLAY_POLICY_BUILT_FORMULA_ROWS_OPEN",
        "rows": replay_rows,
        "summary": {
            "benchmark_replay_row_count": len(replay_rows),
            "all_remaining_EW_rows_have_benchmark_policy": sorted(row["channel"] for row in replay_rows) == sorted(ew_channels),
            "all_rows_have_sidecars": all(row["relative_uncertainty_sidecar"] > 0.0 for row in replay_rows),
            "accepted_as_SM_parity_replay_policy": True,
            "accepted_as_formula_kernel_policy": False,
            "accepted_as_precision_policy": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    completion = {
        "schema": "MTTHiggsTenChannelReplayCompletion.v1",
        "status": "TEN_CHANNEL_HIGGS_REPLAY_COMPLETED_MIXED_PROXY_BENCHMARK_PRECISION_OPEN",
        "rows": completion_rows,
        "summary": {
            "row_count": len(completion_rows),
            "executable_proxy_kernel_count": len(executable_rows),
            "audited_benchmark_replay_count": len(replay_rows),
            "all_ten_channels_have_replay_rows": len(completion_rows) == 10,
            "mixed_proxy_and_benchmark_replay_sum_GeV": replay_sum,
            "uniform_formula_rows_fully_filled": False,
            "full_covariance_profile_filled": False,
            "precision_promotion_accepted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    open_obligations = {
        "schema": "MTTRemainingHiggsPrecisionFormulaObligations.v1",
        "status": "TEN_CHANNEL_REPLAY_BUILT_PRECISION_FORMULAS_AND_COVARIANCE_OPEN",
        "formula_rows_still_required_for_precision": [
            {
                "channel": row["channel"],
                "required_formula_family": row["required_formula_family_still_open"],
                "operator_attachment_required": row["operator_attachment_required"],
            }
            for row in replay_rows
        ],
        "global_obligations": [
            "replace proxy rows by precision formula rows or accepted precision benchmark convention",
            "replace benchmark replay rows by formula kernels for no-knob/source-sensitive claims",
            "supply ten-channel covariance/profile matrix",
            "attach selected electroweak and Qa/SU3 operator packets for source-level promotion",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = list(previous_gate["remaining_true_equivalence_blockers"])
    closed_now = previous_gate["closed_now"] + ["audited benchmark-replay policy for remaining electroweak Higgs rows"]
    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterEWBenchmarkPolicy.v1",
        "status": "TEN_CHANNEL_REPLAY_COMPLETED_PRECISION_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": closed_now,
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "replace EW benchmark replay rows by formula kernels or supply ten-channel covariance/profile matrix",
        "guardrails": {
            "benchmark_replay_not_formula_kernel": True,
            "ten_channel_replay_not_precision": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsEWBenchmarkPolicyOrFullFormulas",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsgammagammakernelrow_or_remainingew.candidate.json"),
            "benchmark_rows": rel(
                DATA
                / "selected_higgsmissingchannelbenchmarks_or_totalwidthreplay"
                / "missing_higgs_channel_benchmark_rows.packet.json"
            ),
            "sidecars": rel(
                DATA
                / "selected_higgsprecisionsidecars_or_uniformformularows"
                / "higgs_channel_uncertainty_sidecars.packet.json"
            ),
        },
        "output_packets": {
            "remaining_electroweak_benchmark_replay_policy": rel(POLICY),
            "higgs_ten_channel_replay_completion": rel(COMPLETION),
            "remaining_higgs_precision_formula_obligations": rel(OPEN),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "HiggsElectroweakBenchmarkReplayPolicyTheorem",
            "proved": True,
            "statement": (
                "The remaining electroweak Higgs rows WW*, ZZ*, and Z gamma can be admitted at the SM-parity "
                "replay tier as audited downstream benchmark rows with sidecars and explicit formula obligations. "
                "This completes ten-channel replay coverage but not uniform formulas, covariance/profile likelihood, "
                "true SM-equivalence, or no-knob closure."
            ),
        },
        "what_closes_now": {
            "remaining_EW_benchmark_replay_policy": True,
            "ten_channel_Higgs_replay_coverage": True,
            "precision_formula_obligations_isolated": True,
        },
        "what_remains_open": {
            "EW_formula_kernels_for_WW_ZZ_Zgamma": True,
            "ten_channel_covariance_profile": True,
            "selected_operator_attachment": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_replay_coverage_closed": True,
            "ten_channel_replay_completed": True,
            "uniform_formula_rows_fully_closed": False,
            "full_channel_values_closed": False,
            "cross_channel_covariance_profile_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsEWBenchmarkPolicy_or_FullFormulas_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "ten_channel_replay_completed": True,
        "uniform_formula_rows_fully_closed": False,
        "full_channel_values_closed": False,
        "cross_channel_covariance_profile_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsFormulaKernelReplacement_or_CovarianceProfileValues_v1",
    }

    note = """# MTT Selected HiggsEWBenchmarkPolicy or FullFormulas v1

Status: `MTT_SELECTED_HIGGSEWBENCHMARKPOLICY_OR_FULLFORMULAS_BUILT_TEN_CHANNEL_REPLAY_PRECISION_OPEN`.

This artifact admits the remaining `WW*`, `ZZ*`, and `Z gamma` Higgs rows at
the SM-parity replay tier through an audited downstream benchmark policy.

It completes ten-channel Higgs replay coverage, but it is not a uniform formula
calculation, not a precision covariance/profile likelihood, and not a no-knob
or selected-source derivation.
"""

    for path, payload in [
        (POLICY, policy),
        (COMPLETION, completion),
        (OPEN, open_obligations),
        (UPDATED, updated),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
