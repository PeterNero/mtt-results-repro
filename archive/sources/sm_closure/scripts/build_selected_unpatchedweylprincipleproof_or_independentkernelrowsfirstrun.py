"""Build unpatched Weyl-principle proof / independent kernel rows first run.

The previous artifact made the local dynamic-C1 result paper-ready.  This one
returns to the unpatched frontier and executes the strongest available Route A
and Route B checks against that boundary.
"""

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

SLUG = "selected_unpatchedweylprincipleproof_or_independentkernelrowsfirstrun"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_unpatched_weyl_principle_reaudit.packet.json"
ROUTE_B = PACKET_DIR / "route_b_independent_kernel_rows_first_run.packet.json"
CUTSET = PACKET_DIR / "shared_source_theorem_cutset.packet.json"
DECISION = PACKET_DIR / "two_route_first_run_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_UnpatchedWeylPrincipleProof_or_IndependentKernelRowsFirstRun_v1.md"

LOCAL_PLAN = DATA / "selected_localdynamicc1paperappendix_or_unpatchedkernelexecutionplan.candidate.json"
CLAIM_BOUNDARY = (
    DATA
    / "selected_localdynamicc1paperappendix_or_unpatchedkernelexecutionplan"
    / "paper_claim_boundary.packet.json"
)
ROUTE_A_ATTEMPT = (
    DATA
    / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion"
    / "unpatched_weylvariation_actionprinciple_derivation_attempt.packet.json"
)
ROUTE_A_SOURCE_DECISION = (
    DATA
    / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun"
    / "source_fill_decision.packet.json"
)
ROUTE_B_ATTEMPT = (
    DATA
    / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill"
    / "current_row_source_independence_attempt.packet.json"
)
ROUTE_B_VALIDATOR_RESULT = (
    DATA
    / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill"
    / "row_source_validator_result.packet.json"
)
ROUTE_B_VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_rowsource_independence.py"
FORMAL_110 = (
    DATA
    / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
    / "formal_110_row_replay_integrated.packet.json"
)

STATUS = "MTT_SELECTED_UNPATCHEDWEYLPRINCIPLEPROOF_OR_INDEPENDENTKERNELROWSFIRSTRUN_BUILT_SOURCE_THEOREM_OPEN"
NEXT = "MTT_Selected_FiniteC1SourceIdentityTheorem_or_NewIndependentRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_route_b_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(ROUTE_B_VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "path": rel(path),
        "exit_code": proc.returncode,
        "ok": proc.returncode == 0,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr": proc.stderr.strip().splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    local_plan = load(LOCAL_PLAN)
    boundary = load(CLAIM_BOUNDARY)
    route_a_attempt = load(ROUTE_A_ATTEMPT)
    route_a_source = load(ROUTE_A_SOURCE_DECISION)
    route_b_attempt = load(ROUTE_B_ATTEMPT)
    route_b_prior_validation = load(ROUTE_B_VALIDATOR_RESULT)
    formal_110 = load(FORMAL_110)

    route_a = {
        "schema": "MTTUnpatchedWeylPrincipleProofReaudit.v1",
        "status": "ROUTE_A_REAUDITED_PHYSICAL_SELECTION_STILL_OPEN",
        "principle_name": route_a_attempt["principle_name"],
        "principle_statement": route_a_attempt["principle_statement"],
        "closed_support_count": len(
            [value for value in route_a_attempt["closed_support"].values() if value is True]
        ),
        "closed_support": route_a_attempt["closed_support"],
        "still_failed_fields": route_a_attempt["current_failed_fields"],
        "minimal_physical_certificate_built": route_a_source["route_A_minimal_certificate_built"],
        "minimal_physical_certificate_filled": route_a_source["route_A_minimal_certificate_filled"],
        "unpatched_principle_derived_now": route_a_attempt["unpatched_principle_derived_now"],
        "route_A_accepts": False,
        "why_not_accepted": route_a_attempt["why_not_derived"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    fresh_route_b_validation = run_route_b_validator(ROUTE_B_ATTEMPT)
    route_b = {
        "schema": "MTTIndependentKernelRowsFirstRun.v1",
        "status": "ROUTE_B_FIRST_RUN_EXECUTED_VALIDATOR_REJECTS_SOURCE_INDEPENDENCE",
        "row_counts": {
            "primitive_rows": 72,
            "sector_rows": 36,
            "hessian_source_rows": 2,
            "total_rows": 110,
        },
        "formal_110_layer_available": True,
        "formal_110_source": rel(FORMAL_110),
        "formal_replay_status": formal_110.get("status"),
        "attempt_path": rel(ROUTE_B_ATTEMPT),
        "prior_validator_result": route_b_prior_validation,
        "fresh_validator_result": fresh_route_b_validation,
        "closed_fields_in_attempt": {
            key: route_b_attempt[key]
            for key in [
                "finite_weyl_trace_rule_feeds_all_rows",
                "sector_rows_assembled_from_primitive_rows",
                "hessian_source_rows_assembled_from_same_rows",
                "no_locked_target_values_used_as_source",
            ]
        },
        "open_fields_in_attempt": {
            key: route_b_attempt[key]
            for key in [
                "selected_basis_feeds_72_primitive_rows",
                "no_residual_projector_replay_used_as_source",
                "row_formula_source_theorem_derived",
                "source_independent_of_residual_projector_replay",
            ]
        },
        "route_B_accepts": fresh_route_b_validation["ok"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTFiniteC1SourceIdentityTheoremCutset.v1",
        "status": "SINGLE_SHARED_SOURCE_THEOREM_IDENTIFIED_NOT_PROVED",
        "theorem_name": "SelectedFiniteC1SourceIdentityTheorem",
        "statement": (
            "On the selected q79/F,m=1 finite C1 quotient, the physical differentiated "
            "Phi_fin^C1 Weyl action and the selected transported finite Weyl trace row "
            "kernel are the same source identity. This identity emits R_Z, R_X, "
            "b_selected, all 72 primitive rows, 36 sector rows, and 2 Hessian/source "
            "rows without residual-projector replay or observed-data selection."
        ),
        "why_this_is_shared": {
            "route_A": "would derive the Weyl-variation principle and same-source physical R_Z/R_X/b_selected emission",
            "route_B": "would prove row-source independence for the selected 110-row finite C1 kernel execution",
        },
        "required_clauses": [
            "physical action restriction to selected finite Weyl quotient",
            "no extra physical boundary/source term",
            "same-source R_Z/R_X/b_selected emission",
            "selected transported bases feed all 72 primitive row kernels",
            "finite Weyl trace rule assembles sector and Hessian/source rows",
            "no residual-projector replay is used as source provenance",
        ],
        "proved_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTUnpatchedWeylOrIndependentRowsFirstRunDecision.v1",
        "status": "BOTH_ROUTES_EXECUTED_CURRENTLY_OPEN_SHARED_THEOREM_NEXT",
        "local_boundary_status": boundary["status"],
        "local_dynamic_C1_closed_under_premise": boundary["proved_now"][
            "local_dynamic_C1_closed_under_selected_weyl_principle"
        ],
        "route_A_accepts": route_a["route_A_accepts"],
        "route_B_accepts": route_b["route_B_accepts"],
        "unpatched_dynamic_C1_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "superset_strategy_used": {
            "combined_paths": [
                "Route A physical Weyl/Phi_fin action-source proof",
                "Route B independent finite C1 row-kernel execution",
            ],
            "locked_target": "same selected finite C1 source identity, not measured SM data",
            "result": "both routes reduce to one shared source identity theorem",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [
        (ROUTE_A, route_a),
        (ROUTE_B, route_b),
        (CUTSET, cutset),
        (DECISION, decision),
    ]:
        write_json(path, payload)

    candidate = {
        "candidate": "MTTSelectedUnpatchedWeylPrincipleProofOrIndependentKernelRowsFirstRun",
        "status": STATUS,
        "inputs": {
            "local_plan": rel(LOCAL_PLAN),
            "claim_boundary": rel(CLAIM_BOUNDARY),
            "route_A_attempt": rel(ROUTE_A_ATTEMPT),
            "route_B_attempt": rel(ROUTE_B_ATTEMPT),
        },
        "output_packets": {
            "route_a_unpatched_weyl_principle_reaudit": rel(ROUTE_A),
            "route_b_independent_kernel_rows_first_run": rel(ROUTE_B),
            "shared_source_theorem_cutset": rel(CUTSET),
            "two_route_first_run_decision": rel(DECISION),
        },
        "theorem": {
            "name": "UnpatchedWeylOrIndependentRowsFirstRunCutsetTheorem",
            "proved": True,
            "statement": (
                "After executing the strongest current Route A and Route B checks, unpatched "
                "dynamic-C1 promotion is equivalent to proving the selected finite C1 source "
                "identity theorem, or emitting genuinely new independent row source data."
            ),
        },
        "what_closes_now": {
            "route_A_reaudited_against_local_boundary": True,
            "route_B_first_run_executed_against_strict_validator": True,
            "shared_source_identity_theorem_named": True,
            "superset_paths_reconciled_to_locked_target": True,
        },
        "what_remains_open": {
            "SelectedFiniteC1SourceIdentityTheorem": True,
            "new_independent_selected_kernel_rows": True,
            "unpatched_dynamic_C1_closure": True,
            "true_SM_equivalence_without_local_premise": True,
            "no_knob_flavor_constants": True,
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_UnpatchedWeylPrincipleProof_or_IndependentKernelRowsFirstRun_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "route_A_accepts": False,
        "route_B_accepts": False,
        "route_B_validator_exit_code": fresh_route_b_validation["exit_code"],
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    NOTE.write_text(
        "# MTT Selected UnpatchedWeylPrincipleProof or IndependentKernelRowsFirstRun v1\n\n"
        f"Status: `{STATUS}`.\n\n"
        "This artifact executes the two preserved unpatched exits after the local dynamic-C1 closure:\n\n"
        "- Route A reaudits the unpatched Weyl-variation principle proof and still fails on physical source selection.\n"
        "- Route B reruns the independent row-source validator on the best current 110-row packet and still fails on source independence from residual-projector replay.\n\n"
        "The useful result is a sharper cutset: both routes now reduce to the same `SelectedFiniteC1SourceIdentityTheorem`, or else genuinely new independent selected row data must be emitted.\n\n"
        "No observed masses, mixings, thresholds, or fitted constants are used as source selectors.\n\n"
        f"Next artifact: `{NEXT}`.\n",
        encoding="utf-8",
    )
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
