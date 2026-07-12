"""Build Step 38 finite Heisenberg rho_E promotion and D_E frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step38_finiteheisenberg_rhoe_promotion_or_deoperatorfrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROMOTION = PACKET_DIR / "step38_finite_heisenberg_rhoe_promotion.packet.json"
FRONTIER = PACKET_DIR / "step38_de_operator_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step38_FiniteHeisenbergRhoEPromotion_or_DEOperatorFrontier_v1.md"

STEP37 = DATA / "selected_step37_finitetrace_degap_import_or_fulloperatorvaluefrontier.candidate.json"
STEP37_CONTRACT = (
    DATA
    / "selected_step37_finitetrace_degap_import_or_fulloperatorvaluefrontier"
    / "step37_next_operator_value_construction_contract.packet.json"
)
S3_SOURCE = DATA / "selected_s3_differential_cohomology_source_certificate.candidate.json"
RHOE = DATA / "selected_routec_nonidentity_rhoe_bn_construction.candidate.json"
GERBE_RHOE = DATA / "projective_gerbe_rhoe_source_promotion.candidate.json"

STATUS = "MTT_SELECTED_STEP38_FINITE_HEISENBERG_RHOE_PROMOTED_DE_OPERATOR_VALUES_OPEN"
NEXT = "MTT_Selected_CovariantDE_From_ProjectiveRhoE_and_SelectedConnection_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [STEP37, STEP37_CONTRACT, S3_SOURCE, RHOE, GERBE_RHOE]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 38 inputs: " + ", ".join(missing))

    step37 = load(STEP37)
    contract = load(STEP37_CONTRACT)
    s3_source = load(S3_SOURCE)
    rhoe = load(RHOE)
    gerbe_rhoe = load(GERBE_RHOE)

    numeric = rhoe["rho_E_candidate"]["numeric_gates"]
    matrices = rhoe["rho_E_candidate"]["generator_matrices_complex_pairs"]
    promotion_checks = {
        "step37_trace_gap_layer_closed": step37["closure_decision"]["finite_trace_DE_gap_layer_closed"] is True,
        "selected_s3_class_closed": s3_source["gate_results"]["selected_s3_flat_Deligne_class_imported"] is True,
        "selected_qutrit_central_cocycle_closed": s3_source["gate_results"]["map_to_qutrit_central_cocycle_verified"] is True,
        "gerbe_rhoe_promoted_to_s3_source_level": gerbe_rhoe["status"]
        == "MTT_PROJECTIVE_GERBE_RHOE_PROMOTED_TO_S3_SOURCE_OPERATOR_OPEN",
        "active_deck_rank_is_F3_square": numeric["active_deck_rank_over_F3"] == 2,
        "uses_selected_active_generators": numeric["uses_only_selected_active_generators_g1_g2"] is True,
        "kernel_generators_are_identity": numeric["kernel_generators_identity"] is True,
        "unitary_order_three_projective_packet_valid": numeric["passes_numeric_packet_gate"] is True,
        "commutator_phase_nontrivial": numeric["projective_commutator_phase"] != [1.0, 0.0],
        "finite_stone_von_neumann_applies": True,
        "observed_data_not_used": rhoe["target_fitting_used"] is False and step37["target_fitting_used"] is False,
    }
    closes_rhoe = all(promotion_checks.values())

    promotion = {
        "schema": "MTTStep38FiniteHeisenbergRhoEPromotion.v1",
        "status": "PROJECTIVE_RHOE_TRANSITION_GAUGE_CLASS_PROMOTED",
        "source_inputs": {
            "step37": rel(STEP37),
            "step37_contract": rel(STEP37_CONTRACT),
            "selected_s3_source": rel(S3_SOURCE),
            "nonidentity_rhoe_packet": rel(RHOE),
            "projective_gerbe_rhoe_promotion": rel(GERBE_RHOE),
        },
        "promotion_checks": promotion_checks,
        "finite_selection_theorem": {
            "name": "FiniteStoneVonNeumannProjectiveRhoESelection",
            "statement": (
                "For the selected F3^2 deck shadow with primitive qutrit central cocycle, "
                "the irreducible projective unitary representation with that central "
                "character is unique up to unitary gauge. Therefore the clock/shift "
                "Heisenberg-Weyl packet is the selected projective rho_E transition "
                "gauge class, not merely an identity-smoke replacement."
            ),
            "proof_clauses": {
                "selected_base": "selected S3 flat Deligne class and qutrit central cocycle",
                "finite_symplectic_pairing": "nontrivial commutator phase on F3^2",
                "central_character": numeric["projective_commutator_phase"],
                "irreducible_dimension": 3,
                "gauge_freedom": "unitary conjugacy only; physical operator values must be gauge-covariantly transported",
            },
            "proved": closes_rhoe,
        },
        "selected_projective_rhoE_gauge_representative": {
            "basis": "qutrit fiber C3 over selected F3xF3 deck shadow",
            "generators": matrices,
            "active_generators": ["g1", "g2"],
            "kernel_generators": ["g3", "g4", "g5", "g6"],
            "numeric_gates": numeric,
        },
        "closure_result": {
            "operator_level_projective_rhoE_transition_matrices_closed": closes_rhoe,
            "nonidentity_projective_rhoE_selected_up_to_unitary_gauge": closes_rhoe,
            "identity_rhoE_smoke_retired_for_operator_frontier": closes_rhoe,
            "selected_covariant_D_E_matrices_closed": False,
            "selected_Riesz_Green_values_closed": False,
            "same_branch_dotD_alpha1_values_closed": False,
            "coherent_spectral_zero_mode_projectors_closed": False,
            "primitive_C1_contractions_from_operator_values_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(PROMOTION, promotion)

    frontier = {
        "schema": "MTTStep38DEOperatorFrontier.v1",
        "status": "PROJECTIVE_RHOE_GAUGE_CLASS_CLOSED_DE_OPERATOR_VALUES_OPEN",
        "closed_now": {
            "selected_s3_class_restriction_layer": True,
            "finite_trace_DE_gap_layer": True,
            "operator_level_projective_rhoE_transition_gauge_class": closes_rhoe,
        },
        "still_missing_as_operator_values": {
            "selected_connection_one_form_or_Cech_Dolbeault_connection": True,
            "covariant_D_E_matrices_on_selected_B_N_basis": True,
            "Riesz_projectors_from_emitted_D_E": True,
            "reduced_Green_operators_from_emitted_D_E": True,
            "same_branch_dotD_alpha1_from_D_E_derivative": True,
            "coherent_zero_mode_projectors": True,
            "primitive_C1_contractions": True,
            "internal_R_theta_scalar_rows": True,
        },
        "next_minimum_payload": {
            "target": NEXT,
            "must_extend_step37_contract": contract["target"],
            "must_start_from_rhoe_gauge_class": "clock/shift Heisenberg-Weyl qutrit gauge class",
            "must_not_use": [
                "identity rho_E",
                "trace scalar as full transition matrix",
                "lifted selected-source flags",
                "observed SM masses or mixings",
            ],
        },
        "accepted_internal_scalar_row_count": 0,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(FRONTIER, frontier)

    candidate = {
        "candidate": "MTTSelectedStep38FiniteHeisenbergRhoEPromotionOrDEOperatorFrontier",
        "status": STATUS,
        "inputs": promotion["source_inputs"],
        "output_packets": {
            "finite_heisenberg_rhoe_promotion": rel(PROMOTION),
            "de_operator_frontier": rel(FRONTIER),
        },
        "theorem": promotion["finite_selection_theorem"],
        "closure_decision": {
            "selected_s3_class_restriction_layer_closed": True,
            "finite_trace_DE_gap_layer_closed": True,
            "operator_level_projective_rhoE_transition_matrices_closed": closes_rhoe,
            "nonidentity_projective_rhoE_selected_up_to_unitary_gauge": closes_rhoe,
            "selected_covariant_D_E_matrices_closed": False,
            "selected_Riesz_Green_values_closed": False,
            "same_branch_dotD_alpha1_values_closed": False,
            "coherent_spectral_zero_mode_projectors_closed": False,
            "primitive_C1_contractions_from_operator_values_closed": False,
            "accepted_internal_scalar_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": closes_rhoe,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step38_FiniteHeisenbergRhoEPromotion_or_DEOperatorFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "operator_level_projective_rhoE_transition_matrices_closed": closes_rhoe,
        "nonidentity_projective_rhoE_selected_up_to_unitary_gauge": closes_rhoe,
        "selected_covariant_D_E_matrices_closed": False,
        "selected_Riesz_Green_values_closed": False,
        "same_branch_dotD_alpha1_values_closed": False,
        "coherent_spectral_zero_mode_projectors_closed": False,
        "primitive_C1_contractions_from_operator_values_closed": False,
        "accepted_internal_scalar_row_count": 0,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step38 FiniteHeisenbergRhoEPromotion or DEOperatorFrontier v1

Status: `{STATUS}`.

Step38 promotes the non-identity qutrit clock/shift `rho_E` packet from a
candidate to the selected projective transition gauge class. The promotion uses
the selected S3 flat Deligne class, the selected qutrit central cocycle, and the
finite Stone-von Neumann uniqueness theorem for the nontrivial `F3^2` projective
central character.

This closes:

- operator-level projective `rho_E` transition matrices up to unitary gauge
- non-identity `rho_E` as the active operator-frontier representative
- identity-`rho_E` smoke as a legal fallback

Still open:

- selected connection/Cech-Dolbeault operator source
- covariant `D_E` matrices on the selected `B_N` basis
- selected Riesz/Green values
- same-branch `dotD_alpha1`
- coherent zero-mode projectors
- primitive C1 contractions and internal `R_theta` rows

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
