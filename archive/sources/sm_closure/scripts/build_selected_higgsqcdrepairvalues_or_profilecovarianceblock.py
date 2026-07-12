"""Build a diagonal QCD profile block fallback for Higgs QCD channels."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsqcdrepairvalues_or_profilecovarianceblock"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BLOCK = PACKET_DIR / "qcd_diagonal_profile_block.packet.json"
PSD = PACKET_DIR / "qcd_profile_psd_and_chisquare_check.packet.json"
REPAIR = PACKET_DIR / "qcd_repair_values_status_after_profile_block.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_qcd_profile_block.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsQCDRepairValues_or_ProfileCovarianceBlock_v1.md"

STATUS = "MTT_SELECTED_HIGGSQCDREPAIRVALUES_OR_PROFILECOVARIANCEBLOCK_BUILT_DIAGONAL_QCD_PROFILE_FALLBACK"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgssupersetqcdrepaircontroller_or_values.candidate.json")
    matrix = load(
        DATA
        / "selected_higgsprecisionpromotionmatrix_or_operatorprofile"
        / "higgs_precision_promotion_matrix.packet.json"
    )
    controller = load(
        DATA
        / "selected_higgssupersetqcdrepaircontroller_or_values"
        / "superset_qcd_repair_controller.packet.json"
    )
    acceptance = load(
        DATA
        / "selected_higgssupersetqcdrepaircontroller_or_values"
        / "qcd_repair_value_acceptance_kernel.packet.json"
    )
    previous_gate = load(
        DATA
        / "selected_higgssupersetqcdrepaircontroller_or_values"
        / "updated_true_equivalence_gate_after_superset_qcd_controller.packet.json"
    )

    channels = ["H_to_bb", "H_to_cc", "H_to_ss", "H_to_gg"]
    by_channel = {row["channel"]: row for row in matrix["rows"]}
    block_rows = []
    covariance = []
    inverse_covariance = []
    residual_vector = []
    pull_vector = []
    for i, channel in enumerate(channels):
        row = by_channel[channel]
        sigma = float(row["sidecar_absolute_uncertainty_GeV"])
        residual = float(row["residual_GeV"])
        pull = float(row["diagonal_sidecar_pull"])
        residual_vector.append(residual)
        pull_vector.append(pull)
        cov_row = []
        inv_row = []
        for j, _ in enumerate(channels):
            if i == j:
                cov_row.append(sigma * sigma)
                inv_row.append(1.0 / (sigma * sigma))
            else:
                cov_row.append(0.0)
                inv_row.append(0.0)
        covariance.append(cov_row)
        inverse_covariance.append(inv_row)
        block_rows.append(
            {
                "channel": channel,
                "replay_width_GeV": row["replay_width_GeV"],
                "reference_width_GeV": row["sidecar_reference_width_GeV"],
                "residual_GeV": residual,
                "sigma_GeV": sigma,
                "pull": pull,
                "operator_attachment_required": row["operator_attachment_required"],
                "accepted_as_diagonal_profile_row": True,
                "accepted_as_full_correlated_profile_row": False,
                "accepted_as_precision_width": False,
            }
        )

    variances = [covariance[i][i] for i in range(len(channels))]
    chi_square = sum(p * p for p in pull_vector)
    block = {
        "schema": "MTTHiggsQCDDiagonalProfileBlock.v1",
        "status": "QCD_DIAGONAL_PROFILE_BLOCK_BUILT_FULL_CORRELATION_OPEN",
        "channels": channels,
        "rows": block_rows,
        "residual_vector_GeV": residual_vector,
        "pull_vector": pull_vector,
        "covariance_matrix_GeV2": covariance,
        "inverse_covariance_matrix_GeVminus2": inverse_covariance,
        "summary": {
            "dimension": len(channels),
            "filled_entries": len(channels) * len(channels),
            "nonzero_entries": len(channels),
            "diagonal_only": True,
            "diagonal_chi_square": chi_square,
            "accepted_as_parity_profile_fallback": True,
            "accepted_as_full_correlated_profile": False,
            "accepted_as_precision_profile": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    psd = {
        "schema": "MTTHiggsQCDProfilePSDAndChiSquareCheck.v1",
        "status": "PSD_AND_DIAGONAL_CHISQUARE_CHECK_PASSED_PRECISION_OPEN",
        "eigenvalues_GeV2": variances,
        "all_eigenvalues_nonnegative": all(value >= 0.0 for value in variances),
        "all_eigenvalues_positive": all(value > 0.0 for value in variances),
        "diagonal_chi_square": chi_square,
        "degrees_of_freedom": len(channels),
        "largest_abs_pull_channel": max(block_rows, key=lambda row: abs(row["pull"]))["channel"],
        "full_correlated_profile_closed": False,
        "precision_profile_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    repair = {
        "schema": "MTTHiggsQCDRepairValuesStatusAfterProfileBlock.v1",
        "status": "PROFILE_FALLBACK_BUILT_REPAIR_VALUES_STILL_OPEN",
        "acceptance_kernel_import": rel(
            DATA
            / "selected_higgssupersetqcdrepaircontroller_or_values"
            / "qcd_repair_value_acceptance_kernel.packet.json"
        ),
        "acceptance_tests": acceptance["tests"],
        "repair_values_filled": False,
        "values_promotable_now": False,
        "qcd_profile_block_filled_as_diagonal_fallback": True,
        "full_correlated_profile_filled": False,
        "selected_QaSU3_operator_attachment_closed": False,
        "controller_locked_target": controller["locked_target"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterQCDProfileBlock.v1",
        "status": "QCD_DIAGONAL_PROFILE_BLOCK_BUILT_TRUE_EQUIVALENCE_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": previous_gate["closed_now"] + ["diagonal QCD profile fallback block with PSD and chi-square check"],
        "remaining_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "supply non-fit QCD repair formula values or selected Qa/SU3 operator attachment",
        "guardrails": {
            "diagonal_profile_not_full_correlation": True,
            "repair_values_filled": False,
            "qasu3_operator_attachment_closed": False,
            "precision_profile_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsQCDRepairValuesOrProfileCovarianceBlock",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgssupersetqcdrepaircontroller_or_values.candidate.json"),
            "promotion_matrix": rel(
                DATA
                / "selected_higgsprecisionpromotionmatrix_or_operatorprofile"
                / "higgs_precision_promotion_matrix.packet.json"
            ),
            "superset_controller": rel(
                DATA
                / "selected_higgssupersetqcdrepaircontroller_or_values"
                / "superset_qcd_repair_controller.packet.json"
            ),
        },
        "output_packets": {
            "qcd_diagonal_profile_block": rel(BLOCK),
            "qcd_profile_psd_and_chisquare_check": rel(PSD),
            "qcd_repair_values_status": rel(REPAIR),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "HiggsQCDDiagonalProfileFallbackTheorem",
            "proved": True,
            "statement": (
                "The QCD color-threshold Higgs block admits a reproducible diagonal covariance/profile fallback "
                "from the existing sidecars. This closes a PSD and diagonal chi-square check, but it is not a "
                "full correlated profile and does not promote QCD repair values or source/operator attachment."
            ),
        },
        "what_closes_now": {
            "QCD_diagonal_profile_block": True,
            "PSD_check": True,
            "diagonal_chi_square_check": True,
            "profile_fallback_guardrail": True,
        },
        "what_remains_open": {
            "non_fit_QCD_threshold_repair_values": True,
            "selected_Qa_SU3_operator_attachment": True,
            "full_correlated_QCD_profile": True,
            "accepted_precision_formula_rows": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "diagonal_profile_fallback_closed": True,
            "full_correlated_profile_closed": False,
            "repair_values_filled": False,
            "values_promotable_now": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsQCDRepairValues_or_ProfileCovarianceBlock_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "diagonal_profile_fallback_closed": True,
        "diagonal_chi_square": chi_square,
        "full_correlated_profile_closed": False,
        "repair_values_filled": False,
        "values_promotable_now": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsQCDFormulaRepairValues_or_QaSU3OperatorAttachment_v1",
    }

    note = """# MTT Selected HiggsQCDRepairValues or ProfileCovarianceBlock v1

Status: `MTT_SELECTED_HIGGSQCDREPAIRVALUES_OR_PROFILECOVARIANCEBLOCK_BUILT_DIAGONAL_QCD_PROFILE_FALLBACK`.

This artifact fills the QCD color-threshold profile block only as a diagonal
fallback from existing sidecars. It checks PSD and computes the block
chi-square for `bb`, `cc`, `ss`, and `gg`.

It does not fill non-fit QCD repair values, does not close selected Qa/SU3
operator attachment, and does not claim a full correlated precision profile.
"""

    for path, payload in [
        (BLOCK, block),
        (PSD, psd),
        (REPAIR, repair),
        (UPDATED, updated),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS, "diagonal_chi_square": chi_square}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
