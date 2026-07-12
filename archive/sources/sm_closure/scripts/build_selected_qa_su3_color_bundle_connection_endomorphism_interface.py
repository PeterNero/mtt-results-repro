"""Build the selected Qa/SU3 color-bundle connection/endomorphism interface."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

INPUT = DATA / "selected_qa_su3_operator_source_import_audit.candidate.json"
OUTPUT_DATA = DATA / "selected_qa_su3_color_bundle_connection_endomorphism_interface.candidate.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_color_bundle_connection_endomorphism_interface_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_Qa_SU3_Color_Bundle_Connection_Endomorphism_Interface_v1.md"

LOCAL_INPUTS = {
    "operator_packet_interface": NONSM / "certificates" / "selected_qa_su3_color_bundle_operator_packet_interface_certificate.json",
    "operator_packet_fill_attempt": NONSM / "certificates" / "selected_qa_su3_color_bundle_operator_packet_fill_attempt_certificate.json",
    "superset_route_map": NONSM / "certificates" / "selected_qa_su3_superset_source_route_map_certificate.json",
    "source_augmentation_fill_attempt": NONSM / "certificates" / "selected_qa_su3_source_augmentation_packet_fill_attempt_certificate.json",
    "repair_options_external_synthesis": NONSM / "certificates" / "selected_qa_su3_repair_options_external_synthesis_certificate.json",
    "visible_source_architecture": NONSM / "certificates" / "selected_qa_su3_visible_source_architecture_certificate.json",
    "visible_operator_source_attempt": NONSM / "certificates" / "selected_qa_su3_visible_operator_source_packet_attempt_certificate.json",
    "terminal_monad_lane_selector": NONSM / "certificates" / "selected_qa_su3_terminal_monad_lane_selector_attempt_certificate.json",
    "spectral_fallback_reduction": NONSM / "certificates" / "selected_qa_su3_spectral_fallback_reduction_certificate.json",
    "routec_source_solve_gate": NONSM / "certificates" / "selected_qa_su3_routec_source_solve_gate_certificate.json",
}

EXTERNAL_CLUES = [
    {
        "id": "iwasawa_geometry",
        "url": "https://arxiv.org/abs/1710.02180",
        "use": "Confirms Iwasawa is a nilmanifold quotient; section data must respect the nil lattice, not only torus intuition.",
        "import_as_proof": False,
    },
    {
        "id": "nil_theta_functions",
        "url": "https://www.ams.org/tran/2010-362-02/S0002-9947-09-04852-1/",
        "use": "Points to nil-theta/Heisenberg harmonic analysis as the right shape for ordinary Iwasawa section-ring data.",
        "import_as_proof": False,
    },
    {
        "id": "twisted_chan_paton_b_field",
        "url": "https://arxiv.org/abs/hep-th/9909089",
        "use": "Supports projective/twisted Chan-Paton bundles when a B-field or gerbe obstructs ordinary bundles.",
        "import_as_proof": False,
    },
    {
        "id": "gerbe_holonomy",
        "url": "https://arxiv.org/abs/hep-th/0204199",
        "use": "Supports Deligne/gerbe holonomy data as a concrete twisted-bundle source container.",
        "import_as_proof": False,
    },
]


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_status() -> dict[str, object]:
    return {
        key: {
            "path": str(path),
            "present": path.exists(),
        }
        for key, path in LOCAL_INPUTS.items()
    }


def build_interface() -> dict[str, object]:
    input_data = load_json(INPUT)
    local = {key: load_json(path) for key, path in LOCAL_INPUTS.items()}
    operator_fill = local["operator_packet_fill_attempt"]
    source_aug = local["source_augmentation_fill_attempt"]
    repair = local["repair_options_external_synthesis"]
    visible = local["visible_source_architecture"]
    spectral = local["spectral_fallback_reduction"]
    routec = local["routec_source_solve_gate"]
    return {
        "candidate": "MTTSelectedQaSU3ColorBundleConnectionEndomorphismInterface",
        "status": "MTT_SELECTED_QA_SU3_COLOR_BUNDLE_CONNECTION_ENDOMORPHISM_INTERFACE_BUILT_SOURCE_SELECTION_GATE_OPEN",
        "input_status": input_data["status"],
        "source_status": source_status(),
        "external_clues": EXTERNAL_CLUES,
        "imported_evidence": {
            "compact_nil_operator_packet_fill": {
                "status": operator_fill["status"],
                "domain_constraints_imported": operator_fill["fill_result"]["domain_constraints_imported"],
                "same_branch_source_found": operator_fill["fill_result"]["same_branch_qa_su3_source_found"],
                "determinant_computable_now": operator_fill["fill_result"]["determinant_computable_now"],
                "remaining_blockers": operator_fill["remaining_blockers"],
            },
            "iwasawa_source_augmentation": {
                "status": source_aug["status"],
                "source_certificate_filled": source_aug["fill_result"]["source_certificate_filled"],
                "section_ring_filled": source_aug["fill_result"]["section_ring_filled"],
                "operator_exit_available": source_aug["fill_result"]["operator_exit_available"],
                "local_frame_mismatch": source_aug["local_frame_mismatch"]["why_not_enough"],
            },
            "repair_synthesis": {
                "status": repair["status"],
                "best_solution_candidate": repair["verdict"]["best_solution_candidate"],
                "solution_found_at_typing_level": repair["verdict"]["solution_found_at_typing_level"],
                "full_packet_closed": repair["verdict"]["full_packet_closed"],
                "primary_next_route": repair["recommendation"]["primary_next_route"],
            },
            "visible_source_architecture": {
                "status": visible["status"],
                "recommended_construction": visible["recommended_construction"],
                "next_object": visible["next_object"],
            },
            "spectral_fallback": {
                "status": spectral["status"],
                "next_object": spectral["next_object"],
                "not_closed": spectral["not_closed"],
            },
            "routec_gate": {
                "status": routec["status"],
                "next_object": routec["next_object"],
                "minimal_new_data_that_would_close": routec["minimal_new_data_that_would_close"],
            },
        },
        "selected_interface": {
            "object_name": "Selected_Qa_SU3_Same_Source_Visible_Color_Operator_Packet",
            "source_payload_required": [
                "same-branch selected visible/color bundle, sheaf, twisted module, or gerbe module",
                "Freed-Witten, Green-Schwarz, Bianchi, and Chern-Weil row from that same source",
                "transition, rho_E, Cech/Dolbeault, or D_E data emitted by that source",
                "connection or HYM/Strominger residual with selected_source_verified true",
                "endomorphism_E or equivalent zero-order Weitzenbock/heat block",
                "Riesz projector, complement gap, reduced Green, dotD_alpha1, and projector retention",
                "finite determinant response: heat table, spectrum, analytic torsion, or Reidemeister torsion",
            ],
            "allowed_source_containers_ranked": [
                {
                    "rank": 1,
                    "id": "rank2_valpha_terminal_monad_plus_s3_gs_same_source",
                    "status": "PRIMARY_IF_SAME_SOURCE_BINDING_PROVED",
                    "why": "It has the strongest visible-bundle skeleton and already-closed S3/Green-Schwarz support, but it still needs Pic0 handling and transition/rho_E/D_E data.",
                },
                {
                    "rank": 2,
                    "id": "projective_gerbe_twisted_chan_paton_module",
                    "status": "PRIMARY_REPAIR_FOR_C_AXIS_OBSTRUCTION",
                    "why": "It solves the ordinary c-axis obstruction at typing level and can preserve twist cancellation into P, but still needs selected Deligne/Cech or B-field data and a determinant.",
                },
                {
                    "rank": 3,
                    "id": "direct_selected_hym_routec_or_spectral_galerkin_operator",
                    "status": "EXECUTION_ENGINE_AFTER_SOURCE_SELECTION",
                    "why": "Validators and finite Galerkin protocol exist, but lifted smoke flags cannot replace selected source verification.",
                },
                {
                    "rank": 4,
                    "id": "ordinary_full_nil_theta_section_ring",
                    "status": "CONDITIONALLY_RETIRED_UNLESS_C_SOURCE_AMENDED",
                    "why": "Ordinary line-bundle sections need a closed nil representative or full nil-theta data; current source does not supply it.",
                },
            ],
            "forbidden_moves": [
                "fill endomorphism_E from the observed Qa/SU3 residual",
                "promote abstract HYM/Strominger existence to a numerical operator matrix",
                "reuse local FP/BRST quotient determinants as an extra correction",
                "use q79 charge-sector or S3 support as a direct Qa/SU3 determinant source",
                "use lifted selected_source_verified smoke flags as proof",
            ],
        },
        "decision": {
            "result": "A source-selection interface is now built; no color operator packet is promoted.",
            "way_forward": "Build the same-source visible/color operator packet, with the gerbe/twisted-module repair and spectral Galerkin engine treated as complementary lanes.",
            "first_executable_artifact": "MTT_Selected_Qa_SU3_Same_Source_Visible_Color_Operator_Packet_v1",
        },
        "gate_results": {
            "interface_built": True,
            "local_cross_repo_evidence_imported": True,
            "external_clues_recorded_as_templates_only": True,
            "primary_same_source_gate_identified": True,
            "gerbe_repair_kept_live": True,
            "spectral_galerkin_kept_as_execution_engine": True,
            "operator_packet_promoted": False,
            "selected_Qa_SU3_packet_closed": False,
            "sm_parity_closure_claimed": False,
            "no_knob_closure_claimed": False,
        },
        "next_required_artifact": "MTT_Selected_Qa_SU3_Same_Source_Visible_Color_Operator_Packet_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSelectedQaSU3ColorBundleConnectionEndomorphismInterface",
        "status": "MTT_SELECTED_QA_SU3_COLOR_BUNDLE_CONNECTION_ENDOMORPHISM_INTERFACE_BUILT_SOURCE_SELECTION_GATE_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "color_bundle_connection_endomorphism_interface": True,
            "cross_repo_operator_attempts_imported": True,
            "same_source_payload_contract": True,
            "gerbe_repair_and_spectral_engine_positioned": True,
            "forbidden_shortcuts_recorded": True,
        },
        "what_remains_open": {
            "same_source_visible_color_bundle_or_twisted_module": True,
            "Pic0_selection_or_physical_quotient": True,
            "Freed_Witten_GS_Bianchi_Chern_Weil_same_source_row": True,
            "transition_rhoE_Cech_Dolbeault_or_DE_packet": True,
            "selected_connection_or_HYM_Strominger_residual": True,
            "endomorphism_E_or_heat_zero_order_block": True,
            "finite_spectrum_heat_or_torsion_response": True,
            "selected_Qa_SU3_color_operator_packet": True,
            "sm_parity_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    sources = "\n".join(
        f"- `{key}`: {body['path']} ({'present' if body['present'] else 'missing'})"
        for key, body in candidate["source_status"].items()
    )
    clues = "\n".join(
        f"- `{row['id']}`: {row['use']} Source: {row['url']}"
        for row in candidate["external_clues"]
    )
    ranked = "\n".join(
        f"- {row['rank']}. `{row['id']}`: `{row['status']}`. {row['why']}"
        for row in candidate["selected_interface"]["allowed_source_containers_ranked"]
    )
    payload = "\n".join(f"- {item}" for item in candidate["selected_interface"]["source_payload_required"])
    forbidden = "\n".join(f"- {item}" for item in candidate["selected_interface"]["forbidden_moves"])
    closes = "\n".join(f"- {name}" for name, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {name}" for name, value in certificate["what_remains_open"].items() if value)
    imported = candidate["imported_evidence"]
    return f"""# MTT Selected Qa/SU3 Color-Bundle Connection/Endomorphism Interface v1

## Purpose

This artifact turns the previous operator-source import audit into an executable
source-selection contract.  The goal is not to add a small correction to the
compact-Nil determinant.  The goal is to identify the exact same-source packet
that can emit the SU3 color bundle, connection, endomorphism, quotient domain,
and finite determinant response before any Qa/SU3 target comparison.

## Local Cross-Repo Inputs

{sources}

## External Clues

These references are templates only. They are not imported as MTT proof data.

{clues}

## Imported Evidence Summary

- Compact-Nil packet fill: `{imported["compact_nil_operator_packet_fill"]["status"]}`
- Same-branch source found there: `{imported["compact_nil_operator_packet_fill"]["same_branch_source_found"]}`
- Iwasawa source augmentation: `{imported["iwasawa_source_augmentation"]["status"]}`
- Gerbe repair synthesis: `{imported["repair_synthesis"]["status"]}`
- Visible source architecture: `{imported["visible_source_architecture"]["status"]}`
- Spectral fallback: `{imported["spectral_fallback"]["status"]}`
- Route C source gate: `{imported["routec_gate"]["status"]}`

## Same-Source Payload Contract

The next artifact must supply:

{payload}

## Ranked Source Containers

{ranked}

## Forbidden Moves

{forbidden}

## Decision

{candidate["decision"]["result"]}

Way forward: {candidate["decision"]["way_forward"]}

First executable artifact:

```text
{candidate["decision"]["first_executable_artifact"]}
```

## Theorem

The selected Qa/SU3 color/operator packet cannot be closed by another local
quotient determinant, by the q79 charge sector alone, or by a target-sized
endomorphism entry.  It can be promoted only when one same-source visible/color
container emits the required transition/operator data and finite determinant
response.

The most credible construction is a merge of the rank-2 V_alpha terminal-monad
lane with the S3/Green-Schwarz visible support, using the direct HYM/Route-C or
spectral Galerkin machinery as the execution engine.  The gerbe/twisted
Chan-Paton route stays live because it is the cleanest repair of the c-axis
ordinary-line-bundle obstruction.

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
    candidate = build_interface()
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
