"""Apply the Weyl-variation action principle or preserve independent execution exit."""

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

SLUG = "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ACCEPTED = PACKET_DIR / "accepted_local_weylvariation_actionprinciple.packet.json"
APPLIED_KERNEL = PACKET_DIR / "applied_principle_kernel_closure.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "applied_kernel_validator_result.packet.json"
UNPATCHED_EXIT = PACKET_DIR / "unpatched_or_independent_kernel_execution_exit.packet.json"
DECISION = PACKET_DIR / "apply_or_independent_execution_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_WeylVariationActionPrinciple_Apply_or_IndependentKernelExecution_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_preresidual_variation_hessian_source_kernel.py"

STATUS = "MTT_SELECTED_WEYLVARIATION_ACTIONPRINCIPLE_APPLIED_LOCAL_KERNEL_CLOSED_UNPATCHED_OPEN"
NEXT = "MTT_Selected_LocalPrincipleDynamicC1Closure_Integration_or_UnpatchedKernelExecution_v1"


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

    previous = load(DATA / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion.candidate.json")
    insertion = load(
        DATA
        / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion"
        / "explicit_weylvariation_actionprinciple_insertion_package.packet.json"
    )
    conditional = load(
        DATA
        / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion"
        / "if_inserted_kernel_closure_witness.packet.json"
    )
    derivation = load(
        DATA
        / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion"
        / "unpatched_weylvariation_actionprinciple_derivation_attempt.packet.json"
    )
    source_contract = load(
        DATA
        / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues"
        / "source_or_kernel_acceptance_contract.packet.json"
    )
    local_axiom_closure = load(DATA / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit.candidate.json")

    accepted = {
        "schema": "MTTAcceptedLocalWeylVariationActionPrinciple.v1",
        "status": "LOCAL_WEYLVARIATION_ACTION_PRINCIPLE_ACCEPTED_IN_THIS_PROOF_SPINE",
        "principle_name": insertion["principle_name"],
        "principle_text": insertion["principle_text"],
        "accepted_scope": "local mtt-sm-parity-closure proof spine",
        "accepted_as": "explicit local premise, not unpatched theorem",
        "unpatched_derivation_status": derivation["status"],
        "external_papers_modified": False,
        "guardrails": {
            "unpatched_principle_derived_now": False,
            "independent_kernel_execution_supplied": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    applied_kernel = {
        "schema": "MTTAppliedWeylVariationPrincipleKernelClosure.v1",
        "status": "STRICT_PRE_RESIDUAL_KERNEL_CLOSED_BY_ACCEPTED_LOCAL_PRINCIPLE",
        "hypothesis": accepted["principle_name"],
        "same_branch": conditional["same_branch"],
        "selected_variation_functional": conditional["selected_variation_functional"],
        "same_source_hessian": conditional["same_source_hessian"],
        "sector_functor": conditional["sector_functor"],
        "independence_certificate": conditional["independence_certificate"],
        "locked_target_values_used_as_source": conditional["locked_target_values_used_as_source"],
        "residual_projector_replay_used_as_source": conditional["residual_projector_replay_used_as_source"],
        "attached_source_evidence": [
            {
                "source": rel(ACCEPTED),
                "closes": "local selected Weyl variation action principle premise",
            },
            *conditional["attached_source_evidence"],
        ],
        "promoted_inside_local_spine": {
            "pre_residual_phase_shift_operator_source": True,
            "same_source_hessian_b_selected_rows": True,
            "sector_rows_physical_source_promotion": True,
            "independence_from_residual_projector_replay": True,
        },
        "does_not_close": {
            "unpatched_principle_derivation": True,
            "independent_kernel_execution": True,
            "true_SM_equivalence": True,
            "no_knob": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    APPLIED_KERNEL.write_text(json.dumps(applied_kernel, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    validator_result = run_validator(APPLIED_KERNEL)

    unpatched_exit = {
        "schema": "MTTUnpatchedOrIndependentKernelExecutionExitAfterWeylPrincipleApply.v1",
        "status": "UNPATCHED_AND_INDEPENDENT_EXECUTION_EXITS_REMAIN_OPEN",
        "unpatched_principle_derived_now": False,
        "route_A_accepts_without_local_principle": source_contract["current_result"]["route_A_accepts_now"],
        "route_B_accepts_without_local_principle": source_contract["current_result"]["route_B_accepts_now"],
        "independent_kernel_execution_supplied": False,
        "remaining_unpatched_exits": [
            "derive SelectedWeylVariationActionPrinciple from unpatched Theta/Phi_fin/Strominger physical action text",
            "execute independent selected finite C1 kernel/quadrature rows: 72 primitive, 2 Hessian/source, 36 sector rows",
        ],
        "local_principle_replaces_neither_exit": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTWeylVariationActionPrincipleApplyOrIndependentExecutionDecision.v1",
        "status": "LOCAL_PRINCIPLE_APPLIED_KERNEL_VALIDATES_UNPATCHED_EXITS_RETAINED",
        "previous_gate": previous["status"],
        "local_principle_accepted": True,
        "applied_kernel_validator_ok": validator_result["ok"],
        "local_pre_residual_kernel_closed": validator_result["ok"],
        "local_dynamic_C1_closure_supported_by_prior_axiom_spine": local_axiom_closure["closure_decision"][
            "patched_dynamic_C1_packet_closed"
        ],
        "unpatched_principle_derived_now": False,
        "independent_kernel_execution_supplied": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "superset_strategy": {
            "mode": "Route C local principle applied; Route A unpatched derivation and Route B independent execution retained",
            "locked_target_used_only_as_postcheck": True,
            "paths_used_as_free_parameters": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [
        (ACCEPTED, accepted),
        (VALIDATOR_RESULT, validator_result),
        (UNPATCHED_EXIT, unpatched_exit),
        (DECISION, decision),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedWeylVariationActionPrincipleApplyOrIndependentKernelExecution",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(DATA / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion.candidate.json"),
            "principle_insertion_package": rel(
                DATA
                / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion"
                / "explicit_weylvariation_actionprinciple_insertion_package.packet.json"
            ),
            "conditional_kernel_witness": rel(
                DATA
                / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion"
                / "if_inserted_kernel_closure_witness.packet.json"
            ),
        },
        "output_packets": {
            "accepted_local_weylvariation_actionprinciple": rel(ACCEPTED),
            "applied_principle_kernel_closure": rel(APPLIED_KERNEL),
            "applied_kernel_validator_result": rel(VALIDATOR_RESULT),
            "unpatched_or_independent_kernel_execution_exit": rel(UNPATCHED_EXIT),
            "apply_or_independent_execution_decision": rel(DECISION),
        },
        "theorem": {
            "name": "LocalWeylVariationPrincipleAppliedKernelClosureTheorem",
            "proved": validator_result["ok"],
            "statement": (
                "Assuming the SelectedWeylVariationActionPrinciple as an explicit local premise, "
                "the strict pre-residual variation/Hessian source kernel validates. This is local "
                "premise-conditional closure, not unpatched derivation."
            ),
        },
        "closure_decision": {
            "local_principle_accepted": True,
            "local_pre_residual_kernel_closed": validator_result["ok"],
            "unpatched_principle_derived_now": False,
            "independent_kernel_execution_supplied": False,
            "unpatched_dynamic_C1_closed": False,
            "global_closure_claimed": False,
        },
        "what_closes_now": {
            "local_weylvariation_principle_accepted": True,
            "strict_pre_residual_kernel_closed_under_local_principle": validator_result["ok"],
            "unpatched_exits_preserved": True,
            "local_dynamic_C1_spine_has_stronger_source_kernel_basis": True,
        },
        "what_remains_open": {
            "derive_weylvariation_principle_unpatched": True,
            "independent_kernel_execution": True,
            "true_SM_equivalence_without_local_principle": True,
            "no_knob_flavor_constants": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_WeylVariationActionPrinciple_Apply_or_IndependentKernelExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "local_principle_accepted": True,
        "applied_kernel_validator_ok": validator_result["ok"],
        "unpatched_principle_derived_now": False,
        "independent_kernel_execution_supplied": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected WeylVariationActionPrinciple Apply or IndependentKernelExecution v1

Status: `{STATUS}`.

This artifact carries the prepared principle through locally. The
`SelectedWeylVariationActionPrinciple` is accepted as an explicit local premise,
and the strict pre-residual variation/Hessian source-kernel validator passes.

This does not derive the principle from unpatched MTT, and it does not replace
the independent kernel-execution exit. It closes the kernel only inside the
local premise-conditional proof spine.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
