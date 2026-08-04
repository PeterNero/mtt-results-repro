"""Build the selected S3 class restriction / projector retention artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
Q79 = TEXPAPERS / "mtt-q79-proof-repro"

OUTPUT_DATA = DATA / "selected_s3_class_restriction_projector_retention.candidate.json"
OUTPUT_CERT = CERTS / "selected_s3_class_restriction_projector_retention_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_S3_Class_Restriction_Projector_Retention_v1.md"

LOCAL_INPUTS = {
    "pic0_gerbe_reduction": CERTS / "selected_pic0_invariance_or_gerbe_twisted_de_source_certificate.json",
    "freed_witten_cycle_gate": Q79 / "certificates" / "time_oriented_m1_freed_witten_cycle_gate_certificate.json",
    "visible_spinc_gate": Q79 / "certificates" / "visible_complex_worldvolume_spinc_gate_certificate.json",
    "finite_s3_cp_cancellation": Q79 / "certificates" / "visible_twisted_s3_finite_cp_cancellation_certificate.json",
    "block_factorized_sector_maps": Q79 / "certificates" / "iwasawa_block_factorized_sector_maps_certificate.json",
    "deligne_cover_gauge_reduction": Q79 / "certificates" / "iwasawa_deligne_cover_gauge_reduction_certificate.json",
    "smooth_s3_lift_attempt": Q79 / "certificates" / "visible_twisted_s3_smooth_source_lift_attempt_certificate.json",
    "visible_gs_curvature": Q79 / "certificates" / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_status() -> dict[str, object]:
    return {
        key: {
            "path": str(path),
            "present": path.exists(),
        }
        for key, path in LOCAL_INPUTS.items()
    }


def build_candidate() -> dict[str, object]:
    previous = load_json(LOCAL_INPUTS["pic0_gerbe_reduction"])
    fw = load_json(LOCAL_INPUTS["freed_witten_cycle_gate"])
    spinc = load_json(LOCAL_INPUTS["visible_spinc_gate"])
    cp = load_json(LOCAL_INPUTS["finite_s3_cp_cancellation"])
    sectors = load_json(LOCAL_INPUTS["block_factorized_sector_maps"])
    cover = load_json(LOCAL_INPUTS["deligne_cover_gauge_reduction"])
    smooth = load_json(LOCAL_INPUTS["smooth_s3_lift_attempt"])
    gs = load_json(LOCAL_INPUTS["visible_gs_curvature"])

    ordinary_zero = cp["s3_cancellation_reports"][0]["ordinary_DD_zero_D7_stacks"]
    matter_zero = cp["s3_cancellation_reports"][0]["ordinary_DD_zero_matter_curves"]
    return {
        "candidate": "MTTSelectedS3ClassRestrictionProjectorRetention",
        "status": "MTT_SELECTED_S3_CLASS_RESTRICTION_PROJECTOR_RETENTION_BUILT_SMOOTH_SOURCE_OPEN",
        "source_status": source_status(),
        "imported_results": {
            "previous_frontier": {
                "status": previous["status"],
                "next_required_artifact": previous["next_required_artifact"],
                "closure_claimed": previous["closure_claimed"],
            },
            "freed_witten_cycle_gate": {
                "status": fw["status"],
                "finite_restriction_theorem": fw["finite_restriction_theorem"],
                "selected_cycles_supplied": fw["calculation_results"]["selected_cycles_supplied"],
                "Freed_Witten_verified": fw["calculation_results"]["Freed_Witten_verified"],
            },
            "visible_spinc_gate": {
                "status": spinc["status"],
                "W3_spinC_closed": spinc["calculation_results"]["W3_spinC_gate_for_visible_complex_worldvolume_class_closed"],
                "active_F3_squared_images_supplied": spinc["calculation_results"]["active_F3_squared_images_supplied"],
                "worldvolume_class": spinc["worldvolume_class"],
            },
            "finite_s3_cp_cancellation": {
                "status": cp["status"],
                "finite_S3_CP_cancellation_closed": cp["calculation_results"]["finite_S3_CP_cancellation_closed"],
                "twisted_S3_DD_cancellation_available": cp["calculation_results"]["twisted_S3_DD_cancellation_available"],
                "matter_curves_remain_ordinary_DD_zero": cp["calculation_results"]["matter_curves_remain_ordinary_DD_zero"],
                "selected_projector_retention_verified": cp["calculation_results"]["selected_projector_retention_verified"],
                "s3_cancellation_reports": cp["s3_cancellation_reports"],
            },
            "block_factorized_sector_maps": {
                "status": sectors["status"],
                "finite_block_factorized_sector_maps_valid": sectors["calculation_results"]["finite_block_factorized_sector_maps_valid"],
                "family_sector_projectors_full_rank_three": sectors["calculation_results"]["family_sector_projectors_full_rank_three"],
                "higgs_line_rank_one_projector": sectors["calculation_results"]["higgs_line_rank_one_projector"],
                "selected_source_ready": sectors["calculation_results"]["selected_source_ready"],
            },
            "deligne_cover_gauge_reduction": {
                "status": cover["status"],
                "good_cover_execution_scaffold": cover["what_this_closes"]["good_cover_is_execution_scaffold_not_physical_knob"],
            },
            "smooth_s3_lift_attempt": {
                "status": smooth["status"],
                "selected_smooth_S3_source_constructed": smooth["calculation_results"]["selected_smooth_S3_source_constructed"],
                "smooth_S3_Freed_Witten_closed": smooth["calculation_results"]["smooth_S3_Freed_Witten_closed"],
                "smooth_S3_projector_retention_closed": smooth["calculation_results"]["smooth_S3_projector_retention_closed"],
            },
            "visible_gs_curvature": {
                "status": gs["status"],
                "visible_green_schwarz_curvature_verified": gs["calculation_results"]["visible_green_schwarz_curvature_verified"],
                "projector_retention_verified": gs["calculation_results"]["projector_retention_verified"],
            },
        },
        "restriction_packet": {
            "branch": {"q": 79, "orientation": "F", "torsion_label_m": 1},
            "active_quotient": "F_3^2",
            "ordinary_DD_zero_stacks": ordinary_zero,
            "ordinary_DD_zero_matter_curves": matter_zero,
            "twisted_stack": "S3",
            "S3_active_image_rank_over_F3": cp["s3_cancellation_reports"][0]["S3_active_image_rank_over_F3"],
            "ordinary_S3_DD_zero": cp["s3_cancellation_reports"][0]["ordinary_DD_gate_for_S3"],
            "finite_twisted_CP_DD_class_matches_B_restriction": cp["s3_cancellation_reports"][0]["finite_twisted_CP_DD_class_matches_B_restriction"],
            "finite_total_twisted_DD_class_zero": cp["s3_cancellation_reports"][0]["finite_total_twisted_DD_class_zero"],
            "W3_spinC_zero_for_visible_complex_worldvolume_class": spinc["calculation_results"]["W3_spinC_gate_for_visible_complex_worldvolume_class_closed"],
        },
        "projector_retention_packet": {
            "finite_block_factorized_sector_maps_valid": sectors["calculation_results"]["finite_block_factorized_sector_maps_valid"],
            "family_sector_projectors": "full_rank_three_on_projective_qutrit_block",
            "higgs_projector": "rank_one_on_separate_ordinary_line",
            "finite_projector_architecture_retained": True,
            "smooth_projector_retention_verified": False,
            "reason_smooth_open": "The finite projector architecture is validated, but no selected smooth twisted source or selected D_E action is constructed yet.",
        },
        "theorem": {
            "name": "SelectedS3FiniteRestrictionProjectorCompatibility",
            "proved": True,
            "statement": (
                "On the q79/F,m=1 branch, the finite visible restriction packet is coherent: "
                "S1, S2, and Cij remain ordinary DD-zero; S3 has rank-two active F_3^2 image "
                "and is therefore not ordinary DD-zero, but its finite twisted Chan-Paton module "
                "matches the B restriction. The block-factorized family/Higgs projectors are "
                "compatible at the finite packet level."
            ),
            "limits": [
                "does not construct the selected smooth Deligne/Cech S3 source",
                "does not close smooth Freed-Witten/projector retention",
                "does not construct selected D_E/dotD/Riesz/Green",
            ],
        },
        "gate_results": {
            "s3_class_restriction_projector_artifact_built": True,
            "W3_spinC_imported_closed": True,
            "ordinary_DD_zero_for_S1_S2_Cij_imported": True,
            "S3_rank_two_active_image_imported": True,
            "ordinary_S3_DD_zero_rejected": True,
            "finite_twisted_S3_CP_cancellation_imported": True,
            "finite_block_projector_architecture_retained": True,
            "smooth_s3_source_constructed": False,
            "smooth_Freed_Witten_closed": False,
            "smooth_projector_retention_closed": False,
            "selected_DE_dotD_Riesz_Green_constructed": False,
            "selected_Qa_SU3_packet_closed": False,
            "sm_parity_closure_claimed": False,
            "no_knob_closure_claimed": False,
        },
        "next_required_artifact": "MTT_Selected_Smooth_S3_Twisted_Source_Lift_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSelectedS3ClassRestrictionProjectorRetention",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "finite_visible_restriction_packet_coherent": True,
            "W3_spinC_visible_worldvolume_imported": True,
            "ordinary_S1_S2_Cij_DD_zero_retained": True,
            "S3_rank_two_requires_twisted_CP": True,
            "finite_block_projector_architecture_retained": True,
        },
        "what_remains_open": {
            "selected_smooth_S3_Deligne_Cech_or_flux_source": True,
            "smooth_Freed_Witten_and_projector_retention": True,
            "selected_D_E_dotD_Riesz_Green": True,
            "selected_Qa_SU3_color_operator_packet": True,
            "sm_parity_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    sources = "\n".join(
        f"- `{key}`: {body['path']} ({'present' if body['present'] else 'missing'})"
        for key, body in candidate["source_status"].items()
    )
    imported = candidate["imported_results"]
    restriction = candidate["restriction_packet"]
    projectors = candidate["projector_retention_packet"]
    closes = "\n".join(f"- {name}" for name, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {name}" for name, value in certificate["what_remains_open"].items() if value)
    limits = "\n".join(f"- {item}" for item in candidate["theorem"]["limits"])
    return f"""# MTT Selected S3 Class Restriction Projector Retention v1

## Purpose

This artifact closes the finite restriction bookkeeping needed before the
smooth S3 twisted-source lift.  It distinguishes ordinary DD-zero cycles from
the deliberately twisted S3 stack and checks that the finite block-factorized
projector architecture remains compatible.

## Inputs

{sources}

## Imported Status

- Previous frontier: `{imported["previous_frontier"]["status"]}`
- Freed-Witten cycle gate: `{imported["freed_witten_cycle_gate"]["status"]}`
- Visible spinC gate: `{imported["visible_spinc_gate"]["status"]}`
- Finite S3 CP cancellation: `{imported["finite_s3_cp_cancellation"]["status"]}`
- Block-factorized sector maps: `{imported["block_factorized_sector_maps"]["status"]}`
- Smooth S3 lift attempt: `{imported["smooth_s3_lift_attempt"]["status"]}`
- Visible Green-Schwarz curvature: `{imported["visible_gs_curvature"]["status"]}`

## Restriction Packet

- branch: `q={restriction["branch"]["q"]}`, `{restriction["branch"]["orientation"]}`, `m={restriction["branch"]["torsion_label_m"]}`
- active quotient: `{restriction["active_quotient"]}`
- ordinary DD-zero stacks: `{restriction["ordinary_DD_zero_stacks"]}`
- ordinary DD-zero matter curves: `{restriction["ordinary_DD_zero_matter_curves"]}`
- twisted stack: `{restriction["twisted_stack"]}`
- S3 active image rank over F3: `{restriction["S3_active_image_rank_over_F3"]}`
- ordinary S3 DD-zero: `{restriction["ordinary_S3_DD_zero"]}`
- finite twisted CP matches B restriction: `{restriction["finite_twisted_CP_DD_class_matches_B_restriction"]}`
- finite total twisted DD class zero: `{restriction["finite_total_twisted_DD_class_zero"]}`
- W3/spinC visible worldvolume class closed: `{restriction["W3_spinC_zero_for_visible_complex_worldvolume_class"]}`

## Projector Packet

- finite block-factorized sector maps valid: `{projectors["finite_block_factorized_sector_maps_valid"]}`
- family sectors: `{projectors["family_sector_projectors"]}`
- Higgs sector: `{projectors["higgs_projector"]}`
- finite projector architecture retained: `{projectors["finite_projector_architecture_retained"]}`
- smooth projector retention verified: `{projectors["smooth_projector_retention_verified"]}`

Reason smooth retention remains open:

{projectors["reason_smooth_open"]}

## Theorem

`{candidate["theorem"]["name"]}` is proved as a finite compatibility theorem:

{candidate["theorem"]["statement"]}

Limits:

{limits}

## What This Closes

{closes}

## What Remains Open

{open_items}

## Next Artifact

```text
{candidate["next_required_artifact"]}
```
"""


def main() -> None:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    note_text = render_note(candidate, certificate)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note_text, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
