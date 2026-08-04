from __future__ import annotations

import hashlib
import json
import math
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79hiddenbundleexistencebianchiallocationandspectrumexecution"
STATUS = (
    "MTT_U6_EXACT_MINIMAL_FUYAU_ALLOCATION_AND_STABLE_BUNDLES_CLOSED_"
    "FULL_HOLONOMY_AND_CHIRAL_VISIBLE_SOURCE_OPEN"
)
NEXT = "MTT_Selected_q79NonPullbackChiralVisibleBundleAndFullSU9HolonomySelection_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79HiddenBundleExistenceBianchiAllocationAndSpectrumExecution_v1.md"

E8_CARTAN = [
    [2, 0, -1, 0, 0, 0, 0, 0],
    [0, 2, 0, -1, 0, 0, 0, 0],
    [-1, 0, 2, -1, 0, 0, 0, 0],
    [0, -1, -1, 2, -1, 0, 0, 0],
    [0, 0, 0, -1, 2, -1, 0, 0],
    [0, 0, 0, 0, -1, 2, -1, 0],
    [0, 0, 0, 0, 0, -1, 2, -1],
    [0, 0, 0, 0, 0, 0, -1, 2],
]
HIGHEST_ROOT = [2, 3, 4, 6, 5, 4, 3, 2]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def determinant(matrix: list[list[int]]) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    result = Fraction(1)
    for column in range(len(work)):
        pivot = next(row for row in range(column, len(work)) if work[row][column])
        if pivot != column:
            work[pivot], work[column] = work[column], work[pivot]
            result *= -1
        scale = work[column][column]
        result *= scale
        for index in range(column, len(work)):
            work[column][index] /= scale
        for row in range(column + 1, len(work)):
            scale = work[row][column]
            for index in range(column, len(work)):
                work[row][index] -= scale * work[column][index]
    require(result.denominator == 1, "nonintegral determinant")
    return result.numerator


def mukai_square(vector: list[int]) -> int:
    rank, h_coefficient, degree_four = vector
    return 2 * h_coefficient**2 - 2 * rank * degree_four


def c2(vector: list[int]) -> int:
    rank, h_coefficient, degree_four = vector
    return rank + h_coefficient**2 - degree_four


def lattice_dot(left: list[int], right: list[int]) -> int:
    return sum(
        left[2 * block] * right[2 * block + 1]
        + left[2 * block + 1] * right[2 * block]
        for block in range(3)
    )


def main() -> int:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")],
        cwd=ROOT,
        check=True,
    )
    candidate = load(CANDIDATE)
    certificate = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    mukai = outputs["Mukai_repair"]
    bianchi = outputs["Bianchi_allocation"]
    bundles = outputs["stable_bundles"]
    hidden = outputs["hidden_embedding_spectrum"]
    chirality = outputs["visible_chirality_no_go"]
    frontier = outputs["U6_frontier"]

    require(candidate["status"] == certificate["status"] == STATUS, "A102 status changed")
    require(candidate["next_required_artifact"] == certificate["next_required_artifact"] == NEXT, "A102 next changed")
    require(all(candidate["checks"].values()), "one or more A102 checks failed")
    require(candidate["results"]["new_fitted_continuous_parameters"] == 0, "fitted parameter added")
    require(candidate["results"]["unfixed_reduced_bundle_moduli_complex_dimension"] == 76, "bundle moduli hidden")

    a = [5, 1, 0]
    b = [7, 3, 1]
    kernel = [3 * a[index] - b[index] for index in range(3)]
    repaired = [kernel[index] + [1, 0, -1][index] for index in range(3)]
    require(kernel == [8, 0, -1], "Mukai kernel arithmetic")
    require(repaired == [9, 0, -2], "Mukai repair arithmetic")
    require(c2(kernel) == 9 and mukai_square(kernel) == 16, "kernel invariants")
    require(c2(repaired) == 11 and mukai_square(repaired) == 36, "repair invariants")
    require(math.gcd(*repaired) == 1, "hidden repair not primitive")
    require(mukai["determinant_free_kernel"]["vector_3a_minus_b"] == kernel, "packet kernel changed")
    require(not mukai["source_guard"]["q7_to_point_ideal_source_map_in_corpus"], "q7 ideal map invented")

    h = bianchi["K3_lattice"]["polarization_h_in_U3_coordinates"]
    delta = bianchi["K3_lattice"]["primitive_ASD_class_delta_in_U3_coordinates"]
    require(lattice_dot(h, h) == 2, "polarization norm")
    require(lattice_dot(delta, delta) == -4, "ASD class norm")
    require(lattice_dot(h, delta) == 0, "ASD class not primitive to h")
    require(math.gcd(*delta) == 1, "ASD class not primitive")
    allocation = bianchi["source_free_Bianchi"]
    require(allocation["c2_visible_SU3"] + allocation["c2_hidden_SU9"] + allocation["torus_curvature_cost"] == 24, "Bianchi identity")
    require(allocation["residual"] == allocation["NS5_charge"] == 0, "source-free residual")
    require(not bianchi["source_guard"]["corpus_identifies_it_with_the_untwisted_FuYau_circle"], "shared circle overpromoted")

    visible = bundles["visible_SU3_bundle"]
    hidden_bundle = bundles["hidden_SU9_bundle"]
    require(visible["stable_locally_free_exists"] and visible["irreducible_HYM_exists"], "visible HYM existence")
    require(hidden_bundle["stable_locally_free_exists"] and hidden_bundle["irreducible_HYM_exists"], "hidden HYM existence")
    require(bundles["K3_stable_bundle_bound"]["visible"]["passes"], "rank-three bound")
    require(bundles["K3_stable_bundle_bound"]["hidden"]["passes"], "rank-nine bound")
    require(not bundles["selection_guard"]["visible_moduli_point_selected"], "visible modulus invented")
    require(not bundles["selection_guard"]["hidden_moduli_point_selected"], "hidden modulus invented")

    affine_pairings = [
        sum(E8_CARTAN[row][column] * HIGHEST_ROOT[column] for column in range(8))
        for row in range(8)
    ]
    require(affine_pairings == [0, 0, 0, 0, 0, 0, 0, 1], "affine E8 attachment")
    a8_gram = hidden["affine_E8_certificate"]["A8_Gram"]
    require(determinant(a8_gram) == 9, "A8 determinant")
    require(a8_gram == [[2 if i == j else -1 if abs(i - j) == 1 else 0 for j in range(8)] for i in range(8)], "A8 chain")
    require(hidden["E8_branching"]["dimension_check"] == 248, "E8 branching dimension")

    end0_c2 = 2 * 9 * 11
    wedge3_c2 = math.comb(7, 2) * 11
    end0_h1 = end0_c2 - 2 * 80
    wedge3_h1 = wedge3_c2 - 2 * 84
    total = end0_h1 + 2 * wedge3_h1
    require((end0_h1, wedge3_h1, total) == (38, 63, 164), "hidden cohomology arithmetic")
    require(total == 2 * (30 * 11 - 248), "E8 index mismatch")
    require(hidden["associated_bundle_index_spectrum"]["total_h1_adE8_if_full_holonomy"] == total, "hidden packet mismatch")
    require(not hidden["selection_guard"]["full_holonomy_selected_or_constructively_certified"], "full holonomy invented")

    require(chirality["K3_cohomology"]["V3"]["h1"] == 3, "visible K3 slots")
    require(chirality["K3_cohomology"]["V3_dual"]["h1"] == 3, "conjugate K3 slots")
    require(chirality["FuYau_pullback"]["c3"] == 0, "pullback c3")
    require(chirality["FuYau_pullback"]["net_chiral_27_index"] == 0, "pullback chirality overclaimed")
    require(chirality["required_visible_exit"]["required_integral_c3_for_three_net_families"] == [6, -6], "three-family c3 target")
    require(not chirality["required_visible_exit"]["selected_now"], "nonpullback bundle invented")

    progress = frontier["A101_hidden_payload_candidate_progress"]
    require(progress["candidate_filled"] == 6 and progress["selected_filled"] == 0, "candidate/selected typing drift")
    require(len(frontier["exact_remaining_cutset"]) == 4, "frontier cutset changed")
    require(not frontier["candidate_hidden_condensate_exit"]["selected_now"], "conditional condensate exit promoted")
    require(not frontier["U6_strong_CP_closed"], "U6 overclosed")

    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A102 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"authority hash mismatch: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in [
        "q79 Mukai kernel and repair",
        "Minimal rank-one Fu-Yau allocation",
        "9+11+4 = 24",
        "Stable HYM bundles exist",
        "248 = 80 + 84 + bar84",
        "total=164=2*(30*11-248)",
        "Visible chirality no-go",
        "stable non-pullback bundle",
        "complex reduced bundle-moduli directions remain unfixed",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print("A102 q79 hidden-bundle/Bianchi/spectrum audit: PASS")
    print(f"status={STATUS}")
    print("exact allocation=9+11+4=24; hidden index=38+63+63=164")
    print("selected hidden payload=0/8; pullback visible net chirality=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
