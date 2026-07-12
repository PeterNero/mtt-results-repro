"""Audit enriched Weyl-pair physical-source rule / primitive-row fallback gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_enrichedweylpairphysicalsourcerule_or_primitivekernelformularows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "enriched_weylpair_physical_source_rule_gate.packet.json"
ROUTE_B = PACKET_DIR / "primitive_kernel_formula_rows_fallback_gate.packet.json"
DYNAMIC = PACKET_DIR / "remaining_dynamic_promotion_cutset.packet.json"
DECISION = PACKET_DIR / "enriched_weylpair_gate_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_EnrichedWeylPairPhysicalSourceRule_or_PrimitiveKernelFormulaRows_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_enrichedweylpairphysicalsourcerule_or_primitivekernelformularows.py"

STATUS = "MTT_SELECTED_ENRICHEDWEYLPAIRPHYSICALSOURCERULE_OR_PRIMITIVEKERNELFORMULAROWS_BUILT_STATIC_CLOSED_DYNAMIC_OPEN"
NEXT = "MTT_Selected_DynamicC1TransferPrimitiveTensorHessian_or_IndependentRows_v1"


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
    dynamic = load(DYNAMIC)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")
    require("retires the static part" in note, "note misses static retirement")

    require(route_a["status"] == "ENRICHED_WEYLPAIR_STATIC_SOURCE_CLOSED_PHYSICAL_DYNAMIC_RULE_OPEN", "Route A status mismatch")
    require(route_a["static_source_provenance_closed"] is True, "static provenance not closed")
    require(all(route_a["source_level_carrier_closed"].values()), "source carrier not closed")
    require(route_a["static_sector_route_closed"] is True, "sector route not closed")
    require(route_a["static_normalization_closed"] is True, "normalization not closed")
    require(route_a["conditional_A_rank"] == 2, "conditional rank mismatch")
    require(route_a["conditional_solve_consistent"] is True, "conditional solve inconsistent")
    require(len(route_a["remaining_physical_rule_requirements"]) == 5, "remaining rule requirements mismatch")
    require(route_a["physical_source_rule_promoted_now"] is False, "physical rule overpromoted")

    require(route_b["status"] == "PRIMITIVE_KERNEL_FORMULA_ROWS_FALLBACK_READY_NOT_EXECUTED", "Route B status mismatch")
    require(route_b["row_count"] == 72, "Route B row count mismatch")
    require(route_b["all_rows_named"] is True, "Route B rows unnamed")
    require(route_b["route_b_executed_now"] is False, "Route B overexecuted")

    require(dynamic["status"] == "STATIC_SOURCE_RETIRED_DYNAMIC_CUTSET_EXACT", "dynamic cutset status mismatch")
    retired = dynamic["retired_blockers"]
    require(retired["source_level_weylpair_provenance_open"] is False, "source provenance still open")
    require(retired["static_sector_routing_open"] is False, "static routing still open")
    require(retired["static_transfer_normalization_open"] is False, "static normalization still open")
    require(retired["operator_alpha1_support_closed_for_frontier"] is True, "alpha1 support not closed")
    require(all(dynamic["active_dynamic_cutset"].values()), "dynamic cutset not all active/open")
    require(dynamic["conditional_values_ready"]["conditional_rank"] == 2, "dynamic conditional rank mismatch")
    require(dynamic["conditional_values_ready"]["A_transpose_b_if_promoted"] == [12.0, 12.0], "dynamic b mismatch")
    require(dynamic["source_gap_not_numeric_gap"] is True, "source-gap conclusion missing")

    require(decision["status"] == "ENRICHED_WEYLPAIR_GATE_BUILT_STATIC_RETIRED_DYNAMIC_NOT_CLOSED", "decision status mismatch")
    require(decision["static_source_provenance_closed"] is True, "decision static not closed")
    require(decision["dynamic_physical_source_rule_closed"] is False, "dynamic rule overclosed")
    require(decision["primitive_formula_rows_executed"] is False, "primitive rows overexecuted")
    require(decision["unpatched_dynamic_C1_packet_closed"] is False, "dynamic C1 overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")

    for label, payload in [
        ("candidate", data),
        ("route_a", route_a),
        ("route_b", route_b),
        ("dynamic", dynamic),
        ("decision", decision),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
