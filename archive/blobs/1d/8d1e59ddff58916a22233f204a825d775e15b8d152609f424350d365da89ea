"""Audit smooth-operator source packet or complement-quotient interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_or_complementquotient.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_or_complementquotient.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_or_complementquotient_certificate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket.template.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_SmoothOperator_SourcePacket_or_ComplementQuotientTheorem_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SMOOTHOPERATOR_SOURCEPACKET_INTERFACE_BUILT_VALUES_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothOperator_SourcePacket_FillAttempt_v1"


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
    template = load(TEMPLATE)
    note = NOTE.read_text(encoding="utf-8")

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("interface built", data["decision"]["interface_built"] is True and cert["interface_built"] is True, cert)
    check("best lane", data["decision"]["best_next_lane"] == "B_selected_smooth_operator_source_packet", data["decision"])
    check("smooth support strong", all(data["lanes"]["smooth_operator_source_packet"]["current_support"].values()), data["lanes"]["smooth_operator_source_packet"]["current_support"])
    check("smooth missing all false", not any(data["lanes"]["smooth_operator_source_packet"]["current_missing"].values()), data["lanes"]["smooth_operator_source_packet"]["current_missing"])
    check("complement not closed", data["decision"]["complement_quotient_theorem_closed"] is False and data["lanes"]["complement_quotient"]["closes_now"] is False, data["lanes"]["complement_quotient"])
    check("template open", template["status"] == "OPEN_VALUES_REQUIRED" and template["next_required_artifact"] == NEXT, template)
    check("template has required sections", set(template) >= {"source_certificate", "smooth_projective_source", "bundle_operator", "finite_part", "admissibility", "forbidden_shortcuts"}, template)
    check("no values filled", template["smooth_projective_source"]["Deligne_Cech_or_B_field_representative"] is None and template["bundle_operator"]["E_Qa_matrix_or_zero_order_block"] is None and template["finite_part"]["finite_part_value"] is None, template)
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["decision"]["E_Qa_computed"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records template", NEXT in note and "same-branch Strominger/Iwasawa context" in note and str(TEMPLATE.relative_to(ROOT)) in note, NOTE)

    print("\nSelected heterotic projective rho_E smooth-operator source-packet interface audit")


if __name__ == "__main__":
    main()
