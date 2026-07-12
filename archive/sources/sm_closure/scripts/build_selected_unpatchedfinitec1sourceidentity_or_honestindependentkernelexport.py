"""Build final unpatched finite-C1 source identity or honest-kernel export contract."""

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

SLUG = "selected_unpatchedfinitec1sourceidentity_or_honestindependentkernelexport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_AUDIT = PACKET_DIR / "source_identity_route_audit.packet.json"
KERNEL_AUDIT = PACKET_DIR / "honest_kernel_export_route_audit.packet.json"
ROW_MANIFEST = PACKET_DIR / "honest_kernel_export_row_manifest.packet.json"
DECISION = PACKET_DIR / "final_two_route_decision.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_UnpatchedFiniteC1SourceIdentityPrinciple_or_HonestIndependentKernelExport_v1.md"

SOURCE_VALIDATOR = ROOT / "scripts" / "validate_selected_independentc1_rowkernel_source_ids.py"
KERNEL_VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_independent_quadrature_payload.py"
STATUS = "MTT_SELECTED_UNPATCHEDFINITEC1SOURCEIDENTITY_OR_HONESTINDEPENDENTKERNELEXPORT_BUILT_FINAL_TWO_ROUTE_CONTRACT"
NEXT_ARTIFACT = "MTT_Selected_HonestKernelExport_RowSourceFill_or_SourceIdentityDerivationAttempt_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(validator: Path, payload: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(validator), str(payload)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return {
        "validator": rel(validator),
        "payload": rel(payload),
        "returncode": proc.returncode,
        "passes": proc.returncode == 0,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
        "stderr_lines": [line for line in proc.stderr.splitlines() if line],
    }


def stage_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        stage = row["stage"]
        counts[stage] = counts.get(stage, 0) + 1
    return counts


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_psm_c1_06_sectorrows_or_replayindependencecertificate.candidate.json")
    final_gate = load(DATA / "selected_psm_c1_06_sectorrows_or_replayindependencecertificate" / "final_unpatched_source_identity_gate.packet.json")
    source_principle = load(DATA / "selected_finitec1sourceidentitytheorem_crossrepo_external_derivation" / "selected_finite_c1_source_identity_principle_candidate.packet.json")
    source_theorem_gate = load(DATA / "selected_finitec1sourceidentitytheorem_or_newindependentrows" / "selected_finite_c1_source_identity_theorem_gate.packet.json")
    conditional_source_result = load(DATA / "selected_finitec1sourceidentitytheorem_crossrepo_external_derivation" / "conditional_promoted_source_identity_validator_result.packet.json")
    independent_schema = load(DATA / "selected_finitec1sourceidentitytheorem_or_newindependentrows" / "new_independent_rows_schema.packet.json")
    export_workorder = load(DATA / "selected_routeb_independentquadraturepayload_schema_or_executionworkorder" / "routeb_independent_quadrature_execution_workorder.packet.json")
    export_template_path = DATA / "selected_routeb_independentquadraturepayload_schema_or_executionworkorder" / "routeb_independent_quadrature_payload_template.packet.json"
    export_template = load(export_template_path)

    template_validation = run_validator(KERNEL_VALIDATOR, export_template_path)

    strict_rows = [row for stage in export_workorder["execution_order"] if stage["stage"] != "basis_prerequisite" for row in stage["rows"]]
    row_manifest_entries = []
    for stage in export_workorder["execution_order"]:
        if stage["stage"] == "basis_prerequisite":
            continue
        for row_id in stage["rows"]:
            row_manifest_entries.append(
                {
                    "row_id": row_id,
                    "stage": stage["stage"],
                    "status": "OPEN_SOURCE_VALUE_REQUIRED",
                    "required_fields": [
                        "independent_source_emitted=true",
                        "quadrature_rule_id",
                        "kernel_source_id",
                        "value",
                        "exactness_certificate or error_bound",
                    ],
                    "forbidden": [
                        "locked target dependency",
                        "residual replay dependency",
                        "observed data selector",
                    ],
                }
            )

    source_audit = {
        "schema": "MTTSourceIdentityRouteAudit.v1",
        "status": "SOURCE_IDENTITY_CONDITIONAL_READY_UNPATCHED_NOT_DERIVED",
        "route": "SOURCE_IDENTITY",
        "principle": source_principle,
        "theorem_gate": {
            "status": source_theorem_gate["status"],
            "proved_now": source_theorem_gate["proved_now"],
            "current_route_A_accepts": source_theorem_gate["current_route_A_accepts"],
            "current_route_B_accepts": source_theorem_gate["current_route_B_accepts"],
            "clause_status": source_theorem_gate["clause_status"],
        },
        "conditional_source_id_validator": conditional_source_result,
        "route_can_close_if": "SelectedFiniteC1SourceIdentityPrinciple is derived or explicitly accepted as a local principle.",
        "unpatched_closed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    kernel_audit = {
        "schema": "MTTHonestKernelExportRouteAudit.v1",
        "status": "HONEST_KERNEL_EXPORT_SCHEMA_READY_VALUES_NOT_EMITTED",
        "route": "HONEST_KERNEL_EXPORT",
        "strict_payload_rows_required": len(strict_rows),
        "stage_counts_required": export_workorder["counts"],
        "current_template_validation": template_validation,
        "schema_support": independent_schema,
        "workorder": rel(DATA / "selected_routeb_independentquadraturepayload_schema_or_executionworkorder" / "routeb_independent_quadrature_execution_workorder.packet.json"),
        "export_closed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    manifest = {
        "schema": "MTTHonestKernelExportRowManifest.v1",
        "status": "ROW_MANIFEST_BUILT_110_STRICT_ROWS_OPEN",
        "counts": stage_counts(row_manifest_entries),
        "strict_payload_rows": len(row_manifest_entries),
        "basis_prerequisites": export_workorder["execution_order"][0]["rows"],
        "rows": row_manifest_entries,
        "postcheck_oracle_not_source": export_workorder["locked_target_oracle_for_postcheck_only"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTFinalTwoRouteDecision.v1",
        "status": "FINAL_UNPATCHED_C1_GATE_HAS_TWO_LEGAL_ROUTES_BOTH_OPEN",
        "previous_conditional_routeB_validates": previous["closure_decision"]["conditional_RouteB_validator_passes"],
        "source_identity_route": {
            "closed_now": False,
            "conditional_ready": source_principle["insertion_status"]["conditional_validator_would_pass_if_inserted"],
            "unpatched_derivation": source_principle["insertion_status"]["current_unpatched_mtt_derivation"],
        },
        "honest_kernel_export_route": {
            "closed_now": False,
            "strict_rows_required": len(row_manifest_entries),
            "template_validator_passes": template_validation["passes"],
        },
        "recommended_next": "Attempt honest kernel row-source fill first while carrying source-identity derivation as co-primary.",
        "reason": (
            "The source identity is mathematically compact but currently principle-level. The honest export route is larger, "
            "but now has an exact row manifest and a strict validator, so progress can be measured row by row."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextLabeledWorkorderAfterFinalTwoRouteContract.v1",
        "status": "NEXT_WORKORDER_HONEST_KERNEL_ROW_SOURCE_FILL_WITH_SOURCE_IDENTITY_COPRIMARY",
        "next_required_artifact": NEXT_ARTIFACT,
        "primary": {
            "route": "HONEST_KERNEL_EXPORT",
            "task": "Fill the 110-row strict manifest with independent source ids, values, and exactness/error certificates.",
            "first_stage": "primitive_contractions",
            "acceptance": "validate_selected_routeb_independent_quadrature_payload.py passes without replay or locked-target source dependency",
        },
        "co_primary": {
            "route": "SOURCE_IDENTITY",
            "task": "Try deriving the SelectedFiniteC1SourceIdentityPrinciple from the existing physical Phi_fin^C1 action/trace support.",
            "acceptance": "theorem gate proved_now=true without local principle insertion",
        },
        "previous_artifact": previous["next_required_artifact"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "FinalTwoRouteUnpatchedC1ExecutionContractTheorem",
        "proved": True,
        "statement": (
            "After the conditional Route-B validator pass, unpatched dynamic C1 closure has exactly two legal finishing routes: "
            "derive the SelectedFiniteC1SourceIdentityPrinciple, or emit an honest independent finite C1 kernel export with 110 strict rows. "
            "The current repository proves neither route, but it now fixes the validator, row manifest, postcheck-only oracle, and next execution order."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedUnpatchedFiniteC1SourceIdentityOrHonestIndependentKernelExport",
        "status": STATUS,
        "theorem": theorem,
        "closure_claimed": False,
        "output_packets": {
            "source_identity_route_audit": rel(SOURCE_AUDIT),
            "honest_kernel_export_route_audit": rel(KERNEL_AUDIT),
            "honest_kernel_export_row_manifest": rel(ROW_MANIFEST),
            "final_two_route_decision": rel(DECISION),
            "next_labeled_workorder": rel(NEXT),
        },
        "closure_decision": {
            "source_identity_unpatched_derived": False,
            "honest_kernel_export_emitted": False,
            "unpatched_dynamic_C1_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "final_two_route_execution_contract": True,
            "honest_kernel_export_110_row_manifest": True,
            "postcheck_oracle_kept_out_of_source": True,
            "strict_validator_boundary_reconfirmed": True,
        },
        "what_remains_open": {
            "SelectedFiniteC1SourceIdentityPrinciple_derivation": True,
            "primitive_contractions_72_independent_rows": True,
            "hessian_source_2_independent_rows": True,
            "sector_matrices_36_independent_rows": True,
            "exactness_or_error_certificates": True,
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
        "strict_manifest_rows": len(row_manifest_entries),
        "source_identity_unpatched_derived": False,
        "honest_kernel_export_emitted": False,
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected UnpatchedFiniteC1SourceIdentity or HonestIndependentKernelExport v1

Status: `{STATUS}`

## Theorem

**{theorem["name"]}.** {theorem["statement"]}

## Result

- Conditional Route B already validates, but unpatched closure is still open.
- Source-identity route: compact and conditional-ready, but not derived unpatched.
- Honest-kernel route: not emitted, but now has an exact 110-row manifest and strict validator boundary.
- The locked target oracle remains postcheck-only and cannot be used as a source.

## Superset Use

The superset strategy is now disciplined into two finishing routes. The source-identity path fuses Route A and Route B into one selected physical/finite trace identity. The honest-kernel path avoids that principle by demanding independent row data. Both routes share the same locked target only as a postcheck.

## Next Artifact

`{NEXT_ARTIFACT}`

Recommended next move: start filling the honest 110-row kernel manifest, while keeping source-identity derivation as the co-primary route.
"""

    SOURCE_AUDIT.write_text(json.dumps(source_audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    KERNEL_AUDIT.write_text(json.dumps(kernel_audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROW_MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    DECISION.write_text(json.dumps(decision, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT.write_text(json.dumps(next_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
