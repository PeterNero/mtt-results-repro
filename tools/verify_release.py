"""Verify release integrity and independently recompute key numerical claims."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / "release"
CURRENT_RESULT_CONFIG = ROOT / "config" / "current_results.json"


def io_path(path: Path) -> str:
    resolved = str(path.resolve())
    if os.name == "nt" and not resolved.startswith("\\\\?\\"):
        return "\\\\?\\" + resolved
    return resolved


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with open(io_path(path), "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def close(left: float, right: float, tolerance: float = 1e-12) -> bool:
    return abs(left - right) <= tolerance * max(1.0, abs(left), abs(right))


def determinant(matrix: list[list[float]]) -> float:
    work = [[float(value) for value in row] for row in matrix]
    result = 1.0
    for column in range(len(work)):
        pivot = max(range(column, len(work)), key=lambda row: abs(work[row][column]))
        if abs(work[pivot][column]) < 1e-15:
            return 0.0
        if pivot != column:
            work[pivot], work[column] = work[column], work[pivot]
            result *= -1.0
        value = work[column][column]
        result *= value
        for row in range(column + 1, len(work)):
            factor = work[row][column] / value
            for index in range(column + 1, len(work)):
                work[row][index] -= factor * work[column][index]
    return result


def cholesky_pivots(matrix: list[list[float]]) -> list[float]:
    size = len(matrix)
    lower = [[0.0] * size for _ in range(size)]
    pivots = []
    for row in range(size):
        for column in range(row + 1):
            remainder = matrix[row][column] - sum(lower[row][k] * lower[column][k] for k in range(column))
            if row == column:
                if remainder <= 0.0:
                    raise ValueError(f"non-positive Cholesky pivot at {row}: {remainder}")
                pivots.append(remainder)
                lower[row][column] = math.sqrt(remainder)
            else:
                lower[row][column] = remainder / lower[column][column]
    return pivots


def complex_matrix(value: list[list[list[float]]]) -> list[list[complex]]:
    return [[complex(cell[0], cell[1]) for cell in row] for row in value]


def sparse_matrix(entries: list[dict[str, Any]], size: int) -> list[list[complex]]:
    output = [[0j] * size for _ in range(size)]
    for entry in entries:
        output[entry["row"]][entry["col"]] = complex(*entry["value"])
    return output


def matmul(left: list[list[complex]], right: list[list[complex]]) -> list[list[complex]]:
    size = len(left)
    return [
        [sum(left[row][k] * right[k][column] for k in range(size)) for column in range(size)]
        for row in range(size)
    ]


def adjoint(matrix: list[list[complex]]) -> list[list[complex]]:
    return [[matrix[column][row].conjugate() for column in range(len(matrix))] for row in range(len(matrix))]


def frobenius_difference(left: list[list[complex]], right: list[list[complex]]) -> float:
    return math.sqrt(sum(abs(a - b) ** 2 for row_a, row_b in zip(left, right) for a, b in zip(row_a, row_b)))


def scale_matrix(value: complex, matrix: list[list[complex]]) -> list[list[complex]]:
    return [[value * cell for cell in row] for row in matrix]


def identity(size: int) -> list[list[complex]]:
    return [[1.0 + 0j if row == column else 0j for column in range(size)] for row in range(size)]


def all_true(mapping: dict[str, Any], keys: list[str]) -> bool:
    return all(mapping.get(key) is True for key in keys)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--full-archive", action="store_true", help="hash every archived artifact")
    parser.add_argument("--report", type=Path, default=ROOT / "verification_report.json")
    args = parser.parse_args()

    checks: list[dict[str, Any]] = []

    def record(name: str, passed: bool, **details: Any) -> None:
        checks.append({"name": name, "passed": bool(passed), "details": details})

    inventory_summary = load(ROOT / "inventory" / "summary.json")
    archive_manifest = load(ROOT / "archive" / "manifest.json")
    hash_only_rows = load_jsonl(ROOT / "archive" / "hash_only_artifacts.jsonl")
    authority = load(RELEASE / "authority_manifest.json")
    results = load(RELEASE / "result_manifest.json")
    parameters = load(RELEASE / "parameter_ledger.json")
    current_snapshot = load(RELEASE / "current_snapshot.json")
    paper_lock = load(RELEASE / "paper_corpus_lock.json")
    current_selection = load(CURRENT_RESULT_CONFIG)

    record(
        "inventory_completeness",
        inventory_summary["completeness_policy"]["all_authority_entries_indexed"]
        and inventory_summary["completeness_policy"]["all_configured_repositories_found"],
        artifacts=inventory_summary["artifact_count"],
        numerical_objects=inventory_summary["numerical_object_count"],
    )
    record(
        "archive_manifest_count",
        archive_manifest["inventory_artifact_count"] == inventory_summary["artifact_count"]
        and archive_manifest["artifact_count"] + archive_manifest["hash_only_artifact_count"] == inventory_summary["artifact_count"]
        and archive_manifest["hash_only_artifact_count"] == len(hash_only_rows),
        archived=archive_manifest["artifact_count"],
        hash_only=archive_manifest["hash_only_artifact_count"],
    )
    record(
        "authority_chain_A01_A99",
        authority["schema"] == "MTTCurrentAuthorityRelease.v2"
        and authority["authority_entry_count"] == 99
        and authority["baseline_authority_entry_count"] == 62
        and authority["current_authority_extension_count"] == 37
        and [row["authority_id"] for row in authority["entries"]] == [f"A{i:02d}" for i in range(1, 100)],
        bundle_artifacts=authority["bundle_artifact_count"],
    )

    authority_hash_failures = []
    for entry in authority["entries"]:
        for artifact in entry["bundle_artifacts"]:
            path = ROOT / artifact["release_path"]
            if not path.is_file() or sha256(path) != artifact["sha256"]:
                authority_hash_failures.append(artifact["release_path"])
    record("authority_bundle_hashes", not authority_hash_failures, failures=authority_hash_failures)

    result_hash_failures = []
    result_paths = {}
    for result in results["results"]:
        path = ROOT / result["release_path"]
        result_paths[result["id"]] = path
        if not path.is_file() or sha256(path) != result["sha256"]:
            result_hash_failures.append(result["id"])
    record("key_result_hashes", not result_hash_failures, result_count=results["result_count"], failures=result_hash_failures)
    current_result_ids = current_snapshot["current_layer"]["result_ids"]
    selected_result_ids = [row["id"] for row in current_selection["results"]]
    record(
        "current_promoted_layer",
        results["schema"] == "MTTKeyResultManifest.v2"
        and current_snapshot["snapshot_date"] == current_selection["snapshot_date"]
        and results["baseline_result_count"] == 28
        and results["current_promoted_result_count"] == len(selected_result_ids)
        and current_snapshot["current_layer"]["authority_extension"] == "A63-A99"
        and current_snapshot["current_layer"]["authority_extension_count"] == 37
        and current_result_ids == selected_result_ids
        and set(current_result_ids).issubset(result_paths),
        baseline_results=results.get("baseline_result_count"),
        current_results=results.get("current_promoted_result_count"),
    )
    hypothesis = current_snapshot["current_layer"]["unified_source_hypothesis"]
    record(
        "unified_source_nonpromotion_guard",
        hypothesis["state"] == "HYPOTHESIS"
        and hypothesis["physical_promotion"] is False
        and "zero-input" in hypothesis["continuous_parameter_claim"],
        hypothesis=hypothesis["id"],
    )
    record(
        "paper_corpus_lock",
        paper_lock["commit"] == "caf55313b90ababc43f83650cc72a325129e1252"
        and paper_lock["canonical_papers"] == 139
        and paper_lock["latest_zenodo_records"] == 138
        and paper_lock["latest_zenodo_pdf_exact_matches"] == 138
        and paper_lock["zenodo_latest_id_differences"] == 0
        and paper_lock["commercial_book_artifacts"] == 0
        and paper_lock["commercial_book_zenodo_records"] == 0,
        paper_commit=paper_lock["commit"],
        papers=paper_lock["canonical_papers"],
        zenodo_latest=paper_lock["latest_zenodo_records"],
    )
    forbidden_tokens = {
        "bad-memory-book",
        "badmemorybook",
        "humanvoicepass",
        "the-universe-has-a-bad-memory",
        "the-universe-had-a-bad-memory",
    }
    forbidden_paths = [
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and any(token in path.as_posix().casefold() for token in forbidden_tokens)
    ]
    record(
        "commercial_book_excluded",
        not forbidden_paths,
        failures=forbidden_paths,
    )
    provenance_files = [
        ROOT / "inventory" / "source_repositories.json",
        ROOT / "archive" / "manifest.json",
        RELEASE / "current_snapshot.json",
    ]
    forbidden_provenance = [
        path.relative_to(ROOT).as_posix()
        for path in provenance_files
        if any(token in path.read_text(encoding="utf-8").casefold() for token in forbidden_tokens)
    ]
    record(
        "commercial_book_absent_from_provenance",
        not forbidden_provenance,
        failures=forbidden_provenance,
    )

    final_audit = load(result_paths["final_12_of_12_audit"])
    record(
        "declared_scope_12_of_12",
        final_audit["obligation_count"] == 12
        and final_audit["closed_obligation_count"] == 12
        and all(row["closed"] for row in final_audit["obligations"])
        and final_audit["decision"]["full_no_knob_closed"] is False,
        scope=final_audit["closure_scope"]["name"],
    )

    crt_solutions = [q for q in range(448) if q % 64 == 15 and q % 7 == 2]
    record("q79_crt", crt_solutions == [79], solutions=crt_solutions)

    qutrit = load(result_paths["qutrit_weyl_27_matrix"])
    X = sparse_matrix(qutrit["left_X27_sparse_entries"], 27)
    Z = sparse_matrix(qutrit["left_Z27_sparse_entries"], 27)
    omega = complex(*qutrit["omega"])
    relation_error = frobenius_difference(matmul(Z, X), scale_matrix(omega, matmul(X, Z)))
    x_unitarity = frobenius_difference(matmul(X, adjoint(X)), identity(27))
    z_unitarity = frobenius_difference(matmul(Z, adjoint(Z)), identity(27))
    record(
        "qutrit_27_weyl_matrices",
        relation_error < 1e-12 and x_unitarity < 1e-12 and z_unitarity < 1e-12,
        relation_error=relation_error,
        x_unitarity=x_unitarity,
        z_unitarity=z_unitarity,
    )

    yukawa = load(result_paths["charged_yukawa_higgs_profile"])
    for sector in ("d", "e", "u"):
        matrix = complex_matrix(yukawa["values"][f"Y_{sector}_MZ_firstpass"])
        diagonal = [abs(matrix[index][index]) for index in range(3)]
        frobenius = math.sqrt(sum(abs(cell) ** 2 for row in matrix for cell in row))
        off_diagonal = math.sqrt(sum(abs(matrix[row][column]) ** 2 for row in range(3) for column in range(3) if row != column))
        expected = yukawa["derived_magnitudes"]
        passed = all(close(a, b, 1e-11) for a, b in zip(diagonal, expected[f"diag_abs_Y_{sector}"]))
        passed = passed and close(frobenius, expected[f"frob_Y_{sector}"], 1e-11)
        passed = passed and close(off_diagonal, expected[f"offdiag_frob_Y_{sector}"], 1e-11)
        record(f"yukawa_{sector}_matrix_norms", passed, diagonal=diagonal, frobenius=frobenius, off_diagonal=off_diagonal)

    precision = load(result_paths["precision_8x8_workspace"])
    covariance = precision["covariance_matrix"]
    symmetric = all(close(covariance[i][j], covariance[j][i], 1e-13) for i in range(8) for j in range(8))
    pivots = cholesky_pivots(covariance)
    record(
        "precision_8x8_covariance",
        symmetric and len(covariance) == 8 and len(pivots) == 8 and min(pivots) > 0 and len(precision["BCT_WZH_cross_rows"]) == 15,
        minimum_pivot=min(pivots),
        cross_rows=len(precision["BCT_WZH_cross_rows"]),
    )

    ckm = load(result_paths["ckm_prediction_profile"])
    record(
        "ckm_profile_rows",
        ckm["selected_prediction"]["selected_Pi_CKM_weight_rows"] == 3
        and ckm["profile_postcheck"]["maximum_absolute_z_score"] < 1.0
        and ckm["requirement_decision"]["exact_equality_to_measured_central_estimator_is_theory_obligation"] is False,
        maximum_absolute_z_score=ckm["profile_postcheck"]["maximum_absolute_z_score"],
    )

    pew = load(result_paths["strict_pew_row"])
    direct_k = load(result_paths["direct_k_higgs_row"])
    record(
        "pew_direct_k_rows",
        pew["accepted_global_strict_P_EW_source_rows"] == 1
        and direct_k["strict_direct_K_threshold_Omega_H_lambda_rows"] == 1
        and direct_k["strict_zero_primitive_K_threshold_row_count"] == 10
        and close(pew["P_EW_value"], direct_k["P_EW_value"]),
        P_EW=pew["P_EW_value"],
    )

    cech = load(result_paths["literal_cech_witness"])
    cocycle_count = 0
    cocycles_pass = True
    group = [(a, b) for a in range(3) for b in range(3)]
    B = lambda x, y: (-y[0] * x[1]) % 3
    add = lambda x, y: ((x[0] + y[0]) % 3, (x[1] + y[1]) % 3)
    for x in group:
        for y in group:
            for z in group:
                cocycle_count += 1
                cocycles_pass &= (B(x, y) + B(add(x, y), z) - B(y, z) - B(x, add(y, z))) % 3 == 0
    record("literal_cech_81_729", len(cech["entries"]) == 81 and cocycle_count == 729 and cocycles_pass, entries=len(cech["entries"]), triples=cocycle_count)

    hym = load(result_paths["hym_wiener_contraction"])
    contraction = hym["contraction"]
    record(
        "hym_wiener_contraction",
        contraction["Z_at_radius"] < 1.0
        and contraction["Y_plus_Zr"] < contraction["radius"]
        and contraction["passes"] is True,
        Z=contraction["Z_at_radius"],
        Y_plus_Zr=contraction["Y_plus_Zr"],
        radius=contraction["radius"],
    )

    representation = load(result_paths["typed_family_representation"])
    record(
        "typed_representation_anomalies",
        all_true(representation["checks"], ["all_local_anomalies_cancel", "Witten_SU2_doublet_count_even", "three_family_chiral_dimension_48"]),
    )
    gauge_group = load(result_paths["native_gauge_group"])
    record(
        "native_gauge_group_z6",
        all_true(gauge_group["checks"], ["global_kernel_has_order_6", "global_kernel_is_diagonal_Z6", "native_lie_dimension_is_12"]),
    )

    finite_df = load(result_paths["physical_df_96"])
    det_one = determinant(finite_df["minimal_completion"]["intersection_form_one_family"])
    det_three = determinant(finite_df["minimal_completion"]["intersection_form_three_families"])
    record(
        "physical_df_96_and_intersection",
        finite_df["physical_DF"]["dimension"] == 96
        and all(abs(value) < 1e-14 for value in finite_df["residuals"].values())
        and close(det_one, 4.0)
        and close(det_three, 324.0),
        determinant_one_family=det_one,
        determinant_three_families=det_three,
    )

    neutral_summand = load(result_paths["neutral_summand_hypercharge"])
    record(
        "neutral_summand_shared_hypercharge",
        all_true(neutral_summand["checks"], ["primitive_phase_vector_is_3_minus1_3", "all_selected_local_anomalies_zero", "no_second_anomaly_free_continuous_U1"]),
    )
    fluctuation = load(result_paths["finite_inner_fluctuation"])
    record(
        "finite_inner_fluctuation_one_higgs",
        all_true(fluctuation["checks"], ["unrestricted_finite_scalar_space_rank_12", "selected_single_Higgs_module_rank_4", "eight_extra_scalar_directions_removed", "single_Higgs_projector_idempotent"]),
    )

    su2 = load(result_paths["su2_finite_gauge_spectrum"])
    su3 = load(result_paths["su3_finite_gauge_spectrum"])
    gap = 4.0 * math.pi**2 / 9.0
    common_logdet = 4.0 * math.log(gap) + 4.0 * math.log(2.0 * gap)
    su2_row = su2["SU2_gauge_ghost_row"]
    su3_row = su3["SU3_gauge_ghost_row"]
    spectra_pass = (
        close(su2_row["positive_spectrum"][0]["eigenvalue"], gap)
        and su2_row["positive_spectrum"][0]["multiplicity"] == 12
        and close(su2_row["log_pseudodeterminant_per_adjoint_lane"], common_logdet)
        and close(su3_row["positive_spectrum"][0]["eigenvalue"], gap)
        and su3_row["positive_spectrum"][0]["multiplicity"] == 32
        and close(su3_row["log_pseudodeterminant_per_adjoint_lane"], common_logdet)
        and su3["ten_row_ledger"]["rows_closed"] == 10
        and su3["epistemic_policy"]["no_knob_gauge_coupling_prediction_closed"] is False
    )
    record("su2_su3_ten_spectrum_contract", spectra_pass, gap=gap, common_logdet=common_logdet)

    anomaly = load(result_paths["e6_qpsi_qcd_anomaly"])
    trace = anomaly["colored_anomaly_trace"]
    record(
        "e6_qpsi_anomaly",
        trace["matter_anomaly_total"] == 12
        and trace["exotic_anomaly_total_for_three_27s"] == -12
        and trace["complete_three_27_anomaly"] == 0
        and anomaly["U6_strong_CP_closed"] is False,
    )
    gr = load(result_paths["gr_tt_support"])
    record(
        "gr_tt_internal_support",
        all(gr["chain_checks"].values())
        and gr["conclusion"]["lambda_GR_TT_internal_exact_branch"] == 15
        and gr["guardrails"]["claims_full_physical_GR_closed"] is False,
    )

    neutral = load(result_paths["neutral_two_primitive_profile"])
    boundary = neutral["closure_boundary"]
    record(
        "neutral_profile_scope",
        boundary["two_primitive_profile_numerical_closure"] is True
        and boundary["strict_MTT_source_for_A_nu_or_mu_nu"] is False
        and boundary["Dirac_ontology_selected_by_MTT"] is False,
    )
    guards = parameters["interpretation_guards"]
    record(
        "parameter_scope_guards",
        parameters["schema"] == "MTTCurrentParameterLedger.v2"
        and parameters["construction_side_continuous_primitives"]["count"] == 1
        and parameters["measured_sm_profile_coordinates"]["count"] == 15
        and parameters["neutral_extension_profile_coordinates"]["count"] == 2
        and parameters["current_effective_model_coordinate_accounting"]["non_neutrino_count_excluding_qcd_theta"] == 13
        and parameters["current_effective_model_coordinate_accounting"]["count_with_minimal_pmns_policy"] == 19
        and all(value is False for value in guards.values()),
    )

    archive_hash_failures = []
    if args.full_archive:
        hash_only_index = {
            (row["repo_id"], row["path"]): row for row in hash_only_rows
        }
        with (ROOT / "inventory" / "artifacts.jsonl").open("r", encoding="utf-8") as handle:
            for line in handle:
                artifact = json.loads(line)
                path = ROOT / "archive" / "sources" / artifact["repo_id"] / artifact["path"]
                key = (artifact["repo_id"], artifact["path"])
                hash_only = hash_only_index.get(key)
                if hash_only is not None:
                    valid = (
                        hash_only["sha256"] == artifact["sha256"]
                        and hash_only["size_bytes"] == artifact["size_bytes"]
                        and not os.path.isfile(io_path(path))
                    )
                else:
                    valid = os.path.isfile(io_path(path)) and sha256(path) == artifact["sha256"]
                if not valid:
                    archive_hash_failures.append(f"{artifact['repo_id']}:{artifact['path']}")
        record("full_archive_hashes", not archive_hash_failures, failures=archive_hash_failures)

    failed = [check for check in checks if not check["passed"]]
    report = {
        "schema": "MTTResultsReproductionVerification.v2",
        "passed": not failed,
        "check_count": len(checks),
        "failed_check_count": len(failed),
        "full_archive_hash_mode": args.full_archive,
        "checks": checks,
        "scope_guard": "Passing verifies the published calculations and declared scopes; it does not upgrade profile replay to no-knob prediction.",
    }
    with args.report.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "passed": report["passed"],
        "checks": report["check_count"],
        "failed": [check["name"] for check in failed],
        "report": str(args.report),
    }, indent=2, sort_keys=True))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
