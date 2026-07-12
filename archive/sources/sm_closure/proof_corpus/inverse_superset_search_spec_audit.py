"""Audit the inverse superset search specification artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "inverse_superset_search_spec_certificate.json"
DATA = REPO / "candidate_data" / "inverse_superset_search_spec.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Inverse_Superset_Search_Spec_v1.md"
SCRIPT = REPO / "scripts" / "build_inverse_superset_search_spec.py"

REQUIRED_DOMAINS = {
    "finite_topology_packet",
    "qa_su3_operator_packet",
    "theta_gauge_threshold_packet",
    "flavor_overlap_packet",
    "absolute_normalization_packet",
}

REQUIRED_SCORING = {
    "target_residual",
    "complexity_penalty",
    "discreteness_bonus",
    "corpus_alignment_score",
    "cross_sector_consistency",
    "forward_replay_score",
}

REQUIRED_GATES = {"G0_inverse_candidate", "G1_compression", "G2_source_alignment", "G3_cross_sector", "G4_forward_replay"}


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
    domain_ids = {row["id"] for row in data["search_domains"]}
    scoring_ids = {row["id"] for row in data["scoring_terms"]}
    promotion_ids = {row["id"] for row in data["promotion_gates"]}
    rejection_text = " ".join(data["rejection_rules"]).lower()
    first = data["required_first_run"]
    checks = [
        check("status", cert["status"] == "MTT_INVERSE_SUPERSET_SEARCH_SPEC_BUILT_NUMERIC_RUN_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("domains complete", REQUIRED_DOMAINS.issubset(domain_ids), domain_ids),
        check("scoring complete", REQUIRED_SCORING.issubset(scoring_ids), scoring_ids),
        check("promotion gates complete", REQUIRED_GATES.issubset(promotion_ids), promotion_ids),
        check("search space defined", gates["search_space_defined"] is True and gates["scoring_defined"] is True, gates),
        check("rejection rules defined", gates["rejection_rules_defined"] is True and "only support is target residual" in rejection_text, data["rejection_rules"]),
        check("reject per constant knobs", "separate independent continuous knobs" in rejection_text, data["rejection_rules"]),
        check("forward replay required", "forward_replay_score" in scoring_ids and "G4_forward_replay" in promotion_ids, data["promotion_gates"]),
        check("first run is qa su3", first["run_id"] == "qa_su3_first" and "qa_su3_operator_packet" in first["domains"], first),
        check("forbidden selectors recorded", "masses" in first["targets_forbidden_as_selectors"] and "gauge_coupling_values" in first["targets_forbidden_as_selectors"], first),
        check("numeric run still open", gates["numeric_search_executed"] is False and cert["what_remains_open"]["actual_numeric_inverse_search"] is True, cert),
        check("no candidate promoted", gates["candidate_promoted"] is False and cert["what_remains_open"]["selected_Qa_SU3_color_operator_packet"] is True, cert),
        check("closure not claimed", gates["sm_parity_closure_claimed"] is False and gates["no_knob_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("target fitting spec labeled", data["target_fitting_used"] is True and data["target_fitting_role"] == "DISCOVERY_ONLY_SPEC", data),
        check("note records anti proof rule", "without claiming no-knob derivation" in note and "current forward SM-parity blocker" in note, NOTE),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Inverse_Qa_SU3_First_Search_Run_v1", data["next_required_artifact"]),
    ]
    print("\nMTT inverse superset search spec audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
