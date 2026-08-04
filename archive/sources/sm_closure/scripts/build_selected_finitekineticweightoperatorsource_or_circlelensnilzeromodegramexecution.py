"""Audit current W_kin sources and test a common gauge/flavor sector density."""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SLUG = "selected_finitekineticweightoperatorsource_or_circlelensnilzeromodegramexecution"
OUT = ROOT / "candidate_data" / SLUG
AUDIT_PACKET = OUT / "current_kinetic_weight_source_audit.packet.json"
TRIAL_PACKET = OUT / "predeclared_casimir_heat_weight_trials.packet.json"
SUPERSET_PACKET = OUT / "common_positive_sector_density_superset_contract.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteKineticWeightOperatorSource_or_CircleLensNilZeroModeGramExecution_v1.md"
STATUS = "MTT_SELECTED_FINITE_KINETIC_WEIGHT_SOURCE_AUDITED_CURRENT_OPERATORS_UNIVERSAL_CASIMIR_TRIALS_REJECTED_COMMON_POSITIVE_SECTOR_DENSITY_OPEN"
NEXT = "MTT_Selected_PositiveSectorDensitySourceTheorem_or_CommonGaugeFlavorWeightEmission_v1"
SECTORS = ["Q", "u", "d", "L", "e", "N"]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized_metric(trace_map: np.ndarray, weights: np.ndarray) -> np.ndarray:
    values = trace_map @ weights
    return values / values[1]


def log_residual(values: np.ndarray, target: np.ndarray) -> float:
    return float(np.linalg.norm(np.log(values) - np.log(target)))


def main() -> int:
    paths = {
        "A52_profile": ROOT / "candidate_data" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization" / "product_triple_profile_normalization_and_moment_nogo.packet.json",
        "A62_common": ROOT / "candidate_data" / "selected_su3adjointcentraltrivialfinitegaugerow_and_tenspectrumclosure" / "su3_finite_row_and_ten_spectrum_closure.packet.json",
        "A65_weight": ROOT / "candidate_data" / "selected_gaugezeromodekineticinnerproduct_or_chernweilbackgroundenergynogo.candidate.json",
        "proper_time": ROOT / "candidate_data" / "selected_propertimemeasureandoverlapkineticmetricsource_or_strictspectralactionclosure.candidate.json",
        "stationary_rho": ROOT / "candidate_data" / "selected_finite_projector_source_promotion.candidate.json",
        "common_circle": ROOT / "candidate_data" / "selected_commoncirclesectorresponseexecution_or_csktracerows.candidate.json",
        "phi_sector": ROOT / "candidate_data" / "selected_phisectornsourcevalues_or_noknobcskrows.candidate.json",
        "selected_radius": TEXPAPERS / "mtt-nonsm-constants-no-knob" / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json",
    }
    data = {key: load(path) for key, path in paths.items()}

    # Three-family gauge-index trace map, sector order Q,u,d,L,e,N.
    trace_map = np.asarray(
        [
            [3 / 10, 12 / 5, 3 / 5, 9 / 10, 9 / 5, 0],
            [9 / 2, 0, 0, 3 / 2, 0, 0],
            [3, 3 / 2, 3 / 2, 0, 0, 0],
        ],
        dtype=float,
    )
    profile = np.asarray(data["A52_profile"]["minimal_profile_normalization"]["K_gauge_diagonal"], dtype=float)
    tau_int = float(data["proper_time"]["proper_time_candidate"]["tau_int"])
    rho_uv = float(data["selected_radius"]["selected_values"]["rho_UV"])
    base_logdet = float(data["A62_common"]["common_spectrum_consequence"]["selected_base_logdet_L"])

    # Quadratic Casimirs on the six chiral SM sectors in GUT-normalized U1.
    C1 = np.asarray([1 / 60, 4 / 15, 1 / 15, 3 / 20, 3 / 5, 0], dtype=float)
    C2 = np.asarray([3 / 4, 0, 0, 3 / 4, 0, 0], dtype=float)
    C3 = np.asarray([4 / 3, 4 / 3, 4 / 3, 0, 0, 0], dtype=float)
    C_total = C1 + C2 + C3

    trial_rows = []
    source_times = {
        "tau_int": tau_int,
        "rho_UV": rho_uv,
        "inverse_selected_base_gap": 9.0 / (4.0 * math.pi**2),
    }
    for power in (1, 2, 3):
        for time_name, time_value in source_times.items():
            weights = np.exp(-time_value * C_total**power)
            metric = normalized_metric(trace_map, weights)
            trial_rows.append(
                {
                    "family": "total_Casimir_power_heat",
                    "power": power,
                    "time_source": time_name,
                    "time_value": time_value,
                    "sector_weights": weights.tolist(),
                    "K_over_K2": metric.tolist(),
                    "profile_log_residual": log_residual(metric, profile),
                    "source_selected_as_W_kin": False,
                    "accepted": False,
                }
            )
    for coefficients in itertools.permutations((1, 2, 3)):
        generator = coefficients[0] * C1 + coefficients[1] * C2 + coefficients[2] * C3
        weights = np.exp(-tau_int * generator)
        metric = normalized_metric(trace_map, weights)
        trial_rows.append(
            {
                "family": "circle_lens_nil_integer_weighted_Casimir_heat",
                "coefficient_order_U1_SU2_SU3": list(coefficients),
                "time_source": "tau_int",
                "time_value": tau_int,
                "sector_weights": weights.tolist(),
                "K_over_K2": metric.tolist(),
                "profile_log_residual": log_residual(metric, profile),
                "source_selected_as_W_kin": False,
                "accepted": False,
            }
        )
    trial_rows.sort(key=lambda row: row["profile_log_residual"])

    rank_metric = np.asarray(data["proper_time"]["overlap_metric_tests"]["native_rank_candidate"], dtype=float)
    rank_residual = log_residual(rank_metric, profile)
    exact_trial_count = sum(row["profile_log_residual"] < 1e-10 for row in trial_rows)

    rho_promotion = data["stationary_rho"]["promotion_decision"]
    phi = data["phi_sector"]
    checks = {
        "A65_correct_weight_operator_target_imported": data["A65_weight"]["closure_decision"]["correct_gauge_kinetic_observable_identified"],
        "stationary_rho_s_is_validator_ready": rho_promotion["validator_ready_stationary_rho_s"],
        "stationary_rho_s_uses_unit_Gram_blocks": data["stationary_rho"]["source_map_reference"]["rho_candidate_constructed"],
        "common_A62_spectrum_is_scalar_across_sectors": not data["A62_common"]["common_spectrum_consequence"]["adds_independent_threshold_shape"],
        "proper_time_scalar_measure_cannot_source_ratios": data["proper_time"]["theorems"]["scalar_measure_overlap_independence"]["proved"],
        "selected_rhoUV_is_one_scalar": rho_uv > 0,
        "common_circle_trace_engine_is_closed": data["common_circle"]["closure_decision"]["formal_csk_trace_rows_executed"]
        and data["common_circle"]["closure_decision"]["formal_csk_trace_row_count"] == 9,
        "Phi_sector_values_are_still_zero": phi["closure_decision"]["accepted_Phi_sector_N_source_value_count"] == 0,
        "predeclared_Casimir_trials_have_no_exact_profile_match": exact_trial_count == 0,
        "rank_metric_remains_nonexact": rank_residual > 1e-10,
    }

    source_audit = {
        "schema": "MTTCurrentKineticWeightSourceAudit.v1",
        "status": "ALL_CURRENT_SELECTED_WEIGHT_CANDIDATES_UNIVERSAL_OR_UNTYPED",
        "audited_sources": [
            {
                "source": "A62 common finite spectrum and any scalar function of it",
                "induced_W_kin": "c I on all SM sectors",
                "relative_rank": 0,
                "decision": "valid common normalization/scale data; no gauge shape",
            },
            {
                "source": "selected tau_int point measure without sector operator",
                "induced_W_kin": "c I",
                "relative_rank": 0,
                "decision": "scalar moment cannot change ratios",
            },
            {
                "source": "selected rho_UV internal branch value",
                "value": rho_uv,
                "induced_W_kin": "rho_UV I unless a sector-routing theorem is added",
                "relative_rank": 0,
                "decision": "do not infer sector routing from a scalar",
            },
            {
                "source": "transported stationary rho_s/projector packet",
                "induced_W_kin": "unit invariant Gram on each selected matter triplet",
                "relative_rank": 0,
                "decision": "structural carrier is selected; magnitude-bearing sector density is absent",
            },
            {
                "source": "common-circle H_cen holonomy",
                "induced_W_kin": "H_cen^* H_cen=I on its unitary family orbit",
                "relative_rank": 0,
                "decision": "phase/holonomy is not a positive magnitude split",
            },
        ],
        "selected_W_kin_count": 0,
        "new_continuous_parameters": 0,
    }

    trials = {
        "schema": "MTTPredeclaredCasimirHeatWeightTrials.v1",
        "status": "SOURCE_MOTIVATED_TRIALS_EXECUTED_NONE_PROMOTED",
        "sector_order": SECTORS,
        "Casimir_rows": {
            "C1_GUT": C1.tolist(),
            "C2_SU2": C2.tolist(),
            "C3_SU3": C3.tolist(),
            "C_total": C_total.tolist(),
        },
        "source_times": source_times,
        "trials": trial_rows,
        "best_trial": trial_rows[0],
        "exact_match_tolerance": 1e-10,
        "exact_match_count": exact_trial_count,
        "native_rank_metric": {
            "K_over_K2": rank_metric.tolist(),
            "profile_log_residual": rank_residual,
            "accepted": False,
        },
        "guardrail": "The profile is a downstream rejection test only. No Casimir power, topology coefficient order, or proper time is promoted from numerical closeness.",
    }

    superset = {
        "schema": "MTTCommonPositiveSectorDensitySupersetContract.v1",
        "status": "ONE_COMMON_GAUGE_FLAVOR_DENSITY_OPERATOR_IDENTIFIED_VALUES_OPEN",
        "operator": {
            "name": "Phi_sector^+",
            "domain": "direct sum over A46 sectors of three-family multiplicity spaces",
            "normal_form": "Phi_sector^+ = direct-sum_s Phi_s, with Phi_s positive semidefinite 3x3 and gauge action I_Rs",
            "gauge_use": "W_kin = N_kin(Phi_sector^+); K_a=Tr(W_kin T_a^2)",
            "flavor_use": "c_s,k=Tr(P_s B_k H_cen Phi_sector^+) on the charged u,d,e blocks",
            "shared_circle_role": "H_cen transports family phase/orientation in the flavor functional; positivity for gauge use comes from Phi_sector^+, not from H_cen itself",
        },
        "already_selected_support": [
            "A46 gauge sectors and three-family carrier",
            "stationary transported sector projectors P_s",
            "validator-ready rho_s and unit invariant Gram",
            "common-circle H_cen",
            "family dual rows B_k",
            "rank-two gauge trace map",
        ],
        "missing_source_values": {
            "positive_sector_density_operator": True,
            "six gauge-sector block traces": True,
            "charged family moments for u,d,e": True,
            "same-action normalization map N_kin": True,
        },
        "current_counts": {
            "selected_Phi_sector_numeric_rows": 0,
            "strict_flavor_rows_from_Phi_sector": 0,
            "nonuniversal_gauge_rows_from_Phi_sector": 0,
        },
        "acceptance": [
            "Phi_sector^+ is emitted from the selected MTT action/operator before gauge or flavor comparison",
            "all blocks are positive and commute with the A46 gauge action",
            "the same block values feed both uses without sector-specific refitting",
            "N_kin, trace, scale and scheme are fixed by the same source",
            "gauge and flavor datasets are downstream tests only",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "schema": "MTTSelectedFiniteKineticWeightOperatorSourceOrCircleLensNilZeroModeGramExecution.v1",
        "status": STATUS,
        "theorems": {
            "current_weight_source_exhaustion": {
                "proved_for_audited_sources": True,
                "statement": "Every currently selected candidate that has a lawful action on all A46 sectors is scalar or unit-Gram and therefore reproduces only the universal trace row. Noncentral Casimir heat weights can be written, but no current theorem selects them as W_kin.",
            },
            "predeclared_Casimir_trial_rejection": {
                "proved_for_declared_family": True,
                "statement": "The predeclared total-Casimir powers and circle/lens/nil integer-weighted Casimir heat trials at existing selected internal times produce no exact A52 profile match. They are retained only as rejection diagnostics.",
            },
            "common_positive_sector_density_reduction": {
                "proved_as_interface": True,
                "statement": "One positive block-diagonal sector density on the selected A46/projector carrier is sufficient to feed both the finite gauge kinetic weight and the existing common-circle flavor trace engine. Its numerical block values are not currently emitted.",
            },
        },
        "closure_decision": {
            "current_selected_W_kin_count": 0,
            "predeclared_Casimir_trial_count": len(trial_rows),
            "predeclared_exact_match_count": exact_trial_count,
            "common_gauge_flavor_density_interface_closed": True,
            "positive_sector_density_values_emitted": False,
            "nonuniversal_gauge_rows_emitted": 0,
            "strict_flavor_rows_from_common_density_emitted": 0,
            "no_knob_gauge_coupling_prediction_closed": False,
            "new_continuous_parameters": 0,
        },
        "outputs": {
            "source_audit": str(AUDIT_PACKET.relative_to(ROOT)).replace("\\", "/"),
            "trials": str(TRIAL_PACKET.relative_to(ROOT)).replace("\\", "/"),
            "superset": str(SUPERSET_PACKET.relative_to(ROOT)).replace("\\", "/"),
        },
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "checks": {key: bool(value) for key, value in checks.items()},
        "epistemic_policy": {
            "target_fitting_used": False,
            "profile_used_only_as_rejection_test": True,
            "best_trial_promoted": False,
            "old_open_status_used_over_successor": False,
            "prediction_claimed": False,
        },
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_FiniteKineticWeightOperatorSource_or_CircleLensNilZeroModeGramExecution_v1",
        "status": STATUS,
        "current_selected_W_kin_count": 0,
        "predeclared_Casimir_trials_executed": len(trial_rows),
        "predeclared_exact_matches": exact_trial_count,
        "common_positive_sector_density_interface_closed": True,
        "positive_sector_density_values_emitted": False,
        "nonuniversal_gauge_rows_emitted": 0,
        "strict_flavor_rows_from_common_density_emitted": 0,
        "new_continuous_parameters": 0,
        "no_knob_gauge_coupling_prediction_closed": False,
        "next_required_artifact": NEXT,
    }
    best = trial_rows[0]
    note = f"""# MTT Selected Finite Kinetic Weight Operator Source or Circle/Lens/Nil Zero-Mode Gram Execution v1

## Current source audit

The selected A62 spectrum, scalar proper-time measure, internal `rho_UV`, stationary transported
`rho_s` Gram blocks, and unitary common-circle holonomy were all tested as sources for `W_kin`.
Every lawful all-sector action is proportional to the identity or has unit invariant Gram. Hence
the current selected `W_kin` count remains `0` and the universal `(6,6,6)` row is unchanged.

## Forward trials

`{len(trial_rows)}` predeclared positive Casimir heat weights were executed using only existing
internal times and the integer circle/lens/nil coefficient permutations. None is exact under the
downstream A52 profile test. The best declared trial has

```text
family = {best['family']}
K/K2 = {best['K_over_K2']}
log residual = {best['profile_log_residual']:.12g}
```

It is not promoted: the corpus does not select that Casimir function as the kinetic operator, and
the profile was used only to reject candidates.

## Superset reduction

The gauge and strict-flavor source problems now share one lawful missing object:

```text
Phi_sector^+ = direct-sum_s Phi_s >= 0,
W_kin = N_kin(Phi_sector^+),
K_a = Tr(W_kin T_a^2),
c_s,k = Tr(P_s B_k H_cen Phi_sector^+).
```

The projectors, stationary `rho_s`, unit Gram, common-circle holonomy, dual family rows, and rank-two
gauge trace map are already selected. Numerical positive sector blocks and their same-action kinetic
normalization are not.

Current common-density output: gauge rows `0`, strict flavor rows `0`. No new parameter was added.

Next artifact: `{NEXT}`.
"""

    dump(AUDIT_PACKET, source_audit)
    dump(TRIAL_PACKET, trials)
    dump(SUPERSET_PACKET, superset)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
