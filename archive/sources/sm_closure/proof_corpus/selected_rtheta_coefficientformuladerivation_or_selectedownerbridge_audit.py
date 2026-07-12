"""Audit R_theta coefficient-formula derivation / selected-owner bridge attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_rtheta_coefficientformuladerivation_or_selectedownerbridge"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FORMULA_BASIS = PACKET_DIR / "dynamic_precoefficient_formula_basis.packet.json"
SLOT_PROJECTION = PACKET_DIR / "rtheta_slot_projection_feasibility.packet.json"
BRIDGE_ATTEMPT = PACKET_DIR / "selected_owner_bridge_attempt.packet.json"
DECISION = PACKET_DIR / "coefficient_formula_derivation_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_coefficient_formula_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RThetaCoefficientFormulaDerivation_or_SelectedOwnerBridge_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_RTHETACOEFFICIENTFORMULADERIVATION_OR_SELECTEDOWNERBRIDGE_"
    "BUILT_PRECOEFFICIENT_BASIS_PROJECTION_KERNEL_OPEN"
)
NEXT = "MTT_Selected_RThetaPhysicalProjectionKernel_or_ProfileResponse_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    basis = load(FORMULA_BASIS)
    slots = load(SLOT_PROJECTION)
    bridge = load(BRIDGE_ATTEMPT)
    decision = load(DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")

    require(
        basis["status"] == "DYNAMIC_PRECOEFFICIENT_FORMULA_BASIS_CLOSED",
        "basis status mismatch",
    )
    require(basis["selected_by_MTT"] is True, "dynamic values not selected")
    require(basis["basis_closed"] is True, "pre-coefficient basis not closed")
    require(len(basis["sector_basis"]) == 4, "wrong sector basis count")
    for row in basis["sector_basis"]:
        require(row["hermitian_residual_norm_sq"] == 0.0, f"sector residual nonzero: {row['sector']}")
        require(abs(row["trace_H1"] - row["trace_recomputed"]) < 1e-12, f"trace mismatch: {row['sector']}")
        require(row["formula_basis_role"] == "selected dynamic pre-coefficient observable", "basis role mismatch")
    require(basis["closure_claimed"] is True, "basis should close locally")

    require(
        slots["status"] == "SLOT_PROJECTION_SKELETONS_BUILT_PHYSICAL_PROJECTION_KERNEL_OPEN",
        "slot projection status mismatch",
    )
    require(slots["slot_count"] == 10, "wrong R_theta slot count")
    require(slots["precoefficient_skeleton_count"] == 8, "wrong skeleton count")
    require(slots["accepted_coefficient_formula_count"] == 0, "coefficient formulas overaccepted")
    require(slots["physical_projection_kernel_required"] == "Pi_Rtheta", "wrong kernel name")
    require(slots["physical_projection_kernel_emitted"] is False, "projection kernel overemitted")
    for row in slots["slot_rows"]:
        require(row["family_or_carrier_projector_emitted"] is False, f"projector overemitted: {row['slot_id']}")
        require(row["physical_threshold_projection_kernel_emitted"] is False, f"kernel overemitted: {row['slot_id']}")
        require(row["accepted_coefficient_formula"] is False, f"formula overaccepted: {row['slot_id']}")
        require("selected physical projection kernel Pi_Rtheta" in row["missing_for_acceptance"], f"missing Pi reason: {row['slot_id']}")
    require(slots["closure_claimed"] is False, "slot projection overclaimed")

    require(
        bridge["status"] == "SELECTED_OWNER_BRIDGE_ATTEMPTED_REDUCED_TO_PHYSICAL_PROJECTION_KERNEL",
        "bridge status mismatch",
    )
    require(bridge["best_current_precursor"] == "same_source_dynamic_matter_overlap_packet", "wrong bridge precursor")
    for key in [
        "same_source",
        "selected_operator_values",
        "selected_overlap_transfer",
        "selected_normalization",
        "selected_b_source",
    ]:
        require(bridge["precursor_satisfies"][key] is True, f"bridge precursor missing: {key}")
    require(bridge["bridge_theorem_closed"] is False, "bridge overclosed")
    require(
        "Pi_Rtheta physical projection kernel from dynamic sectors to threshold/mass-scheme slots"
        in bridge["missing_for_selected_rtheta_owner"],
        "bridge missing Pi_Rtheta reason absent",
    )
    require(bridge["closure_claimed"] is False, "bridge overclaimed")

    require(
        decision["status"] == "PRECOEFFICIENT_BASIS_CLOSED_RTHETA_PROJECTION_KERNEL_OPEN",
        "decision status mismatch",
    )
    require(decision["dynamic_precoefficient_formula_basis_closed"] is True, "decision basis not closed")
    require(decision["slot_projection_skeletons_closed"] is True, "decision slot skeletons not closed")
    require(decision["precoefficient_skeleton_count"] == 8, "decision skeleton count mismatch")
    require(decision["accepted_coefficient_formula_count"] == 0, "decision overaccepted formulas")
    require(decision["selected_owner_bridge_reduced"] is True, "owner bridge not reduced")
    require(len(decision["old_frontier"]) == 4, "old frontier should have four obligations")
    require(len(decision["contracted_frontier"]) == 3, "frontier should contract to three obligations")
    for key in [
        "rtheta_packet_constructed",
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(decision["residual_tables_used_only_for_validation"] is True, "residual validation guard missing")
    require(decision["firstpass_value_packet_used_only_as_replay_target"] is True, "value packet guard missing")
    require(decision["closure_claimed"] is False, "decision overclaimed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closed_now"]["dynamic_precoefficient_formula_basis"] is True, "cutset missing basis closure")
    require(cutset["closed_now"]["owner_bridge_reduced_to_projection_kernel"] is True, "cutset missing bridge reduction")
    require(len(cutset["still_open"]) == 3, "cutset should have three open obligations")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")

    final = data["closure_decision"]
    require(final["dynamic_precoefficient_formula_basis_closed"] is True, "candidate final basis not closed")
    require(final["slot_projection_skeletons_closed"] is True, "candidate final slots not closed")
    for key in [
        "selected_physical_projection_kernel_closed",
        "accepted_coefficient_formulas_closed",
        "selected_owner_bridge_closed",
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(final[key] is False, f"candidate final overclosed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(cert["precoefficient_skeleton_count"] == 8, "certificate skeleton count mismatch")
    require(cert["accepted_coefficient_formula_count"] == 0, "certificate formula overaccepted")
    require(cert["frontier_contracts_to_three_obligations"] is True, "certificate frontier contraction missing")
    require("accepted coefficient formulas         : 0" in note, "note missing zero-formula guard")
    require("frontier obligations after reduction : 3" in note, "note missing three-obligation guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
