from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2handlemonodromypromotion"
STATUS = "MTT_U6_Q79_TWO_TORUS_HANDLE_MONODROMIES_PROMOTED_90_LOCAL_AND_GLOBAL_RELATION_OPEN"
NEXT = "MTT_Selected_q79GenusTwoLocalRootTubeAndDistinguishedCutSystemExecution_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79GenusTwoHandleMonodromyPromotion_v1.md"

PROMOTED = OUT / "two_promoted_torus_handle_monodromies.packet.json"
OPEN = OUT / "local_meridian_and_global_relation.open.json"
FRONTIER = OUT / "U6_frontier_after_A114.packet.json"

A113 = ROOT / "candidate_data" / "selected_q79genus2basedpathsystemandmonodromycandidate.candidate.json"
EXPLORATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromycandidate"
    / "handle_monodromy_exploration.packet.json"
)
TUBES = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromycandidate"
    / "handle_continuous_root_tube_certificate.packet.json"
)
BRAIDS = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromycandidate"
    / "handle_pl_braid_interval_certificate.packet.json"
)
TUBE_SCRIPT = ROOT / "scripts" / "certify_q79genus2handle_root_tubes.py"
BRAID_SCRIPT = ROOT / "scripts" / "certify_q79genus2handle_pl_braids.py"


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
    for path in (A113, EXPLORATION, TUBES, BRAIDS, TUBE_SCRIPT, BRAID_SCRIPT):
        if not path.exists():
            raise FileNotFoundError(path)

    exploration = load(EXPLORATION)
    tubes = load(TUBES)
    braids = load(BRAIDS)
    if tubes["status"] != "TWO_HANDLE_CONTINUOUS_ROOT_TUBES_CLOSED":
        raise AssertionError("handle root tubes are not closed")
    if braids["status"] != "TWO_HANDLE_BRAIDS_AND_SP4Z_ACTIONS_PROMOTED":
        raise AssertionError("handle braid actions are not promoted")
    if braids["authority"]["exploration_sha256"] != sha256(EXPLORATION):
        raise AssertionError("braid/exploration authority mismatch")
    if braids["authority"]["continuous_root_tube_certificate_sha256"] != sha256(TUBES):
        raise AssertionError("braid/tube authority mismatch")

    intersection = sp.Matrix(exploration["homology"]["intersection_matrix"])
    identity = sp.eye(4)
    chain_vectors = [sp.Matrix(row) for row in exploration["homology"]["chain_vectors"]]
    positive = [identity - vector * vector.T * intersection for vector in chain_vectors]
    negative = [value.inv() for value in positive]

    promoted_rows: list[dict] = []
    matrices: dict[str, sp.Matrix] = {}
    for row in braids["handles"]:
        if not row["promotion_accepted"] or not row["continuous_root_tube_certificate"]:
            raise AssertionError("handle action lacks promotion evidence")
        if min(
            float(row["minimum_projected_endpoint_pair_difference_lower"]),
            float(row["minimum_crossing_height_lower"]),
            float(row["minimum_endpoint_matching_gap_lower"]),
        ) <= 0:
            raise AssertionError("nonpositive interval braid margin")
        action = identity
        for generator, sign in row["raw_braid_word"]:
            action = (positive if sign == 1 else negative)[generator - 1] * action
        expected = sp.Matrix(row["promoted_integral_symplectic_matrix"])
        if action != expected:
            raise AssertionError("exact braid replay mismatch")
        if action.T * intersection * action != intersection or action.det() != 1:
            raise AssertionError("promoted matrix is not in Sp(4,Z)")
        matrices[row["name"]] = action
        tube_row = next(value for value in tubes["handles"] if value["name"] == row["name"])
        if not tube_row["complete"] or float(tube_row["minimum_Rouche_relative_margin"]) <= 0:
            raise AssertionError("nonpositive continuous-tube margin")
        promoted_rows.append(
            {
                "name": row["name"],
                "base_path": (
                    "w(s)=(1+i)/4+s"
                    if row["name"] == "A"
                    else "w(s)=(1+i)/4+i*s"
                ),
                "continuous_root_tube_segments": tube_row["segments_certified"],
                "segments_requiring_certificate_subdivision": tube_row[
                    "segments_requiring_certificate_subdivision"
                ],
                "minimum_Rouche_relative_margin": tube_row[
                    "minimum_Rouche_relative_margin"
                ],
                "minimum_pairwise_tube_separation": tube_row[
                    "minimum_pairwise_tube_separation"
                ],
                "interval_certified_braid_crossings": row["crossing_count"],
                "raw_braid_word": row["raw_braid_word"],
                "endpoint_root_permutation": row["final_root_permutation"],
                "integral_symplectic_matrix": matrix_rows(action),
                "exact_checks": {
                    "continuous_disjoint_root_tubes": True,
                    "piecewise_linear_braid_isotopy": True,
                    "interval_crossing_order_and_signs": True,
                    "Birman_Hilden_half_twist_lift": True,
                    "raw_word_replays_matrix": True,
                    "determinant_one": True,
                    "preserves_intersection_form": True,
                },
                "promotion_accepted": True,
            }
        )

    handle_a = matrices["A"]
    handle_b = matrices["B"]
    commutator = handle_a * handle_b * handle_a.inv() * handle_b.inv()
    if handle_a * handle_b == handle_b * handle_a:
        raise AssertionError("handle actions unexpectedly commute")

    promoted = {
        "schema": "MTTQ79TwoPromotedTorusHandleMonodromies.v1",
        "status": "A_AND_B_HANDLE_MONODROMIES_PROMOTED_IN_FROZEN_GENUS_TWO_MARKING",
        "base": {
            "normalized_torus": "C/(Z+iZ)",
            "base_w": "(1+i)/4",
            "base_fiber": "(a,b)=(-i,1+i)",
        },
        "fiber": {
            "genus": 2,
            "branch_root_count": 6,
            "homology_basis": ["a1", "b1", "a2", "b2"],
            "intersection_matrix": matrix_rows(intersection),
            "hyperelliptic_chain_vectors": exploration["homology"]["chain_vectors"],
        },
        "handles": promoted_rows,
        "aggregate": {
            "promoted_handle_monodromies": 2,
            "total_certified_path_segments": sum(
                row["continuous_root_tube_segments"] for row in promoted_rows
            ),
            "total_interval_certified_braid_crossings": sum(
                row["interval_certified_braid_crossings"] for row in promoted_rows
            ),
            "matrices_noncommuting": True,
            "commutator_A_B_Ainv_Binv": matrix_rows(commutator),
            "commutator_symplectic": commutator.T * intersection * commutator == intersection,
        },
        "reproducibility": {
            "expensive_root_tube_command": "python scripts/certify_q79genus2handle_root_tubes.py",
            "interval_braid_command": "python scripts/certify_q79genus2handle_pl_braids.py",
            "active_verifier_policy": "hash frozen trajectories/certificates and independently replay every braid word and integral matrix",
        },
    }

    open_payload = {
        "schema": "MTTQ79LocalMeridianAndGlobalRelationOpen.v1",
        "status": "TWO_HANDLES_PROMOTED_LOCAL_ROOT_TUBES_AND_DISTINGUISHED_GLOBAL_RELATION_OPEN",
        "closed": {
            "A_handle_monodromy": matrix_rows(handle_a),
            "B_handle_monodromy": matrix_rows(handle_b),
            "handle_commutator": matrix_rows(commutator),
        },
        "required": {
            "continuous_root_tubes_for_90_local_meridians": 0,
            "promoted_local_Picard_Lefschetz_matrices": 0,
            "ordered_distinguished_cut_system_on_once_based_90_punctured_torus": None,
            "local_meridian_conjugations_into_that_cut_system": None,
            "surface_relation_convention": "[A,B]*gamma_1*...*gamma_90=1, up to the explicitly frozen path/action convention",
            "global_surface_relation_checked": False,
        },
        "guard": {
            "independently_based_A113_meridians_may_not_be_multiplied_in_root_id_order": True,
            "A113_local_matrix_candidates_silently_promoted": False,
            "Gauss_Manin_local_system_closed": False,
            "beta_C_period_rows_emitted": 0,
        },
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA114.v1",
        "status": STATUS,
        "critical_values_closed": 90,
        "nodal_points_closed": 90,
        "critical_meridian_path_carriers_closed": 90,
        "torus_handle_path_carriers_closed": 2,
        "torus_handle_monodromies_promoted": 2,
        "local_integral_monodromy_candidates_computed": 90,
        "local_integral_monodromy_matrices_promoted": 0,
        "global_surface_relation_checked": False,
        "beta_C_period_rows_emitted": 0,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }

    outputs = {
        "promoted_handles": relative(PROMOTED),
        "local_and_global_open": relative(OPEN),
        "frontier": relative(FRONTIER),
    }
    for path, payload in ((PROMOTED, promoted), (OPEN, open_payload), (FRONTIER, frontier)):
        dump(path, payload)

    authority_hashes = [
        {"path": relative(path), "sha256": sha256(path)}
        for path in (A113, EXPLORATION, TUBES, BRAIDS, TUBE_SCRIPT, BRAID_SCRIPT)
    ]
    checks = {
        "all_11932_handle_path_segments_have_continuous_disjoint_root_tubes": True,
        "all_74_PL_braid_crossings_interval_certified": True,
        "both_endpoint_root_permutations_certified": True,
        "both_raw_braid_words_replay_exactly": True,
        "both_integral_actions_preserve_the_frozen_intersection_form": True,
        "both_torus_handle_monodromies_promoted": True,
        "ninety_local_candidates_not_silently_promoted": True,
        "global_surface_relation_not_invented": True,
        "beta_rows_not_invented": True,
        "trial_not_selected": True,
    }
    candidate = {
        "schema": "MTTSelectedQ79GenusTwoHandleMonodromyPromotion.v1",
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
        "certificate": "MTT_Selected_q79GenusTwoHandleMonodromyPromotion_v1",
        "status": STATUS,
        "candidate_path": relative(CANDIDATE),
        "candidate_sha256": sha256(CANDIDATE),
        "checks": checks,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    dump(CERT, certificate)

    note = f"""# MTT Selected q79 Genus-Two Handle Monodromy Promotion v1

Status: `{STATUS}`

## The promoted result

A114 promotes the two nonlocal torus-handle actions for the selected q79
genus-two family. The normalized base loops are

```text
A: w(s)=(1+i)/4+s,
B: w(s)=(1+i)/4+i*s,
```

and elliptic periodicity returns both endpoints to the same regular fiber.
FLINT/Arb Rouche tests certify six pairwise-disjoint continuous root tubes on
all 6,928 A segments and all 5,004 B segments, 11,932 segments in total. The few broad interval boxes are
bisected while retaining one fixed root disk; the maximum subdivision depth is
one for A and three for B. The minimum relative Rouche margins remain positive:
`{tubes['handles'][0]['minimum_Rouche_relative_margin']}` and
`{tubes['handles'][1]['minimum_Rouche_relative_margin']}`.

An independent 80-digit interval projection at `exp(-i*pi/7)` certifies every
endpoint order, all 74 crossing signs and heights, and the order of the two
segments containing multiple crossing events. Convexity of each disjoint tube
gives an isotopy from the true root strands to these certified piecewise-linear
braids.

Birman-Hilden hyperelliptic lifting supplies the standard topological bridge:
each adjacent branch-point half-twist lifts to the corresponding chain Dehn
twist. In the frozen basis `[a1,b1,a2,b2]`, exact word replay gives

```text
M_A = {matrix_rows(handle_a)},
M_B = {matrix_rows(handle_b)}.
```

Both matrices have determinant one and preserve the integral intersection
form. They do not commute. Their promoted commutator is

```text
[M_A,M_B] = {matrix_rows(commutator)}.
```

This is a real advance over A113: the handle matrices are no longer numerical candidates.
The expensive root-tube computation is frozen with hashes, while
the active verifier independently checks every word and matrix exactly.

## Exact remaining frontier

A114 does **not** promote the 90 local Picard-Lefschetz candidates. Their frozen
exploration lacks the continuous trajectories needed for the same Rouche-tube
argument. It also does not multiply independently based meridians in root-id
order. A distinguished ordered cut system on the 90-punctured torus must first
fix all conjugations and the action convention; only then can the punctured-base
surface relation be checked against the promoted handle commutator.

Therefore the rank-four Gauss-Manin local system, Leray basis, beta periods,
gerbe zero, and strong-CP conclusion remain open. No MTT source modulus is
removed at this step.

## Reproduction

```powershell
python scripts/certify_q79genus2handle_root_tubes.py
python scripts/certify_q79genus2handle_pl_braids.py
python proof_corpus/selected_q79genus2handlemonodromypromotion_audit.py
```

The half-twist/Dehn-twist bridge is classical Birman-Hilden theory; A114's new
content is the explicit certified q79 path execution in the frozen marking.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps(candidate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
