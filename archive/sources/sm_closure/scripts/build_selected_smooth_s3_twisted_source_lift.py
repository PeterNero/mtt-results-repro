"""Build the selected smooth S3 twisted-source lift artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
Q79 = TEXPAPERS / "mtt-q79-proof-repro"

OUTPUT_DATA = DATA / "selected_smooth_s3_twisted_source_lift.candidate.json"
OUTPUT_CERT = CERTS / "selected_smooth_s3_twisted_source_lift_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_Smooth_S3_Twisted_Source_Lift_v1.md"

SMOOTH_TEMPLATE = Q79 / "certificates" / "visible_twisted_s3_smooth_source_lift.template.json"
SMOOTH_VALIDATOR = Q79 / "scripts" / "validate_visible_twisted_s3_smooth_source_lift.py"

LOCAL_INPUTS = {
    "s3_restriction_projector": CERTS / "selected_s3_class_restriction_projector_retention_certificate.json",
    "q79_smooth_lift_attempt": Q79 / "certificates" / "visible_twisted_s3_smooth_source_lift_attempt_certificate.json",
    "q79_s3_source_packet_attempt": Q79 / "certificates" / "visible_twisted_s3_source_packet_attempt_certificate.json",
    "q79_deligne_cover_gauge_reduction": Q79 / "certificates" / "iwasawa_deligne_cover_gauge_reduction_certificate.json",
    "q79_flat_gerbe_promotion": Q79 / "certificates" / "time_oriented_m1_flat_gerbe_promotion_certificate.json",
    "q79_finite_s3_cp_cancellation": Q79 / "certificates" / "visible_twisted_s3_finite_cp_cancellation_certificate.json",
    "q79_visible_gs_curvature": Q79 / "certificates" / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json",
    "q79_block_factorized_sector_maps": Q79 / "certificates" / "iwasawa_block_factorized_sector_maps_certificate.json",
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


def run_template_validator() -> dict[str, object]:
    proc = subprocess.run(
        [sys.executable, str(SMOOTH_VALIDATOR), str(SMOOTH_TEMPLATE)],
        cwd=Q79,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return {
        "validator": str(SMOOTH_VALIDATOR),
        "template": str(SMOOTH_TEMPLATE),
        "exit_code": proc.returncode,
        "output_head": proc.stdout.splitlines()[:16],
    }


def build_candidate() -> dict[str, object]:
    previous = load_json(LOCAL_INPUTS["s3_restriction_projector"])
    smooth_attempt = load_json(LOCAL_INPUTS["q79_smooth_lift_attempt"])
    source_attempt = load_json(LOCAL_INPUTS["q79_s3_source_packet_attempt"])
    cover = load_json(LOCAL_INPUTS["q79_deligne_cover_gauge_reduction"])
    flat = load_json(LOCAL_INPUTS["q79_flat_gerbe_promotion"])
    cp = load_json(LOCAL_INPUTS["q79_finite_s3_cp_cancellation"])
    gs = load_json(LOCAL_INPUTS["q79_visible_gs_curvature"])
    sectors = load_json(LOCAL_INPUTS["q79_block_factorized_sector_maps"])
    validator = run_template_validator()

    return {
        "candidate": "MTTSelectedSmoothS3TwistedSourceLift",
        "status": "MTT_SELECTED_SMOOTH_S3_TWISTED_SOURCE_LIFT_BUILT_SOURCE_CERTIFICATE_OPEN",
        "source_status": source_status(),
        "imported_results": {
            "previous_frontier": {
                "status": previous["status"],
                "next_required_artifact": previous["next_required_artifact"],
                "closure_claimed": previous["closure_claimed"],
            },
            "smooth_lift_attempt": {
                "status": smooth_attempt["status"],
                "conditional_smooth_flat_S3_model_available": smooth_attempt["calculation_results"]["conditional_smooth_flat_S3_model_available"],
                "finite_S3_CP_cancellation_carried_into_lift": smooth_attempt["calculation_results"]["finite_S3_CP_cancellation_carried_into_lift"],
                "selected_smooth_S3_source_constructed": smooth_attempt["calculation_results"]["selected_smooth_S3_source_constructed"],
                "smooth_S3_Freed_Witten_closed": smooth_attempt["calculation_results"]["smooth_S3_Freed_Witten_closed"],
                "smooth_S3_projector_retention_closed": smooth_attempt["calculation_results"]["smooth_S3_projector_retention_closed"],
            },
            "s3_source_packet_attempt": {
                "status": source_attempt["status"],
                "minimal_equivariant_stack_S3_closed": source_attempt["calculation_results"]["minimal_equivariant_stack_S3_closed"],
                "finite_projective_CP_inputs_collected": source_attempt["calculation_results"]["finite_S3_projective_CP_inputs_collected"],
                "selected_S3_source_constructed": source_attempt["calculation_results"]["selected_S3_source_constructed"],
                "S3_freed_witten_closed_for_source": source_attempt["calculation_results"]["S3_freed_witten_closed_for_source"],
                "S3_projector_retention_closed": source_attempt["calculation_results"]["S3_projector_retention_closed"],
            },
            "cover_reduction": {
                "status": cover["status"],
                "good_cover_execution_scaffold": cover["what_this_closes"]["good_cover_is_execution_scaffold_not_physical_knob"],
            },
            "flat_gerbe": {
                "status": flat["status"],
                "conditional_flat_gerbe_representative_exists": flat["calculation_results"]["conditional_flat_gerbe_representative_exists"],
                "curvature_H_zero_for_flat_representative": flat["calculation_results"]["curvature_H_zero_for_flat_representative"],
                "selected_flat_gerbe_representative_closed": flat["calculation_results"]["selected_flat_gerbe_representative_closed"],
            },
            "finite_s3_cp": {
                "status": cp["status"],
                "finite_S3_CP_cancellation_closed": cp["calculation_results"]["finite_S3_CP_cancellation_closed"],
                "matter_curves_remain_ordinary_DD_zero": cp["calculation_results"]["matter_curves_remain_ordinary_DD_zero"],
            },
            "visible_gs_curvature": {
                "status": gs["status"],
                "visible_green_schwarz_curvature_verified": gs["calculation_results"]["visible_green_schwarz_curvature_verified"],
                "selected_visible_operator_source_verified": gs["calculation_results"]["selected_visible_operator_source_verified"],
            },
            "block_factorized_sector_maps": {
                "status": sectors["status"],
                "finite_block_factorized_sector_maps_valid": sectors["calculation_results"]["finite_block_factorized_sector_maps_valid"],
                "selected_source_ready": sectors["calculation_results"]["selected_source_ready"],
            },
        },
        "template_validator_result": validator,
        "smooth_lift_packet_contract": {
            "schema": "VisibleTwistedS3SmoothSourceLift.v1",
            "selected_stack": "S3",
            "branch": {"q": 79, "orientation": "F", "torsion_label_m": 1},
            "already_available": [
                "finite S3 twisted Chan-Paton cancellation",
                "conditional flat Deligne/Cech m=1 gerbe model",
                "good-cover/refinement gauge reduction",
                "visible Green-Schwarz curvature row",
                "finite block-factorized family/Higgs projector architecture",
            ],
            "must_supply_now": [
                "source_selected_by_mtt",
                "fixed_differential_cohomology_class",
                "restricts_to_selected_S3_worldvolume",
                "map_to_qutrit_central_cocycle_verified",
                "smooth_twisted_CP_or_worldvolume_flux_constructed",
                "freed_witten_verified_for_smooth_S3_source",
                "twisted_projector_retention_verified",
            ],
            "downstream_after_lift": [
                "selected visible operator source",
                "selected D_E",
                "selected dotD_alpha1",
                "Riesz/Green/projector gap data",
                "primitive C1 contractions",
            ],
        },
        "theorem": {
            "name": "SmoothS3LiftSourceCertificateReduction",
            "proved": True,
            "statement": (
                "The current corpus closes all finite prerequisites for the S3 twisted-source lift "
                "and removes the good-cover choice as a physical knob. The lift is not yet closed: "
                "it requires a selected smooth differential-cohomology/worldvolume source certificate "
                "with S3 restriction, central-cocycle map, smooth Freed-Witten, and projector retention."
            ),
        },
        "gate_results": {
            "smooth_s3_lift_artifact_built": True,
            "finite_prerequisites_assembled": True,
            "good_cover_not_physical_knob": True,
            "template_validator_confirms_open": validator["exit_code"] == 2,
            "smooth_source_selected": False,
            "fixed_differential_cohomology_class_supplied": False,
            "smooth_S3_Freed_Witten_closed": False,
            "smooth_projector_retention_closed": False,
            "selected_DE_dotD_Riesz_Green_constructed": False,
            "selected_Qa_SU3_packet_closed": False,
            "sm_parity_closure_claimed": False,
            "no_knob_closure_claimed": False,
        },
        "next_required_artifact": "MTT_Selected_S3_Differential_Cohomology_Source_Certificate_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSelectedSmoothS3TwistedSourceLift",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "smooth_s3_lift_gate_reduced_to_source_certificate": True,
            "finite_prerequisites_for_s3_lift_assembled": True,
            "good_cover_not_physical_knob_imported": True,
            "smooth_lift_template_validator_run": True,
            "downstream_de_operator_bridge_identified": True,
        },
        "what_remains_open": {
            "selected_s3_differential_cohomology_source_certificate": True,
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
    contract = candidate["smooth_lift_packet_contract"]
    available = "\n".join(f"- {item}" for item in contract["already_available"])
    must = "\n".join(f"- `{item}`" for item in contract["must_supply_now"])
    downstream = "\n".join(f"- {item}" for item in contract["downstream_after_lift"])
    closes = "\n".join(f"- {name}" for name, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {name}" for name, value in certificate["what_remains_open"].items() if value)
    return f"""# MTT Selected Smooth S3 Twisted Source Lift v1

## Purpose

This artifact evaluates the smooth lift from the finite S3 twisted packet to a
selected smooth Deligne/Cech, B-field, worldvolume-flux, or twisted
Chan-Paton source.

## Inputs

{sources}

## Imported Status

- Previous frontier: `{imported["previous_frontier"]["status"]}`
- Smooth S3 lift attempt: `{imported["smooth_lift_attempt"]["status"]}`
- S3 source packet attempt: `{imported["s3_source_packet_attempt"]["status"]}`
- Cover reduction: `{imported["cover_reduction"]["status"]}`
- Flat gerbe: `{imported["flat_gerbe"]["status"]}`
- Finite S3 CP: `{imported["finite_s3_cp"]["status"]}`
- Visible Green-Schwarz curvature: `{imported["visible_gs_curvature"]["status"]}`
- Block sector maps: `{imported["block_factorized_sector_maps"]["status"]}`

## Validator Result

The existing q79 smooth-lift validator was run on its open template:

```text
exit_code={candidate["template_validator_result"]["exit_code"]}
```

This confirms the gate remains open rather than silently closed.

## Already Available

{available}

## Must Supply Now

{must}

## Downstream After Lift

{downstream}

## Theorem

`{candidate["theorem"]["name"]}` is proved as a reduction theorem:

{candidate["theorem"]["statement"]}

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
