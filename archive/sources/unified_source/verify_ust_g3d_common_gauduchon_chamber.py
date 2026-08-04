#!/usr/bin/env python3
"""Exact compiler for UST.G3D common Gauduchon-HYM chamber packets."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import subprocess
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
DEFAULT_PACKET = ROOT / "state" / "ust_g3d_reference_common_chamber.packet.json"
RESULT_PACKET = ROOT / "state" / "ust_g3d_common_gauduchon_chamber.packet.json"
SCHEMA_PATH = ROOT / "state" / "ust_g3d_common_gauduchon_chamber.schema.json"
LOCK_PATH = ROOT / "state" / "upstream-lock.json"
THEOREM_PATH = ROOT / "UST_G3D_SPECTRAL_TO_COMMON_GAUDUCHON_HYM_CHAMBER_THEOREM_v1.md"

SCHEMA_ID = "mtt.unified-source.common-gauduchon-chamber-certificate.v1"
RESULT_SCHEMA_ID = "mtt.unified-source.common-gauduchon-chamber-result.v1"
QG_REPOSITORY_ID = "q79-quantum-gravity"
QG_COMMIT = "1fa48cb247ff3098e46d1e39ca770287510a4959"
BASE_REPOSITORY_ID = "q79-protospinor-gr-response"
BASE_COMMIT = "a350d0d1a706845205d669542cf344750033c6f6"
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
RATIONAL = re.compile(r"^-?[0-9]+(?:/[1-9][0-9]*)?$")
GRADES = {"PASS", "FAIL", "PARTIAL", "CONDITIONAL", "OPEN", "NOT_SOURCE"}
MODES = {"irreducible_spectral_cover", "finite_stable_orbit", "open"}
BOUND_METHODS = {"exact_harder_narasimhan", "reference_curvature_interval", "open"}

TOP_FIELDS = {
    "schema", "candidate_id", "source_orbit_id", "source_hash",
    "evidence_grade", "complete_physical_pair", "base_geometry", "factors",
    "common_t", "empirical_inputs", "physical_promotion_requested",
}
BASE_FIELDS = {
    "same_q79_principal_elliptic_fibration", "H_square", "H_dot_delta",
    "delta_square", "primitive_harmonic_curvature", "balanced_ray_certificate",
}
FACTOR_FIELDS = {
    "id", "sector", "physical_rank", "twist_order", "spectral_mode",
    "orbit_factor_count", "factor_rank", "locally_free",
    "determinant_trivial", "relative_degree_zero_semistable",
    "spectral_object_selected", "factor_support_reduced",
    "factor_support_irreducible", "physical_topology_match",
    "physical_topology_certificate", "fiber_gap", "mu1_upper_bound",
    "mu1_bound_method", "mu1_bound_certificate",
    "holomorphic_equivariant_descent", "unitary_multiplier",
    "evidence_grade", "provenance",
}
PROVENANCE_FIELDS = {"source_hash", "artifact", "locator"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def q(value: str | int, label: str) -> Fraction:
    require(not isinstance(value, bool), f"{label}: boolean is not rational data")
    require(
        isinstance(value, int) or (isinstance(value, str) and RATIONAL.fullmatch(value)),
        f"{label}: expected exact integer or rational string",
    )
    return Fraction(value)


def validate_factor(factor: dict[str, Any], source_hash: str) -> dict[str, Any]:
    factor_id = factor.get("id", "<missing>")
    require(set(factor) == FACTOR_FIELDS, f"{factor_id}: missing or unexpected fields")
    require(isinstance(factor_id, str) and bool(factor_id), "factor id")
    require(factor["sector"] in {"visible", "hidden"}, f"{factor_id}: sector")
    require(factor["evidence_grade"] in GRADES, f"{factor_id}: evidence grade")
    require(factor["spectral_mode"] in MODES, f"{factor_id}: spectral mode")
    require(factor["mu1_bound_method"] in BOUND_METHODS, f"{factor_id}: slope-bound method")

    for field in ("physical_rank", "twist_order", "orbit_factor_count", "factor_rank"):
        require(
            isinstance(factor[field], int) and not isinstance(factor[field], bool)
            and factor[field] > 0,
            f"{factor_id}: {field} must be a positive integer",
        )

    expected_rank = 3 if factor["sector"] == "visible" else 9
    expected_twist = 1 if factor["sector"] == "visible" else 3
    rank_correct = factor["physical_rank"] == expected_rank
    twist_correct = factor["twist_order"] == expected_twist
    rank_compiles = (
        factor["orbit_factor_count"] * factor["factor_rank"]
        == factor["physical_rank"]
    )
    require(rank_compiles, f"{factor_id}: factor ranks do not compile to physical rank")

    mode = factor["spectral_mode"]
    irreducible_mode = (
        mode == "irreducible_spectral_cover"
        and factor["orbit_factor_count"] == 1
        and factor["factor_rank"] == factor["physical_rank"]
        and factor["factor_support_reduced"] is True
        and factor["factor_support_irreducible"] is True
    )
    finite_orbit_mode = (
        mode == "finite_stable_orbit"
        and factor["sector"] == "hidden"
        and factor["orbit_factor_count"] > 1
        and factor["factor_support_reduced"] is True
        and factor["factor_support_irreducible"] is True
        and factor["unitary_multiplier"] is True
    )
    accepted_mode = irreducible_mode or finite_orbit_mode

    provenance = factor["provenance"]
    require(set(provenance) == PROVENANCE_FIELDS, f"{factor_id}: provenance fields")
    require(
        all(isinstance(provenance[field], str) and provenance[field] for field in PROVENANCE_FIELDS),
        f"{factor_id}: incomplete provenance",
    )
    same_source = provenance["source_hash"] == source_hash

    gap = q(factor["fiber_gap"], f"{factor_id}.fiber_gap")
    mu_bound = q(factor["mu1_upper_bound"], f"{factor_id}.mu1_upper_bound")
    canonical_gap = Fraction(2, factor["twist_order"])
    require(gap == canonical_gap, f"{factor_id}: q79 canonical fiber gap must be 2/twist_order")
    positive_gap = gap > 0
    nonnegative_mu_bound = mu_bound >= 0
    threshold = None
    if positive_gap and nonnegative_mu_bound:
        threshold = Fraction(1) + Fraction(factor["factor_rank"] - 1) * mu_bound / gap

    bool_fields = (
        "locally_free", "determinant_trivial", "relative_degree_zero_semistable",
        "spectral_object_selected", "factor_support_reduced",
        "factor_support_irreducible", "physical_topology_match",
        "holomorphic_equivariant_descent",
        "unitary_multiplier",
    )
    require(
        all(isinstance(factor[field], bool) for field in bool_fields),
        f"{factor_id}: structural flags must be boolean",
    )

    structural_pass = all(
        factor[field] is True
        for field in (
            "locally_free", "determinant_trivial",
            "relative_degree_zero_semistable", "spectral_object_selected",
            "factor_support_reduced", "factor_support_irreducible",
            "physical_topology_match",
            "holomorphic_equivariant_descent",
        )
    )
    require(
        isinstance(factor["physical_topology_certificate"], str)
        and bool(factor["physical_topology_certificate"]),
        f"{factor_id}: physical topology certificate",
    )
    require(
        isinstance(factor["mu1_bound_certificate"], str)
        and bool(factor["mu1_bound_certificate"]),
        f"{factor_id}: slope-bound certificate",
    )
    certified_mu_bound = factor["mu1_bound_method"] != "open"
    accepted = all((
        rank_correct,
        twist_correct,
        accepted_mode,
        positive_gap,
        nonnegative_mu_bound,
        structural_pass,
        certified_mu_bound,
        same_source,
        factor["evidence_grade"] == "PASS",
    ))

    return {
        "id": factor_id,
        "sector": factor["sector"],
        "rank_correct": rank_correct,
        "twist_correct": twist_correct,
        "rank_compiles": rank_compiles,
        "accepted_mode": accepted_mode,
        "same_source": same_source,
        "canonical_gap": canonical_gap,
        "certified_mu_bound": certified_mu_bound,
        "threshold": threshold,
        "accepted": accepted,
    }


def validate_packet(packet: dict[str, Any]) -> dict[str, Any]:
    require(set(packet) == TOP_FIELDS, "missing or unexpected packet fields")
    require(packet["schema"] == SCHEMA_ID, "candidate schema")
    require(isinstance(packet["candidate_id"], str) and packet["candidate_id"], "candidate id")
    require(isinstance(packet["source_orbit_id"], str) and packet["source_orbit_id"], "source orbit id")
    require(isinstance(packet["source_hash"], str) and packet["source_hash"], "source hash")
    require(packet["evidence_grade"] in GRADES, "top-level evidence grade")
    require(isinstance(packet["complete_physical_pair"], bool), "complete physical pair flag")
    require(isinstance(packet["physical_promotion_requested"], bool), "promotion flag")
    require(isinstance(packet["empirical_inputs"], list), "empirical inputs")
    require(all(isinstance(item, str) for item in packet["empirical_inputs"]), "empirical input entries")

    base = packet["base_geometry"]
    require(set(base) == BASE_FIELDS, "base geometry fields")
    require(base["same_q79_principal_elliptic_fibration"] is True, "wrong base fibration")
    require(q(base["H_square"], "H_square") == 2, "q79 H^2")
    require(q(base["H_dot_delta"], "H_dot_delta") == 0, "q79 H.delta")
    require(q(base["delta_square"], "delta_square") == -4, "q79 delta^2")
    require(base["primitive_harmonic_curvature"] is True, "primitive harmonic curvature representative")
    require(
        isinstance(base["balanced_ray_certificate"], str)
        and bool(base["balanced_ray_certificate"]),
        "balanced-ray certificate",
    )

    require(isinstance(packet["factors"], list) and len(packet["factors"]) == 2, "two sector factors required")
    factor_ids = [factor.get("id") for factor in packet["factors"]]
    require(len(set(factor_ids)) == 2, "factor ids must be unique")
    factor_results = [validate_factor(factor, packet["source_hash"]) for factor in packet["factors"]]
    require({item["sector"] for item in factor_results} == {"visible", "hidden"}, "one visible and one hidden factor required")

    common_t = q(packet["common_t"], "common_t")
    require(common_t > 0, "common_t must be positive")
    accepted_thresholds = [
        item["threshold"] for item in factor_results if item["accepted"]
    ]
    threshold_strict = bool(accepted_thresholds) and all(
        threshold is not None and common_t > threshold
        for threshold in accepted_thresholds
    )

    promotion_conditions = {
        "top_level_pass": packet["evidence_grade"] == "PASS",
        "source_hash_is_sha256": bool(HEX64.fullmatch(packet["source_hash"])),
        "complete_physical_pair": packet["complete_physical_pair"] is True,
        "both_factors_accepted": all(item["accepted"] for item in factor_results),
        "strict_common_threshold": len(accepted_thresholds) == 2 and threshold_strict,
        "no_empirical_inputs": packet["empirical_inputs"] == [],
    }
    physically_selected = all(promotion_conditions.values())
    if packet["physical_promotion_requested"]:
        failed = [name for name, passed in promotion_conditions.items() if not passed]
        require(not failed, "physical promotion requested with failed conditions: " + ", ".join(failed))

    return {
        "factor_results": factor_results,
        "common_t": common_t,
        "maximum_threshold": max(accepted_thresholds) if accepted_thresholds else None,
        "threshold_strict": threshold_strict,
        "physically_selected": physically_selected,
        "promotion_conditions": promotion_conditions,
    }


def validate_result_packet() -> tuple[dict[str, Any], dict[str, Any]]:
    result = json.loads(RESULT_PACKET.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    require(schema["$id"] == SCHEMA_ID, "machine schema id")
    require(set(schema["required"]) == TOP_FIELDS, "machine top-level fields")
    require(set(schema["$defs"]["factor"]["required"]) == FACTOR_FIELDS, "machine factor fields")
    require(
        set(schema["$defs"]["factor"]["properties"]["spectral_mode"]["enum"]) == MODES,
        "machine spectral modes",
    )
    require(
        set(schema["$defs"]["factor"]["properties"]["mu1_bound_method"]["enum"])
        == BOUND_METHODS,
        "machine slope-bound methods",
    )
    require(result["schema"] == RESULT_SCHEMA_ID, "result schema")
    require(result["theorem_id"] == "UST.G3D", "result theorem id")
    require(
        result["state"] == "CLOSED_EXACT_UNIVERSAL_CRITERION_PHYSICAL_SPECTRAL_OBJECTS_OPEN",
        "result theorem state",
    )
    require(result["source"]["repository_id"] == QG_REPOSITORY_ID, "result repository id")
    require(result["source"]["commit"] == QG_COMMIT, "result source commit")
    require(result["source"]["base_repository_id"] == BASE_REPOSITORY_ID, "result base repository id")
    require(result["source"]["base_commit"] == BASE_COMMIT, "result base source commit")

    qg_lock = next(
        (repository for repository in lock["repositories"] if repository["id"] == QG_REPOSITORY_ID),
        None,
    )
    require(qg_lock is not None, "q79 quantum-gravity source lock missing")
    require(qg_lock["commit"] == QG_COMMIT, "q79 quantum-gravity lock commit")
    locked_sources = {source["path"]: source for source in qg_lock["sources"]}
    require(len(result["source"]["artifacts"]) == 5, "five q79 source artifacts required")
    for artifact in result["source"]["artifacts"]:
        require(set(artifact) == {"path", "sha256"}, "result source artifact fields")
        require(bool(HEX64.fullmatch(artifact["sha256"])), f"bad source sha256: {artifact['path']}")
        require(artifact["path"] in locked_sources, f"unlocked source artifact: {artifact['path']}")
        require(locked_sources[artifact["path"]]["sha256"] == artifact["sha256"], f"source hash mismatch: {artifact['path']}")

    base_lock = next(
        (repository for repository in lock["repositories"] if repository["id"] == BASE_REPOSITORY_ID),
        None,
    )
    require(base_lock is not None, "q79 base source lock missing")
    require(base_lock["commit"] == BASE_COMMIT, "q79 base lock commit")
    base_artifact = result["source"]["base_artifact"]
    require(set(base_artifact) == {"path", "sha256"}, "result base artifact fields")
    locked_base_sources = {source["path"]: source for source in base_lock["sources"]}
    require(base_artifact["path"] in locked_base_sources, "unlocked q79 base artifact")
    require(
        locked_base_sources[base_artifact["path"]]["sha256"] == base_artifact["sha256"],
        "q79 base artifact hash mismatch",
    )

    geometry = result["q79_geometry"]
    require(q(geometry["H_square"], "result H_square") == 2, "result q79 H^2")
    require(q(geometry["H_dot_delta"], "result H_dot_delta") == 0, "result q79 H.delta")
    require(q(geometry["delta_square"], "result delta_square") == -4, "result q79 delta^2")
    require(geometry["d_balanced_square"] == "0", "balanced square derivative")
    require(geometry["primitive_harmonic_curvature_representative"] is True, "primitive representative")
    require(geometry["all_positive_t_are_Gauduchon"] is True, "Gauduchon ray")

    support = result["q79_support_audit"]
    require(support["visible"]["physical_rank"] == 3, "visible physical rank")
    require(support["visible"]["selected_twisted_Prym_module"] is False, "visible module remains open")
    require(support["hidden_degree3_transform"]["cover_degree"] == 3, "hidden transformed degree")
    require(
        support["hidden_degree3_transform"]["is_physical_rank9_W9_certificate"] is False,
        "degree-three hidden transform must not promote as W9",
    )
    require(support["physical_hidden"]["physical_rank"] == 9, "hidden physical rank")
    require(support["physical_hidden"]["global_length9_spectral_module_selected"] is False, "hidden module remains open")

    decision = result["physical_decision"]
    require(decision["common_chamber_criterion_closed"] is True, "common chamber criterion")
    require(decision["physical_common_chamber_selected"] is False, "physical chamber remains open")
    require(decision["physical_HYM_connections_selected"] is False, "physical HYM remains open")
    require(decision["physical_source_promotion"] is False, "physical source remains unpromoted")
    require(decision["fiber_gap_is_independent_input"] is False, "q79 fiber gap is derived")
    require(decision["certified_mu1_bounds_selected"] is False, "physical slope bounds remain open")
    require(decision["continuous_fit_parameters"] == 0, "no fit parameters")
    require(decision["observed_inputs"] == 0, "no observed inputs")
    require("`UST.G3D` is an exact universal/conditional theorem" in THEOREM_PATH.read_text(encoding="utf-8"), "theorem boundary text")
    return qg_lock, base_lock


def optional_replay_sources(
    repository_lock: dict[str, Any],
    environment_variable: str,
    default_directory: str,
) -> str:
    configured = os.environ.get(environment_variable)
    candidate = Path(configured).expanduser() if configured else ROOT.parent / default_directory
    if not candidate.is_dir() or not (candidate / ".git").exists():
        return f"SKIP (set {environment_variable} for upstream byte replay)"

    commit = repository_lock["commit"]
    subprocess.run(
        ["git", "-C", str(candidate), "cat-file", "-e", f"{commit}^{{commit}}"],
        check=True,
        capture_output=True,
    )
    for source in repository_lock["sources"]:
        blob = subprocess.run(
            ["git", "-C", str(candidate), "rev-parse", f"{commit}:{source['path']}"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        require(blob == source["git_blob"], f"upstream blob mismatch: {source['path']}")
        content = subprocess.run(
            ["git", "-C", str(candidate), "show", f"{commit}:{source['path']}"],
            check=True,
            capture_output=True,
        ).stdout
        expected_byte_hash = source.get("git_blob_sha256", source["sha256"])
        require(hashlib.sha256(content).hexdigest() == expected_byte_hash, f"upstream byte hash mismatch: {source['path']}")
    return "PASS"


def run_reference_falsifiers(packet: dict[str, Any], result: dict[str, Any]) -> None:
    require(packet["candidate_id"] == "UST.G3D.REFERENCE.TWO_SECTOR_COMPILER", "reference candidate id")
    require(result["physically_selected"] is False, "reference packet must not physically promote")
    require(result["maximum_threshold"] == Fraction(5, 2), "reference exact threshold")

    threshold_equality = copy.deepcopy(packet)
    threshold_equality["common_t"] = "5/2"
    require(
        validate_packet(threshold_equality)["threshold_strict"] is False,
        "threshold equality must be rejected",
    )

    spliced = copy.deepcopy(packet)
    spliced["factors"][0]["provenance"]["source_hash"] = "REFERENCE.OTHER.SOURCE"
    require(
        validate_packet(spliced)["promotion_conditions"]["both_factors_accepted"] is False,
        "mixed-source factor must be rejected",
    )

    missing_object = copy.deepcopy(packet)
    missing_object["factors"][0]["spectral_object_selected"] = False
    require(
        validate_packet(missing_object)["promotion_conditions"]["both_factors_accepted"] is False,
        "missing spectral object must be rejected",
    )

    wrong_topology = copy.deepcopy(packet)
    wrong_topology["factors"][1]["physical_topology_match"] = False
    require(
        validate_packet(wrong_topology)["promotion_conditions"]["both_factors_accepted"] is False,
        "wrong-Chern orbit sum must be rejected",
    )

    degree_three_substitute = copy.deepcopy(packet)
    degree_three_substitute["factors"][1]["spectral_mode"] = "irreducible_spectral_cover"
    degree_three_substitute["factors"][1]["orbit_factor_count"] = 1
    degree_three_substitute["factors"][1]["factor_rank"] = 3
    try:
        validate_packet(degree_three_substitute)
    except AssertionError as error:
        require("physical rank" in str(error), "unexpected rank-substitution failure")
    else:
        raise AssertionError("degree-three hidden transform must not compile as physical W9")

    false_promotion = copy.deepcopy(packet)
    false_promotion["physical_promotion_requested"] = True
    try:
        validate_packet(false_promotion)
    except AssertionError as error:
        require("physical promotion requested" in str(error), "unexpected false-promotion failure")
    else:
        raise AssertionError("reference packet must not promote")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, default=DEFAULT_PACKET)
    args = parser.parse_args()

    packet = json.loads(args.candidate.read_text(encoding="utf-8"))
    result = validate_packet(packet)
    qg_lock, base_lock = validate_result_packet()
    qg_replay = optional_replay_sources(qg_lock, "MTT_QG_ROOT", "12 Quantum Gravity")
    base_replay = optional_replay_sources(
        base_lock,
        "MTT_PROTO_GR_ROOT",
        "mtt-protospinor-gr-response-proof",
    )
    if args.candidate.resolve() == DEFAULT_PACKET.resolve():
        run_reference_falsifiers(packet, result)

    maximum_threshold = result["maximum_threshold"]
    threshold_text = str(maximum_threshold) if maximum_threshold is not None else "not compiled"
    print("UST.G3D common Gauduchon-HYM chamber certificate: PASS")
    print(f"candidate: {packet['candidate_id']}")
    print(f"maximum exact threshold: {threshold_text}")
    print(f"strict common chamber: {str(result['threshold_strict']).lower()}")
    print(f"physical common chamber selected: {str(result['physically_selected']).lower()}")
    print(f"q79 quantum-gravity byte replay: {qg_replay}")
    print(f"q79 base byte replay: {base_replay}")


if __name__ == "__main__":
    main()
