from __future__ import annotations

import cmath
import hashlib
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from q79_y_chart_conservative_extension import compatible_source_hash


SLUG = "selected_q79validatedbetatransportandfiniteflatcontourhomotopy"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"
OUT = ROOT / "candidate_data" / SLUG
THEOREM = OUT / "selected_side_endpoint_beta_nonzero.theorem.packet.json"
DECISION = OUT / "broad_contour_rejection_and_next_lattice_gate.packet.json"
FRONTIER = OUT / "U6_frontier_after_A126.packet.json"
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


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def encoded_complex(value: dict) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def recompute_winding(leaves: list[dict], name: str) -> tuple[int, float, float]:
    sectors = [leaf["winding_sectors"][name] for leaf in leaves]
    references = [encoded_complex(sector["reference"]) for sector in sectors]
    half_widths = [float(sector["half_width"]) for sector in sectors]
    total = 0.0
    minimum_overlap = math.inf
    for index, reference in enumerate(references):
        following = (index + 1) % len(references)
        change = cmath.phase(references[following] / reference)
        overlap_width = half_widths[index] + half_widths[following]
        require(overlap_width < math.pi, f"nonunique {name} sector transition")
        overlap = overlap_width - abs(change)
        require(overlap > 0, f"disjoint {name} sector transition")
        minimum_overlap = min(minimum_overlap, overlap)
        total += change
    winding = int(round(total / (2.0 * math.pi)))
    require(abs(total - 2.0 * math.pi * winding) < 1e-7, f"{name} winding")
    return winding, total, minimum_overlap


def verify_boundary_cover(homotopy: dict) -> dict[str, int]:
    leaves = homotopy["boundary_cover"]["leaves"]
    require(len(leaves) == homotopy["boundary_cover"]["leaf_count"], "leaf count")
    gate = float(homotopy["boundary_cover"]["relative_radius_gate"])
    for leaf in leaves:
        require(
            all(float(value) > 0 for value in leaf["absolute_lower_bounds"].values()),
            "boundary enclosure contains zero",
        )
        require(
            all(float(value) < gate for value in leaf["relative_radius_upper_bounds"].values()),
            "boundary enclosure exceeds radius gate",
        )
    for left, right in zip(leaves, leaves[1:]):
        require(
            abs(encoded_complex(left["end"]) - encoded_complex(right["start"]))
            < 2e-15,
            "boundary cover is not contiguous",
        )
    require(
        abs(encoded_complex(leaves[-1]["end"]) - encoded_complex(leaves[0]["start"]))
        < 2e-15,
        "boundary cover is not closed",
    )

    recomputed = {}
    for name, stored in homotopy["argument_principle"].items():
        winding, total, overlap = recompute_winding(leaves, name)
        require(winding == stored["winding_number"], f"stored {name} winding")
        require(
            abs(total - stored["total_reference_argument_change"]) < 1e-12,
            f"stored {name} argument change",
        )
        require(overlap > 0, f"{name} overlap")
        recomputed[name] = winding
    return recomputed


def verify_transport_path(transport: dict) -> None:
    waypoints = [encoded_complex(value) for value in transport["method"]["waypoints"]]
    expected = [0, 0.65, 0.65 - 0.1j, 0.82 - 0.1j, 0.82, 1]
    require(
        all(abs(left - right) < 2e-15 for left, right in zip(waypoints, expected)),
        "validated contour waypoints",
    )
    steps = transport["execution"]["steps"]
    require(len(steps) == transport["execution"]["accepted_step_count"], "step count")
    for segment_index, (left, right) in enumerate(zip(waypoints, waypoints[1:])):
        segment_steps = [
            step for step in steps if step["segment_index"] == segment_index
        ]
        require(segment_steps, f"empty segment {segment_index}")
        require(
            abs(encoded_complex(segment_steps[0]["start"]) - left) < 2e-15,
            f"segment {segment_index} start",
        )
        require(
            abs(encoded_complex(segment_steps[-1]["end"]) - right) < 2e-15,
            f"segment {segment_index} end",
        )
        for first, second in zip(segment_steps, segment_steps[1:]):
            require(
                abs(encoded_complex(first["end"]) - encoded_complex(second["start"]))
                < 2e-15,
                f"segment {segment_index} continuity",
            )
    require(
        max(step["transformed_lift_correction"] for step in steps) < 1e-6,
        "lift correction budget",
    )
    require(
        max(step["beta_increment_error"] for step in steps) < 1e-3,
        "beta increment budget",
    )


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    theorem = load(THEOREM)
    decision = load(DECISION)
    frontier = load(FRONTIER)
    homotopy = load(LOCAL_HOMOTOPY)
    transport = load(LOCAL_TRANSPORT)
    broad = load(BROAD_HOMOTOPY)

    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash")
    for authority in candidate["authority_hashes"]:
        path = ROOT / authority["path"]
        require(path.exists(), f"missing authority {path}")
        require(
            compatible_source_hash(path, authority["sha256"]),
            f"authority hash {path}",
        )

    windings = verify_boundary_cover(homotopy)
    require(
        windings
        == {
            "g_on_q_norm": 0,
            "q_discriminant": -1,
            "q_leading_coefficient": 0,
            "reduction_determinant": 0,
            "y_chart_scale": 0,
        },
        "local winding inventory",
    )
    require(homotopy["domain"]["boundary_orientation"] == "clockwise", "orientation")
    require(-windings["q_discriminant"] == 1, "collision multiplicity")
    require(homotopy["finite_flat_divisor_theorem"]["applies"], "finite flat")
    require(
        homotopy["decision"]["normal_function_endpoint_branch_preserved"],
        "normal-function branch",
    )

    # In A=R[t]/(t^2-S*t+P), multiplication by g0+g1*t has this determinant.
    for g0, g1, root_sum, root_product in [(2, 3, 5, 7), (-1, 4, -2, 9)]:
        determinant = g0 * (g0 + root_sum * g1) - (-root_product * g1) * g1
        norm = g0**2 + root_sum * g0 * g1 + root_product * g1**2
        require(determinant == norm, "quadratic quotient norm identity")

    verify_transport_path(transport)
    endpoint = transport["endpoint"]
    center = [encoded_complex(value) for value in endpoint["beta_center"]]
    center_norm = math.sqrt(sum(abs(value) ** 2 for value in center))
    radius = float(endpoint["uniform_component_radius_upper"])
    norm_lower = center_norm - math.sqrt(len(center)) * radius
    component_lower = max(abs(value) for value in center) - radius
    require(abs(center_norm - float(endpoint["center_norm"])) < 1e-14, "center norm")
    require(
        abs(norm_lower - float(endpoint["euclidean_norm_lower"])) < 1e-13,
        "endpoint norm lower bound",
    )
    require(
        abs(component_lower - float(endpoint["maximum_component_absolute_lower"]))
        < 1e-13,
        "component lower bound",
    )
    require(norm_lower > 2.25, "endpoint zero exclusion")
    require(transport["point_audit"]["maximum_connection_relative_difference"] < 2e-10, "connection audit")
    require(transport["point_audit"]["maximum_source_relative_difference"] < 2e-10, "source audit")
    require(transport["point_audit"]["maximum_residue_relative_difference"] < 1e-13, "residue audit")

    require(
        broad["argument_principle"]["reduction_determinant"]["winding_number"]
        == -4,
        "broad family obstruction",
    )
    require(
        broad["argument_principle"]["g_on_q_norm"]["winding_number"] == -1,
        "broad divisor obstruction",
    )
    require(
        not broad["decision"][
            "straight_and_full_lower_contours_homotopic_in_smooth_family"
        ],
        "broad contour promotion",
    )

    require(theorem["theorem"]["proved"], "A126 theorem")
    require(theorem["scope"]["selected_side_ell_zero_branch_excluded"], "ell=0 branch")
    require(not theorem["scope"]["global_PGL3_ell_zero_no_go"], "global no-go")
    require(not theorem["scope"]["nonzero_integral_Z92_branch_selected"], "Z92 branch")
    require(frontier["selected_side_ell_zero_branch_excluded"], "frontier ell=0")
    require(not frontier["global_ell_zero_no_go"], "frontier global no-go")
    require(not frontier["integral_period_branch_selected"], "frontier lattice")
    require(decision["open"]["interval_8x92_period_lattice"], "next period gate")
    require(candidate["checks"]["broad_contour_wrongly_promoted"] is False, "broad guard")
    require(not candidate["checks"]["observed_SM_target_fitting_used"], "target fitting")
    require(not certificate["global_no_go_proved"], "certificate global no-go")

    print("q79 A126 finite-flat homotopy and validated beta audit: PASS")
    print("local windings: reduction=0, chart=0, q2=0, disc=-1, G-norm=0")
    print(
        "validated endpoint: "
        f"||beta||_2 >= {norm_lower:.12f}, component radius <= {radius:.12f}"
    )
    print("closed: frozen selected-side ell=0 branch; open: integral Z92 branch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
