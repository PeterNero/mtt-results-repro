"""Audit the selected visible Green-Schwarz/operator-source gate artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_visible_green_schwarz_operator_source_certificate.json"
DATA = REPO / "candidate_data" / "selected_visible_green_schwarz_operator_source.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_Visible_Green_Schwarz_Operator_Source_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_visible_green_schwarz_operator_source.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    superset = data["superset_mode"]
    gates = data["gate_results"]
    imported = data["imported_results"]
    sources_present = all(row["present"] for row in data["source_status"].values())
    checks = [
        check("status", cert["status"] == "MTT_SELECTED_VISIBLE_GREEN_SCHWARZ_OPERATOR_SOURCE_GATE_BUILT_OPERATOR_PIPELINE_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("sources present", sources_present, data["source_status"]),
        check("superset classification", cert["superset_mode"] == "SUPERSET_CONVERGENCE_PLUS_REPAIR" and superset["classification"] == "SUPERSET_CONVERGENCE_PLUS_REPAIR", superset),
        check("straight GS path rejected", superset["straight_path"]["succeeds"] is False and cert["what_closes"]["GS_only_straight_path_rejected"] is True, superset["straight_path"]),
        check("no diagnostic fitting", superset["diagnostic_backfit_only"]["used"] is False and data["target_fitting_used"] is False, superset["diagnostic_backfit_only"]),
        check("S3 source imported closed", gates["selected_s3_source_closed"] is True and imported["selected_s3_source"]["status"] == "MTT_SELECTED_S3_DIFFERENTIAL_COHOMOLOGY_SOURCE_CERTIFICATE_CLOSED_OPERATOR_SOURCE_OPEN", imported["selected_s3_source"]),
        check("visible GS curvature imported closed", gates["visible_green_schwarz_curvature_closed"] is True and imported["visible_gs_curvature"]["visible_green_schwarz_curvature_verified"] is True, imported["visible_gs_curvature"]),
        check("operator source still open", gates["operator_source_cut_set_still_open"] is True and gates["selected_visible_operator_source_constructed"] is False, gates),
        check("blocker irreducible", imported["visible_operator_blocker_resolution"]["status"] == "VISIBLE_OPERATOR_SOURCE_BLOCKER_IRREDUCIBLE_NEW_SOURCE_REQUIRED" and gates["blocker_resolved_by_existing_data"] is False, imported["visible_operator_blocker_resolution"]),
        check("first blocker selected operator source", gates["first_blocking_layer_is_selected_operator_source"] is True, gates),
        check("HYM route not closed", gates["selected_hym_or_route_c_residual_closed"] is False and imported["selected_hym_operator_source_attempt"]["selected_hym_operator_source_verified"] is False, imported["selected_hym_operator_source_attempt"]),
        check("DE/dotD still open", gates["selected_D_E_dotD_Riesz_Green_constructed"] is False and cert["what_remains_open"]["selected_D_E_dotD_Riesz_Green"] is True, cert),
        check("Qa/SU3 still open", gates["selected_Qa_SU3_packet_closed"] is False and cert["what_remains_open"]["selected_Qa_SU3_color_operator_packet"] is True, cert),
        check("payload contract same-source", data["operator_source_payload_contract"]["must_be_same_source"] is True and data["operator_source_payload_contract"]["branch"]["q"] == 79, data["operator_source_payload_contract"]),
        check("closure not claimed", gates["sm_parity_closure_claimed"] is False and gates["no_knob_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Selected_RouteC_HYM_Operator_Pipeline_v1", data["next_required_artifact"]),
        check("note records classification", "SUPERSET_CONVERGENCE_PLUS_REPAIR" in note and "They do not" in note, NOTE),
    ]
    print("\nMTT selected visible Green-Schwarz/operator-source gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
