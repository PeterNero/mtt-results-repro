from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_residualcirclelenscostoperator_or_exactgaugekineticvalueemission"
STATUS = "MTT_SELECTED_Q79_CIRCLE_TORSION_RETARDED_RESOLVENT_CANDIDATE_SUBPPB_PROFILE_MATCH_SOURCE_ROUTING_OPEN"
NEXT = "MTT_Selected_RetardedResolventMultiplicityAndProjectorRoutingTheorem_or_StrictGaugeValuePromotion_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    torsion = load(ROOT / "candidate_data" / SLUG / "q79_shared_circle_chord_torsion.packet.json")
    resolvent = load(ROOT / "candidate_data" / SLUG / "retarded_resolvent_cost_operator.packet.json")
    execution = load(ROOT / "candidate_data" / SLUG / "zero_continuous_parameter_gauge_execution.packet.json")
    contract = load(ROOT / "candidate_data" / SLUG / "next_resolvent_routing_source_contract.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_ResidualCircleLensCostOperator_or_ExactGaugeKineticValueEmission_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == contract["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "builder checks")
    check(torsion["source_status"]["positive_chord_value_exact"], "chord exactness")
    check(resolvent["mathematical_properties"]["denominator_positive"], "denominator")
    check(resolvent["mathematical_properties"]["zero_continuous_parameters"], "parameters")
    check(max(abs(value) for value in execution["relative_residual_ppm_U1_SU3"]) < 1.0, "sub-ppm")
    check(not execution["exact_central_value_equality"], "exactness overclaim")
    check(not execution["prediction_claimed"], "prediction overclaim")
    check(resolvent["source_status"]["formula_discovered_after_profile_residual_known"], "target ranking")
    check(not resolvent["source_status"]["strictly_typed_as_one_selected_hessian_spectrum"], "typing overclaim")
    check(not cert["strict_source_closed"], "source overclaim")
    check(cert["strict_gauge_values_accepted"] == 0, "strict rows")
    for phrase in ["Exact q79 chord torsion", "Retarded-resolvent candidate", "Numerical execution", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("residual circle/Lens cost operator audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
