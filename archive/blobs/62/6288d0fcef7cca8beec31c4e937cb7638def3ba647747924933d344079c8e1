"""Build the physical gauge-anchor and electroweak threshold-vector gate.

This is the first artifact after closing the internal K_gauge anchor.  It tries
to promote the selected internal kernel to physical electroweak matching and
records exactly why the present repositories still stop short.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"
GR = ROOT.parent / "mtt-protospinor-gr-response-proof"

INPUTS = {
    "internal_k_gate": DATA / "selected_k_gauge_anchor_or_full_electroweak_matching.candidate.json",
    "ew_kernel_interface": NONSM / "certificates" / "selected_electroweak_kernel_interface_certificate.json",
    "ew_threshold_reduction": NONSM / "certificates" / "selected_electroweak_threshold_kernel_reduction_certificate.json",
    "ew_c1_determinant_reduction": NONSM / "certificates" / "selected_electroweak_c1_determinant_reduction_certificate.json",
    "ew_determinant_template": NONSM / "certificates" / "selected_electroweak_c1_response_determinant_only.template.json",
    "ew_fill_attempt": NONSM / "certificates" / "selected_electroweak_c1_response_fill_attempt_certificate.json",
    "omega_gap": GR / "certificates" / "selected_physical_omega_gap_theorem_certificate.json",
    "mtheory_anchor": GR / "certificates" / "m_theory_modal_gap_dimensional_anchor_candidate_certificate.json",
}

OUTPUT_DATA = DATA / "selected_physical_gauge_anchor_and_electroweak_threshold_vector.candidate.json"
OUTPUT_CERT = CERTS / "selected_physical_gauge_anchor_and_electroweak_threshold_vector_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Physical_Gauge_Anchor_and_Electroweak_Threshold_Vector_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    internal = load(INPUTS["internal_k_gate"])
    kernel = load(INPUTS["ew_kernel_interface"])
    threshold = load(INPUTS["ew_threshold_reduction"])
    c1det = load(INPUTS["ew_c1_determinant_reduction"])
    det_template = load(INPUTS["ew_determinant_template"])
    fill_attempt = load(INPUTS["ew_fill_attempt"])
    omega = load(INPUTS["omega_gap"])
    mtheory = load(INPUTS["mtheory_anchor"])

    i1 = Fraction(2, 3)
    i2 = Fraction(1, 1)
    i3_value = math.log(2008)
    g1_over_g2_tree = i2 / i1
    sin2_tree_gut = Fraction(3, 5) * g1_over_g2_tree / (Fraction(3, 5) * g1_over_g2_tree + 1)

    v1_tilde = det_template["selected_values"]["v1_tilde"]
    target_witness = c1det.get("diagnostic_target", {}).get("p_U1_minus_p_SU2")
    if target_witness is None:
        # Older artifacts record this only in the proof note, not the certificate.
        target_witness = 2.194153126940556
    lambda_target_delta_g12 = v1_tilde * float(target_witness) / (4.0 * math.pi)

    source_checks = {
        "internal_kernel_closed": internal["decision"]["selected_internal_kernel_vector_closed"] is True,
        "internal_K_equals_one": internal["decision"]["internal_K_gauge_value"] == "1",
        "kernel_interface_built": kernel["verdict"]["kernel_interface_built"] is True,
        "kernel_numeric_selection_open": kernel["verdict"]["numeric_electroweak_closure"] is False,
        "threshold_reduction_requires_kernel": threshold["verdict"]["low_energy_weak_angle_closed"] is False,
        "c1_reduced_to_local_determinant": c1det["status"] == "PEW_ALPHA1_REDUCED_TO_SELECTED_LOCAL_DETERMINANT",
        "local_determinant_template_open": det_template["status"] == "OPEN_REDUCED_TO_INDEX_WEIGHTED_LOCAL_DETERMINANT",
        "fill_attempt_blocks_selected_threshold": fill_attempt["status"] == "PEW_ALPHA1_TEMPLATE_FILL_BLOCKED_SELECTED_THRESHOLD_DATA_MISSING",
        "omega_gap_physical_unit_open": omega["guardrails"]["claims_omega_gap_phys"] is False,
        "mtheory_gauge_slot_identified": mtheory["closed_tests"]["m_theory_gauge_slot_identified"] is True,
        "mtheory_physical_anchor_open": mtheory["verdict"]["physical_dimensionful_anchor_available"] is False,
    }

    theorem = {
        "name": "SelectedPhysicalGaugeAnchorAndElectroweakThresholdVectorGate",
        "statement": (
            "Given the selected internal kernel I=(2/3,1,log(2008)) and "
            "K_gauge,int=1, full no-knob electroweak matching is equivalent to "
            "supplying two same-branch physical objects: a compactification/action "
            "anchor K_phys (or physical modal-gap unit) and an index-weighted local "
            "determinant threshold vector Delta_a^sel, with RG scheme and matching "
            "scale fixed before comparison. The present repositories identify the "
            "slots but do not emit their values."
        ),
        "selected_internal_inputs": {
            "I_U1": "2/3",
            "I_SU2": "1",
            "I_Qa_or_SU3": "log(2008)",
            "K_gauge_int": "1",
        },
        "zero_threshold_diagnostic": {
            "g1_squared_over_g2_squared_from_inverse_weights": f"{g1_over_g2_tree.numerator}/{g1_over_g2_tree.denominator}",
            "gut_normalized_sin2_tree": f"{sin2_tree_gut.numerator}/{sin2_tree_gut.denominator}",
            "gut_normalized_sin2_tree_numeric": float(sin2_tree_gut),
            "status": "DIAGNOSTIC_ONLY_NOT_PHYSICAL_PREDICTION",
            "why": "It assumes no physical threshold vector, no running, and no convention reconciliation with the older Theta representative ratio.",
        },
        "physical_anchor_gate": {
            "status": "OPEN",
            "required_source": "selected Omega_0 or ell_p/kappa_11/alpha_prime/action unit from the same branch",
            "mtheory_slot": "f_ab = (1/(2 kappa_11^2)) int_X7 omega_a wedge *_7 omega_b",
            "current_reduction": omega["theorem"]["status"],
        },
        "threshold_vector_gate": {
            "status": "OPEN",
            "required_source": "selected index-weighted local determinant / analytic torsion response",
            "weak_split_minimal_scalar": "lambda_12 = p_U1 - p_SU2",
            "known_selected_prefactor_v1_tilde": v1_tilde,
            "formula_if_lambda12_selected": "Delta_G,12 = v1_tilde * lambda_12 / (4*pi)",
            "diagnostic_target_witness_lambda12": target_witness,
            "diagnostic_target_witness_delta_g12": lambda_target_delta_g12,
            "target_witness_status": "FORBIDDEN_AS_PROOF_INPUT",
        },
        "convention_reconciliation_gate": {
            "status": "OPEN",
            "issue": (
                "The selected internal inverse weights imply a tree-level internal "
                "ratio, while older Theta electroweak notes quote a representative "
                "overlap ratio in their own convention. A proof must name the "
                "hypercharge normalization, embedding map, and matching convention "
                "before comparing either ratio to data."
            ),
            "required_output": "one typed map from selected U1/SU2/Qa carriers to GUT-normalized electroweak variables",
        },
    }

    decision = {
        "physical_electroweak_matching_closed": False,
        "physical_anchor_closed": False,
        "threshold_vector_closed": False,
        "convention_reconciliation_closed": False,
        "minimal_remaining_objects": [
            "K_phys or Omega_0/ell_p/kappa_11/alpha_prime physical anchor",
            "lambda_12 or full Delta_a^sel selected local determinant vector",
            "mu_match and fixed RG/threshold scheme",
            "typed electroweak convention map",
        ],
        "target_fitting_used": False,
        "next_required_object": "Selected_Local_Determinant_Threshold_Vector_or_Physical_Omega0_Source_v1",
    }

    candidate = {
        "candidate": "SelectedPhysicalGaugeAnchorAndElectroweakThresholdVector",
        "status": "PHYSICAL_EW_MATCHING_REDUCED_TO_OMEGA0_AND_LOCAL_DETERMINANT_OPEN",
        "inputs": {name: rel(path) for name, path in INPUTS.items()},
        "source_checks": source_checks,
        "theorem": theorem,
        "decision": decision,
        "guardrails": [
            "Do not treat the zero-threshold tree diagnostic 9/19 as a physical weak-angle prediction.",
            "Do not use the diagnostic lambda_12 target witness as selected determinant data.",
            "Do not mix internal inverse weights with older Theta ratios until the electroweak convention map is explicit.",
            "Do not select K_phys from observed alpha_EM, sin^2(theta_W), g2, g3, M_Z, or masses.",
            "Full no-knob closure requires the physical anchor and threshold vector from the same branch.",
        ],
        "closure_claimed": True,
        "closure_scope": "frontier_reduction_and_diagnostic_calculation_only",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedPhysicalGaugeAnchorAndElectroweakThresholdVector",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "closed": {
            "frontier_reduction": True,
            "zero_threshold_tree_diagnostic": "9/19",
            "selected_internal_kernel_inputs": theorem["selected_internal_inputs"],
            "same_branch_source_slots_identified": True,
            "no_target_fit_used": True,
        },
        "open": {
            "physical_anchor_K_phys_or_Omega0": True,
            "selected_local_determinant_lambda12_or_Delta_vector": True,
            "mu_match_and_RG_scheme": True,
            "electroweak_convention_map": True,
            "measured_electroweak_closure": True,
        },
        "next_required_object": decision["next_required_object"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    theorem = candidate["theorem"]
    decision = candidate["decision"]
    checks = "\n".join(f"{key} = {value}" for key, value in candidate["source_checks"].items())
    guards = "\n".join(f"- {item}" for item in candidate["guardrails"])
    remaining = "\n".join(f"- {item}" for item in decision["minimal_remaining_objects"])
    return f"""# Selected Physical Gauge Anchor and Electroweak Threshold Vector v1

## Result

The physical electroweak match is not closed yet.  It is reduced to the exact
remaining source objects.

```text
physical_electroweak_matching_closed = {str(decision["physical_electroweak_matching_closed"]).lower()}
physical_anchor_closed = {str(decision["physical_anchor_closed"]).lower()}
threshold_vector_closed = {str(decision["threshold_vector_closed"]).lower()}
convention_reconciliation_closed = {str(decision["convention_reconciliation_closed"]).lower()}
target_fitting_used = {str(decision["target_fitting_used"]).lower()}
```

## Theorem

```text
{theorem["name"]}
```

{theorem["statement"]}

## Selected Internal Inputs

```text
I_U1 = {theorem["selected_internal_inputs"]["I_U1"]}
I_SU2 = {theorem["selected_internal_inputs"]["I_SU2"]}
I_Qa_or_SU3 = {theorem["selected_internal_inputs"]["I_Qa_or_SU3"]}
K_gauge,int = {theorem["selected_internal_inputs"]["K_gauge_int"]}
```

## Diagnostic Only

If one ignores physical thresholds, running, and convention reconciliation, the
internal inverse weights imply:

```text
g1^2/g2^2 = {theorem["zero_threshold_diagnostic"]["g1_squared_over_g2_squared_from_inverse_weights"]}
sin^2(theta_W)_tree,GUT = {theorem["zero_threshold_diagnostic"]["gut_normalized_sin2_tree"]}
sin^2(theta_W)_tree,GUT numeric = {theorem["zero_threshold_diagnostic"]["gut_normalized_sin2_tree_numeric"]}
status = {theorem["zero_threshold_diagnostic"]["status"]}
```

This is deliberately not a physical weak-angle prediction:

```text
{theorem["zero_threshold_diagnostic"]["why"]}
```

## Physical Anchor Gate

```text
status = {theorem["physical_anchor_gate"]["status"]}
required_source = {theorem["physical_anchor_gate"]["required_source"]}
mtheory_slot = {theorem["physical_anchor_gate"]["mtheory_slot"]}
current_reduction = {theorem["physical_anchor_gate"]["current_reduction"]}
```

## Threshold Vector Gate

```text
status = {theorem["threshold_vector_gate"]["status"]}
required_source = {theorem["threshold_vector_gate"]["required_source"]}
weak_split_minimal_scalar = {theorem["threshold_vector_gate"]["weak_split_minimal_scalar"]}
known_selected_prefactor_v1_tilde = {theorem["threshold_vector_gate"]["known_selected_prefactor_v1_tilde"]}
formula_if_lambda12_selected = {theorem["threshold_vector_gate"]["formula_if_lambda12_selected"]}
diagnostic_target_witness_lambda12 = {theorem["threshold_vector_gate"]["diagnostic_target_witness_lambda12"]}
diagnostic_target_witness_delta_g12 = {theorem["threshold_vector_gate"]["diagnostic_target_witness_delta_g12"]}
target_witness_status = {theorem["threshold_vector_gate"]["target_witness_status"]}
```

## Convention Reconciliation Gate

```text
status = {theorem["convention_reconciliation_gate"]["status"]}
issue = {theorem["convention_reconciliation_gate"]["issue"]}
required_output = {theorem["convention_reconciliation_gate"]["required_output"]}
```

## Cross-Repo Checks

```text
{checks}
```

## Remaining Objects

{remaining}

## Guardrails

{guards}

## Next Required Object

```text
{decision["next_required_object"]}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    missing = [str(path) for path in INPUTS.values() if not path.exists()]
    if missing:
        print("Missing inputs:")
        print("\n".join(missing))
        return 1
    candidate, certificate, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, certificate)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"Wrote {OUTPUT_DATA}")
    print(f"Wrote {OUTPUT_CERT}")
    print(f"Wrote {OUTPUT_NOTE}")
    print(certificate["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
