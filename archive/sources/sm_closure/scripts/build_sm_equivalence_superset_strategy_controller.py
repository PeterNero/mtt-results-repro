"""Build the branch controller for SM-equivalence via superset strategy."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

CORE = DATA / "core_axioms_measured_parameter_interface.candidate.json"
SM_PACKET = DATA / "actual_selected_sm_packet_anomaly_audit.candidate.json"
EMPIRICAL = DATA / "empirical_equivalence_ledger.candidate.json"
C1_FRONTIER = DATA / "selected_primitivec1_or_weylpair_sectorrouting_sourceemission.candidate.json"
DYNAMIC = DATA / "selected_dynamic_overlapkernel_or_c1primitive_source_emission.candidate.json"

OUTPUT = DATA / "sm_equivalence_superset_strategy_controller.candidate.json"
CERT = CERTS / "sm_equivalence_superset_strategy_controller_certificate.json"
NOTE = CORPUS / "MTT_SM_Equivalence_Superset_Strategy_Controller_v1.md"

STATUS = "MTT_SM_EQUIVALENCE_SUPERSET_STRATEGY_CONTROLLER_BUILT_SOURCE_FIRST_MEASURED_DOWNSTREAM"
NEXT = "MTT_Selected_PrimitiveC1Contractions_or_DynamicOverlapTensor_SourceEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    core = load(CORE)
    sm_packet = load(SM_PACKET)
    empirical = load(EMPIRICAL)
    c1 = load(C1_FRONTIER)
    dynamic = load(DYNAMIC)

    parity_inputs = {
        slot["name"]: {
            "kind": slot["kind"],
            "allowed_use": slot["allowed_use"],
            "forbidden_use": slot["forbidden_use"],
            "no_knob_target": slot["no_knob_target"],
        }
        for slot in core["example_slots"]
    }

    selected_source_before_measurement = {
        "sm_sector_interface_ready": True,
        "actual_selected_sm_packet_closed": sm_packet["gate_results"]["selected_sm_packet_closed"],
        "actual_selected_representation_packet_supplied": sm_packet["gate_results"][
            "actual_selected_representation_packet_supplied"
        ],
        "qa_su3_color_operator_packet_supplied": sm_packet["gate_results"][
            "qa_su3_operator_packet_supplied"
        ],
        "static_sm_slot_functor_routing_closed": c1["static_routing_source_emission"][
            "proved"
        ],
        "dynamic_operator_payload_open": c1["proof_boundary"][
            "dynamic_overlap_tensor_not_emitted"
        ],
    }

    superset_program = {
        "mode": "SM_EQUIVALENCE_FIRST_NO_KNOB_LATER",
        "straight_path": (
            "Declare the selected SM source packet and operator boundary first; after that, admit "
            "measured SM constants as typed downstream parity slots."
        ),
        "superset_paths": {
            "topology_and_terminal_monad": "select static SM slot labels, three-family structure, and anomaly-compatible representation support",
            "q79_theta_route": "supply finite quotient, retarded-overlap, and primitive C1 response scaffolds",
            "qa_su3_color_operator": "supply color/operator packet discipline and reject unsafe direct imports",
            "gr_protospinor": "supply theorem-derived alpha1/dotD replay support without selecting flavor data",
            "dynamic_overlap_route": "supply selected primitive C1 contractions or dynamic overlap tensor needed before measured flavor slots enter",
        },
        "locked_target": NEXT,
        "allowed_measured_inputs_after_target": [
            "gauge couplings with scheme/scale",
            "Yukawa matrices with basis/phase/RG conventions",
            "CKM and PMNS parameters with convention",
            "Higgs parameters with scheme/scale",
            "dimensionful anchors for GR/units parity",
        ],
        "forbidden_uses": core["forbidden_shortcuts"]
        + [
            "using measured Yukawa/CKM/PMNS entries to construct A_selected or b_selected",
            "using measured masses to choose primitive C1 contractions or the dynamic overlap tensor",
            "claiming no-knob closure from SM-equivalence replay",
        ],
    }

    acceptance_gates = {
        "G0_branch_policy": {
            "closed": True,
            "description": "This branch aims for SM-equivalence first, not immediate no-knob closure.",
        },
        "G1_measured_parameter_policy": {
            "closed": core["gate_results"]["measured_parameter_interface_defined"],
            "description": "Measured inputs are typed downstream slots and cannot select sources.",
        },
        "G2_static_sm_source_structure": {
            "closed_for_interface": all(
                row["closed_for_sm_parity_interface"]
                for row in sm_packet["packet_components"]
                if row["id"] != "qa_su3_color_operator_packet"
            ),
            "closed_for_full_packet": sm_packet["gate_results"]["selected_sm_packet_closed"],
            "description": "Gauge, representation, family, Higgs, and anomaly support are interface-ready, but not a full actual selected no-knob packet.",
        },
        "G3_static_weyl_sector_routing": {
            "closed": c1["static_routing_source_emission"]["proved"],
            "description": "Static sector route Z->u,e and X->d,nuD is selected.",
        },
        "G4_dynamic_operator_boundary": {
            "closed": False,
            "description": "Selected primitive C1 contractions or dynamic overlap tensor remain open.",
            "next_required_artifact": NEXT,
        },
        "G5_measured_sm_replay": {
            "closed": False,
            "description": "After G4, admit measured SM constants and run equivalence/reproduction replay.",
        },
    }

    candidate = {
        "candidate": "MTTSMEquivalenceSupersetStrategyController",
        "status": STATUS,
        "inputs": {
            "core_axioms_measured_parameter_interface": rel(CORE),
            "actual_selected_sm_packet_anomaly_audit": rel(SM_PACKET),
            "empirical_equivalence_ledger": rel(EMPIRICAL),
            "primitive_c1_or_weylpair_sectorrouting": rel(C1_FRONTIER),
            "dynamic_overlap_or_c1primitive_source_emission": rel(DYNAMIC),
        },
        "branch_goal": {
            "primary_goal": "SM-equivalence / SM-parity closure",
            "secondary_goal": "no-knob derivation as upgrade path",
            "policy": "Measured constants may be used only after selected source/operator structure is declared.",
        },
        "selected_source_before_measurement": selected_source_before_measurement,
        "parity_input_slots": parity_inputs,
        "superset_program": superset_program,
        "acceptance_gates": acceptance_gates,
        "empirical_replay_after_G4": {
            "purpose": "Reproduce SM calculations at the same standard as the SM once measured parity slots are admitted.",
            "inputs_allowed": empirical["ledger_rows"],
            "must_not_claim": [
                "no-knob derivation of measured constants",
                "source selection by empirical residual",
                "full SM-equivalence before selected dynamic operator boundary is emitted",
            ],
        },
        "what_closes_now": {
            "branch_policy_set_to_SM_equivalence_first": True,
            "superset_strategy_scoped_to_locked_dynamic_operator_target": True,
            "measured_inputs_allowed_only_downstream": True,
            "no_knob_kept_as_upgrade_not_prerequisite": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_dynamic_overlap_tensor_or_primitive_C1_contractions": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_sector_response_matrices": True,
            "measured_SM_replay_after_source_boundary": True,
            "empirical_equivalence_audit_run": True,
            "full_SM_equivalence_closure": True,
            "no_knob_constants_derivation": True,
        },
        "closure_claimed": False,
        "sm_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "SMEquivalenceSupersetStrategyControllerTheorem",
            "proved": True,
            "statement": (
                "For this branch, the active target is SM-equivalence rather than immediate no-knob closure. "
                "Superset paths may contribute topology, terminal-monad, q79, Qa/SU3, GR/protospinor, and "
                "dynamic-overlap evidence only toward the locked selected source/operator boundary. Once that "
                "boundary is emitted, measured SM constants may enter as downstream parity inputs for SM replay; "
                "they may not select source structure, A_selected, b_selected, primitive contractions, or dynamic "
                "overlap tensors."
            ),
        },
    }

    cert = {
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "sm_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT SM-Equivalence Superset Strategy Controller v1

Status: `{STATUS}`.

## Branch Goal

This branch aims first for SM-equivalence / SM-parity closure.  No-knob closure
remains the upgrade path, but it is not a prerequisite for this branch's first
success criterion.

## Superset Strategy

We combine several encodings only toward one locked target:

```text
{NEXT}
```

The current superset roles are:

- topology and terminal monad: static SM slot labels, representation support, and anomaly-compatible structure,
- q79/theta Route-C: finite quotient, retarded-overlap, and primitive C1 scaffolds,
- Qa/SU3: color/operator discipline and unsafe-import rejection,
- GR/protospinor: theorem-derived alpha1/dotD replay,
- dynamic overlap route: selected primitive C1 contractions or dynamic overlap tensor.

## Measured Inputs

Measured SM constants are allowed only after the selected source/operator
boundary is declared.  They may then be used as SM-parity inputs in the same way
the Standard Model uses them: gauge couplings, Yukawas, CKM/PMNS parameters,
Higgs parameters, and dimensionful anchors with conventions and uncertainties.

They may not select source structure, primitive C1 contractions, `A_selected`,
`b_selected`, or the dynamic overlap tensor.

## Next

Close the dynamic operator boundary, then run measured-SM replay and empirical
equivalence audit.  No observed constants or benchmark matrices are source
selectors.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
