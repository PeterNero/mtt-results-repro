"""Search for a same-branch Qa/SU3 Strominger/HYM source packet.

This search distinguishes three levels:

1. general Strominger/HYM existence and fixed-sector templates;
2. visible-sector source-packet analogues;
3. a same-branch Qa/SU3 compact Nil/Iwasawa color-bundle operator packet.

Only the third level can fill the Qa/SU3 determinant packet.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\proof_corpus")
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

FILL_ATTEMPT = CERTS / "selected_qa_su3_color_bundle_operator_packet_fill_attempt_certificate.json"

SOURCES = {
    "mtt_strominger_system": OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
    "heterotic_flux_selection": OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md",
    "heterotic_flux_compactifications": OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
    "core_bundle_realization": OBSIDIAN / "1 Core & Encodings" / "The_Modal_Triplet_Theory_Program_C__Realizing_the_Modal_Triplet_Core.md",
    "visible_operator_after_s3": Q79 / "Visible_Operator_Source_After_S3_Closure_v1.md",
    "visible_chern_weil_gate": Q79 / "Visible_Chern_Weil_Quantization_Gate_v1.md",
    "visible_operator_blocker": Q79 / "Visible_Operator_Source_Blocker_Resolution_v1.md",
    "z7_fuyau_mukai": Q79 / "Z7_FuYau_Mukai_Charge_Sector_Certificate_v1.md",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def scan(path: Path, terms: list[str]) -> dict[str, Any]:
    if not path.exists():
        return {"path": str(path), "present": False, "terms_found": [], "missing_terms": terms}
    text = path.read_text(encoding="utf-8", errors="ignore")
    found = [term for term in terms if term.lower() in text.lower()]
    return {
        "path": str(path),
        "present": True,
        "terms_found": found,
        "missing_terms": [term for term in terms if term not in found],
    }


def main() -> None:
    fill = load(FILL_ATTEMPT)

    source_checks = {
        "mtt_strominger_system": scan(
            SOURCES["mtt_strominger_system"],
            ["fixed topological sector", "HYM", "Bianchi", "positive Hessian", "endomorphism"],
        ),
        "heterotic_flux_selection": scan(
            SOURCES["heterotic_flux_selection"],
            ["Iwasawa", "Hermitian Yang", "Bianchi", "componentwise", "Fu"],
        ),
        "heterotic_flux_compactifications": scan(
            SOURCES["heterotic_flux_compactifications"],
            ["Lens", "Nil", "Iwasawa", "flux", "HYM"],
        ),
        "core_bundle_realization": scan(
            SOURCES["core_bundle_realization"],
            ["bundle", "connection", "principal", "gauge", "Nil"],
        ),
        "visible_operator_after_s3": scan(
            SOURCES["visible_operator_after_s3"],
            ["selected visible bundle", "Chern-Weil", "operator source", "Bianchi", "Freed-Witten"],
        ),
        "visible_chern_weil_gate": scan(
            SOURCES["visible_chern_weil_gate"],
            ["Chern-Weil", "selected visible integral", "bundle", "source-derived"],
        ),
        "visible_operator_blocker": scan(
            SOURCES["visible_operator_blocker"],
            ["IRREDUCIBLE_NEW_SELECTED_OPERATOR_SOURCE_REQUIRED", "selected visible SM bundle", "operator source"],
        ),
        "z7_fuyau_mukai": scan(
            SOURCES["z7_fuyau_mukai"],
            ["Fu-Yau", "Mukai", "HYM background bundle", "charge-sector", "not required"],
        ),
    }

    levels = [
        {
            "level": "general_strominger_hym_fixed_sector_template",
            "status": "FOUND_TEMPLATE",
            "meaning": (
                "The corpus supports fixed topological sectors, HYM/Bianchi equations, "
                "positive Hessian language, and invariant Iwasawa/Fu-Yau templates."
            ),
            "usable_for_qa_su3_determinant": False,
            "why_not": "It does not name the selected Qa/SU3 color bundle, Chern data, connection, or determinant finite part.",
        },
        {
            "level": "visible_sector_source_packet_analogue",
            "status": "FOUND_TEMPLATE",
            "meaning": (
                "The q79 visible branch has the right packet shape: selected source, "
                "Chern-Weil row, Bianchi/Freed-Witten checks, and operator-source gates."
            ),
            "usable_for_qa_su3_determinant": False,
            "why_not": "It is visible-sector data, not the Qa/SU3 compact Nil/Iwasawa color-threshold source.",
        },
        {
            "level": "same_branch_qa_su3_source_packet",
            "status": "NOT_FOUND",
            "meaning": "No current source names a selected Qa/SU3 compact Nil/Iwasawa color-bundle/sheaf/twist with operator data.",
            "usable_for_qa_su3_determinant": False,
            "why_not": "This is the required object and remains missing.",
        },
    ]

    constructive_spec = {
        "name": "selected_qa_su3_strominger_hym_source_packet",
        "required_fields": [
            "branch: compact Nil/Iwasawa Qa sector",
            "source certificate selecting the SU3 color bundle/sheaf/twist",
            "Chern/Mukai/gerbe data on that branch",
            "Bianchi or Freed-Witten/anomaly check on that branch",
            "connection or HYM/Strominger residual data",
            "operator domain compatible with p0 and p!=0 quotient rules",
            "endomorphism_E or equivalent heat-kernel zero-order block",
            "one finite-part computation: heat coefficients, spectrum, or torsion",
            "trace normalization and gauge quotient scheme",
        ],
        "minimal_next_computable_subpacket": [
            "Chern/Bianchi packet for a candidate SU3 source",
            "then Weitzenbock/Laplace-type endomorphism_E from that source",
        ],
    }

    output = {
        "certificate": "SelectedQaSU3StromingerHYMSourcePacketSearch",
        "status": "QA_SU3_STROMINGER_HYM_SOURCE_PACKET_SEARCH_DONE_SAME_BRANCH_SOURCE_NOT_FOUND",
        "input_status": {
            "operator_packet_fill_attempt": fill["status"],
        },
        "source_checks": source_checks,
        "levels": levels,
        "constructive_spec": constructive_spec,
        "search_result": {
            "general_strominger_hym_template_found": True,
            "visible_source_packet_template_found": True,
            "same_branch_qa_su3_source_packet_found": False,
            "selected_endomorphism_E_found": False,
            "determinant_computable_now": False,
            "qa_su3_closed": False,
            "full_sm_closure_achieved": False,
            "target_fitting_used": False,
        },
        "do_not_use": [
            "general Strominger/HYM existence as Qa/SU3 determinant closure",
            "visible Chern-Weil or S3 source packet as Qa/SU3 color source",
            "Z7 Fu-Yau/Mukai charge-sector certificate as selected Qa/SU3 bundle",
            "retired explicit HYM matrix entries",
            "target residual to decide the missing source packet",
        ],
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Chern_Bianchi_Source_Packet_Candidates_v1",
            "must_construct": [
                "candidate SU3 color source classes on compact Nil/Iwasawa",
                "Chern/Mukai/gerbe invariants for each candidate",
                "Bianchi/Freed-Witten admissibility checks",
                "selection rule independent of the Qa residual",
            ],
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
