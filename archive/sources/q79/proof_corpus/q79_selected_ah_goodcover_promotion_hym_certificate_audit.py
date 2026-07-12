"""Audit q79 selected AH/good-cover promotion and conditional HYM bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP = ROOT / "scripts" / "analyze_q79_global_destabilizer_enumeration_or_selected_residual.py"
SCRIPT = ROOT / "scripts" / "analyze_q79_selected_ah_goodcover_promotion_hym_certificate.py"
CERT = ROOT / "certificates" / "q79_selected_ah_goodcover_promotion_hym_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_selected_ah_goodcover_promotion_hym_certificate.candidate.json"
TABLE = (
    ROOT
    / "candidate_data"
    / "q79_selected_ah_goodcover_promotion_hym_certificate"
    / "selected_ah_goodcover_promotion_summary.json"
)
PAPER = (
    ROOT
    / "proof_corpus"
    / "Q79_Selected_RouteC_Selected_AH_or_GoodCover_Promotion_and_HYM_Certificate_v1.md"
)

STATUS = "Q79_SELECTED_ROUTEC_REFLEXIVE_HULL_AND_CONDITIONAL_HYM_BRIDGE_PROVED_AH_SELECTION_OPEN"
NEXT = "Q79_Selected_RouteC_AH_Source_Selection_or_RouteC_SelectedResidual_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def run(script: Path, failures: list[str]) -> None:
    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    require(proc.returncode == 0, f"{script.name} failed:\n{proc.stdout}", failures)


def main() -> int:
    failures: list[str] = []
    run(DEP, failures)
    run(SCRIPT, failures)
    for path in (CERT, CANDIDATE, TABLE, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)
    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    table = load(TABLE)
    paper = PAPER.read_text(encoding="utf-8")

    require(cert == candidate, "certificate and candidate JSON differ", failures)
    require(table == cert["promotion_summary"], "promotion summary table mismatch", failures)
    require(cert["status"] == STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure must stay false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)

    summary = cert["promotion_summary"]
    reflexive = cert["rank_one_torsion_free_reflexive_hull_theorem"]
    stability = cert["reduced_AH_to_full_stability_implication"]
    hym = cert["HYM_bridge"]
    selected = cert["selected_AH_goodcover_status"]
    remaining = cert["what_remains_open"]

    require(summary["reflexive_hull_reduction_proved"] is True, "reflexive hull summary false", failures)
    require(
        summary["conditional_reduced_AH_to_full_stability_bridge_proved"] is True,
        "conditional stability summary false",
        failures,
    )
    require(summary["conditional_HYM_bridge_proved"] is True, "conditional HYM summary false", failures)
    require(summary["selected_AH_or_goodcover_source_supplied"] is False, "selected AH overclaimed", failures)
    require(summary["selected_Gauduchon_chamber_supplied"] is False, "Gauduchon overclaimed", failures)
    require(summary["full_HYM_proved"] is False, "full HYM overclaimed", failures)
    require(summary["full_SM_closure_proved"] is False, "full SM overclaimed", failures)

    require(reflexive["proved"] is True, "reflexive hull theorem not proved", failures)
    require("saturation" in reflexive["statement"], "reflexive theorem missing saturation", failures)
    require("line bundle" in reflexive["statement"], "reflexive theorem missing line bundle", failures)
    require(reflexive["uses_selected_source_data"] is False, "reflexive theorem should be source-independent", failures)

    require(stability["proved_conditionally"] is True, "stability bridge not conditional-proved", failures)
    require(stability["imports_reduced_AH_stability"] is True, "reduced AH stability not imported", failures)
    require(stability["imports_reflexive_hull_reduction"] is True, "reflexive hull not imported", failures)
    require("slope-stable" in stability["conclusion_under_condition"], "stability conclusion missing slope-stable", failures)
    require(len(stability["why_condition_is_still_open"]) >= 3, "condition-open list too short", failures)

    require(hym["li_yau_gauduchon_support_in_corpus"] is True, "Li-Yau/Gauduchon corpus support missing", failures)
    require(hym["proved_conditionally"] is True, "HYM bridge not conditional-proved", failures)
    require(hym["operator_source_not_emitted"] is True, "HYM operator source over-emitted", failures)

    require(selected["AH_degree_product_law_verified"] is True, "AH product law not verified", failures)
    require(
        selected["AH_reduced_boundaries_promoted_conditionally"] is True,
        "AH boundary promotion missing",
        failures,
    )
    require(selected["AH_selected_by_mtt"] is False, "AH source overselected", failures)
    require(selected["AH_neutral_pic0_selected_by_mtt"] is False, "neutral Pic0 overselected", failures)
    require(selected["pullback_cech_validator_passes"] is True, "pullback Cech validator not passing", failures)
    require(
        selected["pullback_cech_role"] == "UNSELECTED_FIXTURE",
        "pullback Cech role should remain UNSELECTED_FIXTURE",
        failures,
    )
    require(selected["AH_automorphy_constructed"] is True, "AH automorphy not constructed", failures)
    require(selected["AH_automorphy_selected_by_mtt"] is False, "AH automorphy overselected", failures)

    for key in (
        "selected_AH_representative_or_literal_goodcover_Cech_source",
        "operator_layer_neutral_Pic0_selection_or_quotient",
        "selected_Gauduchon_chamber_source",
        "selected_HYM_connection_values",
        "selected_RouteC_residual_values",
        "same_source_D_E_Riesz_Green_dotD",
        "full_SM_or_no_knob_closure",
    ):
        require(remaining[key] is True, f"open flag false: {key}", failures)

    for key, value in cert["guardrails"].items():
        require(value is False, f"guardrail violated: {key}", failures)

    for phrase in (
        "reflexive hull reduction",
        "conditional HYM bridge",
        "Full HYM is **not claimed**",
        "selected AH/good-cover source is still open",
        "Q79SelectedRouteCConditionalHYMBridgeTheorem",
        NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 selected AH/good-cover promotion audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 selected AH/good-cover promotion audit PASS")
    print(f"status: {cert['status']}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
