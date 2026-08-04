"""Build a superset route map for the selected Qa/SU3 operator packet.

This is not a closure artifact.  It records the unconventional ways the
missing packet might be obtained while keeping the no-knob guardrails intact.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
GR = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof")

OUTPUT_CERT = CERTS / "selected_qa_su3_superset_source_route_map_certificate.json"
PREVIOUS = [
    CERTS / "selected_qa_su3_iwasawa_automorphy_cocycle_data_or_nogo_certificate.json",
    CERTS / "selected_qa_su3_monad_to_operator_packet_transfer_gate_certificate.json",
    CERTS / "selected_qa_su3_nonsplit_extension_source_construction_certificate.json",
]

SOURCES = {
    "flux_iwasawa": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
    "theta_nonabelian_overlaps": OBSIDIAN
    / "18 Theta-Closure & Execution Program"
    / "Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps.md",
    "theta_twistor_su3": OBSIDIAN
    / "18 Theta-Closure & Execution Program"
    / "Theta_Closure_in_Modal_Triplet_Theory_III__Twistor_Action_Matching_and_Independent_Normalization.md",
    "m_theory": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_M_theory.md",
    "qg_uv": OBSIDIAN
    / "12 Quantum Gravity"
    / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md",
    "q79_cross_repo": Q79 / "certificates" / "constants_gr_cross_repo_clues_certificate.json",
    "q79_visible_twisted_cp": Q79 / "proof_corpus" / "Visible_Twisted_Chan_Paton_Rescue_v1.md",
    "q79_visible_valpha_candidates": Q79
    / "proof_corpus"
    / "Visible_VAlpha_Chern_Bianchi_Source_Packet_Candidates_v1.md",
    "gr_dependency": GR / "certificates" / "gr_dependency_matrix_certificate.json",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def scan(path: Path, terms: dict[str, str]) -> dict[str, Any]:
    if not path.exists():
        return {"path": str(path), "present": False, "terms": {key: False for key in terms}}
    text = path.read_text(encoding="utf-8", errors="ignore")
    return {
        "path": str(path),
        "present": True,
        "terms": {key: term.lower() in text.lower() for key, term in terms.items()},
    }


def route(
    route_id: str,
    name: str,
    status: str,
    promise: list[str],
    blockers: list[str],
    closure_payload: list[str],
    guardrails: list[str],
    priority: int,
) -> dict[str, Any]:
    return {
        "id": route_id,
        "name": name,
        "status": status,
        "priority": priority,
        "promise": promise,
        "blockers": blockers,
        "minimal_closure_payload": closure_payload,
        "guardrails": guardrails,
    }


def main() -> None:
    prior = {p.name: load_json(p).get("status", "UNKNOWN") for p in PREVIOUS if p.exists()}
    scans = {
        "flux_iwasawa": scan(
            SOURCES["flux_iwasawa"],
            {
                "H3C": "H_3(\\mathbb{C})",
                "monad": "monad",
                "generic_maps": "generic holomorphic maps",
                "HYM": "Hermitian--Yang--Mills",
                "A01": "A}^{(0,1)",
                "c3_six": "c_3(E)=6",
                "factor_of_automorphy": "factor of automorphy",
                "transition": "transition",
            },
        ),
        "theta_twistor_su3": scan(
            SOURCES["theta_twistor_su3"],
            {
                "color_fiber": "color fiber",
                "color_harmonic": "color harmonic",
                "L2_norm": "L^2 norm",
                "SU3_overlap": "SU(3)",
            },
        ),
        "m_theory": scan(
            SOURCES["m_theory"],
            {
                "G2": "G_2",
                "SU3_structure": "SU(3)-structure",
                "torsion_classes": "torsion classes",
                "harmonic_2_forms": "harmonic 2",
                "flux": "G_4",
            },
        ),
        "qg_uv": scan(
            SOURCES["qg_uv"],
            {
                "harmonic_projector": "joint harmonic projector",
                "fiber_gap": "fibre spectral gap",
                "Bianchi": "Bianchi",
                "pushforward": "pushforward",
            },
        ),
        "q79_cross_repo": scan(
            SOURCES["q79_cross_repo"],
            {
                "visible_packet": "Qa_SU3_operator_packet_as_visible_V_alpha_packet",
                "source_packet_candidates": "source-packet candidates",
                "torsion": "analytic_or_reidemeister_torsion",
            },
        ),
        "q79_twisted_cp": scan(
            SOURCES["q79_visible_twisted_cp"],
            {
                "Chan_Paton": "Chan",
                "twisted": "twisted",
                "B_field": "B-field",
                "HYM": "HYM",
            },
        ),
    }

    routes = [
        route(
            "A_source_augmented_iwasawa_automorphy",
            "Construct the missing Iwasawa line-bundle automorphy and section ring",
            "PRIMARY_MATHEMATICAL_ROUTE_OPEN",
            [
                "It targets exactly the current blocker: charged section spaces, multiplication table, and f,g maps.",
                "It can feed the typed monad, Cech/Dolbeault, rho_E, and D_E exits from one source.",
            ],
            [
                "current source has H3(C) and Gamma but not generator actions or charge-to-factor maps",
                "flat character and literal constant routes are already rejected for nonzero charges",
            ],
            [
                "Gamma generator action on complex Iwasawa coordinates",
                "factor-of-automorphy a_q(gamma,z) for every required charge",
                "basis and dimension of the eleven required section spaces",
                "multiplication table F_i x G_i -> P",
                "specific f,g coefficients with g f = 0 and local-freeness/stability",
            ],
            [
                "do not use constant scalar entries for nonzero charges",
                "do not use flat characters as nonzero c1 line bundles",
                "do not choose sections from the Qa/SU3 residual",
            ],
            1,
        ),
        route(
            "B_projective_gerbe_chan_paton",
            "Promote q79 twisted/gerbe Chan-Paton data to a selected color packet",
            "UNCONVENTIONAL_PROMISING_IF_SAME_BRANCH_SELECTED",
            [
                "It naturally handles noncommuting/projective color data where ordinary rho_E tables fail.",
                "It may convert the q79 torsion/gerbe branch into a twisted SU3 determinant source.",
            ],
            [
                "must prove the twisted class is the same Qa/SU3 branch, not only visible V_alpha support",
                "must supply a twisted determinant/torsion formula accepted by the operator interface",
            ],
            [
                "Deligne/Cech gerbe or B-field representative with torsion label fixed independently",
                "twisted rank-3 Chan-Paton module or Azumaya/projective bundle",
                "Freed-Witten/Bianchi admissibility check",
                "twisted analytic/Reidemeister torsion or heat finite part",
            ],
            [
                "do not relabel auxiliary projective clock-shift carriers as the selected source",
                "do not ignore the twist in the determinant normalization",
            ],
            2,
        ),
        route(
            "C_direct_operator_galerkin_inverse",
            "Bypass explicit line sections by constructing D_E as a selected finite spectral problem",
            "COMPUTATIONAL_FALLBACK_OPEN",
            [
                "It uses the existing q79 Galerkin validator architecture and does not require closed-form theta sections first.",
                "It could compute heat/spectrum/torsion numerically from source boundary data.",
            ],
            [
                "still needs selected boundary/transition data or an amended source-certified A01 operator",
                "cannot fit boundary data to the target residual",
            ],
            [
                "selected D_E domain, Gram matrix, stiffness matrix, quotient projectors",
                "Riesz gap/error certificate",
                "heat/zeta/torsion finite part for the Qa/SU3 block",
            ],
            [
                "do not use unselected diagnostic A01 repairs",
                "do not accept a spectrum without source-certified operator data",
            ],
            3,
        ),
        route(
            "D_theta_color_harmonic_normalization",
            "Use Theta color-harmonic normalization as a representation/trace selector",
            "AUXILIARY_SELECTOR_NOT_OPERATOR_SOURCE",
            [
                "It may decide whether the determinant acts on E, End(E), ad_SU3, or a local-system sector.",
                "It can normalize the color harmonic without importing observed coupling values.",
            ],
            [
                "color harmonic normalization is not a bundle transition packet",
                "does not compute endomorphism_E or determinant finite part by itself",
            ],
            [
                "proof identifying the Theta color harmonic with one allowed representation",
                "trace normalization and physical quotient scheme",
            ],
            [
                "do not treat overlap normalization as a selected source",
                "do not use it to tune the missing determinant",
            ],
            4,
        ),
        route(
            "E_m_theory_g2_superset_pushdown",
            "Lift to M-theory/G2 or SU3-structure data and push down the color packet",
            "HIGH_RISK_SUPERSET_ROUTE",
            [
                "It may select the SU3 bundle/twist through a higher-dimensional torsion/flux consistency condition.",
                "It could connect the same packet to GR/QG harmonic projector machinery.",
            ],
            [
                "current corpus gives compatibility, not explicit G2-to-Qa/SU3 bundle data",
                "dimensionful or physical anchor gaps cannot be used as hidden knobs",
            ],
            [
                "selected G2/SU3 torsion-flux class",
                "pushdown map to Iwasawa Qa/SU3 bundle or twisted module",
                "Bianchi/Ward compatibility and determinant finite part",
            ],
            [
                "do not use M-theory language as an existence substitute",
                "do not import physical constants to choose the branch",
            ],
            5,
        ),
        route(
            "F_source_certified_a01_erratum",
            "Amend the printed A01 source and derive the Chern/Laplace operator directly",
            "FASTEST_IF_AUTHOR_SOURCE_CAN_BE_CORRECTED",
            [
                "It would close the shortest transfer from corpus monad to endomorphism_E.",
                "It preserves the existing left-invariant calculation style.",
            ],
            [
                "requires a source-certified erratum, not only a diagnostic repair",
                "mu selection remains open unless fixed by the same source or branch rule",
            ],
            [
                "corrected integrable A01 matrix",
                "mu selection rule independent of target residual",
                "Chern connection curvature and zero-order heat block",
                "operator determinant/torsion finite part",
            ],
            [
                "do not promote the diagnostic repair without source amendment",
                "do not select mu by residual matching",
            ],
            6,
        ),
    ]

    output = {
        "certificate": "SelectedQaSU3SupersetSourceRouteMap",
        "status": "QA_SU3_SUPERSET_SOURCE_ROUTE_MAP_BUILT_PRIMARY_AUTOMORPHY_GERBE_GALERKIN",
        "purpose": "Identify unconventional but no-knob-respecting routes to the shared selected Qa/SU3 color/operator packet.",
        "input_status": prior,
        "source_scans": scans,
        "route_decision": {
            "primary": "A_source_augmented_iwasawa_automorphy",
            "secondary": "B_projective_gerbe_chan_paton",
            "computational_fallback": "C_direct_operator_galerkin_inverse",
            "auxiliary_selector": "D_theta_color_harmonic_normalization",
            "high_risk_superset": "E_m_theory_g2_superset_pushdown",
            "fast_if_source_amended": "F_source_certified_a01_erratum",
        },
        "routes": routes,
        "superset_principle": [
            "The packet may be selected in a larger MMT layer, but must descend to the same concrete fields required by the Qa/SU3 verifier.",
            "Equivalent encodings are allowed only if they output the same typed payload: source certificate, bundle/twist/module, representation, quotient, D_E or rho_E, and finite determinant/torsion.",
            "A route that only supplies topology, normalization, or color semantics is auxiliary until it produces operator data.",
        ],
        "minimal_next_experiment": {
            "name": "Selected_Qa_SU3_Source_Augmentation_Packet_for_Iwasawa_Monad_Maps_v1",
            "why": "It is the smallest payload that can turn the monad source into typed maps and then into either Cech/Dolbeault data, rho_E, or D_E.",
            "success_criterion": [
                "at least one nonzero pair F_i,G_i with computable product in P",
                "enough products to choose f,g with g f = 0 without target fitting",
                "local-freeness/stability source condition for the exact maps",
                "one operator exit: Cech/Dolbeault matrices, rho_E transitions, or D_E packet",
            ],
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
