"""Audit the smooth rho_E transition skeleton or complement-kernel equations."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_goodcover_transition_skeleton_or_complement_kernel.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_goodcover_transition_skeleton_or_complement_kernel.candidate.json"
EQS = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_goodcover_transition_skeleton_or_complement_kernel.equations.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_goodcover_transition_skeleton_or_complement_kernel_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_GoodCoverTransitionSkeleton_or_ComplementKernel_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_GOODCOVER_TRANSITION_SKELETON_OR_COMPLEMENT_KERNEL_BUILT_VALUES_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SourceTableSolve_or_ComplementKernelProof_v1"


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
    eqs = load(EQS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    decision = data["decision"]
    transition = eqs["transition_skeleton"]
    kernel = eqs["complement_kernel"]
    labels = kernel["current_known_values"]["labels"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and eqs["status"] == "EQUATIONS_BUILT_VALUES_OPEN", (data["status"], cert["status"], eqs["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("skeletons built", data["transition_skeleton_built"] is True and data["complement_kernel_built"] is True and cert["transition_skeleton_built"] is True and cert["complement_kernel_built"] is True, cert)
    check("eleven unknown tables", len(transition["unknowns"]) == 11 and set(transition["unknowns"]) == set(labels), transition["unknowns"].keys())
    check("tau shadow equations", "projective_triple_overlap" in transition["required_equations"] and "finite_character_shadow" in transition["required_equations"], transition["required_equations"])
    check("metric and bianchi equations", "metric_unitarity" in transition["required_equations"] and "freed_witten_bianchi" in transition["required_equations"], transition["required_equations"])
    check("complement kernel equations", set(kernel["required_factorization_equations"]) >= {"domain_decomposition", "heat_trace_split", "zeta_split", "finite_part_rule", "no_double_count"}, kernel["required_factorization_equations"])
    check("known finite values carried", kernel["current_known_values"]["finite_part_internal_units"] == "log(2008)" and len(kernel["current_known_values"]["D_fin"]) == 11, kernel["current_known_values"])
    check("values remain open", decision["smooth_transition_values_solved"] is False and decision["exact_complement_kernel_proved"] is False and decision["smooth_finitepart_computed"] is False, decision)
    check("source requirements strict", eqs["source_requirements"]["same_branch_source_certificate_required"] is True and eqs["source_requirements"]["observed_data_allowed"] is False, eqs["source_requirements"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records equations", NEXT in note and str(EQS.relative_to(ROOT)) in note and "two explicit equation" in note, NOTE)

    print("\nSelected heterotic projective rho_E good-cover transition skeleton / complement-kernel audit")


if __name__ == "__main__":
    main()
