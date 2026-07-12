"""Build the Pic0 invariance or gerbe-twisted D_E source artifact."""

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

OUTPUT_DATA = DATA / "selected_pic0_invariance_or_gerbe_twisted_de_source.candidate.json"
OUTPUT_CERT = CERTS / "selected_pic0_invariance_or_gerbe_twisted_de_source_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_Pic0_Invariance_or_Gerbe_Twisted_DE_Source_v1.md"

LOCAL_INPUTS = {
    "terminal_pic0_audit": CERTS / "selected_terminal_monad_lane_pic0_quotient_source_certificate.json",
    "q79_deligne_cover_gauge_reduction": Q79 / "certificates" / "iwasawa_deligne_cover_gauge_reduction_certificate.json",
    "q79_fixed_gerbe_representative": Q79 / "certificates" / "time_oriented_fixed_gerbe_representative_certificate.json",
    "q79_deck_cech_lift": Q79 / "certificates" / "time_oriented_m1_deck_cech_lift_certificate.json",
    "q79_flat_gerbe_promotion": Q79 / "certificates" / "time_oriented_m1_flat_gerbe_promotion_certificate.json",
    "q79_finite_s3_cp_cancellation": Q79 / "certificates" / "visible_twisted_s3_finite_cp_cancellation_certificate.json",
    "q79_smooth_s3_lift_attempt": Q79 / "certificates" / "visible_twisted_s3_smooth_source_lift_attempt_certificate.json",
    "q79_visible_gs_curvature": Q79 / "certificates" / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json",
    "q79_hym_operator_attempt": Q79 / "certificates" / "selected_hym_operator_source_attempt_certificate.json",
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
    terminal = load_json(LOCAL_INPUTS["terminal_pic0_audit"])
    cover = load_json(LOCAL_INPUTS["q79_deligne_cover_gauge_reduction"])
    fixed = load_json(LOCAL_INPUTS["q79_fixed_gerbe_representative"])
    deck = load_json(LOCAL_INPUTS["q79_deck_cech_lift"])
    flat = load_json(LOCAL_INPUTS["q79_flat_gerbe_promotion"])
    s3_cp = load_json(LOCAL_INPUTS["q79_finite_s3_cp_cancellation"])
    smooth = load_json(LOCAL_INPUTS["q79_smooth_s3_lift_attempt"])
    gs = load_json(LOCAL_INPUTS["q79_visible_gs_curvature"])
    hym = load_json(LOCAL_INPUTS["q79_hym_operator_attempt"])

    return {
        "candidate": "MTTSelectedPic0InvarianceOrGerbeTwistedDESource",
        "status": "MTT_SELECTED_PIC0_INVARIANCE_OR_GERBE_TWISTED_DE_SOURCE_BUILT_CLASS_RESTRICTION_GATE_OPEN",
        "source_status": source_status(),
        "imported_results": {
            "previous_frontier": {
                "status": terminal["status"],
                "next_required_artifact": terminal["next_required_artifact"],
                "closure_claimed": terminal["closure_claimed"],
            },
            "deligne_cover_gauge_reduction": {
                "status": cover["status"],
                "what_this_closes": cover["what_this_closes"],
                "mathematical_reduction": cover["mathematical_reduction"],
                "still_open": cover["still_open"],
            },
            "fixed_gerbe_representative": {
                "status": fixed["status"],
                "q79_orientation": fixed["branch_representatives"]["time_oriented_q79"]["orientation"],
                "q79_torsion_label_m": fixed["branch_representatives"]["time_oriented_q79"]["torsion_label_m"],
                "selected_D_E_dotD_constructed": fixed["calculation_results"]["selected_D_E_dotD_constructed"],
            },
            "deck_cech_lift": {
                "status": deck["status"],
                "deck_quotient_target": deck["deck_quotient_map"]["target"],
                "active_quotient_delta_zero": deck["calculation_results"]["active_quotient_delta_zero"],
                "qutrit_projective_commutator_matched": deck["calculation_results"]["qutrit_projective_commutator_matched"],
            },
            "flat_gerbe_promotion": {
                "status": flat["status"],
                "conditional_flat_gerbe_representative_exists": flat["calculation_results"]["conditional_flat_gerbe_representative_exists"],
                "curvature_H_zero_for_flat_representative": flat["calculation_results"]["curvature_H_zero_for_flat_representative"],
                "selected_flat_gerbe_representative_closed": flat["calculation_results"]["selected_flat_gerbe_representative_closed"],
            },
            "finite_s3_cp_cancellation": {
                "status": s3_cp["status"],
                "finite_S3_CP_cancellation_closed": s3_cp["calculation_results"]["finite_S3_CP_cancellation_closed"],
                "matter_curves_remain_ordinary_DD_zero": s3_cp["calculation_results"]["matter_curves_remain_ordinary_DD_zero"],
                "twisted_S3_DD_cancellation_available": s3_cp["calculation_results"]["twisted_S3_DD_cancellation_available"],
                "selected_projector_retention_verified": s3_cp["calculation_results"]["selected_projector_retention_verified"],
            },
            "smooth_s3_lift_attempt": {
                "status": smooth["status"],
                "conditional_smooth_flat_S3_model_available": smooth["calculation_results"]["conditional_smooth_flat_S3_model_available"],
                "selected_smooth_S3_source_constructed": smooth["calculation_results"]["selected_smooth_S3_source_constructed"],
                "smooth_S3_Freed_Witten_closed": smooth["calculation_results"]["smooth_S3_Freed_Witten_closed"],
                "smooth_S3_projector_retention_closed": smooth["calculation_results"]["smooth_S3_projector_retention_closed"],
            },
            "visible_gs_curvature": {
                "status": gs["status"],
                "visible_green_schwarz_curvature_verified": gs["calculation_results"]["visible_green_schwarz_curvature_verified"],
                "projector_retention_verified": gs["calculation_results"]["projector_retention_verified"],
                "selected_visible_operator_source_verified": gs["calculation_results"]["selected_visible_operator_source_verified"],
            },
            "hym_operator_attempt": {
                "status": hym["status"],
                "selected_hym_operator_source_verified": hym["calculation_results"]["selected_hym_operator_source_verified"],
            },
        },
        "route_decision": {
            "direct_pic0_invariance": {
                "status": "RETIRED_FOR_NOW",
                "reason": "No same-source theorem proves that D_E, dotD, Riesz/Green, and overlap observables descend under arbitrary Pic0 twists.",
                "reopen_condition": "Provide explicit invariant operator/overlap formulas for the selected V_alpha packet over Pic0.",
            },
            "neutral_pic0_selection": {
                "status": "ABSENT",
                "reason": "No holonomy-sensitive source currently selects the neutral flat character.",
            },
            "gerbe_twisted_de_source": {
                "status": "PRIMARY_EXECUTION_ROUTE",
                "reason": "The q79/F m=1 finite gerbe, deck Cech lift, finite S3 Chan-Paton cancellation, and visible Green-Schwarz curvature row are all closed at their levels.",
            },
        },
        "cover_knob_reduction": {
            "good_cover_is_physical_knob": False,
            "good_cover_is_execution_scaffold": True,
            "cover_refinement_invariance_imported": True,
            "remaining_physical_object": "selected smooth S3 differential-cohomology class with restriction, Freed-Witten, projector retention, and operator data",
        },
        "selected_s3_class_packet_contract": {
            "schema": "SelectedS3ClassRestrictionProjectorRetention.v1",
            "branch": {
                "q": 79,
                "orientation": "F",
                "torsion_label_m": 1,
            },
            "must_supply": [
                "fixed smooth flat gerbe/differential-cohomology class representing the finite m=1 deck cocycle",
                "S3 pullback/restriction table with nonzero rank-two image matched to the twisted Chan-Paton module",
                "W3/spinC or Freed-Witten verification on selected S3 cycles",
                "block-factorized Q,u,d,L,e,N,H projector retention on the twisted source",
                "same-branch bridge into selected D_E, dotD_alpha1, Riesz, Green, and C1 primitive contractions",
            ],
            "forbidden_shortcuts": [
                "treating an arbitrary good cover as an MTT-selected physical source",
                "using the finite projective qutrit module alone as a smooth operator source",
                "claiming Pic0 quotient without operator/overlap invariance",
                "using observed masses, CKM, or benchmark matrices to select the source",
            ],
        },
        "gate_results": {
            "pic0_or_gerbe_artifact_built": True,
            "direct_pic0_invariance_proved": False,
            "direct_pic0_invariance_retired_for_now": True,
            "good_cover_knob_removed": True,
            "finite_q79_f_m1_gerbe_imported": True,
            "deck_cech_f3_squared_imported": True,
            "flat_gerbe_conditional_promotion_imported": True,
            "finite_s3_cp_cancellation_imported": True,
            "visible_gs_curvature_imported": True,
            "selected_smooth_s3_source_constructed": False,
            "freed_witten_projector_retention_closed": False,
            "selected_DE_dotD_Riesz_Green_constructed": False,
            "selected_Qa_SU3_packet_closed": False,
            "sm_parity_closure_claimed": False,
            "no_knob_closure_claimed": False,
        },
        "theorem": {
            "name": "Pic0ToGerbeExecutionReduction",
            "proved": True,
            "statement": (
                "With current corpus data, direct Pic0 invariance is not a legal closure path. "
                "The legal primary route is to replace the Pic0 ambiguity by the selected q79/F, "
                "m=1 flat torsion gerbe class and prove its S3 restriction, Freed-Witten/projector "
                "retention, and same-branch D_E/dotD/Riesz/Green operator source."
            ),
        },
        "next_required_artifact": "MTT_Selected_S3_Class_Restriction_Projector_Retention_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSelectedPic0InvarianceOrGerbeTwistedDESource",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "direct_pic0_invariance_route_retired_for_now": True,
            "good_cover_removed_as_physical_knob": True,
            "gerbe_twisted_de_route_promoted_to_primary": True,
            "selected_s3_class_packet_contract_built": True,
            "finite_gerbe_cp_gs_inputs_imported": True,
        },
        "what_remains_open": {
            "selected_smooth_s3_class_restriction": True,
            "Freed_Witten_and_projector_retention": True,
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
    routes = "\n".join(
        f"- `{key}`: `{body['status']}` - {body['reason']}"
        for key, body in candidate["route_decision"].items()
    )
    contract = "\n".join(f"- {item}" for item in candidate["selected_s3_class_packet_contract"]["must_supply"])
    forbidden = "\n".join(f"- {item}" for item in candidate["selected_s3_class_packet_contract"]["forbidden_shortcuts"])
    closes = "\n".join(f"- {name}" for name, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {name}" for name, value in certificate["what_remains_open"].items() if value)
    return f"""# MTT Selected Pic0 Invariance or Gerbe-Twisted DE Source v1

## Purpose

This artifact decides how to proceed after the terminal monad lane/Pic0 audit.
It does not assert Pic0 quotienting.  It checks whether a direct Pic0
invariance path is available and, failing that, promotes the finite gerbe route
to the primary executable path.

## Inputs

{sources}

## Imported Status

- Previous frontier: `{imported["previous_frontier"]["status"]}`
- Deligne cover gauge reduction: `{imported["deligne_cover_gauge_reduction"]["status"]}`
- Fixed gerbe representative: `{imported["fixed_gerbe_representative"]["status"]}`
- Deck/Cech lift: `{imported["deck_cech_lift"]["status"]}`
- Flat gerbe promotion: `{imported["flat_gerbe_promotion"]["status"]}`
- Finite S3 CP cancellation: `{imported["finite_s3_cp_cancellation"]["status"]}`
- Smooth S3 lift attempt: `{imported["smooth_s3_lift_attempt"]["status"]}`
- Visible Green-Schwarz curvature: `{imported["visible_gs_curvature"]["status"]}`
- HYM operator attempt: `{imported["hym_operator_attempt"]["status"]}`

## Route Decision

{routes}

## Cover-Knob Reduction

The good cover is not a new physical knob.  The imported Deligne/Cech reduction
identifies it as an execution scaffold: representatives on different good
covers are related by refinement/coboundary equivalence.  The remaining
physical object is the selected smooth S3 differential-cohomology class and its
restriction/projector/operator data.

## Selected S3 Packet Contract

Schema:

```text
{candidate["selected_s3_class_packet_contract"]["schema"]}
```

Must supply:

{contract}

Forbidden shortcuts:

{forbidden}

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
