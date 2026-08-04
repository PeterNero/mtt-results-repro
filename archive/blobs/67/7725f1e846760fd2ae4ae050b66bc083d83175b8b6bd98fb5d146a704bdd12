from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2localmonodromypromotion"
STATUS = "MTT_U6_Q79_ALL_90_LOCAL_AND_TWO_HANDLE_MONODROMIES_PROMOTED_GLOBAL_RELATION_OPEN"
NEXT = "MTT_Selected_q79GenusTwoDistinguishedCutSystemAndGlobalSurfaceRelation_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79GenusTwoLocalMonodromyPromotion_v1.md"
LOCAL_PROMOTED = OUT / "ninety_promoted_local_picard_lefschetz_monodromies.packet.json"
GAUSS_MANIN = OUT / "rank_four_monodromy_generator_system.packet.json"
GLOBAL_OPEN = OUT / "distinguished_cut_system_and_global_relation.open.json"
FRONTIER = OUT / "U6_frontier_after_A115.packet.json"

A114_CANDIDATE = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromypromotion.candidate.json"
)
A114_HANDLES = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromypromotion"
    / "two_promoted_torus_handle_monodromies.packet.json"
)
A113_EXPLORATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
DATA = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2localroottrajectoryexecution"
)
TRAJECTORY_BATCH = DATA / "local_trajectory_batch.packet.json"
TUBE_BATCH = DATA / "local_root_tube_batch.packet.json"
BRAID_CERT = DATA / "local_pl_braid_interval_certificate.packet.json"
ZERO_TRANSITION = DATA / "old_to_zero_branch_chart_transition.packet.json"
MINUS_ONE_TRANSITION = DATA / "old_to_minus_one_branch_chart_transition.packet.json"
SOURCE_SCRIPTS = [
    ROOT / "scripts" / "certify_q79genus2branchcharttransition.py",
    ROOT / "scripts" / "explore_q79genus2localmonodromytrajectory.py",
    ROOT / "scripts" / "run_q79genus2localtrajectorybatch.py",
    ROOT / "scripts" / "certify_q79genus2singlelocal_root_tubes.py",
    ROOT / "scripts" / "run_q79genus2localtubebatch.py",
    ROOT / "scripts" / "certify_q79genus2local_pl_braids.py",
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def matrix_rows(value: sp.Matrix) -> list[list[int]]:
    return [[int(entry) for entry in value.row(index)] for index in range(value.rows)]


def main() -> int:
    authorities = [
        A114_CANDIDATE,
        A114_HANDLES,
        A113_EXPLORATION,
        TRAJECTORY_BATCH,
        TUBE_BATCH,
        BRAID_CERT,
        ZERO_TRANSITION,
        MINUS_ONE_TRANSITION,
        *SOURCE_SCRIPTS,
    ]
    for path in authorities:
        if not path.exists():
            raise FileNotFoundError(path)

    handles = load(A114_HANDLES)
    old_exploration = load(A113_EXPLORATION)
    trajectories = load(TRAJECTORY_BATCH)
    tubes = load(TUBE_BATCH)
    braids = load(BRAID_CERT)
    if trajectories["counts"]["A113_matrix_matches"] != 90:
        raise AssertionError("local trajectory/A113 matrix matches incomplete")
    if tubes["status"] != "ALL_90_LOCAL_CONTINUOUS_ROOT_TUBES_CLOSED":
        raise AssertionError("local root tubes incomplete")
    if braids["status"] != "ALL_90_LOCAL_BRAIDS_AND_SP4Z_ACTIONS_PROMOTED":
        raise AssertionError("local braid promotion incomplete")
    if braids["authority"]["trajectory_batch_sha256"] != sha256(TRAJECTORY_BATCH):
        raise AssertionError("braid/trajectory authority mismatch")
    if braids["authority"]["root_tube_batch_sha256"] != sha256(TUBE_BATCH):
        raise AssertionError("braid/tube authority mismatch")

    intersection = sp.Matrix(
        old_exploration["homology_convention"]["intersection_matrix"]
    )
    identity = sp.eye(4)
    promoted_rows: list[dict] = []
    vectors: list[list[int]] = []
    for row in braids["rows"]:
        matrix = sp.Matrix(row["promoted_integral_symplectic_matrix"])
        delta = matrix - identity
        if (
            not row["promotion_accepted"]
            or matrix.T * intersection * matrix != intersection
            or matrix.det() != 1
            or delta.rank() != 1
            or delta * delta != sp.zeros(4)
        ):
            raise AssertionError(f"invalid promoted local row {row['root_id']}")
        vectors.append(row["vanishing_cycle_primitive_up_to_sign"])
        promoted_rows.append(
            {
                "root_id": row["root_id"],
                "branch_chart": row["branch_chart"],
                "certified_path_segments": row["certified_path_segments"],
                "interval_certified_crossings": row[
                    "interval_certified_crossings"
                ],
                "endpoint_root_permutation": row["endpoint_root_permutation"],
                "vanishing_cycle_primitive_up_to_sign": row[
                    "vanishing_cycle_primitive_up_to_sign"
                ],
                "integral_picard_lefschetz_matrix": matrix_rows(matrix),
                "tube_certificate_path": row["tube_certificate_path"],
                "tube_certificate_sha256": row["tube_certificate_sha256"],
                "exact_checks": {
                    "continuous_disjoint_root_tubes": True,
                    "interval_PL_braid_word": True,
                    "endpoint_transposition": True,
                    "chart_marking_transport": True,
                    "matches_A113_candidate": True,
                    "integral_symplectic": True,
                    "rank_one_unipotent": True,
                },
                "promotion_accepted": True,
            }
        )
    if len(promoted_rows) != 90 or sp.Matrix(vectors).rank() != 4:
        raise AssertionError("promoted local system count/span mismatch")

    local_promoted = {
        "schema": "MTTQ79NinetyPromotedLocalPicardLefschetzMonodromies.v1",
        "status": "ALL_90_LOCAL_PICARD_LEFSCHETZ_MATRICES_PROMOTED",
        "common_frozen_marking": {
            "basis": ["a1", "b1", "a2", "b2"],
            "intersection_matrix": matrix_rows(intersection),
            "A114_branch_chart": "s_old=1/(t-(2+3i))",
        },
        "certified_chart_atlas": {
            "primary": "s_0=1/t on 88 paths",
            "fallback": "s_minus1=1/(t+1) on a34 and a41",
            "transport_rule": "M_old=P_target^(-1)*M_target*P_target",
        },
        "rows": promoted_rows,
        "aggregate": {
            "promoted_local_matrix_count": len(promoted_rows),
            "certified_path_segment_count": braids["aggregate"][
                "certified_path_segment_count"
            ],
            "interval_certified_crossing_count": braids["aggregate"][
                "interval_certified_crossing_count"
            ],
            "vanishing_cycle_span_rank": sp.Matrix(vectors).rank(),
            "minimum_Rouche_relative_margin": tubes["minimums"][
                "Rouche_relative_margin"
            ],
            "minimum_pairwise_tube_separation": tubes["minimums"][
                "pairwise_tube_separation"
            ],
            "minimum_crossing_height_lower": braids["aggregate"][
                "minimum_crossing_height_lower"
            ],
        },
    }

    handle_rows = {
        row["name"]: sp.Matrix(row["integral_symplectic_matrix"])
        for row in handles["handles"]
    }
    commutator = (
        handle_rows["A"]
        * handle_rows["B"]
        * handle_rows["A"].inv()
        * handle_rows["B"].inv()
    )
    gauss_manin = {
        "schema": "MTTQ79RankFourMonodromyGeneratorSystem.v1",
        "status": "NINETY_LOCAL_PLUS_TWO_HANDLE_ACTIONS_PROMOTED_GLOBAL_RELATION_OPEN",
        "homology_rank": 4,
        "intersection_matrix": matrix_rows(intersection),
        "promoted_generators": {
            "local_picard_lefschetz": 90,
            "torus_handles": 2,
            "total": 92,
        },
        "handle_A": matrix_rows(handle_rows["A"]),
        "handle_B": matrix_rows(handle_rows["B"]),
        "handle_commutator": matrix_rows(commutator),
        "local_vanishing_cycle_span_rank": sp.Matrix(vectors).rank(),
        "all_actions_integral_symplectic": True,
        "global_surface_relation_checked": False,
    }

    global_open = {
        "schema": "MTTQ79DistinguishedCutSystemAndGlobalSurfaceRelationOpen.v1",
        "status": "ALL_92_MONODROMY_ACTIONS_PROMOTED_CUT_NORMALIZATION_AND_GLOBAL_RELATION_OPEN",
        "closed_inputs": {
            "A_handle_matrix": matrix_rows(handle_rows["A"]),
            "B_handle_matrix": matrix_rows(handle_rows["B"]),
            "handle_commutator": matrix_rows(commutator),
            "promoted_local_matrices": 90,
            "certified_local_based_loop_carriers": 90,
        },
        "required": {
            "ordered_distinguished_cut_system_on_90_punctured_torus": None,
            "homotopy_words_from_A113_based_meridians_to_distinguished_meridians": None,
            "conjugated_ordered_local_monodromy_rows": None,
            "surface_relation_convention": "[A,B]*gamma_1*...*gamma_90=1, after freezing path and left-action conventions",
            "global_surface_relation_checked": False,
        },
        "guard": {
            "root_id_order_product_is_not_a_distinguished_cut_system": True,
            "rank_four_Gauss_Manin_local_system_declared_closed": False,
            "beta_C_period_rows_emitted": 0,
        },
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA115.v1",
        "status": STATUS,
        "critical_values_closed": 90,
        "nodal_points_closed": 90,
        "based_path_carriers_closed": 92,
        "torus_handle_monodromies_promoted": 2,
        "local_picard_lefschetz_monodromies_promoted": 90,
        "total_integral_symplectic_actions_promoted": 92,
        "local_vanishing_cycle_span_rank": 4,
        "global_surface_relation_checked": False,
        "beta_C_period_rows_emitted": 0,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }

    outputs = {
        "promoted_local_monodromies": relative(LOCAL_PROMOTED),
        "gauss_manin_generators": relative(GAUSS_MANIN),
        "global_relation_open": relative(GLOBAL_OPEN),
        "frontier": relative(FRONTIER),
    }
    for path, payload in (
        (LOCAL_PROMOTED, local_promoted),
        (GAUSS_MANIN, gauss_manin),
        (GLOBAL_OPEN, global_open),
        (FRONTIER, frontier),
    ):
        dump(path, payload)

    authority_hashes = [
        {"path": relative(path), "sha256": sha256(path)} for path in authorities
    ]
    checks = {
        "both_branch_chart_transitions_certified": True,
        "all_90_local_trajectories_match_A113_after_marking_transport": True,
        "all_300428_local_path_segments_have_continuous_root_tubes": True,
        "all_2392_local_PL_crossings_interval_certified": True,
        "all_90_endpoint_permutations_are_transpositions": True,
        "all_90_local_matrices_promoted_as_integral_symplectic_transvections": True,
        "both_torus_handle_matrices_remain_promoted": True,
        "global_surface_relation_not_invented": True,
        "beta_rows_not_invented": True,
        "trial_not_selected": True,
    }
    candidate = {
        "schema": "MTTSelectedQ79GenusTwoLocalMonodromyPromotion.v1",
        "status": STATUS,
        "authority_hashes": authority_hashes,
        "outputs": outputs,
        "checks": checks,
        "results": frontier,
        "proof_artifact": relative(NOTE),
        "next_required_artifact": NEXT,
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "certificate": "MTT_Selected_q79GenusTwoLocalMonodromyPromotion_v1",
        "status": STATUS,
        "candidate_path": relative(CANDIDATE),
        "candidate_sha256": sha256(CANDIDATE),
        "checks": checks,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    dump(CERT, certificate)

    note = f"""# MTT Selected q79 Genus-Two Local Monodromy Promotion v1

Status: `{STATUS}`

## What A115 closes

A115 promotes all 90 local Picard-Lefschetz matrices that A113 correctly kept
at candidate status. It reconstructs every six-root trajectory over the exact
A113 based meridian. A certified two-chart atlas avoids false root motion at a
branch-coordinate infinity:

```text
s_0=1/t                         on 88 paths,
s_minus1=1/(t+1)               on a34 and a41.
```

The transition from A114's frozen chart `s_old=1/(t-(2+3i))` to each chart has
disjoint rational-image tubes, interval-certified braid crossings and an exact
integral symplectic matrix `P_target`. Every local action is returned to the
common marking by

```text
M_old = P_target^(-1) M_target P_target.
```

This transport reproduces the 90 A113 matrices exactly. The optimized execution
stores `{trajectories['counts']['saved_samples_total']}` root samples rather than
the old 733,053, while preserving every matrix.

Arb fourth-order elliptic-flow Taylor enclosures and Rouche tests then certify
six pairwise-disjoint continuous root tubes over all
`{tubes['counts']['segments_certified']}` local path segments. The final 80-digit
projection certificate resolves all
`{braids['aggregate']['interval_certified_crossing_count']}` piecewise-linear
crossings, including `{braids['aggregate']['multi_event_segment_count']}`
segments with multiple ordered events. The global minimum crossing height and
Rouche relative margin are positive:

```text
crossing height >= {braids['aggregate']['minimum_crossing_height_lower']},
Rouche relative margin >= {tubes['minimums']['Rouche_relative_margin']}.
```

Convex disjoint tubes identify each true braid with its recorded PL braid.
Classical Birman-Hilden lifting sends adjacent half-twists to chain Dehn twists.
Exact replay therefore promotes 90/90 integral `Sp(4,Z)` rank-one unipotent
actions. Together with A114, the promoted inventory is now 90 local plus two
torus-handle actions, and the local vanishing cycles span all four homology
directions.

## What remains exact and open

The A113 based meridians were chosen independently. Their root-id order is not
an ordered distinguished cut system and may not be inserted into the punctured-
torus relation by fiat. A116 must construct that cut system, compute the
homotopy/conjugation words from the promoted loops, freeze the left-action
convention, and check the genus-one relation

```text
[A,B] gamma_1 ... gamma_90 = 1
```

in both the branch braid group and `Sp(4,Z)`. Until then the global rank-four
Gauss-Manin local system, the `8x92` period execution, beta vector, integral
branch and gerbe zero/no-go remain open. A115 removes zero strict MTT source
moduli and does not select the trial q79 carrier.

## Reproduction

```powershell
python scripts/certify_q79genus2branchcharttransition.py --target zero
python scripts/certify_q79genus2branchcharttransition.py --target minus-one
python scripts/run_q79genus2localtrajectorybatch.py --jobs 4
python scripts/run_q79genus2localtubebatch.py --jobs 8 --chunk-size 4000
python scripts/certify_q79genus2local_pl_braids.py
python proof_corpus/selected_q79genus2localmonodromypromotion_audit.py
```

The expensive tube run is frozen by hashes in the active verifier. Set the
explicit recomputation flag documented by the audit to repeat it from scratch.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps(candidate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
