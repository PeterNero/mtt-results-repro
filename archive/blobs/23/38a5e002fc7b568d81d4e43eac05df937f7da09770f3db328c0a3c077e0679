"""Decide the next Qa/SU3 route after explicit HYM route retirement.

The point is not to close Qa/SU3 numerically.  It is to distinguish:

* the best physical source route if a selected endomorphism_E appears, and
* the best currently executable route that does not reuse the retired matrix.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

RETIREMENT = CERTS / "selected_qa_su3_explicit_hym_route_retirement_certificate.json"
TEMPLATE = CERTS / "selected_qa_su3_color_connection_local_system_torsion.template.json"
FILL = CERTS / "selected_qa_su3_color_connection_template_fill_attempt_certificate.json"
HYM = CERTS / "selected_qa_su3_hym_color_connection_spectrum_or_torsion_certificate.json"
NO_GO = CERTS / "selected_qa_su3_repair_b_primitive_correction_no_go_certificate.json"
SOURCE_HUNT = CERTS / "selected_qa_su3_alternative_operator_or_projector_source_hunt_certificate.json"

SOURCE_PATHS = {
    "superset_core": CORPUS
    / "3 Core Foundations"
    / "Modal_Triplet_Theory__MTT_as_a_Superset_v2.md",
    "finite_coherent_projection": CORPUS
    / "5 Dirac Delta"
    / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md",
    "heterotic_flux": CORPUS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
    "strominger_selection": CORPUS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
    "topology_constraints": CORPUS
    / "13 Standard Model & Topology-Only Constraints"
    / "Topology__Only_Constraints_in_Modal_Triplet_Theory.md",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_hits(path: Path, terms: list[str]) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="ignore").lower() if path.exists() else ""
    hits = [term for term in terms if term.lower() in text]
    return {
        "path": str(path),
        "present": path.exists(),
        "terms_found": hits,
        "missing_terms": [term for term in terms if term not in hits],
    }


def main() -> None:
    retirement = load(RETIREMENT)
    template = load(TEMPLATE)
    fill = load(FILL)
    hym = load(HYM)
    no_go = load(NO_GO)
    source_hunt = load(SOURCE_HUNT)

    op = template["selected_qa_su3_operator"]
    endomorphism_currently_available = (
        fill["partial_fill"]["connection"]["endomorphism_E"] is not None
        or op["connection"]["endomorphism_E"] is not None
    )
    retired_matrix_route = retirement["verdict"]["explicit_hym_matrix_route_currently_retired"]
    selected_spectrum_available = hym["verdict"]["selected_spectrum_or_torsion_available"]

    source_checks = {
        "torsion_local_system_language": source_hits(
            SOURCE_PATHS["superset_core"],
            ["torsion", "holonomy", "character", "local system"],
        ),
        "finite_projection_holonomy_language": source_hits(
            SOURCE_PATHS["finite_coherent_projection"],
            ["holonomy", "spectral", "gauge quotienting", "characteristic internal radius"],
        ),
        "heterotic_endomorphism_language": source_hits(
            SOURCE_PATHS["heterotic_flux"],
            ["HYM connection", "R_+", "Tr}F", "c_3(E)", "left-invariant"],
        ),
        "strominger_laplacian_language": source_hits(
            SOURCE_PATHS["strominger_selection"],
            ["torsionful Laplacians", "HYM bundles", "unique local minimizer", "spectral gaps"],
        ),
        "topology_trace_language": source_hits(
            SOURCE_PATHS["topology_constraints"],
            ["Dynkin index", "colored Weyl", "[SU(3)]^2U(1)", "Chern connection"],
        ),
    }

    routes = [
        {
            "route": "selected_endomorphism_E_or_color_threshold_operator",
            "rank_as_physical_source_if_filled": 1,
            "rank_as_current_executable_next_step": 2,
            "status": "PHYSICALLY_PRIMARY_BUT_SOURCE_BLOCKED",
            "reason": (
                "A selected SU3 color endomorphism or threshold operator would be a real new "
                "source, but the current template has endomorphism_E = null, the selected "
                "spectrum/torsion is unavailable, and the displayed HYM matrix route has "
                "been retired as a proof source."
            ),
            "next_allowed_action": (
                "Reopen only with a source-certified full operator/endomorphism not inherited "
                "from the retired printed matrix or A/B repairs."
            ),
        },
        {
            "route": "acyclic_local_system_torsion",
            "rank_as_physical_source_if_filled": 2,
            "rank_as_current_executable_next_step": 1,
            "status": "BEST_CURRENT_EXECUTABLE_ROUTE",
            "reason": (
                "The p!=0 Nil complex is already acyclic in the corpus audit chain, and "
                "analytic/Reidemeister torsion is the determinant invariant that does not "
                "require the retired explicit HYM matrix.  It still requires a selected "
                "lattice character/local system and color/BRST weights before computation."
            ),
            "next_allowed_action": (
                "Build a selected local-system torsion extraction attempt: enumerate allowed "
                "Nil lattice characters/holonomies from source data, reject target-fitted "
                "characters, and compute torsion only if the character is selected upstream."
            ),
        },
        {
            "route": "global_section_or_fundamental_domain_measure",
            "rank_as_physical_source_if_filled": 3,
            "rank_as_current_executable_next_step": 3,
            "status": "SECONDARY_OPEN",
            "reason": (
                "A global quotient measure could be separate from the local FP/BRST factor, "
                "but the current record does not yet select a global modular region or prove "
                "that it avoids double-counting."
            ),
            "next_allowed_action": (
                "Use only after a source-certified global section/fundamental-domain measure "
                "is shown to be distinct from the already counted local quotient."
            ),
        },
    ]

    output = {
        "certificate": "SelectedQaSU3EndomorphismOrLocalSystemTorsionDecision",
        "status": "QA_SU3_ENDOMORPHISM_OR_LOCAL_SYSTEM_TORSION_DECISION_BUILT_TORSION_PRIMARY",
        "input_status": {
            "explicit_hym_route_retirement": retirement["status"],
            "color_connection_template": fill["status"],
            "hym_spectrum_or_torsion": hym["status"],
            "repair_b_primitive_source_no_go": no_go["status"],
            "alternative_source_hunt": source_hunt["status"],
        },
        "source_checks": source_checks,
        "decision_tests": {
            "retired_matrix_route": retired_matrix_route,
            "endomorphism_E_currently_available": endomorphism_currently_available,
            "selected_spectrum_or_torsion_available": selected_spectrum_available,
            "template_branch_selected": op["branch"] is not None,
            "target_residual_may_select_route": False,
        },
        "route_decision": routes,
        "selected_next_artifact": {
            "name": "Selected_Qa_SU3_Local_System_Torsion_Source_Extraction_v1",
            "purpose": (
                "Try to source-select the local system/lattice character and torsion weights "
                "without using the Qa residual.  If no such selection exists, prove the "
                "torsion route is underdetermined under the current corpus."
            ),
            "must_compute_or_refute": [
                "selected Nil/Iwasawa compact quotient and lattice character",
                "representation/color trace weight",
                "BRST degree weights and zero-mode rule",
                "Ray-Singer/Reidemeister torsion finite part or proof of missing selection",
            ],
        },
        "do_not_use": [
            "retired printed HYM matrix or A/B repairs",
            "observed Qa/SU3 residual to choose a torsion character",
            "local FP/BRST determinant as an extra global factor",
            "soft gauge-tube width or regulator as physical threshold data",
        ],
        "verdict": {
            "qa_su3_closed": False,
            "full_sm_closure_achieved": False,
            "target_fitting_used": False,
            "endomorphism_route_currently_computable": False,
            "torsion_route_currently_computable": False,
            "torsion_route_selected_as_next_executable_test": True,
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
