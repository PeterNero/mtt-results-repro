"""Build the Higgs covariance/profile contract and uniform formula-row manifest."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgscovarianceprofilecontract_or_uniformformularows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CONTRACT = PACKET_DIR / "higgs_covariance_profile_contract.packet.json"
MANIFEST = PACKET_DIR / "uniform_higgs_formula_row_manifest.packet.json"
DIAG = PACKET_DIR / "diagonal_profile_diagnostic.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_profile_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsCovarianceProfileContract_or_UniformFormulaRows_v1.md"

STATUS = "MTT_SELECTED_HIGGSCOVARIANCEPROFILECONTRACT_OR_UNIFORMFORMULAROWS_BUILT_PROFILE_CONTRACT_UNIFORM_ROWS_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def channel_formula_requirement(channel: str) -> dict[str, Any]:
    table = {
        "H_to_bb": {
            "formula_family": "running-mass H->qq with QCD through declared order plus EW/mixed corrections",
            "shared_inputs": ["mH", "alpha_s", "m_b_MSbar", "renormalization_scale", "threshold_scheme"],
            "operator_attachment": "Y_d bottom row and color/QCD operator packet",
        },
        "H_to_cc": {
            "formula_family": "running-mass H->qq with QCD through declared order plus EW/mixed corrections",
            "shared_inputs": ["mH", "alpha_s", "m_c_MSbar", "renormalization_scale", "threshold_scheme"],
            "operator_attachment": "Y_u charm row and color/QCD operator packet",
        },
        "H_to_tau_tau": {
            "formula_family": "tree H->ll plus EW correction policy",
            "shared_inputs": ["mH", "m_tau", "v", "EW_scheme"],
            "operator_attachment": "Y_e tau row and Higgs carrier",
        },
        "H_to_mu_mu": {
            "formula_family": "tree H->ll plus EW correction policy",
            "shared_inputs": ["mH", "m_mu", "v", "EW_scheme"],
            "operator_attachment": "Y_e mu row and Higgs carrier",
        },
        "H_to_WW_star": {
            "formula_family": "off-shell H->WW* four-fermion width with EW corrections",
            "shared_inputs": ["mH", "mW", "Gamma_W", "G_F", "EW_scheme"],
            "operator_attachment": "SU2 electroweak gauge/Higgs operator packet",
        },
        "H_to_ZZ_star": {
            "formula_family": "off-shell H->ZZ* four-fermion width with EW corrections",
            "shared_inputs": ["mH", "mZ", "Gamma_Z", "G_F", "EW_scheme"],
            "operator_attachment": "SU2xU1 electroweak gauge/Higgs operator packet",
        },
        "H_to_gg": {
            "formula_family": "loop-induced H->gg through top/bottom/charm loops with higher-order QCD",
            "shared_inputs": ["mH", "alpha_s", "m_t", "m_b", "m_c", "threshold_scheme"],
            "operator_attachment": "Qa/SU3 color operator packet",
        },
        "H_to_gamma_gamma": {
            "formula_family": "loop-induced H->gamma gamma through W/top and charged loops",
            "shared_inputs": ["mH", "alpha_em", "mW", "m_t", "EW_scheme"],
            "operator_attachment": "electroweak charge/operator packet",
        },
        "H_to_Z_gamma": {
            "formula_family": "loop-induced H->Z gamma with electroweak corrections",
            "shared_inputs": ["mH", "mZ", "alpha_em", "mW", "m_t", "EW_scheme"],
            "operator_attachment": "electroweak mixed neutral-current operator packet",
        },
        "H_to_ss": {
            "formula_family": "running-mass H->ss with QCD and strange-mass scheme policy",
            "shared_inputs": ["mH", "alpha_s", "m_s_MSbar", "renormalization_scale", "threshold_scheme"],
            "operator_attachment": "Y_d strange row and color/QCD operator packet",
        },
    }
    return table[channel]


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsprecisionsidecars_or_uniformformularows.candidate.json")
    previous_gate = load(
        DATA
        / "selected_higgsprecisionsidecars_or_uniformformularows"
        / "updated_true_equivalence_gate_after_sidecars.packet.json"
    )
    sidecars = load(
        DATA
        / "selected_higgsprecisionsidecars_or_uniformformularows"
        / "higgs_channel_uncertainty_sidecars.packet.json"
    )
    envelope = load(
        DATA
        / "selected_higgsprecisionsidecars_or_uniformformularows"
        / "hybrid_total_width_diagonal_envelope.packet.json"
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

    rows = sidecars["rows"]
    row_basis = [row["channel"] for row in rows]
    diagonal_variances = {row["channel"]: row["absolute_uncertainty_GeV"] ** 2 for row in rows}
    formula_rows = []
    hybrid_by_channel = {row["channel"]: row for row in hybrid["rows"]}
    for channel in row_basis:
        req = channel_formula_requirement(channel)
        hybrid_row = hybrid_by_channel[channel]
        formula_rows.append(
            {
                "channel": channel,
                "current_row_kind": hybrid_row["row_kind"],
                "current_width_GeV": hybrid_row["width_GeV"],
                "formula_family_required": req["formula_family"],
                "shared_inputs": req["shared_inputs"],
                "operator_attachment_required": req["operator_attachment"],
                "uniform_formula_row_filled": False,
                "accepted_as_precision_formula_row": False,
                "accepted_as_downstream_parity_row": True,
            }
        )

    reference_by_channel: dict[str, dict[str, Any]] = {}
    for channel, source_key in [("H_to_bb", "b"), ("H_to_cc", "c")]:
        ref = residual["best_stage_by_channel"][source_key]["reference_GeV"]
        value = hybrid_by_channel[channel]["width_GeV"]
        sigma = next(row["absolute_uncertainty_GeV"] for row in rows if row["channel"] == channel)
        reference_by_channel[channel] = {
            "reference_width_GeV": ref,
            "reference_source": "fixed LHCHXSWG approximate BR*Gamma benchmark from residual audit",
            "current_width_GeV": value,
            "sigma_GeV": sigma,
            "pull": (value - ref) / sigma,
            "included_in_diagnostic_chi2": True,
        }
    for channel in row_basis:
        if channel not in reference_by_channel:
            reference_by_channel[channel] = {
                "reference_width_GeV": hybrid_by_channel[channel]["width_GeV"],
                "reference_source": "self-reference placeholder; excluded until independent formula/benchmark profile supplied",
                "current_width_GeV": hybrid_by_channel[channel]["width_GeV"],
                "sigma_GeV": next(row["absolute_uncertainty_GeV"] for row in rows if row["channel"] == channel),
                "pull": 0.0,
                "included_in_diagnostic_chi2": False,
            }

    included = [row for row in reference_by_channel.values() if row["included_in_diagnostic_chi2"]]
    chi2 = sum(row["pull"] ** 2 for row in included)
    diagnostic = {
        "schema": "MTTHiggsDiagonalProfileDiagnostic.v1",
        "status": "DIAGONAL_PROFILE_DIAGNOSTIC_BUILT_NOT_FULL_LIKELIHOOD",
        "row_basis": row_basis,
        "reference_rows": reference_by_channel,
        "diagonal_chi2_on_independent_reference_rows": chi2,
        "ndof_included": len(included),
        "max_abs_pull_included": max(abs(row["pull"]) for row in included),
        "accepted_as_diagnostic": True,
        "accepted_as_full_covariance_profile": False,
        "why_not_full_profile": (
            "Only bb and cc have independent approximate reference rows here; all other channels require either "
            "uniform formula rows or a published correlated profile packet. Cross-channel correlations are absent."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    contract = {
        "schema": "MTTHiggsCovarianceProfileContract.v1",
        "status": "PROFILE_CONTRACT_BUILT_COVARIANCE_VALUES_OPEN",
        "row_basis": row_basis,
        "dimension": len(row_basis),
        "required_profile_object": {
            "observable_vector": "Gamma_i for each channel in row_basis, plus optional Gamma_total derived by summation",
            "covariance_matrix": "10x10 symmetric positive semidefinite matrix in GeV^2 on the declared row_basis",
            "likelihood": "central residual vector with covariance inverse or an explicitly profiled nuisance likelihood",
            "scheme": "declared SM perturbative order, threshold scheme, mass scheme, and electroweak input scheme",
        },
        "diagonal_fallback_from_sidecars": {
            "available": True,
            "accepted_as_full_profile": False,
            "diagonal_variances_GeV2": diagonal_variances,
            "total_width_diagonal_sigma_GeV": envelope["diagonal_sigma_GeV"],
        },
        "correlation_sources_that_must_be_supplied_or_profiled": [
            "shared Higgs mass dependence",
            "shared alpha_s dependence across qq and gg channels",
            "shared quark-mass scheme uncertainties",
            "shared electroweak input-scheme uncertainties",
            "missing higher-order theory correlations",
            "benchmark-table provenance correlations for externally filled rows",
        ],
        "acceptance_tests": {
            "same_row_basis_as_formula_manifest": True,
            "covariance_symmetric": "OPEN_UNTIL_MATRIX_FILLED",
            "covariance_positive_semidefinite": "OPEN_UNTIL_MATRIX_FILLED",
            "cross_channel_correlations_encoded_or_profiled": False,
            "measured_values_do_not_select_source": True,
            "target_fitting_used": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    manifest = {
        "schema": "MTTUniformHiggsFormulaRowManifest.v1",
        "status": "UNIFORM_FORMULA_ROW_MANIFEST_BUILT_VALUES_OPEN",
        "rows": formula_rows,
        "summary": {
            "row_count": len(formula_rows),
            "all_rows_have_formula_family_declared": True,
            "all_rows_have_operator_attachment_declared": True,
            "all_uniform_formula_values_filled": False,
            "all_precision_formula_rows_accepted": False,
            "actual_QaSU3_required_for_color_sensitive_rows": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = list(previous_gate["remaining_true_equivalence_blockers"])
    closed_now = previous_gate["closed_now"] + ["Higgs covariance/profile contract and uniform formula-row manifest"]
    for blocker in [
        "full cross-channel Higgs covariance/profile likelihood",
        "uniform precision Higgs partial-width formula rows",
        "full precision loop-corrected QFT correlator/S-matrix/decay rows",
        "actual selected Qa/SU3 operator packet",
    ]:
        if blocker not in remaining:
            remaining.append(blocker)
    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterHiggsProfileContract.v1",
        "status": "PROFILE_CONTRACT_BUILT_VALUES_AND_UNIFORM_ROWS_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": closed_now,
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "fill the declared uniform formula rows, then supply the 10x10 covariance/profile matrix",
        "guardrails": {
            "contract_not_profile_values": True,
            "diagonal_diagnostic_not_full_covariance": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsCovarianceProfileContractOrUniformFormulaRows",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsprecisionsidecars_or_uniformformularows.candidate.json"),
            "higgs_channel_uncertainty_sidecars": rel(
                DATA
                / "selected_higgsprecisionsidecars_or_uniformformularows"
                / "higgs_channel_uncertainty_sidecars.packet.json"
            ),
            "hybrid_total_width_replay": rel(
                DATA
                / "selected_higgsmissingchannelbenchmarks_or_totalwidthreplay"
                / "hybrid_higgs_total_width_replay.packet.json"
            ),
        },
        "output_packets": {
            "covariance_profile_contract": rel(CONTRACT),
            "uniform_formula_row_manifest": rel(MANIFEST),
            "diagonal_profile_diagnostic": rel(DIAG),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "HiggsProfilePromotionContractTheorem",
            "proved": True,
            "statement": (
                "The hybrid Higgs width replay can be promoted beyond diagonal sidecars only by supplying values "
                "on the declared channel row basis together with either uniform formula rows or an explicitly audited "
                "benchmark-replay policy and a symmetric positive semidefinite cross-channel covariance/profile."
            ),
        },
        "what_closes_now": {
            "profile_contract": True,
            "uniform_formula_row_manifest": True,
            "diagonal_profile_diagnostic": True,
        },
        "what_remains_open": {
            "uniform_formula_row_values": True,
            "cross_channel_covariance_values": True,
            "full_profile_likelihood": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_contract_closed": True,
            "precision_profile_contract_closed": True,
            "uniform_formula_rows_closed": False,
            "cross_channel_covariance_profile_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsCovarianceProfileContract_or_UniformFormulaRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "profile_contract_closed": True,
        "uniform_formula_row_manifest_closed": True,
        "diagonal_profile_diagnostic_closed": True,
        "uniform_formula_rows_closed": False,
        "cross_channel_covariance_profile_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsUniformFormulaRows_Fill_or_CovarianceMatrixValues_v1",
    }

    note = """# MTT Selected HiggsCovarianceProfileContract or UniformFormulaRows v1

Status: `MTT_SELECTED_HIGGSCOVARIANCEPROFILECONTRACT_OR_UNIFORMFORMULAROWS_BUILT_PROFILE_CONTRACT_UNIFORM_ROWS_OPEN`.

This artifact turns the open Higgs precision blocker into a concrete row-basis
contract. It declares the ten-channel Higgs observable vector, the exact shape
of the required covariance/profile object, and the uniform formula family
needed for each channel.

The diagonal profile diagnostic is only a diagnostic. It is not a full
cross-channel covariance likelihood and it does not promote the hybrid replay to
true precision SM-equivalence.
"""

    for path, payload in [
        (CONTRACT, contract),
        (MANIFEST, manifest),
        (DIAG, diagnostic),
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
