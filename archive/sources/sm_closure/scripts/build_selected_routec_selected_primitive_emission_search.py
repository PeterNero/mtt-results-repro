"""Search for selected Route-C primitive emissions already present in the repo.

This is a strict audit artifact: it may promote R1/R4 only if current data
actually emits selected Phi_fin values or quotient-valid B_N data.  Support
scaffolds and formal lifted flags are recorded but cannot promote closure.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
OUTPUT = DATA / "selected_routec_selected_primitive_emission_search.candidate.json"
CERT = CERTS / "selected_routec_selected_primitive_emission_search_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_Selected_Primitive_Emission_Search_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def main() -> None:
    fill = load(DATA / "selected_routec_r1_source_or_r4_bn_basis_fill.candidate.json")
    phifin_contract = load(DATA / "selected_phifin_payload_or_bn_basis_emission" / "selected_phifin_payload.emission_contract.json")
    basis_contract = load(DATA / "selected_phifin_payload_or_bn_basis_emission" / "selected_bn_basis.emission_contract.json")
    rho_metric = load(DATA / "selected_routec_strominger_galerkin_solve" / "rhoE_metric.candidate.json")
    spectral = load(DATA / "selected_routec_strominger_galerkin_solve" / "spectral_galerkin_data.candidate.json")
    same_source = load(DATA / "same_source_symmetry_breaking_source.candidate.json")

    selected_deck_map = (
        same_source["superset_mode"]["repair_paths"]["ordered_integral_cech_or_appell_humbert"]
        ["selected_s3_deck_limit"]["selected_deck_map"]
    )
    deck_rank = (
        same_source["superset_mode"]["repair_paths"]["ordered_integral_cech_or_appell_humbert"]
        ["selected_s3_deck_limit"]["selected_s3_active_image_rank_over_F3"]
    )

    phifin_hits = {
        "rhoE_metric_candidate_path": rel(DATA / "selected_routec_strominger_galerkin_solve" / "rhoE_metric.candidate.json"),
        "candidate_kind": rho_metric.get("candidate_kind"),
        "selected_by_mtt": rho_metric.get("selected_by_mtt") is True,
        "selected_values_emitted": phifin_contract["current_status"]["selected_values_emitted"] is True,
        "identity_smoke_rejected": rho_metric.get("candidate_kind") == "identity_rhoE_smoke_unselected",
        "minimum_payload_fields_still_null": all(
            value is None for value in phifin_contract["minimum_selected_payload_fields"].values()
        ),
    }

    basis_hits = {
        "spectral_candidate_path": rel(DATA / "selected_routec_strominger_galerkin_solve" / "spectral_galerkin_data.candidate.json"),
        "selected_source_verified": spectral.get("selected_source_verified") is True,
        "status": spectral.get("status"),
        "selected_deck_map_present": selected_deck_map is not None,
        "selected_deck_rank_over_F3": deck_rank,
        "selected_deck_is_partial_execution_scaffold": deck_rank == 2,
        "required_success_gates_pass": all(basis_contract["required_success_gates"].values()),
        "minimum_basis_payload_fields_still_null": all(
            value is None for value in basis_contract["minimum_basis_payload_fields"].values()
        ),
    }

    formal_lift_status = {
        "path": rel(DATA / "selected_routec_strominger_galerkin_solve" / "formal_lift_diagnostic"),
        "can_validate_downstream_algebra": True,
        "claims_physical_selected_source": False,
        "promotion_allowed": False,
    }

    r1_promotes = (
        phifin_hits["selected_by_mtt"]
        and phifin_hits["selected_values_emitted"]
        and not phifin_hits["minimum_payload_fields_still_null"]
    )
    r4_promotes = (
        basis_hits["selected_source_verified"]
        and basis_hits["required_success_gates_pass"]
        and not basis_hits["minimum_basis_payload_fields_still_null"]
    )
    r6_ready = r1_promotes and r4_promotes

    candidate = {
        "candidate": "MTTSelectedRouteCSelectedPrimitiveEmissionSearch",
        "status": "MTT_SELECTED_ROUTEC_PRIMITIVE_EMISSION_SEARCH_EXECUTED_NO_LEGAL_EMISSION_FOUND",
        "inputs": {
            "strict_fill_attempt": fill["candidate"],
            "phifin_contract": rel(DATA / "selected_phifin_payload_or_bn_basis_emission" / "selected_phifin_payload.emission_contract.json"),
            "basis_contract": rel(DATA / "selected_phifin_payload_or_bn_basis_emission" / "selected_bn_basis.emission_contract.json"),
        },
        "superset_mode": {
            "classification": "SUPERSET_CONVERGENCE_AUDIT_WITH_STRAIGHT_PROMOTION_TEST",
            "straight_path": {
                "classification": "BLOCKED",
                "R1_promotes": r1_promotes,
                "R4_promotes": r4_promotes,
                "R6_ready": r6_ready,
            },
            "superset_convergence": {
                "selected_deck_map_found": basis_hits["selected_deck_map_present"],
                "selected_deck_rank_over_F3": deck_rank,
                "formal_lift_algebra_available": formal_lift_status["can_validate_downstream_algebra"],
                "support_stacks_closed_from_previous_artifact": True,
            },
            "superset_repair": {
                "classification": "EMIT_SELECTED_PRIMITIVES_FROM_SOURCE",
                "next_required_object": "selected non-identity projective/twisted rho_E plus quotient-valid non-invariant Galerkin B_N from the same q79/F,m=1 branch",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "observed_physical_data_used": False,
            },
        },
        "search_results": {
            "Phi_fin_payload": phifin_hits,
            "B_N_basis": basis_hits,
            "formal_lift_diagnostic": formal_lift_status,
        },
        "what_closes_now": {
            "primitive_search_executed": True,
            "selected_deck_scaffold_identified": True,
            "identity_rhoE_rejected_as_selected_payload": True,
            "formal_lift_rejected_as_proof": True,
            "R1_R4_not_promoted_by_existing_artifacts": True,
        },
        "what_remains_open": {
            "R1_selected_source_certificate": not r1_promotes,
            "R2_selected_rhoE_metric_connection": True,
            "R3_selected_operator_spectral_data": True,
            "R4_selected_basis_data": not r4_promotes,
            "R5_selected_C1_response": True,
            "R6_replay_without_lifted_flags": not r6_ready,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_RouteC_NonIdentity_RhoE_and_BN_Construction_v1",
        "theorem": {
            "name": "SelectedPrimitiveEmissionSearchTheorem",
            "proved": True,
            "statement": (
                "The current repository was searched for legal selected Route-C primitive emissions. "
                "It contains a selected S3 deck scaffold and diagnostic formal-lift algebra, but no "
                "selected Phi_fin payload values and no quotient-valid B_N basis payload. Therefore "
                "R1 through R6 cannot be honestly closed from existing artifacts."
            ),
        },
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": candidate["status"],
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        f"""# MTT Selected Route-C Selected Primitive Emission Search

Status: `{candidate['status']}`

The strict search looked for legal selected primitive emissions already present
in the repo.

## Result

- `Phi_fin` selected payload: not emitted.
- `B_N` quotient/deck-valid basis payload: not emitted.
- selected S3 deck scaffold: present, but only as a partial execution scaffold.
- formal-lift algebra: useful diagnostic, not proof.

This closes the question of whether R1-R6 were blocked only by missing wiring.
They are not.  Existing artifacts supply support and validator shapes, but do
not emit the selected non-identity `rho_E`, metric/connection, operator action,
quadrature, non-invariant basis, gap certificate, or C1 response required for
honest replay.

## Next

Build `MTT_Selected_RouteC_NonIdentity_RhoE_and_BN_Construction_v1`: construct
the selected non-identity projective/twisted `rho_E` and quotient-valid
non-invariant Galerkin `B_N` from the same q79/F,m=1 branch.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": candidate["status"]}, indent=2))


if __name__ == "__main__":
    main()
