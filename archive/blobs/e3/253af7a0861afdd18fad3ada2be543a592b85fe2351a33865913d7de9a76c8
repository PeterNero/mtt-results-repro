"""Import selected Phi_fin alpha1 payload attempt."""

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

PREVIOUS = CERTS / "source_origin_alpha1_driver_reduction_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "selected_phifin_alpha1_payload.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "selected_phifin_alpha1_payload_certificate.json"

OUTPUT_PACKET = DATA / "phifin_alpha1_payload_attempt_import.candidate.json"
OUTPUT_CERT = CERTS / "phifin_alpha1_payload_attempt_import_certificate.json"
OUTPUT_NOTE = CORPUS / "PhiFinAlpha1_Payload_Attempt_Import_v1.md"

STATUS = "PHIFIN_ALPHA1_PAYLOAD_ATTEMPT_IMPORTED_SPECTRAL_VALUES_OPEN"
PREVIOUS_STATUS = "SOURCE_ORIGIN_ALPHA1_DRIVER_IMPORTED_PHIFIN_PAYLOAD_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_PHIFIN_ALPHA1_PAYLOAD_ATTEMPT_BUILT_SELECTED_SPECTRAL_VALUES_OPEN"
NEXT = "MTT_Selected_Spectral_Galerkin_Projector_Retention_Data_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)
    summary = upstream["payload_summary"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_PhiFin_Alpha1_Payload_v1",
        "F1_upstream_attempt_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["closure_claimed"] is False
        and upstream_cert["primary_next_artifact"] == NEXT,
        "F3_support_shapes_all_present": summary["all_support_shapes_present"] is True
        and all(summary["support_candidate_present"].values()),
        "F4_selected_payload_values_all_open": summary["all_selected_values_emitted"] is False
        and all(flag is False for flag in summary["selected_payload_flags"].values()),
        "F5_projective_support_not_promoted_as_values": upstream["projective_gerbe_support"]["source_level_promoted"] is True
        and upstream["projective_gerbe_support"]["operator_level_projective_rhoE_promoted"] is False
        and upstream["projective_gerbe_support"]["uses_projective_prototype_as_selected"] is False,
        "F6_next_blocker_is_spectral_galerkin": upstream["next_blocker"]["name"] == "SelectedSpectralGalerkinProjectorRetentionData"
        and "coherent spectral projector retention for Q,u,d,L,e,N,H" in upstream["next_blocker"]["must_supply"],
        "F7_no_overclaim": upstream_cert["target_fitting_used"] is False
        and upstream_cert["closure_claimed"] is False,
    }

    return {
        "packet": "PhiFinAlpha1_Payload_Attempt_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
        },
        "theorem": {
            "name": "PhiFinAlpha1PayloadAttemptImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected Phi_fin alpha1 payload attempt shows broad finite "
                "support is present, but no selected payload values are emitted. "
                "The straight smoke-promotion path is rejected; the next hard "
                "object is selected spectral Galerkin projector-retention data."
            ),
        },
        "checks": checks,
        "upstream_phifin_alpha1_payload": upstream,
        "what_closes_now": {
            "selected_payload_attempt_built": True,
            "projective_rhoE_support_candidate_imported": True,
            "block_factorized_sector_support_imported": True,
            "routec_de_green_dotd_shapes_imported": True,
            "c1_alpha1_operator_contract_imported": True,
            "straight_smoke_promotion_rejected": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_PhiFin_alpha1_payload_values": True,
            "selected_twist_and_source_verification": True,
            "operator_level_projective_rhoE_promotion": True,
            "coherent_spectral_projector_retention": True,
            "selected_D_E_Riesz_Green_dotD_values": True,
            "finite_C1_Hessian_and_deltaTheta": True,
            "zero_mode_bases_and_primitive_contractions": True,
            "A_selected": True,
            "b_selected": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_PhiFin_alpha1_payload_values": False,
            "claims_selected_twist_or_source_verification": False,
            "claims_operator_level_projective_rhoE_promotion": False,
            "claims_coherent_spectral_projector_retention": False,
            "claims_selected_DE_Riesz_Green_dotD_values": False,
            "claims_finite_C1_Hessian_or_deltaTheta": False,
            "claims_zero_mode_bases_or_primitive_contractions": False,
            "claims_A_selected_or_b_selected": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "uses_observed_constants_masses_or_CKM_phase": False,
            "uses_benchmark_matrices_or_target_residuals": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "PhiFinAlpha1PayloadAttemptImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    return f"""# PhiFinAlpha1 Payload Attempt Import v1

Status: `{cert["status"]}`.

The selected `Phi_fin alpha1` payload attempt is imported.  The support layer is
broad enough: projective `rho_E`, block-factorized sectors, Route-C
`D_E/Riesz/Green/dotD` shapes, and the C1 alpha1 response contract all exist as
support candidates.

No selected payload values are emitted.  Every selected payload flag remains
false, so the smoke/prototype packets are not promoted.  The next hard object is
selected spectral Galerkin projector-retention data for the same branch.

Next artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
