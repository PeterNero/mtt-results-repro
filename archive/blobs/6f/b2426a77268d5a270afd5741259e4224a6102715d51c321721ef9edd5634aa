"""Audit physical action source-rule / independent kernel-formula promotion kernel."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalactionsourcerule_or_independentprimitivekernelformula"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "physical_action_source_rule_promotion_kernel.packet.json"
ROUTE_B = PACKET_DIR / "independent_primitive_kernel_formula_promotion_kernel.packet.json"
SYNTHESIS = PACKET_DIR / "two_route_source_promotion_synthesis.packet.json"
DECISION = PACKET_DIR / "promotion_kernel_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalActionSourceRule_or_IndependentPrimitiveKernelFormula_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_physicalactionsourcerule_or_independentprimitivekernelformula.py"

STATUS = "MTT_SELECTED_PHYSICALACTIONSOURCERULE_OR_INDEPENDENTPRIMITIVEKERNELFORMULA_BUILT_PROMOTION_KERNEL_OPEN"
NEXT = "MTT_Selected_EnrichedWeylPairPhysicalSourceRule_or_PrimitiveKernelFormulaRows_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    synthesis = load(SYNTHESIS)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")
    require("two exact promotion" in note, "note misses promotion-kernel statement")

    require(route_a["status"] == "PHYSICAL_ACTION_SOURCE_RULE_KERNEL_BUILT_NOT_PROMOTED", "Route A status mismatch")
    require(route_a["theorem_name"] == "SelectedPhiFinC1PhysicalVariationSourceTheorem", "Route A theorem mismatch")
    require(len(route_a["required_clauses"]) == 4, "Route A clause count mismatch")
    require(route_a["conditional_values_if_promoted"]["rank"] == 2, "Route A rank mismatch")
    require(route_a["conditional_values_if_promoted"]["A_transpose_b"] == [12.0, 12.0], "Route A b mismatch")
    require(route_a["route_a_promoted_now"] is False, "Route A overpromoted")
    require(all(value is False for value in route_a["acceptance_tests"].values()), "Route A acceptance tests overfilled")
    require(route_a["already_selected_support"]["canonical_Q_residual_available"] is True, "Q support missing")
    require(route_a["already_selected_support"]["alpha1_dotD_driver_verified"] is True, "alpha1/dotD support missing")

    require(route_b["status"] == "INDEPENDENT_PRIMITIVE_KERNEL_FORMULA_KERNEL_BUILT_NOT_EXECUTED", "Route B status mismatch")
    require(route_b["row_count"] == 72, "Route B row count mismatch")
    require(route_b["checklist_row_count"] == 72, "Route B checklist row count mismatch")
    require(route_b["all_rows_named"] is True, "Route B row names mismatch")
    require(route_b["first_row_id"] == "u:phase:r0c0", "Route B first row mismatch")
    require(route_b["route_b_executed_now"] is False, "Route B overexecuted")
    require(route_b["execution_acceptance_tests"]["locked_target_used_only_after_emission"] is True, "oracle guard missing")
    for key, value in route_b["execution_acceptance_tests"].items():
        if key != "locked_target_used_only_after_emission":
            require(value is False, f"Route B test overfilled: {key}")
    require(all(route_b["replay_diagnostics_available"].values()), "Route B diagnostics missing")

    require(synthesis["status"] == "PROMOTION_SYNTHESIS_BUILT_SOURCE_RULE_PRIMARY", "synthesis status mismatch")
    require(synthesis["source_gap_not_numeric_gap"] is True, "source-gap conclusion missing")
    require(synthesis["route_a"]["objects_to_promote"] == 5, "Route A synthesis mismatch")
    require(synthesis["route_b"]["objects_to_execute"] == 72, "Route B synthesis mismatch")
    require(synthesis["route_ladder_import"]["recommended_next"] == "B_enriched_weylpair_basis_transport_or_vertex_source", "recommended route mismatch")
    require("Superset paths" in synthesis["superset_strategy_use"], "superset discipline missing")

    require(decision["status"] == "PROMOTION_KERNEL_BUILT_CLOSURE_NOT_CLAIMED", "decision status mismatch")
    require(decision["route_a_kernel_built"] is True, "Route A kernel not built")
    require(decision["route_b_kernel_built"] is True, "Route B kernel not built")
    require(decision["route_a_promoted_now"] is False, "decision Route A overpromoted")
    require(decision["route_b_executed_now"] is False, "decision Route B overexecuted")
    require(decision["source_gap_not_numeric_gap"] is True, "decision source-gap missing")
    require(decision["unpatched_dynamic_C1_packet_closed"] is False, "dynamic C1 overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")

    for label, payload in [
        ("candidate", data),
        ("route_a", route_a),
        ("route_b", route_b),
        ("synthesis", synthesis),
        ("decision", decision),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
