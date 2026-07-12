from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_productprecisionworkspaceacceptance_or_internaltransportpromotion"
STATUS = "MTT_SELECTED_PRODUCTPRECISIONWORKSPACE_INTERNAL_COMMON_SOURCE_FIRSTPASS_PROMOTED_MULTILOOP_OPEN"
NEXT = "MTT_Selected_MultiLoopCommonSourcePrecisionTransport_or_OfficialJointLikelihood_v1"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")],
        cwd=ROOT,
        check=True,
    )
    candidate = load(f"candidate_data/{SLUG}.candidate.json")
    packet = load(f"candidate_data/{SLUG}/common_source_precision_transport_workspace.packet.json")
    cert = load(f"certificates/{SLUG}_certificate.json")
    firstpass = load(
        "candidate_data/selected_mztomtjacobianexecution_or_selectedthresholdresponsefunctionalfill/"
        "firstpass_weak_bct_crossblock_covariance.packet.json"
    )

    require(candidate["status"] == STATUS and cert["status"] == STATUS, "status changed")
    require(candidate["closure_claimed"] is False and cert["closure_claimed"] is False, "final closure overclaimed")
    require(candidate["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem missing")
    require(candidate["target_fitting_used"] is False, "target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector used")
    require(packet["predecessor_product_zero_rule_rejected"] is True, "invalid independence rule retained")

    rows = packet["cross_covariance_rows"]
    require(len(rows) == 15, "cross row count")
    require(sum(row["covariance"] != 0.0 for row in rows) == 6, "nonzero cross count")
    require(sum(row["covariance"] == 0.0 for row in rows) == 9, "structural-zero cross count")
    require(packet["diagnostics"]["missing_cross_entries"] == 0, "cross entries missing")

    expected = {
        (entry["right"], entry["left"]): entry["covariance"]
        for entry in firstpass["inserted_cross_block_entries"]
        if entry["right"] in packet["basis_order"] and entry["left"] in packet["basis_order"]
    }
    actual = {
        (row["BCT_row"], row["WZH_row"]): row["covariance"]
        for row in rows
        if row["covariance"] != 0.0
    }
    require(actual == expected, "executed common-source cross entries changed")

    matrix = packet["covariance_matrix"]
    require(len(matrix) == 8 and all(len(row) == 8 for row in matrix), "matrix shape")
    require(
        all(abs(matrix[i][j] - matrix[j][i]) <= 1e-20 for i in range(8) for j in range(8)),
        "matrix asymmetric",
    )
    require(packet["diagnostics"]["positive_definite"] is True, "matrix not positive definite")
    require(min(packet["diagnostics"]["cholesky_pivots"]) > 0.0, "nonpositive Cholesky pivot")
    require(packet["diagnostics"]["accepted_as_internal_common_source_firstpass_workspace"] is True, "workspace not accepted")
    require(packet["diagnostics"]["accepted_as_multiloop_precision_workspace"] is False, "multiloop overclaim")
    require(packet["diagnostics"]["accepted_as_published_or_reconstructed_joint_likelihood"] is False, "likelihood overclaim")
    require(packet["diagnostics"]["accepted_as_final_true_precision_equivalence"] is False, "precision overclaim")

    require(cert["BCT_WZH_cross_entries_determined"] == 15, "certificate cross count")
    require(cert["executed_nonzero_cross_entries"] == 6, "certificate nonzero count")
    require(cert["structural_one_loop_zero_cross_entries"] == 9, "certificate zero count")
    require(cert["BCT_WZH_cross_entries_missing"] == 0, "certificate missing count")
    require(cert["accepted_true_equivalence_precision_rows"] == 0, "true precision overclaimed")
    require(cert["next_required_artifact"] == NEXT, "next artifact changed")

    print(json.dumps({
        "status": STATUS,
        "BCT_WZH_cross_entries_determined": 15,
        "executed_nonzero_cross_entries": 6,
        "structural_one_loop_zero_cross_entries": 9,
        "missing_cross_entries": 0,
        "internal_common_source_firstpass_workspace_accepted": True,
        "accepted_true_equivalence_precision_rows": 0,
        "next_required_artifact": NEXT,
    }, indent=2))
    print("selected common-source precision workspace promotion audit passed")


if __name__ == "__main__":
    main()
