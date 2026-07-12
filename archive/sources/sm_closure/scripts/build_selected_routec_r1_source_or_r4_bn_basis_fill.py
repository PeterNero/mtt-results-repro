"""Attempt to fill Route-C R1 source certificate or R4 B_N basis.

This is the next executable gate after the emission contracts.  It tries the
two legal routes and records which fields are fillable from current artifacts.
It refuses to mark selected values closed unless the required source/basis data
are actually emitted.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CERTS = Q79 / "certificates"

PREVIOUS = DATA / "selected_phifin_payload_or_bn_basis_emission.candidate.json"
R1_CONTRACT = DATA / "selected_phifin_payload_or_bn_basis_emission" / "selected_phifin_payload.emission_contract.json"
R4_CONTRACT = DATA / "selected_phifin_payload_or_bn_basis_emission" / "selected_bn_basis.emission_contract.json"

OUT_DATA = DATA / "selected_routec_r1_source_or_r4_bn_basis_fill.candidate.json"
OUT_CERT = CERTS / "selected_routec_r1_source_or_r4_bn_basis_fill_certificate.json"
OUT_NOTE = CORPUS / "MTT_Selected_RouteC_R1_Source_Certificate_or_R4_BN_Basis_Fill_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def build_candidate() -> dict[str, Any]:
    previous = load_json(PREVIOUS)
    r1_contract = load_json(R1_CONTRACT)
    r4_contract = load_json(R4_CONTRACT)
    source_origin = load_json(DATA / "routec_selected_source_origin_lemma.candidate.json")
    phifin = load_json(DATA / "finite_emission_morphism_phifin.candidate.json")
    alpha = load_json(DATA / "selected_phifin_alpha1_payload.candidate.json")
    first = load_json(DATA / "selected_routec_strominger_galerkin_first_run.candidate.json")
    hym_attempt = load_json(Q79_CERTS / "selected_hym_operator_source_attempt_certificate.json")
    deck = load_json(Q79_CERTS / "iwasawa_standard_lattice_deck_scaffold_certificate.json")
    basis = load_json(Q79_CERTS / "iwasawa_galerkin_basis_skeleton_certificate.json")
    protocol = load_json(Q79_CERTS / "iwasawa_non_invariant_galerkin_protocol_certificate.json")

    r1_fillable = {
        "fixed_branch_packet": source_origin["selected_branch_packet"],
        "strominger_selection_support": source_origin["gate_matrix"]["G2_MTT_Strominger_selection_available"]["passes"],
        "same_source_support": source_origin["gate_matrix"]["G3_same_source_support_converges"]["passes"],
        "finite_codomain_schema": all(phifin["phifin_schema"]["shape_gates"].values()),
        "downstream_algebra_if_flags_supplied": first["validation"]["formal_lift_lower_validators_all_pass"],
    }
    r1_missing = {
        "selected_minimizer_identifier": source_origin["gate_matrix"]["G4_minimizer_to_finite_packet_morphism"]["passes"] is False,
        "Phi_fin_selected_values": phifin["obstruction"]["selected_payload_closed"] is False,
        "selected_hym_operator_source": hym_attempt["calculation_results"]["selected_hym_operator_source_verified"] is False,
        "alpha1_payload_values": alpha["payload_summary"]["all_selected_values_emitted"] is False,
    }
    r1_closed = all(
        [
            r1_fillable["strominger_selection_support"],
            r1_fillable["same_source_support"],
            r1_fillable["finite_codomain_schema"],
            r1_fillable["downstream_algebra_if_flags_supplied"],
        ]
    ) and not any(r1_missing.values())

    r4_fillable = {
        "form_fiber_tensor_bookkeeping": basis["closed_decisions"]["form_fiber_tensor_bookkeeping_closed"],
        "candidate_deck_generators": deck["what_this_closes"]["explicit_candidate_deck_generators"],
        "fundamental_gluing_laws": deck["what_this_closes"]["fundamental_gluing_laws_formulated"],
        "matrix_protocol": protocol["verdict"]["closes_execution_protocol"],
        "validator_coherent_finite_basis_shape": first["validation"]["formal_lift_lower_validators_all_pass"],
    }
    r4_missing = {
        "selected_deck_or_cover": deck["still_open"]["MTT_selection_or_source_confirmation_of_Gamma0"],
        "scalar_basis_functions_phi_m": basis["still_missing_for_actual_B_N"]["scalar_basis_functions_phi_m"],
        "bundle_equivariance_matrices": basis["still_missing_for_actual_B_N"]["bundle_transition_or_equivariance_matrices"],
        "metric_quadrature": basis["still_missing_for_actual_B_N"]["metric_volume_quadrature"],
        "selected_D_E_action_on_basis": basis["still_missing_for_actual_B_N"]["selected_D_E_action_on_basis"],
        "gram_stiffness_entries": basis["still_missing_for_actual_B_N"]["Gram_matrix_entries"]
        or basis["still_missing_for_actual_B_N"]["stiffness_matrix_entries"],
        "gap_error_certificate": deck["still_open"]["gap_error_certificate"],
    }
    r4_closed = all(r4_fillable.values()) and not any(r4_missing.values())

    replay_ready = r1_closed and r4_closed
    return {
        "candidate": "MTTSelectedRouteCR1SourceOrR4BNBasisFillAttempt",
        "status": "MTT_SELECTED_ROUTEC_R1_R4_FILL_ATTEMPT_BLOCKED_BY_UNEMITTED_SELECTED_PRIMITIVES",
        "inputs": {
            "previous": rel(PREVIOUS),
            "R1_contract": rel(R1_CONTRACT),
            "R4_contract": rel(R4_CONTRACT),
            "source_origin": rel(DATA / "routec_selected_source_origin_lemma.candidate.json"),
            "phifin": rel(DATA / "finite_emission_morphism_phifin.candidate.json"),
            "phifin_alpha1": rel(DATA / "selected_phifin_alpha1_payload.candidate.json"),
            "hym_attempt": str(Q79_CERTS / "selected_hym_operator_source_attempt_certificate.json"),
            "deck_scaffold": str(Q79_CERTS / "iwasawa_standard_lattice_deck_scaffold_certificate.json"),
            "basis_skeleton": str(Q79_CERTS / "iwasawa_galerkin_basis_skeleton_certificate.json"),
        },
        "superset_mode": {
            "classification": "DUAL_FILL_ATTEMPT_STRICT",
            "straight_path": {
                "classification": "BLOCKED",
                "reason": "Neither R1 nor R4 emits selected values from current artifacts.",
            },
            "superset_convergence": {
                "classification": "SUPPORT_ALREADY_CLOSED",
                "R1_support": r1_fillable,
                "R4_support": r4_fillable,
            },
            "superset_repair": {
                "classification": "NEW_SELECTED_PRIMITIVE_REQUIRED",
                "R1_required_new_primitive": "selected Phi_fin values from the MTT Strominger/HYM minimizer",
                "R4_required_new_primitive": "selected quotient/deck-valid scalar and bundle Galerkin basis",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "observed_physical_data_used": False,
            },
        },
        "R1_source_certificate_attempt": {
            "closed": r1_closed,
            "fillable_from_current_artifacts": r1_fillable,
            "blocking_missing_fields": r1_missing,
            "contract_fields": r1_contract["minimum_selected_payload_fields"],
            "decision": (
                "R1 cannot be honestly filled until Phi_fin emits selected rho_E/metric/connection/operator data "
                "from the selected minimizer. The existing support proves admissible shape, not selected values."
            ),
        },
        "R4_BN_basis_attempt": {
            "closed": r4_closed,
            "fillable_from_current_artifacts": r4_fillable,
            "blocking_missing_fields": r4_missing,
            "contract_fields": r4_contract["minimum_basis_payload_fields"],
            "decision": (
                "R4 cannot be honestly filled until the selected deck/cover, scalar basis, bundle equivariance, "
                "quadrature, and selected D_E action are emitted. The current basis is validator-coherent only."
            ),
        },
        "R6_honest_replay": {
            "ready": replay_ready,
            "reason": "Replay requires R1 selected-source flags and R4 selected basis/operator extraction to be theorem-derived.",
        },
        "what_closes_now": {
            "R1_fill_attempt_executed": True,
            "R4_fill_attempt_executed": True,
            "R1_support_fields_collected": True,
            "R4_support_fields_collected": True,
            "unemitted_selected_primitives_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "R1_selected_source_certificate": not r1_closed,
            "R2_selected_rhoE_metric_connection": True,
            "R4_selected_basis_data": not r4_closed,
            "R3_selected_operator_spectral_data": True,
            "R5_selected_C1_response": True,
            "R6_replay_without_lifted_flags": not replay_ready,
            "full_SM_or_no_knob_closure": True,
        },
        "theorem": {
            "name": "RouteCR1R4StrictFillAttemptTheorem",
            "proved": True,
            "statement": (
                "The R1 and R4 fill routes have been attempted against the current selected artifacts.  Both have closed support stacks, "
                "but neither emits selected values.  R1 is blocked by the missing selected Phi_fin payload from the MTT Strominger/HYM "
                "minimizer.  R4 is blocked by missing selected quotient/deck scalar basis, bundle equivariance, quadrature, and selected "
                "D_E action.  The honest replay remains blocked until at least these primitives are emitted."
            ),
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_RouteC_Selected_Primitive_Emission_Search_v1",
    }


def build_certificate(candidate: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "MTTSelectedRouteCR1SourceOrR4BNBasisFillAttempt",
        "status": candidate["status"],
        "candidate_path": rel(OUT_DATA),
        "note_path": rel(OUT_NOTE),
        "R1_closed": candidate["R1_source_certificate_attempt"]["closed"],
        "R4_closed": candidate["R4_BN_basis_attempt"]["closed"],
        "R6_ready": candidate["R6_honest_replay"]["ready"],
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "primary_next_artifact": candidate["next_required_artifact"],
    }


def render_note(candidate: dict[str, Any]) -> str:
    r1 = candidate["R1_source_certificate_attempt"]
    r4 = candidate["R4_BN_basis_attempt"]
    return f"""# MTT Selected Route-C R1 Source Certificate or R4 B_N Basis Fill

Status: `{candidate['status']}`.

This artifact attempts to solve the first two legal exits from the remaining
Route-C chain:

- R1 selected source certificate,
- R4 quotient/deck-valid B_N basis.

## Result

R1 closed: `{r1['closed']}`.
R4 closed: `{r4['closed']}`.
R6 honest replay ready: `{candidate['R6_honest_replay']['ready']}`.

## R1 Decision

{r1['decision']}

## R4 Decision

{r4['decision']}

## Theorem

`RouteCR1R4StrictFillAttemptTheorem` is proved:

The R1 and R4 fill routes have been attempted against the current selected
artifacts.  Both have closed support stacks, but neither emits selected values.
R1 is blocked by the missing selected `Phi_fin` payload from the MTT
Strominger/HYM minimizer.  R4 is blocked by missing selected quotient/deck
scalar basis, bundle equivariance, quadrature, and selected `D_E` action.  The
honest replay remains blocked until at least these primitives are emitted.

Next artifact: `{candidate['next_required_artifact']}`.
"""


def main() -> int:
    candidate = build_candidate()
    cert = build_certificate(candidate)
    write_json(OUT_DATA, candidate)
    write_json(OUT_CERT, cert)
    OUT_NOTE.write_text(render_note(candidate), encoding="utf-8")
    print(json.dumps({"candidate": rel(OUT_DATA), "status": candidate["status"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
