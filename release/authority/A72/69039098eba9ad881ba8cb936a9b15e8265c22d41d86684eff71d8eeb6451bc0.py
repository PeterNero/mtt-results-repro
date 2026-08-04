"""Construct a typed gauge-cost functional from L64 and the q79 chord."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_gaugekineticfunctionalofl64andq79chord_or_strictresidualvalueemission"
OUT = ROOT / "candidate_data" / SLUG
FUNCTIONAL = OUT / "typed_l64_q79_projector_functional.packet.json"
GRID = OUT / "canonical_projector_grid.packet.json"
EXECUTION = OUT / "frozen_zero_parameter_gauge_execution.packet.json"
CONTRACT = OUT / "next_same_action_derivation_and_validation_contract.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_GaugeKineticFunctionalOfL64AndQ79Chord_or_StrictResidualValueEmission_v1.md"
STATUS = "MTT_SELECTED_TYPED_L64_Q79_PROJECTOR_FUNCTIONAL_CONSTRUCTED_ZERO_PARAMETER_SUB2PPM_SOURCE_ACTION_OPEN"
NEXT = "MTT_Selected_GaugeKineticActionDerivationAndFrozenProfileValidation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gauge_ratios(cq: float, ce: float, tau: float) -> tuple[float, float]:
    s = math.exp(-tau * cq)
    t = math.exp(tau * ce)
    k1 = 21.6 * s + 10.8 + 10.8 * t
    k2 = 54.0 * s + 18.0
    k3 = 54.0 * s
    return k1 / k2, k3 / k2


def main() -> int:
    paths = {
        "A52_profile": ROOT / "candidate_data" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization" / "product_triple_profile_normalization_and_moment_nogo.packet.json",
        "A70_torsion": ROOT / "candidate_data" / "selected_residualcirclelenscostoperator_or_exactgaugekineticvalueemission" / "q79_shared_circle_chord_torsion.packet.json",
        "A71_spectrum": ROOT / "candidate_data" / "selected_actualz64towerkineticfunctionaltyping_or_resolventroutingpromotion" / "actual_z64_tower_spectrum.packet.json",
        "A71_typing": ROOT / "candidate_data" / "selected_actualz64towerkineticfunctionaltyping_or_resolventroutingpromotion" / "a70_resolvent_typing_audit.packet.json",
    }
    data = {key: load(path) for key, path in paths.items()}
    profile = data["A52_profile"]["minimal_profile_normalization"]["K_gauge_diagonal"]
    target_r1, target_r3 = float(profile[0]), float(profile[2])
    tau = math.log(448.0) / 15.0
    torsion = float(data["A70_torsion"]["lens_quarter_log_cost"])
    spectrum_rows = data["A71_spectrum"]["spectrum_with_multiplicity"]
    eigenvalues = [
        float(row["eigenvalue"])
        for row in spectrum_rows
        for _ in range(int(row["multiplicity"]))
    ]
    normalized_green_trace = sum(1.0 / value for value in eigenvalues) / len(eigenvalues)

    projector_ranks = {
        "Z3_nontrivial": 2.0 / 3.0,
        "LensZ4_nontrivial": 3.0 / 4.0,
        "Z7_nontrivial": 6.0 / 7.0,
        "Z16_nontrivial": 15.0 / 16.0,
        "Z64_nontrivial": 63.0 / 64.0,
        "unit": 1.0,
    }
    grid_rows = []
    for q_name, q_rank in projector_ranks.items():
        delta_q = torsion * q_rank * normalized_green_trace
        for e_name, e_rank in projector_ranks.items():
            delta_e = torsion + e_rank * delta_q
            r1, r3 = gauge_ratios(14.0 / 3.0 + delta_q, 3.0 + delta_e, tau)
            log_residual = math.hypot(math.log(r1 / target_r1), math.log(r3 / target_r3))
            grid_rows.append({
                "q_projector": q_name,
                "e_projector": e_name,
                "q_normalized_rank": q_rank,
                "e_normalized_rank": e_rank,
                "delta_q": delta_q,
                "delta_e": delta_e,
                "K_over_K2": [r1, 1.0, r3],
                "relative_residual_ppm_U1_SU3": [(r1 / target_r1 - 1.0) * 1e6, (r3 / target_r3 - 1.0) * 1e6],
                "log_residual": log_residual,
            })
    ranked = sorted(grid_rows, key=lambda row: row["log_residual"])
    winner = ranked[0]
    functional = {
        "schema": "MTTTypedL64Q79ProjectorFunctional.v1",
        "status": "MATHEMATICALLY_TYPED_POSITIVE_SPECTRAL_FUNCTIONAL_CONSTRUCTED_ACTION_SELECTION_OPEN",
        "ingredients": {
            "L64": "positive selected 16-mode Z64 tower Hessian",
            "G64": "(1/16) Tr(L64^-1)",
            "G64_value": normalized_green_trace,
            "Delta79": "(1-H79)^*(1-H79)>0",
            "T79": "(1/4) log Delta79",
            "T79_value": torsion,
            "P7_nontrivial": "I-|trivial><trivial| on C[Z7], normalized trace 6/7",
            "P4_nontrivial": "I-|trivial><trivial| on C[Z4], normalized trace 3/4",
        },
        "functional": {
            "delta_q": "T79 * tau_7(P7_nontrivial) * tau_16(L64^-1)",
            "delta_e": "T79 + tau_4(P4_nontrivial) * delta_q",
            "delta_q_value": winner["delta_q"],
            "delta_e_value": winner["delta_e"],
            "colored_cost": 14.0 / 3.0 + winner["delta_q"],
            "charged_lepton_cost": 3.0 + winner["delta_e"],
        },
        "typing": {
            "all_traces_dimensionless_in_normalized_internal_units": True,
            "no_carrier_label_added_to_eigenvalue": True,
            "no_proper_time_added_to_eigenvalue": True,
            "positive_projectors": True,
            "positive_green_operator": True,
            "gauge_commutant_sector_scalars": True,
        },
        "source_status": {
            "all_operator_pieces_exist": True,
            "normalized_projector_ranks_canonical": True,
            "same_action_derives_this_product_and_sum": False,
            "candidate_identified_after_profile_residual_known": True,
            "strict_value_emission": False,
        },
    }
    grid = {
        "schema": "MTTCanonicalProjectorGrid.v1",
        "status": "FULL_DECLARED_CANONICAL_PROJECTOR_GRID_EXECUTED_Z7_X_LENSZ4_UNIQUE_BEST",
        "projector_dictionary": projector_ranks,
        "trial_count": len(grid_rows),
        "rows_ranked": ranked,
        "winner": winner,
        "runner_up": ranked[1],
        "winner_improvement_over_runner_up": ranked[1]["log_residual"] / winner["log_residual"],
        "winner_unique": winner["log_residual"] < ranked[1]["log_residual"],
        "target_ranking_disclosed": True,
        "accepted_as_strict_selector": False,
    }
    execution = {
        "schema": "MTTFrozenZeroParameterGaugeExecution.v1",
        "status": "TYPED_ZERO_CONTINUOUS_PARAMETER_SUB2PPM_CANDIDATE_FROZEN_NOT_PROMOTED",
        "formula_id": "T79_Z7Green_LensZ4Route_v1",
        "formula_frozen_before_future_validation": True,
        "new_continuous_parameters": 0,
        "K_over_K2": winner["K_over_K2"],
        "profile_K_over_K2_downstream_only": [target_r1, 1.0, target_r3],
        "relative_residual_ppm_U1_SU3": winner["relative_residual_ppm_U1_SU3"],
        "log_residual": winner["log_residual"],
        "both_ratios_within_2ppm": max(abs(value) for value in winner["relative_residual_ppm_U1_SU3"]) < 2.0,
        "exact_central_value_equality": False,
        "prediction_profile_promoted": False,
        "validation_policy": "Do not alter the formula. Test it against an independently versioned common-scheme coupling profile or another declared scale with covariance.",
    }
    contract = {
        "schema": "MTTNextSameActionDerivationAndValidationContract.v1",
        "status": "ACTION_DERIVATION_AND_OUT_OF_SAMPLE_VALIDATION_REQUIRED",
        "required_proofs": [
            "derive T79 times the normalized L64 Green trace from one second variation or spectral action",
            "derive P7_nontrivial on the colored residual channel and P4_nontrivial on the charged-lepton return channel",
            "prove the direct T79 plus routed Green-response sum in the e sector",
            "preserve gauge commutation and A67 positive family blocks",
            "validate the frozen formula on an independently versioned common-scheme profile or another scale with covariance",
        ],
        "guardrails": [
            "do not retune projector ranks or add a coefficient after validation",
            "do not use A70's ill-typed denominator as source support",
            "do not call same-profile sub-2ppm agreement an independent prediction",
        ],
        "next_required_artifact": NEXT,
    }
    checks = {
        "A70_ill_typed_route_not_reused": not data["A71_typing"]["verdict"]["strict_promotion_allowed"],
        "actual_spectrum_has_16_modes": len(eigenvalues) == 16,
        "green_trace_positive": normalized_green_trace > 0.0,
        "projector_rank_6_over_7": abs(projector_ranks["Z7_nontrivial"] - 6.0 / 7.0) < 1e-15,
        "projector_rank_3_over_4": abs(projector_ranks["LensZ4_nontrivial"] - 3.0 / 4.0) < 1e-15,
        "full_grid_has_36_rows": len(grid_rows) == 36,
        "Z7_LensZ4_is_unique_best": winner["q_projector"] == "Z7_nontrivial" and winner["e_projector"] == "LensZ4_nontrivial" and grid["winner_unique"],
        "winner_beats_runner_up_by_factor_gt_5": grid["winner_improvement_over_runner_up"] > 5.0,
        "both_gauge_ratios_within_2ppm": execution["both_ratios_within_2ppm"],
        "zero_continuous_parameters": execution["new_continuous_parameters"] == 0,
        "not_promoted": not execution["prediction_profile_promoted"],
    }
    candidate = {
        "schema": "MTTSelectedGaugeKineticFunctionalOfL64AndQ79ChordOrStrictResidualValueEmission.v1",
        "status": STATUS,
        "results": {
            "typed_same_object_functional_constructed": True,
            "canonical_projector_grid_complete": True,
            "Z7_x_LensZ4_unique_best": True,
            "zero_continuous_parameter_formula_frozen": True,
            "sub2ppm_same_profile_match": True,
            "same_action_source_theorem_closed": False,
            "independent_validation_closed": False,
            "strict_gauge_values_accepted": 0,
        },
        "outputs": {
            "functional": str(FUNCTIONAL.relative_to(ROOT)).replace("\\", "/"),
            "grid": str(GRID.relative_to(ROOT)).replace("\\", "/"),
            "execution": str(EXECUTION.relative_to(ROOT)).replace("\\", "/"),
            "contract": str(CONTRACT.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {key: bool(value) for key, value in checks.items()},
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_GaugeKineticFunctionalOfL64AndQ79Chord_or_StrictResidualValueEmission_v1",
        "status": STATUS,
        "T79": torsion,
        "normalized_green_trace_L64": normalized_green_trace,
        "projector_ranks_q_e": [6.0 / 7.0, 3.0 / 4.0],
        "delta_q_delta_e": [winner["delta_q"], winner["delta_e"]],
        "K_over_K2": winner["K_over_K2"],
        "relative_residual_ppm_U1_SU3": winner["relative_residual_ppm_U1_SU3"],
        "canonical_grid_winner_margin": grid["winner_improvement_over_runner_up"],
        "new_continuous_parameters": 0,
        "same_action_source_closed": False,
        "independent_validation_closed": False,
        "strict_gauge_values_accepted": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Gauge Kinetic Functional of L64 and q79 Chord or Strict Residual Value Emission v1

## Typed functional

Let `G64=(1/16)Tr(L64^-1)={normalized_green_trace:.17g}`. The canonical nontrivial-character
projectors on the selected `Z7` and Lens `Z4` carriers have normalized ranks `6/7` and `3/4`.
Define

```text
delta_q = T79 * (6/7) * G64,
delta_e = T79 + (3/4) delta_q.
```

Every factor is a dimensionless normalized trace or positive spectral value. No carrier label is
added to an eigenvalue, and A70's ill-typed denominator is not used.

## Canonical grid

The complete `6x6` grid from nontrivial projectors on `Z3,Z4,Z7,Z16,Z64` plus the unit projector was
executed. `Z7_nontrivial x LensZ4_nontrivial` is the unique best row, beating the runner-up by a
factor of `{grid['winner_improvement_over_runner_up']:.6g}` in log residual. This ranking is disclosed
as same-profile/after-the-fact evidence, not independent selection.

## Frozen execution

```text
K/K2 = {winner['K_over_K2']},
relative residual ppm (U1,SU3) = {winner['relative_residual_ppm_U1_SU3']}.
```

The formula has zero continuous parameters and is now frozen. Strict promotion still requires one
action theorem deriving the product/sum and projector routing, followed by validation against an
independently versioned profile or another scale with covariance.

Next artifact: `{NEXT}`.
"""

    dump(FUNCTIONAL, functional)
    dump(GRID, grid)
    dump(EXECUTION, execution)
    dump(CONTRACT, contract)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
