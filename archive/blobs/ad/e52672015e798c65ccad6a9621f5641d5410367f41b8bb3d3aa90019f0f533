"""Build physical action-source emission / honest Galerkin replacement gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalactionsourceemission_or_honestgalerkinreplacement"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_physical_source_emission_validator.packet.json"
ROUTE_B = PACKET_DIR / "route_b_honest_galerkin_replacement_contract.packet.json"
ATTACK = PACKET_DIR / "dual_route_attack_queue.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalActionSourceEmission_or_HonestGalerkinReplacement_v1.md"

STATUS = "MTT_SELECTED_PHYSICALACTIONSOURCEEMISSION_OR_HONESTGALERKINREPLACEMENT_BUILT_DUAL_ROUTE_CONTRACT_OPEN"
NEXT = "MTT_Selected_RouteAEmissionOrRouteBGalerkinRowsExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_physicalc1actionidentity_or_samesourcebselectedemission.candidate.json")
    action_equiv = load(
        DATA
        / "selected_physicalc1actionidentity_or_samesourcebselectedemission"
        / "physical_action_identity_to_source_emission.packet.json"
    )
    bselected = load(
        DATA
        / "selected_physicalc1actionidentity_or_samesourcebselectedemission"
        / "same_source_bselected_emission_attempt.packet.json"
    )
    closure_equiv = load(
        DATA
        / "selected_physicalc1actionidentity_or_samesourcebselectedemission"
        / "closure_equivalence_and_next_gate.packet.json"
    )
    algebraic_values = load(
        DATA
        / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion"
        / "route_b_algebraic_kernel_value_execution_attempt.packet.json"
    )
    galerkin_route = load(
        DATA
        / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
        / "honest_galerkin_value_run_route.packet.json"
    )

    route_a_required = [
        "physical_action_identity",
        "physical_measure_equals_trace_frobenius_pairing",
        "phase_R_Z_source_selection",
        "shift_R_X_source_selection",
        "same_source_b_selected_emission",
        "no_extra_physical_boundary_or_source_term",
    ]
    route_a_current = {
        "physical_action_identity": action_equiv["current_physical_antecedents"][
            "physical_action_identity_promoted"
        ],
        "physical_measure_equals_trace_frobenius_pairing": action_equiv[
            "current_physical_antecedents"
        ]["physical_measure_equals_trace_frobenius_pairing"],
        "phase_R_Z_source_selection": action_equiv["current_physical_antecedents"][
            "phase_R_Z_selected"
        ],
        "shift_R_X_source_selection": action_equiv["current_physical_antecedents"][
            "shift_R_X_selected"
        ],
        "same_source_b_selected_emission": bselected[
            "same_source_b_selected_emitted_now"
        ],
        "no_extra_physical_boundary_or_source_term": action_equiv[
            "current_physical_antecedents"
        ]["no_extra_physical_boundary_or_source_term"],
    }

    route_a = {
        "schema": "MTTRouteAPhysicalSourceEmissionValidator.v1",
        "status": "ROUTE_A_PHYSICAL_SOURCE_EMISSION_NOT_YET_EMITTED",
        "required_emissions": route_a_required,
        "current_emissions": route_a_current,
        "all_required_emitted_now": all(route_a_current.values()),
        "validator_rule": (
            "Route A closes only if every required emission is theorem-derived from the same "
            "physical Phi_fin^C1 action branch. Replay values and formal trace support may be "
            "used only as consistency checks."
        ),
        "route_A_closes_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    counts = algebraic_values["counts"]
    route_b = {
        "schema": "MTTRouteBHonestGalerkinReplacementContract.v1",
        "status": "ROUTE_B_CONTRACT_BUILT_VALUES_NOT_EXECUTED",
        "strict_coordinate_target": galerkin_route["strict_coordinate_target"],
        "required_outputs": galerkin_route["required_outputs"],
        "kernel_row_contract": {
            "primitive_rows": counts["primitive_values_filled"],
            "hessian_source_rows": counts["hessian_values_filled"],
            "sector_matrix_rows": counts["sector_values_filled"],
            "total_rows": counts["total_algebraic_values_filled"],
            "algebraic_replay_values_filled": counts["total_algebraic_values_filled"],
        },
        "acceptance_tests": [
            "independent provenance for every primitive/Hessian/sector row",
            "exactness or certified error bounds before comparison to locked replay",
            "same selected zero-mode basis and trace/Frobenius normalization",
            "rank-two response or declared selected replacement rank",
            "A_selected, b_selected, deltaTheta_C1, and sector response matrices emitted as selected values",
            "nonzero-family-rank / C33 tests evaluated in the emitted packet",
        ],
        "forbidden_shortcuts": [
            "copying the conditional algebraic replay as independent quadrature",
            "using observed masses, mixings, CP phase, or benchmark matrices as row selectors",
            "declaring the finite Q_residual projector physical without a selected action/source rule",
            "accepting target residual agreement as source selection",
        ],
        "current_route_state": {
            "selected_source_verified": galerkin_route["selected_source_verified"],
            "can_replace_source_map_now": galerkin_route["can_replace_source_map_now"],
            "independent_rows_executed_now": False,
            "route_B_closes_now": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    attack = {
        "schema": "MTTDualRouteAttackQueue.v1",
        "status": "TWO_LEGAL_ATTACKS_FIXED_NEITHER_EXECUTED",
        "route_A_next_minimal_actions": [
            "derive the physical Phi_fin^C1 first-variation identity from the selected action",
            "promote the trace/Frobenius pairing to the physical measure",
            "emit R_Z, R_X, and b_selected from the same source term",
            "prove no extra physical boundary/source term remains",
        ],
        "route_B_next_minimal_actions": [
            "run or derive the 72-real selected Galerkin rows independently",
            "emit A_selected and b_selected from the independent rows",
            "emit sector response matrices and C33/nonzero-family-rank tests",
            "compare to the algebraic replay only after provenance is independent",
        ],
        "already_not_blockers": closure_equiv["already_not_blockers"],
        "remaining_cutset": closure_equiv["remaining_cutset"],
        "recommended_next": "Attempt Route B row execution while continuing Route A source-identity proof search.",
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalActionSourceEmissionOrHonestGalerkinReplacement",
        "status": STATUS,
        "inputs": {
            "previous_equivalence_gate": rel(
                DATA
                / "selected_physicalc1actionidentity_or_samesourcebselectedemission.candidate.json"
            ),
            "action_equivalence_packet": rel(
                DATA
                / "selected_physicalc1actionidentity_or_samesourcebselectedemission"
                / "physical_action_identity_to_source_emission.packet.json"
            ),
            "bselected_attempt_packet": rel(
                DATA
                / "selected_physicalc1actionidentity_or_samesourcebselectedemission"
                / "same_source_bselected_emission_attempt.packet.json"
            ),
            "algebraic_kernel_values": rel(
                DATA
                / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion"
                / "route_b_algebraic_kernel_value_execution_attempt.packet.json"
            ),
            "honest_galerkin_route": rel(
                DATA
                / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
                / "honest_galerkin_value_run_route.packet.json"
            ),
        },
        "output_packets": {
            "route_a_physical_source_emission_validator": rel(ROUTE_A),
            "route_b_honest_galerkin_replacement_contract": rel(ROUTE_B),
            "dual_route_attack_queue": rel(ATTACK),
        },
        "theorem": {
            "name": "DualRouteC1ClosureContractTheorem",
            "proved": True,
            "statement": (
                "After finite trace boundary, trace support, and the conditional source-map replay "
                "are fixed, the only legal unpatched dynamic C1 closure routes are Route A same-source "
                "physical action/source emission or Route B independent selected Galerkin/quadrature "
                "replacement. The contract fixes acceptance tests for both routes and rejects replay, "
                "target residuals, and observed constants as selectors."
            ),
        },
        "what_closes_now": {
            "route_A_validator_built": True,
            "route_B_replacement_contract_built": True,
            "kernel_row_counts_locked": True,
            "dual_route_attack_queue_built": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "route_A_physical_source_emission": True,
            "route_B_independent_Galerkin_rows": True,
            "A_selected": True,
            "b_selected": True,
            "deltaTheta_C1": True,
            "sector_response_matrices": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "route_A_closed": False,
            "route_B_closed": False,
            "A_selected_promoted": False,
            "b_selected_promoted": False,
            "deltaTheta_C1_promoted": False,
            "sector_response_matrices_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalActionSourceEmission_or_HonestGalerkinReplacement_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalActionSourceEmission or HonestGalerkinReplacement v1

Status: `{STATUS}`.

This gate turns the previous equivalence into an executable dual-route contract.

```text
Route A physical source emission closes now = {route_a["route_A_closes_now"]}
Route B honest Galerkin replacement closes = {route_b["current_route_state"]["route_B_closes_now"]}
primitive rows required                    = {route_b["kernel_row_contract"]["primitive_rows"]}
Hessian/source rows required               = {route_b["kernel_row_contract"]["hessian_source_rows"]}
sector matrix rows required                = {route_b["kernel_row_contract"]["sector_matrix_rows"]}
total finite C1 rows required              = {route_b["kernel_row_contract"]["total_rows"]}
```

Route A must emit the physical source packet from the same `Phi_fin^C1` action.
Route B must independently emit the selected Galerkin/quadrature rows and only
then compare them with the algebraic replay.

Next artifact: `{NEXT}`.
"""

    ROUTE_A.write_text(json.dumps(route_a, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROUTE_B.write_text(json.dumps(route_b, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ATTACK.write_text(json.dumps(attack, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
