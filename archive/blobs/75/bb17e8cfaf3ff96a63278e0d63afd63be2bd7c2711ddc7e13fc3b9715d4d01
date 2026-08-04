"""Build the finite-projected curvature-amplitude lockdown artifact."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_finiteprojectedcurvatureamplitudelaw_or_yukawaexactnessclosure"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
LAW = PACKET_DIR / "finite_projected_curvature_amplitude_law_lock.packet.json"
RESIDUAL = PACKET_DIR / "remaining_yukawa_residual_lockdown.packet.json"
DECISION = PACKET_DIR / "yukawa_exactness_closure_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FiniteProjectedCurvatureAmplitudeLaw_or_YukawaExactnessClosure_v1.md"

SOURCE = DATA / "selected_sourceintegersectoramplitudetheorem_or_q79rankrhoformula"
SOURCE_CANDIDATE = DATA / "selected_sourceintegersectoramplitudetheorem_or_q79rankrhoformula.candidate.json"
SOURCE_FORMULA = SOURCE / "q79_rank_source_formula.packet.json"
SOURCE_EXECUTION = SOURCE / "integer_sector_amplitude_execution.packet.json"
FINITE_A_N = DATA / "selected_finiteprojectedhymsourceprinciple_or_bandlimitexactnessproof.candidate.json"
H_SCALAR = DATA / "selected_hscalarfunctionalonfiniteprojectedhymalgebra_or_halfdensitysourcerule.candidate.json"

STATUS = "MTT_SELECTED_FINITEPROJECTEDCURVATUREAMPLITUDELAW_LOCKED_SOURCE_FORMULA_EXACTNESS_OPEN"
NEXT = "MTT_Selected_YukawaFiniteProjectedOperatorResidualSource_or_ExactMagnitudeClosure_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def projection_trial(residual: np.ndarray, vector: list[float], source_status: str) -> dict[str, object]:
    v = np.array(vector, dtype=float)
    coeff = float((residual @ v) / (v @ v))
    rem = residual - coeff * v
    return {
        "vector": [float(x) for x in v],
        "coefficient": coeff,
        "max_abs_remaining_sector_amplitude": float(np.max(np.abs(rem))),
        "l2_remaining_sector_amplitude": float(np.linalg.norm(rem)),
        "accepted_as_source_correction": False,
        "source_status": source_status,
    }


def main() -> int:
    source_candidate = load(SOURCE_CANDIDATE)
    formula = load(SOURCE_FORMULA)
    execution = load(SOURCE_EXECUTION)
    finite_a_n = load(FINITE_A_N)
    h_scalar = load(H_SCALAR)

    sector_residual = np.array(execution["sector_amplitude_residuals"], dtype=float)
    max_log_residual = float(execution["remaining_max_abs_log_residual"])
    replay_floor = float(h_scalar["numerics"]["replay_residual_floor"])
    residual_floor_ratio = max_log_residual / replay_floor

    trials = {
        "selected_integer_law_vector": projection_trial(
            sector_residual,
            execution["sector_shape"],
            "already consumed by the source rho law; remaining projection is only rho_source-rho_fit and cannot be reused",
        ),
        "phase_side_u_e": projection_trial(
            sector_residual,
            [1.0, 0.0, 1.0],
            "source-shaped phase-side support only; does not close the down-sector amplitude and has no finite amplitude law",
        ),
        "abs_charge_units": projection_trial(
            sector_residual,
            [2.0, 1.0, 3.0],
            "external SM-charge-shaped diagnostic; selected representation/charge packet is not a no-knob value source here",
        ),
        "carrier_boundary_27_6_26": projection_trial(
            sector_residual,
            [27.0, 6.0, 26.0],
            "best small-integer diagnostic; rejected because no selected slot law emits this vector as a Yukawa correction",
        ),
    }

    law = {
        "schema": "MTTFiniteProjectedCurvatureAmplitudeLawLock.v1",
        "status": "SOURCE_FORMULA_LOCKED_FINITE_EXACTNESS_AVAILABLE_BUT_NOT_YUKAWA_EXACTNESS",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_formula_status": formula["status"],
        "selected_source_formula": {
            "sector_shape": formula["derived_rows"]["integer_sector_shape"],
            "sector_shape_formula": formula["derived_rows"]["integer_sector_shape_formula"],
            "curvature_ratio": formula["derived_rows"]["curvature_ratio_value"],
            "curvature_ratio_formula": formula["derived_rows"]["curvature_ratio_formula"],
            "rho": formula["derived_rows"]["rho_value"],
            "rho_formula": formula["derived_rows"]["rho_formula"],
        },
        "finite_projected_source_support": {
            "A_N_exactness_closed": finite_a_n["closure_decision"]["automatic_finite_cutoff_exactness_for_A_N_closed"],
            "finite_projected_HYM_source_principle_closed": finite_a_n["closure_decision"][
                "finite_projected_HYM_source_principle_closed"
            ],
            "H_scalar_functional_on_A_N_closed": h_scalar["closure_decision"]["H_scalar_functional_on_A_N_closed"],
            "strict_tau_H_promoted": h_scalar["closure_decision"]["strict_tau_H_promoted"],
            "strict_r_H_promoted": h_scalar["closure_decision"]["strict_r_H_promoted"],
        },
        "lockdown_theorem": {
            "proved": True,
            "statement": (
                "The q79/rank/theta/s_beta amplitude formula is the locked selected-input "
                "finite-projected curvature-amplitude law currently emitted by the repo. "
                "Finite A_N exactness is available for selected finite source operations, "
                "but it does not by itself prove equality to the downstream Yukawa replay "
                "targets; the remaining residual requires a Yukawa-specific source operator "
                "or an accepted error/tolerance model."
            ),
        },
    }

    residual = {
        "schema": "MTTRemainingYukawaResidualLockdown.v1",
        "status": "PPM_RESIDUAL_LOCALIZED_NO_ACCEPTED_SOURCE_CORRECTION",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "family_shape_Q_retained": execution["family_shape_Q"],
        "sector_amplitude_residuals": execution["sector_amplitude_residuals"],
        "remaining_max_abs_log_residual": max_log_residual,
        "remaining_worst_multiplicative_yukawa_error": execution["remaining_worst_multiplicative_yukawa_error"],
        "replay_residual_floor_imported_from_H_scalar_packet": replay_floor,
        "residual_floor_ratio": residual_floor_ratio,
        "too_large_for_existing_finite_replay_floor": residual_floor_ratio > 1.0e6,
        "diagnostic_correction_trials": trials,
        "best_diagnostic_trial": "carrier_boundary_27_6_26",
        "best_diagnostic_guardrail": (
            "The [27,6,26] vector is retained as a clue only. It is small-integer and close, "
            "but it is not emitted by a selected Yukawa/HYM operator and therefore cannot be "
            "used to close exactness."
        ),
    }

    decision = {
        "schema": "MTTYukawaExactnessClosureDecisionAfterQ79RankLaw.v1",
        "status": "SOURCE_LAW_LOCKED_EXACT_YUKAWA_MAGNITUDE_CLOSURE_OPEN",
        "closed_now": [
            "The q79/rank rho law is locked as the current selected-input amplitude source formula.",
            "Finite A_N source exactness and H scalar source exactness are imported as support, so finite-cutoff approximation is not the active blocker.",
            "The remaining Yukawa mismatch is localized to a single sector-amplitude residual multiplying Q=[-2,3,-1].",
            "Small correction vectors, including [27,6,26], are quarantined unless a selected Yukawa/HYM operator emits them.",
        ],
        "not_closed": [
            "No selected Yukawa finite-projected operator emits the remaining sector residual.",
            "No accepted error/tolerance model allows a 3.56e-6 log residual to count as exact source equality.",
            "Full strict Yukawa magnitude closure and true SM equivalence remain open.",
        ],
        "source_row_counts": {
            "locked_q79_rank_amplitude_laws": 1,
            "accepted_residual_correction_rows": 0,
            "accepted_exact_yukawa_magnitude_rows": 0,
            "accepted_full_no_knob_yukawa_rows": 0,
        },
        "acceptance": {
            "finite_projected_curvature_amplitude_law_locked": True,
            "finite_cutoff_exactness_blocker_retired_for_A_N": True,
            "yukawa_specific_exactness_closed": False,
            "ppm_residual_promoted_by_error_certificate": False,
            "strict_no_knob_yukawa_closure": False,
            "true_SM_equivalence_closed": False,
        },
        "next_exact_target": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedFiniteProjectedCurvatureAmplitudeLawOrYukawaExactnessClosure",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "source_integer_sector_amplitude_candidate": str(SOURCE_CANDIDATE.relative_to(ROOT)),
            "q79_rank_source_formula": str(SOURCE_FORMULA.relative_to(ROOT)),
            "q79_rank_execution": str(SOURCE_EXECUTION.relative_to(ROOT)),
            "finite_projected_A_N_exactness": str(FINITE_A_N.relative_to(ROOT)),
            "H_scalar_A_N_source": str(H_SCALAR.relative_to(ROOT)),
        },
        "output_packets": {
            "finite_projected_curvature_amplitude_law_lock": str(LAW.relative_to(ROOT)),
            "remaining_yukawa_residual_lockdown": str(RESIDUAL.relative_to(ROOT)),
            "yukawa_exactness_closure_decision": str(DECISION.relative_to(ROOT)),
        },
        "theorem": {
            "name": "FiniteProjectedCurvatureAmplitudeLawLockdownTheorem",
            "proved": True,
            "statement": law["lockdown_theorem"]["statement"],
        },
        "key_numbers": {
            "rho_source": execution["rho_source"],
            "sector_shape": execution["sector_shape"],
            "remaining_max_abs_log_residual": max_log_residual,
            "remaining_worst_multiplicative_yukawa_error": execution["remaining_worst_multiplicative_yukawa_error"],
            "residual_floor_ratio": residual_floor_ratio,
        },
        "closure_decision": decision["acceptance"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_FiniteProjectedCurvatureAmplitudeLaw_or_YukawaExactnessClosure_v1",
        "status": STATUS,
        "candidate": str(OUT.relative_to(ROOT)),
        "finite_projected_curvature_amplitude_law_locked": True,
        "finite_cutoff_exactness_blocker_retired_for_A_N": True,
        "yukawa_specific_exactness_closed": False,
        "accepted_residual_correction_rows": 0,
        "accepted_exact_yukawa_magnitude_rows": 0,
        "strict_no_knob_yukawa_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected FiniteProjectedCurvatureAmplitudeLaw or YukawaExactnessClosure v1

Status: `{STATUS}`

## What Is Locked

The q79/rank/theta/Higgs finite-reduction law from the previous artifact is now
the locked selected-input amplitude law:

`I = {execution["sector_shape"]}`

`rho = {execution["rho_source"]}`

It uses no observed masses or Yukawa entries as selectors.

The finite projected `A_N` source exactness theorem and the finite `H` scalar
source theorem are imported as support.  This means finite cutoff approximation
is not the active blocker for selected finite source operations.

## What Is Not Closed

The remaining Yukawa residual is still nonzero:

- max log residual: `{max_log_residual}`
- worst multiplicative Yukawa error: `{execution["remaining_worst_multiplicative_yukawa_error"]}`
- finite replay floor comparison: `{residual_floor_ratio}` times the imported
  H scalar replay floor

Therefore the residual cannot be counted as exactness under the currently
accepted finite replay certificate.

## Quarantined Clue

A small-integer diagnostic vector `[27,6,26]` nearly fits the remaining
sector-amplitude residual, but it is not emitted by a selected Yukawa/HYM
operator.  Equivalently, it is not emitted by a selected Yukawa/HYM operator
with a source certificate.  It is retained only as a clue.

## Decision

Closed now:

- q79/rank amplitude law locked,
- finite `A_N` exactness imported as support,
- remaining mismatch localized to one sector-amplitude residual times
  `Q=[-2,3,-1]`.

Still open:

- selected Yukawa finite-projected operator residual source,
- or accepted exactness/error certificate for the ppm residual.

Next required artifact: `{NEXT}`.
"""

    write_json(LAW, law)
    write_json(RESIDUAL, residual)
    write_json(DECISION, decision)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": str(OUT.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
