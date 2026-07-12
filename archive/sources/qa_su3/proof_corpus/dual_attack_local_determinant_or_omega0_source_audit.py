"""Audit the dual-lane local determinant / Omega0 source attack."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_dual_attack_local_determinant_or_omega0_source.py"
DATA = REPO / "candidate_data" / "dual_attack_local_determinant_or_omega0_source.candidate.json"
CERT = REPO / "certificates" / "dual_attack_local_determinant_or_omega0_source_certificate.json"
NOTE = REPO / "proof_corpus" / "Dual_Attack_Local_Determinant_or_Omega0_Source_v1.md"


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
    a = data["lane_A_local_determinant"]
    b = data["lane_B_omega0"]

    check("status exact", data["status"] == "DUAL_LANE_ATTACK_DONE_LAMBDA12_OPEN_OMEGA0_REDUCED_TO_ALPHA", data["status"])
    check("all source checks pass", all(data["source_checks"].values()), data["source_checks"])
    check("lane A remains open", data["decision"]["lane_A_lambda12_closed"] is False and a["status"] == "OPEN_SELECTED_GAUGE_FACTOR_SPECTRAL_TABLE_REQUIRED", a)
    check("lane A has Qc and SU2 closed", a["what_closes_now"]["qc_circle_block_closed_for_weak_split"] is True and a["what_closes_now"]["su2_flat_fp_policy_closed_for_weak_split"] is True, a["what_closes_now"])
    check("two thirds remains diagnostic", a["diagnostics_not_proof"]["two_thirds_proxy_lambda_12"] != a["diagnostics_not_proof"]["target_witness_lambda_12"], a["diagnostics_not_proof"])
    check("lane B reduced to alpha", data["decision"]["lane_B_reduced_to_alpha_phys_only"] is True and b["status"] == "REDUCED_TO_ALPHA_PHYS_OR_ACTION_UNIT_ONLY", b)
    check("omega formula numeric", abs(b["reduced_formula"]["Omega0_over_sqrt_alpha_phys"] - b["reduced_formula"]["formula_check_sqrt_15_over_log_448"]) < 1e-15, b["reduced_formula"])
    check("alpha still open", b["blocker"]["alpha_phys_or_action_unit_selected"] is False and b["blocker"]["physical_Omega0_numeric_closed"] is False, b["blocker"])
    check("lanes independent", data["cross_lane_independence"]["can_substitute_lane_b_for_lane_a"] is False and data["cross_lane_independence"]["can_substitute_lane_a_for_lane_b"] is False, data["cross_lane_independence"])
    check("certificate agrees", cert["open"]["lambda12_selected_spectral_table"] is True and cert["open"]["alpha_phys_or_action_unit"] is True, cert)
    check("note records both lanes", "Lane A" in note and "Lane B" in note and "alpha_phys" in note and "selected_spectra_computed = False" in note, NOTE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
