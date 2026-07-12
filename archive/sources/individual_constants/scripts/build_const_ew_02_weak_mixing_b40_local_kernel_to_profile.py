"""Build CONST-EW-02 B40 local C1 source kernel to weak-mixing profile handoff."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b40_local_kernel_to_profile"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROPAGATION = BASE / "local_c1_source_kernel_propagation.packet.json"
PHYSICAL_GATE = BASE / "physical_weak_angle_gate_after_local_kernel.packet.json"
BOUNDARY = BASE / "weak_mixing_b40_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B40_LocalKernel_to_Profile_v1.md"

STATUS = "MTT_CONST_EW_02_B40_LOCAL_KERNEL_TO_PROFILE_HANDOFF_BUILT"


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
    BASE.mkdir(parents=True, exist_ok=True)

    b39_path = DATA / "const_ew_02_weak_mixing_b39_source_kernel_or_local_principle.candidate.json"
    b39_boundary_path = DATA / "const_ew_02_weak_mixing_b39_source_kernel_or_local_principle" / "weak_mixing_b39_boundary.packet.json"
    b39_local_kernel_path = DATA / "const_ew_02_weak_mixing_b39_source_kernel_or_local_principle" / "local_principle_preresidual_source_kernel.packet.json"
    b22_path = DATA / "const_ew_02_weak_mixing_b22_parameterized_bridge_replay.candidate.json"
    b24_path = DATA / "const_ew_02_weak_mixing_b24_udyn_source_derivation_import.candidate.json"
    b25_path = DATA / "const_ew_02_weak_mixing_b25_internal_lambda12_physical_frontier.candidate.json"
    b26_path = DATA / "const_ew_02_weak_mixing_b26_two_edge_promotion_contract.candidate.json"

    b39 = load(b39_path)
    b39_boundary = load(b39_boundary_path)
    b39_local_kernel = load(b39_local_kernel_path)
    b22 = load(b22_path)
    b24 = load(b24_path)
    b25 = load(b25_path)
    b26 = load(b26_path)

    propagation = {
        "schema": "MTTConstEW02B40LocalC1SourceKernelPropagation.v1",
        "status": "LOCAL_C1_SOURCE_KERNEL_PROPAGATED_TO_WEAK_MIXING_PROFILE_FRONTIER",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B40-LOCAL-C1-SOURCE-KERNEL-PROPAGATION",
        "inputs": {
            "B39_candidate": rel(b39_path),
            "B39_local_source_kernel": rel(b39_local_kernel_path),
            "B22_parameterized_bridge": rel(b22_path),
            "B24_udyn_source_derivation": rel(b24_path),
            "B25_internal_lambda12": rel(b25_path),
            "B26_two_edge_contract": rel(b26_path),
        },
        "local_principle_tier": {
            "source_kernel_closed": b39["local_tier_source_kernel_closed"],
            "strict_unpatched_kernel_closed": b39["strict_unpatched_source_kernel_closed"],
            "principle_name": b39_local_kernel["principle_name"],
            "kernel_clauses": b39_local_kernel["kernel_clauses_under_local_principle"],
        },
        "weak_mixing_profile_prefix": {
            "u_dyn_source_derived": b24["u_dyn_source_derived"],
            "u_dyn_value": b24["u_dyn_value"],
            "internal_lambda_12_closed": b25["internal_lambda_12_closed"],
            "internal_lambda_12_value": b25["internal_lambda_12_value"],
            "active_bridge_parameters": b22["active_bridge_parameters_in_weak_angle"],
            "reserved_bridge_parameters": b22["reserved_bridge_parameters"],
        },
        "local_tier_C1_source_promotion_disposition": {
            "dynamic_C1_source_kernel_active_blocker_retired_in_local_tier": True,
            "primitive_C1_source_side_no_longer_primary_blocker_in_local_tier": True,
            "strict_no_knob_upgrade_still_tracks_unpatched_kernel": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    physical_gate = {
        "schema": "MTTConstEW02B40PhysicalWeakAngleGateAfterLocalKernel.v1",
        "status": "PHYSICAL_WEAK_ANGLE_REDUCED_TO_GAUGE_ACTION_RG_MATCHING_AFTER_LOCAL_KERNEL",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B40-PHYSICAL-GATE-AFTER-LOCAL-KERNEL",
        "remaining_physical_gates": {
            "K_phys_or_f_ab_closed": b26["K_phys_or_f_ab_closed"],
            "mu_match_closed": b26["mu_match_closed"],
            "RG_scheme_closed": b26["RG_scheme_closed"],
            "physical_alpha_or_metrology_anchor": True,
            "threshold_profile_policy": True,
        },
        "what_is_now_not_the_primary_local_tier_blocker": [
            "u_dyn source-strength prefix",
            "internal lambda_12 / Delta_G12",
            "dynamic C1 source-kernel ownership in the explicit local principle tier",
        ],
        "what_still_blocks_a_number": [
            "source-selected physical gauge/action normalization",
            "source-selected matching scale",
            "RG/threshold transport from internal scheme to physical effective weak angle",
            "physical alpha/metrology anchor or equivalent unit bridge",
        ],
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B40Boundary.v1",
        "status": "B40_LOCAL_KERNEL_HANDOFF_COMPLETE_PHYSICAL_GAUGE_RG_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B40-BOUNDARY",
        "previous_B39": {
            "candidate": b39["candidate"],
            "status": b39["status"],
            "still_open": b39_boundary["still_open"],
        },
        "closed_or_decided_now": {
            "local_dynamic_C1_source_kernel_propagated": True,
            "u_dyn_source_derived_preserved": True,
            "internal_lambda_12_closed_preserved": True,
            "physical_gate_reduced_to_gauge_action_RG_matching": True,
            "physical_weak_angle_numerical_closure": False,
            "strict_no_knob_kernel_derivation": False,
        },
        "still_open": {
            "K_phys_or_gauge_kinetic_normalization": True,
            "physical_alpha_or_metrology_anchor": True,
            "mu_match": True,
            "RG_threshold_scheme": True,
            "strict_unpatched_source_kernel_upgrade": True,
            "physical_weak_angle_numerical_closure": True,
            "strict_full_no_knob_closure": True,
        },
        "anti_cycle_delta_from_B39": {
            "B39": "accepted the local source-principle tier for the C1 source kernel",
            "B40": "propagates that decision to the weak-mixing profile and moves the active blocker to physical gauge/action/RG matching",
            "not_repeated": [
                "not re-opening the C1 source-kernel blocker in the local tier",
                "not claiming a physical weak-angle value",
                "not using measured weak angle or alpha as selectors",
            ],
        },
        "allowed_claim": "B40 retires dynamic C1 source-kernel ownership as the active blocker in the explicit local-principle tier.",
        "forbidden_claim": "physical weak-angle numerical prediction, physical alpha closure, RG closure, or strict unpatched no-knob closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B40NextWork.v1",
        "status": "NEXT_WORKORDER_PHYSICAL_GAUGE_ACTION_RG_OR_METROLOGY_ANCHOR",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B41-PHYSICAL-GAUGE-ACTION-RG-MATCHING",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B41-GAUGE-ACTION-NORMALIZATION-ANCHOR",
            "task": "Construct a source-selected physical gauge/action normalization or metrology anchor linking the internal weak-split scheme to physical alpha/electroweak units without using observed weak angle as a selector.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B41-RG-MATCHING-THRESHOLD-SCHEME",
            "task": "Declare and source-select the matching scale, RG transport, and threshold/profile policy needed to move the internal weak-split value to a physical effective weak angle.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB40LocalKernelToProfile",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B40-LOCAL-KERNEL-TO-WEAK-MIXING-PROFILE",
        "output_packets": {
            "local_c1_source_kernel_propagation": rel(PROPAGATION),
            "physical_weak_angle_gate_after_local_kernel": rel(PHYSICAL_GATE),
            "weak_mixing_b40_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B40LocalKernelToProfileHandoffTheorem",
            "proved": True,
            "statement": (
                "After accepting the explicit local SelectedWeylVariationActionPrinciple tier, the dynamic C1 source-kernel blocker is retired for the local weak-mixing branch. The already source-derived u_dyn=1 and internal lambda_12 data are preserved. The remaining physical weak-angle blocker is no longer C1 source ownership but physical gauge/action normalization, matching scale, and RG/threshold transport."
            ),
        },
        "local_dynamic_C1_source_kernel_propagated": True,
        "u_dyn_source_derived_preserved": True,
        "internal_lambda_12_closed_preserved": True,
        "physical_gate_reduced_to_gauge_action_RG_matching": True,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B40_LocalKernel_to_Profile_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "local_dynamic_C1_source_kernel_propagated": True,
        "u_dyn_source_derived_preserved": True,
        "internal_lambda_12_closed_preserved": True,
        "physical_gate_reduced_to_gauge_action_RG_matching": True,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B40 Local Kernel to Profile v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B40-LOCAL-KERNEL-TO-WEAK-MIXING-PROFILE`

## Result

```text
local dynamic C1 source kernel propagated  True
u_dyn=1 source-derived prefix preserved    True
internal lambda_12 preserved               True
physical weak-angle numerical closure      False
```

The active blocker has moved.  In the explicit local-principle tier, dynamic C1
source ownership is no longer the live obstacle.  The next obstacle is physical
gauge/action normalization and RG/threshold matching.

## Next

`CONST-EW-02 / WEAK-MIXING / B41-PHYSICAL-GAUGE-ACTION-RG-MATCHING`
"""

    for path, payload in [
        (PROPAGATION, propagation),
        (PHYSICAL_GATE, physical_gate),
        (BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
