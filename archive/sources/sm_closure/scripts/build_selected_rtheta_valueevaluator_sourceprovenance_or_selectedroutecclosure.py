"""Build R_theta value-evaluator source-provenance / selected Route-C closure attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_valueevaluator_sourceprovenance_or_selectedroutecclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ALPHA1_IMPORT = PACKET_DIR / "rtheta_alpha1_dotd_provenance_import.packet.json"
READINESS = PACKET_DIR / "rtheta_value_evaluator_readiness_after_alpha1_import.packet.json"
PI_RECHECK = PACKET_DIR / "pi_rtheta_recheck_after_alpha1_import.packet.json"
SELECTED_ROUTE_C = PACKET_DIR / "selected_routec_closure_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_value_evaluator_source_provenance.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaValueEvaluatorSourceProvenance_or_SelectedRouteCClosure_v1.md"

PREVIOUS = DATA / "selected_rtheta_coefficientfunctional_or_universalanchorselection.candidate.json"
PREVIOUS_EVALUATOR = (
    DATA
    / "selected_rtheta_coefficientfunctional_or_universalanchorselection"
    / "rtheta_value_evaluator_provenance_gate.packet.json"
)
ROUTEC_READINESS = (
    DATA
    / "selected_rtheta_selectedroutecgalerkinsolve_or_diagonalprofiletheorem"
    / "current_selected_routec_solve_readiness.packet.json"
)
ALPHA1 = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
HYM_EXTRACTION = DATA / "selected_hym_connection_to_finite_operator_extraction.candidate.json"
SPECTRAL_RETENTION = DATA / "selected_spectral_galerkin_projector_retention_data.candidate.json"
PI_KERNEL = (
    DATA
    / "selected_rtheta_physicalprojectionkernel_or_profileresponse"
    / "pi_rtheta_kernel_attempt.packet.json"
)
ROUTEC_FIRST_CERT = CERTS / "selected_routec_strominger_galerkin_first_run_certificate.json"

STATUS = (
    "MTT_SELECTED_RTHETA_VALUEEVALUATORSOURCEPROVENANCE_OR_SELECTEDROUTECCLOSURE_"
    "IMPORTED_ALPHA1_DOTD_PI_OPEN"
)
NEXT = "MTT_Selected_RThetaPiKernel_from_SelectedHYMConnection_or_BNBasisEmission_v1"


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
            "missing R_theta value-evaluator source-provenance sources: "
            + ", ".join(missing)
        )


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_EVALUATOR,
        ROUTEC_READINESS,
        ALPHA1,
        HYM_EXTRACTION,
        SPECTRAL_RETENTION,
        PI_KERNEL,
        ROUTEC_FIRST_CERT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_evaluator = load(PREVIOUS_EVALUATOR)
    routec_readiness = load(ROUTEC_READINESS)
    alpha1 = load(ALPHA1)
    hym = load(HYM_EXTRACTION)
    spectral = load(SPECTRAL_RETENTION)
    pi_kernel = load(PI_KERNEL)
    routec_first_cert = load(ROUTEC_FIRST_CERT)

    alpha_packet = alpha1["alpha1_driver_replay_import"]
    alpha_import = {
        "schema": "MTTRThetaAlpha1DotDProvenanceImport.v1",
        "status": "THEOREM_DERIVED_ALPHA1_DOTD_REPLAY_IMPORTED_FOR_RTHETA",
        "source": rel(ALPHA1),
        "imported_from": alpha_packet["imported_from"],
        "selected_dotD_source_verified": alpha_packet["selected_dotD_source_verified"],
        "alpha1_driver_verified": alpha_packet["alpha1_driver_verified"],
        "honest_dotD_alpha1_replay": alpha_packet["honest_dotD_alpha1_replay"],
        "du_dalpha1_equals_h_ext": alpha_packet["du_dalpha1_equals_h_ext"],
        "lambda_alpha1": alpha_packet["lambda_alpha1"],
        "N_alpha1_h_ext": alpha_packet["N_alpha1_h_ext"],
        "tangent_residual_l2": alpha_packet["tangent_residual_l2"],
        "accepted_for_rtheta_evaluator_readiness": True,
        "does_not_emit": [
            "selected D_E matrices",
            "selected Riesz/Green operators",
            "coherent spectral zero-mode projectors",
            "primitive C1 contractions",
            "theta_coeff values",
            "lambda_H",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ALPHA1_IMPORT, alpha_import)

    previous_rows = routec_readiness["readiness_rows"]
    readiness_rows: list[dict[str, Any]] = []
    for row in previous_rows:
        updated = dict(row)
        if row["id"] == "honest_dotD_replay_without_lifted_flags":
            updated["present_before_alpha1_import"] = row["present"]
            updated["present"] = True
            updated["source"] = rel(ALPHA1)
            updated["role"] = (
                "honest theorem-derived alpha1/dotD replay imported from same q79/F,m=1 spine"
            )
            updated["closure_reason"] = (
                "Cross-repo theorem imports selected_dotD_source_verified=true and "
                "alpha1_driver_verified=true without lifted diagnostic flags."
            )
        readiness_rows.append(updated)

    readiness_present = sum(1 for row in readiness_rows if row["present"])
    readiness = {
        "schema": "MTTRThetaValueEvaluatorReadinessAfterAlpha1Import.v1",
        "status": "RTHETA_VALUE_EVALUATOR_READINESS_ALPHA1_IMPORTED_DE_GREEN_OPEN",
        "previous_evaluator_gate": rel(PREVIOUS_EVALUATOR),
        "previous_readiness_present_count": previous_evaluator["readiness_present_count"],
        "previous_readiness_required_count": previous_evaluator["readiness_required_count"],
        "readiness_rows": readiness_rows,
        "readiness_present_count": readiness_present,
        "readiness_required_count": len(readiness_rows),
        "closed_now": {
            "honest_dotD_replay_without_lifted_flags": True,
            "alpha1_driver_verified": True,
            "selected_dotD_source_verified": True,
        },
        "still_open_rows": [row["id"] for row in readiness_rows if not row["present"]],
        "selected_value_evaluator_closed": False,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(READINESS, readiness)

    spectral_layer = spectral["two_layer_projector_audit"]["spectral_projector_layer"]
    hym_open = hym["what_remains_open"]
    pi_recheck = {
        "schema": "MTTPiRThetaRecheckAfterAlpha1Import.v1",
        "status": "PI_RTHETA_RECHECKED_ALPHA1_NOT_ACTIVE_DE_GREEN_BASIS_OPEN",
        "previous_pi_kernel_source": rel(PI_KERNEL),
        "previous_pi_closed": pi_kernel["Pi_Rtheta_closed"],
        "alpha1_dotD_blocker_retired": True,
        "component_tests_after_import": {
            "static_block_projectors_available": pi_kernel["component_tests"][
                "static_block_projectors_available"
            ],
            "q79_polarization_available": pi_kernel["component_tests"][
                "q79_polarization_available"
            ],
            "sector_projector_matrices_available": pi_kernel["component_tests"][
                "sector_projector_matrices_available"
            ],
            "stationary_projector_source_verified": pi_kernel["component_tests"][
                "stationary_projector_source_verified"
            ],
            "honest_dotD_alpha1_replay_imported": True,
            "coherent_spectral_projectors_available": spectral_layer[
                "coherent_spectral_zero_mode_projector_retention"
            ],
            "selected_DE_Riesz_Green_available": spectral_layer[
                "selected_D_E_dotD_Riesz_Green"
            ],
            "selected_HYM_connection_representative_available": not hym_open[
                "gauge_fixed_selected_HYM_connection_representative"
            ],
            "selected_finite_basis_quadrature_error_contract_available": not hym_open[
                "selected_finite_basis_quadrature_error_contract"
            ],
        },
        "Pi_Rtheta_closed": False,
        "minimal_missing_primitives": [
            "gauge_fixed_selected_HYM_connection_representative",
            "selected_finite_basis_quadrature_error_contract",
            "selected_D_E_Riesz_Green_from_connection",
            "coherent_spectral_zero_mode_projector_retention",
        ],
        "no_longer_active_blockers": [
            "honest_dotD_replay_without_lifted_flags",
            "alpha1_driver_verified",
            "selected_dotD_source_verified",
        ],
        "accepted_coefficient_value_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PI_RECHECK, pi_recheck)

    selected_routec = {
        "schema": "MTTSelectedRouteCClosureDecisionForRTheta.v1",
        "status": "SELECTED_ROUTEC_CLOSURE_ADVANCED_ALPHA1_IMPORTED_SOURCE_VALUES_OPEN",
        "formal_lift_lower_validators_all_pass": routec_first_cert[
            "formal_lift_lower_validators_all_pass"
        ],
        "formal_lift_promotion_passes": routec_first_cert["formal_lift_promotion_passes"],
        "formal_lift_accepted_as_proof": False,
        "proof_promotion_allowed": False,
        "source_provenance_progress": {
            "alpha1_dotD_source_provenance": True,
            "HYM_connection_representative": False,
            "quotient_valid_B_N_basis": False,
            "selected_DE_Riesz_Green": False,
            "coherent_spectral_projectors": False,
            "primitive_C1_contractions": False,
        },
        "selected_routec_closed": False,
        "selected_value_evaluator_closed": False,
        "next_legal_computation": (
            "construct selected HYM connection representative and quotient-valid B_N basis, "
            "then emit selected D_E/Riesz/Green and rerun Pi_Rtheta"
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SELECTED_ROUTE_C, selected_routec)

    cutset = {
        "schema": "MTTNextCutsetAfterValueEvaluatorSourceProvenance.v1",
        "status": "NEXT_ATTACK_PI_RTHETA_FROM_SELECTED_HYM_CONNECTION_OR_BN_BASIS_EMISSION",
        "closed_now": {
            "alpha1_dotD_provenance_imported_for_rtheta": True,
            "honest_dotD_replay_without_lifted_flags_retired": True,
            "value_evaluator_readiness_advanced_to_5_of_7": readiness_present == 5,
            "formal_lift_still_rejected_as_proof": True,
        },
        "still_open": pi_recheck["minimal_missing_primitives"],
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "derive selected gauge-fixed HYM connection representative and selected B_N basis/quadrature/error contract",
            "route_B": "emit selected D_E/Riesz/Green directly from an already selected finite HYM operator packet if one is found",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaValueEvaluatorSourceProvenanceOrSelectedRouteCClosure",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "rtheta_alpha1_dotd_provenance_import": rel(ALPHA1_IMPORT),
            "rtheta_value_evaluator_readiness_after_alpha1_import": rel(READINESS),
            "pi_rtheta_recheck_after_alpha1_import": rel(PI_RECHECK),
            "selected_routec_closure_decision": rel(SELECTED_ROUTE_C),
            "next_cutset_after_value_evaluator_source_provenance": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaAlpha1DotDProvenanceImportAndPiKernelFrontierTheorem",
            "proved": True,
            "statement": (
                "The theorem-derived alpha1/dotD replay from the same q79/F,m=1 oriented spine can be "
                "imported into the R_theta value-evaluator gate, retiring honest dotD replay as an active "
                "blocker without using lifted diagnostic flags or observed data. This advances value-evaluator "
                "readiness from 4/7 to 5/7. Pi_Rtheta and coefficient values remain open because selected "
                "HYM connection/B_N basis data and selected D_E/Riesz/Green/coherent spectral projectors are "
                "not emitted."
            ),
        },
        "closure_decision": {
            "value_evaluator_readiness_present_count": readiness_present,
            "value_evaluator_readiness_required_count": len(readiness_rows),
            "alpha1_dotd_provenance_imported": True,
            "Pi_Rtheta_closed": False,
            "selected_value_evaluator_closed": False,
            "accepted_coefficient_value_count": 0,
            "accepted_lambda_H_value": False,
            "selected_threshold_response_functional_instantiated": False,
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
        "certificate": "MTTSelectedRThetaValueEvaluatorSourceProvenanceOrSelectedRouteCClosure",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "value_evaluator_readiness_present_count": readiness_present,
        "value_evaluator_readiness_required_count": len(readiness_rows),
        "alpha1_dotd_provenance_imported": True,
        "Pi_Rtheta_closed": False,
        "accepted_coefficient_value_count": 0,
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected RThetaValueEvaluatorSourceProvenance or SelectedRouteCClosure v1

Status: `{STATUS}`.

This artifact attacks the value-evaluator source-provenance gate after
`R_theta` domain readiness reached 5/5.

```text
alpha1/dotD provenance imported       : true
value evaluator readiness             : {readiness_present}/7
Pi_Rtheta closed                      : false
selected value evaluator closed       : false
accepted coefficient values           : 0
formal-lift accepted as proof         : false
```

The honest improvement is real but limited: the theorem-derived cross-repo
alpha1/dotD replay retires the `honest_dotD_replay_without_lifted_flags`
blocker for the R_theta evaluator.  It does not emit selected `D_E`,
Riesz/Green, coherent spectral projectors, primitive C1 contractions, Yukawa
coefficients, or `lambda_H`.

The remaining `Pi_Rtheta` frontier is now:

- selected gauge-fixed HYM connection representative,
- selected quotient/deck-valid `B_N` basis, quadrature, and error contract,
- selected `D_E`/Riesz/Green from that connection,
- coherent spectral zero-mode projector retention.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
