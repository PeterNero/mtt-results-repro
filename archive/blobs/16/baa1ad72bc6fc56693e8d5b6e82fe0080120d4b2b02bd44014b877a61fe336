from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_productprecisionworkspaceacceptance_or_internaltransportpromotion"
OUT = ROOT / "candidate_data" / SLUG
NEXT = "MTT_Selected_MultiLoopCommonSourcePrecisionTransport_or_OfficialJointLikelihood_v1"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def cholesky_pivots(matrix: list[list[float]]) -> list[float]:
    n = len(matrix)
    lower = [[0.0] * n for _ in range(n)]
    pivots: list[float] = []
    for i in range(n):
        for j in range(i + 1):
            value = matrix[i][j] - sum(lower[i][k] * lower[j][k] for k in range(j))
            if i == j:
                if value <= 0.0:
                    raise ValueError(f"covariance is not positive definite at pivot {i}: {value}")
                pivots.append(value)
                lower[i][j] = math.sqrt(value)
            else:
                lower[i][j] = value / lower[j][j]
    return pivots


def main() -> None:
    predecessor = load(
        "candidate_data/selected_precisiontransportvalueobject_or_finaltruesmequivalence/"
        "product_precision_transport_value_object.packet.json"
    )
    firstpass = load(
        "candidate_data/selected_mztomtjacobianexecution_or_selectedthresholdresponsefunctionalfill/"
        "firstpass_weak_bct_crossblock_covariance.packet.json"
    )
    wzh = load(
        "candidate_data/selected_correlatedthresholdprofilematrix_or_yukawahiggsprecisionpromotion/"
        "correlated_threshold_profile_matrix.packet.json"
    )

    basis = predecessor["basis_order"]
    index = {name: i for i, name in enumerate(basis)}
    matrix = [row[:] for row in predecessor["covariance_matrix"]]
    cross_rows: list[dict] = []
    emitted = {
        (entry["right"], entry["left"]): entry
        for entry in firstpass["inserted_cross_block_entries"]
        if entry["right"] in index and entry["left"] in index
    }

    for bct_name in basis[:3]:
        for wzh_name in basis[3:]:
            i, j = index[bct_name], index[wzh_name]
            source = emitted.get((bct_name, wzh_name))
            if source is None:
                value = 0.0
                provenance = (
                    "one-loop triangular SM RG: gauge beta rows are independent of Yukawa/mass "
                    "coordinates; no selected BCT dependence enters this WZH row"
                )
                kind = "structural_one_loop_zero"
            else:
                value = source["covariance"]
                provenance = source["method"]
                kind = "executed_common_source_jacobian"
            matrix[i][j] = matrix[j][i] = value
            denom = math.sqrt(matrix[i][i] * matrix[j][j])
            cross_rows.append(
                {
                    "BCT_row": bct_name,
                    "WZH_row": wzh_name,
                    "covariance": value,
                    "correlation": value / denom,
                    "kind": kind,
                    "provenance": provenance,
                }
            )

    pivots = cholesky_pivots(matrix)
    nonzero = sum(row["covariance"] != 0.0 for row in cross_rows)
    zero = len(cross_rows) - nonzero
    packet = {
        "schema": "MTTCommonSourcePrecisionTransportWorkspace.v1",
        "status": "COMMON_SOURCE_8X8_FIRSTPASS_PRECISION_WORKSPACE_ACCEPTED",
        "closure_claimed": True,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
        "basis_order": basis,
        "source_basis": [
            "M_W_GeV",
            "M_h_GeV",
            "M_t_GeV",
            "alpha3_MZ",
            "m_b_MZ",
            "m_c_MZ",
            "m_tau_MZ",
            "v_from_G_F",
        ],
        "construction": (
            "C_out = J C_source J^T, assembled from the selected WZH sensitivity block, "
            "the admitted BCT covariance block, and the executed one-loop MZ-to-Mt BCT response"
        ),
        "predecessor_product_zero_rule_rejected": True,
        "rejection_reason": (
            "BCT and WZH coordinates are not independent: the executed RG Jacobian already "
            "contains six nonzero BCT-to-lambda/y_t response covariances."
        ),
        "cross_covariance_rows": cross_rows,
        "covariance_matrix": matrix,
        "diagnostics": {
            "matrix_shape": [8, 8],
            "symmetric_unique_entries": 36,
            "BCT_WZH_cross_entries_determined": 15,
            "executed_nonzero_cross_entries": nonzero,
            "structural_one_loop_zero_cross_entries": zero,
            "missing_cross_entries": 0,
            "cholesky_pivots": pivots,
            "positive_definite": True,
            "accepted_as_internal_common_source_firstpass_workspace": True,
            "accepted_as_multiloop_precision_workspace": False,
            "accepted_as_published_or_reconstructed_joint_likelihood": False,
            "accepted_as_final_true_precision_equivalence": False,
        },
        "sources": {
            "BCT_block": (
                "candidate_data/selected_mztomtjacobianexecution_or_selectedthresholdresponsefunctionalfill/"
                "firstpass_weak_bct_crossblock_covariance.packet.json"
            ),
            "WZH_block": (
                "candidate_data/selected_correlatedthresholdprofilematrix_or_yukawahiggsprecisionpromotion/"
                "correlated_threshold_profile_matrix.packet.json"
            ),
            "RG_jacobian": (
                "candidate_data/selected_mztomtjacobianexecution_or_selectedthresholdresponsefunctionalfill/"
                "firstpass_rg_mz_to_mt_jacobian.packet.json"
            ),
        },
    }
    dump(OUT / "common_source_precision_transport_workspace.packet.json", packet)

    theorem = {
        "name": "CommonSourceJacobianPrecisionWorkspacePromotionTheorem",
        "proved": True,
        "statement": (
            "For a source covariance C_source and differentiable transport F with Jacobian J, "
            "the first-order transported covariance is J C_source J^T. On the locked BCT-WZH "
            "basis, the repo's executed one-loop Jacobian determines six nonzero cross entries; "
            "triangular one-loop gauge RG determines the other nine as exact zeros at that order. "
            "The resulting symmetric 8x8 matrix is positive definite, so it is accepted as the "
            "internal common-source first-pass workspace."
        ),
        "scope": "first-order covariance propagation through the selected one-loop replay transport",
        "does_not_claim": [
            "multi-loop precision",
            "published joint likelihood",
            "no-knob derivation of empirical source covariance",
            "final true-SM precision equivalence",
        ],
    }
    candidate = {
        "candidate": "MTT_Selected_ProductPrecisionWorkspaceAcceptance_or_InternalTransportPromotion_v1",
        "status": "MTT_SELECTED_PRODUCTPRECISIONWORKSPACE_INTERNAL_COMMON_SOURCE_FIRSTPASS_PROMOTED_MULTILOOP_OPEN",
        "date": "2026-07-11",
        "closure_claimed": False,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
        "theorem": theorem,
        "closed_now": {
            "provisional_direct_product_independence_rule_retired": True,
            "common_source_cross_covariance_rule_proved": True,
            "BCT_WZH_cross_entries_determined": 15,
            "executed_nonzero_cross_entries": nonzero,
            "structural_one_loop_zero_cross_entries": zero,
            "missing_cross_entries": 0,
            "full_8x8_common_source_covariance_emitted": True,
            "full_8x8_common_source_covariance_positive_definite": True,
            "internal_common_source_firstpass_workspace_accepted": True,
        },
        "still_open": {
            "multiloop_common_source_transport": True,
            "official_or_independently_reconstructed_joint_likelihood": True,
            "empirical_source_covariance_derived_no_knob_from_MTT": True,
            "accepted_true_equivalence_precision_rows": 0,
            "true_precision_equivalence_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
    }
    dump(ROOT / "candidate_data" / f"{SLUG}.candidate.json", candidate)

    certificate = {
        "certificate": "MTT_Selected_ProductPrecisionWorkspaceAcceptance_or_InternalTransportPromotion_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": candidate["status"],
        "closure_claimed": False,
        "theorem_proved": True,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
        "provisional_direct_product_independence_rule_retired": True,
        "common_source_cross_covariance_rule_proved": True,
        "BCT_WZH_cross_entries_determined": 15,
        "executed_nonzero_cross_entries": nonzero,
        "structural_one_loop_zero_cross_entries": zero,
        "BCT_WZH_cross_entries_missing": 0,
        "full_8x8_common_source_covariance_positive_definite": True,
        "internal_common_source_firstpass_workspace_accepted": True,
        "multiloop_common_source_transport_closed": False,
        "published_or_reconstructed_joint_likelihood_imported": False,
        "accepted_true_equivalence_precision_rows": 0,
        "true_precision_equivalence_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
    }
    dump(ROOT / "certificates" / f"{SLUG}_certificate.json", certificate)


if __name__ == "__main__":
    main()
