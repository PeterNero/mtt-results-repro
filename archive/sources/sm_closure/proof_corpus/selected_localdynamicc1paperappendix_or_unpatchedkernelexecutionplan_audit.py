"""Audit local dynamic-C1 appendix / unpatched execution plan."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_localdynamicc1paperappendix_or_unpatchedkernelexecutionplan"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
APPENDIX_PACKET = PACKET_DIR / "local_dynamic_c1_appendix_sections.packet.json"
UNPATCHED_PLAN = PACKET_DIR / "unpatched_kernel_execution_plan.packet.json"
CLAIM_BOUNDARY = PACKET_DIR / "paper_claim_boundary.packet.json"
APPENDIX_DRAFT = ROOT / "proof_corpus" / "paper_appendix_drafts" / "dynamic_c1" / "theta_execution_dynamic_c1_local_principle_appendix.md"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_LocalDynamicC1PaperAppendix_or_UnpatchedKernelExecutionPlan_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_LOCALDYNAMICC1_PAPERAPPENDIX_OR_UNPATCHEDKERNEL_EXECUTIONPLAN_BUILT_OPEN"
NEXT = "MTT_Selected_UnpatchedWeylPrincipleProof_or_IndependentKernelRowsFirstRun_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    appendix = load(APPENDIX_PACKET)
    plan = load(UNPATCHED_PLAN)
    boundary = load(CLAIM_BOUNDARY)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    draft = APPENDIX_DRAFT.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(APPENDIX_DRAFT.exists(), "appendix draft missing")

    require(appendix["status"] == "APPENDIX_SECTIONS_BUILT_LOCAL_PREMISE_CLAIM_ONLY", "appendix status mismatch")
    require(len(appendix["sections"]) == 3, "appendix section count mismatch")
    require(appendix["guardrails"]["local_premise_explicit"] is True, "local premise guard missing")
    require(appendix["guardrails"]["unpatched_derivation_open"] is True, "unpatched guard missing")
    exact = appendix["sections"][1]["exact_values"]
    require(exact["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A mismatch")
    require(exact["A_transpose_b"] == [12.0, 12.0], "b mismatch")
    require(exact["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")

    require(plan["status"] == "EXECUTION_PLAN_BUILT_VALUES_NOT_EXECUTED", "plan status mismatch")
    require(plan["route_A_unpatched_principle_proof"]["current_status"] == "OPEN", "route A overclosed")
    require(plan["route_B_independent_kernel_rows"]["current_status"] == "OPEN", "route B overclosed")
    require(plan["route_B_independent_kernel_rows"]["minimum_row_families"]["total_rows"] == 110, "row count mismatch")
    require("copying the local-premise values as independent rows" in plan["shared_forbidden_shortcuts"], "copying guard missing")

    require(boundary["status"] == "LOCAL_CLOSED_UNPATCHED_OPEN_BOUNDARY_LOCKED", "boundary status mismatch")
    require(boundary["proved_now"]["local_dynamic_C1_closed_under_selected_weyl_principle"] is True, "local proof missing")
    require(boundary["not_proved_now"]["unpatched_weyl_principle_derivation"] is True, "unpatched overproved")
    require(boundary["superset_strategy_classification"]["mode"] == "single local route with preserved dual exit", "superset mode mismatch")

    require(data["closure_claimed"] is False, "closure overclaimed")
    for key in [
        "paper_appendix_claim_boundary",
        "local_theorem_insertable_without_overclaim",
        "unpatched_route_A_and_B_execution_plan",
        "superset_strategy_classified",
    ]:
        require(data["what_closes_now"][key] is True, f"missing achievement: {key}")
    require("local-premise theorem" in draft, "draft missing local-premise wording")
    require("does not derive the Weyl-variation principle unpatched" in draft, "draft missing boundary sentence")
    require("Route A" in note and "Route B" in note and "110" in note, "note missing route summary")

    for packet in [data, appendix["guardrails"], plan, boundary, cert]:
        guard(packet)

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
