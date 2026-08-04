"""Build the two-key electroweak constants frontier interface.

This keeps the constants/electroweak branch separate from the SM flavor/C1
matrix branch.  The current corpus has closed a strong internal kernel, but a
physical electroweak prediction still needs two independent selected objects:

1. a U1/Y local determinant threshold row;
2. a physical action/dimensional anchor.
"""

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
    "dual_frontier": DATA / "dual_attack_local_determinant_or_omega0_source.candidate.json",
    "physical_threshold_vector": DATA / "selected_physical_gauge_anchor_and_electroweak_threshold_vector.candidate.json",
    "u1_spectrum_attempt": DATA / "selected_u1_hypercharge_local_determinant_spectrum_attempt.candidate.json",
    "u1_operator_packet": DATA / "selected_u1_hypercharge_operator_spectrum_source_packet.candidate.json",
    "u1_minimal_source_amendment": DATA / "selected_u1_hypercharge_minimal_source_amendment_or_direct_operator_row.candidate.json",
    "physical_alpha_theorem": GR / "certificates" / "selected_physical_alpha_or_action_unit_theorem_certificate.json",
    "dimensional_anchor_search": GR / "certificates" / "target_independent_dimensional_anchor_search_certificate.json",
    "mtheory_anchor_attempt": GR / "certificates" / "m_theory_dimensional_anchor_packet_attempt_certificate.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_two_key_frontier_interface.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_two_key_frontier_interface_certificate.json"
OUTPUT_U1_TEMPLATE = CERTS / "selected_electroweak_u1y_local_determinant_key.template.json"
OUTPUT_ALPHA_TEMPLATE = CERTS / "selected_electroweak_physical_action_anchor_key.template.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_Two_Key_Frontier_Interface_v1.md"

STATUS = "ELECTROWEAK_TWO_KEY_FRONTIER_INTERFACE_BUILT_KEYS_OPEN"
NEXT = "Selected_Electroweak_Two_Key_FillAttempt_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def u1_template() -> dict[str, Any]:
    return {
        "status": "OPEN_SELECTED_ELECTROWEAK_U1Y_LOCAL_DETERMINANT_KEY_REQUIRED",
        "schema": "SelectedElectroweakU1YLocalDeterminantKey.v1",
        "source_evidence": {
            "selected_by_mtt": None,
            "same_scheme_as_Qa_SU3_and_SU2": None,
            "source_certificate": None,
            "operator_row_emitted_before_electroweak_comparison": None,
        },
        "operator_domain": {
            "carrier": "V/<s>",
            "P_perp_policy_used": None,
            "boundary_or_compact_quotient_domain": None,
            "zero_mode_policy": None,
        },
        "u1y_operator_row": {
            "operator_identity": None,
            "connection_or_transition_data": None,
            "projective_rhoE_or_D_E": None,
            "hypercharge_normalization": None,
            "index_weight_policy": None,
        },
        "spectrum_or_finite_part": {
            "positive_eigenvalues": None,
            "multiplicities": None,
            "zeta_heat_or_torsion_finite_part": None,
            "regularization_scale_policy": None,
            "lambda_12_contribution": None,
        },
        "guardrails": {
            "P_perp_not_used_as_spectrum": None,
            "central_circle_not_double_counted": None,
            "Qa_log2008_not_injected_into_U1Y": None,
            "lambda12_target_not_used": None,
        },
    }


def alpha_template() -> dict[str, Any]:
    return {
        "status": "OPEN_SELECTED_ELECTROWEAK_PHYSICAL_ACTION_ANCHOR_KEY_REQUIRED",
        "schema": "SelectedElectroweakPhysicalActionAnchorKey.v1",
        "source_evidence": {
            "selected_by_mtt": None,
            "target_independent": None,
            "source_certificate": None,
            "computed_before_Newton_Planck_mass_cosmology_or_gauge_comparison": None,
        },
        "dimensionful_anchor": {
            "kind": None,
            "value": None,
            "unit_convention": None,
            "map_to_alpha_phys": None,
            "map_to_Omega0": "Omega0 = sqrt(alpha_phys) * sqrt(15/log(448))",
        },
        "candidate_routes": {
            "m_theory_modal_gap_planck_anchor": None,
            "proper_time_tau": None,
            "flux_bianchi_alpha_prime": None,
            "coherence_capacity": None,
        },
        "guardrails": {
            "internal_alpha_1_not_physical_SI_prediction": None,
            "no_Newton_or_Planck_backsolve": None,
            "no_Theta_5TeV_calibration": None,
            "no_unit_convention_as_prediction": None,
        },
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any], str]:
    dual = load(INPUTS["dual_frontier"])
    physical = load(INPUTS["physical_threshold_vector"])
    u1_attempt = load(INPUTS["u1_spectrum_attempt"])
    u1_operator = load(INPUTS["u1_operator_packet"])
    u1_amendment = load(INPUTS["u1_minimal_source_amendment"])
    alpha = load(INPUTS["physical_alpha_theorem"])
    anchor_search = load(INPUTS["dimensional_anchor_search"])
    mtheory = load(INPUTS["mtheory_anchor_attempt"])

    u1_key_status = {
        "P_perp_quotient_index_closed": u1_attempt["source_checks"]["p_perp_rank_two"],
        "bad_spectrum_shortcuts_rejected": (
            u1_attempt["attempts"]["quotient_identity"]["status"].startswith("REJECTED")
            and u1_attempt["attempts"]["central_circle_reuse"]["status"].startswith("REJECTED")
        ),
        "operator_packet_contract_built": u1_operator["acceptance_contract"]["closed_now"]["source_packet_acceptance_contract"],
        "minimal_source_amendment_audited": u1_amendment["decision"]["minimal_source_amendment_gate_built"],
        "strongest_live_route": u1_amendment["decision"]["strongest_live_route"],
        "operator_row_found": u1_amendment["decision"]["direct_operator_row_found"],
        "lambda_12_closed": u1_amendment["decision"]["lambda_12_closed"],
    }

    alpha_key_status = {
        "Omega0_formula": alpha["final_reduction"]["Omega0"],
        "Omega0_over_sqrt_alpha_phys": alpha["final_reduction"]["Omega0_over_sqrt_alpha_phys"],
        "internal_alpha_closed": alpha["theorem_result"]["alpha_int"] == 1.0,
        "physical_numeric_alpha_selected": alpha["theorem_result"]["physical_numeric_alpha_selected"],
        "best_structural_route": anchor_search["verdict"]["best_route"],
        "best_structural_route_status": anchor_search["verdict"]["best_route_status"],
        "m_theory_slot_identified": mtheory["closure_tests"]["m_theory_slot_identified"],
        "m_theory_dimensionful_value_present": mtheory["closure_tests"]["dimensionful_value_present"],
        "m_theory_selected_by_mtt": mtheory["closure_tests"]["selected_by_mtt"],
    }

    internal_kernel = physical["theorem"]["selected_internal_inputs"]
    two_key_logic = {
        "internal_kernel_closed": physical["source_checks"]["internal_kernel_closed"],
        "selected_internal_kernel": internal_kernel,
        "Omega0_reduced_to_alpha_phys": dual["lane_B_omega0"]["status"] == "REDUCED_TO_ALPHA_PHYS_OR_ACTION_UNIT_ONLY",
        "lambda12_reduced_to_spectral_table": dual["lane_A_local_determinant"]["status"] == "OPEN_SELECTED_GAUGE_FACTOR_SPECTRAL_TABLE_REQUIRED",
        "u1_key_can_replace_alpha_key": False,
        "alpha_key_can_replace_u1_key": False,
        "why_two_keys": (
            "The U1/Y determinant key supplies a dimensionless gauge-factor threshold "
            "difference. The physical action-anchor key supplies absolute physical units. "
            "Neither one logically determines the other."
        ),
    }

    decision = {
        "electroweak_internal_kernel_closed": True,
        "u1y_local_determinant_key_closed": False,
        "physical_action_anchor_key_closed": False,
        "typed_convention_rg_key_closed": False,
        "measured_electroweak_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    u1_tmpl = u1_template()
    alpha_tmpl = alpha_template()
    candidate = {
        "candidate": "SelectedElectroweakTwoKeyFrontierInterface",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "dual_frontier": dual["status"],
            "physical_threshold_vector": physical["status"],
            "u1_spectrum_attempt": u1_attempt["status"],
            "u1_operator_packet": u1_operator["status"],
            "u1_minimal_source_amendment": u1_amendment["status"],
            "physical_alpha_theorem": alpha["status"],
            "dimensional_anchor_search": anchor_search["status"],
            "mtheory_anchor_attempt": mtheory["status"],
        },
        "two_key_logic": two_key_logic,
        "u1y_local_determinant_key_status": u1_key_status,
        "physical_action_anchor_key_status": alpha_key_status,
        "templates": {
            "u1y_local_determinant_key": rel(OUTPUT_U1_TEMPLATE),
            "physical_action_anchor_key": rel(OUTPUT_ALPHA_TEMPLATE),
        },
        "promotion_rule": [
            "Fill the U1/Y local determinant key from a selected same-scheme operator row on V/<s>.",
            "Fill the physical action-anchor key from a target-independent dimensionful source.",
            "Add typed electroweak convention map, mu_match, and RG/threshold scheme before measured comparison.",
            "Then run forward prediction without observed electroweak inputs or target witnesses.",
        ],
        "guardrails": {
            "do_not_promote_internal_alpha_1_to_physical_SI": True,
            "do_not_use_Newton_or_Planck_backsolve": True,
            "do_not_use_lambda12_target_witness": True,
            "do_not_use_Pperp_as_spectrum": True,
            "do_not_inject_Qa_log2008_into_U1Y_row": True,
            "do_not_claim_measured_electroweak_closure": True,
        },
        "decision": decision,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakTwoKeyFrontierInterface",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "u1_template_path": rel(OUTPUT_U1_TEMPLATE),
        "alpha_template_path": rel(OUTPUT_ALPHA_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "closed": {
            "internal_kernel_closed": True,
            "two_key_frontier_formalized": True,
            "u1y_key_template_built": True,
            "physical_action_anchor_template_built": True,
            "forbidden_shortcuts_named": True,
        },
        "open": {
            "u1y_local_determinant_key": True,
            "physical_action_anchor_key": True,
            "typed_convention_rg_scheme": True,
            "measured_electroweak_closure": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, u1_tmpl, alpha_tmpl, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    u1 = candidate["u1y_local_determinant_key_status"]
    alpha = candidate["physical_action_anchor_key_status"]
    kernel = candidate["two_key_logic"]["selected_internal_kernel"]
    return f"""# Selected Electroweak Two Key Frontier Interface v1

## Result

The constants/electroweak branch is reduced to two independent open keys.

```text
I_U1 = {kernel["I_U1"]}
I_SU2 = {kernel["I_SU2"]}
I_Qa_or_SU3 = {kernel["I_Qa_or_SU3"]}
K_gauge_int = {kernel["K_gauge_int"]}

u1y_local_determinant_key_closed = false
physical_action_anchor_key_closed = false
measured_electroweak_closure = false
```

## Key 1: U1/Y Local Determinant

```text
P_perp_quotient_index_closed = {u1["P_perp_quotient_index_closed"]}
bad_spectrum_shortcuts_rejected = {u1["bad_spectrum_shortcuts_rejected"]}
operator_packet_contract_built = {u1["operator_packet_contract_built"]}
strongest_live_route = {u1["strongest_live_route"]}
operator_row_found = {u1["operator_row_found"]}
lambda_12_closed = {u1["lambda_12_closed"]}
```

This key must emit the selected U1/Y threshold operator row on `V/<s>` and its
positive spectrum or zeta/heat/torsion finite part. The `P_perp` quotient is an
index/carrier result, not a spectrum.

## Key 2: Physical Action Anchor

```text
Omega0 = {alpha["Omega0_formula"]}
Omega0_over_sqrt_alpha_phys = {alpha["Omega0_over_sqrt_alpha_phys"]}
internal_alpha_closed = {alpha["internal_alpha_closed"]}
physical_numeric_alpha_selected = {alpha["physical_numeric_alpha_selected"]}
best_structural_route = {alpha["best_structural_route"]}
best_structural_route_status = {alpha["best_structural_route_status"]}
```

This key must supply a target-independent dimensional anchor. Internal
`alpha=1` is closed only as canonical internal action units, not as an SI
prediction.

## Next

```text
{candidate["decision"]["next_required_artifact"]}
```

The next fill attempt must try both templates and report whether either key can
be promoted from current corpus data.

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, u1_tmpl, alpha_tmpl, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    write_json(OUTPUT_U1_TEMPLATE, u1_tmpl)
    write_json(OUTPUT_ALPHA_TEMPLATE, alpha_tmpl)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_U1_TEMPLATE, OUTPUT_ALPHA_TEMPLATE, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
