"""Import source-origin/alpha1-driver reduction to selected Phi_fin alpha1 payload."""

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

PREVIOUS = CERTS / "orientation_carrying_de_dotd_reduction_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "selected_source_origin_and_alpha1_driver.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "selected_source_origin_and_alpha1_driver_certificate.json"

OUTPUT_PACKET = DATA / "source_origin_alpha1_driver_reduction_import.candidate.json"
OUTPUT_CERT = CERTS / "source_origin_alpha1_driver_reduction_import_certificate.json"
OUTPUT_NOTE = CORPUS / "SourceOrigin_Alpha1Driver_Reduction_Import_v1.md"

STATUS = "SOURCE_ORIGIN_ALPHA1_DRIVER_IMPORTED_PHIFIN_PAYLOAD_OPEN"
PREVIOUS_STATUS = "ORIENTATION_CARRYING_DE_DOTD_IMPORTED_SOURCE_ORIGIN_ALPHA1_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_SOURCE_ORIGIN_AND_ALPHA1_DRIVER_REDUCED_TO_SELECTED_PHIFIN_ALPHA1_PAYLOAD"
NEXT = "MTT_Selected_PhiFin_Alpha1_Payload_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)

    source = upstream["source_origin_audit"]
    alpha = upstream["alpha1_driver_audit"]
    contract = upstream["unified_payload_contract"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_Source_Origin_and_Alpha1_Driver_v1",
        "F1_upstream_reduction_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["closure_claimed"] is False
        and upstream_cert["primary_next_artifact"] == NEXT,
        "F3_source_support_is_not_blocker": source["support_closed"]["same_source_support_converges"] is True
        and source["support_closed"]["s3_projective_gerbe_support_promoted"] is True
        and source["support_closed"]["visible_chern_weil_contract_reduced"] is True
        and source["ordinary_nonidentity_rhoe_retired"] is True
        and source["projective_gerbe_rhoe_live"] is True,
        "F4_payload_flags_remain_unfilled": all(flag is False for flag in source["phifin_selected_payload_flags"].values())
        and all(flag is False for flag in source["selected_flags"].values())
        and all(flag is False for flag in alpha["selected_values"].values()),
        "F5_alpha1_support_imported_but_values_open": alpha["operator_level_support"]["selected_driver_alpha1_row"] is True
        and alpha["operator_level_support"]["selected_Xi_operator_level_source"] is True
        and alpha["operator_level_support"]["single_driver_not_algebraically_fatal"] is True
        and alpha["rank_lift_condition"] == "C33(M_C1^(alpha1)) != 0",
        "F6_unified_payload_contract_is_strict": contract["name"] == "SelectedPhiFinAlpha1Payload"
        and "selected dotD_alpha1 as the same-branch derivative of selected D_E" in contract["must_emit"]
        and "no observed masses, CKM phase, or benchmark entries are used as inputs" in contract["acceptance"],
        "F7_no_overclaim": upstream_cert["target_fitting_used"] is False
        and upstream_cert["closure_claimed"] is False,
    }

    return {
        "packet": "SourceOrigin_Alpha1Driver_Reduction_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
        },
        "theorem": {
            "name": "SourceOriginAlpha1DriverReductionImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected source-origin blocker and alpha1-driver blocker "
                "reduce to one object: a selected Phi_fin alpha1 payload emitted "
                "from the q79/F,m=1 S3/Green-Schwarz Strominger/HYM branch. "
                "Support is no longer the active blocker; selected payload values "
                "are."
            ),
        },
        "checks": checks,
        "upstream_source_origin_alpha1_driver": upstream,
        "what_closes_now": {
            "source_origin_support_not_the_blocker": True,
            "source_and_alpha1_reduced_to_one_payload": True,
            "Phi_fin_codomain_shape_already_built": True,
            "alpha1_driver_row_and_operator_level_source_imported": True,
            "ordinary_rhoE_retired_projective_gerbe_route_live": True,
            "single_alpha1_driver_can_lift_rank_if_C33_nonzero": True,
            "target_fitting_excluded_from_promotion": True,
        },
        "what_remains_open": {
            "selected_PhiFin_alpha1_payload": True,
            "selected_nonidentity_rhoE_connection_values": True,
            "source_origin_selected_flags": True,
            "same_branch_dotD_alpha1_derivative": True,
            "finite_C1_source_vector_and_Hessian_blocks": True,
            "deltaTheta_C1_and_sector_dotD": True,
            "zero_mode_bases_and_primitive_contractions": True,
            "branch_selection_or_antiunitary_retarded_selector": True,
            "A_selected": True,
            "b_selected": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_PhiFin_alpha1_payload": False,
            "claims_selected_nonidentity_rhoE_values": False,
            "claims_source_origin_flags": False,
            "claims_same_branch_dotD_derivative": False,
            "claims_finite_C1_source_vector_or_Hessian_blocks": False,
            "claims_deltaTheta_C1_or_sector_dotD": False,
            "claims_zero_mode_bases_or_primitive_contractions": False,
            "claims_A_selected_or_b_selected": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "uses_observed_masses_or_CKM_phase": False,
            "uses_benchmark_entries": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SourceOriginAlpha1DriverReductionImport",
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
    return f"""# SourceOrigin Alpha1Driver Reduction Import v1

Status: `{cert["status"]}`.

The selected source-origin blocker and alpha1-driver blocker now reduce to one
object: `SelectedPhiFinAlpha1Payload`.  The support side is not the active
blocker anymore: S3/projective-gerbe support, visible Chern-Weil reduction,
Route-C/Strominger support, finite shape gates, and alpha1 operator-level row
support are already aligned.

The remaining object must emit selected non-identity `rho_E`, selected
Hermitian metric/projectors, selected `D_E`, Riesz/reduced Green, same-branch
`dotD_alpha1`, finite C1 source vector/Hessian blocks, `deltaTheta_C1`,
zero-mode bases, and primitive C1 contractions.  No observed masses, CKM phase,
or benchmark entries may be selectors.

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
