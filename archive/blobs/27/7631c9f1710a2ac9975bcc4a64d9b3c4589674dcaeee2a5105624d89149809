"""Build local dynamic-C1 paper appendix and unpatched execution plan."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
DRAFT_DIR = CORPUS / "paper_appendix_drafts" / "dynamic_c1"

PREVIOUS_SLUG = "selected_localprinciple_dynamicc1closure_integration_or_unpatchedkernelexecution"
PREVIOUS = DATA / f"{PREVIOUS_SLUG}.candidate.json"
PREVIOUS_DIR = DATA / PREVIOUS_SLUG
LOCAL_CLOSURE = PREVIOUS_DIR / "local_principle_dynamicc1_closure_theorem.packet.json"
UNPATCHED_EXIT = PREVIOUS_DIR / "unpatched_kernel_execution_exit_status.packet.json"
LEDGER = PREVIOUS_DIR / "local_vs_unpatched_closure_ledger.packet.json"

SLUG = "selected_localdynamicc1paperappendix_or_unpatchedkernelexecutionplan"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
APPENDIX_PACKET = PACKET_DIR / "local_dynamic_c1_appendix_sections.packet.json"
UNPATCHED_PLAN = PACKET_DIR / "unpatched_kernel_execution_plan.packet.json"
CLAIM_BOUNDARY = PACKET_DIR / "paper_claim_boundary.packet.json"
APPENDIX_DRAFT = DRAFT_DIR / "theta_execution_dynamic_c1_local_principle_appendix.md"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LocalDynamicC1PaperAppendix_or_UnpatchedKernelExecutionPlan_v1.md"

STATUS = "MTT_SELECTED_LOCALDYNAMICC1_PAPERAPPENDIX_OR_UNPATCHEDKERNEL_EXECUTIONPLAN_BUILT_OPEN"
NEXT = "MTT_Selected_UnpatchedWeylPrincipleProof_or_IndependentKernelRowsFirstRun_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    DRAFT_DIR.mkdir(parents=True, exist_ok=True)

    local = load(LOCAL_CLOSURE)
    exact = local["exact_values"]

    appendix_sections = {
        "schema": "MTTLocalDynamicC1PaperAppendixSections.v1",
        "status": "APPENDIX_SECTIONS_BUILT_LOCAL_PREMISE_CLAIM_ONLY",
        "target_paper_family": "Theta-Closure & Execution Program / dynamic C1 closure",
        "sections": [
            {
                "id": "LD1_local_principle_statement",
                "title": "Local Weyl-Variation Premise",
                "safe_claim": (
                    "Assuming the selected local Weyl-variation action principle, the "
                    "pre-residual variation/Hessian source kernel is theorem-checked inside "
                    "the local proof spine."
                ),
                "must_not_claim": "The premise is derived from MTT without insertion.",
                "dependencies": [
                    "MTT_Selected_WeylVariationActionPrinciple_Apply_or_IndependentKernelExecution_v1",
                    "MTT_Selected_LocalPrincipleDynamicC1Closure_Integration_or_UnpatchedKernelExecution_v1",
                ],
            },
            {
                "id": "LD2_exact_dynamic_c1_values",
                "title": "Exact Dynamic-C1 Consequences",
                "safe_claim": (
                    "Within the local premise, the dynamic packet has A^T A=12 I_2, "
                    "A^T b=(12,12), ||b||^2=24, and deltaTheta_C1=(1,1)."
                ),
                "must_not_claim": "Observed SM masses, mixings, or CP data select these values.",
                "dependencies": [rel(LOCAL_CLOSURE)],
                "exact_values": exact,
            },
            {
                "id": "LD3_unpatched_boundary",
                "title": "Unpatched Boundary",
                "safe_claim": (
                    "The local result is a rigorous conditional theorem; unpatched closure "
                    "requires either deriving the Weyl principle or executing independent "
                    "selected kernel rows."
                ),
                "must_not_claim": "No-knob or true SM-equivalence closure is finished by this local theorem.",
                "dependencies": [rel(UNPATCHED_EXIT), rel(LEDGER)],
            },
        ],
        "guardrails": {
            "local_premise_explicit": True,
            "unpatched_derivation_open": True,
            "independent_execution_open": True,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        },
    }

    unpatched_plan = {
        "schema": "MTTUnpatchedKernelExecutionPlan.v1",
        "status": "EXECUTION_PLAN_BUILT_VALUES_NOT_EXECUTED",
        "goal": "Promote the local dynamic-C1 closure to unpatched closure without using the local premise as an axiom.",
        "route_A_unpatched_principle_proof": {
            "required_output": "SelectedWeylVariationActionPrinciple derived from prior MTT source data",
            "minimum_fields": [
                "selected action functional",
                "admissible C1 variation space",
                "physical boundary/no-extra-source cancellation",
                "same-source R_Z/R_X emission",
                "same-source Hessian and b_selected emission",
            ],
            "current_status": "OPEN",
            "acceptance_test": "strict pre-residual variation/Hessian source-kernel validator passes without explicit insertion",
        },
        "route_B_independent_kernel_rows": {
            "required_output": "independent selected finite C1 kernel row table",
            "minimum_row_families": {
                "primitive_rows": 72,
                "sector_rows": 36,
                "hessian_source_rows": 2,
                "total_rows": 110,
            },
            "current_status": "OPEN",
            "acceptance_test": "independent row provenance plus exact/error certificate reproduces or replaces the local A,b,deltaTheta packet",
        },
        "shared_forbidden_shortcuts": [
            "using measured flavor data as selectors",
            "copying the local-premise values as independent rows",
            "declaring source selection from residual minimization alone",
            "using benchmark matrices as selected operator data",
        ],
        "next_first_run": {
            "preferred_route": "A if a proof of the Weyl principle can be emitted; B if actual selected quadrature rows can be exported",
            "minimal_artifact": NEXT,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    claim_boundary = {
        "schema": "MTTDynamicC1ClaimBoundary.v1",
        "status": "LOCAL_CLOSED_UNPATCHED_OPEN_BOUNDARY_LOCKED",
        "proved_now": {
            "local_dynamic_C1_closed_under_selected_weyl_principle": True,
            "strict_kernel_validates_inside_local_spine": True,
            "exact_values_promoted_inside_local_spine": True,
        },
        "not_proved_now": {
            "unpatched_weyl_principle_derivation": True,
            "independent_kernel_execution": True,
            "true_SM_equivalence_without_local_premise": True,
            "no_knob_flavor_constants": True,
        },
        "superset_strategy_classification": {
            "mode": "single local route with preserved dual exit",
            "local_route": "accepted Weyl-variation principle -> strict source kernel -> dynamic C1 value promotion",
            "preserved_exit_A": "derive the principle from prior MTT data",
            "preserved_exit_B": "independent selected Galerkin/kernel row execution",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [
        (APPENDIX_PACKET, appendix_sections),
        (UNPATCHED_PLAN, unpatched_plan),
        (CLAIM_BOUNDARY, claim_boundary),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    APPENDIX_DRAFT.write_text(
        "# Dynamic-C1 Local Principle Appendix\n\n"
        "Status: `APPENDIX_DRAFT_LOCAL_PREMISE_CLAIM_ONLY`.\n\n"
        "The selected local Weyl-variation action principle is used as an explicit local premise. "
        "Under that premise, the strict pre-residual variation/Hessian source kernel validates and "
        "promotes the dynamic-C1 packet:\n\n"
        "- `A^T A = 12 I_2`;\n"
        "- `A^T b = (12,12)`;\n"
        "- `||b||^2 = 24`;\n"
        "- `deltaTheta_C1 = (1,1)`.\n\n"
        "This appendix may be inserted only with the following boundary sentence:\n\n"
        "> This is a local-premise theorem. It does not derive the Weyl-variation principle unpatched, "
        "does not supply independent selected kernel rows, and does not use measured SM flavor data "
        "as a source selector.\n\n"
        "Unpatched continuation has two legal exits: derive the Weyl principle from selected MTT "
        "source data, or execute an independent selected 110-row finite C1 kernel table.\n",
        encoding="utf-8",
    )

    candidate = {
        "candidate": "MTTSelectedLocalDynamicC1PaperAppendixOrUnpatchedKernelExecutionPlan",
        "status": STATUS,
        "previous": rel(PREVIOUS),
        "output_packets": {
            "appendix_sections": rel(APPENDIX_PACKET),
            "unpatched_kernel_execution_plan": rel(UNPATCHED_PLAN),
            "claim_boundary": rel(CLAIM_BOUNDARY),
            "appendix_draft": rel(APPENDIX_DRAFT),
        },
        "what_closes_now": {
            "paper_appendix_claim_boundary": True,
            "local_theorem_insertable_without_overclaim": True,
            "unpatched_route_A_and_B_execution_plan": True,
            "superset_strategy_classified": True,
        },
        "what_remains_open": {
            "unpatched_weyl_principle_proof": True,
            "independent_kernel_row_execution": True,
            "true_SM_equivalence_without_local_premise": True,
            "no_knob_flavor_constants": True,
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_LocalDynamicC1PaperAppendix_or_UnpatchedKernelExecutionPlan_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "appendix_draft": rel(APPENDIX_DRAFT),
        "unpatched_route_A_open": True,
        "unpatched_route_B_open": True,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    NOTE.write_text(
        "# MTT Selected LocalDynamicC1 PaperAppendix or UnpatchedKernelExecutionPlan v1\n\n"
        f"Status: `{STATUS}`.\n\n"
        "This artifact makes the local dynamic-C1 theorem paper-ready without weakening the proof boundary. "
        "The appendix draft states the local-premise theorem, records the exact values, and requires an "
        "explicit boundary sentence before corpus insertion.\n\n"
        "It also locks the two honest unpatched exits:\n\n"
        "- Route A: derive the selected Weyl-variation principle from prior MTT source data.\n"
        "- Route B: execute independent selected finite C1 kernel rows (`72+36+2=110`).\n\n"
        "No observed masses, mixings, thresholds, or fitted constants are used as source selectors.\n\n"
        f"Next artifact: `{NEXT}`.\n",
        encoding="utf-8",
    )
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
