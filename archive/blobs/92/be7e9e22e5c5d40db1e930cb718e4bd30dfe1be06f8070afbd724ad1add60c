"""Import selected Route-C sector projectors and dotD on smooth B_N scaffold."""

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

PREVIOUS = CERTS / "routec_de_action_on_smooth_bn_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "selected_routec_sector_projectors_dotd_on_smooth_bn_certificate.json"
UPSTREAM_PAYLOAD_DIR = SM / "candidate_data" / "selected_routec_sector_projectors_dotd_on_smooth_bn"

OUTPUT_PACKET = DATA / "routec_sector_projectors_dotd_on_smooth_bn_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_sector_projectors_dotd_on_smooth_bn_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_SectorProjectors_DotD_on_Smooth_BN_Import_v1.md"

STATUS = "ROUTEC_SECTOR_PROJECTORS_DOTD_ON_SMOOTH_BN_IMPORTED_C1_SOURCE_OPEN"
PREVIOUS_STATUS = "ROUTEC_DE_ACTION_ON_SMOOTH_BN_IMPORTED_SOURCE_PROMOTION_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_ROUTEC_SECTOR_PROJECTORS_DOTD_ON_SMOOTH_BN_BUILT_SOURCE_PROMOTION_OPEN"
NEXT = "MTT_Selected_RouteC_C1_Primitive_Response_or_Selected_Source_Proof_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)
    honest_payload = UPSTREAM_PAYLOAD_DIR / "sector_projectors_dotd_on_smooth_bn.honest.json"
    diagnostic_payload = UPSTREAM_PAYLOAD_DIR / "sector_projectors_dotd_on_smooth_bn.source_lift_diagnostic.json"
    honest = load(honest_payload)
    diagnostic = load(diagnostic_payload)
    validation = upstream["validation"]
    residuals = validation["projector_residuals"]
    straight = upstream["superset_mode"]["straight_path"]
    honest_text = "\n".join(validation["honest"]["output"])
    diagnostic_text = "\n".join(validation["diagnostic_source_lift"]["output"])

    family_sectors = ("Q", "u", "d", "L", "e", "N")
    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_RouteC_Sector_Projectors_and_DotD_on_Smooth_BN_v1",
        "F1_upstream_packet_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["candidate_path"].endswith(
            "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
        ),
        "F3_payloads_present_and_typed": honest_payload.exists()
        and diagnostic_payload.exists()
        and honest["candidate_kind"] == "honest_unpromoted_model_active_dotD_response"
        and honest["selected_dotD_source_verified"] is False
        and honest["alpha1_driver_verified"] is False
        and diagnostic["selected_dotD_source_verified"] is True
        and diagnostic["alpha1_driver_verified"] is True
        and diagnostic["claims_physical_selected_source"] is False,
        "F4_honest_validator_rejects_only_source_driver_flags": validation[
            "honest_validator_fails_only_by_source_driver_flags"
        ]
        is True
        and validation["honest"]["exit_code"] == 1
        and "selected_dotD_source_verified is not true" in honest_text
        and "alpha1_driver_verified is not true" in honest_text,
        "F5_diagnostic_dotd_validator_passes": validation["diagnostic_lift_validator_passes"] is True
        and validation["diagnostic_source_lift"]["exit_code"] == 0
        and "dotD response validation PASS" in diagnostic_text,
        "F6_projectors_exact_with_expected_ranks": all(
            residuals[sector]["idempotence_residual"] == 0.0
            and residuals[sector]["hermitian_residual"] == 0.0
            and residuals[sector]["rank_trace"] == 3.0
            for sector in family_sectors
        )
        and residuals["H"]["idempotence_residual"] == 0.0
        and residuals["H"]["hermitian_residual"] == 0.0
        and residuals["H"]["rank_trace"] == 1.0,
        "F7_same_basis_finite_horizontal_response_only": upstream["superset_mode"][
            "superset_convergence"
        ]["uses_same_27_mode_BN_basis"]
        is True
        and upstream["superset_mode"]["superset_convergence"][
            "finite_horizontal_response_algebra_closed_conditionally"
        ]
        is True
        and straight["sector_projectors_on_BN_emitted"] is True
        and straight["dotD_alpha1_matrix_emitted"] is True
        and straight["honest_replay_ready"] is False,
        "F8_remaining_source_and_C1_gates_preserved": upstream["what_remains_open"][
            "selected_dotD_source_verified"
        ]
        is True
        and upstream["what_remains_open"]["alpha1_driver_verified"] is True
        and upstream["what_remains_open"]["primitive_C1_overlap_contractions"] is True
        and upstream["what_remains_open"]["honest_replay_without_lifted_flags"] is True
        and upstream["what_remains_open"]["full_SM_or_no_knob_closure"] is True,
    }

    summary = {
        "family_sector_rank": 3,
        "higgs_sector_rank": 1,
        "family_sectors": list(family_sectors),
        "projectors_idempotent_and_hermitian": True,
        "honest_selected_dotD_source_verified": honest["selected_dotD_source_verified"],
        "honest_alpha1_driver_verified": honest["alpha1_driver_verified"],
        "honest_validator_exit_code": validation["honest"]["exit_code"],
        "diagnostic_selected_dotD_source_verified": diagnostic["selected_dotD_source_verified"],
        "diagnostic_alpha1_driver_verified": diagnostic["alpha1_driver_verified"],
        "diagnostic_claims_physical_selected_source": diagnostic["claims_physical_selected_source"],
        "diagnostic_validator_exit_code": validation["diagnostic_source_lift"]["exit_code"],
        "finite_horizontal_response_algebra_only": True,
    }

    return {
        "packet": "RouteC_SectorProjectors_DotD_on_Smooth_BN_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
            "upstream_payload_dir": str(UPSTREAM_PAYLOAD_DIR),
        },
        "theorem": {
            "name": "RouteCSectorProjectorsDotDOnSmoothBNImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "Sector projectors and finite dotD_alpha1 response slots are "
                "emitted on the same 27-mode smooth B_N scaffold.  The "
                "diagnostic replay validates projector ranks and the finite "
                "horizontal response equation, but the honest packet remains "
                "unpromoted because selected dotD source and alpha1 driver "
                "theorems are still absent.  The next legal gate is primitive "
                "C1 response or a selected source proof."
            ),
        },
        "checks": checks,
        "sector_dotd_summary": summary,
        "upstream_sector_projectors_dotd_on_smooth_bn": upstream,
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_selected_dotD_source_verified": False,
            "claims_alpha1_driver_verified": False,
            "claims_primitive_C1_overlap_contractions": False,
            "claims_honest_replay_ready": False,
            "claims_full_iwasawa_strominger_DE": False,
            "claims_full_iwasawa_truncation_error": False,
            "claims_full_SM_or_no_knob_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCSectorProjectorsDotDOnSmoothBNImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "sector_dotd_summary": packet["sector_dotd_summary"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    summary = cert["sector_dotd_summary"]
    return f"""# RouteC Sector Projectors and DotD on Smooth BN Import v1

Status: `{cert["status"]}`.

The Route-C branch now imports sector projectors and `dotD_alpha1` response
slots on the same smooth `B_N` scaffold.  The finite projector layer has rank
`{summary["family_sector_rank"]}` for `Q,u,d,L,e,N` and rank
`{summary["higgs_sector_rank"]}` for `H`; the projectors are idempotent and
Hermitian, and the diagnostic replay validates the finite horizontal response
equation.

This is finite response algebra only.  The honest packet remains unpromoted
because the selected `dotD` source and `alpha1` driver flags are not
theorem-derived.  Primitive C1 overlap contractions, full Iwasawa/Strominger
replay, and no-knob SM closure remain open.

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
