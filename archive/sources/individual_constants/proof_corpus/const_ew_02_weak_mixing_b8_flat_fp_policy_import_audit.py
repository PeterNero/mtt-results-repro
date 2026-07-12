"""Audit const_ew_02_weak_mixing_b8_flat_fp_policy_import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_ew_02_weak_mixing_b8_flat_fp_policy_import"
CANDIDATE = DATA / "const_ew_02_weak_mixing_b8_flat_fp_policy_import.candidate.json"
IMPORTS = BASE / "flat_fp_imports.packet.json"
POLICY = BASE / "flat_fp_policy_promotion.packet.json"
BOUNDARY = BASE / "weak_mixing_boundary_after_fp.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / "const_ew_02_weak_mixing_b8_flat_fp_policy_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B8_FlatFPPolicyImport_v1.md"
BUILD = ROOT / "scripts" / "build_const_ew_02_weak_mixing_b8_flat_fp_policy_import.py"
STATUS = "MTT_CONST_EW_02_B8_FLAT_FP_POLICY_IMPORTED_SU2_WEAKSPLIT_CLOSED_VALUES_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


def approx(a: float, b: float, eps: float = 1e-12) -> bool:
    return abs(a - b) < eps


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILD)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    imports = load(IMPORTS)
    policy = load(POLICY)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(candidate["what_closes_now"]["flat_FP_quotient_policy_for_weaksplit"] is True, "FP policy not closed")
    require(candidate["what_closes_now"]["SU2_selected_for_lambda12_accounting"] is True, "SU2 accounting not closed")
    require(candidate["what_remains_open"]["low_scale_or_effective_sin2thetaW_prediction"] is True, "weak angle closed too early")

    require(imports["status"] == "FLAT_FP_IMPORTS_ACCEPTED", "imports not accepted")
    require(all(imports["import_checks"].values()), "one or more import checks failed")

    require(policy["status"] == "SU2_FLAT_FP_POLICY_PROMOTED_FOR_WEAKSPLIT", "policy status mismatch")
    require(policy["promoted_policy"]["extra_fp_threshold_term"] == 0.0, "extra FP term not zero")
    require(approx(policy["selected_values_for_weaksplit_accounting"]["selected_p_SU2_for_weak_split"], -1.1961941178318218), "p_SU2 mismatch")
    require(approx(policy["selected_values_for_weaksplit_accounting"]["local_lambda_12_internal"], 2.6179362173268497), "lambda mismatch")
    require(any("does not derive x" in item for item in policy["what_this_does_not_change"]), "x boundary missing")
    require(any("does not fix absolute" in item for item in policy["what_this_does_not_change"]), "absolute boundary missing")

    require(boundary["status"] == "SU2_WEAKSPLIT_POLICY_CLOSED_PHYSICAL_WEAK_ANGLE_OPEN", "boundary status mismatch")
    require(boundary["closed_now"]["flat_FP_quotient_policy_for_weaksplit"] is True, "boundary FP missing")
    require(boundary["still_open"]["source_selected_c1_c2_or_T1_T2"] is True, "c1/c2 closed too early")
    require(boundary["still_open"]["RG_matching_scheme"] is True, "RG closed too early")

    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B9-LOCAL-C1C2-SOURCE", "next primary mismatch")
    require("promote B8 as physical sin2thetaW closure" in next_work["forbidden_shortcuts"], "B8 overclaim guard missing")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["flat_FP_policy_closed_for_weaksplit"] is True, "cert FP missing")
    require(cert["extra_flat_fp_threshold_term"] == 0.0, "cert extra FP mismatch")
    require(cert["low_scale_electroweak_closure"] is False, "cert low-scale overclaim")
    require(cert["physical_sin2thetaW_value_claimed"] is False, "cert physical overclaim")
    require("B9-LOCAL-C1C2-SOURCE" in note, "note next label missing")
    require("not a physical weak-angle closure" in note, "note boundary missing")

    for packet in [candidate, imports, policy, boundary, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
