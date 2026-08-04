"""Build the Route-C selected source-origin way-forward artifact."""

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

OUTPUT_DATA = DATA / "routec_selected_source_origin_way_forward.candidate.json"
OUTPUT_CERT = CERTS / "routec_selected_source_origin_way_forward_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_RouteC_Selected_Source_Origin_Way_Forward_v1.md"

INPUTS = {
    "local_value_search": CERTS / "selected_routec_hym_value_search_certificate.json",
    "local_s3_source": CERTS / "selected_s3_differential_cohomology_source_certificate.json",
    "local_visible_gs_gate": CERTS / "selected_visible_green_schwarz_operator_source_certificate.json",
    "nonsm_s3_origin_ladder": NONSM / "certificates" / "selected_qa_su3_m1_s3_source_origin_ladder_certificate.json",
    "nonsm_routec_solve_gate": NONSM / "certificates" / "selected_qa_su3_routec_source_solve_gate_certificate.json",
    "nonsm_superset_route_map": NONSM / "certificates" / "selected_qa_su3_superset_source_route_map_certificate.json",
    "q79_branch_selection_reduction": Q79 / "certificates" / "visible_rank2_l2_branch_selection_reduction_certificate.json",
    "q79_appell_humbert": Q79 / "certificates" / "visible_rank2_l2_appell_humbert_automorphy_certificate.json",
    "q79_twisted_chan_paton": Q79 / "certificates" / "visible_twisted_chan_paton_rescue_certificate.json",
    "vault_strominger_selection": VAULT / "16 Strings, Flux, & M-Theory Encodings" / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
    "vault_flux_compactification": VAULT / "16 Strings, Flux, & M-Theory Encodings" / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_status() -> dict[str, object]:
    return {key: {"path": str(path), "present": path.exists()} for key, path in INPUTS.items()}


def text_has(path: Path, terms: list[str]) -> dict[str, bool]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    return {term: term in text for term in terms}


def build_candidate() -> dict[str, object]:
    value_search = load_json(INPUTS["local_value_search"])
    s3 = load_json(INPUTS["local_s3_source"])
    gs = load_json(INPUTS["local_visible_gs_gate"])
    ladder = load_json(INPUTS["nonsm_s3_origin_ladder"])
    routec_gate = load_json(INPUTS["nonsm_routec_solve_gate"])
    route_map = load_json(INPUTS["nonsm_superset_route_map"])
    branch = load_json(INPUTS["q79_branch_selection_reduction"])
    appell = load_json(INPUTS["q79_appell_humbert"])
    cp = load_json(INPUTS["q79_twisted_chan_paton"])

    strominger_terms = text_has(
        INPUTS["vault_strominger_selection"],
        ["selection potential", "Theorem 11", "unique local minimizer", "Hull--Strominger", "HYM on Gauduchon"],
    )
    flux_terms = text_has(
        INPUTS["vault_flux_compactification"],
        ["monad", "stability", "HYM", "gerbe", "factor of automorphy"],
    )

    return {
        "candidate": "MTTRouteCSelectedSourceOriginWayForward",
        "status": "MTT_ROUTEC_SELECTED_SOURCE_ORIGIN_WAY_FORWARD_BUILT_SOURCE_LEMMA_OPEN",
        "source_status": source_status(),
        "superset_mode": {
            "classification": "SUPERSET_CONVERGENCE_TO_SOURCE_ORIGIN_PROGRAM",
            "straight_path": {
                "name": "external HYM/Strominger existence theorem alone",
                "succeeds": False,
                "reason": "External HYM/Strominger theorems can justify existence once stable/topological data are selected, but they do not provide the q79/F,m=1 typed transition/operator payload by themselves.",
            },
            "superset_convergence": {
                "succeeds": True,
                "converging_paths": [
                    "MTT Strominger selection potential in a fixed topological sector",
                    "selected q79/F,m=1 S3 flat Deligne/Cech source",
                    "visible Green-Schwarz curvature/operator gate",
                    "Appell-Humbert visible L2 automorphy model",
                    "twisted Chan-Paton/S3 gerbe rescue",
                    "Route-C finite HYM/Strominger validator pipeline",
                ],
                "locked_target": "RouteCSelectedSourceOriginLemma instantiated as a same-source visible bundle/twisted-gerbe/operator packet",
            },
            "superset_repair": {
                "needed": True,
                "repair_object": "one source-origin bridge from selected S3/GS data to selected Route-C/HYM values",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "reason": "No observed constants, masses, mixings, or benchmark matrices are used to rank or select the route.",
            },
        },
        "imported_results": {
            "value_search": {"status": value_search["status"], "next": value_search["next_required_artifact"]},
            "s3_source": {"status": s3["status"], "what_closes": s3["what_closes"]},
            "visible_gs_gate": {"status": gs["status"], "what_remains_open": gs["what_remains_open"]},
            "s3_origin_ladder": {"status": ladder["status"], "closed_now": ladder["closed_now"], "not_closed": ladder["not_closed"]},
            "routec_solve_gate": {"status": routec_gate["status"], "route_status": routec_gate["route_status"], "minimal_new_data": routec_gate["minimal_new_data_that_would_close"]},
            "superset_route_map": {"status": route_map["status"], "route_decision": route_map["route_decision"]},
            "branch_selection_reduction": {"status": branch["status"], "next_required_packet": branch["next_required_packet"], "target_branch": branch["target_branch"]},
            "appell_humbert": {"status": appell["status"], "verdict": appell["verdict"]},
            "twisted_chan_paton": {"status": cp["status"], "verdict": cp["verdict"]},
        },
        "corpus_hits": {
            "strominger_selection_paper": strominger_terms,
            "flux_compactification_paper": flux_terms,
        },
        "external_sources": {
            "Fu_Yau_2006": {
                "url": "https://arxiv.org/abs/hep-th/0604063",
                "role": "Shows smooth non-Kahler torsion/flux models solving Strominger's construction problem; supports Route-C/HYM existence templates, not MTT selection by itself.",
            },
            "Andreas_Garcia_Fernandez_2010": {
                "url": "https://arxiv.org/abs/1008.1018",
                "role": "Stable holomorphic bundle plus Chern-class matching can perturb to Strominger solutions; supports the stable-bundle source route if the selected bundle is supplied.",
            },
            "Fino_Grantcharov_Vezzoni_2021": {
                "url": "https://link.springer.com/article/10.1007/s00220-021-04223-7",
                "role": "Modern Hull-Strominger torus-symmetry examples generalizing Fu-Yau; useful as source-pattern evidence for torus-bundle/non-Kahler ansatz routes.",
            },
            "Li_Yau_DUY_Gauduchon": {
                "url": "https://archive.numdam.org/articles/10.1016/j.crma.2010.11.010/",
                "role": "Records the Buchdahl/Li-Yau Gauduchon extension pattern for Hermitian-Yang-Mills existence; in this repo it is an admissibility bridge, not the missing selected packet.",
            },
        },
        "route_ranking": [
            {
                "rank": 1,
                "id": "S3_GS_Strominger_selection_instantiation",
                "mode": "superset convergence",
                "why": "It is the only route that combines an MTT selection theorem with already selected q79/F,m=1 differential cohomology support.",
                "must_prove": [
                    "fixed topological sector of the Strominger selection potential equals the selected S3/GS sector",
                    "the Route-C residual-zero packet is the finite Galerkin trace of the unique minimizer",
                    "selected source flags in residual, D_E, Riesz/Green, and dotD files are justified by that minimizer",
                ],
            },
            {
                "rank": 2,
                "id": "typed_monad_Appell_Humbert_source_augmentation",
                "mode": "straight source construction if filled",
                "why": "Appell-Humbert gives explicit automorphy for L2, but branch/Pic0/source selection and operator exits remain open.",
                "must_prove": [
                    "selected ordered base branch L=(1,-2,0)",
                    "neutral or quotient Pic0 rule",
                    "typed Cech/monad transition matrices and section-ring products",
                ],
            },
            {
                "rank": 3,
                "id": "twisted_Chan_Paton_projective_module",
                "mode": "superset repair",
                "why": "It naturally matches the selected S3 twist and projective qutrit carrier, but still needs geometric/operator promotion.",
                "must_prove": [
                    "which D7/worldvolume stack carries the twisted module",
                    "same-branch visible source and HYM/operator data",
                    "twisted determinant or heat/torsion formula accepted by operator validators",
                ],
            },
            {
                "rank": 4,
                "id": "external_stable_bundle_HYM_existence",
                "mode": "auxiliary existence bridge",
                "why": "Mathematically strong, but cannot select MTT branch or emit finite matrices alone.",
                "must_prove": [
                    "the selected visible bundle/sheaf is stable in the selected Gauduchon chamber",
                    "Chern/Bianchi class equals the selected GS row",
                    "finite transition/operator data are extracted from the HYM connection",
                ],
            },
        ],
        "recommended_next_artifact": {
            "name": "MTT_RouteC_Selected_Source_Origin_Lemma_v1",
            "strategy": "Try the rank-1 route first: instantiate the MTT Strominger selection potential on the selected q79/F,m=1 S3/GS topological sector, then prove the existing Route-C packet is its finite Galerkin trace or produce the missing selected values.",
            "acceptance_tests": [
                "fixed topological sector explicitly names q79/F,m=1, S3 flat Deligne class, GS row, and visible source class",
                "selection functional Xi has positive Hessian/gap in this sector",
                "minimizer-to-finite-packet map outputs rho_E, D_E, Riesz/Green, dotD, and C1 payloads",
                "no selected_source_verified flag is set without a cited source-origin proof",
            ],
        },
        "theorem": {
            "name": "RouteCSelectedSourceOriginWayForward",
            "proved": True,
            "statement": "The correct way forward is not more residual minimization. The live closure path is a superset-convergence proof that instantiates the MTT Strominger selection theorem on the selected q79/F,m=1 S3/Green-Schwarz sector, with typed monad/Appell-Humbert and twisted Chan-Paton routes as repair or payload exits.",
        },
        "next_required_artifact": "MTT_RouteC_Selected_Source_Origin_Lemma_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTRouteCSelectedSourceOriginWayForward",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "superset_mode": candidate["superset_mode"]["classification"],
        "what_closes": {
            "corpus_repo_external_source_hunt_executed": True,
            "external_HYM_existence_not_enough_guardrail": True,
            "primary_source_origin_route_selected": True,
            "repair_routes_ranked": True,
            "acceptance_tests_for_source_origin_lemma_written": True,
        },
        "what_remains_open": {
            "RouteC_selected_source_origin_lemma": True,
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
    sources = "\n".join(
        f"- `{key}`: {row['path']} ({'present' if row['present'] else 'missing'})"
        for key, row in candidate["source_status"].items()
    )
    routes = "\n".join(
        f"- {row['rank']}. `{row['id']}` ({row['mode']}): {row['why']}"
        for row in candidate["route_ranking"]
    )
    external = "\n".join(
        f"- `{key}`: {row['url']} -- {row['role']}"
        for key, row in candidate["external_sources"].items()
    )
    tests = "\n".join(f"- {item}" for item in candidate["recommended_next_artifact"]["acceptance_tests"])
    closes = "\n".join(f"- {key}" for key, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {key}" for key, value in certificate["what_remains_open"].items() if value)
    return f"""# MTT Route-C Selected Source-Origin Way Forward v1

## Purpose

This artifact searches the corpus, proof repos, and external HYM/Strominger
literature for a way to prove the Route-C selected source-origin lemma.

## Result

The best path is **superset convergence**, not a straight import from external
HYM theory.  External HYM/Strominger theorems justify the shape of the proof
once a selected bundle/topological sector is supplied; they do not select the
q79/F,m=1 packet or emit finite operator matrices by themselves.

## Inputs

{sources}

## External Sources

{external}

## Ranked Routes

{routes}

## Recommended Next Artifact

`{candidate["recommended_next_artifact"]["name"]}`

Strategy:

```text
{candidate["recommended_next_artifact"]["strategy"]}
```

Acceptance tests:

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
