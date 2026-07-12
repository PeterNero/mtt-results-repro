"""Audit const_ew_02_weak_mixing_b7_local_coefficient_source_gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_ew_02_weak_mixing_b7_local_coefficient_source_gate"
CANDIDATE = DATA / "const_ew_02_weak_mixing_b7_local_coefficient_source_gate.candidate.json"
IMPORTS = BASE / "source_imports.packet.json"
COEFF = BASE / "coefficient_source_gate.packet.json"
SU2 = BASE / "su2_quotient_policy_gate.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / "const_ew_02_weak_mixing_b7_local_coefficient_source_gate_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B7_LocalCoefficientSourceGate_v1.md"
BUILD = ROOT / "scripts" / "build_const_ew_02_weak_mixing_b7_local_coefficient_source_gate.py"
STATUS = "MTT_CONST_EW_02_B7_LOCAL_COEFFICIENT_SOURCE_GATE_BUILT_VALUES_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


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
    coeff = load(COEFF)
    su2 = load(SU2)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(candidate["what_closes_now"]["diagnostic_c1_c2_classified"] is True, "diagnostic c1/c2 not classified")
    require(candidate["what_closes_now"]["near_hit_weight_gate_blocked"] is True, "near hit not blocked")
    require(candidate["what_closes_now"]["SU2_flat_background_support_promoted"] is True, "SU2 flat support not promoted")
    require(candidate["what_remains_open"]["flat_FP_quotient_policy"] is True, "flat FP policy closed too early")
    require(candidate["what_remains_open"]["low_scale_or_effective_sin2thetaW_prediction"] is True, "weak angle overclosed")

    require(imports["status"] == "LOCAL_COEFFICIENT_IMPORTS_ACCEPTED_WITH_VALUE_BOUNDARY", "imports status mismatch")
    require(all(imports["import_checks"].values()), "one or more import checks failed")

    require(coeff["status"] == "C1_C2_SOURCE_NOT_SELECTED_DIAGNOSTICS_CLASSIFIED", "coefficient status mismatch")
    require(coeff["closed_formula"]["Delta_alpha_12_split"] == "2*c1 - c2", "Delta alpha formula mismatch")
    require(coeff["diagnostic_coefficients"]["Execution_I"]["promoted"] is False, "Execution-I c1/c2 overpromoted")
    require(coeff["diagnostic_coefficients"]["operator_weight_near_hit"]["promoted"] is False, "near hit overpromoted")
    require(coeff["source_gate"]["current_source_coefficients_selected"] is False, "source coefficients selected too early")
    require(coeff["forbidden_promotions"]["reverse_engineered_weights"]["reason"].startswith("These are solved"), "reverse-engineered guard missing")

    require(su2["status"] == "SU2_FLATNESS_CLOSED_QUOTIENT_POLICY_OPEN", "SU2 status mismatch")
    require(su2["proved_flatness_statement"]["closed"] is True, "SU2 flatness not closed")
    require(su2["conditional_zero_extra_branch"]["selectable_now"] is False, "zero-extra branch selected too early")
    require(su2["decision"]["flat_background_support_promoted"] is True, "flat support missing")
    require(su2["decision"]["flat_FP_quotient_policy_promoted"] is False, "FP policy overpromoted")

    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B8-FLAT-FP-QUOTIENT-POLICY", "next primary mismatch")
    require("reverse-engineer operator weights" in next_work["forbidden_shortcuts"][1], "shortcut guard missing")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["Execution_I_c1_c2_promoted"] is False, "cert Execution-I overclaim")
    require(cert["two_thirds_near_hit_promoted"] is False, "cert near-hit overclaim")
    require(cert["SU2_flat_background_support_promoted"] is True, "cert SU2 support missing")
    require(cert["flat_FP_quotient_policy_closed"] is False, "cert FP policy overclaim")
    require(cert["physical_sin2thetaW_value_claimed"] is False, "cert physical overclaim")
    require("B8-FLAT-FP-QUOTIENT-POLICY" in note, "note next label missing")
    require("not promoted" in note, "note boundary missing")

    for packet in [candidate, imports, coeff, su2, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
