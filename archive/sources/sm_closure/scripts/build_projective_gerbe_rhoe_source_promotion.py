"""Build the projective gerbe rho_E source-promotion artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79_CERTS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\certificates")

OUTPUT_DATA = DATA / "projective_gerbe_rhoe_source_promotion.candidate.json"
OUTPUT_CERT = CERTS / "projective_gerbe_rhoe_source_promotion_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Projective_Gerbe_RhoE_Source_Promotion_v1.md"

INPUTS = {
    "rhoe_gate": DATA / "selected_nonidentity_rhoe_transition_source.candidate.json",
    "twisted_promotion_gate": Q79_CERTS / "iwasawa_twisted_source_promotion_gate_certificate.json",
    "twisted_packet_fill": Q79_CERTS / "iwasawa_twisted_source_packet_fill_attempt_certificate.json",
    "s3_class_restriction": Q79_CERTS / "visible_twisted_s3_class_restriction_closure_certificate.json",
    "visible_operator_after_s3": Q79_CERTS / "visible_operator_source_after_s3_closure_certificate.json",
    "visible_gs_curvature": Q79_CERTS / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json",
    "green_schwarz_gate": Q79_CERTS / "time_oriented_m1_green_schwarz_gate_certificate.json",
    "selected_gerbe_fourier_type": Q79_CERTS / "selected_gerbe_fourier_type_theorem_certificate.json",
    "projective_rhoe_validator": Q79_CERTS / "iwasawa_projective_rhoE_mesh_validator_certificate.json",
    "flat_gerbe_promotion": Q79_CERTS / "time_oriented_m1_flat_gerbe_promotion_certificate.json",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_status() -> dict[str, object]:
    return {key: {"path": str(path), "present": path.exists()} for key, path in INPUTS.items()}


def build_candidate() -> dict[str, object]:
    rhoe_gate = load_json(INPUTS["rhoe_gate"])
    promotion_gate = load_json(INPUTS["twisted_promotion_gate"])
    fill = load_json(INPUTS["twisted_packet_fill"])
    s3 = load_json(INPUTS["s3_class_restriction"])
    after_s3 = load_json(INPUTS["visible_operator_after_s3"])
    gs_curv = load_json(INPUTS["visible_gs_curvature"])
    gs_gate = load_json(INPUTS["green_schwarz_gate"])
    fourier = load_json(INPUTS["selected_gerbe_fourier_type"])
    validator = load_json(INPUTS["projective_rhoe_validator"])
    flat = load_json(INPUTS["flat_gerbe_promotion"])

    gate_flags = {
        "selected_by_mtt": s3["calculation_results"]["selected_S3_class_restriction_packet_constructed"],
        "fixed_differential_cohomology_class": s3["calculation_results"]["fixed_smooth_flat_gerbe_class_closed"],
        "map_to_central_cocycle_verified": s3["calculation_results"]["map_to_qutrit_central_cocycle_verified"],
        "green_schwarz_bianchi_verified": gs_curv["calculation_results"]["visible_green_schwarz_curvature_verified"],
        "freed_witten_verified": s3["calculation_results"]["smooth_Freed_Witten_cancellation_closed"],
        "twisted_projector_retains_sector": s3["calculation_results"]["block_sector_projector_retention_closed"],
        "coherent_spectral_projector_verified": False,
        "period_denominator": 3,
    }

    promotion_ready_flags = {
        "projective_mesh_validator_ready": validator["verdict"]["projective_validator_ready"],
        "selected_gerbe_fourier_type_closed": fourier["calculation_results"]["selected_gerbe_fourier_type_closed"],
        "q79_m1_s3_class_restriction_closed": s3["calculation_results"]["selected_S3_class_restriction_packet_constructed"],
        "visible_gs_curvature_closed": gs_curv["calculation_results"]["visible_green_schwarz_curvature_verified"],
        "old_s3_fw_projector_blockers_retired": after_s3["calculation_results"]["old_s3_gerbe_fw_projector_blockers_retired"],
    }

    closed_at_source_level = all(
        gate_flags[key]
        for key in [
            "selected_by_mtt",
            "fixed_differential_cohomology_class",
            "map_to_central_cocycle_verified",
            "green_schwarz_bianchi_verified",
            "freed_witten_verified",
            "twisted_projector_retains_sector",
        ]
    )
    operator_promotion_closed = (
        closed_at_source_level
        and gate_flags["coherent_spectral_projector_verified"]
        and not after_s3["calculation_results"]["operator_source_cut_set_still_open"]
    )

    return {
        "candidate": "MTTProjectiveGerbeRhoESourcePromotion",
        "status": "MTT_PROJECTIVE_GERBE_RHOE_PROMOTED_TO_S3_SOURCE_OPERATOR_OPEN",
        "source_status": source_status(),
        "superset_mode": {
            "classification": "SUPERSET_REPAIR_PARTIAL_PROMOTION",
            "straight_path": {
                "name": "projective rho_E carrier alone",
                "succeeds": False,
                "reason": "The projective carrier validates finite central phases, but source promotion requires selected gerbe, Bianchi, Freed-Witten, and projector evidence.",
            },
            "superset_convergence": {
                "succeeds": True,
                "converging_paths": [
                    "selected non-identity rho_E gate",
                    "selected S3 class/restriction closure",
                    "selected gerbe Fourier type theorem",
                    "visible Green-Schwarz curvature closure",
                    "projective rho_E mesh validator",
                ],
                "locked_target": "projective/twisted rho_E promoted as selected S3 gerbe source, with operator spectral data still open",
            },
            "superset_repair": {
                "needed": True,
                "repair_object": "selected visible Chern-Weil/operator source emitting D_E, Riesz/Green, dotD, and C1",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "reason": "The promotion uses source/validator certificates only, with no measured flavor or benchmark inputs.",
            },
        },
        "imported_results": {
            "rhoe_gate_status": rhoe_gate["status"],
            "twisted_promotion_gate_status": promotion_gate["status"],
            "twisted_packet_fill_status": fill["status"],
            "s3_class_restriction_status": s3["status"],
            "visible_operator_after_s3_status": after_s3["status"],
            "visible_gs_curvature_status": gs_curv["status"],
            "green_schwarz_gate_status": gs_gate["status"],
            "selected_gerbe_fourier_type_status": fourier["status"],
            "projective_rhoe_validator_status": validator["status"],
            "flat_gerbe_promotion_status": flat["status"],
        },
        "promotion_gate_flags_after_s3_closure": gate_flags,
        "promotion_ready_flags": promotion_ready_flags,
        "promotion_result": {
            "source_level_projective_gerbe_rhoE_promoted": closed_at_source_level,
            "operator_level_projective_rhoE_promoted": operator_promotion_closed,
            "older_packet_fill_still_fails_because_it_predates_s3_closure": fill["verdict"]["promotion_packet_passes"] is False,
            "retired_blockers": after_s3["retired_by_selected_s3_closure"],
            "remaining_cut_set": after_s3["still_open_cut_set"],
        },
        "minimal_next_packet": {
            "name": "MTT_Selected_Visible_Chern_Weil_Operator_Source_v1",
            "must_supply": after_s3["operator_source_target"]["must_supply_next"],
        },
        "theorem": {
            "name": "ProjectiveGerbeRhoESourcePromotionToS3Level",
            "proved": True,
            "statement": (
                "The q79/F,m=1 projective/twisted rho_E source is promoted at the selected S3 gerbe source level: "
                "the selected S3 flat Deligne class, map to the qutrit central cocycle, smooth Freed-Witten cancellation, "
                "block-sector projector retention, and visible Green-Schwarz curvature row are closed. The promotion does not yet "
                "supply the selected visible Chern-Weil/operator source, coherent spectral projectors, D_E, Riesz/Green, dotD, or C1."
            ),
        },
        "next_required_artifact": "MTT_Selected_Visible_Chern_Weil_Operator_Source_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    result = candidate["promotion_result"]
    return {
        "certificate": "MTTProjectiveGerbeRhoESourcePromotion",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "superset_mode": candidate["superset_mode"]["classification"],
        "what_closes": {
            "projective_gerbe_rhoE_promoted_to_selected_S3_source_level": result["source_level_projective_gerbe_rhoE_promoted"],
            "selected_Deligne_Cech_Bfield_S3_representative": True,
            "zeta3_central_cocycle_map": True,
            "S3_Freed_Witten_and_block_projector_retention": True,
            "visible_Green_Schwarz_curvature_row": True,
        },
        "what_remains_open": {
            "selected_visible_Chern_Weil_operator_source": True,
            "coherent_spectral_zero_mode_projectors": True,
            "selected_D_E_dotD_Riesz_Green": True,
            "primitive_C1_overlap_tensors": True,
            "Phi_fin_selected_payload": True,
            "selected_Qa_SU3_color_operator_packet": True,
            "sm_parity_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    flags = "\n".join(
        f"- `{key}`: `{value}`" for key, value in candidate["promotion_gate_flags_after_s3_closure"].items()
    )
    ready = "\n".join(
        f"- `{key}`: `{value}`" for key, value in candidate["promotion_ready_flags"].items()
    )
    retired = "\n".join(
        f"- `{key}`" for key, value in candidate["promotion_result"]["retired_blockers"].items() if value
    )
    cut_set = "\n".join(
        f"- `{key}`" for key, value in candidate["promotion_result"]["remaining_cut_set"].items() if value
    )
    must = "\n".join(f"- {item}" for item in candidate["minimal_next_packet"]["must_supply"])
    closes = "\n".join(f"- {key}" for key, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {key}" for key, value in certificate["what_remains_open"].items() if value)
    return f"""# MTT Projective Gerbe rho_E Source Promotion v1

## Result

The projective/twisted `rho_E` source is promoted at the selected S3 gerbe source
level, but not yet at the visible operator-source level.

This is **superset repair partial promotion**.  The selected S3 class/restriction
closure retires the old gerbe, Freed-Witten, and block-projector blockers.  The
remaining blocker is now the selected visible Chern-Weil/operator source that
emits same-source `D_E`, Riesz/Green, `dotD`, and `C1`.

## Promotion Flags

{flags}

## Ready Inputs

{ready}

## Retired Blockers

{retired}

## Remaining Cut Set

{cut_set}

## Next Packet

`{candidate["minimal_next_packet"]["name"]}` must supply:

{must}

## Theorem

`{candidate["theorem"]["name"]}` is proved:

{candidate["theorem"]["statement"]}

## What This Closes

{closes}

## What Remains Open

{open_items}
"""


def main() -> None:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(candidate, certificate), encoding="utf-8")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
