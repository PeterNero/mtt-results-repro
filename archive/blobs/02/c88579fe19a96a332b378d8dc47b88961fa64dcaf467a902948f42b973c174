"""Audit the locked-base freeze and PEW/direct-K attack contract."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_lockedbasefreeze_or_pewdirectkattackcontract"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LOCKED_BASE = PACKET_DIR / "locked_base_do_not_reopen.packet.json"
ATTACK = PACKET_DIR / "pew_directk_attack_contract.packet.json"
NEXT = PACKET_DIR / "next_nonlooping_execution_order.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_LockedBaseFreeze_or_PEWDirectKAttackContract_v1.md"

STATUS = (
    "MTT_SELECTED_LOCKEDBASEFREEZE_OR_PEWDIRECTKATTACKCONTRACT_"
    "BUILT_BASE_LOCKED_PEW_DIRECTK_SHARPENED"
)
NEXT_ARTIFACT = "MTT_Selected_RowwiseScalarRetardedOverlapQuadratureValues_or_TSchemeLambdaHExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    locked = load(LOCKED_BASE)
    attack = load(ATTACK)
    next_order = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["closure_claimed"] is True, "contract closure")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["target_fitting_used"] is False, "candidate target fitting")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "candidate next")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "cert next")

    require(locked["status"] == "BASE_LOCKED_FOR_NEXT_PEW_DIRECTK_ATTACK", "locked status")
    require(locked["observed_data_used_as_selector"] is False, "locked observed")
    require(locked["target_fitting_used"] is False, "locked target fitting")
    results = locked["locked_results"]
    require(results["finite_27x27_qutrit_spectral_package_closed"] is True, "27x27")
    require(results["minimal_one_primitive_matrix_ledger_closed"] is True, "matrix ledger")
    require(results["two_premise_AH_equivalent_lane_closed"] is True, "AH8")
    require(results["Pi_CKM_weight_rows_closed"] is True, "Pi_CKM")
    require(results["CKM_diagonal_profile_admission_closed"] is True, "CKM profile")
    require(results["finite_replay_yukawa_exactness_closed"] is True, "Yukawa finite replay")
    require(
        results["strict_no_knob_yukawa_closure_at_finite_replay_standard"] is True,
        "Yukawa finite standard",
    )
    require(results["one_shared_primitive_tier_closed"] is True, "one primitive")
    require(len(locked["do_not_reopen"]) == 5, "do-not-reopen count")
    require(len(locked["not_claimed_by_locked_base"]) == 4, "not-claimed count")
    require(locked["key_numbers"]["AH_equivalent_BN27_connection_rows"] == 8, "AH rows")
    require(locked["key_numbers"]["strict_connection_rows"] == 4, "strict rows")
    require(locked["key_numbers"]["finite_replay_yukawa_magnitude_rows"] == 9, "Yukawa rows")
    require(locked["key_numbers"]["final_yukawa_max_abs_log_residual"] < 1e-12, "Yukawa residual")
    require(locked["key_numbers"]["shared_physical_primitive_count"] == 1, "primitive count")
    require(locked["key_numbers"]["H_specific_parameter_count"] == 0, "H parameter")

    require(attack["status"] == "STRICT_ROWS_ZERO_ATTACK_REDUCED_TO_TWO_EXITS", "attack status")
    require(attack["observed_data_used_as_selector"] is False, "attack observed")
    require(attack["target_fitting_used"] is False, "attack fitting")
    counts = attack["current_counts"]
    require(counts["accepted_strict_P_EW_source_rows"] == 0, "strict PEW rows")
    require(counts["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K rows")
    require(counts["accepted_strict_derivation_route_count"] == 0, "strict route count")
    require(counts["premised_P_EW_source_rows"] == 1, "premised PEW")
    require(counts["premised_direct_K_threshold_Omega_H_lambda_rows"] == 1, "premised direct K")
    require(counts["premised_selected_K_row_count"] == 10, "premised K count")
    require(counts["strict_PEW_source_filled_field_count"] == 0, "PEW fields filled")
    require(counts["strict_PEW_source_required_field_count"] == 8, "PEW fields required")

    support = attack["closed_support"]
    require(support["Step10_route_A_source_rule_closed"] is True, "Step10")
    require(support["first_dynamic_value_rows_accepted"] is True, "first rows")
    require(support["external_import_lane_closed_at_admitted_replay_tier"] is True, "external")
    require(support["selected_sector_transfer_imported"] is True, "sector transfer")
    require(support["physical_dotD_alpha1_imported"] is True, "dotD alpha")

    open_rows = attack["open_rows_preventing_strict_close"]
    require(open_rows["rowwise_scalar_retarded_overlap_values_emitted"] is False, "rowwise values")
    require(open_rows["selected_T_scheme_rows_emitted"] is False, "T scheme")
    require(open_rows["selected_lambda_H_payload_emitted"] is False, "lambda payload")
    require(
        open_rows["selected_threshold_response_functional_instantiated"] is False,
        "threshold functional",
    )
    require(open_rows["selected_internal_value_emission_count"] == 0, "internal values")

    require(len(attack["two_legal_exits"]) == 2, "exit count")
    require(
        attack["attack_decision"]["strict_PEW_directK_closed_now"] is False,
        "attack overclosed",
    )
    require(
        attack["attack_decision"]["one_shared_primitive_lane_remains_valid"] is True,
        "one primitive valid",
    )

    require(next_order["status"] == "NEXT_ORDER_SELECTED", "next order status")
    require(next_order["observed_data_used_as_selector"] is False, "next observed")
    require(next_order["target_fitting_used"] is False, "next fitting")
    require(next_order["ordered_targets"][0] == NEXT_ARTIFACT, "first next target")
    require(len(next_order["ordered_targets"]) == 5, "ordered target count")
    require(len(next_order["why_this_is_not_a_loop"]) == 4, "loop guard count")

    decision = data["closure_decision"]
    require(decision["locked_base_freeze_closed"] is True, "decision freeze")
    require(decision["qutrit27_matrix_locked"] is True, "decision matrix")
    require(decision["yukawa_finite_replay_locked"] is True, "decision Yukawa")
    require(decision["one_shared_primitive_standard_locked"] is True, "decision primitive")
    require(decision["PEW_directK_attack_contract_closed"] is True, "decision attack")
    require(decision["strict_PEW_directK_source_rows_closed"] is False, "decision strict")
    require(decision["full_no_knob_closed"] is False, "decision no knob")
    require(decision["true_SM_equivalence_closed"] is False, "decision true SM")

    key = data["key_numbers"]
    require(key["finite_replay_yukawa_magnitude_rows"] == 9, "key Yukawa rows")
    require(key["final_yukawa_max_abs_log_residual"] < 1e-12, "key Yukawa residual")
    require(key["AH_equivalent_BN27_connection_rows"] == 8, "key AH8")
    require(key["accepted_strict_P_EW_source_rows"] == 0, "key PEW")
    require(key["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "key K")
    require(key["accepted_strict_derivation_route_count"] == 0, "key route")
    require(key["strict_PEW_source_filled_field_count"] == 0, "key filled")
    require(key["strict_PEW_source_required_field_count"] == 8, "key required")
    require(key["shared_physical_primitive_count"] == 1, "key primitive")

    require(cert["locked_base_freeze_closed"] is True, "cert freeze")
    require(cert["qutrit27_matrix_locked"] is True, "cert matrix")
    require(cert["yukawa_finite_replay_locked"] is True, "cert Yukawa")
    require(cert["PEW_directK_attack_contract_closed"] is True, "cert attack")
    require(cert["accepted_strict_P_EW_source_rows"] == 0, "cert PEW")
    require(cert["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "cert K")
    require(cert["strict_PEW_directK_source_rows_closed"] is False, "cert strict")
    require(cert["one_shared_primitive_lane_remains_valid"] is True, "cert primitive")
    require(cert["full_no_knob_closed"] is False, "cert no knob")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    for phrase in [
        "Locked Base",
        "finite-replay charged-Yukawa magnitude rows: `9`",
        "accepted strict `P_EW` source rows: `0`",
        "There are two legal exits",
        NEXT_ARTIFACT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
