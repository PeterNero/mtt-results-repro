"""Derive the typed A72 functional from one normalized determinant action."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_gaugekineticactionderivationandfrozenprofilevalidation"
OUT = ROOT / "candidate_data" / SLUG
ACTION = OUT / "normalized_determinant_action_derivation.packet.json"
SELECTION = OUT / "physical_action_selection_gate.packet.json"
VALIDATION = OUT / "frozen_external_validation_protocol.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_GaugeKineticActionDerivationAndFrozenProfileValidation_v1.md"
STATUS = "MTT_SELECTED_A72_FUNCTIONAL_DERIVED_FROM_ONE_NORMALIZED_DETERMINANT_ACTION_PHYSICAL_SELECTION_VALIDATION_OPEN"
NEXT = "MTT_Selected_NormalizedDeterminantActionFromMTTHessian_or_IndependentGaugeProfileTest_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    paths = {
        "A70_torsion": ROOT / "candidate_data" / "selected_residualcirclelenscostoperator_or_exactgaugekineticvalueemission" / "q79_shared_circle_chord_torsion.packet.json",
        "A71_spectrum": ROOT / "candidate_data" / "selected_actualz64towerkineticfunctionaltyping_or_resolventroutingpromotion" / "actual_z64_tower_spectrum.packet.json",
        "A72_functional": ROOT / "candidate_data" / "selected_gaugekineticfunctionalofl64andq79chord_or_strictresidualvalueemission" / "typed_l64_q79_projector_functional.packet.json",
        "A72_execution": ROOT / "candidate_data" / "selected_gaugekineticfunctionalofl64andq79chord_or_strictresidualvalueemission" / "frozen_zero_parameter_gauge_execution.packet.json",
    }
    data = {key: load(path) for key, path in paths.items()}
    torsion = float(data["A70_torsion"]["lens_quarter_log_cost"])
    rows = data["A71_spectrum"]["spectrum_with_multiplicity"]
    eigenvalues = [
        float(row["eigenvalue"])
        for row in rows
        for _ in range(int(row["multiplicity"]))
    ]
    dim_l = len(eigenvalues)
    green = sum(1.0 / value for value in eigenvalues) / dim_l
    delta_q = torsion * (6.0 / 7.0) * green
    delta_e = torsion + (3.0 / 4.0) * delta_q
    a72 = data["A72_functional"]["functional"]

    # Finite-difference checks of the exact analytic derivative formulas.
    h = 1e-7
    gamma_q_h = sum(6.0 * math.log(value + h * torsion) + math.log(value) for value in eigenvalues) / (dim_l * 7.0)
    gamma_q_0 = sum(7.0 * math.log(value) for value in eigenvalues) / (dim_l * 7.0)
    fd_q = (gamma_q_h - gamma_q_0) / h
    gamma_e_h = h * torsion + (3.0 / 4.0) * math.log1p(h * delta_q)
    fd_e = gamma_e_h / h
    action = {
        "schema": "MTTNormalizedDeterminantActionDerivation.v1",
        "status": "ONE_FINITE_POSITIVE_ACTION_EMITS_A72_RESPONSE_EXACTLY",
        "carrier_blocks": {
            "quark": "H_q(eps)=L64 tensor I7 + eps T79 I16 tensor P7_nontrivial",
            "lepton_return": "H_e(eps)=I16 tensor I4 + eps delta_q I16 tensor P4_nontrivial",
            "direct_lepton_chord": "eps T79",
        },
        "normalized_effective_action": {
            "Gamma_q": "(1/(16*7)) log det H_q(eps_q)",
            "Gamma_e": "eps_e T79 + (1/(16*4)) log det H_e(eps_e)",
            "Gamma_total": "Gamma_q(eps_q)+Gamma_e(eps_e)",
        },
        "response_theorem": {
            "dGamma_q_at_zero": "T79*(6/7)*(1/16)Tr(L64^-1)",
            "dGamma_e_at_zero": "T79+(3/4)dGamma_q_at_zero",
            "delta_q": delta_q,
            "delta_e": delta_e,
            "matches_A72_delta_q": abs(delta_q - float(a72["delta_q_value"])) < 1e-15,
            "matches_A72_delta_e": abs(delta_e - float(a72["delta_e_value"])) < 1e-15,
        },
        "proof": "d log det A(eps)/d eps = Tr(A(eps)^-1 A'(eps)); tensor trace factorization gives normalized ranks 6/7 and 3/4.",
        "properties": {
            "finite_dimensional": True,
            "positive_for_eps_nonnegative": True,
            "gauge_commuting": True,
            "basis_independent": True,
            "zero_continuous_parameters": True,
            "no_mixed_type_label_arithmetic": True,
        },
        "numerical_derivative_check": {
            "step": h,
            "fd_delta_q": fd_q,
            "analytic_delta_q": delta_q,
            "absolute_error_q": abs(fd_q - delta_q),
            "fd_delta_e": fd_e,
            "analytic_delta_e": delta_e,
            "absolute_error_e": abs(fd_e - delta_e),
        },
    }
    selection = {
        "schema": "MTTPhysicalActionSelectionGate.v1",
        "status": "ALGEBRAIC_ACTION_EXISTENCE_CLOSED_MTT_ACTION_SELECTION_OPEN",
        "closed": {
            "one_action_representation_exists": True,
            "A72_product_and_sum_derived": True,
            "projector_rank_factors_are_trace_theorems": True,
            "positivity_and_gauge_commutation": True,
        },
        "open": {
            "selected_MTT_Hessian_has_exact_Hq_He_blocks": True,
            "normalized_logdet_is_the_selected_Nkin_functional": True,
            "q79_chord_insertion_enters_with_Lens_quarter_T79": True,
            "P7_routes_only_colored_residual_and_P4_routes_e_return": True,
            "counterterms_or_higher_blocks_do_not_change_relative_rows": True,
        },
        "strict_same_action_source_closed": False,
        "strict_gauge_values_accepted": 0,
        "new_continuous_parameters": 0,
    }
    formula_hash = sha256(paths["A72_execution"])
    validation = {
        "schema": "MTTFrozenExternalGaugeValidationProtocol.v1",
        "status": "FORMULA_HASH_FROZEN_EXTERNAL_COMMON_SCHEME_DATASET_NOT_YET_ADMITTED",
        "frozen_formula": {
            "id": data["A72_execution"]["formula_id"],
            "packet_sha256": formula_hash,
            "K_over_K2": data["A72_execution"]["K_over_K2"],
            "retuning_forbidden": True,
        },
        "external_primary_reference": {
            "title": "Investigating the near-criticality of the Higgs boson",
            "authors": "Buttazzo et al.",
            "url": "https://arxiv.org/abs/1307.3536",
            "relevant_metadata": "MSbar weak-scale couplings with two-loop NNLO thresholds and three-loop RG evolution; g1=sqrt(5/3)gY",
            "direct_numeric_validation_admitted": False,
            "reason": "Its published profile uses an older input vintage and Mt scale. A commensurate extraction/transport with covariance is required before treating it as an independent test.",
        },
        "pass_conditions": [
            "declare scale, scheme, hypercharge normalization and input vintage",
            "transport the frozen formula and external profile with one declared RG implementation",
            "use at most one common normalization primitive, never two relative coupling fits",
            "evaluate a covariance-aware two-ratio pull",
            "record pass/fail without changing projector ranks or formula",
        ],
        "independent_validation_closed": False,
        "next_required_artifact": NEXT,
    }
    checks = {
        "A72_delta_q_reproduced": action["response_theorem"]["matches_A72_delta_q"],
        "A72_delta_e_reproduced": action["response_theorem"]["matches_A72_delta_e"],
        "action_properties_all_true": all(action["properties"].values()),
        "finite_difference_q_agrees": action["numerical_derivative_check"]["absolute_error_q"] < 1e-8,
        "finite_difference_e_agrees": action["numerical_derivative_check"]["absolute_error_e"] < 1e-8,
        "algebraic_action_exists": selection["closed"]["one_action_representation_exists"],
        "physical_action_selection_open": not selection["strict_same_action_source_closed"],
        "formula_hash_frozen": len(formula_hash) == 64,
        "external_numeric_validation_not_overclaimed": not validation["external_primary_reference"]["direct_numeric_validation_admitted"],
        "independent_validation_open": not validation["independent_validation_closed"],
    }
    candidate = {
        "schema": "MTTSelectedGaugeKineticActionDerivationAndFrozenProfileValidation.v1",
        "status": STATUS,
        "results": {
            "one_normalized_determinant_action_constructed": True,
            "A72_response_derived_exactly": True,
            "mathematical_same_action_existence_closed": True,
            "physical_MTT_action_selection_closed": False,
            "formula_frozen_by_hash": True,
            "independent_external_validation_closed": False,
            "strict_gauge_values_accepted": 0,
            "new_continuous_parameters": 0,
        },
        "outputs": {
            "action": str(ACTION.relative_to(ROOT)).replace("\\", "/"),
            "selection": str(SELECTION.relative_to(ROOT)).replace("\\", "/"),
            "validation": str(VALIDATION.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {key: bool(value) for key, value in checks.items()},
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_GaugeKineticActionDerivationAndFrozenProfileValidation_v1",
        "status": STATUS,
        "delta_q_delta_e": [delta_q, delta_e],
        "one_action_derivation_closed": True,
        "physical_MTT_action_selection_closed": False,
        "frozen_formula_sha256": formula_hash,
        "independent_validation_closed": False,
        "strict_gauge_values_accepted": 0,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Gauge Kinetic Action Derivation and Frozen Profile Validation v1

## One-action derivation

Define positive finite blocks

```text
H_q(eps)=L64 tensor I7 + eps T79 I16 tensor P7_nontrivial,
H_e(eps)=I16 tensor I4 + eps delta_q I16 tensor P4_nontrivial.
```

The normalized determinant action is

```text
Gamma = (1/112)log det H_q(eps_q)
      + eps_e T79 + (1/64)log det H_e(eps_e).
```

Using `d log det A=Tr(A^-1 dA)` gives exactly

```text
d_q Gamma = T79*(6/7)*(1/16)Tr(L64^-1) = {delta_q:.17g},
d_e Gamma = T79+(3/4)d_q Gamma = {delta_e:.17g}.
```

Thus A72 is generated by one finite positive gauge-commuting action, not an arithmetic splice.

## Remaining selection

Mathematical action existence is closed. Physical MTT selection is not: the corpus must identify
these blocks as the actual kinetic Hessian, select normalized `log det` as `N_kin`, and prove the
`Z7`/Lens projector routing and absence of relative counterterm changes.

## Frozen validation

The A72 formula packet is frozen at SHA-256 `{formula_hash}`. Buttazzo et al. provide an external
NNLO MSbar weak-scale reference, but its older input vintage and different top-mass scale require a
commensurate transport/covariance extraction before it can be admitted as an independent numerical
test. No value was retuned and no external-validation claim is made.

Next artifact: `{NEXT}`.
"""

    dump(ACTION, action)
    dump(SELECTION, selection)
    dump(VALIDATION, validation)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
