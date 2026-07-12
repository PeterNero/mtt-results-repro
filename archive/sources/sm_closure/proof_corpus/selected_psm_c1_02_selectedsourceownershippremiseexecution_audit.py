"""Audit the PSM-C1-02 selected source-ownership premise execution cutset."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "selected_psm_c1_02_selectedsourceownershippremiseexecution"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
ROUTE_A = BASE / "route_a_gauge_transport_phifin_trace_execution_attempt.packet.json"
ROUTE_B = BASE / "route_b_independent_row_formula_execution_attempt.packet.json"
DECISION = BASE / "source_ownership_premise_execution_decision.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_SelectedSourceOwnershipPremiseExecution_v1.md"
BUILD = ROOT / "scripts" / "build_selected_psm_c1_02_selectedsourceownershippremiseexecution.py"

STATUS = (
    "MTT_SELECTED_PSM_C1_02_SELECTEDSOURCEOWNERSHIPPREMISEEXECUTION_"
    "BUILT_GAUGE_TRANSPORT_TRACE_OR_INDEPENDENT_ROW_EXECUTION_OPEN"
)
NEXT = "MTT_Selected_GaugeTransported_BN_PhiFin_Trace_or_IndependentComplexRowExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILD)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    decision = load(DECISION)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["name"] == "SelectedSourceOwnershipPremiseExecutionCutsetTheorem", "theorem name mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(candidate["closure_decision"]["Route_A_gauge_transport_trace_required"] is True, "Route A target missing")
    require(candidate["closure_decision"]["Route_B_independent_complex_rows_required"] is True, "Route B target missing")
    require(candidate["closure_decision"]["Route_A_closed_now"] is False, "Route A overclosed")
    require(candidate["closure_decision"]["Route_B_closed_now"] is False, "Route B overclosed")
    require(candidate["closure_decision"]["unpatched_PSM_C1_02_closed"] is False, "unpatched overclosed")
    require(candidate["guardrails_pass"] is True, "guardrails failed")

    require(route_a["status"] == "ROUTE_A_GAUGE_TRANSPORT_PHIFIN_TRACE_EXECUTION_ATTEMPT_OPEN", "Route A status mismatch")
    require(route_a["support_closed"]["finite_phifin_codomain_schema_built"] is True, "Phi_fin schema not built")
    require(route_a["support_closed"]["selected_HYM_connection_subgate_closed"] is True, "HYM connection support missing")
    require(route_a["support_closed"]["untransported_BN_equivalence_rejected"] is True, "BN no-go missing")
    require(route_a["support_closed"]["gauge_transport_repair_identified"] is True, "transport repair missing")
    require(route_a["current_execution"]["Phi_fin_selected_payload_closed"] is False, "Phi_fin overclosed")
    require(route_a["current_execution"]["route_A_premise_closed_now"] is False, "Route A premise overclosed")
    require(route_a["next_required_construction"]["name"] == "SelectedGaugeTransportedBNPhiFinTrace", "Route A next mismatch")

    require(route_b["status"] == "ROUTE_B_INDEPENDENT_ROW_FORMULA_EXECUTION_ATTEMPT_OPEN", "Route B status mismatch")
    require(route_b["support_closed"]["selected_basis_independence_clause"] is True, "basis support missing")
    require(route_b["support_closed"]["differentiated_primitive_overlap_formula_source"] is True, "formula support missing")
    require(route_b["support_closed"]["finite_trace_pairing_source"] is True, "trace pairing support missing")
    require(route_b["current_execution"]["computed_independent_complex_entries"] is False, "complex entries overclosed")
    require(route_b["current_execution"]["exactness_or_error_bound_certificate"] is False, "exactness overclosed")
    require(route_b["current_execution"]["provenance_independent_of_residual_projector_replay"] is False, "provenance overclosed")
    require(route_b["current_execution"]["route_B_premise_closed_now"] is False, "Route B premise overclosed")

    require(decision["status"] == "PREMISE_EXECUTION_REDUCED_TO_GAUGE_TRANSPORT_TRACE_OR_INDEPENDENT_COMPLEX_ROWS", "decision status mismatch")
    require(decision["Route_A_currently_closes"] is False, "decision Route A overclosed")
    require(decision["Route_B_currently_closes"] is False, "decision Route B overclosed")
    require(decision["best_next_artifact"] == NEXT, "decision next mismatch")
    require(next_work["next_required_artifact"] == NEXT, "next work mismatch")
    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["Route_A_gauge_transport_trace_required"] is True, "cert Route A target missing")
    require(cert["Route_B_independent_complex_rows_required"] is True, "cert Route B target missing")
    require("U = exp(-u ad(T3))" in note, "note missing transport")
    require("independent complex row execution" in note, "note missing Route B target")

    for packet in [candidate, route_a, route_b, decision, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
