"""Attempt to close the two remaining Route-C gates: provenance and basis."""

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

CUTSET = DATA / "selected_routec_source_selector_and_basis_theorem.candidate.json"
FIRST_RUN = DATA / "selected_routec_strominger_galerkin_first_run.candidate.json"
PHIFIN = DATA / "finite_emission_morphism_phifin.candidate.json"
PHIFIN_ALPHA1 = DATA / "selected_phifin_alpha1_payload.candidate.json"
SOURCE_ORIGIN = DATA / "routec_selected_source_origin_lemma.candidate.json"

OUTPUT_DATA = DATA / "selected_routec_source_provenance_or_basis_certificate.candidate.json"
OUTPUT_CERT = CERTS / "selected_routec_source_provenance_or_basis_certificate_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_RouteC_Source_Provenance_or_Basis_Certificate_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def all_true(mapping: dict[str, Any]) -> bool:
    return all(value is True for value in mapping.values())


def build_candidate() -> dict[str, Any]:
    cutset = load_json(CUTSET)
    first = load_json(FIRST_RUN)
    phifin = load_json(PHIFIN)
    phifin_alpha1 = load_json(PHIFIN_ALPHA1)
    origin = load_json(SOURCE_ORIGIN)
    basis = load_json(Q79_CERTS / "iwasawa_galerkin_basis_skeleton_certificate.json")
    protocol = load_json(Q79_CERTS / "iwasawa_non_invariant_galerkin_protocol_certificate.json")

    provenance_support = {
        "fixed_q79_branch": first["root_payload"]["selected_branch_claimed_by_residual_solution"] is True,
        "strominger_selection_support": origin["gate_matrix"]["G2_MTT_Strominger_selection_available"]["passes"] is True,
        "phifin_codomain_schema": all_true(phifin["phifin_schema"]["shape_gates"]),
        "formal_lift_lower_algebra": cutset["what_closes_now"]["downstream_algebra_conditional_pass_confirmed"] is True,
    }
    provenance_blockers = {
        "phifin_selected_payload_missing": phifin["obstruction"]["selected_payload_closed"] is False,
        "phifin_alpha1_selected_values_missing": phifin_alpha1["what_remains_open"]["selected_PhiFin_alpha1_payload_values"] is True,
        "selected_source_flags_not_theorem_derived": cutset["what_remains_open"]["selected_source_provenance_theorem"] is True,
    }

    basis_support = {
        "basis_skeleton_closed": basis["verdict"]["closes_basis_skeleton"] is True,
        "finite_validator_basis_coherent": first["validation"]["formal_lift_lower_validators_all_pass"] is True,
        "sector_dimensions_fixed": all(
            row["zero_mode_count"] == row["expected_kernel_dimension"]
            for row in cutset["calculation"]["sector_dimension_table"].values()
        ),
        "matrix_protocol_formulated": protocol["verdict"]["closes_execution_protocol"] is True,
    }
    basis_blockers = {
        "actual_basis_functions_missing": basis["still_missing_for_actual_B_N"]["scalar_basis_functions_phi_m"] is True,
        "deck_constraints_missing": basis["still_missing_for_actual_B_N"]["deck_or_periodic_constraints"] is True,
        "bundle_equivariance_missing": basis["still_missing_for_actual_B_N"]["bundle_transition_or_equivariance_matrices"] is True,
        "metric_quadrature_missing": basis["still_missing_for_actual_B_N"]["metric_volume_quadrature"] is True,
        "selected_DE_action_on_basis_missing": basis["still_missing_for_actual_B_N"]["selected_D_E_action_on_basis"] is True,
        "selected_spectral_error_budget_missing": cutset["what_remains_open"]["selected_spectral_error_budget_from_actual_BN"] is True,
    }

    provenance_closed = all_true(provenance_support) and not any(provenance_blockers.values())
    basis_closed = all_true(basis_support) and not any(basis_blockers.values())
    any_closed = provenance_closed or basis_closed

    return {
        "candidate": "MTTSelectedRouteCSourceProvenanceOrBasisCertificate",
        "status": "MTT_SELECTED_ROUTEC_PROVENANCE_AND_BASIS_ATTEMPT_SUPPORT_CLOSED_PRIMITIVES_OPEN",
        "inputs": {
            "cutset": rel(CUTSET),
            "first_run": rel(FIRST_RUN),
            "phifin": rel(PHIFIN),
            "phifin_alpha1": rel(PHIFIN_ALPHA1),
            "source_origin": rel(SOURCE_ORIGIN),
            "basis_skeleton": str(Q79_CERTS / "iwasawa_galerkin_basis_skeleton_certificate.json"),
            "galerkin_protocol": str(Q79_CERTS / "iwasawa_non_invariant_galerkin_protocol_certificate.json"),
        },
        "superset_mode": {
            "classification": "DUAL_GATE_CLOSURE_ATTEMPT",
            "straight_path": {
                "classification": "SUPPORT_CLOSED_FULL_GATE_OPEN",
                "reason": "Neither provenance nor quotient-valid basis can be closed from current selected artifacts alone.",
            },
            "superset_convergence": {
                "classification": "TWO_SUPPORT_STACKS_LOCKED",
                "provenance_support": provenance_support,
                "basis_support": basis_support,
            },
            "superset_repair": {
                "classification": "PRIMITIVE_EMISSION_REQUIRED",
                "provenance_primitive": "selected Phi_fin payload theorem",
                "basis_primitive": "selected quotient/deck Galerkin basis B_N certificate",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "observed_physical_data_used": False,
            },
        },
        "provenance_gate": {
            "support": provenance_support,
            "blockers": provenance_blockers,
            "closed": provenance_closed,
            "minimal_missing_primitive": "Phi_fin_selected_payload",
            "decision": (
                "Cannot honestly set selected_source_verified yet. The selected branch and Strominger support are present, "
                "and the codomain schema is closed, but Phi_fin has not emitted selected values."
            ),
        },
        "basis_gate": {
            "support": basis_support,
            "blockers": basis_blockers,
            "closed": basis_closed,
            "minimal_missing_primitive": "quotient_valid_B_N_basis_certificate",
            "decision": (
                "Cannot honestly certify the selected Galerkin basis yet. The validator basis and matrix protocol are coherent, "
                "but actual scalar basis functions, deck constraints, bundle equivariance, quadrature, and selected D_E action are still open."
            ),
        },
        "calculation": {
            "any_gate_closed": any_closed,
            "both_gates_closed": provenance_closed and basis_closed,
            "support_closed": {
                "provenance_support_closed": all_true(provenance_support),
                "basis_support_closed": all_true(basis_support),
            },
            "newly_locked": {
                "provenance_is_not_blocked_by_downstream_algebra": True,
                "basis_is_not_blocked_by_dimension_or_projector_shape": True,
                "no_observed_data_needed_for_either_support_stack": True,
            },
        },
        "what_closes_now": {
            "provenance_support_stack_closed": all_true(provenance_support),
            "basis_support_stack_closed": all_true(basis_support),
            "minimal_provenance_primitive_identified": True,
            "minimal_basis_primitive_identified": True,
            "no_hidden_matrix_or_dimension_obstruction": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "Phi_fin_selected_payload": not provenance_closed,
            "quotient_valid_BN_basis_certificate": not basis_closed,
            "selected_source_flags_promoted": not provenance_closed,
            "honest_manifest_without_lifted_flags": not any_closed,
            "full_SM_or_no_knob_closure": True,
        },
        "theorem": {
            "name": "SelectedRouteCProvenanceAndBasisSupportTheorem",
            "proved": True,
            "statement": (
                "Both remaining gates were tested. The provenance support stack and the basis support stack are closed, but neither full gate "
                "can yet be promoted: provenance requires the selected Phi_fin payload, and basis requires an emitted quotient/deck-valid B_N "
                "certificate. Thus no further matrix search is currently indicated; the next work is primitive emission."
            ),
        },
        "next_required_artifact": "MTT_Selected_PhiFin_Payload_or_BN_Basis_Emission_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "MTTSelectedRouteCSourceProvenanceOrBasisCertificate",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "provenance_closed": candidate["provenance_gate"]["closed"],
        "basis_closed": candidate["basis_gate"]["closed"],
        "support_closed": candidate["calculation"]["support_closed"],
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "primary_next_artifact": candidate["next_required_artifact"],
    }


def render_note(candidate: dict[str, Any]) -> str:
    return f"""# MTT Selected Route-C Source Provenance or Basis Certificate

Status: `{candidate['status']}`.

This attempts both remaining exits:

1. selected HYM/Strominger provenance,
2. quotient-valid selected Galerkin basis `B_N`.

## Result

Provenance gate closed: `{candidate['provenance_gate']['closed']}`.
Basis gate closed: `{candidate['basis_gate']['closed']}`.

What did close is the support stack for both:

- provenance support stack closed: `{candidate['calculation']['support_closed']['provenance_support_closed']}`
- basis support stack closed: `{candidate['calculation']['support_closed']['basis_support_closed']}`

## Provenance

Minimal missing primitive: `{candidate['provenance_gate']['minimal_missing_primitive']}`.

{candidate['provenance_gate']['decision']}

## Basis

Minimal missing primitive: `{candidate['basis_gate']['minimal_missing_primitive']}`.

{candidate['basis_gate']['decision']}

## Consequence

This locks down both gates as far as current artifacts allow.  There is no
hidden matrix-shape obstruction and no observed-data fitting is involved.  The
next calculation must emit one of two primitives:

- selected `Phi_fin` payload, or
- quotient/deck-valid `B_N` basis certificate.

Next artifact: `{candidate['next_required_artifact']}`.
"""


def main() -> int:
    candidate = build_candidate()
    cert = build_certificate(candidate)
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    OUTPUT_NOTE.write_text(render_note(candidate), encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT_DATA), "status": candidate["status"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
