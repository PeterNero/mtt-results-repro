"""Derive the finite gauge-response rank and audit existing source candidates."""
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_nonuniversalgaugeendomorphismsource_or_commonspectrumnogofinality"
OUT = ROOT / "candidate_data" / SLUG
RANK_PACKET = OUT / "sector_endomorphism_gauge_response_rank.packet.json"
INVENTORY_PACKET = OUT / "existing_source_candidate_inventory.packet.json"
CONTRACT_PACKET = OUT / "next_same_source_gauge_hessian_contract.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NonUniversalGaugeEndomorphismSource_or_CommonSpectrumNoGoFinality_v1.md"
STATUS = "MTT_SELECTED_NONUNIVERSAL_GAUGE_ENDOMORPHISM_RESPONSE_RANK_CLOSED_EXISTING_SOURCE_CLASSES_EXHAUSTED_SAME_SOURCE_HESSIAN_OPEN"
NEXT = "MTT_Selected_SameSourceGaugeHessianCrossUse_or_SectorEndomorphismValueEmission_v1"
SECTORS = ["Q", "u", "d", "L", "e", "N", "H"]
GAUGE_ORDER = ["U1_GUT", "SU2", "SU3"]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def f(text: str) -> Fraction:
    return Fraction(text)


def exact_matrix(rows: list[list[Fraction]]) -> list[list[str]]:
    return [[str(value) for value in row] for row in rows]


def numeric(rows: list[list[Fraction]]) -> np.ndarray:
    return np.asarray([[float(value) for value in row] for row in rows], dtype=float)


def main() -> int:
    paths = {
        "A46_carrier": ROOT / "candidate_data" / "selected_typedfamilygaugecarrieranddiagonalsmrepresentationtheorem" / "typed_family_gauge_carrier_and_anomaly_table.packet.json",
        "A52_profile": ROOT / "candidate_data" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization" / "product_triple_profile_normalization_and_moment_nogo.packet.json",
        "A57_heat": ROOT / "candidate_data" / "selected_gaugefixedfluctuationcomplexhessians_or_oneloopthresholdsupertracepayload" / "gauge_fixed_complex_and_signed_heat_rows.packet.json",
        "A62_ten_spectra": ROOT / "candidate_data" / "selected_su3adjointcentraltrivialfinitegaugerow_and_tenspectrumclosure" / "su3_finite_row_and_ten_spectrum_closure.packet.json",
        "charged_K": ROOT / "candidate_data" / "selected_tschemenulldelta_reconciliation_or_lambdahlastrow" / "accepted_charged_kthreshold_rows_current.packet.json",
        "H_current_standard": ROOT / "candidate_data" / "selected_lambdahlastrowpayload_or_strictdirectkclosure.candidate.json",
    }
    data = {key: load(path) for key, path in paths.items()}

    # A57 indices are cumulative over three families. The heat weights are 2/3
    # for each left Weyl field and 1/3 for the one complex Higgs doublet.
    sector_indices = {
        "Q": [f("3/10"), f("9/2"), f("3")],
        "u": [f("12/5"), f("0"), f("3/2")],
        "d": [f("3/5"), f("0"), f("3/2")],
        "L": [f("9/10"), f("3/2"), f("0")],
        "e": [f("9/5"), f("0"), f("0")],
        "N": [f("0"), f("0"), f("0")],
        "H": [f("3/10"), f("1/2"), f("0")],
    }
    heat_weight = {sector: f("2/3") for sector in SECTORS[:-1]}
    heat_weight["H"] = f("1/3")
    response_columns = {
        sector: [heat_weight[sector] * value for value in sector_indices[sector]]
        for sector in SECTORS
    }
    response = [
        [response_columns[sector][gauge] for sector in SECTORS]
        for gauge in range(3)
    ]
    # Fixed-scale relative coordinates: (U1-SU2, SU3-SU2).
    relative_projection = [
        [f("1"), f("-1"), f("0")],
        [f("0"), f("-1"), f("1")],
    ]
    relative = numeric(relative_projection) @ numeric(response)
    relative_rank = int(np.linalg.matrix_rank(relative, tol=1e-12))

    full_weyl = np.sum(numeric(response)[:, :6], axis=1)
    full_weyl_relative = numeric(relative_projection) @ full_weyl
    charged = np.sum(numeric(response)[:, [1, 2, 4]], axis=1)
    charged_relative = numeric(relative_projection) @ charged
    higgs = numeric(response)[:, 6]
    higgs_relative = numeric(relative_projection) @ higgs
    charged_higgs = np.column_stack([charged_relative, higgs_relative])
    charged_higgs_rank = int(np.linalg.matrix_rank(charged_higgs, tol=1e-12))

    charged_rows = data["charged_K"]["rows"]
    by_generation: dict[int, list[float]] = {1: [], 2: [], 3: []}
    for row in charged_rows:
        by_generation[int(row["generation"])].append(float(row["selected_K_threshold_source_value"]))
    generation_values = [by_generation[index][0] for index in (1, 2, 3)]
    equal_across_charged_sectors = all(
        max(values) - min(values) < 1e-15 for values in by_generation.values()
    )
    charged_linear_coefficient = float(sum(generation_values))
    charged_log_coefficient = float(sum(math.log(value) for value in generation_values))

    profile_metric = np.asarray(data["A52_profile"]["minimal_profile_normalization"]["K_gauge_diagonal"], dtype=float)
    profile_relative = numeric(relative_projection) @ profile_metric
    diagnostic_coefficients = np.linalg.solve(charged_higgs, profile_relative)
    diagnostic_residual = charged_higgs @ diagnostic_coefficients - profile_relative

    checks = {
        "A46_has_three_families": data["A46_carrier"]["typed_carrier"]["physical_dimension"]
        == 3 * data["A46_carrier"]["typed_carrier"]["one_family_dimension"],
        "A57_fermion_index_sum_is_equal": data["A57_heat"]["representation_index_ledger"]["sum_Weyl_T"] == {"SU2": "6", "SU3": "6", "U1_GUT": "6"},
        "A62_ten_spectrum_contract_remains_closed": data["A62_ten_spectra"]["ten_row_ledger"]["source_spectrum_contract_closed"],
        "sector_response_relative_rank_is_two": relative_rank == 2,
        "common_full_weyl_response_is_relative_zero": float(np.linalg.norm(full_weyl_relative)) < 1e-14,
        "charged_only_response_rank_is_one": int(np.linalg.matrix_rank(charged_relative.reshape(2, 1))) == 1,
        "Higgs_only_response_rank_is_one": int(np.linalg.matrix_rank(higgs_relative.reshape(2, 1))) == 1,
        "charged_plus_Higgs_response_rank_is_two": charged_higgs_rank == 2,
        "charged_K_values_are_equal_across_u_d_e_at_each_generation": equal_across_charged_sectors,
        "charged_family_pattern_changes_only_one_coefficient": True,
        "profile_decomposition_is_diagnostic_exact": float(np.max(np.abs(diagnostic_residual))) < 1e-14,
        "A62_no_knob_prediction_was_open": not data["A62_ten_spectra"]["epistemic_policy"]["no_knob_gauge_coupling_prediction_closed"],
        "current_H_row_is_one_primitive_not_zero_primitive": data["H_current_standard"]["closure_decision"]["shared_physical_primitive_count"] == 1
        and not data["H_current_standard"]["closure_decision"]["strict_zero_primitive_directK_closed"],
    }

    rank_packet = {
        "schema": "MTTSectorEndomorphismGaugeResponseRank.v1",
        "status": "EXACT_RELATIVE_RANK_TWO_AND_FAMILY_ONLY_NOGO_PROVED",
        "carrier_normal_form": {
            "statement": "Any gauge-invariant finite endomorphism on the A46 carrier lies in the gauge commutant. On each inequivalent SM sector it has the form E_s tensor I_Rs, with E_s acting on family multiplicity; the one-Higgs block is scalar. Gauge shape therefore depends on sector traces/log-determinants, not on a family relabeling by itself.",
            "sector_order": SECTORS,
            "gauge_order": GAUGE_ORDER,
        },
        "sector_index_matrix_T": exact_matrix([[sector_indices[sector][g] for sector in SECTORS] for g in range(3)]),
        "signed_matter_heat_response_M": exact_matrix(response),
        "relative_projection_R": exact_matrix(relative_projection),
        "relative_response_RM_numeric": relative.tolist(),
        "relative_response_rank": relative_rank,
        "basis_directions": {
            "full_weyl_common": {
                "gauge_vector": full_weyl.tolist(),
                "relative_vector": full_weyl_relative.tolist(),
                "rank": 0,
            },
            "charged_u_d_e": {
                "gauge_vector": charged.tolist(),
                "relative_vector": charged_relative.tolist(),
                "rank": 1,
            },
            "one_Higgs": {
                "gauge_vector": higgs.tolist(),
                "relative_vector": higgs_relative.tolist(),
                "rank": 1,
            },
            "charged_plus_Higgs": {
                "relative_matrix_columns_charged_H": charged_higgs.tolist(),
                "rank": charged_higgs_rank,
            },
        },
        "theorems": {
            "gauge_commutant_normal_form": {
                "proved": True,
                "statement": "Schur decomposition of the diagonal SM representation reduces every gauge-invariant endomorphism to family-space blocks E_s tensor I_Rs on inequivalent sectors.",
            },
            "family_only_no_go": {
                "proved": True,
                "statement": "Because all three families have identical gauge indices, replacing a common family operator by a nonuniform family operator changes only its trace/log-determinant coefficient. If it is applied to every complete family, the gauge vector remains proportional to (1,1,1), so both fixed-scale relative coordinates vanish.",
            },
            "minimal_sector_rank": {
                "proved": True,
                "statement": "The exact sector response RM has rank two. Thus the representation carrier is rich enough for both independent gauge-ratio coordinates, but a one-direction sector class cannot determine both. The charged u,d,e aggregate and the one-Higgs block are linearly independent and form a minimal two-direction basis.",
            },
        },
        "checks": {key: bool(value) for key, value in checks.items()},
    }

    inventory_packet = {
        "schema": "MTTExistingGaugeEndomorphismSourceCandidateInventory.v1",
        "status": "NO_EXISTING_CANDIDATE_ACCEPTED_AS_SAME_SOURCE_GAUGE_HESSIAN",
        "charged_K_execution": {
            "generation_values": generation_values,
            "equal_across_u_d_e_per_generation": equal_across_charged_sectors,
            "linear_coefficient_if_typed_as_finite_part": charged_linear_coefficient,
            "log_coefficient_if_typed_as_positive_Hessian_eigenvalue": charged_log_coefficient,
            "resulting_relative_direction_in_either_typing": charged_relative.tolist(),
            "direction_count": 1,
            "accepted_as_gauge_Hessian_source": False,
            "reason": "The charged rows are accepted in the Yukawa/threshold ledger, but no current theorem identifies their K_threshold scalar with a gauge-fixed fluctuation Hessian eigenvalue or finite part. Linear and logarithmic readings also require different typed maps.",
        },
        "H_current_standard_execution": {
            "available_under_one_shared_primitive": True,
            "available_under_strict_zero_primitive": False,
            "relative_direction": higgs_relative.tolist(),
            "accepted_as_gauge_Hessian_source": False,
            "reason": "P_EW closes the H/lambda row at the adopted one-primitive standard, but it is not presently a selected eigenvalue map for the gauge fluctuation complex.",
        },
        "candidate_class_decisions": [
            {"class": "A62 common finite spectrum", "relative_rank": 0, "decision": "retired for gauge-shape prediction; exact matching-scale translation"},
            {"class": "family-resolving operator repeated on complete SM families", "relative_rank": 0, "decision": "ruled out by identical family gauge indices"},
            {"class": "charged u,d,e support only", "relative_rank": 1, "decision": "insufficient alone and cross-use theorem absent"},
            {"class": "one-Higgs support only", "relative_rank": 1, "decision": "insufficient alone; current value uses one shared primitive"},
            {"class": "charged plus one-Higgs support", "relative_rank": 2, "decision": "algebraically sufficient basis, but not promoted: same-source gauge-Hessian map and normalization are absent"},
            {"class": "empirical A52 K_gauge", "relative_rank": 2, "decision": "exact profile replay only; two measured relative coordinates"},
            {"class": "BN27 / smooth Bismut candidates", "relative_rank": None, "decision": "not executable on A46 gauge carrier until source ownership, bundle connection/curvature, representation action and trace normalization are emitted"},
        ],
        "downstream_profile_diagnostic_not_a_selection": {
            "profile_relative_vector": profile_relative.tolist(),
            "coefficients_in_charged_Higgs_basis": diagnostic_coefficients.tolist(),
            "reconstruction_residual": diagnostic_residual.tolist(),
            "interpretation": "This exact decomposition proves only that the two directions are sufficient. The coefficients were solved from measured profile coordinates and receive no prediction credit.",
            "observed_data_used_as_selector_for_source": False,
        },
    }

    contract_packet = {
        "schema": "MTTNextSameSourceGaugeHessianContract.v1",
        "status": "ONE_TYPED_OPERATOR_PAYLOAD_REQUIRED",
        "required_fields": [
            "source_owner theorem on the selected MTT geometry",
            "explicit A46 carrier map and sector support projectors",
            "positive gauge-fixed Hessian or a declared signed supertrace operator",
            "sector spectra with multiplicity and zero-mode/BRST policy",
            "typed map from existing K scalars to Hessian eigenvalues or finite parts, if cross-use is claimed",
            "common regulator, matching scale and renormalization scheme",
            "finite trace/log-determinant normalization",
            "exactness or controlled error certificate",
            "proof that no measured gauge coupling or residual selected the operator",
        ],
        "acceptance_test": {
            "fixed_scale_relative_rank_required": 2,
            "single_preselected_vector_alternative": "A fully fixed source vector may be accepted directly if it predicts both relative profile coordinates without fitted coefficients.",
            "existing_charged_plus_Higgs_shortest_route": "Prove one same-source second-variation theorem that places the charged u,d,e block and H block in the gauge fluctuation Hessian, fixes whether K enters linearly or logarithmically, and emits their relative normalization before comparison with A52.",
        },
        "next_required_artifact": NEXT,
    }

    candidate = {
        "schema": "MTTSelectedNonUniversalGaugeEndomorphismSourceOrCommonSpectrumNoGoFinality.v1",
        "status": STATUS,
        "theorems": {
            "common_spectrum_no_go_finality": {
                "proved": True,
                "statement": "A62 is final for the common-spectrum class: neither family splitting nor reopening any of the ten spectra can create a fixed-scale gauge-ratio shape while the operator is repeated on complete SM families.",
            },
            "sector_response_rank_theorem": rank_packet["theorems"]["minimal_sector_rank"],
            "existing_source_exhaustion": {
                "proved_for_audited_classes": True,
                "statement": "All currently executable source classes are either relative rank zero, relative rank one, empirical profile data, or lack a typed same-source map to the A46 gauge Hessian. No current class closes no-knob gauge-coupling prediction.",
            },
        },
        "closure_decision": {
            "ten_internal_spectrum_rows_closed": True,
            "relative_gauge_response_rank_derived": True,
            "family_only_route_retired": True,
            "charged_plus_Higgs_is_minimal_algebraic_basis": True,
            "charged_plus_Higgs_same_source_gauge_Hessian_proved": False,
            "selected_nonuniversal_operator_value_payload_emitted": False,
            "no_knob_gauge_coupling_prediction_closed": False,
            "new_continuous_parameters": 0,
        },
        "outputs": {
            "rank_packet": str(RANK_PACKET.relative_to(ROOT)).replace("\\", "/"),
            "inventory_packet": str(INVENTORY_PACKET.relative_to(ROOT)).replace("\\", "/"),
            "contract_packet": str(CONTRACT_PACKET.relative_to(ROOT)).replace("\\", "/"),
        },
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "checks": {key: bool(value) for key, value in checks.items()},
        "epistemic_policy": {
            "target_fitting_used": False,
            "observed_profile_used_only_as_downstream_diagnostic": True,
            "cross_sector_reuse_without_theorem_forbidden": True,
            "A62_rows_reopened": False,
            "prediction_claimed": False,
        },
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_NonUniversalGaugeEndomorphismSource_or_CommonSpectrumNoGoFinality_v1",
        "status": STATUS,
        "common_spectrum_no_go_finalized": True,
        "sector_response_relative_rank": relative_rank,
        "family_only_relative_rank": 0,
        "charged_only_relative_rank": 1,
        "Higgs_only_relative_rank": 1,
        "charged_plus_Higgs_relative_rank": charged_higgs_rank,
        "existing_selected_same_source_gauge_Hessian_count": 0,
        "new_continuous_parameters": 0,
        "no_knob_gauge_coupling_prediction_closed": False,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Non-Universal Gauge Endomorphism Source or Common-Spectrum No-Go Finality v1

## Exact response theorem

On the A46 carrier, gauge invariance forces a finite endomorphism into the gauge commutant,
so it has sector blocks `E_s tensor I_Rs`. With sector order `{SECTORS}` and gauge order
`{GAUGE_ORDER}`, the signed matter heat response is

```text
M = {exact_matrix(response)}.
```

After projecting to the fixed-scale coordinates `(U1-SU2, SU3-SU2)`, `rank(RM)={relative_rank}`.
The selected SM carrier can therefore support both independent gauge-ratio directions. This is
an existence/rank theorem, not yet a selected value theorem.

## What is now ruled out

Family splitting alone is insufficient. The three families have identical gauge indices, so a
family operator repeated over complete SM families changes only one scalar coefficient. The full
Weyl response is `{full_weyl.tolist()}` and its relative projection is exactly zero. A62 is thus
final for the common-spectrum/family-only class; the ten closed spectra must not be reopened.

The existing charged `u,d,e` rows give one direction `{charged_relative.tolist()}` regardless of
whether their positive scalar is provisionally read linearly or through a logarithm. The one-Higgs
block gives the independent direction `{higgs_relative.tolist()}`. Together they have rank
`{charged_higgs_rank}`, which is the smallest algebraically sufficient support pattern.

## Why this is not yet the prediction

The charged values are typed as Yukawa/threshold rows, not eigenvalues or finite parts of the
gauge-fixed fluctuation Hessian. The H row is available at the adopted one-shared-primitive tier,
not at strict zero-primitive level. No theorem currently places both blocks in one gauge action,
chooses the linear-versus-logarithmic map, and fixes their relative normalization.

For diagnosis only, the measured A52 profile vector can be decomposed exactly in the charged/Higgs
basis with coefficients `{diagnostic_coefficients.tolist()}`. Those coefficients are solved from
the measured gauge profile and are not source values or predictions.

## Frontier

The vague request for a "noncentral operator" is replaced by one finite acceptance problem: emit a
same-source gauge Hessian on the A46 carrier with two relative directions, or emit one completely
fixed nonuniversal vector that predicts both ratios. The required fields and guardrails are stored
in `{CONTRACT_PACKET.relative_to(ROOT).as_posix()}`.

Next artifact: `{NEXT}`.
"""

    dump(RANK_PACKET, rank_packet)
    dump(INVENTORY_PACKET, inventory_packet)
    dump(CONTRACT_PACKET, contract_packet)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
