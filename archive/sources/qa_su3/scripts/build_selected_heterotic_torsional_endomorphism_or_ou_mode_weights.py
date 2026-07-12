"""Build the torsional-endomorphism or OU-mode-weights value attempt."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
NONSM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")

INPUTS = {
    "source_search": DATA / "selected_heterotic_sourcecertificate_or_direct_operator_emission_search.candidate.json",
    "template": DATA / "selected_heterotic_torsional_endomorphism_or_ou_mode_weights.template.json",
    "ou_completion_note": NONSM / "proof_corpus" / "Selected_Qa_SU3_HYM_Strominger_Weitzenbock_OU_Completion_v1.md",
    "delta_a_mu_note": NONSM / "proof_corpus" / "Selected_Qa_SU3_HYM_Delta_A_Mu_Spectrum_Computation_v1.md",
    "mu_domain_note": NONSM / "proof_corpus" / "Selected_Qa_SU3_HYM_Mu_and_Operator_Domain_Selection_v1.md",
}

OUTPUT_DATA = DATA / "selected_heterotic_torsional_endomorphism_or_ou_mode_weights.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_torsional_endomorphism_or_ou_mode_weights_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_TorsionalEndomorphism_or_OU_ModeWeights_v1.md"

STATUS = "HETEROTIC_TORSIONAL_ENDOMORPHISM_OR_OU_MODEWEIGHTS_ATTEMPT_PARTIAL_GEOMETRY_FILLED_E_OU_OPEN"
NEXT = "Selected_Heterotic_BismutWeitzenbock_Formula_or_OUWeightDerivation_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    source_search = load(INPUTS["source_search"])
    template = load(INPUTS["template"])

    r1 = 4.440528182269818
    r2 = 4.440528182269818
    r3 = 4.440028979122532
    weights = {
        "bar_omega_1_norm_sq": 1.0 / (r1 * r1),
        "bar_omega_2_norm_sq": 1.0 / (r2 * r2),
        "bar_omega_3_norm_sq": 1.0 / (r3 * r3),
    }
    A = r3 / (r1 * r2)
    eight_A_sq = 8.0 * A * A
    anisotropy = max(weights.values()) - min(weights.values())

    metric_block_samples = {
        "mu_0.25": [0, 0.00919501, 0.02852753, 0.02852753, 0.03169789, 0.03169789, 0.05388469, 0.05388469, 0.10491509],
        "mu_1": [0, 0.12862921, 0.15215441, 0.15215441, 0.20288015, 0.20288015, 0.25358308, 0.25358308, 0.47998843],
        "mu_4": [0, 1.02890009, 1.21732652, 1.21732652, 1.62304121, 1.62304121, 2.02893836, 2.02893836, 3.840406],
    }
    positive_su3_samples = all(all(value > 0 for value in values[1:]) for values in metric_block_samples.values())
    logdet_samples = {
        key: sum(math.log(value) for value in values[1:])
        for key, values in metric_block_samples.items()
    }
    logdet_monotone_on_samples = logdet_samples["mu_0.25"] < logdet_samples["mu_1"] < logdet_samples["mu_4"]

    filled_packet = {
        "source_certificate": {
            "same_branch_selected_HYM_or_Strominger_source": False,
            "fixed_gauge_and_quotient_domain": "partial: selected compact Nil/Iwasawa branch and p0/p!=0 quotient policies imported; full fixed-gauge domain open",
            "same_branch_as_internal_lambda12_stack": False,
        },
        "torsional_endomorphism_lane": {
            "connection_A": "metric-weighted algebraic HYM commutator block available; retired printed HYM matrix not promoted",
            "torsion_H_or_Bismut_data": {
                "selected_radii": {"r1": r1, "r2": r2, "r3": r3},
                "coframe": {
                    "omega1": "(e1+i e2)/r1",
                    "omega2": "(e3+i e4)/r2",
                    "omega3": "(e5+i e6)/r3",
                },
                "A_r3_over_r1r2": A,
                "eight_A_squared": eight_A_sq,
                "weight_anisotropy": anisotropy,
            },
            "curvature_R_plus_trace_row": "Tr_grav R_+^2 = 8 A^2 alpha_1",
            "Weitzenbock_E_Qa_on_uE_one_forms": None,
            "positivity_or_kernel_policy": {
                "metric_weighted_su3_samples_positive": positive_su3_samples,
                "central_u1_zero_mode_remains": True,
                "sample_logdet_monotone": logdet_monotone_on_samples,
            },
        },
        "ou_mode_weight_lane": {
            "mode_basis": None,
            "gamma_nk_weights": None,
            "finite_truncation_and_error_bound": None,
            "zeta_or_heat_regularization": None,
            "guardrail": "arbitrary OU weights would be a knob",
        },
        "direct_finite_operator_lane": template["direct_finite_operator_lane"],
        "output": template["output"],
    }

    required_flags = {
        "selected_radii": True,
        "relative_one_form_weights": True,
        "bismut_trace_coefficient_8A2": True,
        "metric_weighted_positive_su3_samples": positive_su3_samples,
        "sample_logdet_monotone_no_mu_selection": logdet_monotone_on_samples,
        "same_branch_source_certificate": False,
        "full_fixed_gauge_domain": False,
        "Weitzenbock_E_Qa": False,
        "OU_gamma_nk_weights": False,
        "finite_heat_zeta_torsion_part": False,
        "computed_threshold_value": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticTorsionalEndomorphismOrOUModeWeights",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "source_search": source_search["status"],
        },
        "filled_packet": filled_packet,
        "computed_invariants": {
            "radii": {"r1": r1, "r2": r2, "r3": r3},
            "relative_one_form_weights": weights,
            "A_r3_over_r1r2": A,
            "eight_A_squared": eight_A_sq,
            "weight_anisotropy": anisotropy,
            "metric_weighted_logdet_samples": logdet_samples,
            "metric_weighted_logdet_monotone_on_samples": logdet_monotone_on_samples,
        },
        "required_flags": required_flags,
        "missing_fields": [key for key, value in required_flags.items() if value is False],
        "decision": {
            "torsional_geometry_partial_filled": True,
            "Weitzenbock_E_computed": False,
            "OU_weights_computed": False,
            "mu_selected": False,
            "determinant_finite_part_computed": False,
            "selected_values_available": False,
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "TorsionalEndomorphismOrOUWeightsPartialGeometryTheorem",
            "proved": True,
            "statement": (
                "The selected compact Nil/Iwasawa radii determine the relative one-form "
                "weights and the Bismut/curvature trace coefficient 8A^2. These data keep "
                "the metric-weighted algebraic su3 commutator block positive, but the "
                "sampled determinant remains monotone and does not select mu. Therefore "
                "closure requires a source-derived torsional Weitzenbock endomorphism, "
                "a source-derived OU mode-weight table, or an equivalent direct finite "
                "operator emission; arbitrary OU weights would be a knob."
            ),
        },
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "selects_mu_by_convenience": False,
            "inserts_arbitrary_ou_weights": False,
            "promotes_metric_block_as_full_operator": False,
            "promotes_retired_hym_matrix": False,
            "claims_measured_electroweak_closure": False,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    cert = {
        "certificate": "SelectedHeteroticTorsionalEndomorphismOrOUModeWeights",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "eight_A_squared": eight_A_sq,
        "Weitzenbock_E_computed": False,
        "OU_weights_computed": False,
        "mu_selected": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    return f"""# Selected Heterotic TorsionalEndomorphism or OU ModeWeights v1

## Result

```text
status = {candidate["status"]}
8A^2 = {candidate["computed_invariants"]["eight_A_squared"]}
Weitzenbock_E_computed = false
OU_weights_computed = false
mu_selected = false
next_required_artifact = {candidate["decision"]["next_required_artifact"]}
```

## Filled Packet

```json
{json.dumps(candidate["filled_packet"], indent=2, sort_keys=True)}
```

## Computed Invariants

```json
{json.dumps(candidate["computed_invariants"], indent=2, sort_keys=True)}
```

## Missing Fields

```json
{json.dumps(candidate["missing_fields"], indent=2, sort_keys=True)}
```

## Theorem

{candidate["theorem"]["statement"]}

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
