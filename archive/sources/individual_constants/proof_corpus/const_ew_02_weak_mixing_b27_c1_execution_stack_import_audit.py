"""Audit CONST-EW-02 B27 C1 execution-stack import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b27_c1_execution_stack_import"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
C1_VALUES = BASE / "c1_algebraic_values_import.packet.json"
TRACE_MEASURE = BASE / "trace_measure_and_boundary_import.packet.json"
LAST_SOURCE = BASE / "last_source_contract_import.packet.json"
BOUNDARY = BASE / "weak_mixing_b27_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B27_C1ExecutionStackImport_v1.md"

STATUS = "MTT_CONST_EW_02_B27_C1_EXECUTION_STACK_IMPORTED_SOURCE_PROMOTION_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    c1_values = load(C1_VALUES)
    trace_measure = load(TRACE_MEASURE)
    last_source = load(LAST_SOURCE)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("c1_values", c1_values),
        ("trace_measure", trace_measure),
        ("last_source", last_source),
        ("boundary", boundary),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["primitive_C1_algebraic_values_filled"] == 72, "primitive count")
    require(candidate["total_C1_algebraic_values_filled"] == 110, "total count")
    require(candidate["formal_computation_layer_closed_as_support"] is True, "formal layer")
    require(candidate["last_source_theorem_contract_built"] is True, "last contract")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")
    require(candidate["strict_full_no_knob_closure"] is False, "no-knob overclosed")

    counts = c1_values["imported_counts"]
    require(counts["primitive_values_filled"] == 72, "C1 primitive count")
    require(counts["hessian_values_filled"] == 2, "hessian count")
    require(counts["sector_values_filled"] == 36, "sector count")
    require(counts["total_algebraic_values_filled"] == 110, "total algebraic count")
    require(counts["independent_quadrature_values"] == 0, "independent quadrature overclaim")
    require(counts["physical_source_promoted_values"] == 0, "physical source overclaim")
    require(c1_values["what_this_retires_locally"]["locked_target_algebraic_replay"] is True, "locked replay")
    require(c1_values["promotion_still_required"]["derive_selected_physical_action_identity"] is True, "missing action gate")

    boundary_cert = trace_measure["boundary_certificate"]
    require(boundary_cert["algebraic_boundary_closed_now"] is True, "finite boundary not closed")
    require(boundary_cert["physical_boundary_promoted_now"] is False, "physical boundary overpromoted")
    require(trace_measure["what_remains_open"]["physical_PhiFinC1_action_identity"] is True, "physical action missing from open")
    require(trace_measure["what_remains_open"]["same_source_b_selected_emission"] is True, "b_selected missing from open")

    retired = last_source["retired_as_blockers"]
    require(retired["alpha1_dotD"] is True, "alpha1/dotD not retired")
    require(retired["canonical_residual_values"] is True, "canonical residual not retired")
    require(retired["formal_computation_layer"] is True, "formal computation not retired")
    cutset = last_source["remaining_exact_cutset"]
    require(cutset["same_branch_Phi_fin_C1_source_emission"] is True, "Phi_fin source missing")
    require(cutset["same_source_b_selected_emission"] is True, "b_selected missing")
    require(cutset["or_independent_Galerkin_or_row_provenance_run"] is True, "independent run missing")

    advanced = boundary["advanced_now"]
    require(advanced["primitive_C1_algebraic_values_filled"] == 72, "boundary primitive count")
    require(advanced["total_C1_algebraic_values_filled"] == 110, "boundary total count")
    require(advanced["algebraic_finite_trace_boundary_closed"] is True, "boundary finite trace")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "boundary weak angle missing")
    require(boundary["still_open"]["K_phys_or_f_ab"] is True, "gauge edge dropped")
    require(boundary["still_open"]["same_source_b_selected"] is True, "b edge dropped")

    require(cert["status"] == STATUS, "cert status")
    require(cert["same_branch_phifin_source_closed"] is False, "cert source overclosed")
    require(cert["independent_hessian_quadrature_source_closed"] is False, "cert independent overclosed")
    require(cert["physical_weak_angle_closure"] is False, "cert weak angle")
    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B28-SAMEBRANCH-PHIFIN-C1-SOURCE-EMISSION", "next primary")
    require("primitive C1 algebraic values filled = 72" in note, "note count")

    print("CONST-EW-02 B27 C1 execution-stack import audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
