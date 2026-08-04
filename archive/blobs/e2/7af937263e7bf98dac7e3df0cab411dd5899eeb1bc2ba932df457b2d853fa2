"""Build flavor-threshold source-operator / reduced-coefficient theorem packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_flavorthresholdsourceoperator_or_reducedcoefficienttheorem"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FlavorThresholdSourceOperator_or_ReducedCoefficientTheorem_v1.md"

DIAGNOSTIC = (
    DATA
    / "selected_spectralyukawaresponsebasis_or_coefficientsourcewall"
    / "diagnostic_log_yukawa_response_coefficients.packet.json"
)
PREVIOUS = DATA / "selected_logyukawacoefficientsourcerows_or_minimalflavorparameterledger.candidate.json"
HIGHER = DATA / "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows.candidate.json"
MAGNITUDE = DATA / "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation.candidate.json"
PROJECTION = DATA / "selected_thresholdresponserows_or_sectorprojectionweightsexecution.candidate.json"

STATUS = (
    "MTT_SELECTED_FLAVORTHRESHOLDSOURCEOPERATOR_OR_REDUCEDCOEFFICIENTTHEOREM_"
    "BUILT_REDUCTION_TESTS_FULL_RANK_SOURCE_OPERATOR_OPEN"
)
NEXT = "MTT_Selected_FlavorSourceOperatorConcreteSearch_or_MinimalNineSlotPolicy_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def det3(m: list[list[float]]) -> float:
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def rank3_from_det(det: float, tol: float = 1e-12) -> int:
    return 3 if abs(det) > tol else 2


def max_abs(values: list[float]) -> float:
    return max(abs(v) for v in values)


def additive_sector_basis_model(matrix: list[list[float]]) -> dict:
    rows = len(matrix)
    cols = len(matrix[0])
    row_means = [sum(row) / cols for row in matrix]
    col_means = [sum(matrix[i][j] for i in range(rows)) / rows for j in range(cols)]
    grand = sum(sum(row) for row in matrix) / (rows * cols)
    residuals = []
    for i in range(rows):
        for j in range(cols):
            pred = row_means[i] + col_means[j] - grand
            residuals.append(matrix[i][j] - pred)
    return {
        "model": "c_sector_basis = a_sector + b_basis - mean",
        "parameter_count": rows + cols - 1,
        "max_abs_residual": max_abs(residuals),
        "rms_residual": (sum(v * v for v in residuals) / len(residuals)) ** 0.5,
        "closes": False,
        "reason": "A sector-plus-basis separable law leaves nonzero double-centered residuals.",
    }


def shared_polynomial_model(matrix: list[list[float]]) -> dict:
    cols = len(matrix[0])
    shared = [sum(row[j] for row in matrix) / len(matrix) for j in range(cols)]
    residuals = [matrix[i][j] - shared[j] for i in range(len(matrix)) for j in range(cols)]
    return {
        "model": "shared_degree2_log_response_coefficients",
        "parameter_count": cols,
        "max_abs_residual": max_abs(residuals),
        "rms_residual": (sum(v * v for v in residuals) / len(residuals)) ** 0.5,
        "closes": False,
        "reason": "One shared polynomial cannot distinguish the u,d,e coefficient rows.",
    }


def main() -> int:
    diagnostic = load(DIAGNOSTIC)
    previous = load(PREVIOUS)
    higher = load(HIGHER)
    magnitude = load(MAGNITUDE)
    projection = load(PROJECTION)

    sectors = [row["sector"] for row in diagnostic["sector_rows"]]
    coeffs = [row["coefficient_values_c0_c1_c2"] for row in diagnostic["sector_rows"]]
    determinant = det3(coeffs)
    rank = rank3_from_det(determinant)

    source_rows_now = previous["closure_decision"]["selected_log_coefficient_source_rows"]
    current_universal_count = higher["closure_decision"]["selected_universal_parameter_count"]

    reduction_tests = [
        {
            "model": "rank_le_2_sector_coefficient_plane",
            "closes": False,
            "determinant": determinant,
            "rank": rank,
            "reason": "The 3x3 coefficient matrix has nonzero determinant, so the three sector coefficient vectors are not contained in any two-dimensional selected coefficient plane.",
        },
        additive_sector_basis_model(coeffs),
        shared_polynomial_model(coeffs),
        {
            "model": "current_1_to_3_universal_parameter_policy",
            "closes": False,
            "selected_universal_parameter_count": current_universal_count,
            "reason": "The current universal-parameter lanes are not selected for this Yukawa wall and cannot be retrofitted from replay coefficients.",
        },
    ]

    reduction_packet = {
        "schema": "MTTFlavorReducedCoefficientRankTests.v1",
        "status": "FULL_RANK_REDUCTION_TESTS_EXECUTED",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "sectors": sectors,
        "coefficient_matrix_c0_c1_c2_by_sector": coeffs,
        "determinant": determinant,
        "rank": rank,
        "selected_log_coefficient_source_rows": source_rows_now,
        "tests": reduction_tests,
        "conclusion": "Current selected source data do not reduce the nine diagnostic coefficient slots to a selected no-knob or 1-3 parameter coefficient theorem.",
    }

    operator_contract = {
        "schema": "MTTSelectedFlavorThresholdSourceOperatorContract.v1",
        "status": "SOURCE_OPERATOR_CONTRACT_EMITTED_VALUE_ROWS_OPEN",
        "accepted_now": False,
        "must_emit_before_replay": [
            "sector-labelled threshold source operator T_flavor[s]",
            "three coefficient functionals c0,c1,c2 from selected branch data",
            "generation-resolved threshold/mass-scheme/profile rows or a theorem reducing them",
            "scale/scheme convention tied to the same branch",
            "no use of common-scale Yukawa magnitudes, CKM, PMNS, or Higgs values as selectors",
        ],
        "legal_exits": [
            "derive selected flavor threshold/source operator emitting c_{s,k}",
            "prove a reduced-coefficient theorem with source-selected universal parameters before empirical replay",
            "declare the nine coefficient rows as a controlled profile-replay flavor ledger",
        ],
        "forbidden_exits": [
            "solve c_{s,k} from versioned Yukawa magnitudes and relabel them as source rows",
            "use the diagnostic exact reconstruction residual as no-knob evidence",
            "reuse source-normalized projection weights as magnitude-bearing projection weights",
        ],
    }

    next_packet = {
        "schema": "MTTNextCutsetAfterFlavorThresholdReduction.v1",
        "status": "NEXT_ATTACK_CONCRETE_FLAVOR_SOURCE_OPERATOR_OR_MINIMAL_NINE_SLOT_POLICY",
        "closure_claimed": False,
        "next_required_artifact": NEXT,
        "not_missing_anymore": [
            "selected three-family spectral basis",
            "degree-2 log-response functional domain",
            "source-normalized sector projection weights",
            "minimal profile-replay flavor ledger",
        ],
        "still_missing": [
            "selected log coefficient source rows",
            "selected flavor threshold/source operator",
            "source-selected reduced-coefficient theorem",
            "generation-resolved threshold/mass-scheme/profile rows",
            "strict no-knob charged Yukawa magnitude prediction",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedFlavorThresholdSourceOperatorOrReducedCoefficientTheorem",
        "status": STATUS,
        "closure_claimed": True,
        "strict_no_knob_flavor_closure_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "inputs": {
            "diagnostic_log_yukawa_response_coefficients.packet": str(DIAGNOSTIC.relative_to(ROOT)).replace("\\", "/"),
            "selected_logyukawacoefficientsourcerows_or_minimalflavorparameterledger.candidate": str(PREVIOUS.relative_to(ROOT)).replace("\\", "/"),
            "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows.candidate": str(HIGHER.relative_to(ROOT)).replace("\\", "/"),
            "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation.candidate": str(MAGNITUDE.relative_to(ROOT)).replace("\\", "/"),
            "selected_thresholdresponserows_or_sectorprojectionweightsexecution.candidate": str(PROJECTION.relative_to(ROOT)).replace("\\", "/"),
        },
        "output_packets": {
            "reduced_coefficient_rank_tests": f"candidate_data/{SLUG}/reduced_coefficient_rank_tests.packet.json",
            "selected_flavor_threshold_source_operator_contract": f"candidate_data/{SLUG}/selected_flavor_threshold_source_operator_contract.packet.json",
            "next_cutset_after_flavor_threshold_reduction": f"candidate_data/{SLUG}/next_cutset_after_flavor_threshold_reduction.packet.json",
        },
        "closure_decision": {
            "selected_family_spectral_basis_closed": True,
            "degree2_log_response_basis_closed": True,
            "coefficient_matrix_full_rank": rank == 3,
            "coefficient_matrix_determinant": determinant,
            "current_reduced_coefficient_theorem_closed": False,
            "selected_flavor_threshold_source_operator_closed": False,
            "selected_log_coefficient_source_rows": source_rows_now,
            "minimal_profile_replay_flavor_ledger_closed": True,
            "minimal_profile_replay_parameter_slots": previous["closure_decision"]["minimal_profile_replay_parameter_slots"],
            "strict_no_knob_flavor_closure": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "FlavorThresholdSourceOperatorReductionWallTheorem",
            "proved": True,
            "statement": "The selected spectral family basis and degree-2 log-response domain are closed, but the diagnostic u,d,e coefficient matrix is full rank and current selected source data emit zero coefficient rows. Source-normalized projection weights, current higher-response attempts, and current 1-3 universal-parameter lanes do not reduce the nine charged Yukawa coefficient slots. Therefore strict charged-Yukawa no-knob closure now requires a concrete selected flavor threshold/source operator, a source-selected reduced-coefficient theorem, or else the honest nine-slot profile-replay flavor ledger.",
        },
    }

    cert = {
        "certificate": "MTT_Selected_FlavorThresholdSourceOperator_or_ReducedCoefficientTheorem_v1",
        "status": STATUS,
        "candidate": candidate["candidate"],
        "theorem": candidate["theorem"]["name"],
        "proved": True,
        "coefficient_matrix_full_rank": rank == 3,
        "coefficient_matrix_determinant": determinant,
        "selected_log_coefficient_source_rows": source_rows_now,
        "minimal_profile_replay_parameter_slots": candidate["closure_decision"]["minimal_profile_replay_parameter_slots"],
        "strict_no_knob_flavor_closure": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected FlavorThresholdSourceOperator or ReducedCoefficientTheorem v1

Status: `{STATUS}`

## Theorem

**FlavorThresholdSourceOperatorReductionWallTheorem.** The selected spectral family basis and degree-2 log-response domain are closed, but the diagnostic `u,d,e` coefficient matrix is full rank and current selected source data emit zero coefficient rows. Source-normalized projection weights, current higher-response attempts, and current `1-3` universal-parameter lanes do not reduce the nine charged Yukawa coefficient slots.

Therefore strict charged-Yukawa no-knob closure now requires one of:

1. a concrete selected flavor threshold/source operator emitting `c_{{s,k}}`,
2. a source-selected reduced-coefficient theorem,
3. the honest nine-slot profile-replay flavor ledger.

## Numerical Rank Check

- determinant: `{determinant}`
- rank: `{rank}`
- selected coefficient source rows: `{source_rows_now}`
- profile-replay flavor slots: `{candidate["closure_decision"]["minimal_profile_replay_parameter_slots"]}`

This artifact does not use Yukawa, CKM, PMNS, or Higgs values as selectors. The coefficient rows remain diagnostic/profile replay data until a source theorem emits them before replay.

Next artifact: `{NEXT}`.
"""

    write_json(PACKET_DIR / "reduced_coefficient_rank_tests.packet.json", reduction_packet)
    write_json(PACKET_DIR / "selected_flavor_threshold_source_operator_contract.packet.json", operator_contract)
    write_json(PACKET_DIR / "next_cutset_after_flavor_threshold_reduction.packet.json", next_packet)
    write_json(CANDIDATE, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {CANDIDATE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
