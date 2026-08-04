from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_chargedleptondualmetricsignandspectralactioncompleteness"
STATUS = "MTT_SELECTED_COMMON_POSITIVE_HEAT_SIGN_NOGO_AND_UNIQUE_ANCHORING_GRADING_BUILT_PHYSICAL_INSERTION_LAW_OPEN"
NEXT = "MTT_Selected_AnchoringParityInsertionLaw_or_IndependentKineticGramDerivation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    nogo = load(ROOT / "candidate_data" / SLUG / "common_positive_heat_sign_no_go.packet.json")
    grading = load(ROOT / "candidate_data" / SLUG / "anchoring_parity_grading_construction.packet.json")
    corpus = load(ROOT / "candidate_data" / SLUG / "protospinor_source_support_and_missing_insertion_law.packet.json")
    gate = load(ROOT / "candidate_data" / SLUG / "remaining_anchoring_parity_action_gate.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_ChargedLeptonDualMetricSignAndSpectralActionCompleteness_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "builder checks")
    check(nogo["theorem"]["proved"], "nogo")
    check(not nogo["application"]["single_ungraded_heat_function_sufficient"], "ungraded overclaim")
    check(grading["algebra"]["J_anchor_squared_equals_P_active"], "grading algebra")
    check(grading["response"]["exact_match"], "grading response")
    check(not grading["physical_action_insertion_selected"], "insertion overclaim")
    check(all(corpus["closed_classification_support"].values()), "corpus classification")
    check(not any(corpus["missing_statement_search"].values()), "missing law accidentally found")
    check(all(gate["closed"].values()), "closed gate")
    check(gate["remaining_relative_ratio_source_dimension"]["continuous"] == 0, "continuous dimension")
    check(gate["remaining_relative_ratio_source_dimension"]["discrete_if_J_anchor_law_not_proved"] == 1, "sign bit")
    check(cert["strict_gauge_values_accepted"] == 0, "strict values")
    for phrase in ["Positive-response no-go", "Unique anchoring grading", "Corpus result", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("charged-lepton dual-metric sign audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
