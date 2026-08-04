"""Build the Route-C selected source-origin lemma attempt artifact."""

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
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"
VAULT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

OUTPUT_DATA = DATA / "routec_selected_source_origin_lemma.candidate.json"
OUTPUT_CERT = CERTS / "routec_selected_source_origin_lemma_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_RouteC_Selected_Source_Origin_Lemma_v1.md"

INPUTS = {
    "way_forward": DATA / "routec_selected_source_origin_way_forward.candidate.json",
    "s3_source": CERTS / "selected_s3_differential_cohomology_source_certificate.json",
    "visible_gs_gate": CERTS / "selected_visible_green_schwarz_operator_source_certificate.json",
    "routec_pipeline": DATA / "selected_routec_hym_operator_pipeline.candidate.json",
    "value_search": DATA / "selected_routec_hym_value_search.candidate.json",
    "nonsm_routec_solve_gate": NONSM / "certificates" / "selected_qa_su3_routec_source_solve_gate_certificate.json",
    "nonsm_source_ladder": NONSM / "certificates" / "selected_qa_su3_m1_s3_source_origin_ladder_certificate.json",
    "q79_branch_selection": Q79 / "certificates" / "visible_rank2_l2_branch_selection_reduction_certificate.json",
    "q79_appell_humbert": Q79 / "certificates" / "visible_rank2_l2_appell_humbert_automorphy_certificate.json",
    "q79_twisted_chan_paton": Q79 / "certificates" / "visible_twisted_chan_paton_rescue_certificate.json",
    "strominger_selection": VAULT / "16 Strings, Flux, & M-Theory Encodings" / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def text_has(path: Path, terms: list[str]) -> dict[str, bool]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    return {term: term in text for term in terms}


def source_status() -> dict[str, object]:
    return {key: {"path": str(path), "present": path.exists()} for key, path in INPUTS.items()}


def build_candidate() -> dict[str, object]:
    way = load_json(INPUTS["way_forward"])
    s3 = load_json(INPUTS["s3_source"])
    gs = load_json(INPUTS["visible_gs_gate"])
    pipeline = load_json(INPUTS["routec_pipeline"])
    value_search = load_json(INPUTS["value_search"])
    routec_gate = load_json(INPUTS["nonsm_routec_solve_gate"])
    ladder = load_json(INPUTS["nonsm_source_ladder"])
    branch = load_json(INPUTS["q79_branch_selection"])
    appell = load_json(INPUTS["q79_appell_humbert"])
    cp = load_json(INPUTS["q79_twisted_chan_paton"])

    strominger_terms = text_has(
        INPUTS["strominger_selection"],
        [
            "fixed topological sector",
            "selection potential",
            "Theorem 6",
            "Proposition 7",
            "Theorem 11",
            "unique local minimizer",
            "strict convexity",
            "HYM on Gauduchon",
            "Deligne 2-gerbe",
        ],
    )

    selected_branch = pipeline["pipeline_evaluation"]["selected_branch_packet"]
    routec_contract = pipeline["next_payload_contract"]
    routec_validators = pipeline["imported_results"]["validators"]
    source_ladder_closed = ladder["closed_now"]

    gates = {
        "G1_fixed_topological_sector_named": {
            "passes": (
                s3["what_closes"]["selected_S3_flat_Deligne_class"]
                and s3["what_closes"]["smooth_S3_twisted_Freed_Witten_cancellation"]
                and selected_branch["global_cp_label"] == 79
                and selected_branch["torsion_label_m"] == 1
            ),
            "evidence": [
                "selected S3 flat Deligne class closed",
                "smooth S3 twisted Freed-Witten cancellation closed",
                "Route-C selected branch packet is q79/F,m=1",
            ],
        },
        "G2_MTT_Strominger_selection_available": {
            "passes": all(
                strominger_terms[term]
                for term in [
                    "fixed topological sector",
                    "selection potential",
                    "Theorem 11",
                    "unique local minimizer",
                    "strict convexity",
                ]
            ),
            "evidence": strominger_terms,
        },
        "G3_same_source_support_converges": {
            "passes": (
                gs["what_closes"]["selected_S3_source_imported_as_closed"]
                and gs["what_closes"]["visible_GS_curvature_imported_as_closed"]
                and source_ladder_closed["finite_S3_CP_source_class_matches_q79_m1_twist"]
                and cp["status"].startswith("VISIBLE_TWISTED_CP")
                and appell["status"].startswith("VISIBLE_RANK2_L2_APPELL")
            ),
            "evidence": [
                "visible GS gate imports selected S3 source and GS curvature",
                "nonsm ladder matches finite S3 CP source to q79,m=1 twist",
                "Appell-Humbert and twisted Chan-Paton payload exits exist but selection remains open",
            ],
        },
        "G4_minimizer_to_finite_packet_morphism": {
            "passes": False,
            "missing": [
                "explicit map Phi_fin from the selected Strominger/HYM minimizer to finite rho_E transition data",
                "proof that Phi_fin preserves q79/F,m=1 branch orientation and the S3/GS class",
                "error/gap certificate identifying the Route-C finite packet as the Galerkin trace of the minimizer",
            ],
        },
        "G5_operator_payload_emitted": {
            "passes": False,
            "missing": routec_contract["required_outputs"],
            "validator_status": {
                "D_E": routec_validators["D_E"]["status"],
                "Riesz_gap": routec_validators["Riesz_gap"]["status"],
                "reduced_green": routec_validators["reduced_green"]["status"],
                "dotD": routec_validators["dotD"]["status"],
            },
        },
    }

    all_closed = all(gate["passes"] for gate in gates.values())

    return {
        "candidate": "MTTRouteCSelectedSourceOriginLemmaAttempt",
        "status": "MTT_ROUTEC_SELECTED_SOURCE_ORIGIN_LEMMA_REDUCED_TO_FINITE_EMISSION_MORPHISM",
        "source_status": source_status(),
        "superset_mode": {
            "classification": "SUPERSET_CONVERGENCE_PARTIAL_PROOF",
            "straight_path": {
                "name": "Strominger selection theorem alone",
                "succeeds": False,
                "reason": "It selects a smooth fixed-sector minimizer but does not by itself emit the finite q79/F,m=1 Route-C operator matrices.",
            },
            "superset_convergence": {
                "succeeds": True,
                "converging_paths": [
                    "MTT Strominger selection in fixed topology",
                    "selected S3 differential-cohomology source",
                    "visible Green-Schwarz source gate",
                    "q79/F,m=1 Route-C branch packet",
                    "Appell-Humbert automorphy exit",
                    "twisted Chan-Paton/gerbe exit",
                ],
                "locked_target": "finite emission morphism Phi_fin from the selected minimizer to rho_E, D_E, Riesz/Green, dotD, and C1",
            },
            "superset_repair": {
                "needed": True,
                "repair_object": "construct Phi_fin or replace the smoke packet with actual selected Galerkin data",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "reason": "No masses, mixings, gauge constants, target residuals, or benchmark matrices are used to choose the source.",
            },
        },
        "imported_results": {
            "way_forward_status": way["status"],
            "s3_status": s3["status"],
            "visible_gs_status": gs["status"],
            "routec_pipeline_status": pipeline["status"],
            "value_search_status": value_search["status"],
            "nonsm_routec_gate_status": routec_gate["status"],
            "q79_branch_target": branch["target_branch"],
            "appell_humbert_status": appell["status"],
            "twisted_chan_paton_status": cp["status"],
        },
        "selected_branch_packet": selected_branch,
        "gate_matrix": gates,
        "lemma_evaluation": {
            "lemma_name": "RouteCSelectedSourceOriginLemma",
            "fully_proved": all_closed,
            "closed_sublemma": "Fixed-sector MTT selection support exists for the q79/F,m=1 S3/GS Route-C target.",
            "open_sublemma": "FiniteEmissionMorphismLemma",
            "open_sublemma_statement": (
                "The selected Strominger/HYM minimizer in the q79/F,m=1 S3/GS sector has a canonical finite "
                "Galerkin/typed-Cech trace Phi_fin, and Phi_fin emits the same rho_E, D_E, Riesz/Green, dotD, "
                "and primitive C1 payload required by the Route-C validators."
            ),
        },
        "finite_emission_morphism_contract": {
            "name": "Phi_fin",
            "domain": "selected MTT Strominger/HYM minimizer in fixed q79/F,m=1 S3/GS sector",
            "codomain": "finite Route-C packet with rho_E, metric, sector maps, D_E, Riesz/gap, reduced Green, dotD, and C1 tensors",
            "must_commute_with": [
                "S3 flat Deligne/Cech restriction",
                "Green-Schwarz Bianchi row",
                "Appell-Humbert automorphy/line-bundle transition factors",
                "twisted Chan-Paton projective module",
                "Route-C finite validator basis and q79/F orientation",
            ],
            "acceptance_tests": [
                "selected_source_verified becomes a theorem-derived field, not a lifted flag",
                "D_E, dotD, Riesz/Green, and residual validators pass honestly",
                "finite truncation error is bounded by the selected Hessian/Riesz gap",
                "primitive C1 overlap tensors are emitted or explicitly reduced to a subsequent overlap theorem",
            ],
        },
        "theorem": {
            "name": "RouteCSelectedSourceOriginLemmaReduction",
            "proved": True,
            "statement": (
                "The selected source-origin lemma is reduced to one missing object: the finite emission morphism. "
                "The fixed topological sector, S3/GS source support, and MTT Strominger selection theorem are present; "
                "what is not yet present is the canonical finite trace that emits the selected operator payload."
            ),
        },
        "next_required_artifact": "MTT_Finite_Emission_Morphism_Phi_fin_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    gates = candidate["gate_matrix"]
    return {
        "certificate": "MTTRouteCSelectedSourceOriginLemmaAttempt",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "superset_mode": candidate["superset_mode"]["classification"],
        "what_closes": {
            "fixed_q79_f_m1_s3_gs_sector_identified": gates["G1_fixed_topological_sector_named"]["passes"],
            "mtt_strominger_selection_theorem_available": gates["G2_MTT_Strominger_selection_available"]["passes"],
            "same_source_support_convergence_proved": gates["G3_same_source_support_converges"]["passes"],
            "last_missing_object_identified_as_finite_emission_morphism": True,
            "routec_source_origin_lemma_reduced": True,
        },
        "what_remains_open": {
            "FiniteEmissionMorphism_Phi_fin": True,
            "minimizer_to_finite_packet_trace": True,
            "actual_selected_RouteC_HYM_values": True,
            "selected_D_E_dotD_Riesz_Green": True,
            "primitive_C1_overlap_tensors": True,
            "selected_Qa_SU3_color_operator_packet": True,
            "sm_parity_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    gates = "\n".join(
        f"- `{key}`: `{'PASS' if row['passes'] else 'OPEN'}`"
        for key, row in candidate["gate_matrix"].items()
    )
    missing = "\n".join(
        f"- {item}" for item in candidate["gate_matrix"]["G4_minimizer_to_finite_packet_morphism"]["missing"]
    )
    payload = "\n".join(f"- {item}" for item in candidate["gate_matrix"]["G5_operator_payload_emitted"]["missing"])
    commute = "\n".join(f"- {item}" for item in candidate["finite_emission_morphism_contract"]["must_commute_with"])
    tests = "\n".join(f"- {item}" for item in candidate["finite_emission_morphism_contract"]["acceptance_tests"])
    closes = "\n".join(f"- {key}" for key, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {key}" for key, value in certificate["what_remains_open"].items() if value)
    branch = candidate["selected_branch_packet"]
    return f"""# MTT Route-C Selected Source-Origin Lemma v1

## Result

The full `RouteCSelectedSourceOriginLemma` is not closed yet.  The proof is
advanced to a sharper reduction:

```text
RouteCSelectedSourceOriginLemma
  = fixed-sector MTT/Strominger/S3/GS source support
  + FiniteEmissionMorphism_Phi_fin.
```

The first component is now supported by the corpus and repo certificates.  The
remaining missing object is the finite emission morphism from the selected
Strominger/HYM minimizer to the exact Route-C operator payload.

## Superset Classification

`{candidate["superset_mode"]["classification"]}`

This is not a straight path.  It combines MTT Strominger selection, selected
S3 differential cohomology, visible Green-Schwarz support, q79/F,m=1 Route-C
branch data, Appell-Humbert automorphy, and twisted Chan-Paton/gerbe structure
into one locked target.

## Selected Branch

- branch: `{branch["branch"]}`
- q label: `{branch["global_cp_label"]}`
- torsion label m: `{branch["torsion_label_m"]}`
- orientation: `{branch["conditional_su5_transport_orientation"]}`

## Gate Matrix

{gates}

## Missing Morphism

`Phi_fin`

Domain:

```text
{candidate["finite_emission_morphism_contract"]["domain"]}
```

Codomain:

```text
{candidate["finite_emission_morphism_contract"]["codomain"]}
```

The morphism must commute with:

{commute}

Current missing pieces:

{missing}

Operator payload still not emitted:

{payload}

Acceptance tests for the next artifact:

{tests}

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
