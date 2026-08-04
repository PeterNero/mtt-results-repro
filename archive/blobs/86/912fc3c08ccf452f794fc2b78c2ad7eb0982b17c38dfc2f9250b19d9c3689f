from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
)
A110_CECH = (
    ROOT
    / "candidate_data"
    / "selected_q79explicitmodelrelativedelignegerbezeroornogoexecution"
    / "normalized_Poincare_gerbe_Cech_formula.packet.json"
)
A119_PERIODS = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handleandlerayperiodexecution"
    / "full_integral_basis_period_table.packet.json"
)
A120_CANDIDATE = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2normalfunctionbetaandintegralbranchexecution.candidate.json"
)
A120_AFFINE = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2normalfunctionbetaandintegralbranchexecution"
    / "complete_affine_normal_function_cocycle.packet.json"
)
A120_PRODUCTION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2normalfunctionbetaandintegralbranchexecution"
    / "normal_function_handles.production.packet.json"
)
A120_TIGHT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2normalfunctionbetaandintegralbranchexecution"
    / "normal_function_handles.tight.packet.json"
)
TRANSGRESSION = OUT / "normalized_Deligne_Leray_transgression.packet.json"
BETA_VECTOR = OUT / "selected_beta_period_vector.floating.packet.json"
BRANCH_OPEN = OUT / "integral_branch_and_gerbe_decision.open.json"
FRONTIER = OUT / "U6_frontier_after_A121.packet.json"
CANDIDATE = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution.candidate.json"
)
CERTIFICATE = (
    ROOT
    / "certificates"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution.certificate.json"
)


STATUS = (
    "MTT_U6_Q79_NORMALIZED_DELIGNE_TRANSGRESSION_FUNCTIONAL_AND_FLOATING_"
    "BETA_VECTOR_CLOSED_INTEGRAL_BRANCH_OPEN"
)
NEXT = "MTT_Selected_q79GenusTwoIntegralBranchOrPGL3GerbeNoGoExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_complex(value: dict) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_pair(value: complex) -> dict:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def handle(packet: dict, name: str) -> dict:
    selected = [row for row in packet["handles"] if row["name"] == name]
    if len(selected) != 1:
        raise AssertionError(f"missing unique {name} handle")
    return selected[0]


def main() -> int:
    cech = load(A110_CECH)
    periods = load(A119_PERIODS)
    a120_candidate = load(A120_CANDIDATE)
    affine = load(A120_AFFINE)
    production = load(A120_PRODUCTION)
    tight = load(A120_TIGHT)

    if cech["triple_overlap_scalar"]["formula"] != (
        "alpha_ijk(e_hat)=chi_ehat(n_ijk,0)"
    ):
        raise AssertionError("A110 first-circle source marking changed")
    if periods["period_matrix_shape"] != [8, 92]:
        raise AssertionError("A119 period shape changed")
    if not affine["exact_mumford_source"]["all_exact_checks_pass"]:
        raise AssertionError("A120 exact source is not closed")

    production_b = handle(production, "B")
    tight_b = handle(tight, "B")
    if production_b["relative_period_form_order"] != periods["form_order"]:
        raise AssertionError("production form order mismatch")
    if tight_b["relative_period_form_order"] != periods["form_order"]:
        raise AssertionError("tight form order mismatch")

    z_production = np.asarray(
        [parse_complex(value) for value in production_b["relative_periods"]]
    )
    z_tight = np.asarray(
        [parse_complex(value) for value in tight_b["relative_periods"]]
    )
    difference = z_production - z_tight
    maximum_absolute_difference = float(np.max(np.abs(difference)))
    maximum_scaled_difference = float(
        max(
            abs(delta) / max(1.0, abs(first), abs(second))
            for delta, first, second in zip(
                difference, z_production, z_tight
            )
        )
    )

    transgression = {
        "schema": "MTTQ79NormalizedDeligneLerayTransgression.v1",
        "status": "EXACT_QUOTIENT_LEVEL_DELIGNE_TRANSGRESSION_FUNCTIONAL_CLOSED",
        "source_marking": {
            "elliptic_lattice": "Z + i Z",
            "A_cycle": "translation by 1",
            "B_cycle": "translation by i",
            "Fu_Yau_Chern_pair": ["delta", 0],
            "A110_scalar_cocycle": "alpha_ijk(e_hat)=chi_ehat(n_ijk,0)",
            "selected_DD_generator": "DD(alpha)=delta cup u_A",
            "not_an_exchange_ambiguity": (
                "The explicit second coordinate 0 in (n_ijk,0) fixes the "
                "first/A lattice generator in the frozen A114 marking."
            ),
        },
        "normal_function_pairing": {
            "fiber_divisor": (
                "D_delta=P_1+P_2-infinity_plus-infinity_minus"
            ),
            "Abel_Jacobi_lift": "nu",
            "scalar_one_forms": (
                "eta_r=<nu,lambda_r> dw, where omega_r=lambda_r wedge dw"
            ),
            "A120_execution": (
                "R_gamma,r=integral_gamma eta_r for gamma=A,B"
            ),
        },
        "torus_transgression": {
            "orientation": "A dot B=+1",
            "dual_generator_periods": {
                "integral_A_u_A": 1,
                "integral_B_u_A": 0,
            },
            "Riemann_bilinear_formula": (
                "integral_E u_A wedge eta_r=(integral_A u_A) "
                "(integral_B eta_r)-(integral_B u_A) "
                "(integral_A eta_r)=R_B,r"
            ),
            "selected_representative": "z_r=R_B,r",
            "equivalence_space": "C^8 / Pi(H^2(C,Z))",
            "overall_orientation_sign_irrelevant_to_zero_test": True,
        },
        "descent_and_invariance": {
            "local_admissibility": (
                "All 90 A120 local singularity classes vanish, so local "
                "integral thimble corrections remove puncture jumps."
            ),
            "global_consistency": (
                "The exact A120 affine surface relation makes the corrected "
                "fundamental-polygon edges consistent."
            ),
            "lift_or_cut_change": (
                "Changing the Abel-Jacobi lift, local thimble corrections, "
                "or the cut changes R_B by an A119 integral H2 period."
            ),
            "therefore": (
                "[R_B] is the normalized beta_C class in the trace-free "
                "period quotient."
            ),
        },
        "theorem": {
            "name": "Q79NormalizedDeligneLerayTransgressionTheorem",
            "proved": True,
            "statement": (
                "On the frozen square-torus marking, the normalized Fu-Yau "
                "Poincare gerbe has source delta cup u_A. Its restriction to "
                "the A110 spectral surface is represented under Serre duality "
                "by the eight B-handle normal-function sweep periods, modulo "
                "the A119 integral H2 period image."
            ),
        },
        "strict_scope": {
            "exact": "functional and quotient class identification",
            "floating": "A120 numerical values of the representative",
            "not_claimed": [
                "interval enclosure of z_8",
                "integral membership or nonmembership",
                "beta_C zero or nonzero",
                "a PGL3 zero or its covariant Jacobian",
            ],
        },
    }
    dump(TRANSGRESSION, transgression)

    beta_vector = {
        "schema": "MTTQ79SelectedBetaPeriodVectorFloating.v1",
        "status": "SELECTED_FLOATING_BETA_REPRESENTATIVE_EMITTED_NOT_INTERVAL_PROMOTED",
        "form_order": periods["form_order"],
        "representative_rule": "z_8=R_B in C^8/Pi(H^2(C,Z))",
        "production_values": [complex_pair(value) for value in z_production],
        "tight_values": [complex_pair(value) for value in z_tight],
        "production_minus_tight": [
            complex_pair(value) for value in difference
        ],
        "maximum_absolute_difference": format(
            maximum_absolute_difference, ".17g"
        ),
        "maximum_scaled_difference": format(
            maximum_scaled_difference, ".17g"
        ),
        "production_l2_norm": format(
            float(np.linalg.norm(z_production)), ".17g"
        ),
        "same_normalization_as_A119": (
            "Both engines integrate the A111 residue rows with "
            "da/(2b)=period_length*dw."
        ),
        "convergence_scope": {
            "independent_tolerance_rerun": True,
            "interval_enclosure": False,
            "nonzero_representative_is_not_nonzero_quotient_class": True,
        },
    }
    dump(BETA_VECTOR, beta_vector)

    branch_open = {
        "schema": "MTTQ79IntegralBranchAndGerbeDecisionInput.v1",
        "status": "OPEN_EXACT_OR_CERTIFIED_INTEGRAL_PERIOD_MEMBERSHIP",
        "closed_input": {
            "normalized_Deligne_functional": True,
            "selected_floating_z_8_rows": 8,
            "integral_period_matrix_shape": periods["period_matrix_shape"],
            "integral_basis_exact": periods["strict_scope"][
                "exact_integral_basis"
            ],
        },
        "equation": "z_8=Pi_(8x92)*ell, ell in Z^92",
        "open": {
            "interval_enclosure_z_8": False,
            "interval_enclosure_Pi_8x92": False,
            "integral_branch_ell_Z92": None,
            "exact_membership_proved": False,
            "exact_nonmembership_proved": False,
            "beta_C_zero_proved": False,
            "beta_C_nonzero_proved": False,
            "PGL3_covariant_Jacobian_at_zero": None,
        },
        "guard": {
            "nearest_lattice_not_accepted": True,
            "small_floating_residual_not_accepted": True,
            "projected_integral_group_not_assumed_discrete": True,
            "nonzero_floating_representative_not_a_nonzero_class_proof": True,
        },
        "lawful_closing_routes": [
            "construct an exact holomorphic Cech 1-cochain trivializing beta_C",
            "derive exact algebraic or CM period identities giving ell",
            "validate z and Pi and prove a branch-height/separation theorem",
            "after a zero branch, execute the same-source covariant PGL3 Jacobian",
        ],
        "next_required_artifact": NEXT,
    }
    dump(BRANCH_OPEN, branch_open)

    frontier = {
        "schema": "MTTU6FrontierAfterA121.v1",
        "status": STATUS,
        "exact_normalized_Deligne_transgression_functional_closed": True,
        "floating_beta_C_period_rows_emitted": 8,
        "interval_beta_C_period_rows_emitted": 0,
        "integral_period_branch_selected": False,
        "beta_C_zero_or_nonzero_decided": False,
        "PGL3_zero_and_Jacobian_closed": False,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }
    dump(FRONTIER, frontier)

    authority_paths = [
        A110_CECH,
        A119_PERIODS,
        A120_CANDIDATE,
        A120_AFFINE,
        A120_PRODUCTION,
        A120_TIGHT,
        Path(__file__),
        TRANSGRESSION,
        BETA_VECTOR,
        BRANCH_OPEN,
        FRONTIER,
    ]
    candidate = {
        "schema": (
            "MTTSelectedQ79GenusTwoDeligneBetaPeriodAndIntegralBranchExecution.v1"
        ),
        "status": STATUS,
        "proof_artifact": (
            "proof_corpus/MTT_Selected_q79GenusTwoDeligneBetaPeriodAndIntegralBranchExecution_v1.md"
        ),
        "authority_hashes": [
            {
                "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "sha256": sha256(path),
            }
            for path in authority_paths
        ],
        "outputs": {
            "transgression": str(TRANSGRESSION.relative_to(ROOT)).replace(
                "\\", "/"
            ),
            "beta_vector": str(BETA_VECTOR.relative_to(ROOT)).replace(
                "\\", "/"
            ),
            "integral_branch_open": str(BRANCH_OPEN.relative_to(ROOT)).replace(
                "\\", "/"
            ),
            "frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {
            "A110_first_circle_marking_consumed": True,
            "A119_exact_integral_basis_consumed": True,
            "A120_complete_affine_cocycle_consumed": True,
            "B_handle_transgression_selected": True,
            "beta_rows_emitted": 8,
            "maximum_production_tight_difference_below_6e_10": (
                maximum_absolute_difference < 6.0e-10
            ),
            "integral_branch_invented": False,
            "target_fitting_used": False,
        },
        "results": frontier,
        "next_required_artifact": NEXT,
    }
    if not candidate["checks"][
        "maximum_production_tight_difference_below_6e_10"
    ]:
        raise AssertionError("A121 beta-vector convergence gate failed")
    dump(CANDIDATE, candidate)

    certificate = {
        "certificate": (
            "MTTSelectedQ79GenusTwoDeligneBetaPeriodAndIntegralBranchExecution"
        ),
        "status": STATUS,
        "candidate_path": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "candidate_sha256": sha256(CANDIDATE),
        "normalized_Deligne_transgression_functional_closed": True,
        "floating_beta_vector_closed": True,
        "interval_beta_vector_closed": False,
        "integral_branch_selected": False,
        "beta_C_decided": False,
        "full_U6_closed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    dump(CERTIFICATE, certificate)
    print(json.dumps(candidate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
