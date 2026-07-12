"""Audit same-source boundary/residual emission or unpatched Galerkin replacement."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RESIDUAL_VALUES = PACKET_DIR / "canonical_residual_operator_values.packet.json"
SOURCE_STATUS = PACKET_DIR / "same_source_physical_emission_status.packet.json"
GALERKIN_ROUTE = PACKET_DIR / "unpatched_galerkin_replacement_status.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SameSourceBoundaryResidualEmission_or_UnpatchedGalerkinReplacement_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement.py"

STATUS = "MTT_SELECTED_SAMESOURCE_BOUNDARYRESIDUALEMISSION_BUILT_RESIDUAL_VALUES_PHYSICAL_SOURCE_OPEN"
NEXT = "MTT_Selected_PhysicalActionRestrictionEmission_or_IndependentGalerkinRows_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    residual = load(RESIDUAL_VALUES)
    source = load(SOURCE_STATUS)
    galerkin = load(GALERKIN_ROUTE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("closes the algebraic residual-value search" in note, "note misses algebraic closure")
    require("not physical unpatched dynamic C1 closure" in note, "note misses physical guardrail")

    require(residual["source_level_weyl_carrier_selected"] is True, "Weyl carrier missing")
    require(residual["static_source_selector_selected"] is True, "static selector missing")
    require(residual["active_shift_selected"] is True, "active shift missing")
    require(residual["trace_frobenius_transfer_normalization_selected"] is True, "trace normalization missing")
    require(residual["mathematical_residual_values_ready"] is True, "residual values not ready")
    require(residual["physical_same_source_emission_claimed"] is False, "physical residual overclaimed")

    rz = residual["R_Z"]
    rx = residual["R_X"]
    require(rz["coefficient_count"] == 6, "R_Z coefficient count mismatch")
    require(rx["coefficient_count"] == 3, "R_X coefficient count mismatch")
    require(abs(rz["norm_sq"] - 4.0) < 1e-12, "R_Z norm mismatch")
    require(abs(rx["norm_sq"] - 2.0) < 1e-12, "R_X norm mismatch")
    require(rz["reconstruction_error_norm_sq"] < 1e-24, "R_Z reconstruction too large")
    require(rx["reconstruction_error_norm_sq"] < 1e-24, "R_X reconstruction too large")
    require(rz["projector_replay_residual_matches_norm_sq"] < 1e-24, "R_Z projector replay mismatch")
    require(rx["projector_replay_residual_matches_norm_sq"] < 1e-24, "R_X projector replay mismatch")

    checks = residual["canonical_projector_checks"]
    require(checks["fixed_projector_rank"] == 3, "fixed projector rank mismatch")
    require(checks["residual_projector_rank"] == 6, "residual projector rank mismatch")
    require(checks["fixed_projector_idempotence_norm_sq"] == 0.0, "fixed projector not idempotent")
    require(checks["residual_projector_idempotence_norm_sq"] < 1e-24, "residual projector not idempotent")

    for item in [
        "physical Phi_fin^C1/action restriction",
        "zero extra boundary/source term",
        "physical R_Z emission",
        "physical R_X emission",
        "physical b_selected emission",
    ]:
        require(item in source["not_yet_same_source_physical_emissions"], f"missing open physical item: {item}")
    b = source["b_selected_replay"]
    require(b["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A replay mismatch")
    require(b["A_transpose_b"] == [12.0, 12.0], "b replay mismatch")
    require(b["deltaTheta_C1"] == [1.0, 1.0], "delta replay mismatch")
    require(b["same_source_emitted"] is False, "same-source b overemitted")
    require(b["replay_available_under_axiom_patch"] is True, "b replay unavailable")

    if_source = source["if_same_source_physical_emission_supplied"]
    require(if_source["unpatched_SM_parity_dynamic_packet_closed"] is True, "if-source closure implication missing")
    require(if_source["physical_A_selected"] == [[12.0, 0.0], [0.0, 12.0]], "if-source A mismatch")
    require(if_source["physical_b_selected"] == [12.0, 12.0], "if-source b mismatch")

    require(galerkin["status"] == "ROUTE_B_INDEPENDENT_GALERKIN_REPLACEMENT_VALUES_OPEN", "route B status mismatch")
    require(galerkin["current_route_state"]["route_B_closes_now"] is False, "route B overclosed")
    for item in [
        "zero_mode_bases",
        "primitive_three_by_three_contraction_terms",
        "linear_response_matrices",
        "C33/nonzero-family-rank tests",
    ]:
        require(item in galerkin["required_outputs"], f"route B output missing: {item}")

    closure = data["closure_decision"]
    require(closure["canonical_residual_values_emitted"] is True, "residual values not closed")
    require(closure["physical_same_source_residual_emission"] is False, "physical residual overclaimed")
    require(closure["physical_same_source_b_selected_emission"] is False, "physical b overclaimed")
    require(closure["independent_selected_Galerkin_replacement"] is False, "Galerkin overclaimed")
    require(closure["unpatched_A_selected_emitted"] is False, "unpatched A overclaimed")
    require(closure["unpatched_b_selected_emitted"] is False, "unpatched b overclaimed")
    require(closure["unpatched_deltaTheta_C1_emitted"] is False, "unpatched delta overclaimed")
    require(closure["unpatched_dynamic_C1_packet_closed"] is False, "unpatched closure overclaimed")
    require(closure["true_SM_equivalence_closed"] is False, "true SM overclaimed")
    require(closure["no_knob_closed"] is False, "no-knob overclaimed")

    for label, payload in [
        ("candidate", data),
        ("residual", residual),
        ("source", source),
        ("galerkin", galerkin),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
