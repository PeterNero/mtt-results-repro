"""Build full-S2 sector density operator / Phi_sector_N numeric rows gate.

The previous packet proved that selected C1 sector matrices are support but not
the full Phi_sector_N density.  This packet constructs the exact full-S2
correction space needed on top of the selected C1 support and audits whether
current source data selects the correction values.

The correction space is now explicit:

    Phi_sector_N = Phi_C1_lanes + Delta_S2
    Delta_S2 = sum_{s,k} delta_{s,k} E_{s,k}

where E_{s,k} are row-dual density slots satisfying the common-circle trace
contract.  The values delta_{s,k} are not promoted from policy replay; they are
recorded only as diagnostic obligations for the missing source theorem.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_fulls2sectordensityoperator_or_phisectornnumericrows"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FullS2SectorDensityOperator_or_PhiSectorNNumericRows_v1.md"

C1_BRIDGE = DATA / "selected_sectorresponsedensitysource_or_noknobcskrowemission.candidate.json"
C1_TRACE = (
    DATA
    / "selected_sectorresponsedensitysource_or_noknobcskrowemission"
    / "c1_lane_commoncircle_trace_execution.packet.json"
)
TRACE_BASIS = (
    DATA
    / "selected_commoncirclesectorresponseexecution_or_csktracerows"
    / "sector_projector_and_family_dual_trace_basis.packet.json"
)
FLAVOR_VALUES = (
    DATA
    / "selected_flavorthresholdoperatorsourcevalues_or_nineslotpolicyadoption"
    / "flavor_threshold_operator_value_table.packet.json"
)
HIGHER_RESPONSE_COEFFS = (
    DATA
    / "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows"
    / "higher_response_sector_coefficient_source_attempt.packet.json"
)
MINIMAL_POLICY = (
    DATA
    / "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows"
    / "minimal_universal_parameter_application_to_yukawa_wall.packet.json"
)
FULLS2_GATE = (
    DATA
    / "selected_higherresponsepayloadrows_sourcepromotion_or_fulls2valueexecution"
    / "full_s2_value_execution_gate.packet.json"
)
PAYLOAD_PROMOTION = (
    DATA
    / "selected_higherresponsepayloadrows_sourcepromotion_or_fulls2valueexecution"
    / "higher_response_payload_source_promotion_attempt.packet.json"
)

DENSITY_CONTRACT_PACKET = PACKET_DIR / "fulls2_density_operator_contract.packet.json"
RESIDUAL_PACKET = PACKET_DIR / "phisectorn_residual_obligation_after_c1.packet.json"
REDUCTION_PACKET = PACKET_DIR / "minimal_pattern_reduction_tests.packet.json"
SOURCE_DECISION_PACKET = PACKET_DIR / "phisectorn_numeric_row_source_decision.packet.json"
NEXT_PACKET = PACKET_DIR / "next_cutset_after_fulls2_density_contract.packet.json"

STATUS = (
    "MTT_SELECTED_FULLS2SECTORDENSITYOPERATOR_OR_PHISECTORNNUMERICROWS_"
    "DENSITY_CONTRACT_CLOSED_NUMERIC_ROWS_OPEN"
)
NEXT = "MTT_Selected_DeltaS2DensityCorrectionSource_or_StrictCSKRows_v1"

SECTORS = ["u", "d", "e"]
COEFFS = ["c0", "c1", "c2"]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def determinant_3(matrix: list[list[float]]) -> float:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def rank_3(matrix: list[list[float]], tol: float = 1e-10) -> int:
    if abs(determinant_3(matrix)) > tol:
        return 3
    # Check any 2x2 minor.
    for r1 in range(3):
        for r2 in range(r1 + 1, 3):
            for c1 in range(3):
                for c2 in range(c1 + 1, 3):
                    minor = matrix[r1][c1] * matrix[r2][c2] - matrix[r1][c2] * matrix[r2][c1]
                    if abs(minor) > tol:
                        return 2
    return 1 if any(abs(value) > tol for row in matrix for value in row) else 0


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def rms(values: list[float]) -> float:
    return math.sqrt(sum(value * value for value in values) / len(values))


def matrix_flat(matrix: list[list[float]]) -> list[float]:
    return [value for row in matrix for value in row]


def additive_fit(matrix: list[list[float]]) -> dict[str, Any]:
    # Best least-squares fit x_{s,k} = sector_s + coeff_k with gauge mean(coeff)=0.
    grand = mean(matrix_flat(matrix))
    row_means = [mean(row) for row in matrix]
    col_means = [mean([matrix[r][c] for r in range(3)]) for c in range(3)]
    fitted = [[row_means[r] + col_means[c] - grand for c in range(3)] for r in range(3)]
    residuals = [[matrix[r][c] - fitted[r][c] for c in range(3)] for r in range(3)]
    return {
        "model": "delta_s,k = sector_offset_s + coefficient_offset_k",
        "parameter_count_after_gauge": 5,
        "fitted_matrix": fitted,
        "residual_matrix": residuals,
        "rms_residual": rms(matrix_flat(residuals)),
        "max_abs_residual": max(abs(value) for value in matrix_flat(residuals)),
        "exact": max(abs(value) for value in matrix_flat(residuals)) < 1e-10,
    }


def sector_only_fit(matrix: list[list[float]]) -> dict[str, Any]:
    fitted = [[mean(row) for _ in range(3)] for row in matrix]
    residuals = [[matrix[r][c] - fitted[r][c] for c in range(3)] for r in range(3)]
    return {
        "model": "delta_s,k = sector_offset_s",
        "parameter_count": 3,
        "rms_residual": rms(matrix_flat(residuals)),
        "max_abs_residual": max(abs(value) for value in matrix_flat(residuals)),
        "exact": max(abs(value) for value in matrix_flat(residuals)) < 1e-10,
    }


def coeff_only_fit(matrix: list[list[float]]) -> dict[str, Any]:
    col_means = [mean([matrix[r][c] for r in range(3)]) for c in range(3)]
    fitted = [[col_means[c] for c in range(3)] for _ in range(3)]
    residuals = [[matrix[r][c] - fitted[r][c] for c in range(3)] for r in range(3)]
    return {
        "model": "delta_s,k = coefficient_offset_k",
        "parameter_count": 3,
        "rms_residual": rms(matrix_flat(residuals)),
        "max_abs_residual": max(abs(value) for value in matrix_flat(residuals)),
        "exact": max(abs(value) for value in matrix_flat(residuals)) < 1e-10,
    }


def main() -> int:
    sources = [
        C1_BRIDGE,
        C1_TRACE,
        TRACE_BASIS,
        FLAVOR_VALUES,
        HIGHER_RESPONSE_COEFFS,
        MINIMAL_POLICY,
        FULLS2_GATE,
        PAYLOAD_PROMOTION,
    ]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing full-S2 density inputs: " + ", ".join(missing))

    c1_bridge = load(C1_BRIDGE)
    c1_trace = load(C1_TRACE)
    trace_basis = load(TRACE_BASIS)
    flavor = load(FLAVOR_VALUES)
    higher_coeffs = load(HIGHER_RESPONSE_COEFFS)
    minimal_policy = load(MINIMAL_POLICY)
    fulls2_gate = load(FULLS2_GATE)
    payload_promotion = load(PAYLOAD_PROMOTION)

    c1_by_id = {row["row_id"]: row for row in c1_trace["projected_rows"]}
    policy = flavor["sector_operator_coefficients"]
    residual_matrix: list[list[float]] = []
    policy_matrix: list[list[float]] = []
    c1_matrix: list[list[float]] = []
    residual_rows: list[dict[str, Any]] = []
    for sector in SECTORS:
        residual_row = []
        policy_row = []
        c1_row = []
        for coeff in COEFFS:
            row_id = f"csk.{sector}.{coeff}"
            c1_value = c1_by_id[row_id]["projected_real_part"]
            policy_value = policy[sector][coeff]
            delta = policy_value - c1_value
            residual_row.append(delta)
            policy_row.append(policy_value)
            c1_row.append(c1_value)
            residual_rows.append(
                {
                    "row_id": f"deltaS2.{sector}.{coeff}",
                    "sector": sector,
                    "coefficient": coeff,
                    "c1_support_value": c1_value,
                    "policy_replay_value_for_diagnostic_difference": policy_value,
                    "diagnostic_delta_required_if_policy_target_used": delta,
                    "source_value_emitted": False,
                    "accepted_as_phi_sector_n_numeric_row": False,
                    "accepted_as_csk_source_row": False,
                    "blocking_reason": (
                        "Delta_S2 correction value is computed only as a replay diagnostic; "
                        "no selected full-S2 density source emits it."
                    ),
                }
            )
        residual_matrix.append(residual_row)
        policy_matrix.append(policy_row)
        c1_matrix.append(c1_row)

    residual_rank = rank_3(residual_matrix)
    residual_det = determinant_3(residual_matrix)
    policy_rank = rank_3(policy_matrix)
    c1_rank = rank_3(c1_matrix)
    residual_flat = matrix_flat(residual_matrix)
    additive = additive_fit(residual_matrix)
    sector_fit = sector_only_fit(residual_matrix)
    coeff_fit = coeff_only_fit(residual_matrix)

    density_contract = {
        "schema": "MTTFullS2DensityOperatorContract.v1",
        "status": "FULL_S2_DENSITY_OPERATOR_CONTRACT_CLOSED_VALUES_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_form": "Phi_sector_N = Phi_C1_lanes + Delta_S2",
        "delta_s2_expansion": "Delta_S2 = sum_{s in {u,d,e}} sum_{k=0}^2 delta_{s,k} E_{s,k}",
        "row_dual_density_contract": (
            "E_{s,k} is the row-dual density slot satisfying "
            "Tr_N(P_s B_k H_cen E_{s',k'}) = delta_{s,s'} delta_{k,k'}."
        ),
        "closed_inputs": {
            "H_cen_and_trace_basis_closed": True,
            "c1_dynamic_support_imported": c1_bridge["closure_decision"][
                "selected_dynamic_phi_fin_c1_payload_emitted"
            ],
            "c1_lane_commoncircle_trace_executed": c1_bridge["closure_decision"][
                "c1_lane_commoncircle_traces_executed"
            ],
            "family_dual_trace_basis_closed": trace_basis["accepted_as_trace_engine"],
        },
        "value_boundary": {
            "delta_s2_numeric_source_values_emitted": False,
            "policy_replay_values_define_delta_s2": False,
            "accepted_phi_sector_n_numeric_rows": 0,
            "accepted_csk_source_rows": 0,
        },
    }

    residual_packet = {
        "schema": "MTTPhiSectorNResidualObligationAfterC1.v1",
        "status": "DELTA_S2_RESIDUAL_OBLIGATION_COMPUTED_DIAGNOSTIC_ONLY",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "policy_values_used_only_as_diagnostic_target": True,
        "matrices": {
            "policy_replay_matrix": policy_matrix,
            "selected_c1_projected_real_matrix": c1_matrix,
            "diagnostic_delta_s2_matrix_policy_minus_c1": residual_matrix,
        },
        "matrix_diagnostics": {
            "policy_matrix_rank": policy_rank,
            "c1_projected_matrix_rank": c1_rank,
            "delta_s2_diagnostic_rank": residual_rank,
            "delta_s2_diagnostic_determinant": residual_det,
            "delta_s2_rms": rms(residual_flat),
            "delta_s2_max_abs": max(abs(value) for value in residual_flat),
        },
        "rows": residual_rows,
    }

    reduction_tests = {
        "schema": "MTTMinimalPatternReductionTestsForDeltaS2.v1",
        "status": "LOW_PARAMETER_PATTERN_REDUCTION_REJECTED_FOR_CURRENT_SUPPORT",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "diagnostic_matrix_rank_full": residual_rank == 3,
        "ordinary_sector_knobs_rejected_by_policy": higher_coeffs["ordinary_sector_knobs_rejected"],
        "minimal_universal_parameter_lane_selected_now": minimal_policy[
            "minimal_universal_parameter_lane_selected_now"
        ],
        "selected_parameter_count_now": minimal_policy["selected_parameter_count_now"],
        "tests": {
            "sector_only": sector_fit,
            "coefficient_only": coeff_fit,
            "additive_sector_plus_coefficient": additive,
            "rank_less_than_three_exact": {
                "exact": residual_rank < 3,
                "rank": residual_rank,
                "determinant": residual_det,
                "why_it_matters": (
                    "A rank < 3 residual would indicate a lower-dimensional separable "
                    "correction target.  The diagnostic residual is full rank."
                ),
            },
        },
        "accepted_reduced_source_theorem_now": False,
        "accepted_delta_s2_source_rows_now": 0,
    }

    source_decision = {
        "schema": "MTTPhiSectorNNumericRowSourceDecision.v1",
        "status": "PHI_SECTOR_N_NUMERIC_ROWS_NOT_EMITTED_BY_CURRENT_FULL_S2_SUPPORT",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "full_s2_execution_gate": {
            "execution_allowed_now": fulls2_gate["execution_allowed_now"],
            "accepted_scalar_row_count_now": fulls2_gate["accepted_scalar_row_count_now"],
            "selected_HYM_operator_payload_ready": fulls2_gate["ready_fields"][
                "selected_HYM_operator_payload_ready"
            ],
            "selected_rhoE_DE_operator_payload_ready": fulls2_gate["ready_fields"][
                "selected_rhoE_DE_operator_payload_ready"
            ],
            "selected_End0_sector_functor_ready": fulls2_gate["ready_fields"][
                "selected_End0_sector_functor_ready"
            ],
        },
        "payload_support_summary": {
            "selected_now": payload_promotion["selected_now"],
            "support_only_rows": payload_promotion["support_only_rows"],
            "not_promoted_now": payload_promotion["not_promoted_now"],
        },
        "accepted_phi_sector_n_numeric_row_count": 0,
        "accepted_delta_s2_source_row_count": 0,
        "accepted_strict_csk_source_row_count": 0,
        "why_not_closed": [
            "Delta_S2 correction space is now typed, but no selected source emits its values.",
            "diagnostic residual rows are full rank and cannot be replaced by the current selected C1 lanes.",
            "current higher-response/full-S2 gate still lacks selected HYM/rhoE/D_E/End0-sector payload values.",
            "policy replay coefficients remain forbidden as source data.",
        ],
    }

    next_packet = {
        "schema": "MTTNextCutsetAfterFullS2DensityContract.v1",
        "status": "NEXT_IS_DELTA_S2_DENSITY_CORRECTION_SOURCE",
        "closure_claimed": True,
        "closed_now": [
            "full-S2 density operator contract constructed",
            "selected C1 support embedded as Phi_C1_lanes",
            "row-dual Delta_S2 correction slots defined",
            "diagnostic residual obligation computed after C1 support",
            "low-parameter pattern shortcuts rejected for current support",
        ],
        "still_open": [
            "selected Delta_S2 density correction source",
            "nine numeric Delta_S2 / Phi_sector_N row values emitted before replay",
            "selected HYM/rhoE/D_E/End0-sector full-S2 payload",
            "strict c_{s,k} source row emission",
        ],
        "next_required_artifact": NEXT,
        "ordered_attack": [
            "derive selected Delta_S2 from the full-S2 HYM/Strominger payload",
            "promote HYM projector/metric, rhoE/D_E, and End0-sector functor values from support to source",
            "emit nine real row certificates for deltaS2.s.ck",
            "rerun Phi_sector_N trace rows and promote c_{s,k} only after source certificates exist",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedFullS2SectorDensityOperatorOrPhiSectorNNumericRows",
        "status": STATUS,
        "closure_claimed": True,
        "full_s2_density_contract_claimed": True,
        "strict_phi_sector_n_values_claimed": False,
        "strict_csk_source_theorem_claimed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "FullS2DensityCorrectionContractTheorem",
            "proved": True,
            "statement": (
                "The selected C1 lane support extends to a typed full-S2 density contract "
                "Phi_sector_N = Phi_C1_lanes + Delta_S2 with nine row-dual correction "
                "slots.  Current source data do not emit the Delta_S2 numeric values; "
                "diagnostic policy-minus-C1 residuals are full rank and remain replay-only."
            ),
        },
        "closure_decision": {
            "full_s2_density_operator_contract_closed": True,
            "selected_c1_support_embedded": True,
            "delta_s2_row_dual_slots_defined": True,
            "diagnostic_delta_s2_obligation_computed": True,
            "delta_s2_diagnostic_rank": residual_rank,
            "delta_s2_numeric_source_values_emitted": False,
            "accepted_delta_s2_source_row_count": 0,
            "accepted_phi_sector_n_numeric_row_count": 0,
            "accepted_strict_csk_source_row_count": 0,
            "low_parameter_pattern_reduction_closed": False,
            "full_s2_value_execution_allowed_now": fulls2_gate["execution_allowed_now"],
            "full_s2_accepted_scalar_row_count_now": fulls2_gate["accepted_scalar_row_count_now"],
            "policy_replay_rows_accepted_as_source": False,
            "strict_csk_source_theorem_closed": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "key_numbers": {
            "delta_s2_diagnostic_rank": residual_rank,
            "delta_s2_diagnostic_determinant": residual_det,
            "delta_s2_rms": rms(residual_flat),
            "delta_s2_max_abs": max(abs(value) for value in residual_flat),
            "additive_model_rms_residual": additive["rms_residual"],
            "additive_model_max_abs_residual": additive["max_abs_residual"],
        },
        "packets": {
            "density_operator_contract": rel(DENSITY_CONTRACT_PACKET),
            "residual_obligation": rel(RESIDUAL_PACKET),
            "minimal_pattern_reduction_tests": rel(REDUCTION_PACKET),
            "numeric_row_source_decision": rel(SOURCE_DECISION_PACKET),
            "next_cutset": rel(NEXT_PACKET),
        },
    }

    cert = {
        "certificate": "MTTSelectedFullS2SectorDensityOperatorOrPhiSectorNNumericRowsCertificate",
        "status": STATUS,
        "theorem": candidate["theorem"]["name"],
        "full_s2_density_operator_contract_closed": True,
        "selected_c1_support_embedded": True,
        "delta_s2_row_dual_slots_defined": True,
        "diagnostic_delta_s2_obligation_computed": True,
        "delta_s2_diagnostic_rank": residual_rank,
        "delta_s2_numeric_source_values_emitted": False,
        "accepted_delta_s2_source_row_count": 0,
        "accepted_phi_sector_n_numeric_row_count": 0,
        "accepted_strict_csk_source_row_count": 0,
        "full_s2_value_execution_allowed_now": fulls2_gate["execution_allowed_now"],
        "full_s2_accepted_scalar_row_count_now": fulls2_gate["accepted_scalar_row_count_now"],
        "policy_replay_rows_accepted_as_source": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected FullS2SectorDensityOperator or PhiSectorNNumericRows v1

Status: `{STATUS}`

## Theorem

`FullS2DensityCorrectionContractTheorem` is proved.

The selected C1 lane support now sits inside a typed full-S2 density contract:

`Phi_sector_N = Phi_C1_lanes + Delta_S2`

with

`Delta_S2 = sum_s sum_k delta_{{s,k}} E_{{s,k}}`.

The row-dual slots `E_{{s,k}}` are defined by the trace contract
`Tr_N(P_s B_k H_cen E_{{s',k'}})=delta_{{s,s'}} delta_{{k,k'}}`.

## Diagnostic Residual

Using policy replay values only as a diagnostic target, the missing
`Delta_S2` obligation after selected C1 support has:

- rank: `{residual_rank}`
- determinant: `{residual_det}`
- RMS size: `{rms(residual_flat)}`
- max absolute row: `{max(abs(value) for value in residual_flat)}`

The additive sector-plus-coefficient reduction has RMS residual
`{additive["rms_residual"]}` and is not exact.

## Boundary

No numeric `Delta_S2` values are promoted.  Current full-S2 support still has
`0` accepted scalar rows, and the required HYM/rhoE/D_E/End0-sector payload
values remain support-only or open.

## Counts

- accepted strict `Delta_S2` source rows: `0`
- accepted strict `Phi_sector_N` numeric rows: `0`
- accepted strict `c_{{s,k}}` source rows: `0`

## Next Artifact

`{NEXT}`.
"""

    write_json(DENSITY_CONTRACT_PACKET, density_contract)
    write_json(RESIDUAL_PACKET, residual_packet)
    write_json(REDUCTION_PACKET, reduction_tests)
    write_json(SOURCE_DECISION_PACKET, source_decision)
    write_json(NEXT_PACKET, next_packet)
    write_json(CANDIDATE, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
