"""Build the Strominger/Iwasawa source-to-c-twist map or no-go gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

INPUT = DATA / "ctwist_source_value_search.candidate.json"
OUTPUT_DATA = DATA / "strominger_source_to_ctwist_map_or_nogo.candidate.json"
OUTPUT_CERT = CERTS / "strominger_source_to_ctwist_map_or_nogo_certificate.json"

SOURCES = {
    "strominger": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
    "iwasawa_flux": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
    "q79_s3": Q79 / "proof_corpus" / "Visible_Twisted_S3_Class_Restriction_Closure_v1.md",
}


def scan(path: Path, terms: dict[str, str]) -> dict[str, object]:
    if not path.exists():
        return {"path": str(path), "present": False, "terms": {key: False for key in terms}}
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    return {
        "path": str(path),
        "present": True,
        "terms": {key: term.lower() in text for key, term in terms.items()},
    }


def map_row(
    route_id: str,
    status: str,
    closes: list[str],
    missing: list[str],
    verdict: str,
) -> dict[str, object]:
    return {
        "route_id": route_id,
        "status": status,
        "what_it_closes": closes,
        "missing_for_promotion": missing,
        "verdict": verdict,
    }


def main() -> None:
    prior = json.loads(INPUT.read_text(encoding="utf-8"))
    scans = {
        "strominger": scan(
            SOURCES["strominger"],
            {
                "fixed_topological_sector": "Fix a topological sector",
                "fixed_differential_class": "fixed differential cohomology class",
                "Hhat_global": "globally defined curvature",
                "Bianchi": "Bianchi",
                "gerbe_gauge_slice": "gerbe gauge slice",
            },
        ),
        "iwasawa_flux": scan(
            SOURCES["iwasawa_flux"],
            {
                "H_i_dbar_partial_J": "H = i(",
                "integral_periods": "integral periods",
                "B_field_global": "field gerbe is globally well-defined",
                "alpha1_support": "support only on",
                "iwasawa_orientation": "Iwasawa orientation",
            },
        ),
        "q79_s3": scan(
            SOURCES["q79_s3"],
            {
                "flat_H_zero": "curvature H = 0",
                "F3_2_table": "F_3^2",
                "central_cocycle": "qutrit central cocycle",
                "direct_s3_not_full": "not the same as full visible-coordinate closure",
            },
        ),
    }

    required_c_twists = [-1, 1]
    required_monad_map = {
        "source_class": "tau_QaSU3 in differential cohomology / DD class",
        "target": "central c-twist quotient carrying T_+1 and T_-1",
        "required_pairing": "pairing(tau_QaSU3, central quotient) = 1 generator; dual gives -1",
        "product_rule": "T_+1 tensor T_-1 -> T_0 for every monad product",
    }
    candidate_maps = [
        map_row(
            "direct_central_two_torus_restriction",
            "NOT_SUPPLIED",
            [
                "Would be the cleanest proof if a DD/tau restriction to the central z3 quotient were listed.",
            ],
            [
                "No current source gives DD(tau_QaSU3)|central.",
                "The literal invariant c two-form is already nonclosed, so ordinary restriction is invalid.",
            ],
            "OPEN_NOT_PROMOTABLE",
        ),
        map_row(
            "Hhat_curvature_transgression",
            "PARTIAL_FORM_SUPPORT_ONLY",
            [
                "Strominger/Iwasawa source supplies a global Hhat/H gerbe curvature with integral periods.",
                "Iwasawa H involves the nonclosed omega3 direction, so it is adjacent to the central geometry.",
            ],
            [
                "No explicit cycle, slant product, or transgression is supplied.",
                "No computation shows the transgressed class equals the c=+/-1 twist generator.",
                "Bianchi/Freed-Witten for the resulting module is not verified.",
            ],
            "LIVE_BUT_VALUES_OPEN",
        ),
        map_row(
            "finite_Z3_torsion_extraction",
            "OFF_BRANCH_PATTERN_ONLY",
            [
                "q79/S3 supplies the working finite pattern: flat class, F_3^2 table, central cocycle.",
            ],
            [
                "No same-branch selector gives a Z3 quotient for Qa/SU3.",
                "Direct import from q79/S3 would mix branches.",
            ],
            "GUARDRAIL_ONLY",
        ),
        map_row(
            "bianchi_alpha1_support_to_c_twist",
            "INSUFFICIENT",
            [
                "Iwasawa Bianchi support gives a concrete invariant-sector source row.",
            ],
            [
                "Bianchi support controls dH/four-form anomaly, not the finite DD/twist class by itself.",
                "No map from alpha1 support to the central c-twist quotient is stated.",
            ],
            "OPEN_NOT_PROMOTABLE",
        ),
        map_row(
            "source_certified_A01_DE_operator_exit",
            "LIVE_PARALLEL_FALLBACK",
            [
                "Avoids promoting an uncomputed gerbe class.",
                "Can use selected operator data directly if the gerbe-to-c map remains missing.",
            ],
            [
                "Requires selected A01/D_E matrices and one spectral/heat/rho_E exit.",
            ],
            "RUN_IN_PARALLEL",
        ),
    ]
    gate_results = {
        "strominger_source_family_selected": True,
        "global_gerbe_curvature_available": True,
        "same_branch_tau_to_c_twist_map_supplied": False,
        "same_branch_tau_to_c_twist_map_proved_nonzero": False,
        "same_branch_tau_to_c_twist_map_proved_zero": False,
        "gerbe_route_retired": False,
        "A01_DE_parallel_fallback_required": True,
        "closure_claimed": False,
    }
    candidate = {
        "candidate": "SelectedQaSU3StromingerSourceToCTwistMapOrNoGo",
        "status": "STROMINGER_SOURCE_TO_CTWIST_MAP_GATE_BUILT_MAP_OPEN_NO_GO_NOT_TRIGGERED",
        "input_status": prior["status"],
        "source_scans": scans,
        "required_c_twists": required_c_twists,
        "required_monad_map": required_monad_map,
        "candidate_maps": candidate_maps,
        "gate_results": gate_results,
        "decision": {
            "result": "No closure and no no-go yet.",
            "why": "The corpus gives a selected Strominger/Iwasawa gerbe family and integral Hhat/H data, but not the required pairing/slant/restriction from that differential-cohomology class to the Qa/SU3 central c-twist quotient.",
            "most_promising_next_move": "Compute a cover-independent slant/transgression map from Hhat or tau_QaSU3 against the Iwasawa base cycles to the central quotient, and test whether it yields generator 1.",
            "parallel_move": "Build A01/D_E operator exit so the program is not blocked by gerbe source selection.",
        },
        "next_required_artifact": "Selected_Qa_SU3_CTwist_Transgression_Pairing_Computation_v1",
        "parallel_fallback": "Selected_Qa_SU3_A01_DE_Operator_Exit_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3StromingerSourceToCTwistMapOrNoGo",
        "status": "QA_SU3_STROMINGER_SOURCE_TO_CTWIST_MAP_GATE_BUILT_MAP_OPEN_NO_GO_NOT_TRIGGERED",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "selected_strominger_iwasawa_source_family_identified": True,
            "candidate_maps_classified": True,
            "q79_finite_pattern_kept_as_guardrail_only": True,
            "gerbe_route_not_retired": True,
            "A01_DE_parallel_fallback_marked_required": True,
        },
        "what_remains_open": {
            "same_branch_tau_or_DD_class": True,
            "explicit_restriction_slant_or_transgression_to_c_twist": True,
            "nonzero_generator_pairing_for_c_plus_minus_one": True,
            "Freed_Witten_Bianchi_for_mapped_Qa_SU3_source": True,
            "twisted_section_bases_or_operator_exit": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "parallel_fallback": candidate["parallel_fallback"],
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
