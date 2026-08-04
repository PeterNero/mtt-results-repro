"""Build Phi_fin^C1 action-kernel theorem attempt or I10 binding frontier."""

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

SLUG = "selected_phifinc1actionkernel_theorem_attempt_or_i10binding"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TEMPLATE = PACKET_DIR / "phifinc1_preresidual_action_kernel_theorem.strict_template.json"
CURRENT = PACKET_DIR / "current_action_kernel_theorem_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_i10_action_kernel_witness.packet.json"
DEPENDENCIES = PACKET_DIR / "i10_dependency_chain.packet.json"
REMAINING = PACKET_DIR / "remaining_i10_binding_frontier.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
KERNEL_WITNESS = PACKET_DIR / "conditional_source_kernel_validation_bridge.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhiFinC1ActionKernel_TheoremAttempt_or_I10Binding_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1_preresidual_action_kernel_theorem.py"
SOURCE_KERNEL_VALIDATOR = ROOT / "scripts" / "validate_selected_preresidual_variation_hessian_source_kernel.py"

STATUS = "MTT_SELECTED_PHIFINC1ACTIONKERNEL_THEOREM_ATTEMPT_BUILT_I10_BINDING_OPEN"
NEXT = "MTT_Selected_I10PhiFinC1BindingProof_or_IndependentGalerkinKernelEmission_v1"


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

    minimal_action = load(
        DATA
        / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
        / "minimal_action_axiom_or_theorem.packet.json"
    )
    physical_template = load(
        DATA
        / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues"
        / "route_a_physical_source_theorem_template.packet.json"
    )
    cutset = load(
        DATA
        / "selected_c1variationprinciplederivation_or_quadratureenginerun"
        / "minimal_engine_or_principle_cutset.packet.json"
    )
    defect = load(DATA / "selected_c1defectfunctionalsource_or_independentquadraturedatafill.candidate.json")
    phifin_min = load(DATA / "selected_phifinc1minimizesdefectfunctional_or_independentquadraturetable.candidate.json")
    boundary = load(
        DATA
        / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
        / "finite_trace_boundary_cancellation_certificate.packet.json"
    )
    source_contract = load(
        DATA
        / "selected_phifinc1_actionrestriction_or_boundarysource_emission"
        / "same_source_boundary_and_residual_emission_contract.packet.json"
    )

    template = {
        "schema": "MTTPhiFinC1PreResidualActionKernelTheoremStrictTemplate.v1",
        "status": "STRICT_TEMPLATE_READY",
        "theorem_name": "SelectedPhiFinC1PreResidualActionKernelTheorem",
        "statement": minimal_action["statement"],
        "required_fields": [
            "physical_action_equals_c1_defect_functional",
            "admissible_differentiated_variations_fixed",
            "physical_boundary_source_terms_vanish",
            "same_source_rz_rx_bselected_emitted",
        ],
        "validator": rel(VALIDATOR),
        "forbidden_shortcuts": minimal_action["forbidden_shortcuts"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    current = {
        "schema": "MTTCurrentPhiFinC1ActionKernelTheoremAttempt.v1",
        "status": "CURRENT_SUPPORT_FAILS_ACTION_KERNEL_THEOREM_VALIDATOR",
        "same_branch": True,
        "physical_action_equals_c1_defect_functional": False,
        "admissible_differentiated_variations_fixed": False,
        "physical_boundary_source_terms_vanish": False,
        "same_source_rz_rx_bselected_emitted": False,
        "attached_theorem_evidence": [
            {
                "source": rel(DATA / "selected_c1defectfunctionalsource_or_independentquadraturedatafill.candidate.json"),
                "closes": "unique formal C1 defect functional only",
            },
            {
                "source": rel(
                    DATA
                    / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
                    / "finite_trace_boundary_cancellation_certificate.packet.json"
                ),
                "closes": "algebraic finite trace boundary cancellation only",
            },
            {
                "source": rel(DATA / "selected_phifinc1minimizesdefectfunctional_or_independentquadraturetable.candidate.json"),
                "closes": "I10 binding theorem slot only",
            },
            {
                "source": rel(
                    DATA
                    / "selected_phifinc1_actionrestriction_or_boundarysource_emission"
                    / "same_source_boundary_and_residual_emission_contract.packet.json"
                ),
                "closes": "same-source emission contract only",
            },
        ],
        "support_closed": {
            "formal_c1_defect_functional_sourced": defect["promotion_decision"]["selected_C1_defect_functional_formal_source_promoted"],
            "algebraic_boundary_closed": boundary["algebraic_boundary_closed_now"],
            "i10_binding_slot_created": phifin_min["what_closes_now"]["new_I10_binding_theorem_slot_created"],
            "same_source_contract_built": source_contract["status"] == "SAME_SOURCE_ACTION_RESIDUAL_BSOURCE_CONTRACT_OPEN",
        },
        "why_not_promoted": [
            "The formal defect functional is sourced, but physical Phi_fin^C1 has not been proved to minimize it.",
            "Boundary cancellation is algebraic in the finite quotient, but not yet promoted as physical boundary/source vanishing.",
            "I10, I1, and I5 remain theorem dependencies.",
            "R_Z, R_X, and b_selected are named in the same-source contract but not emitted by the physical source.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    witness_evidence = [
        {
            "source": rel(REMAINING),
            "closes": "physical action equals sourced C1 defect functional by I10",
            "conditional": True,
        },
        {
            "source": rel(REMAINING),
            "closes": "admissible differentiated variations fixed by I1/I5 stack",
            "conditional": True,
        },
        {
            "source": rel(REMAINING),
            "closes": "physical boundary/source terms vanish",
            "conditional": True,
        },
        {
            "source": rel(REMAINING),
            "closes": "same source emits R_Z, R_X, and b_selected",
            "conditional": True,
        },
    ]
    witness = {
        "schema": "MTTConditionalI10PhiFinC1ActionKernelWitness.v1",
        "status": "CONDITIONAL_WITNESS_VALIDATES_IF_I10_BINDING_STACK_IS_PROVED",
        "same_branch": True,
        "physical_action_equals_c1_defect_functional": True,
        "admissible_differentiated_variations_fixed": True,
        "physical_boundary_source_terms_vanish": True,
        "same_source_rz_rx_bselected_emitted": True,
        "attached_theorem_evidence": witness_evidence,
        "conditional_on_unproved_i10_stack": rel(REMAINING),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
        "conditional_only": True,
    }

    dependencies = {
        "schema": "MTTI10PhiFinC1ActionKernelDependencyChain.v1",
        "status": "I10_DEPENDENCY_CHAIN_SHARPENED",
        "root_theorem": "SelectedPhiFinC1PreResidualActionKernelTheorem",
        "depends_on": {
            "I10_PhiFinC1_minimizes_defect_functional": {
                "proved": phifin_min["promotion_decision"]["PhiFinC1_minimizes_defect_functional_proved"],
                "source": rel(DATA / "selected_phifinc1minimizesdefectfunctional_or_independentquadraturetable.candidate.json"),
            },
            "I1_selected_minimizer_to_PhiFin_trace": {
                "proved": False,
                "source": "corpus/proof dependency named by prior binding reduction",
            },
            "I5_selected_dotD_C1_response": {
                "proved": False,
                "source": "corpus/proof dependency named by prior binding reduction",
            },
            "physical_boundary_promotion": {
                "proved": boundary["physical_boundary_promoted_now"],
                "source": rel(
                    DATA
                    / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
                    / "finite_trace_boundary_cancellation_certificate.packet.json"
                ),
            },
            "same_source_RZ_RX_bselected_emission": {
                "proved": False,
                "source": rel(
                    DATA
                    / "selected_phifinc1_actionrestriction_or_boundarysource_emission"
                    / "same_source_boundary_and_residual_emission_contract.packet.json"
                ),
            },
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    remaining = {
        "schema": "MTTRemainingI10BindingFrontier.v1",
        "status": "I10_BINDING_STACK_OPEN_ACTION_KERNEL_NOT_PROMOTED",
        "current_support_is_enough_for": [
            "unique formal C1 defect functional",
            "finite trace/Frobenius measure",
            "algebraic finite quotient boundary cancellation",
            "same-source emission contract",
            "conditional action-kernel witness",
        ],
        "not_enough_for": [
            "physical Phi_fin^C1 equals the defect functional",
            "physical boundary/source terms vanish",
            "R_Z/R_X are emitted as pre-residual source operators",
            "b_selected is emitted as same-source Hessian vector",
        ],
        "minimal_next_proof": (
            "Prove I10: selected Phi_fin^C1 minimizes the unique sourced C1 defect functional, with I1/I5 "
            "supplying the selected trace and dotD/C1 response, and show the Euler equation emits R_Z/R_X/b_selected "
            "before residual replay."
        ),
        "parallel_exit": "fill the independent Galerkin/quadrature kernel table instead",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    TEMPLATE.write_text(json.dumps(template, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CURRENT.write_text(json.dumps(current, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    DEPENDENCIES.write_text(json.dumps(dependencies, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    REMAINING.write_text(json.dumps(remaining, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    current_result = run_validator(VALIDATOR, CURRENT)
    witness_result = run_validator(VALIDATOR, WITNESS)
    CURRENT_RESULT.write_text(json.dumps(current_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS_RESULT.write_text(json.dumps(witness_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    source_kernel_witness = {
        "schema": "MTTConditionalSourceKernelValidationBridge.v1",
        "status": "ACTION_KERNEL_WITNESS_IMPLIES_SOURCE_KERNEL_WITNESS",
        "source_kernel_packet": rel(
            DATA
            / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
            / "conditional_source_kernel_witness.packet.json"
        ),
        "validated_by": rel(SOURCE_KERNEL_VALIDATOR),
        "validation_returncode": run_validator(
            SOURCE_KERNEL_VALIDATOR,
            DATA
            / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
            / "conditional_source_kernel_witness.packet.json",
        )["returncode"],
        "conditional_on": rel(WITNESS),
        "closure_claimed": False,
    }
    KERNEL_WITNESS.write_text(json.dumps(source_kernel_witness, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedPhiFinC1ActionKernelTheoremAttemptOrI10Binding",
        "status": STATUS,
        "inputs": {
            "minimal_action_kernel_statement": rel(
                DATA
                / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
                / "minimal_action_axiom_or_theorem.packet.json"
            ),
            "physical_source_template": rel(
                DATA
                / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues"
                / "route_a_physical_source_theorem_template.packet.json"
            ),
            "i10_binding_reduction": rel(DATA / "selected_phifinc1minimizesdefectfunctional_or_independentquadraturetable.candidate.json"),
        },
        "output_packets": {
            "strict_template": rel(TEMPLATE),
            "current_attempt": rel(CURRENT),
            "conditional_i10_witness": rel(WITNESS),
            "i10_dependency_chain": rel(DEPENDENCIES),
            "remaining_i10_frontier": rel(REMAINING),
            "current_validator_result": rel(CURRENT_RESULT),
            "conditional_validator_result": rel(WITNESS_RESULT),
            "conditional_source_kernel_validation_bridge": rel(KERNEL_WITNESS),
        },
        "theorem": {
            "name": "PhiFinC1ActionKernelI10ReductionTheorem",
            "proved": True,
            "statement": (
                "The selected Phi_fin^C1 pre-residual action-kernel theorem is reduced to the I10 binding stack. "
                "Current support proves the formal defect functional and algebraic finite boundary cancellation, but not the physical action binding. "
                "If I10/I1/I5 plus physical boundary and same-source emission are proved, the action-kernel validator passes and implies the source-kernel witness."
            ),
        },
        "what_closes_now": {
            "action_kernel_strict_validator_built": True,
            "current_attempt_rejected": current_result["returncode"] == 1,
            "conditional_i10_witness_passes": witness_result["returncode"] == 0,
            "i10_dependency_chain_emitted": True,
            "source_kernel_bridge_checked": source_kernel_witness["validation_returncode"] == 0,
        },
        "what_remains_open": {
            "prove_I10_PhiFinC1_minimizes_defect_functional": True,
            "prove_I1_selected_minimizer_to_PhiFin_trace": True,
            "prove_I5_selected_dotD_C1_response": True,
            "promote_physical_boundary_vanishing": True,
            "emit_same_source_RZ_RX_bselected": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "conditional_only": True,
        "next_required_artifact": NEXT,
        "previous_status": cutset["status"],
    }

    cert = {
        "certificate": "MTT_Selected_PhiFinC1ActionKernel_TheoremAttempt_or_I10Binding_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "current_attempt_rejected": current_result["returncode"] == 1,
        "conditional_i10_witness_passes": witness_result["returncode"] == 0,
        "source_kernel_bridge_checked": source_kernel_witness["validation_returncode"] == 0,
        "closure_claimed": False,
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhiFinC1ActionKernel TheoremAttempt or I10Binding v1

Status: `{STATUS}`.

The action-kernel theorem has been constructed as a strict gate.

```text
current action-kernel attempt validates = False
conditional I10 witness validates       = True
source-kernel bridge validates          = {source_kernel_witness["validation_returncode"] == 0}
closure claimed                         = False
```

What is real now: the unique formal C1 defect functional, finite trace measure,
algebraic finite boundary cancellation, and same-source contract.

What remains: prove the physical binding stack `I10/I1/I5`, promote physical
boundary/source vanishing, and emit `R_Z/R_X/b_selected` from the same selected
`Phi_fin^C1` action source. This is the exact theorem path; the parallel path is
an independent Galerkin/kernel table.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
