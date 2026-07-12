"""Audit the U1/Y determinant-functional weighting or no-go gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_electroweak_u1y_determinantfunctional_weighting_or_nogo.py"
DATA = REPO / "candidate_data" / "selected_electroweak_u1y_determinantfunctional_weighting_or_nogo.candidate.json"
CERT = REPO / "certificates" / "selected_electroweak_u1y_determinantfunctional_weighting_or_nogo_certificate.json"
TEMPLATE = REPO / "candidate_data" / "selected_electroweak_u1y_determinant_functional_source_theorem.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_U1Y_DeterminantFunctional_Weighting_or_NoGo_v1.md"

STATUS = "ELECTROWEAK_U1Y_DETERMINANT_FUNCTIONAL_WEIGHTING_NOGO_SOURCE_THEOREM_REQUIRED"
NEXT = "Selected_Electroweak_U1Y_DeterminantFunctional_SourceTheorem_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")

    tests = data["candidate_weighting_tests"]
    decision = data["decision"]
    guardrails = data["guardrails"]
    expected = 43.80247549829866 * (2.0 / 3.0)

    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("selected support", data["selected_support"]["Pperp_domain_policy_closed"] is True and data["selected_support"]["conditional_27mode_positive_complement_available"] is True, data["selected_support"]),
        check("conditional weighted logdet", abs(decision["conditional_Pperp_weighted_logdet"] - expected) < 1e-12 and abs(cert["conditional_Pperp_weighted_logdet"] - expected) < 1e-12, decision["conditional_Pperp_weighted_logdet"]),
        check("unweighted rejected", tests["unweighted_rank3_positive_complement"]["status"] == "REJECTED_AS_UNSELECTED_U1Y_FUNCTIONAL", tests["unweighted_rank3_positive_complement"]),
        check("Pperp conditional not promoted", tests["Pperp_weighted_rank3_complement"]["status"] == "CONDITIONAL_MOST_NATURAL_NOT_SELECTED_FINITE_PART" and decision["Pperp_weighting_promoted"] is False, tests["Pperp_weighted_rank3_complement"]),
        check("SU2 open", tests["same_scheme_SU2_cancellation"]["status"] == "OPEN" and decision["same_scheme_SU2_row_or_cancellation_closed"] is False, tests["same_scheme_SU2_cancellation"]),
        check("lambda forbidden", tests["lambda12_from_conditional_weight"]["status"] == "FORBIDDEN_DIAGNOSTIC_ONLY" and decision["lambda_12_closed"] is False, tests["lambda12_from_conditional_weight"]),
        check("template open", template["status"] == "OPEN_SELECTED_U1Y_DETERMINANT_FUNCTIONAL_SOURCE_THEOREM_REQUIRED" and template["functional_components"]["lambda12_formula"] is None, template),
        check("no closure", cert["closure_claimed"] is False and data["closure_claimed"] is False and decision["determinant_functional_source_theorem_found"] is False, decision),
        check("guardrails forbid shortcuts", all(value is False for value in guardrails.values()), guardrails),
        check("note records natural candidate", "natural candidate" in note and "conditional candidate" in note, NOTE),
    ]
    print("\nSelected electroweak U1/Y determinant-functional weighting or no-go audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
