from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
TEXPAPERS = Path(os.environ.get("MTT_TEXPAPERS_ROOT", ROOT.parent))
QG_ROOT = Path(os.environ.get("MTT_QG_ROOT", TEXPAPERS / "12 Quantum Gravity"))
PACKET = ROOT / "q79_global_fitting_descent_and_spectral_divisor_match.packet.json"


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


def source_path(record: dict) -> Path:
    roots = {
        "closure-dynamics": ROOT,
        "quantum-gravity": QG_ROOT,
    }
    require(record["repository"] in roots, "known source repository")
    return roots[record["repository"]] / record["relative_path"]


def verify_inputs(packet: dict) -> dict[str, dict]:
    sources: dict[str, dict] = {}
    for label, record in packet["inputs"].items():
        path = source_path(record)
        require(path.is_file(), f"source exists: {label}")
        require(sha256(path) == record["sha256"], f"source hash: {label}")
        source = load(path)
        identity = source.get("schema") or source.get("certificate")
        require(identity == record["identity"], f"source identity: {label}")
        require(source["status"] == record["status"], f"source status: {label}")
        require(source_checks_pass(source), f"source checks: {label}")
        sources[label] = source
    require(len(sources) == 7, "seven bound sources")
    return sources


def verify_local_global_match(packet: dict, sources: dict[str, dict]) -> None:
    local = sources["local_resolved_cone"]
    hs_source = sources["holomorphic_HS_source"]
    global_object = sources["global_alpha_twisted_object"]
    determinant_source = sources["spectral_determinant"]

    expected_fitting = {
        "Fitt_0_coker": "((r*t)^3)",
        "Fitt_1_coker": "((r*t)^2)",
        "Fitt_2_coker": "(r*t)",
        "Fitt_3_coker": "(a,r,t)",
        "Fitt_4_coker": "R",
    }
    fitting = local["determinantal_and_Fitting_theorem"]
    for key, value in expected_fitting.items():
        require(fitting[key] == value, f"source fitting: {key}")

    a, r, t = sp.symbols("a r t")
    ext = sp.diag(a, 1, 1)
    matrix = ext.row_join(r * sp.eye(3)).col_join(
        (-t * sp.eye(3)).row_join(sp.zeros(3))
    )
    require(sp.factor(matrix.det()) == (r * t) ** 3, "independent determinant")

    match = packet["local_to_global_divisor_match"]
    require(match["determinant"] == "r**3*t**3", "packet determinant")
    require(match["local_Fitting_ladder"] == expected_fitting, "packet fitting ladder")
    require(match["reduced_support_class_H_D0"] == [1, 1], "support vector")
    require(match["zeroth_Fitting_divisor_class_H_D0"] == [3, 3], "divisor vector")
    require(match["zeroth_Fitting_ideal_sheaf"] == "O_J(-3H-3D0)", "Fitt0 sheaf")
    require(match["zeroth_Fitting_divisor"] == "3H+3D0", "Fitt0 divisor")
    require(match["first_Fitting_ideal_sheaf"] == "O_J(-2H-2D0)", "Fitt1 sheaf")
    require(match["second_Fitting_ideal_sheaf"] == "O_J(-H-D0)", "Fitt2 sheaf")
    require(match["third_Fitting_local_germ"] == "(a,r,t)", "Fitt3 germ")
    require(match["exact_match"] is True, "exact class match")

    require(
        hs_source["lci_curve"]["base_degree2_section"]
        == "a with div(a)={u=0,W=+3}+{u=0,W=-3}",
        "selected two-point divisor",
    )
    require(
        global_object["twisted_Chern_symbol"]["virtual_codimension1_class"]
        == "3H+3D0",
        "BHT support class",
    )
    require(
        determinant_source["line_identification"]["determinant"]
        == "O_J(3H+3D0)",
        "global determinant line",
    )


def verify_descent_tier(packet: dict, sources: dict[str, dict]) -> None:
    global_object = sources["global_alpha_twisted_object"]
    global_data = global_object["global_object"]
    require(global_data["category"] == "D^b(J,alpha)", "twisted category")

    descent = packet["twisted_Fitting_descent_theorem"]
    require(
        descent["conclusion"]
        == "every Fitt_k(H^q(S_HS)) is a canonical ordinary ideal sheaf on J",
        "descent conclusion",
    )
    require(descent["literal_overlap_matrices_required_for_this_conclusion"] is False, "intrinsic descent")
    require(descent["literal_overlap_matrices_required_for_connection_execution"] is True, "connection boundary")
    require(len(descent["invariance"]) == 4, "four descent invariances")

    symbolic_fields = (
        global_data["kernel_transition"],
        global_data["local_chain_transition"],
        global_data["triple_overlap_law"],
    )
    require(all(isinstance(value, str) for value in symbolic_fields), "symbolic overlap fields")
    forbidden = {
        "overlap_matrices",
        "overlap_chain_matrices",
        "chain_homotopies",
        "triple_overlap_matrix_products",
    }
    require(forbidden.isdisjoint(global_data), "no literal overlap payload")
    audit = packet["source_audit"]
    require(audit["symbolic_overlap_law_present"] is True, "symbolic law retained")
    require(audit["literal_overlap_matrix_payload_present"] is False, "literal boundary")


def verify_endpoint_tiers(packet: dict, sources: dict[str, dict]) -> None:
    transport = sources["hidden_topological_transport"]
    hym = sources["invariant_split_HYM_reduction"]
    bott_chern = sources["invariant_Bott_Chern_source_reduction"]
    transport_tiers = transport["claim_tiers"]
    require(
        transport_tiers["actual_smooth_P39_representative_with_cover_rows"]
        == "CLOSED_EXACT_CONSTRUCTIVE_SELECTED_K0",
        "topological endpoint",
    )
    require(transport_tiers["balanced_HYM_connection"] == "OPEN", "HYM open")
    require(
        all(
            value == "OPEN"
            for value in hym["single_remaining_source_object"]["required_rows"].values()
        ),
        "split-source rows open",
    )
    require(
        "removal of two separate exact quadratic-form rows as mandatory Aeppli premises"
        in bott_chern["revised_frontier"]["closed_here"],
        "Bott-Chern gate reduction",
    )

    endpoint = packet["physical_endpoint_reclassification"]
    require(
        endpoint["hidden_W9_smooth_projective_topological_endpoint"]
        == "CLOSED_EXACT_SELECTED_K0",
        "packet topological endpoint",
    )
    require(endpoint["hidden_W9_balanced_HYM"] == "OPEN", "packet HYM boundary")
    require(
        endpoint["exact_HYM_Chern_Weil_split_source"]
        == "OPTIONAL_SUFFICIENT_ROUTE_NOT_MANDATORY_FOR_AEPPLI",
        "split-source reclassification",
    )
    require(
        endpoint["basic_total_Chern_Weil_or_positive_metric_exit"] == "OPEN",
        "positive metric exit",
    )
    require(
        endpoint["visible_V3_relation"]
        == "SEPARATE_SOURCE_BRANCH_NOT_EMITTED_BY_THIS_HIDDEN_HS_CONE",
        "visible-hidden typing",
    )
    require(endpoint["continuum_to_finite_physical_intertwiner"] == "OPEN", "finite boundary")


def main() -> None:
    packet = load(PACKET)
    require(
        packet["schema"] == "MTTQ79GlobalFittingDescentAndSpectralDivisorMatch.v1",
        "schema",
    )
    sources = verify_inputs(packet)
    verify_local_global_match(packet, sources)
    verify_descent_tier(packet, sources)
    verify_endpoint_tiers(packet, sources)

    require(all_boolean_leaves_true(packet["checks"]), "packet checks")
    require(packet["parameter_ledger"]["new_continuous_parameters"] == 0, "continuous parameters")
    require(packet["parameter_ledger"]["new_discrete_fitted_parameters"] == 0, "discrete parameters")
    require(packet["parameter_ledger"]["observed_masses_or_mixings_used"] == 0, "observed inputs")
    guardrails = packet["guardrails"]
    require(guardrails and all(value is False for value in guardrails.values()), "guardrails")
    require(
        packet["frontier_delta"]["next_primary_target"]
        == "q79SelectedHolomorphicNonpullbackV3W9WorldsheetSource.v1",
        "next primary target",
    )

    print("Q79_GLOBAL_FITTING_DESCENT_AND_SPECTRAL_DIVISOR_MATCH_VERIFY_PASS")


if __name__ == "__main__":
    main()
