"""Import spectral Galerkin projector-retention reduction."""

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

PREVIOUS = CERTS / "phifin_alpha1_payload_attempt_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "selected_spectral_galerkin_projector_retention_data.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "selected_spectral_galerkin_projector_retention_data_certificate.json"

OUTPUT_PACKET = DATA / "spectral_galerkin_projector_retention_reduction_import.candidate.json"
OUTPUT_CERT = CERTS / "spectral_galerkin_projector_retention_reduction_import_certificate.json"
OUTPUT_NOTE = CORPUS / "SpectralGalerkin_ProjectorRetention_Reduction_Import_v1.md"

STATUS = "SPECTRAL_GALERKIN_PROJECTOR_RETENTION_IMPORTED_ROUTEC_SOLVE_OPEN"
PREVIOUS_STATUS = "PHIFIN_ALPHA1_PAYLOAD_ATTEMPT_IMPORTED_SPECTRAL_VALUES_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_SPECTRAL_GALERKIN_PROJECTOR_RETENTION_DATA_REDUCED_TO_SELECTED_ROUTEC_GALERKIN_SOLVE"
NEXT = "MTT_Selected_RouteC_Strominger_Galerkin_Solve_Spec_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)
    projector = upstream["two_layer_projector_audit"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_Spectral_Galerkin_Projector_Retention_Data_v1",
        "F1_upstream_reduction_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["closure_claimed"] is False
        and upstream_cert["primary_next_artifact"] == NEXT,
        "F3_block_layer_closed_but_spectral_layer_open": projector["layer_separation_honest"] is True
        and projector["block_projector_layer"]["block_family_Higgs_projector_retention"] is True
        and projector["spectral_projector_layer"]["coherent_spectral_zero_mode_projector_retention"] is False
        and projector["spectral_projector_layer"]["selected_D_E_dotD_Riesz_Green"] is False,
        "F4_corpus_support_available": all(upstream["corpus_support"].values()),
        "F5_selected_solve_contract_built": upstream["selected_solve_contract"]["name"] == "SelectedRouteCStromingerGalerkinResidualSolve"
        and "coherent spectral projectors proved, not merely block projectors" in upstream["selected_solve_contract"]["acceptance"],
        "F6_no_overclaim": upstream_cert["target_fitting_used"] is False
        and upstream_cert["closure_claimed"] is False,
    }

    return {
        "packet": "SpectralGalerkin_ProjectorRetention_Reduction_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
        },
        "theorem": {
            "name": "SpectralGalerkinProjectorRetentionReductionImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "Block-family/Higgs projector retention is closed for the selected "
                "twisted S3 source, but coherent spectral zero-mode projector "
                "retention remains open and reduces to an honest selected Route-C/"
                "Strominger Galerkin residual solve."
            ),
        },
        "checks": checks,
        "upstream_spectral_projector_retention": upstream,
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_coherent_spectral_projector_retention": False,
            "claims_selected_DE_Riesz_Green_dotD_values": False,
            "claims_selected_HYM_Strominger_metric_connection": False,
            "claims_operator_level_projective_rhoE": False,
            "claims_zero_mode_bases_or_primitive_C1": False,
            "claims_finite_C1_Hessian_deltaTheta_dotD": False,
            "claims_full_SM_or_no_knob_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SpectralGalerkinProjectorRetentionReductionImport",
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
    return f"""# SpectralGalerkin ProjectorRetention Reduction Import v1

Status: `{cert["status"]}`.

Block-sector projector retention is closed for the selected twisted S3 source.
That is not enough for the `D_E/dotD` layer: coherent spectral zero-mode
projector retention, selected `D_E/Riesz/Green/dotD`, zero-mode bases, and C1
data remain open.

The next object is the selected Route-C/Strominger Galerkin residual solve with
gap/error bounds and emitted operator data.

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
