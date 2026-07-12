"""Import same-source symmetry-breaking reduction to orientation-carrying D_E/dotD."""

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

PREVIOUS = CERTS / "nonsplit_routec_and_minimal_hsel_gret_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "same_source_symmetry_breaking_source.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "same_source_symmetry_breaking_source_certificate.json"

OUTPUT_PACKET = DATA / "same_source_symmetry_breaking_reduction_import.candidate.json"
OUTPUT_CERT = CERTS / "same_source_symmetry_breaking_reduction_import_certificate.json"
OUTPUT_NOTE = CORPUS / "SameSourceSymmetryBreaking_Reduction_Import_v1.md"

STATUS = "SAME_SOURCE_SYMMETRY_BREAKING_IMPORTED_ORIENTATION_DE_DOTD_OPEN"
PREVIOUS_STATUS = "NONSPLIT_ROUTEC_AND_MINIMAL_HSEL_GRET_IMPORTED_PROMOTION_OPEN"
UPSTREAM_STATUS = "MTT_SAME_SOURCE_SYMMETRY_BREAKING_SOURCE_REDUCED_TO_ORIENTATION_CARRYING_DE_DOTD_PACKET"
NEXT = "MTT_Selected_Orientation_Carrying_DE_DotD_Source_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)

    primary = upstream["superset_mode"]["primary_superset_path"]
    repairs = upstream["superset_mode"]["repair_paths"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_SameSource_SymmetryBreaking_Source_v1",
        "F1_upstream_reduction_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["closure_claimed"] is False
        and upstream_cert["primary_next_artifact"] == NEXT,
        "F3_primary_orientation_route_selected": primary["classification"] == "SUPERSET_CONVERGENCE_PRIMARY"
        and primary["closed"]["conjugate_pair_reduced_to_q79_q369"] is True
        and primary["closed"]["finite_branch_data_reaches_validator_layer"] is True
        and primary["closed"]["dotd_response_validator_formulated"] is True
        and primary["open"]["selected_orientation_carrying_source"] is True
        and primary["open"]["actual_selected_D_E_action"] is True
        and primary["open"]["actual_selected_dotD_alpha1_operator"] is True,
        "F4_shortcuts_retired_or_demoted": upstream["superset_mode"]["straight_path"]["classification"]
        == "STRAIGHT_PATH_BLOCKED"
        and repairs["gauduchon_wall"]["equal_radius_current_source_rejected"] is True
        and repairs["pic0_rule_only"]["classification"] == "NECESSARY_BUT_NOT_SUFFICIENT"
        and repairs["ordered_integral_cech_or_appell_humbert"]["selected_s3_deck_limit"]["selected_s3_active_image_rank_over_F3"] == 2,
        "F5_template_contract_requires_real_operator_payload": upstream["selected_template_contract"]["validator_contract"]["must_feed_existing_D_E_dotD_validators"] is True
        and "selected_dotD_source_verified, alpha1_driver_verified, green_operator_verified, and horizontal_gauge_verified must be true"
        == upstream["selected_template_contract"]["validator_contract"]["supported_format"]["source_flags"],
        "F6_no_overclaim": upstream_cert["target_fitting_used"] is False
        and previous["guardrails"]["claims_smooth_Qa_SU3_operator_promotion"] is False
        and previous["guardrails"]["claims_selected_DE_dotD_Riesz_Green"] is False,
    }

    return {
        "packet": "SameSourceSymmetryBreaking_Reduction_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
        },
        "theorem": {
            "name": "SameSourceSymmetryBreakingReductionImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The same-source symmetry-breaking requirement is reduced to the "
                "selected orientation-carrying D_E/dotD packet. Current topology, "
                "h1, finite qutrit label, Appell-Humbert existence, equal-radius, "
                "and curvature data do not select the source. The primary live "
                "route is now a genuine operator payload that can bind q79/q369 "
                "orientation, sector domains, selected D_E, reduced Green, and "
                "same-branch dotD without observed-data or benchmark selectors."
            ),
        },
        "checks": checks,
        "upstream_same_source_symmetry_breaking": upstream,
        "what_closes_now": {
            "symmetry_breaking_shortcuts_triaged": True,
            "straight_topology_h1_qutrit_curvature_path_blocked": True,
            "orientation_carrying_DE_dotD_route_selected_as_primary": True,
            "q79_q369_conjugate_pair_formulated": True,
            "finite_DE_dotD_validator_layer_reachable": True,
            "gauduchon_wall_repair_kept_but_current_equal_radius_source_rejected": True,
            "ordered_integral_two_block_repair_kept_as_source_certificate_gap": True,
            "pic0_only_marked_necessary_but_insufficient": True,
            "operator_payload_template_contract_locked": True,
        },
        "what_remains_open": {
            "selected_orientation_carrying_de_dotd_source": True,
            "unique_m1_vs_m2_or_antiunitary_retarded_selection": True,
            "pic0_selected_or_quotiented": True,
            "selected_D_E_action": True,
            "selected_dotD_same_branch_derivative": True,
            "selected_reduced_green": True,
            "primitive_C1_contractions": True,
            "A_selected": True,
            "b_selected": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_orientation_source": False,
            "claims_unique_m1_vs_m2_selection": False,
            "claims_selected_pic0_resolution": False,
            "claims_selected_DE_dotD_Riesz_Green": False,
            "claims_primitive_C1_contractions": False,
            "claims_A_selected_or_b_selected": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "uses_observed_cp_sign": False,
            "uses_benchmark_flavor_matrices": False,
            "uses_lifted_selected_flags_as_proof": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SameSourceSymmetryBreakingReductionImport",
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
    return f"""# SameSourceSymmetryBreaking Reduction Import v1

Status: `{cert["status"]}`.

The same-source symmetry breaker is now reduced to an orientation-carrying
`D_E/dotD` source packet.  The current invariant data are not enough:
topology, `h1`, the finite qutrit label, Appell-Humbert existence, equal-radius
data, and curvature rows are all base-swap/Pic0 or conjugation insensitive at
the required gate.

The primary route is now `MTT_Selected_Orientation_Carrying_DE_DotD_Source_v1`.
It must supply selected source origin, q79/q369 orientation handling, selected
`D_E`, reduced Green, same-branch `dotD_alpha1`, and validator-passing source
flags without observed CP sign, benchmark flavor matrices, or lifted selected
flags.

Repair paths remain live but secondary: the Gauduchon wall route is blocked by
the current equal-radius source, ordered integral/Appell-Humbert data still need
a source certificate, and Pic0-only is necessary but not sufficient.

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
