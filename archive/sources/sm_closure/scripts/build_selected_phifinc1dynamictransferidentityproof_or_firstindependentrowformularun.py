"""Build PhiFinC1 dynamic-transfer proof / first independent row formula run gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_phifinc1dynamictransferidentityproof_or_firstindependentrowformularun"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PHIFIN = PACKET_DIR / "phifinc1_dynamic_transfer_identity_proof_attempt.packet.json"
FIRST_ROW = PACKET_DIR / "first_independent_row_formula_run_attempt.packet.json"
DECISION = PACKET_DIR / "phifinc1_or_firstrow_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhiFinC1DynamicTransferIdentityProof_or_FirstIndependentRowFormulaRun_v1.md"

STATUS = "MTT_SELECTED_PHIFINC1DYNAMICTRANSFERIDENTITYPROOF_OR_FIRSTINDEPENDENTROWFORMULARUN_ATTEMPTED_OPEN"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1PrimitiveOverlap_or_FirstRowKernelFormulaSource_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_samesourcedynamictransferidentity_or_independentrowformulaexecution.candidate.json")
    current_identity = load(
        DATA
        / "selected_samesourcedynamictransferidentity_or_independentrowformulaexecution"
        / "same_source_dynamic_transfer_identity_current_gate.packet.json"
    )
    old_phifin = load(DATA / "selected_phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run.candidate.json")
    first_row_old = load(
        DATA
        / "selected_physicalrzrxbsourceemission_or_primitiverowfirstexecution"
        / "route_b_first_primitive_row_execution_attempt.packet.json"
    )
    row_gate = load(
        DATA
        / "selected_samesourcedynamictransferidentity_or_independentrowformulaexecution"
        / "independent_row_formula_execution_current_gate.packet.json"
    )

    phifin = {
        "schema": "MTTPhiFinC1DynamicTransferIdentityProofAttempt.v1",
        "status": "STATIONARY_PHIFIN_TRACE_CLOSED_DIFFERENTIATED_C1_IDENTITY_OPEN",
        "stationary_trace_layer_closed": old_phifin["partial_promotion_theorem"]["corollary_now"][
            "stationary_source_layer_closed"
        ],
        "stationary_trace_sufficient_for_C1_transfer_identity": old_phifin["PhiFinC1_identity_attempt"][
            "stationary_trace_sufficient_for_C1_transfer_identity"
        ],
        "selected_identity_proved_now": False,
        "target_identity": current_identity["identity_equations"],
        "minimal_missing_equations": current_identity["minimal_missing_equations"],
        "missing_dynamic_objects": old_phifin["PhiFinC1_identity_attempt"]["missing_dynamic_objects"],
        "required_next_emissions": [
            "differentiated Phi_fin^C1 transfer derivative in the fixed 72-real coordinate system",
            "primitive C1 overlap contractions for phase and shift columns",
            "selected Hessian/source vector b_selected",
            "sector response matrices M_u, M_d, M_e, M_nuD",
        ],
        "if_future_identity_proved_then_values": current_identity["finite_values_if_identity_proved"],
        "why_not_proved_now": old_phifin["PhiFinC1_identity_attempt"]["reason"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    first_row = {
        "schema": "MTTFirstIndependentRowFormulaRunAttempt.v1",
        "status": "FIRST_ROW_ALGEBRAIC_VALUE_READY_INDEPENDENT_FORMULA_SOURCE_OPEN",
        "row_id": first_row_old["row_id"],
        "sector": first_row_old["sector"],
        "response": first_row_old["response"],
        "matrix_coordinate": first_row_old["matrix_coordinate"],
        "algebraic_support_value": first_row_old["algebraic_support_value"],
        "value_source": first_row_old["value_source"],
        "available_support": row_gate["available_support"],
        "required_kernel_fields_per_row": row_gate["required_kernel_fields_per_row"],
        "selected_primitive_kernel_formula": None,
        "selected_trace_or_pairing_source": None,
        "computed_complex_entry_value_independent": None,
        "exactness_or_error_bound_certificate": None,
        "provenance_independent_of_residual_projector_replay": False,
        "first_row_independently_executed_now": False,
        "why_not_executed_now": (
            "The row value 4/3 is available as algebraic residual support, but the current route requires "
            "a selected primitive kernel formula and pairing source independent of residual-projector replay."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTPhiFinC1OrFirstRowDecision.v1",
        "status": "PHIFINC1_IDENTITY_AND_FIRST_ROW_ATTEMPTED_NEITHER_CLOSED",
        "stationary_PhiFin_trace_closed": True,
        "differentiated_PhiFinC1_identity_closed": False,
        "first_independent_row_formula_executed": False,
        "source_gap_not_numeric_gap": True,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_actionable_target": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhiFinC1DynamicTransferIdentityProofOrFirstIndependentRowFormulaRun",
        "status": STATUS,
        "inputs": {
            "current_frontier": rel(DATA / "selected_samesourcedynamictransferidentity_or_independentrowformulaexecution.candidate.json"),
            "previous_phifin_gate": rel(DATA / "selected_phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run.candidate.json"),
            "first_row_support": rel(
                DATA
                / "selected_physicalrzrxbsourceemission_or_primitiverowfirstexecution"
                / "route_b_first_primitive_row_execution_attempt.packet.json"
            ),
        },
        "output_packets": {
            "phifinc1_dynamic_transfer_identity_proof_attempt": rel(PHIFIN),
            "first_independent_row_formula_run_attempt": rel(FIRST_ROW),
            "phifinc1_or_firstrow_decision": rel(DECISION),
        },
        "theorem": {
            "name": "PhiFinC1IdentityOrFirstIndependentRowAttemptTheorem",
            "proved": True,
            "statement": (
                "The stationary Phi_fin trace layer is selected-source closed, but it does not prove the "
                "differentiated C1 transfer identity. The first primitive row has an algebraic support value, "
                "but not an independent selected formula/pairing provenance. Thus the remaining blocker is "
                "differentiated Phi_fin^C1 primitive-overlap emission or first-row kernel formula source."
            ),
        },
        "previous_status": previous["status"],
        "closure_decision": decision,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PhiFinC1DynamicTransferIdentityProof_or_FirstIndependentRowFormulaRun_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "stationary_PhiFin_trace_closed": True,
        "differentiated_PhiFinC1_identity_closed": False,
        "first_independent_row_formula_executed": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhiFinC1DynamicTransferIdentityProof or FirstIndependentRowFormulaRun v1

Status: `{STATUS}`.

This artifact attempts both current exits.

Route A: stationary `Phi_fin` trace is closed, but it is not the differentiated
`Phi_fin^C1` transfer identity. The missing object is the C1 derivative with
primitive overlap contractions and `b_selected` in the fixed 72-real coordinate
system.

Route B: the first row `u:phase:r0c0` has algebraic value `4/3`, but the value is
not independently emitted from a selected primitive kernel formula and pairing
source.

No unpatched dynamic-C1, true-SM-equivalence, or no-knob closure is claimed.
"""

    for path, payload in [
        (PHIFIN, phifin),
        (FIRST_ROW, first_row),
        (DECISION, decision),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
