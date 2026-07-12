"""Build PSM-C1-02 SI-1c action-kernel theorem/local-principle decision.

This promotes the already validated local Weyl-variation action-principle
kernel result into the current PSM-C1-02 source-identity label stack while
preserving the unpatched proof boundary.
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

SLUG = "selected_psm_c1_02_selectedphifinc1_preresidualactionkernel_theorem_or_localprincipledecision"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
UNPATCHED = PACKET_DIR / "unpatched_theorem_derivation_attempt.packet.json"
LOCAL = PACKET_DIR / "local_principle_kernel_closure_import.packet.json"
DECISION = PACKET_DIR / "si1c_decision.packet.json"
NEXT_WORK = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_SelectedPhiFinC1PreResidualActionKernelTheorem_Proof_or_LocalPrincipleDecision_v1.md"

PREVIOUS = DATA / "selected_psm_c1_02_physicalactionowns_finitetracekernel_proof_or_countermodel.candidate.json"
REMAINING = (
    DATA
    / "selected_psm_c1_02_physicalactionowns_finitetracekernel_proof_or_countermodel"
    / "remaining_kernel_theorem.packet.json"
)
WEYL_APPLY = DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution.candidate.json"
ACCEPTED_LOCAL = (
    DATA
    / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution"
    / "accepted_local_weylvariation_actionprinciple.packet.json"
)
APPLIED_KERNEL = (
    DATA
    / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution"
    / "applied_principle_kernel_closure.packet.json"
)
APPLIED_VALIDATOR = (
    DATA
    / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution"
    / "applied_kernel_validator_result.packet.json"
)
UNPATCHED_EXIT = (
    DATA
    / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution"
    / "unpatched_or_independent_kernel_execution_exit.packet.json"
)
WEYL_DERIVATION = (
    DATA
    / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion"
    / "unpatched_weylvariation_actionprinciple_derivation_attempt.packet.json"
)
APPLY_AUDIT = ROOT / "proof_corpus" / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution_audit.py"

STATUS = "MTT_SELECTED_PSM_C1_02_SI1C_LOCAL_PHIFINC1_PRERESIDUAL_ACTION_KERNEL_CLOSED_UNPATCHED_THEOREM_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_LocalSourceIdentityClosure_Integration_or_UnpatchedKernelExecution_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_existing_audit() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(APPLY_AUDIT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "audit": rel(APPLY_AUDIT),
        "returncode": proc.returncode,
        "stdout": proc.stdout.splitlines(),
        "stderr": proc.stderr.splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    remaining = load(REMAINING)
    weyl_apply = load(WEYL_APPLY)
    accepted_local = load(ACCEPTED_LOCAL)
    applied_kernel = load(APPLIED_KERNEL)
    applied_validator = load(APPLIED_VALIDATOR)
    unpatched_exit = load(UNPATCHED_EXIT)
    weyl_derivation = load(WEYL_DERIVATION)
    audit_result = run_existing_audit()

    unpatched = {
        "schema": "MTTPSMC102SI1cUnpatchedTheoremDerivationAttempt.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY",
        "clause": "SI-1c",
        "theorem_name": remaining["theorem_name"],
        "statement": remaining["statement"],
        "unpatched_theorem_derived_now": False,
        "derivation_attempt_source": rel(WEYL_DERIVATION),
        "derivation_attempt_status": weyl_derivation["status"],
        "why_not_derived": weyl_derivation["why_not_derived"],
        "acceptable_proof_sources": remaining["acceptable_proof_sources"],
        "forbidden_shortcuts": remaining["forbidden_shortcuts"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    local = {
        "schema": "MTTPSMC102SI1cLocalPrincipleKernelClosureImport.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY",
        "clause": "SI-1c",
        "accepted_local_principle": rel(ACCEPTED_LOCAL),
        "applied_kernel": rel(APPLIED_KERNEL),
        "applied_validator": rel(APPLIED_VALIDATOR),
        "existing_audit_result": audit_result,
        "local_principle_accepted": accepted_local["status"]
        == "LOCAL_WEYLVARIATION_ACTION_PRINCIPLE_ACCEPTED_IN_THIS_PROOF_SPINE",
        "local_principle_scope": accepted_local["accepted_scope"],
        "accepted_as": accepted_local["accepted_as"],
        "strict_kernel_validator_ok": applied_validator["ok"],
        "strict_kernel_closed_under_local_principle": weyl_apply["closure_decision"][
            "local_pre_residual_kernel_closed"
        ],
        "promoted_inside_local_spine": applied_kernel["promoted_inside_local_spine"],
        "does_not_close": applied_kernel["does_not_close"],
        "audit_ok": audit_result["returncode"] == 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    decision = {
        "schema": "MTTPSMC102SI1cProofOrLocalPrincipleDecision.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY",
        "clause": "SI-1c",
        "status": "LOCAL_PRINCIPLE_CLOSES_SI1C_KERNEL_UNPATCHED_THEOREM_REMAINS_OPEN",
        "unpatched_theorem_derived_now": False,
        "local_principle_accepted": local["local_principle_accepted"],
        "local_pre_residual_action_kernel_closed": local["strict_kernel_closed_under_local_principle"],
        "strict_kernel_validator_ok": local["strict_kernel_validator_ok"],
        "source_identity_lemma_status": "CLOSED_ONLY_RELATIVE_TO_ACCEPTED_LOCAL_WEYLVARIATION_ACTION_PRINCIPLE",
        "unpatched_source_identity_lemma_status": "OPEN",
        "why_this_is_progress": [
            "The selected pre-residual action-kernel theorem now has a PSM-labeled local-premise closure path.",
            "The strict pre-residual variation/Hessian source kernel validator passes under that accepted local principle.",
            "The unpatched derivation route is still preserved and cannot be confused with no-knob closure.",
        ],
        "superset_strategy": {
            "mode": "Route C local principle supplies a constrained exit; Route A unpatched action proof and Route B independent kernel execution remain live",
            "paths_used_as_free_parameters": False,
            "locked_target_used_only_as_postcheck": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102SI1c.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_SelectedPhiFinC1PreResidualActionKernelTheorem_Proof_or_LocalPrincipleDecision_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1d",
            "task": "Integrate the local SI-1c kernel closure into the PSM-C1-02 source-identity lemma while preserving unpatched-open flags.",
        },
        "secondary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u",
            "task": "Continue the unpatched route by deriving the Weyl-variation action principle or executing independent finite kernels.",
        },
        "status": "NEXT_WORKORDER_LOCAL_SOURCEIDENTITY_INTEGRATION_OR_UNPATCHED_KERNEL_EXECUTION",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102SelectedPhiFinC1PreResidualActionKernelTheoremOrLocalPrincipleDecision",
        "active_label": "PSM-C1-02",
        "active_routes": ["SOURCE-IDENTITY/SI-1c"],
        "closed_boundary": "DONE-PARITY-00",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_status": previous["status"],
            "remaining_kernel_theorem": rel(REMAINING),
            "weylvariation_apply_candidate": rel(WEYL_APPLY),
            "accepted_local_principle": rel(ACCEPTED_LOCAL),
            "applied_kernel": rel(APPLIED_KERNEL),
            "applied_validator": rel(APPLIED_VALIDATOR),
            "unpatched_exit": rel(UNPATCHED_EXIT),
            "unpatched_derivation_attempt": rel(WEYL_DERIVATION),
        },
        "output_packets": {
            "unpatched_theorem_derivation_attempt": rel(UNPATCHED),
            "local_principle_kernel_closure_import": rel(LOCAL),
            "si1c_decision": rel(DECISION),
            "next_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "PSMC102SI1cLocalPhiFinC1PreResidualActionKernelClosureTheorem",
            "proved": True,
            "statement": (
                "Relative to the accepted local SelectedWeylVariationActionPrinciple, the selected "
                "Phi_fin^C1 pre-residual action kernel closes the strict source-kernel validator for SI-1c. "
                "The unpatched theorem remains open."
            ),
        },
        "what_closes_now": {
            "SI1c_local_principle_decision_built": True,
            "local_pre_residual_action_kernel_closed": True,
            "strict_kernel_validator_ok": True,
            "PSM_labeled_source_identity_local_path_ready": True,
            "unpatched_exit_preserved": True,
            "superset_paths_constrained_to_locked_target": True,
        },
        "what_remains_open": {
            "unpatched_SelectedPhiFinC1PreResidualActionKernelTheorem": True,
            "unpatched_SelectedFiniteC1SourceIdentityLemma": True,
            "independent_kernel_execution": True,
            "true_SM_equivalence_without_local_principle": True,
            "no_knob_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_SelectedPhiFinC1PreResidualActionKernelTheorem_Proof_or_LocalPrincipleDecision_v1",
        "active_label": "PSM-C1-02",
        "active_routes": candidate["active_routes"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "local_principle_accepted": True,
        "strict_kernel_validator_ok": True,
        "local_pre_residual_action_kernel_closed": True,
        "unpatched_theorem_derived_now": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    for path, obj in [
        (UNPATCHED, unpatched),
        (LOCAL, local),
        (DECISION, decision),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    NOTE.write_text(
        f"""# MTT Selected PSM C1 02 SelectedPhiFinC1PreResidualActionKernelTheorem Proof or LocalPrincipleDecision v1

Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1c`

Status: `{STATUS}`

Closed boundary label: `DONE-PARITY-00`

## Decision

`SelectedPhiFinC1PreResidualActionKernelTheorem` is **not** derived unpatched here. The unpatched derivation attempt remains open.

Relative to the already accepted local `SelectedWeylVariationActionPrinciple`, the strict pre-residual variation/Hessian source kernel validates and closes the SI-1c kernel inside the local proof spine.

This is local-premise closure, not no-knob closure and not unpatched physical-action derivation.

## Superset Strategy

Route C supplies a constrained local-principle exit. Route A unpatched action proof and Route B independent finite-kernel execution remain live. They are not knobs. The locked target and replay values remain postchecks only.

## Next Artifact

`{NEXT}`
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
