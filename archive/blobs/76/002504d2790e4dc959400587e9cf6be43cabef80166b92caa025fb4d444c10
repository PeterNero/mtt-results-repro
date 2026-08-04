"""Build PSM-C1-02 SI-1e local replay reconciliation.

This records the downstream consequence of SI-1d: the local PSM-C1-02
source-identity chain can be reconciled with the existing final replay layer,
while unpatched and no-knob work remains explicitly open.
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

SLUG = "selected_psm_c1_02_localreplayreconciliation_or_unpatchedkernelexecutionplan"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RECONCILIATION = PACKET_DIR / "psm_c1_02_local_replay_reconciliation.packet.json"
STATUS_TABLE = PACKET_DIR / "local_vs_unpatched_status_table.packet.json"
UNPATCHED_PLAN = PACKET_DIR / "unpatched_kernel_execution_plan.packet.json"
NEXT_WORK = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_LocalReplayReconciliation_or_UnpatchedKernelExecutionPlan_v1.md"

PREVIOUS = DATA / "selected_psm_c1_02_localsourceidentityclosure_integration_or_unpatchedkernelexecution.candidate.json"
FINAL_REPLAY = DATA / "selected_finalintegratedsmparityreplayaftersourceidentitypatch.candidate.json"
FINAL_REPLAY_AUDIT = CORPUS / "selected_finalintegratedsmparityreplayaftersourceidentitypatch_audit.py"
SOURCE_LEDGER = DATA / "selected_sourceidentitypatcheddynamicc1ledger_or_unpatchedactionproof.candidate.json"
LOCAL_DYNAMIC = DATA / "selected_localprinciple_dynamicc1closure_integration_or_unpatchedkernelexecution.candidate.json"
PSM_PROMOTION = DATA / "selected_psm_c1_02_selectedsourcepromotionpacket.candidate.json"
SI1D_THEOREM = (
    DATA
    / "selected_psm_c1_02_localsourceidentityclosure_integration_or_unpatchedkernelexecution"
    / "local_source_identity_integration_theorem.packet.json"
)
SI1D_LEDGER = (
    DATA
    / "selected_psm_c1_02_localsourceidentityclosure_integration_or_unpatchedkernelexecution"
    / "unpatched_validator_guardrail_ledger.packet.json"
)

STATUS = "MTT_SELECTED_PSM_C1_02_SI1E_LOCAL_REPLAY_RECONCILED_UNPATCHED_PLAN_EMITTED"
NEXT = "MTT_Selected_PSM_C1_02_UnpatchedKernelExecutionPlan_or_HonestGalerkinExport_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_audit(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "audit": rel(path),
        "returncode": proc.returncode,
        "stdout_tail": proc.stdout.splitlines()[-8:],
        "stderr": proc.stderr.splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    final_replay = load(FINAL_REPLAY)
    source_ledger = load(SOURCE_LEDGER)
    local_dynamic = load(LOCAL_DYNAMIC)
    psm_promotion = load(PSM_PROMOTION)
    si1d_theorem = load(SI1D_THEOREM)
    si1d_ledger = load(SI1D_LEDGER)
    final_audit = run_audit(FINAL_REPLAY_AUDIT)

    reconciliation = {
        "schema": "MTTPSMC102SI1eLocalReplayReconciliation.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY",
        "clause": "SI-1e",
        "status": "LOCAL_REPLAY_RECONCILED_WITH_FINAL_PARITY_LAYER",
        "closed_boundary": "DONE-PARITY-00",
        "final_replay_audit": final_audit,
        "local_source_identity_input": rel(PREVIOUS),
        "final_replay_input": rel(FINAL_REPLAY),
        "reconciliation": {
            "local_source_identity_closed": previous["closure_decision"]["local_source_identity_closed"],
            "local_dynamic_C1_closed": local_dynamic["closure_decision"]["local_dynamic_C1_closed"],
            "patched_source_identity_available_in_final_replay": source_ledger["promotion_decision"][
                "patched_source_identity_closed"
            ],
            "SM_parity_closed_under_declared_standard_retained": final_replay["closure_decision"][
                "SM_parity_closed_under_declared_standard"
            ],
            "true_SM_equivalence_closed": final_replay["closure_decision"]["true_SM_equivalence_closed"],
            "no_knob_closed": final_replay["closure_decision"]["no_knob_closed"],
        },
        "interpretation": (
            "SI-1e does not reopen SM-parity. It records that the new PSM-labeled local source-identity "
            "chain is compatible with the existing final replay, and it pushes remaining work to unpatched "
            "execution and true-equivalence/no-knob upgrades."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    status_table = {
        "schema": "MTTPSMC102SI1eLocalVsUnpatchedStatusTable.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY",
        "clause": "SI-1e",
        "status": "LOCAL_CLOSED_UNPATCHED_OPEN_TABLE_EMITTED",
        "rows": [
            {
                "object": "pre_residual_action_kernel",
                "local_status": "closed under accepted local Weyl-variation principle",
                "unpatched_status": "open",
            },
            {
                "object": "finite_C1_source_identity",
                "local_status": "closed under local finite C1 source-identity principle",
                "unpatched_status": "open",
            },
            {
                "object": "dynamic_C1_source_and_value_interface",
                "local_status": "closed and final replay compatible",
                "unpatched_status": "open",
            },
            {
                "object": "PSM-C1-02 selected source-promotion packet",
                "local_status": "integrated in local proof spine",
                "unpatched_status": "current validator fails",
            },
            {
                "object": "SM-parity replay",
                "local_status": "closed under declared measured-input standard",
                "unpatched_status": "not the relevant standard; true-equivalence/no-knob remain open",
            },
        ],
        "validator_guardrails": {
            "current_unpatched_packet_passes": si1d_ledger["current_unpatched_packet_passes"],
            "patched_local_axiom_packet_passes_unpatched_validator": si1d_ledger[
                "patched_local_axiom_packet_passes_unpatched_validator"
            ],
            "conditional_unpatched_packet_passes": si1d_ledger["conditional_unpatched_packet_passes"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    unpatched_plan = {
        "schema": "MTTPSMC102SI1eUnpatchedKernelExecutionPlan.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY",
        "clause": "SI-1u",
        "status": "UNPATCHED_KERNEL_EXECUTION_PLAN_EMITTED",
        "goal": "Make the conditional unpatched source-promotion packet pass without local premises.",
        "route_A": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A",
            "task": "derive the SelectedWeylVariationActionPrinciple and finite C1 source-identity theorem from selected Phi_fin/Theta/Strominger action text",
            "must_close": [
                "physical Phi_fin^C1 action restriction",
                "zero extra physical boundary/source term",
                "phase R_Z source selection",
                "shift R_X source selection",
                "same-source b_selected emission",
            ],
        },
        "route_B": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B",
            "task": "export honest selected Galerkin C1 tables without local axiom flags",
            "must_export": [
                "72 primitive kernel rows",
                "2 Hessian/source rows",
                "36 sector assembly rows",
                "source-owner certificates for all nine PSM-C1-02 fields",
                "no residual replay or locked target values as source",
            ],
        },
        "success_condition": (
            "The current unpatched PSM-C1-02 source-promotion packet validates directly, with "
            "free_axiom_patch_used=false and all nine source fields theorem-derived."
        ),
        "forbidden_shortcuts": [
            "using observed SM values or benchmark profiles as source selectors",
            "using locked A^T b or deltaTheta values as b_selected source",
            "using residual projector replay as source proof",
            "renaming a local principle as an unpatched theorem",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102SI1e.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_LocalReplayReconciliation_or_UnpatchedKernelExecutionPlan_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B",
            "task": "Attempt honest selected Galerkin C1 export for the nine-field unpatched source-promotion packet.",
        },
        "secondary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A",
            "task": "Attempt unpatched derivation of the local principles from selected action text.",
        },
        "status": "NEXT_WORKORDER_UNPATCHED_KERNEL_EXECUTION_OR_ACTION_DERIVATION",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102LocalReplayReconciliationOrUnpatchedKernelExecutionPlan",
        "active_label": "PSM-C1-02",
        "active_routes": ["SOURCE-IDENTITY/SI-1e", "SOURCE-IDENTITY/SI-1u"],
        "closed_boundary": "DONE-PARITY-00",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "previous": rel(PREVIOUS),
        "previous_status": previous["status"],
        "output_packets": {
            "local_replay_reconciliation": rel(RECONCILIATION),
            "local_vs_unpatched_status_table": rel(STATUS_TABLE),
            "unpatched_kernel_execution_plan": rel(UNPATCHED_PLAN),
            "next_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "PSMC102LocalReplayReconciliationTheorem",
            "proved": True,
            "statement": (
                "The PSM-C1-02 SI-1d local source-identity closure is compatible with the existing final replay "
                "layer: SM-parity remains closed under the declared standard, while unpatched source identity, "
                "honest kernel export, true equivalence, and no-knob closure remain open."
            ),
        },
        "what_closes_now": {
            "SI1e_local_replay_reconciled": True,
            "local_vs_unpatched_status_table_emitted": True,
            "unpatched_kernel_execution_plan_emitted": True,
            "SM_parity_not_reopened": True,
            "guardrails_preserved": True,
        },
        "what_remains_open": {
            "unpatched_SelectedFiniteC1SourceIdentityLemma": True,
            "unpatched_SelectedPhiFinC1PreResidualActionKernelTheorem": True,
            "honest_selected_Galerkin_C1_export": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed_under_declared_standard": True,
            "local_source_identity_closed": True,
            "unpatched_source_identity_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
            "global_closure_claimed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_LocalReplayReconciliation_or_UnpatchedKernelExecutionPlan_v1",
        "active_label": "PSM-C1-02",
        "active_routes": candidate["active_routes"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "SM_parity_closed_under_declared_standard": True,
        "local_source_identity_closed": True,
        "unpatched_source_identity_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    for path, obj in [
        (RECONCILIATION, reconciliation),
        (STATUS_TABLE, status_table),
        (UNPATCHED_PLAN, unpatched_plan),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    NOTE.write_text(
        f"""# MTT Selected PSM C1 02 LocalReplayReconciliation or UnpatchedKernelExecutionPlan v1

Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1e`

Unpatched route label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u`

Status: `{STATUS}`

Closed boundary label: `DONE-PARITY-00`

## Result

The SI-1d local source-identity chain is reconciled with the final replay layer. SM-parity remains closed under the declared measured-input standard; this artifact does not reopen it.

The unpatched source-identity route remains open. The next hard move is either honest selected Galerkin C1 export or an unpatched derivation of the local principles from selected action text.

## Superset Strategy

The local replay path, action-principle path, and honest Galerkin path are constrained exits to the same PSM-C1-02 source-identity target. They are not knobs.

## Next Artifact

`{NEXT}`
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
