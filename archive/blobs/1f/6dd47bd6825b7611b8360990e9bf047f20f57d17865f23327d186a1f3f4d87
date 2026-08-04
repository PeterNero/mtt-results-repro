"""Build the inverse superset reconstruction artifact.

This artifact allows measured constants as discovery data only.  It is not a
forward no-knob proof; it is a disciplined inverse search program for finding
candidate selected source packets that may later be promoted into the forward
SM-parity/no-knob ledger.
"""

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

INPUT = DATA / "actual_selected_sm_packet_anomaly_audit.candidate.json"
OUTPUT_DATA = DATA / "inverse_superset_reconstruction.candidate.json"
OUTPUT_CERT = CERTS / "inverse_superset_reconstruction_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Inverse_Superset_Reconstruction_v1.md"


SOURCE_REGISTRY = {
    "selected_sm_packet_audit": [
        CORPUS / "MTT_Actual_Selected_SM_Packet_and_Anomaly_Audit_v1.md",
        CERTS / "actual_selected_sm_packet_anomaly_audit_certificate.json",
    ],
    "no_knob_backlog": [
        CORPUS / "MTT_No_Knob_Upgrade_Backlog_v1.md",
        CERTS / "no_knob_upgrade_backlog_certificate.json",
    ],
    "theta_program": [
        OBSIDIAN
        / "18 Theta-Closure & Execution Program"
        / "Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry.md",
        OBSIDIAN
        / "18 Theta-Closure & Execution Program"
        / "Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v2.md",
    ],
    "topology_and_string_sources": [
        OBSIDIAN
        / "13 Standard Model & Topology-Only Constraints"
        / "Topology__Only_Constraints_in_Modal_Triplet_Theory.md",
        OBSIDIAN
        / "16 Strings, Flux, & M-Theory Encodings"
        / "Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md",
    ],
    "q79_flavor_branch": [
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
    ],
    "nonsm_constants": [
        TEXPAPERS
        / "mtt-nonsm-constants-no-knob"
        / "certificates"
        / "nonsm_constants_status_matrix_certificate.json",
        TEXPAPERS / "mtt-nonsm-constants-no-knob" / "reports" / "verification_report.txt",
    ],
}


MEASURED_TARGETS = [
    {
        "id": "gauge_couplings",
        "targets": ["alpha_em", "sin2_theta_w", "alpha_s", "running_thresholds"],
        "allowed_use": "DISCOVERY_ONLY",
        "candidate_knobs": [
            "heat_kernel_spectrum",
            "threshold_packet",
            "U1_normalization",
            "SU2_SU3_embedding_index",
            "same_branch_period_selector",
        ],
        "promotion_test": "Recovered knobs must be discrete or corpus-selected before they can enter the forward ledger.",
    },
    {
        "id": "yukawa_masses_mixings",
        "targets": ["fermion_mass_ratios", "CKM", "PMNS", "CP_phase", "Higgs_yukawa_slots"],
        "allowed_use": "DISCOVERY_ONLY",
        "candidate_knobs": [
            "overlap_kernel_blocks",
            "typed_multiplication_maps",
            "family_holonomy_or_index",
            "q79_CP_branch",
            "Higgs_carrier_section",
        ],
        "promotion_test": "Recovered overlap data must be computable from the same selected source packet, not from benchmark flavor entries.",
    },
    {
        "id": "gravity_and_dimensionful_scales",
        "targets": ["G_N", "Planck_scale", "cosmological_normalization", "absolute_units"],
        "allowed_use": "DISCOVERY_ONLY",
        "candidate_knobs": [
            "internal_volume",
            "modal_gap",
            "G10_over_R1_cubed",
            "shared_circle_scale",
            "unit_dictionary_anchor",
        ],
        "promotion_test": "Recovered scale must match an independently selected normalization object.",
    },
    {
        "id": "qa_su3_color_operator_packet",
        "targets": ["color_embedding", "representation_packet", "anomaly_table", "operator_packet"],
        "allowed_use": "DISCOVERY_ONLY",
        "candidate_knobs": [
            "D_E_or_rho_E_operator",
            "typed_monad_maps",
            "Cech_Dolbeault_representatives",
            "section_ring_generators",
            "Freed_Witten_Bianchi_source",
        ],
        "promotion_test": "Recovered packet must instantiate the selected representation/anomaly table and pass the Qa/SU3 source gate.",
    },
]


RECONSTRUCTION_STAGES = [
    {
        "stage": "inverse_fit",
        "purpose": "Use observed constants to search the superset branch space.",
        "claim_allowed": "A branch or packet is compatible with observed data.",
        "claim_forbidden": "MTT predicts the constants from first principles.",
    },
    {
        "stage": "compression",
        "purpose": "Check whether fitted knobs collapse to a small discrete or algebraic packet.",
        "claim_allowed": "The inverse fit points to a compact candidate source.",
        "claim_forbidden": "A continuous free knob is promoted as selected data.",
    },
    {
        "stage": "corpus_alignment",
        "purpose": "Demand independent support from topology, theta, string/flux, q79, Qa/SU3, or non-SM artifacts.",
        "claim_allowed": "The candidate is corpus-aligned.",
        "claim_forbidden": "A numerically convenient packet is accepted without source evidence.",
    },
    {
        "stage": "forward_replay",
        "purpose": "Remove the measured constants as selectors and recompute forward from the candidate packet.",
        "claim_allowed": "The candidate graduates into a forward proof obligation.",
        "claim_forbidden": "The inverse fit itself closes SM-parity or no-knob closure.",
    },
]


GUARDRAILS = [
    "Measured constants may rank candidate branches but may not select final source data.",
    "Every fitted knob must be tagged as continuous, discrete, algebraic, or corpus-selected.",
    "Continuous fitted knobs remain parity inputs or discovery diagnostics unless independently selected.",
    "No observed masses, couplings, CKM, PMNS, or CP values may be used inside a no-knob proof step.",
    "Promotion requires forward replay with the measured targets removed from the selector set.",
    "A candidate that fits one sector must also survive cross-sector consistency checks.",
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


def build_candidate() -> dict[str, object]:
    input_data = load_input()
    return {
        "candidate": "MTTInverseSupersetReconstruction",
        "status": "INVERSE_SUPERSET_RECONSTRUCTION_PROTOCOL_BUILT_DISCOVERY_ONLY",
        "input_status": input_data["status"],
        "source_status": source_status(),
        "measured_targets": MEASURED_TARGETS,
        "reconstruction_stages": RECONSTRUCTION_STAGES,
        "guardrails": GUARDRAILS,
        "promotion_path_to_sm_parity": {
            "helps_sm_parity_closure": True,
            "mechanism": "Backfit results can propose the missing selected Qa/SU3 color/operator packet, representation table, threshold packet, or normalization object.",
            "required_conversion": "Any recovered knob must be independently selected or discretized, then replayed forward without measured constants as selectors.",
            "current_frontier_link": "MTT_Qa_SU3_Color_Operator_Packet_Source_Gate_v1",
        },
        "gate_results": {
            "inverse_reconstruction_protocol_built": True,
            "measured_constants_allowed_as_discovery_data": True,
            "measured_constants_allowed_as_forward_selectors": False,
            "promotion_tests_defined": True,
            "guardrails_defined": True,
            "sm_parity_help_path_defined": True,
            "actual_numeric_inverse_fit_run": False,
            "candidate_packet_promoted": False,
            "sm_parity_closure_claimed": False,
            "no_knob_closure_claimed": False,
        },
        "next_required_artifact": "MTT_Inverse_Superset_Search_Spec_v1",
        "target_fitting_used": True,
        "target_fitting_role": "DISCOVERY_ONLY",
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTInverseSupersetReconstruction",
        "status": "MTT_INVERSE_SUPERSET_RECONSTRUCTION_PROTOCOL_BUILT_DISCOVERY_ONLY",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "inverse_reconstruction_program_started": True,
            "measured_constants_discovery_policy": True,
            "promotion_path_into_SM_parity_gate": True,
            "guardrails_against_backfit_as_proof": True,
        },
        "what_remains_open": {
            "actual_numeric_inverse_fit_run": True,
            "superset_branch_search_space_implementation": True,
            "candidate_knob_compression_test": True,
            "corpus_alignment_score": True,
            "forward_replay_without_targets": True,
            "selected_Qa_SU3_color_operator_packet": True,
            "sm_parity_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": True,
        "target_fitting_role": "DISCOVERY_ONLY",
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    sources = "\n".join(
        f"- `{key}`: {len(body['present'])}/{len(body['paths'])} present"
        for key, body in candidate["source_status"].items()
    )
    targets = []
    for row in candidate["measured_targets"]:
        knobs = "\n".join(f"  - `{knob}`" for knob in row["candidate_knobs"])
        values = ", ".join(f"`{item}`" for item in row["targets"])
        targets.append(
            f"### {row['id']}\n\n"
            f"- Measured targets: {values}\n"
            f"- Allowed use: `{row['allowed_use']}`\n"
            f"- Candidate superset knobs:\n{knobs}\n"
            f"- Promotion test: {row['promotion_test']}\n"
        )
    stages = "\n".join(
        f"### {row['stage']}\n\n"
        f"- Purpose: {row['purpose']}\n"
        f"- Claim allowed: {row['claim_allowed']}\n"
        f"- Claim forbidden: {row['claim_forbidden']}\n"
        for row in candidate["reconstruction_stages"]
    )
    guardrails = "\n".join(f"- {item}" for item in candidate["guardrails"])
    closes = "\n".join(f"- {name}" for name, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {name}" for name, value in certificate["what_remains_open"].items() if value)
    return f"""# MTT Inverse Superset Reconstruction v1

## Purpose

This artifact starts the inverse reconstruction track.  It deliberately allows
observed constants as discovery data so the superset branch space can be
searched.  It does not allow those constants to become forward selectors, and
it does not claim no-knob prediction.

The point is practical: a successful inverse fit may reveal the missing
selected packet needed by the current SM-parity frontier.

## Source Registry

{sources}

## Measured Targets and Candidate Superset Knobs

{chr(10).join(targets)}

## Reconstruction Stages

{stages}

## Guardrails

{guardrails}

## Link Back to SM-Parity Closure

Backfitting can help SM-parity closure if it recovers a compact packet that
passes independent promotion tests.  In particular, it may propose the missing
`D_E` or `rho_E` operator packet, typed monad maps, section-ring generators,
period selector, or selected representation table required by:

```text
{candidate["promotion_path_to_sm_parity"]["current_frontier_link"]}
```

The recovered packet must then be replayed forward with the measured constants
removed from the selector set.

## Inverse Reconstruction Theorem

Measured constants may be used as boundary data for branch discovery.  A branch
found this way can become a serious candidate only if its fitted knobs compress
to a discrete, algebraic, or corpus-selected packet and survive forward replay
without target values as selectors.

Therefore this artifact opens a legitimate search path toward the selected
SM-packet gate, while preserving the distinction between inverse discovery,
SM-parity closure, and no-knob proof.

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
