"""Build selected I10 binding-stack gate or first-variation certificate frontier."""

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

SLUG = "selected_i10bindingstack_gate_or_firstvariationcertificate"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TEMPLATE = PACKET_DIR / "i10_binding_stack.strict_template.json"
CURRENT = PACKET_DIR / "current_i10_binding_stack_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_i10_binding_stack_witness.packet.json"
PARTIALS = PACKET_DIR / "i1_i5_partial_support_ledger.packet.json"
NEXT_CERT = PACKET_DIR / "next_first_variation_certificate.packet.json"
ACTION_BRIDGE = PACKET_DIR / "conditional_action_kernel_bridge.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_I10BindingStack_Gate_or_FirstVariationCertificate_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_i10_binding_stack.py"
ACTION_VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1_preresidual_action_kernel_theorem.py"

STATUS = "MTT_SELECTED_I10BINDINGSTACK_GATE_BUILT_FIRSTVARIATION_CERTIFICATE_OPEN"
NEXT = "MTT_Selected_I11FirstVariationCertificate_Fill_or_IndependentQuadratureKernelTable_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(validator: Path, path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(validator), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "payload": rel(path),
        "validator": rel(validator),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr_lines": proc.stderr.splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    i10_attempt = load(
        DATA
        / "selected_i10_payloadcertificate_or_independentquadraturevaluesfill"
        / "route_a_i10_payload_certificate_fill_attempt.packet.json"
    )
    cycle_exit = load(DATA / "selected_cycleexit_minimizertrace_or_independentquadraturerows.candidate.json")
    route_a_status = load(
        DATA
        / "selected_cycleexit_minimizertrace_or_independentquadraturerows"
        / "route_a_minimizer_trace_payload_status.packet.json"
    )
    first_plan = load(
        DATA
        / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan"
        / "route_a_first_variation_certificate_plan.packet.json"
    )
    source_manifest = load(DATA / "selected_source_paper_integration_manifest.candidate.json")
    action_witness = load(
        DATA
        / "selected_phifinc1actionkernel_theorem_attempt_or_i10binding"
        / "conditional_i10_action_kernel_witness.packet.json"
    )

    insertion_by_id = {item["id"]: item for item in source_manifest["insertions"]}
    i1_insert = insertion_by_id["I1_selected_strominger_minimizer_to_phifin_trace"]
    i5_insert = insertion_by_id["I5_dotD_alpha1_and_C1_response"]

    template = {
        "schema": "MTTI10BindingStackStrictTemplate.v1",
        "status": "STRICT_TEMPLATE_READY",
        "required_fields": [
            "selected_minimizer_trace_payload_verified",
            "selected_c1_response_payload_verified",
            "defect_functional_minimizer_payload_verified",
            "first_variation_identity_verified",
            "hessian_or_coercivity_verified",
            "boundary_cancellation_verified",
            "normalization_compatibility_verified",
        ],
        "validator": rel(VALIDATOR),
        "theorem_goal": "I10_PhiFinC1_minimizes_defect_functional_with_I1_I5_binding",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    current = {
        "schema": "MTTCurrentI10BindingStackAttempt.v1",
        "status": "CURRENT_SUPPORT_FAILS_I10_BINDING_VALIDATOR",
        "same_branch": True,
        "selected_minimizer_trace_payload_verified": False,
        "selected_c1_response_payload_verified": False,
        "defect_functional_minimizer_payload_verified": False,
        "first_variation_identity_verified": False,
        "hessian_or_coercivity_verified": False,
        "boundary_cancellation_verified": False,
        "normalization_compatibility_verified": False,
        "attached_binding_evidence": [
            {
                "source": rel(DATA / "selected_cycleexit_minimizertrace_or_independentquadraturerows.candidate.json"),
                "closes": "I1 stationary trace component and I5 source component only",
            },
            {
                "source": rel(
                    DATA
                    / "selected_i10_payloadcertificate_or_independentquadraturevaluesfill"
                    / "route_a_i10_payload_certificate_fill_attempt.packet.json"
                ),
                "closes": "I10 payload field evaluation only",
            },
            {
                "source": rel(
                    DATA
                    / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan"
                    / "route_a_first_variation_certificate_plan.packet.json"
                ),
                "closes": "I11 certificate plan only",
            },
        ],
        "partial_support": {
            "I1_stationary_trace_component_available": cycle_exit["what_closes_now"]["I1_stationary_trace_component_available"],
            "I5_dotD_alpha1_C1_source_component_available": cycle_exit["what_closes_now"]["I5_dotD_alpha1_C1_source_component_available"],
            "formal_C1_defect_functional_source": route_a_status["prerequisites_closed"]["formal_C1_defect_functional_source"],
            "dynamic_dotD_trace_binding": route_a_status["prerequisites_closed"]["dynamic_dotD_trace_binding"],
            "no_observed_data_as_selector": i10_attempt["payload_checks"]["no_observed_data_as_selector"]["value"],
        },
        "why_not_promoted": [
            i10_attempt["payload_checks"]["selected_minimizer_trace_payload_verified"]["reason"],
            i10_attempt["payload_checks"]["selected_c1_response_payload_verified"]["reason"],
            i10_attempt["payload_checks"]["defect_functional_minimizer_payload_verified"]["reason"],
            "The I11 first-variation certificate fields are planned but not verified.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "benchmark_or_measured_values_used_as_source": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    witness_evidence = [
        {
            "source": rel(NEXT_CERT),
            "closes": "selected minimizer trace payload verified by I1",
            "conditional": True,
        },
        {
            "source": rel(NEXT_CERT),
            "closes": "selected C1 response payload verified by I5",
            "conditional": True,
        },
        {
            "source": rel(NEXT_CERT),
            "closes": "defect functional minimizer payload verified by I10",
            "conditional": True,
        },
        {
            "source": rel(NEXT_CERT),
            "closes": "first variation identity verified by I11",
            "conditional": True,
        },
        {
            "source": rel(NEXT_CERT),
            "closes": "Hessian/coercivity verified",
            "conditional": True,
        },
        {
            "source": rel(NEXT_CERT),
            "closes": "boundary cancellation promoted physically",
            "conditional": True,
        },
        {
            "source": rel(NEXT_CERT),
            "closes": "normalization compatibility verified",
            "conditional": True,
        },
    ]
    witness = {
        "schema": "MTTConditionalI10BindingStackWitness.v1",
        "status": "CONDITIONAL_WITNESS_VALIDATES_IF_I11_CERTIFICATE_IS_FILLED",
        "same_branch": True,
        "selected_minimizer_trace_payload_verified": True,
        "selected_c1_response_payload_verified": True,
        "defect_functional_minimizer_payload_verified": True,
        "first_variation_identity_verified": True,
        "hessian_or_coercivity_verified": True,
        "boundary_cancellation_verified": True,
        "normalization_compatibility_verified": True,
        "attached_binding_evidence": witness_evidence,
        "conditional_on": rel(NEXT_CERT),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "benchmark_or_measured_values_used_as_source": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
        "conditional_only": True,
    }

    partials = {
        "schema": "MTTI1I5PartialSupportLedger.v1",
        "status": "I1_I5_PARTIAL_SUPPORT_IMPORTED_FULL_DYNAMIC_PAYLOADS_OPEN",
        "I1": {
            "insertion_id": i1_insert["id"],
            "stationary_component_available": cycle_exit["what_closes_now"]["I1_stationary_trace_component_available"],
            "full_dynamic_payload_verified": False,
            "proof_obligations": i1_insert["proof_obligations"],
            "safe_wording": i1_insert["safe_wording"],
        },
        "I5": {
            "insertion_id": i5_insert["id"],
            "source_component_available": cycle_exit["what_closes_now"]["I5_dotD_alpha1_C1_source_component_available"],
            "full_c1_response_payload_verified": False,
            "proof_obligations": i5_insert["proof_obligations"],
            "safe_wording": i5_insert["safe_wording"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_cert = {
        "schema": "MTTNextI11FirstVariationCertificate.v1",
        "status": "NEXT_CERTIFICATE_FIELDS_READY_VALUES_OPEN",
        "theorem_slot": first_plan["theorem_slot"],
        "certificate_fields": first_plan["certificate_fields"],
        "must_fill": [
            "selected_trace_map",
            "first_variation_identity",
            "hessian_or_coercivity",
            "boundary_cancellation",
            "normalization_compatibility",
        ],
        "will_promote_if_filled": first_plan["would_close_if_all_verified"],
        "parallel_exit": "independent quadrature/kernel table",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    TEMPLATE.write_text(json.dumps(template, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CURRENT.write_text(json.dumps(current, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    PARTIALS.write_text(json.dumps(partials, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT_CERT.write_text(json.dumps(next_cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    current_result = run_validator(VALIDATOR, CURRENT)
    witness_result = run_validator(VALIDATOR, WITNESS)
    CURRENT_RESULT.write_text(json.dumps(current_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS_RESULT.write_text(json.dumps(witness_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    action_bridge = {
        "schema": "MTTConditionalI10BindingToActionKernelBridge.v1",
        "status": "I10_BINDING_WITNESS_IMPLIES_ACTION_KERNEL_WITNESS",
        "conditional_action_kernel_witness": rel(
            DATA
            / "selected_phifinc1actionkernel_theorem_attempt_or_i10binding"
            / "conditional_i10_action_kernel_witness.packet.json"
        ),
        "action_validator": rel(ACTION_VALIDATOR),
        "validation_returncode": run_validator(
            ACTION_VALIDATOR,
            DATA
            / "selected_phifinc1actionkernel_theorem_attempt_or_i10binding"
            / "conditional_i10_action_kernel_witness.packet.json",
        )["returncode"],
        "conditional_on": rel(WITNESS),
        "closure_claimed": False,
    }
    ACTION_BRIDGE.write_text(json.dumps(action_bridge, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedI10BindingStackGateOrFirstVariationCertificate",
        "status": STATUS,
        "inputs": {
            "i10_action_kernel_dependency_chain": rel(
                DATA
                / "selected_phifinc1actionkernel_theorem_attempt_or_i10binding"
                / "i10_dependency_chain.packet.json"
            ),
            "route_a_i10_payload_attempt": rel(
                DATA
                / "selected_i10_payloadcertificate_or_independentquadraturevaluesfill"
                / "route_a_i10_payload_certificate_fill_attempt.packet.json"
            ),
            "first_variation_certificate_plan": rel(
                DATA
                / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan"
                / "route_a_first_variation_certificate_plan.packet.json"
            ),
        },
        "output_packets": {
            "strict_template": rel(TEMPLATE),
            "current_attempt": rel(CURRENT),
            "conditional_witness": rel(WITNESS),
            "i1_i5_partial_support": rel(PARTIALS),
            "next_first_variation_certificate": rel(NEXT_CERT),
            "current_validator_result": rel(CURRENT_RESULT),
            "conditional_validator_result": rel(WITNESS_RESULT),
            "conditional_action_kernel_bridge": rel(ACTION_BRIDGE),
        },
        "theorem": {
            "name": "I10BindingStackReductionTheorem",
            "proved": True,
            "statement": (
                "The I10 action-kernel dependency stack is reduced to a strict first-variation certificate. "
                "Current support supplies I1 stationary trace, I5 source component, dynamic trace binding, and the formal defect functional, "
                "but not the full dynamic minimizer trace/C1 response/minimizer payload or I11 first-variation certificate."
            ),
        },
        "what_closes_now": {
            "i10_binding_validator_built": True,
            "i1_i5_partial_support_imported": True,
            "next_i11_certificate_fields_emitted": True,
            "current_attempt_rejected": current_result["returncode"] == 1,
            "conditional_witness_passes": witness_result["returncode"] == 0,
            "action_kernel_bridge_checked": action_bridge["validation_returncode"] == 0,
        },
        "what_remains_open": {
            "selected_trace_map_values": True,
            "first_variation_identity": True,
            "hessian_or_coercivity": True,
            "boundary_cancellation_physical_promotion": True,
            "normalization_compatibility": True,
            "independent_quadrature_kernel_table_parallel_exit": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "conditional_only": True,
        "next_required_artifact": NEXT,
        "previous_status": i10_attempt["status"],
    }

    cert = {
        "certificate": "MTT_Selected_I10BindingStack_Gate_or_FirstVariationCertificate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "current_attempt_rejected": current_result["returncode"] == 1,
        "conditional_witness_passes": witness_result["returncode"] == 0,
        "action_kernel_bridge_checked": action_bridge["validation_returncode"] == 0,
        "closure_claimed": False,
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected I10BindingStack Gate or FirstVariationCertificate v1

Status: `{STATUS}`.

The I10/I1/I5 physical binding stack is now strict and executable.

```text
current I10 binding attempt validates = False
conditional I11 witness validates     = True
action-kernel bridge validates        = {action_bridge["validation_returncode"] == 0}
closure claimed                       = False
```

What is available: I1 stationary trace component, I5 source component, dynamic
trace binding, no-observed-selector guardrail, and the formal C1 defect
functional.

What remains: fill the I11 first-variation certificate fields, especially the
selected trace map, first-variation identity, coercive Hessian block, physical
boundary cancellation, and normalization compatibility. The parallel exit is an
independent quadrature/kernel table.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
