"""Audit the selected Qa/SU3 operator-source import audit artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_operator_source_import_audit_certificate.json"
DATA = REPO / "candidate_data" / "selected_qa_su3_operator_source_import_audit.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_Qa_SU3_Operator_Source_Import_Audit_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_operator_source_import_audit.py"

REQUIRED_ROUTES = {
    "nontrivial_su3_color_bundle_connection_endomorphism",
    "global_section_gribov_fundamental_domain_measure",
    "ray_singer_reidemeister_torsion_local_system",
    "finite_coherent_projector_jacobian",
    "local_fp_brst_extra_jacobian",
    "soft_gauge_tube_width",
}


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
    gates = data["gate_results"]
    sources_present = all(body["present"] for body in data["source_status"].values())
    route_ids = {row["id"] for row in data["import_routes"]}
    routes = {row["id"]: row for row in data["import_routes"]}
    checks = [
        check("status", cert["status"] == "MTT_SELECTED_QA_SU3_OPERATOR_SOURCE_IMPORT_AUDIT_BUILT_BEST_ROUTE_IDENTIFIED_SOURCE_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("sources present", sources_present, data["source_status"]),
        check("routes complete", REQUIRED_ROUTES.issubset(route_ids), route_ids),
        check("external templates recorded", len(data["external_templates"]) >= 4 and all(row["import_as_proof"] is False for row in data["external_templates"]), data["external_templates"]),
        check("compact branch imported", data["computed_compact_nil_branch"]["fully_computed"] is True and data["computed_compact_nil_branch"]["obstructed_as_final_proof"] is True, data["computed_compact_nil_branch"]),
        check("best route identified", data["decision"]["best_next_route"] == "nontrivial_su3_color_bundle_connection_endomorphism" and gates["best_next_route_identified"] is True, data["decision"]),
        check("best route open not promoted", routes["nontrivial_su3_color_bundle_connection_endomorphism"]["legal"] is True and routes["nontrivial_su3_color_bundle_connection_endomorphism"]["promoted_now"] is False, routes["nontrivial_su3_color_bundle_connection_endomorphism"]),
        check("torsion route open", routes["ray_singer_reidemeister_torsion_local_system"]["legal"] is True, routes["ray_singer_reidemeister_torsion_local_system"]),
        check("global section route open", routes["global_section_gribov_fundamental_domain_measure"]["legal"] is True, routes["global_section_gribov_fundamental_domain_measure"]),
        check("double counting rejected", routes["local_fp_brst_extra_jacobian"]["legal"] is False and routes["soft_gauge_tube_width"]["legal"] is False and gates["double_counting_routes_rejected"] is True, routes),
        check("no operator promoted", gates["operator_source_promoted"] is False and cert["what_remains_open"]["selected_Qa_SU3_color_operator_packet"] is True, cert),
        check("closure not claimed", gates["sm_parity_closure_claimed"] is False and gates["no_knob_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", data["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert),
        check("note records template guardrail", "not imported as MTT proof data" in note and "double-count" in note, NOTE),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Selected_Qa_SU3_Color_Bundle_Connection_Endomorphism_Interface_v1", data["next_required_artifact"]),
    ]
    print("\nMTT selected Qa/SU3 operator-source import audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
