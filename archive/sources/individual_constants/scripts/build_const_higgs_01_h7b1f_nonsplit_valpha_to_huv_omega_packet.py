"""Build CONST-HIGGS-01 H7B1F non-split V_alpha to Huv/Omega packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79_REPO = TEXPAPERS / "mtt-q79-proof-repro"
SM_PARITY_REPO = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
REDUCTION_CONTRACT = BASE / "nonsplit_to_huv_reduction_contract.packet.json"
CURRENT_PACKET_AUDIT = BASE / "current_packet_value_audit.packet.json"
FUNCTOR_THEOREM = BASE / "basis_invariant_huv_functor_theorem.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1F_NonSplitVAlphaToHuvOmegaPacket_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1F_NONSPLIT_TO_HUV_REDUCTION_CONTRACT_BUILT_VALUES_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    h7b1c_payload_path = DATA / "const_higgs_01_h7b1c_selected_two_higgs_mass_strain_hessian" / "minimal_two_by_two_hessian_payload_request.packet.json"
    h7b1e_path = DATA / "const_higgs_01_h7b1e_binding_retirement_and_omega_route.candidate.json"
    h7b1e_route_path = DATA / "const_higgs_01_h7b1e_binding_retirement_and_omega_route" / "nonsplit_omega_route_status.packet.json"
    valpha_path = Q79_REPO / "candidate_data" / "all_remaining_valpha_gates" / "selected_valpha_chern_weil_operator_source.after_terminal_lockdown.json"
    extraction_contract_path = SM_PARITY_REPO / "candidate_data" / "selected_visibleoperatorpayload_or_routechymresidual" / "hym_operator_extraction_contract.packet.json"
    e6_dictionary_path = Q79_REPO / "certificates" / "e6_to_sm_yukawa_operator_dictionary_certificate.json"

    h7b1c_payload = load(h7b1c_payload_path)
    h7b1e = load(h7b1e_path)
    h7b1e_route = load(h7b1e_route_path)
    valpha = load(valpha_path)
    extraction_contract = load(extraction_contract_path)
    e6_dictionary = load(e6_dictionary_path)

    valpha_ext = valpha["valpha_extension"]
    operator_execution = valpha["operator_execution"]
    e6_higgs_slots = {
        "5_H": e6_dictionary["representation_dictionary"]["sm_assignments"]["5_H"],
        "bar5_H": e6_dictionary["representation_dictionary"]["sm_assignments"]["bar5_H"],
    }

    reduction_contract = {
        "schema": "MTTConstHiggs01H7B1FNonSplitToHuvReductionContract.v1",
        "status": "NONSPLIT_VALPHA_TO_HUV_REDUCTION_CONTRACT_BUILT_VALUES_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1F-NONSPLIT-VALPHA-TO-HUV-REDUCTION-CONTRACT",
        "source_route": {
            "selected_branch": valpha["source_identity"]["branch_id"],
            "source_shape": "0 -> L -> V_alpha -> L^-1 -> 0",
            "selected_L": valpha_ext["selected_L"],
            "selected_L2": valpha_ext["selected_L2"],
            "h1_L2": valpha_ext["h1_L2"],
            "c2_valpha": valpha_ext["c2_valpha"],
            "nonzero_ext_class_selected": valpha_ext["nonzero_ext_class_selected"],
        },
        "required_payload": {
            "P_source": "same-source non-split V_alpha or Route-C selected operator packet with selected_source_verified true",
            "B_Huv": "B_Huv: source-orthonormal two-column Higgs-slot projection/lift matrix with columns H_u and H_d^dagger",
            "M_source": "M_source: same-source Hermitian mass/strain or Hessian operator before Higgs reduction",
            "Q_quotient": "quotient row [1,1] implementing q(H_u)=H, q(H_d^dagger)=H",
            "exactness": "finite residual/truncation/source certificate for P_source, B_Huv, and M_source",
            "no_target_fit": "none of P_source, B_Huv, M_source may be chosen from measured lambda_H, Higgs mass, tan_beta, or threshold residual",
        },
        "computed_packet_when_filled": {
            "Huv": "B_Huv^* M_source B_Huv",
            "Huu": "(Huv)_{11}",
            "Hud": "(Huv)_{12}",
            "Hdd": "(Huv)_{22}",
            "Delta": "(Huu-Hdd)/2",
            "Omega": "Hud",
            "P_L": "light eigenprojector of Huv with q|im(P_L) nonzero",
            "s_beta": "Delta^2/(Delta^2+|Omega|^2)",
        },
        "basis_invariance_requirement": {
            "source_unitary_change": "M_source -> U^* M_source U and B_Huv -> U^* B_Huv leaves Huv invariant",
            "Huv_basis_phase_change": "H_u,H_d^dagger phase changes conjugate Huv, leaving s_beta invariant",
        },
        "current_packet_passes": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    current_packet_audit = {
        "schema": "MTTConstHiggs01H7B1FCurrentPacketValueAudit.v1",
        "status": "CURRENT_NONSPLIT_SUPPORT_DOES_NOT_EMIT_HUV_VALUES",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1F-CURRENT-PACKET-VALUE-AUDIT",
        "closed_support_imported": h7b1e_route["closed_support_fields"],
        "missing_for_reduction": {
            "selected_source_identity": valpha["source_identity"]["selected_by_mtt"],
            "source_certificate": valpha["source_identity"]["source_certificate"],
            "pic0_selected_or_quotiented": valpha_ext["pic0_selected_or_quotiented"],
            "non_split_stability_or_hym_proved": valpha_ext["non_split_stability_or_hym_proved"],
            "hym_strominger_or_routec_residual_pass": operator_execution["hym_strominger_or_routec_residual_pass"],
            "typed_transition_or_rhoE_data_emitted": operator_execution["typed_transition_or_rhoE_data_emitted"],
            "sector_D_E_packets_pass": operator_execution["sector_D_E_packets_pass"],
            "reduced_green_packets_pass": operator_execution["reduced_green_packets_pass"],
            "dotD_packets_pass": operator_execution["dotD_packets_pass"],
            "primitive_C1_or_Yukawa_contractions": operator_execution["primitive_C1_or_Yukawa_contractions"],
            "Higgs_slot_projection_B_Huv_emitted": False,
            "Hermitian_mass_strain_M_source_emitted": False,
        },
        "external_operator_extraction_contract": {
            "source": rel(extraction_contract_path),
            "selected_operator_values_closed": extraction_contract["selected_operator_values_closed"],
            "actual_extraction_theorem_supplied": extraction_contract["actual_extraction_theorem_supplied"],
            "actual_visible_operator_payload_emitted": extraction_contract["actual_visible_operator_payload_emitted"],
        },
        "e6_higgs_slot_support": {
            "source": rel(e6_dictionary_path),
            "slots": e6_higgs_slots,
            "physical_light_higgs_doublet_selection_open": e6_dictionary["open"]["physical_light_higgs_doublet_selection"],
        },
        "conclusion": {
            "selected_Huv_basis_binding_found": False,
            "selected_finite_Huv_reduction_found": False,
            "selected_offdiagonal_Omega_found": False,
            "selected_Huu_Hud_Hdd_found": False,
            "selected_s_beta_value_found": False,
            "numeric_lambda_H_derived": False,
            "strict_no_knob_Higgs_closure": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    functor_theorem = {
        "schema": "MTTConstHiggs01H7B1FBasisInvariantHuvFunctorTheorem.v1",
        "status": "BASIS_INVARIANT_HUV_REDUCTION_FUNCTOR_PROVED_CONDITIONAL_VALUES_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1F-BASIS-INVARIANT-HUV-FUNCTOR",
        "theorem": {
            "name": "BasisInvariantNonSplitToHuvReductionFunctor",
            "proved": True,
            "statement": (
                "Given a same-source Hermitian operator M_source and a same-source source-orthonormal Higgs-slot lift B_Huv with columns (H_u,H_d^dagger), the finite Huv block B_Huv^* M_source B_Huv is independent of source-basis unitary changes. The H7B1B formulas then compute Delta, Omega, P_L, and s_beta without introducing a beta knob. Current packets do not provide M_source or B_Huv, so this is a conditional functor theorem, not value closure."
            ),
        },
        "proof_steps": [
            "Hermiticity of M_source implies Huv=B^*MB is Hermitian.",
            "If the source basis changes by U, then M -> U^*MU and B -> U^*B, so B^*MB is unchanged.",
            "If the Huv basis changes by a diagonal phase V, then Huv -> V^*Huv V; eigenprojector and (Tr(J_D P_L))^2 are invariant.",
            "With Huv fixed, H7B1B gives Delta=(Huu-Hdd)/2, Omega=Hud, and s_beta=Delta^2/(Delta^2+|Omega|^2).",
        ],
        "conditional_values_open": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1FNextWork.v1",
        "status": "NEXT_WORKORDER_H7B1G_FILL_BHUV_OR_MSOURCE",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1F-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1G-FILL-BHUV-OR-MSOURCE",
            "task": "Try to emit either the selected Higgs-slot lift B_Huv or the selected Hermitian source operator M_source from the non-split V_alpha/Route-C packet.",
        },
        "parallel_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B2-SELECTED-EW-BOUNDARY-RG-PACKET",
            "task": "Continue selected electroweak boundary/RG transport in parallel.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1FNonSplitVAlphaToHuvOmegaPacket",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1F-NONSPLIT-VALPHA-TO-HUV-OMEGA-PACKET",
        "output_packets": {
            "nonsplit_to_huv_reduction_contract": rel(REDUCTION_CONTRACT),
            "current_packet_value_audit": rel(CURRENT_PACKET_AUDIT),
            "basis_invariant_huv_functor_theorem": rel(FUNCTOR_THEOREM),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": functor_theorem["theorem"],
        "reduction_contract_built": True,
        "basis_invariant_Huv_functor_proved": True,
        "rank2_valpha_model_selected": valpha_ext["rank2_valpha_model_selected"],
        "terminal_L_L2_source_closed": valpha_ext["terminal_monad_difference_L3_minus_K2_selector_closed"],
        "nonzero_ext_class_selected": valpha_ext["nonzero_ext_class_selected"],
        "selected_source_identity_closed": valpha["source_identity"]["selected_by_mtt"],
        "selected_Huv_basis_binding_found": False,
        "selected_Higgs_lift_B_Huv_found": False,
        "selected_Hermitian_M_source_found": False,
        "selected_finite_Huv_reduction_found": False,
        "selected_offdiagonal_Omega_found": False,
        "selected_Huu_Hud_Hdd_found": False,
        "selected_Delta_Omega_found": False,
        "selected_s_beta_value_found": False,
        "selected_EW_boundary_RG_packet_closed": False,
        "new_Higgs_specific_parameters": 0,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1G_FillBHuvOrMSource_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1F_NonSplitVAlphaToHuvOmegaPacket_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "reduction_contract_built": True,
        "basis_invariant_Huv_functor_proved": True,
        "rank2_valpha_model_selected": valpha_ext["rank2_valpha_model_selected"],
        "terminal_L_L2_source_closed": valpha_ext["terminal_monad_difference_L3_minus_K2_selector_closed"],
        "nonzero_ext_class_selected": valpha_ext["nonzero_ext_class_selected"],
        "selected_source_identity_closed": valpha["source_identity"]["selected_by_mtt"],
        "selected_Huv_basis_binding_found": False,
        "selected_Higgs_lift_B_Huv_found": False,
        "selected_Hermitian_M_source_found": False,
        "selected_finite_Huv_reduction_found": False,
        "selected_offdiagonal_Omega_found": False,
        "selected_Huu_Hud_Hdd_found": False,
        "selected_Delta_Omega_found": False,
        "selected_s_beta_value_found": False,
        "selected_EW_boundary_RG_packet_closed": False,
        "new_Higgs_specific_parameters": 0,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H7B1F Non-Split VAlpha to Huv/Omega Packet v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1F-NONSPLIT-VALPHA-TO-HUV-OMEGA-PACKET`

## Result

```text
non-split -> H_uv reduction contract        True
basis-invariant H_uv functor proved         True
rank2 V_alpha support imported              {valpha_ext["rank2_valpha_model_selected"]}
selected Higgs lift B_Huv                   False
selected Hermitian M_source                 False
selected finite H_uv values                 False
selected off-diagonal Omega                 False
selected s_beta                             False
numeric lambda_H                            False
strict no-knob Higgs closure                False
```

## Contract

The exact reduction is:

```text
H_uv = B_Huv^* M_source B_Huv
Delta = (Huu-Hdd)/2
Omega = Hud
s_beta = Delta^2/(Delta^2+|Omega|^2)
```

Here `B_Huv` must be the same-source Higgs-slot lift with columns
`(H_u,H_d^dagger)`, and `M_source` must be the same-source Hermitian
mass/strain operator.  Source-basis changes cancel, so this is a genuine
functorial target, not a coordinate trick.

## What Remains

The non-split `V_alpha` route has good support, but current packets still do
not emit `B_Huv` or `M_source`.  Therefore the next executable slot is:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1G-FILL-BHUV-OR-MSOURCE`
"""

    for path, payload in [
        (REDUCTION_CONTRACT, reduction_contract),
        (CURRENT_PACKET_AUDIT, current_packet_audit),
        (FUNCTOR_THEOREM, functor_theorem),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
