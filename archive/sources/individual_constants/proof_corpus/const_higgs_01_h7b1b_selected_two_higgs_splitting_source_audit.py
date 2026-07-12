"""Audit CONST-HIGGS-01 H7B1B selected two-Higgs splitting source."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1b_selected_two_higgs_splitting_source"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
MASS_STRAIN_BRIDGE = BASE / "two_higgs_mass_strain_to_projector_bridge.packet.json"
SOURCE_TRIAGE = BASE / "source_candidate_triage.packet.json"
SOURCE_CONTRACT = BASE / "selected_mass_strain_or_projector_source_contract.packet.json"
ROUTE_LEDGER = BASE / "positive_route_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1B_SelectedTwoHiggsSplittingSource_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1B_MASS_STRAIN_PROJECTOR_BRIDGE_BUILT_SELECTED_MATRIX_OPEN"


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
    bridge = load(MASS_STRAIN_BRIDGE)
    triage = load(SOURCE_TRIAGE)
    contract = load(SOURCE_CONTRACT)
    ledger = load(ROUTE_LEDGER)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("bridge", bridge),
        ("triage", triage),
        ("contract", contract),
        ("ledger", ledger),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["bridge_from_mass_strain_to_projector_built"] is True, "bridge built")
    require(candidate["source_candidate_triage_built"] is True, "triage built")
    require(candidate["low_energy_H_projector_imported"] is True, "H projector imported")
    require(candidate["selected_UV_two_Higgs_mass_strain_matrix_found"] is False, "matrix overfound")
    require(candidate["selected_Delta_Omega_found"] is False, "Delta/Omega overfound")
    require(candidate["selected_rank_one_light_projector_P_L_found"] is False, "P_L overfound")
    require(candidate["selected_s_beta_value_found"] is False, "s_beta overfound")
    require(candidate["selected_EW_boundary_RG_packet_closed"] is False, "EW overclosed")
    require(candidate["new_Higgs_specific_parameters"] == 0, "new params")
    require(candidate["numeric_lambda_H_derived"] is False, "lambda overderived")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "no-knob overclosed")

    setup = bridge["setup"]
    require(setup["UV_two_Higgs_plane"] == "E_H^UV = span(e_u=H_u, e_d=H_d^dagger)", "bridge plane")
    require(setup["quotient_map"] == "q(e_u)=H, q(e_d)=H", "bridge q")
    require(setup["Dterm_involution"] == "J_D=diag(1,-1)", "bridge JD")
    require(setup["non_scalar_condition"] == "Delta^2 + |Omega|^2 > 0", "bridge non-scalar")
    formula = bridge["s_beta_formula"]
    require(formula["trace_formula"] == "s_beta=(Tr(J_D P_L))^2", "trace formula")
    require(formula["mass_strain_formula"] == "s_beta = Delta^2 / (Delta^2 + |Omega|^2)", "mass formula")
    require(formula["one_ratio_form"] == "with r_H=|Omega|/|Delta|, s_beta=1/(1+r_H^2) when Delta != 0", "ratio")
    require(formula["range"] == "0 <= s_beta <= 1", "range")
    canon = bridge["canonical_projector_formula"]
    require(canon["projector_is_basis_free_after_source_matrix_selected"] is True, "projector canonical")
    require(canon["new_beta_parameter_introduced"] is False, "beta param")
    require("q restricted to im(P_L) must be nonzero" in canon["quotient_admissibility"], "quotient admissible")

    witnesses = {item["id"]: item for item in bridge["exact_witnesses"]}
    require(witnesses["oriented_diagonal_split"]["s_beta"] == 1, "diagonal s")
    require(witnesses["oriented_diagonal_split"]["currently_selected_by_source"] is False, "diagonal selected")
    require(witnesses["balanced_minimal_lift"]["s_beta"] == 0, "balanced s")
    require(witnesses["balanced_minimal_lift"]["Omega"] == -1, "balanced omega")
    require(witnesses["kernel_light_line_rejected"]["s_beta"] == 0, "kernel s")
    require("fails low-energy H acceptance" in witnesses["kernel_light_line_rejected"]["meaning"], "kernel rejected")
    proved = bridge["what_is_proved"]
    require(proved["selected_mass_strain_matrix_would_emit_P_L"] is True, "would emit P")
    require(proved["selected_mass_strain_matrix_would_emit_s_beta"] is True, "would emit s")
    require(proved["selected_source_values_currently_emitted"] is False, "source values overemitted")
    require(proved["numeric_lambda_H_derived"] is False, "bridge lambda")
    require(proved["strict_no_knob_Higgs_closure"] is False, "bridge no-knob")

    sources = triage["candidate_sources"]
    require(len(sources) == 8, "source count")
    for source in sources:
        require(source["accepted_as_selected_UV_two_Higgs_splitting"] is False, f"source promoted {source['id']}")
    summary = triage["summary"]
    require(summary["low_energy_H_projector_found"] is True, "low H found")
    require(summary["UV_two_Higgs_projector_found"] is False, "UV projector overfound")
    require(summary["selected_mass_strain_matrix_found"] is False, "matrix found")
    require(summary["selected_Delta_Omega_found"] is False, "Delta found")
    require(summary["direct_selected_s_beta_found"] is False, "direct s")

    accepted = contract["accepted_equivalent_payloads"]
    for key in [
        "selected_Hermitian_mass_strain_matrix",
        "selected_light_projector",
        "selected_horizontal_lift",
        "direct_selected_s_beta",
    ]:
        require(accepted[key]["filled"] is False, f"accepted payload {key}")
    require(accepted["selected_Hermitian_mass_strain_matrix"]["minimal_values"] == ["Delta", "Re(Omega)", "Im(Omega)"], "minimal matrix values")
    current = contract["current_filled_fields"]
    require(current["single_Higgs_quotient_q"] is True, "filled q")
    require(current["Dterm_projector_functor"] is True, "filled functor")
    require(current["quotient_to_projector_underdetermination"] is True, "filled underdetermination")
    require(current["low_energy_rank_one_H_projector"] is True, "filled low H")
    require(current["mass_strain_to_projector_formula"] is True, "filled bridge")
    for key, value in contract["current_open_fields"].items():
        require(value is True, f"open field not open {key}")
    require("low-energy H rank-one projector -> UV two-Higgs light projector" in contract["forbidden_promotions"], "forbid low H")
    require("external MSSM matching formula -> MTT source value" in contract["forbidden_promotions"], "forbid external")

    routes = {item["label"]: item for item in ledger["routes"]}
    require(routes["H7B1C-SELECTED-TWO-HIGGS-MASS-STRAIN-HESSIAN"]["status"] == "OPEN", "mass route")
    require(routes["H7B1C-BALANCED-MINIMAL-LIFT"]["status"] == "CONDITIONAL_OPEN", "balanced route")
    require(routes["H7B1C-ONE-UNIVERSAL-RATIO-RH"]["status"] == "ALLOWED_ONLY_AS_SHARED_PRIMITIVE_TIER", "primitive route")
    require(routes["H7B2-SELECTED-EW-BOUNDARY-RG-PACKET"]["status"] == "OPEN", "H7B2 route")
    superset = ledger["superset_use"]
    require(superset["straight_way"] == "mass/strain eigenprojector on the UV two-Higgs plane", "straight")
    require(superset["locked_target"] == "selected P_L or selected Delta/Omega on span(H_u,H_d^dagger)", "target")
    require(superset["combined_as_numeric_knobs"] is False, "knobs")

    require("H7B1C-SELECTED-TWO-HIGGS-MASS-STRAIN-HESSIAN" in next_work["primary_next"]["label"], "next primary")
    require("H7B1C-SECTION-RING-HORIZONTAL-LIFT" in next_work["alternate_next"]["label"], "next alternate")
    require("H7B2-SELECTED-EW-BOUNDARY-RG-PACKET" in next_work["parallel_next"]["label"], "next parallel")
    require(cert["status"] == STATUS, "cert status")
    require(cert["bridge_from_mass_strain_to_projector_built"] is True, "cert bridge")
    require(cert["selected_UV_two_Higgs_mass_strain_matrix_found"] is False, "cert matrix")
    require(cert["selected_Delta_Omega_found"] is False, "cert Delta")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert no-knob")
    require("s_beta = (Tr(J_D P_L))^2 = Delta^2 / (Delta^2 + |Omega|^2)" in note, "note formula")
    require("External shape guardrail" in note and "not used as an MTT source selector" in note, "note external guardrail")

    print("CONST-HIGGS-01 H7B1B selected two-Higgs splitting source audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
