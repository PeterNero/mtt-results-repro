"""Audit CONST-HIGGS-01 H7B1H near-hit source-export audit."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1h_nearhit_source_export_audit"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
RANK_ONE_REJECTION = BASE / "rank_one_higgs_projector_rejection.packet.json"
VALPHA_REJECTION = BASE / "conditional_valpha_msource_rejection.packet.json"
NEARHIT_SCAN = BASE / "current_nearhit_scan.packet.json"
ROUTE_DECISION = BASE / "source_export_route_decision.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1H_NearHitSourceExportAudit_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1H_NEARHIT_SOURCE_EXPORT_AUDIT_BUILT_VALUES_OPEN"


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
    rank_one = load(RANK_ONE_REJECTION)
    valpha = load(VALPHA_REJECTION)
    nearhit = load(NEARHIT_SCAN)
    route = load(ROUTE_DECISION)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("rank_one", rank_one),
        ("valpha", valpha),
        ("nearhit", nearhit),
        ("route", route),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "theorem")
    require(candidate["rank_one_H_projector_promoted_to_B_Huv"] is False, "rank-one promoted")
    require(candidate["conditional_valpha_promoted_to_M_source"] is False, "valpha promoted")
    for key in [
        "B_Huv_value_emitted",
        "M_source_value_emitted",
        "selected_finite_Huv_reduction_found",
        "selected_offdiagonal_Omega_found",
        "selected_s_beta_value_found",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(candidate[key] is False, f"candidate overclosed {key}")
    require(candidate["selected_next_route"] == "M_source_first", "candidate next route")
    require(candidate["new_Higgs_specific_parameters"] == 0, "candidate new params")

    require(rank_one["status"] == "RANK_ONE_HIGGS_PROJECTOR_NOT_BHUV", "rank-one status")
    support = rank_one["support_imported"]
    require(support["finite_stationary_projector_replay"] is True, "finite replay")
    require(support["selected_projector_source_verified"] is True, "projector verified")
    require(support["H_sector_projector_rank"] == 1, "H rank")
    require(support["H_sector_transport"] == "identity on Higgs singlet", "H transport")
    require(support["block_factorized_family_Higgs_projector_retention"] is True, "block retention")
    why_b = rank_one["why_not_B_Huv"]
    for key in [
        "current_H_projector_is_rank_one_collapsed_line",
        "current_H_transport_is_identity_on_singlet",
        "no_Hu_Hd_dagger_two_column_lift",
        "no_color_triplet_decoupling_certificate",
        "no_two_Higgs_metric_or_light_projector",
    ]:
        require(why_b[key] is True, f"B rejection {key}")
    require(rank_one["promotion_decision"]["rank_one_H_projector_promoted_to_B_Huv"] is False, "rank-one decision")
    require(rank_one["promotion_decision"]["B_Huv_value_emitted"] is False, "B emitted")
    require(rank_one["promotion_decision"]["safe_support_for_future_B_Huv"] is True, "B support")

    require(valpha["status"] == "CONDITIONAL_VALPHA_VALIDATOR_SUCCESS_NOT_MSOURCE", "valpha status")
    vsupport = valpha["support_imported"]
    require(vsupport["conditional_valpha_top_report_passes"] is True, "conditional pass")
    require(vsupport["conditional_theorem_proved"] is True, "conditional theorem")
    require(vsupport["actual_packet_status"] == "OPEN", "actual status")
    require(vsupport["actual_packet_open_item_count"] > 0, "actual open count")
    require(vsupport["visible_gs_gate_reduces_to_operator_source"] is True, "visible GS theorem")
    require(vsupport["selected_DE_gap_Riesz_Green_layer_carried"] is True, "DE gap")
    require(vsupport["same_basis_dotD_value_matrices_available"] is True, "dotD values")
    require(vsupport["ordinary_rhoE_source_routes_retired"] is True, "rhoE retired")
    why_m = valpha["why_not_M_source"]
    require(why_m["hypothetical_flags_are_not_physical_proof"] is True, "hypothetical guard")
    for key in [
        "claims_D_E_dotD_constructed",
        "claims_selected_source_constructed",
        "selected_visible_operator_source_constructed",
        "selected_D_E_dotD_Riesz_Green_constructed",
    ]:
        require(why_m[key] is False, f"M false guard {key}")
    for key in [
        "selected_dotD_source_theorem_open",
        "same_branch_alpha1_driver_theorem_open",
        "selected_Hess_Xi_finite_blocks_open",
    ]:
        require(why_m[key] is True, f"M open guard {key}")
    require(valpha["promotion_decision"]["conditional_valpha_promoted_to_M_source"] is False, "M decision")
    require(valpha["promotion_decision"]["M_source_value_emitted"] is False, "M emitted")
    require(valpha["promotion_decision"]["safe_support_for_future_M_source"] is True, "M support")

    hits = nearhit["near_hits"]
    require(hits["rank_one_H_projector"]["promotable_to_B_Huv"] is False, "rank-one nearhit")
    require(hits["block_family_Higgs_projector_retention"]["promotable_to_B_Huv"] is False, "block nearhit")
    require(hits["conditional_valpha_validator_pass"]["promotable_to_M_source"] is False, "conditional nearhit")
    require(hits["selected_DE_gap_and_dotD_value_prefix"]["promotable_to_M_source"] is False, "prefix nearhit")
    require(hits["execution_ii_split_hym_yukawa_shape"]["source_exists"] is True, "execution ii exists")
    require(hits["execution_ii_split_hym_yukawa_shape"]["promotable_to_selector"] is False, "execution ii selector")
    for key in ["B_Huv", "M_source", "Huv", "Omega", "s_beta", "lambda_H"]:
        require(nearhit["no_values_exported"][key] is True, f"nearhit value {key}")

    require(route["status"] == "TRY_MSOURCE_FIRST_BHUV_WATCH_REMAINS_OPEN", "route status")
    require(route["selected_next_route"] == "M_source_first", "route selected")
    require(route["route_scores"]["M_source_first"]["score"] > route["route_scores"]["B_Huv_first"]["score"], "route score")
    require("selected D_E/gap/Riesz/Green prefix is carried" in route["route_scores"]["M_source_first"]["strengths"], "route strength")
    require(route["exact_next_payload"]["label"].endswith("H7B1I-MSOURCE-FROM-SELECTED-RESPONSE-PREFIX"), "exact next label")
    require(len(route["exact_next_payload"]["must_emit"]) == 5, "exact next fields")

    require(next_work["status"] == "NEXT_WORKORDER_H7B1I_MSOURCE_FROM_SELECTED_RESPONSE_PREFIX", "next status")
    require(next_work["primary_next"]["label"].endswith("H7B1I-MSOURCE-FROM-SELECTED-RESPONSE-PREFIX"), "next primary")
    require("BHUV-WATCH" in next_work["watch_parallel"]["label"], "B watch")

    require(cert["status"] == STATUS, "cert status")
    require(cert["rank_one_H_projector_promoted_to_B_Huv"] is False, "cert B")
    require(cert["conditional_valpha_promoted_to_M_source"] is False, "cert M")
    require(cert["selected_next_route"] == "M_source_first", "cert route")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")
    require("rank-one H projector -> B_Huv             False" in note, "note B rejection")
    require("conditional V_alpha -> M_source           False" in note, "note M rejection")

    print("CONST-HIGGS-01 H7B1H near-hit source-export audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
