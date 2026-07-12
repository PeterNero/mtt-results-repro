"""Audit CONST-HIGGS-01 H7B1I M_source from selected response prefix."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1i_msource_from_selected_response_prefix"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
PREFIX = BASE / "selected_response_prefix_import.packet.json"
FUNCTOR = BASE / "msource_acceptance_functor.packet.json"
CURRENT = BASE / "current_msource_export_attempt.packet.json"
OBSTRUCTION = BASE / "dynamic_hessian_obstruction_theorem.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1I_MSourceFromSelectedResponsePrefix_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1I_MSOURCE_RESPONSE_PREFIX_CONTRACT_BUILT_VALUE_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def all_true(packet: dict[str, object], name: str) -> None:
    for key, value in packet.items():
        require(value is True, f"{name} missing true field {key}")


def all_none(packet: dict[str, object], name: str) -> None:
    for key, value in packet.items():
        require(value is None, f"{name} emitted value {key}")


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
    prefix = load(PREFIX)
    functor = load(FUNCTOR)
    current = load(CURRENT)
    obstruction = load(OBSTRUCTION)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("prefix", prefix),
        ("functor", functor),
        ("current", current),
        ("obstruction", obstruction),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["H7B1G_contract_imported"] is True, "H7B1G import")
    require(candidate["H7B1H_msource_first_route_imported"] is True, "H7B1H route import")
    require(candidate["selected_response_prefix_imported"] is True, "response prefix import")
    require(candidate["selected_DE_gap_Riesz_Green_layer_closed"] is True, "DE gap layer")
    require(candidate["H_sector_rank_two_zero_cluster_support_imported"] is True, "H support")
    require(candidate["M_source_acceptance_functor_built"] is True, "functor built")
    require(candidate["dynamic_hessian_obstruction_proved"] is True, "obstruction")
    for key in [
        "M_source_value_emitted",
        "B_Huv_value_emitted",
        "selected_finite_Huv_reduction_found",
        "selected_offdiagonal_Omega_found",
        "selected_s_beta_value_found",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(candidate[key] is False, f"candidate overclosed {key}")
    require(candidate["new_Higgs_specific_parameters"] == 0, "candidate new params")
    require(
        candidate["selected_next_artifact"] == "MTT_CONST_HIGGS_01_H7B1J_DynamicHessianOrHSectorRestrictionExport_v1",
        "candidate next artifact",
    )

    require(prefix["status"] == "SELECTED_RESPONSE_PREFIX_IMPORTED_DYNAMIC_MSOURCE_OPEN", "prefix status")
    static = prefix["selected_static_prefix"]
    branch = static["branch"]
    require(branch["q"] == 79, "branch q")
    require(branch["orientation"] == "F", "branch orientation")
    require(branch["torsion_label_m"] == 1, "branch torsion")
    require(static["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3", "basis id")
    require(static["basis_dimension"] == 27, "basis dim")
    require(static["selected_eta_N"] == 1.0, "eta")
    require(static["selected_gap_lower_bound"] == 2.386490844928603, "gap")
    require(static["selected_green_norm_bound"] == 0.4190252822989217, "green")
    require(static["zero_cluster_indices"] == [12, 13, 14], "zero cluster")
    require("rank-two projector on indices 13,14" in static["H_sector_trace_identity"], "H trace")
    require(static["transition_slot_closed"] is True, "transition slot")
    require(static["source_value_emitted_for_DE_gap_layer"] is True, "DE source emitted")
    dynamic = prefix["dynamic_parts_still_open"]
    require(dynamic["selected_dotD_alpha1_source_identity_closed"] is False, "dotD should remain open")
    require(dynamic["actual_dynamic_QaSU3_operator_packet_closed"] is False, "Qa/SU3 should remain open")
    require(dynamic["full_S2_value_emission_closed"] is False, "S2 should remain open")
    require(dynamic["determinant_torsion_slot_closed"] is False, "torsion should remain open")
    require(dynamic["finite_determinant_heat_spectrum_or_torsion_response"] is True, "heat/torsion open")
    require(dynamic["primitive_C1_response"] is True, "C1 open")
    require(dynamic["A_selected_and_b_selected"] is True, "A/b open")
    require(prefix["value_emitted"] is False, "prefix value")

    require(functor["status"] == "MSOURCE_ACCEPTANCE_FUNCTOR_BUILT_VALUES_OPEN", "functor status")
    space = functor["finite_source_space"]
    require(space["same_source_required"] is True, "same source")
    require(space["basis_dimension"] == 27, "functor dim")
    construction = functor["formal_construction_when_payload_exists"]
    require("M_source =" in construction["Hermitian_projection"], "M formula")
    require("H_uv =" in construction["Huv_link"], "Huv formula")
    require(len(functor["acceptance_requirements"]) == 7, "acceptance requirement count")
    supplies = functor["what_current_prefix_supplies"]
    require(supplies["selected_DE_gap_Riesz_Green_layer"] is True, "supplies DE")
    require(supplies["selected_trace_equality_for_27mode_DE"] is True, "supplies trace")
    require("rank-two projector on indices 13,14" in supplies["H_sector_rank_two_zero_cluster_support"], "supplies H")
    require(supplies["selected_green_norm_bound"] == 0.4190252822989217, "supplies green")
    require(supplies["same_basis_dotD_value_matrices_available_as_support"] is True, "supplies dotD support")
    all_true(functor["what_current_prefix_does_not_supply"], "functor missing")
    require(functor["M_source_value_emitted"] is False, "functor value")

    require(current["status"] == "CURRENT_MSOURCE_EXPORT_ATTEMPT_BLOCKED_BY_DYNAMIC_HESSIAN_AND_RESTRICTION", "current status")
    attempted = current["attempted_export"]
    require(attempted["available_prefix_is_sufficient_for_contract"] is True, "contract sufficiency")
    require(attempted["available_prefix_is_sufficient_for_values"] is False, "value sufficiency")
    all_true(current["strict_missing_fields"], "strict missing")
    all_none(current["computed_values"], "computed values")
    require(current["new_Higgs_specific_parameters"] == 0, "current params")

    require(obstruction["status"] == "DYNAMIC_HESSIAN_OBSTRUCTION_PROVED_MSOURCE_VALUE_OPEN", "obstruction status")
    require(obstruction["theorem"]["name"] == "H7B1IDynamicHessianNotImpliedByTraceGapTheorem", "obstruction theorem")
    require(obstruction["theorem"]["proved"] is True, "obstruction proof")
    require(len(obstruction["proof_steps"]) == 5, "proof step count")
    all_true(obstruction["countermodel_boundary"], "countermodel")

    require(next_work["status"] == "NEXT_WORKORDER_H7B1J_DYNAMIC_HESSIAN_OR_HSECTOR_RESTRICTION_EXPORT", "next status")
    require(next_work["primary_next"]["label"].endswith("H7B1J-DYNAMIC-HESSIAN-OR-HSECTOR-RESTRICTION-EXPORT"), "next label")
    require(len(next_work["two_subroutes"]) == 2, "subroute count")
    require(len(next_work["do_not_repeat"]) == 3, "guardrail count")

    require(cert["status"] == STATUS, "cert status")
    require(cert["selected_response_prefix_imported"] is True, "cert prefix")
    require(cert["M_source_acceptance_functor_built"] is True, "cert functor")
    require(cert["dynamic_hessian_obstruction_proved"] is True, "cert obstruction")
    require(cert["M_source_value_emitted"] is False, "cert M")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")
    require("M_source acceptance functor built          True" in note, "note functor")
    require("M_source value emitted                     False" in note, "note value")
    require("H7B1J-DYNAMIC-HESSIAN-OR-HSECTOR-RESTRICTION-EXPORT" in note, "note next")

    print("CONST-HIGGS-01 H7B1I M_source response-prefix audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
