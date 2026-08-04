"""Build Phi_fin^C1 residual-projector application or honest Galerkin execution gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PROJECTOR_GATE = DATA / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill.candidate.json"
PROJECTOR_PACKET = (
    DATA
    / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill"
    / "canonical_fixedfiber_residual_projector.packet.json"
)
CUTSET_PACKET = (
    DATA
    / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill"
    / "projector_or_galerkin_cutset_decision.packet.json"
)
PHIFIN_DIFF = DATA / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun.candidate.json"
PHIFIN_DYNAMIC = DATA / "selected_phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run.candidate.json"
GALERKIN_CONTRACT = (
    DATA
    / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun"
    / "honest_galerkin_c1_value_run_contract.packet.json"
)

OUTPUT = DATA / "selected_phifinc1_residualprojectorapplication_or_honestgalerkinexecution_valuefill.candidate.json"
PACKET_DIR = DATA / "selected_phifinc1_residualprojectorapplication_or_honestgalerkinexecution_valuefill"
APPLICATION_AUDIT_PACKET = PACKET_DIR / "phifinc1_projector_application_audit.packet.json"
EXECUTION_CONTRACT_PACKET = PACKET_DIR / "honest_galerkin_execution_contract.packet.json"
DECISION_PACKET = PACKET_DIR / "application_or_execution_decision.packet.json"
CERT = CERTS / "selected_phifinc1_residualprojectorapplication_or_honestgalerkinexecution_valuefill_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhiFinC1ResidualProjectorApplication_or_HonestGalerkinExecution_ValueFill_v1.md"

STATUS = "MTT_SELECTED_PHIFINC1_RESIDUALPROJECTORAPPLICATION_OR_HONESTGALERKINEXECUTION_VALUEFILL_BUILT_APPLICATION_NOGO_OPEN"
NEXT = "MTT_Selected_DifferentiatedResidualProjectorSourceRule_or_HonestGalerkinC1Execution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    projector_gate = load(PROJECTOR_GATE)
    projector_packet = load(PROJECTOR_PACKET)
    cutset = load(CUTSET_PACKET)
    phifin_diff = load(PHIFIN_DIFF)
    phifin_dynamic = load(PHIFIN_DYNAMIC)
    galerkin_contract = load(GALERKIN_CONTRACT)

    transport_no_go = phifin_diff["transport_only_no_go_theorem"]
    conditional = cutset["if_lane_A_application_theorem_is_supplied"]

    application_audit = {
        "schema": "MTTPhiFinC1ResidualProjectorApplicationAudit.v1",
        "status": "PROJECTOR_APPLICATION_NOT_DERIVED_BY_EXISTING_PHIFINC1_ARTIFACTS",
        "canonical_projector_available": projector_gate["projector_closure"]["canonical_projector_computed"],
        "canonical_projector_mathematically_selected": projector_gate["projector_closure"][
            "canonical_projector_selected_as_mathematical_consequence"
        ],
        "projector_operator_checks": projector_packet["operator_checks"],
        "existing_PhiFinC1_support": {
            "stationary_transport_source_layer_available": True,
            "alpha1_dotD_driver_attached": phifin_diff["driver_contract"]["alpha1_driver_verified"],
            "selected_dotD_source_verified": phifin_diff["driver_contract"]["selected_dotD_source_verified"],
            "selected_PhiFinC1_identity_claimed": phifin_diff["selected_PhiFinC1_identity_claimed"],
            "dynamic_transfer_identity_status": phifin_dynamic["status"],
        },
        "blocking_no_go": {
            "name": transport_no_go["name"],
            "proved": transport_no_go["proved"],
            "scope": transport_no_go["scope"],
            "all_sector_matrices_verified_zero": transport_no_go["finite_evidence"][
                "all_sector_matrices_verified_zero"
            ],
            "canonical_all_zero": transport_no_go["finite_evidence"]["canonical_all_zero"],
            "consequence": (
                "Existing stationary Phi_fin^C1 transport plus the canonical mode-conserving "
                "primitive tensor cannot be reinterpreted as the physical application of "
                "Q_residual.  A new differentiated residual-projector source rule, "
                "basis-transport/vertex/Hessian source, or honest Galerkin execution is required."
            ),
        },
        "conditional_value_if_new_application_rule_is_proved": conditional,
        "promotion_decision": {
            "PhiFinC1_projector_application_promoted": False,
            "selected_A_selected_promoted": False,
            "selected_b_selected_promoted": False,
            "selected_deltaTheta_C1_promoted": False,
            "SM_parity_dynamic_packet_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    execution_contract = {
        "schema": "MTTHonestGalerkinC1ExecutionContract.v1",
        "status": "HONEST_GALERKIN_EXECUTION_VALUES_OPEN",
        "source_contract_status": galerkin_contract["status"],
        "current_manifest_status": galerkin_contract["current_manifest_status"],
        "required_inputs": galerkin_contract["required_inputs"],
        "required_outputs": galerkin_contract["required_outputs"],
        "acceptance_checks": galerkin_contract["acceptance_checks"],
        "selected_source_verified_now": galerkin_contract["selected_source_verified"],
        "observed_flavor_data_forbidden": galerkin_contract["observed_flavor_data_forbidden"],
        "target_fitting_forbidden": galerkin_contract["target_fitting_forbidden"],
        "promotion_decision": {
            "honest_Galerkin_C1_execution_promoted": False,
            "replacement_A_selected_promoted": False,
            "replacement_b_selected_promoted": False,
            "replacement_deltaTheta_C1_promoted": False,
            "SM_parity_dynamic_packet_closed": False,
        },
    }

    decision = {
        "schema": "MTTApplicationOrExecutionDecision.v1",
        "status": "APPLICATION_NOGO_EXECUTION_VALUES_OPEN",
        "straight_path": (
            "Prove a selected differentiated residual-projector source rule: "
            "Phi_fin^C1 applies Q_residual to the selected Weyl source packet."
        ),
        "superset_path": (
            "Run honest selected Galerkin C1 execution using the typed monad/HYM/finite "
            "Weyl data and replace the conditional packet with emitted values."
        ),
        "locked_target": "SM-parity dynamic packet closure only.",
        "what_is_now_ruled_out": [
            "promoting Q_residual merely because it is canonical",
            "using stationary transport-only Phi_fin^C1 as the dynamic C1 application rule",
            "using observed flavor constants or benchmark residuals as selectors",
        ],
        "what_would_close_next": [
            "selected differentiated residual-projector source rule",
            "selected basis-transport/vertex/Hessian source emitting the same residual application",
            "honest selected Galerkin C1 execution values passing the acceptance checks",
        ],
        "SM_parity_dynamic_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_flavor_constants_closed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhiFinC1ResidualProjectorApplicationOrHonestGalerkinExecutionValueFill",
        "status": STATUS,
        "inputs": {
            "canonical_projector_gate": rel(PROJECTOR_GATE),
            "canonical_projector_packet": rel(PROJECTOR_PACKET),
            "projector_or_galerkin_cutset": rel(CUTSET_PACKET),
            "differentiated_PhiFinC1_gate": rel(PHIFIN_DIFF),
            "PhiFinC1_dynamic_transfer_gate": rel(PHIFIN_DYNAMIC),
            "honest_galerkin_contract": rel(GALERKIN_CONTRACT),
        },
        "output_packets": {
            "phifinc1_projector_application_audit": rel(APPLICATION_AUDIT_PACKET),
            "honest_galerkin_execution_contract": rel(EXECUTION_CONTRACT_PACKET),
            "application_or_execution_decision": rel(DECISION_PACKET),
        },
        "what_closes_now": {
            "canonical_projector_not_enough_guardrail": True,
            "stationary_transport_only_application_rejected": True,
            "PhiFinC1_application_rule_reduced_to_new_differentiated_source_rule": True,
            "honest_Galerkin_execution_contract_reemitted": True,
            "straight_vs_superset_paths_separated": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "selected_differentiated_residual_projector_source_rule": True,
            "selected_basis_transport_vertex_or_Hessian_source": True,
            "honest_selected_Galerkin_C1_execution_values": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_deltaTheta_C1": True,
            "SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_flavor_closure": True,
        },
        "promotion_decision": {
            "PhiFinC1_projector_application_promoted": False,
            "honest_Galerkin_C1_execution_promoted": False,
            "selected_A_selected_promoted": False,
            "selected_b_selected_promoted": False,
            "selected_deltaTheta_C1_promoted": False,
            "SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_flavor_constants_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "PhiFinC1ResidualProjectorApplicationGuardrailTheorem",
            "proved": True,
            "statement": (
                "The canonical residual projector Q_residual is now selected as a mathematical "
                "consequence of the fixed-fiber quotient, but existing Phi_fin^C1 artifacts do "
                "not prove that the physical differentiated C1 transfer applies it.  In fact, "
                "the current selected stationary transport plus canonical mode-conserving "
                "primitive tensor has zero one-response C1 matrices, so it cannot emit the "
                "phase/shift residual columns.  Therefore SM-parity dynamic closure still "
                "requires a new selected differentiated residual-projector source rule, a "
                "selected basis-transport/vertex/Hessian source, or an honest selected "
                "Galerkin C1 execution."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_PhiFinC1ResidualProjectorApplication_or_HonestGalerkinExecution_ValueFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "application_audit_packet_path": rel(APPLICATION_AUDIT_PACKET),
        "execution_contract_packet_path": rel(EXECUTION_CONTRACT_PACKET),
        "decision_packet_path": rel(DECISION_PACKET),
        "theorem_proved": True,
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhiFinC1ResidualProjectorApplication or HonestGalerkinExecution ValueFill v1

Status: `{STATUS}`.

The canonical projector is now mathematically selected, but that is not yet a
physical C1 transfer rule.  Existing `Phi_fin^C1` artifacts prove a guardrail:
stationary transport plus the canonical mode-conserving primitive tensor gives
zero one-response C1 matrices, so it cannot emit the residual `R_Z/R_X` columns.

Straight path:

```text
prove selected differentiated Phi_fin^C1 applies Q_residual
```

Superset fallback:

```text
run honest selected Galerkin C1 execution and emit replacement values
```

The conditional values remain available if the straight path is proved:

```text
A^T A = {conditional["A_transpose_A"]}
A^T b = {conditional["A_transpose_b"]}
deltaTheta_C1 = {conditional["deltaTheta_C1"]}
```

No observed masses, CKM/PMNS values, CP phase, benchmark matrices, or target
residuals are used as selectors.

Next artifact: `{NEXT}`.
"""

    APPLICATION_AUDIT_PACKET.write_text(json.dumps(application_audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    EXECUTION_CONTRACT_PACKET.write_text(json.dumps(execution_contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    DECISION_PACKET.write_text(json.dumps(decision, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
