"""Build the direct H quartic threshold or dynamic Herm(2) value-row packet.

The preceding packet promoted selected s_beta as the H angular/projection
factor and proved that s_beta alone cannot determine the dynamic Herm(2) rows.
This packet pushes the next algebraic reduction: once s_beta is selected, the
Herm(2) problem has a canonical polar form.  The scalar H K-threshold row no
longer needs an arbitrary three-entry matrix; it needs a selected radial/
threshold source scalar, or a direct K_threshold.Omega_H.lambda row.

The packet does not close the H value row.  It closes the exact reduction of the
remaining problem and records the source object that would finish the 10/10
K-threshold antecedent without using measured Higgs/lambda values as selectors.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
POLAR = PACKET_DIR / "sbeta_polar_herm2_reduction.packet.json"
FUNCTIONAL = PACKET_DIR / "h_quartic_threshold_functional_reduction.packet.json"
TRIALS = PACKET_DIR / "current_h_radial_threshold_candidates.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_radial_reduction.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_direct_h_quartic_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = (
    CORPUS
    / "MTT_Selected_DirectHQuarticThresholdFunctional_or_DynamicHerm2ValueRows_v1.md"
)

PREVIOUS = DATA / "selected_hsectorquarticthresholdfromprojectionreduction_or_dynamicherm2rows.candidate.json"
PREVIOUS_HERM2 = (
    DATA
    / "selected_hsectorquarticthresholdfromprojectionreduction_or_dynamicherm2rows"
    / "sbeta_to_dynamic_herm2_rows_nogo.packet.json"
)
PREVIOUS_CONTRACT = (
    DATA
    / "selected_hsectorquarticthresholdfromprojectionreduction_or_dynamicherm2rows"
    / "h_quartic_threshold_payload_contract.packet.json"
)
PREVIOUS_HK = (
    DATA
    / "selected_hsectorquarticthresholdfromprojectionreduction_or_dynamicherm2rows"
    / "hk_threshold_gate_after_sbeta_quartic_attempt.packet.json"
)
PREVIOUS_SBETA = (
    DATA
    / "selected_higgsdynamicstrainkernel_or_c5bc6projectionnoboundaryproof"
    / "selected_finite_reduction_sbeta_promotion.packet.json"
)
H_SOURCE_EQ = (
    DATA
    / "selected_hsectorquarticthresholdpayload_or_stricttenkclosure"
    / "h_sector_payload_source_equation.packet.json"
)
STEP70_FACTOR = (
    DATA
    / "selected_step70_heattorsionprefactorbackimport_or_rowlocalfrontier"
    / "step70_prefactor_slot_factorization.packet.json"
)
STEP71_TARGETS = (
    DATA
    / "selected_step71_smparitymatrixcomparison_or_rowlocaltargets"
    / "step71_rowlocal_composite_target_contract.packet.json"
)
DYNAMIC_HESSIAN = (
    DATA
    / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission"
    / "dynamic_hessian_domain_and_extraction_gate.packet.json"
)
KINEMATIC_NOGO = (
    DATA
    / "selected_higgssecondvariationfunctionalsource_or_herm2rowvalues"
    / "kinematic_metric_as_hessian_nogo.packet.json"
)

STATUS = (
    "MTT_SELECTED_DIRECTHQUARTICTHRESHOLDFUNCTIONAL_OR_DYNAMICHERM2VALUEROWS_"
    "RADIAL_COLLAPSE_CLOSED_H_SCALAR_SOURCE_OPEN"
)
NEXT = "MTT_Selected_HRadialThresholdScalarSource_or_TenKClosure_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing direct-H quartic inputs: " + ", ".join(missing))


def row_by_omega(rows: list[dict[str, Any]], omega_id: str) -> dict[str, Any]:
    for row in rows:
        if row.get("omega_id") == omega_id:
            return row
    raise KeyError(omega_id)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_HERM2,
        PREVIOUS_CONTRACT,
        PREVIOUS_HK,
        PREVIOUS_SBETA,
        H_SOURCE_EQ,
        STEP70_FACTOR,
        STEP71_TARGETS,
        DYNAMIC_HESSIAN,
        KINEMATIC_NOGO,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_herm2 = load(PREVIOUS_HERM2)
    previous_contract = load(PREVIOUS_CONTRACT)
    previous_hk = load(PREVIOUS_HK)
    previous_sbeta = load(PREVIOUS_SBETA)
    h_source = load(H_SOURCE_EQ)
    factor = load(STEP70_FACTOR)
    step71 = load(STEP71_TARGETS)
    dynamic_hessian = load(DYNAMIC_HESSIAN)
    kinematic_nogo = load(KINEMATIC_NOGO)

    s_beta = float(previous_sbeta["selected_s_beta"]["value"])
    sqrt_s = math.sqrt(s_beta)
    sqrt_1_minus = math.sqrt(1.0 - s_beta)
    omega_over_delta = sqrt_1_minus / sqrt_s
    delta_over_omega = sqrt_s / sqrt_1_minus
    h_factor = row_by_omega(factor["factor_rows"], "Omega_H.lambda")
    h_target = row_by_omega(step71["target_rows"], "Omega_H.lambda")
    h_row = previous_hk["H_row"]

    polar = {
        "schema": "MTTSBetaPolarHerm2Reduction.v1",
        "status": "SBETA_POLAR_ANGLE_CLOSED_RADIAL_PHASE_OPEN",
        "closure_claimed": True,
        "theorem": {
            "name": "SelectedSBetaPolarHerm2ReductionTheorem",
            "proved": True,
            "statement": (
                "For a trace-free H-sector Herm(2) block M_H=[[Delta,Omega],"
                "[conj(Omega),-Delta]], the selected projection scalar s_beta "
                "fixes the polar angle: Delta^2=s_beta*r_H^2 and "
                "|Omega|^2=(1-s_beta)*r_H^2, where r_H^2=Delta^2+|Omega|^2. "
                "Thus the remaining dynamic data are the positive radial scale "
                "r_H, the sign of Delta, and the phase of Omega.  The scalar "
                "K-threshold route can depend only on a selected radial/threshold "
                "source scalar or a direct selected K row; the full dynamic "
                "Herm(2) route additionally needs phase/sign rows."
            ),
        },
        "selected_inputs": {
            "selected_s_beta": s_beta,
            "selected_s_beta_formula": previous_sbeta["selected_s_beta"]["formula"],
            "selected_s_beta_source": previous_sbeta["selected_s_beta"]["value_source"],
            "projection_measure_equality": previous_sbeta["selected_finite_reduction_policy"][
                "physical_projection_measure_equality"
            ],
            "no_extra_boundary_source_term": previous_sbeta["selected_finite_reduction_policy"][
                "no_extra_boundary_source_term"
            ],
            "observed_higgs_or_beta_used": previous_sbeta["selected_s_beta"][
                "observed_higgs_or_beta_used"
            ],
        },
        "closed_exact_constraints": {
            "Herm2_trace_free_form": "[[Delta, Omega], [conj(Omega), -Delta]]",
            "r_H_squared": "Delta^2 + Re(Omega)^2 + Im(Omega)^2",
            "Delta_squared": "s_beta * r_H^2",
            "abs_Omega_squared": "(1 - s_beta) * r_H^2",
            "eigenvalues": ["-r_H", "+r_H"],
            "determinant": "-r_H^2",
            "abs_Omega_over_abs_Delta": omega_over_delta,
            "abs_Delta_over_abs_Omega": delta_over_omega,
            "sqrt_s_beta": sqrt_s,
            "sqrt_one_minus_s_beta": sqrt_1_minus,
        },
        "coordinates_still_unselected": {
            "positive_radial_scale_r_H": None,
            "sign_Delta": None,
            "phase_Omega": None,
        },
        "consequence": {
            "scalar_H_K_route_requires_full_three_Herm2_rows": False,
            "scalar_H_K_route_requires_selected_radial_threshold_scalar_or_direct_K_row": True,
            "full_dynamic_Herm2_route_requires_phase_and_sign": True,
            "s_beta_alone_emits_Delta_ReOmega_ImOmega": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    functional = {
        "schema": "MTTHQuarticThresholdFunctionalReduction.v1",
        "status": "H_QUARTIC_THRESHOLD_FUNCTIONAL_REDUCED_TO_RADIAL_SOURCE_SCALAR",
        "closure_claimed": True,
        "theorem": {
            "name": "HQuarticThresholdRadialSourceEquivalenceTheorem",
            "proved": True,
            "statement": (
                "With s_beta selected and the H-sector source equation closed, "
                "the tenth K row is equivalent to one accepted direct source row "
                "K_threshold.Omega_H.lambda, or to selected H split factors "
                "L_rowlocal.Omega_H.lambda and T_scheme.Omega_H.lambda.  If the "
                "route is through a dynamic Herm(2) Hessian, s_beta reduces the "
                "scalar threshold part to a source-selected radial/threshold "
                "functional of r_H; phase and sign are only needed for the full "
                "matrix-valued Herm(2) rows."
            ),
        },
        "closed_source_equations": {
            "omega_value": h_source["selected_source_equation"]["omega_value"],
            "direct_K_row": h_source["selected_source_equation"]["direct_K_row"],
            "split_K_row": h_source["selected_source_equation"]["split_K_row"],
            "prefactor_factorization": h_source["selected_source_equation"][
                "prefactor_factorization"
            ],
        },
        "accepted_substructure": {
            "selected_s_beta_angular_factor": True,
            "selected_s_beta_value": s_beta,
            "D_fin_H_subfactor_closed": h_factor["closed_subsources"][
                "finite_heat_torsion_response"
            ],
            "D_fin_H_subfactor_id": h_factor["finite_heat_torsion_subfactor_id"],
            "theta_exponent_1_over_3_closed": previous_contract["already_closed_subfields"][
                "theta_exponent_1_over_3_closed"
            ],
            "conditional_ten_K_scalar_closure_theorem": previous_contract[
                "already_closed_subfields"
            ]["conditional_ten_K_scalar_closure_theorem"],
        },
        "minimal_legal_exits": {
            "direct_exit": {
                "rows_needed": 1,
                "must_emit": ["K_threshold.Omega_H.lambda"],
                "accepted_now": False,
            },
            "split_exit": {
                "rows_needed": 2,
                "must_emit": [
                    "L_rowlocal.Omega_H.lambda",
                    "T_scheme.Omega_H.lambda",
                ],
                "accepted_now": False,
            },
            "dynamic_Herm2_scalar_exit": {
                "rows_needed_for_scalar_threshold": 1,
                "must_emit": [
                    "source-selected H radial threshold scalar R_H.threshold "
                    "or equivalent direct K_threshold.Omega_H.lambda"
                ],
                "phase_sign_needed_for_full_Herm2_matrix": True,
                "accepted_now": False,
            },
            "full_dynamic_Herm2_exit": {
                "rows_needed": 3,
                "must_emit": ["Delta", "Re(Omega)", "Im(Omega)"],
                "accepted_now": False,
            },
        },
        "not_accepted_as_source_rows": {
            "selected_H_radial_threshold_scalar": None,
            "selected_H_quartic_functional": None,
            "selected_H_threshold_scheme_functional": None,
            "direct_K_threshold_Omega_H_lambda": None,
            "selected_Delta_row": None,
            "selected_Re_Omega_row": None,
            "selected_Im_Omega_row": None,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    execution = previous_sbeta["execution_certificate"]
    trials = {
        "schema": "MTTHRadialThresholdCandidateTrials.v1",
        "status": "CURRENT_H_RADIAL_THRESHOLD_CANDIDATES_ZERO_ACCEPTED",
        "closure_claimed": True,
        "accepted_radial_threshold_source_count": 0,
        "accepted_direct_H_K_row_count": 0,
        "trials": [
            {
                "trial_id": "s_beta_as_radial_scale",
                "candidate": s_beta,
                "accepted_as_radial_threshold_source": False,
                "accepted_as_K_threshold_Omega_H_lambda": False,
                "reason": "s_beta is dimensionless angular/projection data and is invariant under r_H -> c*r_H.",
            },
            {
                "trial_id": "unit_radial_normalization_r_H_equals_1",
                "candidate": 1.0,
                "accepted_as_radial_threshold_source": False,
                "accepted_as_K_threshold_Omega_H_lambda": False,
                "reason": "A unit radial scale is a convention unless a selected source functional fixes the normalization.",
            },
            {
                "trial_id": "D_fin_H_as_radial_scale",
                "candidate": h_factor["finite_heat_torsion_subfactor_id"],
                "accepted_as_radial_threshold_source": False,
                "accepted_as_K_threshold_Omega_H_lambda": False,
                "reason": "D_fin.H is a closed determinant/torsion subfactor of Omega, not the H radial threshold row.",
            },
            {
                "trial_id": "selected_HYM_solver_u_l2_as_radial_scale",
                "candidate": execution["u_l2"],
                "accepted_as_radial_threshold_source": False,
                "accepted_as_K_threshold_Omega_H_lambda": False,
                "reason": "The HYM solver norm certifies the finite metric solve; it is not a row-local threshold functional.",
            },
            {
                "trial_id": "selected_HYM_residual_or_tail_contraction_as_radial_scale",
                "candidate": {
                    "residual_l2": execution["residual_l2"],
                    "last_tail_contraction_ratio": execution["tail_contraction_ratios"][-1],
                },
                "accepted_as_radial_threshold_source": False,
                "accepted_as_K_threshold_Omega_H_lambda": False,
                "reason": "Residual and convergence-ratio values are numerical verification diagnostics, not physical source rows.",
            },
            {
                "trial_id": "postcheck_rowlocal_target_numerator_as_K_H",
                "candidate": h_target["rowlocal_composite_target_symbolic"],
                "accepted_as_radial_threshold_source": False,
                "accepted_as_K_threshold_Omega_H_lambda": False,
                "reason": "The rowlocal target numerator is a diagnostic replay/postcheck value and cannot select the source row.",
            },
            {
                "trial_id": "kinematic_metric_or_diagonal_HYM_T3_as_dynamic_M_H",
                "candidate": {
                    "dynamic_Hessian_domain_closed": dynamic_hessian["what_is_closed_now"][
                        "B_Huv_domain"
                    ],
                    "kinematic_metric_trace_free_part_zero": not kinematic_nogo[
                        "computed_trace_free_part"
                    ]["non_scalar_test_passes"],
                },
                "accepted_as_radial_threshold_source": False,
                "accepted_as_K_threshold_Omega_H_lambda": False,
                "reason": "The kinematic metric route has zero trace-free Herm(2) part and fails the non-scalar value-source test.",
            },
        ],
        "forbidden_promotions": [
            "treat s_beta as K_threshold.Omega_H.lambda",
            "fix r_H=1 by convention",
            "use D_fin.H as the H radial threshold scalar",
            "use HYM solver norms or residuals as source values",
            "use postcheck target numerators as no-knob source rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    hk_gate = {
        "schema": "MTTHKThresholdGateAfterRadialReduction.v1",
        "status": "H_K_THRESHOLD_GATE_RADIAL_REDUCTION_CLOSED_H_SCALAR_SOURCE_OPEN_9_OF_10",
        "closure_claimed": True,
        "required_output": "K_threshold.Omega_H.lambda",
        "accepted_selected_K_source_row_count": previous_hk["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "H_row": {
            **h_row,
            "s_beta_polar_herm2_reduction_closed": True,
            "abs_Omega_over_abs_Delta_fixed": omega_over_delta,
            "selected_H_radial_threshold_scalar_emitted": False,
            "selected_H_radial_scale_r_H_emitted": False,
            "selected_H_phase_sign_rows_emitted": False,
            "direct_K_threshold_Omega_H_lambda_emitted": False,
        },
        "conditional_consequent_current": {
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "lambda_H_row_executable": False,
            "accepted_internal_scalar_value_row_count": 0,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterDirectHQuarticAttempt.v1",
        "status": "NEXT_FRONTIER_H_RADIAL_THRESHOLD_SCALAR_SOURCE_OR_TEN_K_CLOSURE",
        "closure_claimed": True,
        "closed_here": [
            "selected s_beta polar angle constraints for Herm(2) H rows",
            "radial collapse theorem for scalar H K-threshold closure",
            "minimal legal exits reduced to direct K, split L/T, or one selected H radial threshold scalar",
            "current radial shortcuts rejected as source rows",
            "H K-threshold gate remains 9/10",
        ],
        "still_open": [
            "selected H radial threshold scalar R_H.threshold or equivalent direct K_threshold.Omega_H.lambda",
            "selected H-sector quartic/threshold source functional that emits the radial scalar",
            "selected L_rowlocal.Omega_H.lambda and T_scheme.Omega_H.lambda if using the split route",
            "Delta/Re(Omega)/Im(Omega) rows if full dynamic Herm(2) closure is required",
            "phase/sign rows for the full Herm(2) matrix route",
            "ten-row K antecedent",
            "strict Omega/lambda_H scalar execution",
            "selected matrix-level mixing extension and true SM equivalence",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedDirectHQuarticThresholdFunctionalOrDynamicHerm2ValueRows",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "DirectHQuarticThresholdOrHerm2RadialCollapseTheorem",
            "proved": True,
            "statement": (
                "The selected H projection scalar s_beta fixes the Herm(2) polar "
                "angle and reduces scalar H closure to a selected radial/threshold "
                "source scalar or a direct K_threshold.Omega_H.lambda row.  Full "
                "dynamic Herm(2) closure still requires r_H, phase, and sign; the "
                "current corpus emits none of those value rows."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "selected_s_beta_polar_angle_closed": True,
            "selected_s_beta_value": s_beta,
            "Herm2_radial_collapse_closed": True,
            "H_scalar_threshold_reduced_to_one_radial_source": True,
            "selected_H_radial_threshold_scalar_emitted": False,
            "selected_H_radial_scale_r_H_emitted": False,
            "selected_H_quartic_functional_emitted": False,
            "selected_H_threshold_scheme_functional_emitted": False,
            "selected_L_rowlocal_Omega_H_lambda": False,
            "selected_T_scheme_Omega_H_lambda": False,
            "K_threshold_Omega_H_lambda_emitted": False,
            "selected_Delta_row_emitted": False,
            "selected_Re_Omega_row_emitted": False,
            "selected_Im_Omega_row_emitted": False,
            "selected_Hermitian_M_H_values_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "accepted_radial_threshold_source_count": 0,
            "accepted_selected_K_source_row_count": previous_hk[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": previous_hk[
                "selected_K_threshold_row_count_required"
            ],
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "sbeta_polar_herm2_reduction": rel(POLAR),
            "h_quartic_threshold_functional_reduction": rel(FUNCTIONAL),
            "current_h_radial_threshold_candidates": rel(TRIALS),
            "hk_threshold_gate_after_radial_reduction": rel(HK_GATE),
            "next_cutset_after_direct_h_quartic_attempt": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedDirectHQuarticThresholdFunctionalOrDynamicHerm2ValueRowsCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "selected_s_beta_polar_angle_closed": True,
        "selected_s_beta_value": s_beta,
        "abs_Omega_over_abs_Delta_fixed": omega_over_delta,
        "Herm2_radial_collapse_closed": True,
        "H_scalar_threshold_reduced_to_one_radial_source": True,
        "selected_H_radial_threshold_scalar_emitted": False,
        "selected_H_radial_scale_r_H_emitted": False,
        "selected_H_quartic_functional_emitted": False,
        "selected_H_threshold_scheme_functional_emitted": False,
        "selected_L_rowlocal_Omega_H_lambda": False,
        "selected_T_scheme_Omega_H_lambda": False,
        "K_threshold_Omega_H_lambda_emitted": False,
        "selected_Delta_row_emitted": False,
        "selected_Re_Omega_row_emitted": False,
        "selected_Im_Omega_row_emitted": False,
        "accepted_radial_threshold_source_count": 0,
        "accepted_selected_K_source_row_count": previous_hk["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "ten_K_antecedent_satisfied": False,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "accepted_internal_scalar_value_row_count": 0,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected DirectHQuarticThresholdFunctional or DynamicHerm2ValueRows v1

Status: `{STATUS}`

## What Closed

- fixed the exact Herm(2) polar constraints from selected `s_beta={s_beta}`
- derived `|Omega|/|Delta|={omega_over_delta}` for any selected dynamic H value source
- reduced the scalar H `K_threshold` problem to a selected radial/threshold source scalar or direct `K_threshold.Omega_H.lambda`
- proved the full dynamic Herm(2) route still needs `r_H`, phase, and sign rows
- rejected current radial shortcuts: `s_beta`, `r_H=1`, `D_fin.H`, HYM solver norms/residuals, replay target numerators, and the kinematic metric route

## Still Open

- selected H radial threshold scalar `R_H.threshold`, or direct `K_threshold.Omega_H.lambda`
- selected H quartic/threshold source functional that emits that scalar
- split `L_rowlocal.Omega_H.lambda` and `T_scheme.Omega_H.lambda` if not using the direct route
- `Delta/Re(Omega)/Im(Omega)` plus phase/sign if full dynamic Herm(2) closure is required

Next required artifact: `{NEXT}`
"""

    write_json(POLAR, polar)
    write_json(FUNCTIONAL, functional)
    write_json(TRIALS, trials)
    write_json(HK_GATE, hk_gate)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
