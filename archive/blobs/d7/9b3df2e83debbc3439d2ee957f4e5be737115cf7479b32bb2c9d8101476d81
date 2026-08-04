"""Hunt for selected data that could fill the visible rank-two L^2 packet.

The source-packet ledger identifies the next executable object:

    certificates/visible_rank2_l2_cohomology_data.template.json

This script checks whether the current repo, the local MTT corpus, or the
nearby Iwasawa/monad certificates already contain the selected Cech/Dolbeault
data needed for that packet.  It deliberately separates useful adjacent data
from data that can actually fill H^1(X,L^2).
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"
PROOF_CORPUS = ROOT / "proof_corpus"
EXTERNAL_CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
FLUX_SOURCE = (
    EXTERNAL_CORPUS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)

L2_GATE = CERTIFICATES / "visible_rank2_l2_ext_h1_gate_certificate.json"
VALPHA_LEDGER = CERTIFICATES / "visible_valpha_chern_bianchi_source_packet_candidates_certificate.json"
MONAD_GATE = CERTIFICATES / "iwasawa_monad_map_data_gate_certificate.json"
A01_GATE = CERTIFICATES / "iwasawa_dolbeault_complex_extraction_certificate.json"
CORRECTED_A01 = CERTIFICATES / "corrected_a01_candidate_scan_certificate.json"
INDEX_GATE = CERTIFICATES / "index_to_three_family_upgrade_gate_certificate.json"

CANDIDATE = CANDIDATE_DATA / "visible_rank2_l2_cohomology_source_hunt.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_rank2_l2_cohomology_source_hunt_certificate.json"

TARGET_L = [1, -2, 0]
TARGET_L2 = [2, -4, 0]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def has_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns)


def collect_repo_hits() -> dict[str, list[str]]:
    patterns = {
        "target_L2_vector": [r"\(2,\s*-4,\s*0\)", r"\[2,\s*-4,\s*0\]"],
        "h1_l2": [r"H\^1\(X,\s*L\^2\)", r"H1\(X,\s*L\^2\)"],
        "cech_dolbeault": [r"Cech", r"Deligne/Cech", r"Dolbeault", r"transition data"],
        "nonzero_ext": [r"nonzero Ext", r"closed non-exact", r"Ext\^1\(L\^{-1},L\)"],
    }
    hits = {key: [] for key in patterns}
    for root in (PROOF_CORPUS, CERTIFICATES, CANDIDATE_DATA):
        for path in sorted(root.rglob("*")):
            if path.suffix.lower() not in {".md", ".json", ".py"}:
                continue
            text = read_text(path)
            for key, pats in patterns.items():
                if has_any(text, pats):
                    hits[key].append(str(path.relative_to(ROOT)))
    return hits


def vector_matches(monad: dict[str, Any]) -> dict[str, Any]:
    source_monad = monad.get("source_monad", {})
    line_vectors = source_monad.get("line_bundle_c1_vectors_abc", {})
    typed = monad.get("typed_map_check", {})
    f_types = typed.get("f_entry_types", {})
    g_types = typed.get("g_entry_types", {})

    all_named: dict[str, list[int]] = {}
    for key, value in line_vectors.items():
        all_named[f"line.{key}"] = value
    for key, value in f_types.items():
        all_named[f"f_type.{key}"] = value
    for key, value in g_types.items():
        all_named[f"g_type.{key}"] = value

    direct_matches = [name for name, value in all_named.items() if value == TARGET_L2]
    sign_matches = [name for name, value in all_named.items() if value == [-v for v in TARGET_L2]]
    return {
        "target_l_vector": TARGET_L,
        "target_l2_vector": TARGET_L2,
        "checked_vector_count": len(all_named),
        "direct_target_matches": direct_matches,
        "opposite_target_matches": sign_matches,
        "all_checked_vectors": all_named,
    }


def analyze() -> dict[str, Any]:
    l2_gate = load_json(L2_GATE)
    valpha = load_json(VALPHA_LEDGER)
    monad = load_json(MONAD_GATE)
    a01 = load_json(A01_GATE)
    corrected = load_json(CORRECTED_A01)
    index_gate = load_json(INDEX_GATE)
    flux_text = read_text(FLUX_SOURCE)
    repo_hits = collect_repo_hits()
    vector_scan = vector_matches(monad)

    flux_hits = {
        "flux_source_exists": FLUX_SOURCE.exists(),
        "explicit_left_invariant_barpartial_E_section": "ExplicitDolbeault" in flux_text
        and "bar\\partial_E" in flux_text,
        "monad_sequence_present": "0\\longrightarrow K_1" in flux_text
        and "E:=\\ker g / \\mathrm{im}\\,f" in flux_text,
        "generic_maps_constant_matrices_claim": "generic holomorphic maps" in flux_text
        and "constant matrices" in flux_text,
        "target_L2_vector_literal_present": "(2,-4,0)" in flux_text
        or "(2, -4, 0)" in flux_text,
        "H1_X_L2_literal_present": "H^1(X,L^2)" in flux_text
        or "H^1(X, L^2)" in flux_text,
    }

    route_evaluation = {
        "R1_direct_selected_L2_cochain_packet": {
            "status": "BLOCKED_NOT_FOUND",
            "evidence": {
                "repo_h1_l2_hits": repo_hits["h1_l2"],
                "repo_target_L2_hits": repo_hits["target_L2_vector"],
                "external_flux_H1_X_L2_literal_present": flux_hits["H1_X_L2_literal_present"],
                "external_flux_target_L2_vector_literal_present": flux_hits[
                    "target_L2_vector_literal_present"
                ],
            },
            "reason": "The current corpus mentions the target only in the new gates; no selected matrices d0,d1 or extension vector are present.",
        },
        "R2_flux_explicit_barpartial_E": {
            "status": "BLOCKED_WRONG_OBJECT_AND_LITERAL_A01_FAILS",
            "evidence": {
                "explicit_barpartial_E_section_present": flux_hits[
                    "explicit_left_invariant_barpartial_E_section"
                ],
                "source_object": "rank-three monad E, not the line bundle L^2",
                "literal_A01_integrable": a01.get("literal_integrability_result", {}).get(
                    "integrable"
                ),
                "literal_A01_can_fill_zero_mode_slots": a01.get(
                    "consequence_for_sm_closure", {}
                ).get("literal_A01_can_fill_zero_mode_slots"),
            },
            "reason": "Even before selection, the printed A^(0,1) is not a scalar L^2 Dolbeault operator and the audited literal matrix fails integrability.",
        },
        "R3_typed_monad_or_line_table_reuse": {
            "status": "BLOCKED_TYPED_MAPS_AND_NO_L2_MATCH",
            "evidence": {
                "typed_f_entries_available": monad.get("source_monad", {}).get(
                    "source_gives_explicit_f_entries"
                ),
                "typed_g_entries_available": monad.get("source_monad", {}).get(
                    "source_gives_explicit_g_entries"
                ),
                "requires_transition_data": monad.get("typed_map_check", {}).get(
                    "requires_global_holomorphic_sections_or_transition_data"
                ),
                "vector_scan": vector_scan,
            },
            "reason": "The printed monad is useful matter data, but no listed line or typed map slot is the target c1(L^2)=(2,-4,0), and f,g sections are absent.",
        },
        "R4_corrected_A01_or_diagnostic_h1": {
            "status": "BLOCKED_UNSELECTED_WRONG_OBJECT",
            "evidence": {
                "sparse_h1_three_candidates_exist": corrected.get("verdict", {}).get(
                    "sparse_h1_three_candidates_exist"
                ),
                "can_select_unique_corrected_A01_from_sparse_scan": corrected.get(
                    "consequence_for_sm_closure", {}
                ).get("can_select_unique_corrected_A01_from_sparse_scan"),
                "upgrade_h1_X_E_equals_three": index_gate.get("upgrade_requirements", {}).get(
                    "h1_X_E_equals_three"
                ),
            },
            "reason": "Diagnostic h1 candidates test the finite machinery but do not select L^2, the Ext class, or the visible V_alpha source.",
        },
        "R5_construct_selected_L2_from_geometry": {
            "status": "NEXT_REQUIRED_CONSTRUCTION",
            "required_packet": "SelectedVisibleL2LineBundleCohomologyPacket.v1",
            "minimum_fields": [
                "source certificate selecting the holomorphic line bundle L^2 with c1=(2,-4,0)",
                "good-cover transition functions or equivalent Dolbeault operator",
                "finite bases C0,C1,C2",
                "differentials d0,d1 with d1*d0=0",
                "extension vector eta in C1",
                "validator proof that eta is closed and not exact",
                "no observed or benchmark flavor inputs",
            ],
            "validator": "scripts/validate_visible_rank2_l2_cohomology.py",
        },
    }

    selected_l2_found = False
    report = {
        "calculation": "VisibleRank2L2CohomologySourceHunt",
        "status": "VISIBLE_RANK2_L2_COHOMOLOGY_SOURCE_HUNT_BLOCKED_SELECTED_DATA_ABSENT",
        "generated_by": "scripts/hunt_visible_rank2_l2_cohomology_source.py",
        "input_certificates": {
            "visible_rank2_l2_ext_h1_gate": L2_GATE.name,
            "visible_valpha_chern_bianchi_source_packet_candidates": VALPHA_LEDGER.name,
            "iwasawa_monad_map_data_gate": MONAD_GATE.name,
            "iwasawa_dolbeault_complex_extraction": A01_GATE.name,
            "corrected_a01_candidate_scan": CORRECTED_A01.name,
            "index_to_three_family_upgrade_gate": INDEX_GATE.name,
        },
        "source_targets": {
            "extension_sequence": "0 -> L -> V_alpha -> L^-1 -> 0",
            "l_vector_abc": TARGET_L,
            "l2_vector_abc": TARGET_L2,
            "validator_template": "certificates/visible_rank2_l2_cohomology_data.template.json",
        },
        "repo_search_hits": repo_hits,
        "flux_source_hits": flux_hits,
        "route_evaluation": route_evaluation,
        "calculation_results": {
            "selected_L2_cochain_packet_found": selected_l2_found,
            "external_flux_explicit_dolbeault_section_found": flux_hits[
                "explicit_left_invariant_barpartial_E_section"
            ],
            "external_flux_section_can_fill_L2": False,
            "monad_line_or_typed_slot_matches_L2_vector": bool(
                vector_scan["direct_target_matches"]
            ),
            "typed_monad_maps_available": False,
            "diagnostic_h1_candidates_selected": False,
            "must_construct_selected_L2_packet_from_geometry": True,
        },
        "what_this_closes": {
            "corpus_hunt_for_hidden_L2_packet": True,
            "flux_A01_shortcut_rejected_for_L2": True,
            "typed_monad_reuse_rejected_for_L2": True,
            "diagnostic_h1_reuse_rejected_for_L2": True,
            "exact_next_L2_packet_requirements_recorded": True,
        },
        "still_open": {
            "construct_selected_L2_transition_or_Dolbeault_data": True,
            "compute_actual_h1_for_L_squared": True,
            "select_nonzero_extension_class": True,
            "prove_non_split_extension_stability": True,
            "prove_HYM_or_Route_C_residual": True,
            "derive_same_total_source_D_E_dotD_Riesz_Green": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_L2_packet_found": False,
            "claims_flux_A01_fills_L2": False,
            "claims_monad_E_is_V_alpha": False,
            "claims_diagnostic_h1_is_selected": False,
            "claims_actual_H1_value": False,
            "claims_nonzero_Ext_class": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The corpus does not currently contain the selected Cech or "
                "Dolbeault matrices for H^1(X,L^2). The flux paper supplies an "
                "explicit Dolbeault-looking object, but it belongs to the old "
                "rank-three monad E, not L^2, and the audited literal A^(0,1) "
                "matrix is not a valid selected operator. The typed monad table "
                "also has no c1(L^2)=(2,-4,0) slot with explicit sections."
            ),
            "next_action": (
                "Construct a SelectedVisibleL2LineBundleCohomologyPacket from "
                "geometry: transition functions or a Dolbeault operator for "
                "c1(L^2)=(2,-4,0), finite cochain bases, d0,d1, and a closed "
                "non-exact eta, then run the existing validator."
            ),
        },
    }
    return report


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleRank2L2CohomologySourceHunt",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_rank2_l2_cohomology_source_hunt.candidate.json",
        "input_certificates": report["input_certificates"],
        "source_targets": report["source_targets"],
        "repo_search_hits": report["repo_search_hits"],
        "flux_source_hits": report["flux_source_hits"],
        "route_evaluation": report["route_evaluation"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
