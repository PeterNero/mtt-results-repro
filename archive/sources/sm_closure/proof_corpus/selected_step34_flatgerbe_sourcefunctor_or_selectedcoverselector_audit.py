"""Audit Step 34 flat gerbe source functor and selected-cover selector boundary."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step34_flatgerbe_sourcefunctor_or_selectedcoverselector"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FUNCTOR = PACKET_DIR / "step34_finite_group_flat_gerbe_source_functor.packet.json"
SELECTOR = PACKET_DIR / "step34_selected_cover_classifying_map_obligation.packet.json"
OPERATOR = PACKET_DIR / "step34_operator_promotion_boundary.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step34_FlatGerbeSourceFunctor_or_SelectedCoverSelector_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP34_FLAT_GERBE_SOURCE_FUNCTOR_CONSTRUCTED_SELECTED_COVER_OPEN"
NEXT = "MTT_Selected_S3ClassifyingMapCoverSelector_and_ProjectorRetention_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    functor = load(FUNCTOR)
    selector = load(SELECTOR)
    operator = load(OPERATOR)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    finite = functor["input_finite_data"]
    require(finite["active_group"] == "F_3^2", "wrong active group")
    require(finite["central_phase_label"] == "zeta_3^2", "wrong central phase")
    require(finite["branch"]["q"] == 79, "wrong q")
    require(finite["branch"]["orientation"] == "F", "wrong orientation")
    require(finite["branch"]["torsion_label_m"] == 1, "wrong torsion label")
    require("a*d - b*c mod 3" in finite["commutator_form"], "wrong commutator form")

    construction = functor["construction"]
    require(construction["classifying_space"] == "B(F_3^2)", "wrong classifying space")
    require("c:Y -> B(F_3^2)" in construction["smooth_input"], "classifying map not named")
    require("curvature H=0" in construction["smooth_output"], "flat curvature not named")
    require("zeta_3^2" in construction["holonomy_output"], "holonomy phase not named")

    proved = functor["proved_by_construction"]
    for key in [
        "finite_to_smooth_flat_gerbe_source_functor",
        "curvature_H_zero_for_flat_source",
        "qutrit_central_cocycle_holonomy_map",
        "finite_twisted_CP_cancellation_transports_conditionally",
        "ordinary_rank_two_DD_zero_route_not_used",
    ]:
        require(proved[key] is True, f"functor proof missing: {key}")
    not_proved = functor["not_proved_by_functor_alone"]
    for key in [
        "selected_classifying_map_c_supplied_by_MTT",
        "selected_good_cover_supplied_by_MTT",
        "smooth_projector_retention_verified",
        "operator_level_projective_rhoE_transition_verified",
        "selected_D_E_Riesz_Green_dotD_values",
    ]:
        require(not_proved[key] is True, f"open obligation missing: {key}")

    require(selector["status"] == "SELECTED_COVER_CLASSIFYING_MAP_SELECTOR_IS_ONLY_SOURCE_MISSING_LAYER", "selector status mismatch")
    require(selector["current_support"]["finite_S3_CP_cancellation_closed"] is True, "finite support missing")
    require(selector["current_support"]["visible_cycles_W3_spinC_zero_finite_support"] is True, "finite W3/spinC support missing")
    require(selector["current_support"]["selected_cycles_supplied_in_q79_gate"] is False, "selected cycles overclosed")
    require(selector["selector_axiom_status"] == "FORMULATED_NOT_PROVED", "selector axiom overproved")
    require(selector["closure_claimed"] is False, "selector closure overclaimed")
    for item in [
        "classifying map c:Y -> B(F_3^2) whose induced pi1 image is the active rank-two S3 image",
        "Deligne-Cech cocycle representative for c^*[omega_m=1]",
        "W3=0 or spinC-compatible cancellation data on the same selected Y",
    ]:
        require(item in selector["must_select"], f"selector obligation missing: {item}")

    require(operator["operator_values_closed_now"] is False, "operator values overclosed")
    require(operator["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    for item in [
        "selected_classifying_map_c_supplied_by_MTT",
        "smooth_projector_retention_verified",
        "operator_level_projective_rhoE_transition_verified",
    ]:
        require(item in operator["blocked_until"], f"operator blocker missing: {item}")

    decision = data["closure_decision"]
    for key in [
        "finite_to_smooth_flat_gerbe_source_functor_constructed",
        "qutrit_central_extension_holonomy_map_constructed",
        "finite_twisted_CP_cancellation_conditionally_transported",
        "selected_cover_classifying_map_obligation_isolated",
        "operator_promotion_boundary_reduced_to_selected_cover_and_projectors",
    ]:
        require(decision[key] is True, f"decision close missing: {key}")
    for key in [
        "selected_classifying_map_c_closed",
        "selected_good_cover_closed",
        "smooth_freed_witten_projector_retention_closed",
        "operator_level_projective_rhoE_transition_closed",
        "selected_D_E_Riesz_Green_dotD_values_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "accepted scalar rows overclosed")
    require(data["theorem"]["proved"] is True, "functor theorem not proved")
    require(cert["finite_to_smooth_flat_gerbe_source_functor_constructed"] is True, "certificate functor flag missing")
    require(cert["selected_classifying_map_c_closed"] is False, "certificate selected map overclosed")
    require(cert["operator_sector_values_closed"] is False, "certificate operator values overclosed")

    for phrase in [
        "finite q79/F,m=1 F_3^2 cocycle",
        "flat Deligne-Cech gerbe via c:Y -> B(F_3^2)",
        "not yet the selected smooth source",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
