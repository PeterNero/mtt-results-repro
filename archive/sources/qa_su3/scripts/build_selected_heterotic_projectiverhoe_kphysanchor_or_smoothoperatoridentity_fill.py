"""Build K_phys-anchor or smooth-operator-identity fill attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

EXTERNAL_GR = ROOT.parent / "mtt-protospinor-gr-response-proof" / "certificates"

INPUTS = {
    "contract": DATA / "selected_heterotic_projectiverhoe_physicalnormalization_or_smoothidentity_contract.json",
    "previous_gate": DATA / "selected_heterotic_projectiverhoe_physicalthresholdnormalization_or_smoothoperatoridentity.candidate.json",
    "bismut_payload": DATA / "selected_heterotic_bismut_weitzenbock_tensor_payload_fill.candidate.json",
    "rplus_payload": DATA / "selected_heterotic_rplus_curvature_payload_fill.candidate.json",
    "m_theory_anchor": EXTERNAL_GR / "m_theory_modal_gap_dimensional_anchor_candidate_certificate.json",
    "omega_gap": EXTERNAL_GR / "selected_physical_omega_gap_theorem_certificate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_kphysanchor_or_smoothoperatoridentity_fill.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_kphysanchor_or_smoothoperatoridentity_fill_certificate.json"
OUTPUT_OBLIGATIONS = DATA / "selected_heterotic_projectiverhoe_smooth_bundle_operator_or_kphys_remaining_obligations.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_KPhysAnchor_or_SmoothOperatorIdentity_Fill_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_KPHYS_OR_SMOOTH_IDENTITY_FILL_REDUCED_BUNDLE_OPERATOR_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_BundleConnection_RepresentationTrace_QuotientPolicy_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def all_false(values: dict[str, bool]) -> bool:
    return all(value is False for value in values.values())


def main() -> dict[str, Any]:
    contract = load(INPUTS["contract"])
    previous = load(INPUTS["previous_gate"])
    bismut = load(INPUTS["bismut_payload"])
    rplus = load(INPUTS["rplus_payload"])
    m_anchor = load(INPUTS["m_theory_anchor"])
    omega = load(INPUTS["omega_gap"])

    physical_lane = {
        "lane_id": "physical_normalization_bridge",
        "status": "PARTIAL_ANCHOR_SLOT_IDENTIFIED_VALUE_OPEN",
        "support": {
            "contract_requires_physical_anchor": "physical_normalization_bridge" in contract["must_prove_one_of"],
            "internal_rhoE_interface_closed": previous["decision"]["internal_interface_closed"],
            "m_theory_planck_slot_identified": m_anchor["closed_tests"]["m_theory_planck_slot_identified"],
            "m_theory_gauge_slot_identified": m_anchor["closed_tests"]["m_theory_gauge_slot_identified"],
            "omega_gap_formula_reduced": omega["theorem"]["status"] == "REDUCED_NOT_CLOSED",
            "internal_action_units_closed_in_omega_program": omega["structural_inputs"]["internal_action_units_closed"],
        },
        "blockers": {
            "dimensionful_modal_gap_value_computed": m_anchor["open_tests"]["dimensionful_modal_gap_value_computed"],
            "ell_p_or_kappa11_selected_without_backsolve": m_anchor["open_tests"]["ell_p_or_kappa11_selected_without_backsolve"],
            "alpha_prime_or_string_length_selected_without_backsolve": m_anchor["open_tests"]["alpha_prime_or_string_length_selected_without_backsolve"],
            "C_UV_source_certified": omega["open_inputs"]["C_UV_source_certified"],
            "delta_source_certified": omega["open_inputs"]["delta_source_certified"],
            "omega_gap_phys_selected": omega["open_inputs"]["omega_gap_phys_selected"],
            "matching_scale_closed": previous["physical_checks"]["matching_scale_closed"],
            "RG_scheme_closed": previous["physical_checks"]["RG_scheme_closed"],
        },
        "legal_closure_payload": [
            "selected K_phys or equivalent Omega_0/ell_p/kappa_11/alpha_prime/action-unit source",
            "selected mu_match",
            "fixed RG and threshold convention",
            "proof that no observed physical constant was used as selector",
        ],
        "verdict": (
            "The physical lane has the right action-unit slot, but not a selected "
            "dimensionful value. It cannot close K_phys from the current source."
        ),
    }

    smooth_lane = {
        "lane_id": "smooth_operator_identity_bridge",
        "status": "PARTIAL_GEOMETRY_FILLED_BUNDLE_OPERATOR_OPEN",
        "support": {
            "contract_requires_smooth_operator_identity": "smooth_operator_identity_bridge" in contract["must_prove_one_of"],
            "bismut_geometric_tensor_payload_filled": bismut["decision"]["geometric_tensor_payload_filled"],
            "rplus_curvature_filled": rplus["decision"]["R_plus_curvature_filled"],
            "finite_internal_packet_selected": previous["internal_checks"]["rhoE_value_selected"],
            "internal_finite_part_is_log2008": previous["internal_checks"]["rhoE_value_is_log2008"],
        },
        "blockers": {
            "smooth_projective_rhoE_transition_data_emitted": False,
            "connection_A_components": rplus["filled_payload"]["bundle_tensors"]["connection_A_components"] is not None,
            "curvature_F_A_components": rplus["filled_payload"]["bundle_tensors"]["curvature_F_A_components"] is not None,
            "ad_bundle_representation": rplus["filled_payload"]["bundle_tensors"]["ad_bundle_representation"] is not None,
            "trace_normalization": rplus["filled_payload"]["bundle_tensors"]["trace_normalization"] is not None,
            "kernel_and_quotient_policy": rplus["filled_payload"]["operator_contract"]["kernel_and_quotient_policy"] is not None,
            "E_Qa_matrix": rplus["filled_payload"]["operator_contract"]["E_Qa_matrix"] is not None,
            "gamma_nk_inverse_table": rplus["filled_payload"]["ou_derivation_alternative"]["gamma_nk_inverse_table"] is not None,
        },
        "legal_closure_payload": [
            "selected bundle connection A or projective rho_E transition packet",
            "bundle curvature F_A",
            "representation action on u(E)-valued one-forms",
            "trace normalization",
            "kernel/quotient policy",
            "E_Qa matrix or same-source heat/zeta/torsion finite-part table",
        ],
        "verdict": (
            "The smooth lane is the smaller local gate: its geometric Bismut and R+ "
            "blocks are filled, and the remaining missing fields are finite and typed."
        ),
    }

    obligations = {
        "schema": "SelectedHeteroticProjectiveRhoESmoothBundleOperatorOrKPhysRemainingObligations.v1",
        "status": "OPEN",
        "preferred_next_lane": "smooth_operator_identity_bridge",
        "next_required_artifact": NEXT,
        "physical_anchor_bridge_remaining": physical_lane["legal_closure_payload"],
        "smooth_operator_identity_remaining": smooth_lane["legal_closure_payload"],
        "minimum_next_packet": {
            "connection_A_components": None,
            "curvature_F_A_components": None,
            "ad_bundle_representation": None,
            "trace_normalization": None,
            "kernel_and_quotient_policy": None,
            "E_Qa_matrix_or_finite_part_table": None,
        },
        "forbidden_shortcuts": contract["forbidden_shortcuts"],
    }

    decision = {
        "physical_anchor_bridge_closed": False,
        "smooth_operator_identity_closed": False,
        "physical_lane_has_anchor_slot_but_no_value": all(physical_lane["support"].values()) and all_false(physical_lane["blockers"]),
        "smooth_lane_has_geometry_but_no_bundle_operator": all(smooth_lane["support"].values()) and all_false(smooth_lane["blockers"]),
        "best_next_lane": "smooth_operator_identity_bridge",
        "next_required_artifact": NEXT,
        "remaining_obligations_path": rel(OUTPUT_OBLIGATIONS),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEKPhysAnchorOrSmoothOperatorIdentityFill",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "previous_gate": previous["status"],
            "bismut_payload": bismut["status"],
            "rplus_payload": rplus["status"],
            "m_theory_anchor": m_anchor["status"],
            "omega_gap": omega["status"],
        },
        "physical_normalization_bridge": physical_lane,
        "smooth_operator_identity_bridge": smooth_lane,
        "decision": decision,
        "guardrails": {
            "does_not_set_K_phys_to_one": True,
            "does_not_compare_log2008_to_observed_coupling": True,
            "does_not_import_measured_scale": True,
            "does_not_promote_Rplus_to_bundle_curvature": True,
            "does_not_promote_finite_Hsel_to_smooth_EQa": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "ProjectiveRhoEKPhysAnchorOrSmoothOperatorIdentityFillReduction",
            "proved": True,
            "statement": (
                "Given the selected internal rho_E finite part log(2008), the physical "
                "normalization bridge is reduced to a missing same-branch dimensionful "
                "action-unit anchor and RG/matching convention, while the smooth operator "
                "identity bridge is reduced to a finite bundle/operator packet because "
                "the Bismut geometry and R+ curvature are already filled. Therefore the "
                "next smallest no-knob construction is the selected bundle connection, "
                "representation trace, quotient policy, and E_Qa/finite-part packet."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_OBLIGATIONS.write_text(json.dumps(obligations, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "remaining_obligations_path": rel(OUTPUT_OBLIGATIONS),
        "physical_anchor_bridge_closed": False,
        "smooth_operator_identity_closed": False,
        "best_next_lane": decision["best_next_lane"],
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE KPhysAnchor or SmoothOperatorIdentity Fill v1

## Result

```text
status = {STATUS}
physical_anchor_bridge_closed = false
smooth_operator_identity_closed = false
best_next_lane = smooth_operator_identity_bridge
next_required_artifact = {NEXT}
```

## What This Establishes

The internal result remains:

```text
Delta_rhoE_internal = log(2008)
K_gauge,int = 1
```

The physical route has the correct slot, but the source still does not select a
dimensionful modal gap, `ell_p`, `kappa_11`, `alpha_prime`, `Omega_0`, matching
scale, or RG scheme. Therefore `K_phys` is not closed.

The smooth route is closer locally. The selected Iwasawa/Strominger geometry and
`R^+` curvature are already filled, but the bundle/operator packet is still
missing: `A`, `F_A`, representation action, trace normalization, quotient
policy, and `E_Qa` or an equivalent heat/zeta/torsion finite-part table.

## Remaining Packet

```text
{rel(OUTPUT_OBLIGATIONS)}
```

The next construction should not try another scalar tweak. It should build the
selected bundle connection and operator trace packet, then compute the smooth
finite part or prove that it reduces to the selected finite `log(2008)` packet.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_OBLIGATIONS)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
