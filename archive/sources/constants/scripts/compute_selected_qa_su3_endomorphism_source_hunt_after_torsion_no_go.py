"""Source hunt for the selected Qa/SU3 endomorphism after torsion no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\proof_corpus")
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

ROUTE_DECISION = CERTS / "selected_qa_su3_projective_clock_shift_or_endomorphism_route_decision_certificate.json"
CENTRAL_NO_GO = CERTS / "selected_qa_su3_central_character_homomorphism_theorem_certificate.json"
RETIREMENT = CERTS / "selected_qa_su3_explicit_hym_route_retirement_certificate.json"

SOURCES = {
    "qa_alternative_source_hunt": ROOT / "proof_corpus" / "Selected_Qa_SU3_Alternative_Operator_or_Projector_Source_Hunt_v1.md",
    "visible_operator_source_blocker": Q79 / "Visible_Operator_Source_Blocker_Resolution_v1.md",
    "z7_fuyau_mukai_charge_sector": Q79 / "Z7_FuYau_Mukai_Charge_Sector_Certificate_v1.md",
    "visible_twisted_s3_source_packet": Q79 / "Visible_Twisted_S3_Source_Packet_Attempt_v1.md",
    "mtt_strominger_system": OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
    "heterotic_flux_compactifications": OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def check_terms(path: Path, terms: list[str]) -> dict[str, Any]:
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
    decision = load(ROUTE_DECISION)
    central = load(CENTRAL_NO_GO)
    retirement = load(RETIREMENT)

    source_checks = {
        "qa_alternative_source_hunt": check_terms(
            SOURCES["qa_alternative_source_hunt"],
            ["nontrivial SU3 color-bundle connection", "endomorphism", "global section", "analytic torsion"],
        ),
        "visible_operator_source_blocker": check_terms(
            SOURCES["visible_operator_source_blocker"],
            ["IRREDUCIBLE_NEW_SELECTED_OPERATOR_SOURCE_REQUIRED", "selected visible SM bundle", "Route C", "operator source"],
        ),
        "z7_fuyau_mukai_charge_sector": check_terms(
            SOURCES["z7_fuyau_mukai_charge_sector"],
            ["Fu-Yau", "HYM background bundle", "charge-sector", "not required"],
        ),
        "visible_twisted_s3_source_packet": check_terms(
            SOURCES["visible_twisted_s3_source_packet"],
            ["selected S3 source", "Freed-Witten", "finite HYM/Strominger twisted solve", "not yet constructed"],
        ),
        "mtt_strominger_system": check_terms(
            SOURCES["mtt_strominger_system"],
            ["Strominger", "HYM", "Bianchi", "fixed sector"],
        ),
        "heterotic_flux_compactifications": check_terms(
            SOURCES["heterotic_flux_compactifications"],
            ["Strominger", "Hermitian Yang-Mills", "Bianchi", "flux"],
        ),
    }

    candidate_routes = [
        {
            "route": "direct_selected_qa_su3_endomorphism_E",
            "status": "MISSING",
            "evidence": [
                "Prior Qa/SU3 source hunt names this as the best legal route.",
                "No current certificate supplies selected endomorphism_E, heat coefficients, spectrum, or determinant finite part.",
            ],
            "would_close_if": [
                "selected color-bundle connection is supplied",
                "zero-order Weitzenbock/endomorphism block is computed in the selected BRST quotient domain",
                "finite determinant contribution is computed before target comparison",
            ],
        },
        {
            "route": "visible_fuyau_strominger_template_transfer",
            "status": "TEMPLATE_ONLY_NOT_QA_SU3_SOURCE",
            "evidence": [
                "Visible source files show the same kind of frontier: a selected operator source is required.",
                "Z7 Fu-Yau/Mukai closes a charge-sector/topological quotient, not a Qa/SU3 threshold determinant.",
            ],
            "would_close_if": [
                "a same-branch theorem maps the Fu-Yau/Strominger HYM background to the Qa/SU3 operator domain",
                "selected D_E or equivalent color-threshold matrices are produced",
            ],
        },
        {
            "route": "projective_or_twisted_carrier_promoted_to_operator",
            "status": "CONDITIONAL_AUXILIARY",
            "evidence": [
                "The projective clock-shift carrier exists for the q64 phase.",
                "Existing qutrit/Chan-Paton sources remain visible-sector and order-3 in scope.",
            ],
            "would_close_if": [
                "selected q64 twisted-bundle/gerbe source acts on the Qa/SU3 determinant complex",
                "analytic torsion or determinant finite part is computed in that twisted complex",
            ],
        },
        {
            "route": "global_section_fundamental_domain_measure",
            "status": "BACKUP_OPEN",
            "evidence": [
                "It remains legal only if distinct from the already counted local FP/BRST quotient.",
            ],
            "would_close_if": [
                "a global measure factor is selected independently",
                "the factor is proven not to double-count local ghost/BRST normalization",
            ],
        },
    ]

    output = {
        "certificate": "SelectedQaSU3EndomorphismSourceHuntAfterTorsionNoGo",
        "status": "QA_SU3_ENDOMORPHISM_SOURCE_HUNT_AFTER_TORSION_NO_GO_BUILT_SOURCE_STILL_MISSING",
        "input_status": {
            "route_decision": decision["status"],
            "central_no_go": central["status"],
            "explicit_hym_route": retirement["status"],
        },
        "source_checks": source_checks,
        "candidate_routes": candidate_routes,
        "source_hunt_result": {
            "selected_endomorphism_E_found": False,
            "selected_qa_su3_operator_source_found": False,
            "visible_fuyau_template_found": True,
            "visible_template_legally_transfers_to_qa_su3": False,
            "qa_su3_closed": False,
            "full_sm_closure_achieved": False,
            "target_fitting_used": False,
        },
        "positive_takeaway": (
            "The visible Fu-Yau/Strominger corpus confirms the right shape of the missing object: "
            "a selected operator-source packet, not another correction factor.  The Qa/SU3 branch "
            "should now construct the analogous selected color-bundle/operator packet directly."
        ),
        "do_not_use": [
            "Z7 Fu-Yau/Mukai charge-sector closure as Qa/SU3 determinant closure",
            "visible SM operator-source templates as selected Qa/SU3 operator data",
            "retired HYM matrix entries as endomorphism_E",
            "projective q64 carrier existence as selected determinant finite part",
            "global-section measure without a no-double-count proof against FP/BRST",
        ],
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Color_Bundle_Operator_Packet_Interface_v1",
            "must_define": [
                "operator domain after selected p0 and p!=0 quotient",
                "bundle or sheaf carrying the color threshold source",
                "connection/curvature/HYM or Strominger residual data",
                "endomorphism_E or equivalent heat-kernel zero-order block",
                "spectrum, heat coefficient, or torsion finite part",
            ],
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
