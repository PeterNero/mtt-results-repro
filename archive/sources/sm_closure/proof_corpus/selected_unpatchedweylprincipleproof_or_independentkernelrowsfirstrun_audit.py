"""Audit unpatched Weyl-principle / independent kernel rows first run."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_unpatchedweylprincipleproof_or_independentkernelrowsfirstrun"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_unpatched_weyl_principle_reaudit.packet.json"
ROUTE_B = PACKET_DIR / "route_b_independent_kernel_rows_first_run.packet.json"
CUTSET = PACKET_DIR / "shared_source_theorem_cutset.packet.json"
DECISION = PACKET_DIR / "two_route_first_run_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_UnpatchedWeylPrincipleProof_or_IndependentKernelRowsFirstRun_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_UNPATCHEDWEYLPRINCIPLEPROOF_OR_INDEPENDENTKERNELROWSFIRSTRUN_BUILT_SOURCE_THEOREM_OPEN"
NEXT = "MTT_Selected_FiniteC1SourceIdentityTheorem_or_NewIndependentRows_v1"


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
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    cutset = load(CUTSET)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next mismatch")

    require(route_a["status"] == "ROUTE_A_REAUDITED_PHYSICAL_SELECTION_STILL_OPEN", "route A status mismatch")
    require(route_a["route_A_accepts"] is False, "route A overaccepted")
    require(route_a["unpatched_principle_derived_now"] is False, "principle overderived")
    require(route_a["minimal_physical_certificate_built"] is True, "minimal certificate missing")
    require(route_a["minimal_physical_certificate_filled"] is False, "minimal certificate overfilled")
    require(route_a["closed_support_count"] >= 10, "route A support unexpectedly weak")

    require(route_b["status"] == "ROUTE_B_FIRST_RUN_EXECUTED_VALIDATOR_REJECTS_SOURCE_INDEPENDENCE", "route B status mismatch")
    require(route_b["row_counts"]["total_rows"] == 110, "row count mismatch")
    require(route_b["fresh_validator_result"]["ok"] is False, "route B overaccepted")
    require(route_b["fresh_validator_result"]["exit_code"] == 1, "route B validator exit mismatch")
    require(route_b["closed_fields_in_attempt"]["finite_weyl_trace_rule_feeds_all_rows"] is True, "trace rule not closed")
    require(route_b["open_fields_in_attempt"]["source_independent_of_residual_projector_replay"] is False, "source independence overclosed")

    require(cutset["status"] == "SINGLE_SHARED_SOURCE_THEOREM_IDENTIFIED_NOT_PROVED", "cutset status mismatch")
    require(cutset["theorem_name"] == "SelectedFiniteC1SourceIdentityTheorem", "theorem name mismatch")
    require(cutset["proved_now"] is False, "cutset overproved")
    require(len(cutset["required_clauses"]) == 6, "clause count mismatch")

    require(decision["status"] == "BOTH_ROUTES_EXECUTED_CURRENTLY_OPEN_SHARED_THEOREM_NEXT", "decision status mismatch")
    require(decision["route_A_accepts"] is False, "decision route A overaccepted")
    require(decision["route_B_accepts"] is False, "decision route B overaccepted")
    require(decision["unpatched_dynamic_C1_closed"] is False, "unpatched overclosed")
    require(decision["next_required_artifact"] == NEXT, "decision next mismatch")
    require(decision["superset_strategy_used"]["locked_target"] == "same selected finite C1 source identity, not measured SM data", "superset target mismatch")

    require(data["closure_claimed"] is False, "closure overclaimed")
    for key in [
        "route_A_reaudited_against_local_boundary",
        "route_B_first_run_executed_against_strict_validator",
        "shared_source_identity_theorem_named",
        "superset_paths_reconciled_to_locked_target",
    ]:
        require(data["what_closes_now"][key] is True, f"missing achievement: {key}")
    require("SelectedFiniteC1SourceIdentityTheorem" in note, "note missing theorem")
    require("No observed masses" in note, "note missing guardrail")

    for packet in [data, route_a, route_b, cutset, decision, cert]:
        guard(packet)

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
