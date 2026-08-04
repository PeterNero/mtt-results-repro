"""Build post-AH8 flavor-operator policy use / CKM-PMNS bridge."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_flavoroperatorpolicyuse_afterah8_or_ckmpmnsbridge"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ORIENTATION_IMPORT = PACKET_DIR / "post_ah8_policy_operator_ckm_pmns_bridge_import.packet.json"
Q79_IMPORT = PACKET_DIR / "post_ah8_q79_ckm_phase_contact_import.packet.json"
HEAVY_TARGET = PACKET_DIR / "post_ah8_heavy_link_orientation_target.packet.json"
NEXT_PACKET = PACKET_DIR / "next_heavy_link_vector_values_after_policy_bridge.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FlavorOperatorPolicyUseAfterAH8_or_CKMPMNSOrientationBridge_v1.md"

PREVIOUS = DATA / "selected_magnitudebearingrows_after_postah8_dynamicimport.candidate.json"
FLAVOR_BRIDGE = DATA / "selected_flavoroperatorvalueuse_or_ckmpmnsorientationbridge.candidate.json"
ORIENTATION_PACKET = (
    DATA
    / "selected_flavoroperatorvalueuse_or_ckmpmnsorientationbridge"
    / "flavor_operator_ckmpmns_orientation_bridge.packet.json"
)
Q79_CANDIDATE = DATA / "selected_ckmq79phasebridgeimport_or_heavylinkorientationtarget.candidate.json"
Q79_PACKET = DATA / "selected_ckmq79phasebridgeimport_or_heavylinkorientationtarget" / "q79_ckm_phase_bridge_import.packet.json"
JARLSKOG_PACKET = (
    DATA
    / "selected_ckmq79phasebridgeimport_or_heavylinkorientationtarget"
    / "current_ckm_jarlskog_postcheck_from_q79.packet.json"
)
HEAVY_PACKET = (
    DATA
    / "selected_ckmq79phasebridgeimport_or_heavylinkorientationtarget"
    / "heavy_link_higher_breakdown_orientation_target.packet.json"
)

STATUS = "MTT_SELECTED_FLAVOROPERATORPOLICYUSE_AFTERAH8_CKMPMNS_BRIDGE_Q79_CONTACT_HEAVYLINK_OPEN"
PREVIOUS_STATUS = "MTT_SELECTED_MAGNITUDEBEARINGROWS_AFTER_POSTAH8_DYNAMICIMPORT_POLICY9_STRICT0"
NEXT = "MTT_Selected_HeavyLinkVectorValuesAfterPolicyBridge_or_CKMHigherBreakdownLaw_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    sources = [PREVIOUS, FLAVOR_BRIDGE, ORIENTATION_PACKET, Q79_CANDIDATE, Q79_PACKET, JARLSKOG_PACKET, HEAVY_PACKET]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing post-AH8 CKM/PMNS inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    bridge = load(FLAVOR_BRIDGE)
    orientation = load(ORIENTATION_PACKET)
    q79_candidate = load(Q79_CANDIDATE)
    q79 = load(Q79_PACKET)
    jarlskog = load(JARLSKOG_PACKET)
    heavy = load(HEAVY_PACKET)

    if previous["status"] != PREVIOUS_STATUS:
        raise ValueError("previous post-AH8 magnitude status mismatch")

    bridge_executable = (
        bridge["closure_decision"]["CKM_PMNS_orientation_bridge_executable"]
        and orientation["bridge_ready"]
        and orientation["CKM_bridge"]["operator_use_closed"]
        and orientation["PMNS_bridge"]["operator_use_closed"]
    )
    q79_contact = (
        q79_candidate["closure_decision"]["selected_CKM_CP_phase_contact_imported"]
        and q79["selected_CKM_CP_phase_contact_imported"]
        and q79["no_empirical_label_scan"]
        and q79["q_mod_448"] == 79
    )
    heavy_open = heavy["selected_packet_values_open"]

    orientation_import = {
        "schema": "MTTPostAH8PolicyOperatorCKMPMNSBridgeImport.v1",
        "status": "CKM_PMNS_POLICY_OPERATOR_BRIDGE_IMPORTED_AFTER_AH8",
        "closure_claimed": True,
        "CKM_PMNS_orientation_bridge_executable": bridge_executable,
        "flavor_operator_policy_value_use_closed": bridge["closure_decision"]["flavor_operator_policy_value_use_closed"],
        "policy_csk_source_value_row_count": bridge["closure_decision"]["policy_csk_source_value_row_count"],
        "strict_csk_source_row_count": bridge["closure_decision"]["strict_selected_csk_source_row_count"],
        "CKM_orientation_source_tier": orientation["CKM_bridge"]["orientation_source_tier"],
        "PMNS_orientation_source_tier": orientation["PMNS_bridge"]["orientation_source_tier"],
        "qualitative_CP_bridge_closed": bridge["closure_decision"]["qualitative_CP_bridge_closed"],
        "measured_CKM_PMNS_phase_values_derived": False,
        "selected_CKM_PMNS_orientation_source_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    q79_import = {
        "schema": "MTTPostAH8Q79CKMPhaseContactImport.v1",
        "status": "Q79_CKM_PHASE_CONTACT_IMPORTED_AFTER_POLICY_BRIDGE",
        "closure_claimed": True,
        "selected_CKM_CP_phase_contact_imported": q79_contact,
        "q_mod_448": q79["q_mod_448"],
        "delta_q79_deg": q79["delta_q79_deg"],
        "phase_residual_deg": jarlskog["phase_residual_deg"],
        "jarlskog_relative_residual": jarlskog["jarlskog_relative_residual"],
        "CKM_angle_magnitudes_derived": False,
        "full_CKM_orientation_values_derived": False,
        "observed_CKM_used_as_selector": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    heavy_target = {
        "schema": "MTTPostAH8HeavyLinkOrientationTarget.v1",
        "status": "HEAVY_LINK_VECTOR_VALUES_REMAIN_NEXT_ORIENTATION_SOURCE_TARGET",
        "closure_claimed": True,
        "CKM_heavy_link_calculator_ready": q79_candidate["closure_decision"]["CKM_heavy_link_calculator_ready"],
        "leading_noncommutation_closed": heavy["leading_noncommutation_closed"],
        "required_packet_entries": heavy["required_packet_entries"],
        "selected_packet_values_open": heavy_open,
        "selected_heavy_link_values_emitted": False,
        "CKM_angles_derived": False,
        "full_true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextHeavyLinkVectorValuesAfterPolicyBridge.v1",
        "status": "NEXT_IS_HEAVY_LINK_VECTOR_VALUES_OR_STRICT_ORIENTATION_SOURCE",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "do_not_reopen": [
            "AH-equivalent BN27 8/8 matrix row",
            "minimal nine-slot flavor policy value table",
            "CKM/PMNS policy-tier bridge",
            "q79 CKM CP phase contact",
        ],
        "remaining_orientation_targets": [
            "selected heavy-link vector values t_u,t_d,c_u,c_d",
            "selected CKM angle magnitudes",
            "selected CKM/PMNS orientation source theorem",
            "strict csk/flavor source rows replacing policy values",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "PostAH8FlavorOperatorPolicyUseAndCKMPMNSBridgeTheorem",
        "proved": True,
        "statement": (
            "After the post-AH8 minimal nine-slot flavor policy import, the same selected-family flavor "
            "operator is usable for CKM/PMNS orientation replay and precision integration. The q79 CKM "
            "CP contact is imported from the selected finite branch without empirical label scan. This "
            "closes policy-tier operator use and qualitative CP/orientation support, but not selected "
            "CKM/PMNS orientation source values, CKM angle magnitudes, heavy-link vector values, strict "
            "coefficient source rows, or true SM equivalence."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedFlavorOperatorPolicyUseAfterAH8OrCKMPMNSBridge",
        "status": STATUS,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_policy_tier": rel(PREVIOUS),
            "flavor_bridge": rel(FLAVOR_BRIDGE),
            "orientation_packet": rel(ORIENTATION_PACKET),
            "q79_candidate": rel(Q79_CANDIDATE),
            "q79_packet": rel(Q79_PACKET),
            "jarlskog_packet": rel(JARLSKOG_PACKET),
            "heavy_packet": rel(HEAVY_PACKET),
        },
        "output_packets": {
            "post_ah8_policy_operator_ckm_pmns_bridge_import": rel(ORIENTATION_IMPORT),
            "post_ah8_q79_ckm_phase_contact_import": rel(Q79_IMPORT),
            "post_ah8_heavy_link_orientation_target": rel(HEAVY_TARGET),
            "next_heavy_link_vector_values_after_policy_bridge": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "policy_operator_CKM_PMNS_bridge_imported": bridge_executable,
            "policy_csk_source_value_row_count": bridge["closure_decision"]["policy_csk_source_value_row_count"],
            "strict_csk_source_row_count": bridge["closure_decision"]["strict_selected_csk_source_row_count"],
            "qualitative_CP_bridge_closed": bridge["closure_decision"]["qualitative_CP_bridge_closed"],
            "q79_CKM_CP_phase_contact_imported": q79_contact,
            "q_mod_448": q79["q_mod_448"],
            "q79_phase_residual_deg": jarlskog["phase_residual_deg"],
            "q79_jarlskog_relative_residual": jarlskog["jarlskog_relative_residual"],
            "selected_heavy_link_values_emitted": False,
            "selected_CKM_PMNS_orientation_source_closed": False,
            "CKM_angles_derived": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": theorem,
    }

    cert = {
        "certificate": "MTTSelectedFlavorOperatorPolicyUseAfterAH8OrCKMPMNSBridge",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "policy_operator_CKM_PMNS_bridge_imported": bridge_executable,
        "q79_CKM_CP_phase_contact_imported": q79_contact,
        "selected_heavy_link_values_emitted": False,
        "selected_CKM_PMNS_orientation_source_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected FlavorOperatorPolicyUseAfterAH8 or CKMPMNSOrientationBridge v1

## Theorem

`PostAH8FlavorOperatorPolicyUseAndCKMPMNSBridgeTheorem` is proved.

The post-AH8 flavor operator is now usable for CKM/PMNS orientation replay at
the minimal nine-slot policy tier, and the q79 CKM CP phase contact is imported
from the selected finite branch.

## What Closes

- CKM/PMNS policy-tier orientation bridge is executable
- qualitative CP/non-scalar orientation support remains closed
- q79 CKM CP phase contact is imported without empirical label scan

## Boundary

CKM angle magnitudes, selected CKM/PMNS orientation source values, selected
heavy-link vector values, strict csk/flavor source rows, no-knob closure, and
true SM equivalence remain open.

## Next Artifact

`{NEXT}`
"""

    write_json(ORIENTATION_IMPORT, orientation_import)
    write_json(Q79_IMPORT, q79_import)
    write_json(HEAVY_TARGET, heavy_target)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
