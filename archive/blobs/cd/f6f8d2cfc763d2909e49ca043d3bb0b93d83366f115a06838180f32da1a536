"""Audit CONST-HIGGS-01 H7B1C selected two-Higgs mass/strain Hessian."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1c_selected_two_higgs_mass_strain_hessian"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
HESSIAN_SEARCH = BASE / "hessian_source_search.packet.json"
MINIMAL_PAYLOAD = BASE / "minimal_two_by_two_hessian_payload_request.packet.json"
INSUFFICIENCY = BASE / "current_source_insufficiency_proof.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1C_SelectedTwoHiggsMassStrainHessian_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1C_HESSIAN_SOURCE_REQUEST_BUILT_VALUES_OPEN"


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
    search = load(HESSIAN_SEARCH)
    minimal = load(MINIMAL_PAYLOAD)
    insuff = load(INSUFFICIENCY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("search", search),
        ("minimal", minimal),
        ("insufficiency", insuff),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["minimal_Huv_hessian_payload_request_built"] is True, "payload request")
    require(candidate["hessian_source_search_executed"] is True, "search executed")
    require(candidate["current_source_insufficiency_proved"] is True, "insufficiency")
    for key in [
        "selected_Huv_basis_labels_found",
        "selected_Huu_Hud_Hdd_found",
        "selected_Delta_Omega_found",
        "selected_rank_one_light_projector_P_L_found",
        "selected_s_beta_value_found",
        "selected_EW_boundary_RG_packet_closed",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(candidate[key] is False, f"candidate overclosed {key}")
    require(candidate["new_Higgs_specific_parameters"] == 0, "new params")

    require(search["status"] == "HESSIAN_LANES_SEARCHED_SELECTED_TWO_BY_TWO_HIGGS_BLOCK_NOT_FOUND", "search status")
    lanes = search["searched_lanes"]
    require(len(lanes) == 8, "lane count")
    for lane in lanes:
        require(lane["emits_Huv_2x2_block"] is False, f"lane overemits {lane['id']}")
    result = search["result"]
    for key in [
        "selected_Huv_basis_labels_found",
        "selected_Huu_Hud_Hdd_found",
        "selected_Delta_Omega_found",
        "selected_P_L_found",
        "selected_s_beta_found",
    ]:
        require(result[key] is False, f"search result overclosed {key}")

    source_identity = minimal["source_identity_required"]
    require(source_identity["selected_source_verified"] is False, "source verified overclosed")
    require(source_identity["no_observed_or_benchmark_selector"] is True, "selector guardrail")
    basis = minimal["basis_required"]
    require(basis["ordered_basis"] == ["H_u", "H_d^dagger"], "basis")
    require(basis["basis_source_ids"] is None, "basis source ids")
    require(basis["basis_labels_currently_emitted"] is False, "basis labels emitted")
    matrix = minimal["matrix_required"]
    require(matrix["Huu"] is None and matrix["Hud"] is None and matrix["Hdd"] is None, "matrix values emitted")
    require(matrix["Delta_formula"] == "Delta=(Huu-Hdd)/2", "Delta formula")
    require(matrix["Omega_formula"] == "Omega=Hud", "Omega formula")
    require(matrix["values_currently_emitted"] is False, "values emitted")
    tests = minimal["acceptance_tests"]
    require(tests["non_scalar"] == "Delta^2+|Omega|^2>0", "non scalar")
    require("q restricted to im(P_L) is nonzero" in tests["quotient_admissible_light_line"], "q admissible")
    require("not chosen from measured lambda_H" in tests["no_target_fit"], "no target fit")
    computed_when = minimal["computed_when_filled"]
    require(computed_when["s_beta"] == "Delta^2/(Delta^2+|Omega|^2)", "computed s")
    require(minimal["current_packet_passes"] is False, "packet passes")

    require(insuff["status"] == "CURRENT_HESSIAN_LIKE_SOURCES_FACTOR_THROUGH_COLLAPSED_H_OR_OTHER_SECTORS", "insuff status")
    require(len(insuff["proof_steps"]) == 6, "proof steps")
    counter = insuff["countermodel_family_still_allowed"]
    require(counter["preserves_current_closed_low_energy_data"] is True, "counter preserves")
    require(counter["changes_s_beta"] == "s_beta=Delta^2/(Delta^2+|Omega|^2)", "counter changes")
    conclusion = insuff["conclusion"]
    require(conclusion["current_sources_emit_Huv_2x2"] is False, "insuff Huv")
    require(conclusion["current_sources_emit_s_beta"] is False, "insuff s")
    require(conclusion["strict_no_knob_Higgs_closure"] is False, "insuff closure")

    require("H7B1D-FILL-HUV-HESSIAN-PAYLOAD" in next_work["primary_next"]["label"], "next primary")
    require("H7B1D-SELECTED-HORIZONTAL-LIFT-THEOREM" in next_work["alternate_next"]["label"], "next alternate")
    require("H7B2-SELECTED-EW-BOUNDARY-RG-PACKET" in next_work["parallel_next"]["label"], "next parallel")
    require(cert["status"] == STATUS, "cert status")
    require(cert["minimal_Huv_hessian_payload_request_built"] is True, "cert request")
    require(cert["current_source_insufficiency_proved"] is True, "cert insuff")
    require(cert["selected_Huu_Hud_Hdd_found"] is False, "cert matrix")
    require(cert["selected_Delta_Omega_found"] is False, "cert Delta")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert no-knob")
    require("minimal H_uv Hessian payload request" in note, "note title")
    require("H_uv:   [[Huu, Hud], [conj(Hud), Hdd]]" in note, "note payload")

    print("CONST-HIGGS-01 H7B1C selected two-Higgs mass/strain Hessian audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
