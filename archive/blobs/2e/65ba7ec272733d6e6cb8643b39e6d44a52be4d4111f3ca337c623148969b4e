"""Build the actual selected SM packet and anomaly audit artifact."""

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

INPUT = DATA / "no_knob_upgrade_backlog.candidate.json"
OUTPUT_DATA = DATA / "actual_selected_sm_packet_anomaly_audit.candidate.json"
OUTPUT_CERT = CERTS / "actual_selected_sm_packet_anomaly_audit_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Actual_Selected_SM_Packet_and_Anomaly_Audit_v1.md"


SOURCES = {
    "topology_only": OBSIDIAN
    / "13 Standard Model & Topology-Only Constraints"
    / "Topology__Only_Constraints_in_Modal_Triplet_Theory.md",
    "central_circle": OBSIDIAN
    / "13 Standard Model & Topology-Only Constraints"
    / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md",
    "heterotic_flux": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md",
    "m_theory": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_M_theory.md",
    "qa_su3_dependency": TEXPAPERS
    / "mtt-qa-su3-packet-proof"
    / "certificates"
    / "full_corpus_dependency_audit_certificate.json",
    "qa_su3_dependency_note": TEXPAPERS
    / "mtt-qa-su3-packet-proof"
    / "proof_corpus"
    / "Selected_Qa_SU3_Full_Corpus_Dependency_Audit_v1.md",
    "nonsm_qa_su3_monad_interface": TEXPAPERS
    / "mtt-nonsm-constants-no-knob"
    / "proof_corpus"
    / "Selected_Qa_SU3_Typed_Monad_DE_or_RhoE_Data_Interface_v1.md",
    "nonsm_qa_su3_monad_fill": TEXPAPERS
    / "mtt-nonsm-constants-no-knob"
    / "proof_corpus"
    / "Selected_Qa_SU3_Typed_Monad_Data_Fill_Attempt_v1.md",
}

PACKET_COMPONENTS = [
    {
        "id": "gauge_carrier_su3_su2_u1",
        "component": "SM gauge carrier SU3 x SU2 x U1",
        "corpus_status": "STRUCTURAL_SUPPORT_PRESENT",
        "evidence": [
            "Topology-only constraints corpus states exact SM hypercharges and anomaly cancellation from triplet line-bundle difference charges.",
            "Theta/gauge and Qa/SU3 repos provide sector-specific gauge packet scaffolds.",
        ],
        "required_selected_data": "A single selected gauge-carrier packet with maps to SU3, SU2, and U1 carriers and convention-normalized embeddings.",
        "closed_for_sm_parity_interface": True,
        "closed_as_actual_selected_no_knob_packet": False,
    },
    {
        "id": "fermion_representation_packet",
        "component": "chiral fermion representation content",
        "corpus_status": "STRUCTURAL_SUPPORT_PRESENT",
        "evidence": [
            "Topology-only corpus gives line-bundle and charge rules for hypercharge, Dirac/Majorana criteria, and local gauge/gravity anomaly cancellation.",
            "String/flux corpus supports chiral zero-mode and index-theoretic representation mechanisms.",
        ],
        "required_selected_data": "Explicit selected representation table with chiralities, conjugates, hypercharges, color/weak reps, and source maps.",
        "closed_for_sm_parity_interface": True,
        "closed_as_actual_selected_no_knob_packet": False,
    },
    {
        "id": "three_family_selector",
        "component": "three-family index or central-circle/holonomy selector",
        "corpus_status": "STRUCTURAL_SUPPORT_PRESENT",
        "evidence": [
            "Topology-only and central-circle corpus discuss family multiplicity from Dirac index or Z3 holonomy.",
            "M-theory/string corpus points to topological integers and internal Dirac zero modes.",
        ],
        "required_selected_data": "Actual selected index/holonomy computation tied to the same SM packet branch.",
        "closed_for_sm_parity_interface": True,
        "closed_as_actual_selected_no_knob_packet": False,
    },
    {
        "id": "higgs_carrier_and_yukawa_slots",
        "component": "Higgs carrier plus Yukawa-admitting trilinear slots",
        "corpus_status": "STRUCTURAL_SUPPORT_PRESENT",
        "evidence": [
            "Topology-only corpus records trilinear line-bundle conditions and Yukawa allowances.",
            "Central-circle and string/flux corpus identify Yukawas as overlap integrals with Higgs/coherent modes.",
        ],
        "required_selected_data": "Selected Higgs representation/carrier, trilinear map, and overlap-domain convention.",
        "closed_for_sm_parity_interface": True,
        "closed_as_actual_selected_no_knob_packet": False,
    },
    {
        "id": "anomaly_cancellation_certificate",
        "component": "local, mixed, gravitational, and SU2 global anomaly checks",
        "corpus_status": "STRUCTURAL_SUPPORT_STRONG",
        "evidence": [
            "Topology-only paper claims full cancellation of local gauge/gravitational anomalies and absence of the SU2 Witten anomaly for three families.",
            "Heterotic flux corpus equates FCC with componentwise anomaly/primitivity/quantization constraints in worked examples.",
        ],
        "required_selected_data": "Machine-checkable anomaly table evaluated on the selected representation packet, not only a generic corpus theorem.",
        "closed_for_sm_parity_interface": True,
        "closed_as_actual_selected_no_knob_packet": False,
    },
    {
        "id": "qa_su3_color_operator_packet",
        "component": "Qa/SU3 color/operator packet",
        "corpus_status": "OPEN_CRITICAL_BLOCKER",
        "evidence": [
            "Qa/SU3 full corpus dependency audit closes assumption checking and rejects unsafe shortcuts.",
            "The same certificate leaves selected D_E/rho_E operator packet, typed monad/Cech-Dolbeault maps, same-branch period selector, and Freed-Witten/Bianchi mapped source open.",
        ],
        "required_selected_data": "Typed monad or section-ring source with selected operator maps, period/finite quotient selector, and mapped Bianchi/Freed-Witten certificate.",
        "closed_for_sm_parity_interface": False,
        "closed_as_actual_selected_no_knob_packet": False,
    },
]

ANOMALY_TESTS = [
    "List the selected representation packet before evaluating anomalies.",
    "Evaluate cubic nonabelian, mixed gauge-U1, U1 cubic, mixed gravitational-U1, and SU2 global anomaly checks.",
    "Record whether each cancellation is inherited from topology-only theorem or recomputed on the selected packet.",
    "Reject generic anomaly cancellation if the actual representation packet is not listed.",
    "Reject Qa/SU3 closure if selected D_E/rho_E operator data or typed monad maps are absent.",
]

UNSAFE_SHORTCUTS_REJECTED = [
    "Do not use observed SM couplings, masses, or CKM data to choose the packet.",
    "Do not import q79 CP success as a direct Qa/SU3 color proof.",
    "Do not count generic topology-only anomaly cancellation as the actual selected packet unless the representation table is instantiated.",
    "Do not count identity rho_E, diagnostic validators, or benchmark matrices as selected operator data.",
]


def read_json_if_present(path: Path) -> dict[str, object] | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def load_input() -> dict[str, object]:
    return json.loads(INPUT.read_text(encoding="utf-8"))


def source_presence() -> dict[str, object]:
    return {
        key: {
            "path": str(path),
            "present": path.exists(),
        }
        for key, path in SOURCES.items()
    }


def build_candidate() -> dict[str, object]:
    input_data = load_input()
    qa_cert = read_json_if_present(SOURCES["qa_su3_dependency"])
    return {
        "candidate": "MTTActualSelectedSMPacketAndAnomalyAudit",
        "status": "ACTUAL_SELECTED_SM_PACKET_AUDIT_BUILT_PACKET_STILL_OPEN",
        "input_status": input_data["status"],
        "source_presence": source_presence(),
        "qa_su3_dependency_status": qa_cert["status"] if qa_cert else "MISSING",
        "qa_su3_what_remains_open": qa_cert.get("what_remains_open", {}) if qa_cert else {},
        "packet_components": PACKET_COMPONENTS,
        "anomaly_tests": ANOMALY_TESTS,
        "unsafe_shortcuts_rejected": UNSAFE_SHORTCUTS_REJECTED,
        "gate_results": {
            "topology_only_sm_structure_supported": True,
            "anomaly_structure_supported": True,
            "actual_selected_representation_packet_supplied": False,
            "actual_anomaly_table_computed_on_selected_packet": False,
            "qa_su3_operator_packet_supplied": False,
            "typed_monad_or_section_ring_values_supplied": False,
            "selected_sm_packet_closed": False,
            "sm_parity_closure_claimed": False,
            "no_knob_closure_claimed": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": "MTT_Qa_SU3_Color_Operator_Packet_Source_Gate_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTActualSelectedSMPacketAndAnomalyAudit",
        "status": "MTT_ACTUAL_SELECTED_SM_PACKET_AUDIT_BUILT_PACKET_STILL_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "corpus_support_for_SM_structure_audited": True,
            "anomaly_requirements_listed": True,
            "selected_packet_missing_data_identified": True,
            "qa_su3_operator_packet_blocker_identified": True,
            "unsafe_shortcuts_rejected": True,
        },
        "what_remains_open": {
            "actual_selected_representation_packet": True,
            "actual_anomaly_table_on_selected_packet": True,
            "actual_Qa_SU3_color_operator_packet": True,
            "typed_monad_or_section_ring_values": True,
            "same_branch_period_or_finite_quotient_selector": True,
            "Freed_Witten_Bianchi_for_mapped_source": True,
            "selected_sm_packet_closed": False,
            "sm_parity_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    components = []
    for row in candidate["packet_components"]:
        evidence = "\n".join(f"  - {item}" for item in row["evidence"])
        components.append(
            f"### {row['id']}: {row['component']}\n\n"
            f"- Corpus status: `{row['corpus_status']}`\n"
            f"- Evidence:\n{evidence}\n"
            f"- Required selected data: {row['required_selected_data']}\n"
            f"- Closed for SM-parity interface: `{row['closed_for_sm_parity_interface']}`\n"
            f"- Closed as actual selected no-knob packet: `{row['closed_as_actual_selected_no_knob_packet']}`\n"
        )
    tests = "\n".join(f"- {item}" for item in candidate["anomaly_tests"])
    shortcuts = "\n".join(f"- {item}" for item in candidate["unsafe_shortcuts_rejected"])
    sources = "\n".join(
        f"- `{key}`: {body['path']} ({'present' if body['present'] else 'missing'})"
        for key, body in candidate["source_presence"].items()
    )
    closes = "\n".join(f"- {name}" for name, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {name}" for name, value in certificate["what_remains_open"].items() if value)
    return f"""# MTT Actual Selected SM Packet and Anomaly Audit v1

## Purpose

This artifact audits the selected Standard Model packet gate using the local
corpus and adjacent proof repos.

The result is deliberately split: the corpus strongly supports SM-like
topology, hypercharge, anomaly, family, Higgs, and Yukawa structure, but the
actual selected packet is not yet closed because the selected representation
table and Qa/SU3 color/operator packet are still missing.

## Source Registry

{sources}

## Packet Components

{chr(10).join(components)}

## Required Anomaly Tests

{tests}

## Unsafe Shortcuts Rejected

{shortcuts}

## Audit Theorem

The current corpus is sufficient to support the SM-packet program structurally,
but not sufficient to close the actual selected SM packet.  Closure requires an
instantiated selected representation table, anomaly table evaluated on that
packet, and a selected Qa/SU3 color/operator packet via typed monad,
Cech-Dolbeault, section-ring, or equivalent source data.

Therefore this artifact closes the audit of what is missing, not the selected
packet itself.

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
