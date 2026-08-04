from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79covariantperiodbranchcutsetandtightbetatransport"
OUT = ROOT / "candidate_data" / SLUG
A126 = (
    ROOT
    / "candidate_data"
    / "selected_q79validatedbetatransportandfiniteflatcontourhomotopy.candidate.json"
)
TRANSPORT_DIR = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
)
OLD_BETA = TRANSPORT_DIR / "pgl3_selected_side_beta.local_lower.defect_interval.packet.json"
TIGHT_BETA = TRANSPORT_DIR / "pgl3_selected_side_beta.local_lower.order40.interval.packet.json"
LLL = (
    ROOT
    / "candidate_data"
    / "selected_q79validatedbetatransportandfiniteflatcontourhomotopy"
    / "identity_integral_period_branch_lll.exploratory.json"
)
FIBRATION = OUT / "selected_alignment_genus2_fibration_seed.interval.packet.json"
DISCRIMINANT = OUT / "selected_alignment_dual_discriminant.interval.packet.json"
FAN = OUT / "selected_alignment_distinguished_radial_fan.interval.packet.json"
MONODROMY = OUT / "selected_alignment_meridian_monodromy_batch.packet.json"
TIGHT_TRANSPORT_SCRIPT = (
    ROOT / "scripts" / "certify_q79_selected_side_beta_defect_transport.py"
)
LLL_SCRIPT = ROOT / "scripts" / "explore_q79_a126_integral_period_branch_lll.py"
FIBRATION_SCRIPT = ROOT / "scripts" / "build_q79_selected_alignment_fibration_seed.py"
DISCRIMINANT_SCRIPT = ROOT / "scripts" / "build_q79_selected_alignment_dual_discriminant.py"
FAN_SCRIPT = ROOT / "scripts" / "build_q79_selected_alignment_distinguished_cut_system.py"
ROOT_TRANSPORT_SCRIPT = ROOT / "scripts" / "q79_selected_alignment_genus2_root_transport.py"
MONODROMY_WORKER = ROOT / "scripts" / "compute_q79_selected_alignment_single_meridian_monodromy.py"
MONODROMY_BATCH_SCRIPT = ROOT / "scripts" / "run_q79_selected_alignment_meridian_monodromy_batch.py"
TIGHT_THEOREM = OUT / "tight_selected_side_endpoint_beta.theorem.packet.json"
CUTSET_THEOREM = OUT / "same_carrier_integral_branch_cutset.theorem.packet.json"
PERIOD_INPUT = OUT / "selected_alignment_period_execution_input.packet.json"
FRONTIER = OUT / "U6_frontier_after_A127.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"

STATUS = (
    "MTT_U6_Q79_SELECTED_ALIGNMENT_90_NODE_PERIOD_EXECUTION_INPUT_CLOSED_"
    "CERTIFIED_ROOT_TUBES_AND_PERIOD_ROWS_OPEN"
)
NEXT = "MTT_Selected_q79SelectedAlignmentRootTubesIntegralBasisAndPeriodExecution_v1"


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


def decoded_complex(value: dict) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def main() -> int:
    a126 = load(A126)
    old_beta = load(OLD_BETA)
    tight_beta = load(TIGHT_BETA)
    lll = load(LLL)
    fibration = load(FIBRATION)
    discriminant = load(DISCRIMINANT)
    fan = load(FAN)
    monodromy = load(MONODROMY)

    if not a126["checks"]["selected_side_ell_zero_branch_excluded"]:
        raise AssertionError("A126 selected-side branch theorem is unavailable")
    if tight_beta["status"] != "EXECUTED_CONTOUR_ENDPOINT_BETA_NONZERO_INTERVAL_CERTIFIED":
        raise AssertionError("tight selected-side transport is unavailable")
    if tight_beta["method"]["path"] != "selected local lower contour":
        raise AssertionError("tight transport uses the wrong contour")
    if int(tight_beta["method"]["order"]) != 40:
        raise AssertionError("tight Taylor order changed")
    tight_endpoint = tight_beta["endpoint"]
    old_endpoint = old_beta["endpoint"]
    tight_radius = float(tight_endpoint["uniform_component_radius_upper"])
    old_radius = float(old_endpoint["uniform_component_radius_upper"])
    if not tight_endpoint["zero_excluded"] or float(
        tight_endpoint["euclidean_norm_lower"]
    ) <= 2.3:
        raise AssertionError("tight endpoint beta does not exclude zero")
    if not tight_radius < old_radius / 5:
        raise AssertionError("tight transport did not improve A126 by factor five")
    center_difference = max(
        abs(decoded_complex(left) - decoded_complex(right))
        for left, right in zip(
            tight_endpoint["beta_center"], old_endpoint["beta_center"]
        )
    )
    if center_difference > 1e-12:
        raise AssertionError("tight and A126 endpoint centers disagree")

    if not lll["inputs"]["same_carrier_as_A119_period_table"]:
        raise AssertionError("the retained LLL diagnostic is cross-carrier")
    if lll["inputs"]["beta_source"] != "identity":
        raise AssertionError("the retained LLL beta is not the identity beta")
    best = lll["candidates_by_residual"][0]
    if not float(best["residual_l2_norm"]) < 1e-6:
        raise AssertionError("identity LLL diagnostic unexpectedly weakened")
    if not float(best["period_plus_beta_error_proxy_component_maximum"]) > 1e-4:
        raise AssertionError("identity LLL uncertainty guard disappeared")
    if lll["strict_scope"]["exact_Z92_membership_proved"]:
        raise AssertionError("floating LLL search was promoted to exact membership")
    if lll["strict_scope"]["exact_Z92_nonmembership_proved"]:
        raise AssertionError("floating LLL search was promoted to exact nonmembership")

    if not fibration["splitting_identity"][
        "every_residual_coefficient_contains_zero"
    ]:
        raise AssertionError("selected fibration splitting identity failed")
    if float(fibration["source"]["alignment_determinant_absolute_lower"]) <= 0:
        raise AssertionError("selected alignment is not invertible")
    if not discriminant["dual_discriminant"][
        "identity_pullback_exactly_reproduces_A111_P45_Q43"
    ]:
        raise AssertionError("dual discriminant lost its A111 crosscheck")
    if discriminant["norm90"]["degree"] != 90:
        raise AssertionError("selected discriminant norm degree changed")
    if discriminant["norm90"]["isolated_root_count"] != 90:
        raise AssertionError("selected critical-value count changed")
    if discriminant["critical_points_on_E"]["count"] != 90:
        raise AssertionError("selected elliptic critical lifts are incomplete")
    if not discriminant["strict_scope"][
        "ninety_simple_discriminant_zeros_certified"
    ]:
        raise AssertionError("selected nodal discriminant is not simple")
    if discriminant["selected_y_line_chart_zeros"]["count"] != 3:
        raise AssertionError("selected line-chart wall inventory changed")

    fan_certificate = {
        key: float(value) for key, value in fan["geometric_certificate"].items()
    }
    if not all(value > 0 for value in fan_certificate.values()):
        raise AssertionError("selected distinguished fan lost a clearance")
    if len(fan["distinguished_positive_meridians"]) != 90:
        raise AssertionError("selected distinguished fan is incomplete")
    if monodromy["counts"]["monodromy_packets_complete"] != 90:
        raise AssertionError("selected pointwise monodromy batch is incomplete")
    if monodromy["strict_scope"]["continuous_root_tubes_certified"] != 0:
        raise AssertionError("pointwise monodromy was silently promoted")

    tight_theorem = {
        "schema": "MTTQ79TightSelectedSideEndpointBetaTheorem.v1",
        "status": "SELECTED_SIDE_ELL_ZERO_BRANCH_TIGHT_INTERVAL_EXCLUDED",
        "theorem": {
            "name": "Q79Order40SelectedSideBetaRefinementTheorem",
            "proved": True,
            "statement": (
                "On the A126-certified local lower contour, order-40 "
                "defect-corrected transport with maximum trial step 0.005 "
                "encloses the same endpoint beta center with uniform component "
                "radius below 0.007061 and Euclidean norm above 2.3372. This "
                "strictly refines A126 and again excludes the frozen ell=0 "
                "representative."
            ),
        },
        "old_A126_component_radius": old_endpoint[
            "uniform_component_radius_upper"
        ],
        "tight_component_radius": tight_endpoint[
            "uniform_component_radius_upper"
        ],
        "radius_improvement_factor": old_radius / tight_radius,
        "tight_endpoint": tight_endpoint,
        "execution": {
            "Taylor_order": tight_beta["method"]["order"],
            "accepted_steps": tight_beta["execution"]["accepted_step_count"],
            "rejected_steps": tight_beta["execution"]["rejected_step_count"],
            "minimum_accepted_step": tight_beta["execution"][
                "minimum_accepted_step"
            ],
            "center_difference_from_A126": center_difference,
        },
        "scope": {
            "frozen_selected_ell_zero_branch_excluded": True,
            "nonzero_integral_branch_decided": False,
            "observed_SM_values_used": False,
        },
    }
    dump(TIGHT_THEOREM, tight_theorem)

    cutset = {
        "schema": "MTTQ79SameCarrierIntegralBranchCutsetTheorem.v1",
        "status": "CROSS_CARRIER_PERIOD_REUSE_FORBIDDEN_ENDPOINT_BASIS_ROUTE_PROVED",
        "theorem": {
            "name": "Q79SameCarrierPeriodEquationAndBasisInvarianceTheorem",
            "proved": True,
            "statement": (
                "For F(A,ell)=z(A)-Pi(A)ell, z and Pi must be evaluated on "
                "the same surface and residue-row carrier. Thus the A126 "
                "selected-alignment beta cannot be paired with A119's identity-"
                "alignment period table. Conversely, an independently certified "
                "integral basis B' on the endpoint surface is sufficient: if "
                "B'=B U with U in GL(92,Z), then image(Pi_B')=image(Pi_B). "
                "Transporting A119's individual basis columns is therefore not "
                "required for the membership decision."
            ),
        },
        "equations": {
            "branch_equation": "F(A,ell)=z(A)-Pi(A)*ell",
            "covariant_Jacobian": "J=nabla(z)-sum_I ell_I*nabla(Pi_I)",
            "basis_change": "Pi_B'=Pi_B*U, ell'=U^-1*ell",
        },
        "identity_alignment_diagnostic": {
            "real_period_shape": lll["real_period_system"]["shape"],
            "floating_rank": lll["real_period_system"]["floating_rank"],
            "best_floating_residual_l2": best["residual_l2_norm"],
            "best_uncertainty_proxy_component_maximum": best[
                "period_plus_beta_error_proxy_component_maximum"
            ],
            "interpretation": (
                "The small identity-alignment LLL residual is below an "
                "uncertified two-run error proxy and decides no exact branch."
            ),
        },
        "scope": {
            "cross_carrier_A126_A119_residual_has_proof_status": False,
            "endpoint_basis_invariance_proved": True,
            "bounded_CVP_without_branch_height_is_global_proof": False,
            "exact_integral_branch_decided": False,
        },
    }
    dump(CUTSET_THEOREM, cutset)

    period_input = {
        "schema": "MTTQ79SelectedAlignmentPeriodExecutionInput.v1",
        "status": "SELECTED_ALIGNMENT_90_NODE_CUT_SYSTEM_AND_POINTWISE_MONODROMY_EXECUTED",
        "closed_inputs": {
            "selected_alignment_interval_fibration": True,
            "splitting_identity_interval_preserved": True,
            "exact_dual_discriminant_degree": 30,
            "selected_elliptic_discriminant_norm_degree": 90,
            "simple_nodal_critical_values": 90,
            "uniformizing_critical_lifts": 90,
            "selected_y_chart_wall_points": 3,
            "distinguished_meridian_paths": 90,
            "pointwise_integral_PL_matrices": 90,
        },
        "positive_clearances": fan["geometric_certificate"],
        "monodromy_counts": monodromy["counts"],
        "remaining_execution": [
            "promote continuous six-root tubes on all 90 selected paths",
            "assemble the selected endpoint integral H2 presentation",
            "execute the 90 thimble and eight handle period columns in the same residue rows",
            "append the two exact Leray-edge columns and test z in image(Pi)",
        ],
        "strict_scope": {
            "continuous_root_tubes_certified": 0,
            "endpoint_integral_H2_basis_columns": 0,
            "endpoint_period_rows_emitted": 0,
            "integral_branch_selected": False,
            "observed_SM_values_used": False,
        },
    }
    dump(PERIOD_INPUT, period_input)

    frontier = {
        "schema": "MTTU6FrontierAfterA127.v1",
        "status": STATUS,
        "A126_selected_side_ell_zero_exclusion_preserved": True,
        "tight_selected_side_beta_norm_lower": tight_endpoint[
            "euclidean_norm_lower"
        ],
        "cross_carrier_A119_reuse_retired": True,
        "direct_endpoint_integral_basis_route_proved_sufficient": True,
        "selected_alignment_simple_nodal_critical_values": 90,
        "selected_alignment_distinguished_paths": 90,
        "selected_alignment_pointwise_PL_matrices": 90,
        "selected_alignment_continuous_root_tubes": 0,
        "selected_alignment_integral_H2_basis_columns": 0,
        "selected_alignment_period_columns": 0,
        "integral_period_branch_selected": False,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }
    dump(FRONTIER, frontier)

    authority_paths = [
        A126,
        OLD_BETA,
        TIGHT_BETA,
        LLL,
        FIBRATION,
        DISCRIMINANT,
        FAN,
        MONODROMY,
        TIGHT_TRANSPORT_SCRIPT,
        LLL_SCRIPT,
        FIBRATION_SCRIPT,
        DISCRIMINANT_SCRIPT,
        FAN_SCRIPT,
        ROOT_TRANSPORT_SCRIPT,
        MONODROMY_WORKER,
        MONODROMY_BATCH_SCRIPT,
        Path(__file__),
        TIGHT_THEOREM,
        CUTSET_THEOREM,
        PERIOD_INPUT,
        FRONTIER,
    ]
    candidate = {
        "schema": "MTTSelectedQ79CovariantPeriodBranchCutsetAndTightBetaTransport.v1",
        "status": STATUS,
        "proof_artifact": (
            "proof_corpus/"
            "MTT_Selected_q79CovariantPeriodBranchCutsetAndTightBetaTransport_v1.md"
        ),
        "authority_hashes": [
            {
                "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "sha256": sha256(path),
            }
            for path in authority_paths
        ],
        "outputs": {
            "tight_beta_theorem": str(TIGHT_THEOREM.relative_to(ROOT)).replace("\\", "/"),
            "same_carrier_cutset": str(CUTSET_THEOREM.relative_to(ROOT)).replace("\\", "/"),
            "selected_period_input": str(PERIOD_INPUT.relative_to(ROOT)).replace("\\", "/"),
            "frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {
            "tight_beta_refines_A126": True,
            "cross_carrier_period_reuse_retired": True,
            "direct_endpoint_basis_route_proved_sufficient": True,
            "selected_alignment_90_node_input_closed": True,
            "pointwise_monodromy_overpromoted": False,
            "integral_branch_invented": False,
            "observed_SM_target_fitting_used": False,
        },
        "results": frontier,
        "next_required_artifact": NEXT,
    }
    dump(CANDIDATE, candidate)

    certificate = {
        "certificate": "MTTSelectedQ79CovariantPeriodBranchCutsetAndTightBetaTransport",
        "status": STATUS,
        "candidate_sha256": sha256(CANDIDATE),
        "tight_selected_side_beta_nonzero": True,
        "same_carrier_cutset_proved": True,
        "selected_alignment_critical_values_certified": 90,
        "selected_alignment_distinguished_paths_certified": 90,
        "selected_alignment_pointwise_monodromies_computed": 90,
        "selected_alignment_period_columns_emitted": 0,
        "integral_branch_selected": False,
        "observed_SM_target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    dump(CERTIFICATE, certificate)
    print(f"wrote {CANDIDATE.relative_to(ROOT)}")
    print(f"wrote {CERTIFICATE.relative_to(ROOT)}")
    print(
        "A127: same-carrier endpoint period input closed through 90 pointwise "
        "monodromies; root tubes, integral basis and periods remain"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
