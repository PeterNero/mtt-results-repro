from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent

MINIMAL_CERT = ROOT / "certificates" / "minimal_cln_gr_hessian_candidate_certificate.json"
MINIMAL_DATA = ROOT / "candidate_data" / "minimal_cln_gr_hessian_candidate.json"
OUT_CERT = ROOT / "certificates" / "lens_shear_projection_source_search_certificate.json"

SOURCES = {
    "proto_spinor_main": TEXPAPERS / "10 ProtoSpinor" / "_md" / "10 ProtoSpinor.md",
    "world_in_world": TEXPAPERS / "10 ProtoSpinor" / "_work" / "World_in_World_Genesis__A_Proto_Geometric_Origin_of_Time__Gravity__Matter__and_Quantization_in_Modal_Triplet_Theory_v4" / "main.tex",
    "proto_spinor_triadic": TEXPAPERS / "10 ProtoSpinor" / "_work" / "The_Proto_Spinor__Triadic_Closure_from_Pointwise_Internal_Embedding_v4" / "main.tex",
    "proto_worldsheet": TEXPAPERS / "10 ProtoSpinor" / "_work" / "Proto_Spinor_Closure_and_Worldsheet_Encoding_in_Modal_Triplet_Theory_v3" / "main.tex",
    "gr_reduction": TEXPAPERS / "11 General Relativity & Geometry" / "_md" / "Modal_Triplet_Theory__From_MTT_to_General_Relativity_v2.md",
    "qg_uv": TEXPAPERS / "12 Quantum Gravity" / "_md" / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md",
    "qg_all": TEXPAPERS / "12 Quantum Gravity" / "_md" / "12 Quantum Gravity.md",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def has(text: str, pattern: str) -> bool:
    return bool(re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL))


def source_hits() -> dict[str, Any]:
    patterns = {
        "lens_transport_role": r"lens.*transport|transport.*lens|local transport|redundancy transport|lens curvature",
        "lens_shear_language": r"lens.*shear|shear.*lens",
        "metric_response_language": r"metric response|metric perturb|tetrad|Lorentzian chart|geometric response",
        "tt_sector": r"transverse--traceless|transverse-traceless|\bTT\b|Lichnerowicz",
        "plus_cross_polarizations": r"plus.*cross|cross.*plus|polarization",
        "direct_lens_to_tt_formula": r"lens.*(TT|transverse|traceless|graviton|metric perturb|polarization)|(?:TT|transverse|traceless|graviton|metric perturb|polarization).*lens",
        "explicit_projection_formula": r"P_GR|lens_shear_plus|lens_shear_cross|h_TT_plus|h_TT_cross|H_L.*TT|TT.*H_L",
    }
    result: dict[str, Any] = {}
    for source_id, path in SOURCES.items():
        text = read(path)
        result[source_id] = {
            "path": str(path),
            "exists": path.exists(),
            "hits": {name: has(text, pattern) for name, pattern in patterns.items()},
        }
    return result


def main() -> None:
    minimal_cert = load_json(MINIMAL_CERT)
    minimal_data = load_json(MINIMAL_DATA)
    hits = source_hits()

    direct_sources = [
        source_id
        for source_id, row in hits.items()
        if row["hits"]["direct_lens_to_tt_formula"] or row["hits"]["explicit_projection_formula"]
    ]
    indirect_lens_sources = [
        source_id
        for source_id, row in hits.items()
        if row["hits"]["lens_transport_role"]
    ]
    tt_sources = [
        source_id
        for source_id, row in hits.items()
        if row["hits"]["tt_sector"]
    ]
    metric_sources = [
        source_id
        for source_id, row in hits.items()
        if row["hits"]["metric_response_language"]
    ]

    direct_projection_closed = bool(direct_sources)
    relative_normalization_closed = False
    source_selection_closed = direct_projection_closed and relative_normalization_closed

    cert = {
        "certificate": "LensShearProjectionSourceSearchCertificate",
        "status": "LENS_SHEAR_PROJECTION_SOURCE_SEARCH_BLOCKED_DIRECT_SELECTION_MISSING",
        "purpose": "Test whether the formal CLN candidate can be promoted by corpus evidence identifying lens shear with the TT metric response directions.",
        "minimal_candidate_certificate": str(MINIMAL_CERT),
        "source_hits": hits,
        "evidence_summary": {
            "indirect_lens_transport_sources": indirect_lens_sources,
            "metric_response_sources": metric_sources,
            "tt_sector_sources": tt_sources,
            "direct_lens_to_TT_sources": direct_sources,
        },
        "promotion_tests": {
            "formal_candidate_passes_rank_test": minimal_cert["formal_result"]["candidate_matches_required_rank_pattern"],
            "direct_lens_to_TT_projection_found": direct_projection_closed,
            "relative_plus_cross_normalization_selected": relative_normalization_closed,
            "source_selection_closed": source_selection_closed,
        },
        "blocked_claim": {
            "claim": "lens_shear_plus/cross are the selected h_TT_plus/cross response directions",
            "blocked": not source_selection_closed,
            "reason": "The corpus supports lens as transport/compatibility data and TT as the physical graviton sector, but no source-certified projection P_GR or relative lens-shear normalization was found.",
        },
        "candidate_retained": {
            "retain_formal_candidate": True,
            "candidate_K_GR": minimal_data["K_GR"]["matrix"],
            "allowed_use": "rank-pattern witness and search guide",
            "forbidden_use": "selected GR Hessian theorem",
        },
        "next_gate": {
            "name": "Explicit_Lens_TT_Projection_or_Retire_Minimal_CLN",
            "close_by_one_of": [
                "find or prove an explicit source formula P_GR(lens_shear_plus,cross)=h_TT_plus,cross",
                "derive plus/cross lens shear from a symmetric trace-free spatial metric perturbation basis",
                "retire the minimal CLN ansatz and search a different closure basis for TT response",
            ],
        },
        "guardrails": {
            "claims_selected_P_GR": False,
            "claims_selected_GR_Hessian": False,
            "uses_observed_GR_data": False,
        },
    }
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(json.dumps({"wrote": str(OUT_CERT), "status": cert["status"]}, indent=2))


if __name__ == "__main__":
    main()

