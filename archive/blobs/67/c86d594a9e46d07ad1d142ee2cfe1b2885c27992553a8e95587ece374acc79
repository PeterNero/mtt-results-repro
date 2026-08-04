from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

STF_CERT = ROOT / "certificates" / "stf_shear_tt_bridge_certificate.json"
OUT_CERT = ROOT / "certificates" / "lens_to_stf_source_identification_attempt_certificate.json"

SOURCES = {
    "proto_spinor_triadic": TEXPAPERS
    / "10 ProtoSpinor"
    / "_work"
    / "The_Proto_Spinor__Triadic_Closure_from_Pointwise_Internal_Embedding_v4"
    / "main.tex",
    "world_in_world": TEXPAPERS
    / "10 ProtoSpinor"
    / "_work"
    / "World_in_World_Genesis__A_Proto_Geometric_Origin_of_Time__Gravity__Matter__and_Quantization_in_Modal_Triplet_Theory_v4"
    / "main.tex",
    "closure_geometry": TEXPAPERS
    / "10 ProtoSpinor"
    / "_work"
    / "Closure_Geometry_and_Unified_Dynamics__A_Ten_Dimensional_Action_for_Mass__Scalar_Relaxation__Quantization__and_Curvature_v3"
    / "main.tex",
    "gr_reduction": OBSIDIAN
    / "11 General Relativity & Geometry"
    / "Modal_Triplet_Theory__From_MTT_to_General_Relativity_v2.md",
    "qg_uv": TEXPAPERS
    / "12 Quantum Gravity"
    / "_md"
    / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md",
    "theta_twistor_normalization": OBSIDIAN
    / "18 Theta-Closure & Execution Program"
    / "Theta_Closure_in_Modal_Triplet_Theory_III__Twistor_Action_Matching_and_Independent_Normalization.md",
}

PATTERNS = {
    "lens_transport_role": r"lens.*transport|transport.*lens|local transport|redundancy transport|lens curvature",
    "lens_as_gauge_redundancy": r"lens.*gauge redundancy|gauge redundancy.*lens|upstream carrier of gauge",
    "gauge_flat_lens": r"gauge-flat lens|orthogonal to gauge-flat lens",
    "bookkeeping_strain_curvature": r"bookkeeping strain|closure strain|integrability obstruction|Frobenius integrability",
    "tetrad_synchronization": r"tetrads? are bookkeeping|synchronization|bookkeeping.*synchron",
    "lens_spatial_metric_scale": r"spatial metric.*R_\\?\{?\\?mathrm\{lens\}|direction-sphere area|S\^2_\\?\{?f_2R|lens sector.*4\\pi",
    "stf_tt_language": r"trace-free|trace free|symmetric trace-free|\bSTF\b|transverse--traceless|transverse-traceless|\bTT\b|h_TT",
    "direct_lens_to_stf": r"\blens\b[^\n.;]{0,160}\b(STF|trace-free|trace free|transverse shear|TT|h_TT|metric shear)\b|\b(STF|trace-free|trace free|transverse shear|TT|h_TT|metric shear)\b[^\n.;]{0,160}\blens\b",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def has(text: str, pattern: str) -> bool:
    return bool(re.search(pattern, text, flags=re.IGNORECASE))


def snippets(text: str, pattern: str, limit: int = 2, radius: int = 120) -> list[str]:
    out: list[str] = []
    for match in re.finditer(pattern, text, flags=re.IGNORECASE):
        start = max(0, match.start() - radius)
        end = min(len(text), match.end() + radius)
        snippet = re.sub(r"\s+", " ", text[start:end]).strip()
        out.append(snippet)
        if len(out) >= limit:
            break
    return out


def scan_sources() -> dict[str, Any]:
    result: dict[str, Any] = {}
    for source_id, path in SOURCES.items():
        text = read(path)
        result[source_id] = {
            "path": str(path),
            "exists": path.exists(),
            "hits": {name: has(text, pattern) for name, pattern in PATTERNS.items()},
            "snippets": {
                name: snippets(text, pattern, limit=1)
                for name, pattern in PATTERNS.items()
                if has(text, pattern)
            },
        }
    return result


def sources_with(hits: dict[str, Any], key: str) -> list[str]:
    return [source_id for source_id, row in hits.items() if row["hits"].get(key)]


def main() -> None:
    stf_cert = load_json(STF_CERT)
    hits = scan_sources()

    lens_transport = sources_with(hits, "lens_transport_role")
    lens_gauge = sources_with(hits, "lens_as_gauge_redundancy")
    gauge_flat_lens = sources_with(hits, "gauge_flat_lens")
    strain_curvature = sources_with(hits, "bookkeeping_strain_curvature")
    tetrad_sync = sources_with(hits, "tetrad_synchronization")
    lens_scale = sources_with(hits, "lens_spatial_metric_scale")
    stf_tt = sources_with(hits, "stf_tt_language")
    direct_lens_stf = sources_with(hits, "direct_lens_to_stf")

    direct_lens_to_stf_closed = bool(direct_lens_stf) and not bool(gauge_flat_lens)
    source_promotes_minimal_cln = direct_lens_to_stf_closed
    points_away_from_lens_tt = bool(gauge_flat_lens or lens_gauge) and not direct_lens_to_stf_closed

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "lens_to_stf_source_identification_attempt",
        "status": "LENS_TO_STF_SOURCE_IDENTIFICATION_BLOCKED_GAUGE_FLAT_LENS_EVIDENCE",
        "input_certificate": {
            "stf_bridge_status": stf_cert["status"],
            "stf_bridge_closed": stf_cert["bridge_closed"],
        },
        "evidence_summary": {
            "lens_transport_sources": lens_transport,
            "lens_as_gauge_redundancy_sources": lens_gauge,
            "gauge_flat_lens_sources": gauge_flat_lens,
            "bookkeeping_strain_curvature_sources": strain_curvature,
            "tetrad_synchronization_sources": tetrad_sync,
            "lens_spatial_metric_scale_sources": lens_scale,
            "stf_tt_language_sources": stf_tt,
            "direct_lens_to_stf_sources": direct_lens_stf,
        },
        "source_tests": {
            "ordinary_stf_to_tt_bridge_closed": stf_cert["bridge_closed"],
            "lens_transport_present": bool(lens_transport),
            "gravity_as_strain_integrability_present": bool(strain_curvature),
            "lens_spatial_metric_scale_present": bool(lens_scale),
            "direct_lens_to_stf_metric_shear_found": bool(direct_lens_stf),
            "gauge_flat_lens_evidence_found": bool(gauge_flat_lens),
            "direct_lens_to_stf_closed": direct_lens_to_stf_closed,
            "source_promotes_minimal_cln_candidate": source_promotes_minimal_cln,
            "points_away_from_lens_tt_identification": points_away_from_lens_tt,
        },
        "interpretation": {
            "closed": (
                "The corpus supports lens as redundancy transport and supports an "
                "independent STF/TT target for gravitational response."
            ),
            "not_closed": (
                "The corpus does not source-certify a map from lens transport/shear "
                "to transverse trace-free metric shear."
            ),
            "correction": (
                "The minimal CLN finite candidate must remain a rank-pattern witness, "
                "not a selected GR source theorem."
            ),
            "preferred_forward_route": (
                "Promote the TT source search from the closure-strain/integrability "
                "sector, especially the subspace orthogonal to gauge-flat lens "
                "directions, rather than identifying lens directions with physical TT modes."
            ),
        },
        "next_obligation": {
            "name": "closure_strain_to_stf_source_candidate",
            "must_compute": [
                "decompose closure/bookkeeping strain into gauge-flat, scalar radial, and STF tensor pieces",
                "prove the STF tensor piece is transverse after synchronization constraints",
                "extract the selected Hessian restricted to that STF tensor piece",
                "compare the resulting TT block with the Lichnerowicz target",
            ],
        },
        "guardrails": {
            "claims_lens_is_selected_TT_source": False,
            "claims_minimal_cln_source_closed": False,
            "claims_full_GR_closed": False,
            "claims_only_standard_linear_algebra_bridge_closed": True,
        },
        "source_scan": hits,
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
