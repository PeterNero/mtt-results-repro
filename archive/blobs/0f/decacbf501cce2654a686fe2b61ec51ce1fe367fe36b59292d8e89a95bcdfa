"""Audit the selected normalized Ext local-form table checkpoint."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_normalized_ext_local_form_table.candidate.json"
CERT = ROOT / "certificates" / "selected_normalized_ext_local_form_table_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_Normalized_Ext_Local_Form_Table_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_NORMALIZED_EXT_LOCAL_FORM_TABLE_BUILT_L2_THETA_QUADRATURE_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    identity = data["selected_ext_identity"]
    require(identity["label"] == "theta_plus_0_tensor_eta_minus_0", "wrong selected Ext label")
    require(identity["cohomology_vector_C1"] == [1, 0, 0, 0, 0, 0, 0, 0], "wrong Ext vector")
    require(identity["central_shared_circle_degree"] == 0, "shared circle degree must remain zero")
    policy = data["normalization_policy"]
    require(policy["cohomological_normalization_closed"] is True, "cohomological normalization missing")
    require(policy["cohomological_coefficient"] == 1, "cohomological coefficient must be one")
    require(policy["L2_theta_quadrature_closed"] is False, "L2 quadrature must remain open")
    require(policy["overlap_trivialization_table_closed"] is False, "overlap table must remain open")
    require("not a computed physical L2 norm" in policy["guardrail"], "guardrail missing")
    table = data["local_form_table"]
    require(len(table) == 1, "expected one selected local-form row")
    row = table[0]
    require(row["row_id"] == "eta_00", "wrong row id")
    require(row["selected"] is True, "row must be selected")
    require(row["cohomology_coefficient"] == 1, "wrong row coefficient")
    require(row["l2_norm_value"] is None, "L2 norm must not be filled")
    require(row["overlap_transition_values"] is None, "overlap values must not be filled")
    require(row["newton_ready"] is False, "row must not be Newton-ready")
    support = data["yoneda_scalar_support"]
    require(support["selected_row_scalar"] == 1, "Yoneda scalar support must be one")
    require(support["nonzero_image"] is True, "Yoneda image must be nonzero")
    readiness = data["newton_readiness"]
    require(readiness["ready"] is False, "Newton must remain blocked")
    require(readiness["cohomological_row_ready"] is True, "cohomological row should be ready")
    require(
        readiness["first_blocker"] == "selected_L2_theta_quadrature_and_overlap_table_for_eta_00",
        "wrong first blocker",
    )
    require(
        data["next_required_artifact"] == "MTT_Selected_Ext_L2_Theta_Quadrature_Table_v1",
        "wrong next artifact",
    )
    require(cert["newton_ready"] is False, "certificate must keep Newton blocked")
    require("not a physical `L2` norm" in proof, "proof must state L2 guardrail")
    require("MTT_Selected_Ext_L2_Theta_Quadrature_Table_v1" in proof, "proof must state next artifact")

    print("PASS selected normalized Ext local-form table audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
