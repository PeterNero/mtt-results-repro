"""Audit const_em_01_alpha1_dimensional_anchor_fill_attempt."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_em_01_alpha1_dimensional_anchor_fill_attempt"
CANDIDATE = DATA / "const_em_01_alpha1_dimensional_anchor_fill_attempt.candidate.json"
STRICT = BASE / "strict_no_knob_fill.packet.json"
ONE_ANCHOR = BASE / "one_anchor_metrology.packet.json"
EXECUTION = BASE / "execution_formulae.packet.json"
CERT = ROOT / "certificates" / "const_em_01_alpha1_dimensional_anchor_fill_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EM_01_Alpha1_DimensionalAnchorFillAttempt_v1.md"
BUILD = ROOT / "scripts" / "build_const_em_01_alpha1_dimensional_anchor_fill_attempt.py"
STATUS = "MTT_CONST_EM_01_DIMENSIONAL_ANCHOR_FILL_ATTEMPT_STRICT_OPEN_ONE_ANCHOR_READY"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


def close(a: float, b: float, tol: float = 1e-14) -> bool:
    return abs(a - b) < tol


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
    strict = load(STRICT)
    one_anchor = load(ONE_ANCHOR)
    execution = load(EXECUTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["what_closes_now"]["strict_fill_attempt_executed"] is True, "fill not executed")
    require(candidate["what_closes_now"]["mtheory_structural_slot_filled"] is True, "M-theory slot missing")
    require(candidate["what_closes_now"]["conditional_execution_formulae"] is True, "formulae missing")
    require(candidate["what_closes_now"]["one_anchor_extension_ready"] is True, "one-anchor extension missing")
    require(candidate["what_closes_now"]["strict_no_knob_promotion"] is False, "strict promotion overclaimed")
    require(candidate["what_remains_open"]["source_selected_L0_or_E0"] is True, "source-selected anchor closed too early")

    require(strict["checks"]["gate_available"] is True, "gate unavailable")
    require(strict["checks"]["route_is_mtheory_modal_gap"] is True, "wrong route")
    require(strict["checks"]["mtheory_structural_slot_filled"] is True, "structural slot not filled")
    require(strict["checks"]["same_branch_alignment"] is True, "same-branch alignment missing")
    require(strict["checks"]["forbidden_inputs_absent"] is True, "forbidden input present")
    require(strict["checks"]["dimensionful_value_present"] is False, "dimensionful value unexpectedly present")
    require(strict["checks"]["selected_by_mtt"] is False, "selected_by_mtt unexpectedly true")
    require(strict["checks"]["computed_before_target_comparison"] is False, "computed-before-target unexpectedly true")
    require(strict["checks"]["alpha_phys_value_present"] is False, "alpha value unexpectedly present")
    require(strict["promotion_now"] is False, "strict promotion true")

    tau = math.log(448) / 15
    require(close(one_anchor["length_anchor_form"]["numeric_coefficients"]["tau_int"], tau), "length tau mismatch")
    require(close(one_anchor["energy_anchor_form"]["numeric_coefficients"]["sqrt_tau_int"], math.sqrt(tau)), "energy sqrt tau mismatch")
    require(one_anchor["status"] == "ONE_ANCHOR_EXTENSION_READY_NOT_SELECTED", "one-anchor status mismatch")

    vals = execution["dimensionless_internal_values"]
    require(close(vals["tau_int"], tau), "execution tau mismatch")
    require(close(vals["inv_sqrt_tau_int"], 1 / math.sqrt(tau)), "inverse sqrt tau mismatch")
    require(vals["lambda_internal"] == 15, "lambda internal mismatch")
    require(execution["source_text_checks"]["modal_unit_theorem_has_lambda_internal"] is True, "modal source check failed")
    require(execution["source_text_checks"]["metrology_no_go_has_one_anchor_solution"] is True, "metrology source check failed")
    require(execution["source_text_checks"]["clock_search_has_same_branch_bridge"] is True, "clock source check failed")

    require(cert["strict_no_knob_promotion"] is False, "cert strict overclaim")
    require(cert["one_anchor_extension_ready"] is True, "cert one-anchor missing")
    require(cert["physical_value_claimed"] is False, "cert physical overclaim")
    require("Strict no-knob promotion is still open" in note, "note verdict missing")
    require("This is not a fitted knob if, and only if" in note, "note one-anchor guard missing")

    for packet in [candidate, strict, one_anchor, execution, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
