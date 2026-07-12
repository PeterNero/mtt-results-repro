"""Build ten-channel Higgs covariance/profile and branching-ratio replay gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgstenchannelcovarianceprofile_or_branchingreplay"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TOTAL = PACKET_DIR / "ten_channel_total_width_diagonal_profile.packet.json"
BRANCHING = PACKET_DIR / "ten_channel_branching_ratio_replay.packet.json"
JACOBIAN = PACKET_DIR / "branching_ratio_diagonal_covariance_jacobian.packet.json"
DECISION = PACKET_DIR / "precision_total_width_and_branching_decision.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_ten_channel_branching.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsTenChannelCovarianceProfile_or_BranchingReplay_v1.md"

STATUS = "MTT_SELECTED_HIGGSTENCHANNELCOVARIANCEPROFILE_OR_BRANCHINGREPLAY_BUILT_DIAGONAL_REPLAY_PRECISION_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsewformulakernelexecution_or_precisionimportrows.candidate.json")
    refreshed = load(
        DATA
        / "selected_higgscomputedchannelrefresh_or_totalwidthreplay"
        / "refreshed_higgs_total_width_replay.packet.json"
    )
    covariance_contract = load(
        DATA
        / "selected_higgscovarianceprofilecontract_or_uniformformularows"
        / "higgs_covariance_profile_contract.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgsewformulakernelexecution_or_precisionimportrows"
        / "updated_true_equivalence_gate_after_ew_import_profile.packet.json"
    )

    row_basis = covariance_contract["row_basis"]
    replay_by_channel = {row["channel"]: row for row in refreshed["rows"]}
    variances = covariance_contract["diagonal_fallback_from_sidecars"]["diagonal_variances_GeV2"]
    widths = [float(replay_by_channel[channel]["width_GeV"]) for channel in row_basis]
    covariance_diag = [float(variances[channel]) for channel in row_basis]
    total_width = sum(widths)
    reference_total = float(refreshed["summary"]["reference_total_width_GeV"])
    total_variance = sum(covariance_diag)
    total_sigma = total_variance**0.5
    total_residual = total_width - reference_total
    total_pull = total_residual / total_sigma

    total_rows = []
    for channel, width, variance in zip(row_basis, widths, covariance_diag):
        row = replay_by_channel[channel]
        total_rows.append(
            {
                "channel": channel,
                "row_kind": row["row_kind"],
                "width_GeV": width,
                "variance_GeV2": variance,
                "sigma_GeV": variance**0.5,
                "precision_accepted": row["precision_accepted"],
                "source_packet": row.get("source_packet"),
            }
        )

    total = {
        "schema": "MTTHiggsTenChannelTotalWidthDiagonalProfile.v1",
        "status": "TEN_CHANNEL_TOTAL_WIDTH_DIAGONAL_PROFILE_BUILT_NOT_PRECISION",
        "row_basis": row_basis,
        "rows": total_rows,
        "summary": {
            "channel_count": len(row_basis),
            "computed_proxy_channel_count": refreshed["summary"]["computed_proxy_channel_count"],
            "external_fill_channel_count": refreshed["summary"]["external_benchmark_fill_channel_count"],
            "total_width_GeV": total_width,
            "reference_total_width_GeV": reference_total,
            "total_minus_reference_GeV": total_residual,
            "relative_residual_to_reference": total_residual / reference_total,
            "diagonal_total_sigma_GeV": total_sigma,
            "diagonal_total_pull": total_pull,
            "accepted_as_total_width_replay_scaffold": True,
            "accepted_as_precision_total_width": False,
            "accepted_as_full_correlated_profile": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    branching_rows = []
    jacobian_rows: list[list[float]] = []
    br_covariance = []
    for i, channel in enumerate(row_basis):
        br = widths[i] / total_width
        jacobian_row = []
        for j in range(len(row_basis)):
            delta = 1.0 if i == j else 0.0
            jacobian_row.append((delta * total_width - widths[i]) / (total_width * total_width))
        jacobian_rows.append(jacobian_row)
        variance = sum((jacobian_row[j] ** 2) * covariance_diag[j] for j in range(len(row_basis)))
        br_covariance.append(variance)
        branching_rows.append(
            {
                "channel": channel,
                "branching_ratio": br,
                "branching_ratio_percent": 100.0 * br,
                "diagonal_sigma": variance**0.5,
                "row_kind": replay_by_channel[channel]["row_kind"],
                "accepted_as_precision_branching_ratio": False,
            }
        )

    branching = {
        "schema": "MTTHiggsTenChannelBranchingRatioReplay.v1",
        "status": "TEN_CHANNEL_BRANCHING_RATIO_REPLAY_BUILT_FROM_CURRENT_WIDTH_SCAFFOLD",
        "normalization_width_GeV": total_width,
        "rows": branching_rows,
        "summary": {
            "branching_ratio_sum": sum(row["branching_ratio"] for row in branching_rows),
            "largest_branching_ratio_channel": max(branching_rows, key=lambda row: row["branching_ratio"])["channel"],
            "smallest_branching_ratio_channel": min(branching_rows, key=lambda row: row["branching_ratio"])["channel"],
            "accepted_as_branching_replay_scaffold": True,
            "accepted_as_precision_branching_ratios": False,
            "normalization_uses_current_mixed_proxy_import_widths": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    jacobian = {
        "schema": "MTTBranchingRatioDiagonalCovarianceJacobian.v1",
        "status": "BRANCHING_RATIO_DIAGONAL_JACOBIAN_PROPAGATION_BUILT_FULL_PROFILE_OPEN",
        "row_basis": row_basis,
        "jacobian_dBR_dGamma": jacobian_rows,
        "input_diagonal_variances_GeV2": dict(zip(row_basis, covariance_diag)),
        "output_diagonal_variances": dict(zip(row_basis, br_covariance)),
        "summary": {
            "input_dimension": len(row_basis),
            "output_dimension": len(row_basis),
            "propagates_total_width_normalization_uncertainty": True,
            "accepted_as_diagonal_error_propagation": True,
            "accepted_as_full_correlated_profile": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTPrecisionTotalWidthAndBranchingDecision.v1",
        "status": "TEN_CHANNEL_REPLAY_BUILT_PRECISION_TOTAL_WIDTH_AND_BRANCHING_STILL_OPEN",
        "total_width_replay_built": True,
        "branching_ratio_replay_built": True,
        "diagonal_covariance_propagation_built": True,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "values_promotable_to_precision_now": False,
        "blocked_by": [
            "three EW rows remain external import identities rather than executable formula kernels or accepted precision imports",
            "QCD and gamma rows remain proxy/first-pass formula rows rather than full precision rows",
            "diagonal propagation is not a full empirical correlated likelihood",
            "actual no-knob Qa/SU3 and electroweak operator-source packets remain open",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterTenChannelBranching.v1",
        "status": "TEN_CHANNEL_BRANCHING_REPLAY_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "closed_now": previous_true["closed_now"] + [
            "ten-channel diagonal total-width profile propagation",
            "ten-channel branching-ratio replay scaffold",
            "branching-ratio diagonal covariance Jacobian",
        ],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "replace mixed proxy/import Higgs replay with accepted precision formula/import rows and a full correlated profile",
        "guardrails": {
            "branching_ratios_are_current_scaffold_ratios": True,
            "diagonal_profile_not_full_likelihood": True,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsTenChannelCovarianceProfileOrBranchingReplay",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsewformulakernelexecution_or_precisionimportrows.candidate.json"),
            "refreshed_total_width_replay": rel(
                DATA
                / "selected_higgscomputedchannelrefresh_or_totalwidthreplay"
                / "refreshed_higgs_total_width_replay.packet.json"
            ),
            "covariance_profile_contract": rel(
                DATA
                / "selected_higgscovarianceprofilecontract_or_uniformformularows"
                / "higgs_covariance_profile_contract.packet.json"
            ),
        },
        "output_packets": {
            "ten_channel_total_width_diagonal_profile": rel(TOTAL),
            "ten_channel_branching_ratio_replay": rel(BRANCHING),
            "branching_ratio_diagonal_covariance_jacobian": rel(JACOBIAN),
            "precision_total_width_and_branching_decision": rel(DECISION),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsTenChannelCovarianceProfileBranchingReplayTheorem",
            "proved": True,
            "statement": (
                "Given the refreshed ten-channel Higgs width replay and diagonal sidecar covariance contract, "
                "the repo can compute the current total-width scaffold, propagate diagonal uncertainty through "
                "the total width and branching-ratio normalization, and emit a ten-channel branching-ratio replay. "
                "Because the rows are still mixed proxy/import rows and the covariance is diagonal-only, this does "
                "not close precision total width, precision branching ratios, true SM equivalence, or no-knob closure."
            ),
        },
        "what_closes_now": {
            "ten_channel_total_width_diagonal_profile": True,
            "ten_channel_branching_ratio_replay": True,
            "branching_ratio_diagonal_covariance_jacobian": True,
            "precision_promotion_decision_recorded": True,
        },
        "what_remains_open": {
            "accepted_precision_Higgs_formula_or_import_rows": True,
            "full_ten_channel_correlated_profile": True,
            "precision_total_width": True,
            "precision_branching_ratios": True,
            "actual_QaSU3_and_EW_operator_sources": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "total_width_replay_built": True,
            "branching_ratio_replay_built": True,
            "diagonal_covariance_propagation_built": True,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsTenChannelCovarianceProfile_or_BranchingReplay_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "total_width_replay_built": True,
        "branching_ratio_replay_built": True,
        "diagonal_covariance_propagation_built": True,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsPrecisionRows_or_FullCorrelatedProfile_v1",
    }

    note = f"""# MTT Selected HiggsTenChannelCovarianceProfile or BranchingReplay v1

Status: `{STATUS}`.

This artifact uses the current ten-channel Higgs width scaffold to compute a
total-width replay, branching-ratio replay, and diagonal covariance propagation
through the branching-ratio normalization.

The branching ratios are scaffold ratios of the current mixed proxy/import width
rows. They are not precision branching ratios, not a full correlated profile,
and not a no-knob derivation.
"""

    for path, payload in [
        (TOTAL, total),
        (BRANCHING, branching),
        (JACOBIAN, jacobian),
        (DECISION, decision),
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
