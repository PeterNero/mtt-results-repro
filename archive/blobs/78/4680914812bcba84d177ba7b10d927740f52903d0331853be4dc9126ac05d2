from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_nativebundleautomorphismgaugegroup_or_parameterassumptionaudit"
STATUS = "MTT_SELECTED_NATIVE_BUNDLE_AUTOMORPHISM_SM_GAUGE_GROUP_Z6_QUOTIENT_CLOSED_PARAMETER_ASSUMPTIONS_RECLASSIFIED"
NEXT = "MTT_Selected_NativeGaugeActionToFullFiniteBimodule_or_DirectGenerativeSMBaseClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "native_bundle_gauge_group_and_parameter_audit.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NativeBundleAutomorphismGaugeGroup_or_ParameterAssumptionAudit_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "packet/candidate mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem failed")
    require(cert["native_low_energy_gauge_lie_algebra_closed"] is True, "native gauge algebra open")
    require(cert["faithful_global_SM_gauge_group_Z6_quotient_closed"] is True, "global gauge quotient open")
    require(cert["global_kernel_order"] == 6, "global kernel order changed")
    require(cert["new_continuous_knobs_A44_A47"] == 0, "new knob introduced")
    require(cert["A40_A46_parameter_assumptions_reclassified"] is True, "parameter audit open")
    require(cert["direct_route_needs_E6_Wilson_line"] is False, "direct route incorrectly depends on Wilson line")
    require(cert["full_Connes_finite_bimodule_closed"] is False, "finite bimodule overclosed")
    require(cert["strict_dimensionful_no_knob_closed"] is False, "metrology overclosed")
    require(packet["parameter_assumption_audit"]["A42_G_route_is_alternative_not_additive"] is True, "alternative primitive double-counted")
    require(packet["parameter_assumption_audit"]["proof_obligations_must_not_be_counted_as_parameters"] is True, "proof obligations counted as knobs")
    for phrase in ["Direct Low-Energy Gauge Selection", "/Z6", "no new continuous gauge or representation knobs", "proof obligations", "alternative universal metrology anchor", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("native bundle gauge group and parameter-assumption audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
