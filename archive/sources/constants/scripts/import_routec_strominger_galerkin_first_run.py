"""Import selected Route-C/Strominger Galerkin first-run manifest."""

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

PREVIOUS = CERTS / "routec_strominger_galerkin_solve_spec_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "selected_routec_strominger_galerkin_first_run.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "selected_routec_strominger_galerkin_first_run_certificate.json"

OUTPUT_PACKET = DATA / "routec_strominger_galerkin_first_run_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_strominger_galerkin_first_run_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_Strominger_Galerkin_FirstRun_Import_v1.md"

STATUS = "ROUTEC_STROMINGER_GALERKIN_FIRST_RUN_IMPORTED_SELECTOR_OPEN"
PREVIOUS_STATUS = "ROUTEC_STROMINGER_GALERKIN_SOLVE_SPEC_IMPORTED_FIRST_RUN_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_ROUTEC_STROMINGER_GALERKIN_FIRST_RUN_MANIFEST_FILLED_SELECTOR_OPEN"
NEXT = "MTT_Selected_RouteC_Source_Selector_and_Basis_Theorem_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)
    formal = upstream["validation"]["formal_lift_diagnostic"]
    honest = upstream["validation"]["honest_root"]
    manifest_filled = upstream["manifest_filled"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_RouteC_Strominger_Galerkin_First_Run_v1",
        "F1_upstream_first_run_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["closure_claimed"] is False
        and upstream_cert["proof_promotion_allowed"] is False
        and upstream_cert["primary_next_artifact"] == NEXT,
        "F3_all_manifest_slots_filled": all(manifest_filled.values())
        and set(manifest_filled)
        == {
            "c1_primitive_contractions",
            "de_action",
            "dotd_response",
            "reduced_green",
            "rhoE_mesh",
            "rhoE_metric",
            "riesz_gap",
            "route_c_residual",
            "sector_maps",
            "spectral_galerkin_data",
        },
        "F4_honest_root_remains_unselected": upstream["root_payload"]["claims_selected_source"] is False
        and upstream["root_payload"]["selected_source_verified"] is False
        and upstream["validation"]["honest_root_all_pass"] is False
        and honest["route_c_residual"]["passed"] is False,
        "F5_formal_lift_is_diagnostic_only": upstream["formal_lift_payload"]["claims_selected_source"] is False
        and upstream["formal_lift_payload"]["selected_source_verified"] is True
        and upstream["validation"]["formal_lift_lower_validators_all_pass"] is True
        and upstream["validation"]["formal_lift_promotion_passes"] is True
        and upstream["interpretation"]["proof_promotion_allowed"] is False,
        "F6_downstream_shape_validators_pass_under_lift": all(value["passed"] is True for value in formal.values()),
        "F7_selected_source_gap_isolated": upstream["interpretation"]["selector_provenance_obstruction_found"] is True
        and upstream["what_closes_now"]["selected_source_gap_isolated"] is True
        and upstream["what_remains_open"]["actual_selected_hym_strominger_source"] is True
        and upstream["what_remains_open"]["quotient_valid_selected_galerkin_basis_BN"] is True,
        "F8_no_overclaim": upstream_cert["target_fitting_used"] is False
        and upstream_cert["closure_claimed"] is False
        and upstream_cert["proof_promotion_allowed"] is False,
    }

    return {
        "packet": "RouteC_Strominger_Galerkin_FirstRun_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
        },
        "theorem": {
            "name": "RouteCStromingerGalerkinFirstRunImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The first-run Route-C/Strominger Galerkin manifest is filled "
                "and the lifted-source diagnostic validates the downstream "
                "finite algebra.  The honest root payload remains unselected, "
                "so proof promotion is forbidden until MTT derives the selected "
                "HYM/Strominger source and quotient-valid Galerkin basis."
            ),
        },
        "checks": checks,
        "upstream_first_run": upstream,
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_selected_source_theorem": False,
            "claims_quotient_valid_selected_basis_BN": False,
            "claims_honest_root_manifest_passes": False,
            "promotes_formal_lift_to_proof": False,
            "claims_primitive_C1_contractions": False,
            "claims_spectral_projector_error_bounds": False,
            "claims_proof_usable_de_response_packet": False,
            "claims_full_SM_or_no_knob_closure": False,
            "uses_observed_masses_mixings_or_benchmark_matrices": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCStromingerGalerkinFirstRunImport",
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
    return f"""# RouteC Strominger Galerkin FirstRun Import v1

Status: `{cert["status"]}`.

The selected Route-C/Strominger Galerkin first-run manifest is filled.  This is
substantial: all declared finite files exist, the downstream finite algebra can
be tested, and the formal-lift diagnostic passes the lower validators.

It is not proof promotion.  The honest root payload still has selected-source
flags false, and the formal lift is diagnostic only.  The missing object is now
sharp: MTT must derive the selected HYM/Strominger source and a quotient-valid
Galerkin basis, then rerun the same manifest without lifted flags.

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
