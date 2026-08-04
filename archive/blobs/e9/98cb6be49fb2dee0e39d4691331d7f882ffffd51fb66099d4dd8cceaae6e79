"""Audit physical-anchor or smooth-EQa source-fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_physicalanchor_or_smootheqa_sourcefillattempt.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_physicalanchor_or_smootheqa_sourcefillattempt.candidate.json"
REPORT = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_physicalanchor_or_smootheqa_sourcefill_report.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_physicalanchor_or_smootheqa_sourcefillattempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_PhysicalAnchor_or_SmoothEQa_SourceFillAttempt_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SOURCEFILL_PARTIAL_EW_INTERNAL_THRESHOLD_CLOSED_PHYSICAL_ANCHOR_SMOOTHEQA_OPEN"
NEXT = "Selected_Electroweak_GaugeKinetic_Normalization_and_RG_Scheme_SourceTheorem_v1"


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
    report = load(REPORT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    physical = report["filled_physical_lane"]
    smooth = report["filled_smooth_lane"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("internal branch locked", decision["internal_branch_remains_locked"] is True, decision)
    check("physical convention filled", physical["typed_electroweak_convention_map"]["filled"] is True and decision["new_physical_lane_progress"]["typed_electroweak_convention_map_closed"] is True, physical["typed_electroweak_convention_map"])
    check("internal weaksplit filled", physical["threshold_vector_or_local_determinant_vector_if_electroweak_matching_is_attempted"]["filled"] == "partial_internal_weaksplit_only" and decision["new_physical_lane_progress"]["internal_weaksplit_threshold_closed"] is True, physical["threshold_vector_or_local_determinant_vector_if_electroweak_matching_is_attempted"])
    check("known internal weaksplit values", physical["threshold_vector_or_local_determinant_vector_if_electroweak_matching_is_attempted"]["lambda_12_internal"] > 0 and physical["threshold_vector_or_local_determinant_vector_if_electroweak_matching_is_attempted"]["Delta_G12_internal"] > 0, physical["threshold_vector_or_local_determinant_vector_if_electroweak_matching_is_attempted"])
    check("no target proof filled", physical["proof_no_observed_constant_selected_any_missing_value"]["filled"] is True and physical["proof_no_observed_constant_selected_any_missing_value"]["target_fitting_used"] is False, physical["proof_no_observed_constant_selected_any_missing_value"])
    check("physical anchor still open", decision["physical_anchor_still_open"] is True and physical["K_phys_or_Omega0_or_ellp_or_kappa11_or_alpha_prime"]["filled"] is False, physical["K_phys_or_Omega0_or_ellp_or_kappa11_or_alpha_prime"])
    check("RG and matching still open", decision["matching_scale_still_open"] is True and decision["RG_scheme_still_open"] is True, decision)
    check("smooth geometry support but no EQa", smooth["bundle_curvature_F_A"]["R_plus_curvature_available"] is True and smooth["smooth_E_Qa_matrix_or_equivalent_finitepart_operator"]["filled"] is False and decision["smooth_EQa_still_open"] is True, smooth)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure overclaim", data["closure_claimed"] is False and report["closure_claimed"] is False and cert["closure_claimed"] is False, cert)
    check("note records result", NEXT in note and "lambda_12_internal" in note and NOTE.exists(), NOTE)

    print("\nSelected heterotic projective rho_E physical-anchor / smooth-EQa source-fill audit")


if __name__ == "__main__":
    main()
