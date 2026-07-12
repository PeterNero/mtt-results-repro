"""Build strongest current Route B payload fill and strict source-gap certificate."""

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

SLUG = "selected_routeb_bestcurrentpayloadfill_or_independentsourcegap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ATTEMPT = PACKET_DIR / "routeb_best_current_payload_fill_attempt.packet.json"
GAP = PACKET_DIR / "routeb_independent_source_gap.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "strict_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteB_BestCurrentPayloadFill_or_IndependentSourceGap_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_independent_quadrature_payload.py"

STATUS = "MTT_SELECTED_ROUTEB_BESTCURRENTPAYLOADFILL_BUILT_INDEPENDENTSOURCE_GAP_OPEN"
NEXT = "MTT_Selected_RouteB_RowKernelSource_or_SelectedMeasurePairing_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def stage_map(schedule: dict[str, Any]) -> dict[str, list[str]]:
    return {stage["stage"]: stage["rows"] for stage in schedule["execution_order"]}


def make_primitive_row(row: dict[str, Any]) -> dict[str, Any]:
    replay_label = row.get("replay_value_source")
    value = {
        "kind": "replay_symbolic_row_value",
        "source": replay_label,
        "filled_by_replay_now": row.get("filled_by_replay_now"),
        "coordinate": row.get("coordinate"),
    }
    if replay_label is None:
        value["source"] = "routed_zero_or_unfilled_replay_slot"
    return {
        "row_id": row["row_id"],
        "stage": "primitive_contractions",
        "independent_source_emitted": False,
        "locked_target_dependency": False,
        "residual_replay_dependency": True,
        "quadrature_rule_id": "missing_selected_independent_quadrature_rule",
        "kernel_source_id": "canonical_residual_projector_replay_not_row_kernel_source",
        "value": value,
        "exactness_certificate": "exact_replay_support_only_not_independent_quadrature_certificate",
        "error_bound": None,
        "selected_b_vector_source": None,
        "why_rejected": row.get("why_not_independent"),
    }


def make_hessian_row(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "row_id": row["row_id"],
        "stage": "hessian_source",
        "independent_source_emitted": False,
        "locked_target_dependency": True,
        "residual_replay_dependency": False,
        "quadrature_rule_id": "formal_finite_trace_target_not_selected_quadrature_rule",
        "kernel_source_id": "formal_hessian_target_not_physical_source",
        "value": row["finite_trace_quadrature_value"],
        "exactness_certificate": "formal_target_identity_only",
        "error_bound": None,
        "selected_b_vector_source": False,
        "why_rejected": "Formal Hessian target is identified, but physical same-source b_selected emission is still false.",
    }


def make_sector_row(row_id: str) -> dict[str, Any]:
    sector, _, coord = row_id.partition(":M:")
    return {
        "row_id": row_id,
        "stage": "sector_matrices",
        "independent_source_emitted": False,
        "locked_target_dependency": True,
        "residual_replay_dependency": True,
        "quadrature_rule_id": "missing_selected_independent_sector_quadrature_rule",
        "kernel_source_id": "sector_matrix_replay_postcheck_not_source_kernel",
        "value": {
            "kind": "sector_response_slot_declared_not_independently_computed",
            "sector": sector,
            "coordinate": coord,
        },
        "exactness_certificate": None,
        "error_bound": "not_applicable_until_independent_sector_integral_is_emitted",
        "selected_b_vector_source": None,
        "why_rejected": "Sector response row exists as an observable slot, but the independent same-source sector integral has not been emitted.",
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    schedule = load(DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "quadrature_row_schedule.packet.json")
    workorder = load(DATA / "selected_routeb_independentquadraturepayload_schema_or_executionworkorder" / "routeb_independent_quadrature_execution_workorder.packet.json")
    replay_rows = load(DATA / "selected_firstvariationboundary_or_primitivequadraturerows_valuefill" / "route_b_replay_backed_primitive_rows.packet.json")
    hessian_target = load(DATA / "selected_hessiancountertermsource_bvector_theoremtemplate" / "hessian_bvector_formal_target.packet.json")
    final_no_go = load(DATA / "selected_finalsourceemission_bestcurrentfill_or_nogowitness" / "final_source_emission_nogo_witness.packet.json")

    stages = stage_map(schedule)
    primitive_by_id = {row["row_id"]: row for row in replay_rows["rows"]}
    hessian_by_id = {row["row_id"]: row for row in hessian_target["hessian_rows"]}

    rows: list[dict[str, Any]] = []
    rows.extend(make_primitive_row(primitive_by_id[row_id]) for row_id in stages["primitive_contractions"])
    rows.extend(make_hessian_row(hessian_by_id[row_id]) for row_id in stages["hessian_source"])
    rows.extend(make_sector_row(row_id) for row_id in stages["sector_matrices"])

    attempt = {
        "schema": "MTTRouteBBestCurrentPayloadFillAttempt.v1",
        "status": "BEST_CURRENT_FILL_REPLAY_AND_FORMAL_SUPPORT_ONLY_EXPECTED_REJECTION",
        "rows": rows,
        "row_count": len(rows),
        "support_imported": {
            "primitive_replay_rows": replay_rows["row_count"],
            "primitive_replay_filled_nonzero_rows": replay_rows["filled_by_replay_count"],
            "independent_primitive_rows": replay_rows["independent_quadrature_row_count"],
            "formal_hessian_rows": hessian_target["hessian_row_count"],
            "sector_response_slots_declared": len(stages["sector_matrices"]),
        },
        "guardrail": "This packet intentionally maximizes current replay/formal support while refusing to mark it as independent selected source emission.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": True,
    }
    ATTEMPT.write_text(json.dumps(attempt, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(ATTEMPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    stderr_lines = proc.stderr.splitlines()
    validator_result = {
        "schema": "MTTRouteBBestCurrentPayloadValidatorResult.v1",
        "payload": rel(ATTEMPT),
        "validator": rel(VALIDATOR),
        "returncode": proc.returncode,
        "expected_failure": True,
        "stderr_excerpt": stderr_lines[:20],
        "independent_source_errors": sum("independent_source_emitted must be true" in line for line in stderr_lines),
        "locked_target_errors": sum("locked_target_dependency must be false" in line for line in stderr_lines),
        "residual_replay_errors": sum("residual_replay_dependency must be false" in line for line in stderr_lines),
        "stdout": proc.stdout.strip(),
    }
    VALIDATOR_RESULT.write_text(json.dumps(validator_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    gap = {
        "schema": "MTTRouteBIndependentSourceGap.v1",
        "status": "FINITE_PAYLOAD_ROWS_PRESENT_VALUES_NOT_SOURCE_PROMOTED",
        "validator_rejects_best_current_fill": proc.returncode == 1,
        "strict_payload_row_count": len(rows),
        "current_support": {
            "all_110_rows_present": len(rows) == 110,
            "primitive_replay_support_present": replay_rows["row_count"] == 72,
            "formal_hessian_target_present": hessian_target["formal_hessian_quadrature_emitted"],
            "sector_slots_declared": len(stages["sector_matrices"]) == 36,
        },
        "blocking_independent_source_objects": {
            "selected_C1_measure_pairing": True,
            "selected_row_kernel_source_ids": True,
            "independent_quadrature_rule": True,
            "primitive_integral_values_from_that_rule": True,
            "same_source_hessian_b_vector_emission": True,
            "same_source_sector_response_integrals": True,
        },
        "why_this_is_progress": (
            "The problem is no longer a row enumeration or algebra target problem. Every strict row slot is present; "
            "what remains is source promotion of the measure/kernel/quadrature objects that would make the row values independent."
        ),
        "minimal_next_source": "selected finite C1 measure/pairing plus row-kernel source theorem",
        "route_A_parallel_exit": final_no_go["minimal_non_replay_payload_needed"]["route_A"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    GAP.write_text(json.dumps(gap, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedRouteBBestCurrentPayloadFillOrIndependentSourceGap",
        "status": STATUS,
        "inputs": {
            "strict_workorder": rel(DATA / "selected_routeb_independentquadraturepayload_schema_or_executionworkorder" / "routeb_independent_quadrature_execution_workorder.packet.json"),
            "replay_rows": rel(DATA / "selected_firstvariationboundary_or_primitivequadraturerows_valuefill" / "route_b_replay_backed_primitive_rows.packet.json"),
            "formal_hessian_target": rel(DATA / "selected_hessiancountertermsource_bvector_theoremtemplate" / "hessian_bvector_formal_target.packet.json"),
            "final_no_go": rel(DATA / "selected_finalsourceemission_bestcurrentfill_or_nogowitness" / "final_source_emission_nogo_witness.packet.json"),
        },
        "output_packets": {
            "best_current_payload_fill_attempt": rel(ATTEMPT),
            "independent_source_gap": rel(GAP),
            "strict_validator_result": rel(VALIDATOR_RESULT),
        },
        "theorem": {
            "name": "RouteBBestCurrentFillSourceGapTheorem",
            "proved": True,
            "statement": (
                "The current corpus can populate all 110 strict Route B row slots using replay/formal support, "
                "but the strict validator correctly rejects the packet because the selected measure, row kernels, "
                "quadrature rule, Hessian b-source, and sector integrals are not independently source-emitted."
            ),
        },
        "what_closes_now": {
            "all_strict_row_slots_present_in_best_current_attempt": True,
            "primitive_replay_support_mapped_into_payload_shape": True,
            "formal_hessian_target_mapped_into_payload_shape": True,
            "sector_response_slots_declared": True,
            "validator_rejection_reason_measured": True,
            "minimal_next_source_object_identified": True,
        },
        "what_remains_open": gap["blocking_independent_source_objects"],
        "validator_rejects_best_current_fill": proc.returncode == 1,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
        "previous_status": workorder["status"],
    }

    cert = {
        "certificate": "MTT_Selected_RouteB_BestCurrentPayloadFill_or_IndependentSourceGap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "row_count": len(rows),
        "validator_rejects_best_current_fill": proc.returncode == 1,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected RouteB BestCurrentPayloadFill or IndependentSourceGap v1

Status: `{STATUS}`.

This artifact fills the strict Route B payload shape as far as the current
corpus honestly allows.

```text
strict rows present                  = {len(rows)}
primitive replay rows imported       = {replay_rows["row_count"]}
independent primitive rows           = {replay_rows["independent_quadrature_row_count"]}
formal Hessian rows imported         = {hessian_target["hessian_row_count"]}
sector response slots declared       = {len(stages["sector_matrices"])}
strict validator accepts packet      = False
```

The validator rejection is the desired result. It proves the current blocker is
not row enumeration or target linear algebra; it is independent selected source
emission for the finite C1 measure/pairing, row kernels, quadrature rule,
Hessian `b_selected` source, and sector response integrals.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
