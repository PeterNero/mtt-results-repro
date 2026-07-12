"""Audit the Higgs-specific M_H acceptance-object frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsspecificmhacceptanceobject_or_valuefrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
MH_OBJECT = PACKET_DIR / "higgs_specific_mh_acceptance_object.packet.json"
VALUE_FRONTIER = PACKET_DIR / "mh_three_real_row_value_frontier.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_mh_acceptance_object.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_mh_acceptance_object.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsSpecificMHAcceptanceObject_or_ValueFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HIGGSSPECIFICMHACCEPTANCEOBJECT_OR_VALUEFRONTIER_"
    "CONTRACT_CLOSED_THREE_REAL_ROWS_OPEN"
)
NEXT = "MTT_Selected_HiggsSpecificMHValueEmission_or_C5C6ProjectionBridge_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    mh_object = load(MH_OBJECT)
    value_frontier = load(VALUE_FRONTIER)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("M_H object", mh_object),
        ("value frontier", value_frontier),
        ("H K gate", hk_gate),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "theorem proved")
    require(cert["theorem_proved"] is True, "cert theorem proved")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")

    decision = data["closure_decision"]
    for key in [
        "B_Huv_two_column_uv_lift_emitted",
        "same_source_functional_alpha1_dotD_side_closed",
        "M_H_acceptance_object_bound_to_B_Huv_domain",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    for key in [
        "M_H_three_real_value_rows_emitted",
        "selected_Delta_row_emitted",
        "selected_Re_Omega_row_emitted",
        "selected_Im_Omega_row_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "direct_Huu_Hud_Hdd_emitted",
        "selected_s_beta_value_found",
        "K_threshold_Omega_H_lambda_emitted",
        "ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K selected count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "K required")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows")

    domain = mh_object["domain"]
    require(domain["name"] == "source-orthonormal B_Huv two-column UV Higgs domain", "domain")
    require(domain["orthonormality"] == "B_Huv^* G_Q B_Huv = I_2", "orthonormality")
    require(domain["ordered_basis"] == ["B_Huv[H_u]", "B_Huv[H_d^dagger]"], "basis")

    form = mh_object["accepted_Herm2_form"]
    require(form["minimal_real_value_rows"] == ["Delta", "Re(Omega)", "Im(Omega)"], "rows")
    require(form["nondegeneracy"] == "Delta^2 + |Omega|^2 > 0", "nondegeneracy")
    require(form["scalar_m0_relevance"].startswith("drops out"), "m0 irrelevance")
    require(form["trace_free_part"][0] == ["Delta", "Omega"], "trace-free first row")
    require(form["trace_free_part"][1] == ["conj(Omega)", "-Delta"], "trace-free second row")

    formulas = mh_object["downstream_formulas"]
    require(formulas["Huu"] == "m0 + Delta", "Huu formula")
    require(formulas["Hud"] == "Omega", "Hud formula")
    require(formulas["Hdd"] == "m0 - Delta", "Hdd formula")
    require(formulas["s_beta"] == "Delta^2/(Delta^2+|Omega|^2)", "s_beta formula")
    for key in ["Delta", "Re_Omega", "Im_Omega", "Huu", "Hud", "Hdd", "P_L", "s_beta"]:
        require(mh_object["not_emitted"][key] is None, f"{key} should not be emitted")

    contract = mh_object["source_contract_alignment"]
    require(contract["now_bound_to_emitted_B_Huv_domain"] is True, "contract bound")
    require(contract["H7B1C_minimal_payload_request_built"] is True, "H7B1C request")
    require(contract["H7B1B_selected_matrix_payload"]["filled"] is False, "H7B1B overfilled")

    payload = value_frontier["exact_value_payload_required"]
    for key in [
        "Delta",
        "Re_Omega",
        "Im_Omega",
        "exactness_or_error_certificate",
        "source_ownership_certificate",
        "nondegeneracy_certificate",
        "light_line_not_kernel_certificate",
    ]:
        require(payload[key] is None, f"value frontier overfilled {key}")
    for phrase in [
        "direct selected Higgs-specific Hessian/mass-strain execution on the B_Huv domain",
        "full same-source M_source plus H-sector restriction R_H",
        "C5-C6 projection-measure/no-boundary bridge that emits the equivalent H K row",
    ]:
        require(phrase in value_frontier["accepted_source_routes"], f"route missing {phrase}")
    for phrase in [
        "promote the diagonal metric Gram matrix as M_H",
        "promote matter/neutrino alpha1/dotD blocks as Huv",
        "use collapsed rank-one H sector values as UV two-Higgs data",
        "backsolve Delta/Omega/s_beta/lambda_H from observed Higgs or threshold data",
    ]:
        require(phrase in value_frontier["forbidden_shortcuts"], f"shortcut guard missing {phrase}")

    h_row = hk_gate["H_row"]
    require(h_row["M_H_acceptance_object_bound_to_B_Huv_domain"] is True, "H row M_H object")
    require(h_row["M_H_three_real_value_rows_emitted"] is False, "H row values overclosed")
    require(h_row["K_threshold_Omega_H_lambda_emitted"] is False, "H K overclosed")
    route = hk_gate["direct_route_state"]
    require(route["M_H_acceptance_object_closed"] is True, "route object")
    require(route["M_H_three_real_value_rows_emitted"] is False, "route values")
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "H K selected count")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "H K required")
    require(hk_gate["conditional_consequent_current"]["accepted_internal_scalar_value_row_count"] == 0, "H scalar rows")

    for phrase in [
        "M_H acceptance object is bound to the emitted B_Huv domain",
        "minimal source value rows are Delta, Re(Omega), Im(Omega)",
        "H K-threshold gate remains 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset missing {phrase}")
    for phrase in [
        "source-owned Delta row",
        "source-owned Re(Omega) row",
        "source-owned Im(Omega) row",
        "K_threshold.Omega_H.lambda source row",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")
    for phrase in [
        "source-owned `Delta`",
        "source-owned `Re(Omega)`",
        "source-owned `Im(Omega)`",
        "selected `K_threshold.Omega_H.lambda`",
    ]:
        require(phrase in note, f"note open missing {phrase}")

    print(
        "AUDIT_PASS: M_H acceptance object is bound to B_Huv; "
        "Delta/ReOmega/ImOmega value rows remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
