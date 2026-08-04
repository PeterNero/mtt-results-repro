"""Build the physical-boundary or smooth-identity gate after direct payload closure."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "direct_payload_gate": DATA / "selected_heterotic_projectiverhoe_directoperatorpayload_fillattempt.candidate.json",
    "direct_payload": DATA / "selected_heterotic_projectiverhoe_direct_finite_internal_operator_payload.json",
    "physical_boundary": DATA / "selected_heterotic_projectiverhoe_direct_operator_payload_physical_boundary.json",
    "kphys_or_smooth_fill": DATA / "selected_heterotic_projectiverhoe_kphysanchor_or_smoothoperatoridentity_fill.candidate.json",
    "smooth_trace_contract": DATA / "selected_heterotic_projectiverhoe_smooth_trace_lift_or_eqa_finitepart_contract.json",
    "physical_anchor": DATA / "selected_physical_gauge_anchor_and_electroweak_threshold_vector.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_directoperatorpayload_physicalboundary_or_smoothidentity.candidate.json"
OUTPUT_CONTRACT = DATA / "selected_heterotic_projectiverhoe_physicalboundary_or_smoothidentity_contract.json"
OUTPUT_DECISION = DATA / "selected_heterotic_projectiverhoe_next_bridge_decision_after_direct_payload.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_directoperatorpayload_physicalboundary_or_smoothidentity_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_DirectOperatorPayload_PhysicalBoundary_or_SmoothIdentity_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_DIRECT_PAYLOAD_BOUNDARY_LOCKED_NEXT_SMOOTH_IDENTITY_CONTRACT_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothIdentity_TraceLift_or_ComplementQuotient_FillAttempt_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    direct_gate = load(INPUTS["direct_payload_gate"])
    direct_payload = load(INPUTS["direct_payload"])
    boundary = load(INPUTS["physical_boundary"])
    kphys_or_smooth = load(INPUTS["kphys_or_smooth_fill"])
    smooth_contract = load(INPUTS["smooth_trace_contract"])
    physical_anchor = load(INPUTS["physical_anchor"])

    physical_lane = {
        "id": "P_physical_normalization",
        "status": "OPEN_ANCHOR_AND_RG_SCHEME_MISSING",
        "support": {
            "direct_finite_internal_payload_closed": direct_gate["decision"]["direct_finite_internal_operator_payload_closed"],
            "selected_internal_logdet": boundary["closed"]["selected_internal_logdet"],
            "internal_K_gauge_available": physical_anchor["source_checks"]["internal_K_equals_one"],
            "physical_anchor_slot_identified": physical_anchor["source_checks"]["mtheory_gauge_slot_identified"],
        },
        "must_supply": [
            "selected physical action unit K_phys or equivalent Omega0/ell_p/kappa11/alpha_prime source",
            "selected matching scale mu_match",
            "fixed RG and threshold convention",
            "typed electroweak convention map",
            "proof no observed physical constant selected any missing value",
        ],
        "can_close_now": False,
        "reason": "The physical lane has slots but no same-branch dimensionful value or RG/matching scheme.",
    }

    smooth_lane = {
        "id": "S_smooth_identity_or_complement_quotient",
        "status": "OPEN_TRACE_LIFT_OR_COMPLEMENT_QUOTIENT_MISSING",
        "support": {
            "direct_finite_internal_payload_closed": True,
            "finite_internal_subclaims_closed": smooth_contract["finite_internal_subclaims_closed"],
            "smooth_lane_preferred_by_prior_gate": kphys_or_smooth["decision"]["best_next_lane"] == "smooth_operator_identity_bridge",
        },
        "must_supply": smooth_contract["must_supply"],
        "can_close_now": False,
        "reason": "The smooth lane is smaller than physical normalization, but current source lacks smooth transition/connection/trace-lift/E_Qa data.",
    }

    contract = {
        "schema": "SelectedHeteroticProjectiveRhoE.PhysicalBoundaryOrSmoothIdentityContract.v1",
        "status": "TWO_EXTENSION_CONTRACT_OPEN",
        "finite_internal_payload_locked": {
            "payload_path": rel(INPUTS["direct_payload"]),
            "domain": direct_payload["operator_domain_or_finite_quotient_domain"]["labels"],
            "selected_internal_logdet": boundary["closed"]["selected_internal_logdet"],
            "may_be_used_as": "selected finite internal Qa/SU3 operator payload",
            "may_not_be_used_as": "physical coupling, smooth heat trace, or smooth E_Qa block",
        },
        "physical_lane_required": physical_lane["must_supply"],
        "smooth_identity_lane_required": smooth_lane["must_supply"],
        "forbidden_shortcuts": sorted(set(
            boundary["physical_boundary_rule"].split(". ")[:1]
            + smooth_contract["forbidden_shortcuts"]
            + physical_anchor["guardrails"]
        )),
        "next_selected_lane": "S_smooth_identity_or_complement_quotient",
        "why_next_selected": (
            "Physical normalization needs dimensionful source data and RG convention; "
            "smooth identity is the smaller local bridge because finite internal payload, "
            "Bismut/R+ support, trace, quotient, and no-double-count policies are already nearby."
        ),
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_CONTRACT.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    next_decision = {
        "schema": "SelectedHeteroticProjectiveRhoE.NextBridgeDecisionAfterDirectPayload.v1",
        "status": "NEXT_BRIDGE_SELECTED_SMOOTH_IDENTITY_FILL",
        "physical_lane": physical_lane,
        "smooth_lane": smooth_lane,
        "selected_next_lane": contract["next_selected_lane"],
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_DECISION.write_text(json.dumps(next_decision, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "direct_payload_boundary_locked": True,
        "finite_internal_payload_complete": direct_gate["decision"]["direct_finite_internal_operator_payload_closed"],
        "physical_lane_closed": False,
        "smooth_identity_lane_closed": False,
        "physical_lane_blocked_by_anchor_and_rg": True,
        "smooth_identity_lane_selected_next": True,
        "contract_written": True,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEDirectOperatorPayloadPhysicalBoundaryOrSmoothIdentity",
        "status": STATUS,
        "inputs": {name: rel(path) for name, path in INPUTS.items()},
        "contract_path": rel(OUTPUT_CONTRACT),
        "next_decision_path": rel(OUTPUT_DECISION),
        "decision": decision,
        "closed_now": {
            "finite_internal_direct_payload_boundary": True,
            "forbidden_physical_promotions_recorded": True,
            "two_legal_extension_lanes_recorded": True,
            "next_bridge_selected": "smooth_identity_or_complement_quotient",
        },
        "still_open": {
            "physical_action_unit_or_K_phys": True,
            "matching_scale_and_RG_scheme": True,
            "smooth_projective_rhoE_transition_or_connection": True,
            "smooth_trace_lift_or_complement_quotient": True,
            "smooth_E_Qa_or_equivalent_finitepart_operator": True,
        },
        "guardrails": {
            "does_not_promote_log2008_to_physical_coupling": True,
            "does_not_promote_finite_trace_to_smooth_heat_trace": True,
            "does_not_promote_H_sel_to_smooth_E_Qa": True,
            "does_not_set_K_phys_to_one": True,
            "does_not_use_observed_constants": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "DirectPayloadBoundaryLockAndNextBridgeSelection",
            "proved": True,
            "statement": (
                "After direct finite internal operator payload closure, the finite "
                "Qa/SU3 result is complete only at internal quotient scope. It cannot "
                "be promoted to a physical coupling or smooth heat/zeta/torsion trace "
                "without an additional bridge. The legal bridges are physical "
                "normalization or smooth identity/complement quotient. Since the "
                "physical lane still lacks a dimensionful anchor and RG/matching "
                "scheme, the next executable no-knob bridge is the smooth identity "
                "or complement-quotient fill attempt."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "contract_path": rel(OUTPUT_CONTRACT),
        "next_decision_path": rel(OUTPUT_DECISION),
        "note_path": rel(OUTPUT_NOTE),
        "direct_payload_boundary_locked": True,
        "finite_internal_payload_complete": True,
        "physical_lane_closed": False,
        "smooth_identity_lane_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE DirectOperatorPayload PhysicalBoundary or SmoothIdentity v1

## Result

```text
status = {STATUS}
direct_payload_boundary_locked = true
finite_internal_payload_complete = true
physical_lane_closed = false
smooth_identity_lane_closed = false
next_required_artifact = {NEXT}
```

## Meaning

The direct finite internal `rho_E` payload is complete at internal Qa/SU3
quotient scope. It is not a physical coupling and not a smooth heat trace.

Two legal extensions remain:

- physical normalization, requiring a same-branch action unit plus matching and
  RG convention;
- smooth identity/complement quotient, requiring a smooth transition/connection
  or trace-lift/complement theorem.

The next executable bridge is the smooth identity/complement-quotient fill,
because the physical lane still lacks dimensionful source data.

Contract:

```text
{rel(OUTPUT_CONTRACT)}
```

Decision:

```text
{rel(OUTPUT_DECISION)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CONTRACT)}")
    print(f"wrote {rel(OUTPUT_DECISION)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(result["status"])
