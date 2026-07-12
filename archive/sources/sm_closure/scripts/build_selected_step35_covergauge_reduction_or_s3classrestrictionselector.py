"""Build Step 35 cover-gauge reduction and S3 class/restriction selector."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step35_covergauge_reduction_or_s3classrestrictionselector"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
REDUCTION = PACKET_DIR / "step35_cover_gauge_reduction.packet.json"
SELECTOR = PACKET_DIR / "step35_s3_class_restriction_selector.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step35_CoverGaugeReduction_or_S3ClassRestrictionSelector_v1.md"

STEP34 = DATA / "selected_step34_flatgerbe_sourcefunctor_or_selectedcoverselector.candidate.json"
Q79_COVER = Q79 / "candidate_data" / "iwasawa_deligne_cover_gauge_reduction.candidate.json"

STATUS = "MTT_SELECTED_STEP35_COVER_GAUGE_REDUCED_TO_S3_CLASS_RESTRICTION_SELECTOR_OPEN"
NEXT = "MTT_Selected_S3DifferentialCohomologyClassRestriction_and_ProjectorRetention_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    step34 = load(STEP34)
    cover = load(Q79_COVER)

    reduction = {
        "schema": "MTTStep35CoverGaugeReduction.v1",
        "status": "GOOD_COVER_NOT_PHYSICAL_KNOB",
        "imported_q79_status": cover["status"],
        "what_closes": cover["what_this_closes"],
        "mathematical_reduction": cover["mathematical_reduction"],
        "step34_refinement": {
            "old_wording": "selected cover/good-cover selector",
            "new_wording": "selected smooth differential-cohomology class plus S3 restriction; good cover is execution representative",
            "step34_functor_kept": step34["closure_decision"]["finite_to_smooth_flat_gerbe_source_functor_constructed"],
        },
        "good_cover_as_new_knob": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(REDUCTION, reduction)

    selector = {
        "schema": "MTTStep35S3ClassRestrictionSelector.v1",
        "status": "S3_DIFFERENTIAL_COHOMOLOGY_CLASS_RESTRICTION_SELECTOR_OPEN",
        "must_select_next": [
            "fixed smooth flat differential-cohomology class on the q79/F,m=1 S3 worldvolume",
            "restriction/pullback table of that class to S3",
            "twisted CP module matching the pulled-back class",
            "W3/spinC input on the same selected worldvolume",
            "block-sector family/Higgs projector retention",
        ],
        "execution_representatives_allowed_after_selection": [
            "good-cover Deligne/Cech table",
            "equivalent stack/Cech nerve representative",
            "B-field period representative",
            "holonomy/classifying-map representative",
        ],
        "still_open_from_q79": cover["still_open"],
        "selected_class_restriction_closed": False,
        "projector_retention_closed": False,
        "operator_values_closed": False,
    }
    write_json(SELECTOR, selector)

    candidate = {
        "candidate": "MTTSelectedStep35CoverGaugeReductionOrS3ClassRestrictionSelector",
        "status": STATUS,
        "inputs": {
            "step34": rel(STEP34),
            "q79_cover_gauge_reduction": rel(Q79_COVER),
        },
        "output_packets": {
            "cover_gauge_reduction": rel(REDUCTION),
            "s3_class_restriction_selector": rel(SELECTOR),
        },
        "theorem": {
            "name": "Step35CoverGaugeReductionTheorem",
            "proved": True,
            "statement": (
                "The good cover/Cech table is an execution representative of the "
                "flat Deligne-Cech gerbe, not an independent MTT physical selector. "
                "The Step34 source functor remains valid, but the live selector is "
                "sharpened to the selected smooth differential-cohomology class on "
                "S3, its q79/F,m=1 restriction, twisted CP cancellation, and projector retention."
            ),
        },
        "closure_decision": {
            "good_cover_removed_as_physical_knob": True,
            "cover_refinement_invariance_imported": True,
            "step34_functor_preserved": True,
            "frontier_reduced_to_selected_s3_class_restriction": True,
            "selected_s3_differential_cohomology_class_closed": False,
            "s3_restriction_pullback_table_closed": False,
            "smooth_freed_witten_projector_retention_closed": False,
            "operator_level_projective_rhoE_transition_closed": False,
            "selected_D_E_Riesz_Green_dotD_values_closed": False,
            "accepted_internal_scalar_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step35_CoverGaugeReduction_or_S3ClassRestrictionSelector_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "good_cover_removed_as_physical_knob": True,
        "frontier_reduced_to_selected_s3_class_restriction": True,
        "selected_s3_differential_cohomology_class_closed": False,
        "operator_sector_values_closed": False,
        "accepted_internal_scalar_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step35 CoverGaugeReduction or S3ClassRestrictionSelector v1

Status: `{STATUS}`.

Step35 imports the q79 cover-gauge reduction: a good cover is an execution
representative for Deligne/Cech data, not a new physical knob. The frontier is
therefore not "select an arbitrary cover"; it is the selected smooth
differential-cohomology class on S3 plus its q79/F,m=1 restriction, twisted CP
cancellation, and projector retention.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
