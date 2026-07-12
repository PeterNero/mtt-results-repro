"""Audit heterotic projective rho_E finite-candidate promotion attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_finitecandidate_promotion_or_smoothrepresentative.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_finitecandidate_promotion_or_smoothrepresentative.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_finitecandidate_promotion_or_smoothrepresentative_certificate.json"
OBLIGATIONS = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_promotion_obligations.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_FiniteCandidate_PromotionOrSmoothRepresentative_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_FINITE_CANDIDATE_PROMOTION_ATTEMPT_SMOOTH_REPRESENTATIVE_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothSourceTheorem_or_DirectFiniteOperatorClosure_v1"


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
    obligations = load(OBLIGATIONS)
    note = NOTE.read_text(encoding="utf-8")

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("finite replay", data["fill_result"]["finite_candidate_values_replayed"] is True and cert["finite_candidate_values_replayed"] is True, data["fill_result"])
    finite = data["finite_candidate_replay"]
    check("finite values intact", finite["central_cocycle_law_checked"] is True and finite["finite_part"]["finite_trace_tau_squared"] == 8 and finite["Riesz_projector"][2][2] == 1, finite)
    fill = data["fill_result"]
    check("smooth representative open", fill["selected_Deligne_Cech_or_B_field_representative"] is False and cert["smooth_heterotic_representative_emitted"] is False, fill)
    check("transition tables open", fill["rho_E_transition_or_boundary_matrices"] is False and cert["rho_E_transition_tables_emitted"] is False, fill)
    check("operator identity open", fill["same_source_operator_identity_to_finite_response"] is False and cert["same_source_smooth_operator_identity_proved"] is False, fill)
    check("admissibility open", fill["Freed_Witten_check"] is False and fill["projector_retention_check"] is False, fill)
    check("q79 guardrail only", data["smooth_representative_search"]["q79_explicit_flat_values_found"] is True and data["smooth_representative_search"]["same_branch_Qa_SU3_values_found"] is False, data["smooth_representative_search"])
    check("obligations written", obligations["status"] == "OPEN" and len(obligations["minimal_closing_options"]) == 3 and len(obligations["unmet_smooth_promotion_leaves"]) >= 10, obligations)
    check("no downstream closure", cert["EndE_to_BN_functor_filled"] is False and cert["E_Qa_computed"] is False and cert["threshold_value_computed"] is False, cert)
    check("guardrails true", all(data["guardrails"].values()) and data["target_fitting_used"] is False, data["guardrails"])
    check("note records legal closures", NEXT in note and "Legal Closures" in note and "finite Galerkin quotient" in note, NOTE)

    print("\nSelected heterotic projective rho_E finite-candidate promotion audit")


if __name__ == "__main__":
    main()
