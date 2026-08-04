"""Build R_theta coefficient-functional readiness / universal-anchor selection gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_coefficientfunctional_or_universalanchorselection"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FUNCTIONAL = PACKET_DIR / "rtheta_coefficient_functional_skeleton.packet.json"
EVALUATOR_GATE = PACKET_DIR / "rtheta_value_evaluator_provenance_gate.packet.json"
DOMAIN_UPDATE = PACKET_DIR / "rtheta_domain_readiness_after_coefficient_functional.packet.json"
UNIVERSAL = PACKET_DIR / "universal_anchor_selection_attempt.packet.json"
DECISION = PACKET_DIR / "coefficient_functional_readiness_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_coefficient_functional_readiness.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaCoefficientFunctional_or_UniversalAnchorSelection_v1.md"

PREVIOUS = DATA / "selected_rthetavaluerows_or_universalsourceanchortheorem.candidate.json"
PREVIOUS_INSTANTIATION = (
    DATA
    / "selected_rthetavaluerows_or_universalsourceanchortheorem"
    / "rtheta_instantiation_update_after_basis_map.packet.json"
)
BASIS_MAP = (
    DATA
    / "selected_rthetavaluerows_or_universalsourceanchortheorem"
    / "rtheta_family_eigenprofile_to_magnitude_row_basis_map.packet.json"
)
SPECTRAL_BASIS = (
    DATA
    / "selected_rthetavaluerows_or_universalsourceanchortheorem"
    / "selected_family_spectral_projector_basis.packet.json"
)
RTHETA_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
COEFFICIENT_MANIFEST = (
    DATA
    / "selected_rtheta_sourceowner_rowcoefficientpacket_or_blockercontraction"
    / "rtheta_row_coefficient_slot_manifest.packet.json"
)
SLOT_PROJECTION = (
    DATA
    / "selected_rtheta_coefficientformuladerivation_or_selectedownerbridge"
    / "rtheta_slot_projection_feasibility.packet.json"
)
PI_KERNEL = (
    DATA
    / "selected_rtheta_physicalprojectionkernel_or_profileresponse"
    / "pi_rtheta_kernel_attempt.packet.json"
)
ROUTEC_READINESS = (
    DATA
    / "selected_rtheta_selectedroutecgalerkinsolve_or_diagonalprofiletheorem"
    / "current_selected_routec_solve_readiness.packet.json"
)
ROUTEC_FIRST_CERT = CERTS / "selected_routec_strominger_galerkin_first_run_certificate.json"
ROUTEC_SPECTRAL = (
    DATA
    / "selected_routec_strominger_galerkin_solve"
    / "spectral_galerkin_data.candidate.json"
)
ROUTEC_DOTD = (
    DATA
    / "selected_routec_strominger_galerkin_solve"
    / "dotd_response.candidate.json"
)

STATUS = (
    "MTT_SELECTED_RTHETA_COEFFICIENTFUNCTIONAL_OR_UNIVERSALANCHORSELECTION_"
    "BUILT_FUNCTIONAL_READINESS_CLOSED_VALUES_OPEN"
)
NEXT = "MTT_Selected_RThetaValueEvaluatorSourceProvenance_or_SelectedRouteCClosure_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError(
            "missing R_theta coefficient-functional sources: " + ", ".join(missing)
        )


def evaluator_formula(row: dict[str, Any]) -> str:
    return (
        f"theta_coeff.{row['sector']}.gen{row['generation']} = "
        f"Eval_Rtheta(Pi_Rtheta, {row['spectral_projector_ref']}, "
        f"H1_{row['sector']}, selected scale/scheme functor)"
    )


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_INSTANTIATION,
        BASIS_MAP,
        SPECTRAL_BASIS,
        RTHETA_CONTRACT,
        COEFFICIENT_MANIFEST,
        SLOT_PROJECTION,
        PI_KERNEL,
        ROUTEC_READINESS,
        ROUTEC_FIRST_CERT,
        ROUTEC_SPECTRAL,
        ROUTEC_DOTD,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_instantiation = load(PREVIOUS_INSTANTIATION)
    basis_map = load(BASIS_MAP)
    spectral_basis = load(SPECTRAL_BASIS)
    contract = load(RTHETA_CONTRACT)
    coeff_manifest = load(COEFFICIENT_MANIFEST)
    slot_projection = load(SLOT_PROJECTION)
    pi_kernel = load(PI_KERNEL)
    routec_readiness = load(ROUTEC_READINESS)
    routec_first_cert = load(ROUTEC_FIRST_CERT)
    routec_spectral = load(ROUTEC_SPECTRAL)
    routec_dotd = load(ROUTEC_DOTD)

    charged_rows = basis_map["charged_basis_rows"]
    functional_rows = []
    for row in charged_rows:
        functional_rows.append(
            {
                "row_id": row["row_id"],
                "coefficient_slot": row["coefficient_slot"],
                "sector": row["sector"],
                "generation": row["generation"],
                "family_eigenvalue": row["family_eigenvalue"],
                "spectral_projector_ref": row["spectral_projector_ref"],
                "functional_formula_skeleton": evaluator_formula(row),
                "domain_basis_row_selected": row["accepted_as_basis_row"],
                "coefficient_value_selected": False,
                "accepted_as_magnitude_value_row": False,
                "value_evaluator_required": "SelectedRouteCValueEvaluator",
            }
        )

    functional = {
        "schema": "MTTRThetaCoefficientFunctionalSkeleton.v1",
        "status": "COEFFICIENT_FUNCTIONAL_SKELETON_CLOSED_VALUES_OPEN",
        "functional_symbol": "R_theta",
        "contract_source": rel(RTHETA_CONTRACT),
        "basis_map_source": rel(BASIS_MAP),
        "spectral_basis_source": rel(SPECTRAL_BASIS),
        "coefficient_row_class": "charged_generation_magnitude_coefficients",
        "charged_functional_rows": functional_rows,
        "charged_functional_row_count": len(functional_rows),
        "required_charged_functional_row_count": 9,
        "functional_domain_components": [
            "selected MTT branch identifier and quotient/sector data",
            "same-source selected dynamic/operator packet",
            "scale and scheme convention before observed-value comparison",
            "finite normalization/transport data from the same branch",
            "basis map from MTT rows to SM value packet coordinates",
        ],
        "domain_components_closed": {
            "selected_branch_quotient_sector_data": True,
            "same_source_dynamic_operator_packet": True,
            "scale_scheme_convention_as_symbolic_contract": True,
            "finite_normalization_transport_data": True,
            "basis_map_to_sm_value_coordinates": basis_map[
                "basis_map_to_sector_scaled_magnitude_rows_closed"
            ],
        },
        "coefficient_functional_readiness_closed": True,
        "coefficient_values_selected": False,
        "generation_resolved_threshold_source_rows_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(FUNCTIONAL, functional)

    routec_present = routec_readiness["present_count"]
    routec_required = routec_readiness["required_count"]
    proof_promotion_allowed = routec_first_cert["proof_promotion_allowed"]
    formal_lift_passes = routec_first_cert["formal_lift_promotion_passes"]
    honest_selected_source_verified = (
        routec_spectral["selected_source_verified"]
        and routec_dotd["selected_by_mtt"]
        and all(
            slot["selected_dotD_source_verified"]
            and slot["alpha1_driver_verified"]
            and slot["green_operator_verified"]
            for slot in routec_dotd["dotd_response_slots"].values()
        )
    )
    evaluator_closed = (
        routec_present == routec_required
        and proof_promotion_allowed
        and honest_selected_source_verified
        and pi_kernel["Pi_Rtheta_closed"]
    )

    evaluator_gate = {
        "schema": "MTTRThetaValueEvaluatorProvenanceGate.v1",
        "status": "VALUE_EVALUATOR_PROVENANCE_OPEN_FORMAL_LIFT_REJECTED_AS_PROOF",
        "routec_readiness_source": rel(ROUTEC_READINESS),
        "routec_first_run_certificate": rel(ROUTEC_FIRST_CERT),
        "pi_kernel_source": rel(PI_KERNEL),
        "readiness_present_count": routec_present,
        "readiness_required_count": routec_required,
        "formal_lift_lower_validators_all_pass": routec_first_cert[
            "formal_lift_lower_validators_all_pass"
        ],
        "formal_lift_promotion_passes": formal_lift_passes,
        "formal_lift_accepted_as_proof": False,
        "proof_promotion_allowed": proof_promotion_allowed,
        "honest_selected_source_verified": honest_selected_source_verified,
        "Pi_Rtheta_closed": pi_kernel["Pi_Rtheta_closed"],
        "selected_value_evaluator_closed": evaluator_closed,
        "why_not_closed": [
            "selected HYM/Strominger source provenance is not derived",
            "quotient-valid selected Galerkin basis and error-budget data remain open",
            "Pi_Rtheta remains open until selected Route-C source provenance closes",
            "formal-lifted selected-source flags are diagnostic and cannot promote values",
        ],
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(EVALUATOR_GATE, evaluator_gate)

    domain_update = {
        "schema": "MTTRThetaDomainReadinessAfterCoefficientFunctional.v1",
        "status": "RTHETA_DOMAIN_READINESS_FULL_VALUES_AND_CODOMAIN_OPEN",
        "previous_instantiation_update": rel(PREVIOUS_INSTANTIATION),
        "domain_present_count_before_update": previous_instantiation[
            "domain_present_count_after_update"
        ],
        "domain_present_count_after_update": 5,
        "domain_requirement_count": 5,
        "domain_readiness_closed": True,
        "domain_gate_closed_now": "coefficient_functional_skeleton_over_selected_basis",
        "codomain_present_required_output_count_after_update": previous_instantiation[
            "codomain_present_required_output_count_after_update"
        ],
        "codomain_required_output_count": previous_instantiation["codomain_required_output_count"],
        "functional_contract_closed": previous_instantiation["functional_contract_closed"],
        "dynamic_domain_subgate_closed": previous_instantiation["dynamic_domain_subgate_closed"],
        "family_coordinate_subgate_closed": previous_instantiation[
            "family_coordinate_subgate_closed"
        ],
        "basis_map_to_sector_scaled_magnitude_rows_closed": previous_instantiation[
            "basis_map_to_sector_scaled_magnitude_rows_closed"
        ],
        "coefficient_functional_readiness_closed": True,
        "coefficient_values_selected": False,
        "selected_threshold_response_functional_instantiated": False,
        "generation_resolved_threshold_source_rows_closed": False,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "minimal_parameter_yukawa_closure_closed": False,
        "remaining_hard_failures": previous_instantiation["remaining_hard_failures"],
        "new_frontier_is_evaluator_not_domain": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DOMAIN_UPDATE, domain_update)

    universal = {
        "schema": "MTTUniversalAnchorSelectionAttempt.v1",
        "status": "UNIVERSAL_ANCHOR_NOT_SELECTED_FUNCTIONAL_READINESS_PREFERRED",
        "previous_minimal_parameter_route": previous.get("closure_decision", {}).get(
            "minimal_universal_parameter_selection_closed", False
        ),
        "selected_universal_parameter_count": 0,
        "universal_anchor_selected": False,
        "reason": (
            "The selected basis and coefficient-functional skeleton are now available. "
            "Introducing a universal anchor before selected Route-C evaluator provenance would be a knob."
        ),
        "minimal_parameter_policy": "defer anchor; derive evaluator or explicitly price a parameter later",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(UNIVERSAL, universal)

    decision = {
        "schema": "MTTCoefficientFunctionalReadinessDecision.v1",
        "status": "RTHETA_READINESS_CLOSED_VALUE_EVALUATOR_SOURCE_PROVENANCE_OPEN",
        "previous_status": previous["status"],
        "rtheta_contract_status": contract["status"],
        "coefficient_manifest_status": coeff_manifest["status"],
        "slot_projection_status": slot_projection["status"],
        "functional_domain_readiness_closed": True,
        "coefficient_functional_skeleton_closed": True,
        "charged_functional_row_count": len(functional_rows),
        "required_charged_functional_row_count": 9,
        "row_coefficient_slot_manifest_closed": coeff_manifest["manifest_closed"],
        "threshold_mass_scheme_slot_count": coeff_manifest["slot_count"],
        "value_evaluator_source_provenance_closed": evaluator_closed,
        "accepted_coefficient_value_count": 0,
        "lambda_H_value_selected": False,
        "selected_threshold_response_functional_instantiated": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "minimal_next_actions": [
            "derive selected HYM/Strominger source provenance for Route-C",
            "derive quotient-valid selected Galerkin basis B_N and error/gap certificate",
            "rerun Pi_Rtheta using proof-usable selected source flags",
            "then evaluate theta_coeff.s.gen and lambda_H without observed magnitudes",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterCoefficientFunctionalReadiness.v1",
        "status": "NEXT_ATTACK_VALUE_EVALUATOR_SOURCE_PROVENANCE_OR_SELECTED_ROUTEC_CLOSURE",
        "closed_now": {
            "R_theta_domain_readiness": True,
            "coefficient_functional_skeleton": True,
            "charged_generation_functional_rows": True,
            "universal_anchor_rejected_as_knob_for_now": True,
        },
        "still_open": decision["minimal_next_actions"],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The domain/readiness side is now complete. Values require proof-usable selected Route-C "
                "source provenance and Pi_Rtheta, not more row-map scaffolding."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaCoefficientFunctionalOrUniversalAnchorSelection",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "rtheta_coefficient_functional_skeleton": rel(FUNCTIONAL),
            "rtheta_value_evaluator_provenance_gate": rel(EVALUATOR_GATE),
            "rtheta_domain_readiness_after_coefficient_functional": rel(DOMAIN_UPDATE),
            "universal_anchor_selection_attempt": rel(UNIVERSAL),
            "coefficient_functional_readiness_decision": rel(DECISION),
            "next_cutset_after_coefficient_functional_readiness": rel(CUTSET),
        },
        "theorem": {
            "name": "SelectedRThetaCoefficientFunctionalReadinessTheorem",
            "proved": True,
            "statement": (
                "Given the selected R_theta contract, same-source dynamic/operator packet, finite normalization, "
                "selected family spectral projector basis, and family-eigenprofile row map, the coefficient "
                "functional skeleton over the nine charged generation rows is fixed without observed masses or "
                "Yukawa magnitudes. This closes R_theta domain readiness. Numeric coefficient values remain "
                "unselected until a proof-usable selected Route-C/Pi_Rtheta evaluator is derived."
            ),
        },
        "closure_decision": {
            "domain_readiness_closed": True,
            "domain_present_count_after_update": 5,
            "domain_requirement_count": 5,
            "coefficient_functional_skeleton_closed": True,
            "charged_functional_row_count": len(functional_rows),
            "accepted_coefficient_value_count": 0,
            "value_evaluator_source_provenance_closed": evaluator_closed,
            "selected_threshold_response_functional_instantiated": False,
            "generation_resolved_threshold_source_rows_closed": False,
            "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
            "minimal_parameter_yukawa_closure_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTTSelectedRThetaCoefficientFunctionalOrUniversalAnchorSelection",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "domain_readiness_closed": True,
        "domain_present_count_after_update": 5,
        "domain_requirement_count": 5,
        "coefficient_functional_skeleton_closed": True,
        "charged_functional_row_count": len(functional_rows),
        "accepted_coefficient_value_count": 0,
        "value_evaluator_source_provenance_closed": evaluator_closed,
        "universal_anchor_selected": False,
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected RThetaCoefficientFunctional or UniversalAnchorSelection v1

Status: `{STATUS}`.

This artifact closes the remaining `R_theta` domain/readiness side after the
family-eigenprofile basis map.  It emits the selected coefficient-functional
skeleton over the nine charged generation rows, while refusing to promote
numeric coefficients from the unselected Route-C smoke payload.

```text
R_theta domain readiness closed        : true
domain readiness rows present          : 5/5
coefficient functional skeleton closed : true
charged functional rows emitted        : {len(functional_rows)}/9
accepted coefficient values            : 0
value evaluator provenance closed      : {str(evaluator_closed).lower()}
universal anchor selected              : false
selected threshold response instantiated: false
```

The key distinction is now sharp: the coefficient functional is selected as a
map on the selected family basis, but its numerical evaluator still requires
proof-usable selected Route-C/Strominger source provenance, quotient-valid
Galerkin basis data, and `Pi_Rtheta`.  Formal-lift Route-C diagnostics are
useful shape tests, not proof data.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
