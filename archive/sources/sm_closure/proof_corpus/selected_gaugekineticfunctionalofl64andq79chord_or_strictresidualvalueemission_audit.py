from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_gaugekineticfunctionalofl64andq79chord_or_strictresidualvalueemission"
STATUS = "MTT_SELECTED_TYPED_L64_Q79_PROJECTOR_FUNCTIONAL_CONSTRUCTED_ZERO_PARAMETER_SUB2PPM_SOURCE_ACTION_OPEN"
NEXT = "MTT_Selected_GaugeKineticActionDerivationAndFrozenProfileValidation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    functional = load(ROOT / "candidate_data" / SLUG / "typed_l64_q79_projector_functional.packet.json")
    grid = load(ROOT / "candidate_data" / SLUG / "canonical_projector_grid.packet.json")
    execution = load(ROOT / "candidate_data" / SLUG / "frozen_zero_parameter_gauge_execution.packet.json")
    contract = load(ROOT / "candidate_data" / SLUG / "next_same_action_derivation_and_validation_contract.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_GaugeKineticFunctionalOfL64AndQ79Chord_or_StrictResidualValueEmission_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == contract["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "builder checks")
    check(all(functional["typing"].values()), "typing")
    check(grid["trial_count"] == 36, "grid")
    check(grid["winner"]["q_projector"] == "Z7_nontrivial", "q winner")
    check(grid["winner"]["e_projector"] == "LensZ4_nontrivial", "e winner")
    check(grid["winner_improvement_over_runner_up"] > 5.0, "winner margin")
    check(execution["both_ratios_within_2ppm"], "numerical gate")
    check(execution["new_continuous_parameters"] == 0, "parameters")
    check(not execution["exact_central_value_equality"], "exactness overclaim")
    check(not execution["prediction_profile_promoted"], "promotion overclaim")
    check(not cert["same_action_source_closed"], "action overclaim")
    check(not cert["independent_validation_closed"], "validation overclaim")
    check(cert["strict_gauge_values_accepted"] == 0, "strict rows")
    for phrase in ["Typed functional", "Canonical grid", "Frozen execution", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("typed L64/q79 gauge functional audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
