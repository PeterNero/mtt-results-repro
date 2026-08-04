"""Audit the smooth rho_E new-source insertion fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_newsourceinsertion_fillattempt.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_newsourceinsertion_fillattempt.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_newsourceinsertion_fillattempt_certificate.json"
MISSING = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_newsourceinsertion_fillattempt_missing_leaves.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_NewSourceInsertion_FillAttempt_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_NEWSOURCE_FILLATTEMPT_PARTIAL_SOURCE_LAYER_ONLY_VALUES_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_GoodCoverTransitionSkeleton_or_ComplementKernel_v1"


def check(label: str, condition: bool, detail: object) -> None:
    if not condition:
        print(f"FAIL: {label} -- {detail}")
        sys.exit(1)
    print(f"PASS: {label} -- {detail}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    check("script reruns", proc.returncode == 0, proc.stdout + proc.stderr)

    data = load(DATA)
    cert = load(CERT)
    missing = load(MISSING)
    note = NOTE.read_text(encoding="utf-8")

    decision = data["decision"]
    lane_a = data["lane_A_good_cover_transition_tables_fill"]
    lane_b = data["lane_B_exact_complement_factorization_fill"]
    source = data["source_certificate_fill"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("fill executed", decision["fill_attempt_executed"] is True and cert["fill_attempt_executed"] is True, decision)
    check("support imported", decision["ordered_AH_goodcover_source_layer_imported"] is True and decision["terminal_AH_binding_imported"] is True and decision["finite_internal_packet_imported"] is True, decision)
    check("finite leaves filled", lane_a["selected_cover_or_finite_quotient_cover"]["filled"] is True and lane_a["Z3_central_character_matches_tau"]["filled"] is True and lane_b["projection_to_eleven_label_quotient"]["filled"] is True and lane_b["finite_part_equals_log2008_internal_units"]["filled"] is True, (lane_a, lane_b))
    check("source certificate remains heterotic-open", source["same_branch_Qa_SU3_heterotic_projective_source"]["filled"] is False, source)
    check("lane A remains open", decision["lane_A_closed"] is False and cert["lane_A_closed"] is False and lane_a["projective_rhoE_transition_matrices"]["filled"] is False and lane_a["cocycle_law_checked"]["filled"] is False, lane_a)
    check("lane B remains open", decision["lane_B_closed"] is False and cert["lane_B_closed"] is False and lane_b["smooth_operator_domain"]["filled"] is False and lane_b["det_heat_zeta_torsion_factorization"]["filled"] is False, lane_b)
    check("missing leaves written", set(missing) == {"source_certificate", "lane_A_good_cover_transition_tables", "lane_B_exact_complement_factorization"} and len(missing["lane_A_good_cover_transition_tables"]) >= 5 and len(missing["lane_B_exact_complement_factorization"]) >= 3, missing)
    check("no promotion outputs", decision["smooth_transition_tables_emitted"] is False and decision["smooth_finitepart_computed"] is False and decision["E_Qa_computed"] is False, decision)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records boundary", NEXT in note and "maximal legal fill" in note and str(MISSING.relative_to(ROOT)) in note, NOTE)

    print("\nSelected heterotic projective rho_E new-source insertion fill attempt audit")


if __name__ == "__main__":
    main()
