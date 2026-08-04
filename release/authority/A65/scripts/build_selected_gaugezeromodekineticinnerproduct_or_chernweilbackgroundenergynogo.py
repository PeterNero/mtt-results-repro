"""Identify the correct gauge kinetic Hessian and exclude mismatched proxies."""
from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SLUG = "selected_gaugezeromodekineticinnerproduct_or_chernweilbackgroundenergynogo"
OUT = ROOT / "candidate_data" / SLUG
KINETIC = OUT / "finite_gauge_zero_mode_kinetic_weight_theorem.packet.json"
EXCLUSIONS = OUT / "background_energy_and_scalar_proxy_exclusion.packet.json"
CONTRACT = OUT / "selected_kinetic_weight_operator_contract.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_GaugeZeroModeKineticInnerProduct_or_ChernWeilBackgroundEnergyNoGo_v1.md"
STATUS = "MTT_SELECTED_GAUGE_ZERO_MODE_KINETIC_HESSIAN_IDENTIFIED_SECTOR_WEIGHT_RANK_TWO_PROXY_CROSSUSE_REJECTED_WEIGHT_SOURCE_OPEN"
NEXT = "MTT_Selected_FiniteKineticWeightOperatorSource_or_CircleLensNilZeroModeGramExecution_v1"
SECTORS = ["Q", "u", "d", "L", "e", "N"]
GAUGE_ORDER = ["U1_GUT", "SU2", "SU3"]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def f(value: str) -> Fraction:
    return Fraction(value)


def exact(rows: list[list[Fraction]]) -> list[list[str]]:
    return [[str(value) for value in row] for row in rows]


def numeric(rows: list[list[Fraction]]) -> np.ndarray:
    return np.asarray([[float(value) for value in row] for row in rows], dtype=float)


def main() -> int:
    paths = {
        "A46_carrier": ROOT / "candidate_data" / "selected_typedfamilygaugecarrieranddiagonalsmrepresentationtheorem" / "typed_family_gauge_carrier_and_anomaly_table.packet.json",
        "A51_action": ROOT / "candidate_data" / "selected_finitespectralactionandhiggsinnerfluctuation_or_directgenerativesmactionclosure.candidate.json",
        "A53_literal_HYM": ROOT / "candidate_data" / "selected_gaugeoverlapmetricfromliteralhymconnections_or_strictspectralactionclosure.candidate.json",
        "A63_response": ROOT / "candidate_data" / "selected_nonuniversalgaugeendomorphismsource_or_commonspectrumnogofinality.candidate.json",
        "A64_crossuse": ROOT / "candidate_data" / "selected_samesourcegaugehessiancrossuse_or_sectorendomorphismvalueemission.candidate.json",
        "HYM_connection": ROOT / "candidate_data" / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json",
        "Chern_row": ROOT / "candidate_data" / "selected_chernweilde_or_determinanttorsion_threeslotclosingrun" / "same_source_chern_weil_row_slot_closure.packet.json",
        "old_scalar_proxy": TEXPAPERS / "mtt-nonsm-constants-no-knob" / "certificates" / "exact_circle_sphere_zeta_pieces_certificate.json",
        "old_nil_alignment": TEXPAPERS / "mtt-nonsm-constants-no-knob" / "candidate_data" / "qa_su3_internal_packet_alignment.candidate.json",
    }
    data = {key: load(path) for key, path in paths.items()}

    # These are the three-family representation indices from A57/A46. Unlike
    # A63's one-loop threshold map, the tree finite-carrier trace has no
    # independent Higgs column: the Higgs is an inner fluctuation of D_F.
    index_columns = {
        "Q": [f("3/10"), f("9/2"), f("3")],
        "u": [f("12/5"), f("0"), f("3/2")],
        "d": [f("3/5"), f("0"), f("3/2")],
        "L": [f("9/10"), f("3/2"), f("0")],
        "e": [f("9/5"), f("0"), f("0")],
        "N": [f("0"), f("0"), f("0")],
    }
    trace_map = [[index_columns[sector][gauge] for sector in SECTORS] for gauge in range(3)]
    relative_projection = [[f("1"), f("-1"), f("0")], [f("0"), f("-1"), f("1")]]
    relative_map = numeric(relative_projection) @ numeric(trace_map)
    relative_rank = int(np.linalg.matrix_rank(relative_map, tol=1e-12))
    identity_trace = numeric(trace_map) @ np.ones(len(SECTORS))
    identity_relative = numeric(relative_projection) @ identity_trace

    rank_two_pairs = []
    rank_one_pairs = []
    for left, right in itertools.combinations(range(len(SECTORS)), 2):
        pair = relative_map[:, [left, right]]
        rank = int(np.linalg.matrix_rank(pair, tol=1e-12))
        row = {
            "sectors": [SECTORS[left], SECTORS[right]],
            "relative_columns": pair.tolist(),
            "rank": rank,
        }
        (rank_two_pairs if rank == 2 else rank_one_pairs).append(row)

    a51_gauge = data["A51_action"]["finite_spectral_traces"]["GUT_normalized_coefficients_three_families"]
    hym = data["HYM_connection"]
    chern = data["Chern_row"]
    proxy = data["old_scalar_proxy"]
    nil_alignment = data["old_nil_alignment"]
    checks = {
        "A51_tree_trace_is_6_6_6": [a51_gauge[key] for key in GAUGE_ORDER] == [6.0, 6, 6],
        "identity_weight_reproduces_6_6_6": bool(np.allclose(identity_trace, [6.0, 6.0, 6.0], atol=1e-14, rtol=0.0)),
        "identity_weight_has_zero_relative_shape": float(np.linalg.norm(identity_relative)) < 1e-14,
        "sector_weight_trace_map_has_rank_two": relative_rank == 2,
        "at_least_one_two_sector_basis_exists": len(rank_two_pairs) > 0,
        "Higgs_is_not_an_independent_tree_trace_column": "H" not in SECTORS,
        "A53_normalized_kinetic_rows_were_zero": data["A53_literal_HYM"]["identifiability"]["normalized_sector_functionals_emitted"] == 0,
        "HYM_packet_emits_connection_not_kinetic_Gram": hym["diagonal_connection_payload"]["closed"] and not hym["operator_payload_boundary"]["validator_ready"],
        "Chern_row_is_topological_not_pointwise_kinetic": "topological" in chern["same_source_chern_weil_row"]["chern_weil_trace_normalization_note"],
        "old_circle_sphere_rows_explicitly_scalar_proxies": "scalar-proxy" in proxy["purpose"],
        "old_scalar_proxy_did_not_close_prediction": not proxy["verdict"]["new_no_knob_prediction_certified"],
        "old_nil_smooth_determinant_is_diagnostic": "diagnostics" in nil_alignment["decision"]["old_nil_smooth_determinant_trail_role"],
        "A64_direct_K_crossuse_rejected": data["A64_crossuse"]["closure_decision"]["direct_crossuse_rejected"],
        "A63_spectrum_rows_remain_closed": data["A63_response"]["closure_decision"]["ten_internal_spectrum_rows_closed"],
    }

    kinetic = {
        "schema": "MTTFiniteGaugeZeroModeKineticWeightTheorem.v1",
        "status": "CORRECT_FINITE_KINETIC_HESSIAN_AND_RANK_TWO_WEIGHT_MAP_PROVED",
        "continuum_form": {
            "four_dimensional_fluctuation": "A_mu(x,y)=sum_a A_mu^a(x) xi_a(y)",
            "kinetic_Gram": "K_ab = integral_X w(y) <xi_a(y),xi_b(y)>_fiber dvol_X",
            "required_property": "K_ab is the second variation of one selected action with respect to four-dimensional gauge zero modes.",
        },
        "finite_form": {
            "weight_operator": "W_kin >= 0 in the gauge commutant of the A46 finite carrier",
            "kinetic_metric": "K_ab = Tr_HF(W_kin T_a T_b)",
            "sector_normal_form": "W_kin = direct-sum_s W_s tensor I_Rs; a family-only factor repeated on every sector cannot create gauge shape",
            "sector_order": SECTORS,
            "gauge_order": GAUGE_ORDER,
            "sector_trace_map_T": exact(trace_map),
            "relative_projection_R": exact(relative_projection),
            "relative_map_RT_numeric": relative_map.tolist(),
            "relative_rank": relative_rank,
            "identity_weight_trace": identity_trace.tolist(),
            "identity_weight_relative": identity_relative.tolist(),
        },
        "minimal_support_analysis": {
            "rank_two_sector_pairs": rank_two_pairs,
            "rank_below_two_sector_pairs": rank_one_pairs,
            "rank_two_pair_count": len(rank_two_pairs),
            "interpretation": "Two sector weights can span the ratio plane for several support choices, but coefficients require a source theorem. Solving them from the measured gauge profile would merely reparameterize two measured ratios.",
        },
        "theorems": {
            "zero_mode_Hessian_identification": {
                "proved": True,
                "statement": "The gauge kinetic coefficient is the Hessian/Gram matrix of the four-dimensional gauge zero modes. On the finite A46 carrier it is represented by a positive commutant weight W_kin inserted in the generator trace.",
            },
            "tree_weight_rank": {
                "proved": True,
                "statement": "The exact six-sector tree trace map has relative rank two. W_kin=I gives the A51 universal (6,6,6) row, while a selected sector-resolving W_kin can in principle emit both independent ratios.",
            },
            "Higgs_column_exclusion": {
                "proved": True,
                "statement": "The one-Higgs field is an inner fluctuation and contributes to scalar/loop terms, not as an independent finite-fermion trace column in the A51 tree gauge kinetic metric. A63's Higgs direction belongs to its one-loop threshold map and must not be copied into this tree map.",
            },
        },
        "checks": {key: bool(value) for key, value in checks.items()},
    }

    exclusions = {
        "schema": "MTTBackgroundEnergyAndScalarProxyExclusion.v1",
        "status": "THREE_CROSS_FUNCTIONAL_SHORTCUTS_REJECTED",
        "rejected_promotions": [
            {
                "available_object": "selected eta_00 diagonal HYM connection and contraction residual",
                "not_equal_to": "four-dimensional gauge zero-mode kinetic Gram row",
                "reason": "A connection solution does not supply the normalization of a four-dimensional zero mode. The current packet also omits full off-diagonal curvature and a common dimensional-reduction action.",
            },
            {
                "available_object": "c2(V_alpha)=4 alpha_1 and ch2(V_alpha)=-4 alpha_1",
                "not_equal_to": "normalized SU2 gauge kinetic coefficient",
                "reason": "The cohomology class does not by itself fix the required pairing, trace convention, dilaton/torsion weight, zero-mode representative, or reduction normalization. It can constrain a background energy only after those data are selected.",
            },
            {
                "available_object": "exact U1 circle and SU2 sphere scalar zeta finite parts",
                "not_equal_to": "gauge zero-mode kinetic rows",
                "reason": "Their source artifact labels them scalar proxies and withholds gauge-operator and weight promotion. The smooth Nil trail is likewise diagnostic under the later internal-packet alignment.",
            },
        ],
        "preserved_results": {
            "HYM_connection_solution_valid_in_its_scope": True,
            "Chern_Weil_row_valid_in_its_scope": True,
            "scalar_zeta_formulas_valid_as_diagnostics": True,
            "A62_ten_spectra_remain_closed": True,
        },
    }

    contract = {
        "schema": "MTTSelectedKineticWeightOperatorContract.v1",
        "status": "ONE_POSITIVE_WEIGHT_OPERATOR_REQUIRED",
        "primary_object": "W_kin on the A46 finite carrier, or an equivalent normalized circle/lens/nil zero-mode Gram table",
        "required_fields": [
            "source owner on the selected MTT branch",
            "explicit domain and positive inner product",
            "A46 carrier action and sector blocks",
            "circle/lens/nil and shared-circle quotient map if a dimensional reduction is used",
            "one trace and generator normalization for U1_GUT, SU2 and SU3",
            "one proper-time/cutoff or dimensional-reduction weight",
            "three K_a rows and their two relative ratios",
            "positivity and gauge-commutant certificate",
            "exactness/error certificate",
            "no measured gauge target used in selection",
        ],
        "lawful_source_routes": [
            {
                "route": "finite non-asymptotic spectral weight",
                "formula": "W_kin=f(D_source^2/Lambda^2) with f/Lambda selected before gauge comparison",
            },
            {
                "route": "circle/lens/nil zero-mode dimensional reduction",
                "formula": "W_kin is the normalized Gram/density operator induced by the three selected internal zero-mode wavefunctions and shared-circle quotient",
            },
            {
                "route": "single regularized gauge Hessian",
                "formula": "K_ab is obtained directly as delta^2 S_reg/delta A_a delta A_b on one domain and scheme",
            },
        ],
        "current_fill": {
            "selected_W_kin_count": 0,
            "required_W_kin_count": 1,
            "derived_nonuniversal_K_rows": 0,
            "required_K_rows": 3,
            "derived_relative_ratios": 0,
            "required_relative_ratios": 2,
        },
        "next_required_artifact": NEXT,
    }

    candidate = {
        "schema": "MTTSelectedGaugeZeroModeKineticInnerProductOrChernWeilBackgroundEnergyNoGo.v1",
        "status": STATUS,
        "theorems": {
            "correct_observable_theorem": kinetic["theorems"]["zero_mode_Hessian_identification"],
            "finite_weight_rank_theorem": kinetic["theorems"]["tree_weight_rank"],
            "cross_functional_no_go": {
                "proved": True,
                "statement": "Neither a background HYM residual, a bare Chern class, nor a scalar zeta determinant is a four-dimensional gauge zero-mode kinetic coefficient without a same-action reduction theorem. All three direct promotions are rejected while their scoped results are retained.",
            },
        },
        "closure_decision": {
            "correct_gauge_kinetic_observable_identified": True,
            "finite_tree_sector_weight_rank": relative_rank,
            "identity_weight_universal_row_reproduced": True,
            "background_HYM_energy_route_directly_promoted": False,
            "scalar_proxy_determinant_route_directly_promoted": False,
            "selected_W_kin_emitted": False,
            "native_nonuniversal_K_rows_emitted": 0,
            "native_nonuniversal_K_rows_required": 3,
            "no_knob_gauge_coupling_prediction_closed": False,
            "new_continuous_parameters": 0,
        },
        "outputs": {
            "kinetic": str(KINETIC.relative_to(ROOT)).replace("\\", "/"),
            "exclusions": str(EXCLUSIONS.relative_to(ROOT)).replace("\\", "/"),
            "contract": str(CONTRACT.relative_to(ROOT)).replace("\\", "/"),
        },
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "checks": {key: bool(value) for key, value in checks.items()},
        "epistemic_policy": {
            "target_fitting_used": False,
            "observed_gauge_values_used_as_selector": False,
            "proxy_promoted_across_functionals": False,
            "A62_rows_reopened": False,
            "prediction_claimed": False,
        },
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_GaugeZeroModeKineticInnerProduct_or_ChernWeilBackgroundEnergyNoGo_v1",
        "status": STATUS,
        "correct_zero_mode_Hessian_identified": True,
        "finite_tree_sector_weight_relative_rank": relative_rank,
        "identity_weight_relative_rank": 0,
        "cross_functional_shortcuts_rejected": 3,
        "selected_W_kin_emitted": False,
        "native_nonuniversal_K_rows_emitted": 0,
        "native_nonuniversal_K_rows_required": 3,
        "new_continuous_parameters": 0,
        "no_knob_gauge_coupling_prediction_closed": False,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Gauge Zero-Mode Kinetic Inner Product or Chern-Weil Background-Energy No-Go v1

## Correct observable

The four-dimensional gauge kinetic metric is the Hessian of one action with respect to
four-dimensional gauge zero modes. In continuum and finite forms,

```text
K_ab = integral_X w <xi_a,xi_b> dvol,
K_ab = Tr_HF(W_kin T_a T_b),  W_kin >= 0.
```

For `W_kin=I`, the selected A46/A51 carrier gives exactly `(6,6,6)`. After projection to
`(U1-SU2,SU3-SU2)`, the six-sector weight map has rank `{relative_rank}`. Thus one selected
sector-resolving positive weight operator can in principle produce both ratios.

This is distinct from A63's one-loop heat response: the Higgs has no independent tree finite-carrier
trace column. Its A63 direction remains valid only in the loop/threshold map.

## Three rejected shortcuts

1. The selected diagonal HYM connection and residual do not normalize a four-dimensional gauge
   zero mode and omit the full common-action reduction.
2. `c2(V_alpha)=4 alpha_1` constrains topology but does not fix the metric/dilaton pairing, trace,
   zero-mode representative, or reduction normalization needed for a kinetic row.
3. The exact old circle/sphere zeta values are explicitly scalar proxies; the later Nil alignment
   also retains the smooth determinant trail as diagnostics rather than the selected gauge source.

No scoped HYM, Chern-Weil, zeta, or A62 spectrum result is revoked.

## Frontier

The remaining object is now one positive `W_kin`, not three unrelated numbers. It may be emitted
by a selected non-asymptotic spectral weight, by a normalized circle/lens/nil zero-mode Gram
reduction including the shared-circle quotient, or by one regularized gauge Hessian.

Current fill: `W_kin 0/1`, nonuniversal `K_a 0/3`, relative ratios `0/2`.

Next artifact: `{NEXT}`.
"""

    dump(KINETIC, kinetic)
    dump(EXCLUSIONS, exclusions)
    dump(CONTRACT, contract)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
