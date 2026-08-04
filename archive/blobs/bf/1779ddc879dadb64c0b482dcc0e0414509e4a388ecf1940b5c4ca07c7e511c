from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_gaugekineticactionderivationandfrozenprofilevalidation"
STATUS = "MTT_SELECTED_A72_FUNCTIONAL_DERIVED_FROM_ONE_NORMALIZED_DETERMINANT_ACTION_PHYSICAL_SELECTION_VALIDATION_OPEN"
NEXT = "MTT_Selected_NormalizedDeterminantActionFromMTTHessian_or_IndependentGaugeProfileTest_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    action = load(ROOT / "candidate_data" / SLUG / "normalized_determinant_action_derivation.packet.json")
    selection = load(ROOT / "candidate_data" / SLUG / "physical_action_selection_gate.packet.json")
    validation = load(ROOT / "candidate_data" / SLUG / "frozen_external_validation_protocol.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_GaugeKineticActionDerivationAndFrozenProfileValidation_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == validation["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "builder checks")
    check(action["response_theorem"]["matches_A72_delta_q"], "delta q")
    check(action["response_theorem"]["matches_A72_delta_e"], "delta e")
    check(all(action["properties"].values()), "action properties")
    check(selection["closed"]["one_action_representation_exists"], "action existence")
    check(not selection["strict_same_action_source_closed"], "physical source overclaim")
    check(validation["frozen_formula"]["retuning_forbidden"], "freeze")
    check(not validation["independent_validation_closed"], "validation overclaim")
    check(not validation["external_primary_reference"]["direct_numeric_validation_admitted"], "external admission")
    check(cert["strict_gauge_values_accepted"] == 0, "strict rows")
    for phrase in ["One-action derivation", "Remaining selection", "Frozen validation", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("gauge kinetic action derivation audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
