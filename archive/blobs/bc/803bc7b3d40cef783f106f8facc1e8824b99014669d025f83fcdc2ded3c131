"""Attempt to fill the selected CKM heavy-link packet.

The calculator needs eight selected entries:

    t_u13, t_u23, t_d13, t_d23,
    c_u13, c_u23, c_d13, c_d23.

This script tries to source them from the current proof package.  It does not
invent entries.  If the selected C1 primitive contractions and selected C6
support matrices are absent, it returns a blocked attempt packet with the exact
missing fields.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERT_DIR = ROOT / "certificates"
EXTERNAL_CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

TEMPLATE = CERT_DIR / "selected_ckm_heavy_link_packet.template.json"
C1_PRIMITIVES = CERT_DIR / "selected_c1_primitive_contractions.template.json"
C1_RESPONSE = CERT_DIR / "selected_c1_response_data_certificate.template.json"
C6_SUPPORT_CANDIDATES = [
    CERT_DIR / "selected_c6_support_matrices_certificate.json",
    CERT_DIR / "iwasawa_c6_support_matrices_certificate.json",
    CERT_DIR / "selected_c6_support_data_certificate.json",
    ROOT / "candidate_data" / "selected_c6_support_matrices.json",
    ROOT / "candidate_data" / "iwasawa_c6_support_matrices.selected.json",
]
ENTRY_TOKENS = (
    "t_u13",
    "t_u23",
    "t_d13",
    "t_d23",
    "c_u13",
    "c_u23",
    "c_d13",
    "c_d23",
    "C_u13",
    "C_u23",
    "C_d13",
    "C_d23",
)
PRIMITIVE_TERMS = (
    "theta_overlap_variation",
    "left_zero_mode_response",
    "right_zero_mode_response",
    "higgs_zero_mode_response",
    "explicit_vertex",
    "basis_connection",
)
SECTORS = ("u", "d", "e", "nuD")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def missing_null_paths(value: Any, prefix: str = "") -> list[str]:
    if value is None:
        return [prefix]
    if isinstance(value, dict):
        paths: list[str] = []
        for key, item in value.items():
            child = f"{prefix}.{key}" if prefix else str(key)
            paths.extend(missing_null_paths(item, child))
        return paths
    if isinstance(value, list):
        paths = []
        for index, item in enumerate(value):
            child = f"{prefix}[{index}]"
            paths.extend(missing_null_paths(item, child))
        return paths
    return []


def primitive_missing(template: dict[str, Any]) -> list[str]:
    sectors = template.get("sectors", {})
    missing: list[str] = []
    for sector in SECTORS:
        sector_data = sectors.get(sector, {})
        for term in PRIMITIVE_TERMS:
            if sector_data.get(term) is None:
                missing.append(f"sectors.{sector}.{term}")
    return missing


def present_c6_support_files() -> list[str]:
    return [rel(path) for path in C6_SUPPORT_CANDIDATES if path.exists()]


def direct_token_hits(root: Path, max_hits: int = 25) -> list[str]:
    if not root.exists():
        return []
    hits: list[str] = []
    suffixes = {".md", ".txt", ".json", ".tex", ".py"}
    for path in root.rglob("*"):
        if len(hits) >= max_hits:
            break
        if not path.is_file() or path.suffix.lower() not in suffixes:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for token in ENTRY_TOKENS:
            if token in text:
                hits.append(f"{rel(path)}:{token}")
                break
    return hits


def heavy_link_missing_entries(packet: dict[str, Any]) -> list[str]:
    inputs = packet.get("inputs", {})
    return missing_null_paths(inputs, "inputs")


def build_attempt() -> dict[str, Any]:
    template = load_json(TEMPLATE)
    c1_template = load_json(C1_PRIMITIVES)
    c1_response = load_json(C1_RESPONSE)
    c1_missing = primitive_missing(c1_template)
    c6_present = present_c6_support_files()
    repo_hits = direct_token_hits(ROOT)
    external_hits = direct_token_hits(EXTERNAL_CORPUS)

    attempt = dict(template)
    attempt["certificate"] = "SelectedCKMHeavyLinkPacketAttempt"
    attempt["status"] = "BLOCKED_SELECTED_HEAVY_LINK_SOURCES_MISSING"
    attempt["description"] = (
        "Attempted fill of the leading CKM heavy-link packet from current "
        "selected C1 primitive contractions and selected C6 support data."
    )
    attempt["source_hunt"] = {
        "selected_c1_primitive_contractions_file": rel(C1_PRIMITIVES),
        "selected_c1_primitive_contractions_complete": len(c1_missing) == 0,
        "selected_c1_missing_primitive_matrices": len(c1_missing),
        "selected_c1_response_delta_v": c1_response.get("computed_tests", {}).get("Delta_v_ud"),
        "selected_c6_support_files_present": c6_present,
        "selected_c6_support_files_expected": [rel(path) for path in C6_SUPPORT_CANDIDATES],
        "repo_direct_entry_token_hits": repo_hits,
        "external_corpus_path": str(EXTERNAL_CORPUS),
        "external_corpus_available": EXTERNAL_CORPUS.exists(),
        "external_direct_entry_token_hits": external_hits,
    }
    attempt["fill_attempt"] = {
        "character_trivial_entries_filled": False,
        "c6_entries_filled": False,
        "Delta_v_computable": False,
        "missing_heavy_link_entries": heavy_link_missing_entries(attempt),
        "first_blocker": "selected_C6_support_and_character_trivial_heavy_link_values_absent",
    }
    attempt["blocked_by"] = {
        "t_u_t_d": (
            "Requires selected character-trivial heavy-link aggregate, at least "
            "selected primitive contractions feeding M_u13,M_u23,M_d13,M_d23, "
            "plus any other retained non-C6 channel support."
        ),
        "c_u_c_d": (
            "Requires selected C6 amplitude-support matrices or equivalent "
            "sector-resolved C6 heavy-link entries."
        ),
    }
    attempt["can_compute_now"] = {
        "selected_t_u_t_d": False,
        "selected_c_u_c_d": False,
        "selected_Delta_v": False,
        "leading_CKM_noncommutation_pass_fail": False,
        "Jarlskog_value": False,
        "Yukawa_magnitudes": False,
        "full_SM_closure": False,
    }
    attempt["guardrails"] = {
        "uses_execution_ii_benchmarks": False,
        "uses_observed_masses_or_mixings": False,
        "invents_heavy_link_entries": False,
        "claims_selected_Delta_v_computed": False,
        "claims_full_SM_closure": False,
    }
    return attempt


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", type=Path, help="optional path for the attempt packet")
    args = parser.parse_args()

    attempt = build_attempt()
    encoded = json.dumps(attempt, indent=2, sort_keys=True)
    if args.write is not None:
        target = args.write
        if not target.is_absolute():
            target = ROOT / target
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(encoded + "\n", encoding="utf-8")
    print(encoded)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
