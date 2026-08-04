"""Import same-source dynamic-transfer identity normal form / Galerkin fallback."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = CERTS / "dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill_import_certificate.json"
SM_PACKET = SM / "candidate_data" / "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission.candidate.json"
SM_CERT = SM / "certificates" / "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission_certificate.json"

OUTPUT_PACKET = DATA / "samesource_dynamictransferidentity_or_galerkinc1contractions_emission_import.candidate.json"
OUTPUT_CERT = CERTS / "samesource_dynamictransferidentity_or_galerkinc1contractions_emission_import_certificate.json"
OUTPUT_NOTE = CORPUS / "SameSourceDynamicTransferIdentity_or_GalerkinC1Contractions_Emission_Import_v1.md"

STATUS = "SAMESOURCE_DYNAMIC_TRANSFER_IDENTITY_NORMAL_FORM_IMPORTED_OPEN"
PREVIOUS_STATUS = "DYNAMIC_TRANSFER_HESSIAN_BSELECTED_VALUEFILL_IMPORTED_CONDITIONAL_GRAM_EXACT_SOURCE_OPEN"
SM_STATUS = (
    "MTT_SELECTED_SAMESOURCE_DYNAMICTRANSFERIDENTITY_OR_GALERKINC1CONTRACTIONS_"
    "EMISSION_BUILT_NORMAL_FORM_IDENTITY_OPEN"
)
NEXT = "Selected_U1Y_RouteC_PhiFinC1_DynamicTransferIdentity_Proof_or_GalerkinContractions_Run_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    sm_packet = load(SM_PACKET)
    sm_cert = load(SM_CERT)
    identity = sm_packet["normal_form_identity"]
    lane_a = sm_packet["lane_A_same_source_dynamic_transfer"]
    lane_b = sm_packet["lane_B_honest_Galerkin_C1_contractions"]
    decision = sm_packet["promotion_decision"]

    checks = {
        "G0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "G1_upstream_theorem_proved": sm_cert["status"] == SM_STATUS
        and sm_cert["theorem_proved"] is True
        and sm_packet["theorem"]["proved"] is True,
        "G2_closed_support_available": all(sm_packet["closed_support"].values()),
        "G3_normal_form_identity_built": identity["name"] == "SelectedSameSourceDynamicTransferIdentityNormalForm"
        and identity["coordinate_system"]["codomain_real_dimension"] == 72
        and len(identity["identity_equations"]) == 7
        and identity["finite_values_if_identity_proved"]["Gram_A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]]
        and identity["finite_values_if_identity_proved"]["A_transpose_b"] == [12.0, 12.0]
        and identity["finite_values_if_identity_proved"]["deltaTheta_C1"] == [1.0, 1.0]
        and identity["proved_conditionally"] is True
        and identity["selected_identity_proved_now"] is False,
        "G4_lane_A_identity_equations_missing": lane_a["can_promote_now"] is False
        and len(lane_a["minimal_missing_equations"]) == 4
        and all(value is False for value in lane_a["selected_status"].values()),
        "G5_lane_B_galerkin_fallback_open": lane_b["can_promote_now"] is False
        and lane_b["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING"
        and lane_b["selected_source_verified"] is False
        and lane_b["coordinate_compatibility_required"]["codomain_real_dimension"] == 72,
        "G6_falsifier_contract_present": all(
            key in sm_packet["falsifier_contract"]
            for key in [
                "if_selected_dynamic_transfer_emits_different_Gram",
                "if_selected_b_selected_differs_from_phase_plus_shift",
                "if_honest_Galerkin_emits_different_response_matrices",
                "if_observed_flavor_data_selects_any_equation",
            ]
        ),
        "G7_promotion_not_overclaimed": decision["identity_normal_form_built"] is True
        and decision["selected_dynamic_transfer_identity_promoted"] is False
        and decision["selected_A_selected_promoted"] is False
        and decision["selected_b_selected_promoted"] is False
        and decision["selected_deltaTheta_C1_promoted"] is False
        and decision["honest_Galerkin_C1_contractions_promoted"] is False
        and decision["full_no_knob_flavor_closure_promoted"] is False,
        "G8_no_target_or_closure_overclaim": sm_packet["closure_claimed"] is False
        and sm_packet["selected_dynamic_transfer_identity_claimed"] is False
        and sm_packet["A_selected_claimed"] is False
        and sm_packet["b_selected_claimed"] is False
        and sm_packet["deltaTheta_C1_claimed"] is False
        and sm_packet["Galerkin_C1_contractions_claimed"] is False
        and sm_packet["observed_data_used"] is False
        and sm_packet["target_fitting_used"] is False,
    }

    return {
        "packet": "SameSourceDynamicTransferIdentity_or_GalerkinC1Contractions_Emission_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "sm_same_source_identity_packet": str(SM_PACKET),
            "sm_same_source_identity_certificate": str(SM_CERT),
        },
        "theorem": {
            "name": "SameSourceDynamicTransferIdentityNormalFormImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "Selected flavor promotion is reduced to one normal-form "
                "same-source identity in the fixed 72-real coordinate system: "
                "Phi_C1_selected(Z)=phase_packet, Phi_C1_selected(X)=shift_packet, "
                "A_selected=[phase,shift], b_selected=phase+shift, and "
                "G_selected=12 I_2. If proved, deltaTheta_C1=(1,1) follows; "
                "if falsified, an honest selected Galerkin C1 contraction "
                "emission must supply replacement response matrices."
            ),
        },
        "checks": checks,
        "closed_support": sm_packet["closed_support"],
        "normal_form_identity": identity,
        "lane_A_same_source_dynamic_transfer": lane_a,
        "lane_B_honest_Galerkin_C1_contractions": lane_b,
        "falsifier_contract": sm_packet["falsifier_contract"],
        "promotion_decision": decision,
        "what_closes_now": sm_packet["what_closes_now"],
        "what_remains_open": sm_packet["what_remains_open"],
        "frontier_update": {
            "old_next": previous["next_required_artifact"],
            "current_next": NEXT,
            "why": (
                "The conditional finite solve is now a normal-form same-source "
                "identity target, with honest Galerkin C1 emission as falsifying "
                "or replacement route."
            ),
        },
        "guardrails": {
            "identity_normal_form_built": True,
            "selected_identity_proved_now": False,
            "selected_dynamic_transfer_identity_claimed": False,
            "selected_A_selected_claimed": False,
            "selected_b_selected_claimed": False,
            "selected_deltaTheta_C1_claimed": False,
            "honest_Galerkin_C1_contractions_claimed": False,
            "observed_data_used": False,
            "target_fitting_used": False,
            "full_SM_closure_claimed": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SameSourceDynamicTransferIdentityOrGalerkinC1ContractionsEmissionImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "frontier_update": packet["frontier_update"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    identity = packet["normal_form_identity"]
    values = identity["finite_values_if_identity_proved"]
    return f"""# SameSourceDynamicTransferIdentity or GalerkinC1Contractions Emission Import v1

Status: `{cert["status"]}`.

## Normal Form

Selected promotion is now equivalent to proving:

```text
Phi_C1_selected(Z) = phase_packet
Phi_C1_selected(X) = shift_packet
A_selected = [phase_packet, shift_packet]
b_selected = phase_packet + shift_packet
G_selected = A_selected^T A_selected = 12 I_2
```

If this identity is proved in the fixed 72-real coordinate system, then:

```text
A_selected^T b_selected = {values["A_transpose_b"]}
deltaTheta_C1 = {values["deltaTheta_C1"]}
```

## Falsifier

If selected transfer, selected `b_selected`, or honest Galerkin C1 contractions
emit different values, the conditional Weyl-pair packet remains diagnostic and
the emitted selected equation must be solved instead.

No observed masses, CKM/PMNS values, CP phase, benchmark matrices, or lifted
flags are used as selectors.

Next artifact: `{packet["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
