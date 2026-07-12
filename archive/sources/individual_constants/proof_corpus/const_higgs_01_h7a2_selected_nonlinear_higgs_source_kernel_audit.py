"""Audit CONST-HIGGS-01 H7A2 selected nonlinear Higgs source-kernel gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7a2_selected_nonlinear_higgs_source_kernel"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
SPECTRAL_OBSTRUCTION = BASE / "zero_mode_spectral_determinant_obstruction.packet.json"
NONLINEAR_CANDIDATES = BASE / "nonlinear_source_candidate_hunt.packet.json"
KERNEL_CONTRACT = BASE / "selected_nonlinear_kernel_acceptance_contract.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7A2_SelectedNonlinearHiggsSourceKernel_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7A2_NONLINEAR_SOURCE_KERNEL_GATE_BUILT_SOURCE_OPEN"


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
    obstruction = load(SPECTRAL_OBSTRUCTION)
    candidates = load(NONLINEAR_CANDIDATES)
    contract = load(KERNEL_CONTRACT)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("obstruction", obstruction),
        ("candidates", candidates),
        ("contract", contract),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["zero_mode_spectral_determinant_obstruction_proved"] is True, "obstruction")
    require(candidate["nonlinear_source_candidates_classified"] is True, "candidate hunt")
    require(candidate["nonlinear_kernel_acceptance_contract_ready"] is True, "contract")
    require(candidate["selected_nonlinear_source_kernel_found"] is False, "source overfound")
    require(candidate["same_source_H_sector_fourth_variation_row_emitted"] is False, "K4 emitted")
    require(candidate["numeric_lambda_H_derived"] is False, "lambda numeric")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "no-knob")
    require(candidate["new_Higgs_specific_parameters"] == 0, "Higgs params")

    spectral = obstruction["selected_finite_spectral_data"]
    require(spectral["finite_heat_spectrum_response_slot_closed"] is True, "heat slot")
    require(spectral["H_sector_kernel_dimension"] == 1, "H kernel")
    require(spectral["Higgs_amplitude_coordinate"] == 12, "H coordinate")
    require(spectral["Higgs_coordinate_is_zero_mode"] is True, "H zero mode")
    routes = obstruction["two_naive_determinant_routes"]
    require(routes["positive_complement_only"]["depends_on_Higgs_zero_mode_amplitude"] is False, "positive complement dependence")
    require(routes["positive_complement_only"]["emits_K4_for_a_H"] is False, "positive complement K4")
    require(routes["reinsert_zero_mode_as_mass_shift"]["analytic_at_a_H_0"] is False, "zero analytic")
    require(routes["reinsert_zero_mode_as_mass_shift"]["emits_finite_fourth_derivative_at_origin"] is False, "zero finite K4")
    verdict = obstruction["verdict"]
    require(verdict["spectral_heat_logdet_support_remains_valid"] is True, "spectral support")
    require(verdict["naive_logdet_promoted_to_Higgs_quartic"] is False, "logdet promoted")
    require(verdict["separate_selected_nonlinear_zero_mode_potential_required"] is True, "zero potential")

    for candidate_info in candidates["candidates"].values():
        require(candidate_info["promoted_to_nonlinear_kernel"] is False, "candidate promoted")
    require(candidates["candidate_promoted"] is False, "candidate promotion")
    require(candidates["best_current_strict_route_A_candidate"] == "selected nonlinear zero-mode effective potential from same q79/F,m=1 source", "best route")

    target = contract["target_row"]
    require(target["formal_object"] == "K_H^(4)[a_H,a_H,a_H,a_H]", "target object")
    require(target["row_address"] == [12, 12, 12, 12], "target row")
    required = contract["current_field_status"]
    for key, value in required.items():
        require(value is False, f"field {key} overfilled")
    theorem = contract["required_source_theorem"]
    require(theorem["name"] == "SelectedNonlinearHiggsZeroModePotentialTheorem", "source theorem name")
    require("V_eff is analytic at a_H=0 after zero-mode projection/renormalization" in theorem["must_prove"], "analytic theorem")
    formula = contract["conditional_exact_formula_slot"]
    require("d^4/da_H^4" in formula["if_functional_supplied"], "conditional formula")
    require(formula["filled_now"] is False, "formula filled")

    require("H7A3-SELECTED-NONLINEAR-ZERO-MODE-POTENTIAL-THEOREM" in next_work["route_A_next"]["label"], "next A3")
    require("H7B-UV-BETA-OR-TWO-HIGGS-PROJECTION-THEOREM" in next_work["route_B_parallel"]["label"], "next B")
    require(cert["status"] == STATUS, "cert status")
    require(cert["zero_mode_spectral_determinant_obstruction_proved"] is True, "cert obstruction")
    require(cert["selected_nonlinear_source_kernel_found"] is False, "cert source")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert no-knob")
    require("log(a_H^2)" in note and "H7A2-SELECTED-NONLINEAR" in note, "note")

    print("CONST-HIGGS-01 H7A2 selected nonlinear Higgs source-kernel audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
