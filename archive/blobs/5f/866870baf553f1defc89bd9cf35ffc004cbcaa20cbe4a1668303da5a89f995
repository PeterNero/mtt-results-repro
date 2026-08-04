from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79validatedbetatransportandfiniteflatcontourhomotopy"
OUT = ROOT / "candidate_data" / SLUG
A125 = (
    ROOT
    / "candidate_data"
    / "selected_q79picardlefschetzintervalwallandbaselift.candidate.json"
)
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
)
LOCAL_HOMOTOPY = (
    DIRECTORY / "pgl3_selected_local_lower_contour_homotopy.interval.packet.json"
)
LOCAL_TRANSPORT = (
    DIRECTORY / "pgl3_selected_side_beta.local_lower.defect_interval.packet.json"
)
BROAD_HOMOTOPY = DIRECTORY / "pgl3_full_lower_contour_homotopy.interval.packet.json"
BROAD_TRANSPORT = DIRECTORY / "pgl3_selected_side_beta.defect_interval.packet.json"
HOMOTOPY_SCRIPT = ROOT / "scripts" / "certify_q79_full_lower_contour_homotopy.py"
TRANSPORT_SCRIPT = ROOT / "scripts" / "certify_q79_selected_side_beta_defect_transport.py"
THEOREM = OUT / "selected_side_endpoint_beta_nonzero.theorem.packet.json"
DECISION = OUT / "broad_contour_rejection_and_next_lattice_gate.packet.json"
FRONTIER = OUT / "U6_frontier_after_A126.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"


STATUS = (
    "MTT_U6_Q79_SELECTED_SIDE_ELL_ZERO_BRANCH_INTERVAL_EXCLUDED_"
    "INTEGRAL_PERIOD_BRANCH_OPEN"
)
NEXT = "MTT_Selected_q79IntegralPeriodLatticeDistanceOrNonzeroBranch_v1"


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


def beta_centers(packet: dict) -> list[complex]:
    return [
        complex(float(value["real"]), float(value["imaginary"]))
        for value in packet["endpoint"]["beta_center"]
    ]


def main() -> int:
    a125 = load(A125)
    homotopy = load(LOCAL_HOMOTOPY)
    transport = load(LOCAL_TRANSPORT)
    broad_homotopy = load(BROAD_HOMOTOPY)
    broad_transport = load(BROAD_TRANSPORT)

    if not a125["checks"]["selected_side_base_lift_interval_certified"]:
        raise AssertionError("A125 selected-side base lift is unavailable")

    if homotopy["status"] != "LOCAL_LOWER_CONTOUR_HOMOTOPY_INTERVAL_CERTIFIED":
        raise AssertionError("local lower-contour homotopy is unavailable")
    expected_windings = {
        "reduction_determinant": 0,
        "y_chart_scale": 0,
        "q_leading_coefficient": 0,
        "q_discriminant": -1,
        "g_on_q_norm": 0,
    }
    observed_windings = {
        name: row["winding_number"]
        for name, row in homotopy["argument_principle"].items()
    }
    if observed_windings != expected_windings:
        raise AssertionError("unexpected local-strip winding inventory")
    if not homotopy["decision"]["smooth_genus_two_family_on_closed_lower_strip"]:
        raise AssertionError("the local strip is not a smooth family")
    if not homotopy["decision"]["finite_flat_symmetric_divisor_preserved"]:
        raise AssertionError("the finite flat divisor was not preserved")
    if not homotopy["decision"]["normal_function_endpoint_branch_preserved"]:
        raise AssertionError("the normal-function branch was not preserved")
    finite_flat = homotopy["finite_flat_divisor_theorem"]
    if not finite_flat["applies"]:
        raise AssertionError("finite-flat theorem is unavailable")
    if finite_flat["q_discriminant_zero_count_with_multiplicity"] != 1:
        raise AssertionError("the root-collision count changed")
    if finite_flat["individual_q_roots_globally_labelled"]:
        raise AssertionError("the colliding roots were incorrectly globally labelled")
    if homotopy["boundary_cover"]["leaf_count"] < 1000:
        raise AssertionError("local homotopy boundary cover is incomplete")

    if (
        transport["status"]
        != "EXECUTED_CONTOUR_ENDPOINT_BETA_NONZERO_INTERVAL_CERTIFIED"
    ):
        raise AssertionError("validated endpoint transport is unavailable")
    if transport["method"]["path"] != "selected local lower contour":
        raise AssertionError("the wrong validated contour was executed")
    if not transport["method"][
        "aligned_quadratic_source_evaluated_by_exact_quotient_trace"
    ]:
        raise AssertionError("the collision-safe quotient trace is unavailable")
    if transport["method"]["raw_connection_exponential_bound_used"]:
        raise AssertionError("the rejected raw exponential bound reappeared")
    endpoint = transport["endpoint"]
    if not endpoint["zero_excluded"]:
        raise AssertionError("endpoint beta still contains zero")
    if float(endpoint["euclidean_norm_lower"]) <= 2.0:
        raise AssertionError("endpoint beta lower bound is too small")
    if float(endpoint["uniform_component_radius_upper"]) >= 0.05:
        raise AssertionError("endpoint beta radius is too broad")
    if float(endpoint["maximum_component_absolute_lower"]) <= 1.0:
        raise AssertionError("no endpoint component excludes zero")
    execution = transport["execution"]
    if execution["accepted_step_count"] != 160:
        raise AssertionError("validated accepted-step count changed")
    if execution["rejected_step_count"] != 69:
        raise AssertionError("validated rejected-step count changed")
    if max(step["transformed_lift_correction"] for step in execution["steps"]) >= 1e-6:
        raise AssertionError("a local lift correction exceeds its budget")
    if max(step["beta_increment_error"] for step in execution["steps"]) >= 1e-3:
        raise AssertionError("a local beta increment exceeds its budget")
    audit = transport["point_audit"]
    if audit["maximum_connection_relative_difference"] >= 2e-10:
        raise AssertionError("connection point audit failed")
    if audit["maximum_source_relative_difference"] >= 2e-10:
        raise AssertionError("source point audit failed")
    if audit["maximum_residue_relative_difference"] >= 1e-13:
        raise AssertionError("residue point audit failed")
    if transport["strict_scope"]["observed_SM_values_used"]:
        raise AssertionError("observed Standard-Model values entered the transport")
    if transport["strict_scope"]["selected_side_ell_zero_branch_excluded"]:
        raise AssertionError("transport alone was overpromoted")

    broad_windings = {
        name: row["winding_number"]
        for name, row in broad_homotopy["argument_principle"].items()
    }
    if broad_windings["reduction_determinant"] != -4:
        raise AssertionError("broad-contour family obstruction changed")
    if broad_windings["g_on_q_norm"] != -1:
        raise AssertionError("broad-contour divisor obstruction changed")
    if broad_homotopy["decision"][
        "straight_and_full_lower_contours_homotopic_in_smooth_family"
    ]:
        raise AssertionError("the broad contour was incorrectly promoted")

    local_center = beta_centers(transport)
    broad_center = beta_centers(broad_transport)
    broad_endpoint_difference = max(
        abs(local - broad)
        for local, broad in zip(local_center, broad_center)
    )
    if broad_endpoint_difference >= 1e-8:
        raise AssertionError("the broad/local endpoint diagnostic changed")

    theorem = {
        "schema": "MTTQ79SelectedSideEndpointBetaNonzeroTheorem.v1",
        "status": "SELECTED_SIDE_ELL_ZERO_BRANCH_INTERVAL_EXCLUDED",
        "theorem": {
            "name": "Q79FiniteFlatContourAndSelectedSideBetaNonzeroTheorem",
            "proved": True,
            "statement": (
                "On the closed local strip 0.65<=Re(lambda)<=0.82 and "
                "-0.1<=Im(lambda)<=0, the selected genus-two family is "
                "smooth and the y chart is regular. Although Q2 has one "
                "simple discriminant zero, its leading coefficient is a unit "
                "and G3 has unit norm in O[t]/(Q2). Hence U=G3 defines a "
                "finite flat symmetric degree-two Cartier divisor and its "
                "Abel-Jacobi normal function and exact quotient-trace source "
                "extend through the root exchange. The local lower contour "
                "therefore preserves the selected straight-path branch. "
                "Validated order-28 defect-corrected transport gives "
                "||beta(1)||_2>2.2500100575, excluding beta(1)=0 on the "
                "frozen selected ell=0 branch."
            ),
        },
        "homotopy": {
            "domain": homotopy["domain"],
            "windings": observed_windings,
            "q_discriminant_zero_count_with_multiplicity": 1,
            "finite_flat_symmetric_divisor_preserved": True,
            "normal_function_endpoint_branch_preserved": True,
        },
        "validated_endpoint": endpoint,
        "scope": {
            "frozen_A124_selected_carrier": True,
            "selected_side_ell_zero_branch_excluded": True,
            "global_PGL3_ell_zero_no_go": False,
            "nonzero_integral_Z92_branch_selected": False,
            "normalized_Deligne_pairing_zero_or_no_go_closed": False,
            "observed_SM_values_used": False,
        },
    }
    dump(THEOREM, theorem)

    decision = {
        "schema": "MTTQ79BroadContourRejectionAndNextLatticeGate.v1",
        "status": "BROAD_CONTOUR_RETIRED_SELECTED_LOCAL_BRANCH_CLOSED",
        "broad_contour": {
            "windings": broad_windings,
            "homotopic_to_selected_straight_path": False,
            "validated_endpoint_center_difference_from_local": (
                broad_endpoint_difference
            ),
            "interpretation": (
                "Endpoint agreement does not promote the broad contour: its "
                "strip encloses four reduction-determinant zeros and one "
                "G-on-Q zero. Only the certified local contour is used by "
                "the selected-branch theorem."
            ),
        },
        "closed": {
            "local_finite_flat_contour_homotopy": True,
            "validated_selected_side_beta_nonzero": True,
            "frozen_selected_ell_zero_branch_excluded": True,
        },
        "open": {
            "global_PGL3_ell_zero_no_go": True,
            "interval_8x92_period_lattice": True,
            "exact_nonzero_integral_branch_selection": True,
            "normalized_Deligne_pairing_zero_or_no_go": True,
        },
        "next_required_artifact": NEXT,
    }
    dump(DECISION, decision)

    frontier = {
        "schema": "MTTU6FrontierAfterA126.v1",
        "status": STATUS,
        "A125_interval_wall_and_base_lift_preserved": True,
        "selected_local_contour_homotopy_interval_certified": True,
        "finite_flat_symmetric_divisor_through_one_root_collision": True,
        "validated_endpoint_beta_euclidean_norm_lower": endpoint[
            "euclidean_norm_lower"
        ],
        "selected_side_ell_zero_branch_excluded": True,
        "global_ell_zero_no_go": False,
        "integral_period_branch_selected": False,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }
    dump(FRONTIER, frontier)

    authority_paths = [
        A125,
        LOCAL_HOMOTOPY,
        LOCAL_TRANSPORT,
        BROAD_HOMOTOPY,
        BROAD_TRANSPORT,
        HOMOTOPY_SCRIPT,
        TRANSPORT_SCRIPT,
        Path(__file__),
        THEOREM,
        DECISION,
        FRONTIER,
    ]
    candidate = {
        "schema": "MTTSelectedQ79ValidatedBetaTransportAndFiniteFlatContourHomotopy.v1",
        "status": STATUS,
        "proof_artifact": (
            "proof_corpus/"
            "MTT_Selected_q79ValidatedBetaTransportAndFiniteFlatContourHomotopy_v1.md"
        ),
        "authority_hashes": [
            {
                "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "sha256": sha256(path),
            }
            for path in authority_paths
        ],
        "outputs": {
            "theorem": str(THEOREM.relative_to(ROOT)).replace("\\", "/"),
            "decision": str(DECISION.relative_to(ROOT)).replace("\\", "/"),
            "frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {
            "local_homotopy_interval_certified": True,
            "finite_flat_divisor_theorem_closed": True,
            "validated_selected_side_endpoint_beta_nonzero": True,
            "selected_side_ell_zero_branch_excluded": True,
            "broad_contour_wrongly_promoted": False,
            "global_ell_zero_no_go_invented": False,
            "integral_Z92_branch_invented": False,
            "observed_SM_target_fitting_used": False,
        },
        "results": frontier,
        "next_required_artifact": NEXT,
    }
    dump(CANDIDATE, candidate)

    certificate = {
        "certificate": (
            "MTTSelectedQ79ValidatedBetaTransportAndFiniteFlatContourHomotopy"
        ),
        "status": STATUS,
        "candidate_sha256": sha256(CANDIDATE),
        "local_homotopy_interval_certified": True,
        "finite_flat_divisor_theorem_closed": True,
        "selected_side_beta_nonzero_interval": True,
        "selected_side_ell_zero_branch_excluded": True,
        "global_no_go_proved": False,
        "integral_period_branch_selected": False,
        "observed_SM_target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    dump(CERTIFICATE, certificate)
    print(f"wrote {CANDIDATE.relative_to(ROOT)}")
    print(f"wrote {CERTIFICATE.relative_to(ROOT)}")
    print(
        "selected-side ell=0 branch excluded; integral period branch remains open"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
