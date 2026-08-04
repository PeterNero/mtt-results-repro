"""Build the Bismut-Weitzenbock formula or OU-weight derivation gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "torsional_ou_attempt": DATA / "selected_heterotic_torsional_endomorphism_or_ou_mode_weights.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_bismut_weitzenbock_formula_or_ouweight_derivation.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_bismut_weitzenbock_formula_or_ouweight_derivation_certificate.json"
OUTPUT_TEMPLATE = DATA / "selected_heterotic_bismut_weitzenbock_tensor_payload.template.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_BismutWeitzenbock_Formula_or_OUWeightDerivation_v1.md"

STATUS = "HETEROTIC_BISMUT_WEITZENBOCK_FORMULA_OR_OUWEIGHT_DERIVATION_BUILT_TENSOR_PAYLOAD_OPEN"
NEXT = "Selected_Heterotic_BismutWeitzenbock_TensorPayload_Fill_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build_template() -> dict[str, Any]:
    return {
        "schema": "SelectedHeteroticBismutWeitzenbockTensorPayload.v1",
        "status": "OPEN_TENSOR_VALUES_REQUIRED",
        "source_identity": {
            "same_branch_selected_HYM_or_Strominger_source": None,
            "fixed_frame_and_gauge": None,
            "selected_domain": None,
        },
        "geometric_tensors": {
            "orthonormal_coframe": None,
            "structure_constants_c_ij_k": None,
            "complex_structure_J": None,
            "Hermitian_form_omega": None,
            "torsion_H_or_d_c_omega_components": None,
            "Bismut_connection_coefficients": None,
            "R_plus_curvature_components": None,
        },
        "bundle_tensors": {
            "connection_A_components": None,
            "curvature_F_A_components": None,
            "ad_bundle_representation": None,
            "trace_normalization": None,
        },
        "operator_contract": {
            "principal_symbol": "nabla_plus_A^* nabla_plus_A",
            "zero_order_terms": [
                "curvature action on u(E)-valued one-forms",
                "torsion contraction terms",
                "gauge-fixing curvature/torsion correction",
                "possible dilaton/Strominger lower-order correction if selected",
            ],
            "E_Qa_matrix": None,
            "kernel_and_quotient_policy": None,
        },
        "ou_derivation_alternative": {
            "selected_mode_basis": None,
            "OU_generator": None,
            "gamma_nk_inverse_table": None,
            "proof_weights_are_source_derived": None,
        },
        "acceptance_tests": [
            "all tensors are emitted before threshold comparison",
            "E_Qa is self-adjoint in the selected inner product",
            "central/gauge zero modes match the selected quotient policy",
            "positive spectrum/heat/torsion finite part is computable",
            "no arbitrary OU weights or fitted mu are inserted",
        ],
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    prior = load(INPUTS["torsional_ou_attempt"])
    inv = prior["computed_invariants"]
    template = build_template()

    contract = {
        "known_inputs": {
            "selected_radii": inv["radii"],
            "relative_one_form_weights": inv["relative_one_form_weights"],
            "A_r3_over_r1r2": inv["A_r3_over_r1r2"],
            "eight_A_squared": inv["eight_A_squared"],
            "metric_weighted_logdet_monotone_on_samples": inv["metric_weighted_logdet_monotone_on_samples"],
        },
        "bismut_weitz_lhs": "Delta_threshold = nabla_{+,A}^* nabla_{+,A} + E_Qa",
        "minimal_tensor_payload": [
            "structure constants in selected orthonormal real frame",
            "J and Hermitian form omega",
            "H=d^c omega or equivalent Bismut torsion components",
            "Bismut connection coefficients Gamma^+",
            "R^+ curvature components and trace row",
            "bundle connection A and curvature F_A in selected gauge",
            "representation action on u(E)-valued one-forms",
            "inner product/trace normalization and quotient projector",
        ],
        "ou_weight_payload": [
            "selected OU mode basis indexed by (n,k)",
            "source-derived gamma_{n,k}^{-1}",
            "finite truncation/error theorem",
            "zeta or heat regularization rule",
        ],
        "selection_condition": (
            "Since the current metric-weighted algebraic block has monotone logdet samples, "
            "any interior mu selection must come from E_Qa, source-derived OU weights, "
            "or a direct finite operator emission."
        ),
    }

    route_tests = {
        "bismut_weitzenbock_formula_lane": {
            "status": "PRIMARY_TENSOR_PAYLOAD_OPEN",
            "known_geometry_enough_to_start": True,
            "E_Qa_computed": False,
            "missing": template["geometric_tensors"] | template["bundle_tensors"] | {"E_Qa_matrix": None, "kernel_and_quotient_policy": None},
        },
        "ou_weight_derivation_lane": {
            "status": "ALTERNATIVE_OPEN",
            "weights_computed": False,
            "guardrail": "arbitrary gamma_{n,k}^{-1} values are forbidden",
            "missing": template["ou_derivation_alternative"],
        },
        "direct_finite_operator_emission_lane": {
            "status": "ACCEPTABLE_IF_EMITTED",
            "would_bypass_symbolic_E": True,
            "required": [
                "rho_E mesh/metric",
                "D_E action",
                "Riesz/gap",
                "reduced Green",
                "finite determinant or torsion finite part",
            ],
        },
    }

    candidate = {
        "candidate": "SelectedHeteroticBismutWeitzenbockFormulaOrOUWeightDerivation",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {"torsional_ou_attempt": prior["status"]},
        "contract": contract,
        "route_tests": route_tests,
        "decision": {
            "formula_contract_built": True,
            "tensor_payload_available": False,
            "E_Qa_computed": False,
            "OU_weights_computed": False,
            "direct_finite_operator_emitted": False,
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
        },
        "next_template_path": rel(OUTPUT_TEMPLATE),
        "theorem": {
            "name": "BismutWeitzenbockOrOUWeightDerivationContractTheorem",
            "proved": True,
            "statement": (
                "The remaining heterotic threshold source problem is now reduced to a "
                "specific tensor payload. Either compute the Bismut/Weitzenbock zero-order "
                "block E_Qa from the selected torsion, curvature, bundle connection, trace, "
                "and quotient data, or derive the OU mode weights from the same selected "
                "source. A direct finite operator emission may replace this symbolic route, "
                "but it must emit rho_E, D_E, Riesz/gap, Green, and finite-part data honestly."
            ),
        },
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "inserts_arbitrary_ou_weights": False,
            "selects_mu_by_convenience": False,
            "promotes_contract_as_values": False,
            "claims_measured_electroweak_closure": False,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    cert = {
        "certificate": "SelectedHeteroticBismutWeitzenbockFormulaOrOUWeightDerivation",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "template_path": rel(OUTPUT_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "formula_contract_built": True,
        "tensor_payload_available": False,
        "E_Qa_computed": False,
        "OU_weights_computed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, template, render_note(candidate, cert, template)


def render_note(candidate: dict[str, Any], cert: dict[str, Any], template: dict[str, Any]) -> str:
    return f"""# Selected Heterotic BismutWeitzenbock Formula or OUWeightDerivation v1

## Result

```text
status = {candidate["status"]}
formula_contract_built = true
tensor_payload_available = false
E_Qa_computed = false
OU_weights_computed = false
next_required_artifact = {candidate["decision"]["next_required_artifact"]}
```

## Contract

```json
{json.dumps(candidate["contract"], indent=2, sort_keys=True)}
```

## Route Tests

```json
{json.dumps(candidate["route_tests"], indent=2, sort_keys=True)}
```

## Theorem

{candidate["theorem"]["statement"]}

## Next Template

```json
{json.dumps(template, indent=2, sort_keys=True)}
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
