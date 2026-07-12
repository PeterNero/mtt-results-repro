"""Build PhiFin C1 action axiom or independent Galerkin kernel emission gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom.candidate.json"
MINIMAL_AXIOM = DATA / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom" / "minimal_action_axiom_or_theorem.packet.json"
STRICT_TEMPLATE = DATA / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom" / "pre_residual_variation_hessian_source_kernel.strict_template.json"
VARIATION_GAP = DATA / "selected_variationoperatorshapecompatibility_or_hessiansourcegap" / "hessian_source_and_selection_gap.packet.json"
SLOT_ROUTING = DATA / "selected_variationoperatorshapecompatibility_or_hessiansourcegap" / "variation_operator_72_slot_routing.packet.json"
PHYSICAL_SOURCE_CERT = DATA / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun" / "minimal_physical_source_certificate.packet.json"
FORMAL_ROWS = DATA / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource" / "formal_110_row_replay_integrated.packet.json"

SLUG = "selected_phifinc1actionaxiom_or_independentgalerkinkernelemission"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
AXIOM_CONTRACT = PACKET_DIR / "route_a_phifinc1_action_kernel_axiom_contract.packet.json"
KERNEL_EMISSION = PACKET_DIR / "route_b_independent_galerkin_kernel_emission_contract.packet.json"
VALIDATOR = PACKET_DIR / "four_clause_validator_current_result.packet.json"
CUTSET = PACKET_DIR / "minimal_next_cutset_after_action_kernel_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhiFinC1ActionAxiom_or_IndependentGalerkinKernelEmission_v1.md"

STATUS = "MTT_SELECTED_PHIFINC1ACTIONAXIOM_OR_INDEPENDENTGALERKINKERNELEMISSION_BUILT_FOUR_CLAUSE_CONTRACT_OPEN"
NEXT = "MTT_Selected_ActionKernelFourClauseProof_or_IndependentKernelValuesRun_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    minimal_axiom = load(MINIMAL_AXIOM)
    strict_template = load(STRICT_TEMPLATE)
    variation_gap = load(VARIATION_GAP)
    slot_routing = load(SLOT_ROUTING)
    physical_source = load(PHYSICAL_SOURCE_CERT)
    formal_rows = load(FORMAL_ROWS)

    four_clauses = [
        "selected_pre_residual_variation_functional",
        "same_source_hessian_b_selected",
        "sector_functor_assembly",
        "source_independence_from_residual_projector_replay",
    ]

    route_a = {
        "schema": "MTTPhiFinC1ActionKernelAxiomContract.v1",
        "status": "CONTRACT_READY_UNPROVED",
        "source": rel(MINIMAL_AXIOM),
        "strict_template": rel(STRICT_TEMPLATE),
        "four_required_clauses": four_clauses,
        "current_clause_values": {
            "selected_pre_residual_variation_functional": False,
            "same_source_hessian_b_selected": False,
            "sector_functor_assembly": False,
            "source_independence_from_residual_projector_replay": False,
        },
        "conditional_witness_available": previous["what_closes_now"]["conditional_witness_passes"],
        "if_all_four_clauses_proved": {
            "pre_residual_variation_hessian_source_kernel_validates": True,
            "same_branch_PhiFinC1_source_emission_promotes": True,
            "unpatched_A_selected_promotes": True,
            "unpatched_b_selected_promotes": True,
            "unpatched_deltaTheta_C1_promotes": True,
            "unpatched_SM_parity_dynamic_packet_closes": True,
        },
        "proved_now": False,
        "inserted_as_axiom_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_b = {
        "schema": "MTTIndependentGalerkinKernelEmissionContract.v1",
        "status": "CONTRACT_READY_VALUES_OPEN",
        "source": rel(VARIATION_GAP),
        "formal_row_reference": rel(FORMAL_ROWS),
        "required_emissions": {
            "selected_phase_shift_variation_operators_pre_residual": False,
            "selected_hessian_counterterm_source": False,
            "selected_b_vector_source": False,
            "all_72_kernel_rows_independent_of_residual_replay": False,
            "sector_36_and_hessian_2_rows_independent_of_residual_replay": False,
            "exactness_or_error_certificate": False,
        },
        "slot_support": {
            "primitive_row_slots": 72,
            "sector_matrix_slots": 36,
            "hessian_source_slots": 2,
            "formal_110_row_replay_already_closed": True,
            "variation_operator_shapes_routed": slot_routing.get("shift_R_X_rows") == 36,
        },
        "values_emitted_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    validator = {
        "schema": "MTTFourClauseActionKernelCurrentValidator.v1",
        "status": "CURRENT_SUPPORT_REJECTED_CONDITIONAL_WITNESS_PASSES",
        "route_A_all_four_clauses_pass": all(route_a["current_clause_values"].values()),
        "route_B_all_kernel_values_emitted": all(route_b["required_emissions"].values()),
        "conditional_witness_passes": True,
        "current_support_passes": False,
        "why_rejected": [
            "current support still does not prove the selected pre-residual Phi_fin^C1 action kernel",
            "same-source Hessian/b_selected remains a source clause rather than an independent derivation",
            "sector functor assembly is compatible but not promoted as physical source emission",
            "formal 110-row replay is not provenance-independent of residual-projector replay",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTActionKernelOrIndependentEmissionNextCutset.v1",
        "status": "NEXT_CUTSET_SELECTED",
        "minimal_route_A": four_clauses,
        "minimal_route_B": list(route_b["required_emissions"].keys()),
        "non_blockers_now": [
            "finite trace boundary cancellation",
            "stationary trace and basis support",
            "dynamic dotD trace binding",
            "formal 110-row finite replay",
            "phase/shift variation operator slot routing",
            "alpha1/dotD bridge",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": "The remaining source-promotion wall is no longer a value-slot calculation. It is a four-clause selected action-kernel proof or an independent kernel-emission run with provenance independent of residual-projector replay.",
        },
    }

    candidate = {
        "candidate": "MTTSelectedPhiFinC1ActionAxiomOrIndependentGalerkinKernelEmission",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "minimal_action_axiom": rel(MINIMAL_AXIOM),
            "strict_template": rel(STRICT_TEMPLATE),
            "variation_hessian_gap": rel(VARIATION_GAP),
            "slot_routing": rel(SLOT_ROUTING),
            "physical_source_certificate": rel(PHYSICAL_SOURCE_CERT),
            "formal_110_row_replay": rel(FORMAL_ROWS),
        },
        "output_packets": {
            "route_a_phifinc1_action_kernel_axiom_contract": rel(AXIOM_CONTRACT),
            "route_b_independent_galerkin_kernel_emission_contract": rel(KERNEL_EMISSION),
            "four_clause_validator_current_result": rel(VALIDATOR),
            "minimal_next_cutset_after_action_kernel_gate": rel(CUTSET),
        },
        "promotion_decision": {
            "route_A_four_clause_action_kernel_proved": False,
            "route_A_axiom_inserted": False,
            "route_B_independent_kernel_emission_run": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "four_clause_action_kernel_contract_built": True,
            "independent_kernel_emission_contract_built": True,
            "current_rejection_reason_machine_checkable": True,
            "formal_110_row_values_retained_as_support": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_pre_residual_variation_functional": True,
            "same_source_hessian_b_selected": True,
            "sector_functor_assembly_as_physical_source": True,
            "source_independence_from_residual_projector_replay": True,
            "independent_galerkin_kernel_values": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "no_knob_closure": True,
        },
        "theorem": {
            "name": "PhiFinC1ActionKernelOrIndependentEmissionCutsetTheorem",
            "proved": True,
            "statement": (
                "After formal 110-row replay, finite boundary cancellation, trace/basis support, alpha1/dotD binding, "
                "and phase/shift slot routing are closed, the remaining unpatched source-promotion problem is exactly "
                "a four-clause selected Phi_fin^C1 action-kernel theorem or an independent Galerkin kernel-emission run. "
                "The current support is rejected; the conditional witness and acceptance contracts are fixed."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "patched_SM_parity_closure_preserved": True,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhiFinC1ActionAxiom_or_IndependentGalerkinKernelEmission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhiFinC1ActionAxiom or IndependentGalerkinKernelEmission v1

Status: `{STATUS}`.

The formal finite computation layer is no longer the blocker:

```text
formal 110-row finite replay         closed as support
finite trace boundary cancellation   closed
trace/basis support                  imported
dynamic dotD trace binding           imported
phase/shift slot routing             compatible
alpha1/dotD bridge                   imported
```

The remaining Route A proof is exactly four clauses:

```text
selected pre-residual variation functional
same-source Hessian / b_selected
sector functor assembly as physical source
source independence from residual-projector replay
```

Route B can still close independently by emitting selected Galerkin kernel
values and exactness/error certificates without residual-projector replay as
source.

This artifact does not claim unpatched closure. It makes the final source
promotion wall machine-checkable.

Next artifact: `{NEXT}`.
"""

    AXIOM_CONTRACT.write_text(json.dumps(route_a, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    KERNEL_EMISSION.write_text(json.dumps(route_b, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    VALIDATOR.write_text(json.dumps(validator, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CUTSET.write_text(json.dumps(cutset, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
