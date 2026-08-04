from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2normalfunctionbetaandintegralbranchexecution.candidate.json"
)
CERTIFICATE = (
    ROOT
    / "certificates"
    / "selected_q79genus2normalfunctionbetaandintegralbranchexecution.certificate.json"
)
OUT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2normalfunctionbetaandintegralbranchexecution"
)
AFFINE = OUT / "complete_affine_normal_function_cocycle.packet.json"
CONVERGENCE = OUT / "normal_function_floating_convergence.packet.json"
BETA_OPEN = OUT / "beta_period_and_integral_branch.open.json"
FRONTIER = OUT / "U6_frontier_after_A120.packet.json"
FACTORIZATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedcutsystemandglobalrelation"
    / "global_integral_gauss_manin_factorization.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def compose(
    second: tuple[sp.Matrix, sp.Matrix],
    first: tuple[sp.Matrix, sp.Matrix],
) -> tuple[sp.Matrix, sp.Matrix]:
    return (
        second[0] * first[0],
        second[0] * first[1] + second[1],
    )


def inverse(
    pair: tuple[sp.Matrix, sp.Matrix],
) -> tuple[sp.Matrix, sp.Matrix]:
    matrix_inverse = pair[0].inv()
    return matrix_inverse, -matrix_inverse * pair[1]


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    affine = load(AFFINE)
    convergence = load(CONVERGENCE)
    beta_open = load(BETA_OPEN)
    frontier = load(FRONTIER)
    factorization = load(FACTORIZATION)

    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash")
    for authority in candidate["authority_hashes"]:
        path = ROOT / authority["path"]
        require(path.exists(), f"missing authority {path}")
        require(sha256(path) == authority["sha256"], f"authority hash {path}")

    require(
        affine["exact_mumford_source"]["all_exact_checks_pass"],
        "Mumford source",
    )
    rows = affine["local_rows"]
    require(len(rows) == 90, "local row count")
    require(
        [row["distinguished_index"] for row in rows] == list(range(1, 91)),
        "local row order",
    )
    require(affine["direct_rows"] == 88, "direct row count")
    require(
        affine["relation_completed_rows"] == [43, 45],
        "relation-completed rows",
    )
    require(
        affine["affine_surface_relation"]["unique_integer_solution"]
        == {"m43": 1, "m45": 0},
        "hard-node solution",
    )
    require(
        float(affine["maximum_direct_coordinate_rounding_error"]) < 2.7e-6,
        "direct coordinate fit",
    )

    factors = factorization["factors"]
    product = (sp.eye(4), sp.zeros(4, 1))
    for row, factor in zip(rows, factors):
        vanishing = sp.Matrix(row["positive_vanishing_cycle_up_to_sign"])
        translation = sp.Matrix(row["integer_translation"])
        require(
            translation == row["translation_multiplier"] * vanishing,
            f"PL translation {row['distinguished_index']}",
        )
        product = compose(
            (
                sp.Matrix(factor["positive_picard_lefschetz_matrix"]),
                translation,
            ),
            product,
        )

    handle_data = affine["physical_handle_lifts"]
    require(handle_data["A"] == "+A_braid", "A lift")
    require(handle_data["B"] == "-B_braid", "B lift")
    handle_a = (
        sp.Matrix(factorization["handle_actions"]["A"]),
        sp.Matrix(handle_data["A_translation"]),
    )
    handle_b = (
        -sp.Matrix(factorization["handle_actions"]["B"]),
        sp.Matrix(handle_data["B_translation"]),
    )
    boundary = compose(
        inverse(handle_b),
        compose(inverse(handle_a), compose(handle_b, handle_a)),
    )
    require(product == boundary, "exact affine surface relation")
    require(
        list(boundary[1]) == [7, 6, -4, 7],
        "boundary translation",
    )

    c = sp.Matrix(sp.symbols("c0:4"))
    equations = []
    for row, factor in zip(rows, factors):
        matrix = sp.Matrix(factor["positive_picard_lefschetz_matrix"])
        equations.extend(
            list((matrix - sp.eye(4)) * c - sp.Matrix(row["integer_translation"]))
        )
    equations.extend(list((handle_a[0] - sp.eye(4)) * c - handle_a[1]))
    equations.extend(list((handle_b[0] - sp.eye(4)) * c - handle_b[1]))
    require(sp.linsolve(equations, list(c)) == sp.EmptySet, "global cocycle")
    require(
        affine["cohomology"]["all_local_singularity_classes_zero"],
        "local admissibility",
    )
    require(
        affine["cohomology"]["global_cocycle_nontrivial"],
        "global class",
    )

    require(
        convergence["strict_scope"]["two_run_floating_check"],
        "two-run convergence",
    )
    require(
        not convergence["strict_scope"]["interval_enclosure"],
        "interval overclaim",
    )
    require(
        beta_open["guard"]["affine_monodromy_is_not_itself_z_8"],
        "beta guard",
    )
    require(
        frontier["normal_function_local_translations_selected"] == 90,
        "frontier local rows",
    )
    require(
        frontier["Deligne_beta_C_period_rows_emitted"] == 0,
        "beta rows invented",
    )
    require(
        not frontier["integral_period_branch_selected"],
        "integral branch invented",
    )
    require(
        not frontier["gerbe_zero_or_no_go_executed"],
        "gerbe decision invented",
    )
    require(candidate["checks"]["affine_surface_relation_exact"], "candidate relation")
    require(certificate["complete_affine_normal_function_cocycle_closed"], "certificate cocycle")
    require(not certificate["Deligne_beta_period_closed"], "certificate beta overclaim")
    print("q79 A120 normal-function affine cocycle audit: PASS")
    print("closed: exact Mumford source, 90 local translations, A/B translations")
    print("exact affine boundary translation: [7, 6, -4, 7]")
    print("open: Deligne z_8, integral H2 branch, beta_C zero/no-go")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
