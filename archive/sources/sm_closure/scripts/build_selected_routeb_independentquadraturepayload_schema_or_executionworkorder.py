"""Build Route B independent quadrature payload schema and execution workorder."""

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

SLUG = "selected_routeb_independentquadraturepayload_schema_or_executionworkorder"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SCHEMA_PACKET = PACKET_DIR / "routeb_independent_quadrature_payload_schema.packet.json"
WORKORDER = PACKET_DIR / "routeb_independent_quadrature_execution_workorder.packet.json"
TEMPLATE = PACKET_DIR / "routeb_independent_quadrature_payload_template.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "strict_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteB_IndependentQuadraturePayload_Schema_or_ExecutionWorkorder_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_independent_quadrature_payload.py"

STATUS = "MTT_SELECTED_ROUTEB_INDEPENDENTQUADRATUREPAYLOAD_SCHEMA_BUILT_EXECUTION_VALUES_OPEN"
NEXT = "MTT_Selected_RouteB_IndependentQuadraturePayload_Fill_or_RouteA_PhiFinSourceEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def stage_map(schedule: dict[str, Any]) -> dict[str, list[str]]:
    return {stage["stage"]: stage["rows"] for stage in schedule["execution_order"]}


def row_stage(row_id: str) -> str:
    if row_id.startswith("theta_"):
        return "hessian_source"
    if ":M:" in row_id:
        return "sector_matrices"
    return "primitive_contractions"


def empty_row(row_id: str) -> dict[str, Any]:
    stage = row_stage(row_id)
    return {
        "row_id": row_id,
        "stage": stage,
        "independent_source_emitted": False,
        "locked_target_dependency": False,
        "residual_replay_dependency": False,
        "quadrature_rule_id": None,
        "kernel_source_id": None,
        "value": None,
        "exactness_certificate": None,
        "error_bound": None,
        "selected_b_vector_source": False if stage == "hessian_source" else None,
        "notes": "Fill from selected source data only; do not copy replay or locked-target values.",
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    schedule = load(DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "quadrature_row_schedule.packet.json")
    no_go = load(DATA / "selected_finalsourceemission_bestcurrentfill_or_nogowitness" / "final_source_emission_nogo_witness.packet.json")
    engine = load(DATA / "selected_c1variationprinciplederivation_or_quadratureenginerun" / "route_b_quadrature_engine_run_attempt.packet.json")
    hessian_template = load(DATA / "selected_hessiancountertermsource_bvector_theoremtemplate" / "hessian_bvector_formal_target.packet.json")

    stages = stage_map(schedule)
    required_rows = stages["primitive_contractions"] + stages["hessian_source"] + stages["sector_matrices"]
    counts = {
        "basis_prerequisite_rows": len(stages["basis"]),
        "primitive_contractions": len(stages["primitive_contractions"]),
        "hessian_source": len(stages["hessian_source"]),
        "sector_matrices": len(stages["sector_matrices"]),
        "strict_payload_rows": len(required_rows),
    }

    schema_packet = {
        "schema": "MTTRouteBIndependentQuadraturePayloadSchema.v1",
        "status": "STRICT_PAYLOAD_SCHEMA_BUILT_VALUES_OPEN",
        "required_stage_counts": counts,
        "strict_payload_excludes_basis_rows": True,
        "basis_rows_are_prerequisites": stages["basis"],
        "required_row_fields": [
            "row_id",
            "stage",
            "independent_source_emitted",
            "locked_target_dependency",
            "residual_replay_dependency",
            "quadrature_rule_id",
            "kernel_source_id",
            "value",
            "exactness_certificate or error_bound",
        ],
        "hessian_row_extra_requirement": "theta_phase and theta_shift must set selected_b_vector_source=true",
        "accepted_provenance": [
            "same-branch selected finite C1 measure/pairing",
            "selected row kernel before residual replay",
            "independent quadrature rule not copied from locked target",
            "exact symbolic certificate or rigorous numerical error bound",
        ],
        "forbidden_provenance": [
            "replay-backed residual rows",
            "locked target A^T b or deltaTheta values used as source",
            "observed masses, CKM, PMNS, CP, or Higgs values used as selectors",
            "local axiom patch treated as unpatched theorem",
        ],
        "validator": rel(VALIDATOR),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
    }

    workorder = {
        "schema": "MTTRouteBIndependentQuadratureExecutionWorkorder.v1",
        "status": "EXECUTION_WORKORDER_BUILT_VALUES_OPEN",
        "source_schedule": rel(DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "quadrature_row_schedule.packet.json"),
        "strict_payload_schema": rel(SCHEMA_PACKET),
        "counts": counts,
        "execution_order": [
            {
                "stage": "basis_prerequisite",
                "rows": stages["basis"],
                "acceptance": "selected basis ids and normalization must be source-emitted before strict rows are filled",
            },
            {
                "stage": "primitive_contractions",
                "rows": stages["primitive_contractions"],
                "acceptance": "72 independent primitive values with kernel source and exactness/error certificate",
            },
            {
                "stage": "hessian_source",
                "rows": stages["hessian_source"],
                "acceptance": "2 independent Hessian/source rows emitting selected_b_vector_source",
            },
            {
                "stage": "sector_matrices",
                "rows": stages["sector_matrices"],
                "acceptance": "36 sector response matrix rows computed from the same independent source packet",
            },
        ],
        "minimal_non_replay_payload_needed": no_go["minimal_non_replay_payload_needed"]["route_B"],
        "locked_target_oracle_for_postcheck_only": engine["locked_acceptance_oracle"],
        "formal_hessian_target_for_postcheck_only": {
            "A_transpose_b": hessian_template["A_transpose_b"],
            "b_norm_sq": hessian_template["b_norm_sq"],
            "deltaTheta_C1": hessian_template["deltaTheta_C1"],
        },
        "postchecks_after_payload_validates": [
            "assemble A and b from independent rows",
            "verify rank(A)=2",
            "verify D>0 for the induced Hessian block",
            "verify kappa_q>0 and 0<rho_q<2*kappa_q if q-selection branch is re-entered",
            "compare against locked target only after source independence is certified",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
    }

    template = {
        "schema": "MTTRouteBIndependentQuadraturePayload.v1",
        "status": "TEMPLATE_UNFILLED_EXPECTED_TO_FAIL_STRICT_VALIDATOR",
        "rows": [empty_row(row_id) for row_id in required_rows],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
    }

    SCHEMA_PACKET.write_text(json.dumps(schema_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WORKORDER.write_text(json.dumps(workorder, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    TEMPLATE.write_text(json.dumps(template, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(TEMPLATE)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    validator_result = {
        "schema": "MTTRouteBIndependentQuadraturePayloadValidatorResult.v1",
        "payload": rel(TEMPLATE),
        "validator": rel(VALIDATOR),
        "returncode": proc.returncode,
        "expected_failure": True,
        "stderr_excerpt": proc.stderr.splitlines()[:12],
        "stdout": proc.stdout.strip(),
    }
    VALIDATOR_RESULT.write_text(json.dumps(validator_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedRouteBIndependentQuadraturePayloadSchemaOrExecutionWorkorder",
        "status": STATUS,
        "inputs": {
            "schedule": rel(DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "quadrature_row_schedule.packet.json"),
            "final_no_go_witness": rel(DATA / "selected_finalsourceemission_bestcurrentfill_or_nogowitness" / "final_source_emission_nogo_witness.packet.json"),
            "route_b_engine_attempt": rel(DATA / "selected_c1variationprinciplederivation_or_quadratureenginerun" / "route_b_quadrature_engine_run_attempt.packet.json"),
            "formal_hessian_template": rel(DATA / "selected_hessiancountertermsource_bvector_theoremtemplate" / "hessian_bvector_formal_target.packet.json"),
        },
        "output_packets": {
            "payload_schema": rel(SCHEMA_PACKET),
            "execution_workorder": rel(WORKORDER),
            "unfilled_payload_template": rel(TEMPLATE),
            "strict_validator_result": rel(VALIDATOR_RESULT),
        },
        "theorem": {
            "name": "RouteBIndependentQuadraturePayloadReadinessTheorem",
            "proved": True,
            "statement": (
                "A Route B source-emission proof is now reduced to one finite payload with exactly "
                "72 primitive contraction rows, 2 Hessian/source rows, and 36 sector response rows, "
                "each carrying independent source provenance and exactness/error certification."
            ),
        },
        "what_closes_now": {
            "strict_route_B_payload_contract": True,
            "required_110_non_basis_rows_enumerated": True,
            "basis_prerequisites_separated_from_strict_payload": True,
            "validator_for_future_filled_payload": True,
            "replay_shortcut_rejected_by_construction": True,
        },
        "what_remains_open": {
            "selected_quadrature_rule_id_values": True,
            "selected_kernel_source_ids": True,
            "72_independent_primitive_values": True,
            "2_independent_hessian_source_values": True,
            "36_independent_sector_response_values": True,
            "exactness_or_error_certificates": True,
            "Route_A_same_branch_phifin_source_emission": True,
        },
        "validator_rejects_unfilled_template": proc.returncode == 1,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_RouteB_IndependentQuadraturePayload_Schema_or_ExecutionWorkorder_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "strict_payload_rows": counts["strict_payload_rows"],
        "validator_rejects_unfilled_template": proc.returncode == 1,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected RouteB IndependentQuadraturePayload Schema or ExecutionWorkorder v1

Status: `{STATUS}`.

This artifact turns the Route B exit into a strict finite payload rather than a
loose instruction.

Required strict payload rows:

```text
primitive contractions = {counts["primitive_contractions"]}
hessian/source rows    = {counts["hessian_source"]}
sector matrix rows     = {counts["sector_matrices"]}
total strict rows      = {counts["strict_payload_rows"]}
```

The `19` basis rows remain prerequisites, but the source-emission payload itself
is the `72+2+36` non-basis packet.

The unfilled template is intentionally rejected by the strict validator. A
future filled payload must attach independent selected source provenance,
quadrature/kernel ids, row values, and exactness or error certificates. Replay
rows and locked target values are accepted only as postchecks, not as source.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
