from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
A134 = PERIOD_DIRECTORY / "selected_alignment_height4_E32_handle_interval_and_thimble_cutset.packet.json"
MONODROMY = DIRECTORY / "selected_alignment_interval_braid_and_global_relation.packet.json"
PACKET = PERIOD_DIRECTORY / "selected_alignment_height4_E32_thimble_regular_singular_reduction.packet.json"
FRONTIER = PERIOD_DIRECTORY / "U6_frontier_after_A135.packet.json"
SLUG = "selected_q79e32thimbleregularsingularreduction"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79E32ThimbleRegularSingularReduction_v1.md"


J = np.asarray(
    [
        [0, 1, 0, 0],
        [-1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, -1, 0],
    ],
    dtype=object,
)
I4 = np.eye(4, dtype=object)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def exact_rank_one(matrix: np.ndarray) -> bool:
    if not np.any(matrix != 0):
        return False
    for row_a in range(4):
        for row_b in range(row_a + 1, 4):
            for col_a in range(4):
                for col_b in range(col_a + 1, 4):
                    determinant = (
                        matrix[row_a, col_a] * matrix[row_b, col_b]
                        - matrix[row_a, col_b] * matrix[row_b, col_a]
                    )
                    if determinant != 0:
                        return False
    return True


def primitive_image_generator(matrix: np.ndarray) -> list[int]:
    for column in range(4):
        values = [int(matrix[row, column]) for row in range(4)]
        if not any(values):
            continue
        divisor = 0
        for value in values:
            divisor = math.gcd(divisor, abs(value))
        values = [value // divisor for value in values]
        first = next(value for value in values if value)
        if first < 0:
            values = [-value for value in values]
        return values
    raise AssertionError("rank-one matrix has no image generator")


def main() -> int:
    a134 = load(A134)
    monodromy = load(MONODROMY)
    manifest = a134["selected_E32_decomposition"]["primitive_thimble_chain"]
    selected_indices = [int(row["distinguished_index"]) for row in manifest]
    coefficients = {
        int(row["distinguished_index"]): int(row["coefficient"])
        for row in manifest
    }
    if len(selected_indices) != 71 or len(set(selected_indices)) != 71:
        raise AssertionError("A134 selected thimble support changed")

    source_rows = {
        int(row["distinguished_index"]): row
        for row in monodromy["rows"]
        if int(row["distinguished_index"]) <= 90
    }
    if len(source_rows) != 90:
        raise AssertionError("selected local monodromy inventory changed")

    rows = []
    directions = set()
    for index in selected_indices:
        source = source_rows[index]
        matrix = np.asarray(source["integral_symplectic_matrix"], dtype=object)
        nilpotent = matrix - I4
        if matrix.shape != (4, 4):
            raise AssertionError(f"d{index:03d} monodromy shape changed")
        if not exact_rank_one(nilpotent):
            raise AssertionError(f"d{index:03d} local logarithm is not rank one")
        if np.any(nilpotent @ nilpotent != 0):
            raise AssertionError(f"d{index:03d} local logarithm is not square zero")
        if np.any(matrix.T @ J @ matrix != J):
            raise AssertionError(f"d{index:03d} local monodromy is not symplectic")
        vector = primitive_image_generator(nilpotent)
        vector_array = np.asarray(vector, dtype=object)
        if np.any(nilpotent @ vector_array != 0):
            raise AssertionError(f"d{index:03d} vanishing direction is not fixed")
        if np.any(matrix @ vector_array != vector_array):
            raise AssertionError(f"d{index:03d} vanishing direction is not invariant")
        directions.add(tuple(vector))
        rows.append(
            {
                "distinguished_index": index,
                "root_id": source["root_id"],
                "height_four_chain_coefficient": coefficients[index],
                "integral_local_monodromy_T": matrix.astype(int).tolist(),
                "integer_logarithm_numerator_N_equals_T_minus_I": nilpotent.astype(int).tolist(),
                "primitive_vanishing_image_generator": vector,
                "exact_rank_N": 1,
                "N_squared_zero": True,
                "T_symplectic": True,
                "N_v_zero": True,
                "T_v_equals_v": True,
            }
        )

    packet = {
        "schema": "MTTQ79SelectedE32ThimbleRegularSingularReduction.v1",
        "status": "ALL_SELECTED_E32_THIMBLE_POLES_REDUCED_TO_LOG_FREE_FROBENIUS_BRANCH",
        "authority": [
            {"path": relative(path), "sha256": sha256(path)}
            for path in (A134, MONODROMY, Path(__file__))
        ],
        "exact_selected_inventory": {
            "selected_thimble_count": len(rows),
            "selected_coefficient_l1_norm": sum(abs(coefficients[index]) for index in selected_indices),
            "distinct_primitive_image_directions_with_canonical_sign": len(directions),
            "rows": rows,
        },
        "local_theorem": {
            "coordinate": "x=0 at the simple nodal critical value",
            "regular_singular_system": "x*dY/dx=B(x)Y, B(x)=R+sum_{k>=1} B_k x^k",
            "monodromy_relation": "on compact H1, exp(2*pi*i*R)=T or T^(-1), according to local loop orientation; the finite-node degeneration fixes the affine puncture summand",
            "integer_logarithm": "log(T)=T-I=N because N^2=0",
            "residue_nilpotence": "on the compact block R is conjugate to +(N/(2*pi*i)) or -(N/(2*pi*i)); extension by zero on the fixed puncture summand preserves R^2=0 in the five-period affine frame",
            "vanishing_branch": "the primitive vanishing direction v lies in image(N), hence N v=0 and the selected vanishing-cycle period is the monodromy-invariant, log-free local branch",
            "frobenius_recurrence": "choose Y_0 in ker(R); for n>=1, Y_n=(nI-R)^(-1)*sum_{k=1}^n B_k Y_(n-k)",
            "closed_form_inverse": "(nI-R)^(-1)=n^(-1)*(I+R/n), since R^2=0",
            "E32_tail": "if q_E32(x)=sum q_k x^k is the analytic residue row, then the endpoint tail integral is obtained coefficientwise from q_E32(x)Y(x), dividing its x^n coefficient by n+1",
            "proved_for_all_selected_thimbles": True,
        },
        "computational_consequence": {
            "raw_connection_norm_Gronwall_is_admissible": False,
            "reason": "the fixed-frame connection contains a nilpotent 1/x pole although the selected vanishing solution is regular",
            "selected_method": "certified local Frobenius seed in ker(R), followed by ordinary-point ball continuation and exact tail-series integration",
            "required_local_data": [
                "analytic coefficients B_k after the nilpotent singular factor is removed",
                "the log-free initial vector Y_0 from the nodal quadratic factor",
                "analytic E32 row coefficients q_k",
                "a majorant-series tail bound",
            ],
        },
        "scope": {
            "observed_SM_values_used": False,
            "exact_local_monodromy_used": True,
            "regular_singular_nilpotent_reduction_closed": True,
            "log_free_vanishing_branch_selected_topologically": True,
            "local_Frobenius_coefficients_numerically_emitted": False,
            "weighted_71_thimble_interval_closed": False,
            "fixed_carrier_exact_separation_proved": False,
            "covariant_alignment_zero_solved": False,
        },
        "next_required_artifact": "MTT_Selected_q79E32ThimbleFrobeniusSeedAndWeightedIntervalExecution_v1",
    }
    dump(PACKET, packet)

    frontier = {
        "schema": "MTTU6FrontierAfterA135.v1",
        "status": "U6_E32_HANDLE_INTERVAL_AND_THIMBLE_NILPOTENT_REDUCTION_CLOSED_FROBENIUS_VALUES_OPEN",
        "closed": [
            "A133 refined beta interval and one-row E32 cutset",
            "A134 rigorous selected E32 handle interval",
            "A135 exact rank-one square-zero local logarithms for all 71 selected thimbles",
            "A135 topological selection of the log-free vanishing branch and explicit Frobenius recurrence",
        ],
        "active_target": "emit certified local B_k, Y_0, and q_k data, then continue the weighted E32 sum within the A134 radius budget",
        "remaining_weighted_thimble_radius_budget": a134["strict_budget_ledger"][
            "remaining_weighted_thimble_combination_radius_budget"
        ],
        "not_closed": [
            "certified numerical Frobenius coefficients and tail majorants",
            "weighted 71-thimble E32 interval",
            "exact frozen-carrier decision",
            "covariant PGL3 F/J continuation",
        ],
    }
    dump(FRONTIER, frontier)

    candidate = {
        "schema": "MTTSelectedQ79E32ThimbleRegularSingularReduction.v1",
        "status": packet["status"],
        "artifact": "A135",
        "packet": relative(PACKET),
        "packet_sha256": sha256(PACKET),
        "frontier": relative(FRONTIER),
        "frontier_sha256": sha256(FRONTIER),
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "what_closes": {
            "all_selected_local_logarithms_rank_one_square_zero": True,
            "vanishing_solution_log_free_branch": True,
            "Frobenius_recurrence_and_inverse": True,
        },
        "what_remains_open": {
            "Frobenius_value_packets": True,
            "weighted_E32_thimble_interval": True,
            "fixed_carrier_and_covariant_decisions": True,
        },
        "next_required_artifact": packet["next_required_artifact"],
    }

    note = f"""# MTT Selected q79 E32 Thimble Regular-Singular Reduction v1

## Exact local theorem

A135 checks the exact interval-certified Picard-Lefschetz matrix `T` for each
of the `{len(rows)}` thimbles in the A134 weighted chain. In every case,

```text
N = T - I,       rank(N) = 1,       N^2 = 0,
T^T J T = J.
```

The primitive generator `v` of `image(N)` also satisfies `N v=0` and
`T v=v`. These are exact integer identities, not floating diagnostics. Since
`N^2=0`, the local monodromy logarithm truncates:

```text
log(T) = N.
```

Thus the compact Gauss-Manin residue is conjugate, up to local loop
orientation, to `+N/(2*pi*i)` or `-N/(2*pi*i)` and is square-zero. The node is
finite, so the affine puncture summand used by the five-period frame is fixed;
extending the residue by zero preserves square-zero nilpotence. The selected
vanishing cycle is in its kernel, so its period is the monodromy-invariant
log-free Frobenius branch.

## Computable recurrence

Write the regular-singular system as

```text
x dY/dx = (R + B_1 x + B_2 x^2 + ...) Y,      R^2=0.
```

For `Y_0 in ker(R)`, every analytic coefficient is uniquely determined by

```text
Y_n = (nI-R)^(-1) sum_(k=1)^n B_k Y_(n-k),
(nI-R)^(-1) = (1/n)(I+R/n).
```

The `E32` endpoint tail is then the ordinary integral of the analytic series
`q_E32(x)Y(x)`. This removes the false fixed-frame blow-up encountered by a
raw matrix-norm Gronwall bound and supplies the correct certificate design:
certified Frobenius seed, majorant tail, then ordinary-point continuation.

## Frontier

A135 closes the singular-structure theorem for all selected thimbles. It does
not yet emit the numerical `B_k`, `Y_0`, and `q_k` balls, so the weighted
71-thimble interval remains open with radius budget
`{a134['strict_budget_ledger']['remaining_weighted_thimble_combination_radius_budget']:.17g}`.
No observed Standard Model value is used.
"""
    NOTE.write_text(note, encoding="utf-8")
    candidate["note"] = relative(NOTE)
    candidate["note_sha256"] = sha256(NOTE)
    dump(CANDIDATE, candidate)

    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79E32ThimbleRegularSingularReduction",
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
                "selected_thimbles": len(rows),
                "selected_l1_norm": sum(abs(coefficients[index]) for index in selected_indices),
                "distinct_image_directions": len(directions),
                "all_rank_one": True,
                "all_square_zero": True,
                "all_vanishing_directions_fixed": True,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
