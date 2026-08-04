"""Build first honest-kernel row-source fill attempt and source-identity co-primary audit."""

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

SLUG = "selected_honestkernelexport_rowsourcefill_or_sourceidentityderivationattempt"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PRIMITIVE_ATTEMPT = PACKET_DIR / "primitive_stage_postcheck_fill_attempt.packet.json"
PRIMITIVE_VALIDATION = PACKET_DIR / "primitive_stage_postcheck_fill_validator_result.packet.json"
SOURCE_IDENTITY = PACKET_DIR / "source_identity_derivation_attempt_status.packet.json"
ROW_PROGRESS = PACKET_DIR / "row_source_fill_progress_ledger.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HonestKernelExport_RowSourceFill_or_SourceIdentityDerivationAttempt_v1.md"

KERNEL_VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_independent_quadrature_payload.py"
STATUS = "MTT_SELECTED_HONESTKERNELEXPORT_ROWSOURCEFILL_OR_SOURCEIDENTITYDERIVATIONATTEMPT_BUILT_PRIMITIVE_POSTCHECK_FILLED_SOURCE_OPEN"
NEXT_ARTIFACT = "MTT_Selected_PrimitiveRows_SourcePromotion_or_IndependentFormulaDerivation_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(payload: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(KERNEL_VALIDATOR), str(payload)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return {
        "validator": rel(KERNEL_VALIDATOR),
        "payload": rel(payload),
        "returncode": proc.returncode,
        "passes": proc.returncode == 0,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
        "stderr_lines": [line for line in proc.stderr.splitlines() if line],
    }


def value_from_row(row: dict[str, Any]) -> Any:
    return row["computed_complex_entry_value"]


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_unpatchedfinitec1sourceidentity_or_honestindependentkernelexport.candidate.json")
    manifest = load(DATA / "selected_unpatchedfinitec1sourceidentity_or_honestindependentkernelexport" / "honest_kernel_export_row_manifest.packet.json")
    template = load(DATA / "selected_routeb_independentquadraturepayload_schema_or_executionworkorder" / "routeb_independent_quadrature_payload_template.packet.json")
    exact72 = load(DATA / "selected_firstrowprovenancepromotion_or_allrowsweylexecution" / "all_72_exact_weyl_row_execution.packet.json")
    all_rows_decision = load(DATA / "selected_firstrowprovenancepromotion_or_allrowsweylexecution" / "all_rows_execution_decision.packet.json")
    source_gate = load(DATA / "selected_finitec1sourceidentitytheorem_or_newindependentrows" / "selected_finite_c1_source_identity_theorem_gate.packet.json")

    exact_by_id = {row["row_id"]: row for row in exact72["rows"]}
    filled_rows = []
    primitive_filled = 0
    for row in template["rows"]:
        new_row = dict(row)
        exact = exact_by_id.get(row["row_id"])
        if exact:
            primitive_filled += 1
            new_row.update(
                {
                    "value": value_from_row(exact),
                    "exactness_certificate": exact["exactness_or_error_bound_certificate"],
                    "error_bound": None,
                    "quadrature_rule_id": "postcheck_finite_qutrit_weyl_polynomial_route",
                    "kernel_source_id": f"postcheck_{exact['value_source']}_not_source",
                    "independent_source_emitted": False,
                    "locked_target_dependency": False,
                    "residual_replay_dependency": True,
                    "notes": "Exact primitive value carried as postcheck only; independent row source not emitted.",
                }
            )
        filled_rows.append(new_row)

    attempt = {
        "schema": "MTTPrimitiveStagePostcheckFillAttempt.v1",
        "status": "PRIMITIVE_72_VALUES_FILLED_AS_POSTCHECK_SOURCE_PROVENANCE_OPEN",
        "locked_target_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "rows": filled_rows,
        "primitive_rows_filled_with_postcheck_values": primitive_filled,
        "strict_rows_total": len(filled_rows),
        "source_promotion": {
            "primitive_independent_source_emitted": False,
            "provenance_independent_of_residual_projector_replay": exact72["provenance_independent_of_residual_projector_replay_for_all_rows"],
            "physical_source_promoted_for_any_row": exact72["physical_source_promoted_for_any_row"],
        },
    }
    PRIMITIVE_ATTEMPT.write_text(json.dumps(attempt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    validation = run_validator(PRIMITIVE_ATTEMPT)
    validation["observed_data_used_as_selector"] = False
    validation["target_fitting_used"] = False

    source_identity = {
        "schema": "MTTSourceIdentityDerivationAttemptStatus.v1",
        "status": "SOURCE_IDENTITY_DERIVATION_STILL_OPEN_AFTER_PRIMITIVE_POSTCHECK_FILL",
        "proved_now": source_gate["proved_now"],
        "route_A_accepts": source_gate["current_route_A_accepts"],
        "route_B_accepts": source_gate["current_route_B_accepts"],
        "open_clauses": {
            key: value
            for key, value in source_gate["clause_status"].items()
            if value["proved"] is False
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    progress = {
        "schema": "MTTRowSourceFillProgressLedger.v1",
        "status": "PRIMITIVE_VALUES_AVAILABLE_SOURCE_FLAGS_OPEN",
        "manifest_rows": manifest["strict_payload_rows"],
        "postcheck_value_progress": {
            "primitive_contractions": {
                "values_available": primitive_filled,
                "values_required": 72,
                "independent_source_rows_closed": 0,
            },
            "hessian_source": {
                "values_available": 0,
                "values_required": 2,
                "independent_source_rows_closed": 0,
            },
            "sector_matrices": {
                "values_available": 0,
                "values_required": 36,
                "independent_source_rows_closed": 0,
            },
        },
        "validator_passes": validation["passes"],
        "expected_failure_classes": [
            "primitive rows independent_source_emitted=false",
            "primitive rows residual_replay_dependency=true",
            "hessian and sector rows still lack values/source certificates",
        ],
        "closed_support_imported": {
            "all_72_row_values_exact": all_rows_decision["all_72_row_values_exact"],
            "all_72_row_exactness_certificates": all_rows_decision["all_72_row_exactness_certificates"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextLabeledWorkorderAfterPrimitivePostcheckFill.v1",
        "status": "NEXT_WORKORDER_PRIMITIVE_SOURCE_PROMOTION_OR_INDEPENDENT_FORMULA",
        "next_required_artifact": NEXT_ARTIFACT,
        "primary": {
            "route": "HONEST_KERNEL_EXPORT",
            "task": "Promote the 72 primitive postcheck rows to independent source rows by deriving non-replay kernel_source_id and quadrature_rule_id.",
            "acceptance": "primitive rows set independent_source_emitted=true and residual_replay_dependency=false with theorem-backed source ids",
        },
        "co_primary": {
            "route": "SOURCE_IDENTITY",
            "task": "Prove the finite C1 source identity clauses that would promote the primitive rows in one step.",
            "acceptance": "source identity theorem gate proved_now=true",
        },
        "previous_artifact": previous["next_required_artifact"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "PrimitivePostcheckFillBoundaryTheorem",
        "proved": True,
        "statement": (
            "The existing exact 72 primitive row values can populate the honest-kernel export table only as postchecks. "
            "They do not satisfy strict independent source provenance because every primitive row still lacks physical/source promotion "
            "and remains residual-lineage dependent. Therefore the next real closure step is primitive source promotion or an independent formula derivation."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedHonestKernelExportRowSourceFillOrSourceIdentityDerivationAttempt",
        "status": STATUS,
        "theorem": theorem,
        "closure_claimed": False,
        "output_packets": {
            "primitive_stage_postcheck_fill_attempt": rel(PRIMITIVE_ATTEMPT),
            "primitive_stage_postcheck_fill_validator_result": rel(PRIMITIVE_VALIDATION),
            "source_identity_derivation_attempt_status": rel(SOURCE_IDENTITY),
            "row_source_fill_progress_ledger": rel(ROW_PROGRESS),
            "next_labeled_workorder": rel(NEXT),
        },
        "closure_decision": {
            "honest_kernel_export_validates": validation["passes"],
            "primitive_source_rows_closed": False,
            "source_identity_unpatched_derived": False,
            "unpatched_dynamic_C1_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "primitive_72_postcheck_values_loaded": True,
            "strict_validator_boundary_reconfirmed": True,
            "source_promotion_next_gate_identified": True,
        },
        "what_remains_open": {
            "primitive_source_provenance": True,
            "hessian_source_values": True,
            "sector_matrix_source_values": True,
            "source_identity_derivation": True,
        },
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": f"{SLUG}_certificate",
        "status": STATUS,
        "candidate": rel(OUTPUT),
        "theorem_proved": theorem["proved"],
        "primitive_postcheck_values_loaded": primitive_filled,
        "validator_passes": validation["passes"],
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HonestKernelExport RowSourceFill or SourceIdentityDerivationAttempt v1

Status: `{STATUS}`

## Theorem

**{theorem["name"]}.** {theorem["statement"]}

## Result

- Loaded all 72 primitive row values as postcheck values.
- The strict honest-kernel validator still fails, correctly.
- No primitive row is promoted as an independent source row.
- The next gate is primitive source promotion: derive non-replay `kernel_source_id` and `quadrature_rule_id`, or prove the source identity theorem.

## Guardrail

The exact primitive values are useful, but they are not proof of source provenance. This artifact keeps replay and locked targets out of the source lane.

## Next Artifact

`{NEXT_ARTIFACT}`
"""

    PRIMITIVE_VALIDATION.write_text(json.dumps(validation, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SOURCE_IDENTITY.write_text(json.dumps(source_identity, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROW_PROGRESS.write_text(json.dumps(progress, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT.write_text(json.dumps(next_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
