from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralalgebrasummandorequivalentaxiomrevision"
STATUS = "MTT_SELECTED_CN_FROM_COMPLEX_1M_AND_UNIQUE_ANOMALY_FREE_SHARED_HYPERCHARGE_LINE_CLOSED_PROFILE_FINITE_TRIPLE_CLOSED"
NEXT = "MTT_Selected_FiniteSpectralActionAndHiggsInnerFluctuation_or_DirectGenerativeSMActionClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "neutral_summand_and_hypercharge_reduction.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NeutralAlgebraSummandOrEquivalentAxiomRevision_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "packet/candidate mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(cert["theorem_proved"] is True, "theorem failed")
    require(cert["CN_selected_from_complex_1M_carrier"] is True, "C_N not selected")
    require(cert["selected_phase_vector"] == [3, -1, 3], "phase vector changed")
    require(cert["selected_integer_hypercharges_6Y"] == [1, -4, 2, -3, 6, 0], "hypercharges changed")
    require(cert["independent_CN_U1_rejected_by_anomalies"] is True, "extra C_N U1 survived")
    require(cert["shared_circle_reduction_closed"] is True, "shared circle open")
    require(cert["faithful_Z6_SM_gauge_group_preserved"] is True, "Z6 group changed")
    require(cert["full_finite_triple_at_profile_standard_closed"] is True, "profile finite triple open")
    require(cert["strict_no_knob_DF_values_closed"] is False, "profile values promoted")
    require(cert["new_continuous_knobs"] == 0, "new continuous knob introduced")
    require(packet["abelian_phase_system"]["nullspace_dimension"] == 1, "extra anomaly-free U1 exists")
    require(all(value == 0 for value in packet["selected_gauge_line"]["anomalies"].values()), "selected anomaly nonzero")
    require(packet["rejected_extra_directions"]["independent_CN_anomalies"]["U1_cubic"] != 0, "independent C_N cubic anomaly vanished")
    for phrase in ["End_C(1_M) = C_N", "Shared Circle Calculation", "(3,-1,3)", "(1,-4,2,-3,6,0)", "No extra `U(1)`", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("neutral algebra summand and shared hypercharge audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
