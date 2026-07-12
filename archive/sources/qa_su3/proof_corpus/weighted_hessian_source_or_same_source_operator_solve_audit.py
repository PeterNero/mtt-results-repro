"""Audit the weighted Hessian source / same-source operator solve artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "weighted_hessian_source_or_same_source_operator_solve_certificate.json"
DATA = REPO / "candidate_data" / "weighted_hessian_source_or_same_source_operator_solve.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Weighted_Hessian_Source_or_Same_Source_Operator_Solve_v1.md"
SCRIPT = REPO / "scripts" / "build_weighted_hessian_source_or_same_source_operator_solve.py"


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
    family = data["product_pair_symmetric_family"]
    unit = data["examples"]["unit_counting_metric"]
    nontrivial = data["examples"]["nontrivial_positive_metric"]
    checks = [
        check("status", cert["status"] == "QA_SU3_WEIGHTED_HESSIAN_SOLVE_SELECTOR_STABLE_SOURCE_ORTHOGONALITY_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("family derived", family["derived"] == {"x2": "3*x1 - 2*x5", "x4": "4*x1 - 3*x5"}, family),
        check("unit metric recovers finite H", unit["H"] == [[26, -3, 0], [-3, 10, 0], [0, 0, 8]], unit["H"]),
        check("nontrivial metric exists", nontrivial["weights"]["F2"] == "3/2" and nontrivial["c_axis_decoupled"] is True, nontrivial),
        check("selector stable in examples", unit["Pi_tw_stable"] is True and nontrivial["Pi_tw_stable"] is True, data["examples"]),
        check("unit not required", cert["what_closes"]["unit_weights_not_required_for_tau"] is True, cert),
        check("unit unique under full block", "x1=x2=x3=x4=x5=p=1" in data["strong_unit_uniqueness_if_full_block_selected"]["result"], data["strong_unit_uniqueness_if_full_block_selected"]),
        check("source remains open", all(value == "OPEN" for value in data["source_status"].values()), data["source_status"]),
        check("not closure", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("note records next", cert["next_required_artifact"] in note and "H13 = H23 = 0" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 weighted Hessian source or same-source operator solve audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
