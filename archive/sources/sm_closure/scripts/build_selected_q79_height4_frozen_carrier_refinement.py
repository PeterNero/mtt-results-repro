from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
PERIODS = PERIOD_DIRECTORY / "selected_alignment_full_integral_basis_period_table.packet.json"
CONVERGENCE = PERIOD_DIRECTORY / "selected_alignment_full_integral_basis_convergence.packet.json"
INTEGRAL_BASIS = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmentintegralh2presentation"
    / "selected_alignment_exact_integral_H2_basis.packet.json"
)
A132 = PERIOD_DIRECTORY / "selected_alignment_effective_branch_quotient_and_height4_seed.packet.json"
REFINED_BETA = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_selected_side_beta.local_lower.order40_step003.interval.packet.json"
)
PACKET = PERIOD_DIRECTORY / "selected_alignment_height4_frozen_carrier_refinement_and_interval_cutset.packet.json"
FRONTIER = PERIOD_DIRECTORY / "U6_frontier_after_A133.packet.json"
SLUG = "selected_q79heightfourfrozencarrierrefinementandintervalcutset"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79HeightFourFrozenCarrierRefinementAndIntervalCutset_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def main() -> int:
    periods = load(PERIODS)
    convergence = load(CONVERGENCE)
    basis = load(INTEGRAL_BASIS)
    a132 = load(A132)
    refined_beta = load(REFINED_BETA)

    matrix = np.asarray(
        [
            [complex_value(value) for value in row]
            for row in periods["period_matrix_rows"]
        ],
        dtype=np.complex128,
    )
    form_names = list(periods["form_names"])
    if matrix.shape != (8, 92) or len(form_names) != 8:
        raise AssertionError("A131 period table shape changed")
    if np.any(matrix[:, 90:] != 0.0):
        raise AssertionError("A131 exact Leray-null block changed")

    seed = a132["height_four_continuation_seed"]
    ell = np.asarray(seed["ell_Z92"], dtype=np.int64)
    if ell.shape != (92,) or np.any(ell[90:] != 0):
        raise AssertionError("A132 canonical height-four representative changed")
    if int(np.max(np.abs(ell))) != 4:
        raise AssertionError("A132 height-four seed changed")

    beta_center = np.asarray(
        [complex_value(value) for value in refined_beta["endpoint"]["beta_center"]],
        dtype=np.complex128,
    )
    beta_radius = float(refined_beta["endpoint"]["uniform_component_radius_upper"])
    old_beta_radius = float(
        a132["fixed_height_search"]["beta_uniform_component_radius_upper"]
    )
    if beta_center.shape != (8,) or not beta_radius < old_beta_radius:
        raise AssertionError("refined beta enclosure did not improve A132")
    if int(refined_beta["method"]["order"]) != 40:
        raise AssertionError("refined beta Taylor order changed")
    if int(refined_beta["execution"]["accepted_step_count"]) != 421:
        raise AssertionError("refined beta accepted-step count changed")

    residual = beta_center - matrix @ ell
    residual_absolute = np.abs(residual)
    old_residual = np.asarray(
        [complex_value(value) for value in seed["floating_residual"]],
        dtype=np.complex128,
    )
    center_shift = float(np.max(np.abs(residual - old_residual)))

    entrywise_primary = np.asarray(
        convergence["primary_entrywise_absolute_difference_envelope_rows"],
        dtype=np.float64,
    )
    if entrywise_primary.shape != (8, 90):
        raise AssertionError("A131 primary convergence envelope shape changed")
    period_proxy_radius = entrywise_primary @ np.abs(ell[:90]).astype(np.float64)
    proxy_total_radius = beta_radius + period_proxy_radius
    proxy_separation_lower = np.maximum(0.0, residual_absolute - proxy_total_radius)
    separating_index = int(np.argmax(proxy_separation_lower))
    admissible_period_radius = float(
        residual_absolute[separating_index] - beta_radius
    )
    if admissible_period_radius <= 0:
        raise AssertionError("refined beta does not expose a separating component")
    if proxy_separation_lower[separating_index] <= 0:
        raise AssertionError("A131 convergence proxy no longer separates the seed")

    primary_basis = np.asarray(
        basis["primary_basis"]["basis_columns"], dtype=object
    )
    if primary_basis.shape != (98, 90):
        raise AssertionError("A130 primary basis shape changed")
    primitive = primary_basis @ np.asarray(ell[:90], dtype=object)
    primitive = np.asarray([int(value) for value in primitive], dtype=np.int64)
    thimble_chain = primitive[:90]
    handle_chain = primitive[90:]
    thimble_manifest = [
        {
            "distinguished_index": index + 1,
            "coefficient": int(coefficient),
        }
        for index, coefficient in enumerate(thimble_chain)
        if coefficient
    ]
    if len(thimble_manifest) != seed["primitive_chain_coordinates"]["thimble_support_size"]:
        raise AssertionError("A132 primitive thimble support changed")
    if handle_chain.tolist() != seed["primitive_chain_coordinates"]["handle_coordinates"]:
        raise AssertionError("A132 primitive handle coordinates changed")

    row_ledger = []
    for index, name in enumerate(form_names):
        row_ledger.append(
            {
                "row_index": index,
                "form": name,
                "residual_center": complex_pair(residual[index]),
                "residual_center_absolute_value": float(residual_absolute[index]),
                "rigorous_beta_component_radius": beta_radius,
                "A131_two_run_period_combination_proxy_radius": float(
                    period_proxy_radius[index]
                ),
                "conditional_total_radius": float(proxy_total_radius[index]),
                "conditional_separation_lower": float(proxy_separation_lower[index]),
            }
        )

    target = {
        "row_index": separating_index,
        "form": form_names[separating_index],
        "selected_period_combination": (
            f"sum_I m_I Pi_{form_names[separating_index]},I"
        ),
        "residual_center": complex_pair(residual[separating_index]),
        "residual_center_absolute_value": float(
            residual_absolute[separating_index]
        ),
        "rigorous_beta_radius": beta_radius,
        "strict_required_period_combination_radius_upper": admissible_period_radius,
        "A131_two_run_proxy_radius": float(period_proxy_radius[separating_index]),
        "proxy_to_strict_budget_ratio": float(
            admissible_period_radius
            / max(period_proxy_radius[separating_index], np.finfo(float).tiny)
        ),
        "certificate_logic": (
            "If a rigorous complex-ball enclosure of this single selected "
            "period combination has radius strictly below the displayed bound "
            "and contains the A131 center, then the frozen A132 carrier is "
            "separated from F(A,m)=0 in this row."
        ),
    }

    authority_paths = [
        PERIODS,
        CONVERGENCE,
        INTEGRAL_BASIS,
        A132,
        REFINED_BETA,
        Path(__file__),
    ]
    packet = {
        "schema": "MTTQ79HeightFourFrozenCarrierRefinementAndIntervalCutset.v1",
        "status": "RIGOROUS_BETA_REFINED_FROZEN_HEIGHT4_PROXY_SEPARATED_ONE_PERIOD_INTERVAL_OPEN",
        "authority": [
            {"path": relative(path), "sha256": sha256(path)}
            for path in authority_paths
        ],
        "refined_beta": {
            "old_uniform_component_radius": old_beta_radius,
            "new_uniform_component_radius": beta_radius,
            "radius_improvement_factor": old_beta_radius / beta_radius,
            "maximum_residual_center_shift_from_A132": center_shift,
            "Taylor_order": int(refined_beta["method"]["order"]),
            "accepted_steps": int(
                refined_beta["execution"]["accepted_step_count"]
            ),
            "rejected_steps": int(
                refined_beta["execution"]["rejected_step_count"]
            ),
            "minimum_accepted_step": refined_beta["execution"][
                "minimum_accepted_step"
            ],
            "rigorous_interval_enclosure": True,
        },
        "height_four_seed": {
            "effective_coordinates_Z90": ell[:90].tolist(),
            "coefficient_height": int(np.max(np.abs(ell))),
            "coefficient_l1_norm": int(np.sum(np.abs(ell))),
            "primitive_thimble_chain": thimble_manifest,
            "primitive_thimble_support": len(thimble_manifest),
            "primitive_thimble_l1_norm": int(np.sum(np.abs(thimble_chain))),
            "primitive_handle_coordinates": handle_chain.tolist(),
            "primitive_order": (
                "90 canonically oriented thimbles, then "
                "A:a1,A:b1,A:a2,A:b2,B:a1,B:b1,B:a2,B:b2"
            ),
        },
        "component_ledger": row_ledger,
        "minimal_strict_interval_target": target,
        "scope": {
            "observed_SM_values_used": False,
            "beta_interval_refinement_closed": True,
            "all_720_period_intervals_required_for_frozen_separation": False,
            "one_selected_complex_period_combination_suffices": True,
            "A131_two_run_proxy_is_an_interval_certificate": False,
            "fixed_carrier_proxy_separation_observed": True,
            "fixed_carrier_exact_separation_proved": False,
            "height_four_branch_globally_rejected": False,
            "covariant_alignment_zero_solved": False,
            "small_residual_promoted_to_equality": False,
        },
        "next_required_artifact": "MTT_Selected_q79HeightFourE32CombinedPeriodIntervalAndCovariantContinuation_v1",
    }
    dump(PACKET, packet)

    frontier = {
        "schema": "MTTU6FrontierAfterA133.v1",
        "status": "U6_HEIGHT4_BETA_INTERVAL_REFINED_ONE_COMBINED_PERIOD_INTERVAL_AND_COVARIANT_ZERO_OPEN",
        "closed": [
            "A131 selected-carrier floating 8x92 period matrix",
            "A132 exact effective Z90 quotient and height-four seed",
            "A133 order-40 step-0.003 rigorous beta enclosure",
            "A133 reduction of frozen-carrier separation to one complex E32 period-combination interval",
        ],
        "active_target": (
            "certify the selected E32 combined period radius below "
            f"{admissible_period_radius:.17g}, then execute the full covariant "
            "F(A,m), J(A,m) continuation"
        ),
        "not_closed": [
            "rigorous interval enclosure of the selected E32 period combination",
            "exact frozen-carrier separation or membership",
            "covariant PGL3 zero and nonzero Jacobian",
        ],
    }
    dump(FRONTIER, frontier)

    candidate = {
        "schema": "MTTSelectedQ79HeightFourFrozenCarrierRefinementAndIntervalCutset.v1",
        "status": packet["status"],
        "artifact": "A133",
        "packet": relative(PACKET),
        "packet_sha256": sha256(PACKET),
        "frontier": relative(FRONTIER),
        "frontier_sha256": sha256(FRONTIER),
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "what_closes": {
            "rigorous_beta_radius_refined": True,
            "minimal_one_row_period_interval_cutset": True,
            "full_primitive_chain_manifest_emitted": True,
        },
        "what_remains_open": {
            "selected_E32_combined_period_interval": True,
            "exact_frozen_carrier_decision": True,
            "covariant_PGL3_zero_and_Jacobian": True,
        },
        "next_required_artifact": packet["next_required_artifact"],
    }

    note = f"""# MTT Selected q79 Height-Four Frozen-Carrier Refinement and Interval Cutset v1

## Result

A133 reruns the A127 validated selected-side beta transport at Taylor order 40
with maximum step `0.003`. The endpoint center agrees with A132 to
`{center_shift:.3e}`, while the rigorous uniform component radius improves from

```text
{old_beta_radius:.17g}  to  {beta_radius:.17g}.
```

This is a factor `{old_beta_radius / beta_radius:.6f}` refinement. The beta
enclosure is no longer what prevents a frozen-carrier decision for the A132
height-four seed.

## Honest fixed-carrier decision

At the refined center the largest residual occurs in row
`{form_names[separating_index]}`:

```text
F_{form_names[separating_index]} center = {residual[separating_index].real:.17g}
                                      {residual[separating_index].imag:+.17g} i,
|F_{form_names[separating_index]} center| = {residual_absolute[separating_index]:.17g}.
```

The A131 two-run period envelope would give a positive separation lower bound
`{proxy_separation_lower[separating_index]:.17g}`. That is strong numerical
evidence, but it is not promoted to a theorem because the A131 envelope is not
an interval enclosure.

The exact remaining frozen-carrier object is only one complex number:

```text
sum_I m_I Pi_{form_names[separating_index]},I.
```

A rigorous enclosure of that selected combination with radius strictly below

```text
{admissible_period_radius:.17g}
```

proves separation in the `{form_names[separating_index]}` row. Therefore all
720 individual period intervals are unnecessary for this decision. The full
primitive chain is emitted as `{len(thimble_manifest)}` nonzero thimbles with
handle coordinates `{handle_chain.tolist()}` so the next computation has no
hidden lattice reconstruction.

## Covariant scope

Frozen-carrier separation would not reject the height-four branch globally.
It would prove that the alignment must move. The branch must then be tested by

```text
F(A,m)=beta(A)-Pi_primary(A)m,
J_rs=nabla_s beta_r-sum_I m_I nabla_s Pi_rI.
```

Both derivative terms remain mandatory. A133 closes the refined beta and the
minimal interval cutset; it does not claim exact membership, exact separation,
or a covariant PGL3 zero.

No observed Standard Model value is used.
"""
    NOTE.write_text(note, encoding="utf-8")
    candidate["note"] = relative(NOTE)
    candidate["note_sha256"] = sha256(NOTE)
    dump(CANDIDATE, candidate)

    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79HeightFourFrozenCarrierRefinementAndIntervalCutset",
        "candidate_path": relative(CANDIDATE),
        "candidate_sha256": sha256(CANDIDATE),
        "status": candidate["status"],
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }
    dump(CERTIFICATE, certificate)
    print(f"wrote {relative(PACKET)}")
    print(f"wrote {relative(FRONTIER)}")
    print(f"wrote {relative(CANDIDATE)}")
    print(f"wrote {relative(CERTIFICATE)}")
    print(f"wrote {relative(NOTE)}")
    print(
        json.dumps(
            {
                "beta_radius": beta_radius,
                "radius_improvement_factor": old_beta_radius / beta_radius,
                "separating_form": form_names[separating_index],
                "residual_absolute": float(residual_absolute[separating_index]),
                "strict_period_radius_budget": admissible_period_radius,
                "conditional_separation_lower": float(
                    proxy_separation_lower[separating_index]
                ),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
