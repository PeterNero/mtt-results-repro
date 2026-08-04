"""Attempt to fill the Qa/SU3 color-connection/torsion template from corpus data.

This is a source-data extraction, not a fit.  The script records which fields
can be filled from the heterotic/NCG/topology corpus and which fields remain
open before a determinant can be computed.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = (
    ROOT
    / "certificates"
    / "selected_qa_su3_color_connection_local_system_torsion.template.json"
)
INTERFACE_CERT = (
    ROOT
    / "certificates"
    / "selected_qa_su3_color_connection_local_system_torsion_interface_certificate.json"
)

CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
SOURCES = {
    "heterotic_selection": CORPUS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md",
    "heterotic_explicit": CORPUS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
    "ncg": CORPUS
    / "15 Discrete & Spectral & Operator Geometric Theories"
    / "Modal_Triplet_Theory__From_MTT_to_Noncommutative_Geometry_v3.md",
    "topology_tier1": CORPUS
    / "13 Standard Model & Topology-Only Constraints"
    / "Topology__Only_Constraints_in_Modal_Triplet_Theory.md",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def has(path: Path, terms: list[str]) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore").lower() if path.exists() else ""
    missing = [term for term in terms if term.lower() not in text]
    return {
        "path": str(path),
        "present": path.exists(),
        "terms_found": [term for term in terms if term not in missing],
        "missing_terms": missing,
    }


def main() -> None:
    template = load(TEMPLATE)
    interface = load(INTERFACE_CERT)

    source_checks = {
        "heterotic_selection": has(
            SOURCES["heterotic_selection"],
            [
                "left-invariant",
                "Hermitian Yang--Mills",
                "Tr}F",
                "R_{+}",
                "Iwasawa",
                "Lens",
            ],
        ),
        "heterotic_explicit_su3_bundle": has(
            SOURCES["heterotic_explicit"],
            [
                "rank",
                "SU(3) bundle",
                "HYM connection",
                "unique",
                "c_3(E)",
                "TrF_E\\wedge F_E=0",
            ],
        ),
        "ncg_sm_embedding": has(
            SOURCES["ncg"],
            ["inner fluctuations", "SU(3)_c", "finite connection", "spectral action"],
        ),
        "topology_color_constraints": has(
            SOURCES["topology_tier1"],
            ["[SU(3)]^2U(1)", "Dynkin index", "colored Weyl", "anomaly"],
        ),
    }

    partial_fill = {
        "branch": "selected_su3_color_connection_spectrum",
        "reference_scale_squared": template["selected_qa_su3_operator"][
            "reference_scale_squared"
        ],
        "geometry": {
            "internal_space": {
                "selected_candidates": [
                    "Iwasawa complex balanced SU(3)-structure branch",
                    "Lens x Nil balanced non-integrable SU(3)-structure branch",
                ],
                "fill_status": "PARTIAL_AMBIGUOUS_TWO_CORPUS_BRANCHES",
                "reason": (
                    "Both branches are source-supported. The Qa/SU3 compact-Nil "
                    "calculation previously used the compact Nil color fiber, while "
                    "the heterotic source supplies Iwasawa and Lens x Nil six-dimensional branches."
                ),
            },
            "metric_parameters": {
                "iwasawa": "r3^2 = 8(2*pi)^2 / (16/alpha_prime + 8/R^4), with R still a scale/modulus unless separately selected",
                "lens_nil": "ratio R1/R fixed by two anomaly equations for integer (f,h), overall scale not fixed at this order",
                "fill_status": "PARTIAL_RELATIONAL_NOT_ABSOLUTE",
            },
            "orientation_or_volume_normalization": "left-invariant frame normalization supplied; determinant reference normalization still open",
        },
        "color_bundle": {
            "gauge_group": "SU3",
            "representation": {
                "selected_candidate": "rank-3 SU(3) bundle E on Iwasawa / color fundamental or adjoint trace depending threshold field",
                "fill_status": "PARTIAL_REPRESENTATION_ROLE_OPEN",
                "reason": "The source has an SU(3) bundle E; the Qa threshold operator must still state whether it acts in fundamental color, adjoint gauge, or associated local system.",
            },
            "trace_normalization": {
                "source_values": [
                    "Tr(T^2)=1 for abelian flux generator",
                    "Dynkin index T(3) common factor in topology anomaly audit",
                ],
                "fill_status": "PARTIAL_THRESHOLD_TRACE_OPEN",
            },
            "bundle_or_local_system": {
                "selected_candidate": "indecomposable rank-3 SU(3) HYM bundle E on Iwasawa",
                "properties": {
                    "c1": 0,
                    "c2_net_statement": "c2(E)=0 / Tr F_E wedge F_E = 0 in invariant sector",
                    "c3": "6 a wedge b wedge c",
                    "connection": "unique HYM connection up to unitary gauge by Li-Yau, but not written as spectral operator data",
                },
                "fill_status": "PARTIAL_CONNECTION_EXISTS_SPECTRUM_OPEN",
            },
        },
        "connection": {
            "connection_type": "Hermitian-Yang-Mills / Chern connection on selected SU(3) bundle, with heterotic R_+ torsional background",
            "connection_data": {
                "available": [
                    "componentwise Bianchi/anomaly coefficients",
                    "left-invariant HYM existence/uniqueness",
                    "Tr F_E wedge F_E = 0 in invariant sector",
                ],
                "missing": [
                    "explicit connection one-forms for the Qa threshold operator",
                    "operator eigenvalues or heat coefficients",
                ],
            },
            "curvature_or_flux_data": {
                "iwasawa_abelian_flux": "u1=8(2*pi)^2, u2=u3=0 for the stated two-line embedding",
                "iwasawa_grav": "Tr_grav R_+^2 = 8*r3^2/(r1^2*r2^2) alpha1",
                "lens_nil_flux": "Tr F^2 = 2(2*pi)^2(f^2 beta1 + h^2 beta3)",
                "fill_status": "CURVATURE_FOR_ANOMALY_PRESENT_NOT_THRESHOLD_SPECTRUM",
            },
            "endomorphism_E": None,
        },
        "brst_domain": {
            "physical_quotient": "Qa/SU3 p=0 and p!=0 BRST quotient rules selected in earlier certificates",
            "zero_mode_rule": "harmonic zero modes excluded from threshold det prime",
            "ghost_rule": "local FP/BRST quotient already counted; may not be reused as extra",
            "boundary_conditions": "compact quotient / left-invariant sector; determinant boundary/domain for color connection still open",
        },
        "spectrum_modes": None,
        "analytic_torsion": None,
    }

    remaining_blockers = [
        "choose Iwasawa versus Lens x Nil versus compact Nil color-fiber branch for this Qa operator",
        "state whether the threshold operator acts in SU3 fundamental, adjoint, or associated local-system representation",
        "derive explicit selected connection/operator eigenvalues, heat coefficients, or analytic torsion finite parts",
        "fix determinant normalization/reference scale from source data rather than target residual",
        "prove compatibility between the six-dimensional heterotic branch and the prior compact-Nil Qa Hodge calculation",
    ]

    output = {
        "status": "QA_SU3_COLOR_CONNECTION_TEMPLATE_FILL_ATTEMPT_BLOCKED_SPECTRUM_OPEN",
        "input_template_status": template["status"],
        "interface_status": interface["status"],
        "source_checks": source_checks,
        "partial_fill": partial_fill,
        "remaining_blockers": remaining_blockers,
        "computed_numeric_response": None,
        "template_filled": False,
        "reason_template_not_written": (
            "The corpus supports a partial selected SU3/HYM connection candidate, "
            "but not the exact Qa threshold representation, spectrum, torsion, or "
            "determinant normalization. Writing the template as complete would overclaim."
        ),
        "next_required_artifact": "Selected_Qa_SU3_HYM_Color_Connection_Spectrum_or_Torsion_Computation_v1",
        "verdict": {
            "source_selected_color_connection_candidate_found": True,
            "selected_numeric_determinant_available": False,
            "can_close_Qa_SU3_now": False,
            "target_fitting_used": False,
            "full_SM_closure_achieved": False,
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
