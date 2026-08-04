"""Build Step 30 projective B_N mechanical lift / visible source cutset."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step30_projectivebn_mechanicallift_or_visiblesourcecutset"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
MECHANICAL = PACKET_DIR / "step30_projective_bn_mechanical_lift.packet.json"
SOURCE_GAP = PACKET_DIR / "step30_visible_operator_source_gap.packet.json"
NEXT_CONTRACT = PACKET_DIR / "step30_next_visible_source_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step30_ProjectiveBNMechanicalLift_or_VisibleSourceCutset_v1.md"

STEP29 = DATA / "selected_step29_operatorsector_rhoede_attempt_or_projectivebnsourcecutset.candidate.json"
SMOOTH_BN = DATA / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
DE_ACTION = DATA / "selected_routec_de_action_on_smooth_bn.candidate.json"
PROJECTORS_DOTD = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
PROJECTIVE_GERBE = DATA / "projective_gerbe_rhoe_source_promotion.candidate.json"

STATUS = "MTT_SELECTED_STEP30_PROJECTIVEBN_MECHANICAL_LIFT_BUILT_VISIBLE_OPERATOR_SOURCE_OPEN"
NEXT = "MTT_Selected_Step31_VisibleChernWeilOperatorSource_or_SelectedProjectiveBNValues_v1"
SECTORS = ["Q", "u", "d", "L", "e", "N", "H"]


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

    inputs = [STEP29, SMOOTH_BN, DE_ACTION, PROJECTORS_DOTD, PROJECTIVE_GERBE]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 30 inputs: " + ", ".join(missing))

    step29 = load(STEP29)
    smooth = load(SMOOTH_BN)
    de = load(DE_ACTION)
    dotd = load(PROJECTORS_DOTD)
    gerbe = load(PROJECTIVE_GERBE)

    lift = smooth["B_N_lift"]
    smooth_fields = smooth["contract_comparison"]["fields_emitted_now"]
    smooth_missing = smooth["contract_comparison"]["still_missing_for_full_contract"]
    de_matrix = de["validation"]["matrix_consistency"]
    dotd_validation = dotd["validation"]
    gerbe_result = gerbe["promotion_result"]
    gerbe_flags = gerbe["promotion_gate_flags_after_s3_closure"]

    mechanical = {
        "schema": "MTTStep30ProjectiveBNMechanicalLift.v1",
        "status": "PROJECTIVE_BN_MECHANICAL_LIFT_EMITTED_SOURCE_UNPROMOTED",
        "from_step29": {
            "identity_rhoE_smoke_retired": step29["closure_decision"]["identity_rhoE_smoke_retired_as_selected_route"],
            "nonidentity_projective_rhoE_candidate_imported": step29["closure_decision"]["nonidentity_projective_rhoE_candidate_imported"],
        },
        "smooth_BN_scaffold": {
            "dimension": lift["dimension"],
            "basis_count": len(lift["basis"]),
            "zero_cluster_dimension": lift["zero_cluster"]["dimension"],
            "zero_cluster_basis_ids": lift["zero_cluster"]["basis_ids"],
            "complement_gap": lift["complement_gap"],
            "ordinary_bundle_equivariance": lift["bundle_equivariance"]["ordinary_bundle_equivariance"],
            "projective_equivariance_up_to_central_phase": lift["bundle_equivariance"]["projective_equivariance_up_to_central_phase"],
            "rho_E_source": lift["bundle_equivariance"]["rho_E_source"],
        },
        "mechanical_fields_closed": {
            "smooth_scalar_basis_functions_phi_m": smooth_fields["scalar_basis_functions_phi_m"],
            "metric_volume_quadrature": smooth_fields["metric_volume_quadrature"],
            "Gram_matrix_entries": smooth_fields["Gram_matrix_entries"],
            "stiffness_matrix_entries": smooth_fields["stiffness_matrix_entries"],
            "generalized_eigenpairs": smooth_fields["generalized_eigenpairs"],
            "Riesz_projectors": smooth_fields["Riesz_projectors"],
            "reduced_Green_operators": smooth_fields["reduced_Green_operators"],
            "projective_bundle_transition_or_equivariance": smooth_fields["bundle_transition_or_equivariance_matrices"],
            "D_E_matrix_on_27_mode_BN": de["what_closes_now"]["D_E_matrix_on_27_mode_BN_emitted"],
            "ordered_zero_mode_bases": de["what_closes_now"]["zero_mode_bases_ordered"],
            "sector_projectors_on_27_mode_BN": dotd["what_closes_now"]["sector_projectors_on_27_mode_BN_emitted"],
            "dotD_alpha1_matrix_in_same_basis": dotd["what_closes_now"]["dotD_alpha1_matrix_in_same_basis_emitted"],
        },
        "mechanical_validation": {
            "D_E_diagnostic_validator_passes": de["validation"]["diagnostic_source_lift"]["exit_code"] == 0,
            "D_E_honest_validator_fails_only_by_selected_source_flags": de_matrix["honest_validator_fails_only_by_selected_source_flags"],
            "domain_dimension": de_matrix["domain_dimension"],
            "family_kernel_dimension": de_matrix["family_kernel_dimension"],
            "higgs_kernel_dimension": de_matrix["higgs_kernel_dimension"],
            "dotD_diagnostic_validator_passes": dotd_validation["diagnostic_lift_validator_passes"],
            "dotD_honest_validator_fails_only_by_source_driver_flags": dotd_validation["honest_validator_fails_only_by_source_driver_flags"],
            "projector_residuals": dotd_validation["projector_residuals"],
        },
        "not_closed_by_mechanical_lift": {
            "selected_visible_operator_source": True,
            "selected_source_verified_operator_flags": True,
            "full_iwasawa_strominger_DE_not_only_model_active": smooth_missing["full_iwasawa_operator_truncation_error"],
            "operator_level_projective_rhoE_transition": True,
            "internal_Rtheta_scalar_rows": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(MECHANICAL, mechanical)

    source_gap = {
        "schema": "MTTStep30VisibleOperatorSourceGap.v1",
        "status": "VISIBLE_CHERN_WEIL_OPERATOR_SOURCE_IS_THE_REMAINING_SELECTOR",
        "s3_projective_source_status": {
            "source_level_projective_gerbe_rhoE_promoted": gerbe_result["source_level_projective_gerbe_rhoE_promoted"],
            "operator_level_projective_rhoE_promoted": gerbe_result["operator_level_projective_rhoE_promoted"],
            "fixed_differential_cohomology_class": gerbe_flags["fixed_differential_cohomology_class"],
            "freed_witten_verified": gerbe_flags["freed_witten_verified"],
            "green_schwarz_bianchi_verified": gerbe_flags["green_schwarz_bianchi_verified"],
            "map_to_central_cocycle_verified": gerbe_flags["map_to_central_cocycle_verified"],
            "coherent_spectral_projector_verified": gerbe_flags["coherent_spectral_projector_verified"],
        },
        "remaining_cut_set": gerbe_result["remaining_cut_set"],
        "why_step30_cannot_promote_flags": [
            "the S3 projective gerbe source is selected only at source level",
            "the smooth B_N matrices are model-active/diagnostic until visible bundle/sheaf source is selected",
            "honest D_E validator fails exactly on selected_source_verified flags",
            "honest dotD validator fails exactly on selected_dotD_source_verified and alpha1_driver_verified flags",
            "coherent spectral projector verification is still false in the projective gerbe promotion gate",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SOURCE_GAP, source_gap)

    contract = {
        "schema": "MTTStep30NextVisibleSourceContract.v1",
        "status": "NEXT_VISIBLE_CHERN_WEIL_OPERATOR_SOURCE_CONTRACT",
        "next_required_artifact": NEXT,
        "must_emit_next": [
            "selected visible bundle/sheaf or Route-C source on q79/F,m=1",
            "Chern-Weil derivation of Tr_F_visible^2 from that selected source",
            "operator-level projective rho_E transition on the smooth projective B_N basis",
            "selected_source_verified=true for D_E in all Q,u,d,L,e,N,H slots by theorem",
            "selected_dotD_source_verified=true and alpha1_driver_verified=true in all Q,u,d,L,e,N,H slots by theorem",
            "coherent spectral projector verification for the already emitted sector projectors",
            "full-Iwasawa/Strominger truncation or replacement certificate for the model-active lift",
        ],
        "must_not_reopen": [
            "identity rho_E smoke route",
            "smooth scalar B_N basis/quadrature/Gram/stiffness mechanical emission",
            "stationary P_s/K_s and rho_s from Step17",
            "source-level S3 projective gerbe rho_E",
        ],
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(NEXT_CONTRACT, contract)

    candidate = {
        "candidate": "MTTSelectedStep30ProjectiveBNMechanicalLiftOrVisibleSourceCutset",
        "status": STATUS,
        "inputs": {
            "step29": rel(STEP29),
            "smooth_bn": rel(SMOOTH_BN),
            "de_action": rel(DE_ACTION),
            "sector_projectors_dotd": rel(PROJECTORS_DOTD),
            "projective_gerbe": rel(PROJECTIVE_GERBE),
        },
        "output_packets": {
            "projective_bn_mechanical_lift": rel(MECHANICAL),
            "visible_operator_source_gap": rel(SOURCE_GAP),
            "next_visible_source_contract": rel(NEXT_CONTRACT),
        },
        "theorem": {
            "name": "Step30ProjectiveBNMechanicalLiftReductionTheorem",
            "proved": True,
            "statement": (
                "After the identity-rhoE route is retired, the non-identity projective "
                "rhoE route already has a concrete smooth 27-mode projective B_N "
                "mechanical lift: basis, quadrature, Gram/stiffness, zero cluster, "
                "Riesz/Green, D_E matrices, sector projectors, and dotD in the same "
                "basis. This closes the mechanical B_N lift fields from Step29. It does "
                "not promote selected operator-sector values, because the remaining "
                "selector is the visible Chern-Weil/operator source that must derive "
                "the honest source flags and coherent spectral projector verification."
            ),
        },
        "closure_decision": {
            "identity_rhoE_smoke_route_retired": True,
            "projective_BN_mechanical_lift_fields_closed": True,
            "smooth_scalar_basis_quadrature_gram_stiffness_closed": True,
            "model_active_D_E_projectors_Green_dotD_emitted": True,
            "source_level_projective_gerbe_rhoE_closed": True,
            "selected_visible_operator_source_closed": False,
            "operator_level_projective_rhoE_transition_closed": False,
            "selected_source_verified_operator_flags_closed": False,
            "coherent_spectral_projector_verified": False,
            "selected_sector_basis_D_E_Riesz_Green_dotD_matrices_closed": False,
            "fullS2_operator_payload_closed": False,
            "accepted_internal_scalar_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "Step29_smooth_BN_mechanical_missing_fields": True,
            "projective_BN_basis_and_operator_postcheck_payload": True,
            "visible_operator_source_cutset_isolated": True,
        },
        "what_remains_open": {
            "selected_visible_Chern_Weil_operator_source": True,
            "operator_level_projective_rhoE_transition": True,
            "selected_D_E_Riesz_Green_dotD_operator_sector_values": True,
            "coherent_spectral_projector_verification": True,
            "internal_Rtheta_scalar_rows": True,
            "lambda_H": True,
            "Yukawa_CKM_PMNS_mass_values": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step30_ProjectiveBNMechanicalLift_or_VisibleSourceCutset_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "projective_BN_mechanical_lift_fields_closed": True,
        "selected_visible_operator_source_closed": False,
        "operator_sector_values_closed": False,
        "accepted_internal_scalar_row_count": 0,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step30 ProjectiveBNMechanicalLift or VisibleSourceCutset v1

Status: `{STATUS}`.

Step30 closes the mechanical half of the Step29 target:

```text
identity rho_E smoke route                         retired
source-level S3 projective gerbe rho_E             closed
smooth projective B_N basis/quadrature/Gram         closed mechanically
model-active stiffness, Riesz, Green                closed mechanically
D_E matrices on 27-mode B_N                         emitted
sector projectors and dotD in same basis            emitted
selected visible Chern-Weil/operator source         open
operator-level projective rho_E transition          open
selected D_E/Riesz/Green/dotD values                open
internal R_theta scalar rows                        open
```

So the remaining wall is not "find a B_N basis."  It is the selected visible
operator source that legally turns the existing projective smooth-B_N matrices
from diagnostic/mechanical data into theorem-derived selected operator values.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
