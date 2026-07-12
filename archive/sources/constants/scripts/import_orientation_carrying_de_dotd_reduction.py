"""Import orientation-carrying D_E/dotD reduction to source-origin/alpha1 driver."""

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

PREVIOUS = CERTS / "same_source_symmetry_breaking_reduction_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "selected_orientation_carrying_de_dotd_source.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "selected_orientation_carrying_de_dotd_source_certificate.json"

OUTPUT_PACKET = DATA / "orientation_carrying_de_dotd_reduction_import.candidate.json"
OUTPUT_CERT = CERTS / "orientation_carrying_de_dotd_reduction_import_certificate.json"
OUTPUT_NOTE = CORPUS / "OrientationCarrying_DE_DotD_Reduction_Import_v1.md"

STATUS = "ORIENTATION_CARRYING_DE_DOTD_IMPORTED_SOURCE_ORIGIN_ALPHA1_OPEN"
PREVIOUS_STATUS = "SAME_SOURCE_SYMMETRY_BREAKING_IMPORTED_ORIENTATION_DE_DOTD_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_ORIENTATION_CARRYING_DE_DOTD_SOURCE_REDUCED_TO_SOURCE_ORIGIN_AND_ALPHA1_DRIVER"
NEXT = "MTT_Selected_Source_Origin_and_Alpha1_Driver_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)
    audit = upstream["finite_payload_audit"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_Orientation_Carrying_DE_DotD_Source_v1",
        "F1_upstream_reduction_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["closure_claimed"] is False
        and upstream_cert["primary_next_artifact"] == NEXT,
        "F3_finite_payload_shape_is_not_blocker": audit["q79_residuals_zero"] is True
        and audit["q79_positive_gates"]["mtt_hessian_min_eigenvalue"] is True
        and audit["q79_positive_gates"]["riesz_gap_min"] is True
        and audit["q79_de_action_flags"]["boundary_conditions_verified"] is True
        and audit["q79_reduced_green_flags"]["operator_data_verified"] is True
        and audit["q79_dotd_response_flags"]["green_operator_verified"] is True
        and audit["q79_dotd_response_flags"]["horizontal_gauge_verified"] is True
        and audit["q369_conjugate_shape_present"] is True,
        "F4_source_flags_are_exact_blocker": audit["q79_selected_source_verified"] is False
        and audit["q79_de_action_flags"]["selected_source_verified"] is False
        and audit["q79_reduced_green_flags"]["selected_source_verified"] is False
        and audit["q79_dotd_response_flags"]["selected_dotD_source_verified"] is False
        and audit["q79_dotd_response_flags"]["alpha1_driver_verified"] is False,
        "F5_validator_open_items_match_source_origin": "selected_by_mtt must be true" in upstream["validator_open_items"]
        and "same_branch_derivative_verified must be true" in upstream["validator_open_items"]
        and "selected_dotD_alpha1 validator did not pass (exit 1)" in upstream["validator_open_items"],
        "F6_no_overclaim": upstream_cert["target_fitting_used"] is False
        and upstream_cert["closure_claimed"] is False,
    }

    return {
        "packet": "OrientationCarrying_DE_DotD_Reduction_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
        },
        "theorem": {
            "name": "OrientationCarryingDEDotDReductionImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The orientation-carrying D_E/dotD gate is not blocked by finite "
                "operator shape: q79 has zero residual smoke, positive Hessian and "
                "Riesz gates, coherent D_E, reduced Green, and horizontal dotD; "
                "q369 reaches the conjugate layer. The exact remaining blocker is "
                "source-origin and alpha1-driver provenance."
            ),
        },
        "checks": checks,
        "upstream_orientation_carrying_de_dotd": upstream,
        "what_closes_now": {
            "finite_branch_residuals_hit_zero_in_smoke": True,
            "hessian_and_riesz_positive_in_smoke": True,
            "de_action_boundary_shapes_present": True,
            "reduced_green_riesz_shapes_present": True,
            "dotd_horizontal_green_shapes_present": True,
            "q79_q369_conjugate_pair_reaches_same_layer": True,
            "validator_stack_first_blocker_identified": True,
            "source_origin_alpha1_driver_next_gate_locked": True,
        },
        "what_remains_open": {
            "selected_source_origin": True,
            "selected_by_mtt": True,
            "visible_bundle_or_twisted_gerbe_source": True,
            "pic0_selected_or_quotiented": True,
            "selection_justified_by_source": True,
            "same_branch_derivative_verified": True,
            "selected_D_E_source_flags": True,
            "selected_Green_source_flags": True,
            "selected_dotD_source_flags": True,
            "alpha1_driver_provenance": True,
            "primitive_C1_contractions": True,
            "A_selected": True,
            "b_selected": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_source_origin": False,
            "claims_selected_by_mtt": False,
            "claims_pic0_resolution": False,
            "claims_same_branch_derivative": False,
            "claims_selected_DE_Green_dotD_flags": False,
            "claims_alpha1_driver_provenance": False,
            "claims_primitive_C1_contractions": False,
            "claims_A_selected_or_b_selected": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "uses_observed_cp_sign": False,
            "uses_observed_or_benchmark_inputs": False,
            "uses_lifted_selected_flags_as_proof": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "OrientationCarryingDEDotDReductionImport",
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
    return f"""# OrientationCarrying DEDotD Reduction Import v1

Status: `{cert["status"]}`.

The orientation-carrying `D_E/dotD` gate is now reduced to source-origin and
alpha1-driver provenance.  The finite operator payload is coherent: q79 has
zero residual smoke, positive Hessian/Riesz gates, coherent `D_E`, reduced
Green, and horizontal `dotD`; q369 reaches the conjugate layer.

This does not promote the smoke data.  The selected-source flags, Pic0/source
justification, same-branch derivative, selected `D_E/Green/dotD` validators,
alpha1 driver provenance, and primitive C1 contractions remain open.

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
