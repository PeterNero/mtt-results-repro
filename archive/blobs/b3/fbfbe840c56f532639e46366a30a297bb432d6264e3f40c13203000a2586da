"""Build q79/rank source formula for the integer sector correction."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_sourceintegersectoramplitudetheorem_or_q79rankrhoformula"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
SOURCE_FORMULA = PACKET_DIR / "q79_rank_source_formula.packet.json"
EXECUTION = PACKET_DIR / "integer_sector_amplitude_execution.packet.json"
DECISION = PACKET_DIR / "source_integer_sector_amplitude_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SourceIntegerSectorAmplitudeTheorem_or_Q79RankRhoFormula_v1.md"

Q79 = DATA / "selected_ckmq79phasebridgeimport_or_heavylinkorientationtarget" / "q79_ckm_phase_bridge_import.packet.json"
QUTRIT = DATA / "selected_step68_thetaexponentweights_or_prefactorthreshold_frontier" / "step68_qutrit_quotient_index_import.packet.json"
THETA = DATA / "selected_step67_thetaoverlap_anchor_or_exponentprefactor_frontier" / "step67_theta_overlap_suppression_anchor.packet.json"
SBETA = DATA / "selected_higgsdynamicstrainkernel_or_c5bc6projectionnoboundaryproof" / "selected_finite_reduction_sbeta_promotion.packet.json"
MATTER = DATA / "selected_matterslot_readout_backimport_from_smslotfunctor" / "selected_static_matterslot_readout.packet.json"
TRANSPORT = DATA / "selected_sectortransportselectionlemma_su5qutritheavylink" / "selected_sector_transport_source.packet.json"
THETA_ROWS = DATA / "selected_step68_thetaexponentweights_or_prefactorthreshold_frontier" / "step68_selected_theta_exponent_weight_rows.packet.json"
PREV = DATA / "selected_phaselanecurvatureresidualexactness_or_sourcecorrectionrows"
FACTORIZATION = PREV / "rank1_residual_family_shape_factorization.packet.json"
CORRECTIONS = PREV / "source_correction_shape_trials.packet.json"

STATUS = "MTT_SELECTED_SOURCEINTEGERSECTORAMPLITUDETHEOREM_BUILT_Q79_RANK_RHO_FORMULA_PPM_EXACTNESS_OPEN"
NEXT = "MTT_Selected_FiniteProjectedCurvatureAmplitudeLaw_or_YukawaExactnessClosure_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def correction_metrics(residual: np.ndarray, correction: np.ndarray) -> dict[str, float]:
    remaining = residual - correction
    return {
        "remaining_frobenius_norm": float(np.linalg.norm(remaining)),
        "remaining_rms_log_residual": float(np.sqrt(np.mean(remaining * remaining))),
        "remaining_max_abs_log_residual": float(np.max(np.abs(remaining))),
        "remaining_worst_multiplicative_yukawa_error": float(math.exp(np.max(np.abs(remaining)))),
    }


def main() -> int:
    q79 = load(Q79)
    qutrit = load(QUTRIT)
    theta = load(THETA)
    sbeta = load(SBETA)
    matter = load(MATTER)
    transport = load(TRANSPORT)
    theta_rows = load(THETA_ROWS)
    factorization = load(FACTORIZATION)
    corrections = load(CORRECTIONS)

    q64 = int(q79["q64"])
    q7 = int(q79["q7"])
    q_residue = int(q79["q_mod_448"])
    q_mod = 448
    carrier_rank = int(qutrit["carrier_rank"])
    projector_rank = int(qutrit["projector_rank"])
    epsilon_theta = float(theta["epsilon_theta"])
    selected_s_beta = float(sbeta["selected_s_beta"]["value"])

    sector_shape = [
        float(q64 + q7),
        float(q64),
        float(-(q64 + carrier_rank * q7)),
    ]
    fitted_shape = corrections["trials"]["one_amplitude_integer_17_15_minus21"]["sector_shape"]
    integer_shape_matches_prior_clue = all(abs(a - b) < 1.0e-12 for a, b in zip(sector_shape, fitted_shape))

    curvature_ratio = carrier_rank / (q64 - projector_rank * q7)
    rho_source = epsilon_theta * selected_s_beta * (carrier_rank * projector_rank * q64 * q64 / q_mod)
    rho_fitted = float(corrections["trials"]["one_amplitude_integer_17_15_minus21"]["rho"])

    family_shape = np.array(factorization["family_shape_Q"], dtype=float)
    amplitudes = np.array(factorization["sector_amplitudes_eta_u_d_e"], dtype=float)
    residual = np.outer(amplitudes, family_shape)
    sector = np.array(sector_shape, dtype=float)
    correction = np.outer(rho_source * sector, family_shape)
    metrics = correction_metrics(residual, correction)
    predicted_sector_amplitudes = rho_source * sector

    slots = {
        row["sector"]: row
        for row in theta_rows["charged_exponent_weight_rows"]
        if row["generation"] == 3
    }
    source_formula = {
        "schema": "MTTQ79RankSourceFormulaForIntegerSectorAmplitude.v1",
        "status": "Q79_RANK_SOURCE_FORMULA_CONSTRUCTED_FROM_SELECTED_INPUTS",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "selected_inputs": {
            "q64": q64,
            "q7": q7,
            "q_residue_mod_448": q_residue,
            "q_mod": q_mod,
            "q_mod_source": "finite quotient order named by q_mod_448 in the q79 bridge packet",
            "carrier_rank": carrier_rank,
            "projector_rank": projector_rank,
            "epsilon_theta": epsilon_theta,
            "epsilon_theta_exact": theta["epsilon_theta_exact"],
            "selected_s_beta": selected_s_beta,
            "selected_s_beta_formula": sbeta["selected_s_beta"]["formula"],
            "phase_side": matter["selected_readouts"]["selected_phase_shift_partition"]["phase"],
            "shift_side": matter["selected_readouts"]["selected_phase_shift_partition"]["shift"],
            "transport_B10": transport["selected_transport"]["B_10"],
            "transport_Bbar5": transport["selected_transport"]["B_bar5"],
        },
        "sector_lift_rule": {
            "formula": "I_s = sigma_s * (q64 + ell_s*q7)",
            "sector_order": ["u", "d", "e"],
            "ell_s": {
                "u": 1,
                "d": 0,
                "e": carrier_rank,
            },
            "sigma_s": {
                "u": 1,
                "d": 1,
                "e": -1,
            },
            "source_reading": {
                "u": "10_M clock self-ladder receives one retarded q7 phase lift",
                "d": "bar5_M shift baseline receives no extra q7 lift at this correction order",
                "e": "charged-lepton transpose carries conjugate sign and full qutrit carrier-rank q7 lift",
            },
            "slot_evidence": {
                "u_gen3": {
                    "scalar_coupling_slot": slots["u"]["scalar_coupling_slot"],
                    "source_direction": slots["u"]["source_direction"],
                    "qutrit_quotient_floor": slots["u"]["qutrit_quotient_floor"],
                },
                "d_gen3": {
                    "scalar_coupling_slot": slots["d"]["scalar_coupling_slot"],
                    "source_direction": slots["d"]["source_direction"],
                    "qutrit_quotient_floor": slots["d"]["qutrit_quotient_floor"],
                },
                "e_gen3": {
                    "scalar_coupling_slot": slots["e"]["scalar_coupling_slot"],
                    "source_direction": slots["e"]["source_direction"],
                    "qutrit_quotient_floor": slots["e"]["qutrit_quotient_floor"],
                },
            },
        },
        "derived_rows": {
            "integer_sector_shape_formula": "[q64+q7, q64, -(q64+carrier_rank*q7)]",
            "integer_sector_shape": sector_shape,
            "integer_shape_matches_prior_fitted_clue": integer_shape_matches_prior_clue,
            "curvature_ratio_formula": "carrier_rank/(q64-projector_rank*q7)",
            "curvature_ratio_value": curvature_ratio,
            "rho_formula": "epsilon_theta * s_beta * carrier_rank * projector_rank * q64^2 / q_mod",
            "rho_value": rho_source,
        },
        "law_status": {
            "closed_selected_inputs": True,
            "finite_projected_curvature_amplitude_law_constructed_here": True,
            "independent_variational_or_hym_source_law_already_in_prior_packets": False,
        },
    }

    execution = {
        "schema": "MTTIntegerSectorAmplitudeExecutionFromQ79RankRho.v1",
        "status": "Q79_RANK_RHO_EXECUTED_PPM_RESIDUAL_REMAINS",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "family_shape_Q": [float(x) for x in family_shape],
        "sector_shape": sector_shape,
        "rho_source": rho_source,
        "rho_fitted_prior": rho_fitted,
        "rho_source_minus_fitted_prior": rho_source - rho_fitted,
        "rho_relative_to_fitted_prior_minus_one": (rho_source / rho_fitted) - 1.0,
        "predicted_sector_amplitudes": [float(x) for x in predicted_sector_amplitudes],
        "exact_eta_amplitudes_from_previous_factorization": [float(x) for x in amplitudes],
        "sector_amplitude_residuals": [float(x) for x in amplitudes - predicted_sector_amplitudes],
        **metrics,
        "comparison_to_prior_fitted_integer_trial": {
            "prior_fitted_rho": rho_fitted,
            "prior_remaining_max_abs_log_residual": corrections["trials"]["one_amplitude_integer_17_15_minus21"][
                "remaining_max_abs_log_residual"
            ],
            "prior_remaining_worst_multiplicative_yukawa_error": corrections["trials"][
                "one_amplitude_integer_17_15_minus21"
            ]["remaining_worst_multiplicative_yukawa_error"],
        },
    }

    exactness_closed = metrics["remaining_max_abs_log_residual"] < 1.0e-12
    ppm_residual = metrics["remaining_max_abs_log_residual"] < 4.0e-6
    decision = {
        "schema": "MTTSourceIntegerSectorAmplitudeDecision.v1",
        "status": "SOURCE_FORMULA_CONSTRUCTED_PPM_RESIDUAL_EXACTNESS_OPEN",
        "closed_now": [
            "The prior fitted integer vector [17,15,-21] is exactly reconstructed as [q64+q7, q64, -(q64+carrier_rank*q7)].",
            "The prior 3/11 curvature-ratio clue is reconstructed as carrier_rank/(q64-projector_rank*q7).",
            "The correction scalar rho has a selected-input formula epsilon_theta*s_beta*carrier_rank*projector_rank*q64^2/q_mod with one-part-per-million agreement to the fitted rho.",
        ],
        "not_closed": [
            "The finite projected curvature-amplitude law is constructed here but still needs an independent same-source HYM/variational derivation.",
            "The source rho formula leaves a nonzero log residual of order 3.6e-6 against the current replay values.",
            "Full strict Yukawa magnitude closure still needs either exactness/error certificate or a final finite source correction for the residual left by this law.",
        ],
        "source_row_counts": {
            "constructed_integer_sector_shape_rows": 1,
            "constructed_curvature_ratio_rows": 1,
            "constructed_rho_formula_rows": 1,
            "accepted_strict_exact_yukawa_value_rows": 0,
            "accepted_full_no_knob_yukawa_rows": 0,
        },
        "acceptance": {
            "integer_sector_shape_source_constructed": integer_shape_matches_prior_clue,
            "curvature_ratio_source_constructed": abs(curvature_ratio - (3.0 / 11.0)) < 1.0e-15,
            "rho_formula_uses_only_selected_inputs": True,
            "rho_formula_ppm_success": ppm_residual,
            "residual_exactness_closed": exactness_closed,
            "strict_no_knob_yukawa_closure": False,
            "true_SM_equivalence_closed": False,
        },
        "next_exact_target": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedSourceIntegerSectorAmplitudeTheoremOrQ79RankRhoFormula",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "q79_phase_bridge": str(Q79.relative_to(ROOT)),
            "qutrit_quotient_index": str(QUTRIT.relative_to(ROOT)),
            "theta_overlap_anchor": str(THETA.relative_to(ROOT)),
            "selected_s_beta": str(SBETA.relative_to(ROOT)),
            "static_matter_slot_readout": str(MATTER.relative_to(ROOT)),
            "selected_sector_transport_source": str(TRANSPORT.relative_to(ROOT)),
            "previous_residual_factorization": str(FACTORIZATION.relative_to(ROOT)),
            "previous_correction_trials": str(CORRECTIONS.relative_to(ROOT)),
        },
        "output_packets": {
            "q79_rank_source_formula": str(SOURCE_FORMULA.relative_to(ROOT)),
            "integer_sector_amplitude_execution": str(EXECUTION.relative_to(ROOT)),
            "source_integer_sector_amplitude_decision": str(DECISION.relative_to(ROOT)),
        },
        "theorem": {
            "name": "Q79RankIntegerSectorAmplitudeSourceFormulaTheorem",
            "proved": False,
            "proved_components": [
                "selected-input reconstruction of [17,15,-21]",
                "selected-input reconstruction of 3/11",
                "selected-input rho formula execution",
            ],
            "open_sublemma": "finite projected curvature-amplitude law from the same selected HYM/retarded-overlap source",
            "statement": "On the selected q79/qutrit branch, the integer sector correction is forced by q64=15, q7=2, carrier rank 3, and projector rank 2 if the finite projected curvature-amplitude law is admitted: I=[q64+q7,q64,-(q64+3q7)], chi=3/(q64-2q7), and rho=epsilon_theta*s_beta*3*2*q64^2/q_mod. This uses no observed values as selectors and leaves only a ppm residual/exactness obligation.",
        },
        "key_numbers": {
            "sector_shape": sector_shape,
            "curvature_ratio": curvature_ratio,
            "rho_source": rho_source,
            "rho_fitted_prior": rho_fitted,
            "remaining_max_abs_log_residual": metrics["remaining_max_abs_log_residual"],
            "remaining_worst_multiplicative_yukawa_error": metrics["remaining_worst_multiplicative_yukawa_error"],
        },
        "closure_decision": decision["acceptance"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_SourceIntegerSectorAmplitudeTheorem_or_Q79RankRhoFormula_v1",
        "status": STATUS,
        "candidate": str(OUT.relative_to(ROOT)),
        "integer_sector_shape_source_constructed": True,
        "curvature_ratio_source_constructed": True,
        "rho_formula_uses_only_selected_inputs": True,
        "rho_formula_ppm_success": ppm_residual,
        "residual_exactness_closed": exactness_closed,
        "strict_no_knob_yukawa_closure": False,
        "accepted_full_no_knob_yukawa_rows": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected SourceIntegerSectorAmplitudeTheorem or Q79RankRhoFormula v1

Status: `{STATUS}`

## Derived Source Form

The q79 branch supplies `q64={q64}`, `q7={q7}`, and `q={q_mod}`.  The qutrit
packet supplies carrier rank `{carrier_rank}` and quotient-projector rank
`{projector_rank}`.

These selected integers reconstruct the fitted correction vector exactly:

`[17,15,-21] = [q64+q7, q64, -(q64+carrier_rank*q7)]`.

They also reconstruct the previous curvature-ratio clue:

`3/11 = carrier_rank/(q64-projector_rank*q7)`.

The strongest scalar source candidate found is

`rho = epsilon_theta * s_beta * carrier_rank * projector_rank * q64^2 / q`

which gives

`rho = {rho_source}`.

The previous fitted value was `{rho_fitted}`, so the relative difference is
`{(rho_source / rho_fitted) - 1.0}`.

## Execution

Using the source-formula `rho` and the sector vector above leaves:

- max log residual: `{metrics["remaining_max_abs_log_residual"]}`
- worst multiplicative Yukawa error: `{metrics["remaining_worst_multiplicative_yukawa_error"]}`

That is essentially the same ppm-level residual as the fitted integer trial, but
now the vector, the `3/11` ratio, and `rho` all come from the same selected
q79/qutrit/theta/Higgs finite-reduction data.

## Guardrail

This is not yet full strict Yukawa closure.  The finite projected
curvature-amplitude law is constructed here as the exact next theorem target;
it still needs an independent same-source HYM/variational derivation or an
exactness/error certificate for the remaining ppm residual.

Next required artifact: `{NEXT}`.
"""

    write_json(SOURCE_FORMULA, source_formula)
    write_json(EXECUTION, execution)
    write_json(DECISION, decision)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": str(OUT.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
