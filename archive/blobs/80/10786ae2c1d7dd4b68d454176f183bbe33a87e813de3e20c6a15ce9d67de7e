"""Audit the direct End_0 differential-table attempt from AH/Ext forms."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_end0_direct_differential_table_from_ah_ext_forms.candidate.json"
CERT = ROOT / "certificates" / "selected_end0_direct_differential_table_from_ah_ext_forms_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_End0_Direct_Differential_Table_From_AH_Ext_Forms_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_END0_DIRECT_TABLE_PARTIAL_AH_EXT_FORM_TEMPLATE_BUILT_HYM_TABLES_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    require(data["selected_source_boundary"]["selected_AH_source_layer_imported"] is True, "selected AH layer missing")
    require(data["AH_transition_seed"]["built"] is True, "AH transition seed missing")
    require(data["AH_transition_seed"]["central_shared_circle_degree_zero"] is True, "shared circle guardrail missing")
    ext = data["Ext_local_form_template"]
    require(ext["built"] is True, "Ext symbolic template not built")
    require(ext["selected_basis_slot"] == "theta_plus_0_tensor_eta_minus_0", "wrong Ext slot")
    require(ext["symbolic_representative"] == "theta_plus_0(z1) tensor eta_minus_0(z2) dbar_z2", "wrong symbolic form")
    require(ext["closed_nonexact"] is True, "Ext should be closed nonexact")
    require(ext["not_yet_numeric_local_form"] is True, "must not be numeric table yet")
    table = data["partial_End0_differential_table"]
    require(table["built"] is True, "partial End0 table missing")
    require(table["safe_to_use_for_newton"] is False, "must not be Newton safe")
    require(data["newton_readiness"]["ready"] is False, "Newton must remain blocked")
    require(
        data["newton_readiness"]["first_blocker"] == "selected_normalized_local_form_table_for_theta_plus_0_tensor_eta_minus_0",
        "wrong first blocker",
    )
    require(data["what_closes_now"]["Newton_first_blocker_reduced_to_normalized_local_form_table"] is True, "blocker not reduced")
    require(
        data["next_required_artifact"] == "MTT_Selected_Normalized_Ext_Local_Form_Table_v1",
        "wrong next artifact",
    )
    require(cert["newton_ready"] is False, "certificate must keep Newton blocked")
    require("symbolic local-form bridge" in proof, "proof must state symbolic bridge")
    require("This is not yet a Newton-ready table" in proof, "proof must state nonclosure")

    print("PASS selected End0 direct AH/Ext form table audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
