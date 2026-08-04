from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
TEXPAPERS = Path(os.environ.get("MTT_TEXPAPERS_ROOT", ROOT.parent))
QG_ROOT = Path(os.environ.get("MTT_QG_ROOT", TEXPAPERS / "12 Quantum Gravity"))
REPOSITORIES = {
    "closure-dynamics": ROOT,
    "q79-qg-corpus": QG_ROOT,
}
PACKET = ROOT / "q79_cohesive_maurer_cartan_repair_and_derived_transform_intertwiner.packet.json"


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def all_boolean_leaves_true(value: object) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, dict):
        return bool(value) and all(all_boolean_leaves_true(item) for item in value.values())
    return False


def source_checks_pass(source: dict) -> bool:
    if "checks" in source:
        return all_boolean_leaves_true(source["checks"])
    if "declared_dependency_hash_checks" in source:
        return all_boolean_leaves_true(source["declared_dependency_hash_checks"])
    return False


def verify_inputs(packet: dict) -> dict[str, dict]:
    loaded: dict[str, dict] = {}
    for label, record in packet["inputs"].items():
        repository = record["repository"]
        require(repository in REPOSITORIES, f"repository: {label}")
        path = REPOSITORIES[repository] / record["relative_path"]
        require(path.is_file(), f"source exists: {label}")
        require(sha256(path) == record["sha256"], f"source hash: {label}")
        source = load(path)
        identity = source.get("schema") or source.get("certificate")
        require(identity == record["identity"], f"source identity: {label}")
        require(source.get("status") == record["status"], f"source status: {label}")
        require(source_checks_pass(source), f"source checks: {label}")
        loaded[label] = source
    return loaded


def matrix(values: list[list[object]]) -> sp.Matrix:
    local_symbols = {"I": sp.I, "sqrt": sp.sqrt}
    return sp.Matrix(
        [
            [sp.sympify(entry, locals=local_symbols) for entry in row]
            for row in values
        ]
    )


def is_zero(value: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in value)


def hessian(expression: sp.Expr, variables: tuple[sp.Symbol, ...]) -> sp.Matrix:
    return sp.Matrix(
        [
            [sp.diff(expression, row, col) for col in variables]
            for row in variables
        ]
    )


def verify_source_composition(packet: dict, sources: dict[str, dict]) -> None:
    mc = sources["universal_heterotic_MC_Hodge_bridge"]
    require(
        mc["universal_L3_Hodge_repair_theorem"]["name"]
        == "MaurerCartanGaugeDefectHodgeRepairTheorem",
        "bound MC theorem",
    )
    require(
        mc["universal_L3_Hodge_repair_theorem"]["conclusions"][1]
        == "Hess E(0)=d1* d1+d0 d0*=Delta_1",
        "bound Hessian theorem",
    )
    cohesive = sources["twisted_cohesive_SHS_source"]
    require(
        cohesive["endomorphism_untwisting_theorem"]["global_algebra"]
        == "Omega^(0,*)(End E) is ordinary and untwisted",
        "bound ordinary End algebra",
    )
    require(
        cohesive["endomorphism_untwisting_theorem"]["nilpotence"]
        == "d_End^2(T)=[Ebar^2,T]=0",
        "bound End nilpotence",
    )
    global_twisted = sources["global_alpha_twisted_HS_object"]
    require(global_twisted["global_object"]["category"] == "D^b(J,alpha)", "SHS category")
    bht = sources["conditional_BHT_twisted_equivalence"]
    require(
        bht["claim_tiers"]["non_equivariant_twisted_derived_equivalence"]
        == "CLOSED_BY_PRIMARY_THEOREM_CONDITIONAL",
        "BHT conditional tier",
    )
    require(
        bht["claim_tiers"]["sigma_projective_descent_on_global_alpha_twisted_object"]
        == "OPEN",
        "E3 boundary",
    )
    hs_source = sources["holomorphic_HS_source"]
    require(
        hs_source["claim_tiers"]["primitive_MTT_uniqueness_of_this_representative"]
        == "OPEN_SELECTION_GATE",
        "primitive selection open",
    )

    theorem = packet["same_source_cohesive_repair_theorem"]
    require(theorem["differential"] == "d(T)=[Ebar,T]", "instantiated differential")
    require(theorem["curvature_residual"] == "F(a)=d a+a^2=(Ebar+a)^2", "MC curvature")
    require(
        theorem["Hessian_at_background"]
        == "Hess E(0)=d_1^dagger d_1+d_0 d_0^dagger=Delta_1",
        "Hodge Hessian",
    )
    require(len(theorem["canonical_without_metric"]) == 4, "algebraic rows")
    require(len(theorem["requires_selected_Hermitian_data"]) == 4, "metric rows")
    require("not identified" in theorem["guard"], "moment-map guard")

    transport = packet["conditional_BHT_deformation_transport_theorem"]
    require(len(transport["preserved"]) == 4, "derived preserved rows")
    require(len(transport["not_automatic"]) == 6, "nonautomatic rows")
    require("CONDITIONAL" in transport["tier"], "derived conditional guard")


def verify_exact_witness(packet: dict) -> None:
    witness = packet["exact_isometric_transform_witness"]
    y1, y2, z1, z2 = sp.symbols("y1 y2 z1 z2", real=True)
    y = sp.Matrix([y1, y2])
    z = sp.Matrix([z1, z2])

    d0 = matrix(witness["source_d0"])
    d1 = matrix(witness["source_d1"])
    stored_delta = matrix(witness["source_Delta1"])
    delta = sp.simplify(d1.T * d1 + d0 * d0.T)
    require(is_zero(d1 * d0), "source complex")
    require(is_zero(delta - stored_delta), "stored source Hodge")
    require(is_zero(delta - sp.eye(2)), "source Hodge identity")

    phi = sp.Matrix([y2 + y2**2, y1])
    stored_phi = sp.Matrix(
        [sp.sympify(item, locals={"y1": y1, "y2": y2}) for item in witness["source_Phi"]]
    )
    require(is_zero(phi - stored_phi), "stored source residual")
    cost = sp.expand(sp.Rational(1, 2) * phi.dot(phi))
    require(
        sp.simplify(cost - sp.sympify(witness["source_cost"], locals={"y1": y1, "y2": y2}))
        == 0,
        "stored source cost",
    )
    jacobian_zero = phi.jacobian(y).subs({y1: 0, y2: 0})
    hessian_zero = hessian(cost, (y1, y2)).subs({y1: 0, y2: 0})
    require(is_zero(jacobian_zero - matrix(witness["source_Jacobian_at_zero"])), "source Jacobian")
    require(is_zero(hessian_zero - matrix(witness["source_Hessian_at_zero"])), "source Hessian")
    require(is_zero(hessian_zero - delta), "source Hessian Hodge")

    u0 = matrix(witness["U0"])
    u1 = matrix(witness["U1"])
    u2 = matrix(witness["U2"])
    u_out = matrix(witness["U_out"])
    require(is_zero(u0.T * u0 - sp.eye(1)), "U0 isometry")
    require(is_zero(u1.T * u1 - sp.eye(2)), "U1 isometry")
    require(is_zero(u2.T * u2 - sp.eye(1)), "U2 isometry")
    require(is_zero(u_out - sp.diag(u2[0, 0], u0[0, 0])), "output isometry")

    d0_target = sp.simplify(u1 * d0 * u0.T)
    d1_target = sp.simplify(u2 * d1 * u1.T)
    require(is_zero(d0_target - matrix(witness["target_d0"])), "target d0")
    require(is_zero(d1_target - matrix(witness["target_d1"])), "target d1")
    require(is_zero(d1_target * d0_target), "target complex")
    delta_target = sp.simplify(d1_target.T * d1_target + d0_target * d0_target.T)
    require(is_zero(delta_target - matrix(witness["target_Delta1"])), "target Hodge")
    require(is_zero(delta_target - u1 * delta * u1.T), "Hodge intertwiner")

    source_coordinates = sp.simplify(u1.T * z)
    stored_coordinates = sp.Matrix(
        [
            sp.sympify(item, locals={"z1": z1, "z2": z2, "sqrt": sp.sqrt})
            for item in witness["source_coordinates_from_target"]
        ]
    )
    require(is_zero(source_coordinates - stored_coordinates), "coordinate transport")
    substitutions = {y1: source_coordinates[0], y2: source_coordinates[1]}
    phi_target = sp.simplify(u_out * phi.subs(substitutions, simultaneous=True))
    stored_target_phi = sp.Matrix(
        [
            sp.sympify(item, locals={"z1": z1, "z2": z2, "sqrt": sp.sqrt})
            for item in witness["target_Phi"]
        ]
    )
    require(is_zero(phi_target - stored_target_phi), "target residual")
    linear_mc = sp.simplify((d1_target * z)[0])
    gauge = sp.simplify((d0_target.T * z)[0])
    require(
        sp.simplify(linear_mc - sp.sympify(witness["target_MC_linear"], locals={"z1": z1, "z2": z2, "sqrt": sp.sqrt}))
        == 0,
        "target MC linear",
    )
    quadratic_mc = sp.expand(phi_target[0] - linear_mc)
    require(quadratic_mc != 0, "nonzero target quadratic")
    require(
        sp.simplify(quadratic_mc - sp.sympify(witness["target_MC_quadratic"], locals={"z1": z1, "z2": z2, "sqrt": sp.sqrt}))
        == 0,
        "target MC quadratic",
    )
    require(sp.simplify(phi_target[1] - gauge) == 0, "target gauge")

    target_cost = sp.expand(sp.Rational(1, 2) * phi_target.dot(phi_target))
    source_cost_substituted = sp.expand(cost.subs(substitutions, simultaneous=True))
    require(sp.simplify(target_cost - source_cost_substituted) == 0, "isometric cost")
    require(witness["cost_residual_after_coordinate_change"] == "0", "stored cost residual")
    target_jacobian_zero = phi_target.jacobian(z).subs({z1: 0, z2: 0})
    require(
        is_zero(target_jacobian_zero - u_out * jacobian_zero * u1.T),
        "Jacobian conjugacy",
    )
    target_hessian_zero = hessian(target_cost, (z1, z2)).subs({z1: 0, z2: 0})
    require(is_zero(target_hessian_zero - u1 * hessian_zero * u1.T), "Hessian conjugacy")
    require(is_zero(target_hessian_zero - delta_target), "target Hessian Hodge")
    require(
        is_zero(-target_hessian_zero - matrix(witness["target_repair_Jacobian_at_zero"])),
        "repair linearization",
    )


def verify_boundary(packet: dict) -> None:
    sufficient = packet["isometric_intertwiner_sufficient_condition"]
    require(len(sufficient["chain_rows"]) == 3, "isometric rows")
    require(len(sufficient["consequences"]) == 5, "isometric consequences")
    require(sufficient["physical_status"].startswith("OPEN"), "physical intertwiner open")
    delta = packet["frontier_delta"]
    require(len(delta["newly_closed"]) == 4, "new advances")
    require(len(delta["not_reproved"]) == 4, "reused results")
    require(delta["strict_physical_upper_state_closed"] == 3, "strict count")
    require(delta["strict_physical_upper_state_total"] == 13, "strict total")
    require(len(packet["open"]) == 6, "open rows")
    parameters = packet["parameter_ledger"]
    require(parameters["new_fitted_parameters"] == 0, "fitted parameters")
    require(parameters["new_observed_values"] == 0, "observed values")
    require(parameters["algebraic_MC_coefficients_added"] == 0, "MC coefficients")
    require(parameters["Hermitian_metric_physically_selected_here"] is False, "metric guard")
    require(
        packet["next_theorem"]["name"]
        == "q79SelectedPhysicalV3W9CohesiveEndpointAndIsometricFiniteIntertwiner.v1",
        "next theorem",
    )
    require(len(packet["next_theorem"]["required_rows"]) == 6, "next rows")
    require(len(packet["primary_mathematical_sources"]) == 4, "sources")
    require(len(packet["checks"]) == 33 and all(packet["checks"].values()), "checks")


def main() -> int:
    packet = load(PACKET)
    require(
        packet["schema"]
        == "MTTQ79CohesiveMaurerCartanRepairAndDerivedTransformIntertwiner.v1",
        "schema",
    )
    require(
        packet["theorem"]["name"]
        == "q79CohesiveMaurerCartanRepairAndDerivedTransformIntertwinerTheorem",
        "theorem name",
    )
    require(packet["theorem"]["fitted_parameters"] == 0, "theorem parameters")
    require(packet["theorem"]["observed_values_used"] == 0, "theorem observations")
    sources = verify_inputs(packet)
    verify_source_composition(packet, sources)
    verify_exact_witness(packet)
    verify_boundary(packet)
    print(
        "Q79_COHESIVE_MAURER_CARTAN_REPAIR_AND_DERIVED_TRANSFORM_INTERTWINER_VERIFY_PASS"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
