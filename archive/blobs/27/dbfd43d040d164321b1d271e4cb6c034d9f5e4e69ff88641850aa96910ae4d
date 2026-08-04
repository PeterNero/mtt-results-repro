"""Audit CONST-HIGGS-01 H7B UV beta or two-Higgs projection theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b_uv_beta_or_two_higgs_projection_theorem"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
EXTERNAL_REF = BASE / "external_susy_eft_boundary_reference.packet.json"
SOURCE_SEARCH = BASE / "selected_route_b_source_search.packet.json"
UNDERDETERMINATION = BASE / "projection_invariant_underdetermination_proof.packet.json"
PAYLOAD_CONTRACT = BASE / "minimal_route_b_payload_contract.packet.json"
NEXT_WORK = BASE / "h7b_decision_and_next_work.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B_UVBetaOrTwoHiggsProjectionTheorem_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B_UV_BETA_ROUTE_UNDERDETERMINED_MINIMAL_PAYLOAD_BUILT"


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
    external = load(EXTERNAL_REF)
    source = load(SOURCE_SEARCH)
    under = load(UNDERDETERMINATION)
    contract = load(PAYLOAD_CONTRACT)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("external", external),
        ("source", source),
        ("underdetermination", under),
        ("contract", contract),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["route_B_minimal_payload_contract_built"] is True, "contract built")
    require(candidate["route_B_projection_invariant_reduction_built"] is True, "invariant reduction")
    require(candidate["current_closed_data_underdetermine_route_B"] is True, "underdetermination")
    require(candidate["selected_Dterm_projection_invariant_s_beta_found"] is False, "s_beta overfound")
    require(candidate["selected_UV_beta_or_tan_beta_found"] is False, "beta overfound")
    require(candidate["selected_EW_boundary_RG_packet_closed"] is False, "EW RG overclosed")
    require(candidate["external_methodology_promoted_to_MTT_source"] is False, "external promoted")
    require(candidate["beta_primitive_declared_now"] is False, "beta primitive")
    require(candidate["new_Higgs_specific_parameters"] == 0, "new params")
    require(candidate["numeric_lambda_H_derived"] is False, "lambda numeric")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "no-knob")

    refs = external["references"]
    require(len(refs) == 2, "external reference count")
    for ref in refs:
        require(ref["value_imported"] is False, "external value imported")
        require(ref["counts_as_MTT_source_selector"] is False, "external selector")
        require(str(ref["url"]).startswith("https://"), "external url")
    guard = external["guardrail_result"]
    require(guard["standard_boundary_formula_supported_as_methodology"] is True, "external methodology")
    require(guard["numeric_lambda_or_beta_imported"] is False, "external numeric")
    require(guard["external_phenomenology_allowed_to_select_MTT_branch"] is False, "external branch")
    require(guard["threshold_and_scheme_policy_required_before_precision_claim"] is True, "external policy")

    support = source["closed_support"]
    require(support["route_A_parked_pending_new_source"] is True, "route A parked")
    require(support["route_B_promoted_as_near_term_primary"] is True, "route B primary")
    require(support["low_energy_single_Higgs_projection_closed"] is True, "single Higgs")
    require(support["H_u_to_H"] is True, "Hu")
    require(support["H_d_to_Hdagger"] is True, "Hd")
    require(support["Dterm_boundary_formula_ready"] is True, "Dterm formula")
    require(support["symbolic_boundary_functor_defined"] is True, "symbolic functor")
    require(support["tree_boundary"] == "lambda = (g^2 + g'^2) * cos^2(2 beta) / 8", "tree boundary")
    neg = source["negative_result"]
    for key in [
        "selected_Dterm_projection_invariant_s_beta_found",
        "selected_UV_beta_or_tan_beta_found",
        "selected_two_Higgs_projection_angle_found",
        "selected_heavy_Higgs_decoupling_angle_found",
        "selected_EW_boundary_RG_packet_closed",
        "external_methodology_promoted_to_MTT_source",
        "beta_primitive_declared_now",
    ]:
        require(neg[key] is False, f"source negative {key}")
    superset = source["superset_strategy"]
    require("s_beta=cos^2(2 beta)" in superset["locked_target"], "locked target")
    require(superset["paths_combined_as_free_parameters"] is False, "free parameter combine")

    fixed = under["fixed_by_current_closed_packets"]
    not_fixed = under["not_fixed_by_current_closed_packets"]
    require(any("single-Higgs" in item for item in fixed), "fixed single Higgs")
    require(any("s_beta=cos^2(2 beta)" in item for item in not_fixed), "not fixed s_beta")
    family = under["countermodel_family"]
    require(family["symbolic_gauge_factor"] == "A_EW=(g_2^2+g_Y^2)/8", "A_EW")
    require(family["free_projection_invariant"] == "s_beta in [0,1]", "s range")
    require(family["family"] == "lambda_s(mu_match)=A_EW(mu_match)*s_beta", "family")
    require(family["preserves_all_current_closed_route_B_data"] is True, "preserves")
    require(family["changes_lambda_boundary_for_distinct_s_beta_when_A_EW_nonzero"] is True, "changes")
    require(family["therefore_unique_lambda_boundary_determined"] is False, "unique overclaimed")
    proof = under["proof_result"]
    require(proof["current_closed_data_underdetermine_route_B"] is True, "proof under")
    require(proof["selected_s_beta_is_minimal_new_Higgs_object"] is True, "minimal")
    require(proof["full_beta_angle_stronger_than_needed"] is True, "beta stronger")
    require(proof["numeric_lambda_H_derived"] is False, "proof lambda")
    require(proof["strict_no_knob_Higgs_closure"] is False, "proof no-knob")

    payload = contract["minimal_payload"]
    require(payload["potential_and_Dterm_convention"]["filled"] is True, "payload convention")
    require(payload["low_energy_single_Higgs_projection"]["filled"] is True, "payload single Higgs")
    require(payload["selected_Dterm_projection_invariant_s_beta"]["filled"] is False, "payload s_beta")
    require(payload["selected_EW_boundary_pair"]["filled"] is False, "payload EW")
    require(payload["selected_matching_scale"]["filled"] is False, "payload scale")
    require(payload["selected_threshold_RG_transport"]["filled"] is False, "payload RG")
    require(payload["selector_guardrail"]["filled"] is True, "payload guardrail")
    eval_ = contract["current_packet_evaluation"]
    require(eval_["route_B_UV_Dterm_beta_passes"] is False, "eval route B")
    require(eval_["minimal_invariant_contract_passes"] is False, "eval minimal")
    require(eval_["one_primitive_declared_now"] is False, "eval primitive")
    require(eval_["numeric_lambda_H_derived"] is False, "eval lambda")
    require(eval_["strict_no_knob_Higgs_closure"] is False, "eval no-knob")
    use = contract["superset_use"]
    require(use["straight_way"] == "D-term boundary route with locked target s_beta", "straight way")
    require(use["combined_paths_with_locked_target"] is True, "locked combine")
    require(use["combined_as_numeric_knobs"] is False, "knob combine")

    decision = next_work["decision"]
    require(decision["route_B_minimal_object"] == "s_beta=cos^2(2 beta)", "decision minimal")
    require(decision["route_B_underdetermined_now"] is True, "decision under")
    require(decision["full_beta_angle_required"] is False, "decision beta")
    require(decision["selected_projection_invariant_required"] is True, "decision s")
    require(decision["EW_boundary_RG_required"] is True, "decision EW")
    require("H7B1-SELECTED-DTERM-PROJECTION-INVARIANT-SOURCE" in next_work["primary_next"]["label"], "next H7B1")
    require("H7B2-SELECTED-EW-BOUNDARY-RG-PACKET" in next_work["parallel_next"]["label"], "next H7B2")
    require("H7P-SHARED-PRIMITIVE-HIGGS-REPLAY" in next_work["portfolio_fallback"]["label"], "next H7P")

    require(cert["status"] == STATUS, "cert status")
    require(cert["route_B_minimal_payload_contract_built"] is True, "cert contract")
    require(cert["current_closed_data_underdetermine_route_B"] is True, "cert under")
    require(cert["selected_Dterm_projection_invariant_s_beta_found"] is False, "cert s")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert no-knob")
    require("H7B-UV-BETA" in note and "s_beta = cos^2(2 beta)" in note, "note")

    print("CONST-HIGGS-01 H7B UV beta / two-Higgs projection audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
