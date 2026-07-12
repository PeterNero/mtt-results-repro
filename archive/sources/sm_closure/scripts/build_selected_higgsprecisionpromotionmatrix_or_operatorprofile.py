"""Build a Higgs precision-promotion matrix from the ten-channel replay layer."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsprecisionpromotionmatrix_or_operatorprofile"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
MATRIX = PACKET_DIR / "higgs_precision_promotion_matrix.packet.json"
DIAGONAL = PACKET_DIR / "higgs_diagonal_sidecar_profile_stress.packet.json"
OPERATOR = PACKET_DIR / "higgs_operator_profile_promotion_obligations.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_higgs_promotion_matrix.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsPrecisionPromotionMatrix_or_OperatorProfile_v1.md"

STATUS = "MTT_SELECTED_HIGGSPRECISIONPROMOTIONMATRIX_OR_OPERATORPROFILE_BUILT_PRECISION_PROMOTION_BLOCKERS_EXACT"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def operator_obligation(channel: str, row_kind: str) -> str:
    if channel in {"H_to_bb", "H_to_cc", "H_to_ss"}:
        return "Qa/SU3 color plus running-mass/Yukawa operator packet"
    if channel == "H_to_gg":
        return "Qa/SU3 color trace, heavy-quark loop, threshold, and QCD K-factor operator packet"
    if channel == "H_to_gamma_gamma":
        return "electroweak charge/operator packet with W and top charged-loop representations"
    if channel in {"H_to_WW_star", "H_to_ZZ_star"}:
        return "off-shell electroweak gauge/Higgs four-fermion operator packet"
    if channel == "H_to_Z_gamma":
        return "mixed neutral-current electroweak loop operator packet"
    if channel in {"H_to_tau_tau", "H_to_mu_mu"}:
        return "lepton Yukawa, electroweak correction, and mass-scheme operator packet"
    return f"operator packet required for {row_kind}"


def formula_obligation(channel: str) -> str:
    if channel in {"H_to_bb", "H_to_cc", "H_to_ss"}:
        return "precision H->qq running-mass formula with QCD/EW corrections and threshold matching"
    if channel == "H_to_gg":
        return "precision H->gg loop formula with finite-mass effects, multi-loop QCD, and thresholds"
    if channel == "H_to_gamma_gamma":
        return "precision H->gamma gamma loop formula with all charged loops and EW/QCD corrections"
    if channel in {"H_to_WW_star", "H_to_ZZ_star"}:
        return "off-shell H->VV* four-fermion width with EW corrections and phase-space integration"
    if channel == "H_to_Z_gamma":
        return "precision H->Z gamma mixed loop formula with EW corrections"
    if channel in {"H_to_tau_tau", "H_to_mu_mu"}:
        return "precision H->ll formula with EW correction and mass-scheme convention"
    return "precision formula row"


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsewbenchmarkpolicy_or_fullformulas.candidate.json")
    completion = load(
        DATA
        / "selected_higgsewbenchmarkpolicy_or_fullformulas"
        / "higgs_ten_channel_replay_completion.packet.json"
    )
    sidecars = load(
        DATA
        / "selected_higgsprecisionsidecars_or_uniformformularows"
        / "higgs_channel_uncertainty_sidecars.packet.json"
    )
    previous_gate = load(
        DATA
        / "selected_higgsewbenchmarkpolicy_or_fullformulas"
        / "updated_true_equivalence_gate_after_ew_benchmark_policy.packet.json"
    )

    sidecar_by_channel = {row["channel"]: row for row in sidecars["rows"]}
    rows: list[dict[str, Any]] = []
    stress_terms: list[dict[str, Any]] = []
    for row in completion["rows"]:
        channel = row["channel"]
        sidecar = sidecar_by_channel[channel]
        replay_width = float(row["width_GeV"])
        reference_width = float(sidecar["width_GeV"])
        sigma = float(sidecar["absolute_uncertainty_GeV"])
        residual = replay_width - reference_width
        pull = residual / sigma if sigma > 0.0 else None
        precision_blockers = [
            "promote proxy kernel to accepted precision formula"
            if row["row_kind"] == "executable_proxy_kernel"
            else "replace downstream benchmark replay by executable formula kernel",
            formula_obligation(channel),
            operator_obligation(channel, row["row_kind"]),
            "cross-channel covariance/profile row",
            "multi-loop convention and threshold provenance",
        ]
        rows.append(
            {
                "channel": channel,
                "row_kind": row["row_kind"],
                "replay_width_GeV": replay_width,
                "sidecar_reference_width_GeV": reference_width,
                "sidecar_relative_uncertainty": sidecar["relative_uncertainty"],
                "sidecar_absolute_uncertainty_GeV": sigma,
                "residual_GeV": residual,
                "diagonal_sidecar_pull": pull,
                "accepted_for_SM_parity_replay": row["accepted_for_replay_completion"],
                "accepted_as_precision_width": False,
                "accepted_as_no_knob_or_source_derived_value": False,
                "required_formula_family": formula_obligation(channel),
                "operator_attachment_required": operator_obligation(channel, row["row_kind"]),
                "precision_blockers": precision_blockers,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )
        if pull is not None:
            stress_terms.append(
                {
                    "channel": channel,
                    "pull": pull,
                    "pull_squared": pull * pull,
                    "diagonal_only_not_full_covariance": True,
                }
            )

    chi2 = sum(term["pull_squared"] for term in stress_terms)
    largest = max(stress_terms, key=lambda term: abs(term["pull"]))
    benchmark_replay_rows = [row for row in rows if row["row_kind"] == "audited_benchmark_replay"]
    proxy_rows = [row for row in rows if row["row_kind"] == "executable_proxy_kernel"]

    matrix = {
        "schema": "MTTHiggsPrecisionPromotionMatrix.v1",
        "status": "TEN_CHANNEL_PROMOTION_MATRIX_BUILT_NO_PRECISION_ROW_PROMOTED",
        "rows": rows,
        "summary": {
            "row_count": len(rows),
            "SM_parity_replay_rows": len(rows),
            "executable_proxy_kernel_rows": len(proxy_rows),
            "audited_benchmark_replay_rows": len(benchmark_replay_rows),
            "precision_rows_promoted": 0,
            "all_rows_have_sidecar_reference": len(rows) == len(sidecar_by_channel),
            "all_rows_have_operator_obligations": all(row["operator_attachment_required"] for row in rows),
            "all_rows_have_formula_obligations": all(row["required_formula_family"] for row in rows),
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    diagonal = {
        "schema": "MTTHiggsDiagonalSidecarProfileStress.v1",
        "status": "DIAGONAL_STRESS_EXECUTED_FULL_COVARIANCE_PROFILE_OPEN",
        "terms": stress_terms,
        "summary": {
            "term_count": len(stress_terms),
            "diagonal_chi_square": chi2,
            "max_abs_pull": abs(largest["pull"]),
            "largest_abs_pull_channel": largest["channel"],
            "full_covariance_profile_closed": False,
            "accepted_as_precision_profile_likelihood": False,
            "why_not_precision": (
                "The stress uses diagonal sidecars and mixed proxy/benchmark references. "
                "It is an audit diagnostic, not a correlated likelihood or precision Higgs fit."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    operator = {
        "schema": "MTTHiggsOperatorProfilePromotionObligations.v1",
        "status": "OPERATOR_AND_FORMULA_PROMOTION_OBLIGATIONS_ENUMERATED",
        "operator_obligations": [
            {
                "channel": row["channel"],
                "operator_attachment_required": row["operator_attachment_required"],
                "required_formula_family": row["required_formula_family"],
                "source_sensitive": row["channel"] in {"H_to_bb", "H_to_cc", "H_to_ss", "H_to_gg"},
                "precision_promotion_status": "OPEN",
            }
            for row in rows
        ],
        "global_required_packets": [
            "selected electroweak gauge/Higgs operator packet for WW*, ZZ*, gamma gamma, and Z gamma",
            "selected Qa/SU3 color/operator packet for qq and gg rows",
            "mass-scheme and threshold provenance map for all fermion and loop rows",
            "ten-channel covariance/profile matrix",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterHiggsPromotionMatrix.v1",
        "status": "HIGGS_PROMOTION_MATRIX_BUILT_TRUE_EQUIVALENCE_GATES_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": previous_gate["closed_now"] + ["ten-channel Higgs precision-promotion matrix and diagonal sidecar stress"],
        "remaining_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"]
        + [
            "Higgs ten-channel precision formula/operator promotion",
            "Higgs ten-channel correlated covariance/profile likelihood",
        ],
        "next_primary_value_gate": "build accepted formula/operator rows for WW*, ZZ*, Z gamma or supply a correlated ten-channel profile",
        "guardrails": {
            "diagonal_profile_not_full_covariance": True,
            "mixed_proxy_benchmark_rows_not_precision": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsPrecisionPromotionMatrixOrOperatorProfile",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsewbenchmarkpolicy_or_fullformulas.candidate.json"),
            "ten_channel_replay_completion": rel(
                DATA
                / "selected_higgsewbenchmarkpolicy_or_fullformulas"
                / "higgs_ten_channel_replay_completion.packet.json"
            ),
            "diagonal_sidecars": rel(
                DATA
                / "selected_higgsprecisionsidecars_or_uniformformularows"
                / "higgs_channel_uncertainty_sidecars.packet.json"
            ),
        },
        "output_packets": {
            "higgs_precision_promotion_matrix": rel(MATRIX),
            "higgs_diagonal_sidecar_profile_stress": rel(DIAGONAL),
            "higgs_operator_profile_promotion_obligations": rel(OPERATOR),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "HiggsPrecisionPromotionMatrixTheorem",
            "proved": True,
            "statement": (
                "Given the completed ten-channel replay layer and diagonal sidecars, every Higgs channel can be "
                "classified into an SM-parity replay row with explicit formula, operator, threshold, and covariance "
                "obligations. No row is promoted to full precision until those obligations are supplied."
            ),
        },
        "what_closes_now": {
            "ten_channel_precision_promotion_decision_table": True,
            "diagonal_sidecar_stress_executed": True,
            "operator_formula_obligations_per_channel": True,
        },
        "what_remains_open": {
            "accepted_precision_formula_rows": True,
            "ten_channel_correlated_covariance_profile": True,
            "selected_electroweak_operator_attachment": True,
            "selected_Qa_SU3_operator_attachment": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_Higgs_replay_rows_closed": True,
            "precision_promotion_matrix_closed": True,
            "diagonal_sidecar_stress_closed_as_diagnostic": True,
            "full_covariance_profile_closed": False,
            "Higgs_precision_widths_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsPrecisionPromotionMatrix_or_OperatorProfile_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "ten_channel_precision_promotion_decision_table": True,
        "diagonal_sidecar_stress_executed": True,
        "precision_rows_promoted": 0,
        "full_covariance_profile_closed": False,
        "Higgs_precision_widths_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsAcceptedFormulaRows_or_CorrelatedProfileValues_v1",
    }

    note = """# MTT Selected HiggsPrecisionPromotionMatrix or OperatorProfile v1

Status: `MTT_SELECTED_HIGGSPRECISIONPROMOTIONMATRIX_OR_OPERATORPROFILE_BUILT_PRECISION_PROMOTION_BLOCKERS_EXACT`.

This artifact turns the completed ten-channel Higgs replay layer into a
promotion matrix. Every row is accepted for SM-parity replay only, and every
row receives explicit formula, operator, threshold, and covariance obligations.

The diagonal sidecar stress is a diagnostic audit. It is not a correlated
likelihood, not a precision Higgs-width calculation, and not a no-knob source
derivation.
"""

    for path, payload in [
        (MATRIX, matrix),
        (DIAGONAL, diagonal),
        (OPERATOR, operator),
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
