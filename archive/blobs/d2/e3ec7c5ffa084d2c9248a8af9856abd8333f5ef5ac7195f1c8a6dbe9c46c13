"""Build the corpus-backed MTT no-knob upgrade backlog."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

INPUT = DATA / "empirical_equivalence_ledger.candidate.json"
OUTPUT_DATA = DATA / "no_knob_upgrade_backlog.candidate.json"
OUTPUT_CERT = CERTS / "no_knob_upgrade_backlog_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_No_Knob_Upgrade_Backlog_v1.md"


SOURCE_REGISTRY = {
    "qm_measurement_born_records": [
        OBSIDIAN
        / "8 Measurement, Selection & Computation"
        / "Measurement_as_Disturbance_and_Stabilization_in_Modal_Triplet_Theory_v5.md",
        OBSIDIAN
        / "8 Measurement, Selection & Computation"
        / "Why_Quantum_Contextuality_and_Measurement_Order_Dependence_Are_the_Same_Phenomenon.md",
    ],
    "qft_local_observables": [
        OBSIDIAN
        / "7 Quantum Field Theory"
        / "Modal_Triplet_Theory__Quantum_Amplitudes_from_Modal_Geometry_v2.md",
    ],
    "sm_topology_only": [
        OBSIDIAN
        / "13 Standard Model & Topology-Only Constraints"
        / "Topology__Only_Constraints_in_Modal_Triplet_Theory.md",
        OBSIDIAN
        / "13 Standard Model & Topology-Only Constraints"
        / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md",
    ],
    "string_flux_mtheory": [
        OBSIDIAN
        / "16 Strings, Flux, & M-Theory Encodings"
        / "Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md",
        OBSIDIAN
        / "16 Strings, Flux, & M-Theory Encodings"
        / "Modal_Triplet_Theory__From_MTT_to_M_theory.md",
    ],
    "theta_gauge_flavor": [
        OBSIDIAN
        / "18 Theta-Closure & Execution Program"
        / "Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry.md",
        OBSIDIAN
        / "18 Theta-Closure & Execution Program"
        / "Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v2.md",
    ],
    "q79_flavor_cp": [
        TEXPAPERS
        / "mtt-q79-proof-repro"
        / "proof_corpus"
        / "Terminal_Closure_Certificate_and_Remaining_Proof_Obligations_v1.md",
        TEXPAPERS
        / "mtt-q79-proof-repro"
        / "proof_corpus"
        / "Theta_Selected_Overlap_Kernel_Skeleton_for_No_Proxy_Flavor_v1.md",
    ],
    "qa_su3_packet": [
        TEXPAPERS
        / "mtt-qa-su3-packet-proof"
        / "certificates"
        / "full_corpus_dependency_audit_certificate.json",
        TEXPAPERS
        / "mtt-qa-su3-packet-proof"
        / "proof_corpus"
        / "Selected_Qa_SU3_Full_Corpus_Dependency_Audit_v1.md",
        TEXPAPERS
        / "mtt-qa-su3-packet-proof"
        / "certificates"
        / "gr_surface_internal_quantum_separation_theorem_certificate.json",
    ],
    "nonsm_constants": [
        TEXPAPERS
        / "mtt-nonsm-constants-no-knob"
        / "certificates"
        / "nonsm_constants_status_matrix_certificate.json",
        TEXPAPERS / "mtt-nonsm-constants-no-knob" / "reports" / "verification_report.txt",
    ],
    "gr_response": [
        TEXPAPERS
        / "mtt-protospinor-gr-response-proof"
        / "certificates"
        / "gr_dependency_matrix_certificate.json",
        TEXPAPERS
        / "mtt-protospinor-gr-response-proof"
        / "proof_corpus"
        / "Absolute_Normalization_Bridge_from_NonSM_v1.md",
    ],
    "quantum_gravity": [
        OBSIDIAN
        / "11 General Relativity & Geometry"
        / "Why__GR_Falls_Out_of_String_Theory___A_Coherent_Admissibility_Shadow_Bridge_in_Modal_Triplet_Theory.md",
        OBSIDIAN
        / "12 Quantum Gravity"
        / "A_Third_Corner_Shadow_Bridge__Asymptotic_Safety__the_String_Corner__and_the_Coherent_Spine_in_Modal_Triplet_Theory.md",
    ],
}


BACKLOG_ROWS = [
    {
        "id": "born_record_no_knob",
        "target": "Born weights and stable record selection",
        "source_keys": ["qm_measurement_born_records"],
        "current_support": "Corpus contains basin/projection/FCC measurement papers with explicit Born-rule and record-stability claims.",
        "upgrade_needed": "Extract a compact theorem with stated hypotheses, map it into the measured-parameter interface, and audit that no empirical outcome frequencies select the source.",
        "priority": "P0",
        "status": "CORPUS_SUPPORT_PRESENT_FORMAL_AUDIT_OPEN",
    },
    {
        "id": "local_qft_functor",
        "target": "Local QFT observable functor and renormalization interface",
        "source_keys": ["qft_local_observables", "theta_gauge_flavor"],
        "current_support": "QFT corpus claims MTT-to-AQFT projection, local nets, pAQFT, LSZ/scattering regimes, and RG freedom; theta papers supply gauge/RG execution scaffolds.",
        "upgrade_needed": "Turn the local observable projection into a reproducible functor certificate and separate selected operator structure from measured running parameters.",
        "priority": "P0",
        "status": "CORPUS_SUPPORT_PRESENT_FUNCTOR_CERTIFICATE_OPEN",
    },
    {
        "id": "selected_sm_packet",
        "target": "Actual selected SM gauge/representation/family/Higgs packet",
        "source_keys": ["sm_topology_only", "string_flux_mtheory", "qa_su3_packet"],
        "current_support": "Topology-only corpus supports hypercharges, anomalies, family/topology claims, and operator forbiddance; Qa/SU3 audit finds no contradiction but leaves selected operator/source packet open.",
        "upgrade_needed": "Supply the actual selected representation packet, anomaly calculation certificate, and Qa/SU3 color/operator packet via typed monad or section-ring data.",
        "priority": "P0",
        "status": "STRUCTURAL_SUPPORT_STRONG_SELECTED_PACKET_OPEN",
    },
    {
        "id": "gauge_threshold_no_knob",
        "target": "Gauge coupling threshold kernels and absolute gauge normalization",
        "source_keys": ["theta_gauge_flavor", "nonsm_constants", "qa_su3_packet"],
        "current_support": "Theta and non-SM repos contain gauge ratio, threshold, determinant, zeta, U1/SU2, Qc/SU2, and Qa/SU3 candidate work. The Qa/SU3 packet repo now source-amends the GR-surface/internal-quantum split and promotes log(2008) only as the internal reduced Qa/SU3 determinant.",
        "upgrade_needed": "Bridge the internal reduced logdet log(2008) to a selected coupling/threshold response rule, while keeping the GR/protospinor smooth surface out of the Qa/SU3 determinant and avoiding observed gauge values as selectors.",
        "priority": "P1",
        "status": "INTERNAL_REDUCED_QA_SU3_DETERMINANT_STATUS_CLOSED_COUPLING_BRIDGE_OPEN",
    },
    {
        "id": "yukawa_cp_higgs_no_knob",
        "target": "Yukawa magnitudes, CKM/PMNS, CP labels, and Higgs parameters",
        "source_keys": ["q79_flavor_cp", "theta_gauge_flavor", "string_flux_mtheory", "sm_topology_only"],
        "current_support": "q79 exact-charge branch proves q=79 mod 448 for the selected CP branch; theta/string/topology corpus supports overlap-integral and central-circle/Yukawa mechanisms.",
        "upgrade_needed": "Compute actual selected overlap matrices and Higgs source kernels from the same branch, not benchmark flavor inputs.",
        "priority": "P1",
        "status": "CP_LABEL_BRANCH_STRONG_NUMERIC_YUKAWA_HIGGS_OPEN",
    },
    {
        "id": "gr_dynamics_and_stress_response",
        "target": "GR metric dynamics, stress-energy coupling, and matter/gauge response",
        "source_keys": ["gr_response", "quantum_gravity"],
        "current_support": "GR dependency matrix shows full GR target reaches many open response gates; GR/QG corpus aligns Einstein dynamics with admissibility/RG fixed points.",
        "upgrade_needed": "Close chart/time/curvature response, finite C1 matrices, Hessian kernel, stress response, and unit dictionary certificates.",
        "priority": "P0",
        "status": "DEPENDENCY_MAP_BUILT_RESPONSE_GATES_OPEN",
    },
    {
        "id": "absolute_dimensionful_normalization",
        "target": "Physical absolute normalization for G_N, Planck scale, f_a, and related dimensionful anchors",
        "source_keys": ["nonsm_constants", "gr_response"],
        "current_support": "Non-SM status matrix certifies conditional/rational results and identifies absolute normalization as the main blocker; GR bridge tracks selected absolute normalization as open.",
        "upgrade_needed": "Supply selected G10/R1^3, volume, modal gap, or equivalent physical anchor without observed target backsolve.",
        "priority": "P0",
        "status": "MAIN_DIMENSIONFUL_BLOCKER_OPEN",
    },
    {
        "id": "actual_empirical_equivalence_run",
        "target": "Numerical empirical equivalence audit after source packet and parity inputs are declared",
        "source_keys": ["nonsm_constants", "q79_flavor_cp", "qa_su3_packet", "gr_response"],
        "current_support": "Repos contain verification scripts, certificates, and partial numerical candidates across constants, q79, Qa/SU3, and GR.",
        "upgrade_needed": "Build a single audit that imports declared selected packets and measured parity slots, computes observables, and records pass/fail without source re-selection.",
        "priority": "P0",
        "status": "AUDIT_INFRASTRUCTURE_PRESENT_INTEGRATION_OPEN",
    },
]


def load_input() -> dict[str, object]:
    return json.loads(INPUT.read_text(encoding="utf-8"))


def source_status() -> dict[str, object]:
    return {
        key: {
            "paths": [str(path) for path in paths],
            "present": [str(path) for path in paths if path.exists()],
            "missing": [str(path) for path in paths if not path.exists()],
            "all_present": all(path.exists() for path in paths),
        }
        for key, paths in SOURCE_REGISTRY.items()
    }


def expand_rows(status: dict[str, object]) -> list[dict[str, object]]:
    rows = []
    for row in BACKLOG_ROWS:
        sources = []
        missing = []
        for key in row["source_keys"]:
            sources.extend(status[key]["present"])
            missing.extend(status[key]["missing"])
        new_row = dict(row)
        new_row["supporting_sources"] = sources
        new_row["missing_sources"] = missing
        new_row["corpus_backed"] = bool(sources)
        new_row["closed_now"] = False
        rows.append(new_row)
    return rows


def build_candidate() -> dict[str, object]:
    input_data = load_input()
    status = source_status()
    rows = expand_rows(status)
    return {
        "candidate": "MTTNoKnobUpgradeBacklog",
        "status": "NO_KNOB_UPGRADE_BACKLOG_BUILT_FROM_CORPUS_AND_REPOS",
        "input_status": input_data["status"],
        "source_status": status,
        "backlog_rows": rows,
        "priority_order": [row["id"] for row in rows if row["priority"] == "P0"]
        + [row["id"] for row in rows if row["priority"] != "P0"],
        "gate_results": {
            "corpus_and_repo_sources_harvested": True,
            "all_backlog_rows_have_sources": all(row["corpus_backed"] for row in rows),
            "p0_blockers_identified": True,
            "selected_sm_packet_still_open": True,
            "absolute_normalization_still_open": True,
            "actual_empirical_equivalence_still_open": True,
            "qa_su3_internal_reduced_packet_status_imported": True,
            "qa_su3_coupling_bridge_still_open": True,
            "no_knob_closure_claimed": False,
            "sm_parity_closure_claimed": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": "MTT_Actual_Selected_SM_Packet_and_Anomaly_Audit_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTNoKnobUpgradeBacklog",
        "status": "MTT_NO_KNOB_UPGRADE_BACKLOG_BUILT_FROM_CORPUS_AND_REPOS",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "corpus_backed_no_knob_backlog": True,
            "source_registry_for_upgrade_targets": True,
            "priority_order_for_closure": True,
            "open_gate_map": True,
        },
        "what_remains_open": {
            "actual_selected_SM_packet_and_anomaly_audit": True,
            "actual_Qa_SU3_color_operator_packet": True,
            "Qa_SU3_internal_reduced_logdet_to_coupling_bridge": True,
            "actual_QM_Born_record_formal_audit": True,
            "actual_local_QFT_functor_certificate": True,
            "actual_absolute_dimensionful_normalization": True,
            "actual_empirical_equivalence_run": True,
            "no_knob_constants": True,
            "sm_parity_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    rows = []
    for row in candidate["backlog_rows"]:
        sources = "\n".join(f"  - {path}" for path in row["supporting_sources"])
        missing = "\n".join(f"  - {path}" for path in row["missing_sources"]) or "  - none"
        rows.append(
            f"### {row['id']}: {row['target']}\n\n"
            f"- Priority: `{row['priority']}`\n"
            f"- Status: `{row['status']}`\n"
            f"- Current support: {row['current_support']}\n"
            f"- Upgrade needed: {row['upgrade_needed']}\n"
            f"- Supporting sources:\n{sources}\n"
            f"- Missing source paths:\n{missing}\n"
            f"- Closed now: `{row['closed_now']}`\n"
        )
    closes = "\n".join(f"- {name}" for name, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {name}" for name, value in certificate["what_remains_open"].items() if value)
    priority = "\n".join(f"- `{item}`" for item in candidate["priority_order"])
    return f"""# MTT No-Knob Upgrade Backlog v1

## Purpose

This artifact starts filling the no-knob upgrade backlog from the local corpus
and the adjacent proof repos.

It does not close no-knob constants.  It records where the corpus already gives
support, what the proof repos have certified, and which concrete gates remain
open before SM-parity or no-knob closure can be claimed.

## Priority Order

{priority}

## Backlog Rows

{chr(10).join(rows)}

## Backlog Theorem

The current corpus and proof repos supply enough structure to name the remaining
no-knob gates precisely.  The decisive open gates are the actual selected SM
packet, the Qa/SU3 color/operator packet, the formal Born/record audit, the
local QFT functor certificate, the absolute dimensionful normalization, and the
single empirical equivalence run.

This artifact closes the corpus-backed backlog, not the gates themselves.

## What This Closes

{closes}

## What Remains Open

{open_items}

## Next Artifact

```text
{candidate["next_required_artifact"]}
```
"""


def main() -> None:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    note_text = render_note(candidate, certificate)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note_text, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
