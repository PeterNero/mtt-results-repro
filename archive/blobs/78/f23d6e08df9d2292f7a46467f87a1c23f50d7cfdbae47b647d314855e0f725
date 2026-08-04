"""Audit flat-torsion promotion / smooth-transition table gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_flattorsionpromotion_or_smoothtransitiontables.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_flattorsionpromotion_or_smoothtransitiontables.candidate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_symbolic_smoothtransition_table_template.json"
SOURCE_GAP = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothtransition_source_gap.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_flattorsionpromotion_or_smoothtransitiontables_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_FlatTorsionPromotion_or_SmoothTransitionTables_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SYMBOLIC_TRANSITION_TABLE_TEMPLATE_BUILT_SMOOTH_PROMOTION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothTransitionSourceGap_Closure_or_DirectOperatorPayload_v1"


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
    template = load(TEMPLATE)
    source_gap = load(SOURCE_GAP)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and template["status"] == "SYMBOLIC_TEMPLATE_ONLY_NOT_SOURCE_PROMOTED", (data["status"], cert["status"], template["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("symbolic table built", decision["symbolic_smooth_transition_template_built"] is True and cert["symbolic_smooth_transition_template_built"] is True, decision)
    check("eleven labels", len(template["symbolic_transition_table"]) == 11 and set(template["symbolic_transition_table"]) == {"F1", "F2", "F3", "F4", "F5", "G1", "G2", "G3", "G4", "G5", "P"}, template["symbolic_transition_table"].keys())
    check("cocycle laws", template["formal_all_cocycles_pass"] is True and decision["formal_cocycle_law_passes"] is True and cert["formal_cocycle_law_passes"] is True, template)
    check("unitarity laws", template["formal_all_unitarity_pass"] is True and decision["formal_unitarity_passes_for_scalar_U1_phases"] is True, template)
    check("curvature split", template["curvature_layer"]["B_exact"] == {"56": "6"} and template["curvature_layer"]["dB_equals_H"] is True and template["curvature_layer"]["flat_layer_curvature"] == 0, template["curvature_layer"])
    check("product cancellation", template["formal_all_products_cancel_to_P"] is True and cert["formal_products_cancel_to_P"] is True and len(template["product_checks"]) == 5, template["product_checks"])
    check("source gap open", all(value is None for value in source_gap["not_yet_source_promoted"].values()) and len(source_gap["minimal_closing_payload"]) == 6, source_gap)
    check("formal passes recorded", all(source_gap["passed_formally"].values()), source_gap["passed_formally"])
    check("not promoted", decision["smooth_source_promoted"] is False and cert["smooth_source_promoted"] is False and template["smooth_source_promoted"] is False, decision)
    check("S1 remains open", decision["S1_closed"] is False and cert["S1_closed"] is False and data["still_open"]["selected_smooth_good_cover_or_domain"] is True, data["still_open"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no target fitting or closure", data["target_fitting_used"] is False and template["target_fitting_used"] is False and source_gap["target_fitting_used"] is False and cert["closure_claimed"] is False, cert)
    check("note records template and gap", str(TEMPLATE.relative_to(ROOT)) in note and str(SOURCE_GAP.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic projective rho_E flat-torsion promotion / smooth-transition table audit")


if __name__ == "__main__":
    main()
