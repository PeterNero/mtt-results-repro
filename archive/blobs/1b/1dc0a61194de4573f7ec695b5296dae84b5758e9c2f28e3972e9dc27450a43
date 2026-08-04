"""Audit CONST-EW-02 B19 visible source solve / EndE values frontier."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b19_visible_source_solve_or_ende_values"
DATA = ROOT / "candidate_data"
BASE = DATA / SLUG
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(DATA / f"{SLUG}.candidate.json")
    visible = load(BASE / "visible_source_solve_attempt_import.packet.json")
    finite = load(BASE / "routec_finite_cochain_construct_import.packet.json")
    ende = load(BASE / "ende_domain_or_nonidentity_rhoe_import.packet.json")
    boundary = load(BASE / "weak_mixing_b19_boundary.packet.json")
    next_work = load(BASE / "next_labeled_workorder.packet.json")
    cert = load(CERT)

    for name, packet in [
        ("candidate", candidate),
        ("visible", visible),
        ("finite", finite),
        ("ende", ende),
        ("boundary", boundary),
        ("cert", cert),
    ]:
        require(packet["observed_data_used_as_selector"] is False, f"{name} used observed selector")
        require(packet["target_fitting_used"] is False, f"{name} used target fitting")
        require(packet["closure_claimed"] is False, f"{name} claimed closure")

    require(candidate["theorem"]["proved"] is True, "B19 theorem did not prove")
    require(candidate["strict_xL_emitted_now"] is False, "xL incorrectly emitted")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclaimed")
    require(candidate["source_solve_closed"] is False, "source solve overclosed")
    require(cert["source_solve_closed"] is False, "certificate source solve overclosed")
    require(cert["strict_xL_emitted_now"] is False, "certificate xL overclosed")
    require(cert["physical_weak_angle_closure"] is False, "certificate weak angle overclosed")

    require(visible["all_three_lanes_executed"] is True, "visible lanes not all executed")
    require(visible["best_next_lane"] == "LaneB_RouteC_FiniteCochain", "Route-C finite lane not prioritized")
    require(visible["source_solve_closed"] is False, "visible source solve overclosed")
    require(visible["full_sm_or_lambda12_closed"] is False, "full SM/lambda12 overclosed")

    require(finite["closed_or_constructed"]["finite_construct_executed"] is True, "finite construct not executed")
    require(
        finite["closed_or_constructed"]["routec_operator_algebra_closed_conditionally"] is True,
        "Route-C conditional algebra not closed",
    )
    require(
        finite["closed_or_constructed"]["source_level_weyl_carrier_closed"] is True,
        "source-level Weyl carrier not closed",
    )
    require(finite["still_open"]["finite_cochain_source_closed"] is False, "finite cochain source overclosed")
    require(finite["still_open"]["lambda_12_closed"] is False, "lambda12 overclosed")
    require(
        finite["next_true_object"] == "Selected_U1Y_RouteC_MatterSlot_Overlap_Normalization_Source_v1",
        "wrong next Route-C object",
    )
    require(
        "selected singlet rule placing nuD on the shift side" in finite["must_emit_next"],
        "nuD shift-side rule not required next",
    )
    require(
        "same-source primitive C1/overlap tensors in validator basis" in finite["must_emit_next"],
        "primitive C1 tensors not required next",
    )

    require(ende["gate_built"]["sourceemission_gate_built"] is True, "EndE/rhoE gate not built")
    require(ende["fill_attempt"]["fill_attempt_executed"] is True, "EndE/rhoE fill attempt not executed")
    require(ende["fill_attempt"]["lane_a_filled"] == 0, "EndE lane A unexpectedly filled")
    require(ende["fill_attempt"]["lane_b_filled"] == 0, "EndE lane B unexpectedly filled")
    require(ende["still_open"]["typed_cech_EndE_domain_basis_emitted"] is False, "typed EndE basis overemitted")
    require(ende["still_open"]["projective_twisted_nonidentity_rhoE_emitted"] is False, "rhoE table overemitted")
    require(ende["still_open"]["same_source_identity_proved"] is False, "same-source identity overproved")

    require(boundary["closed_now"]["finite_RouteC_cochain_lane_prioritized"] is True, "boundary Route-C not prioritized")
    require(boundary["closed_now"]["source_level_weyl_carrier_closed"] is True, "boundary Weyl carrier not closed")
    require(boundary["closed_now"]["EndE_nonidentity_rhoE_gate_built"] is True, "boundary EndE/rhoE gate not built")
    require(boundary["still_open"]["matter_slot_overlap_normalization_source"] is True, "matter-slot source not left open")
    require(boundary["still_open"]["same_source_primitive_C1_overlap_tensors"] is True, "primitive C1 tensors not left open")
    require(boundary["still_open"]["actual_xL_source_emission"] is True, "xL not left open")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "weak angle not left open")

    require(
        next_work["active_label"] == "CONST-EW-02 / WEAK-MIXING / B20-MATTERSLOT-OVERLAP-OR-SOURCE-AUGMENTATION",
        "wrong next B20 label",
    )
    require("MATTERSLOT-OVERLAP" in next_work["primary"]["label"], "primary B20 route mislabeled")
    require("SOURCEAUGMENTED" in next_work["parallel"]["label"], "parallel B20 route mislabeled")

    print("CONST-EW-02 B19 visible source solve / EndE values audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
