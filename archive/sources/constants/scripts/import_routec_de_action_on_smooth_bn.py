"""Import selected Route-C D_E action on smooth B_N matrix scaffold."""

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

PREVIOUS = CERTS / "routec_smooth_bn_galerkin_lift_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "selected_routec_de_action_on_smooth_bn.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "selected_routec_de_action_on_smooth_bn_certificate.json"
UPSTREAM_PAYLOAD_DIR = SM / "candidate_data" / "selected_routec_de_action_on_smooth_bn"

OUTPUT_PACKET = DATA / "routec_de_action_on_smooth_bn_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_de_action_on_smooth_bn_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_DE_Action_on_Smooth_BN_Import_v1.md"

STATUS = "ROUTEC_DE_ACTION_ON_SMOOTH_BN_IMPORTED_SOURCE_PROMOTION_OPEN"
PREVIOUS_STATUS = "ROUTEC_SMOOTH_BN_GALERKIN_LIFT_IMPORTED_SELECTED_DE_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_ROUTEC_DE_ACTION_ON_SMOOTH_BN_MATRIX_BUILT_SOURCE_PROMOTION_OPEN"
NEXT = "MTT_Selected_RouteC_Sector_Projectors_and_DotD_on_Smooth_BN_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)
    honest_payload = UPSTREAM_PAYLOAD_DIR / "de_action_on_smooth_bn.honest.json"
    diagnostic_payload = UPSTREAM_PAYLOAD_DIR / "de_action_on_smooth_bn.source_lift_diagnostic.json"
    honest = load(honest_payload)
    diagnostic = load(diagnostic_payload)
    validation = upstream["validation"]
    matrix = validation["matrix_consistency"]
    straight = upstream["superset_mode"]["straight_path"]
    honest_text = "\n".join(validation["honest"]["output"])
    diagnostic_text = "\n".join(validation["diagnostic_source_lift"]["output"])

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_RouteC_DE_Action_on_Smooth_BN_v1",
        "F1_upstream_packet_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["candidate_path"].endswith("selected_routec_de_action_on_smooth_bn.candidate.json"),
        "F3_payloads_present_and_typed": honest_payload.exists()
        and diagnostic_payload.exists()
        and honest["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3"
        and honest["candidate_kind"] == "honest_unpromoted_model_active_DE_action"
        and honest["selected_source_verified"] is False
        and diagnostic["selected_source_verified"] is True
        and diagnostic["claims_physical_selected_source"] is False,
        "F4_honest_validator_rejects_source_promotion": validation["honest"]["exit_code"] == 1
        and "selected_source_verified is not true" in honest_text
        and straight["honest_validator_promotes"] is False,
        "F5_diagnostic_source_lift_passes_matrix_gates": validation["diagnostic_source_lift"]["exit_code"] == 0
        and "D_E action validation PASS" in diagnostic_text
        and straight["diagnostic_lift_passes"] is True,
        "F6_matrix_consistency_emitted": matrix["domain_dimension"] == 27
        and matrix["family_kernel_dimension"] == 3
        and matrix["higgs_kernel_dimension"] == 1
        and matrix["diagnostic_lift_validator_passes"] is True,
        "F7_closes_only_model_active_matrix_layer": upstream["what_closes_now"][
            "D_E_matrix_on_27_mode_BN_emitted"
        ]
        is True
        and upstream["what_closes_now"]["stiffness_equals_DstarD"] is True
        and upstream["what_closes_now"]["zero_mode_bases_ordered"] is True
        and upstream["what_remains_open"]["selected_D_E_source_promotion"] is True
        and upstream["what_remains_open"]["full_iwasawa_strominger_DE_action_not_only_model_active"] is True,
        "F8_no_full_replay_or_closure": upstream["what_remains_open"]["R6_replay_without_lifted_flags"] is True
        and upstream["what_remains_open"]["dotD_alpha1_in_same_basis"] is True
        and upstream["what_remains_open"]["sector_projectors"] is True
        and upstream["what_remains_open"]["full_SM_or_no_knob_closure"] is True,
    }

    summary = {
        "basis_id": honest["basis_id"],
        "domain_dimension": matrix["domain_dimension"],
        "family_kernel_dimension": matrix["family_kernel_dimension"],
        "higgs_kernel_dimension": matrix["higgs_kernel_dimension"],
        "honest_selected_source_verified": honest["selected_source_verified"],
        "honest_validator_exit_code": validation["honest"]["exit_code"],
        "diagnostic_selected_source_verified": diagnostic["selected_source_verified"],
        "diagnostic_claims_physical_selected_source": diagnostic["claims_physical_selected_source"],
        "diagnostic_validator_exit_code": validation["diagnostic_source_lift"]["exit_code"],
        "model_active_DE_only": True,
    }

    return {
        "packet": "RouteC_DE_Action_on_Smooth_BN_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
            "upstream_payload_dir": str(UPSTREAM_PAYLOAD_DIR),
        },
        "theorem": {
            "name": "RouteCDEActionOnSmoothBNImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "A finite model-active D_E matrix realization has been emitted "
                "on the imported 27-mode smooth B_N scaffold.  The diagnostic "
                "source-lift packet validates the matrix, Gram, stiffness, and "
                "zero-mode data, while the honest packet still fails source "
                "promotion.  Therefore this closes the finite matrix layer but "
                "not selected D_E source promotion, full Iwasawa/Strominger D_E, "
                "sector projectors, dotD_alpha1, C1 response, or honest replay."
            ),
        },
        "checks": checks,
        "de_action_summary": summary,
        "upstream_de_action_on_smooth_bn": upstream,
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_selected_DE_source_promotion": False,
            "claims_full_iwasawa_strominger_DE_action": False,
            "claims_sector_projectors_constructed": False,
            "claims_dotD_alpha1_in_same_basis": False,
            "claims_C1_response": False,
            "claims_honest_replay_ready": False,
            "claims_full_SM_or_no_knob_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCDEActionOnSmoothBNImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "de_action_summary": packet["de_action_summary"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    summary = cert["de_action_summary"]
    return f"""# RouteC DE Action on Smooth BN Import v1

Status: `{cert["status"]}`.

The Route-C branch now imports a finite model-active `D_E` action on the same
smooth `B_N` scaffold.  The emitted matrix layer has domain dimension
`{summary["domain_dimension"]}`, family kernel dimension
`{summary["family_kernel_dimension"]}`, and Higgs kernel dimension
`{summary["higgs_kernel_dimension"]}`.  The diagnostic source-lift packet passes
the matrix validator.

This is not selected-source closure.  The honest packet still has
`selected_source_verified = false` and fails the validator for that reason.
Thus the matrix scaffold is usable as the next carrier, but selected `D_E`
source promotion, full Iwasawa/Strominger `D_E`, sector projectors,
`dotD_alpha1`, C1 response, and honest replay remain open.

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
