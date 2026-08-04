"""Audit the finite Galerkin to smooth operator promotion/no-go artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "finite_galerkin_to_smooth_operator_promotion_or_nogo_certificate.json"
DATA = REPO / "candidate_data" / "finite_galerkin_to_smooth_operator_promotion_or_nogo.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Finite_Galerkin_to_Smooth_Operator_Promotion_or_NoGo_v1.md"
SCRIPT = REPO / "scripts" / "build_finite_galerkin_to_smooth_operator_promotion_or_nogo.py"


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
    tests = {row["id"]: row for row in data["source_theorem_tests"]}
    coeffs = data["weighted_hessian_gate"]["entry_coefficients_for_H_QT_W_Q"]
    checks = [
        check("status", cert["status"] == "QA_SU3_FINITE_GALERKIN_TO_SMOOTH_OPERATOR_PROMOTION_CURRENT_SOURCE_NO_GO_CONDITIONAL_THEOREM_BUILT", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("finite candidate preserved", data["finite_result_reused"]["validator_passed"] is True and data["finite_result_reused"]["Pi_tw"] == [0, 0, 1], data["finite_result_reused"]),
        check("conditional theorem built", "Q^T W Q" in data["conditional_promotion_theorem"]["statement"], data["conditional_promotion_theorem"]["statement"]),
        check("weighted coefficients include c couplings", coeffs["H13"]["F1"] == -3 and coeffs["H23"]["G4"] == 1 and coeffs["H33"]["F5"] == 1, coeffs),
        check("unit gate records validated block", data["weighted_hessian_gate"]["unit_weight_equations"] == {"H11": 26, "H12": -3, "H13": 0, "H22": 10, "H23": 0, "H33": 8}, data["weighted_hessian_gate"]),
        check("same-source operator not promoted", tests["same_source_smooth_operator"]["current_result"] is False, tests),
        check("charge factorization not found", tests["charge_factorization"]["verdict"] == "NOT_FOUND_IN_CURRENT_SOURCE", tests["charge_factorization"]),
        check("modal democracy not proof-level", tests["unit_weight_or_selected_weight_metric"]["verdict"] == "MODAL_DEMOCRACY_FOUND_ONLY_AS_TIER2_ASSUMPTION", tests["unit_weight_or_selected_weight_metric"]),
        check("current-source no-go", data["decision"]["promotes_now"] is False and data["decision"]["current_source_no_go"] is True, data["decision"]),
        check("not closure", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("note records next", cert["next_required_artifact"] in note and "Modal democracy" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 finite Galerkin to smooth operator promotion/no-go audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
