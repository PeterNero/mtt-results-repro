"""Audit the inverse superset reconstruction artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "inverse_superset_reconstruction_certificate.json"
DATA = REPO / "candidate_data" / "inverse_superset_reconstruction.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Inverse_Superset_Reconstruction_v1.md"
SCRIPT = REPO / "scripts" / "build_inverse_superset_reconstruction.py"

REQUIRED_TARGETS = {
    "gauge_couplings",
    "yukawa_masses_mixings",
    "gravity_and_dimensionful_scales",
    "qa_su3_color_operator_packet",
}

REQUIRED_STAGES = {
    "inverse_fit",
    "compression",
    "corpus_alignment",
    "forward_replay",
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
    target_ids = {row["id"] for row in data["measured_targets"]}
    stage_ids = {row["stage"] for row in data["reconstruction_stages"]}
    all_sources_present = all(body["all_present"] for body in data["source_status"].values())
    guardrail_text = " ".join(data["guardrails"]).lower()
    checks = [
        check("status", cert["status"] == "MTT_INVERSE_SUPERSET_RECONSTRUCTION_PROTOCOL_BUILT_DISCOVERY_ONLY", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("sources present", all_sources_present, data["source_status"]),
        check("target groups complete", REQUIRED_TARGETS.issubset(target_ids), target_ids),
        check("stages complete", REQUIRED_STAGES.issubset(stage_ids), stage_ids),
        check("measured constants discovery only", gates["measured_constants_allowed_as_discovery_data"] is True and gates["measured_constants_allowed_as_forward_selectors"] is False, gates),
        check("target fitting labeled", data["target_fitting_used"] is True and data["target_fitting_role"] == "DISCOVERY_ONLY", data),
        check("promotion path to sm parity", data["promotion_path_to_sm_parity"]["helps_sm_parity_closure"] is True, data["promotion_path_to_sm_parity"]),
        check("frontier link retained", data["promotion_path_to_sm_parity"]["current_frontier_link"] == "MTT_Qa_SU3_Color_Operator_Packet_Source_Gate_v1", data["promotion_path_to_sm_parity"]),
        check("promotion tests defined", gates["promotion_tests_defined"] is True, gates),
        check("guardrails forbid selectors", "may not select final source data" in guardrail_text and "forward replay" in guardrail_text, data["guardrails"]),
        check("no numeric fit yet", gates["actual_numeric_inverse_fit_run"] is False and cert["what_remains_open"]["actual_numeric_inverse_fit_run"] is True, cert),
        check("no packet promoted yet", gates["candidate_packet_promoted"] is False and cert["what_remains_open"]["selected_Qa_SU3_color_operator_packet"] is True, cert),
        check("closure not claimed", gates["sm_parity_closure_claimed"] is False and gates["no_knob_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("note states not no-knob proof", "does not claim no-knob prediction" in note and "removed from the selector set" in note, NOTE),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Inverse_Superset_Search_Spec_v1", data["next_required_artifact"]),
    ]
    print("\nMTT inverse superset reconstruction audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
