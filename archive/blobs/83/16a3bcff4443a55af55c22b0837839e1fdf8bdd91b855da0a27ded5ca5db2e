from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

import sympy as sp
from flint import acb, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from q79_y_chart_conservative_extension import compatible_source_hash


SLUG = "selected_q79covariantperiodbranchcutsetandtightbetatransport"
OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"
TIGHT = OUT / "tight_selected_side_endpoint_beta.theorem.packet.json"
CUTSET = OUT / "same_carrier_integral_branch_cutset.theorem.packet.json"
PERIOD_INPUT = OUT / "selected_alignment_period_execution_input.packet.json"
FRONTIER = OUT / "U6_frontier_after_A127.packet.json"
DISCRIMINANT = OUT / "selected_alignment_dual_discriminant.interval.packet.json"
FAN = OUT / "selected_alignment_distinguished_radial_fan.interval.packet.json"
MONODROMY = OUT / "selected_alignment_meridian_monodromy_batch.packet.json"
IDENTITY_DISCRIMINANT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2lefschetzperiodreduction"
    / "degree90_nodal_discriminant_certificate.packet.json"
)
HOMOLOGY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
MONODROMY_WORKER = (
    ROOT / "scripts" / "compute_q79_selected_alignment_single_meridian_monodromy.py"
)
SELECTED_ROOT_TRANSPORT = (
    ROOT / "scripts" / "q79_selected_alignment_genus2_root_transport.py"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def decode_acb(value: dict[str, str]) -> acb:
    return acb(arb(value["real"]), arb(value["imaginary"]))


def decoded_complex(value: dict) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def lower(value: arb) -> float:
    return math.nextafter(float(value.lower()), -math.inf)


def evaluate(coefficients: list[acb], value: acb) -> acb:
    result = acb(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def main() -> int:
    ctx.dps = 100
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    tight = load(TIGHT)
    cutset = load(CUTSET)
    period_input = load(PERIOD_INPUT)
    frontier = load(FRONTIER)
    discriminant = load(DISCRIMINANT)
    fan = load(FAN)
    monodromy = load(MONODROMY)

    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash")
    for authority in candidate["authority_hashes"]:
        path = ROOT / authority["path"]
        require(path.exists(), f"missing authority {path}")
        require(
            compatible_source_hash(path, authority["sha256"]),
            f"authority hash {path}",
        )

    endpoint = tight["tight_endpoint"]
    center = [decoded_complex(value) for value in endpoint["beta_center"]]
    center_norm = math.sqrt(sum(abs(value) ** 2 for value in center))
    radius = float(endpoint["uniform_component_radius_upper"])
    norm_lower = center_norm - math.sqrt(len(center)) * radius
    require(abs(center_norm - float(endpoint["center_norm"])) < 1e-14, "beta center norm")
    require(abs(norm_lower - float(endpoint["euclidean_norm_lower"])) < 1e-13, "beta norm lower")
    require(norm_lower > 2.337, "tight beta zero exclusion")
    require(tight["radius_improvement_factor"] > 5, "beta radius improvement")
    require(tight["scope"]["frozen_selected_ell_zero_branch_excluded"], "ell=0 branch")
    require(not tight["scope"]["nonzero_integral_branch_decided"], "integral branch guard")

    dual_rows = discriminant["dual_discriminant"]["integer_coefficient_rows"]
    l0, l1, l2, a, b = sp.symbols("l0 l1 l2 a b")
    dual = sp.Poly(
        sum(
            int(row["coefficient"])
            * l0 ** int(row["powers_L0_L1_L2"][0])
            * l1 ** int(row["powers_L0_L1_L2"][1])
            * l2 ** int(row["powers_L0_L1_L2"][2])
            for row in dual_rows
        ),
        l0,
        l1,
        l2,
        domain=sp.ZZ,
    )
    require(dual.total_degree() == 30, "dual discriminant degree")
    require(len(dual.terms()) == 496, "dual discriminant term count")
    identity = sp.expand(dual.as_expr().subs({l0: a, l1: b, l2: 1}))
    reduced = sp.rem(
        sp.Poly(identity, b, domain=sp.QQ[a]),
        sp.Poly(b**2 - a**3 + a, b, domain=sp.QQ[a]),
    ).as_expr()
    reduced_poly = sp.Poly(reduced, b, domain=sp.QQ[a])
    identity_packet = load(IDENTITY_DISCRIMINANT)["discriminant_on_E"]
    require(
        sp.expand(reduced_poly.coeff_monomial(1) - sp.sympify(identity_packet["P45"])) == 0,
        "identity P45 crosscheck",
    )
    require(
        sp.expand(reduced_poly.coeff_monomial(b) - sp.sympify(identity_packet["Q43"])) == 0,
        "identity Q43 crosscheck",
    )

    norm_coefficients = [
        decode_acb(row["coefficient"])
        for row in discriminant["norm90"]["coefficients_ascending"]
    ]
    norm_derivative = [
        norm_coefficients[index] * index for index in range(1, 91)
    ]
    roots = [decode_acb(value) for value in discriminant["norm90"]["roots"]]
    require(len(roots) == 90, "selected norm root count")
    for root_index, root in enumerate(roots):
        require(evaluate(norm_coefficients, root).contains(0), "root misses N90")
        derivative_lower = lower(abs(evaluate(norm_derivative, root)))
        require(
            derivative_lower > 0,
            f"multiple N90 root {root_index}: lower={derivative_lower}",
        )
    require(
        min(lower(abs(left - right)) for index, left in enumerate(roots) for right in roots[:index])
        > 0.0054,
        "selected norm root separation",
    )
    require(discriminant["critical_points_on_E"]["count"] == 90, "critical lifts")
    for point in discriminant["critical_points_on_E"]["points"]:
        a_value = decode_acb(point["a"])
        b_value = decode_acb(point["b"])
        require((b_value**2 - a_value**3 + a_value).contains(0), "elliptic lift")
        require(float(point["b_absolute_lower"]) > 0, "critical b zero")
        require(float(point["norm_derivative_absolute_lower"]) > 0, "critical simplicity")

    clearances = {key: float(value) for key, value in fan["geometric_certificate"].items()}
    require(len(clearances) == 11, "selected fan clearance inventory")
    require(all(value > 0 for value in clearances.values()), "selected fan clearance")
    require(len(fan["distinguished_positive_meridians"]) == 90, "selected fan count")
    require(fan["topology"]["all_paths_avoid_selected_y_chart_zero_balls"], "chart avoidance")

    homology = load(HOMOLOGY)["homology_convention"]
    intersection = sp.Matrix(homology["intersection_matrix"])
    require(
        monodromy["authority"]["worker_sha256"] == sha256(MONODROMY_WORKER),
        "monodromy worker authority",
    )
    require(
        monodromy["authority"]["selected_root_transport_sha256"]
        == sha256(SELECTED_ROOT_TRANSPORT),
        "selected root-transport authority",
    )
    require(len(monodromy["rows"]) == 90, "monodromy row count")
    for row in monodromy["rows"]:
        path = ROOT / row["packet_path"]
        require(sha256(path) == row["packet_sha256"], f"monodromy hash {path}")
        packet = load(path)
        matrix = sp.Matrix(packet["homology"]["integral_picard_lefschetz_matrix"])
        delta = matrix - sp.eye(4)
        require(matrix.T * intersection * matrix == intersection, "symplectic monodromy")
        require(delta.rank() == 1 and delta * delta == sp.zeros(4), "PL transvection")
        permutation = packet["braid"]["final_root_permutation"]
        require(sum(value != index for index, value in enumerate(permutation)) == 2, "root transposition")
        require(not packet["strict_scope"]["local_monodromy_promoted"], "tube overpromotion")

    require(cutset["theorem"]["proved"], "same-carrier theorem")
    require(not cutset["scope"]["cross_carrier_A126_A119_residual_has_proof_status"], "cross-carrier guard")
    require(cutset["scope"]["endpoint_basis_invariance_proved"], "basis invariance")
    require(period_input["closed_inputs"]["simple_nodal_critical_values"] == 90, "period input nodes")
    require(period_input["closed_inputs"]["pointwise_integral_PL_matrices"] == 90, "period input matrices")
    require(period_input["strict_scope"]["endpoint_period_rows_emitted"] == 0, "period row guard")
    require(frontier["cross_carrier_A119_reuse_retired"], "frontier carrier guard")
    require(frontier["selected_alignment_pointwise_PL_matrices"] == 90, "frontier monodromy")
    require(frontier["selected_alignment_period_columns"] == 0, "frontier period guard")
    require(not certificate["integral_branch_selected"], "certificate branch guard")

    print("q79 A127 same-carrier selected-alignment period input audit: PASS")
    print(
        f"tight beta: ||beta||_2 >= {norm_lower:.12f}, radius <= {radius:.12f}"
    )
    print(
        "selected endpoint: 90 simple nodes, 90 certified paths, "
        "90 pointwise PL matrices"
    )
    print("open: continuous root tubes, endpoint H2 basis, 8x92 period rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
