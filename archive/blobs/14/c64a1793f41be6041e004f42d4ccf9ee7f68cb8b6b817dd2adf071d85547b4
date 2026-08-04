"""Audit heterotic projective rho_E smooth-source/direct-operator closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_smoothsourcetheorem_or_directfiniteoperatorclosure.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothsourcetheorem_or_directfiniteoperatorclosure.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_smoothsourcetheorem_or_directfiniteoperatorclosure_certificate.json"
CONTRACT = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_source_selection_theorem_contract.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_SmoothSourceTheorem_or_DirectFiniteOperatorClosure_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SMOOTHSOURCE_OR_DIRECTFINITE_CLOSURE_REDUCED_SOURCE_SELECTION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SourceSelectionTheorem_or_DirectOperatorIdentity_v1"


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
    check("finite support reused", data["decision"]["finite_response_support_reused"] is True and cert["finite_response_support_reused"] is True, data["decision"])

    lane_a = data["lane_a_finite_quotient"]
    lane_b = data["lane_b_smooth_representative"]
    lane_c = data["lane_c_direct_operator"]
    check("finite quotient partial only", lane_a["support"]["chi_Qa_selected_finite_response_closed"] is True and lane_a["closes_now"] is False, lane_a)
    check("finite quotient blockers exact", lane_a["blocks"]["finite_candidate_identified_as_selected_heterotic_projective_rhoE_source"] is False and lane_a["blocks"]["EndE_to_BN_or_heterotic_threshold_functor_identity"] is False, lane_a["blocks"])
    check("smooth lane open", lane_b["blocks"]["same_branch_Qa_SU3_values_found"] is False and lane_b["closes_now"] is False, lane_b)
    check("direct lane open", lane_c["blocks"]["direct_operator_emission_found"] is False and lane_c["blocks"]["source_certificate_found"] is False and lane_c["closes_now"] is False, lane_c["blocks"])
    check("contract has three options", set(contract["must_prove_one_of"]) == {"finite_physical_quotient_selection", "smooth_representative_map", "direct_operator_identity"}, contract["must_prove_one_of"])
    check("contract keeps finite values", contract["finite_values_available"]["finite_part"]["finite_trace_tau_squared"] == 8 and contract["finite_values_available"]["Riesz_projector"][2][2] == 1, contract["finite_values_available"])
    check("no downstream closure", cert["EndE_to_BN_functor_filled"] is False and cert["E_Qa_computed"] is False and cert["threshold_value_computed"] is False, cert)
    check("guardrails true", all(data["guardrails"].values()) and data["target_fitting_used"] is False, data["guardrails"])
    check("note records reduction", NEXT in note and "One of three things" in note, NOTE)

    print("\nSelected heterotic projective rho_E smooth-source/direct-operator closure audit")


if __name__ == "__main__":
    main()
