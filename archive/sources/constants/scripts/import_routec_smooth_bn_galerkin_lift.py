"""Import selected Route-C smooth B_N Galerkin lift scaffold."""

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

PREVIOUS = CERTS / "routec_nonidentity_rhoe_bn_construction_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "selected_routec_smooth_bn_galerkin_lift_certificate.json"

OUTPUT_PACKET = DATA / "routec_smooth_bn_galerkin_lift_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_smooth_bn_galerkin_lift_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_Smooth_BN_GalerkinLift_Import_v1.md"

STATUS = "ROUTEC_SMOOTH_BN_GALERKIN_LIFT_IMPORTED_SELECTED_DE_OPEN"
PREVIOUS_STATUS = "ROUTEC_NONIDENTITY_RHOE_PACKET_IMPORTED_SMOOTH_BN_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_ROUTEC_SMOOTH_BN_GALERKIN_LIFT_SCAFFOLD_BUILT_SELECTED_DE_STILL_OPEN"
NEXT = "MTT_Selected_RouteC_DE_Action_on_Smooth_BN_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def is_identity(matrix: list[list[float]]) -> bool:
    return all(
        abs(value - (1.0 if i == j else 0.0)) < 1e-12
        for i, row in enumerate(matrix)
        for j, value in enumerate(row)
    )


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)
    lift = upstream["B_N_lift"]
    gates = upstream["gates"]
    fields = upstream["contract_comparison"]["fields_emitted_now"]
    missing = upstream["contract_comparison"]["still_missing_for_full_contract"]
    straight = upstream["superset_mode"]["straight_path"]
    equivariance = lift["bundle_equivariance"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_RouteC_Smooth_BN_Galerkin_Lift_v1",
        "F1_upstream_packet_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["candidate_path"].endswith("selected_routec_smooth_bn_galerkin_lift.candidate.json"),
        "F3_smooth_basis_and_quadrature_emitted": lift["dimension"] == 27
        and len(lift["basis"]) == 27
        and len(lift["quadrature_rule"]["nodes"]) == 9
        and fields["scalar_basis_functions_phi_m"] is True
        and fields["metric_volume_quadrature"] is True,
        "F4_gram_and_stiffness_model_active_gates": is_identity(lift["gram_matrix"])
        and gates["Gram_matrix_positive_definite"] is True
        and fields["Gram_matrix_entries"] is True
        and gates["stiffness_matrix_positive_semidefinite"] is True
        and fields["stiffness_matrix_entries"] is True,
        "F5_kernel_gap_riesz_green_model_active": lift["zero_cluster"]["dimension"] == 3
        and lift["complement_gap"] > 0
        and gates["kernel_dimension_is_three"] is True
        and gates["complement_gap_positive"] is True
        and gates["Riesz_projector_constructed"] is True
        and gates["reduced_Green_operator_constructed"] is True
        and fields["Riesz_projectors"] is True
        and fields["reduced_Green_operators"] is True,
        "F6_projective_twisted_equivariance_only": equivariance["ordinary_bundle_equivariance"] is False
        and equivariance["projective_equivariance_up_to_central_phase"] is True
        and gates["bundle_equivariance_projective_only"] is True
        and gates["basis_extends_beyond_left_invariant_forms"] is True,
        "F7_selected_DE_and_sector_data_still_open": gates["selected_D_E_action_on_basis"] is False
        and gates["sector_projection_maps_constructed"] is False
        and gates["dotD_alpha1_and_Green_operator_constructed"] is False
        and gates["truncation_error_certified_for_full_iwasawa_operator"] is False
        and missing["selected_D_E_action_on_basis"] is True
        and missing["sector_projection_maps_constructed"] is True
        and missing["dotD_alpha1_in_same_basis"] is True
        and missing["full_iwasawa_operator_truncation_error"] is True,
        "F8_straight_path_remains_partial": straight["smooth_BN_scaffold_built"] is True
        and straight["full_BN_payload_gate"] is False
        and straight["selected_DE_action_emitted"] is False
        and straight["honest_replay_ready"] is False,
        "F9_no_target_fit_or_closure_overclaim": upstream["target_fitting_used"] is False
        and upstream["what_remains_open"]["full_SM_or_no_knob_closure"] is True,
    }

    summary = {
        "basis_id": lift["basis_id"],
        "dimension": lift["dimension"],
        "basis_count": len(lift["basis"]),
        "quadrature_nodes": len(lift["quadrature_rule"]["nodes"]),
        "zero_cluster_dimension": lift["zero_cluster"]["dimension"],
        "complement_gap": lift["complement_gap"],
        "ordinary_bundle_equivariance": equivariance["ordinary_bundle_equivariance"],
        "projective_equivariance_up_to_central_phase": equivariance[
            "projective_equivariance_up_to_central_phase"
        ],
        "model_active_laplacian_only": True,
        "selected_DE_action_on_basis": gates["selected_D_E_action_on_basis"],
        "sector_projection_maps_constructed": gates["sector_projection_maps_constructed"],
        "dotD_alpha1_and_Green_operator_constructed": gates[
            "dotD_alpha1_and_Green_operator_constructed"
        ],
        "full_iwasawa_truncation_error_certified": gates[
            "truncation_error_certified_for_full_iwasawa_operator"
        ],
    }

    return {
        "packet": "RouteC_Smooth_BN_GalerkinLift_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
        },
        "theorem": {
            "name": "RouteCSmoothBNGalerkinLiftImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The Route-C branch now has a smooth 27-mode Galerkin B_N "
                "scaffold with metric quadrature, Gram/stiffness matrices, "
                "a three-dimensional model-active kernel, positive complement "
                "gap, Riesz projector, and reduced Green operator.  This is "
                "only a model-active Galerkin lift: selected D_E action, "
                "sector projectors, dotD_alpha1 response, full Iwasawa "
                "truncation error, and honest replay remain open."
            ),
        },
        "checks": checks,
        "smooth_bn_summary": summary,
        "upstream_smooth_bn_lift": upstream,
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_selected_DE_action_on_basis": False,
            "claims_sector_projectors_constructed": False,
            "claims_dotD_alpha1_in_same_basis": False,
            "claims_full_iwasawa_truncation_error": False,
            "claims_full_BN_payload_gate": False,
            "claims_honest_replay_ready": False,
            "claims_full_SM_or_no_knob_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCSmoothBNGalerkinLiftImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "smooth_bn_summary": packet["smooth_bn_summary"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    summary = cert["smooth_bn_summary"]
    return f"""# RouteC Smooth BN Galerkin Lift Import v1

Status: `{cert["status"]}`.

The Route-C branch now imports the smooth `B_N` Galerkin scaffold.  The lift has
dimension `{summary["dimension"]}`, `{summary["quadrature_nodes"]}` metric
quadrature nodes, a three-dimensional model-active kernel, and positive
complement gap `{summary["complement_gap"]:.12g}`.  The model-active
Gram/stiffness, Riesz projector, and reduced Green data are emitted.

This is not a full straight proof.  The imported object is projectively
equivariant rather than ordinarily equivariant, and it remains a model-active
Galerkin scaffold until the selected `D_E` action on the same basis, sector
projectors, `dotD_alpha1` response, and full Iwasawa truncation-error certificate
are supplied.

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
