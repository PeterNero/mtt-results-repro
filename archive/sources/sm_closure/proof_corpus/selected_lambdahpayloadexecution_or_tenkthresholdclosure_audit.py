"""Audit selected lambda_H payload execution or ten-K threshold closure gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_lambdahpayloadexecution_or_tenkthresholdclosure"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTES = PACKET_DIR / "h_lambda_payload_route_evaluation.packet.json"
ANTECEDENT = PACKET_DIR / "h_sector_kthreshold_antecedent_recheck.packet.json"
MINIMAL = PACKET_DIR / "minimal_h_lambda_payload_theorem.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_h_lambda_route_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_LambdaHPayloadExecution_or_TenKThresholdClosure_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_LAMBDAHPAYLOADEXECUTION_OR_TENKTHRESHOLDCLOSURE_"
    "BUILT_H_PAYLOAD_ROUTES_REJECTED_TEN_K_9_OF_10"
)
NEXT = "MTT_Selected_HSectorQuarticThresholdPayload_or_StrictTenKClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")
    require(packet.get("closure_claimed") is True, f"{label} should close its local route/gate theorem")


def route_by_id(routes: dict, route_id: str) -> dict:
    for route in routes["routes"]:
        if route["route_id"] == route_id:
            return route
    raise AssertionError(f"missing route {route_id}")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    routes = load(ROUTES)
    antecedent = load(ANTECEDENT)
    minimal = load(MINIMAL)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("routes", routes),
        ("antecedent", antecedent),
        ("minimal theorem", minimal),
        ("cutset", cutset),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaim")

    decision = data["closure_decision"]
    require(decision["charged_K_rows_preserved"] is True, "charged K rows not preserved")
    require(decision["accepted_selected_charged_K_threshold_row_count"] == 9, "charged K count mismatch")
    require(decision["accepted_selected_K_source_row_count"] == 9, "selected K count mismatch")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K count mismatch")
    require(decision["selected_lambda_H_payload_emitted"] is False, "lambda payload overemitted")
    require(decision["selected_H_K_threshold_row_emitted"] is False, "H K overemitted")
    require(decision["ten_K_antecedent_satisfied"] is False, "ten-K antecedent overclosed")
    require(decision["strict_Omega_lambda_scalar_execution_closed"] is False, "strict scalar execution overclosed")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(decision["true_SM_equivalence_closed"] is False, "true SM closure overclaimed")
    require(decision["full_no_knob_closed"] is False, "full no-knob closure overclaimed")

    require(routes["status"] == "H_LAMBDA_PAYLOAD_ROUTES_EVALUATED_NO_SELECTED_PAYLOAD", "routes status")
    require(routes["omega_id"] == "Omega_H.lambda", "routes omega mismatch")
    require(routes["combined_kernel_row_id"] == "K_threshold.Omega_H.lambda", "routes K id mismatch")
    require(routes["accepted_selected_lambda_H_payload"] is False, "routes lambda overaccepted")
    require(routes["lambda_H_value_row_emitted"] is False, "routes lambda value emitted")
    require(routes["selected_H_K_threshold_row_emitted"] is False, "routes H K emitted")

    rank_route = route_by_id(routes, "rank_one_H_projector_quartic_shortcut")
    rank_support = rank_route["closed_support"]
    require(rank_support["selected_H_projector_source_verified"] is True, "H projector source not verified")
    require(rank_support["H_projector_rank"] == 1, "H projector rank mismatch")
    require(rank_support["H_transport_identity"] is True, "H transport identity lost")
    require(rank_support["H_stationary_rho_s_promoted"] is True, "H rho_s not promoted")
    require(rank_route["accepted_as_lambda_H_payload"] is False, "rank route overaccepted")
    require("does not emit a selected quartic functional" in rank_route["reason_rejected"], "rank rejection missing")

    heat_route = route_by_id(routes, "heat_torsion_shared_circle_payload")
    heat_support = heat_route["closed_support"]
    require(heat_support["D_fin_H_selected"] is True, "D_fin.H not selected")
    require(heat_support["D_fin_H_subfactor_id"] == "D_fin.H", "D_fin.H id mismatch")
    require(heat_support["H_theta_exponent_selected"] is True, "H theta exponent not selected")
    require(heat_support["H_theta_exponent"] == "1/3", "H theta exponent mismatch")
    require(heat_support["prefactor_factorization_row_accepted"] is True, "H factorization row missing")
    require(heat_support["heat_torsion_alone_emits_all_prefactor_rows"] is False, "heat shortcut overproved")
    require(heat_route["accepted_as_lambda_H_payload"] is False, "heat route overaccepted")
    require("cannot emit full row-local prefactors" in heat_route["reason_rejected"], "heat rejection missing")

    replay_route = route_by_id(routes, "external_top_higgs_formula_map_replay")
    replay_support = replay_route["closed_support"]
    require(replay_support["top_higgs_external_formula_map_import_closed"] is True, "external formula import missing")
    require(replay_support["lambda_Mt_external_formula_map_row_closed"] is True, "external lambda row missing")
    require(replay_support["same_branch_Rtheta_threshold_derivation_closed"] is False, "Rtheta threshold overclosed")
    require(replay_route["accepted_as_lambda_H_payload"] is False, "external replay overaccepted")
    require("not a same-branch selected H-sector source row" in replay_route["reason_rejected"], "replay rejection")

    anchor_route = route_by_id(routes, "candidate_specific_universal_anchor")
    require(anchor_route["closed_support"]["universal_anchor_policy_available"] is True, "anchor policy missing")
    require(anchor_route["closed_support"]["selected_H_anchor_emitted_here"] is False, "H anchor overemitted")
    require(anchor_route["accepted_as_lambda_H_payload"] is False, "anchor route overaccepted")

    for phrase in [
        "do not set L_rowlocal.Omega_H.lambda=1 from rank alone",
        "do not promote D_fin.H or theta exponent 1/3 into a quartic value payload",
        "do not use external lambda_H replay as a no-knob selector",
    ]:
        require(phrase in routes["guardrails"], f"guardrail missing {phrase}")

    require(antecedent["status"] == "TEN_K_ANTECEDENT_RECHECKED_PRESENT_9_REQUIRED_10", "antecedent status")
    require(antecedent["accepted_selected_charged_K_threshold_row_count"] == 9, "antecedent charged count")
    require(antecedent["accepted_selected_K_source_row_count"] == 9, "antecedent selected K count")
    require(antecedent["selected_K_threshold_row_count_required"] == 10, "antecedent required count")
    require(antecedent["antecedent_satisfied"] is False, "antecedent overclosed")
    h_row = antecedent["H_row"]
    require(h_row["omega_id"] == "Omega_H.lambda", "H omega mismatch")
    require(h_row["combined_kernel_row_id"] == "K_threshold.Omega_H.lambda", "H K id mismatch")
    require(h_row["selected_lambda_H_payload_emitted"] is False, "H lambda overemitted")
    require(h_row["selected_H_K_threshold_row_emitted"] is False, "H K overemitted")
    require(h_row["H_sector_Lrowlocal_available"] is False, "H L overemitted")
    require(h_row["T_scheme_Omega_H_lambda_source_row_emitted"] is False, "H T overemitted")
    for phrase in [
        "the charged zero-delta route cannot supply the H/lambda row",
        "post-null-delta charged closure supplies 9/10 K rows but does not supply the H row",
        "all current H routes are support-only or replay-only",
    ]:
        require(phrase in h_row["blocking_reasons"], f"H blocker missing {phrase}")
    current = antecedent["conditional_consequent_current"]
    require(current["strict_Omega_rows_executable"] is False, "Omega overclosed")
    require(current["lambda_H_row_executable"] is False, "lambda row executable overclaimed")
    require(current["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")

    require(minimal["status"] == "MINIMAL_H_LAMBDA_PAYLOAD_THEOREM_SHARPENED", "minimal status")
    require("directly emits K_threshold.Omega_H.lambda" in minimal["statement"], "minimal direct K route missing")
    for phrase in [
        "rank-one selected H projector/carrier",
        "D_fin.H finite heat/torsion subsource",
        "shared-circle theta exponent 1/3",
        "selected H-sector quartic functional",
        "selected H threshold/scheme functional",
        "same-branch convention binding for the H scalar value",
    ]:
        require(phrase in minimal["allowed_source_inputs"], f"minimal input missing {phrase}")
    success = minimal["minimal_success_criteria"]
    require(success["selected_lambda_H_payload_emitted"] is True, "minimal lambda criterion")
    require(success["selected_H_K_threshold_row_emitted"] is True, "minimal H K criterion")
    require(success["accepted_selected_K_source_row_count"] == 10, "minimal count criterion")
    require(success["strict_Omega_lambda_scalar_execution_triggers"] is True, "minimal trigger criterion")
    require(minimal["current_success_criteria_satisfied"] is False, "minimal criteria overclosed")

    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    for phrase in [
        "post-null-delta charged closure rechecked as 9/10 selected K rows",
        "rank-one H projector shortcut rejected as quartic/value payload",
        "D_fin.H plus shared-circle 1/3 shortcut rejected as full H payload",
        "external top/Higgs lambda replay rejected as no-knob selector",
        "minimal H/lambda payload theorem stated with exact success criteria",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected H-sector quartic functional",
        "selected H-sector threshold/scheme functional",
        "selected L_rowlocal.Omega_H.lambda and T_scheme.Omega_H.lambda, or direct K_threshold.Omega_H.lambda",
        "ten-row K antecedent",
        "strict Omega/lambda_H scalar execution",
        "selected matrix-level mixing extension and true SM equivalence",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "selected charged `K_threshold` rows preserved: `9/10`",
        "rank-one H projector shortcut rejected",
        "`D_fin.H` plus shared-circle `1/3` shortcut rejected",
        "external top/Higgs formula replay rejected",
        "selected `K_threshold.Omega_H.lambda`: `false`",
        "ten-K antecedent satisfied: `false`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
