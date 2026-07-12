"""Extract or refute selected Qa/SU3 local-system torsion data.

This is the executable follow-up to the route decision:

* try to find a source-selected Nil/Iwasawa lattice character or local system,
* carry forward already selected BRST/zero-mode rules,
* refuse to choose a character from the Qa residual.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
Q79 = ROOT.parent / "mtt-q79-proof-repro"

DECISION = CERTS / "selected_qa_su3_endomorphism_or_local_system_torsion_decision_certificate.json"
TEMPLATE = CERTS / "selected_qa_su3_color_connection_local_system_torsion.template.json"
PNONZERO = CERTS / "selected_qa_su3_pnonzero_physical_quotient_determinant_certificate.json"
P0 = CERTS / "selected_qa_su3_p0_ghost_measure_normalization_certificate.json"
SPECTRUM = CERTS / "sourced_compact_nil_scalar_spectrum_certificate.json"
SCALAR_ZETA = CERTS / "compact_nil_scalar_hurwitz_zeta_candidate_certificate.json"
CHARACTER_RHO = CERTS / "selected_character_channel_covariance_closure_certificate.json"

SOURCES = {
    "nil_origin": CORPUS
    / "1 Core & Encodings"
    / "The_Modal_Triplet_Theory_Program_B0__Why_Description_Forces_Circle__Lens__and_Nil.md",
    "finite_projection": CORPUS
    / "5 Dirac Delta"
    / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md",
    "heterotic_flux": CORPUS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
    "topology": CORPUS
    / "13 Standard Model & Topology-Only Constraints"
    / "Topology__Only_Constraints_in_Modal_Triplet_Theory.md",
    "book": CORPUS
    / "10 The Book on Modal Triplet Theory"
    / "The_Book_on_Modal_Triplet_Theory_v9.md",
    "z64_cp": Q79
    / "proof_corpus"
    / "Twisted_Equivariant_Central_Circle_Z64_CP_Sector_Candidate_v1.md",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_hits(path: Path, terms: list[str]) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="ignore").lower() if path.exists() else ""
    found = [term for term in terms if term.lower() in text]
    return {
        "path": str(path),
        "present": path.exists(),
        "terms_found": found,
        "missing_terms": [term for term in terms if term not in found],
    }


def main() -> None:
    decision = load(DECISION)
    template = load(TEMPLATE)
    pnonzero = load(PNONZERO)
    p0 = load(P0)
    spectrum = load(SPECTRUM)
    scalar_zeta = load(SCALAR_ZETA)
    character_rho = load(CHARACTER_RHO)

    source_checks = {
        "nil_origin_holonomy_not_character": source_hits(
            SOURCES["nil_origin"],
            ["Nil", "holonomy", "circle", "shared", "lattice character", "local system"],
        ),
        "finite_projection_global_holonomy_not_selection": source_hits(
            SOURCES["finite_projection"],
            ["holonomy", "gauge quotienting", "spectral", "characteristic internal radius"],
        ),
        "compact_nil_spectrum_external_data": {
            "status": spectrum["status"],
            "external_source": spectrum["external_source"],
            "selected_geometry_map": spectrum["selected_geometry_map"],
        },
        "heterotic_flux_branch": source_hits(
            SOURCES["heterotic_flux"],
            ["Iwasawa", "Lens", "Nil", "HYM connection", "left-invariant", "TrF"],
        ),
        "topology_color_weights": source_hits(
            SOURCES["topology"],
            ["Dynkin index", "colored Weyl", "[SU(3)]^2U(1)", "Chern connection"],
        ),
        "z64_character_branch": source_hits(
            SOURCES["z64_cp"],
            ["q64", "character", "15", "CP", "selected"],
        ),
        "book_character_language": source_hits(
            SOURCES["book"],
            ["inequivalent character sectors", "family", "character", "holonomy"],
        ),
    }

    candidates = [
        {
            "candidate": "trivial_unit_local_system",
            "source_status": "AVAILABLE_AS_DEFAULT_ONLY",
            "selected_for_Qa_SU3_torsion": False,
            "reason": (
                "The trivial character is a conventionally available flat local system, "
                "but it is not a source-selected nontrivial Qa/SU3 torsion character. "
                "It also reintroduces ordinary zero-mode/cohomology issues rather than "
                "the selected p!=0 acyclic sector."
            ),
        },
        {
            "candidate": "compact_nil_p_nonzero_central_momentum_tower",
            "source_status": "STRUCTURAL_TOWER_SELECTED_NOT_SINGLE_CHARACTER",
            "selected_for_Qa_SU3_torsion": False,
            "known_data": {
                "integer_ranges": spectrum["spectrum_formula"]["integer_ranges"],
                "selected_mtt_form": spectrum["spectrum_formula"]["selected_mtt_form"],
                "acyclic": pnonzero["selected_rule"]["nonzero_central_hodge_complex_acyclic"],
            },
            "reason": (
                "The p!=0 central-momentum tower is selected for the compact Nil Hodge "
                "determinant and gives acyclicity, but it is a summed oscillator sector, "
                "not an upstream-selected flat local-system character with torsion weights."
            ),
        },
        {
            "candidate": "z64_q64_15_character_channel",
            "source_status": "SELECTED_FOR_RHO_UV_CP_BRANCH_NOT_QA_SU3_LOCAL_SYSTEM",
            "selected_for_Qa_SU3_torsion": False,
            "known_data": {
                "selected_character": character_rho["closed_on_branch"][
                    "selected_character"
                ],
                "rho_uv_status": character_rho["status"],
            },
            "reason": (
                "The q64=15 character is selected in the rho_UV/CP channel.  The current "
                "corpus does not identify that character with a Qa/SU3 compact-Nil local "
                "system or its Ray-Singer/Reidemeister torsion; a bridge theorem is missing."
            ),
        },
        {
            "candidate": "su3_fundamental_or_adjoint_color_holonomy",
            "source_status": "REPRESENTATION_LANGUAGE_PRESENT_CHARACTER_ABSENT",
            "selected_for_Qa_SU3_torsion": False,
            "reason": (
                "Color representations and Dynkin-index language are present, but the "
                "lattice homomorphism pi_1(Nil/Iwasawa)->SU3 or U(1) and torsion finite "
                "part are not selected."
            ),
        },
        {
            "candidate": "heterotic_lens_nil_flux_integers",
            "source_status": "FLUX_INTEGERS_PRESENT_NOT_LOCAL_SYSTEM_CHARACTER",
            "selected_for_Qa_SU3_torsion": False,
            "reason": (
                "Lens x Nil flux integers constrain the heterotic Bianchi/anomaly branch. "
                "They are not a selected compact-Nil Qa/SU3 local-system character, and "
                "using them would still require a branch-compatibility theorem."
            ),
        },
    ]

    selected_candidates = [item for item in candidates if item["selected_for_Qa_SU3_torsion"]]
    brst_payload = {
        "p0_zero_mode_rule": p0["selected_p0_measure_rule"],
        "pnonzero_physical_rule": pnonzero["selected_rule"],
        "scalar_zeta_status": scalar_zeta["status"],
        "scalar_zeta_central_value": scalar_zeta["central_window_result"][
            "total_scalar_finite_logdet_candidate"
        ],
        "pnonzero_selected_response": pnonzero["finite_parts"][
            "selected_pnonzero_physical_quotient_response"
        ],
    }

    output = {
        "certificate": "SelectedQaSU3LocalSystemTorsionSourceExtraction",
        "status": "QA_SU3_LOCAL_SYSTEM_TORSION_SOURCE_EXTRACTION_UNDERDETERMINED",
        "input_status": {
            "route_decision": decision["status"],
            "template": template["status"],
            "p0_rule": p0["status"],
            "pnonzero_rule": pnonzero["status"],
            "compact_nil_spectrum": spectrum["status"],
            "scalar_zeta_candidate": scalar_zeta["status"],
        },
        "source_checks": source_checks,
        "candidate_extraction": candidates,
        "selected_candidates_count": len(selected_candidates),
        "carried_forward_selected_data": brst_payload,
        "blocked_formula": {
            "ray_singer_log_torsion_response": (
                "1/2 * sum_q (-1)^q * q * weight_q * zeta_derivative_at_zero_q"
            ),
            "missing_terms": [
                "selected lattice/local-system character",
                "degree-wise torsion zeta derivatives for that character",
                "representation/color trace weights for Qa/SU3",
                "proof that the selected character is not imported from the target residual",
            ],
            "can_evaluate_now": False,
        },
        "negative_result": {
            "statement": (
                "Under the current corpus, the acyclic local-system torsion route is "
                "not source-selected strongly enough to compute a no-knob Qa/SU3 "
                "correction."
            ),
            "not_a_mathematical_no_go": True,
            "meaning": (
                "Ray-Singer/Reidemeister torsion remains a legitimate future route, "
                "but it requires a new source-certified character/local-system "
                "selection theorem or an external mathematical torsion computation "
                "with an upstream MTT character selection."
            ),
        },
        "next_routes": [
            {
                "rank": 1,
                "route": "prove_or_import_selected_nil_local_system_character_theorem",
                "status": "BEST_IF_SOURCE_CAN_BE_FOUND",
                "test": (
                    "Search or derive a theorem selecting a nontrivial character of the "
                    "compact Nil/Iwasawa lattice from MTT data before Qa comparison."
                ),
            },
            {
                "rank": 2,
                "route": "source_certified_endomorphism_E_full_operator",
                "status": "PARALLEL_REOPEN_ONLY_WITH_NEW_SOURCE",
                "test": (
                    "Construct a full threshold operator/endomorphism_E not inherited "
                    "from the retired HYM matrix route."
                ),
            },
            {
                "rank": 3,
                "route": "global_section_or_fundamental_domain_measure",
                "status": "SECONDARY_OPEN",
                "test": (
                    "Prove a global quotient measure distinct from the already counted "
                    "local FP/BRST quotient."
                ),
            },
        ],
        "do_not_use": [
            "observed Qa/SU3 residual to choose a lattice character",
            "q64=15 CP/rho_UV character as a Qa/SU3 local system without a bridge theorem",
            "compact Nil scalar zeta finite part as analytic torsion",
            "trivial local system as a nontrivial acyclic torsion correction",
            "local FP/BRST quotient as an extra torsion factor",
        ],
        "verdict": {
            "qa_su3_closed": False,
            "full_sm_closure_achieved": False,
            "target_fitting_used": False,
            "local_system_character_selected": False,
            "ray_singer_torsion_computable_now": False,
            "torsion_route_retired": False,
            "torsion_route_underdetermined_under_current_corpus": True,
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
