"""Build physical action restriction actual-fill attempt or Route B independent run."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalactionrestrictionsourceactualfill_or_routebindependentrun"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_SCAN = PACKET_DIR / "actual_fill_source_scan.packet.json"
ACTUAL_FILL = PACKET_DIR / "physical_action_restriction_actual_fill_attempt.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "actual_fill_validator_result.packet.json"
ROUTE_B_RUN = PACKET_DIR / "route_b_independent_run_actual_status.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_actual_fill_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalActionRestrictionSourceActualFill_or_RouteBIndependentRun_v1.md"

PREVIOUS = DATA / "selected_physicalrestrictionsublemma_or_routebindependentrowsexecution.candidate.json"
PREVIOUS_CUTSET = DATA / "selected_physicalrestrictionsublemma_or_routebindependentrowsexecution" / "next_cutset_after_physical_restriction_probe.packet.json"
RESTRICTION_PROBE = DATA / "selected_physicalrestrictionsublemma_or_routebindependentrowsexecution" / "physical_restriction_sublemma_probe.packet.json"
STRICT_FILL = DATA / "selected_physicalsourcecertificatefill_or_routebindependentrunexecution" / "current_fill_attempt.packet.json"
ROUTE_B_GAP = DATA / "selected_physicalrestrictionsublemma_or_routebindependentrowsexecution" / "route_b_independent_rows_execution_gap.packet.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"

STATUS = "MTT_SELECTED_PHYSICALACTIONRESTRICTIONSOURCEACTUALFILL_OR_ROUTEBINDEPENDENTRUN_BUILT_NO_ACTUAL_SOURCE_ROW_FOUND"
NEXT = "MTT_Selected_SourceRowConstructionFromCorpus_or_RouteBProvenanceFill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "validator": rel(VALIDATOR),
        "payload": rel(path),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr_lines": proc.stderr.strip().splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    previous_cutset = load(PREVIOUS_CUTSET)
    restriction_probe = load(RESTRICTION_PROBE)
    strict_fill = load(STRICT_FILL)
    route_b_gap = load(ROUTE_B_GAP)

    scan = {
        "schema": "MTTPhysicalActionRestrictionActualFillSourceScan.v1",
        "status": "NO_ACTUAL_SAME_BRANCH_ACTION_ROW_FOUND",
        "searched_for": [
            "PhysicalActionRestrictionSourceActualFill",
            "same-branch physical Phi_fin^C1 action row",
            "selected action-to-finite-quotient identity",
            "restriction map to selected finite Weyl quotient",
        ],
        "source_rows_found": [],
        "nearby_non_sources": restriction_probe["candidate_sources_checked"],
        "reason_nearby_items_do_not_fill": [
            "They are validators, probes, templates, or support ledgers.",
            "They do not attach at least five same-branch physical source evidence entries.",
            "They do not set physical_action_restricts_to_selected_finite_Weyl_quotient true.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_a = json.loads(json.dumps(strict_fill["route_A_physical_source_certificate"]))
    actual_fill = {
        "schema": "MTTPhysicalActionRestrictionActualFillAttempt.v1",
        "status": "ACTUAL_FILL_ATTEMPT_REJECTED_SOURCE_ROW_ABSENT",
        "route_A_physical_source_certificate": route_a,
        "route_B_independent_execution": strict_fill["route_B_independent_execution"],
        "formal_support_available": strict_fill["formal_support_available"],
        "actual_source_row_found": False,
        "why_not_filled": restriction_probe["why_not_filled"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "promotion_allowed_now": False,
        "closure_claimed": False,
    }

    route_b_status = {
        "schema": "MTTRouteBIndependentRunActualStatus.v1",
        "status": "ROUTE_B_NOT_EXECUTED_PROVENANCE_FIELDS_OPEN",
        "all_72_primitive_rows_executed": route_b_gap["all_72_primitive_rows_executed"],
        "formal_110_rows_executed": route_b_gap["formal_110_rows_executed"],
        "selected_basis_independent_of_residual_projector": route_b_gap[
            "selected_basis_independent_of_residual_projector"
        ],
        "quadrature_rule_independent_of_locked_target": route_b_gap[
            "quadrature_rule_independent_of_locked_target"
        ],
        "source_independent_of_residual_projector_replay": route_b_gap[
            "source_independent_of_residual_projector_replay"
        ],
        "exactness_or_error_certificates_attached": route_b_gap[
            "exactness_or_error_certificates_attached"
        ],
        "attached_independent_provenance_sources_count": len(
            route_b_gap["attached_independent_provenance_sources"]
        ),
        "ready_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    write_json(SOURCE_SCAN, scan)
    write_json(ACTUAL_FILL, actual_fill)
    write_json(ROUTE_B_RUN, route_b_status)

    validator_result = run_validator(ACTUAL_FILL)
    write_json(VALIDATOR_RESULT, validator_result)

    next_cutset = {
        "schema": "MTTNextCutsetAfterPhysicalActionRestrictionActualFillAttempt.v1",
        "status": "ACTUAL_SOURCE_ROW_ABSENT_ROUTE_B_PROVENANCE_OPEN",
        "closed_now": [
            "actual fill scan found no same-branch physical action restriction row",
            "strict validator replay rejects the actual-fill attempt",
            "Route B formal rows are present but provenance fields are still open",
        ],
        "route_A_required_construction": [
            "derive same-branch physical Phi_fin^C1 action row from MTT/Theta/Phi_fin/Strominger action text",
            "construct restriction map to selected finite Weyl quotient",
            "attach at least five same-branch source evidence entries",
        ],
        "route_B_required_construction": previous_cutset["route_B_next_object"]["must_emit"],
        "recommended_next": {
            "artifact": NEXT,
            "reason": "The repo has no actual same-branch action row; the next step must construct it from corpus action text or fill Route B provenance.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(NEXT_CUTSET, next_cutset)

    candidate = {
        "candidate": "MTTSelectedPhysicalActionRestrictionSourceActualFillOrRouteBIndependentRun",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "previous_cutset": rel(PREVIOUS_CUTSET),
            "restriction_probe": rel(RESTRICTION_PROBE),
            "strict_fill_attempt": rel(STRICT_FILL),
            "route_b_gap": rel(ROUTE_B_GAP),
        },
        "output_packets": {
            "actual_fill_source_scan": rel(SOURCE_SCAN),
            "physical_action_restriction_actual_fill_attempt": rel(ACTUAL_FILL),
            "actual_fill_validator_result": rel(VALIDATOR_RESULT),
            "route_b_independent_run_actual_status": rel(ROUTE_B_RUN),
            "next_cutset_after_actual_fill_attempt": rel(NEXT_CUTSET),
        },
        "what_closes_now": {
            "actual_fill_attempt_executed": True,
            "no_same_branch_physical_action_restriction_row_found": True,
            "strict_validator_rejects_actual_fill_attempt": validator_result["returncode"] == 1,
            "route_B_actual_run_not_executed": True,
            "source_row_construction_or_routeB_provenance_is_now_the_frontier": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "construct_same_branch_physical_action_restriction_row": True,
            "construct_restriction_map_to_selected_finite_Weyl_quotient": True,
            "attach_same_branch_source_evidence": True,
            "route_B_independent_basis_quadrature_provenance": True,
            "route_B_exactness_or_error_certificates": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "no_knob_closure": True,
        },
        "promotion_decision": {
            "physical_action_restriction_actual_fill_succeeded": False,
            "route_B_independent_run_executed": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "theorem": {
            "name": "PhysicalActionRestrictionActualFillNoSourceRowTheorem",
            "proved": True,
            "statement": (
                "The current repo contains probes, templates, and support ledgers for the physical action "
                "restriction sublemma, but no actual same-branch physical Phi_fin^C1 action row or restriction "
                "map to the selected finite Weyl quotient. The strict validator rejects the actual-fill attempt. "
                "The frontier is therefore construction of that source row from corpus action text, or Route B "
                "independent provenance execution."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "patched_SM_parity_closure_preserved": previous["patched_SM_parity_closure_preserved"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalActionRestrictionSourceActualFill_or_RouteBIndependentRun_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "physical_action_restriction_actual_fill_succeeded": False,
        "route_B_independent_run_executed": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalActionRestrictionSourceActualFill or RouteBIndependentRun v1

Status: `{STATUS}`.

I tried the actual fill for the physical restriction row. The repo currently
contains support/probe/template artifacts, but no emitted same-branch physical
`Phi_fin^C1` action row and no restriction map to the selected finite Weyl
quotient.

The strict source-certificate validator still rejects this attempt.

Next frontier:

```text
Route A: construct the source row from MTT/Theta/Phi_fin/Strominger action text
Route B: fill independent basis/quadrature/provenance and exactness certificates
```

Next artifact: `{NEXT}`.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
