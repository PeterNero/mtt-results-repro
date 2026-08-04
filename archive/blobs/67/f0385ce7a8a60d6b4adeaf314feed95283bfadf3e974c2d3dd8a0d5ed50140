from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
REPOSITORIES = {"closure-dynamics": ROOT}
PACKET = ROOT / "q79_augmented_endpoint_hilbert_spectral_compiler.packet.json"


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix(values: list[list[object]]) -> sp.Matrix:
    return sp.Matrix([[sp.sympify(entry) for entry in row] for row in values])


def is_zero(value: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in value)


def spectrum(value: sp.MatrixBase) -> dict[str, int]:
    return {
        str(sp.simplify(eigenvalue)): int(multiplicity)
        for eigenvalue, multiplicity in value.eigenvals().items()
    }


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
        require(all(source["checks"].values()), f"source checks: {label}")
        loaded[label] = source
    return loaded


def verify_route(packet: dict, sources: dict[str, dict]) -> None:
    route = packet["route_correction"]
    augmented = sources["augmented_route_correction"]
    current = augmented["primary_heterotic_total_complex"]
    require(route["current_complex"] == current["degree_spaces"], "current complex")
    require(route["current_differential"] == current["block_form"], "current differential")
    require(route["cochain_relations"] == current["cochain_conditions"], "cochain relations")
    require(
        route["Q_Hodge_compression"]
        == "p_Q Delta_Y,1 i_Q=Delta_Q,1+(1/4)A_0 A_0^dagger",
        "Hodge compression",
    )
    require(
        augmented["superseded_direct_target"]["retired_claim"]
        == "the full heterotic L3 degree spaces and differential can be identified directly with Q_phys and Dbar_Q alone",
        "retired direct target",
    )
    require(
        sources["BK3_cohomology_survival"]["frontier_delta"]
        ["physical_prerequisite_count_after"]
        == "1/6",
        "BK3 current count",
    )


def verify_weighted_witness(packet: dict) -> None:
    witness = packet["exact_weighted_total_complex_witness"]
    l0 = matrix(witness["L0"])
    l1 = matrix(witness["L1"])
    g0 = matrix(witness["G0"])
    g1 = matrix(witness["G1"])
    g2 = matrix(witness["G2"])
    stored_l0_adjoint = matrix(witness["L0_adjoint"])
    stored_l1_adjoint = matrix(witness["L1_adjoint"])
    stored_jacobian = matrix(witness["residual_Jacobian"])
    stored_residual_adjoint = matrix(witness["residual_adjoint"])
    stored_hodge = matrix(witness["weighted_hodge"])
    stored_naive = matrix(witness["naive_unweighted_hodge"])

    require(is_zero(l1 * l0), "cochain condition")
    for index, metric in enumerate((g0, g1, g2)):
        require(metric == metric.T, f"metric symmetry {index}")
        require(metric.is_positive_definite is True, f"metric positivity {index}")

    l0_adjoint = sp.simplify(g0.inv() * l0.T * g1)
    l1_adjoint = sp.simplify(g1.inv() * l1.T * g2)
    hodge = sp.simplify(l1_adjoint * l1 + l0 * l0_adjoint)
    jacobian = l1.col_join(l0_adjoint)
    defect_metric = sp.diag(g2, g0)
    residual_adjoint = sp.simplify(g1.inv() * jacobian.T * defect_metric)
    gram = sp.simplify(residual_adjoint * jacobian)
    naive = sp.simplify(l1.T * l1 + l0 * l0.T)

    require(is_zero(l0_adjoint - stored_l0_adjoint), "stored L0 adjoint")
    require(is_zero(l1_adjoint - stored_l1_adjoint), "stored L1 adjoint")
    require(is_zero(jacobian - stored_jacobian), "stored Jacobian")
    require(is_zero(residual_adjoint - stored_residual_adjoint), "stored residual adjoint")
    require(is_zero(hodge - stored_hodge), "stored Hodge")
    require(is_zero(naive - stored_naive), "stored naive Hodge")
    require(is_zero(hodge - gram), "Gram identity")
    require(is_zero(hodge.T * g1 - g1 * hodge), "metric self-adjointness")
    require(hodge == sp.Rational(14, 5) * sp.eye(2), "exact weighted Hodge")
    require(naive == 2 * sp.eye(2), "exact naive Hodge")
    require(not is_zero(hodge - naive), "unweighted transpose no-go")
    require(spectrum(hodge) == witness["weighted_hodge_spectrum"], "stored spectrum")
    require(spectrum(hodge) == {"14/5": 2}, "independent spectrum")
    require(witness["bare_Q_hodge"] == "1", "bare Q Hodge")
    require(witness["full_augmented_Q_compression"] == "2", "full compression")
    require(witness["positive_Q_compression_correction"] == "1", "positive correction")


def verify_source_cutset(packet: dict, sources: dict[str, dict]) -> None:
    cutset = packet["corrected_physical_source_cutset"]
    ledger = cutset["physical_gate_ledger"]
    require(len(ledger) == cutset["physical_total"] == 6, "six gate ledger")
    require(cutset["physically_closed_now"] == 1, "physical count")
    require(cutset["conditionally_derived_after_endpoint"] == 2, "derived count")
    require(cutset["independent_compound_source_objects"] == 2, "source count")
    require(
        sum("CLOSED_EXACT" in row["status"] for row in ledger.values()) == 1,
        "one closed row",
    )
    require(
        sum("CONDITIONAL_DERIVED" in row["status"] for row in ledger.values()) == 2,
        "two derived rows",
    )
    require(
        {row["dependency"] for row in ledger.values() if row["dependency"] in {"S_cont", "T_fin"}}
        == {"S_cont", "T_fin"},
        "two dependencies",
    )
    require(len(cutset["S_cont"]["must_emit"]) == 4, "continuum source rows")
    require(len(cutset["S_cont"]["automatically_derives"]) == 3, "derived rows")
    require(len(cutset["T_fin"]["must_emit"]) == 4, "finite source rows")
    require("not two fitted scalar" in cutset["source_counting"], "source typing")

    sector = sources["sector_polarized_compiler"]["source_readiness"]
    require(not sector["selected_characteristic_zero_visible_U_eta9"], "visible open")
    require(not sector["hidden_physical_twisted_locally_free_rank9_endpoint"], "hidden open")
    require(not sector["one_common_positive_Gauduchon_chamber_and_HYM_pair"], "HYM open")
    require(
        sources["warped_product_regime_split"]["q79_regime_split"]
        ["physical_warped_branch"]["status"]
        == "OPEN",
        "warp regime open",
    )


def verify_compiler_boundary(packet: dict) -> None:
    compiler = packet["endpoint_to_Hilbert_compiler"]
    require(len(compiler["hypotheses"]) == 5, "compiler hypotheses")
    require(len(compiler["derived_objects"]) == 7, "compiler outputs")
    require("boundary" in compiler["boundary"], "boundary guard")
    residual = packet["same_source_augmented_residual_theorem"]
    require(residual["zero_defect"] == "Phi_Y(C_*)=0", "zero defect")
    require(
        residual["Hessian"]
        == "Hess E_Y(C_*)=J_1^dagger J_1=Delta_Y,1",
        "residual Hessian",
    )
    require(residual["physical_status"].startswith("OPEN"), "physical residual boundary")

    spectral = packet["spectral_Galerkin_theorem"]
    require("compact resolvent" in spectral["finite_rank_condition"], "compactness condition")
    require("not independent constants" in spectral["row_source"], "row source")
    require("27-state" in spectral["accepted_finite_carrier_boundary"], "finite carrier boundary")


def main() -> int:
    packet = load(PACKET)
    require(packet["schema"] == "MTTQ79AugmentedEndpointHilbertSpectralCompiler.v1", "schema")
    require(
        packet["theorem"]["name"]
        == "q79AugmentedEndpointHilbertSpectralCompilerTheorem",
        "theorem name",
    )
    require(packet["theorem"]["fitted_parameters"] == 0, "fitted parameters")
    require(packet["theorem"]["observed_values_used"] == 0, "observed values")
    sources = verify_inputs(packet)
    verify_route(packet, sources)
    verify_weighted_witness(packet)
    verify_source_cutset(packet, sources)
    verify_compiler_boundary(packet)

    parameters = packet["parameter_ledger"]
    require(parameters["new_physical_couplings"] == 0, "physical couplings")
    require(parameters["remaining_compound_source_maps"] == 2, "remaining maps")
    require(len(packet["closed"]) == 6, "closed rows")
    require(len(packet["open"]) == 5, "open rows")
    require(
        packet["next_theorem"]["name"]
        == "q79SelectedAugmentedContinuumResidualAndFiniteIntertwiner.v1",
        "next theorem",
    )
    require(len(packet["checks"]) == 32 and all(packet["checks"].values()), "packet checks")
    print("Q79_AUGMENTED_ENDPOINT_HILBERT_SPECTRAL_COMPILER_VERIFY_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
