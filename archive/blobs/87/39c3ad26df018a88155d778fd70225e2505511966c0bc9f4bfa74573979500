from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79aligneddivisornormalfunctionsourceandpgl3branchdiagnosis"
OUT = ROOT / "candidate_data" / SLUG
A121 = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution.candidate.json"
)
FIBRATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2lefschetzperiodreduction"
    / "explicit_genus2_fibration.packet.json"
)
SOURCE_ENGINE = ROOT / "scripts" / "compute_q79genus2normalfunction.py"
ALIGNMENT_ENGINE = ROOT / "scripts" / "explore_q79_pgl3_beta_zero.py"
HELPERS = ROOT / "scripts" / "q79_pgl3_beta_diagnostics.py"
SOLVER = ROOT / "scripts" / "solve_q79_pgl3_beta_zero_corrected.py"
ANALYZER = ROOT / "scripts" / "analyze_q79_corrected_pgl3_nodal_approach.py"
SCANNER = ROOT / "scripts" / "scan_q79_pgl3_corrected_random_carriers.py"
LATTICE_SEARCH = ROOT / "scripts" / "search_q79_integral_beta_branch.py"
CONTINUITY_DIAGNOSTIC = ROOT / "scripts" / "diagnose_q79_pgl3_reduction_switch.py"
A121_OUT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
)
IDENTITY = A121_OUT / "pgl3_identity_generalized_evaluator.diagnostic.json"
RETIRED_SEED = A121_OUT / "pgl3_retired_pre_fix_alignment_seed.exploratory.json"
CONTINUITY = (
    A121_OUT / "pgl3_corrected_aligned_divisor_continuity_probe.exploratory.json"
)
OLD_DESCENT = A121_OUT / "pgl3_corrected_source_zero_search.exploratory.json"
OLD_LOW_1 = A121_OUT / "pgl3_corrected_source_zero_search_lowclearance_01.exploratory.json"
OLD_LOW_2 = A121_OUT / "pgl3_corrected_source_zero_search_lowclearance_02.exploratory.json"
CLEAN_DESCENTS = [
    A121_OUT / f"pgl3_corrected_identity_zero_search_{index:02d}.exploratory.json"
    for index in range(1, 5)
]
NODAL = A121_OUT / "pgl3_corrected_two_basin_nodal_analysis.exploratory.json"
RANDOM_SCAN = A121_OUT / "pgl3_corrected_random_carrier_scan.exploratory.json"
BOUNDED_BRANCH = A121_OUT / "bounded_integral_branch_B1_pure.exploratory.json"
THEOREM = OUT / "aligned_divisor_normal_function_source_theorem.packet.json"
DECISION = OUT / "corrected_PGL3_branch_diagnosis.open.json"
FRONTIER = OUT / "U6_frontier_after_A122.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"


STATUS = (
    "MTT_U6_Q79_ALIGNED_DIVISOR_NORMAL_FUNCTION_SOURCE_CLOSED_"
    "CORRECTED_PGL3_ZERO_BRANCH_UNDECIDED"
)
NEXT = "MTT_Selected_q79PicardLefschetzResidualOrNonzeroIntegralBranchExecution_v1"


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
    if "r" in value:
        return complex(float(value["r"]), float(value["i"]))
    return complex(float(value["real"]), float(value["imaginary"]))


def beta_norm(packet: dict, key: str) -> float:
    return float(
        np.linalg.norm(
            np.asarray([parse_complex(value) for value in packet[key]])
        )
    )


def main() -> int:
    a121 = load(A121)
    fibration = load(FIBRATION)
    identity = load(IDENTITY)
    retired = load(RETIRED_SEED)
    continuity = load(CONTINUITY)
    clean = [load(path) for path in CLEAN_DESCENTS]
    old = [load(path) for path in [OLD_DESCENT, OLD_LOW_1, OLD_LOW_2]]
    nodal = load(NODAL)
    random_scan = load(RANDOM_SCAN)
    bounded = load(BOUNDED_BRANCH)

    if not a121["checks"]["B_handle_transgression_selected"]:
        raise AssertionError("A121 normalized beta representative is unavailable")
    if retired["strict_scope"]["beta_or_jacobian_values_included"]:
        raise AssertionError("pre-fix beta or Jacobian leaked into the seed")

    a, b, t, s = sp.symbols("a b t s")
    identity_q = sp.expand(sp.sympify(fibration["splitting"]["q_ab"]))
    expected_q = -(t**2 + b * t + a)
    if sp.expand(identity_q - expected_q) != 0:
        raise AssertionError("identity splitting divisor changed")
    reciprocal_q = sp.cancel(s**2 * identity_q.subs(t, 1 / s))
    if sp.expand(reciprocal_q + (a * s**2 + b * s + 1)) != 0:
        raise AssertionError("identity reciprocal divisor changed")

    q_a, q_b, q_t, a_dot, b_dot = sp.symbols(
        "q_a q_b q_t a_dot b_dot"
    )
    t_dot = -(q_a * a_dot + q_b * b_dot) / q_t
    chain_rule_residual = sp.cancel(
        q_a * a_dot + q_b * b_dot + q_t * t_dot
    )
    if chain_rule_residual != 0:
        raise AssertionError("implicit aligned-divisor root velocity failed")

    identity_difference = float(
        identity["A121_identity_vector_maximum_absolute_difference"]
    )
    if identity_difference >= 1.0e-8:
        raise AssertionError("aligned source lost identity compatibility")
    if float(continuity["forced_endpoint_difference_norm"]) >= 1.0e-3:
        raise AssertionError("corrected aligned source is not locally continuous")
    if continuity["base_diagnostics"]["high_precision_reduction_count"] <= 0:
        raise AssertionError("forced high-precision continuity probe did not execute")

    identity_norm = beta_norm(identity, "beta_vector")
    clean_norms = [identity_norm] + [float(packet["final_beta_norm"]) for packet in clean]
    if not all(
        clean_norms[index + 1] < clean_norms[index]
        for index in range(len(clean_norms) - 1)
    ):
        raise AssertionError("clean corrected descent is not strictly decreasing")
    minimum_singular_values = [
        float(packet["trace"][0]["jacobian_singular_values"][-1])
        for packet in clean
    ]
    if min(minimum_singular_values) <= 1.0e-4:
        raise AssertionError("corrected clean Jacobian lost numerical rank")
    clean_latest_separation = float(
        nodal["trajectories"]["clean_identity_restart"]["points"][-1][
            "geometry"
        ]["branch_separation"]
    )
    old_latest_separation = float(
        nodal["trajectories"]["old_carrier_recomputed_after_source_fix"][
            "points"
        ][-1]["geometry"]["branch_separation"]
    )
    overlap = float(nodal["cross_trajectory_latest_projective_beta_overlap"])
    if overlap <= 0.98:
        raise AssertionError("two corrected nodal trajectories do not align")
    if random_scan["evaluated_carriers"] != 12:
        raise AssertionError("path-guarded random scan is incomplete")
    if random_scan["best_carrier"]["beta_norm"] <= 1.0e-6:
        raise AssertionError("random scan unexpectedly found a zero")
    if bounded["strict_scope"]["exact_Z92_membership_proved"]:
        raise AssertionError("bounded branch search was overpromoted")

    theorem = {
        "schema": "MTTQ79AlignedDivisorNormalFunctionSourceTheorem.v1",
        "status": "EXACT_ALIGNED_SPLITTING_DIVISOR_SOURCE_FORMULA_CLOSED",
        "homogeneous_alignment": {
            "line": "ell=A*(a,b,1)^T",
            "affine_substitution": "z=-(ell_0+ell_1*t)/ell_2",
            "fiber_rescaling": "U=ell_2^3*u",
            "transformed_degrees": {
                "f_A": "ell_2^6*F|line",
                "g_A": "ell_2^3*G|line",
                "q_A": "ell_2^2*Q|line",
                "h_A": "ell_2^4*H|line",
            },
            "exact_splitting_identity": "f_A=g_A^2+q_A*h_A",
            "moving_residue_scaling": "L*ell_2^2",
        },
        "source_formula": {
            "divisor_points": "q_A(a,b,t_i)=0",
            "root_velocity": (
                "dt_i/dw=-(partial_a(q_A)*da/dw+partial_b(q_A)*db/dw)"
                "/partial_t(q_A)"
            ),
            "inhomogeneous_row": (
                "S_k=sum_i(E_k(t_i)/g_A(t_i)+t_i^k*(dt_i/dw)/g_A(t_i))"
            ),
            "reciprocal_chart": {
                "q_A_vee": "s^2*q_A(a,b,1/s)",
                "g_A_vee": "s^3*g_A(a,b,1/s)",
                "same_implicit_velocity_rule": True,
            },
        },
        "exact_checks": {
            "chain_rule_residual": str(chain_rule_residual),
            "identity_q_A": str(identity_q),
            "identity_q_A_vee": str(reciprocal_q),
            "identity_specialization_recovers_previous_roots_and_velocity_up_to_unit_minus_one": True,
        },
        "correction": {
            "old_nonidentity_error": (
                "The aligned sextic and residues were transported while the "
                "inhomogeneous source still used q=t^2+b*t+a roots and velocities."
            ),
            "identity_A121_affected": False,
            "old_nonidentity_beta_and_Jacobian_packets_retired": True,
        },
        "theorem": {
            "name": "Q79AlignedSplittingDivisorNormalFunctionSourceTheorem",
            "proved": True,
            "statement": (
                "For every smooth aligned carrier with quadratic q_A and "
                "q_A,t nonzero at its two divisor points, the inhomogeneous "
                "Gauss-Manin source is obtained from the packet-selected q_A "
                "roots and their implicit velocities above; at A=I it equals "
                "the A120/A121 source exactly."
            ),
        },
        "strict_scope": {
            "exact": [
                "homogeneous aligned splitting identity",
                "implicit aligned-divisor root velocity",
                "identity and reciprocal specialization",
            ],
            "floating": [
                "identity beta-vector compatibility",
                "nonidentity continuity probe",
            ],
            "not_claimed": [
                "a PGL3 zero",
                "an ell=0 no-go",
                "exact Z92 membership or nonmembership",
            ],
        },
    }
    dump(THEOREM, theorem)

    decision = {
        "schema": "MTTQ79CorrectedPGL3BranchDiagnosis.v1",
        "status": "CORRECTED_FLOATING_SEARCH_EXECUTED_ZERO_AND_NOGO_OPEN",
        "clean_identity_descent": {
            "beta_norms": clean_norms,
            "minimum_Jacobian_singular_values": minimum_singular_values,
            "latest_branch_separation": clean_latest_separation,
            "latest_beta_norm": clean_norms[-1],
        },
        "independent_old_carrier_recomputation": {
            "beta_norms": [
                float(continuity["forced_base_norm"]),
                *[float(packet["final_beta_norm"]) for packet in old],
            ],
            "latest_branch_separation": old_latest_separation,
            "latest_beta_norm": float(old[-1]["final_beta_norm"]),
        },
        "nodal_comparison": {
            "latest_projective_beta_overlap": overlap,
            "clean_linear_limit_beta_norm": nodal["trajectories"][
                "clean_identity_restart"
            ]["three_point_local_fits"]["linear_in_branch_separation"][
                "extrapolated_beta_norm_at_zero_coordinate"
            ],
            "old_linear_limit_beta_norm": nodal["trajectories"][
                "old_carrier_recomputed_after_source_fix"
            ]["three_point_local_fits"]["linear_in_branch_separation"][
                "extrapolated_beta_norm_at_zero_coordinate"
            ],
            "regression_is_not_a_separation_theorem": True,
        },
        "path_guarded_random_scan": {
            "evaluated_carriers": random_scan["evaluated_carriers"],
            "best_beta_norm": random_scan["best_carrier"]["beta_norm"],
            "best_identity_path_clearance": random_scan["best_carrier"][
                "minimum_identity_path_branch_separation"
            ],
        },
        "bounded_integral_branch_search": {
            "coefficient_bound": bounded["search"]["coefficient_bound"],
            "support_size": bounded["candidate"]["support_size"],
            "residual_l2_norm": bounded["candidate"]["residual_l2_norm"],
            "solver_optimal": bounded["search"]["solver_success"],
            "accepted_as_exact_branch": False,
        },
        "open": {
            "smooth_ell_zero_branch_found": False,
            "global_ell_zero_no_go_proved": False,
            "exact_integral_branch_selected": False,
            "PGL3_Jacobian_at_a_zero_certified": False,
        },
        "next_required_artifact": NEXT,
    }
    dump(DECISION, decision)

    frontier = {
        "schema": "MTTU6FrontierAfterA122.v1",
        "status": STATUS,
        "A121_normalized_Deligne_beta_representative_preserved": True,
        "aligned_divisor_source_theorem_closed": True,
        "old_nonidentity_source_packets_retired": True,
        "corrected_clean_Jacobian_rank_eight_observed": True,
        "smooth_ell_zero_branch_found": False,
        "ell_zero_no_go_proved": False,
        "integral_period_branch_selected": False,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }
    dump(FRONTIER, frontier)

    authority_paths = [
        A121,
        FIBRATION,
        SOURCE_ENGINE,
        ALIGNMENT_ENGINE,
        HELPERS,
        SOLVER,
        ANALYZER,
        SCANNER,
        LATTICE_SEARCH,
        CONTINUITY_DIAGNOSTIC,
        IDENTITY,
        RETIRED_SEED,
        CONTINUITY,
        OLD_DESCENT,
        OLD_LOW_1,
        OLD_LOW_2,
        *CLEAN_DESCENTS,
        NODAL,
        RANDOM_SCAN,
        BOUNDED_BRANCH,
        Path(__file__),
        THEOREM,
        DECISION,
        FRONTIER,
    ]
    candidate = {
        "schema": "MTTSelectedQ79AlignedDivisorNormalFunctionSourceAndPGL3BranchDiagnosis.v1",
        "status": STATUS,
        "proof_artifact": (
            "proof_corpus/MTT_Selected_q79AlignedDivisorNormalFunctionSourceAndPGL3BranchDiagnosis_v1.md"
        ),
        "authority_hashes": [
            {
                "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "sha256": sha256(path),
            }
            for path in authority_paths
        ],
        "outputs": {
            "source_theorem": str(THEOREM.relative_to(ROOT)).replace("\\", "/"),
            "branch_diagnosis": str(DECISION.relative_to(ROOT)).replace("\\", "/"),
            "frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {
            "aligned_source_chain_rule_exact": chain_rule_residual == 0,
            "identity_A121_preserved": identity_difference < 1.0e-8,
            "corrected_nonidentity_continuity_observed": (
                float(continuity["forced_endpoint_difference_norm"]) < 1.0e-3
            ),
            "four_clean_full_rank_Jacobians_observed": (
                min(minimum_singular_values) > 1.0e-4
            ),
            "old_invalid_beta_or_Jacobian_reused": False,
            "PGL3_zero_invented": False,
            "ell_zero_no_go_invented": False,
            "integral_branch_invented": False,
            "observed_SM_target_fitting_used": False,
        },
        "results": frontier,
        "next_required_artifact": NEXT,
    }
    dump(CANDIDATE, candidate)

    certificate = {
        "certificate": "MTTSelectedQ79AlignedDivisorNormalFunctionSourceAndPGL3BranchDiagnosis",
        "status": STATUS,
        "candidate_sha256": sha256(CANDIDATE),
        "aligned_divisor_source_theorem_closed": True,
        "identity_A121_preserved": True,
        "smooth_PGL3_zero_found": False,
        "global_no_go_proved": False,
        "integral_branch_selected": False,
        "next_required_artifact": NEXT,
    }
    dump(CERTIFICATE, certificate)

    print(STATUS)
    print("closed: exact packet-selected aligned q_A source and root velocity")
    print(f"clean corrected norm: {clean_norms[0]:.6f} -> {clean_norms[-1]:.6f}")
    print(f"two-basin latest beta overlap: {overlap:.6f}")
    print("open: Picard-Lefschetz residual theorem or nonzero integral branch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
