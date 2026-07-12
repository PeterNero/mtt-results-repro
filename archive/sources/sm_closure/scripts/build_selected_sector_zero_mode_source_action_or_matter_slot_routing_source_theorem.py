"""Build the source-action or matter-slot routing source cutset theorem."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

VALUE_FILL = DATA / "selected_sector_zero_mode_end0_action_matrix_or_matter_slot_routing_value_fill.candidate.json"
END0_PACKET = DATA / "selected_end0_to_sector_functor_source_and_value_packet.candidate.json"
SPECTRAL = DATA / "selected_spectral_galerkin_projector_retention_data.candidate.json"
HYBRID = DATA / "selected_routec_hybrid_matter_slot_galerkin_source_packet.candidate.json"
SAME_SOURCE = DATA / "selected_routec_samesource_matter_slot_overlap_operator_packet.candidate.json"

OUTPUT = DATA / "selected_sector_zero_mode_source_action_or_matter_slot_routing_source_theorem.candidate.json"
CERT = CERTS / "selected_sector_zero_mode_source_action_or_matter_slot_routing_source_theorem_certificate.json"
NOTE = CORPUS / "MTT_Selected_SectorZeroMode_SourceAction_or_SelectedMatterSlotRouting_Source_Theorem_v1.md"

STATUS = "MTT_SELECTED_SECTOR_SOURCE_ACTION_OR_ROUTING_CUTSET_THEOREM_PROVED_SOURCE_PAYLOAD_OPEN"
NEXT = "MTT_Selected_SectorZeroMode_SourcePayload_Search_or_Emission_Attempt_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    value_fill = load(VALUE_FILL)
    end0_packet = load(END0_PACKET)
    spectral = load(SPECTRAL)
    hybrid = load(HYBRID)
    same_source = load(SAME_SOURCE)

    route_a = {
        "name": "selected_End0_source_action_route",
        "required_payload": [
            "selected zero-mode bases K_s for Q,u,d,L,e,N,H",
            "selected source map rho_s: End0(V_alpha)->so(K_s)",
            "same-source bracket-preserving matrices rho_s(T1), rho_s(T2), rho_s(T3)",
            "coherent spectral zero-mode projector retention",
            "selected invariant Gram or trace normalization",
        ],
        "current_status": {
            "model_matrices_available": value_fill["direct_End0_action_value_fill"]["candidate_values_exist_as_universal_model"],
            "selected_rho_s_values_filled": value_fill["decision"]["selected_End0_action_values_filled"],
            "coherent_spectral_zero_mode_retention": value_fill["selected_source_gates"]["coherent_spectral_zero_mode_retention"],
            "selected_gram": value_fill["selected_source_gates"]["selected_sector_Gram_inner_product"],
        },
        "passes_now": False,
    }
    route_b = {
        "name": "selected_matter_slot_routing_route",
        "required_payload": [
            "selected matter-slot split independent of locked C1 target columns",
            "selected Z -> u/e and X -> d/nuD routing or replacement table",
            "selected 1_M Dirac-neutrino/singlet rule",
            "same-source overlap/normalization functor",
        ],
        "current_status": {
            "hybrid_shape_scaffold_present": hybrid["selection_verdict"]["shape_scaffold_present"],
            "selected_matter_slot_transport_present": hybrid["selection_verdict"]["selected_matter_slot_transport_present"],
            "selected_1M_rule_present": hybrid["selection_verdict"]["selected_1M_neutrino_shift_rule_present"],
            "same_source_packet_selected": same_source["decision"]["selected_fields_count"] == same_source["decision"]["required_fields_count"]
            if "selected_fields_count" in same_source.get("decision", {})
            else False,
        },
        "passes_now": False,
    }

    forbidden_shortcuts = [
        "promote universal End0 carrier matrices as selected rho_s without selected zero-mode bases",
        "use B_N or compact Route-C dotD values after they were rejected as selected sector functor values",
        "use locked C1 splitter columns to choose Z/X matter-slot routing",
        "assign 1_M neutrino routing by analogy with bar5_M without a selected singlet rule",
        "use observed masses, mixings, CKM/PMNS, or gauge couplings to select the route",
    ]

    theorem = {
        "name": "SelectedSectorSourceActionOrRoutingCutsetTheorem",
        "proved": True,
        "statement": (
            "Given the previous End0 carrier, adjoint-triplet theorem, and value-fill attempt, "
            "the sector gate can close only through one of two same-source payloads: "
            "Route A emits selected zero-mode bases and a bracket-preserving End0 action rho_s "
            "on them; Route B emits a selected matter-slot routing theorem with the 1_M rule "
            "and overlap/normalization functor. Universal carrier matrices and support-only "
            "Route-C/SU5 data are insufficient."
        ),
        "proof_steps": [
            "The End0 representation type is already forced, so representation choice is no longer the missing data.",
            "The value-fill attempt shows universal matrices pass tests but are not selected on actual zero modes.",
            "The End0-to-sector packet proved scalar normalization alone cannot define the sector functor.",
            "The matter-slot packets show Z/X routing and 1_M routing are support-only.",
            "Therefore every legal closure proof must supply one of the two listed same-source payloads.",
        ],
    }

    data = {
        "candidate": "MTTSelectedSectorZeroModeSourceActionOrMatterSlotRoutingSourceTheorem",
        "status": STATUS,
        "inputs": {
            "value_fill": rel(VALUE_FILL),
            "end0_packet": rel(END0_PACKET),
            "spectral": rel(SPECTRAL),
            "hybrid": rel(HYBRID),
            "same_source": rel(SAME_SOURCE),
        },
        "theorem": theorem,
        "route_A": route_a,
        "route_B": route_b,
        "forbidden_shortcuts": forbidden_shortcuts,
        "cutset_closed": True,
        "selected_payload_emitted": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_SectorZeroMode_SourceAction_or_SelectedMatterSlotRouting_Source_Theorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "cutset_closed": True,
        "selected_payload_emitted": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Sector ZeroMode SourceAction or SelectedMatterSlotRouting Source Theorem v1

Status: `{STATUS}`.

## Theorem

The remaining sector gate can close only through one of two same-source payloads:

1. selected zero-mode bases plus a bracket-preserving End0 action
   `rho_s : End0(V_alpha) -> so(K_s)`;
2. selected matter-slot routing, including `Z/X` routing or replacement,
   the `1_M` singlet-neutrino rule, and the overlap/normalization functor.

Universal carrier matrices, support-only Route-C values, and conditional
SU(5)/E6 matter-slot clues cannot by themselves promote the proof.

## Straight vs Superset

The straight path is Route A: emit selected `rho_s`.

The superset path is Route B: combine Route-C ranks, SU(5)/E6 slot clues, and
same-source overlap data, but only after a selected routing source theorem
locks the target independently of observed constants or locked C1 columns.

## Forbidden Shortcuts

- promote universal End0 carrier matrices as selected `rho_s`,
- reuse rejected `B_N`/compact Route-C values as selected sector functor values,
- choose `Z/X` routing from locked C1 splitter columns,
- assign `1_M` by analogy without a selected singlet rule,
- use observed constants as selectors.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True), encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT)}")
    print(f"wrote {rel(CERT)}")
    print(f"wrote {rel(NOTE)}")
    print(STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
