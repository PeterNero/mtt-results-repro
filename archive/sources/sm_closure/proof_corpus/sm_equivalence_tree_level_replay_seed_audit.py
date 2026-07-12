"""Audit the first tree-level SM-equivalence replay seed."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "sm_equivalence_tree_level_replay_seed.candidate.json"
CERT = ROOT / "certificates" / "sm_equivalence_tree_level_replay_seed_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_SM_Equivalence_Tree_Level_Replay_Seed_v1.md"
BUILDER = ROOT / "scripts" / "build_sm_equivalence_tree_level_replay_seed.py"

STATUS = "MTT_SM_EQUIVALENCE_TREE_LEVEL_REPLAY_SEED_BUILT_PARTIAL_NUMERIC_REPLAY"
NEXT = "MTT_SM_Equivalence_CKM_Gauge_PMNS_Convention_Fill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note missing next artifact")
    require(data["source_boundary_preserved"] is True, "source boundary not preserved")

    replay = data["tree_level_replay"]
    tests = data["replay_tests"]
    require(tests["mass_replay_exact_by_construction"] is True, "mass replay failed")
    require(tests["max_abs_mass_residual_GeV"] <= 1e-15, "mass residual too large")
    require(tests["diagonal_yukawa_matrices_built"] is True, "Yukawa matrices missing")
    require(tests["higgs_lambda_tree_built"] is True, "Higgs lambda missing")
    require(tests["electroweak_tree_seed_built"] is True, "EW seed missing")
    for key in [
        "CKM_replay_done",
        "PMNS_replay_done",
        "gauge_running_replay_done",
        "RG_common_scale_replay_done",
        "full_SM_equivalence_replay_done",
    ]:
        require(tests[key] is False, f"replay overclaimed: {key}")

    for matrix_name in ["Y_u_diag", "Y_d_diag", "Y_e_diag"]:
        matrix = replay["yukawa_matrices"][matrix_name]
        require(len(matrix) == 3 and all(len(row) == 3 for row in matrix), f"bad matrix shape: {matrix_name}")
        for i in range(3):
            for j in range(3):
                if i != j:
                    require(matrix[i][j] == 0.0, f"matrix not diagonal: {matrix_name}")

    higgs = replay["higgs_tree"]
    require(higgs["lambda_tree"] > 0, "lambda not positive")
    require(higgs["status"] == "TREE_LEVEL_SEED_NOT_RG_MATCHED", "Higgs status overclaimed")

    ew = replay["electroweak_tree"]
    require(ew["g2_from_mW_tree"] > 0, "g2 not positive")
    require(ew["g1_from_mW_mZ_tree"] > 0, "g1 not positive")
    require(0 < ew["sin2thetaW_on_shell_from_masses"] < 1, "sin2 out of range")
    require(ew["status"] == "TREE_LEVEL_ON_SHELL_SEED_NOT_RUNNING_GAUGE_TRIPLET", "EW status overclaimed")

    interp = data["interpretation"]
    not_demo = " ".join(interp["what_this_does_not_demonstrate"])
    for phrase in ["full SM-equivalence", "CKM", "running gauge-coupling", "no-knob"]:
        require(phrase in not_demo, f"interpretation overclaim guard missing: {phrase}")

    closes = data["what_closes_now"]
    for key in [
        "first_numeric_tree_level_replay_seed",
        "diagonal_mass_to_yukawa_to_mass_loop",
        "higgs_tree_lambda_seed",
        "electroweak_tree_coupling_seed",
        "measured_replay_executable_without_source_selection",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "CKM_reference_and_replay",
        "PMNS_neutrino_reference_and_replay",
        "gauge_running_triplet_reference_and_replay",
        "common_RG_scale_transport",
        "full_complex_Yukawa_matrices",
        "full_SM_equivalence_closure",
        "full_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["sm_equivalence_claimed"] is False, "SM equivalence overclaimed")
    require(data["no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used as selector")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("not full SM-equivalence" in note, "note overclaim guard missing")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
