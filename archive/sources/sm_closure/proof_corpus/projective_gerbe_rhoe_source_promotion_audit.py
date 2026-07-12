"""Audit the projective gerbe rho_E source-promotion artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "projective_gerbe_rhoe_source_promotion.candidate.json"
CERT = REPO / "certificates" / "projective_gerbe_rhoe_source_promotion_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Projective_Gerbe_RhoE_Source_Promotion_v1.md"


def check(name: str, condition: bool, detail: object) -> tuple[str, bool, object]:
    return name, condition, detail


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    flags = data["promotion_gate_flags_after_s3_closure"]
    result = data["promotion_result"]

    checks = [
        check("status", data["status"] == "MTT_PROJECTIVE_GERBE_RHOE_PROMOTED_TO_S3_SOURCE_OPERATOR_OPEN", data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert),
        check("superset partial promotion", data["superset_mode"]["classification"] == "SUPERSET_REPAIR_PARTIAL_PROMOTION", data["superset_mode"]),
        check("no target fitting", data["target_fitting_used"] is False and data["superset_mode"]["diagnostic_backfit_only"]["used"] is False, data["superset_mode"]["diagnostic_backfit_only"]),
        check("S3 source flags close", all(flags[k] for k in ["selected_by_mtt", "fixed_differential_cohomology_class", "map_to_central_cocycle_verified", "green_schwarz_bianchi_verified", "freed_witten_verified", "twisted_projector_retains_sector"]), flags),
        check("coherent spectral still open", flags["coherent_spectral_projector_verified"] is False and cert["what_remains_open"]["coherent_spectral_zero_mode_projectors"] is True, flags),
        check("source level promoted", result["source_level_projective_gerbe_rhoE_promoted"] is True and cert["what_closes"]["projective_gerbe_rhoE_promoted_to_selected_S3_source_level"] is True, result),
        check("operator level open", result["operator_level_projective_rhoE_promoted"] is False and cert["what_remains_open"]["selected_visible_Chern_Weil_operator_source"] is True, result),
        check("remaining cut set retained", result["remaining_cut_set"]["selected_D_E_dotD_Riesz_Green"] is True and result["remaining_cut_set"]["Chern_Weil_row_derived_from_selected_source"] is True, result["remaining_cut_set"]),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Selected_Visible_Chern_Weil_Operator_Source_v1" and cert["next_required_artifact"] == "MTT_Selected_Visible_Chern_Weil_Operator_Source_v1", cert),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["Phi_fin_selected_payload"] is True, cert),
        check("note records partial promotion", "promoted at the selected S3 gerbe source" in note and "not yet at the visible operator-source level" in note, NOTE),
    ]

    failed = False
    for name, condition, detail in checks:
        status = "PASS" if condition else "FAIL"
        print(f"{status}: {name} -- {detail}")
        if not condition:
            failed = True
    print("\nMTT projective gerbe rho_E source-promotion audit")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
