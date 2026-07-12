"""Audit CONST-HIGGS-01 H7B1A selected two-Higgs metric/projector source."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1a_selected_two_higgs_metric_or_light_projector_source"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
QUOTIENT_IMPORT = BASE / "single_higgs_quotient_map_import.packet.json"
NEARMISS_TRIAGE = BASE / "projector_source_nearmiss_triage.packet.json"
UNDERDETERMINATION = BASE / "quotient_to_projector_underdetermination_proof.packet.json"
SPLITTING_CONTRACT = BASE / "selected_splitting_or_projector_source_contract.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1A_SelectedTwoHiggsMetricOrLightProjectorSource_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1A_QUOTIENT_TO_PROJECTOR_UNDERDETERMINED_SPLITTING_SOURCE_OPEN"


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
    quotient = load(QUOTIENT_IMPORT)
    nearmiss = load(NEARMISS_TRIAGE)
    under = load(UNDERDETERMINATION)
    contract = load(SPLITTING_CONTRACT)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("quotient", quotient),
        ("nearmiss", nearmiss),
        ("underdetermination", under),
        ("contract", contract),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["single_Higgs_quotient_imported"] is True, "quotient imported")
    require(candidate["quotient_to_projector_underdetermination_proved"] is True, "underdetermined")
    require(candidate["selected_metric_on_two_Higgs_plane_found"] is False, "metric overfound")
    require(candidate["selected_rank_one_light_projector_P_L_found"] is False, "P_L overfound")
    require(candidate["selected_splitting_source_found"] is False, "splitting overfound")
    require(candidate["selected_s_beta_value_found"] is False, "s_beta overfound")
    require(candidate["selected_EW_boundary_RG_packet_closed"] is False, "EW overclosed")
    require(candidate["new_Higgs_specific_parameters"] == 0, "new params")
    require(candidate["numeric_lambda_H_derived"] is False, "lambda")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "no-knob")

    q = quotient["q79_low_energy_projection"]["quotient_map_q"]
    require(q["q(H_u)"] == "H", "q Hu")
    require(q["q(H_d^dagger)"] == "H", "q Hd")
    require(q["rank"] == 1, "q rank")
    require(q["kernel_generator"] == "H_u - H_d^dagger", "q kernel")
    classification = quotient["classification"]
    require(classification["is_low_energy_quotient_or_identification"] is True, "classification quotient")
    require(classification["is_selected_Hermitian_projector_on_UV_two_Higgs_plane"] is False, "classification projector")
    require(classification["selects_horizontal_lift_or_splitting"] is False, "classification splitting")
    require(classification["emits_s_beta"] is False, "classification s")

    sources = nearmiss["candidate_sources"]
    require(len(sources) == 5, "nearmiss count")
    for source in sources:
        require(source["accepted_as_H7B1A_source"] is False, f"nearmiss promoted {source['id']}")
    collision = nearmiss["source_name_collision_guardrail"]
    require(collision["P_L_symbol_collision_detected"] is True, "symbol collision")
    require(collision["collision_promoted"] is False, "symbol collision promoted")
    open_fields = nearmiss["open_fields_confirmed"]
    require(open_fields["q79_channel_weights_open"] is True, "q79 channel weights")
    require(open_fields["q79_family_kinetic_metrics_open"] is True, "q79 metrics")
    require(open_fields["weight_protocol_numerical_A_gamma_open"] is True, "A gamma")
    require(open_fields["weight_protocol_family_kinetic_metrics_open"] is True, "protocol metrics")
    require(open_fields["rank_attempt_channel_weights_null"] is True, "rank weights")
    require(open_fields["rank_attempt_family_kinetic_metrics_null"] is True, "rank metrics")

    setup = under["setup"]
    require(setup["quotient_map"] == "q(e_u)=H, q(e_d)=H", "under q")
    require(setup["Dterm_involution"] == "J_D=diag(1,-1)", "under JD")
    require(setup["projector_invariant"] == "s_beta=(Tr(J_D P_L))^2", "under invariant")
    witnesses = under["two_witness_light_lines_same_quotient_different_s_beta"]
    require(witnesses[0]["name"] == "up_axis_line", "witness 0")
    require(witnesses[0]["q_image"] == "H", "witness 0 q")
    require(witnesses[0]["s_beta"] == 1, "witness 0 s")
    require(witnesses[1]["name"] == "diagonal_line", "witness 1")
    require(witnesses[1]["q_image"] == "sqrt(2) H", "witness 1 q")
    require(witnesses[1]["s_beta"] == 0, "witness 1 s")
    family = under["family_statement"]
    require(family["same_low_energy_channel_when"].startswith("c_u+c_d != 0"), "family channel")
    require(family["s_beta"] == "(|c_u|^2-|c_d|^2)^2", "family s")
    require(family["range"] == "0 <= s_beta <= 1", "family range")
    proof = under["proof_result"]
    require(proof["single_Higgs_projection_determines_channel_labels"] is True, "proof labels")
    require(proof["single_Higgs_projection_determines_light_line_projector"] is False, "proof projector")
    require(proof["single_Higgs_projection_determines_s_beta"] is False, "proof s")
    require(proof["selected_metric_or_splitting_required"] is True, "proof splitting")
    require(proof["numeric_lambda_H_derived"] is False, "proof lambda")
    require(proof["strict_no_knob_Higgs_closure"] is False, "proof no-knob")

    accepted = contract["accepted_equivalent_payloads"]
    for key in [
        "selected_horizontal_lift",
        "selected_rank_one_projector",
        "selected_Hermitian_metric_plus_minimal_lift_rule",
        "selected_two_Higgs_mass_or_strain_matrix",
        "direct_selected_s_beta",
    ]:
        require(accepted[key]["filled"] is False, f"accepted payload {key}")
    filled = contract["current_filled_fields"]
    require(filled["quotient_map_q"] is True, "filled q")
    require(filled["Dterm_involution_J_D"] is True, "filled JD")
    require(filled["projector_to_sbeta_functor"] is True, "filled functor")
    eval_ = contract["current_packet_evaluation"]
    for key in [
        "selected_projector_source_found",
        "selected_splitting_source_found",
        "selected_s_beta_emitted",
        "selected_EW_boundary_RG_packet_closed",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(eval_[key] is False, f"eval {key}")
    require("quotient map q alone -> P_L" in contract["forbidden_promotions"], "forbid q")
    require("sector-L projector symbol P_L -> Higgs light-line projector" in contract["forbidden_promotions"], "forbid symbol")
    superset = contract["superset_use"]
    require(superset["straight_way"] == "exact sequence splitting for the UV two-Higgs plane", "straight")
    require(superset["combined_paths_with_locked_target"] is True, "locked")
    require(superset["combined_as_numeric_knobs"] is False, "knobs")

    require("H7B1B-SELECTED-TWO-HIGGS-SPLITTING-SOURCE" in next_work["primary_next"]["label"], "next primary")
    require("H7B2-SELECTED-EW-BOUNDARY-RG-PACKET" in next_work["parallel_next"]["label"], "next parallel")
    require(cert["status"] == STATUS, "cert status")
    require(cert["single_Higgs_quotient_imported"] is True, "cert quotient")
    require(cert["quotient_to_projector_underdetermination_proved"] is True, "cert under")
    require(cert["selected_rank_one_light_projector_P_L_found"] is False, "cert P_L")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert no-knob")
    require("H7B1A-SELECTED-TWO-HIGGS" in note and "Ker(q)=span(H_u-H_d^dagger)" in note, "note")

    print("CONST-HIGGS-01 H7B1A selected two-Higgs metric/projector source audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
