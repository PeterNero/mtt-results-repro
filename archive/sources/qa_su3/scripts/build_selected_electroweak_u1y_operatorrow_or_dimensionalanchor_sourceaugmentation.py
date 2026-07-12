"""Build the electroweak U1/Y-or-dimensional-anchor source-augmentation gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
GR = ROOT.parent / "mtt-protospinor-gr-response-proof"

INPUTS = {
    "two_key_fill_attempt": DATA / "selected_electroweak_two_key_fill_attempt.candidate.json",
    "u1_key_fill_attempt": DATA / "selected_electroweak_u1y_local_determinant_key.fill_attempt.json",
    "alpha_key_fill_attempt": DATA / "selected_electroweak_physical_action_anchor_key.fill_attempt.json",
    "u1_minimal_source_amendment": DATA / "selected_u1_hypercharge_minimal_source_amendment_or_direct_operator_row.candidate.json",
    "u1_operator_source_packet": DATA / "selected_u1_hypercharge_operator_spectrum_source_packet.candidate.json",
    "physical_alpha_theorem": GR / "certificates" / "selected_physical_alpha_or_action_unit_theorem_certificate.json",
    "dimensional_anchor_search": GR / "certificates" / "target_independent_dimensional_anchor_search_certificate.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_u1y_operatorrow_or_dimensionalanchor_sourceaugmentation.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_u1y_operatorrow_or_dimensionalanchor_sourceaugmentation_certificate.json"
OUTPUT_U1_TEMPLATE = DATA / "selected_electroweak_u1y_operator_row_source_packet.template.json"
OUTPUT_ANCHOR_TEMPLATE = DATA / "selected_electroweak_dimensional_action_anchor_source_packet.template.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_U1Y_OperatorRow_or_DimensionalAnchor_SourceAugmentation_v1.md"

STATUS = "ELECTROWEAK_U1Y_OR_DIMENSIONAL_ANCHOR_SOURCE_AUGMENTATION_BUILT_VALUES_OPEN"
NEXT = "Selected_Electroweak_U1Y_OperatorRow_SourcePacket_or_PhysicalActionAnchor_ValuePacket_Fill_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build_u1_template(u1_key: dict[str, Any], u1_amendment: dict[str, Any], u1_operator: dict[str, Any]) -> dict[str, Any]:
    required_fields = u1_operator["route_tests"]["same_source_operator_spectrum_packet"]["required_fields"]
    source_fields = [field["field"] for field in u1_amendment["source_amendment_fields"]]
    return {
        "schema": "SelectedElectroweakU1YOperatorRowSourcePacket.v1",
        "status": "OPEN_SELECTED_U1Y_OPERATOR_ROW_SOURCE_PACKET_REQUIRED",
        "carrier": u1_key["operator_domain"]["carrier"],
        "source_identity": {
            "selected_by_mtt": None,
            "source_certificate": None,
            "same_source_as_internal_kernel": None,
            "emitted_before_electroweak_comparison": None,
            "live_route": u1_amendment["decision"]["strongest_live_route"],
        },
        "domain_and_quotient": {
            "compact_domain_or_boundary_condition": None,
            "shared_circle_vector_s": "selected qutrit representative already closed; must be re-emitted or referenced by this operator packet",
            "P_perp_policy": "operator acts on V/<s>; P_perp is zero-mode quotient only, not the spectrum",
            "central_circle_double_counting_forbidden": True,
        },
        "operator_row": {
            "operator_identity": None,
            "connection_transition_or_cocycle_data": None,
            "projective_rhoE_or_D_E": None,
            "Chern_Weil_or_threshold_functional": None,
            "hypercharge_normalization": None,
            "same_scheme_SU2_row_reference": None,
        },
        "finite_part": {
            "positive_eigenvalues": None,
            "multiplicities": None,
            "index_or_Dynkin_weights": None,
            "zeta_heat_torsion_or_equivalent_finite_part": None,
            "regularization_scale_policy": None,
            "lambda_12_contribution": None,
        },
        "acceptance_contract": {
            "required_operator_packet_fields": required_fields,
            "minimal_source_amendment_fields": source_fields,
            "must_not_use": u1_operator["acceptance_contract"]["must_not_use"],
        },
    }


def build_anchor_template(alpha_key: dict[str, Any], alpha_theorem: dict[str, Any], anchor_search: dict[str, Any]) -> dict[str, Any]:
    best = anchor_search["verdict"]["best_route"]
    return {
        "schema": "SelectedElectroweakDimensionalActionAnchorSourcePacket.v1",
        "status": "OPEN_SELECTED_DIMENSIONAL_ACTION_ANCHOR_SOURCE_PACKET_REQUIRED",
        "source_identity": {
            "selected_by_mtt": None,
            "source_certificate": None,
            "target_independent": True,
            "computed_before_Newton_Planck_mass_cosmology_or_gauge_comparison": None,
        },
        "dimensionful_anchor": {
            "kind": best,
            "value": None,
            "units": None,
            "physical_inverse_length_or_action_unit": None,
            "map_to_ell_p_kappa11_alpha_prime": None,
            "map_to_alpha_phys": alpha_key["dimensionful_anchor"]["map_to_alpha_phys"],
            "map_to_Omega0": alpha_key["dimensionful_anchor"]["map_to_Omega0"],
        },
        "structural_support": {
            "internal_alpha_closed": alpha_theorem["closed_inputs"]["internal_alpha_equals_one"],
            "internal_G10_closed": alpha_theorem["closed_inputs"]["internal_G10_equals_one"],
            "best_route_status": anchor_search["verdict"]["best_route_status"],
            "best_route_closed_support": anchor_search["route_table"][best]["closed"],
        },
        "acceptance_contract": {
            "must_supply": anchor_search["route_table"][best]["next_packet_fields"],
            "must_not_use": [
                "observed Newton constant",
                "observed Planck mass or Planck length",
                "observed cosmological density",
                "Theta 5 TeV calibration",
                "unit convention as physical prediction",
                "electroweak measured couplings",
            ],
        },
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any], str]:
    two_key = load(INPUTS["two_key_fill_attempt"])
    u1_key = load(INPUTS["u1_key_fill_attempt"])
    alpha_key = load(INPUTS["alpha_key_fill_attempt"])
    u1_amendment = load(INPUTS["u1_minimal_source_amendment"])
    u1_operator = load(INPUTS["u1_operator_source_packet"])
    alpha_theorem = load(INPUTS["physical_alpha_theorem"])
    anchor_search = load(INPUTS["dimensional_anchor_search"])

    u1_template = build_u1_template(u1_key, u1_amendment, u1_operator)
    anchor_template = build_anchor_template(alpha_key, alpha_theorem, anchor_search)

    source_augmentation_gate = {
        "u1y_operator_row_branch": {
            "template_path": rel(OUTPUT_U1_TEMPLATE),
            "primary_gain_if_filled": "computes the dimensionless U1/Y local determinant contribution and lambda_12 lane",
            "cannot_replace": "physical action anchor alpha_phys/Omega0",
            "first_blocking_field": "operator_row.operator_identity",
            "status": u1_template["status"],
        },
        "dimensional_action_anchor_branch": {
            "template_path": rel(OUTPUT_ANCHOR_TEMPLATE),
            "primary_gain_if_filled": "sets physical action/unit normalization for Omega0 and absolute coupling units",
            "cannot_replace": "U1/Y local determinant threshold row",
            "first_blocking_field": "dimensionful_anchor.value",
            "status": anchor_template["status"],
        },
        "joint_promotion_rule": {
            "either_branch_may_be_filled_next": True,
            "measured_electroweak_closure_requires_both_branches": True,
            "also_requires": [
                "typed electroweak convention map",
                "matching scale or cancellation theorem",
                "RG/threshold scheme emitted before data comparison",
            ],
        },
    }

    route_priority = [
        {
            "route": "U1Y_operator_row_source_packet",
            "why_first": "dimensionless, same-source, and directly adjacent to the closed P_perp and U1/Y operator-row corpus; it can close lambda_12 without selecting physical units.",
            "risk": "requires actual operator/spectrum values, not another structural hypercharge packet",
        },
        {
            "route": "dimensional_action_anchor_source_packet",
            "why_second": "would set the absolute physical unit, but the sibling GR repo has an explicit dimensionful-obstruction theorem and only a structural M-theory slot so far.",
            "risk": "easy to accidentally backsolve from Planck/Newton/TeV data; guardrails must remain strict",
        },
    ]

    decision = {
        "source_augmentation_gate_built": True,
        "u1y_operator_row_packet_closed": False,
        "dimensional_action_anchor_packet_closed": False,
        "measured_electroweak_closure": False,
        "target_fitting_used": False,
        "recommended_next_fill": route_priority[0]["route"],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedElectroweakU1YOperatorRowOrDimensionalAnchorSourceAugmentation",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "two_key_fill_attempt": two_key["status"],
            "u1_key_fill_attempt": u1_key["status"],
            "alpha_key_fill_attempt": alpha_key["status"],
            "u1_minimal_source_amendment": u1_amendment["status"],
            "u1_operator_source_packet": u1_operator["status"],
            "physical_alpha_theorem": alpha_theorem["status"],
            "dimensional_anchor_search": anchor_search["status"],
        },
        "source_augmentation_gate": source_augmentation_gate,
        "route_priority": route_priority,
        "decision": decision,
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_lambda12_target_witness": False,
            "uses_Newton_or_Planck_backsolve": False,
            "uses_Theta_5TeV_calibration": False,
            "promotes_projector_as_spectrum": False,
            "claims_dimensionful_constant_from_dimensionless_data": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakU1YOperatorRowOrDimensionalAnchorSourceAugmentation",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "u1_operator_row_template_path": rel(OUTPUT_U1_TEMPLATE),
        "dimensional_action_anchor_template_path": rel(OUTPUT_ANCHOR_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "closed": {
            "two_branch_source_augmentation_gate": True,
            "u1y_operator_row_acceptance_contract": True,
            "dimensional_anchor_acceptance_contract": True,
            "joint_promotion_rule": True,
        },
        "open": {
            "selected_u1y_operator_row_values": True,
            "selected_dimensional_action_anchor_value": True,
            "measured_electroweak_closure": True,
        },
        "recommended_next_fill": decision["recommended_next_fill"],
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, u1_template, anchor_template, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    gate = candidate["source_augmentation_gate"]
    return f"""# Selected Electroweak U1Y OperatorRow or DimensionalAnchor SourceAugmentation v1

## Result

```text
status = {candidate["status"]}
u1y_operator_row_packet_closed = false
dimensional_action_anchor_packet_closed = false
measured_electroweak_closure = false
recommended_next_fill = {candidate["decision"]["recommended_next_fill"]}
```

## U1/Y Branch

```json
{json.dumps(gate["u1y_operator_row_branch"], indent=2, sort_keys=True)}
```

## Dimensional Anchor Branch

```json
{json.dumps(gate["dimensional_action_anchor_branch"], indent=2, sort_keys=True)}
```

## Joint Promotion Rule

```json
{json.dumps(gate["joint_promotion_rule"], indent=2, sort_keys=True)}
```

The practical next move is to try the U1/Y operator-row packet first: it is
dimensionless and can close the `lambda_12` lane without pretending to solve
the absolute physical unit problem.  The dimensional-anchor packet remains
available as the parallel route, but it must supply an actual target-independent
dimensionful value.

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, u1_template, anchor_template, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    write_json(OUTPUT_U1_TEMPLATE, u1_template)
    write_json(OUTPUT_ANCHOR_TEMPLATE, anchor_template)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_U1_TEMPLATE, OUTPUT_ANCHOR_TEMPLATE, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
