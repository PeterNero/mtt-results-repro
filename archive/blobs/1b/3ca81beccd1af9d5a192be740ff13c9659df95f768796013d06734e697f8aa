"""Audit the smooth-transition/complement-quotient/no-double-count gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_smoothtransitiontables_or_complementquotient_nodoublecount.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothtransitiontables_or_complementquotient_nodoublecount.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_smoothtransitiontables_or_complementquotient_nodoublecount_certificate.json"
CONTRACT = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_exact_complement_or_smooth_transition_value_contract.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_SmoothTransitionTables_or_ComplementQuotient_NoDoubleCount_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_NODOUBLECOUNT_POLICY_CLOSED_SMOOTHTABLES_COMPLEMENTQUOTIENT_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_ExactComplementQuotient_or_SmoothRhoETransitionTables_ValuePacket_v1"


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
    contract = load(CONTRACT)
    note = NOTE.read_text(encoding="utf-8")

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("no double count closed", data["decision"]["no_double_count_policy_closed"] is True and cert["no_double_count_policy_closed"] is True, data["no_double_count_policy"])
    check("GR routing closed", data["decision"]["GR_surface_routing_closed"] is True and data["no_double_count_policy"]["smooth_GR_surface_not_counted_as_QaSU3_internal_threshold"] is True, data["no_double_count_policy"])
    check("finite retained", data["decision"]["finite_internal_quotient_retained"] is True and data["no_double_count_policy"]["finite_internal_value_retained"] == "log(2008)", data["decision"])
    check("smooth lanes open", data["decision"]["smooth_transition_tables_emitted"] is False and data["decision"]["exact_complement_quotient_closed"] is False, data["decision"])
    check("E and finite part open", data["decision"]["E_Qa_computed"] is False and data["decision"]["smooth_finitepart_computed"] is False, data["decision"])
    check("contract requires two lanes", len(contract["lane_A_smooth_transition_tables_required"]) >= 8 and len(contract["lane_B_exact_complement_quotient_required"]) >= 5, contract)
    check("contract prerequisites", all(contract["closed_prerequisites"].values()), contract["closed_prerequisites"])
    check("cross checks", data["cross_checks"]["GR_no_double_count_guardrail_present"] is True and data["cross_checks"]["smooth_nonidentifiability_examples_retained"] is True, data["cross_checks"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["decision"]["full_physical_threshold_claimed"] is False, data["decision"])
    check("note documents closed/open split", NEXT in note and "no-double-count policy" in note and "does not prove exact" in note, NOTE)

    print("\nSelected heterotic projective rho_E smooth-transition/complement-quotient no-double-count audit")


if __name__ == "__main__":
    main()
