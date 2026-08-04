"""Decide the next Qa/SU3 route after the rank-one local-system no-go.

The previous theorem blocks q64=15 as an ordinary rank-one compact-Nil
character and as a scalar SU3 center element.  This script evaluates the two
remaining serious routes:

1. a nonabelian/projective clock-shift carrier for the order-64 phase;
2. a source-certified Qa/SU3 endomorphism_E or full threshold operator.

The projective route is mathematically real, but it is not automatically a
Qa/SU3 threshold determinant.  The selected route therefore becomes a source
hunt for the actual endomorphism/operator, with the projective carrier retained
only as a conditional auxiliary branch.
"""

from __future__ import annotations

import json
from math import gcd
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_CORPUS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\proof_corpus")

CENTRAL_NO_GO = CERTS / "selected_qa_su3_central_character_homomorphism_theorem_certificate.json"
TORSION_DECISION = CERTS / "selected_qa_su3_endomorphism_or_local_system_torsion_decision_certificate.json"
ROUTE_RETIREMENT = CERTS / "selected_qa_su3_explicit_hym_route_retirement_certificate.json"

PROJECTIVE_SOURCES = {
    "z64_exact_branch": Q79_CORPUS / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md",
    "visible_twisted_chan_paton": Q79_CORPUS / "Visible_Twisted_Chan_Paton_Rescue_v1.md",
    "visible_twisted_d7_qutrit_selector": Q79_CORPUS / "Visible_Twisted_D7_Qutrit_Symmetry_Selector_v1.md",
    "visible_twisted_s3_finite_cp": Q79_CORPUS / "Visible_Twisted_S3_Finite_Chan_Paton_Cancellation_v1.md",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_terms(path: Path, terms: list[str]) -> dict[str, Any]:
    if not path.exists():
        return {
            "path": str(path),
            "present": False,
            "terms_found": [],
            "missing_terms": terms,
        }
    text = path.read_text(encoding="utf-8", errors="ignore")
    terms_found = [term for term in terms if term.lower() in text.lower()]
    return {
        "path": str(path),
        "present": True,
        "terms_found": terms_found,
        "missing_terms": [term for term in terms if term not in terms_found],
    }


def main() -> None:
    central = load(CENTRAL_NO_GO)
    torsion = load(TORSION_DECISION)
    retirement = load(ROUTE_RETIREMENT)

    q = 15
    n = 64
    phase_order = n // gcd(q, n)
    minimal_projective_dimension = phase_order

    clock_shift_model = {
        "mathematical_status": "EXISTS_AS_PROJECTIVE_NONABELIAN_CARRIER",
        "phase": "exp(2*pi*i*15/64)",
        "phase_order": phase_order,
        "minimal_irreducible_clock_shift_dimension": minimal_projective_dimension,
        "presentation": (
            "For omega=exp(2*pi*i/64), clock C and shift S on C^64 satisfy "
            "C S C^-1 S^-1 = omega I.  Replacing C by C^15 gives the selected "
            "central commutator phase omega^15."
        ),
        "determinant_consistency": (
            "As a U(64) commutator this has determinant (omega^15)^64=1, so "
            "there is no determinant obstruction inside the 64-dimensional "
            "projective carrier."
        ),
    }

    projective_source_checks = {
        "z64_exact_branch": source_terms(
            PROJECTIVE_SOURCES["z64_exact_branch"],
            ["Z64", "q_64=15", "primitive shift", "central-circle"],
        ),
        "visible_twisted_chan_paton": source_terms(
            PROJECTIVE_SOURCES["visible_twisted_chan_paton"],
            ["projective", "Chan-Paton", "qutrit", "twisted"],
        ),
        "visible_twisted_d7_qutrit_selector": source_terms(
            PROJECTIVE_SOURCES["visible_twisted_d7_qutrit_selector"],
            ["clock", "shift", "qutrit", "F_3"],
        ),
        "visible_twisted_s3_finite_cp": source_terms(
            PROJECTIVE_SOURCES["visible_twisted_s3_finite_cp"],
            ["qutrit", "projective", "Chan-Paton", "zeta_3"],
        ),
    }

    projective_route = {
        "route": "nonabelian_projective_clock_shift_representation",
        "decision": "KEEP_AS_CONDITIONAL_AUXILIARY_BRANCH_NOT_SELECTED_PROOF_SOURCE",
        "mathematical_carrier": clock_shift_model,
        "source_support": {
            "z64_exact_shift_support": "Present for central-circle/Z64 flavor-CP branch.",
            "visible_projective_support": (
                "Present in qutrit/F3^2 twisted Chan-Paton/D7 files, mostly order-3 "
                "visible-sector support rather than order-64 Qa/SU3 threshold data."
            ),
            "qa_su3_operator_support": "Missing.",
        },
        "why_not_selected_now": [
            "The order-64 carrier is naturally a 64-dimensional projective module, not a selected SU3 color-bundle determinant.",
            "Existing projective visible-sector sources are qutrit/F3^2/order-3 D7/Chan-Paton statements, not q64/U64 Qa/SU3 operator statements.",
            "The corpus does not prove that this projective module twists the selected Qa/SU3 BRST or HYM threshold complex.",
            "No degree-wise analytic torsion, Reidemeister torsion, or zeta finite part has been computed for the q64 projective Qa/SU3 complex.",
        ],
        "would_be_promoted_if": [
            "A selected gerbe/twisted-bundle source identifies the q64 projective carrier with the Qa/SU3 threshold complex.",
            "The induced operator domain is the same domain as the Qa/SU3 determinant being computed.",
            "The finite determinant/torsion contribution is computed without using the Qa/SU3 residual.",
        ],
    }

    endomorphism_route = {
        "route": "source_certified_endomorphism_E_full_operator",
        "decision": "PRIMARY_NEXT_QA_SU3_ROUTE",
        "why_primary": [
            "It targets the actual Qa/SU3 threshold operator rather than an auxiliary carrier.",
            "It avoids using a visible-sector qutrit projective source as a color-threshold proof.",
            "It is the route that could directly produce the missing local determinant finite part.",
        ],
        "current_status": "OPEN_SOURCE_MISSING",
        "known_blockers": [
            "The explicit printed HYM matrix route is retired as a proof source.",
            "The local-system rank-one torsion route is closed negative for q64 center.",
            "No current certificate supplies the selected endomorphism_E, spectrum, or heat coefficient table for Qa/SU3.",
        ],
    }

    global_measure_route = {
        "route": "global_section_or_fundamental_domain_measure",
        "decision": "SECONDARY_BACKUP_ONLY",
        "why_secondary": (
            "It may still exist, but it must prove it is not merely a relabeling of "
            "the already-selected FP/BRST quotient normalization."
        ),
    }

    output = {
        "certificate": "SelectedQaSU3ProjectiveClockShiftOrEndomorphismRouteDecision",
        "status": "QA_SU3_PROJECTIVE_CLOCK_SHIFT_OR_ENDOMORPHISM_DECISION_BUILT_ENDOMORPHISM_PRIMARY",
        "input_status": {
            "central_character_no_go": central["status"],
            "torsion_route_decision": torsion["status"],
            "explicit_hym_route_retirement": retirement["status"],
        },
        "selected_phase": {
            "q64": q,
            "modulus": n,
            "order": phase_order,
            "not_rank_one_nil_character": central["verdict"]["rank_one_u1_local_system_bridge_closed_negative"],
            "not_su3_scalar_center": central["verdict"]["su3_scalar_center_bridge_closed_negative"],
        },
        "route_decisions": [
            projective_route,
            endomorphism_route,
            global_measure_route,
        ],
        "projective_source_checks": projective_source_checks,
        "decision": {
            "selected_primary_route": "source_certified_endomorphism_E_full_operator",
            "conditional_auxiliary_route": "nonabelian_projective_clock_shift_representation",
            "secondary_backup_route": "global_section_or_fundamental_domain_measure",
            "qa_su3_closed": False,
            "full_sm_closure_achieved": False,
            "target_fitting_used": False,
        },
        "do_not_use": [
            "qutrit/F3^2 projective Chan-Paton results as q64/U64 Qa/SU3 closure",
            "U64 clock-shift determinant as SU3 threshold determinant without an operator-domain theorem",
            "projective carrier existence as analytic torsion finite part",
            "Qa/SU3 residual to choose a clock-shift dimension, power, or normalization",
            "retired explicit HYM matrix entries as selected endomorphism_E data",
        ],
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Endomorphism_Source_Hunt_After_Torsion_No_Go_v1",
            "must_find_or_prove": [
                "selected Qa/SU3 operator domain after p0 and p!=0 BRST quotient",
                "selected endomorphism_E or equivalent zero-order Weitzenbock block",
                "heat coefficient, spectrum, or torsion finite part in that domain",
                "normalization policy compatible with the already selected gauge quotient scheme",
            ],
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
