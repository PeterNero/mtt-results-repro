from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_normalizeddeterminantactionfrommtthessian_or_independentgaugeprofiletest"
STATUS = "MTT_SELECTED_FINITE_TRACE_PROJECTOR_NORMALIZATION_UNIQUE_LEGACY_INDEPENDENT_PROFILE_COMPATIBLE_PHYSICAL_HESSIAN_IDENTITY_OPEN"
NEXT = "MTT_Selected_PhysicalKineticHessianBlockIdentity_or_ModernPrecisionGaugeValidation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    trace = load(ROOT / "candidate_data" / SLUG / "finite_trace_and_projector_uniqueness.packet.json")
    validation = load(ROOT / "candidate_data" / SLUG / "buttazzo_legacy_independent_profile_test.packet.json")
    gate = load(ROOT / "candidate_data" / SLUG / "remaining_physical_hessian_action_gate.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NormalizedDeterminantActionFromMTTHessian_or_IndependentGaugeProfileTest_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == gate["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "builder checks")
    check(trace["general_finite_trace_theorem"]["proved"], "trace theorem")
    check(trace["closure"]["A72_trace_normalizations_are_not_knobs"], "trace knob")
    check(trace["closure"]["A72_projector_rank_coefficients_are_not_knobs"], "projector knob")
    check(validation["covariance_test"]["compatible"], "legacy validation")
    check(validation["covariance_test"]["p_value"] > 0.05, "p value")
    check(not validation["frozen_formula"]["retuned"], "retuning")
    check(not validation["scope"]["modern_high_precision_validation_closed"], "precision overclaim")
    check(all(gate["closed"].values()), "closed gate fields")
    check(not gate["strict_physical_action_selected"], "physical action overclaim")
    check(cert["strict_gauge_values_accepted"] == 0, "strict rows")
    for phrase in ["Trace selection", "Independent legacy test", "Remaining physical gate", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("normalized determinant action / independent profile audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
