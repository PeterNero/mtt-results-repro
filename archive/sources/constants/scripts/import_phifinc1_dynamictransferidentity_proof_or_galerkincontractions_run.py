"""Import PhiFinC1 dynamic-transfer identity attempt / Galerkin run boundary."""

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

PREVIOUS = CERTS / "samesource_dynamictransferidentity_or_galerkinc1contractions_emission_import_certificate.json"
SM_PACKET = SM / "candidate_data" / "selected_phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run.candidate.json"
SM_CERT = SM / "certificates" / "selected_phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run_certificate.json"

OUTPUT_PACKET = DATA / "phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run_import.candidate.json"
OUTPUT_CERT = CERTS / "phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run_import_certificate.json"
OUTPUT_NOTE = CORPUS / "PhiFinC1_DynamicTransferIdentity_Proof_or_GalerkinContractions_Run_Import_v1.md"

STATUS = "PHIFINC1_DYNAMIC_TRANSFER_ATTEMPT_IMPORTED_STATIONARY_TRACE_CLOSED_C1_OPEN"
PREVIOUS_STATUS = "SAMESOURCE_DYNAMIC_TRANSFER_IDENTITY_NORMAL_FORM_IMPORTED_OPEN"
SM_STATUS = "MTT_SELECTED_PHIFINC1_DYNAMICTRANSFERIDENTITY_PROOF_OR_GALERKINCONTRACTIONS_RUN_BUILT_STATIONARY_TRACE_CLOSED_C1_OPEN"
NEXT = "Selected_U1Y_RouteC_DifferentiatedPhiFinC1_PrimitiveOverlapContractions_or_GalerkinRun_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    sm_packet = load(SM_PACKET)
    sm_cert = load(SM_CERT)
    stationary = sm_packet["stationary_trace_import"]
    boundary = sm_packet["phifin_payload_boundary"]
    identity = sm_packet["PhiFinC1_identity_attempt"]
    galerkin = sm_packet["Galerkin_run_attempt"]
    theorem = sm_packet["partial_promotion_theorem"]

    checks = {
        "G0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "G1_upstream_theorem_proved": sm_cert["status"] == SM_STATUS
        and sm_cert["theorem_proved"] is True
        and theorem["proved"] is True,
        "G2_coordinate_system_preserved": sm_packet["coordinate_system"]["codomain_real_dimension"] == 72
        and sm_packet["coordinate_system"]["columns"] == ["phase_packet", "shift_packet"],
        "G3_stationary_trace_layer_closed": stationary["selected_source_verified"] is True
        and stationary["selected_projector_source_verified"] is True
        and stationary["selected_riesz_green_source_verified"] is True
        and stationary["selected_rho_s_validator_ready"] is True
        and stationary["transport_closed_finite_validator_replay"] is True
        and stationary["symbolic_transport_conjugation_validator_extended"] is True
        and stationary["functional_gauge_transported_trace_proved"] is True,
        "G4_stationary_trace_does_not_overclaim_C1": stationary[
            "selected_dotD_source_verified_inside_stationary_transport_replay"
        ]
        is False
        and stationary["alpha1_driver_verified_inside_stationary_transport_replay"] is False
        and boundary["all_support_shapes_present"] is True
        and boundary["all_selected_values_emitted"] is False
        and boundary["finite_Hessian_C1_source_selected"] is False
        and boundary["primitive_C1_contractions_selected"] is False
        and boundary["dotD_alpha1_selected_inside_phifin_payload"] is False,
        "G5_crossrepo_alpha1_support_not_promotion": stationary["crossrepo_alpha1_dotD_support"][
            "import_available"
        ]
        is True
        and stationary["crossrepo_alpha1_dotD_support"]["selected_dotD_source_verified_imported"] is True
        and stationary["crossrepo_alpha1_dotD_support"]["alpha1_driver_verified_imported"] is True
        and stationary["crossrepo_alpha1_dotD_support"]["primitive_C1_contractions_claimed_by_import"]
        is False
        and stationary["crossrepo_alpha1_dotD_support"]["A_selected_claimed_by_import"] is False
        and stationary["crossrepo_alpha1_dotD_support"]["b_selected_claimed_by_import"] is False,
        "G6_identity_attempt_open_with_conditional_values_preserved": identity[
            "stationary_trace_sufficient_for_C1_transfer_identity"
        ]
        is False
        and identity["selected_identity_proved_now"] is False
        and identity["normal_form_values_not_promoted_now"] is True
        and len(identity["missing_dynamic_objects"]) == 5
        and identity["if_future_identity_proved_then_values"]["deltaTheta_C1"] == [1.0, 1.0],
        "G7_galerkin_run_still_open": galerkin["stationary_support_reused"][
            "stationary_support_closed_by_transport_conjugation"
        ]
        is True
        and galerkin["open_dynamic_stages"]["C1_manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING"
        and galerkin["open_dynamic_stages"]["C1_manifest_selected_source_verified"] is False
        and galerkin["can_promote_honest_galerkin_C1_now"] is False,
        "G8_no_target_or_closure_overclaim": sm_packet["closure_claimed"] is False
        and sm_packet["selected_PhiFinC1_identity_claimed"] is False
        and sm_packet["A_selected_claimed"] is False
        and sm_packet["b_selected_claimed"] is False
        and sm_packet["deltaTheta_C1_claimed"] is False
        and sm_packet["Galerkin_C1_contractions_claimed"] is False
        and sm_packet["observed_data_used"] is False
        and sm_packet["target_fitting_used"] is False,
    }

    return {
        "packet": "PhiFinC1_DynamicTransferIdentity_Proof_or_GalerkinContractions_Run_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "sm_phifinc1_packet": str(SM_PACKET),
            "sm_phifinc1_certificate": str(SM_CERT),
        },
        "theorem": {
            "name": "StationaryPhiFinTraceNotC1TransferImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected stationary PhiFin trace and symbolic transport "
                "conjugation close projector/Riesz/Green/rho_s source support, "
                "but they do not prove the differentiated PhiFinC1 dynamic "
                "transfer identity. The normal-form values remain conditional "
                "until differentiated PhiFinC1 primitive overlap contractions "
                "or an honest selected Galerkin C1 run emit the selected response."
            ),
        },
        "checks": checks,
        "coordinate_system": sm_packet["coordinate_system"],
        "stationary_trace_import": stationary,
        "phifin_payload_boundary": boundary,
        "PhiFinC1_identity_attempt": identity,
        "Galerkin_run_attempt": galerkin,
        "partial_promotion_theorem": theorem,
        "promotion_decision": sm_packet["promotion_decision"],
        "what_closes_now": sm_packet["what_closes_now"],
        "what_remains_open": sm_packet["what_remains_open"],
        "frontier_update": {
            "old_next": previous["next_required_artifact"],
            "current_next": NEXT,
            "why": (
                "Stationary PhiFin source transport is closed, but C1 promotion "
                "requires differentiated PhiFinC1 primitive overlap contractions "
                "or an honest Galerkin C1 run."
            ),
        },
        "guardrails": {
            "stationary_source_layer_promoted": True,
            "selected_PhiFinC1_identity_claimed": False,
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
        "certificate": "PhiFinC1DynamicTransferIdentityProofOrGalerkinContractionsRunImport",
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
    values = packet["PhiFinC1_identity_attempt"]["if_future_identity_proved_then_values"]
    return f"""# PhiFinC1 DynamicTransferIdentity Proof or GalerkinContractions Run Import v1

Status: `{cert["status"]}`.

## Closed

The stationary PhiFin trace and symbolic transport-conjugation layer close the
selected stationary projector/Riesz/Green/rho_s source support.

## Boundary

This stationary trace theorem is not the differentiated `Phi_fin^C1` transfer
identity. The conditional normal-form values remain unpromoted:

```text
A^T A = {values["Gram_A_transpose_A"]}
A^T b = {values["A_transpose_b"]}
deltaTheta_C1 = {values["deltaTheta_C1"]}
```

The live target is differentiated PhiFinC1 primitive overlap contractions, or an
honest selected Galerkin C1 run in the fixed 72-real coordinate system.

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

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
