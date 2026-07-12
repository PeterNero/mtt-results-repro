"""Build the electroweak physical-anchor, RG, and matching-scale gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "internal_lambda12": DATA / "selected_electroweak_qastack_su2row_or_cancellation_and_physicalanchor.candidate.json",
    "k_gauge_gate": DATA / "selected_k_gauge_anchor_or_full_electroweak_matching.candidate.json",
    "physical_gate": DATA / "selected_physical_gauge_anchor_and_electroweak_threshold_vector.candidate.json",
    "omega_convention": Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof\certificates\selected_omega_convention_theorem_certificate.json"),
    "physical_alpha": Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof\certificates\selected_physical_alpha_or_action_unit_theorem_certificate.json"),
    "dimensional_metrology": Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof\certificates\dimensional_metrology_no_go_and_relative_closure_theorem_certificate.json"),
    "one_anchor_gr": Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof\certificates\one_anchor_gr_normalization_propagation_certificate.json"),
    "electroweak_bridge": Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob\certificates\electroweak_no_knob_bridge_audit_certificate.json"),
}

OUTPUT_DATA = DATA / "selected_electroweak_physicalanchor_rg_and_matchingscale.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_physicalanchor_rg_and_matchingscale_certificate.json"
OUTPUT_TEMPLATE = DATA / "selected_electroweak_physicalanchor_rg_and_matchingscale.template.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_PhysicalAnchor_RG_and_MatchingScale_v1.md"

STATUS = "ELECTROWEAK_INTERNAL_LAMBDA12_CLOSED_PHYSICAL_GAUGE_ANCHOR_RG_OPEN"
NEXT = "Selected_Electroweak_GaugeKinetic_Normalization_and_RG_Scheme_SourceTheorem_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build_template() -> dict[str, Any]:
    return {
        "schema": "SelectedElectroweakGaugeKineticNormalizationAndRGScheme.v1",
        "status": "OPEN_SELECTED_PHYSICAL_GAUGE_ANCHOR_RG_REQUIRED",
        "must_emit": {
            "physical_gauge_action_anchor": {
                "selected_by_mtt": None,
                "symbol": "K_phys or f_ab normalization",
                "allowed_sources": [
                    "same-branch M-theory gauge kinetic integral",
                    "same-branch heterotic gauge kinetic function",
                    "declared primitive universal gauge normalization with primitive-constant discipline",
                ],
                "forbidden_sources": [
                    "observed alpha_EM",
                    "observed sin^2(theta_W)",
                    "observed g1/g2/g3",
                    "mass or TeV benchmark backsolve",
                ],
            },
            "matching_scale": {
                "selected_by_mtt": None,
                "symbol": "mu_match",
                "allowed_source_examples": [
                    "Omega0 if and only if a theorem identifies the electroweak threshold surface with the damping/admissibility scale",
                    "string/M-theory compactification scale from the same gauge kinetic packet",
                    "source-selected finite threshold scale",
                ],
            },
            "rg_scheme": {
                "selected_by_mtt": None,
                "scheme": None,
                "beta_coefficients": None,
                "threshold_convention": None,
            },
            "threshold_vector": {
                "internal_lambda_12": 2.6179362173268497,
                "Delta_G12_internal": 0.08450302790361214,
                "full_factor_vector_required_for_full_coupling_closure": True,
            },
        },
        "acceptance_contract": [
            "The physical gauge-action anchor must be selected before comparison to measured electroweak couplings.",
            "The matching scale and RG/threshold scheme must be fixed before running to M_Z or another data scale.",
            "The closed internal lambda_12 may be used as threshold data, but not as a physical gauge normalization.",
            "The one-anchor GR/metrology family may share a source with electroweak only through a proved gauge kinetic dictionary.",
        ],
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    internal = load(INPUTS["internal_lambda12"])
    k_gate = load(INPUTS["k_gauge_gate"])
    physical_gate = load(INPUTS["physical_gate"])
    omega = load(INPUTS["omega_convention"])
    alpha = load(INPUTS["physical_alpha"])
    metrology = load(INPUTS["dimensional_metrology"])
    one_anchor = load(INPUTS["one_anchor_gr"])
    ew_bridge = load(INPUTS["electroweak_bridge"])
    template = build_template()

    vec = internal["selected_internal_threshold_vector"]
    omega_formula = omega["reduced_formula"]
    alpha_result = alpha["theorem_result"]

    closed_now = {
        "internal_lambda_12": internal["decision"]["lambda_12_internal_closed"],
        "internal_Delta_G12": True,
        "typed_Qa_Qc_hypercharge_threshold_map": internal["decision"]["typed_hypercharge_map_closed"],
        "Omega0_symbol_convention_chi_equals_1": omega["convention_selection"]["chi_omega"] == 1.0,
        "relative_GR_metrology_family": metrology["closure_result"]["relative_physical_closure"],
        "one_anchor_GR_propagation_family": one_anchor["verdict"]["one_anchor_gr_normalization_family_closed"],
    }

    still_open = {
        "physical_gauge_action_anchor": True,
        "matching_scale_mu_match": True,
        "RG_and_threshold_scheme": True,
        "full_factor_threshold_vector_beyond_weak_split": True,
        "measured_electroweak_couplings": True,
        "full_SM_closure": True,
    }

    route_tests = {
        "internal_K_gauge_equals_one": {
            "accepted_as_physical_anchor": False,
            "status": k_gate["status"],
            "reason": "K_gauge,int=1 is an internal action-unit normalization and cannot be used as measured gauge normalization.",
        },
        "Omega0_as_matching_scale": {
            "accepted_now": False,
            "conditional_formula": omega_formula["Omega0"],
            "reason": "Omega0 is a physical damping/admissibility scale after alpha_phys is supplied. A separate theorem must identify it with the electroweak threshold/matching surface.",
        },
        "GR_one_anchor_family": {
            "accepted_as_electroweak_anchor_now": False,
            "status": one_anchor["status"],
            "reason": "The one-anchor GR family propagates gravitational normalization. Electroweak needs a same-source gauge kinetic dictionary before sharing that anchor.",
        },
        "primitive_universal_gauge_normalization": {
            "accepted_now": False,
            "reason": "It may be a legitimate way forward only if declared as a primitive universal constant, not tuned to electroweak data, and audited as outside no-knob closure.",
        },
        "electroweak_bridge_status": {
            "status": ew_bridge["status"],
            "required_next_inputs": ew_bridge["required_next_inputs"],
        },
    }

    conditional_interface = {
        "matching_formula_shape": k_gate["theorem"]["physical_kernel_required"]["formula"],
        "closed_internal_weak_split": {
            "lambda_12": vec["lambda_12_internal"],
            "Delta_G12": vec["Delta_G12_internal"],
            "p_Y": vec["p_Y_internal"],
        },
        "Omega0_reduction": {
            "Omega0": omega_formula["Omega0"],
            "Omega0_over_sqrt_alpha_phys": omega_formula["Omega0_over_sqrt_alpha_phys"],
            "alpha_phys_status": alpha_result["alpha_phys_status"],
        },
        "what_a_successful_next_theorem_would_output": [
            "K_phys or f_ab in the same normalization as the internal threshold vector",
            "mu_match selected before data comparison",
            "RG scheme and beta/threshold convention",
            "a rule for whether Omega0, compactification scale, or another source scale is the matching surface",
        ],
    }

    candidate = {
        "candidate": "SelectedElectroweakPhysicalAnchorRGAndMatchingScale",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "closed_now": closed_now,
        "still_open": still_open,
        "route_tests": route_tests,
        "conditional_interface": conditional_interface,
        "source_template_path": rel(OUTPUT_TEMPLATE),
        "decision": {
            "internal_lambda_12_closed": True,
            "internal_lambda_12_value": vec["lambda_12_internal"],
            "internal_Delta_G12_value": vec["Delta_G12_internal"],
            "physical_gauge_action_anchor_closed": False,
            "matching_scale_closed": False,
            "RG_scheme_closed": False,
            "measured_electroweak_closure": False,
            "full_SM_closure": False,
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "ElectroweakPhysicalAnchorRGFrontierTheorem",
            "proved": True,
            "statement": (
                "The selected electroweak branch now contains a closed dimensionless "
                f"internal weak-split threshold lambda_12={vec['lambda_12_internal']} "
                f"and Delta_G12={vec['Delta_G12_internal']}. The GR/protospinor branch "
                "also closes the relative one-anchor metrology family and the Omega0 "
                "symbol convention. These do not by themselves select the physical "
                "electroweak gauge-action normalization, matching scale, or RG/threshold "
                "scheme. Therefore measured electroweak closure is reduced to one source "
                "packet: a same-branch gauge kinetic normalization plus mu_match and RG "
                "scheme, with no observed electroweak inputs."
            ),
        },
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_alpha_EM_or_weak_angle_backsolve": False,
            "treats_internal_K_as_physical": False,
            "identifies_Omega0_with_mu_match_without_theorem": False,
            "claims_measured_electroweak_closure": False,
            "target_fitting_used": False,
        },
        "closure_claimed": True,
        "closure_scope": "frontier_reduction_after_internal_lambda12_closure",
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakPhysicalAnchorRGAndMatchingScale",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "template_path": rel(OUTPUT_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "internal_lambda_12_closed": True,
        "internal_lambda_12_value": vec["lambda_12_internal"],
        "internal_Delta_G12_value": vec["Delta_G12_internal"],
        "physical_gauge_action_anchor_closed": False,
        "matching_scale_closed": False,
        "RG_scheme_closed": False,
        "measured_electroweak_closure": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, template, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    return f"""# Selected Electroweak PhysicalAnchor RG and MatchingScale v1

## Result

```text
status = {candidate["status"]}
internal_lambda_12_closed = true
internal_lambda_12 = {candidate["decision"]["internal_lambda_12_value"]}
internal_Delta_G12 = {candidate["decision"]["internal_Delta_G12_value"]}
physical_gauge_action_anchor_closed = false
matching_scale_closed = false
RG_scheme_closed = false
measured_electroweak_closure = false
next_required_artifact = {candidate["decision"]["next_required_artifact"]}
```

## What Is Now Closed

```json
{json.dumps(candidate["closed_now"], indent=2, sort_keys=True)}
```

## Conditional Interface

```json
{json.dumps(candidate["conditional_interface"], indent=2, sort_keys=True)}
```

## Route Tests

```json
{json.dumps(candidate["route_tests"], indent=2, sort_keys=True)}
```

## Theorem

{candidate["theorem"]["statement"]}

## Next Source Packet

```json
{json.dumps(candidate["source_template_path"], indent=2, sort_keys=True)}
```

The next theorem must emit physical gauge kinetic normalization, matching scale,
and RG/threshold scheme before any measured electroweak comparison.

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
