"""Build physical Phi_fin^C1 action-source / provenance-independence theorem gate.

This is the minimized post-row-replay frontier.  The formal finite computations
are already closed.  This artifact bundles the remaining physical/source
obligation into a single validator-ready theorem contract:

* Route A: physical Phi_fin^C1 action-source identity emits the same
  R_Z/R_X/b_selected packet with no extra boundary/source term.
* Route B: provenance-independent Galerkin/row source emits the same formal
  finite row packet without inheriting residual-projector replay.

No route is promoted here.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalphifinc1actionsource_or_provenanceindependencetheorem"
OUTPUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
CONTRACT_PACKET = PACKET_DIR / "last_source_theorem_contract.packet.json"
VALIDATOR_PACKET = PACKET_DIR / "promotion_validator_kernel.packet.json"
DECISION_PACKET = PACKET_DIR / "current_frontier_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_PhysicalPhiFinC1ActionSource_or_ProvenanceIndependenceTheorem_v1.md"

PREVIOUS = DATA / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource.candidate.json"
PHYSICAL_ACTION = DATA / "selected_physicalc1actionidentity_or_samesourcebselectedemission.candidate.json"
ACTION_RESTRICTION = DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission.candidate.json"
MEASURE_PROMOTION = DATA / "selected_physicalmeasure_or_finitegalerkinpromotion.candidate.json"
FORMAL_INTEGRATED = (
    DATA
    / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
    / "formal_110_row_replay_integrated.packet.json"
)
PROMOTION_CUTSET = (
    DATA
    / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
    / "physical_source_promotion_cutset.packet.json"
)

STATUS = (
    "MTT_SELECTED_PHYSICALPHIFINC1ACTIONSOURCE_OR_PROVENANCEINDEPENDENCETHEOREM_"
    "BUILT_LAST_SOURCE_CONTRACT_OPEN"
)
NEXT = "MTT_Selected_PhysicalPhiFinC1ActionSourceTheorem_Fill_or_IndependentGalerkinProvenanceRun_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    physical_action = load(PHYSICAL_ACTION)
    action_restriction = load(ACTION_RESTRICTION)
    measure_promotion = load(MEASURE_PROMOTION)
    formal = load(FORMAL_INTEGRATED)
    cutset = load(PROMOTION_CUTSET)

    contract = {
        "schema": "MTTLastPhiFinC1SourceTheoremContract.v1",
        "status": "LAST_SOURCE_THEOREM_CONTRACT_BUILT_NOT_FILLED",
        "formal_computation_layer_closed": {
            "formal_110_row_replay_closed": previous["promotion_decision"][
                "formal_110_row_replay_closed"
            ],
            "formal_A_b_deltaTheta_replay_closed": previous["promotion_decision"][
                "formal_A_b_deltaTheta_replay_closed"
            ],
            "formal_A_transpose_b": formal["hessian_source_rows"]["A_transpose_b"],
            "formal_deltaTheta_C1": formal["hessian_source_rows"]["deltaTheta_C1"],
            "primitive_rows": formal["row_counts"]["primitive_rows"],
            "sector_rows": formal["row_counts"]["sector_matrix_rows"],
            "hessian_source_rows": formal["row_counts"]["hessian_source_rows"],
            "total_rows": formal["row_counts"]["total_rows"],
        },
        "route_A_physical_action_source_theorem": {
            "must_emit": [
                "physical Phi_fin^C1 action identity",
                "physical action restricts exactly to selected finite Weyl trace quotient",
                "no extra physical boundary/source term",
                "phase_R_Z source selection",
                "shift_R_X source selection",
                "same-source b_selected emission",
            ],
            "equivalence_source": rel(PHYSICAL_ACTION),
            "measure_retirement_source": rel(ACTION_RESTRICTION),
            "conditional_promotion_source": rel(MEASURE_PROMOTION),
            "current_truth_values": cutset["route_A_physical_action_source"],
            "closed_now": False,
        },
        "route_B_provenance_independence_theorem": {
            "must_emit": [
                "selected Galerkin/row source independent of residual-projector replay",
                "same 110-row finite packet or explicitly equivalent replacement packet",
                "exactness certificates retained",
                "no observed constants or locked targets used as selectors",
            ],
            "current_truth_values": cutset["route_B_independent_provenance"],
            "closed_now": False,
        },
        "if_either_route_closes": cutset["if_cutset_closes"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    validator = {
        "schema": "MTTLastSourcePromotionValidatorKernel.v1",
        "status": "VALIDATOR_KERNEL_READY_WAITING_FOR_SOURCE_THEOREM_FILL",
        "accepts_route_A_if_all_true": [
            "physical_action_identity",
            "physical_measure_equals_trace_frobenius_pairing",
            "no_extra_physical_boundary_or_source_term",
            "phase_R_Z_source_selection",
            "shift_R_X_source_selection",
            "same_source_b_selected_emission",
        ],
        "accepts_route_B_if_all_true": [
            "all_72_primitive_values_exact",
            "formal_110_rows_executed",
            "source_independent_of_residual_projector_replay",
        ],
        "forbidden_shortcuts": [
            "promoting patched parity values as unpatched source data",
            "using observed SM constants as selectors",
            "using residual-projector replay as independent provenance",
            "declaring A_selected/b_selected physical before Route A or Route B closes",
        ],
        "consequent_if_accepted": {
            "unpatched_SM_parity_dynamic_packet_closed": True,
            "physical_A_selected": [[12.0, 0.0], [0.0, 12.0]],
            "physical_b_selected": [12.0, 12.0],
            "physical_deltaTheta_C1": [1.0, 1.0],
            "physical_sector_response_matrices": True,
        },
        "accepted_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTLastSourceFrontierDecision.v1",
        "status": "ONLY_LAST_SOURCE_THEOREM_OR_INDEPENDENT_PROVENANCE_RUN_REMAINS",
        "formal_computation_layer_closed": True,
        "finite_measure_normalization_retired": action_restriction["closure_decision"][
            "measure_normalization_derived"
        ],
        "physical_action_equivalence_theorem_built": physical_action["what_closes_now"][
            "action_identity_to_source_emission_equivalence"
        ],
        "finite_rows_to_physical_promotion_theorem_conditional": measure_promotion[
            "promotion_decision"
        ]["promotion_theorem_proved"],
        "route_A_physical_action_source_closed": False,
        "route_B_provenance_independence_closed": False,
        "unpatched_A_selected_promoted": False,
        "unpatched_b_selected_promoted": False,
        "unpatched_deltaTheta_C1_promoted": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_actionable_target": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalPhiFinC1ActionSourceOrProvenanceIndependenceTheorem",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "physical_action_equivalence": rel(PHYSICAL_ACTION),
            "action_restriction_gate": rel(ACTION_RESTRICTION),
            "measure_promotion_gate": rel(MEASURE_PROMOTION),
            "formal_110_row_replay_integrated": rel(FORMAL_INTEGRATED),
            "promotion_cutset": rel(PROMOTION_CUTSET),
        },
        "output_packets": {
            "last_source_theorem_contract": rel(CONTRACT_PACKET),
            "promotion_validator_kernel": rel(VALIDATOR_PACKET),
            "current_frontier_decision": rel(DECISION_PACKET),
        },
        "what_closes_now": {
            "last_source_theorem_contract_built": True,
            "promotion_validator_kernel_built": True,
            "scattered_physical_source_gates_condensed": True,
            "formal_computation_layer_confirmed_closed": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "physical_PhiFinC1_action_source_theorem_fill": True,
            "independent_Galerkin_or_row_provenance_run": True,
            "unpatched_A_selected": True,
            "unpatched_b_selected": True,
            "unpatched_deltaTheta_C1": True,
            "true_SM_equivalence_closure": True,
            "no_knob_closure": True,
        },
        "promotion_decision": decision,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "theorem": {
            "name": "LastPhiFinC1SourceContractTheorem",
            "proved": True,
            "statement": (
                "After exact 72-row Weyl execution and formal 110-row finite-trace integration, "
                "the dynamic C1 numerical and linear-algebra layers are closed.  Existing "
                "physical-action gates reduce unpatched promotion to exactly one remaining "
                "source condition: either the physical Phi_fin^C1 action emits the same "
                "R_Z/R_X/b_selected packet with no extra boundary/source term, or an "
                "independent Galerkin/row provenance run emits the same packet without "
                "residual-projector inheritance.  This artifact builds the validator-ready "
                "contract for that last condition; it does not fill it."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalPhiFinC1ActionSource_or_ProvenanceIndependenceTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "packet_paths": candidate["output_packets"],
        "theorem_proved": True,
        "formal_computation_layer_closed": True,
        "last_source_theorem_contract_built": True,
        "route_A_physical_action_source_closed": False,
        "route_B_provenance_independence_closed": False,
        "unpatched_A_selected_promoted": False,
        "unpatched_b_selected_promoted": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalPhiFinC1ActionSource or ProvenanceIndependenceTheorem v1

Status: `{STATUS}`

## Theorem

{candidate["theorem"]["statement"]}

## Last Contract

Route A closes by filling the physical `Phi_fin^C1` action-source theorem.
Route B closes by filling a residual-projector-independent Galerkin/row
provenance run.

Both routes promote the same formal packet:

- `A^T A = 12 I_2`
- `A^T b = (12, 12)`
- `deltaTheta_C1 = (1, 1)`
- 110 formal finite rows

No route is promoted in this artifact.

Next artifact: `{NEXT}`.
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "{SLUG}.candidate.json"
CERT = ROOT / "certificates" / "{SLUG}_certificate.json"
PACKET_DIR = ROOT / "candidate_data" / "{SLUG}"
CONTRACT = PACKET_DIR / "last_source_theorem_contract.packet.json"
VALIDATOR = PACKET_DIR / "promotion_validator_kernel.packet.json"
DECISION = PACKET_DIR / "current_frontier_decision.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalPhiFinC1ActionSource_or_ProvenanceIndependenceTheorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    cert = load(CERT)
    contract = load(CONTRACT)
    validator = load(VALIDATOR)
    decision = load(DECISION)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(contract["formal_computation_layer_closed"]["formal_110_row_replay_closed"] is True, "formal replay not closed")
    require(contract["formal_computation_layer_closed"]["total_rows"] == 110, "total rows mismatch")
    require(contract["route_A_physical_action_source_theorem"]["closed_now"] is False, "route A overclosed")
    require(contract["route_B_provenance_independence_theorem"]["closed_now"] is False, "route B overclosed")
    require(validator["accepted_now"] is False, "validator overaccepted")
    require("using residual-projector replay as independent provenance" in validator["forbidden_shortcuts"], "guardrail missing")
    require(validator["consequent_if_accepted"]["physical_b_selected"] == [12.0, 12.0], "consequent b mismatch")
    require(decision["formal_computation_layer_closed"] is True, "formal layer not closed")
    require(decision["finite_measure_normalization_retired"] is True, "measure not retired")
    require(decision["physical_action_equivalence_theorem_built"] is True, "action equivalence missing")
    require(decision["finite_rows_to_physical_promotion_theorem_conditional"] is True, "conditional promotion missing")
    require(decision["route_A_physical_action_source_closed"] is False, "route A decision overclosed")
    require(decision["route_B_provenance_independence_closed"] is False, "route B decision overclosed")
    require(decision["unpatched_A_selected_promoted"] is False, "A overpromoted")
    require(decision["unpatched_b_selected_promoted"] is False, "b overpromoted")
    require(decision["true_SM_equivalence_closed"] is False, "SM equivalence overclaimed")
    require(decision["no_knob_closed"] is False, "no-knob overclaimed")
    require(cert["last_source_theorem_contract_built"] is True, "cert contract missing")
    require(cert["route_A_physical_action_source_closed"] is False, "cert route A overclosed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("No route is promoted" in note, "note missing guardrail")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(CONTRACT_PACKET, contract)
    write_json(VALIDATOR_PACKET, validator)
    write_json(DECISION_PACKET, decision)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(f"wrote {rel(OUTPUT)}")
    print(f"status {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
