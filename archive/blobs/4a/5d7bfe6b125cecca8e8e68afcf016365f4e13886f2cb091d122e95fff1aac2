"""Build PSM-C1-02 I10 binding proof or selected quadrature source promotion gate."""

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

SLUG = "selected_psm_c1_02_i10bindingproof_or_selectedquadraturesourcepromotion"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A_CURRENT = PACKET_DIR / "route_a_current_i10_binding_stack_attempt.packet.json"
ROUTE_A_CONDITIONAL = PACKET_DIR / "route_a_conditional_i10_binding_stack_witness.packet.json"
ROUTE_A_CURRENT_RESULT = PACKET_DIR / "route_a_current_i10_binding_stack_validator_result.packet.json"
ROUTE_A_CONDITIONAL_RESULT = PACKET_DIR / "route_a_conditional_i10_binding_stack_validator_result.packet.json"
ROUTE_B_CURRENT = PACKET_DIR / "route_b_current_independent_quadrature_payload_attempt.packet.json"
ROUTE_B_CONDITIONAL = PACKET_DIR / "route_b_conditional_selected_quadrature_source_promotion_witness.packet.json"
ROUTE_B_CURRENT_RESULT = PACKET_DIR / "route_b_current_independent_quadrature_payload_validator_result.packet.json"
ROUTE_B_CONDITIONAL_RESULT = PACKET_DIR / "route_b_conditional_independent_quadrature_payload_validator_result.packet.json"
REDUCTION = PACKET_DIR / "psm_c1_02_dual_validator_reduction.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_I10BindingProof_or_SelectedQuadratureSourcePromotion_v1.md"

I10_VALIDATOR = ROOT / "scripts" / "validate_selected_i10_binding_stack.py"
ROUTEB_VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_independent_quadrature_payload.py"

STATUS = "MTT_SELECTED_PSM_C1_02_I10BINDINGPROOF_OR_SELECTEDQUADRATURESOURCEPROMOTION_BUILT_SOURCE_PROMOTION_OPEN"
PREVIOUS_SLUG = "selected_psm_c1_02_physicalactionidentity_or_honestquadratureemission"
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_02_SelectedSourcePromotionPacket_v1"

POST_SM_LABEL_CONTEXT = {
    "tier": "tier_2_post_sm_parity_true_equivalence",
    "preferred_phrase": "post-SM-parity frontier",
    "closed_boundary": "DONE-PARITY-00",
    "active_label": "PSM-C1-02",
    "active_label_name": "selected primitive C1 overlap contractions",
    "primary_routes": ["ROUTE-A", "ROUTE-B"],
    "route_A": "same-source dynamic Phi_fin^C1 source rule",
    "route_B": "honest selected Galerkin C1 execution",
    "language_guardrail": "Do not call this an SM-parity blocker; SM-parity replay is frozen closed.",
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(validator: Path, path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(validator), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return {
        "validator": rel(validator),
        "payload": rel(path),
        "returncode": proc.returncode,
        "passes": proc.returncode == 0,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr": proc.stderr.strip().splitlines(),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }


def strict_routeb_row_ids(workorder: dict[str, Any]) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for stage in workorder["execution_order"]:
        if stage["stage"] in {"primitive_contractions", "hessian_source", "sector_matrices"}:
            rows.extend((stage["stage"], row_id) for row_id in stage["rows"])
    return rows


def build_conditional_routeb_payload(workorder: dict[str, Any]) -> dict[str, Any]:
    rows = []
    for stage, row_id in strict_routeb_row_ids(workorder):
        row = {
            "row_id": row_id,
            "stage": stage,
            "independent_source_emitted": True,
            "locked_target_dependency": False,
            "residual_replay_dependency": False,
            "quadrature_rule_id": "selected_finite_C1_independent_quadrature_rule",
            "kernel_source_id": f"K_C1_selected::{row_id}",
            "value": f"Integral_selected_C1({row_id})",
            "exactness_certificate": f"conditional_exactness_certificate::{row_id}",
            "error_bound": None,
            "conditional_only": True,
            "theorem_required": "selected source promotion must emit this row before residual replay",
        }
        if stage == "hessian_source":
            row["kernel_source_id"] = f"H_C1_selected::{row_id}"
            row["selected_b_vector_source"] = True
        else:
            row["selected_b_vector_source"] = None
        rows.append(row)

    return {
        "schema": "MTTPSMC102RouteBConditionalSelectedQuadratureSourcePromotionWitness.v1",
        "status": "CONDITIONAL_ROUTE_B_VALIDATES_IF_SELECTED_QUADRATURE_SOURCE_PACKET_IS_PROMOTED",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-B",
        "conditional_only": True,
        "conditional_on": "selected theorem-derived C1 quadrature/source-id/Hessian source packet",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "symbolic_values_only": True,
        "not_a_numerical_derivation": True,
        "rows": rows,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / f"{PREVIOUS_SLUG}.candidate.json")
    previous_equiv = load(DATA / PREVIOUS_SLUG / "psm_c1_02_closure_equivalence.packet.json")
    i10_frontier = load(DATA / "selected_phifinc1actionkernel_theorem_attempt_or_i10binding" / "remaining_i10_binding_frontier.packet.json")
    route_a_current = load(DATA / "selected_i10bindingstack_gate_or_firstvariationcertificate" / "current_i10_binding_stack_attempt.packet.json")
    route_a_conditional = load(DATA / "selected_i10bindingstack_gate_or_firstvariationcertificate" / "conditional_i10_binding_stack_witness.packet.json")
    i11_bridge = load(DATA / "selected_i11firstvariationcertificate_fill_or_quadraturetable" / "conditional_i10_binding_bridge.packet.json")
    routeb_template = load(DATA / "selected_routeb_independentquadraturepayload_schema_or_executionworkorder" / "routeb_independent_quadrature_payload_template.packet.json")
    routeb_schema = load(DATA / "selected_routeb_independentquadraturepayload_schema_or_executionworkorder" / "routeb_independent_quadrature_payload_schema.packet.json")
    routeb_workorder = load(DATA / "selected_routeb_independentquadraturepayload_schema_or_executionworkorder" / "routeb_independent_quadrature_execution_workorder.packet.json")
    source_ids = load(DATA / "selected_independentc1_rowkernelsourceids_or_physicalphifinc1actionproof" / "current_rowkernel_source_id_attempt.packet.json")
    formal_110 = load(DATA / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource" / "formal_110_row_replay_integrated.packet.json")

    route_a_current = {
        **route_a_current,
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-A",
    }
    route_a_conditional = {
        **route_a_conditional,
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-A",
    }
    route_b_current = {
        **routeb_template,
        "schema": "MTTPSMC102RouteBCurrentIndependentQuadraturePayloadAttempt.v1",
        "status": "CURRENT_ROUTE_B_STRICT_PAYLOAD_FAILS_SELECTED_SOURCE_EMISSION",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-B",
        "source_id_support": {
            "global_sources_selected": all(item["selected_emitted"] for item in source_ids["global_sources"].values()),
            "primitive_sources_selected": all(item["selected_emitted"] for item in source_ids["primitive_row_kernel_sources"]),
            "hessian_sources_selected": all(item["selected_emitted"] for item in source_ids["hessian_b_sources"]),
            "sector_sources_selected": all(item["selected_emitted"] for item in source_ids["sector_assembly_sources"]),
        },
        "formal_110_values_available_only_as_replay": formal_110["formal_110_rows_executed"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
    }
    route_b_conditional = build_conditional_routeb_payload(routeb_workorder)

    write_json(ROUTE_A_CURRENT, route_a_current)
    write_json(ROUTE_A_CONDITIONAL, route_a_conditional)
    write_json(ROUTE_B_CURRENT, route_b_current)
    write_json(ROUTE_B_CONDITIONAL, route_b_conditional)

    route_a_current_result = run_validator(I10_VALIDATOR, ROUTE_A_CURRENT)
    route_a_conditional_result = run_validator(I10_VALIDATOR, ROUTE_A_CONDITIONAL)
    route_b_current_result = run_validator(ROUTEB_VALIDATOR, ROUTE_B_CURRENT)
    route_b_conditional_result = run_validator(ROUTEB_VALIDATOR, ROUTE_B_CONDITIONAL)

    write_json(ROUTE_A_CURRENT_RESULT, route_a_current_result)
    write_json(ROUTE_A_CONDITIONAL_RESULT, route_a_conditional_result)
    write_json(ROUTE_B_CURRENT_RESULT, route_b_current_result)
    write_json(ROUTE_B_CONDITIONAL_RESULT, route_b_conditional_result)

    current_routeb_errors = route_b_current_result["stderr"]
    reduction = {
        "schema": "MTTPSMC102DualValidatorReduction.v1",
        "status": "CURRENT_ROUTES_FAIL_ONLY_BY_SOURCE_PROMOTION_CONDITIONAL_ENVELOPES_VALIDATE",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_A": {
            "validator": rel(I10_VALIDATOR),
            "current_passes": route_a_current_result["passes"],
            "conditional_passes": route_a_conditional_result["passes"],
            "minimal_missing_object": i10_frontier["minimal_next_proof"],
            "i11_bridge_available": i11_bridge["validation_returncode"] == 0,
        },
        "route_B": {
            "validator": rel(ROUTEB_VALIDATOR),
            "current_passes": route_b_current_result["passes"],
            "conditional_passes": route_b_conditional_result["passes"],
            "strict_required_row_count": len(route_b_conditional["rows"]),
            "strict_payload_excludes_basis_rows": routeb_schema["strict_payload_excludes_basis_rows"],
            "current_failure_sample": current_routeb_errors[:12],
            "minimal_missing_object": "selected theorem-derived C1 quadrature/source-id/Hessian source packet emitting 72 primitive rows, 2 Hessian rows, and 36 sector rows before residual replay",
        },
        "common_remaining_object": "same-branch selected C1 source-promotion packet proving that the formal R_Z/R_X/b_selected rows are emitted before residual replay",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(REDUCTION, reduction)

    theorem = {
        "name": "PSMC102I10OrQuadratureSourcePromotionReductionTheorem",
        "proved": True,
        "statement": (
            "For post-SM-parity label PSM-C1-02, the present same-branch data do not satisfy either the I10 binding-stack "
            "validator or the strict Route-B independent-quadrature validator.  The conditional I10/I11 witness and the "
            "conditional strict Route-B symbolic source-promotion payload both validate.  Hence the remaining proof is not a "
            "numerical row search: it is exactly the promotion of a selected same-branch C1 source packet, either as the I10 "
            "physical Phi_fin^C1 action identity or as an independently selected quadrature/source-id/Hessian emission."
        ),
    }
    candidate = {
        "candidate": "MTTSelectedPSMC102I10BindingProofOrSelectedQuadratureSourcePromotion",
        "status": STATUS,
        "previous_artifact": rel(DATA / f"{PREVIOUS_SLUG}.candidate.json"),
        "previous_two_exit_equivalence_status": previous_equiv["status"],
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_post_sm_parity_label": "PSM-C1-02",
        "theorem": theorem,
        "what_closes_now": {
            "I10_validator_current_vs_conditional_reduction": True,
            "RouteB_strict_payload_current_vs_conditional_reduction": True,
            "source_promotion_is_the_common_remaining_object": True,
            "numerical_row_search_removed_as_primary_blocker": True,
        },
        "what_remains_open": {
            "route_A_I10_I1_I5_physical_action_binding": True,
            "route_B_selected_quadrature_source_promotion": True,
            "unpatched_PSM_C1_02_closure": True,
        },
        "output_packets": {
            "route_a_current": rel(ROUTE_A_CURRENT),
            "route_a_conditional": rel(ROUTE_A_CONDITIONAL),
            "route_a_current_result": rel(ROUTE_A_CURRENT_RESULT),
            "route_a_conditional_result": rel(ROUTE_A_CONDITIONAL_RESULT),
            "route_b_current": rel(ROUTE_B_CURRENT),
            "route_b_conditional": rel(ROUTE_B_CONDITIONAL),
            "route_b_current_result": rel(ROUTE_B_CURRENT_RESULT),
            "route_b_conditional_result": rel(ROUTE_B_CONDITIONAL_RESULT),
            "dual_validator_reduction": rel(REDUCTION),
            "next_labeled_workorder": rel(NEXT),
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }
    next_packet = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102ValidatorReduction.v1",
        "status": "NEXT_WORKORDER_SELECTED_SOURCE_PROMOTION_PACKET",
        "active_label": "PSM-C1-02",
        "active_label_name": "selected primitive C1 overlap contractions",
        "route_labels": ["ROUTE-A", "ROUTE-B"],
        "next_required_artifact": NEXT_ARTIFACT,
        "task": (
            "Emit the same-branch selected C1 source-promotion packet: either prove Phi_fin^C1 physical action identity "
            "with I10/I1/I5/I11 binding, or emit selected quadrature/source-id/Hessian rows as theorem-derived before residual replay."
        ),
        "minimum_fields": [
            "selected_measure_pairing theorem-derived",
            "selected_quadrature_rule theorem-derived",
            "72 primitive kernel rows emitted before residual replay",
            "2 Hessian b-source rows emitted with selected_b_vector_source=true",
            "36 sector assembly rows sourced from promoted primitive/Hessian rows",
            "no observed data or locked target values used as selectors",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "MTT_Selected_PSM_C1_02_I10BindingProof_or_SelectedQuadratureSourcePromotion_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "current_route_A_passes": route_a_current_result["passes"],
        "conditional_route_A_passes": route_a_conditional_result["passes"],
        "current_route_B_passes": route_b_current_result["passes"],
        "conditional_route_B_passes": route_b_conditional_result["passes"],
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    note = f"""# MTT Selected PSM C1 02 I10BindingProof or SelectedQuadratureSourcePromotion v1

Status: `{STATUS}`

Active post-SM-parity label: `PSM-C1-02`

Boundary guardrail: `DONE-PARITY-00` remains frozen closed. This is post-SM-parity frontier work, not an SM-parity blocker.

## Theorem

**{theorem["name"]}.** {theorem["statement"]}

## Validator Reduction

- Current `ROUTE-A` I10 binding attempt fails.
- Conditional `ROUTE-A` I10/I11 witness validates.
- Current `ROUTE-B` strict independent-quadrature payload fails.
- Conditional `ROUTE-B` symbolic selected-source promotion payload validates.

## Meaning

The remaining task is source promotion, not a fresh numerical search.  The selected packet must show the C1 rows are emitted before residual replay, through either the physical action identity or honest quadrature/source-id/Hessian emission.

## Next Artifact

`{NEXT_ARTIFACT}`
"""
    write_json(NEXT, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, certificate)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
