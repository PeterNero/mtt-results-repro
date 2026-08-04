"""Attempt to fill the two electroweak constants frontier keys."""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
GR = ROOT.parent / "mtt-protospinor-gr-response-proof"

INPUTS = {
    "frontier_interface": DATA / "selected_electroweak_two_key_frontier_interface.candidate.json",
    "u1_template": CERTS / "selected_electroweak_u1y_local_determinant_key.template.json",
    "alpha_template": CERTS / "selected_electroweak_physical_action_anchor_key.template.json",
    "u1_minimal_source_amendment": DATA / "selected_u1_hypercharge_minimal_source_amendment_or_direct_operator_row.candidate.json",
    "u1_operator_packet": DATA / "selected_u1_hypercharge_operator_spectrum_source_packet.candidate.json",
    "physical_alpha_theorem": GR / "certificates" / "selected_physical_alpha_or_action_unit_theorem_certificate.json",
    "dimensional_anchor_search": GR / "certificates" / "target_independent_dimensional_anchor_search_certificate.json",
    "mtheory_anchor_attempt": GR / "certificates" / "m_theory_dimensional_anchor_packet_attempt_certificate.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_two_key_fill_attempt.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_two_key_fill_attempt_certificate.json"
OUTPUT_U1_FILL = DATA / "selected_electroweak_u1y_local_determinant_key.fill_attempt.json"
OUTPUT_ALPHA_FILL = DATA / "selected_electroweak_physical_action_anchor_key.fill_attempt.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_Two_Key_FillAttempt_v1.md"

STATUS = "ELECTROWEAK_TWO_KEY_FILL_ATTEMPT_CURRENT_CORPUS_KEYS_OPEN"
NEXT = "Selected_Electroweak_U1Y_OperatorRow_or_DimensionalAnchor_SourceAugmentation_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any], str]:
    frontier = load(INPUTS["frontier_interface"])
    u1_template = load(INPUTS["u1_template"])
    alpha_template = load(INPUTS["alpha_template"])
    u1_amendment = load(INPUTS["u1_minimal_source_amendment"])
    u1_operator = load(INPUTS["u1_operator_packet"])
    alpha_theorem = load(INPUTS["physical_alpha_theorem"])
    anchor_search = load(INPUTS["dimensional_anchor_search"])
    mtheory = load(INPUTS["mtheory_anchor_attempt"])

    u1_fill = copy.deepcopy(u1_template)
    u1_fill["status"] = "FILL_ATTEMPT_PARTIAL_SUPPORT_OPERATOR_ROW_VALUES_OPEN"
    u1_fill["source_evidence"].update(
        {
            "selected_by_mtt": False,
            "same_scheme_as_Qa_SU3_and_SU2": False,
            "source_certificate": None,
            "operator_row_emitted_before_electroweak_comparison": False,
        }
    )
    u1_fill["operator_domain"].update(
        {
            "P_perp_policy_used": True,
            "boundary_or_compact_quotient_domain": None,
            "zero_mode_policy": "shared central-circle line removed by P_perp; positive threshold operator still absent",
        }
    )
    u1_fill["u1y_operator_row"].update(
        {
            "operator_identity": None,
            "connection_or_transition_data": None,
            "projective_rhoE_or_D_E": None,
            "hypercharge_normalization": "structural support only; not selected same-scheme threshold normalization",
            "index_weight_policy": "P_perp trace index 2/3 is selected, but determinant weights are open",
        }
    )
    u1_fill["spectrum_or_finite_part"].update(
        {
            "positive_eigenvalues": None,
            "multiplicities": None,
            "zeta_heat_or_torsion_finite_part": None,
            "regularization_scale_policy": None,
            "lambda_12_contribution": None,
        }
    )
    u1_fill["guardrails"].update(
        {
            "P_perp_not_used_as_spectrum": True,
            "central_circle_not_double_counted": True,
            "Qa_log2008_not_injected_into_U1Y": True,
            "lambda12_target_not_used": True,
        }
    )

    alpha_fill = copy.deepcopy(alpha_template)
    alpha_fill["status"] = "FILL_ATTEMPT_STRUCTURAL_SLOT_FILLED_DIMENSIONFUL_VALUE_OPEN"
    alpha_fill["source_evidence"].update(
        {
            "selected_by_mtt": False,
            "target_independent": True,
            "source_certificate": None,
            "computed_before_Newton_Planck_mass_cosmology_or_gauge_comparison": True,
        }
    )
    alpha_fill["dimensionful_anchor"].update(
        {
            "kind": anchor_search["verdict"]["best_route"],
            "value": None,
            "unit_convention": "canonical internal action units closed; physical SI/metrological unit open",
            "map_to_alpha_phys": alpha_theorem["final_reduction"]["alpha_phys_if_Omega0_were_independently_measured"],
        }
    )
    alpha_fill["candidate_routes"].update(anchor_search["route_table"])
    alpha_fill["guardrails"].update(
        {
            "internal_alpha_1_not_physical_SI_prediction": True,
            "no_Newton_or_Planck_backsolve": True,
            "no_Theta_5TeV_calibration": True,
            "no_unit_convention_as_prediction": True,
        }
    )

    u1_attempt_result = {
        "filled_support": {
            "P_perp_policy": True,
            "bad_shortcuts_rejected": True,
            "operator_source_live_route": u1_amendment["decision"]["strongest_live_route"],
            "operator_packet_contract": u1_operator["acceptance_contract"]["closed_now"]["source_packet_acceptance_contract"],
        },
        "blocking_fields": [
            "source_evidence.selected_by_mtt",
            "source_evidence.same_scheme_as_Qa_SU3_and_SU2",
            "u1y_operator_row.operator_identity",
            "u1y_operator_row.projective_rhoE_or_D_E",
            "spectrum_or_finite_part.positive_eigenvalues",
            "spectrum_or_finite_part.zeta_heat_or_torsion_finite_part",
            "spectrum_or_finite_part.lambda_12_contribution",
        ],
        "promotes": False,
    }

    alpha_attempt_result = {
        "filled_support": {
            "best_route": anchor_search["verdict"]["best_route"],
            "m_theory_slot_identified": mtheory["closure_tests"]["m_theory_slot_identified"],
            "Omega0_formula": alpha_theorem["final_reduction"]["Omega0"],
            "Omega0_over_sqrt_alpha_phys": alpha_theorem["final_reduction"]["Omega0_over_sqrt_alpha_phys"],
        },
        "blocking_fields": mtheory["promotion"]["blocking_fields"],
        "promotes": False,
    }

    decision = {
        "u1y_local_determinant_key_promoted": False,
        "physical_action_anchor_key_promoted": False,
        "typed_convention_rg_key_promoted": False,
        "measured_electroweak_closure": False,
        "current_corpus_exhausted_for_two_key_closure": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedElectroweakTwoKeyFillAttempt",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "frontier_interface": frontier["status"],
            "u1_minimal_source_amendment": u1_amendment["status"],
            "u1_operator_packet": u1_operator["status"],
            "physical_alpha_theorem": alpha_theorem["status"],
            "dimensional_anchor_search": anchor_search["status"],
            "mtheory_anchor_attempt": mtheory["status"],
        },
        "u1y_local_determinant_key_fill_path": rel(OUTPUT_U1_FILL),
        "physical_action_anchor_key_fill_path": rel(OUTPUT_ALPHA_FILL),
        "u1y_local_determinant_key_attempt": u1_attempt_result,
        "physical_action_anchor_key_attempt": alpha_attempt_result,
        "decision": decision,
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_Newton_or_Planck_backsolve": False,
            "uses_lambda12_target_witness": False,
            "promotes_internal_units_as_physical_prediction": False,
            "promotes_projector_as_spectrum": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakTwoKeyFillAttempt",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "u1_fill_path": rel(OUTPUT_U1_FILL),
        "alpha_fill_path": rel(OUTPUT_ALPHA_FILL),
        "note_path": rel(OUTPUT_NOTE),
        "closed": {
            "fill_attempt_executed": True,
            "u1_support_fields_partially_filled": True,
            "alpha_structural_slot_partially_filled": True,
            "forbidden_shortcuts_rejected": True,
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
    return candidate, cert, u1_fill, alpha_fill, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    u1 = candidate["u1y_local_determinant_key_attempt"]
    alpha = candidate["physical_action_anchor_key_attempt"]
    return f"""# Selected Electroweak Two Key FillAttempt v1

## Result

```text
status = {candidate["status"]}
u1y_local_determinant_key_promoted = false
physical_action_anchor_key_promoted = false
measured_electroweak_closure = false
current_corpus_exhausted_for_two_key_closure = true
```

## U1/Y Key

Filled support:

```json
{json.dumps(u1["filled_support"], indent=2, sort_keys=True)}
```

Blocking fields:

```json
{json.dumps(u1["blocking_fields"], indent=2)}
```

## Physical Action Anchor Key

Filled support:

```json
{json.dumps(alpha["filled_support"], indent=2, sort_keys=True)}
```

Blocking fields:

```json
{json.dumps(alpha["blocking_fields"], indent=2)}
```

## Next

```text
{candidate["decision"]["next_required_artifact"]}
```

This is now a source-augmentation problem: supply either the selected U1/Y
operator row with finite determinant data, or a selected target-independent
dimensionful action anchor.

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, u1_fill, alpha_fill, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    write_json(OUTPUT_U1_FILL, u1_fill)
    write_json(OUTPUT_ALPHA_FILL, alpha_fill)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_U1_FILL, OUTPUT_ALPHA_FILL, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
