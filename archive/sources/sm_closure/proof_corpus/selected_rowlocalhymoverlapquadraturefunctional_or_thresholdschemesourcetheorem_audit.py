"""Audit selected row-local HYM overlap quadrature / threshold scheme gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FUNCTIONAL_PACKET = PACKET_DIR / "selected_overlap_quadrature_functional.packet.json"
SOURCE_LEDGER_PACKET = PACKET_DIR / "available_source_import_ledger.packet.json"
MODEL_TRIAL_PACKET = PACKET_DIR / "finite_model_active_quadrature_trial.packet.json"
THRESHOLD_GATE_PACKET = PACKET_DIR / "threshold_scheme_source_gate.packet.json"
DEGENERACY_PACKET = PACKET_DIR / "current_source_degeneracy_nogo.packet.json"
CUTSET_PACKET = PACKET_DIR / "next_cutset_after_quadrature_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RowLocalHYMOverlapQuadratureFunctional_or_ThresholdSchemeSourceTheorem_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_ROWLOCALHYMOVERLAPQUADRATUREFUNCTIONAL_OR_THRESHOLDSCHEMESOURCETHEOREM_"
    "BUILT_FUNCTIONAL_AND_DEGENERACY_NOGO_ROWS_OPEN"
)
NEXT = "MTT_Selected_PhiFinMinimizerTraceRowLocalKernel_or_ThresholdSchemeValueRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")
    require(packet.get("closure_claimed") is True, f"{label} should close this audit theorem")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    functional = load(FUNCTIONAL_PACKET)
    source = load(SOURCE_LEDGER_PACKET)
    trial = load(MODEL_TRIAL_PACKET)
    threshold = load(THRESHOLD_GATE_PACKET)
    degeneracy = load(DEGENERACY_PACKET)
    cutset = load(CUTSET_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("functional", functional),
        ("source", source),
        ("trial", trial),
        ("threshold", threshold),
        ("degeneracy", degeneracy),
        ("cutset", cutset),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    require(len(functional["functional_rows"]) == 5, "functional row contract incomplete")
    require(functional["acceptance_predicate"]["ordinary_fit_parameters_forbidden"] is True, "fit guard missing")
    require(functional["acceptance_predicate"]["target_values_used_only_after_emission"] is True, "postcheck guard missing")

    require(source["closed_inputs"]["diagonal_HYM_first_solve"] is True, "diagonal HYM not imported")
    require(source["closed_inputs"]["full_diagonal_End0_Green"] is True, "Green not imported")
    require(source["closed_inputs"]["model_active_projector_values_emitted"] is True, "model values not imported")
    require(source["open_inputs"]["selected_HYM_projector_values_promoted"] is False, "projectors overpromoted")
    require(source["open_inputs"]["physical_dotD_alpha1_verified"] is False, "dotD overpromoted")
    require(source["open_inputs"]["selected_threshold_response_functional_instantiated"] is False, "threshold overpromoted")

    require(trial["row_count"] == 10, "trial row count mismatch")
    require(trial["target_values_are_postcheck_only"] is True, "trial target guard missing")
    require(trial["charged_basis_degenerate"] is True, "charged basis degeneracy missing")
    require(trial["distinct_model_active_L_values"] <= 1, "model-active L should be degenerate")
    require(trial["accepted_L_rowlocal_source_row_count"] == 0, "L rows overaccepted")
    require(trial["accepted_T_scheme_source_row_count"] == 0, "T rows overaccepted")
    for row in trial["trial_rows"]:
        require(row["accepted_as_selected_L_rowlocal_source_row"] is False, f"L row accepted: {row['omega_id']}")
        require(row["projector_source_verified"] is False, f"projector source oververified: {row['omega_id']}")

    require(threshold["functional_contract_closed"] is True, "threshold contract should be closed")
    require(threshold["selected_threshold_response_functional_instantiated"] is False, "threshold instantiated")
    require(threshold["accepted_T_scheme_source_row_count"] == 0, "T rows overaccepted")

    require(degeneracy["theorem"]["proved"] is True, "degeneracy theorem missing")
    require(degeneracy["required_total_row_count"] == 10, "degeneracy row count mismatch")
    require(degeneracy["selected_projector_values_promoted"] is False, "degeneracy overpromoted projectors")
    require(degeneracy["accepted_source_row_count"] == 0, "degeneracy overaccepted rows")

    for phrase in [
        "Phi_fin selected minimizer trace that promotes finite projectors and zero-mode bases",
        "physical dotD_alpha1 / retarded overlap derivative row kernel",
        "selected threshold scheme values T_scheme.*",
    ]:
        require(phrase in cutset["still_missing"], f"cutset missing {phrase}")
    for phrase in [
        "promote model-active B_N projectors while selected_source_verified is false",
        "use diagnostic prefactor targets to define L_rowlocal or T_scheme",
        "claim scalar no-knob closure from the diagonal HYM solve alone",
    ]:
        require(phrase in cutset["forbidden_routes"], f"forbidden route missing {phrase}")

    decision = data["closure_decision"]
    for key in [
        "overlap_quadrature_functional_defined",
        "diagonal_HYM_Green_imported",
        "finite_model_active_quadrature_trial_executed",
        "current_source_degeneracy_nogo_proved",
        "threshold_scheme_source_gate_built",
    ]:
        require(decision[key] is True, f"decision missing {key}")
        require(cert[key] is True, f"certificate missing {key}")
    for key in [
        "accepted_L_rowlocal_source_row_count",
        "accepted_T_scheme_source_row_count",
        "accepted_rowlocal_source_row_count",
        "accepted_omega_source_row_count",
        "accepted_internal_scalar_value_row_count",
    ]:
        require(decision[key] == 0, f"decision overaccepted {key}")
        require(cert[key] == 0, f"certificate overaccepted {key}")
    for key in [
        "selected_projector_values_promoted",
        "selected_retarded_overlap_derivative_rows_emitted",
        "lambda_H_value_row_emitted",
        "strict_omega_acceptance_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
        require(cert[key] is False, f"certificate overclosed {key}")

    for phrase in [
        "charged basis degenerate            : True",
        "accepted L_rowlocal source rows     : 0",
        "accepted T_scheme source rows       : 0",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
