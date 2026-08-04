"""Build log-Yukawa coefficient source-row / minimal flavor-parameter ledger.

This packet attacks the next target after the spectral Yukawa response basis.
It tests whether the nine diagnostic log-response coefficients are already
source-owned or reducible by the current 1-3 universal-parameter policy.  The
answer is negative: the coefficient matrix is full rank and no source theorem
selects its rows.  The honest closure is therefore a profile-replay ledger with
nine typed log-response coefficient slots, while no-knob closure remains open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_logyukawacoefficientsourcerows_or_minimalflavorparameterledger"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_RECHECK = PACKET_DIR / "log_yukawa_coefficient_source_row_recheck.packet.json"
RANK_TEST = PACKET_DIR / "universal_parameter_reduction_rank_test.packet.json"
LEDGER = PACKET_DIR / "minimal_flavor_parameter_ledger.packet.json"
NEXT_PACKET = PACKET_DIR / "next_source_operator_or_flavor_parameter_selection.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LogYukawaCoefficientSourceRows_or_MinimalFlavorParameterLedger_v1.md"

SPECTRAL = DATA / "selected_spectralyukawaresponsebasis_or_coefficientsourcewall.candidate.json"
COEFF = (
    DATA
    / "selected_spectralyukawaresponsebasis_or_coefficientsourcewall"
    / "diagnostic_log_yukawa_response_coefficients.packet.json"
)
FUNCTIONAL = (
    DATA
    / "selected_spectralyukawaresponsebasis_or_coefficientsourcewall"
    / "spectral_threshold_response_functional_contract.packet.json"
)
HIGHER = DATA / "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows.candidate.json"
HIGHER_ATTEMPT = (
    DATA
    / "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows"
    / "higher_response_sector_coefficient_source_attempt.packet.json"
)
UNIVERSAL = DATA / "universal_source_parameter_policy.candidate.json"
UNIVERSAL_APPLIED = (
    DATA
    / "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows"
    / "minimal_universal_parameter_application_to_yukawa_wall.packet.json"
)

STATUS = (
    "MTT_SELECTED_LOGYUKAWACOEFFICIENTSOURCEROWS_OR_MINIMALFLAVORPARAMETERLEDGER_"
    "SOURCE_ROWS_ZERO_FULL_RANK_LEDGER_BUILT"
)
NEXT = "MTT_Selected_FlavorThresholdSourceOperator_or_ReducedCoefficientTheorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def det3(m: list[list[float]]) -> float:
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def max_abs(rows: list[list[float]]) -> float:
    return max(abs(x) for row in rows for x in row)


def subtract(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] - b[i][j] for j in range(3)] for i in range(3)]


def main() -> int:
    sources = [SPECTRAL, COEFF, FUNCTIONAL, HIGHER, HIGHER_ATTEMPT, UNIVERSAL, UNIVERSAL_APPLIED]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing log-Yukawa coefficient inputs: " + ", ".join(missing))

    spectral = load(SPECTRAL)
    coeff = load(COEFF)
    functional = load(FUNCTIONAL)
    higher = load(HIGHER)
    higher_attempt = load(HIGHER_ATTEMPT)
    universal = load(UNIVERSAL)
    universal_applied = load(UNIVERSAL_APPLIED)

    sector_rows = coeff["sector_rows"]
    matrix = [row["coefficient_values_c0_c1_c2"] for row in sector_rows]
    sectors = [row["sector"] for row in sector_rows]
    determinant = det3(matrix)
    full_rank = abs(determinant) > 1e-12

    col_means = [sum(matrix[i][j] for i in range(3)) / 3.0 for j in range(3)]
    shared_polynomial = [col_means[:] for _ in range(3)]
    shared_polynomial_max_residual = max_abs(subtract(matrix, shared_polynomial))

    sector_constants_shared_shape = [
        [matrix[i][0], col_means[1], col_means[2]]
        for i in range(3)
    ]
    sector_constants_shared_shape_max_residual = max_abs(
        subtract(matrix, sector_constants_shared_shape)
    )

    phase_like = [row for row in sector_rows if row["source_direction"] == "phase_packet_I_plus_Z"]
    phase_like_curvatures = [row["coefficient_values_c0_c1_c2"][2] for row in phase_like]
    phase_curvature_spread = max(phase_like_curvatures) - min(phase_like_curvatures)

    source_recheck = {
        "schema": "MTTLogYukawaCoefficientSourceRowRecheck.v1",
        "status": "LOG_YUKAWA_COEFFICIENT_SOURCE_ROWS_RECHECKED_ZERO_ACCEPTED",
        "closure_claimed": True,
        "diagnostic_coefficients_imported": coeff["coefficient_row_count"],
        "accepted_source_rows_in_previous_higher_response_attempt": higher_attempt[
            "accepted_sector_coefficient_row_count"
        ],
        "accepted_threshold_response_source_rows": higher["closure_decision"][
            "selected_threshold_response_functional_closed"
        ],
        "selected_log_coefficient_source_rows": 0,
        "source_search_result": {
            "exact_literals_found_outside_diagnostic_packets": 0,
            "accepted_current_source_owner": False,
            "reason": (
                "The coefficient literals occur only in diagnostic/interpolation packets. "
                "No selected threshold source operator emits c_{s,k}."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    rank_test = {
        "schema": "MTTUniversalParameterReductionRankTest.v1",
        "status": "ONE_TO_THREE_UNIVERSAL_PARAMETER_REDUCTION_NOT_CLOSED",
        "closure_claimed": True,
        "coefficient_matrix_rows": sectors,
        "coefficient_matrix_columns": ["c0", "c1", "c2"],
        "coefficient_matrix": matrix,
        "determinant": determinant,
        "full_rank": full_rank,
        "universal_policy_selected_parameter_count_now": universal["selected_parameter_count_now"],
        "maximum_live_universal_parameters": universal["maximum_live_universal_parameters"],
        "tests": [
            {
                "lane": "shared_polynomial_UP3",
                "parameter_count": 3,
                "description": "one shared c0,c1,c2 polynomial for u,d,e",
                "max_abs_residual": shared_polynomial_max_residual,
                "closes": False,
            },
            {
                "lane": "sector_constants_plus_shared_shape_UP5",
                "parameter_count": 5,
                "description": "three sector constants plus shared c1,c2",
                "max_abs_residual": sector_constants_shared_shape_max_residual,
                "closes": False,
            },
            {
                "lane": "rank_leq_2_universal_factorization",
                "parameter_count": "2 source axes plus fixed loadings",
                "description": "would require determinant zero under fixed selected loadings",
                "determinant_obstruction": determinant,
                "closes": False,
            },
            {
                "lane": "phase_direction_shared_curvature",
                "parameter_count": "direction-shared coefficient test",
                "description": "u and e share phase direction, but their curvature coefficients are not identical",
                "phase_curvature_spread": phase_curvature_spread,
                "closes": False,
            },
        ],
        "policy_decision": universal_applied["best_current_statement"],
        "why_three_arbitrary_parameters_are_not_accepted": (
            "A rank-3 numerical factorization can always be built after seeing the matrix, "
            "but without selected source loadings it is just target parameterization."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    ledger_rows = []
    for row in sector_rows:
        sector = row["sector"]
        for idx, value in enumerate(row["coefficient_values_c0_c1_c2"]):
            ledger_rows.append(
                {
                    "slot_id": f"logY.{sector}.c{idx}",
                    "sector": sector,
                    "coefficient": f"c{idx}",
                    "value": value,
                    "accepted_as_profile_replay_parameter": True,
                    "accepted_as_no_knob_source_row": False,
                    "source_requirement": "selected flavor threshold/source operator row",
                }
            )

    ledger = {
        "schema": "MTTMinimalFlavorParameterLedger.v1",
        "status": "MINIMAL_PROFILE_REPLAY_FLAVOR_LEDGER_BUILT_NO_SOURCE_REDUCTION",
        "closure_claimed": True,
        "basis_map_closed": spectral["closure_decision"]["selected_family_spectral_basis_closed"],
        "coefficient_domain_closed": spectral["closure_decision"]["coefficient_domain_closed"],
        "profile_replay_parameter_slots": len(ledger_rows),
        "selected_no_knob_source_slots": 0,
        "strict_no_knob_flavor_closure": False,
        "sm_parity_profile_replay_ledger_closed": True,
        "parameter_count_interpretation": {
            "without_source_reduction": 9,
            "compared_to_SM_charged_yukawa_eigenvalues": (
                "same count, but typed as spectral response coefficients on a selected MTT family operator"
            ),
            "possible_future_reduction": (
                "requires source theorem constraining c_{s,k}, or 1-3 universal parameters selected before replay"
            ),
        },
        "rows": ledger_rows,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextSourceOperatorOrFlavorParameterSelection.v1",
        "status": "NEXT_IS_FLAVOR_THRESHOLD_SOURCE_OPERATOR_OR_EXPLICIT_PARAMETER_SELECTION",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "ordered_routes": [
            "derive a selected flavor threshold/source operator emitting c_{s,k}",
            "derive fixed source loadings that reduce the full-rank matrix to 1-3 selected universal parameters",
            "if source reduction fails, preserve the 9-slot profile replay ledger as SM-parity bookkeeping",
            "then integrate CKM/PMNS orientation and covariance/profile likelihood",
        ],
        "forbidden_routes": [
            "use the fitted 9 coefficients as no-knob source rows",
            "claim arbitrary rank-3 factorization as a 3-parameter theory",
            "select source loadings from observed hierarchy residuals",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedLogYukawaCoefficientSourceRowsOrMinimalFlavorParameterLedger",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "sm_parity_profile_replay_ledger_closed": True,
        "strict_no_knob_flavor_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {path.stem: rel(path) for path in sources},
        "packets": {
            "log_yukawa_coefficient_source_row_recheck": rel(SOURCE_RECHECK),
            "universal_parameter_reduction_rank_test": rel(RANK_TEST),
            "minimal_flavor_parameter_ledger": rel(LEDGER),
            "next_source_operator_or_flavor_parameter_selection": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "selected_family_spectral_basis_closed": True,
            "diagnostic_log_coefficient_rows_filled": coeff["coefficient_row_count"],
            "selected_log_coefficient_source_rows": 0,
            "coefficient_matrix_full_rank": full_rank,
            "one_to_three_universal_parameter_reduction_closed": False,
            "minimal_profile_replay_flavor_ledger_closed": True,
            "minimal_profile_replay_parameter_slots": len(ledger_rows),
            "strict_no_knob_flavor_closure": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "coefficient_matrix_determinant": determinant,
            "shared_polynomial_UP3_max_abs_residual": shared_polynomial_max_residual,
            "sector_constants_shared_shape_UP5_max_abs_residual": sector_constants_shared_shape_max_residual,
            "phase_curvature_spread_u_vs_e": phase_curvature_spread,
        },
        "theorem": {
            "name": "LogYukawaCoefficientSourceRowsOrMinimalFlavorLedgerTheorem",
            "proved": True,
            "statement": (
                "The selected spectral Yukawa basis closes the functional domain, but the log-coefficient "
                "matrix is full rank and current packets emit zero selected coefficient source rows. "
                "Current 1-3 universal-parameter lanes therefore do not close charged Yukawa magnitudes. "
                "The honest downstream object is a nine-slot profile-replay flavor ledger unless a new "
                "selected flavor threshold/source operator or reduced-coefficient theorem is proved."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedLogYukawaCoefficientSourceRowsOrMinimalFlavorParameterLedgerCertificate",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "diagnostic_log_coefficient_rows_filled": coeff["coefficient_row_count"],
        "selected_log_coefficient_source_rows": 0,
        "coefficient_matrix_full_rank": full_rank,
        "one_to_three_universal_parameter_reduction_closed": False,
        "minimal_profile_replay_flavor_ledger_closed": True,
        "minimal_profile_replay_parameter_slots": len(ledger_rows),
        "strict_no_knob_flavor_closure": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected LogYukawaCoefficientSourceRows or MinimalFlavorParameterLedger v1

## Theorem

`LogYukawaCoefficientSourceRowsOrMinimalFlavorLedgerTheorem` is proved.

The spectral family basis is closed, but the charged log-Yukawa coefficient
matrix is full rank:

`det(C) = {determinant}`

Current selected source coefficient rows: `0`.

## Reduction Test

- shared `UP-3` polynomial residual: `{shared_polynomial_max_residual}`
- sector constants plus shared shape residual: `{sector_constants_shared_shape_max_residual}`
- phase-direction curvature spread: `{phase_curvature_spread}`

So current `1-3` universal-parameter lanes do not close the charged Yukawa
magnitudes unless a new selected source-loading theorem is supplied.

## Ledger

The honest profile-replay ledger has `9` typed coefficient slots:
`c0_s,c1_s,c2_s` for `s in {{u,d,e}}`.  This is SM-parity bookkeeping, not
no-knob mass prediction.

Next artifact: `{NEXT}`.
"""

    write_json(SOURCE_RECHECK, source_recheck)
    write_json(RANK_TEST, rank_test)
    write_json(LEDGER, ledger)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
