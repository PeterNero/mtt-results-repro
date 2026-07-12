"""Build the twisted section-ring and gerbe-source gate for Qa/SU3."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
DATA = ROOT / "candidate_data"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

INPUT = DATA / "gerbe_twist_cancellation_packet.candidate.json"
OUTPUT_CERT = CERTS / "twisted_section_ring_and_gerbe_source_gate_certificate.json"
OUTPUT_DATA = DATA / "twisted_section_ring_and_gerbe_source_gate.candidate.json"


SOURCES = {
    "q79_twisted_s3_source_attempt": Q79 / "proof_corpus" / "Visible_Twisted_S3_Source_Packet_Attempt_v1.md",
    "q79_twisted_s3_cp_cancellation": Q79 / "proof_corpus" / "Visible_Twisted_S3_Finite_Chan_Paton_Cancellation_v1.md",
    "flux_iwasawa": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
}


def scan(path: Path, terms: dict[str, str]) -> dict[str, object]:
    if not path.exists():
        return {"path": str(path), "present": False, "terms": {key: False for key in terms}}
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    return {"path": str(path), "present": True, "terms": {key: term.lower() in text for key, term in terms.items()}}


def main() -> None:
    cancellation = json.loads(INPUT.read_text(encoding="utf-8"))
    scans = {
        "q79_twisted_s3_source_attempt": scan(
            SOURCES["q79_twisted_s3_source_attempt"],
            {
                "Deligne_Cech": "Deligne/Cech",
                "B_field": "B-field",
                "twisted_CP": "twisted Chan-Paton",
                "Freed_Witten": "Freed-Witten",
                "projector_retention": "projector-retention",
                "source_not_selected": "source is not yet constructed",
            },
        ),
        "q79_twisted_s3_cp_cancellation": scan(
            SOURCES["q79_twisted_s3_cp_cancellation"],
            {
                "finite_CP_cancellation": "finite twisted",
                "gerbe_class": "gerbe class",
                "smooth_open": "smooth Deligne/Cech",
            },
        ),
        "flux_iwasawa": scan(
            SOURCES["flux_iwasawa"],
            {
                "Bianchi": "Bianchi",
                "H_field": "H=",
                "gerbe": "gerbe",
                "HYM": "Hermitian--Yang--Mills",
                "Iwasawa": "Iwasawa",
            },
        ),
    }
    pair_results = cancellation["pair_results"]
    twisted_section_requirements = [
        {
            "space": pair["F"],
            "module_kind": "twisted" if pair["F"]["gerbe_c_twist"] else "ordinary",
            "basis_supplied": False,
        }
        for pair in pair_results
    ] + [
        {
            "space": pair["G"],
            "module_kind": "twisted" if pair["G"]["gerbe_c_twist"] else "ordinary",
            "basis_supplied": False,
        }
        for pair in pair_results
    ]
    p_space = {"space": cancellation["P"], "module_kind": "ordinary", "basis_supplied": False}
    source_packet_fields = {
        "source_selected_by_mtt": False,
        "fixed_differential_cohomology_or_gerbe_class": False,
        "geometric_Deligne_Cech_or_B_field_source_constructed": False,
        "twisted_module_source_constructed": False,
        "twisted_section_bases_constructed": False,
        "twisted_multiplication_table_constructed": False,
        "green_schwarz_bianchi_verified": False,
        "freed_witten_verified": False,
        "twisted_projector_or_operator_retention_verified": False,
    }
    typed_multiplication_law = [
        {
            "pair": pair["pair"],
            "law": "H0(L_ab,F with twist t) x H0(L_ab,G with twist -t) -> H0(P untwisted)",
            "twist_cancellation_verified": pair["gerbe_twist_cancels"],
            "ordinary_ab_target_verified": pair["ordinary_ab_product_matches_P_ab"],
            "basis_level_product_computed": False,
        }
        for pair in pair_results
    ]
    candidate = {
        "candidate": "SelectedQaSU3TwistedSectionRingAndGerbeSourceGate",
        "status": "TWISTED_SECTION_RING_GATE_BUILT_TYPING_PASS_SOURCE_VALUES_OPEN",
        "input_status": cancellation["status"],
        "source_scans": scans,
        "twisted_section_requirements": twisted_section_requirements + [p_space],
        "typed_multiplication_law": typed_multiplication_law,
        "source_packet_fields": source_packet_fields,
        "what_is_solved": [
            "The c-axis obstruction is retyped as a gerbe/twisted-module charge.",
            "Every monad product has opposite twists and lands in untwisted P.",
            "The ordinary closed a,b line-bundle part remains available for section algebra.",
        ],
        "what_is_not_solved": [
            "No selected smooth gerbe/B-field representative has been supplied.",
            "No twisted section bases or multiplication constants have been computed.",
            "No Freed-Witten/Bianchi/source admissibility proof has been supplied.",
            "No D_E/rho_E/heat/torsion operator exit is supplied.",
        ],
        "target_fitting_used": False,
    }
    all_typing_passes = all(
        item["twist_cancellation_verified"] and item["ordinary_ab_target_verified"]
        for item in typed_multiplication_law
    )
    certificate = {
        "certificate": "SelectedQaSU3TwistedSectionRingAndGerbeSourceGate",
        "status": "QA_SU3_TWISTED_SECTION_RING_GATE_TYPING_PASS_SOURCE_VALUES_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "twisted_monad_typing_rule": True,
            "all_typed_products_land_in_untwisted_P": all_typing_passes,
            "q79_twisted_source_pattern_imported_as_guardrail_not_data": True,
        },
        "what_remains_open": {
            **source_packet_fields,
            "operator_exit": True,
            "qa_su3_packet_closed": False,
        },
        "route_update": {
            "primary_route": "selected_gerbe_B_field_or_twisted_CP_source_for_c_twist",
            "parallel_route": "source_certified_A01_D_E_operator_exit",
            "next_required_artifact": "Selected_Qa_SU3_Minimal_Gerbe_Source_Candidate_or_NoGo_v1",
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    text_data = json.dumps(candidate, indent=2, sort_keys=True)
    text_cert = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(text_data + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(text_cert + "\n", encoding="utf-8")
    print(text_cert)


if __name__ == "__main__":
    main()
