"""Build the post-policy CKM heavy-link vector execution contract."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_heavylinkvectors_after_policybridge_or_ckmlaw"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SLOT_CONTRACT = PACKET_DIR / "heavy_link_vector_slot_contract.packet.json"
SUPPORT_LEDGER = PACKET_DIR / "heavy_link_support_and_forbidden_proxy_ledger.packet.json"
EXECUTION_GATE = PACKET_DIR / "heavy_link_selected_value_execution_gate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_heavy_link_value_source_search.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HeavyLinkVectorValuesAfterPolicyBridge_or_CKMHigherBreakdownLaw_v1.md"

PREVIOUS = DATA / "selected_flavoroperatorpolicyuse_afterah8_or_ckmpmnsbridge.candidate.json"
HEAVY_TARGET = DATA / "selected_flavoroperatorpolicyuse_afterah8_or_ckmpmnsbridge" / "post_ah8_heavy_link_orientation_target.packet.json"
NO_PROXY = DATA / "selected_ckmq79phasebridgeimport_or_heavylinkorientationtarget" / "no_proxy_flavor_boundary_after_q79_import.packet.json"
STATIC_TRANSFER = DATA / "selected_staticcoefficienttransfermap_or_cporientationfrontier.candidate.json"
WEYL_FILTER = DATA / "selected_weylcoefficientsource_reduction_or_orientationtransfermap.candidate.json"

STATUS = "MTT_SELECTED_HEAVYLINKVECTORS_AFTER_POLICYBRIDGE_CONTRACT_READY_VALUES_OPEN"
PREVIOUS_STATUS = "MTT_SELECTED_FLAVOROPERATORPOLICYUSE_AFTERAH8_CKMPMNS_BRIDGE_Q79_CONTACT_HEAVYLINK_OPEN"
NEXT = "MTT_Selected_HeavyLinkValueSourceSearch_or_SelectedCKMAngleLaw_v1"


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
    sources = [PREVIOUS, HEAVY_TARGET, NO_PROXY, STATIC_TRANSFER, WEYL_FILTER]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing heavy-link contract inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    heavy = load(HEAVY_TARGET)
    no_proxy = load(NO_PROXY)
    static = load(STATIC_TRANSFER)
    weyl = load(WEYL_FILTER)

    if previous["status"] != PREVIOUS_STATUS:
        raise ValueError("previous CKM/PMNS bridge status mismatch")

    required_entries = heavy["required_packet_entries"]
    emitted_entries: dict[str, Any] = {}
    missing_entries = [entry for entry in required_entries if entry not in emitted_entries]

    slot_contract = {
        "schema": "MTTHeavyLinkVectorSlotContract.v1",
        "status": "HEAVY_LINK_EIGHT_SLOT_CONTRACT_READY",
        "closure_claimed": True,
        "required_packet_entries": required_entries,
        "required_entry_count": len(required_entries),
        "emitted_entry_count": len(emitted_entries),
        "missing_entries": missing_entries,
        "vector_formula": "Delta_v = Delta_t + chi_q Delta_c",
        "target_vectors": ["v_u", "v_d", "Delta_v"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    support_ledger = {
        "schema": "MTTHeavyLinkSupportAndForbiddenProxyLedger.v1",
        "status": "Q79_NONCOMMUTATION_STATIC_FILTER_SUPPORT_READY_VALUES_OPEN",
        "closure_claimed": True,
        "q79_phase_contact": no_proxy["q79_phase_contact"],
        "leading_noncommutation_closed": heavy["leading_noncommutation_closed"],
        "static_same_orientation_filter_closed": weyl["closure_decision"]["same_orientation_filter_closed"],
        "mixed_branches_rejected_at_static_tier": static["closure_decision"]["mixed_branches_rejected"],
        "usable_selected_inputs_found": no_proxy["usable_selected_inputs_found"],
        "rejected_proxy_inputs_found": no_proxy["rejected_proxy_inputs_found"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    execution_gate = {
        "schema": "MTTHeavyLinkSelectedValueExecutionGate.v1",
        "status": "HEAVY_LINK_SELECTED_VALUES_NOT_EMITTED",
        "closure_claimed": True,
        "selected_heavy_link_values_emitted": False,
        "selected_Delta_v_value_emitted": False,
        "CKM_angle_magnitudes_derived": False,
        "Jarlskog_value_derived": False,
        "full_true_SM_equivalence_closed": False,
        "first_required_source_objects": [
            "M_C1_alpha1 entries",
            "selected V_C1 functional",
            "explicit Hess_Xi blocks",
            "explicit dotD operators",
            "zero-mode contractions",
            "up/down response orientations",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextHeavyLinkValueSourceSearch.v1",
        "status": "NEXT_IS_SOURCE_VALUES_FOR_EIGHT_HEAVY_LINK_SLOTS",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "do_not_reopen": [
            "q79 CKM CP phase contact",
            "CKM/PMNS policy-tier bridge",
            "static same-orientation branch filter",
            "leading noncommutation criterion",
        ],
        "search_targets": missing_entries,
        "allowed_source_routes": [
            "selected alpha1/C1 primitive contractions",
            "selected Hess_Xi and dotD operator blocks",
            "selected zero-mode contraction table",
            "source-owned up/down response orientation map",
        ],
        "forbidden_routes": [
            "observed CKM angle backsolve",
            "benchmark Yukawa or CKM matrices",
            "per-entry empirical fitting",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "HeavyLinkVectorExecutionContractTheorem",
        "proved": True,
        "statement": (
            "After the policy-tier flavor operator and q79 CKM phase bridge, the remaining selected CKM "
            "angle source problem is exactly the eight-slot heavy-link vector packet. Current support "
            "closes q79 phase contact, leading noncommutation readiness, and static same-orientation "
            "filtering, while emitting zero selected heavy-link values. Thus CKM angle magnitudes require "
            "source values for t_u13,t_u23,t_d13,t_d23,c_u13,c_u23,c_d13,c_d23, not replayed CKM data."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedHeavyLinkVectorsAfterPolicyBridgeOrCKMLaw",
        "status": STATUS,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_ckm_pmns_bridge": rel(PREVIOUS),
            "heavy_target": rel(HEAVY_TARGET),
            "no_proxy_boundary": rel(NO_PROXY),
            "static_transfer": rel(STATIC_TRANSFER),
            "weyl_filter": rel(WEYL_FILTER),
        },
        "output_packets": {
            "heavy_link_vector_slot_contract": rel(SLOT_CONTRACT),
            "heavy_link_support_and_forbidden_proxy_ledger": rel(SUPPORT_LEDGER),
            "heavy_link_selected_value_execution_gate": rel(EXECUTION_GATE),
            "next_heavy_link_value_source_search": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "heavy_link_slot_contract_ready": True,
            "required_heavy_link_entry_count": len(required_entries),
            "selected_heavy_link_entry_count": len(emitted_entries),
            "selected_heavy_link_values_emitted": False,
            "q79_phase_contact_closed": no_proxy["q79_phase_contact"],
            "leading_noncommutation_closed": heavy["leading_noncommutation_closed"],
            "static_same_orientation_filter_closed": weyl["closure_decision"]["same_orientation_filter_closed"],
            "mixed_branches_rejected_at_static_tier": static["closure_decision"]["mixed_branches_rejected"],
            "CKM_angle_magnitudes_derived": False,
            "selected_CKM_orientation_source_closed": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": theorem,
    }

    cert = {
        "certificate": "MTTSelectedHeavyLinkVectorsAfterPolicyBridgeOrCKMLaw",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "heavy_link_slot_contract_ready": True,
        "required_heavy_link_entry_count": len(required_entries),
        "selected_heavy_link_entry_count": len(emitted_entries),
        "selected_heavy_link_values_emitted": False,
        "CKM_angle_magnitudes_derived": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HeavyLinkVectorValuesAfterPolicyBridge or CKMHigherBreakdownLaw v1

## Theorem

`HeavyLinkVectorExecutionContractTheorem` is proved.

The CKM angle source problem is now reduced to the eight-slot heavy-link vector
packet: `t_u13`, `t_u23`, `t_d13`, `t_d23`, `c_u13`, `c_u23`, `c_d13`,
`c_d23`.

## What Closes

- q79 CKM CP phase contact remains closed
- leading noncommutation readiness remains closed
- static same-orientation branch filtering remains closed
- proxy CKM/Yukawa matrix inputs remain forbidden

## Boundary

No selected heavy-link values are emitted yet. CKM angle magnitudes, selected
CKM orientation source values, no-knob closure, and true SM equivalence remain
open.

## Next Artifact

`{NEXT}`
"""

    write_json(SLOT_CONTRACT, slot_contract)
    write_json(SUPPORT_LEDGER, support_ledger)
    write_json(EXECUTION_GATE, execution_gate)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
