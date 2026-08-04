"""Audit the selected Qa/SU3 color-bundle connection/endomorphism interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_color_bundle_connection_endomorphism_interface_certificate.json"
DATA = REPO / "candidate_data" / "selected_qa_su3_color_bundle_connection_endomorphism_interface.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_Qa_SU3_Color_Bundle_Connection_Endomorphism_Interface_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_color_bundle_connection_endomorphism_interface.py"

REQUIRED_CONTAINERS = {
    "rank2_valpha_terminal_monad_plus_s3_gs_same_source",
    "projective_gerbe_twisted_chan_paton_module",
    "direct_selected_hym_routec_or_spectral_galerkin_operator",
    "ordinary_full_nil_theta_section_ring",
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
    evidence = data["imported_evidence"]
    containers = {row["id"]: row for row in data["selected_interface"]["allowed_source_containers_ranked"]}
    sources_present = all(row["present"] for row in data["source_status"].values())
    checks = [
        check("status", cert["status"] == "MTT_SELECTED_QA_SU3_COLOR_BUNDLE_CONNECTION_ENDOMORPHISM_INTERFACE_BUILT_SOURCE_SELECTION_GATE_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("sources present", sources_present, data["source_status"]),
        check("external clues templates only", len(data["external_clues"]) >= 4 and all(row["import_as_proof"] is False for row in data["external_clues"]), data["external_clues"]),
        check("compact nil source still missing", evidence["compact_nil_operator_packet_fill"]["same_branch_source_found"] is False and evidence["compact_nil_operator_packet_fill"]["determinant_computable_now"] is False, evidence["compact_nil_operator_packet_fill"]),
        check("source augmentation blocked honestly", evidence["iwasawa_source_augmentation"]["section_ring_filled"] is False and evidence["iwasawa_source_augmentation"]["operator_exit_available"] is False, evidence["iwasawa_source_augmentation"]),
        check("gerbe repair kept live", evidence["repair_synthesis"]["solution_found_at_typing_level"] is True and gates["gerbe_repair_kept_live"] is True, evidence["repair_synthesis"]),
        check("visible source architecture imported", "same-source" in evidence["visible_source_architecture"]["recommended_construction"]["reason"].lower(), evidence["visible_source_architecture"]),
        check("spectral fallback is engine", gates["spectral_galerkin_kept_as_execution_engine"] is True and "selected_source_verified" in evidence["spectral_fallback"]["next_object"]["exact_task"], evidence["spectral_fallback"]),
        check("route c new source required", "selected visible SM bundle or sheaf model on the q79/F branch" in evidence["routec_gate"]["minimal_new_data_that_would_close"], evidence["routec_gate"]),
        check("ranked containers complete", REQUIRED_CONTAINERS.issubset(containers), containers.keys()),
        check("primary same-source gate identified", gates["primary_same_source_gate_identified"] is True and containers["rank2_valpha_terminal_monad_plus_s3_gs_same_source"]["rank"] == 1, containers["rank2_valpha_terminal_monad_plus_s3_gs_same_source"]),
        check("operator not promoted", gates["operator_packet_promoted"] is False and cert["what_remains_open"]["selected_Qa_SU3_color_operator_packet"] is True, cert),
        check("closure not claimed", gates["sm_parity_closure_claimed"] is False and gates["no_knob_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", data["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert),
        check("note has theorem and next artifact", "same-source visible/color" in note and "MTT_Selected_Qa_SU3_Same_Source_Visible_Color_Operator_Packet_v1" in note, NOTE),
    ]
    print("\nMTT selected Qa/SU3 color-bundle connection/endomorphism interface audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
