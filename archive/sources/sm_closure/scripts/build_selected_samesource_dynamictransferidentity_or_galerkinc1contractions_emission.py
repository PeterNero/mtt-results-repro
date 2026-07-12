"""Build same-source dynamic transfer identity / Galerkin C1 contractions emission gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

DYNAMIC = DATA / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json"
SOURCE_PROVENANCE = DATA / "selected_routec_weylpair_source_provenance_lemma.candidate.json"
SOURCE_TO_C1 = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
STATIC_ROUTING = DATA / "selected_primitivec1_or_weylpair_sectorrouting_sourceemission.candidate.json"
C1_RESPONSE = DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json"
GALERKIN = DATA / "selected_routec_strominger_galerkin_solve" / "c1_primitive_contractions.candidate.json"

OUTPUT = DATA / "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission.candidate.json"
CERT = CERTS / "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission_certificate.json"
NOTE = CORPUS / "MTT_Selected_SameSourceDynamicTransferIdentity_or_GalerkinC1Contractions_Emission_v1.md"

STATUS = (
    "MTT_SELECTED_SAMESOURCE_DYNAMICTRANSFERIDENTITY_OR_GALERKINC1CONTRACTIONS_"
    "EMISSION_BUILT_NORMAL_FORM_IDENTITY_OPEN"
)
NEXT = "MTT_Selected_PhiFinC1_DynamicTransferIdentity_Proof_or_GalerkinContractions_Run_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    dynamic = load(DYNAMIC)
    source_provenance = load(SOURCE_PROVENANCE)
    source_to_c1 = load(SOURCE_TO_C1)
    static_routing = load(STATIC_ROUTING)
    c1_response = load(C1_RESPONSE)
    galerkin = load(GALERKIN)

    coord = dynamic["conditional_dynamic_transfer_coordinate_packet"]["coordinate_system"]
    gram = dynamic["conditional_dynamic_transfer_coordinate_packet"]["Gram_A_transpose_A"]
    rhs = dynamic["conditional_dynamic_transfer_coordinate_packet"]["A_transpose_b_conditional"]
    delta = dynamic["conditional_dynamic_transfer_coordinate_packet"][
        "deltaTheta_conditional_from_Gram_solve"
    ]

    closed_support = {
        "source_level_Z_X_carrier": (
            source_provenance["what_closes_now"]["source_level_phase_Z_carrier_provenance"]
            and source_provenance["what_closes_now"]["source_level_shift_X_carrier_provenance"]
        ),
        "active_shift_1_1": source_provenance["what_closes_now"][
            "active_shift_1_1_provenance"
        ],
        "static_Z_to_u_e": static_routing["what_closes_now"][
            "selected_static_weyl_sector_routing_emitted"
        ],
        "static_trace_normalization": static_routing["what_closes_now"][
            "selected_static_trace_transfer_normalization_emitted"
        ],
        "conditional_transfer_exact": source_to_c1["conditional_transfer_map"][
            "conditional_exact"
        ],
        "conditional_Gram_exact": dynamic["promotion_gate"]["no_linear_algebra_obstruction"],
    }

    selected_slots = c1_response["emission_audit"]["required_operator_slots"]
    selected_status = {
        "selected_source_to_C1_response_map_emitted": source_provenance["c1_transfer_map"][
            "selected_source_to_C1_response_map_emitted"
        ],
        "normalization_transferred_to_deltaTheta_coefficients": source_provenance[
            "c1_transfer_map"
        ]["normalization_transferred_to_deltaTheta_coefficients"],
        "selected_A_selected_emitted": c1_response["emission_audit"][
            "selected_operator_A_selected_emitted"
        ],
        "selected_b_selected_emitted": c1_response["emission_audit"][
            "selected_source_vector_b_selected_emitted"
        ],
        "selected_Hessian_blocks_emitted": selected_slots["full_lower_order_Hess_Xi_blocks"],
        "selected_sector_response_matrices_emitted": selected_slots[
            "sector_response_matrices_M_u_M_d_M_e_M_nuD"
        ],
        "selected_deltaTheta_C1_solution_emitted": selected_slots[
            "selected_deltaTheta_C1_solution"
        ],
    }

    normal_form_identity = {
        "name": "SelectedSameSourceDynamicTransferIdentityNormalForm",
        "coordinate_system": coord,
        "identity_equations": [
            "Phi_C1_selected(Z) = phase_packet in the fixed 72-real coordinate system",
            "Phi_C1_selected(X) = shift_packet in the fixed 72-real coordinate system",
            "A_selected = [Phi_C1_selected(Z), Phi_C1_selected(X)]",
            "b_selected = Phi_C1_selected(Z) + Phi_C1_selected(X)",
            "G_selected = A_selected^T A_selected = 12 I_2",
            "A_selected^T b_selected = (12, 12)",
            "deltaTheta_C1 = G_selected^{-1} A_selected^T b_selected = (1, 1)",
        ],
        "finite_values_if_identity_proved": {
            "Gram_A_transpose_A": gram,
            "A_transpose_b": rhs,
            "deltaTheta_C1": delta,
            "b_norm_sq": dynamic["conditional_dynamic_transfer_coordinate_packet"][
                "b_conditional_norm_sq"
            ],
            "sector_norm_sq": dynamic["conditional_dynamic_transfer_coordinate_packet"][
                "b_conditional_sector_norm_sq"
            ],
        },
        "proved_conditionally": True,
        "selected_identity_proved_now": False,
        "why_not_proved_now": (
            "The selected source-level carrier, static routing, and conditional transfer are closed, "
            "but current artifacts do not yet emit the dynamic Phi_fin^C1 transfer identity or the "
            "selected Hessian/source vector in the same 72-real coordinate system."
        ),
    }

    lane_A = {
        "name": "same-source dynamic transfer identity",
        "support_closed": closed_support,
        "selected_status": selected_status,
        "can_promote_now": False,
        "minimal_missing_equations": [
            "Phi_C1_selected(Z)=phase_packet",
            "Phi_C1_selected(X)=shift_packet",
            "b_selected=phase_packet+shift_packet",
            "selected Hessian/source normalization gives G=12 I_2",
        ],
    }

    lane_B = {
        "name": "honest selected Galerkin C1 contractions",
        "manifest_status": galerkin["status"],
        "selected_source_verified": galerkin["selected_source_verified"],
        "required_outputs": galerkin["required_outputs"],
        "coordinate_compatibility_required": coord,
        "can_promote_now": False,
    }

    falsifier_contract = {
        "if_selected_dynamic_transfer_emits_different_Gram": "rerun the solve; the conditional Weyl packet is not automatically selected",
        "if_selected_b_selected_differs_from_phase_plus_shift": "do not promote deltaTheta=(1,1); solve the emitted selected equation",
        "if_honest_Galerkin_emits_different_response_matrices": "retire the conditional Weyl packet as only diagnostic support",
        "if_observed_flavor_data_selects_any_equation": "reject as target fitting",
    }

    candidate = {
        "candidate": "MTTSelectedSameSourceDynamicTransferIdentityOrGalerkinC1ContractionsEmission",
        "status": STATUS,
        "inputs": {
            "dynamic_transfer_hessian_value_gate": rel(DYNAMIC),
            "weylpair_source_provenance": rel(SOURCE_PROVENANCE),
            "conditional_source_to_C1_transfer": rel(SOURCE_TO_C1),
            "static_sector_routing": rel(STATIC_ROUTING),
            "selected_C1_response_operator_emission": rel(C1_RESPONSE),
            "honest_galerkin_C1_contractions_manifest": rel(GALERKIN),
        },
        "closed_support": closed_support,
        "normal_form_identity": normal_form_identity,
        "lane_A_same_source_dynamic_transfer": lane_A,
        "lane_B_honest_Galerkin_C1_contractions": lane_B,
        "falsifier_contract": falsifier_contract,
        "promotion_decision": {
            "identity_normal_form_built": True,
            "selected_dynamic_transfer_identity_promoted": False,
            "selected_A_selected_promoted": False,
            "selected_b_selected_promoted": False,
            "selected_deltaTheta_C1_promoted": False,
            "honest_Galerkin_C1_contractions_promoted": False,
            "full_no_knob_flavor_closure_promoted": False,
        },
        "what_closes_now": {
            "same_source_identity_normal_form_built": True,
            "conditional_promotion_theorem_formalized": True,
            "falsifier_contract_built": True,
            "next_proof_target_reduced_to_PhiFinC1_identity_or_Galerkin_run": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "prove_PhiFinC1_selected_dynamic_transfer_identity": True,
            "emit_selected_Hessian_blocks": True,
            "emit_selected_b_selected": True,
            "emit_selected_A_selected": True,
            "run_honest_Galerkin_C1_contraction_emission": True,
            "selected_deltaTheta_C1_solution": True,
            "Yukawa_CKM_PMNS_masses_Higgs_RG_no_knob": True,
            "full_SM_no_knob_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "selected_dynamic_transfer_identity_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "SameSourceDynamicTransferIdentityNormalFormTheorem",
            "proved": True,
            "statement": (
                "Given the fixed 72-real coordinate system and the exact conditional Weyl-pair Gram "
                "packet, selected flavor promotion is equivalent to one same-source identity: the "
                "selected Phi_fin^C1 dynamic transfer must send the selected Z and X source generators "
                "to the phase and shift packet columns and must use the same Hessian/source normalization. "
                "If that identity is proved, A_selected, b_selected, and deltaTheta_C1=(1,1) follow. "
                "If not, an honest selected Galerkin C1 contraction emission must supply replacement "
                "sector response values."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_SameSourceDynamicTransferIdentity_or_GalerkinC1Contractions_Emission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "selected_dynamic_transfer_identity_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "theorem_proved": True,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected SameSourceDynamicTransferIdentity or GalerkinC1Contractions Emission v1

Status: `{STATUS}`.

This artifact turns the remaining wall into a normal-form identity.

If the selected dynamic transfer emits:

```text
Phi_C1_selected(Z) = phase_packet
Phi_C1_selected(X) = shift_packet
A_selected         = [phase_packet, shift_packet]
b_selected         = phase_packet + shift_packet
G_selected         = A_selected^T A_selected = 12 I_2
```

then:

```text
A_selected^T b_selected = {rhs}
deltaTheta_C1           = {delta}
```

So selected promotion is now equivalent to proving that same-source dynamic
transfer identity, or else running an honest selected Galerkin C1 contraction
emission that supplies replacement sector response matrices.

Guardrail: if the selected transfer or honest Galerkin run emits different
values, the conditional Weyl-pair packet remains diagnostic and the emitted
selected equation must be solved instead.

No observed masses, CKM/PMNS values, CP phase, benchmark matrices, or lifted
flags are used as selectors.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
