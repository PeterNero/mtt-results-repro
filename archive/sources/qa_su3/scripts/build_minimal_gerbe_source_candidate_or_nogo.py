"""Build the minimal gerbe-source candidate/no-go gate for Qa/SU3."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
DATA = ROOT / "candidate_data"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

INPUT = DATA / "twisted_section_ring_and_gerbe_source_gate.candidate.json"
OUTPUT_DATA = DATA / "minimal_gerbe_source_candidate_or_nogo.candidate.json"
OUTPUT_CERT = CERTS / "minimal_gerbe_source_candidate_or_nogo_certificate.json"


SOURCES = {
    "flux_iwasawa_gerbe": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
    "strominger_fixed_gerbe_class": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
    "q79_s3_class_closure": Q79 / "proof_corpus" / "Visible_Twisted_S3_Class_Restriction_Closure_v1.md",
    "q79_s3_smooth_source_lift_attempt": Q79 / "proof_corpus" / "Visible_Twisted_S3_Smooth_Source_Lift_Attempt_v1.md",
}


TERM_SETS = {
    "flux_iwasawa_gerbe": {
        "iwasawa": "Iwasawa",
        "flux_quantization": "Flux quantization",
        "heterotic_gerbe": "heterotic gerbe",
        "b_field_gerbe": "field gerbe",
        "bianchi": "Bianchi",
        "integral_periods": "integral periods",
    },
    "strominger_fixed_gerbe_class": {
        "deligne_2_gerbe": "Deligne 2-gerbe",
        "fixed_differential_cohomology_class": "fixed differential cohomology class",
        "global_curvature": "globally defined curvature",
        "twisted_laplacian": "twisted Laplacian",
        "bounded_twisted_projector": "Bounded twisted projector",
        "iwasawa": "Iwasawa",
    },
    "q79_s3_class_closure": {
        "selected_s3_flat_deligne_class": "selected S3 flat Deligne class",
        "smooth_freed_witten": "smooth S3 twisted Freed-Witten",
        "twisted_cp_module": "twisted CP module",
        "projector_retention": "projectors are retained",
        "not_full_visible_closure": "not the same as full visible-coordinate closure",
    },
    "q79_s3_smooth_source_lift_attempt": {
        "conditional_flat_deligne": "conditional flat Deligne/Cech",
        "candidate_iwasawa_deck": "candidate aspherical Iwasawa deck scaffold",
        "actual_good_cover_open": "actual good-cover Deligne/Cech data",
        "smooth_freed_witten_open": "smooth S3 Freed-Witten",
        "projector_retention_open": "twisted projector retention",
    },
}


def scan(path: Path, terms: dict[str, str]) -> dict[str, object]:
    if not path.exists():
        return {"path": str(path), "present": False, "terms": {key: False for key in terms}}
    text = path.read_text(encoding="utf-8", errors="ignore")
    folded = text.lower()
    return {
        "path": str(path),
        "present": True,
        "terms": {key: needle.lower() in folded for key, needle in terms.items()},
    }


def route(
    route_id: str,
    status: str,
    closes: list[str],
    blocks: list[str],
    evidence: list[str],
    promotion: str,
) -> dict[str, object]:
    return {
        "route_id": route_id,
        "status": status,
        "what_it_closes": closes,
        "what_blocks_promotion": blocks,
        "evidence_sources": evidence,
        "promotion_rule": promotion,
    }


def main() -> None:
    prior = json.loads(INPUT.read_text(encoding="utf-8"))
    scans = {key: scan(path, TERM_SETS[key]) for key, path in SOURCES.items()}

    c_twist_values = sorted(
        {
            item["space"]["gerbe_c_twist"]
            for item in prior["twisted_section_requirements"]
            if item["space"].get("gerbe_c_twist") != 0
        }
    )
    source_fields = {
        "selected_Deligne_Cech_or_B_field_representative_for_Qa_SU3_c_twist": False,
        "map_from_representative_to_c_twist_values_minus1_plus1": False,
        "same_branch_MTT_selection_of_Qa_SU3_source": False,
        "Freed_Witten_cancellation_for_Qa_SU3_twisted_modules": False,
        "Green_Schwarz_Bianchi_for_Qa_SU3_source": False,
        "twisted_section_bases_from_selected_source": False,
        "twisted_multiplication_constants_from_selected_source": False,
        "twisted_projector_or_operator_retention": False,
    }
    routes = [
        route(
            "global_Hhat_gerbe_from_iwasawa_flux",
            "STRUCTURAL_SOURCE_SUPPORTED_NOT_C_TWIST_PACKET",
            [
                "Corpus supports a globally meaningful B-field/gerbe structure on Iwasawa-type heterotic flux backgrounds.",
                "Bianchi and integrality language is present in the invariant flux construction.",
            ],
            [
                "No explicit representative is identified with the Qa/SU3 c=+/-1 twisted module charges.",
                "No twisted section bases or multiplication constants are derived from this source.",
            ],
            ["flux_iwasawa_gerbe"],
            "Promote only after an explicit Qa/SU3 c-twist representative and Bianchi/Freed-Witten check are supplied.",
        ),
        route(
            "fixed_differential_cohomology_class_from_strominger_selection",
            "SELECTION_PRINCIPLE_SUPPORTED_CLASS_NOT_EXPLICIT",
            [
                "Corpus treats the B-field as a fixed differential-cohomology/Deligne gerbe object.",
                "Twisted Laplacian and bounded projector language exists on the Strominger branch.",
            ],
            [
                "The selected class is not instantiated as the Qa/SU3 source packet.",
                "The link from fixed Strominger sector to the monad c-axis twist remains unproved.",
            ],
            ["strominger_fixed_gerbe_class"],
            "Promote only when the fixed class is computed in the same branch and acts on the Qa/SU3 monad spaces.",
        ),
        route(
            "q79_s3_flat_deligne_import",
            "ADJACENT_GUARDRAIL_NOT_SAME_SOURCE",
            [
                "q79 supplies the strongest nearby pattern: selected flat Deligne class plus twisted CP cancellation.",
                "It gives a concrete checklist for finite class, restriction, cancellation, and projector retention.",
            ],
            [
                "S3 visible stack data is not automatically the Qa/SU3 Iwasawa c-twist source.",
                "Importing the result directly would mix branches and would be target/proxy fitting.",
            ],
            ["q79_s3_class_closure", "q79_s3_smooth_source_lift_attempt"],
            "Use only as a guardrail unless a same-branch restriction map from S3 data to Qa/SU3 c-twist is proved.",
        ),
        route(
            "twisted_section_ring_candidate",
            "BEST_CURRENT_ROUTE_SOURCE_OPEN",
            [
                "All five monad products are typed by opposite c-gerbe twists and land in untwisted P.",
                "The literal c-axis line-bundle obstruction has a mathematically coherent repair target.",
            ],
            [
                "The gerbe source itself is still unselected.",
                "Basis-level section algebra and operator exit are still absent.",
            ],
            ["twisted_section_ring_and_gerbe_source_gate"],
            "Promote after source selection, module construction, multiplication table, and operator retention all pass.",
        ),
    ]
    candidate = {
        "candidate": "SelectedQaSU3MinimalGerbeSourceCandidateOrNoGo",
        "status": "MINIMAL_GERBE_SOURCE_CANDIDATE_BUILT_SELECTED_SOURCE_OPEN",
        "input_status": prior["status"],
        "c_twist_values_required": c_twist_values,
        "source_scans": scans,
        "evaluated_routes": routes,
        "gate_results": {
            "minimal_gerbe_source_candidate_exists": True,
            "structural_corpus_support_for_gerbe_source": all(
                scans[key]["present"] for key in ["flux_iwasawa_gerbe", "strominger_fixed_gerbe_class"]
            ),
            "same_branch_Qa_SU3_selected_source_supplied": False,
            "Freed_Witten_Bianchi_verified_for_Qa_SU3": False,
            "twisted_section_bases_supplied": False,
            "operator_exit_supplied": False,
            "no_go_triggered": False,
        },
        "source_packet_fields": source_fields,
        "decision": {
            "best_current_path": "construct a same-branch Qa/SU3 Deligne/Cech or B-field representative whose Dixmier-Douady/c-twist class is +/-1 on the required twisted modules",
            "strict_no_go_condition": "If every selected MTT gerbe/flux source has zero restriction to the Qa/SU3 c-axis twist class, the twisted-section route fails and the proof must exit through A01/D_E instead.",
            "why_not_closed": "The corpus gives structural gerbe machinery and nearby q79 twisted-class closure, but not the actual selected Qa/SU3 source map.",
        },
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3MinimalGerbeSourceCandidateOrNoGo",
        "status": "QA_SU3_MINIMAL_GERBE_SOURCE_CANDIDATE_BUILT_SELECTED_SOURCE_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "minimal_candidate_route_identified": True,
            "corpus_supports_iwasawa_or_strominger_gerbe_machinery": candidate["gate_results"][
                "structural_corpus_support_for_gerbe_source"
            ],
            "q79_s3_twisted_class_used_only_as_guardrail": True,
            "literal_no_go_not_triggered": True,
        },
        "what_remains_open": source_fields | {
            "basis_level_section_ring": True,
            "operator_exit": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": "Selected_Qa_SU3_CTwist_Deligne_Cech_Template_v1",
        "fallback_required_if_no_source": "Selected_Qa_SU3_A01_DE_Operator_Exit_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
