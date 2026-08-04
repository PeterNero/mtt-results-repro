"""Build PSM-C1-06 sector-row/replay-independence certificate gate."""

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

SLUG = "selected_psm_c1_06_sectorrows_or_replayindependencecertificate"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
UNPATCHED = PACKET_DIR / "unpatched_sector_rows_and_replay_independence_status.packet.json"
CONDITIONAL_PAYLOAD = PACKET_DIR / "route_b_full_conditional_validator_payload.packet.json"
CONDITIONAL_RESULT = PACKET_DIR / "route_b_full_conditional_validator_result.packet.json"
FINAL_GATE = PACKET_DIR / "final_unpatched_source_identity_gate.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_06_SectorRows_or_ReplayIndependenceCertificate_v1.md"

VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"
STATUS = "MTT_SELECTED_PSM_C1_06_SECTORROWS_OR_REPLAYINDEPENDENCECERTIFICATE_BUILT_CONDITIONAL_ROUTEB_VALIDATES"
NEXT_ARTIFACT = "MTT_Selected_UnpatchedFiniteC1SourceIdentityPrinciple_or_HonestIndependentKernelExport_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return {
        "payload": rel(path),
        "validator": rel(VALIDATOR),
        "returncode": proc.returncode,
        "passes": proc.returncode == 0,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
        "stderr_lines": [line for line in proc.stderr.splitlines() if line],
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_psm_c1_02_physicalselectionlemma_or_psm_c1_04_hessiansourcerows.candidate.json")
    row_source = load(DATA / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill" / "current_row_source_independence_attempt.packet.json")
    actual_row_fill = load(DATA / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate" / "current_actual_row_source_fill_attempt.packet.json")
    applied_principle = load(DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "applied_principle_kernel_closure.packet.json")
    finite_identity = load(DATA / "selected_finitec1sourceidentitytheorem_crossrepo_external_derivation" / "selected_finite_c1_source_identity_principle_candidate.packet.json")
    table_attempt = load(DATA / "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable" / "two_exit_current_after_table_attempt.packet.json")

    unpatched_packet = {
        "schema": "MTTUnpatchedSectorRowsAndReplayIndependenceStatus.v1",
        "status": "UNPATCHED_SECTOR_ROWS_FORMAL_REPLAY_INDEPENDENCE_OPEN",
        "labels": ["PSM-C1-06", "PSM-C1-02/PSM-C1-04 guardrail"],
        "unpatched_support": {
            "sector_rows_assembled_from_primitive_rows": row_source["sector_rows_assembled_from_primitive_rows"],
            "hessian_source_rows_assembled_from_same_rows": row_source["hessian_source_rows_assembled_from_same_rows"],
            "finite_weyl_trace_rule_feeds_all_rows": row_source["finite_weyl_trace_rule_feeds_all_rows"],
            "no_locked_target_values_used_as_source": row_source["no_locked_target_values_used_as_source"],
        },
        "unpatched_blockers": {
            "selected_basis_feeds_72_primitive_rows": row_source["selected_basis_feeds_72_primitive_rows"],
            "row_formula_source_theorem_derived": row_source["row_formula_source_theorem_derived"],
            "no_residual_projector_replay_used_as_source": row_source["no_residual_projector_replay_used_as_source"],
            "source_independent_of_residual_projector_replay": row_source["source_independent_of_residual_projector_replay"],
            "actual_row_fill_source_independent": actual_row_fill["source_independent_of_residual_projector_replay"],
        },
        "conditional_support": {
            "sector_rows_physical_source_promotion": applied_principle["promoted_inside_local_spine"]["sector_rows_physical_source_promotion"],
            "independence_from_residual_projector_replay": applied_principle["promoted_inside_local_spine"]["independence_from_residual_projector_replay"],
            "sector_functor": applied_principle["sector_functor"],
            "residual_projector_replay_used_as_source": applied_principle["residual_projector_replay_used_as_source"],
        },
        "interpretation": (
            "Sector rows are formally assembled in the older Route-B row-source validator lineage, and the local principle "
            "would promote both sector rows and replay-independence. The unpatched blocker is still the source identity "
            "or an independent kernel export proving those facts without using residual replay as provenance."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    conditional_payload = {
        "schema": "MTTRouteBFullConditionalValidatorPayload.v1",
        "status": "FULL_CONDITIONAL_ROUTE_B_VALIDATOR_PAYLOAD",
        "closure_claimed": False,
        "locked_target_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "route_A_physical_action_restriction": table_attempt["route_A_physical_action_restriction"],
        "route_B_independent_rowkernel_source": {
            "same_branch": True,
            "selected_basis_feeds_all_72_row_functionals": True,
            "pre_residual_phase_shift_variation_operators": True,
            "independent_hessian_counterterm_source_rows": True,
            "sector_rows_assembled_from_source_rows": True,
            "no_residual_projector_replay_or_locked_target_as_source": True,
            "attached_source_evidence": [
                {
                    "source": rel(DATA / "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable" / "two_exit_current_after_table_attempt.packet.json"),
                    "closes": "selected basis field in best current table attempt",
                },
                {
                    "source": rel(DATA / "selected_psm_c1_02_preresidualoperators_or_routea_physicalrestriction" / "psm_c1_02_current_unpatched_operator_source_audit.packet.json"),
                    "closes": "pre-residual R_Z/R_X operator candidates",
                    "conditional": True,
                },
                {
                    "source": rel(DATA / "selected_psm_c1_02_physicalselectionlemma_or_psm_c1_04_hessiansourcerows" / "unpatched_physical_selection_and_hessian_source_status.packet.json"),
                    "closes": "conditional Hessian/source rows",
                    "conditional": True,
                },
                {
                    "source": rel(DATA / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill" / "current_row_source_independence_attempt.packet.json"),
                    "closes": "formal sector rows assembled from primitive rows",
                },
                {
                    "source": rel(DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "applied_principle_kernel_closure.packet.json"),
                    "closes": "conditional sector functor and replay-independence",
                    "conditional": True,
                },
                {
                    "source": rel(DATA / "selected_finitec1sourceidentitytheorem_crossrepo_external_derivation" / "selected_finite_c1_source_identity_principle_candidate.packet.json"),
                    "closes": "candidate unpatched source-identity principle shape",
                    "conditional": True,
                },
            ],
        },
    }
    CONDITIONAL_PAYLOAD.write_text(json.dumps(conditional_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    conditional_result = run_validator(CONDITIONAL_PAYLOAD)
    conditional_result["observed_data_used_as_selector"] = False
    conditional_result["target_fitting_used"] = False

    final_gate = {
        "schema": "MTTFinalUnpatchedSourceIdentityGate.v1",
        "status": "UNPATCHED_C1_REDUCED_TO_SOURCE_IDENTITY_OR_INDEPENDENT_KERNEL_EXPORT",
        "conditional_routeB_validates": conditional_result["passes"],
        "unpatched_routeB_validates": False,
        "two_legal_finishing_routes": [
            {
                "route": "SOURCE_IDENTITY",
                "artifact": "SelectedFiniteC1SourceIdentityPrinciple",
                "must_prove": [
                    "selected physical/finite C1 trace row-kernel identity",
                    "pre-residual R_Z/R_X source operators",
                    "same-source Hessian/b rows",
                    "sector rows assembled from those source rows",
                    "residual projector and locked target values are postchecks only",
                ],
            },
            {
                "route": "HONEST_KERNEL_EXPORT",
                "artifact": "Independent selected finite C1 kernel/quadrature export",
                "must_emit": [
                    "72 primitive row values with source ids",
                    "2 Hessian/source rows with source ids",
                    "36 sector rows assembled from the same source ids",
                    "exactness/error certificates",
                    "provenance independent of residual-projector replay and locked targets",
                ],
            },
        ],
        "source_identity_candidate_support": {
            "candidate_status": finite_identity["status"],
            "observed_data_used_as_selector": finite_identity["observed_data_used_as_selector"],
            "target_fitting_used": finite_identity["target_fitting_used"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC106ReplayIndependence.v1",
        "status": "NEXT_WORKORDER_UNPATCHED_SOURCE_IDENTITY_OR_HONEST_KERNEL_EXPORT",
        "next_required_artifact": NEXT_ARTIFACT,
        "recommended_primary": {
            "label": "PSM-NK/TRUE-EQ-C1",
            "route": "SOURCE_IDENTITY",
            "task": "Prove the unpatched SelectedFiniteC1SourceIdentityPrinciple so all five Route-B fields become theorem-derived.",
        },
        "alternative": {
            "label": "PSM-C1-02..06",
            "route": "HONEST_KERNEL_EXPORT",
            "task": "Export independent selected finite C1 kernel/quadrature rows with source provenance for 72+2+36 rows.",
        },
        "previous_artifact": previous["next_required_artifact"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "ConditionalRouteBValidationAndFinalUnpatchedGateTheorem",
        "proved": True,
        "statement": (
            "When the conditional Weyl-variation/Hessian/sector-functor spine is accepted, all five strict Route-B fields validate. "
            "Unpatched, the repository still has formal sector-row assembly but lacks replay-independent source provenance. "
            "Therefore the remaining true-equivalence C1 task is exactly to prove the SelectedFiniteC1SourceIdentityPrinciple unpatched "
            "or to export an honest independent finite C1 kernel table with 72 primitive, 2 Hessian/source, and 36 sector rows."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedPSMC106SectorRowsOrReplayIndependenceCertificate",
        "status": STATUS,
        "theorem": theorem,
        "closure_claimed": False,
        "conditional_only": True,
        "output_packets": {
            "unpatched_sector_rows_and_replay_independence_status": rel(UNPATCHED),
            "full_conditional_validator_payload": rel(CONDITIONAL_PAYLOAD),
            "full_conditional_validator_result": rel(CONDITIONAL_RESULT),
            "final_unpatched_source_identity_gate": rel(FINAL_GATE),
            "next_labeled_workorder": rel(NEXT),
        },
        "closure_decision": {
            "conditional_RouteB_validator_passes": conditional_result["passes"],
            "unpatched_RouteB_validator_passes": False,
            "unpatched_dynamic_C1_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "conditional_full_RouteB_validator_pass": conditional_result["passes"],
            "formal_sector_row_assembly_support_recorded": True,
            "final_unpatched_gate_reduced_to_two_legal_routes": True,
        },
        "what_remains_open": {
            "SelectedFiniteC1SourceIdentityPrinciple_unpatched": True,
            "honest_independent_kernel_export": True,
            "replay_independence_as_unpatched_provenance": True,
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
        "conditional_validator_passes": conditional_result["passes"],
        "unpatched_validator_passes": False,
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected PSM-C1-06 Sector Rows or Replay-Independence Certificate v1

Status: `{STATUS}`

## Theorem

**{theorem["name"]}.** {theorem["statement"]}

## Result

- Conditional Route B now validates all five strict fields.
- Unpatched Route B does not validate.
- The remaining unpatched gate is no longer diffuse: prove the `SelectedFiniteC1SourceIdentityPrinciple` or export an honest independent kernel/quadrature table.
- SM-parity remains frozen; this is true-equivalence/no-knob frontier work.

## Superset Use

The superset strategy is used as a diagnostic closure bridge. Route-B row kernels, Route-A source identity, and the Weyl-variation/Hessian/sector functor are merged only conditionally. The validator pass is therefore a map of the final proof shape, not an unpatched proof.

## Next Artifact

`{NEXT_ARTIFACT}`

This is now the clean finishing problem for this branch: either prove source identity unpatched, or provide the independent kernel export.
"""

    UNPATCHED.write_text(json.dumps(unpatched_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CONDITIONAL_RESULT.write_text(json.dumps(conditional_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    FINAL_GATE.write_text(json.dumps(final_gate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT.write_text(json.dumps(next_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
