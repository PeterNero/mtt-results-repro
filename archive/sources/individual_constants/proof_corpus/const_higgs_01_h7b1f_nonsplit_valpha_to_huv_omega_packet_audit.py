"""Audit CONST-HIGGS-01 H7B1F non-split V_alpha to Huv/Omega packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
REDUCTION_CONTRACT = BASE / "nonsplit_to_huv_reduction_contract.packet.json"
CURRENT_PACKET_AUDIT = BASE / "current_packet_value_audit.packet.json"
FUNCTOR_THEOREM = BASE / "basis_invariant_huv_functor_theorem.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1F_NonSplitVAlphaToHuvOmegaPacket_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1F_NONSPLIT_TO_HUV_REDUCTION_CONTRACT_BUILT_VALUES_OPEN"


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
    contract = load(REDUCTION_CONTRACT)
    current = load(CURRENT_PACKET_AUDIT)
    functor = load(FUNCTOR_THEOREM)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("contract", contract),
        ("current", current),
        ("functor", functor),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["reduction_contract_built"] is True, "contract built")
    require(candidate["basis_invariant_Huv_functor_proved"] is True, "functor proved")
    require(candidate["rank2_valpha_model_selected"] is True, "rank2 support")
    require(candidate["terminal_L_L2_source_closed"] is True, "L source")
    require(candidate["nonzero_ext_class_selected"] is True, "Ext support")
    require(candidate["selected_source_identity_closed"] is False, "source identity overclosed")
    for key in [
        "selected_Huv_basis_binding_found",
        "selected_Higgs_lift_B_Huv_found",
        "selected_Hermitian_M_source_found",
        "selected_finite_Huv_reduction_found",
        "selected_offdiagonal_Omega_found",
        "selected_Huu_Hud_Hdd_found",
        "selected_Delta_Omega_found",
        "selected_s_beta_value_found",
        "selected_EW_boundary_RG_packet_closed",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(candidate[key] is False, f"candidate overclosed {key}")
    require(candidate["new_Higgs_specific_parameters"] == 0, "new params")

    required = contract["required_payload"]
    require("B_Huv" in required["B_Huv"], "B_Huv required")
    require("M_source" in required["M_source"], "M_source required")
    computed_when = contract["computed_packet_when_filled"]
    require(computed_when["Huv"] == "B_Huv^* M_source B_Huv", "Huv formula")
    require(computed_when["Omega"] == "Hud", "Omega formula")
    require(computed_when["s_beta"] == "Delta^2/(Delta^2+|Omega|^2)", "s formula")
    invariance = contract["basis_invariance_requirement"]
    require("leaves Huv invariant" in invariance["source_unitary_change"], "source invariance")
    require(contract["current_packet_passes"] is False, "contract passes")

    missing = current["missing_for_reduction"]
    require(missing["selected_source_identity"] is False, "missing selected source")
    require(missing["source_certificate"] is None, "source certificate")
    for key in [
        "pic0_selected_or_quotiented",
        "non_split_stability_or_hym_proved",
        "hym_strominger_or_routec_residual_pass",
        "typed_transition_or_rhoE_data_emitted",
        "sector_D_E_packets_pass",
        "reduced_green_packets_pass",
        "dotD_packets_pass",
        "primitive_C1_or_Yukawa_contractions",
        "Higgs_slot_projection_B_Huv_emitted",
        "Hermitian_mass_strain_M_source_emitted",
    ]:
        require(missing[key] is False, f"missing field overclosed {key}")
    extraction = current["external_operator_extraction_contract"]
    require(extraction["selected_operator_values_closed"] is False, "operator values")
    require(extraction["actual_extraction_theorem_supplied"] is False, "extraction theorem")
    require(extraction["actual_visible_operator_payload_emitted"] is False, "payload emitted")
    e6 = current["e6_higgs_slot_support"]
    require(e6["slots"]["5_H"] == "H_u + color triplet", "5H")
    require(e6["slots"]["bar5_H"] == "H_d + color antitriplet", "bar5H")
    require(e6["physical_light_higgs_doublet_selection_open"] is True, "light Higgs open")
    conclusion = current["conclusion"]
    for key in [
        "selected_Huv_basis_binding_found",
        "selected_finite_Huv_reduction_found",
        "selected_offdiagonal_Omega_found",
        "selected_Huu_Hud_Hdd_found",
        "selected_s_beta_value_found",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(conclusion[key] is False, f"conclusion overclosed {key}")

    require(functor["status"] == "BASIS_INVARIANT_HUV_REDUCTION_FUNCTOR_PROVED_CONDITIONAL_VALUES_OPEN", "functor status")
    require(functor["theorem"]["proved"] is True, "functor theorem")
    require(len(functor["proof_steps"]) == 4, "proof step count")
    require(functor["conditional_values_open"] is True, "conditional open")

    require("H7B1G-FILL-BHUV-OR-MSOURCE" in next_work["primary_next"]["label"], "next primary")
    require("H7B2-SELECTED-EW-BOUNDARY-RG-PACKET" in next_work["parallel_next"]["label"], "next parallel")
    require(cert["status"] == STATUS, "cert status")
    require(cert["reduction_contract_built"] is True, "cert contract")
    require(cert["basis_invariant_Huv_functor_proved"] is True, "cert functor")
    require(cert["selected_Higgs_lift_B_Huv_found"] is False, "cert B")
    require(cert["selected_Hermitian_M_source_found"] is False, "cert M")
    require(cert["selected_offdiagonal_Omega_found"] is False, "cert Omega")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require("H_uv = B_Huv^* M_source B_Huv" in note, "note formula")
    require("do\nnot emit `B_Huv` or `M_source`" in note, "note guardrail")

    print("CONST-HIGGS-01 H7B1F non-split V_alpha to Huv/Omega packet audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
