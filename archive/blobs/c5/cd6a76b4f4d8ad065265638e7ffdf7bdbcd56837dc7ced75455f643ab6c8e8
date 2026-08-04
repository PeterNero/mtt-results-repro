from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_samegeometryqutrittosmalgebrabridge_or_generativebasefrontier"
STATUS = "MTT_SELECTED_SAME_GEOMETRY_QUTRIT_TO_SM_ALGEBRA_CONDITIONAL_BRIDGE_CLOSED_SOURCE_SELECTION_OPEN"
NEXT = "MTT_Selected_ClassLaneProjectorsAndWeakRealStructureSourceTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "same_geometry_qutrit_to_sm_algebra_bridge.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_SameGeometryQutritToSMAlgebraBridge_or_GenerativeBaseFrontier_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "packet/candidate mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "bridge theorem failed")
    require(cert["embedded_local_QFT_recovery_closed"] is True, "closed QFT recovery reopened")
    require(cert["standard_quantization_imported"] is True, "quantization scope hidden")
    require(cert["direct_qutrit_equals_SM_algebra_rejected"] is True, "direct algebra mismatch not guarded")
    require(cert["conditional_C_H_M3_bridge_closed"] is True, "conditional SM algebra bridge open")
    require(cert["candidate_SM_algebra_real_dimension"] == 24, "candidate algebra dimension changed")
    for key in ["class_lane_assignment_selected", "weak_real_structure_selected", "representation_and_anomaly_packet_closed", "same_geometry_generative_base_closed"]:
        require(cert[key] is False, f"source selection overclosed: {key}")
    no_go = packet["direct_identification_no_go"]
    require((no_go["A_Q_real_dimension"], no_go["A_F_real_dimension"]) == (54, 24), "algebra dimensions changed")
    require((no_go["A_Q_center_real_dimension"], no_go["A_F_center_real_dimension"]) == (6, 5), "center dimensions changed")
    bridge = packet["conditional_same_geometry_bridge"]
    require(bridge["quaternion_real_rank"] == 4, "quaternion rank changed")
    require(bridge["max_quaternion_multiplication_residual"] < 1e-15, "quaternion multiplication failed")
    require(bridge["max_antiunitary_fixed_residual"] < 1e-15, "real structure failed")
    require(packet["epistemic_policy"]["observed_SM_values_used"] is False, "observed values entered bridge")
    require(packet["epistemic_policy"]["embedded_QFT_recovery_reopened"] is False, "old recovery blocker reopened")
    for phrase in ["already closed at the declared standard", "cannot simply be renamed", "exact real-star-algebra reduction", "cannot be silently reused", "genuinely generative MTT base", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("same-geometry qutrit-to-SM algebra bridge audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
