from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
PACKET = VALIDATED / "n3.junction_reverse_composition.a409t.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    require(packet["artifact"] == "A409T", "A409T artifact changed")
    require(packet["schema"] == "MTTQ79HeightFourJunctionReverseCompositionTheorem.v1", "A409T schema changed")
    theorem = packet["theorem"]
    require(theorem["proved"], "A409T theorem flag false")
    require(theorem["augmented_coordinate"] == "q", "A409T augmented coordinate changed")
    require(theorem["augmented_forward_block_operator"] == "T_e^(q)=[[U_e,0],[V_e,I_8]]", "A409T augmented forward block changed")
    require(theorem["augmented_reverse_block_operator"] == "(T_e^(q))^{-1}=[[U_e^{-1},0],[-V_e U_e^{-1},I_8]]", "A409T augmented inverse block changed")
    require(theorem["selected_physical_residue_sign_bridge"] == "r_phys=-q", "A409T physical sign bridge changed")
    require(theorem["forward_block_operator"] == "T_e^(r)=[[U_e,0],[-V_e,I_8]]", "A409T physical forward block changed")
    require(theorem["reverse_block_operator"] == "(T_e^(r))^{-1}=[[U_e^{-1},0],[+V_e U_e^{-1},I_8]]", "A409T physical inverse block changed")
    require("p_hub=0" in theorem["zero_trunk_rule"], "A409T zero-trunk premise missing")
    contract = packet["execution_contract"]
    require("invertible" in contract["A405_requirement"], "A409T lost the invertibility gate")
    require("A123" in contract["chart_requirement"], "A409T lost the chart gate")
    require("affine error frame" in contract["frame_requirement"], "A409T lost the frame gate")
    require("r_phys=-q" in contract["residue_coordinate_requirement"], "A409T lost the residue-coordinate gate")
    inventory = packet["inventory"]
    require(int(inventory["selected_thimble_entries"]) == 76, "A409T thimble count changed")
    require(int(inventory["selected_handle_entries"]) == 1, "A409T handle count changed")
    require(int(inventory["common_period_dimension"]) == 5, "A409T period dimension changed")
    require(int(inventory["integrated_residue_dimension"]) == 8, "A409T residue dimension changed")
    require(int(inventory["native_y_target_count"]) + int(inventory["native_z_target_count"]) == 76, "A409T chart inventory changed")
    for label, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        require(path.is_file(), f"A409T authority missing: {label}")
        require(sha256(path) == entry["sha256"], f"A409T authority stale: {label}")
    scope = packet["strict_scope"]
    for key in (
        "reverse_affine_operator_formula_proved",
        "selected_physical_residue_sign_bridge_proved",
        "integer_sum_commutes_with_reverse_transport_proved",
        "zero_common_trunk_elimination_rule_proved",
        "A123_chart_transition_required_for_native_z_targets",
    ):
        require(scope[key], f"A409T theorem gate false: {key}")
    require(not scope["A405_numeric_operator_sweeps_consumed"], "A409T overclaims A405")
    require(not scope["outer_thimble_states_consumed"], "A409T overclaims outer states")
    require(not scope["common_hub_sum_executed"], "A409T overclaims the hub sum")
    require(not scope["full_correlation_preserving_path_execution_closed"], "A409T overclaims full transport")
    require(not scope["interval_Newton_existence_and_uniqueness_closed"], "A409T overclaims Newton")
    require(not scope["covariant_zero_proved"], "A409T overclaims a zero")
    require(not scope["full_SM_closure_proved"], "A409T overclaims SM closure")
    require(not scope["observed_SM_values_used"], "observed SM data entered A409T")
    print("PASS: A409T fixes the exact reverse affine operator and zero-trunk composition rule")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
