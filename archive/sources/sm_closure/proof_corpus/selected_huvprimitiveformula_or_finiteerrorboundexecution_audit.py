"""Audit Huv primitive formula or finite error-bound execution packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_huvprimitiveformula_or_finiteerrorboundexecution"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HuvPrimitiveFormulaOrFiniteErrorBoundExecution_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

CONTRACT = BASE / "huv_primitive_formula_execution_contract.packet.json"
UNDERDETERMINATION = BASE / "bhuv_support_underdetermination_witness.packet.json"
ATTEMPT = BASE / "huv_primitive_formula_execution_attempt.packet.json"
CUTSET = BASE / "next_cutset_after_huv_primitive_formula_attempt.packet.json"

STATUS = (
    "MTT_SELECTED_HUVPRIMITIVEFORMULA_OR_FINITEERRORBOUNDEXECUTION_"
    "UNDERDETERMINED_SOURCE_FUNCTIONAL_OPEN"
)
NEXT = "MTT_Selected_FiniteHFunctionalOrMSourceValueEmission_v1"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_no_selector(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label}: observed selector")
    require(packet.get("target_fitting_used") is False, f"{label}: target fitting")


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    cert = load(CERT)
    contract = load(CONTRACT)
    under = load(UNDERDETERMINATION)
    attempt = load(ATTEMPT)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require_no_selector(candidate, "candidate")

    decision = candidate["closure_decision"]
    for key in [
        "primitive_formula_contract_closed",
        "underdetermination_witness_constructed",
        "B_Huv_support_direct_closure_rejected",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "selected_finite_H_functional_emitted",
        "selected_M_source_value_emitted",
        "selected_primitive_H_response_kernel_emitted",
        "finite_error_bound_emitted",
        "selected_H_response_value_rows_emitted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    nums = candidate["key_numbers"]
    require(nums["non_scalar_herm2_witnesses"] == 2, "witness count")
    require(nums["accepted_value_row_count"] == 0, "accepted values")
    require(nums["accepted_final_certificate_count"] == 0, "accepted certs")
    require(nums["accepted_payload_slot_count"] == 0, "accepted payload")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(cert["non_scalar_herm2_witnesses"] == 2, "cert witness count")
    for key in [
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
        "selected_finite_H_functional_emitted",
        "selected_M_source_value_emitted",
        "selected_primitive_H_response_kernel_emitted",
        "finite_error_bound_emitted",
        "selected_H_response_value_rows_emitted",
    ]:
        require(cert[key] is False, f"cert false {key}")

    require(contract["status"] == "HUV_PRIMITIVE_FORMULA_EXECUTION_CONTRACT_FIXED", "contract status")
    for value in contract["closed_inputs"].values():
        require(value is True, "contract closed input")
    routes = contract["legal_execution_routes"]
    require(set(routes) == {
        "finite_H_functional_second_variation",
        "selected_M_source_restriction",
        "direct_primitive_overlap_rows",
    }, "routes")
    require(contract["decision"]["formula_contract_closed"] is True, "contract closed")
    require(contract["decision"]["execution_requires_value_source_not_more_support"] is True, "needs value source")
    require_no_selector(contract, "contract")

    require(under["status"] == "BHUV_SUPPORT_UNDERDETERMINES_HERM2_VALUE_ROWS", "under status")
    require(len(under["two_non_scalar_herm2_completions_same_support"]) == 2, "under witnesses")
    rows0 = under["two_non_scalar_herm2_completions_same_support"][0]["rows"]
    rows1 = under["two_non_scalar_herm2_completions_same_support"][1]["rows"]
    require(rows0 != rows1, "witness rows differ")
    udec = under["decision"]
    require(udec["underdetermination_witness_constructed"] is True, "under built")
    require(udec["B_Huv_support_selects_value_rows"] is False, "support selects")
    require(udec["direct_closure_from_support_only_allowed"] is False, "support closure")
    require_no_selector(under, "under")

    require(attempt["status"] == "HUV_PRIMITIVE_FORMULA_EXECUTION_ATTEMPTED_ZERO_ROWS", "attempt status")
    adec = attempt["decision"]
    require(adec["execution_attempted"] is True, "attempted")
    require(adec["formula_contract_available"] is True, "contract available")
    require(adec["underdetermination_witness_constructed"] is True, "witness available")
    for key in [
        "selected_finite_H_functional_emitted",
        "selected_M_source_value_emitted",
        "selected_primitive_H_response_kernel_emitted",
        "finite_error_bound_emitted",
        "selected_H_response_value_rows_emitted",
    ]:
        require(adec[key] is False, f"attempt false {key}")
    require(adec["accepted_value_row_count"] == 0, "attempt accepted rows")
    for value in attempt["execution_values"].values():
        require(value is None, "attempt value emitted")
    require_no_selector(attempt, "attempt")

    require(cutset["status"] == "NEXT_FRONTIER_FINITE_H_FUNCTIONAL_OR_MSOURCE_VALUE_EMISSION", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "primitive Huv formula execution contract fixed",
        "B_Huv support-only direct closure rejected by explicit Herm(2) underdetermination witness",
        "current finite-H, M_source, and primitive-overlap routes rechecked with zero accepted rows",
    ]:
        require(phrase in cutset["closed_here"], f"closed {phrase}")
    for phrase in [
        "selected finite H-sector functional F_H with second variation on B_Huv",
        "or selected same-source Hermitian M_source values",
        "or selected primitive H-response kernel K_H with finite trace execution",
        "row-level exactness proof or rigorous finite error bound",
    ]:
        require(phrase in cutset["still_open"], f"open {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "The direct closure attempt is now mathematically decided.",
        "diag(1,-1)  -> Huu=1, Hud=0, Hdd=-1",
        "[[0,1],[1,0]] -> Huu=0, Hud=1, Hdd=0",
        "attaching `B_Huv` support cannot close the final row payload",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: direct Huv primitive formula attack completed; "
        "B_Huv support underdetermines rows, so F_H/M_source/K_H value emission remains."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
