"""Build Higgs channel uncertainty sidecars and the next precision gate."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsprecisionsidecars_or_uniformformularows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SIDECARS = PACKET_DIR / "higgs_channel_uncertainty_sidecars.packet.json"
ENVELOPE = PACKET_DIR / "hybrid_total_width_diagonal_envelope.packet.json"
GATE = PACKET_DIR / "uniform_formula_row_precision_gate.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_sidecars.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsPrecisionSidecars_or_UniformFormulaRows_v1.md"

STATUS = "MTT_SELECTED_HIGGSPRECISIONSIDECARS_OR_UNIFORMFORMULAROWS_BUILT_SIDECARS_UNIFORM_ROWS_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsmissingchannelbenchmarks_or_totalwidthreplay.candidate.json")
    previous_gate = load(
        DATA
        / "selected_higgsmissingchannelbenchmarks_or_totalwidthreplay"
        / "updated_true_equivalence_gate_after_missing_channel_benchmarks.packet.json"
    )
    hybrid = load(
        DATA
        / "selected_higgsmissingchannelbenchmarks_or_totalwidthreplay"
        / "hybrid_higgs_total_width_replay.packet.json"
    )
    residual = load(
        DATA
        / "selected_higgsdecayresidualaudit_or_precisionpromotion"
        / "higgs_decay_proxy_residual_audit.packet.json"
    )

    best_residual = {
        f"H_to_{channel}{channel}": abs(row["relative_residual"])
        for channel, row in residual["best_stage_by_channel"].items()
    }
    default_relative_uncertainty = {
        "H_to_tau_tau": 0.05,
        "H_to_mu_mu": 0.05,
        "H_to_WW_star": 0.043,
        "H_to_ZZ_star": 0.043,
        "H_to_gg": 0.04,
        "H_to_gamma_gamma": 0.03,
        "H_to_Z_gamma": 0.09,
        "H_to_ss": 0.08,
    }

    rows = []
    for row in hybrid["rows"]:
        channel = row["channel"]
        width = float(row["width_GeV"])
        if row["row_kind"] == "computed_proxy" and channel in best_residual:
            rel_unc = max(best_residual[channel], 0.05)
            source = "non-fit residual against fixed LHCHXSWG benchmark; conservative proxy model sidecar"
        elif row["row_kind"] == "computed_proxy":
            rel_unc = default_relative_uncertainty.get(channel, 0.10)
            source = "placeholder proxy uncertainty; full lepton/EW sidecar not yet supplied"
        else:
            rel_unc = default_relative_uncertainty[channel]
            source = "external benchmark/theory uncertainty placeholder from LHCHXSWG-style public tables"
        rows.append(
            {
                "channel": channel,
                "width_GeV": width,
                "row_kind": row["row_kind"],
                "relative_uncertainty": rel_unc,
                "absolute_uncertainty_GeV": width * rel_unc,
                "uncertainty_source": source,
                "covariance_status": "DIAGONAL_ONLY_NO_CROSS_CHANNEL_CORRELATIONS",
                "accepted_as_uncertainty_sidecar": True,
                "accepted_as_full_covariance_profile": False,
            }
        )

    diagonal_sigma = math.sqrt(sum(row["absolute_uncertainty_GeV"] ** 2 for row in rows))
    width_sum = float(hybrid["summary"]["hybrid_width_sum_GeV"])
    reference = float(hybrid["summary"]["reference_total_width_GeV"])
    sidecars = {
        "schema": "MTTHiggsChannelUncertaintySidecars.v1",
        "status": "HIGGS_CHANNEL_UNCERTAINTY_SIDECARS_BUILT_DIAGONAL_ONLY",
        "rows": rows,
        "summary": {
            "sidecar_count": len(rows),
            "all_hybrid_rows_have_sidecars": len(rows) == len(hybrid["rows"]),
            "all_sidecars_diagonal_only": all(row["covariance_status"] == "DIAGONAL_ONLY_NO_CROSS_CHANNEL_CORRELATIONS" for row in rows),
            "full_covariance_profile_filled": False,
        },
        "accepted_as_precision_sidecars": True,
        "accepted_as_full_covariance_profile": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    envelope = {
        "schema": "MTTHybridTotalWidthDiagonalEnvelope.v1",
        "status": "HYBRID_TOTAL_WIDTH_DIAGONAL_ENVELOPE_BUILT_FULL_PROFILE_OPEN",
        "hybrid_width_sum_GeV": width_sum,
        "reference_total_width_GeV": reference,
        "diagonal_sigma_GeV": diagonal_sigma,
        "relative_diagonal_sigma": diagonal_sigma / width_sum,
        "pull_vs_reference_diagonal_only": (width_sum - reference) / diagonal_sigma,
        "within_one_sigma_diagonal_only": abs(width_sum - reference) <= diagonal_sigma,
        "accepted_as_diagonal_uncertainty_envelope": True,
        "accepted_as_full_covariance_profile": False,
        "why_not_full_profile": (
            "Uncertainties mix proxy-model residuals and external benchmark placeholders, and cross-channel correlations "
            "are not encoded. This is a conservative diagonal envelope only."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    precision_gate = {
        "schema": "MTTUniformFormulaRowPrecisionGate.v1",
        "status": "SIDECARS_BUILT_UNIFORM_FORMULA_ROWS_STILL_OPEN",
        "closed_now": [
            "uncertainty sidecars for all hybrid Higgs width rows",
            "diagonal total-width uncertainty envelope",
        ],
        "still_required_for_precision_promotion": [
            "replace proxy rows by uniform declared formula rows or accepted benchmark-replay policy",
            "replace benchmark placeholders by formula rows or explicitly audited benchmark-only policy",
            "supply cross-channel covariance/profile likelihood",
            "attach source/operator-sensitive rows to actual selected Qa/SU3 packet",
        ],
        "precision_promotion_accepted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = list(previous_gate["remaining_true_equivalence_blockers"])
    closed_now = previous_gate["closed_now"] + ["Higgs total-width uncertainty sidecars"]
    for blocker in ["Higgs total-width covariance/profile sidecars"]:
        if blocker in remaining:
            remaining.remove(blocker)
    for blocker in [
        "uniform precision Higgs partial-width formula rows",
        "full cross-channel Higgs covariance/profile likelihood",
        "full precision loop-corrected QFT correlator/S-matrix/decay rows",
        "actual selected Qa/SU3 operator packet",
    ]:
        if blocker not in remaining:
            remaining.append(blocker)
    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterSidecars.v1",
        "status": "HIGGS_SIDECARS_BUILT_UNIFORM_ROWS_AND_FULL_COVARIANCE_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": closed_now,
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "uniform precision Higgs partial-width formula rows or full cross-channel covariance profile",
        "guardrails": {
            "diagonal_sidecars_not_full_covariance": True,
            "hybrid_replay_not_precision": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsPrecisionSidecarsOrUniformFormulaRows",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsmissingchannelbenchmarks_or_totalwidthreplay.candidate.json"),
            "hybrid_total_width_replay": rel(
                DATA
                / "selected_higgsmissingchannelbenchmarks_or_totalwidthreplay"
                / "hybrid_higgs_total_width_replay.packet.json"
            ),
            "higgs_decay_residual_audit": rel(
                DATA
                / "selected_higgsdecayresidualaudit_or_precisionpromotion"
                / "higgs_decay_proxy_residual_audit.packet.json"
            ),
        },
        "output_packets": {
            "higgs_channel_uncertainty_sidecars": rel(SIDECARS),
            "hybrid_total_width_diagonal_envelope": rel(ENVELOPE),
            "uniform_formula_row_precision_gate": rel(GATE),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "HiggsPrecisionSidecarEnvelopeTheorem",
            "proved": True,
            "statement": (
                "Every hybrid Higgs width row now carries a conservative uncertainty sidecar, and the total-width "
                "replay has a diagonal uncertainty envelope. This closes sidecar bookkeeping but not uniform formula "
                "rows, cross-channel covariance, true SM equivalence, or no-knob closure."
            ),
        },
        "what_closes_now": {
            "sidecars_for_all_hybrid_Higgs_rows": True,
            "diagonal_total_width_envelope": True,
            "precision_promotion_gate_updated": True,
        },
        "what_remains_open": {
            "uniform_precision_Higgs_formula_rows": True,
            "cross_channel_covariance_profile": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "sidecar_bookkeeping_closed": True,
            "full_covariance_profile_closed": False,
            "uniform_formula_rows_closed": False,
            "precision_total_width_closed": False,
            "actual_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsPrecisionSidecars_or_UniformFormulaRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "sidecar_bookkeeping_closed": True,
        "full_covariance_profile_closed": False,
        "uniform_formula_rows_closed": False,
        "precision_total_width_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsUniformFormulaRows_or_FullCovarianceProfile_v1",
    }

    note = """# MTT Selected HiggsPrecisionSidecars or UniformFormulaRows v1

Status: `MTT_SELECTED_HIGGSPRECISIONSIDECARS_OR_UNIFORMFORMULAROWS_BUILT_SIDECARS_UNIFORM_ROWS_OPEN`.

This artifact adds conservative uncertainty sidecars to every row of the
hybrid Higgs total-width replay and computes a diagonal-only total-width
uncertainty envelope.

The sidecars close bookkeeping, not precision. The replay still mixes proxy
rows and external benchmark fills, and cross-channel covariance is not encoded.
"""

    for path, payload in [
        (SIDECARS, sidecars),
        (ENVELOPE, envelope),
        (GATE, precision_gate),
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
