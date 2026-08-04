"""Build the q79 trace-split CLN carrier and world-in-world bridge theorem."""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79tracesplitclncarrierandworldinworldbridge"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "q79_trace_split_cln_carrier_and_bridge_cutset.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_q79TraceSplitCLNCarrierAndWorldInWorldBridge_v1.md"
)

A45_CERT = (
    ROOT
    / "certificates"
    / "selected_classlaneprojectorsandweakrealstructuresourcetheorem_certificate.json"
)
A103_CERT = (
    ROOT
    / "certificates"
    / "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection_certificate.json"
)
A103_COVER = (
    ROOT
    / "candidate_data"
    / "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection"
    / "q79_genus_two_determinant_zero_spectral_cover.packet.json"
)
A103_SHARED = (
    ROOT
    / "candidate_data"
    / "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection"
    / "rank_one_fuyau_shared_circle_clutching.packet.json"
)
A104_CERT = (
    ROOT
    / "certificates"
    / "selected_q79twistedspectralgerbelifthymandbianchiexecution_certificate.json"
)
A104_TOPOLOGY = (
    ROOT
    / "candidate_data"
    / "selected_q79twistedspectralgerbelifthymandbianchiexecution"
    / "spectral_surface_invariants.packet.json"
)


Matrix = list[list[Fraction]]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def identity(size: int) -> Matrix:
    return [
        [Fraction(int(row == column)) for column in range(size)]
        for row in range(size)
    ]


def zero(rows: int, columns: int) -> Matrix:
    return [[Fraction(0) for _ in range(columns)] for _ in range(rows)]


def add(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[row][column] + right[row][column] for column in range(len(left[0]))]
        for row in range(len(left))
    ]


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[row][column] - right[row][column] for column in range(len(left[0]))]
        for row in range(len(left))
    ]


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(
                (left[row][index] * right[index][column] for index in range(len(right))),
                Fraction(0),
            )
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def transpose(matrix: Matrix) -> Matrix:
    return [list(column) for column in zip(*matrix)]


def scale(value: Fraction, matrix: Matrix) -> Matrix:
    return [[value * entry for entry in row] for row in matrix]


def rank(matrix: Matrix) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        divisor = work[pivot_row][column]
        work[pivot_row] = [entry / divisor for entry in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            coefficient = work[row][column]
            if coefficient:
                work[row] = [
                    work[row][index] - coefficient * work[pivot_row][index]
                    for index in range(columns)
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def determinant(matrix: Matrix) -> Fraction:
    if len(matrix) != len(matrix[0]):
        raise ValueError("determinant requires a square matrix")
    work = [row[:] for row in matrix]
    result = Fraction(1)
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result *= -1
        pivot_value = work[column][column]
        result *= pivot_value
        for row in range(column + 1, len(work)):
            coefficient = work[row][column] / pivot_value
            for index in range(column, len(work)):
                work[row][index] -= coefficient * work[column][index]
    return result


def block_diagonal(*blocks: Matrix) -> Matrix:
    size = sum(len(block) for block in blocks)
    output = zero(size, size)
    offset = 0
    for block in blocks:
        for row in range(len(block)):
            for column in range(len(block[0])):
                output[offset + row][offset + column] = block[row][column]
        offset += len(block)
    return output


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def permutation_matrix(permutation: tuple[int, ...]) -> Matrix:
    matrix = zero(len(permutation), len(permutation))
    for row, column in enumerate(permutation):
        matrix[row][column] = Fraction(1)
    return matrix


def encode_matrix(matrix: Matrix) -> list[list[str]]:
    return [[str(entry) for entry in row] for row in matrix]


def main() -> int:
    a45 = load(A45_CERT)
    a103 = load(A103_CERT)
    cover = load(A103_COVER)
    shared = load(A103_SHARED)
    a104 = load(A104_CERT)
    topology = load(A104_TOPOLOGY)

    if not a45["native_rank_flag_closed_up_to_unitary_equivalence"]:
        raise AssertionError("A45 rank-signature authority changed")
    if not a103["results"]["determinant_zero_q79_spectral_cover_constructed"]:
        raise AssertionError("A103 degree-three spectral cover changed")
    if cover["determinant_zero_cover"]["degree_over_K3"] != 3:
        raise AssertionError("q79 spectral degree changed")
    if cover["determinant_zero_cover"]["fiberwise_determinant"] != 0:
        raise AssertionError("q79 determinant-zero condition changed")
    if topology["Lefschetz_and_Hodge"]["betti"][0] != 1:
        raise AssertionError("q79 spectral surface connectedness changed")
    if shared["rank_one_FuYau_topology"]["space"] != "X=P_delta x S1_shared":
        raise AssertionError("q79 shared-circle topology changed")

    identity3 = identity(3)
    p_trace = [[Fraction(1, 3) for _ in range(3)] for _ in range(3)]
    p_zero = subtract(identity3, p_trace)
    p_full = identity3

    trace_row = [[Fraction(1), Fraction(1), Fraction(1)]]
    unit_column = [[Fraction(1)], [Fraction(1)], [Fraction(1)]]
    trace_zero_basis = [
        [Fraction(1), Fraction(0)],
        [Fraction(-1), Fraction(1)],
        [Fraction(0), Fraction(-1)],
    ]
    reuse_basis = [
        [unit_column[row][0], *trace_zero_basis[row]]
        for row in range(3)
    ]

    permutations = list(itertools.permutations(range(3)))
    signed_rotations = []
    monodromy_checks = []
    for permutation in permutations:
        sign = permutation_sign(permutation)
        raw = permutation_matrix(permutation)
        oriented = scale(Fraction(sign), raw)
        signed_rotations.append(oriented)
        monodromy_checks.append(
            determinant(oriented) == 1
            and multiply(transpose(oriented), oriented) == identity3
            and multiply(oriented, p_trace) == multiply(p_trace, oriented)
            and multiply(oriented, p_zero) == multiply(p_zero, oriented)
        )

    lane_projectors = [
        block_diagonal(identity(1), zero(2, 2), zero(3, 3)),
        block_diagonal(zero(1, 1), identity(2), zero(3, 3)),
        block_diagonal(zero(1, 1), zero(2, 2), identity(3)),
    ]
    identity6 = identity(6)

    exact_checks = {
        "trace_after_unit_is_degree_three": multiply(trace_row, unit_column)
        == [[Fraction(3)]],
        "trace_projector_idempotent": multiply(p_trace, p_trace) == p_trace,
        "trace_zero_projector_idempotent": multiply(p_zero, p_zero) == p_zero,
        "trace_and_zero_projectors_orthogonal": multiply(p_trace, p_zero)
        == zero(3, 3),
        "trace_plus_zero_is_full": add(p_trace, p_zero) == p_full,
        "trace_zero_basis_is_in_kernel": multiply(trace_row, trace_zero_basis)
        == zero(1, 2),
        "reuse_basis_is_an_isomorphism": determinant(reuse_basis) != 0,
        "canonical_carrier_ranks_are_1_2_3": [
            rank(p_trace),
            rank(p_zero),
            rank(p_full),
        ]
        == [1, 2, 3],
        "signed_sheet_monodromy_is_SO3": all(monodromy_checks),
        "six_dimensional_lane_projectors_are_idempotent": all(
            multiply(projector, projector) == projector for projector in lane_projectors
        ),
        "six_dimensional_lane_projectors_are_pairwise_orthogonal": all(
            multiply(lane_projectors[left], lane_projectors[right]) == zero(6, 6)
            for left in range(3)
            for right in range(3)
            if left != right
        ),
        "six_dimensional_lane_projectors_sum_to_identity": add(
            add(lane_projectors[0], lane_projectors[1]), lane_projectors[2]
        )
        == identity6,
        "six_dimensional_lane_projector_ranks_are_1_2_3": [
            rank(projector) for projector in lane_projectors
        ]
        == [1, 2, 3],
    }
    if not all(exact_checks.values()):
        failed = [name for name, passed in exact_checks.items() if not passed]
        raise AssertionError(f"trace-split exact checks failed: {failed}")

    bridge_obligations = {
        "worldinworld_real_rank3_carrier_to_q79_signed_sheet_carrier_intertwiner": False,
        "q79_sheet_monodromy_spin3_lift_or_w2_zero_certificate": False,
        "selected_global_hermitian_or_euclidean_continuation_across_branch_locus": False,
        "selected_worldinworld_Q_or_same_source_closure_hessian_endomorphism": False,
        "uniform_polar_or_spectral_gap_and_degeneracy_stratification": False,
        "proto_spinor_J_intertwiner_on_trace_zero_rank2_lane": False,
        "selected_shared_circle_holonomy_value_if_value_bearing": False,
        "connection_and_HYM_covariance_intertwiner": False,
    }

    packet = {
        "schema": "MTTSelectedQ79TraceSplitCLNCarrierAndWorldInWorldBridge.v1",
        "status": "Q79_DEGREE3_TRACE_SPLIT_CLN_1_2_3_CARRIER_CLOSED_WORLDINWORLD_Q_AND_PHYSICAL_INTERTWINER_OPEN",
        "authority": [
            {"path": relative(path), "sha256": sha256(path)}
            for path in (
                A45_CERT,
                A103_CERT,
                A103_COVER,
                A103_SHARED,
                A104_CERT,
                A104_TOPOLOGY,
                Path(__file__),
            )
        ],
        "exact_q79_carrier_theorem": {
            "finite_flat_cover": "pi:C->K3 is the pullback of the universal degree-three divisor in E x |3*0|",
            "pushforward_algebra": "A=pi_* O_C is finite locally free of rank 3",
            "trace_identity": "Tr_A(1)=3",
            "canonical_projector": "p_cen=(1/3) unit o Tr",
            "trace_zero_projector": "p_lens=I-p_cen",
            "canonical_split": "A=O direct-sum A_0, A_0=ker(Tr), ranks 1+2",
            "nil_full_carrier": "B_nil uses the full rank-3 A carrier as a reused copy",
            "six_filter_carrier": "H_CLN=L_shared tensor (O direct-sum A_0 direct-sum A)",
            "rank_signature": [1, 2, 3],
            "total_rank": 6,
            "shared_circle_statement": "the same rank-one local-system factor L_shared twists all three lanes; its holonomy value is not selected here",
            "fitted_continuous_parameters_added": 0,
            "proved": True,
        },
        "exact_matrices": {
            "p_trace_rank1": encode_matrix(p_trace),
            "p_trace_zero_rank2": encode_matrix(p_zero),
            "p_full_rank3": encode_matrix(p_full),
            "trace_zero_basis_columns": encode_matrix(trace_zero_basis),
            "unit_plus_trace_zero_reuse_basis": encode_matrix(reuse_basis),
            "six_lane_projectors": [encode_matrix(projector) for projector in lane_projectors],
            "checks": exact_checks,
        },
        "monodromy_and_orientation_theorem": {
            "spectral_surface_connected": True,
            "generic_three_sheet_monodromy_transitive": True,
            "global_ordered_sheet_flag_selected": False,
            "reason": "a global chosen sheet would split the connected degree-three cover; transitive monodromy instead preserves only the trace line and trace-zero plane canonically",
            "raw_permutation_determinant": "sign(sigma)",
            "canonical_orientation_correction": "rho_plus(sigma)=sign(sigma) P_sigma",
            "rho_plus_lies_in_SO3": True,
            "spin_lift_status": "open; compute the lift of q79 sheet monodromy to the binary double cover, equivalently the relevant w2 obstruction",
            "signed_S3_rotation_count_checked": len(signed_rotations),
        },
        "a45_scope_correction": {
            "conditional_complete_flag_linear_algebra_remains_true": True,
            "rank_signature_alone_implies_nested_complete_flag": False,
            "corpus_phrase_adds_1_2_3_directions_supports_incremental_lanes": True,
            "correct_q79_realization": "orthogonal rank-1 trace and rank-2 trace-zero lanes plus one reused full rank-3 carrier",
            "old_nested_representatives_are_not_source_promoted_by_rank_count_alone": True,
            "effect_on_locked_27_yukawa_ew_values": "none; this changes foundational source provenance, not the already computed finite matrices or profile values",
        },
        "worldinworld_polar_bridge": {
            "local_real_theorem": "for an invertible real 3x3 Q, Q=R S with R in SO3 and S positive symmetric after orientation choice; Mat3=so3 direct-sum Sym3 has dimensions 3+6",
            "q79_unbranched_carrier": "the sign-twisted real three-sheet local system has a canonical Euclidean metric and SO3 monodromy",
            "what_this_closes": "a parameter-free oriented rank-3 target carrier with canonical 1+2 decomposition",
            "what_it_does_not_close": "the same-source map from T(P) and T(I) to that carrier, the selected Q/Hessian, branch-locus continuation, or HYM connection compatibility",
        },
        "physical_bridge_contract": {
            "fields": bridge_obligations,
            "closed_count": sum(bridge_obligations.values()),
            "required_count": len(bridge_obligations),
            "full_bridge_closed": all(bridge_obligations.values()),
        },
        "external_math_anchors": [
            "https://stacks.math.columbia.edu/tag/02K9",
            "https://stacks.math.columbia.edu/tag/0BVH",
            "https://stacks.math.columbia.edu/tag/01C5",
        ],
        "next_required_artifact": "MTT_Selected_q79SignedPermutationSpinLiftAndWorldInWorldQSource_v1",
    }
    dump(PACKET, packet)

    note = """# MTT Selected q79 Trace-Split CLN Carrier and World-in-World Bridge v1

## Result

The q79 degree-three spectral cover supplies a canonical global realization of
the MTT `1+2+3=6` rank pattern, but it is not the nested ordered-sheet flag used
in the earlier A45 source interpretation.

Let

```text
pi:C -> K3
```

be the q79 determinant-zero degree-three spectral cover. It is the pullback of
the universal relative degree-three divisor over `|3*0|`. Hence it is finite
locally free of degree three and

```text
A = pi_* O_C
```

is a rank-three algebra bundle. The unit and trace obey

```text
Tr_A(1)=3.
```

Because the theory is over characteristic zero, the maps

```text
p_cen  = (1/3) unit o Tr,
p_lens = I-p_cen
```

are canonical complementary idempotents. Therefore

```text
A = O direct-sum A_0,       A_0=ker(Tr),
rank(O)=1, rank(A_0)=2, rank(A)=3.
```

Pull these bundles to `X=P_delta x S1_shared` and tensor every lane by the
same shared-circle line/local-system carrier `L_shared`. The six-direction
filter carrier is then

```text
H_CLN = L_shared tensor (O direct-sum A_0 direct-sum A),
rank(H_CLN)=1+2+3=6.
```

This construction adds no continuous parameter. The numerical holonomy of
`L_shared`, if it is used as a value-bearing phase, remains a separate source
question.

## Why this is better than a global sheet flag

The q79 spectral surface is connected (`b0=1`). Away from the branch locus its
three sheets therefore have transitive monodromy. A globally selected first
sheet would split the cover, so no global ordered sheet flag is available.
What survives monodromy canonically is exactly:

```text
constant/trace line             rank 1,
trace-zero standard plane       rank 2,
full permutation carrier        rank 3.
```

The earlier A45 linear-algebra statement remains true conditionally: if a
complete flag is supplied, it is unitarily equivalent to the displayed nested
projectors. What was not proved there is that the corpus rank count by itself
supplies the inclusion maps of a complete flag. The q79 geometry instead
selects orthogonal incremental lanes. This matches the Book's wording that the
three bundles add `1`, `2`, and `3` filter directions and that the Laplacians
commute.

This correction does not change the computed 27x27 matrix, Yukawa, mass, or
electroweak profile values. It changes only the claimed provenance of the
nested projectors.

## Orientation and the proto-spinor target

On the unbranched locus, let `P_sigma` be the real permutation action on the
three sheets. Odd permutations reverse orientation. There is a canonical
parameter-free correction

```text
rho_plus(sigma)=sign(sigma) P_sigma.
```

For every `sigma in S3`, `rho_plus(sigma)` is orthogonal with determinant one.
Thus the sign-twisted three-sheet carrier has `SO(3)` monodromy and the standard
Euclidean metric. Its invariant line and orthogonal plane are the same
rank-`1+2` trace decomposition, with the line carrying the sign character.

This supplies the correct oriented rank-three target for the world-in-world
polar construction. It does not yet prove a `Spin(3)` lift. That next check is
the lift of the actual q79 sheet monodromy to the binary double cover, or
equivalently the relevant `w2` obstruction.

## World-in-world polar bridge

For an invertible real `3x3` map `Q`, polar decomposition gives

```text
Q=R S,       R in SO(3),       S=S^T>0,
Mat(3,R)=so(3) direct-sum Sym(3),
dimensions 9=3+6.
```

The theorem above now supplies a q79-side oriented rank-three carrier on which
such a local map can live. The missing statement is no longer "where do ranks
1,2,3 come from?" It is the typed same-source map that identifies the real
world-in-world carrier with the sign-twisted q79 sheet carrier and emits the
actual `Q` or closure Hessian.

Eight physical bridge fields remain open: the real-carrier intertwiner, the
Spin lift, continuation across the branch locus, the selected `Q`/Hessian, a
gap/degeneracy certificate, the proto-spinor `J` map on the rank-two lane, any
value-bearing shared-circle holonomy, and HYM/connection covariance.

## Scope

Closed here:

```text
q79 finite-flat rank-three pushforward algebra,
canonical rank-one trace and rank-two trace-zero lanes,
shared-circle rank pattern 1+2+3=6,
transitive-monodromy no-go for a global ordered sheet flag,
canonical SO(3) sign-twist of the sheet carrier.
```

Still open:

```text
actual q79 sheet-monodromy Spin(3) lift,
same-source world-in-world carrier intertwiner,
selected Q/Hessian and branch-locus continuation,
proto-spinor J and HYM connection compatibility,
the independent A136 weighted-thimble interval decision.
```

No observed Standard Model value and no fitted continuous parameter enters this
theorem.

## External mathematical anchors

- [Finite locally free morphisms](https://stacks.math.columbia.edu/tag/02K9)
- [Trace and discriminant of a finite locally free morphism](https://stacks.math.columbia.edu/tag/0BVH)
- [Direct summands of finite locally free sheaves](https://stacks.math.columbia.edu/tag/01C5)

Next artifact:
`MTT_Selected_q79SignedPermutationSpinLiftAndWorldInWorldQSource_v1`.
"""
    NOTE.write_text(note, encoding="utf-8")

    candidate = {
        "schema": "MTTSelectedQ79TraceSplitCLNCarrierAndWorldInWorldBridge.v1",
        "artifact": "FoundationalBridge-FB1",
        "status": packet["status"],
        "packet": relative(PACKET),
        "packet_sha256": sha256(PACKET),
        "note": relative(NOTE),
        "note_sha256": sha256(NOTE),
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "new_fitted_continuous_parameters": 0,
        "what_closes": {
            "q79_trace_split_rank_1_2_3_carrier": True,
            "shared_circle_rank_six_carrier": True,
            "global_ordered_sheet_flag_no_go": True,
            "signed_sheet_SO3_carrier": True,
        },
        "what_remains_open": {
            "full_worldinworld_q79_intertwiner": True,
            "q79_sheet_spin_lift": True,
            "selected_Q_or_Hessian": True,
            "HYM_connection_compatibility": True,
            "A136_weighted_thimble_interval": True,
        },
        "next_required_artifact": packet["next_required_artifact"],
    }
    dump(CANDIDATE, candidate)

    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79TraceSplitCLNCarrierAndWorldInWorldBridge",
        "candidate_path": relative(CANDIDATE),
        "candidate_sha256": sha256(CANDIDATE),
        "status": candidate["status"],
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "new_fitted_continuous_parameters": 0,
        "q79_trace_split_rank_1_2_3_carrier_closed": True,
        "worldinworld_q79_physical_intertwiner_closed": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }
    dump(CERTIFICATE, certificate)

    print(f"wrote {relative(PACKET)}")
    print(f"wrote {relative(CANDIDATE)}")
    print(f"wrote {relative(CERTIFICATE)}")
    print(f"wrote {relative(NOTE)}")
    print("closed: canonical q79 trace split with ranks 1+2+3=6")
    print("closed: signed three-sheet monodromy lies in SO(3)")
    print("open: Spin lift, world-in-world Q source, and HYM intertwiner")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
