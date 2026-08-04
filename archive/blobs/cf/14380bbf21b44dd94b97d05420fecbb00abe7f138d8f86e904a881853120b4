"""Import selected Route-C/Strominger Galerkin solve specification."""

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

PREVIOUS = CERTS / "spectral_galerkin_projector_retention_reduction_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "selected_routec_strominger_galerkin_solve_spec.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "selected_routec_strominger_galerkin_solve_spec_certificate.json"

OUTPUT_PACKET = DATA / "routec_strominger_galerkin_solve_spec_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_strominger_galerkin_solve_spec_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_Strominger_Galerkin_SolveSpec_Import_v1.md"

STATUS = "ROUTEC_STROMINGER_GALERKIN_SOLVE_SPEC_IMPORTED_FIRST_RUN_OPEN"
PREVIOUS_STATUS = "SPECTRAL_GALERKIN_PROJECTOR_RETENTION_IMPORTED_ROUTEC_SOLVE_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_ROUTEC_STROMINGER_GALERKIN_SOLVE_SPEC_BUILT_VALUES_OPEN"
NEXT = "MTT_Selected_RouteC_Strominger_Galerkin_First_Run_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_RouteC_Strominger_Galerkin_Solve_Spec_v1",
        "F1_upstream_spec_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["closure_claimed"] is False
        and upstream_cert["primary_next_artifact"] == NEXT,
        "F3_mesh_accounting_reproduced": upstream["mesh_scaffold"]["matches_certificate_counts"] is True
        and upstream["mesh_scaffold"]["counts"]["mesh_N"] == 1,
        "F4_execution_stages_complete": [stage["stage"] for stage in upstream["execution_stages"]]
        == [
            "S0_selected_source",
            "S1_basis_and_domain",
            "S2_connection_metric_rhoE",
            "S3_sector_operators",
            "S4_spectral_projectors",
            "S5_alpha1_response",
            "S6_c1_contractions",
        ],
        "F5_acceptance_contracts_built": upstream["residual_acceptance"]["selected_source_rule"].startswith("selected_source_verified must be true")
        and upstream["spectral_acceptance"]["basis_minimum"].startswith("The solve must use a quotient-valid basis")
        and upstream["promotion_gate"]["must_pass_after_outputs_exist"] is True,
        "F6_values_remain_open": upstream["currently_blocked_by"]["actual_selected_values"] is True
        and upstream["basis_protocol"]["non_invariant_protocol_values_open"]["basis_B_N"] is True
        and upstream["residual_acceptance"]["positive_gates"]["mtt_hessian_min_eigenvalue"] is None,
        "F7_no_overclaim": upstream_cert["target_fitting_used"] is False
        and upstream_cert["closure_claimed"] is False,
    }

    return {
        "packet": "RouteC_Strominger_Galerkin_SolveSpec_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
        },
        "theorem": {
            "name": "RouteCStromingerGalerkinSolveSpecImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected Route-C/Strominger Galerkin solve is specified as "
                "an executable finite contract with S0-S6 stages, residual and "
                "spectral acceptance rules, output manifest, and validator order. "
                "It does not compute selected values; first run remains open."
            ),
        },
        "checks": checks,
        "upstream_routec_solve_spec": upstream,
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_actual_selected_small_N_solve": False,
            "claims_selected_rhoE_metric_connection_values": False,
            "claims_actual_basis_BN_or_quadrature": False,
            "claims_selected_DE_Riesz_Green_dotD_outputs": False,
            "claims_spectral_gap_error_numbers": False,
            "claims_zero_mode_bases_or_C1_primitives": False,
            "claims_full_SM_or_no_knob_closure": False,
            "uses_observed_masses_mixings_or_benchmark_matrices": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCStromingerGalerkinSolveSpecImport",
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
    return f"""# RouteC Strominger Galerkin SolveSpec Import v1

Status: `{cert["status"]}`.

The selected Route-C/Strominger Galerkin solve is now an executable spec.  It
locks stages `S0` through `S6`, the residual acceptance rule, the spectral
gap/error rule, the validator order, and the output manifest for the first run.

It does not compute selected values.  The next task is the first honest selected
small-`N` solve or symbolic selected ansatz.

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
