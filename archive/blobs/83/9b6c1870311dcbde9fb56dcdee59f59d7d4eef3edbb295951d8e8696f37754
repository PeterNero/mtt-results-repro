"""Audit CONST-GR-01 G3 CUV/Qtau/Omega0 source-data consolidation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_gr_01_absolute_scale_g3_cuv_qtau_omega0_source_data"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
SOURCE_SPLIT = BASE / "source_data_split.packet.json"
CHAR_IMPORT = BASE / "character_channel_internal_ratio.packet.json"
OMEGA_GATE = BASE / "omega0_physical_unit_gate.packet.json"
PROVENANCE = BASE / "strict_provenance_upgrade.packet.json"
BOUNDARY = BASE / "g3_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_GR_01_AbsoluteScale_G3_CUV_Qtau_Omega0_SourceData_v1.md"

STATUS = "MTT_CONST_GR_01_G3_CUV_QTAU_OMEGA0_SOURCE_DATA_BUILT"


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
    source_split = load(SOURCE_SPLIT)
    char_import = load(CHAR_IMPORT)
    omega_gate = load(OMEGA_GATE)
    provenance = load(PROVENANCE)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("source_split", source_split),
        ("char_import", char_import),
        ("omega_gate", omega_gate),
        ("provenance", provenance),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["internal_CUV_Qtau_ratio_accepted_for_shared_scale_data"] is True, "internal ratio")
    require(candidate["physical_unit_gate_reduced_to_Omega0_or_E0_L0"] is True, "physical gate")
    require(candidate["literal_GR_TT_noise_identity_closed"] is False, "literal identity overclosed")
    require(candidate["physical_Omega0_selected"] is False, "Omega0 overclosed")
    require(candidate["measured_Newton_or_Planck_derived"] is False, "Newton overclosed")
    require(candidate["strict_no_knob_absolute_scale_closure"] is False, "strict overclosed")

    split = source_split["split"]
    require(split["internal_ratio_gate"]["status"] == "CLOSED_FOR_SHARED_INTERNAL_SCALE_DATA", "ratio split")
    require(split["internal_ratio_gate"]["conditional_premise"]["required"] is True, "premise")
    require(split["strict_literal_GR_noise_gate"]["status"] == "OPEN_OPTIONAL_STRENGTHENING", "strict split")
    require(split["physical_unit_gate"]["status"] == "ACTIVE_BLOCKER", "physical split")

    require(char_import["status"] == "INTERNAL_QTAU_CUV_RATIO_IMPORTED_OMEGA0_OPEN", "char status")
    data = char_import["internal_selected_data"]
    require(data["selected_character"] == "q_64=15", "q64")
    require(data["D_raw_norm_squared_d_Q"] == 1.0, "d_Q")
    require(data["G_11"] == 1.0, "G11")
    require(data["C_UV_norm_internal"] == 0.405623467693425, "C_UV")
    require(data["rho_UV"] == 0.164530397543639, "rho")
    require(data["s_star"] == 1.464646774701829, "s star")
    require(char_import["still_open"]["physical_Omega_0_selected"] is False, "char physical open")
    require(char_import["guardrails"]["claims_physical_units"] is False, "physical unit guard")

    require(omega_gate["status"] == "OMEGA0_OR_EQUIVALENT_METROLOGY_PRIMITIVE_REMAINS_ACTIVE_GATE", "omega status")
    require(omega_gate["closed_or_reduced"]["chi_omega_convention_closed"] is True, "chi")
    require(omega_gate["closed_or_reduced"]["Omega0_over_sqrt_alpha_phys"] == 1.5675093859261626, "omega factor")
    require(omega_gate["active_formulae"]["Omega0"] == "sqrt(alpha_phys) * sqrt(15/log(448))", "omega formula")
    require(omega_gate["still_open"]["physical_alpha_or_equivalent_inverse_length_unit_selected"] is False, "alpha open")
    require(omega_gate["still_open"]["Omega0_physical_numeric_closed"] is False, "Omega0 numeric")
    require(omega_gate["guardrails"]["claims_physical_Omega0_numeric_closed"] is False, "Omega0 guard")
    require(omega_gate["guardrails"]["declares_one_metrology_primitive_as_no_knob"] is False, "primitive guard")

    upgrades = provenance["open_upgrades"]
    require(provenance["status"] == "STRICT_PROVENANCE_UPGRADES_LABELED_NOT_ACTIVE_PHYSICAL_UNIT_GATE", "provenance status")
    require(upgrades["literal_GR_TT_stochastic_channel_equals_E15"] is False, "literal channel should be open")
    require(upgrades["unconditional_all_covariance_models_closed"] is False, "covariance models")
    require(upgrades["independent_higher_order_functional_evaluation_supplied_here"] is False, "higher-order")
    require(upgrades["selected_finite_memory_covariance_Q_tau_derived"] is False, "Q_tau provenance")

    closed = boundary["closed_or_tightened_now"]
    open_ = boundary["still_open"]
    require(closed["internal_CUV_Qtau_ratio_accepted_for_shared_scale_data"] is True, "boundary ratio")
    require(closed["physical_unit_gate_reduced_to_Omega0_or_E0_L0"] is True, "boundary physical gate")
    require(open_["physical_Omega0_selected"] is True, "Omega0 open boundary")
    require(open_["literal_GR_TT_stochastic_channel_equals_E15"] is True, "literal open boundary")
    require("not promoting internal rho_UV as a physical unit" in boundary["anti_cycle_delta_from_G2"]["not_repeated"], "anti-cycle")

    require(next_work["primary"]["label"] == "CONST-GR-01 / ABSOLUTE-SCALE-GN / G4-OMEGA0-PHYSICAL-UNIT-OR-ONE-METROLOGY-PRIMITIVE", "primary")
    require(next_work["strict_upgrade"]["label"] == "CONST-GR-01 / ABSOLUTE-SCALE-GN / G4B-GR-TT-STOCHASTIC-CHANNEL-E15-IDENTITY", "strict")

    require(cert["status"] == STATUS, "cert status")
    require(cert["internal_CUV_Qtau_ratio_accepted_for_shared_scale_data"] is True, "cert ratio")
    require(cert["physical_unit_gate_reduced_to_Omega0_or_E0_L0"] is True, "cert gate")
    require(cert["physical_Omega0_selected"] is False, "cert Omega0")
    require("G3-CUV-QTAU-OMEGA0" in note and "G4-OMEGA0-PHYSICAL-UNIT" in note, "note")

    print("CONST-GR-01 G3 CUV/Qtau/Omega0 source-data audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
