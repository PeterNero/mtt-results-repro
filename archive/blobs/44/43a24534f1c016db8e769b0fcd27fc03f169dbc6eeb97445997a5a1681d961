"""Audit the U1/Y stability/HYM or Route-C residual source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_stability_hym_or_routec_residual_source.py"
DATA = REPO / "candidate_data" / "selected_u1y_stability_hym_or_routec_residual_source.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_stability_hym_or_routec_residual_source_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_Stability_HYM_or_RouteC_Residual_Source_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> None:
    if condition:
        print(f"PASS: {name} -- {detail}")
        return
    print(f"FAIL: {name} -- {detail}")
    raise SystemExit(1)


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout)
    check("builder exits cleanly", proc.returncode == 0, proc.returncode)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    progress = data["stability_progress"]
    theorem = data["reduced_AH_theorem"]
    residual = data["routec_residual_lane"]
    decision = data["decision"]

    check("status exact", data["status"] == "U1Y_STABILITY_HYM_ROUTEC_SOURCE_REDUCED_AH_GLOBAL_STABILITY_PROVED_PROMOTION_OPEN", data["status"])
    check("rank2 and reduced AH closed", progress["rank2_l2_arithmetic_closed"] is True and progress["reduced_AH_global_rank_one_enumeration_proved"] is True, progress)
    check("full stability refused", progress["full_stability_proved"] is False and decision["full_stability_proved"] is False, decision)
    check("AH theorem has six Q candidates", theorem["hom_to_L_nonnegative_candidates"] == [] and len(theorem["hom_to_Q_nonnegative_candidates"]) == 6, theorem)
    check("routec residual shape not selected", residual["shape_gates_closed"]["residual_equations_present_and_zero"] is True and residual["selected_values_emitted"] is False, residual)
    check("promotion gap explicit", data["promotion_gap"]["selected_AH_representative_or_literal_good_cover_table"] is True and data["promotion_gap"]["selected_RouteC_residual_values"] is True, data["promotion_gap"])
    check("lambda remains open", decision["lambda_12_closed"] is False and decision["target_fitting_used"] is False, decision)
    check("certificate agrees", cert["closed"]["reduced_AH_global_rank_one_enumeration_proved"] is True and cert["open"]["selected_HYM_or_Strominger_existence_certificate"] is True, cert)
    check("note records next object", "Selected_U1Y_Selected_AH_or_GoodCover_Promotion_and_HYM_Certificate_v1" in note and "lambda_12_closed = false" in note, NOTE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
