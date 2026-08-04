"""Audit the dual path End_0 table / B_N identification attempt."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_end0_basis_differential_table_or_bn_identification.candidate.json"
CERT = ROOT / "certificates" / "selected_end0_basis_differential_table_or_bn_identification_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_End0_Basis_Differential_Table_or_BN_Identification_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_END0_BASIS_DIFFERENTIAL_TABLE_DUAL_PATH_ATTEMPTED_SELECTED_TABLES_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    path_a = data["path_A_identify_existing_BN"]
    require(path_a["attempted"] is True, "Path A not attempted")
    require(path_a["closed"] is False, "Path A must not close")
    require(path_a["support_retained"]["dimension_match_27"] is True, "B_N dimension support missing")
    require(path_a["support_retained"]["zero_cluster_dimension_3"] is True, "B_N zero-cluster support missing")
    require(path_a["blocking_evidence"]["ordinary_bundle_equivariance"] is False, "ordinary equivariance blocker missing")
    require(path_a["blocking_evidence"]["projective_equivariance_up_to_central_phase"] is True, "projective blocker missing")
    path_b = data["path_B_direct_End0_table"]
    require(path_b["attempted"] is True, "Path B not attempted")
    require(path_b["closed"] is False, "Path B must remain open")
    require(path_b["emitted_universal_tables"]["Iwasawa_left_invariant_dbar_rules"]["dbar_e3"] == "e1 wedge e2", "dbar table missing")
    require(data["two_path_verdict"]["winner_for_rigor"] == "Path B", "wrong rigorous route")
    require(data["what_closes_now"]["both_paths_tested"] is True, "both paths should be tested")
    require(data["what_closes_now"]["BN_identification_rejected_at_selected_End0_level"] is True, "B_N rejection missing")
    require(
        data["next_required_artifact"] == "MTT_Selected_End0_Direct_Differential_Table_From_AH_Ext_Forms_v1",
        "wrong next artifact",
    )
    require(cert["path_A_BN_identification_closed"] is False, "certificate must keep Path A open")
    require(cert["path_B_direct_table_closed"] is False, "certificate must keep Path B open")
    require("Both paths were tried" in proof, "proof must say both paths were tried")
    require("ordinary_bundle_equivariance = false" in proof, "proof must state B_N blocker")

    print("PASS selected End0 table / BN identification dual-path audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
