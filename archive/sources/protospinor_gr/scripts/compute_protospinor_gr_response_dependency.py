from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79_REPO = TEXPAPERS / "mtt-q79-proof-repro"
NONSM_REPO = TEXPAPERS / "mtt-nonsm-constants-no-knob"

SOURCE_FILES = {
    "protospinor_core": TEXPAPERS / "10 ProtoSpinor" / "_md" / "10 ProtoSpinor.md",
    "gr_from_mtt": TEXPAPERS
    / "11 General Relativity & Geometry"
    / "_md"
    / "Modal_Triplet_Theory__From_MTT_to_General_Relativity_v2.md",
    "gr_string_bridge": TEXPAPERS
    / "11 General Relativity & Geometry"
    / "_md"
    / "Why__GR_Falls_Out_of_String_Theory___A_Coherent_Admissibility_Shadow_Bridge_in_Modal_Triplet_Theory.md",
    "qg_uv_finite": TEXPAPERS
    / "12 Quantum Gravity"
    / "_md"
    / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md",
}

IMPORTED_CERTIFICATES = {
    "internal_rho_uv_radius": NONSM_REPO
    / "certificates"
    / "final_internal_rho_uv_selected_radius_theorem_certificate.json",
    "dimensionful_obstruction": NONSM_REPO
    / "certificates"
    / "dimensionful_constant_obstruction_certificate.json",
    "qa_su3_current_source_no_go": NONSM_REPO
    / "certificates"
    / "selected_qa_su3_repair_b_primitive_correction_no_go_certificate.json",
    "time_oriented_m1_deresponse": Q79_REPO
    / "certificates"
    / "time_oriented_m1_deresponse_target_certificate.json",
    "shared_knob_ledger": Q79_REPO
    / "certificates"
    / "shared_knob_cross_encoding_ledger_certificate.json",
    "c1_finite_response": Q79_REPO
    / "certificates"
    / "c1_finite_response_matrix_reduction_certificate.json",
}


@dataclass(frozen=True)
class SourceHit:
    source_id: str
    path: str
    patterns_found: dict[str, bool]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"missing": True, "path": str(path)}
    return json.loads(path.read_text(encoding="utf-8"))


def status_of(data: dict[str, Any]) -> str:
    if data.get("missing"):
        return "MISSING"
    return str(data.get("status") or data.get("certificate") or "STATUS_NOT_RECORDED")


def find_source_patterns() -> list[SourceHit]:
    patterns = {
        "proto_spinor_upstream": r"prior to spacetime|upstream of spacetime|downstream Lorentzian",
        "binary_loop_obstruction": r"pi_1\(SO\(3\)\)|Spin\(3\)|double cover|Z2",
        "time_as_response": r"time .*emergent|emergent ordering|arrow",
        "gravity_as_response": r"gravity .*response|curvature .*response|Einstein dynamics",
        "einstein_ir_limit": r"Einstein|Einstein-Hilbert|beta-function|infrared",
        "quantum_gravity_loop": r"loop|holonomy|BRST|UV finite|unitary quantum gravity",
    }
    hits: list[SourceHit] = []
    for source_id, path in SOURCE_FILES.items():
        text = read_text(path)
        found = {
            key: bool(re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL))
            for key, pattern in patterns.items()
        }
        hits.append(SourceHit(source_id, str(path), found))
    return hits


def bool_from_path(data: dict[str, Any], dotted_path: str, default: bool = False) -> bool:
    cur: Any = data
    for part in dotted_path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return default
        cur = cur[part]
    return bool(cur)


def build_dependency_certificate() -> dict[str, Any]:
    imported = {key: load_json(path) for key, path in IMPORTED_CERTIFICATES.items()}
    source_hits = find_source_patterns()

    topological_invariants = {
        "internal_orientation_dimension": 3,
        "pi1_SO3_order": 2,
        "minimal_spin_lift_cover_degree": 2,
        "pi1_SO2_is_finite_binary": False,
        "binary_loop_obstruction_closed": True,
        "interpretation": "In the selected 3D internal orientation sector, orientable loop closure has a Z2 obstruction, forcing the minimal Spin(3)=SU(2) double-cover lift.",
    }

    dependencies = [
        {
            "id": "proto_spinor_binary_loop_closure",
            "kind": "topological_numeric",
            "closed": True,
            "numerical_witness": {"pi1_SO3_order": 2, "cover_degree": 2},
            "depends_on": [],
        },
        {
            "id": "space_as_chart_response",
            "kind": "structural_response",
            "closed": False,
            "numerical_witness": None,
            "depends_on": ["proto_spinor_binary_loop_closure", "selected_response_chart_kernel"],
        },
        {
            "id": "time_as_ordering_response",
            "kind": "structural_response",
            "closed": False,
            "numerical_witness": None,
            "depends_on": ["finite_capacity_bookkeeping", "selected_retarded_order_kernel"],
        },
        {
            "id": "gravity_as_curvature_response",
            "kind": "response_operator",
            "closed": False,
            "numerical_witness": None,
            "depends_on": [
                "proto_spinor_binary_loop_closure",
                "space_as_chart_response",
                "time_as_ordering_response",
                "selected_internal_rho_uv_branch",
                "matter_gauge_stress_response",
                "selected_GR_Hessian_kernel",
            ],
        },
        {
            "id": "selected_internal_rho_uv_branch",
            "kind": "imported_closed_numeric",
            "closed": bool_from_path(imported["internal_rho_uv_radius"], "closed.selected_internal_rho_uv"),
            "numerical_witness": imported["internal_rho_uv_radius"].get("selected_values", {}),
            "depends_on": ["selected_character_channel_covariance", "horizontal_scale_law"],
        },
        {
            "id": "dimensionful_GR_normalization",
            "kind": "absolute_normalization",
            "closed": bool_from_path(
                imported["dimensionful_obstruction"],
                "verdict.absolute_dimensionful_predictions_closed",
            ),
            "numerical_witness": None,
            "depends_on": ["selected_absolute_normalization", "unit_dictionary_certificate"],
        },
        {
            "id": "finite_C1_response_matrices",
            "kind": "imported_open_response_data",
            "closed": False,
            "numerical_witness": None,
            "depends_on": ["primitive_zero_mode_contractions", "sector_dotD_operators"],
        },
        {
            "id": "selected_visible_source_packet",
            "kind": "imported_open_source_gate",
            "closed": not bool_from_path(
                imported["time_oriented_m1_deresponse"],
                "calculation_results.selected_source_still_absent",
                default=True,
            ),
            "numerical_witness": None,
            "depends_on": ["visible_bundle_or_twisted_gerbe_data", "projector_retention"],
        },
        {
            "id": "full_GR_numeric_closure",
            "kind": "theorem_target",
            "closed": False,
            "numerical_witness": None,
            "depends_on": [
                "gravity_as_curvature_response",
                "dimensionful_GR_normalization",
                "selected_visible_source_packet",
                "finite_C1_response_matrices",
            ],
        },
    ]

    closed_count = sum(1 for row in dependencies if row["closed"])
    total_count = len(dependencies)
    closure_ratio = closed_count / total_count

    corpus_alignment = {
        hit.source_id: hit.patterns_found for hit in source_hits
    }
    required_pattern_groups = {
        "proto_spinor": ["proto_spinor_upstream", "binary_loop_obstruction"],
        "response": ["time_as_response", "gravity_as_response"],
        "gr_limit": ["einstein_ir_limit"],
        "qg_loop": ["quantum_gravity_loop"],
    }
    alignment_scores = {}
    for group, keys in required_pattern_groups.items():
        numerator = sum(
            1
            for hit in source_hits
            for key in keys
            if hit.patterns_found.get(key)
        )
        denominator = len(source_hits) * len(keys)
        alignment_scores[group] = numerator / denominator

    return {
        "certificate": "ProtospinorGRResponseDependencyCertificate",
        "status": "PROTOSPINOR_LOOP_RESPONSE_LEDGER_BUILT_GR_NUMERIC_CLOSURE_OPEN",
        "purpose": "Use the two proof repos plus the protospinor/GR/QG corpus to audit whether MTT can claim that space, time, and GR are downstream responses.",
        "imported_repositories": {
            "q79_proof_repro": str(Q79_REPO),
            "nonsm_constants_no_knob": str(NONSM_REPO),
        },
        "source_files": {key: str(path) for key, path in SOURCE_FILES.items()},
        "source_pattern_hits": corpus_alignment,
        "topological_invariants": topological_invariants,
        "imported_certificate_statuses": {
            key: status_of(value) for key, value in imported.items()
        },
        "dependency_rows": dependencies,
        "closure_accounting": {
            "closed_dependency_rows": closed_count,
            "total_dependency_rows": total_count,
            "closure_ratio": closure_ratio,
            "full_GR_numeric_closure": False,
            "space_time_as_response_numerically_closed": False,
            "protospinor_loop_obstruction_closed": True,
        },
        "alignment_scores": alignment_scores,
        "guardrails": {
            "claims_full_GR_derivation": False,
            "claims_Newton_constant_prediction": False,
            "uses_observed_GR_constant_as_input": False,
            "treats_space_and_time_as_primitive": False,
            "allows_structural_alignment_to_count_as_numeric_closure": False,
        },
        "next_required_objects": [
            "Selected_GR_Hessian_Kernel_Certificate",
            "Selected_Retarded_Order_Kernel_Certificate",
            "Matter_Gauge_Stress_Response_Map_Certificate",
            "Absolute_GR_Normalization_Certificate",
            "Quantum_Gravity_Loop_to_GR_Response_Operator_Equivalence_Certificate",
        ],
        "verdict": {
            "what_is_achieved": "A reproducible dependency theorem scaffold: proto-spinor binary loop closure is numerically/topologically fixed, and the corpus supports the response-ordering narrative.",
            "what_is_not_yet_achieved": "A full numerical derivation of Einstein dynamics, Newton normalization, or spacetime metric response.",
            "correct_forward_path": "Construct the selected GR Hessian and retarded response kernels from the same branch data, then test whether their low-energy response gives the Einstein operator with the imported internal rho_UV data and no fitted GR constants.",
        },
    }


def main() -> None:
    cert = build_dependency_certificate()
    out = ROOT / "certificates" / "protospinor_gr_response_dependency_certificate.json"
    out.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(json.dumps({"wrote": str(out), "status": cert["status"]}, indent=2))


if __name__ == "__main__":
    main()
