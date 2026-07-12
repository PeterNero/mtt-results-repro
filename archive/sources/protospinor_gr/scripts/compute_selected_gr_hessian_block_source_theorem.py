from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79_REPO = TEXPAPERS / "mtt-q79-proof-repro"
NONSM_REPO = TEXPAPERS / "mtt-nonsm-constants-no-knob"

CANDIDATE_CERT = ROOT / "certificates" / "selected_gr_hessian_kernel_candidate_certificate.json"
DEP_MATRIX_CERT = ROOT / "certificates" / "gr_dependency_matrix_certificate.json"

SOURCES = {
    "proto_world_in_world": TEXPAPERS / "10 ProtoSpinor" / "_work" / "World_in_World_Genesis__A_Proto_Geometric_Origin_of_Time__Gravity__Matter__and_Quantization_in_Modal_Triplet_Theory_v4" / "main.tex",
    "proto_action": TEXPAPERS / "10 ProtoSpinor" / "_work" / "Closure_Geometry_and_Unified_Dynamics__A_Ten_Dimensional_Action_for_Mass__Scalar_Relaxation__Quantization__and_Curvature_v3" / "main.tex",
    "proto_worldsheet": TEXPAPERS / "10 ProtoSpinor" / "_work" / "Proto_Spinor_Closure_and_Worldsheet_Encoding_in_Modal_Triplet_Theory_v3" / "main.tex",
    "gr_reduction": TEXPAPERS / "11 General Relativity & Geometry" / "_md" / "Modal_Triplet_Theory__From_MTT_to_General_Relativity_v2.md",
    "qg_uv": TEXPAPERS / "12 Quantum Gravity" / "_md" / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md",
    "qg_all": TEXPAPERS / "12 Quantum Gravity" / "_md" / "12 Quantum Gravity.md",
    "q79_z64": Q79_REPO / "proof_corpus" / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md",
    "nonsm_z64": NONSM_REPO / "proof_corpus" / "Damping_Hessian_Z64_Block_Identification_v1.md",
}

OUT_CERT = ROOT / "certificates" / "selected_gr_hessian_block_source_theorem_certificate.json"
OUT_TEMPLATE = ROOT / "candidate_data" / "selected_gr_hessian_block_source.template.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def has(pattern: str, text: str) -> bool:
    return bool(re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL))


def source_census() -> dict[str, dict[str, Any]]:
    patterns = {
        "anchor_hessian_symbolic": r"H_\{?(?:\\rm\s*)?(?:anchor|align)\}?|anchored Hessian|Anchored Quadratic Form",
        "closure_strain": r"closure strain|bookkeeping strain|curvature--strain|Closure--Curvature",
        "gr_projection": r"coherent-sector projection|observable projection|\\mathcal P|I\\!\\circ\\!\\Pi|I\\circ\\Pi",
        "einstein_hilbert": r"Einstein--Hilbert|G_\\?\\{?\\rm eff\\}?|G_eff|G_{\s*\\rm eff\s*}",
        "tt_lichnerowicz": r"TT Lichnerowicz|Lichnerowicz operator|transverse--traceless",
        "proper_time_gap": r"proper-time support gap|tau_0|Stieltjes|Bernstein",
        "retarded_kernel": r"retarded kernel|future cone|future-lightcone support",
        "explicit_numeric_matrix": r"\[\s*\[[-+0-9., eE]+\]\s*(?:,\s*\[[-+0-9., eE]+\]\s*)+\]",
        "z64_exact_hessian": r"Z64|Z_64|L_64|L_tower|K_ret,64",
        "gr_hanchor_to_tt_projection": r"\bP_GR\b|K_GR\s*=|P_GR\^T\s*H|H_(?:anchor|align)\s*(?:->|\\to|to)\s*TT",
    }
    census: dict[str, dict[str, Any]] = {}
    for source_id, path in SOURCES.items():
        text = read(path)
        census[source_id] = {
            "path": str(path),
            "exists": path.exists(),
            "hits": {name: has(pattern, text) for name, pattern in patterns.items()},
        }
    return census


def main() -> None:
    candidate = load_json(CANDIDATE_CERT)
    matrix = load_json(DEP_MATRIX_CERT)
    census = source_census()

    found_any_anchor = any(row["hits"]["anchor_hessian_symbolic"] for row in census.values())
    found_any_tt = any(row["hits"]["tt_lichnerowicz"] for row in census.values())
    found_any_proper_time = any(row["hits"]["proper_time_gap"] for row in census.values())
    found_any_retarded = any(row["hits"]["retarded_kernel"] for row in census.values())
    found_gr_projection = any(row["hits"]["gr_projection"] for row in census.values())
    found_numeric_matrix = any(row["hits"]["explicit_numeric_matrix"] for row in census.values())
    found_gr_projection_formula = any(row["hits"]["gr_hanchor_to_tt_projection"] for row in census.values())

    z64_sources = [
        source_id
        for source_id, row in census.items()
        if row["hits"]["z64_exact_hessian"]
    ]
    z64_is_gr_hessian_substitute = False

    theorem_rows = [
        {
            "object": "symbolic anchored closure Hessian",
            "status": "FOUND_STRUCTURAL",
            "source_basis": [sid for sid, row in census.items() if row["hits"]["anchor_hessian_symbolic"]],
            "closed_for_GR": False,
            "reason": "The corpus has anchored Hessian normal forms but not a numeric selected GR block.",
        },
        {
            "object": "TT/Lichnerowicz target block",
            "status": "FOUND_TARGET_OPERATOR",
            "source_basis": [sid for sid, row in census.items() if row["hits"]["tt_lichnerowicz"]],
            "closed_for_GR": True,
            "reason": "The QG corpus identifies the TT Lichnerowicz operator target.",
        },
        {
            "object": "proper-time/Stieltjes retarded kernel class",
            "status": "FOUND_STRUCTURAL_KERNEL_CLASS",
            "source_basis": [sid for sid, row in census.items() if row["hits"]["proper_time_gap"] or row["hits"]["retarded_kernel"]],
            "closed_for_GR": False,
            "reason": "The class and support theorem are present, but no selected finite measure for this GR block is provided.",
        },
        {
            "object": "H_anchor to TT projection P_GR",
            "status": "MISSING_SELECTED_MAP",
            "source_basis": [sid for sid, row in census.items() if row["hits"]["gr_hanchor_to_tt_projection"]],
            "closed_for_GR": False,
            "reason": "No explicit P_GR or equivalent selected derivative map from closure strain to TT metric perturbations was found.",
        },
        {
            "object": "exact Z64 Hessian/kernel",
            "status": "FOUND_NON_GR_EXACT_BLOCK",
            "source_basis": z64_sources,
            "closed_for_GR": z64_is_gr_hessian_substitute,
            "reason": "Z64 is an exact central-circle tower block. It is useful evidence for the method but not a GR TT Hessian block.",
        },
    ]

    template = {
        "certificate": "SelectedGRHessianBlockSourceDataTemplate",
        "status": "TEMPLATE_REQUIRED_TO_CLOSE_SELECTED_GR_HESSIAN_BLOCK",
        "basis": {
            "closure_basis_labels": [],
            "tt_basis_labels": [
                "h_TT_plus",
                "h_TT_cross"
            ],
            "gauge_basis_labels": [
                "diffeomorphism_0",
                "diffeomorphism_1",
                "diffeomorphism_2",
                "diffeomorphism_3"
            ],
        },
        "H_anchor": {
            "matrix": [],
            "symmetric": True,
            "positive_semidefinite_before_gauge_quotient": None,
            "source_certificate": None,
        },
        "P_GR": {
            "matrix": [],
            "maps_from": "closure_basis_labels",
            "maps_to": "tt_basis_labels plus gauge_basis_labels",
            "source_certificate": None,
        },
        "K_GR": {
            "formula": "P_GR^T H_anchor P_GR after BRST/diffeomorphism quotient",
            "matrix": [],
            "principal_symbol": "P_TT |k|_g^2 P_TT",
            "source_certificate": None,
        },
        "retarded_measure": {
            "type": "positive Stieltjes/proper-time measure",
            "support_lower_bound_tau0": None,
            "moments_or_atoms": [],
            "normalization": "F(0)=1",
            "source_certificate": None,
        },
        "stress_response_map": {
            "formula": "T_{mu nu}=-(2/sqrt(-g)) delta S_matter/delta g^{mu nu}",
            "selected_matter_gauge_inputs": [],
            "source_certificate": None,
        },
        "normalization": {
            "G_eff_inverse": "V_int/G_10",
            "absolute_G_eff_closed": False,
            "dimensionless_only_mode_allowed": True,
            "source_certificate": "dimensionful_constant_obstruction_certificate.json",
        },
    }
    OUT_TEMPLATE.write_text(json.dumps(template, indent=2), encoding="utf-8")

    closure_conditions = {
        "symbolic_anchor_found": found_any_anchor,
        "tt_target_found": found_any_tt,
        "proper_time_kernel_class_found": found_any_proper_time and found_any_retarded,
        "gr_projection_found": found_gr_projection,
        "numeric_h_anchor_matrix_found_anywhere": found_numeric_matrix,
        "selected_h_anchor_to_tt_projection_found": found_gr_projection_formula,
        "z64_exact_block_found": bool(z64_sources),
        "z64_allowed_as_gr_substitute": z64_is_gr_hessian_substitute,
    }

    selected_block_closed = (
        closure_conditions["tt_target_found"]
        and closure_conditions["proper_time_kernel_class_found"]
        and closure_conditions["numeric_h_anchor_matrix_found_anywhere"]
        and closure_conditions["selected_h_anchor_to_tt_projection_found"]
        and z64_is_gr_hessian_substitute
    )

    cert = {
        "certificate": "SelectedGRHessianBlockSourceTheorem",
        "status": "SELECTED_GR_HESSIAN_BLOCK_SOURCE_THEOREM_TARGET_CLOSED_SOURCE_OPEN",
        "purpose": "Determine whether the current corpus and two repos already supply the selected GR Hessian block source data.",
        "input_candidate_certificate": str(CANDIDATE_CERT),
        "dependency_matrix_certificate": str(DEP_MATRIX_CERT),
        "source_census": census,
        "theorem_rows": theorem_rows,
        "closure_conditions": closure_conditions,
        "selected_block_closed": selected_block_closed,
        "template_written": str(OUT_TEMPLATE),
        "numeric_conclusion": {
            "TT_target_components": candidate["target_kernel"]["physical_massless_spin2_polarizations"],
            "symmetric_tensor_components_4D": candidate["finite_numeric_checks"]["symmetric_tensor_component_count"],
            "full_GR_reachable_open_nodes": matrix["reachable_open_nodes"],
        },
        "verdict": {
            "what_is_closed": "The target TT/Lichnerowicz Einstein block and the proper-time/Stieltjes retarded-kernel class are identified.",
            "what_is_open": "The selected numeric closure Hessian matrix and its selected projection P_GR into the TT metric block are absent.",
            "why_z64_does_not_close_GR": "The exact Z64 block is a central-circle/tower Hessian-kernel block, not the spacetime TT Lichnerowicz block.",
            "next_action": "Fill candidate_data/selected_gr_hessian_block_source.template.json with source-certified H_anchor, P_GR, retarded measure, and stress map.",
        },
        "guardrails": {
            "claims_selected_GR_Hessian_closed": False,
            "uses_Z64_as_GR_Hessian": False,
            "uses_observed_GR_data": False,
            "claims_absolute_G_eff": False,
        },
    }
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(json.dumps({"wrote": str(OUT_CERT), "status": cert["status"], "template": str(OUT_TEMPLATE)}, indent=2))


if __name__ == "__main__":
    main()
