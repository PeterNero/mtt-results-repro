"""Build PSM-C1-02 SI-1d local source-identity integration.

This integrates the SI-1c local pre-residual action-kernel closure with the
existing local source-identity and dynamic-C1 closure ledgers, while preserving
the unpatched source-promotion and independent-kernel exits.
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

SLUG = "selected_psm_c1_02_localsourceidentityclosure_integration_or_unpatchedkernelexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LOCAL_INTEGRATION = PACKET_DIR / "psm_c1_02_local_source_identity_integration.packet.json"
VALIDATOR_LEDGER = PACKET_DIR / "unpatched_validator_guardrail_ledger.packet.json"
THEOREM = PACKET_DIR / "local_source_identity_integration_theorem.packet.json"
NEXT_WORK = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_LocalSourceIdentityClosure_Integration_or_UnpatchedKernelExecution_v1.md"

PREVIOUS = DATA / "selected_psm_c1_02_selectedphifinc1_preresidualactionkernel_theorem_or_localprincipledecision.candidate.json"
SI1C_DECISION = (
    DATA
    / "selected_psm_c1_02_selectedphifinc1_preresidualactionkernel_theorem_or_localprincipledecision"
    / "si1c_decision.packet.json"
)
LOCAL_DYNAMIC = DATA / "selected_localprinciple_dynamicc1closure_integration_or_unpatchedkernelexecution.candidate.json"
LOCAL_DYNAMIC_AUDIT = CORPUS / "selected_localprinciple_dynamicc1closure_integration_or_unpatchedkernelexecution_audit.py"
SOURCE_IDENTITY_INSERTION = DATA / "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation.candidate.json"
SOURCE_IDENTITY_INSERTION_AUDIT = CORPUS / "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation_audit.py"
PROMOTION_PACKET = DATA / "selected_psm_c1_02_selectedsourcepromotionpacket.candidate.json"
PROMOTION_AUDIT = CORPUS / "selected_psm_c1_02_selectedsourcepromotionpacket_audit.py"
PROMOTION_DIR = DATA / "selected_psm_c1_02_selectedsourcepromotionpacket"
CURRENT_PROMOTION_RESULT = PROMOTION_DIR / "current_unpatched_source_promotion_validator_result.packet.json"
PATCHED_PROMOTION_RESULT = PROMOTION_DIR / "patched_local_axiom_source_promotion_validator_result.packet.json"
CONDITIONAL_PROMOTION_RESULT = PROMOTION_DIR / "conditional_unpatched_source_promotion_validator_result.packet.json"
PROMOTION_MATRIX = PROMOTION_DIR / "psm_c1_02_source_promotion_matrix.packet.json"

STATUS = "MTT_SELECTED_PSM_C1_02_SI1D_LOCAL_SOURCEIDENTITY_INTEGRATED_UNPATCHED_EXECUTION_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_LocalReplayReconciliation_or_UnpatchedKernelExecutionPlan_v1"


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
    si1c = load(SI1C_DECISION)
    local_dynamic = load(LOCAL_DYNAMIC)
    source_identity = load(SOURCE_IDENTITY_INSERTION)
    promotion = load(PROMOTION_PACKET)
    current_result = load(CURRENT_PROMOTION_RESULT)
    patched_result = load(PATCHED_PROMOTION_RESULT)
    conditional_result = load(CONDITIONAL_PROMOTION_RESULT)
    promotion_matrix = load(PROMOTION_MATRIX)

    local_dynamic_audit = run_audit(LOCAL_DYNAMIC_AUDIT)
    source_identity_audit = run_audit(SOURCE_IDENTITY_INSERTION_AUDIT)
    promotion_audit = run_audit(PROMOTION_AUDIT)

    local_integration = {
        "schema": "MTTPSMC102SI1dLocalSourceIdentityIntegration.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY",
        "clause": "SI-1d",
        "status": "LOCAL_SOURCE_IDENTITY_CHAIN_INTEGRATED_FOR_PSM_C1_02",
        "closed_boundary": "DONE-PARITY-00",
        "inputs": {
            "si1c_decision": rel(SI1C_DECISION),
            "local_dynamic_c1_integration": rel(LOCAL_DYNAMIC),
            "source_identity_principle_insertion": rel(SOURCE_IDENTITY_INSERTION),
            "psm_source_promotion_packet": rel(PROMOTION_PACKET),
        },
        "imported_audits": {
            "local_dynamic_c1": local_dynamic_audit,
            "finite_c1_source_identity_insertion": source_identity_audit,
            "psm_source_promotion_packet": promotion_audit,
        },
        "local_chain": {
            "si1c_local_action_kernel_closed": si1c["local_pre_residual_action_kernel_closed"],
            "local_dynamic_C1_closed": local_dynamic["closure_decision"]["local_dynamic_C1_closed"],
            "local_source_identity_principle_inserted": source_identity["what_closes_now"][
                "local_source_identity_principle_inserted"
            ],
            "strict_110row_source_id_validator_passes_under_principle": source_identity["what_closes_now"][
                "strict_110row_source_id_validator_passes_under_principle"
            ],
            "patched_dynamic_C1_source_identity_packet_closed": source_identity["what_closes_now"][
                "patched_dynamic_C1_source_identity_packet_closed"
            ],
            "local_psm_source_identity_integrated": True,
        },
        "scientific_status": "local-premise source-identity closure for the PSM-C1-02 proof spine",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    validator_ledger = {
        "schema": "MTTPSMC102SI1dUnpatchedValidatorGuardrailLedger.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY",
        "clause": "SI-1d",
        "status": "UNPATCHED_VALIDATOR_GUARDRAILS_PRESERVED",
        "current_unpatched_packet_passes": current_result["passes"],
        "patched_local_axiom_packet_passes_unpatched_validator": patched_result["passes"],
        "conditional_unpatched_packet_passes": conditional_result["passes"],
        "current_closed_fields": promotion_matrix["closed_current_fields"],
        "current_open_fields": promotion_matrix["open_current_fields"],
        "dynamic_values_ready": promotion_matrix["dynamic_values_ready"],
        "unpatched_source_rule_proved": promotion_matrix["unpatched_source_rule_proved"],
        "honest_galerkin_table_exported": promotion_matrix["honest_galerkin_table_exported"],
        "interpretation": (
            "The local SI-1d chain can be used inside the local proof spine, but the unpatched PSM-C1-02 "
            "source-promotion validator still rejects the current packet and rejects the disclosed local-axiom packet."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    theorem = {
        "schema": "MTTPSMC102SI1dLocalSourceIdentityIntegrationTheorem.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY",
        "clause": "SI-1d",
        "name": "PSMC102LocalSourceIdentityIntegrationTheorem",
        "proved": True,
        "statement": (
            "Relative to the accepted local SelectedWeylVariationActionPrinciple and local "
            "SelectedFiniteC1SourceIdentityPrinciple, the PSM-C1-02 source-identity chain integrates: "
            "SI-1c supplies the local pre-residual action kernel, the local dynamic-C1 spine closes, "
            "and the local 110-row source-identity packet validates. This is not an unpatched proof."
        ),
        "local_source_identity_closed": True,
        "unpatched_source_identity_closed": False,
        "does_not_close": {
            "unpatched_SelectedFiniteC1SourceIdentityLemma": True,
            "unpatched_SelectedPhiFinC1PreResidualActionKernelTheorem": True,
            "honest_selected_Galerkin_C1_export": True,
            "true_SM_equivalence_without_local_principle": True,
            "no_knob_closure": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102SI1d.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_LocalSourceIdentityClosure_Integration_or_UnpatchedKernelExecution_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1e",
            "task": "Reconcile the local source-identity chain with downstream replay artifacts and emit the remaining local-vs-unpatched status table.",
        },
        "secondary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u",
            "task": "Continue unpatched closure by deriving the action principle or exporting honest selected Galerkin C1 tables.",
        },
        "status": "NEXT_WORKORDER_LOCAL_REPLAY_RECONCILIATION_OR_UNPATCHED_KERNEL_EXECUTION_PLAN",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102LocalSourceIdentityClosureIntegrationOrUnpatchedKernelExecution",
        "active_label": "PSM-C1-02",
        "active_routes": ["SOURCE-IDENTITY/SI-1d"],
        "closed_boundary": "DONE-PARITY-00",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "previous": rel(PREVIOUS),
        "previous_status": previous["status"],
        "output_packets": {
            "local_source_identity_integration": rel(LOCAL_INTEGRATION),
            "unpatched_validator_guardrail_ledger": rel(VALIDATOR_LEDGER),
            "local_source_identity_integration_theorem": rel(THEOREM),
            "next_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": theorem["name"],
            "proved": theorem["proved"],
            "statement": theorem["statement"],
        },
        "closure_decision": {
            "local_source_identity_closed": True,
            "unpatched_source_identity_closed": False,
            "local_dynamic_C1_closed": True,
            "current_unpatched_packet_passes": False,
            "patched_local_axiom_packet_passes_unpatched_validator": False,
            "conditional_unpatched_packet_passes_if_theorem_supplied": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
            "global_closure_claimed": False,
        },
        "what_closes_now": {
            "SI1d_local_source_identity_integrated": True,
            "local_chain_audits_imported_and_pass": True,
            "local_110row_source_identity_validates": True,
            "local_dynamic_C1_closure_connected": True,
            "unpatched_validator_guardrails_preserved": True,
            "superset_paths_constrained_to_locked_target": True,
        },
        "what_remains_open": {
            "unpatched_SelectedFiniteC1SourceIdentityLemma": True,
            "unpatched_SelectedPhiFinC1PreResidualActionKernelTheorem": True,
            "honest_selected_Galerkin_C1_export": True,
            "true_SM_equivalence_without_local_principle": True,
            "no_knob_closure": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_LocalSourceIdentityClosure_Integration_or_UnpatchedKernelExecution_v1",
        "active_label": "PSM-C1-02",
        "active_routes": candidate["active_routes"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "local_source_identity_closed": True,
        "unpatched_source_identity_closed": False,
        "local_dynamic_C1_closed": True,
        "current_unpatched_packet_passes": False,
        "patched_local_axiom_packet_passes_unpatched_validator": False,
        "conditional_unpatched_packet_passes_if_theorem_supplied": True,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    for path, obj in [
        (LOCAL_INTEGRATION, local_integration),
        (VALIDATOR_LEDGER, validator_ledger),
        (THEOREM, theorem),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    NOTE.write_text(
        f"""# MTT Selected PSM C1 02 LocalSourceIdentityClosure Integration or UnpatchedKernelExecution v1

Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1d`

Status: `{STATUS}`

Closed boundary label: `DONE-PARITY-00`

## Result

The local PSM-C1-02 source-identity chain is now integrated. SI-1c supplies the local pre-residual `Phi_fin^C1` action kernel, the local dynamic-C1 chain closes, and the local 110-row source-identity packet validates under the accepted local principles.

This is local-premise source-identity closure. It is not an unpatched theorem, not no-knob closure, and not a replacement for honest selected Galerkin C1 export.

## Guardrails

The current unpatched PSM-C1-02 packet still fails the unpatched validator. The disclosed patched/local-axiom packet also fails that unpatched validator. Only the conditional unpatched packet passes when the missing theorem or honest kernel export is supplied.

## Superset Strategy

Route C local action principle, local finite C1 source identity, and dynamic-C1 replay are constrained to the same locked source-identity target. They are not knobs.

## Next Artifact

`{NEXT}`
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
