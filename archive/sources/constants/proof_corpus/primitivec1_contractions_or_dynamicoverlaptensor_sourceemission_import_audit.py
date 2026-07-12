"""Audit primitive-C1 contraction envelope / dynamic-overlap tensor import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "primitivec1_contractions_or_dynamicoverlaptensor_sourceemission_import.candidate.json"
CERT = ROOT / "certificates" / "primitivec1_contractions_or_dynamicoverlaptensor_sourceemission_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "PrimitiveC1_Contractions_or_DynamicOverlapTensor_SourceEmission_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_primitivec1_contractions_or_dynamicoverlaptensor_sourceemission.py"

STATUS = "PRIMITIVEC1_CONTRACTION_ENVELOPE_IMPORTED_DYNAMIC_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_DynamicOverlapTensor_HessianNormalization_or_GalerkinC1Contractions_ValueEmission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER), "--write"], cwd=ROOT, check=True)
    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")

    for name, value in data["checks"].items():
        require(value is True, f"failed check: {name}")

    envelope = data["contraction_envelope"]
    require(envelope["constructed"] is True, "envelope not constructed")
    require(envelope["active_shift"] == [1, 1], "active shift mismatch")
    require(envelope["fixed_fiber_class"] == [0, 1, 2], "fiber class mismatch")
    require(envelope["phase_route"] == ["u", "e"], "phase route mismatch")
    require(envelope["shift_route"] == ["d", "nuD"], "shift route mismatch")
    require(envelope["selected_as_dynamic_tensor"] is False, "dynamic tensor overclaimed")
    summary = envelope["candidate_summary"]
    require(summary["fixed_fiber_candidates"] == [0, 1, 2], "candidate fibers mismatch")
    require(summary["all_fixed_fiber_rank_three"] is True, "rank-three check failed")
    require(summary["all_fixed_fiber_rank_values"] == [3], "rank values mismatch")

    manifests = data["honest_vs_formal_primitive_manifest"]
    require(
        manifests["honest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
        "honest manifest not open",
    )
    require(manifests["honest_selected_source_verified"] is False, "honest source oververified")
    require(
        manifests["formal_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
        "formal manifest not open",
    )
    require(manifests["formal_selected_source_verified"] is False, "formal source oververified")
    require(manifests["formal_lift_promoted"] is False, "formal lift promoted")

    promotion = data["promotion_test"]
    require(promotion["all_required_fields_emitted"] is False, "all fields overclaimed")
    require(promotion["A_selected_promotion_allowed"] is False, "A promotion overclaimed")
    require(promotion["b_selected_promotion_allowed"] is False, "b promotion overclaimed")
    require(promotion["rank_or_consistency_test_allowed"] is False, "rank test overenabled")
    for key, value in promotion["required_fields"].items():
        require(value is False, f"required field unexpectedly emitted: {key}")

    live = data["live_blockers"]
    for key in [
        "selected_dynamic_overlap_tensor_or_transfer_functor",
        "selected_primitive_C1_contractions",
        "selected_b_selected_or_Hessian_normalization",
        "selected_A_selected_response_operator",
        "selected_sector_response_matrices",
        "selected_deltaTheta_C1_solution",
    ]:
        require(live[key] is True, f"live blocker missing: {key}")

    guardrails = data["guardrails"]
    require(guardrails["contraction_envelope_constructed"] is True, "guardrail envelope missing")
    require(guardrails["selected_dynamic_overlap_tensor_claimed"] is False, "tensor claimed")
    require(guardrails["selected_primitive_C1_contractions_claimed"] is False, "contractions claimed")
    require(guardrails["A_selected_claimed"] is False, "A selected claimed")
    require(guardrails["b_selected_claimed"] is False, "b selected claimed")
    require(guardrails["rank_tests_allowed_now"] is False, "rank tests enabled")
    require(guardrails["observed_data_used"] is False, "observed data used")
    require(guardrails["target_fitting_used"] is False, "target fitting used")
    require(guardrails["full_SM_closure_claimed"] is False, "closure claimed")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
