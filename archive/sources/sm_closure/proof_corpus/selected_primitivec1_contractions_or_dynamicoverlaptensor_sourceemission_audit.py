"""Audit primitive-C1 contractions / dynamic-overlap tensor source emission."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_primitivec1_contractions_or_dynamicoverlaptensor_sourceemission.candidate.json"
CERT = ROOT / "certificates" / "selected_primitivec1_contractions_or_dynamicoverlaptensor_sourceemission_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrimitiveC1Contractions_or_DynamicOverlapTensor_SourceEmission_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_primitivec1_contractions_or_dynamicoverlaptensor_sourceemission.py"

STATUS = (
    "MTT_SELECTED_PRIMITIVEC1_CONTRACTIONS_OR_DYNAMICOVERLAPTENSOR_SOURCEEMISSION_"
    "ENVELOPE_BUILT_DYNAMIC_VALUES_OPEN"
)
NEXT = "MTT_Selected_DynamicOverlapTensor_HessianNormalization_or_GalerkinC1Contractions_ValueEmission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note missing next artifact")

    closed = data["closed_inputs"]
    for key in [
        "alpha1_driver_verified",
        "selected_dotD_source_verified",
        "honest_dotD_alpha1_replay",
        "static_weyl_sector_routing",
        "static_singlet_neutrino_shift_rule",
        "static_trace_transfer_normalization",
        "primitive_class_C1_observable_layer",
        "current_layer_not_flavor_closure",
    ]:
        require(closed[key] is True, f"closed input missing: {key}")

    envelope = data["contraction_envelope"]
    require(envelope["constructed"] is True, "contraction envelope not constructed")
    require(envelope["phase_route"] == ["u", "e"], "phase route mismatch")
    require(envelope["shift_route"] == ["d", "nuD"], "shift route mismatch")
    require(envelope["active_shift"] == [1, 1], "active shift mismatch")
    require(envelope["fixed_fiber_class"] == [0, 1, 2], "fiber class mismatch")
    require(envelope["selected_as_dynamic_tensor"] is False, "dynamic tensor overclaimed")
    summary = envelope["candidate_summary"]
    require(summary["fixed_fiber_candidates"] == [0, 1, 2], "fixed candidates mismatch")
    require(summary["all_fixed_fiber_rank_three"] is True, "fixed fiber candidates not rank three")
    require(summary["all_fixed_fiber_rank_values"] == [3], "rank values mismatch")

    promotion = data["promotion_test"]
    require(promotion["all_required_fields_emitted"] is False, "all fields overclaimed")
    require(promotion["A_selected_promotion_allowed"] is False, "A_selected promotion overclaimed")
    require(promotion["b_selected_promotion_allowed"] is False, "b_selected promotion overclaimed")
    require(promotion["rank_or_consistency_test_allowed"] is False, "rank test overenabled")
    for key, value in promotion["required_fields"].items():
        require(value is False, f"promotion field unexpectedly true: {key}")

    manifests = data["honest_vs_formal_primitive_manifest"]
    require(
        manifests["honest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
        "honest primitive status mismatch",
    )
    require(manifests["honest_selected_source_verified"] is False, "honest source oververified")
    require(
        manifests["formal_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
        "formal primitive status mismatch",
    )
    require(manifests["formal_selected_source_verified"] is False, "formal source oververified")
    require(manifests["formal_lift_promoted"] is False, "formal lift overpromoted")

    retired = data["retired_blockers"]
    for key in [
        "alpha1_dotD_replay",
        "static_sector_routing",
        "static_1M_shift_rule",
        "static_trace_transfer_normalization",
        "absolute_fiber_origin_for_current_spectral_observables",
    ]:
        require(retired[key] is True, f"retired blocker missing: {key}")

    live = data["live_blockers"]
    for key in [
        "selected_dynamic_overlap_tensor_or_transfer_functor",
        "selected_primitive_C1_contractions",
        "selected_b_selected_or_Hessian_normalization",
        "selected_A_selected_response_operator",
        "selected_sector_response_matrices",
        "selected_deltaTheta_C1_solution",
        "dynamic_visible_routec_operator_source_identity",
    ]:
        require(live[key] is True, f"live blocker missing: {key}")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["A_selected_claimed"] is False, "A_selected claimed")
    require(data["b_selected_claimed"] is False, "b_selected claimed")
    require(data["dynamic_overlap_tensor_claimed"] is False, "dynamic tensor claimed")
    require(data["primitive_C1_contractions_claimed"] is False, "primitive contractions claimed")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
