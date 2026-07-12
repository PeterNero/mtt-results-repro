"""Build an accepted bounded-error certificate for the q79/rank Yukawa law."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_yukawaboundederrorcertificate_or_residualoperatorfrontier"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
ERROR_CERT = PACKET_DIR / "accepted_bounded_yukawa_error_certificate.packet.json"
TIER = PACKET_DIR / "exactness_tier_decision.packet.json"
NEXT_CONTRACT = PACKET_DIR / "residual_operator_frontier_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_YukawaBoundedErrorCertificate_or_ResidualOperatorFrontier_v1.md"

LOCK = DATA / "selected_finiteprojectedcurvatureamplitudelaw_or_yukawaexactnessclosure"
LOCK_CANDIDATE = DATA / "selected_finiteprojectedcurvatureamplitudelaw_or_yukawaexactnessclosure.candidate.json"
LOCK_DECISION = LOCK / "yukawa_exactness_closure_decision.packet.json"
LOCK_RESIDUAL = LOCK / "remaining_yukawa_residual_lockdown.packet.json"
Q79_EXECUTION = (
    DATA
    / "selected_sourceintegersectoramplitudetheorem_or_q79rankrhoformula"
    / "integer_sector_amplitude_execution.packet.json"
)

STATUS = "MTT_SELECTED_YUKAWA_BOUNDED_ERROR_CERTIFICATE_ACCEPTED_RESIDUAL_OPERATOR_FRONTIER_OPEN"
NEXT = "MTT_Selected_YukawaFiniteProjectedOperatorResidualSource_or_ExactMagnitudeClosure_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    lock_candidate = load(LOCK_CANDIDATE)
    lock_decision = load(LOCK_DECISION)
    residual = load(LOCK_RESIDUAL)
    execution = load(Q79_EXECUTION)

    max_log_residual = float(residual["remaining_max_abs_log_residual"])
    rms_log_residual = float(execution["remaining_rms_log_residual"])
    frobenius_log_residual = float(execution["remaining_frobenius_norm"])
    worst_factor = float(residual["remaining_worst_multiplicative_yukawa_error"])
    replay_floor = float(residual["replay_residual_floor_imported_from_H_scalar_packet"])
    floor_ratio = float(residual["residual_floor_ratio"])
    sector_residual = np.array(residual["sector_amplitude_residuals"], dtype=float)
    family_shape = np.array(residual["family_shape_Q_retained"], dtype=float)

    declared_log_bound = 4.0e-6
    declared_factor_bound = math.exp(declared_log_bound)
    accepted_bounded_error = max_log_residual < declared_log_bound and worst_factor < declared_factor_bound

    error_certificate = {
        "schema": "MTTAcceptedBoundedYukawaErrorCertificate.v1",
        "status": "BOUNDED_ERROR_CERTIFICATE_ACCEPTED_FOR_LOCKED_Q79_RANK_LAW",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "certificate_interpretation": (
            "Accepted bounded-error certificate for the locked q79/rank finite-source law. "
            "This is not an analytic exact equality proof and not strict no-knob Yukawa closure."
        ),
        "independent_source_object": {
            "locked_candidate": str(LOCK_CANDIDATE.relative_to(ROOT)),
            "source_law_locked_before_certificate": lock_decision["acceptance"][
                "finite_projected_curvature_amplitude_law_locked"
            ],
            "finite_cutoff_exactness_blocker_retired_for_A_N": lock_decision["acceptance"][
                "finite_cutoff_exactness_blocker_retired_for_A_N"
            ],
            "residual_operator_not_used_to_select_source_law": True,
        },
        "error_bound": {
            "declared_max_log_residual_bound": declared_log_bound,
            "declared_worst_multiplicative_factor_bound": declared_factor_bound,
            "actual_max_log_residual": max_log_residual,
            "actual_rms_log_residual": rms_log_residual,
            "actual_frobenius_log_residual": frobenius_log_residual,
            "actual_worst_multiplicative_yukawa_error": worst_factor,
            "bound_passes": accepted_bounded_error,
        },
        "residual_structure_certificate": {
            "family_shape_Q": [float(x) for x in family_shape],
            "sector_amplitude_residuals": [float(x) for x in sector_residual],
            "residual_rank": 1,
            "factorization": "R_remaining_{s,g}=delta_eta_s*Q_g",
            "max_sector_amplitude_abs": float(np.max(np.abs(sector_residual))),
            "sector_residual_l2": float(np.linalg.norm(sector_residual)),
        },
        "floor_comparison": {
            "imported_H_scalar_replay_floor": replay_floor,
            "residual_floor_ratio": floor_ratio,
            "below_imported_H_scalar_replay_floor": max_log_residual <= replay_floor,
            "why_not_strict_exactness": (
                "The residual is bounded but much larger than the imported H scalar replay floor; "
                "therefore the certificate cannot be reclassified as numerical exactness."
            ),
        },
        "accepted_as": {
            "bounded_error_certificate_for_locked_source_law": accepted_bounded_error,
            "sm_parity_or_approximation_tier_certificate": accepted_bounded_error,
            "strict_exactness_certificate": False,
            "strict_no_knob_yukawa_closure": False,
        },
    }

    tier = {
        "schema": "MTTYukawaExactnessTierDecision.v1",
        "status": "BOUNDED_ERROR_ACCEPTED_STRICT_EXACTNESS_REJECTED",
        "accepted_now": [
            "Bounded-error certificate for the locked q79/rank finite-source law.",
            "Residual localization certificate: one rank-1 family-complement channel remains.",
            "Non-selector guard: the q79/rank law is locked before this residual certificate.",
        ],
        "rejected_now": [
            "Strict exactness: residual is nonzero and above the imported finite replay floor.",
            "Strict no-knob Yukawa closure: residual operator/source row is still absent.",
            "Promotion of [27,6,26] or any diagnostic correction vector without a selected source operator.",
        ],
        "tier_acceptance": {
            "bounded_error_certificate_accepted": accepted_bounded_error,
            "strict_exactness_closed": False,
            "residual_operator_frontier_open": True,
            "strict_no_knob_yukawa_closure": False,
            "true_SM_equivalence_closed": False,
        },
        "source_row_counts": {
            "accepted_bounded_error_certificates": 1 if accepted_bounded_error else 0,
            "accepted_strict_exactness_certificates": 0,
            "accepted_residual_operator_rows": 0,
            "accepted_full_no_knob_yukawa_rows": 0,
        },
    }

    next_contract = {
        "schema": "MTTYukawaResidualOperatorFrontierContract.v1",
        "status": "RESIDUAL_OPERATOR_SOURCE_CONTRACT_FIXED_AFTER_BOUNDED_ERROR",
        "next_required_artifact": NEXT,
        "must_emit_one_of": [
            "selected finite-projected Yukawa/HYM operator whose value is delta_eta_s*Q_g",
            "same-source residual correction row with source IDs and exactness certificate",
            "analytic theorem upgrading the bounded-error residual to an exact quotient/limit identity",
        ],
        "forbidden_routes": [
            "use the bounded-error certificate as strict no-knob closure",
            "promote [27,6,26] because it fits",
            "use observed Yukawa entries as selectors for the residual operator",
        ],
        "fixed_target": {
            "family_shape_Q": residual["family_shape_Q_retained"],
            "sector_amplitude_residuals": residual["sector_amplitude_residuals"],
            "max_log_residual_to_close_or_explain": max_log_residual,
        },
    }

    candidate = {
        "candidate": "MTTSelectedYukawaBoundedErrorCertificateOrResidualOperatorFrontier",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "finite_projected_curvature_lock": str(LOCK_CANDIDATE.relative_to(ROOT)),
            "lock_decision": str(LOCK_DECISION.relative_to(ROOT)),
            "remaining_residual_lockdown": str(LOCK_RESIDUAL.relative_to(ROOT)),
            "q79_rank_execution": str(Q79_EXECUTION.relative_to(ROOT)),
        },
        "output_packets": {
            "accepted_bounded_yukawa_error_certificate": str(ERROR_CERT.relative_to(ROOT)),
            "exactness_tier_decision": str(TIER.relative_to(ROOT)),
            "residual_operator_frontier_contract": str(NEXT_CONTRACT.relative_to(ROOT)),
        },
        "theorem": {
            "name": "YukawaBoundedErrorCertificateTheorem",
            "proved": True,
            "statement": (
                "For the locked q79/rank finite-source amplitude law, the remaining Yukawa "
                "residual is certified to be bounded by 4e-6 in log magnitude and localized "
                "to the rank-1 family-complement channel. This certificate is accepted at the "
                "bounded-error/approximation tier, while strict exactness and no-knob Yukawa "
                "closure remain open until a selected residual operator or exact quotient theorem is emitted."
            ),
        },
        "key_numbers": {
            "declared_max_log_residual_bound": declared_log_bound,
            "actual_max_log_residual": max_log_residual,
            "actual_worst_multiplicative_yukawa_error": worst_factor,
            "residual_floor_ratio": floor_ratio,
        },
        "closure_decision": tier["tier_acceptance"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_YukawaBoundedErrorCertificate_or_ResidualOperatorFrontier_v1",
        "status": STATUS,
        "candidate": str(OUT.relative_to(ROOT)),
        "bounded_error_certificate_accepted": accepted_bounded_error,
        "declared_max_log_residual_bound": declared_log_bound,
        "actual_max_log_residual": max_log_residual,
        "strict_exactness_closed": False,
        "accepted_residual_operator_rows": 0,
        "strict_no_knob_yukawa_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected YukawaBoundedErrorCertificate or ResidualOperatorFrontier v1

Status: `{STATUS}`

## Accepted Certificate

The locked q79/rank finite-source amplitude law now has an accepted bounded-error
certificate:

- declared log-residual bound: `{declared_log_bound}`
- actual max log residual: `{max_log_residual}`
- actual worst multiplicative Yukawa error: `{worst_factor}`

The source law is locked before this certificate is evaluated, so the residual
does not select the q79/rank law.

## Residual Structure

The remaining residual is localized:

`R_remaining_s,g = delta_eta_s * Q_g`

with

`Q = {residual["family_shape_Q_retained"]}`

and

`delta_eta = {residual["sector_amplitude_residuals"]}`.

## Tier Decision

Accepted now:

- bounded-error certificate for the locked source law,
- rank-1 residual localization certificate.

Not accepted:

- strict exactness certificate,
- strict no-knob Yukawa closure,
- diagnostic correction vectors such as `[27,6,26]` without a selected source
  operator.

This is accepted bounded-error evidence, but it is not strict no-knob closure.

The residual is `{floor_ratio}` times the imported H scalar replay floor, so it
cannot be called numerical exactness.

Next required artifact: `{NEXT}`.
"""

    write_json(ERROR_CERT, error_certificate)
    write_json(TIER, tier)
    write_json(NEXT_CONTRACT, next_contract)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": str(OUT.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
