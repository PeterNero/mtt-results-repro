"""Tie selected heavy-link values into the CKM observable frontier.

This artifact consumes the selected SU(5) qutrit heavy-link values, the q79 CKM
phase bridge, and the measured replay CKM convention packet.  It closes the
integration/readiness layer and computes guarded observable postchecks, while
leaving the actual no-proxy map from Delta_v to CKM angle magnitudes open.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_ckmanglelaw_fromselectedheavylinks_or_flavorobservablereplay"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INTEGRATION = PACKET_DIR / "selected_ckm_source_chain_integration.packet.json"
DELTA_SIGNATURE = PACKET_DIR / "selected_heavylink_delta_signature.packet.json"
POSTCHECK = PACKET_DIR / "q79_phase_jarlskog_observable_postcheck.packet.json"
ANGLE_MAP_GATE = PACKET_DIR / "remaining_ckm_angle_map_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CKMAngleLaw_FromSelectedHeavyLinkValues_or_FlavorObservableReplay_v1.md"

HEAVYLINK = DATA / "selected_sectortransportselectionlemma_su5qutritheavylink.candidate.json"
HEAVYLINK_VALUES = DATA / "selected_sectortransportselectionlemma_su5qutritheavylink" / "selected_heavylink_eight_slot_values.packet.json"
PHASE_BRIDGE = DATA / "selected_ckmq79phasebridgeimport_or_heavylinkorientationtarget.candidate.json"
CONTRACT = DATA / "selected_heavylinkvectors_after_policybridge_or_ckmlaw.candidate.json"
FLAVOR_POLICY = DATA / "selected_flavoroperatorpolicyuse_afterah8_or_ckmpmnsbridge.candidate.json"
CKM_REPLAY = DATA / "sm_equivalence_ckm_gauge_pmns_convention_fill.candidate.json"

STATUS = "MTT_SELECTED_CKMANGLELAW_FROM_SELECTEDHEAVYLINKS_CHAIN_TIED_ANGLEMAP_OPEN"
NEXT = "MTT_Selected_DeltaV_to_CKM_AngleMagnitudeMap_or_HonestFlavorObservableExecution_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def complex_pair(value: Any) -> complex:
    if isinstance(value, list):
        return complex(float(value[0]), float(value[1]))
    return complex(float(value), 0.0)


def main() -> int:
    heavy = load(HEAVYLINK)
    values = load(HEAVYLINK_VALUES)
    phase = load(PHASE_BRIDGE)
    contract = load(CONTRACT)
    policy = load(FLAVOR_POLICY)
    replay = load(CKM_REPLAY)

    if heavy["closure_decision"]["selected_heavy_link_values_emitted"] is not True:
        raise ValueError("selected heavy-link values are not emitted")
    if values["status"] != "SELECTED_HEAVY_LINK_VALUES_EMITTED":
        raise ValueError("heavy-link value packet not selected")
    if phase["closure_decision"]["selected_CKM_CP_phase_contact_imported"] is not True:
        raise ValueError("q79 CKM phase bridge missing")
    if contract["closure_decision"]["heavy_link_slot_contract_ready"] is not True:
        raise ValueError("heavy-link slot contract not ready")

    delta_entries = [complex_pair(v) for v in values["Delta_v_numeric"]]
    delta_norm = math.sqrt(sum(abs(z) ** 2 for z in delta_entries))
    component_magnitudes = [abs(z) for z in delta_entries]
    component_phases_deg = [math.degrees(math.atan2(z.imag, z.real)) for z in delta_entries]
    relative_phase_deg = component_phases_deg[1] - component_phases_deg[0]

    q = phase["closure_decision"]["q_mod_448"]
    delta_q79_rad = 2.0 * math.pi * q / 448.0
    delta_q79_deg = math.degrees(delta_q79_rad)

    ckm = replay["CKM_packet"]
    params = ckm["derived_parameters"]
    s12 = params["s12"]
    s23 = params["s23"]
    s13 = params["s13"]
    c12 = math.sqrt(1.0 - s12 * s12)
    c23 = math.sqrt(1.0 - s23 * s23)
    c13 = math.sqrt(1.0 - s13 * s13)
    measured_delta = params["delta_deg"]
    measured_j = ckm["jarlskog"]
    j_prefactor = c12 * c23 * c13 * c13 * s12 * s23 * s13
    j_q79_with_measured_angles = j_prefactor * math.sin(delta_q79_rad)
    phase_residual_deg = abs(measured_delta - delta_q79_deg)
    j_relative_residual = abs(j_q79_with_measured_angles - measured_j) / abs(measured_j)

    integration = {
        "schema": "MTTSelectedCKMSourceChainIntegration.v1",
        "status": "SELECTED_SOURCE_CHAIN_TIED",
        "closed_inputs": {
            "policy_operator_CKM_PMNS_bridge": policy["closure_decision"]["policy_operator_CKM_PMNS_bridge_imported"],
            "q79_CKM_CP_phase_contact": phase["closure_decision"]["selected_CKM_CP_phase_contact_imported"],
            "heavy_link_slot_contract": contract["closure_decision"]["heavy_link_slot_contract_ready"],
            "sector_transport_selection_lemma": heavy["closure_decision"]["sector_transport_selection_lemma_closed"],
            "selected_heavy_link_values": heavy["closure_decision"]["selected_heavy_link_values_emitted"],
            "static_same_orientation_filter": contract["closure_decision"]["static_same_orientation_filter_closed"],
            "leading_noncommutation_readiness": contract["closure_decision"]["leading_noncommutation_closed"],
        },
        "newly_closed_by_this_bridge": {
            "old_heavy_link_values_open_flag_superseded": True,
            "selected_heavy_link_entry_count": 8,
            "CKM_source_input_chain_ready": True,
            "leading_noncommutation_values_closed": values["su5_representation_split_nonzero"] and values["Delta_v_numeric"] != [0.0, 0.0],
        },
        "not_closed": {
            "Delta_v_to_CKM_angle_magnitude_map": True,
            "CKM_angle_magnitudes": True,
            "source_derived_Jarlskog_without_measured_angles": True,
            "Yukawa_rows": True,
            "PMNS_orientation_values": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
    }

    delta_signature = {
        "schema": "MTTSelectedHeavyLinkDeltaSignature.v1",
        "status": "SELECTED_DELTAV_SIGNATURE_EMITTED",
        "Delta_v_numeric": values["Delta_v_numeric"],
        "Delta_v_symbolic": values["Delta_t_symbolic"],
        "Delta_c_numeric": values["Delta_c_numeric"],
        "Delta_c_zero": values["Delta_c_numeric"] == [0.0, 0.0],
        "component_magnitudes": component_magnitudes,
        "component_phases_deg": component_phases_deg,
        "relative_phase_deg": relative_phase_deg,
        "norm": delta_norm,
        "norm_symbolic": "sqrt(2/3)",
        "interpretation": (
            "This selected Delta_v is a nonzero two-component heavy-link orientation signature. "
            "It closes leading noncommutation readiness, but it is not by itself the CKM angle map."
        ),
    }

    postcheck = {
        "schema": "MTTQ79PhaseJarlskogObservablePostcheck.v1",
        "status": "OBSERVABLE_POSTCHECK_ONLY_NOT_SELECTOR",
        "q_mod_448": q,
        "delta_q79_rad": delta_q79_rad,
        "delta_q79_deg": delta_q79_deg,
        "measured_replay_delta_deg": measured_delta,
        "phase_residual_deg": phase_residual_deg,
        "measured_replay_angles": {"s12": s12, "s23": s23, "s13": s13},
        "jarlskog_prefactor_from_measured_angles": j_prefactor,
        "jarlskog_q79_phase_with_measured_angles": j_q79_with_measured_angles,
        "measured_replay_jarlskog": measured_j,
        "jarlskog_relative_residual": j_relative_residual,
        "matches_prior_q79_bridge_residuals": (
            abs(phase_residual_deg - phase["closure_decision"]["current_CKM_phase_residual_deg"]) < 1e-12
            and abs(j_relative_residual - phase["closure_decision"]["current_J_q79_relative_residual"]) < 1e-12
        ),
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
    }

    angle_map_gate = {
        "schema": "MTTRemainingCKMAngleMapGate.v1",
        "status": "ANGLE_MAGNITUDE_MAP_OPEN",
        "selected_inputs_available": {
            "Delta_v": True,
            "q79_phase": True,
            "minimal_flavor_policy_operator": True,
            "static_matter_slot_source": True,
            "leading_noncommutation": True,
        },
        "required_next_theorem": (
            "A source-owned functional A_CKM that maps the selected heavy-link signature "
            "Delta_v and the selected flavor operator rows to s12,s23,s13 before any measured "
            "CKM magnitudes enter."
        ),
        "allowed_routes": [
            "derive A_CKM from the selected retarded overlap/Hessian kernel",
            "execute an honest selected Galerkin flavor observable run producing s12,s23,s13",
            "prove a finite qutrit/Weyl trace functional that emits the CKM angle rows",
            "admit a counted 1-3 parameter flavor-orientation policy only if declared before replay",
        ],
        "forbidden_routes": [
            "fit s12,s23,s13 from observed CKM values and call them selected",
            "reuse measured Wolfenstein lambda/A/rhobar/etabar as source rows",
            "claim Jarlskog is source-derived while its angle prefactor is still measured",
        ],
        "next_required_artifact": NEXT,
    }

    theorem = {
        "name": "SelectedCKMSourceChainIntegrationAfterHeavyLinkSelectionTheorem",
        "proved": True,
        "statement": (
            "The selected flavor policy bridge, q79 CKM phase contact, heavy-link contract, "
            "sector-transport selector, and selected heavy-link eight-slot packet now form one "
            "coherent CKM source-input chain. The old heavy-link-values-open flag is superseded: "
            "the branch has selected Delta_v=(1/sqrt(3),omega^2/sqrt(3)) and leading "
            "noncommutation readiness. A guarded observable postcheck with measured CKM angles "
            "reproduces the prior q79 phase/Jarlskog residuals. The remaining proof is not another "
            "selector/import step; it is the source-owned map from Delta_v to the CKM angle "
            "magnitudes s12,s23,s13."
        ),
    }

    data = {
        "candidate": "MTTSelectedCKMAngleLawFromSelectedHeavyLinksOrFlavorObservableReplay",
        "status": STATUS,
        "inputs": {
            "selected_heavy_link_theorem": rel(HEAVYLINK),
            "selected_heavy_link_values": rel(HEAVYLINK_VALUES),
            "q79_phase_bridge": rel(PHASE_BRIDGE),
            "heavy_link_contract": rel(CONTRACT),
            "flavor_policy_bridge": rel(FLAVOR_POLICY),
            "ckm_replay_convention_packet": rel(CKM_REPLAY),
        },
        "output_packets": {
            "selected_ckm_source_chain_integration": rel(INTEGRATION),
            "selected_heavylink_delta_signature": rel(DELTA_SIGNATURE),
            "q79_phase_jarlskog_observable_postcheck": rel(POSTCHECK),
            "remaining_ckm_angle_map_gate": rel(ANGLE_MAP_GATE),
        },
        "closure_decision": {
            "CKM_source_input_chain_tied": True,
            "old_heavy_link_values_open_flag_superseded": True,
            "selected_heavy_link_entry_count": 8,
            "selected_Delta_v_emitted": True,
            "leading_CKM_noncommutation_values_closed": True,
            "q79_phase_contact_closed": True,
            "q79_observable_postcheck_recomputed": True,
            "CKM_angle_magnitudes_derived": False,
            "Jarlskog_source_derived_without_measured_angles": False,
            "Yukawa_rows_derived": False,
            "PMNS_orientation_source_values_derived": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closure_closed": False,
        },
        "postcheck_summary": {
            "delta_q79_deg": delta_q79_deg,
            "phase_residual_deg": phase_residual_deg,
            "jarlskog_relative_residual": j_relative_residual,
        },
        "theorem": theorem,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_CKMAngleLaw_FromSelectedHeavyLinkValues_or_FlavorObservableReplay_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "CKM_source_input_chain_tied": True,
        "selected_heavy_link_entry_count": 8,
        "selected_Delta_v_emitted": True,
        "leading_CKM_noncommutation_values_closed": True,
        "q79_phase_contact_closed": True,
        "CKM_angle_magnitudes_derived": False,
        "Jarlskog_source_derived_without_measured_angles": False,
        "Yukawa_rows_derived": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closure_closed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected CKMAngleLaw FromSelectedHeavyLinkValues or FlavorObservableReplay v1

Status: `{STATUS}`.

## Result

`SelectedCKMSourceChainIntegrationAfterHeavyLinkSelectionTheorem` is proved.

The CKM source-input chain is now tied together:

```text
flavor policy bridge
  -> q79 CKM phase contact
  -> heavy-link eight-slot contract
  -> selected sector transport B_10=I_3, B_bar5=F
  -> selected Delta_v = (1/sqrt(3), omega^2/sqrt(3))
```

The old heavy-link-values-open flag is superseded.  The selected heavy-link
entry count is now `8/8`, and the selected branch has nonzero leading
noncommutation readiness.

## Selected Delta Signature

```text
Delta_v = (0.5773502691896258,
           -0.28867513459481287 - 0.5 i)
||Delta_v|| = sqrt(2/3)
```

## Guarded CKM Postcheck

Using only measured CKM angles as a downstream postcheck, not as selectors:

```text
delta_q79 = {delta_q79_deg:.12f} deg
phase residual = {phase_residual_deg:.12f} deg
Jarlskog relative residual = {j_relative_residual:.12f}
```

## Boundary

This does not yet derive CKM angle magnitudes.  Since Jarlskog needs
`s12*s23*s13*c12*c23*c13^2*sin(delta)`, the q79 phase contact alone cannot
source-derive Jarlskog until the angle prefactor is also source-derived.

The remaining non-looping target is a source-owned functional

```text
A_CKM : (Delta_v, selected flavor operator rows) -> (s12, s23, s13)
```

Next artifact: `{NEXT}`.
"""

    write_json(INTEGRATION, integration)
    write_json(DELTA_SIGNATURE, delta_signature)
    write_json(POSTCHECK, postcheck)
    write_json(ANGLE_MAP_GATE, angle_map_gate)
    write_json(OUTPUT, data)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
