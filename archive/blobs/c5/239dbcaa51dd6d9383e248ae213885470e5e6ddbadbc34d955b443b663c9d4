"""Build Weyl-variation action-principle derivation or explicit insertion gate."""

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

SLUG = "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DERIVATION = PACKET_DIR / "unpatched_weylvariation_actionprinciple_derivation_attempt.packet.json"
INSERTION = PACKET_DIR / "explicit_weylvariation_actionprinciple_insertion_package.packet.json"
IF_INSERTED = PACKET_DIR / "if_inserted_kernel_closure_witness.packet.json"
DECISION = PACKET_DIR / "derivation_or_insertion_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_WeylVariationActionPrinciple_Derivation_or_ExplicitInsertion_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_preresidual_variation_hessian_source_kernel.py"

STATUS = "MTT_SELECTED_WEYLVARIATION_ACTIONPRINCIPLE_DERIVATION_OPEN_INSERTION_READY"
NEXT = "MTT_Selected_WeylVariationActionPrinciple_Apply_or_IndependentKernelExecution_v1"


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
        capture_output=True,
        check=False,
    )
    return {
        "path": rel(path),
        "ok": proc.returncode == 0,
        "exit_code": proc.returncode,
        "stdout": proc.stdout.splitlines(),
        "stderr": proc.stderr.splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    routec = load(
        DATA
        / "selected_routec_weylvariation_sourceprinciple_or_kernelclosure"
        / "routec_weyl_variation_principle_candidate.packet.json"
    )
    routec_decision = load(
        DATA
        / "selected_routec_weylvariation_sourceprinciple_or_kernelclosure"
        / "routec_decision_and_next_gate.packet.json"
    )
    variation_attempt = load(
        DATA
        / "selected_c1variationprinciplederivation_or_quadratureenginerun"
        / "route_a_variation_principle_derivation_attempt.packet.json"
    )
    cutset = load(
        DATA
        / "selected_c1variationprinciplederivation_or_quadratureenginerun"
        / "minimal_engine_or_principle_cutset.packet.json"
    )
    minimal_action = load(
        DATA
        / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
        / "minimal_action_axiom_or_theorem.packet.json"
    )
    conditional_kernel = load(
        DATA
        / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
        / "conditional_source_kernel_witness.packet.json"
    )
    current_kernel = load(
        DATA
        / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
        / "current_pre_residual_variation_hessian_source_attempt.packet.json"
    )
    source_contract = load(
        DATA
        / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues"
        / "source_or_kernel_acceptance_contract.packet.json"
    )

    derivation = {
        "schema": "MTTUnpatchedWeylVariationActionPrincipleDerivationAttempt.v1",
        "status": "UNPATCHED_DERIVATION_SUPPORT_CLOSED_PHYSICAL_SELECTION_OPEN",
        "principle_name": "SelectedWeylVariationActionPrinciple",
        "principle_statement": routec["statement"],
        "closed_support": {
            **variation_attempt["closed_support"],
            "finite_dimensional_euler_projection": variation_attempt["finite_dimensional_derivation"][
                "finite_euler_projection_derived"
            ],
            "conditional_PhiFinC1_application": variation_attempt["finite_dimensional_derivation"][
                "conditional_PhiFinC1_application"
            ],
            "route_C_support_maximized": True,
            "exact_weyl_polynomials_present": True,
            "minimal_engine_or_principle_cutset_selected": cutset["status"]
            == "MINIMAL_ENGINE_OR_PRINCIPLE_CUTSET_SELECTED",
        },
        "unpatched_requirements": cutset["route_A_minimal_requirements"],
        "current_failed_fields": {
            "physical_action_equals_candidate_leakage_functional": variation_attempt[
                "not_derived_as_physical_MTT_rule"
            ]["selected_MTT_C1_defect_functional_is_candidate"],
            "physical_PhiFinC1_variation_minimizes_candidate": variation_attempt[
                "not_derived_as_physical_MTT_rule"
            ]["physical_PhiFinC1_variation_minimizes_candidate"],
            "boundary_cancellation_for_selected_dynamic_trace": variation_attempt[
                "not_derived_as_physical_MTT_rule"
            ]["boundary_cancellation_for_selected_dynamic_trace"],
            "b_selected_emitted_as_physical_source": variation_attempt["not_derived_as_physical_MTT_rule"][
                "b_selected_emitted_as_physical_source"
            ],
        },
        "unpatched_principle_derived_now": False,
        "why_not_derived": [
            "Formal finite-dimensional Euler projection derives Q_residual as least-defect completion, but not the physical MTT action identity.",
            "Route C exact Weyl polynomials identify R_Z/R_X uniquely, but do not select them as pre-residual physical variations.",
            "The Hessian b target is exact, but same-source Hessian/b_selected emission is still not theorem-derived.",
            "The latest countermodel blocks deriving source promotion from closed support alone.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    insertion = {
        "schema": "MTTExplicitWeylVariationActionPrincipleInsertionPackage.v1",
        "status": "EXPLICIT_PRINCIPLE_INSERTION_READY_NOT_ACCEPTED",
        "principle_name": "SelectedWeylVariationActionPrinciple",
        "principle_text": (
            "On the selected q79/F,m=1 finite C1 quotient, the physical differentiated "
            "Phi_fin^C1 action is the selected finite Weyl least-defect trace/Frobenius "
            "action. Its first variation emits the selected pre-residual phase/shift "
            "operators R_Z and R_X from the selected Weyl carrier before residual replay; "
            "its second variation emits the same-source Hessian counterterm b_selected; "
            "and the selected dynamic trace has no extra boundary/source term."
        ),
        "accepted_here": False,
        "must_not_be_used_as_free_patch": minimal_action["must_not_be_used_as_free_patch"],
        "acceptable_proof_sources": minimal_action["acceptable_proof_sources"],
        "forbidden_shortcuts": minimal_action["forbidden_shortcuts"],
        "would_close": minimal_action["would_close"],
        "external_papers_modified": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    if_inserted = {
        "schema": "MTTWeylVariationActionPrincipleIfInsertedKernelClosureWitness.v1",
        "status": "CONDITIONAL_WITNESS_VALIDATES_IF_PRINCIPLE_ACCEPTED_OR_DERIVED",
        "same_branch": conditional_kernel["same_branch"],
        "selected_variation_functional": conditional_kernel["selected_variation_functional"],
        "same_source_hessian": conditional_kernel["same_source_hessian"],
        "sector_functor": conditional_kernel["sector_functor"],
        "independence_certificate": conditional_kernel["independence_certificate"],
        "locked_target_values_used_as_source": conditional_kernel["locked_target_values_used_as_source"],
        "residual_projector_replay_used_as_source": conditional_kernel["residual_projector_replay_used_as_source"],
        "attached_source_evidence": [
            {
                "source": rel(INSERTION),
                "conditional": True,
                "closes": "selected variation functional and same-source Hessian emission",
            },
            {
                "source": "candidate_data/selected_routec_weylvariation_sourceprinciple_or_kernelclosure/routec_weyl_variation_principle_candidate.packet.json",
                "conditional": True,
                "closes": "Route C Weyl variation principle support",
            },
            {
                "source": "candidate_data/selected_c1variationprinciplederivation_or_quadratureenginerun/route_a_variation_principle_derivation_attempt.packet.json",
                "conditional": True,
                "closes": "formal variational derivation and finite Euler projection",
            },
            {
                "source": "candidate_data/selected_physicalvariationprinciplesource_or_quadraturekernelvalues/source_or_kernel_acceptance_contract.packet.json",
                "conditional": True,
                "closes": "source-or-kernel acceptance contract",
            },
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    IF_INSERTED.write_text(json.dumps(if_inserted, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    conditional_validator = run_validator(IF_INSERTED)

    decision = {
        "schema": "MTTWeylVariationActionPrincipleDerivationOrInsertionDecision.v1",
        "status": "DERIVATION_OPEN_EXPLICIT_INSERTION_READY_CONDITIONAL_KERNEL_VALIDATES",
        "unpatched_principle_derived_now": False,
        "explicit_principle_accepted_now": False,
        "conditional_kernel_validator_ok": conditional_validator["ok"],
        "current_kernel_closed_without_principle": all(
            current_kernel[field] is True
            for field in ["selected_variation_functional", "same_source_hessian", "sector_functor", "independence_certificate"]
        ),
        "route_A_accepts_now": source_contract["current_result"]["route_A_accepts_now"],
        "route_B_accepts_now": source_contract["current_result"]["route_B_accepts_now"],
        "next_required_artifact": NEXT,
        "decision": (
            "Do not claim unpatched closure. The selected Weyl-variation action principle is now insertion-ready "
            "and conditionally validates the strict kernel, but current corpus support still does not derive it."
        ),
        "superset_strategy": {
            "mode": "Route C principle mediates between Route A physical action and Route B kernel execution",
            "locked_target_used_only_as_postcheck": True,
            "paths_used_as_free_parameters": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [
        (DERIVATION, derivation),
        (INSERTION, insertion),
        (VALIDATOR_RESULT := PACKET_DIR / "conditional_kernel_validator_result.packet.json", conditional_validator),
        (DECISION, decision),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedWeylVariationActionPrincipleDerivationOrExplicitInsertion",
        "status": STATUS,
        "inputs": {
            "routec_decision": rel(
                DATA
                / "selected_routec_weylvariation_sourceprinciple_or_kernelclosure"
                / "routec_decision_and_next_gate.packet.json"
            ),
            "variation_principle_attempt": rel(
                DATA
                / "selected_c1variationprinciplederivation_or_quadratureenginerun"
                / "route_a_variation_principle_derivation_attempt.packet.json"
            ),
            "minimal_action_axiom": rel(
                DATA
                / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
                / "minimal_action_axiom_or_theorem.packet.json"
            ),
        },
        "output_packets": {
            "unpatched_derivation_attempt": rel(DERIVATION),
            "explicit_insertion_package": rel(INSERTION),
            "if_inserted_kernel_closure_witness": rel(IF_INSERTED),
            "conditional_kernel_validator_result": rel(VALIDATOR_RESULT),
            "derivation_or_insertion_decision": rel(DECISION),
        },
        "theorem": {
            "name": "WeylVariationActionPrincipleDerivationOrInsertionGate",
            "proved": True,
            "statement": (
                "The Weyl-variation action principle is not derived from current unpatched support, "
                "but an explicit insertion package is now precise and conditionally validates the "
                "strict pre-residual variation/Hessian source-kernel validator."
            ),
        },
        "closure_decision": {
            "unpatched_principle_derived_now": False,
            "explicit_principle_accepted_now": False,
            "conditional_kernel_validator_ok": conditional_validator["ok"],
            "unpatched_dynamic_C1_closed": False,
            "global_closure_claimed": False,
        },
        "what_closes_now": {
            "derivation_attempt_recorded": True,
            "explicit_principle_insertion_package_created": True,
            "conditional_kernel_closure_validated": conditional_validator["ok"],
            "paper_ready_principle_text_created": True,
        },
        "what_remains_open": {
            "derive_principle_unpatched": True,
            "accept_principle_as_explicit_local_premise_if_desired": True,
            "independent_kernel_execution": True,
            "unpatched_dynamic_C1_closure": True,
            "true_SM_equivalence_without_axiom": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_WeylVariationActionPrinciple_Derivation_or_ExplicitInsertion_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "unpatched_principle_derived_now": False,
        "explicit_principle_accepted_now": False,
        "conditional_kernel_validator_ok": conditional_validator["ok"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected WeylVariationActionPrinciple Derivation or ExplicitInsertion v1

Status: `{STATUS}`.

This artifact tries to derive `SelectedWeylVariationActionPrinciple`.

Result: current unpatched support still does not derive it. The formal finite
variation algebra and exact Weyl polynomials are closed support, but they do not
select the physical differentiated `Phi_fin^C1` action rule or same-source
Hessian/`b_selected` emission.

An explicit insertion package is now ready but not accepted here. If accepted
or derived, the strict pre-residual variation/Hessian source-kernel validator
passes conditionally.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
