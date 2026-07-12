from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
THETA = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\18 Theta-Closure & Execution Program\_md_v3_corrected")

UPSTREAM_CERT = ROOT / "certificates" / "selected_tt_domain_boundary_condition_theorem_certificate.json"
STROMINGER = (
    CORPUS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md"
)
M_THEORY = (
    CORPUS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_M_theory.md"
)
QG_I = (
    CORPUS
    / "12 Quantum Gravity"
    / "Constructive_MTT_Quantum_Gravity_I__Borel_Summability_of_the_SPT_Filtered_TT_Sector.md"
)
QG_II = (
    CORPUS
    / "12 Quantum Gravity"
    / "Constructive_MTT_Quantum_Gravity_II__BRST_Lifting__Gauge_Invariant_Observables__and_the_Physical_Hilbert_Space_under_SPT_Damping.md"
)
QG_ALIGNMENT = THETA / "Quantum_Gravity_Alignment_Evaluation_for_Z64_CKM_Closure_v1.md"
FLAVOR_QG_COMPAT = THETA / "Flavor_QG_Projector_Compatibility_Lemma_for_Z64_CKM_Closure_v1.md"
Z64_CERT = THETA / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md"
TWISTED_Z64 = THETA / "Twisted_Equivariant_Central_Circle_Z64_CP_Sector_Candidate_v1.md"

OUT_CERT = ROOT / "certificates" / "tt_domain_selection_from_fixed_point_or_internal_quotient_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "fixed_point_to_tt_domain_externalization.template.json"
OUT_NOTE = ROOT / "proof_corpus" / "TT_Domain_Selection_From_Fixed_Point_or_Internal_Quotient_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def main() -> None:
    upstream = load_json(UPSTREAM_CERT)
    strominger = read(STROMINGER)
    m_theory = read(M_THEORY)
    qg_i = read(QG_I)
    qg_ii = read(QG_II)
    qg_alignment = read(QG_ALIGNMENT)
    flavor_qg = read(FLAVOR_QG_COMPAT)
    z64_cert = read(Z64_CERT)
    twisted_z64 = read(TWISTED_Z64)

    source_tests = {
        "strominger_selects_unique_internal_fixed_point": (
            "unique coherent fixed point" in strominger
            and "Theorem 11" in strominger
            and "unique local minimizer" in strominger
        ),
        "strominger_fuyau_torus_bundle_source": (
            "Fu--Yau class" in strominger
            and "torus bundles over K3" in strominger
        ),
        "mtheory_fixed_point_topological_scales": (
            "modal gap scale(s) and topological integers" in m_theory
            and "coherent fixed point" in m_theory
        ),
        "mtheory_uses_bounded_geometry_fixed_point": (
            "M_{10}=Y^4\\times B_1\\times B_2\\times B_3" in m_theory
            and "bounded geometry" in m_theory
        ),
        "qg_external_domain_class_sourced": (
            "bounded domain" in qg_i
            and "Dirichlet or mixed" in qg_i
            and "BRST variations produce no boundary contributions" in qg_ii
        ),
        "qg_selects_external_TT_domain": False,
        "flavor_selects_finite_internal_quotient": (
            "Z64 exact central-circle branch certificate       CLOSED" in z64_cert
            and "finite quotient MTT actually needs" in twisted_z64
        ),
        "flavor_qg_projector_compatibility_present": (
            "Quantum_Gravity_Alignment" in qg_alignment
            or "QG" in flavor_qg
            or "quantum gravity" in flavor_qg.lower()
        ),
        "flavor_quotient_identified_with_TT_external_domain": False,
    }

    route_table = [
        {
            "route": "internal_flux_fixed_point",
            "closed": True,
            "selects": "compactification/fixed topological sector/internal geometry",
            "does_not_select": "external TT spatial topology, boundary condition, or length",
            "status": "usable_source_for_internal_data_not_yet_TT_domain",
        },
        {
            "route": "constructive_qg_external_domain",
            "closed": True,
            "selects": "admissible analytic class for TT construction",
            "does_not_select": "one unique domain inside the allowed class",
            "status": "class_sourced_selection_open",
        },
        {
            "route": "finite_flavor_quotient_Z64",
            "closed": source_tests["flavor_selects_finite_internal_quotient"],
            "selects": "finite internal/coherent character quotient for flavor/CP branch",
            "does_not_select": "external spacetime TT domain",
            "status": "strong_internal_clue_not_a_GR_TT_domain_substitute",
        },
        {
            "route": "fixed_point_to_TT_externalization_map",
            "closed": False,
            "selects": "would select external TT topology, boundary, metric scale, and Q-sector rule",
            "does_not_select": None,
            "status": "required_next_theorem",
        },
    ]

    packet = {
        "artifact": "Fixed_Point_to_TT_Domain_Externalization_Template",
        "purpose": "Fill this only with source-derived data, not with convenient benchmark spectra.",
        "required_fields": {
            "selected_fixed_point_id": None,
            "internal_geometry_or_quotient": None,
            "external_TT_domain_functor": None,
            "external_spatial_topology": None,
            "boundary_condition_inheritance_rule": None,
            "dimensionless_length_or_radius_normalization": None,
            "TT_operator": "projected linearized graviton/Lichnerowicz operator with SPT damping",
            "zero_mode_and_Q_sector_rule": None,
            "lowest_positive_eigenvalue": None,
            "proof_same_branch_as_GR_response_operator": None,
        },
        "disallowed_shortcuts": [
            "Do not identify Z64 or Z448 with the external TT domain.",
            "Do not promote flat periodic T3 to selected without the externalization map.",
            "Do not set L=2*pi by convention unless MTT selects that normalization.",
            "Do not use observed Newton/Planck input or phenomenological calibration.",
        ],
    }
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")

    note = """# TT Domain Selection From Fixed Point or Internal Quotient v1

## Result

The corpus now gives a sharp reduction:

```text
MTT fixed point selects internal compactification/topological data.
Constructive QG selects an admissible external analytic class.
The map from the selected fixed point to one external TT domain is still open.
```

This means the flat periodic `T3` spectrum, the Dirichlet box spectrum, and the
IR-box regulator remain models until an externalization theorem selects one of
them.

## What Is Closed

The flux/Strominger and M-theory papers strongly support fixed-point selection:
unique coherent fixed points, Fu-Yau torus-bundle examples, topological
integers, modal gap scales, and compactification data are selected internally.

The QG papers separately support the TT execution class: bounded geometry,
Dirichlet/mixed/support boundary behavior, and BRST-compatible no-boundary-term
conditions.

## What Is Not Closed

The finite flavor/CP quotients, including the exact Z64 central-circle branch,
are internal coherent quotients. They are important clues, but they are not yet
the external TT spatial domain.

## Next Gate

The next theorem must construct:

```text
Fixed_Point_to_TT_Domain_Externalization_Theorem
```

It has to supply a source-derived map from the selected fixed point/internal
quotient to:

- external TT spatial topology;
- inherited boundary condition;
- dimensionless length/radius normalization;
- zero-mode and Q-sector removal rule;
- proof that the resulting TT operator is on the same branch as the GR response
  operator.
"""
    OUT_NOTE.write_text(note, encoding="utf-8")

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "tt_domain_selection_from_fixed_point_or_internal_quotient",
        "status": "TT_DOMAIN_SELECTION_REDUCED_TO_FIXED_POINT_EXTERNALIZATION_MAP",
        "input_certificates": {
            "selected_tt_domain_boundary_condition_theorem": str(UPSTREAM_CERT),
        },
        "source_files": {
            "strominger_flux_system": str(STROMINGER),
            "m_theory_bridge": str(M_THEORY),
            "constructive_qg_i": str(QG_I),
            "constructive_qg_ii": str(QG_II),
            "qg_alignment": str(QG_ALIGNMENT),
            "flavor_qg_projector_compatibility": str(FLAVOR_QG_COMPAT),
            "z64_exact_branch": str(Z64_CERT),
            "twisted_z64_candidate": str(TWISTED_Z64),
        },
        "source_tests": source_tests,
        "route_table": route_table,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
        "closed_now": {
            "internal_fixed_point_selection_sourced": source_tests[
                "strominger_selects_unique_internal_fixed_point"
            ],
            "fu_yau_torus_bundle_internal_slice_sourced": source_tests[
                "strominger_fuyau_torus_bundle_source"
            ],
            "m_theory_topological_scale_dependence_sourced": source_tests[
                "mtheory_fixed_point_topological_scales"
            ],
            "external_TT_domain_class_sourced": source_tests["qg_external_domain_class_sourced"],
            "finite_internal_quotient_classified_as_internal_not_external": True,
        },
        "selection_result": {
            "selected_external_TT_domain_closed": False,
            "selected_external_boundary_closed": False,
            "selected_external_length_closed": False,
            "selected_TT_lambda_closed": False,
            "fixed_point_to_external_TT_map_closed": False,
            "reason": (
                "The fixed-point corpus selects internal compactification/coherent quotient data. "
                "The QG corpus supplies the external TT analytic class. A theorem identifying "
                "how the selected internal fixed point externalizes to a unique TT domain is not "
                "yet present in the sourced corpus."
            ),
        },
        "next_gate": {
            "name": "Fixed_Point_to_TT_Domain_Externalization_Theorem",
            "must_supply": [
                "a functor or construction from selected fixed-point data to external TT domain",
                "boundary-condition inheritance compatible with QG BRST no-boundary terms",
                "dimensionless length/radius normalization",
                "zero-mode and Q-sector projector rule",
                "proof of same-branch identity with the GR TT response operator",
                "then compute the lowest positive TT eigenvalue",
            ],
        },
        "guardrails": {
            "claims_periodic_T3_selected": False,
            "claims_dirichlet_box_selected": False,
            "claims_Z64_is_external_TT_domain": False,
            "claims_lambda_TT_numeric_selected": False,
            "claims_full_GR_response_closed": False,
        },
        "previous_status": upstream["status"],
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
