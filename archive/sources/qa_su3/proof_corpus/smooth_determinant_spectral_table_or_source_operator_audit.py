"""Audit the smooth determinant spectral-table/source-operator gate."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "smooth_determinant_spectral_table_or_source_operator_certificate.json"
DATA = REPO / "candidate_data" / "smooth_determinant_spectral_table_or_source_operator.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Smooth_Determinant_Spectral_Table_or_Source_Operator_v1.md"
SCRIPT = REPO / "scripts" / "build_smooth_determinant_spectral_table_or_source_operator.py"


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
    finite = data["finite_hessian_determinant"]
    test = data["smooth_complement_identifiability"]
    source_scan = data["source_scan"]
    checks = [
        check("status", cert["status"] == "QA_SU3_FINITE_HESSIAN_DETERMINANT_CLOSED_SMOOTH_SPECTRUM_UNDERDETERMINED", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("finite spectrum exact", finite["eigenvalues_exact"] == ["8", "18 - sqrt(73)", "18 + sqrt(73)"], finite),
        check("finite determinant exact", finite["determinant_exact"] == 2008 and finite["zeta_regularized_finite_rank_logdet"] == "log(2008)", finite),
        check("finite logdet numeric", abs(finite["zeta_regularized_finite_rank_logdet_numeric"] - math.log(2008)) < 1e-12, finite["zeta_regularized_finite_rank_logdet_numeric"]),
        check("complement changes determinant", test["completion_A"]["determinant"] == "2008" and test["completion_B"]["determinant"] == "2008*Lambda", test),
        check("smooth determinant not identified", test["smooth_determinant_identified"] is False and data["rejection_theorem"]["verdict"] == "SMOOTH_DETERMINANT_REQUIRES_SELECTED_COMPLEMENT_SPECTRUM_OR_SOURCE_OPERATOR", data["rejection_theorem"]),
        check("source scan refuses bounds as table", source_scan["fixed_point_corpus"]["usable_for_full_table"] is False and source_scan["theta_nil_laplacian_corpus"]["usable_for_full_table"] is False, source_scan),
        check("decision split exact", data["decision"]["finite_projected_hessian_zeta_determinant"] == "CLOSED_LOG_2008" and data["decision"]["smooth_threshold_spectral_table"] == "OPEN" and data["decision"]["full_Qa_SU3_threshold_closure_now"] is False, data["decision"]),
        check("not full closure", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("note records next", cert["next_required_artifact"] in note and "finite projected determinant: closed" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 smooth determinant spectral table or source operator audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
