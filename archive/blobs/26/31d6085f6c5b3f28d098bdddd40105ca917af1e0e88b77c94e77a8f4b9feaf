"""Build external clue synthesis for the U1/Y Route-C Phi_fin morphism.

External references are used only as design anchors for the finite-emission
container. They do not select MTT data, close Phi_fin, or provide target
observables.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
SM = TEXPAPERS / "mtt-sm-parity-closure"

INPUTS = {
    "pic0_residual_split": DATA / "selected_u1y_routec_operatorlayer_pic0_or_selected_residual_source_subpacket.candidate.json",
    "sm_source_origin_lemma": SM / "candidate_data" / "routec_selected_source_origin_lemma.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_phifin_external_clues.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_phifin_external_clues_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_PhiFin_External_Clues_v1.md"

STATUS = "U1Y_ROUTEC_PHIFIN_EXTERNAL_CLUES_BUILT_NO_PROOF_IMPORT"
NEXT = "Selected_U1Y_RouteC_FiniteEmissionMorphism_PhiFin_Subpacket_v1"

EXTERNAL_ANCHORS = [
    {
        "id": "wang_balanced_metrics_stable_bundles",
        "url": "https://www.researchwithrutgers.com/en/publications/canonical-metrics-on-stable-vector-bundles/",
        "role": "Balanced metrics on stable vector bundles converge to weak Hermitian-Einstein/HYM data; this suggests the finite Hermitian-matrix plus section-basis side of Phi_fin.",
        "container": "balanced_bergman_hym",
    },
    {
        "id": "douglas_karp_lukic_reinbacher_hym_fermat_quintic",
        "url": "https://arxiv.org/abs/hep-th/0606261",
        "role": "Numerical HYM construction on stable bundles uses Donaldson-style finite iteration; this suggests how selected HYM data could be emitted as finite matrices.",
        "container": "balanced_bergman_hym",
    },
    {
        "id": "arnold_falk_winther_feec_acta",
        "url": "https://sites.math.rutgers.edu/~falk/papers/acta.pdf",
        "role": "FEEC builds finite subcomplexes and commuting projections; this is the right template for preserving Cech/Deligne, Bianchi, and projective-module structure under projection.",
        "container": "commuting_galerkin_projection",
    },
    {
        "id": "osborn_galerkin_spectral_approximation",
        "url": "https://epubs.siam.org/doi/pdf/10.1137/0724082",
        "role": "Galerkin spectral approximation supplies the model for Riesz projectors, gap control, and finite eigenvalue/eigenvector error certificates.",
        "container": "spectral_gap_riesz_green",
    },
    {
        "id": "strominger_superstrings_with_torsion",
        "url": "https://doi.org/10.1016/0550-3213(86)90286-5",
        "role": "The original torsionful heterotic system frames the smooth source object: metric, torsion, Yang-Mills field, and dilaton are selected together.",
        "container": "smooth_strominger_source",
    },
    {
        "id": "fu_yau_non_kahler_flux_solution",
        "url": "https://arxiv.org/abs/hep-th/0604063",
        "role": "Fu-Yau style constructions support treating a non-Kahler Strominger solution as a legitimate smooth source before finite emission.",
        "container": "smooth_strominger_source",
    },
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    split = load(INPUTS["pic0_residual_split"])
    origin = load(INPUTS["sm_source_origin_lemma"])
    contract = origin["finite_emission_morphism_contract"]

    construction_pattern = [
        {
            "stage": "domain_lock",
            "map": "select M_* in the fixed q79/F,m=1 S3/GS Strominger/HYM sector",
            "must_prove": [
                "Pic0 is carried as a side condition rather than a selector",
                "S3 flat Deligne/Cech restriction and GS row are unchanged",
                "q79/F orientation and torsion label m=1 are preserved",
            ],
        },
        {
            "stage": "finite_basis",
            "map": "choose a source-selected holomorphic/Cech/Galerkin basis B_N from M_*",
            "must_prove": [
                "basis is emitted by the selected source, not by target columns",
                "basis respects Appell-Humbert or twisted Chan-Paton transition laws",
                "basis contains the Route-C finite validator slots as a trace",
            ],
        },
        {
            "stage": "projection_commuting_square",
            "map": "define P_N and prove P_N commutes with the typed differential/cocycle rows",
            "must_prove": [
                "Cech/Deligne restriction commutes with P_N",
                "Green-Schwarz/Bianchi row commutes with P_N",
                "projective-module twists and q79/F orientation commute with P_N",
            ],
        },
        {
            "stage": "finite_operator_payload",
            "map": "emit rho_E^N, h_N, sector projectors, D_E^N, dotD^N, K_N, Riesz_N, G_N, and primitive C1 tensors",
            "must_prove": [
                "D_E, dotD, Riesz/Green, and residual validators pass honestly",
                "rho_E and metric are selected by the same finite trace",
                "primitive C1 contractions are emitted or reduced to a named overlap theorem",
            ],
        },
        {
            "stage": "error_gap_certificate",
            "map": "certify residual_N <= epsilon_N and gap_N >= gamma_N > 0",
            "must_prove": [
                "finite truncation error is bounded by the selected Hessian/Riesz gap",
                "Riesz and Green objects are stable on the complement of the selected kernel",
                "selected_source_verified becomes theorem-derived, not lifted",
            ],
        },
    ]

    clue_evaluation = {
        "primary_template": "balanced_or_bergman_finite_hym_trace_plus_feec_style_commuting_projection",
        "why_primary": [
            "Balanced/Bergman HYM methods naturally emit finite section bases and Hermitian matrices.",
            "FEEC/Galerkin theory supplies the commuting-projection and gap-certificate discipline needed by Phi_fin.",
            "Strominger/Fu-Yau sources justify beginning from a smooth torsionful selected minimizer, but not importing operator values.",
        ],
        "fallback_template": "direct_routec_finite_basis_if_it_is_proved_to_be_the_galerkin_trace_of_M_star",
        "rejected_shortcuts": [
            "lifted selected_source_verified flags",
            "Route-C residual smoke treated as selected source",
            "observed masses, mixings, gauge constants, or benchmark columns",
            "Pic0-only quotient promoted to operator payload",
        ],
    }

    candidate = {
        "candidate": "SelectedU1YRouteCPhiFinExternalClues",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_status": split["status"],
        "local_contract": contract,
        "external_anchors": EXTERNAL_ANCHORS,
        "construction_pattern": construction_pattern,
        "clue_evaluation": clue_evaluation,
        "what_closes_now": {
            "external_clue_synthesis": True,
            "five_stage_phifin_construction_pattern": True,
            "proof_import_from_external_sources": False,
            "selected_operator_payload": False,
            "Phi_fin": False,
            "lambda_12": False,
        },
        "what_remains_open": {
            "actual_selected_basis_B_N": True,
            "projection_commuting_square_proof": True,
            "rho_E_metric_sector_projectors": True,
            "D_E_Riesz_Green_dotD": True,
            "primitive_C1_tensors": True,
            "finite_error_gap_certificate": True,
            "theorem_derived_selected_source_verified": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "external_sources_are_container_evidence_only": True,
            "claims_Phi_fin_closed": False,
            "claims_selected_operator_tables": False,
            "claims_lambda12": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "target_fitting_used": False,
        },
    }
    cert = {
        "certificate": "SelectedU1YRouteCPhiFinExternalClues",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "external_anchor_count": len(EXTERNAL_ANCHORS),
        "construction_stages": [stage["stage"] for stage in construction_pattern],
        "primary_template": clue_evaluation["primary_template"],
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "Phi_fin_closed": False,
        "lambda_12_closed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C PhiFin External Clues v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"Phi_fin_closed = {str(cert['Phi_fin_closed']).lower()}",
        f"lambda_12_closed = {str(cert['lambda_12_closed']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "External sources are container evidence only. They suggest how to build",
        "`Phi_fin`, but they do not select MTT data, close the operator payload,",
        "or provide benchmark values.",
        "",
        "## External Clues",
        "",
    ]
    for anchor in candidate["external_anchors"]:
        lines.append(f"- `{anchor['id']}` ({anchor['url']}): {anchor['role']}")
    lines.extend(
        [
            "",
            "## Recommended PhiFin Shape",
            "",
            "The strongest external clue is the hybrid:",
            "",
            "```text",
            "balanced/Bergman finite HYM trace",
            "+ FEEC/Galerkin commuting projection",
            "+ Riesz/gap/Green certificate",
            "```",
            "",
        ]
    )
    for stage in candidate["construction_pattern"]:
        lines.append(f"### {stage['stage']}")
        lines.append("")
        lines.append(f"`{stage['map']}`")
        lines.append("")
        for item in stage["must_prove"]:
            lines.append(f"- {item}")
        lines.append("")
    lines.extend(
        [
            "## Guardrails",
            "",
        ]
    )
    for shortcut in candidate["clue_evaluation"]["rejected_shortcuts"]:
        lines.append(f"- Reject: {shortcut}.")
    lines.extend(
        [
            "- Keep Pic0 as a side condition, not a standalone operator source.",
            "- Do not use observed masses, mixings, gauge constants, or benchmark matrices.",
            "",
            "## Next Artifact",
            "",
            "```text",
            candidate["next_required_artifact"],
            "```",
            "",
            "It must construct the actual selected finite trace and emit the operator",
            "payload, or prove a precise no-go for the current source record.",
            "",
            "## Certificate",
            "",
            "```json",
            json.dumps(cert, indent=2, sort_keys=True),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    candidate, cert, note = build()
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
