"""Audit the dynamic C1 breakthrough decision import."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
JSON_PATH = ROOT / "selected_dynamicc1_breakthrough_axiom_or_galerkin_decision.import.json"
MD_PATH = ROOT / "DynamicC1_Breakthrough_Attempt_Axiom_or_Galerkin_Decision_v1.md"

EXPECTED_STATUS = "BREAKTHROUGH_CONDITIONAL_AXIOM_READY_STRICT_UNPATCHED_OPEN"
EXPECTED_NEXT = "MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    text = MD_PATH.read_text(encoding="utf-8", errors="ignore")

    require(data["status"] == EXPECTED_STATUS, "unexpected status")
    require(data["next_required_artifact"] == EXPECTED_NEXT, "unexpected next artifact")
    require(data["closure_claimed"] is False, "strict closure must not be claimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    support = data["closed_support"]
    require(all(support.values()), "all closed support fields should be true")

    normal = data["conditional_normal_form"]
    require(normal["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "unexpected A^T A")
    require(normal["A_transpose_b"] == [12.0, 12.0], "unexpected A^T b")
    require(normal["deltaTheta_C1"] == [1.0, 1.0], "unexpected deltaTheta")
    require(normal["rank"] == 2, "unexpected rank")

    lane_a = data["lane_A_axiom"]
    require(lane_a["name"] == "DifferentiatedPhiFinC1ResidualProjectorAxiom", "wrong axiom")
    require(lane_a["contract_ready"] is True, "axiom contract not ready")
    require(lane_a["inserted_now"] is False, "axiom should not be recorded inserted")
    require(lane_a["proved_unpatched_now"] is False, "unpatched proof should remain open")
    require(lane_a["if_accepted_closes_SM_parity_dynamic_C1"] is True, "axiom implication missing")

    for phrase in [
        "closest available breakthrough",
        "DifferentiatedPhiFinC1ResidualProjectorAxiom",
        "strict unpatched/no-knob closure remains open",
    ]:
        require(phrase in text, f"missing markdown phrase: {phrase}")

    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    print("PASS selected_dynamicc1_breakthrough_axiom_or_galerkin_decision.import.json")


if __name__ == "__main__":
    main()
