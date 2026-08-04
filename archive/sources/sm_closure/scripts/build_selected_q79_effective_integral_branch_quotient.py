from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

from explore_q79_a126_integral_period_branch_lll import (
    candidate_record,
    kannan_candidates,
    realification,
)


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
PERIODS = PERIOD_DIRECTORY / "selected_alignment_full_integral_basis_period_table.packet.json"
CONVERGENCE = PERIOD_DIRECTORY / "selected_alignment_full_integral_basis_convergence.packet.json"
BETA = DIRECTORY / "tight_selected_side_endpoint_beta.theorem.packet.json"
INTEGRAL_BASIS = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmentintegralh2presentation"
    / "selected_alignment_exact_integral_H2_basis.packet.json"
)
PACKET = PERIOD_DIRECTORY / "selected_alignment_effective_branch_quotient_and_height4_seed.packet.json"
FRONTIER = PERIOD_DIRECTORY / "U6_frontier_after_A132.packet.json"
CANDIDATE = ROOT / "candidate_data" / "selected_q79effectiveintegralbranchquotientandheightfourseed.candidate.json"
CERTIFICATE = ROOT / "certificates" / "selected_q79effectiveintegralbranchquotientandheightfourseed.certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79EffectiveIntegralBranchQuotientAndHeightFourSeed_v1.md"

SEARCH_SCALE = 1_000_000
SEARCH_WEIGHTS = list(range(900, 1601, 10))
MARKER_MULTIPLIERS = [1, 2, 3, 5, 8]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def concise(record: dict | None) -> dict | None:
    if record is None:
        return None
    return {
        key: record[key]
        for key in (
            "coefficient_height",
            "coefficient_l1_norm",
            "support_size",
            "residual_maximum_absolute_value",
            "residual_l2_norm",
            "embedding_scale",
            "coefficient_weight",
            "marker_weight",
        )
    }


def main() -> int:
    period_packet = load(PERIODS)
    convergence_packet = load(CONVERGENCE)
    beta_packet = load(BETA)
    basis_packet = load(INTEGRAL_BASIS)
    if basis_packet["surface_H2_rank"] != 92:
        raise AssertionError("A130 H2 rank changed")
    if basis_packet["Leray_edge_basis"] != ["F", "Gamma_0"]:
        raise AssertionError("A130 Leray pair changed")
    if not basis_packet["exact_checks"]["edge_rank_2_primitive"]:
        raise AssertionError("A130 Leray pair is not primitive")

    period_matrix = np.asarray(
        [
            [complex_value(value) for value in row]
            for row in period_packet["period_matrix_rows"]
        ],
        dtype=np.complex128,
    )
    beta = np.asarray(
        [
            complex_value(value)
            for value in beta_packet["tight_endpoint"]["beta_center"]
        ],
        dtype=np.complex128,
    )
    beta_radius = float(
        beta_packet["tight_endpoint"]["uniform_component_radius_upper"]
    )
    if period_matrix.shape != (8, 92) or beta.shape != (8,):
        raise AssertionError("selected period/beta dimensions changed")
    if np.any(period_matrix[:, 90:] != 0.0):
        raise AssertionError("A131 Leray block is not exactly zero")
    active_matrix = period_matrix[:, :90]
    real_matrix = np.vstack([active_matrix.real, active_matrix.imag])
    real_beta = realification(beta)

    entrywise_primary = np.asarray(
        [
            [float(value) for value in row]
            for row in convergence_packet[
                "primary_entrywise_absolute_difference_envelope_rows"
            ]
        ],
        dtype=np.float64,
    )
    entrywise_error = np.hstack(
        [entrywise_primary, np.zeros((8, 2), dtype=np.float64)]
    )
    primary_basis = np.asarray(
        basis_packet["primary_basis"]["basis_columns"], dtype=object
    )

    records: list[dict] = []
    seen: set[tuple[int, ...]] = set()
    active_indices = np.arange(90, dtype=np.int64)
    for coefficient_weight in SEARCH_WEIGHTS:
        for marker_multiplier in MARKER_MULTIPLIERS:
            marker_weight = coefficient_weight * marker_multiplier
            for method, ell_active in kannan_candidates(
                real_matrix,
                real_beta,
                scale=SEARCH_SCALE,
                coefficient_weight=coefficient_weight,
                marker_weight=marker_weight,
            ):
                key = tuple(int(value) for value in ell_active)
                if key in seen:
                    continue
                seen.add(key)
                records.append(
                    candidate_record(
                        ell_active=ell_active,
                        active_indices=active_indices,
                        period_matrix=period_matrix,
                        beta=beta,
                        entrywise_error=entrywise_error,
                        primary_basis=primary_basis,
                        beta_radius=beta_radius,
                        method=method,
                        scale=SEARCH_SCALE,
                        coefficient_weight=coefficient_weight,
                        marker_weight=marker_weight,
                    )
                )
    if not records:
        raise AssertionError("fixed Kannan search emitted no candidates")

    by_height: dict[str, dict | None] = {}
    for height in range(0, 9):
        eligible = [
            record for record in records if record["coefficient_height"] <= height
        ]
        best = (
            None
            if not eligible
            else min(
                eligible,
                key=lambda row: (
                    row["residual_maximum_absolute_value"],
                    row["residual_l2_norm"],
                    row["coefficient_l1_norm"],
                ),
            )
        )
        by_height[str(height)] = concise(best)

    center_nonseparated = [
        record
        for record in records
        if record["residual_maximum_absolute_value"] < beta_radius
    ]
    if not center_nonseparated:
        raise AssertionError("fixed search found no beta-enclosure seed")
    minimum_height = min(
        record["coefficient_height"] for record in center_nonseparated
    )
    selected = min(
        (
            record
            for record in center_nonseparated
            if record["coefficient_height"] == minimum_height
        ),
        key=lambda row: (
            row["residual_maximum_absolute_value"],
            row["residual_l2_norm"],
            row["coefficient_l1_norm"],
        ),
    )
    if minimum_height != 4:
        raise AssertionError("fixed search height frontier changed")
    if selected["ell_Z92"][-2:] != [0, 0]:
        raise AssertionError("canonical quotient representative changed")

    packet = {
        "schema": "MTTQ79SelectedAlignmentEffectiveIntegralBranchQuotientAndHeightFourSeed.v1",
        "status": "EXACT_LERAY_NULL_QUOTIENT_CLOSED_HEIGHT4_CONTINUATION_SEED_COMPUTED",
        "authority": {
            "period_table": relative(PERIODS),
            "period_table_sha256": sha256(PERIODS),
            "period_convergence": relative(CONVERGENCE),
            "period_convergence_sha256": sha256(CONVERGENCE),
            "beta_packet": relative(BETA),
            "beta_packet_sha256": sha256(BETA),
            "integral_basis": relative(INTEGRAL_BASIS),
            "integral_basis_sha256": sha256(INTEGRAL_BASIS),
            "builder_source": relative(Path(__file__)),
            "builder_source_sha256": sha256(Path(__file__)),
        },
        "exact_effective_branch_quotient": {
            "integral_domain": "H2(C_A,Z) congruent Z^92 in the A130 basis",
            "known_primitive_null_sublattice": "K_L=<Leray_F,Leray_Gamma0> congruent Z^2",
            "null_period_entries": 16,
            "factorization": "Pi:Z^92 -> C^8 factors through Z^92/K_L congruent Z^90",
            "canonical_representative": "ell=(m_1,...,m_90,0,0)",
            "branch_equation": "F(A,m)=beta(A)-Pi_primary(A)m",
            "additional_exact_kernel_excluded": False,
            "theorem": "The two Leray coefficients are unidentifiable by the eight trace-free residue periods and may be set to zero without loss. This proves a rank-90 effective search quotient; it does not prove that K_L is the full exact kernel.",
        },
        "fixed_height_search": {
            "method": "FLINT LLL Kannan embeddings",
            "embedding_scale": SEARCH_SCALE,
            "coefficient_weights": SEARCH_WEIGHTS,
            "marker_multipliers": MARKER_MULTIPLIERS,
            "unique_candidates": len(records),
            "beta_uniform_component_radius_upper": beta_radius,
            "center_nonseparated_candidates": len(center_nonseparated),
            "best_candidate_by_maximum_height": by_height,
            "minimum_center_nonseparated_height_in_fixed_search": minimum_height,
            "fixed_search_is_not_an_exhaustive_height_theorem": True,
        },
        "height_four_continuation_seed": selected,
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_selected_carrier": True,
            "exact_branch_domain_reduced_from_92_to_90": True,
            "height_four_seed_is_a_discrete_lattice_vector_not_four_parameters": True,
            "beta_enclosure_is_rigorous": True,
            "period_two_run_envelopes_are_not_interval_bounds": True,
            "center_nonseparation_is_not_exact_membership": True,
            "exact_Z90_membership_proved": False,
            "exact_Z90_nonmembership_proved": False,
            "PGL3_covariant_zero_solved": False,
            "small_residual_accepted_as_proof": False,
        },
    }
    write_json(PACKET, packet)

    frontier = {
        "schema": "MTTU6FrontierAfterA132.v1",
        "status": "U6_SELECTED_PERIOD_MATRIX_CLOSED_EFFECTIVE_Z90_BRANCH_QUOTIENT_CLOSED_EXACT_BRANCH_OPEN",
        "closed": [
            "A131 selected-carrier floating 8x92 period matrix",
            "A132 exact factorization through the primitive rank-2 Leray-null quotient",
            "canonical effective branch coordinates m in Z^90",
            "deterministic height-4 same-carrier continuation seed",
        ],
        "active_target": "certify the covariant F(A,m)=0 solve for the A132 discrete seed, or prove branch separation",
        "not_closed": [
            "interval enclosures for the nonzero period entries",
            "exact integral-lattice membership",
            "selected PGL3 alignment and nonzero covariant Jacobian",
        ],
    }
    write_json(FRONTIER, frontier)

    candidate = {
        "schema": "MTTSelectedQ79EffectiveIntegralBranchQuotientAndHeightFourSeed.v1",
        "status": "SELECTED_Q79_EFFECTIVE_Z90_BRANCH_QUOTIENT_CLOSED_HEIGHT4_SEED_COMPUTED_EXACT_BRANCH_OPEN",
        "artifact": "A132",
        "packet": relative(PACKET),
        "packet_sha256": sha256(PACKET),
        "frontier": relative(FRONTIER),
        "frontier_sha256": sha256(FRONTIER),
        "what_closes": {
            "primitive_Leray_null_quotient": True,
            "canonical_effective_Z90_branch_domain": True,
            "fixed_search_height4_continuation_seed": True,
        },
        "what_remains_open": {
            "interval_nonzero_periods": True,
            "exact_Z90_membership": True,
            "covariant_PGL3_zero_and_Jacobian": True,
        },
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "next_required_artifact": "MTT_Selected_q79CovariantHeightFourBranchContinuationAndIntervalDecision_v1",
    }
    note = f"""# MTT Selected q79 Effective Integral Branch Quotient and Height-Four Seed v1

## Scope

This is successor **A132** to A131. It does not reconstruct the selected
period matrix; A131 is consumed as closed authority. A132 removes the exact
Leray-null redundancy from the integral branch and emits one deterministic
same-carrier continuation seed.

## Exact effective branch quotient

A130 gives the primitive integral decomposition

```text
H2(C_A,Z) = <primary_1,...,primary_90,Leray_F,Leray_Gamma0>.
```

A131 proves all `8x2=16` periods of the final Leray pair vanish exactly for
the eight trace-free residue forms. Hence

```text
Pi(m,u,v)=Pi_primary*m
```

for every `(m,u,v) in Z^90 x Z^2`. The branch equation therefore factors
exactly through

```text
Z^92/<Leray_F,Leray_Gamma0> = Z^90,
F(A,m)=beta(A)-Pi_primary(A)m.
```

The canonical representative is `(m,0,0)`. This proves that the two Leray
coefficients cannot be selected by these period equations and are not branch
parameters. It does not assert that the displayed pair is the entire exact
kernel of `Pi`.

## Fixed discrete search

The fixed Kannan grid uses scale `{SEARCH_SCALE}`, coefficient weights
`900,910,...,1600`, and marker multipliers `{MARKER_MULTIPLIERS}`. It emits
`{len(records)}` distinct target-coefficient-one vectors. The smallest
coefficient height entering the current beta-center component balls in this
fixed search is `{minimum_height}`. The selected continuation seed has:

```text
height                 = {selected['coefficient_height']}
support                = {selected['support_size']}
l1 norm                = {selected['coefficient_l1_norm']}
max center residual    = {selected['residual_maximum_absolute_value']:.17g}
beta component radius  = {beta_radius:.17g}
primitive support      = {selected['primitive_chain_coordinates']['thimble_support_size']}
primitive handle row   = {selected['primitive_chain_coordinates']['handle_coordinates']}
```

The height is a bound on integer cycle multiplicities, not a count of fitted
parameters. The height-three result is outside the current beta enclosure in
this fixed search. This is not a global height-minimality theorem because the
Kannan grid is not exhaustive over `Z^90`.

## What the numerical overlap means

The beta enclosure is rigorous, but A131's nonzero period entries currently
have independent two-run convergence envelopes rather than interval bounds.
Therefore the height-four center residual is a lawful continuation seed and a
nonseparation diagnostic, not a proof of exact lattice membership. A small
residual is not promoted to equality.

## Next theorem

Hold the integer vector fixed and execute the same-source covariant system

```text
F(A,m)=beta(A)-Pi_primary(A)m,
J_rs=nabla_s beta_r-sum_I m_I nabla_s Pi_rI.
```

An interval Newton/Krawczyk zero with `det J != 0` would select an isolated
alignment on this branch. A separation certificate would reject it. Either
outcome advances the exact branch decision.

No observed Standard Model value is used.
"""
    NOTE.write_text(note, encoding="utf-8")
    candidate["note"] = relative(NOTE)
    candidate["note_sha256"] = sha256(NOTE)
    write_json(CANDIDATE, candidate)
    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79EffectiveIntegralBranchQuotientAndHeightFourSeed",
        "candidate_path": relative(CANDIDATE),
        "candidate_sha256": sha256(CANDIDATE),
        "status": candidate["status"],
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }
    write_json(CERTIFICATE, certificate)
    print(f"wrote {relative(PACKET)}")
    print(f"wrote {relative(CANDIDATE)}")
    print(f"wrote {relative(CERTIFICATE)}")
    print(f"wrote {relative(NOTE)}")
    print(
        json.dumps(
            {
                "unique_candidates": len(records),
                "minimum_fixed_search_height": minimum_height,
                "selected_residual_maximum": selected[
                    "residual_maximum_absolute_value"
                ],
                "beta_radius": beta_radius,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
