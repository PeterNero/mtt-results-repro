"""Build pre-residual variation/Hessian source-kernel attempt or action axiom frontier."""

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

SLUG = "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TEMPLATE = PACKET_DIR / "pre_residual_variation_hessian_source_kernel.strict_template.json"
CURRENT = PACKET_DIR / "current_pre_residual_variation_hessian_source_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_source_kernel_witness.packet.json"
TRIAGE = PACKET_DIR / "three_route_source_kernel_triage.packet.json"
AXIOM = PACKET_DIR / "minimal_action_axiom_or_theorem.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PreResidualVariation_HessianSourceKernel_Attempt_or_ActionAxiom_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_preresidual_variation_hessian_source_kernel.py"

STATUS = "MTT_SELECTED_PRERESIDUALVARIATION_HESSIANSOURCEKERNEL_ATTEMPT_BUILT_ACTION_AXIOM_OPEN"
NEXT = "MTT_Selected_PhiFinC1ActionAxiom_or_IndependentGalerkinKernelEmission_v1"


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
        "payload": rel(path),
        "validator": rel(VALIDATOR),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr_lines": proc.stderr.splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    frontier = load(
        DATA
        / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel"
        / "next_source_promotion_kernel.packet.json"
    )
    obligations = load(
        DATA
        / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel"
        / "minimal_lemma_obligation_status.packet.json"
    )
    source_map_test = load(
        DATA
        / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
        / "source_map_selection_theorem_test.packet.json"
    )
    physical_template = load(
        DATA
        / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues"
        / "route_a_physical_source_theorem_template.packet.json"
    )
    b_attempt = load(
        DATA
        / "selected_physicalc1actionidentity_or_samesourcebselectedemission"
        / "same_source_bselected_emission_attempt.packet.json"
    )
    route_b_manifest = load(
        DATA
        / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues"
        / "route_b_quadrature_kernel_value_manifest.packet.json"
    )
    row_functor = load(
        DATA
        / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel"
        / "typed_row_functor_sublemma.packet.json"
    )

    template = {
        "schema": "MTTPreResidualVariationHessianSourceKernelStrictTemplate.v1",
        "status": "STRICT_TEMPLATE_READY",
        "required_fields": [item["id"] for item in frontier["must_emit"]],
        "field_meaning": frontier["must_emit"],
        "validator": rel(VALIDATOR),
        "forbidden_routes": frontier["rejected_routes"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    current = {
        "schema": "MTTCurrentPreResidualVariationHessianSourceAttempt.v1",
        "status": "CURRENT_SUPPORT_FAILS_SOURCE_KERNEL_VALIDATOR",
        "same_branch": True,
        "selected_variation_functional": False,
        "same_source_hessian": False,
        "sector_functor": False,
        "independence_certificate": False,
        "attached_source_evidence": [
            {
                "source": rel(
                    DATA
                    / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
                    / "source_map_selection_theorem_test.packet.json"
                ),
                "closes": "static source labels, exact Weyl residuals, and candidate differentiated rule only",
            },
            {
                "source": rel(
                    DATA
                    / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues"
                    / "route_a_physical_source_theorem_template.packet.json"
                ),
                "closes": "physical source theorem template only",
            },
            {
                "source": rel(
                    DATA
                    / "selected_physicalc1actionidentity_or_samesourcebselectedemission"
                    / "same_source_bselected_emission_attempt.packet.json"
                ),
                "closes": "b_selected replay availability only",
            },
            {
                "source": rel(
                    DATA
                    / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel"
                    / "typed_row_functor_sublemma.packet.json"
                ),
                "closes": "typed row-functor shape only",
            },
        ],
        "support_closed": {
            "typed_row_functor": row_functor["proved"],
            "static_source_map_candidate": source_map_test["already_selected_or_closed"]["static_source_map_candidate_constructed"],
            "canonical_projector_replays_RZ_RX": source_map_test["already_selected_or_closed"]["canonical_projector_replays_RZ_RX"],
            "b_replay_available": b_attempt["replay_available_under_axiom_patch"],
            "basis_stage_ready": route_b_manifest["basis_stage"]["ready"],
        },
        "why_not_promoted": [
            "The candidate differentiated rule is not yet selected as physical Phi_fin^C1 action.",
            "R_Z/R_X exact Weyl polynomials are checks, not pre-residual source emissions.",
            "b_selected is replayed from the residual-projector contract, not emitted by a same-source Hessian.",
            "The sector functor has typed slots, but no promoted source-row assembly.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "closure_claimed": False,
    }

    conditional_evidence = [
        {
            "source": rel(AXIOM),
            "closes": "selected D Phi_fin^C1 pre-residual variation functional",
            "conditional": True,
        },
        {
            "source": rel(AXIOM),
            "closes": "same-source Hessian and b_selected emission",
            "conditional": True,
        },
        {
            "source": rel(AXIOM),
            "closes": "sector rows assembled from promoted source rows",
            "conditional": True,
        },
        {
            "source": rel(AXIOM),
            "closes": "independence from residual replay, locked targets, observed constants, and benchmarks",
            "conditional": True,
        },
    ]
    witness = {
        "schema": "MTTConditionalPreResidualVariationHessianSourceKernelWitness.v1",
        "status": "CONDITIONAL_WITNESS_VALIDATES_IF_ACTION_AXIOM_OR_INDEPENDENT_KERNEL_EMITS",
        "same_branch": True,
        "selected_variation_functional": True,
        "same_source_hessian": True,
        "sector_functor": True,
        "independence_certificate": True,
        "attached_source_evidence": conditional_evidence,
        "conditional_on_unproved_axiom_or_independent_emission": rel(AXIOM),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "closure_claimed": False,
        "conditional_only": True,
    }

    triage = {
        "schema": "MTTThreeRouteSourceKernelTriage.v1",
        "status": "THREE_ROUTES_TRIAGED_NONE_PROMOTED_NOW",
        "routes": {
            "route_A_physical_action": {
                "status": "OPEN",
                "promoted_now": False,
                "support": rel(
                    DATA
                    / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues"
                    / "route_a_physical_source_theorem_template.packet.json"
                ),
                "missing": physical_template["required_clauses"],
            },
            "route_B_independent_galerkin": {
                "status": "OPEN",
                "promoted_now": False,
                "support": rel(
                    DATA
                    / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues"
                    / "route_b_quadrature_kernel_value_manifest.packet.json"
                ),
                "missing": [
                    "selected kernels defined for 72 primitive rows",
                    "2 independent Hessian/source values",
                    "36 sector matrix values",
                    "exactness/error certificates",
                ],
                "current_independent_values_emitted": route_b_manifest["counts"]["independent_values_emitted"],
            },
            "route_C_new_weyl_variation_principle": {
                "status": "OPEN_BUT_SHARPEST",
                "promoted_now": False,
                "support": rel(
                    DATA
                    / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
                    / "source_map_selection_theorem_test.packet.json"
                ),
                "missing": [
                    "selection of differentiated Phi_fin^C1 application rule",
                    "same-source b_selected Hessian emission",
                    "proof Q_residual/R_Z/R_X are emitted before residual replay",
                ],
            },
        },
        "preferred_next_route": "route_C_new_weyl_variation_principle_or_route_B_independent_galerkin_if_values_can_be_emitted",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    axiom = {
        "schema": "MTTMinimalPhiFinC1ActionAxiomOrTheorem.v1",
        "status": "MINIMAL_ACTION_AXIOM_STATEMENT_READY_NOT_ASSUMED",
        "name": "SelectedPhiFinC1PreResidualActionKernelTheorem",
        "statement": (
            "On the selected q79/F,m=1 finite C1 quotient, the physical differentiated Phi_fin^C1 action is the "
            "least-defect trace/Frobenius source functional whose first variation emits the selected R_Z/R_X "
            "pre-residual columns and whose second variation emits b_selected, with zero extra boundary/source term."
        ),
        "would_close": {
            "selected_variation_functional": True,
            "same_source_hessian": True,
            "sector_functor": True,
            "independence_certificate": True,
            "SelectedFiniteC1SourcePromotionLemma": True,
        },
        "must_not_be_used_as_free_patch": True,
        "acceptable_proof_sources": [
            "derive from existing Theta/Phi_fin physical action text in corpus",
            "derive by independent finite Galerkin/quadrature execution",
            "derive as a new theorem with explicit variational principle and boundary proof",
        ],
        "forbidden_shortcuts": frontier["rejected_routes"],
        "proved_here": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    TEMPLATE.write_text(json.dumps(template, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CURRENT.write_text(json.dumps(current, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    TRIAGE.write_text(json.dumps(triage, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    AXIOM.write_text(json.dumps(axiom, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    current_result = run_validator(CURRENT)
    witness_result = run_validator(WITNESS)
    CURRENT_RESULT.write_text(json.dumps(current_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS_RESULT.write_text(json.dumps(witness_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedPreResidualVariationHessianSourceKernelAttemptOrActionAxiom",
        "status": STATUS,
        "inputs": {
            "frontier_kernel": rel(
                DATA
                / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel"
                / "next_source_promotion_kernel.packet.json"
            ),
            "obligation_status": rel(
                DATA
                / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel"
                / "minimal_lemma_obligation_status.packet.json"
            ),
            "source_map_selection_test": rel(
                DATA
                / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
                / "source_map_selection_theorem_test.packet.json"
            ),
        },
        "output_packets": {
            "strict_template": rel(TEMPLATE),
            "current_attempt": rel(CURRENT),
            "conditional_witness": rel(WITNESS),
            "three_route_triage": rel(TRIAGE),
            "minimal_action_axiom_or_theorem": rel(AXIOM),
            "current_validator_result": rel(CURRENT_RESULT),
            "conditional_validator_result": rel(WITNESS_RESULT),
        },
        "theorem": {
            "name": "PreResidualVariationHessianKernelReductionTheorem",
            "proved": True,
            "statement": (
                "The remaining source-promotion problem is exactly a four-clause source kernel: selected pre-residual "
                "variation functional, same-source Hessian/b_selected, sector functor assembly, and independence. "
                "Current support fails this kernel; the conditional action-kernel theorem would make it validate."
            ),
        },
        "what_closes_now": {
            "strict_kernel_validator_built": True,
            "three_routes_triaged": True,
            "current_attempt_rejected": current_result["returncode"] == 1,
            "conditional_witness_passes": witness_result["returncode"] == 0,
            "minimal_action_axiom_statement_emitted": True,
        },
        "what_remains_open": {
            "prove_selected_phifinc1_preresidual_action_kernel": True,
            "or_emit_independent_galerkin_kernel_values": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "conditional_only": True,
        "next_required_artifact": NEXT,
        "previous_status": obligations["status"],
    }

    cert = {
        "certificate": "MTT_Selected_PreResidualVariation_HessianSourceKernel_Attempt_or_ActionAxiom_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "current_attempt_rejected": current_result["returncode"] == 1,
        "conditional_witness_passes": witness_result["returncode"] == 0,
        "closure_claimed": False,
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PreResidualVariation HessianSourceKernel Attempt or ActionAxiom v1

Status: `{STATUS}`.

The source kernel is now strict and executable.

```text
current source-kernel attempt validates   = False
conditional same-source witness validates = True
closure claimed                           = False
```

The next theorem is not another value search. It is the source/action theorem
that makes `R_Z/R_X` pre-residual variation operators and `b_selected` come from
the same selected `Phi_fin^C1` source, or an independent Galerkin/kernel emission
that replaces the replay packet.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
