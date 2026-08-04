#!/usr/bin/env python3
"""Verify the hash-bound UST.G2P/G5A upstream integration and exact cutsets."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
from fractions import Fraction
from pathlib import Path

from verify_ust_g1_candidate_adjudication import matrix, multiply, transpose


ROOT = Path(__file__).resolve().parent
PACKET = ROOT / "state" / "ust_g2p_g5a_physical_residual_transfer.packet.json"
LOCK = ROOT / "state" / "upstream-lock.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def subtract(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    require(len(a) == len(b) and len(a[0]) == len(b[0]), "subtraction shape")
    return [[left - right for left, right in zip(arow, brow)] for arow, brow in zip(a, b)]


def main() -> None:
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    lock = json.loads(LOCK.read_text(encoding="utf-8"))

    require(packet["schema"] == "mtt.unified-source.physical-residual-transfer-ingestion.v1", "schema")
    require(packet["theorem_ids"] == ["UST.G2P", "UST.G5A"], "theorem ids")
    require("PHYSICAL_ENDPOINT_OPEN" in packet["state"], "tier boundary")

    source = packet["source"]
    closure = next(item for item in lock["repositories"] if item["id"] == "closure-dynamics")
    require(source["repository_id"] == closure["id"], "source repository")
    require(source["commit"] == closure["commit"], "source commit")
    locked_sources = {item["path"]: item.get("sha256") for item in closure["sources"]}
    locked_blob_hashes = {item["path"]: item.get("git_blob_sha256") for item in closure["sources"]}
    locked_blobs = {item["path"]: item.get("git_blob") for item in closure["sources"]}
    for artifact in source["artifacts"]:
        require(locked_sources.get(artifact["path"]) == artifact["sha256"], f"source hash: {artifact['path']}")
        require(
            locked_blob_hashes.get(artifact["path"]) == artifact["git_blob_sha256"],
            f"canonical blob-byte hash: {artifact['path']}",
        )

    closure_root = Path(
        os.environ.get(
            "MTT_CLOSURE_ROOT",
            ROOT.parent / "20 Mathematical Language Discovery Program - Closure Dynamics",
        )
    )
    local_source_audit = (closure_root / ".git").exists()
    if local_source_audit:
        for artifact in source["artifacts"]:
            revision = f"{source['commit']}:{artifact['path']}"
            content = subprocess.run(
                ["git", "show", revision],
                cwd=closure_root,
                check=True,
                capture_output=True,
            ).stdout
            blob = subprocess.run(
                ["git", "rev-parse", revision],
                cwd=closure_root,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
            require(
                hashlib.sha256(content).hexdigest() == artifact["git_blob_sha256"],
                f"local canonical blob-byte sha256: {artifact['path']}",
            )
            require(
                hashlib.sha256(content.replace(b"\n", b"\r\n")).hexdigest() == artifact["sha256"],
                f"local Windows artifact sha256: {artifact['path']}",
            )
            require(blob == locked_blobs[artifact["path"]], f"local source Git blob: {artifact['path']}")

    residual = packet["physical_residual"]
    require(
        residual["extra_rows"]
        == ["mu_TX", "mu_V", "mu_W", "balanced", "anomaly_Bianchi", "SU3_normalization"],
        "six complete physical rows",
    )
    require(residual["anomaly_derivative_curvature_square_coefficient"] == "alpha_prime/2", "anomaly derivative factor")
    require(residual["Hessian"] == "H_phys=Delta_Y,1+K^dagger*K", "full Hessian")
    require(not residual["physical_endpoint_selected"], "physical endpoint remains open")
    require(not residual["physical_K_coefficients_selected"], "physical K values remain open")

    metric = packet["repair_metric_binding"]
    require(metric["state"] == "BOUND_STRUCTURAL_REPAIR_METRIC", "repair metric tier")
    require(metric["relative_lane_weights"] == ["1"] * 7, "minimal equal lane weights")
    require(metric["cross_block_C"] == "0", "orthogonal repair target")
    require(metric["continuous_fit_parameters"] == metric["discrete_fit_parameters"] == 0, "zero fitted parameters")
    require(metric["observed_inputs"] == 0, "zero observed inputs")
    require(metric["declared_structural_metric_bindings"] == 1, "one declared metric binding")
    require(not metric["source_commutant_uniqueness_proved"], "source metric uniqueness remains open")
    require(not metric["Lorentzian_BV_or_ten_dimensional_action_identification"], "action identification remains open")
    require(not metric["UST_G3C_physical_metric_promotion"], "G3C physical metric remains open")

    rank = packet["rank102"]
    lane_ranks = dict(zip(rank["lane_order"], rank["lane_ranks"]))
    require(sum(rank["lane_ranks"]) == 102, "lane ranks sum to 102")
    require(rank["corrected_allowed_ordered_blocks"] == len(rank["lane_order"]) ** 2 == 25, "dense five-lane mask")
    require(rank["corrected_structural_positions"] == 102**2 == 10404, "all rank-102 positions")
    newly_reconsidered = sum(
        2 * lane_ranks[left] * lane_ranks[right]
        for left, right in rank["newly_allowed_pairs"]
    )
    require(newly_reconsidered == rank["newly_reconsidered_positions"] == 2688, "six ordered cross-gauge blocks")
    require(
        rank["corrected_structural_positions"] - newly_reconsidered
        == rank["base_structural_positions"]
        == 7716,
        "base 19-block position count",
    )
    require(not rank["mask_is_nonvanishing_claim"], "support is not nonvanishing")
    require(not rank["finite_27_carrier_replaced"], "rank-102 correction does not retype finite 27")

    transfer = packet["finite_transfer"]
    require(len(transfer["exact_conditions"]) == 4, "complete exact transfer conditions")
    witness = transfer["nonreducing_counterexample"]
    k_c = matrix(witness["K_c"])
    k_f = matrix(witness["K_f"])
    s_r = matrix(witness["S_R"])
    t_fin = matrix(witness["T_fin"])
    require(multiply(s_r, k_c) == multiply(k_f, t_fin), "forward K intertwining")

    k_c_gram = multiply(transpose(k_c), k_c)
    k_f_gram = multiply(transpose(k_f), k_f)
    gram_defect = subtract(multiply(k_f_gram, t_fin), multiply(t_fin, k_c_gram))
    require(gram_defect == matrix([["0"], ["1/2"]]), "nonreducing K-Gram defect")

    identity = matrix([["1", "0"], ["0", "1"]])
    range_projector = multiply(t_fin, transpose(t_fin))
    leakage_projector = subtract(identity, range_projector)
    leakage = multiply(multiply(leakage_projector, transpose(k_f)), s_r)
    require(leakage == matrix([["0"], ["1/2"]]), "adjoint leakage witness")
    require(witness["epsilon_K"] == "0" and witness["epsilon_perp"] == "1/2", "reported leakage values")
    require(not transfer["physical_T_fin_selected"], "physical finite map remains open")

    audit = packet["candidate_audit"]
    require(audit["current_candidate_classes"] == 4, "four current candidate classes")
    require(audit["promotable_candidates"] == 0, "zero promotable candidates")
    require(not audit["physical_promotion"], "no physical promotion")

    print("UST.G2P/G5A upstream integration: PASS")
    print("complete physical residual rows: 6; symbolic K: closed")
    print("rank-102 allowable mask: 25 blocks, 10404 positions")
    print("same-source full-Hessian transfer criterion: closed")
    print("physical endpoint, K values, action metric and T_fin: open")
    print(f"local locked-source replay: {str(local_source_audit).lower()}")


if __name__ == "__main__":
    main()
