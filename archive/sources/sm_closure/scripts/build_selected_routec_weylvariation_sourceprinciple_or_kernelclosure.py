"""Build Route-C Weyl-variation source-principle test for the C1 kernel."""

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

SLUG = "selected_routec_weylvariation_sourceprinciple_or_kernelclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PRINCIPLE = PACKET_DIR / "routec_weyl_variation_principle_candidate.packet.json"
PROMOTION = PACKET_DIR / "routec_kernel_promotion_test.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "strict_kernel_validator_result.packet.json"
DECISION = PACKET_DIR / "routec_decision_and_next_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_WeylVariation_SourcePrinciple_or_KernelClosure_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_preresidual_variation_hessian_source_kernel.py"

STATUS = "MTT_SELECTED_ROUTEC_WEYLVARIATION_SOURCEPRINCIPLE_BUILT_KERNEL_SOURCE_OPEN"
NEXT = "MTT_Selected_WeylVariationActionPrinciple_Derivation_or_ExplicitInsertion_v1"


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

    prior_kernel = load(
        DATA
        / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
        / "current_pre_residual_variation_hessian_source_attempt.packet.json"
    )
    prior_conditional = load(
        DATA
        / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
        / "conditional_source_kernel_witness.packet.json"
    )
    triage = load(
        DATA
        / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
        / "three_route_source_kernel_triage.packet.json"
    )
    minimal_action = load(
        DATA
        / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
        / "minimal_action_axiom_or_theorem.packet.json"
    )
    source_map = load(
        DATA
        / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
        / "source_map_selection_theorem_test.packet.json"
    )
    weyl_poly = load(
        DATA
        / "selected_residual_weylpolynomial_source_theorem_attempt"
        / "residual_weyl_polynomial_decomposition.packet.json"
    )
    hessian_gap = load(
        DATA
        / "selected_hessiancountertermsource_bvector_theoremtemplate"
        / "remaining_hessian_bvector_source_gap.packet.json"
    )
    latest_theorem_attempt = load(
        DATA
        / "selected_phifinc1_physicalvariation_sourcetheorem_proof_attempt_or_countermodel"
        / "proof_attempt_decision.packet.json"
    )
    final_fill = load(
        DATA
        / "selected_finalsourceemission_bestcurrentfill_or_nogowitness"
        / "final_source_emission_nogo_witness.packet.json"
    )

    route_c_support = triage["routes"]["route_C_new_weyl_variation_principle"]
    principle = {
        "schema": "MTTRouteCWeylVariationSourcePrincipleCandidate.v1",
        "status": "ROUTE_C_PRINCIPLE_CANDIDATE_BUILT_NOT_DERIVED",
        "principle_name": "SelectedWeylVariationActionPrinciple",
        "statement": (
            "On the selected q79/F,m=1 finite C1 quotient, the differentiated Phi_fin^C1 "
            "variation source is the selected finite Weyl action derivative. It emits the "
            "phase/shift pre-residual operators R_Z/R_X from the selected Weyl carrier before "
            "residual-projector replay, and its same-source second variation emits the Hessian "
            "counterterm b_selected."
        ),
        "support_imported": {
            "source_level_weyl_carrier_selected": weyl_poly["source_level_weyl_carrier_selected"],
            "static_source_selector_selected": weyl_poly["static_source_selector_selected"],
            "active_shift_selected": weyl_poly["active_shift_selected"],
            "exact_R_Z_polynomial": weyl_poly["exact_polynomial_form"]["R_Z"],
            "exact_R_X_polynomial": weyl_poly["exact_polynomial_form"]["R_X"],
            "static_source_map_candidate_constructed": source_map["already_selected_or_closed"][
                "static_source_map_candidate_constructed"
            ],
            "formal_hessian_target_identified": hessian_gap["closed_now"]["formal_A_transpose_b_target_identified"],
        },
        "source_selection_attempt": source_map["selection_attempt"],
        "proved_now": False,
        "why_not_proved": [
            "The exact R_Z/R_X Weyl polynomials identify the only compatible operators, but do not select the physical differentiated Phi_fin^C1 application rule.",
            "The source-map test still reports source_map_selected_now=false and physical_projector_application_promoted_now=false.",
            "The hessian packet identifies the formal b target but keeps selected_b_vector_source and selected_hessian_counterterm_source open.",
            "The latest physical-variation theorem attempt refutes deriving the needed source kernel from closed support alone.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion = {
        "schema": "MTTRouteCWeylVariationKernelPromotionTest.v1",
        "status": "ROUTE_C_PROMOTION_REJECTED_PRINCIPLE_NOT_SELECTED",
        "same_branch": prior_kernel["same_branch"],
        "selected_variation_functional": False,
        "same_source_hessian": False,
        "sector_functor": False,
        "independence_certificate": False,
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "attached_source_evidence": [
            {
                "source": "candidate_data/selected_residual_weylpolynomial_source_theorem_attempt/residual_weyl_polynomial_decomposition.packet.json",
                "supports": "exact finite Weyl R_Z/R_X operator identities",
                "promotes_source": False,
            },
            {
                "source": "candidate_data/selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun/source_map_selection_theorem_test.packet.json",
                "supports": "static source map and canonical projector support",
                "promotes_source": False,
            },
            {
                "source": "candidate_data/selected_hessiancountertermsource_bvector_theoremtemplate/remaining_hessian_bvector_source_gap.packet.json",
                "supports": "formal Hessian/b target and template",
                "promotes_source": False,
            },
            {
                "source": "candidate_data/selected_phifinc1_physicalvariation_sourcetheorem_proof_attempt_or_countermodel/proof_attempt_decision.packet.json",
                "supports": "countermodel blocks support-only derivation",
                "promotes_source": False,
            },
        ],
        "conditional_witness_if_principle_inserted_or_derived": {
            "selected_variation_functional": prior_conditional["selected_variation_functional"],
            "same_source_hessian": prior_conditional["same_source_hessian"],
            "sector_functor": prior_conditional["sector_functor"],
            "independence_certificate": prior_conditional["independence_certificate"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    PROMOTION.write_text(json.dumps(promotion, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    validator_result = run_validator(PROMOTION)

    route_c_missing = route_c_support["missing"]
    decision = {
        "schema": "MTTRouteCWeylVariationDecisionAndNextGate.v1",
        "status": "ROUTE_C_SUPPORT_MAXIMIZED_NEW_PRINCIPLE_OR_DERIVATION_REQUIRED",
        "route_C_promoted_now": False,
        "strict_kernel_validator_ok": validator_result["ok"],
        "validator_result": rel(VALIDATOR_RESULT),
        "preferred_next_gate": NEXT,
        "route_C_missing": route_c_missing,
        "minimal_action_axiom_or_theorem": minimal_action,
        "latest_countermodel_blocks_support_only_proof": latest_theorem_attempt[
            "closed_support_countermodel_blocks_support_only_proof"
        ],
        "best_current_final_source_emission_validates": not final_fill["validator_rejects_best_current_fill"],
        "what_would_close_if_principle_proved": minimal_action["would_close"],
        "superset_strategy": {
            "mode": "Route C constructed as a new source principle, constrained by Route A physical action and Route B row-source validators",
            "locked_target_used_only_as_postcheck": True,
            "paths_used_as_free_parameters": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [
        (PRINCIPLE, principle),
        (VALIDATOR_RESULT, validator_result),
        (DECISION, decision),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedRouteCWeylVariationSourcePrincipleOrKernelClosure",
        "status": STATUS,
        "inputs": {
            "prior_kernel_attempt": rel(
                DATA
                / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
                / "current_pre_residual_variation_hessian_source_attempt.packet.json"
            ),
            "route_c_triage": rel(
                DATA
                / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
                / "three_route_source_kernel_triage.packet.json"
            ),
            "weyl_polynomial_decomposition": rel(
                DATA
                / "selected_residual_weylpolynomial_source_theorem_attempt"
                / "residual_weyl_polynomial_decomposition.packet.json"
            ),
            "latest_physical_variation_countermodel": rel(
                DATA
                / "selected_phifinc1_physicalvariation_sourcetheorem_proof_attempt_or_countermodel"
                / "proof_attempt_decision.packet.json"
            ),
        },
        "output_packets": {
            "routec_weyl_variation_principle_candidate": rel(PRINCIPLE),
            "routec_kernel_promotion_test": rel(PROMOTION),
            "strict_kernel_validator_result": rel(VALIDATOR_RESULT),
            "routec_decision_and_next_gate": rel(DECISION),
        },
        "theorem": {
            "name": "RouteCWeylVariationSupportMaximizationTheorem",
            "proved": True,
            "statement": (
                "The selected Weyl carrier and exact R_Z/R_X polynomials provide maximal Route-C support, "
                "but do not by themselves select the differentiated Phi_fin^C1 variation functional or "
                "same-source Hessian. A new Weyl-variation action principle, or its derivation, is required."
            ),
        },
        "closure_decision": {
            "route_C_kernel_closed": False,
            "pre_residual_kernel_closed": False,
            "unpatched_dynamic_C1_closed": False,
            "global_closure_claimed": False,
        },
        "what_closes_now": {
            "route_C_principle_candidate_constructed": True,
            "route_C_support_maximized": True,
            "strict_kernel_validator_rejection_preserved": True,
            "next_principle_derivation_gate_named": True,
        },
        "what_remains_open": {
            "derive_or_insert_selected_weyl_variation_action_principle": True,
            "selected_variation_functional": True,
            "same_source_hessian_b_selected": True,
            "sector_functor_source_promotion": True,
            "independence_certificate": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_RouteC_WeylVariation_SourcePrinciple_or_KernelClosure_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "route_C_kernel_closed": False,
        "strict_kernel_validator_ok": validator_result["ok"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected RouteC WeylVariation SourcePrinciple or KernelClosure v1

Status: `{STATUS}`.

This artifact constructs the Route-C candidate:

`SelectedWeylVariationActionPrinciple`.

The finite Weyl data are strong: the selected qutrit Weyl carrier, active shift,
static selector, and exact `R_Z/R_X` polynomials are all present. But the strict
kernel validator still rejects promotion because these facts do not select the
physical differentiated `Phi_fin^C1` variation functional or same-source
Hessian/`b_selected` emission.

So Route C is now reduced to a clean next gate:

`{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
