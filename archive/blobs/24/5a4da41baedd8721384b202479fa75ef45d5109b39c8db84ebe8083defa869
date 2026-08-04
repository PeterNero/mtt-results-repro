"""Audit CONST-HIGGS-01 H7B1R Huv source or primitive-C1/lambda bridge gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1r_huv_source_operator_or_primitive_c1_lambda_bridge"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
DIRECT_HUV = BASE / "direct_huv_source_lane.packet.json"
C1_BRIDGE = BASE / "primitive_c1_lambda_bridge_lane.packet.json"
CONTRACT = BASE / "huv_bridge_acceptance_contract.packet.json"
NO_CYCLE = BASE / "non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1R_HuvSourceOperatorOrPrimitiveC1LambdaBridge_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1R_BOTH_EXITS_TESTED_HUV_SOURCE_PAYLOAD_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def require_all_true(packet: dict[str, object], name: str) -> None:
    for key, value in packet.items():
        require(value is True, f"{name} expected true: {key}")


def require_all_false(packet: dict[str, object], name: str) -> None:
    for key, value in packet.items():
        require(value is False, f"{name} expected false: {key}")


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
    direct = load(DIRECT_HUV)
    c1 = load(C1_BRIDGE)
    contract = load(CONTRACT)
    no_cycle = load(NO_CYCLE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("direct", direct),
        ("c1", c1),
        ("contract", contract),
        ("no_cycle", no_cycle),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "theorem")
    require(candidate["H7B1Q_imported"] is True, "H7B1Q import")
    require(candidate["same_source_functional_exit_closed"] is True, "functional exit")
    require(candidate["direct_Huv_source_exit_closed"] is False, "direct overclose")
    require(candidate["primitive_C1_lambda_bridge_exit_closed"] is False, "primitive bridge overclose")
    require(candidate["current_C1_codomain_contains_Huv"] is False, "C1 codomain")
    require(candidate["lambda12_reclassified_as_gauge_threshold_not_Higgs_lambda"] is True, "lambda12")
    require(candidate["Huv_bridge_acceptance_contract_built"] is True, "contract built")
    for key in [
        "UV_twoHiggs_basis_emitted",
        "B_Huv_value_emitted",
        "M_source_value_emitted",
        "direct_Huv_entries_emitted",
        "selected_s_beta_value_found",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(candidate[key] is False, f"candidate overclosed {key}")
    require(candidate["new_Higgs_specific_parameters"] == 0, "candidate params")
    require(
        candidate["selected_next_artifact"] == "MTT_CONST_HIGGS_01_H7B1S_HuvBridgeFunctorOrNonlinearHYMRowExecution_v1",
        "candidate next",
    )

    require(direct["status"] == "DIRECT_UV_HUV_SOURCE_LANE_TESTED_PAYLOAD_OPEN", "direct status")
    require_all_true(direct["closed_support"], "direct support")
    require_all_false(direct["missing_payload"], "direct missing payload")
    direct_decision = direct["decision"]
    require(direct_decision["direct_Huv_source_exit_closed"] is False, "direct closure")
    require(direct_decision["rank_one_or_single_H_projection_promoted_to_UV_twoHiggs"] is False, "single H overpromoted")
    require(direct_decision["conditional_Huv_functor_promoted_as_value"] is False, "functor overpromoted")
    require("route_A_Hsector_dynamic_extension" in direct["minimal_payload_to_close"], "direct route A")
    require("route_B_nonlinear_HYM_or_direct_rows" in direct["minimal_payload_to_close"], "direct route B")

    require(c1["status"] == "PRIMITIVE_C1_LAMBDA_BRIDGE_TESTED_NO_HUV_CODOMAIN", "c1 status")
    coord = c1["C1_coordinate_system"]
    require(coord["codomain_real_dimension"] == 72, "c1 dimension")
    require(coord["sector_order"] == ["u", "d", "e", "nuD"], "c1 sectors")
    for key in [
        "contains_H_sector",
        "contains_Hu_sector",
        "contains_Hd_dagger_sector",
        "contains_Huv_sector",
    ]:
        require(coord[key] is False, f"c1 codomain overcontains {key}")
    primitive = c1["primitive_C1_status"]
    require(primitive["same_source_identity_normal_form_built"] is True, "normal form")
    require(primitive["first_row_formula_source_specified"] is True, "first row formula")
    require(primitive["first_row_value_execution_open"] is True, "first row open")
    for key in [
        "selected_A_selected_promoted",
        "selected_b_selected_promoted",
        "honest_Galerkin_C1_contractions_promoted",
        "selected_C1_response_operator_A_emitted",
        "selected_source_vector_b_emitted",
    ]:
        require(primitive[key] is False, f"primitive overpromoted {key}")
    dynamic = c1["nonSM_dynamic_layer_status"]
    require(dynamic["current_layer_value_packet_emitted"] is True, "dynamic current")
    require(dynamic["current_layer_flavor_no_go"] is True, "dynamic no-go")
    require(dynamic["sector_order"] == ["d", "e", "nuD", "u"], "dynamic sectors")
    require(dynamic["contains_Huv_sector"] is False, "dynamic Huv")
    require(dynamic["selected_dynamic_overlap_tensor_claimed"] is False, "dynamic tensor")
    require(dynamic["selected_Galerkin_C1_contractions_claimed"] is False, "dynamic Galerkin")
    lambda12 = c1["lambda12_status"]
    require(lambda12["formula"] == "lambda_12 = p_Y - p_SU2", "lambda formula")
    require(lambda12["is_hypercharge_threshold_split"] is True, "lambda split")
    require(lambda12["is_Higgs_lambda_H"] is False, "lambda overpromoted")
    require(lambda12["determinant_amplitudes_selected"] is False, "lambda determinant values")
    c1_decision = c1["decision"]
    require(c1_decision["primitive_C1_lambda_bridge_exit_closed"] is False, "bridge closed")
    require(c1_decision["lambda12_can_be_used_as_Higgs_lambda_without_bridge"] is False, "lambda shortcut")
    require(c1_decision["matter_sector_C1_rows_can_be_used_as_Huv_without_bridge"] is False, "matter shortcut")
    require(c1_decision["current_bridge_codomain_missing"] is True, "codomain missing")

    require(contract["status"] == "HUV_BRIDGE_ACCEPTANCE_CONTRACT_BUILT", "contract status")
    future = contract["necessary_future_object"]
    require(future["codomain"] == "Hermitian 2x2 Higgs mass/strain block on ordered basis (H_u,H_d^dagger)", "future codomain")
    require(len(future["must_emit_one_of"]) == 3, "future exits")
    forbidden = contract["forbidden_promotions"]
    require("using lambda_12=p_Y-p_SU2 as lambda_H" in forbidden, "forbid lambda")
    require("using u,d,e,nuD C1 rows as Huv rows" in forbidden, "forbid rows")
    tests = contract["acceptance_tests"]
    require(tests["basis_labels_emitted"] == "ordered basis exactly [H_u,H_d^dagger]", "basis test")
    require("Huu,Hdd real" in tests["Hermitian_payload_emitted"], "Hermitian test")

    require(no_cycle["status"] == "NO_CIRCULATION_LEDGER_UPDATED_H7B1R", "no cycle")
    require_all_true(no_cycle["retired_or_do_not_reopen"], "retired")
    require_all_true(no_cycle["active_not_retired"], "active")
    circ = no_cycle["circulation_test"]
    require(circ["is_reopening_H7B1Q"] is False, "reopen Q")
    require(circ["is_reopening_plain_C1_projection"] is False, "reopen C1")
    require(circ["is_promoting_lambda12_as_lambda_H"] is False, "lambda as H")
    require(circ["is_promoting_matter_rows_as_Huv"] is False, "matter as Huv")
    require(len(circ["new_information_added"]) == 4, "new info")

    require(next_work["status"] == "NEXT_WORKORDER_H7B1S_HUV_BRIDGE_FUNCTOR_OR_NONLINEAR_HYM_ROW_EXECUTION", "next status")
    require(next_work["primary_next"]["label"].endswith("H7B1S-HUV-BRIDGE-FUNCTOR-OR-NONLINEAR-HYM-ROW-EXECUTION"), "next label")
    require(len(next_work["legal_exits"]) == 2, "next exits")
    strategy = next_work["superset_strategy"]
    require(strategy["combining_paths"] is True, "superset combining")
    require(strategy["using_one_straight_way"] is False, "superset multiple")
    require("not measured lambda_H or weak lambda_12" in strategy["locked_target"], "locked target")

    require(cert["status"] == STATUS, "cert status")
    require(cert["same_source_functional_exit_closed"] is True, "cert functional")
    require(cert["direct_Huv_source_exit_closed"] is False, "cert direct")
    require(cert["primitive_C1_lambda_bridge_exit_closed"] is False, "cert primitive")
    require(cert["current_C1_codomain_contains_Huv"] is False, "cert codomain")
    require(cert["lambda12_reclassified_as_gauge_threshold_not_Higgs_lambda"] is True, "cert lambda")
    require(cert["Huv_bridge_acceptance_contract_built"] is True, "cert contract")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert closure")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")

    require("direct Huv source exit closed                    False" in note, "note direct")
    require("primitive C1/lambda bridge exit closed           False" in note, "note c1")
    require("H7B1S-HUV-BRIDGE-FUNCTOR-OR-NONLINEAR-HYM-ROW-EXECUTION" in note, "note next")

    print("CONST-HIGGS-01 H7B1R Huv/C1-lambda bridge audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
