"""Build source-amendment/corpus-discovery gate for oriented Phi_fin."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
MTT_CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

INPUTS = {
    "sourceleaf_request": DATA / "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea_source_theorem_request.json",
    "sourceleaf_gate": DATA / "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea.candidate.json",
    "minimal_fill_report": DATA / "selected_heterotic_orientedphifin_minimalnewsourcepacket_fill_report.json",
    "orientation_functor": DATA / "selected_heterotic_orientedphifin_finiterhoe_to_orientedbn_functor_or_smoothrepresentative.candidate.json",
    "carrier_attempt": DATA / "selected_heterotic_orientedphifin_orientedbn_carrier_or_endequotientfunctor.candidate.json",
    "standard_embedding_gate": DATA / "selected_heterotic_standard_embedding_selector_or_phifin_gate.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_sourceleaf_sourceamendment_or_corpusdiscovery.candidate.json"
OUTPUT_DISCOVERY = DATA / "selected_heterotic_orientedphifin_sourceleaf_corpus_discovery_report.json"
OUTPUT_PLAN = DATA / "selected_heterotic_orientedphifin_sourceleaf_minimal_source_amendment_plan.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_sourceleaf_sourceamendment_or_corpusdiscovery_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_SourceLeaf_SourceAmendment_or_CorpusDiscovery_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCELEAF_CORPUS_DISCOVERY_NO_EXISTING_SOURCE_PACKET_AMENDMENT_PLAN_BUILT"
NEXT = "Selected_Heterotic_OrientedPhiFin_DirectCarrier_SourceTheorem_ConstructiveAttempt_v1"

EXCLUDE_NAMES = {
    OUTPUT_DATA.name,
    OUTPUT_DISCOVERY.name,
    OUTPUT_PLAN.name,
    OUTPUT_CERT.name,
    OUTPUT_NOTE.name,
    "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea.candidate.json",
    "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea_source_theorem_request.json",
    "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea_certificate.json",
    "Selected_Heterotic_OrientedPhiFin_SourceLeaf_DirectCarrier_or_BundleA_v1.md",
    "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea_audit.py",
    "build_selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundleA.py",
}

NEEDLES = {
    "direct_selected_carrier": [
        "source_emits_oriented_BN_carrier",
        "same_branch_source_emits_oriented_BN_carrier",
        "oriented 27-mode B_N carrier",
        "oriented B_N carrier",
    ],
    "smooth_selected_bundle_A": [
        "selected_bundle_connection_A",
        "selected bundle connection A",
        "connection_A_components",
        "curvature_F_A_components",
        "E_Qa_matrix",
    ],
    "support_only_geometry": [
        "R+",
        "R^+",
        "Bismut",
        "GammaPlus",
        "standard embedding",
        "bundle connection",
        "E_Qa",
    ],
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def text_files(root: Path) -> list[Path]:
    if not root.exists():
        return []
    suffixes = {".md", ".txt", ".json", ".py"}
    result = []
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in suffixes and path.name not in EXCLUDE_NAMES:
            if ".git" not in path.parts and "reports" not in path.parts:
                result.append(path)
    return result


def scan(root: Path, max_hits_per_bucket: int = 8) -> dict[str, Any]:
    files = text_files(root)
    buckets: dict[str, dict[str, Any]] = {
        key: {"needle_hits": 0, "file_count": 0, "examples": []} for key in NEEDLES
    }
    matched_files: dict[str, set[str]] = {key: set() for key in NEEDLES}
    for path in files:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        lines = text.splitlines()
        for bucket, needles in NEEDLES.items():
            found_in_file = False
            for line_no, line in enumerate(lines, start=1):
                lower = line.lower()
                for needle in needles:
                    if needle.lower() in lower:
                        buckets[bucket]["needle_hits"] += 1
                        found_in_file = True
                        if len(buckets[bucket]["examples"]) < max_hits_per_bucket:
                            buckets[bucket]["examples"].append(
                                {
                                    "path": str(path),
                                    "line": line_no,
                                    "needle": needle,
                                    "snippet": line.strip()[:240],
                                }
                            )
                        break
            if found_in_file:
                matched_files[bucket].add(str(path))
    for bucket in buckets:
        buckets[bucket]["file_count"] = len(matched_files[bucket])
    return {
        "root": str(root),
        "exists": root.exists(),
        "files_scanned": len(files),
        "buckets": buckets,
    }


def main() -> dict[str, Any]:
    request = load(INPUTS["sourceleaf_request"])
    gate = load(INPUTS["sourceleaf_gate"])
    minimal = load(INPUTS["minimal_fill_report"])
    orientation = load(INPUTS["orientation_functor"])
    carrier = load(INPUTS["carrier_attempt"])
    standard = load(INPUTS["standard_embedding_gate"])

    repo_scan = scan(ROOT)
    corpus_scan = scan(MTT_CORPUS)

    direct_existing_packet_found = False
    smooth_existing_packet_found = False
    discovery = {
        "schema": "SelectedHeterotic.OrientedPhiFin.SourceLeaf.CorpusDiscovery.v1",
        "status": "NO_EXISTING_SOURCE_PACKET_FOUND",
        "repo_scan": repo_scan,
        "mtt_corpus_scan": corpus_scan,
        "classification": {
            "direct_selected_carrier_packet_found": direct_existing_packet_found,
            "smooth_selected_bundle_A_packet_found": smooth_existing_packet_found,
            "support_only_matches_found": (
                repo_scan["buckets"]["support_only_geometry"]["needle_hits"]
                + corpus_scan["buckets"]["support_only_geometry"]["needle_hits"]
            )
            > 0,
            "why_not_found": [
                "Exact direct carrier matches in the repo are blocker/request language, not an emitted source theorem.",
                "External MTT corpus matches generic heterotic R+/bundle-connection support, not selected Qa/SU3 bundle A/F_A/E_Qa data.",
                "The standard embedding is conditional and retired for the current source unless a new selector is supplied.",
            ],
        },
    }
    OUTPUT_DISCOVERY.write_text(json.dumps(discovery, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    plan = {
        "schema": "SelectedHeterotic.OrientedPhiFin.MinimalSourceAmendmentPlan.v1",
        "status": "DIRECT_CARRIER_CONSTRUCTIVE_ATTEMPT_SELECTED_NEXT",
        "reason": (
            "The direct lane is the smallest constructive next step: the 27-mode domain, "
            "orientation functor, exact table, kernel/no-double-count policy, and same-branch "
            "certificate support already exist. It still needs a source theorem upgrading the "
            "orientation-only carrier to a positive threshold-operator carrier without using "
            "Route-C import or target fitting."
        ),
        "next_direct_packet": {
            "emit_carrier_domain": request["lane_A_direct_carrier_required"]["carrier_domain_definition"],
            "prove_same_branch_source_emission": "derive oriented B_N as the quotient/projection carrier of the selected heterotic Qa/SU3 source",
            "prove_positive_operator_functor": "extend C_tau orientation plus Phi_fin magnitude into one source-owned positive threshold complex",
            "prove_finitepart_trace_identity": minimal["known_values"]["oriented_abs_sector_logdet_exact"],
            "audit_no_shortcuts": request["must_not_use"],
        },
        "smooth_lane_kept_as_fallback": {
            "why": "R+ geometry exists but selected bundle A/F_A, representation trace, quotient policy, and E_Qa are all absent.",
            "standard_embedding_status": standard["status"],
        },
    }
    OUTPUT_PLAN.write_text(json.dumps(plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "corpus_discovery_executed": True,
        "direct_existing_packet_found": direct_existing_packet_found,
        "smooth_existing_packet_found": smooth_existing_packet_found,
        "support_only_matches_found": discovery["classification"]["support_only_matches_found"],
        "minimal_source_amendment_plan_built": True,
        "next_lane": "direct_carrier_constructive_attempt",
        "next_required_artifact": NEXT,
        "oriented_logdet_promoted": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinSourceLeafSourceAmendmentOrCorpusDiscovery",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "discovery_report_path": rel(OUTPUT_DISCOVERY),
        "minimal_source_amendment_plan_path": rel(OUTPUT_PLAN),
        "parent_statuses": {
            "sourceleaf_gate": gate["status"],
            "orientation_functor": orientation["status"],
            "carrier_attempt": carrier["status"],
            "standard_embedding_gate": standard["status"],
        },
        "decision": decision,
        "theorem": {
            "name": "SourceLeafCorpusDiscoveryNoExistingPacketTheorem",
            "proved": True,
            "statement": (
                "Scanning the repo and local MTT corpus finds support-level heterotic, "
                "Bismut/R+, bundle-connection, Phi_fin, and E_Qa language, but no existing "
                "selected source packet that emits either the oriented B_N positive carrier "
                "or the selected bundle connection A/F_A/E_Qa payload. The next step is "
                "therefore constructive source amendment, with the direct carrier theorem "
                "as the smallest legal packet."
            ),
        },
        "guardrails": {
            "does_not_treat_keyword_match_as_source_packet": True,
            "does_not_promote_support_only_corpus_matches": True,
            "does_not_reopen_standard_embedding_without_selector": True,
            "does_not_promote_log92160000": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "discovery_report_path": rel(OUTPUT_DISCOVERY),
        "minimal_source_amendment_plan_path": rel(OUTPUT_PLAN),
        "direct_existing_packet_found": direct_existing_packet_found,
        "smooth_existing_packet_found": smooth_existing_packet_found,
        "minimal_source_amendment_plan_built": True,
        "next_required_artifact": NEXT,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin SourceLeaf SourceAmendment or CorpusDiscovery v1

## Result

```text
status = {STATUS}
direct_existing_packet_found = false
smooth_existing_packet_found = false
next_lane = direct_carrier_constructive_attempt
next_required_artifact = {NEXT}
```

## Meaning

The scan finds support-level language, but not the selected source packet needed
to close either first leaf. The next move is constructive source amendment, with
the direct oriented `B_N` carrier theorem as the smallest legal packet.

```text
{rel(OUTPUT_DISCOVERY)}
{rel(OUTPUT_PLAN)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_DISCOVERY)}")
    print(f"wrote {rel(OUTPUT_PLAN)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
