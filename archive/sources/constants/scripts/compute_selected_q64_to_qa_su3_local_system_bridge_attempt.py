"""Attempt the q64=15 -> Qa/SU3 local-system character bridge.

The prior extraction found q64=15 selected in the rho_UV/CP branch, but not
selected as a Qa/SU3 local system.  This script tests the strongest bridge
that the current source record can support.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79 = ROOT.parent / "mtt-q79-proof-repro" / "proof_corpus"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

TORSION_EXTRACTION = (
    CERTS / "selected_qa_su3_local_system_torsion_source_extraction_certificate.json"
)
RHO_CHAR = CERTS / "selected_character_channel_covariance_closure_certificate.json"
NIL_SPECTRUM = CERTS / "sourced_compact_nil_scalar_spectrum_certificate.json"
PNONZERO = CERTS / "selected_qa_su3_pnonzero_physical_quotient_determinant_certificate.json"

SOURCES = {
    "z64_exact": Q79 / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md",
    "z64_cp": Q79 / "Twisted_Equivariant_Central_Circle_Z64_CP_Sector_Candidate_v1.md",
    "bounded_lag": Q79 / "Bounded_Retarded_Lag_Model_for_Dyadic_CKM_PreQuarter_v1.md",
    "arithmetic_descent": Q79 / "Arithmetic_Fixed_Sector_Descent_Theorem_for_Lens_Nil_Z7_CP_v1.md",
    "nil_origin": OBSIDIAN
    / "1 Core & Encodings"
    / "The_Modal_Triplet_Theory_Program_B0__Why_Description_Forces_Circle__Lens__and_Nil.md",
    "finite_projection": OBSIDIAN
    / "5 Dirac Delta"
    / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md",
    "heterotic_flux": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def has_all(path: Path, terms: list[str]) -> dict[str, Any]:
    body = text(path).lower()
    found = [term for term in terms if term.lower() in body]
    return {
        "path": str(path),
        "present": path.exists(),
        "terms_found": found,
        "missing_terms": [term for term in terms if term not in found],
    }


def main() -> None:
    torsion = load(TORSION_EXTRACTION)
    rho = load(RHO_CHAR)
    nil = load(NIL_SPECTRUM)
    pnonzero = load(PNONZERO)

    selected_character = rho["closed_on_branch"]["selected_character"]
    q64_closed = selected_character == "q_64=15"
    nil_central_acyclic = pnonzero["selected_rule"]["nonzero_central_hodge_complex_acyclic"]
    nil_has_selected_geometry = nil["selected_geometry_map"]["N"] == 79

    source_checks = {
        "z64_exact_selects_q64_15": has_all(
            SOURCES["z64_exact"],
            ["selected component", "q_64=15", "central-circle", "Z64"],
        ),
        "z64_cp_character_carrier": has_all(
            SOURCES["z64_cp"],
            ["central circle", "Wilson/deck", "character", "q_64"],
        ),
        "bounded_lag_selects_q64_15": has_all(
            SOURCES["bounded_lag"],
            ["0 < epsilon < 2", "q_64=15", "CRT(15,2)", "79"],
        ),
        "arithmetic_descent_lens_nil_character": has_all(
            SOURCES["arithmetic_descent"],
            ["Lens-Nil", "unitary CP character", "holonomy", "order 448"],
        ),
        "nil_origin_shared_circle": has_all(
            SOURCES["nil_origin"],
            ["shared", "circle", "Nil", "holonomy"],
        ),
        "finite_projection_holonomy": has_all(
            SOURCES["finite_projection"],
            ["holonomy", "gauge quotienting", "spectral", "central circle"],
        ),
        "heterotic_flux_lens_nil": has_all(
            SOURCES["heterotic_flux"],
            ["Lens", "Nil", "Iwasawa", "left-invariant", "flux"],
        ),
    }

    bridge_requirements = [
        {
            "id": "same_carrier_identification",
            "status": "PARTIAL",
            "test": "Z64 selected character and Qa/SU3 compact Nil both use central-circle language.",
            "evidence": [
                "q64=15 selected in central-circle CP carrier",
                "compact Nil p!=0 sector is central-momentum/central-circle structured",
            ],
            "missing": (
                "A theorem that the CP central-circle deck carrier acts as the same "
                "local-system character carrier on the Qa/SU3 compact Nil quotient."
            ),
        },
        {
            "id": "homomorphism_to_local_system",
            "status": "MISSING",
            "test": "Construct rho: pi_1(Nil/Iwasawa) -> U(1) or SU3 with rho(center)=exp(2*pi*i*15/64).",
            "evidence": [
                "q64=15 is a selected U(1)-phase character in the CP branch",
                "compact Nil has an integer central momentum tower",
            ],
            "missing": (
                "The corpus does not specify the lattice homomorphism, its kernel, "
                "or its compatibility with the compact Nil quotient."
            ),
        },
        {
            "id": "operator_domain_compatibility",
            "status": "MISSING",
            "test": "Show the q64 character twists the same Hilbert complex whose p!=0 BRST quotient was selected.",
            "evidence": [
                "p!=0 compact Nil Hodge complex is acyclic",
                "BRST p0/p!=0 rules are selected",
            ],
            "missing": (
                "No source states that the CP character projector E_15 twists the "
                "Qa/SU3 threshold complex, rather than only the flavor/CP carrier."
            ),
        },
        {
            "id": "torsion_finite_part",
            "status": "MISSING",
            "test": "Compute Ray-Singer/Reidemeister torsion for the selected character.",
            "evidence": [
                "scalar Nil spectrum has been imported",
                "scalar zeta diagnostic is stable but not torsion",
            ],
            "missing": (
                "Degree-wise zeta derivatives or Reidemeister torsion for the q64-twisted "
                "Qa/SU3 local system are absent."
            ),
        },
        {
            "id": "no_target_selection",
            "status": "PASS",
            "test": "Bridge must be chosen without using the Qa/SU3 residual.",
            "evidence": [
                "q64=15 was selected upstream by retarded-lag/CP branch criteria",
                "current computation does not use the required Qa residual",
            ],
            "missing": None,
        },
    ]

    missing = [row["id"] for row in bridge_requirements if row["status"] == "MISSING"]
    output = {
        "certificate": "SelectedQ64ToQaSU3LocalSystemBridgeAttempt",
        "status": "Q64_TO_QA_SU3_LOCAL_SYSTEM_BRIDGE_ATTEMPT_PARTIAL_NOT_CLOSED",
        "input_status": {
            "torsion_extraction": torsion["status"],
            "rho_character": rho["status"],
            "nil_spectrum": nil["status"],
            "pnonzero_rule": pnonzero["status"],
        },
        "selected_data": {
            "selected_character": selected_character,
            "q64_selected": q64_closed,
            "nil_has_selected_geometry_N79": nil_has_selected_geometry,
            "nil_pnonzero_acyclic": nil_central_acyclic,
            "candidate_character_value_if_bridge_existed": "center -> exp(2*pi*i*15/64)",
        },
        "source_checks": source_checks,
        "bridge_requirements": bridge_requirements,
        "missing_bridge_requirements": missing,
        "bridge_candidate": {
            "statement": (
                "The strongest legal candidate is to map the compact Nil central "
                "generator to the selected CP deck character exp(2*pi*i*15/64)."
            ),
            "status": "CANDIDATE_ONLY",
            "why_not_closed": (
                "The source record supplies shared central-circle language but not "
                "the required pi_1-to-character homomorphism, operator-domain "
                "compatibility, or torsion finite part."
            ),
        },
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Central_Character_Homomorphism_Theorem_v1",
            "must_prove": [
                "identify the compact Nil/Iwasawa lattice central generator used by Qa/SU3",
                "define the selected character rho(center)=exp(2*pi*i*15/64) from upstream MTT data",
                "prove E_15 twists the Qa/SU3 threshold complex, not only CP/flavor space",
                "compute or import the degree-wise torsion finite part",
            ],
        },
        "do_not_use": [
            "q64=15 as Qa/SU3 torsion by name similarity alone",
            "compact Nil p!=0 tower as a single finite deck character",
            "scalar Hurwitz-zeta determinant as Ray-Singer torsion",
            "Qa/SU3 residual to decide the homomorphism",
        ],
        "verdict": {
            "bridge_closed": False,
            "qa_su3_closed": False,
            "full_sm_closure_achieved": False,
            "target_fitting_used": False,
            "q64_to_nil_character_candidate_identified": True,
            "homomorphism_theorem_missing": True,
            "torsion_route_advanced": True,
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
