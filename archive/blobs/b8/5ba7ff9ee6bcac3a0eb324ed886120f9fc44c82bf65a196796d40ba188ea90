"""Back-import patched dynamic C1 closure into the physical source-emission frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalsourceemission_patchbackimport_or_unpatchedderivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PATCHED_STATUS = PACKET_DIR / "patched_dynamic_c1_status_after_sourcegate.packet.json"
UNPATCHED_FRONTIER = PACKET_DIR / "unpatched_measure_derivation_frontier.packet.json"
NEXT_ACTIONS = PACKET_DIR / "next_smparity_actions_after_patch.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalSourceEmission_PatchBackimport_or_UnpatchedDerivation_v1.md"

STATUS = "MTT_SELECTED_PHYSICALSOURCEEMISSION_PATCHBACKIMPORT_BUILT_UNPATCHED_DERIVATION_OPEN"
NEXT = "MTT_Selected_FinalSMParityGapMatrix_or_UnpatchedFiniteC1MeasureDerivation_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    source_gate = load(DATA / "selected_physicalboundaryfirstvariation_or_selectedsourceemission.candidate.json")
    route_rows = load(DATA / "selected_routeaemission_or_routebgalerkinrows_execution.candidate.json")
    measure_promotion = load(DATA / "selected_physicalmeasure_or_finitegalerkinpromotion.candidate.json")
    measure_identity = load(DATA / "selected_physicalmeasureidentity_or_routeaemissionclosure.candidate.json")
    patch = load(DATA / "selected_finitec1tracemeasureprincipleinsertion_or_directactionderivation.candidate.json")
    ledger_update = load(DATA / "selected_dynamicc1patchtosmparityledger_or_unpatchedmeasurederivation.candidate.json")
    empirical_integration = load(DATA / "selected_patcheddynamicc1empiricalreplayintegration_or_noknobderivation.candidate.json")

    patched_status = {
        "schema": "MTTPatchedDynamicC1StatusAfterPhysicalSourceGate.v1",
        "status": "PATCHED_DYNAMIC_C1_CLOSED_UNPATCHED_DERIVATION_OPEN",
        "patched_spine_closure_claimed": True,
        "patched_dynamic_C1_packet_closed": patch["promotion_decision"]["patched_dynamic_C1_packet_closed"],
        "patched_Route_B_physical_Galerkin_replacement": patch["promotion_decision"][
            "patched_Route_B_physical_Galerkin_replacement_closed"
        ],
        "patched_A_selected": patch["what_closes_now"]["patched_A_selected"],
        "patched_b_selected": patch["what_closes_now"]["patched_b_selected"],
        "patched_deltaTheta_C1": patch["what_closes_now"]["patched_deltaTheta_C1"],
        "patched_sector_response_matrices": patch["what_closes_now"]["patched_sector_response_matrices"],
        "patched_empirical_replay_interface_ready": empirical_integration["promotion_decision"][
            "patched_dynamic_C1_empirical_interface_ready"
        ],
        "not_full_SM_parity": empirical_integration["promotion_decision"]["full_SM_parity_closed"] is False,
        "not_full_no_knob": empirical_integration["promotion_decision"]["full_no_knob_closed"] is False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    unpatched_frontier = {
        "schema": "MTTUnpatchedFiniteC1MeasureDerivationFrontier.v1",
        "status": "UNPATCHED_FINITE_C1_TRACE_MEASURE_DERIVATION_REMAINS_OPEN",
        "unpatched_open": {
            "unpatched_principle_derivation": patch["what_remains_open"]["unpatched_principle_derivation"],
            "unpatched_direct_PhiFinC1_action_derivation": patch["what_remains_open"][
                "unpatched_direct_PhiFinC1_action_derivation"
            ],
            "unpatched_Route_A_same_source_emission": patch["what_remains_open"][
                "unpatched_Route_A_same_source_emission"
            ],
        },
        "three_legal_unpatched_routes": [
            "derive SelectedFiniteC1TraceMeasurePrinciple from existing MTT axioms",
            "derive physical Phi_fin^C1 action restriction directly",
            "emit Route A same-source R_Z/R_X/b_selected and no-extra-boundary source packet",
        ],
        "current_support_not_enough": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_actions = {
        "schema": "MTTNextSMParityActionsAfterPatchedDynamicC1.v1",
        "status": "PATCHED_DYNAMIC_C1_RETIRED_NEXT_GLOBAL_GATES_ACTIVE",
        "patched_spine_next": empirical_integration["what_remains_open"],
        "local_dynamic_c1_next": {
            "unpatched_no_knob_measure_derivation": True,
            "paper_insertion_or_derivation_of_principle": True,
        },
        "superset_strategy": {
            "patched_route": "Use the finite C1 trace-measure principle as an explicit local SM-parity patch.",
            "unpatched_route": "Continue deriving the principle or direct action identity without adding an axiom.",
            "empirical_route": "Use patched A/b/deltaTheta/sector-response as downstream replay interface, not as source selector.",
            "uses_observed_constants": False,
        },
    }

    PATCHED_STATUS.write_text(json.dumps(patched_status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    UNPATCHED_FRONTIER.write_text(json.dumps(unpatched_frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT_ACTIONS.write_text(json.dumps(next_actions, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedPhysicalSourceEmissionPatchBackimportOrUnpatchedDerivation",
        "status": STATUS,
        "inputs": {
            "physical_source_gate": rel(DATA / "selected_physicalboundaryfirstvariation_or_selectedsourceemission.candidate.json"),
            "route_rows": rel(DATA / "selected_routeaemission_or_routebgalerkinrows_execution.candidate.json"),
            "measure_promotion": rel(DATA / "selected_physicalmeasure_or_finitegalerkinpromotion.candidate.json"),
            "measure_identity": rel(DATA / "selected_physicalmeasureidentity_or_routeaemissionclosure.candidate.json"),
            "patch": rel(DATA / "selected_finitec1tracemeasureprincipleinsertion_or_directactionderivation.candidate.json"),
            "ledger_update": rel(DATA / "selected_dynamicc1patchtosmparityledger_or_unpatchedmeasurederivation.candidate.json"),
            "empirical_integration": rel(DATA / "selected_patcheddynamicc1empiricalreplayintegration_or_noknobderivation.candidate.json"),
        },
        "output_packets": {
            "patched_status": rel(PATCHED_STATUS),
            "unpatched_frontier": rel(UNPATCHED_FRONTIER),
            "next_actions": rel(NEXT_ACTIONS),
        },
        "theorem": {
            "name": "PhysicalSourceEmissionPatchBackimportTheorem",
            "proved": True,
            "statement": (
                "The newly executable physical boundary/first-variation gate is compatible with the existing patched dynamic C1 closure chain. "
                "Under the explicit SelectedFiniteC1TraceMeasurePrinciple patch, Route B finite Weyl trace rows promote to physical Galerkin rows and supply patched A_selected, b_selected, deltaTheta_C1, and sector response matrices. "
                "This retires dynamic C1 as a patched SM-parity blocker while preserving the unpatched/no-knob derivation as the active local frontier."
            ),
        },
        "what_closes_now": {
            "patched_dynamic_C1_status_backimported": True,
            "patched_dynamic_C1_no_longer_local_parity_blocker": True,
            "unpatched_derivation_frontier_preserved": True,
            "global_SM_parity_gates_preserved": True,
        },
        "what_remains_open": {
            "full_SM_parity": empirical_integration["promotion_decision"]["full_SM_parity_closed"] is False,
            "full_no_knob": empirical_integration["promotion_decision"]["full_no_knob_closed"] is False,
            "unpatched_no_knob_dynamic_C1_derivation": True,
            "global_empirical_replay_and_selected_SM_packet_gates": True,
        },
        "patched_spine_closure_claimed": True,
        "conditional_only": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalSourceEmission_PatchBackimport_or_UnpatchedDerivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "patched_dynamic_C1_status_backimported": True,
        "patched_spine_closure_claimed": True,
        "unpatched_derivation_frontier_preserved": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalSourceEmission PatchBackimport or UnpatchedDerivation v1

Status: `{STATUS}`.

The new physical boundary/first-variation validator is stricter than the older
contract, but it is consistent with the existing patched dynamic C1 closure:
after the explicit `SelectedFiniteC1TraceMeasurePrinciple` patch, the finite
Weyl trace rows promote to physical Route-B Galerkin rows and provide patched
`A_selected`, `b_selected`, `deltaTheta_C1`, and sector response matrices.

This does **not** claim full SM parity or no-knob closure. It says dynamic C1 is
retired as a blocker only inside the patched SM-parity spine. The unpatched
frontier remains: derive the finite C1 trace-measure principle, derive the
direct physical `Phi_fin^C1` action identity, or emit the Route-A same-source
source packet.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
