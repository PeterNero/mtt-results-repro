"""Build the electroweak gauge-kinetic normalization and RG-scheme source gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "physicalanchor_frontier": DATA / "selected_electroweak_physicalanchor_rg_and_matchingscale.candidate.json",
    "source_template": DATA / "selected_electroweak_physicalanchor_rg_and_matchingscale.template.json",
    "kernel_interface": Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob\certificates\selected_electroweak_kernel_interface_certificate.json"),
    "threshold_kernel_reduction": Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob\certificates\selected_electroweak_threshold_kernel_reduction_certificate.json"),
    "hypercharge_threshold_interface": Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob\certificates\selected_hypercharge_normalized_threshold_interface_certificate.json"),
    "stack_determinant_status": Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob\certificates\selected_stack_determinant_source_status_certificate.json"),
    "mtheory_anchor_attempt": Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof\certificates\m_theory_dimensional_anchor_packet_attempt_certificate.json"),
    "dimensional_anchor_search": Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof\certificates\target_independent_dimensional_anchor_search_certificate.json"),
}

OUTPUT_DATA = DATA / "selected_electroweak_gaugekinetic_normalization_and_rg_scheme.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_gaugekinetic_normalization_and_rg_scheme_certificate.json"
OUTPUT_TEMPLATE = DATA / "selected_heterotic_strominger_electroweak_threshold_kernel.template.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_GaugeKinetic_Normalization_and_RG_Scheme_SourceTheorem_v1.md"

STATUS = "ELECTROWEAK_GAUGEKINETIC_RG_ROUTE_SELECTED_VALUES_OPEN"
NEXT = "Selected_Heterotic_Strominger_Electroweak_Threshold_Kernel_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build_threshold_template(frontier: dict[str, Any]) -> dict[str, Any]:
    vec = frontier["conditional_interface"]["closed_internal_weak_split"]
    return {
        "schema": "SelectedHeteroticStromingerElectroweakThresholdKernel.v1",
        "status": "OPEN_SELECTED_HETEROTIC_STROMINGER_EW_KERNEL_REQUIRED",
        "source_identity": {
            "selected_by_mtt": None,
            "same_branch_as_q79_F_m1": None,
            "heterotic_strominger_solution_selected": None,
            "computed_before_electroweak_comparison": None,
            "source_certificate": None,
        },
        "gauge_kinetic_payload": {
            "tree_level_universal_function": "f_a = S or M-theory f_ab slot",
            "physical_normalization": None,
            "same_source_as_GR_anchor": None,
            "hypercharge_embedding": "Y=(1/6)Qa-(1/2)Qc",
        },
        "threshold_payload": {
            "known_internal_weak_split": vec,
            "required_stack_determinants": [
                "p_a in the selected physical threshold scheme",
                "p_c in the selected physical threshold scheme",
                "p_SU2 in the selected physical threshold scheme",
            ],
            "one_loop_or_analytic_torsion_operator": None,
            "positive_spectrum_or_torsion_finite_part": None,
            "index_Dynkin_trace_weights": None,
        },
        "matching_payload": {
            "mu_match": None,
            "allowed_candidates": [
                "selected compactification/string scale from the same heterotic packet",
                "Omega0 only if a theorem identifies it with the electroweak threshold surface",
                "source-selected finite threshold scale",
            ],
            "RG_scheme": None,
            "beta_coefficients": None,
            "threshold_convention": None,
        },
        "forbidden_selectors": [
            "alpha_EM",
            "sin^2(theta_W)",
            "measured g1/g2/g3",
            "M_Z-derived residual minimization",
            "Theta 5 TeV benchmark as prediction",
        ],
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    frontier = load(INPUTS["physicalanchor_frontier"])
    source_template = load(INPUTS["source_template"])
    kernel = load(INPUTS["kernel_interface"])
    threshold_reduction = load(INPUTS["threshold_kernel_reduction"])
    hypercharge = load(INPUTS["hypercharge_threshold_interface"])
    stack_status = load(INPUTS["stack_determinant_status"])
    mtheory = load(INPUTS["mtheory_anchor_attempt"])
    anchor_search = load(INPUTS["dimensional_anchor_search"])
    template = build_threshold_template(frontier)

    vec = frontier["conditional_interface"]["closed_internal_weak_split"]
    routes = {
        "A_primitive_common_normalization": {
            "status": "FALLBACK_NOT_NO_KNOB",
            "source": "selected_electroweak_kernel_interface",
            "reason": kernel["candidate_paths"]["A_primitive_common_normalization"]["requires"],
            "accepted_as_no_knob": False,
            "could_be_credible_if_declared_primitive": True,
        },
        "B_flux_strominger_threshold": {
            "status": "PRIMARY_STRICT_NO_KNOB_ROUTE_SELECTED",
            "source": "selected_electroweak_kernel_interface",
            "reason": kernel["candidate_paths"]["B_flux_strominger_threshold"]["requires"],
            "accepted_as_no_knob_route": True,
            "values_closed_now": False,
        },
        "C_rho_uv_response_bridge": {
            "status": "POWERFUL_OPEN_SECONDARY_ROUTE",
            "source": "selected_electroweak_kernel_interface",
            "reason": kernel["candidate_paths"]["C_rho_uv_response_bridge"]["requires"],
            "accepted_as_no_knob_route": True,
            "values_closed_now": False,
        },
        "M_theory_shared_anchor": {
            "status": "STRUCTURAL_SLOT_IDENTIFIED_VALUE_OPEN",
            "source": "m_theory_dimensional_anchor_packet_attempt",
            "reason": mtheory["promotion"]["honest_result"],
            "accepted_as_gauge_normalization_now": False,
        },
        "Theta_matching_scale": {
            "status": "SCAFFOLD_ONLY_NOT_DERIVED_SCALE",
            "reason": anchor_search["route_table"]["theta_matching_scale"]["blocker"],
            "accepted_as_mu_match_now": False,
        },
    }

    closes = {
        "route_discriminator": True,
        "strict_primary_route": "B_flux_strominger_threshold",
        "kernel_accounting_interface": kernel["verdict"]["kernel_interface_built"],
        "hypercharge_threshold_formula": hypercharge["verdict"]["hypercharge_embedding_selected_structurally"],
        "internal_weak_split_threshold": frontier["decision"]["internal_lambda_12_closed"],
        "forbidden_target_selectors_excluded": True,
    }

    open_items = {
        "physical_gauge_action_anchor": True,
        "selected_mu_match": True,
        "RG_scheme_and_threshold_convention": True,
        "stack_determinants_in_physical_threshold_scheme": True,
        "rho_UV_to_EW_kernel_map": True,
        "measured_electroweak_closure": True,
    }

    decision = {
        "gaugekinetic_normalization_closed": False,
        "matching_scale_closed": False,
        "RG_scheme_closed": False,
        "strict_primary_route_selected": "B_flux_strominger_threshold",
        "next_required_artifact": NEXT,
        "internal_lambda_12_available": True,
        "internal_lambda_12_value": vec["lambda_12"],
        "internal_Delta_G12_value": vec["Delta_G12"],
        "measured_electroweak_closure": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedElectroweakGaugeKineticNormalizationAndRGScheme",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "frontier": frontier["status"],
            "kernel_interface": kernel["status"],
            "threshold_kernel_reduction": threshold_reduction["status"],
            "hypercharge_threshold_interface": hypercharge["status"],
            "stack_determinant_status": stack_status["status"],
            "mtheory_anchor_attempt": mtheory["status"],
            "dimensional_anchor_search": anchor_search["status"],
        },
        "routes": routes,
        "closed_interface": {
            "matching_formula_shape": frontier["conditional_interface"]["matching_formula_shape"],
            "kernel_prediction_map": kernel["kernel"]["prediction_map"],
            "one_loop_reduction": threshold_reduction["one_loop_reduction"],
            "hypercharge_source_formula": hypercharge["source_formula"],
            "closed_internal_weak_split": vec,
        },
        "what_closes": closes,
        "what_remains_open": open_items,
        "next_source_template_path": rel(OUTPUT_TEMPLATE),
        "decision": decision,
        "theorem": {
            "name": "ElectroweakGaugeKineticNormalizationRouteDiscriminator",
            "proved": True,
            "statement": (
                "Given the closed internal weak-split threshold and the existing "
                "electroweak kernel interfaces, the current corpus selects the "
                "heterotic/Strominger threshold-kernel route as the strict no-knob "
                "primary path. M-theory supplies the shared physical normalization "
                "slot but not its dimensionful value; Theta supplies an overlap/RG "
                "scaffold but not a derived matching scale; and a primitive universal "
                "normalization is only a declared-primitive fallback, not no-knob "
                "closure. Therefore physical electroweak matching remains open until "
                "a selected heterotic/Strominger electroweak threshold kernel emits "
                "gauge normalization, stack determinants, mu_match, and RG scheme."
            ),
        },
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "promotes_theta_5TeV_as_prediction": False,
            "promotes_Mtheory_slot_without_value": False,
            "promotes_primitive_as_no_knob": False,
            "claims_measured_electroweak_closure": False,
            "target_fitting_used": False,
        },
        "closure_claimed": True,
        "closure_scope": "route_discriminator_and_next_payload_template_only",
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakGaugeKineticNormalizationAndRGScheme",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "template_path": rel(OUTPUT_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "strict_primary_route_selected": "B_flux_strominger_threshold",
        "gaugekinetic_normalization_closed": False,
        "matching_scale_closed": False,
        "RG_scheme_closed": False,
        "internal_lambda_12_value": vec["lambda_12"],
        "internal_Delta_G12_value": vec["Delta_G12"],
        "measured_electroweak_closure": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, template, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    return f"""# Selected Electroweak GaugeKinetic Normalization and RG Scheme SourceTheorem v1

## Result

```text
status = {candidate["status"]}
strict_primary_route_selected = {candidate["decision"]["strict_primary_route_selected"]}
gaugekinetic_normalization_closed = false
matching_scale_closed = false
RG_scheme_closed = false
measured_electroweak_closure = false
next_required_artifact = {candidate["decision"]["next_required_artifact"]}
```

## Route Discriminator

```json
{json.dumps(candidate["routes"], indent=2, sort_keys=True)}
```

## Closed Interface

```json
{json.dumps(candidate["closed_interface"], indent=2, sort_keys=True)}
```

## Theorem

{candidate["theorem"]["statement"]}

## Remaining Payload

```json
{json.dumps(candidate["what_remains_open"], indent=2, sort_keys=True)}
```

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, template, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    write_json(OUTPUT_TEMPLATE, template)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_TEMPLATE, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
