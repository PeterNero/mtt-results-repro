"""Audit q79 AH source selection or Route-C residual reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP = ROOT / "scripts" / "analyze_q79_selected_ah_goodcover_promotion_hym_certificate.py"
SCRIPT = ROOT / "scripts" / "analyze_q79_ah_source_selection_or_routec_residual_reduction.py"
CERT = ROOT / "certificates" / "q79_ah_source_selection_or_routec_residual_reduction_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_ah_source_selection_or_routec_residual_reduction.candidate.json"
TABLE = (
    ROOT
    / "candidate_data"
    / "q79_ah_source_selection_or_routec_residual_reduction"
    / "source_selection_or_residual_reduction_summary.json"
)
PAPER = (
    ROOT
    / "proof_corpus"
    / "Q79_Selected_RouteC_AH_Source_Selection_or_RouteC_SelectedResidual_v1.md"
)

STATUS = "Q79_AH_GOODCOVER_EQUIVALENCE_PROVED_SOURCE_OR_ROUTEC_RESIDUAL_OPEN"
NEXT = "Q79_Selected_Monad_Difference_L2_Source_and_OperatorPic0_or_RouteC_Residual_v1"


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
    require(table == cert["source_selection_or_residual_summary"], "summary table mismatch", failures)
    require(cert["status"] == STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure must stay false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)

    summary = cert["source_selection_or_residual_summary"]
    equiv = cert["AH_goodcover_representative_equivalence_theorem"]
    reduction = cert["selected_AH_source_reduction"]
    routec = cert["routec_residual_bypass"]
    contract = cert["minimal_remaining_contract"]
    remaining = cert["what_remains_open"]

    require(summary["literal_goodcover_independent_blocker_removed"] is True, "good-cover blocker not removed", failures)
    require(summary["AH_to_goodcover_representative_equivalence_proved"] is True, "AH/good-cover equivalence false", failures)
    require(summary["ordered_source_lane_reduction_imported"] is True, "ordered lane reduction missing", failures)
    require(summary["ordered_layer_pic0_quotient_imported"] is True, "ordered Pic0 quotient missing", failures)
    require(summary["operator_layer_pic0_recheck_required"] is True, "operator Pic0 recheck missing", failures)
    require(summary["selected_routec_residual_available"] is False, "Route-C residual overclosed", failures)
    require(summary["selected_source_promotion_available"] is False, "selected-source promotion overclosed", failures)
    require(summary["full_HYM_or_SM_closure_claimed"] is False, "full closure overclaimed", failures)

    require(equiv["proved"] is True, "equivalence theorem not proved", failures)
    require(equiv["imports_AH_automorphy_exists"] is True, "AH automorphy not imported", failures)
    require(equiv["imports_pullback_cech_validator_passes"] is True, "Cech validator not imported", failures)
    require(equiv["imports_AH_yoneda_product_law"] is True, "AH Yoneda law not imported", failures)
    require(equiv["does_not_select_AH_source"] is True, "AH source overselected", failures)
    require(equiv["does_not_resolve_Pic0"] is True, "Pic0 overresolved", failures)

    require(reduction["proved"] is True, "AH source reduction not proved", failures)
    require(
        reduction["monad_sufficiency_relative_theorem_proved"] is True,
        "monad sufficiency theorem not imported",
        failures,
    )
    require(
        reduction["monad_sufficiency_only_source_and_pic0_changed"] is True,
        "monad promotion delta changed extra fields",
        failures,
    )
    require(reduction["ordered_layer_pic0_quotient_proved"] is True, "Pic0 quotient not imported", failures)
    require(reduction["terminal_lane_reduction_proved"] is True, "terminal lane reduction not imported", failures)
    require(
        reduction["terminal_lane_hypothetical_selected_packet_passes"] is True,
        "terminal lane hypothetical packet should pass",
        failures,
    )
    require(
        "source.selected_by_mtt is not true" in reduction["strict_open_items_after_ordered_pic0_quotient"],
        "strict open items missing source.selected_by_mtt",
        failures,
    )
    require(
        all("Pic0" not in item for item in reduction["strict_open_items_after_ordered_pic0_quotient"]),
        "ordered-layer open items should have Pic0 removed",
        failures,
    )

    require(routec["attempted"] is True, "Route-C bypass not attempted", failures)
    require(routec["route_c_residual_validator_pass"] is False, "Route-C validator overpassed", failures)
    require(routec["selected_source_promotion_validator_pass"] is False, "selected-source validator overpassed", failures)
    require(routec["selected_hym_operator_source_verified"] is False, "selected HYM operator oververified", failures)
    require(routec["route_c_honest_operator_pipeline_pass"] is False, "Route-C pipeline overpassed", failures)
    require(routec["bypass_open"] is True, "Route-C bypass should remain open", failures)

    require(contract["goodcover_table_independent_search"] == "removed", "good-cover search not removed", failures)
    require(len(contract["must_supply_one_of"]) == 2, "contract should have two alternatives", failures)
    require("operator-layer Pic0 selection or physical quotient" in contract["must_recheck_if_operator_path"], "operator Pic0 recheck absent", failures)

    for key in (
        "selected_terminal_monad_lane_L3_minus_K2_source_selector",
        "binding_L3_minus_K2_to_AH_or_Cech_transitions",
        "operator_layer_Pic0_selection_or_quotient",
        "selected_RouteC_residual_values",
        "same_source_D_E_Riesz_Green_dotD",
        "full_SM_or_no_knob_closure",
    ):
        require(remaining[key] is True, f"open flag false: {key}", failures)

    for key, value in cert["guardrails"].items():
        require(value is False, f"guardrail violated: {key}", failures)

    for phrase in (
        "AH/good-cover representative equivalence",
        "does not select the AH source",
        "does not close operator-layer `Pic0`",
        "Good-cover table independent search: `removed`",
        "Q79AHSourceOrRouteCResidualReductionTheorem",
        NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 AH source selection or Route-C residual reduction audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 AH source selection or Route-C residual reduction audit PASS")
    print(f"status: {cert['status']}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
