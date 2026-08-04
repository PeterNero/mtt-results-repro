from __future__ import annotations

import hashlib
import itertools
import json
import os
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
TEXPAPERS = Path(os.environ.get("MTT_TEXPAPERS_ROOT", ROOT.parent))
PROTO_ROOT = Path(
    os.environ.get(
        "MTT_PROTO_ROOT",
        TEXPAPERS / "mtt-protospinor-gr-response-proof",
    )
)

K3_BASE = (
    PROTO_ROOT
    / "certificates"
    / "q79_degree2_k3_fuyau_torsion_glsm_base_certificate.json"
)
PICARD = ROOT / "q79_k3_nodal_quartic_frobenius_bridge.packet.json"
GLOBAL_BK3 = (
    ROOT / "q79_bk3_transcendental_torus_closure_and_picard_cutset.packet.json"
)
OUT_PACKET = ROOT / "q79_k3_real_structure_bk3_kernel.packet.json"
OUT_NOTE = ROOT / "Q79_K3_REAL_STRUCTURE_BK3_KERNEL_v1.md"

CRITICAL_INTERVALS = (
    (sp.Rational(-1710, 1000), sp.Rational(-1709, 1000)),
    (sp.Rational(-403, 1000), sp.Rational(-402, 1000)),
    (sp.Rational(184, 1000), sp.Rational(185, 1000)),
    (sp.Rational(947, 1000), sp.Rational(948, 1000)),
    (sp.Rational(1423, 1000), sp.Rational(1424, 1000)),
    (sp.Rational(404883, 1000), sp.Rational(404884, 1000)),
)
FIBER_SAMPLES = (
    sp.Rational(-2),
    sp.Rational(-1),
    sp.Rational(0),
    sp.Rational(1, 2),
    sp.Rational(1),
    sp.Rational(2),
    sp.Rational(405),
)
EXPECTED_FIBER_COUNTS = (2, 0, 2, 0, 2, 0, 2)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_record(path: Path, repository: str, repository_root: Path) -> dict:
    return {
        "repository": repository,
        "relative_path": path.relative_to(repository_root).as_posix(),
        "sha256": sha256(path),
    }


def rational_record(value: sp.Rational) -> dict[str, int]:
    return {
        "numerator": int(value.p),
        "denominator": int(value.q),
    }


def interval_record(
    interval: tuple[sp.Rational, sp.Rational],
) -> list[dict[str, int]]:
    return [rational_record(interval[0]), rational_record(interval[1])]


def coefficient_list(poly: sp.Poly) -> list[int]:
    return [int(poly.nth(index)) for index in range(poly.degree() + 1)]


def normalized_primitive(poly: sp.Poly) -> tuple[int, sp.Poly]:
    content, primitive = poly.primitive()
    if primitive.LC() < 0:
        content = -content
        primitive = -primitive
    return int(content), primitive


def branch_polynomial(k3: dict) -> sp.Expr:
    x, y, z = sp.symbols("x y z")
    f6 = sp.expand(
        sp.sympify(
            k3["explicit_K3"]["F6_equals_G3_squared_plus_Q2_H4"]
        )
    )
    require(sp.Poly(f6, x, y, z).total_degree() == 6, "branch degree")
    require(
        k3["checks"]["plane_branch_sextic_is_projectively_smooth"],
        "source projective smoothness",
    )
    require(
        k3["explicit_K3"]["branch_smoothness_certificate"][
            "z_equals_1_groebner_basis"
        ]
        == ["1"],
        "source affine smoothness certificate",
    )
    return f6


def exact_projection_certificate(f6: sp.Expr) -> dict:
    x, y, z = sp.symbols("x y z")
    smoothness_charts = []
    for name, substitution, variables in (
        ("z_equals_1", {z: 1}, (x, y)),
        ("y_equals_1", {y: 1}, (x, z)),
        ("x_equals_1", {x: 1}, (y, z)),
    ):
        chart = sp.expand(f6.subs(substitution))
        basis = sp.groebner(
            [chart, *(sp.diff(chart, variable) for variable in variables)],
            *variables,
            order="grevlex",
            domain=sp.QQ,
        )
        basis_strings = [str(item.as_expr()) for item in basis.polys]
        require(basis_strings == ["1"], f"projective smoothness chart {name}")
        smoothness_charts.append(
            {
                "chart": name,
                "variables": [str(variable) for variable in variables],
                "jacobian_groebner_basis": basis_strings,
            }
        )

    affine = sp.Poly(sp.expand(f6.subs(z, 1)), y, x, domain=sp.ZZ)
    center_value = int(f6.subs({x: 0, y: 1, z: 0}))
    require(center_value != 0, "projection center off branch curve")
    require(affine.degree(y) == 6, "constant affine fiber degree")
    require(sp.Poly(affine.LC(), x).degree() == 0, "constant y-leading term")

    derivative = sp.diff(affine.as_expr(), y)
    raw_resultant = sp.Poly(
        sp.resultant(affine.as_expr(), derivative, y),
        x,
        domain=sp.ZZ,
    )
    content, critical = normalized_primitive(raw_resultant)
    require(critical.degree() == 30, "critical resultant degree")
    require(sp.gcd(critical, critical.diff()).degree() == 0, "squarefree resultant")
    require(
        critical.count_roots(-sp.oo, sp.oo) == 6,
        "six real critical values",
    )

    interval_rows = []
    for index, interval in enumerate(CRITICAL_INTERVALS, start=1):
        count = critical.count_roots(interval[0], interval[1])
        require(count == 1, f"critical isolating interval {index}")
        interval_rows.append(
            {
                "critical_index": index,
                "interval": interval_record(interval),
                "sturm_root_count": int(count),
            }
        )

    for index, sample in enumerate(FIBER_SAMPLES):
        if index:
            require(
                sample > CRITICAL_INTERVALS[index - 1][1],
                f"sample {index} above left critical interval",
            )
        if index < len(CRITICAL_INTERVALS):
            require(
                sample < CRITICAL_INTERVALS[index][0],
                f"sample {index} below right critical interval",
            )

    fiber_rows = []
    for index, (sample, expected) in enumerate(
        zip(FIBER_SAMPLES, EXPECTED_FIBER_COUNTS, strict=True)
    ):
        fiber = sp.Poly(
            affine.as_expr().subs(x, sample),
            y,
            domain=sp.QQ,
        )
        count = int(fiber.count_roots(-sp.oo, sp.oo))
        require(count == expected, f"fiber real-root count {index}")
        fiber_rows.append(
            {
                "interval_index": index,
                "sample_x": rational_record(sample),
                "real_branch_points_in_fiber": count,
            }
        )

    infinity = sp.Poly(
        sp.expand(f6.subs({x: 1, z: 0})),
        y,
        domain=sp.ZZ,
    )
    require(infinity.degree() == 6, "infinity fiber degree")
    require(sp.gcd(infinity, infinity.diff()).degree() == 0, "infinity squarefree")
    infinity_real_roots = int(infinity.count_roots(-sp.oo, sp.oo))
    require(infinity_real_roots == 2, "two real points at infinity")

    # The two bounded active bands each close through two simple folds. The
    # two tails meet both regular infinity points, producing one K_2,2 cycle.
    component_graphs = [
        {
            "name": "unbounded_affine_pair_projectively_closed",
            "vertices": ["critical_1", "critical_6", "infinity_1", "infinity_2"],
            "edges": [
                ["critical_1", "infinity_1"],
                ["critical_1", "infinity_2"],
                ["critical_6", "infinity_1"],
                ["critical_6", "infinity_2"],
            ],
            "connected_components": 1,
        },
        {
            "name": "bounded_oval_critical_2_to_3",
            "vertices": ["critical_2", "critical_3"],
            "edges": [
                ["critical_2", "critical_3", "lower_arc"],
                ["critical_2", "critical_3", "upper_arc"],
            ],
            "connected_components": 1,
        },
        {
            "name": "bounded_oval_critical_4_to_5",
            "vertices": ["critical_4", "critical_5"],
            "edges": [
                ["critical_4", "critical_5", "lower_arc"],
                ["critical_4", "critical_5", "upper_arc"],
            ],
            "connected_components": 1,
        },
    ]

    return {
        "projection": "[x:y:z] -> [x:z]",
        "projective_smoothness_charts": smoothness_charts,
        "projection_center": "[0:1:0]",
        "projection_center_branch_value": center_value,
        "affine_chart": "z=1",
        "affine_equation": str(affine.as_expr()),
        "affine_degree_in_y": affine.degree(y),
        "critical_value_resultant": {
            "raw_resultant_content": content,
            "primitive_coefficients_low_to_high": coefficient_list(critical),
            "degree": critical.degree(),
            "squarefree": True,
            "total_real_root_count": 6,
            "isolating_intervals": interval_rows,
        },
        "regular_fiber_counts": fiber_rows,
        "fiber_count_pattern": list(EXPECTED_FIBER_COUNTS),
        "infinity_fiber": {
            "equation": str(infinity.as_expr()),
            "coefficients_low_to_high": coefficient_list(infinity),
            "squarefree": True,
            "real_point_count": infinity_real_roots,
            "projection_critical_points": 0,
        },
        "simple_fold_reason": (
            "The branch curve is smooth, the y-degree is constant, and the "
            "critical-value resultant is squarefree. Hence each real "
            "critical value contains one real simple ramification point."
        ),
        "topology_graphs": component_graphs,
        "real_branch_components": 3,
        "all_components_are_ovals": True,
        "oval_reason": (
            "An even-degree smooth real plane curve has trivial mod-two "
            "homology class; disjoint pseudoline components cannot occur."
        ),
    }


def is_rooted_forest(parents: tuple[int, ...]) -> bool:
    for node in range(len(parents)):
        seen: set[int] = set()
        current = node
        while parents[current] != -1:
            current = parents[current]
            if current in seen:
                return False
            seen.add(current)
    return True


def possible_positive_region_euler_characteristics(
    oval_count: int,
) -> tuple[list[int], int]:
    values: set[int] = set()
    forest_count = 0
    parent_choices = range(-1, oval_count)
    for parents in itertools.product(parent_choices, repeat=oval_count):
        if any(parents[node] == node for node in range(oval_count)):
            continue
        if not is_rooted_forest(parents):
            continue
        forest_count += 1
        root_children = sum(parent == -1 for parent in parents)
        child_counts = [
            sum(parent == node for parent in parents)
            for node in range(oval_count)
        ]
        region_euler = [1 - root_children]
        region_euler.extend(1 - count for count in child_counts)

        depths = []
        for node in range(oval_count):
            depth = 1
            current = node
            while parents[current] != -1:
                depth += 1
                current = parents[current]
            depths.append(depth)

        for outside_positive in (False, True):
            total = region_euler[0] if outside_positive else 0
            for node, depth in enumerate(depths):
                positive = (
                    outside_positive and depth % 2 == 0
                ) or (
                    not outside_positive and depth % 2 == 1
                )
                if positive:
                    total += region_euler[node + 1]
            values.add(total)
    return sorted(values), forest_count


def real_structure_certificate(
    projection: dict,
    picard: dict,
    global_bk3: dict,
) -> dict:
    require(
        picard["status"] == "CLOSED_EXACT_GEOMETRIC_PICARD_RANK_TWO",
        "exact Picard predecessor",
    )
    exact = picard["exact_picard_rank_certificate"]
    require(exact["geometric_picard_rank"] == 2, "Picard rank two")
    require(exact["transcendental_rank"] == 20, "transcendental rank twenty")
    require(
        exact["geometric_Neron_Severi_lattice"]
        == "<H,delta>=diag(2,-4)",
        "exact Neron-Severi lattice",
    )
    require(
        global_bk3["compactness_and_kernel_theorem"][
            "rho_less_than_twenty"
        ]["kernel_rank"]
        == [0, 1],
        "predecessor kernel cutset",
    )

    oval_count = int(projection["real_branch_components"])
    possible_region_euler, forest_count = (
        possible_positive_region_euler_characteristics(oval_count)
    )
    require(
        possible_region_euler == [-2, -1, 0, 1, 2, 3],
        "three-oval region Euler possibilities",
    )
    real_k3_euler = [2 * value for value in possible_region_euler]
    h2_plus = [10 + value // 2 for value in real_k3_euler]
    require(h2_plus == [8, 9, 10, 11, 12, 13], "H2 plus dimensions")

    # Real divisor classes acquire a minus sign in Betti H^2 under an
    # antiholomorphic pullback (the codimension-one Tate twist).
    ns_minus_dimension = 2
    transcendental_pairs = [
        {
            "chi_X_real": chi,
            "H2_plus_dimension": plus,
            "H2_minus_dimension": 22 - plus,
            "T_plus_dimension": plus,
            "T_minus_dimension": 20 - plus,
        }
        for chi, plus in zip(real_k3_euler, h2_plus, strict=True)
    ]
    allocation_independent_pairs = sorted(
        {
            (plus - ns_plus, 20 - (plus - ns_plus))
            for plus in h2_plus
            for ns_plus in range(3)
        }
    )
    require(
        all(
            row["T_plus_dimension"] not in (1, 19)
            and row["T_minus_dimension"] not in (1, 19)
            for row in transcendental_pairs
        ),
        "nonextreme transcendental conjugation eigenspaces",
    )
    require(
        all(plus not in (1, 19) and minus not in (1, 19)
            for plus, minus in allocation_independent_pairs),
        "allocation-independent nonextreme eigenspaces",
    )

    return {
        "real_double_plane": {
            "real_locus_projection": (
                "X(R) -> R_plus={p in RP2:F6(p)>=0}"
            ),
            "covering_multiplicity": "two on the interior, one on the branch",
            "branch_euler_characteristic": 0,
            "formula": "chi(X(R))=2*chi(R_plus)",
        },
        "three_oval_nesting_exhaustion": {
            "labeled_rooted_forests_checked": forest_count,
            "possible_chi_R_plus": possible_region_euler,
            "possible_chi_X_real": real_k3_euler,
        },
        "real_lefschetz": {
            "formula": "chi(X(R))=2+tr(c*|H2)",
            "possible_H2_plus_dimensions": h2_plus,
            "possible_H2_minus_dimensions": [
                22 - value for value in h2_plus
            ],
        },
        "Neron_Severi_real_action": {
            "real_divisor_classes": ["H", "delta"],
            "antiholomorphic_pullback_eigenvalue": -1,
            "NS_plus_dimension": 0,
            "NS_minus_dimension": ns_minus_dimension,
            "reason": (
                "Both divisors are defined by real equations; on a real "
                "codimension-one cycle, antiholomorphic pullback contributes "
                "the Betti Tate-twist sign -1."
            ),
        },
        "transcendental_conjugation_possibilities": transcendental_pairs,
        "allocation_independent_check": {
            "allowed_NS_plus_dimensions": [0, 1, 2],
            "possible_T_eigenspace_pairs": [
                list(pair) for pair in allocation_independent_pairs
            ],
            "rank_one_extremes_absent_without_using_divisor_sign": True,
        },
        "rank_one_resonance_obstruction": {
            "kernel_lattice": (
                "Lambda_b=W intersect (H2(K3,Z)+R*delta), "
                "W=span_R{Re(Omega),Im(Omega)}"
            ),
            "rational_reduction": (
                "Pairing with delta^2=-4 shows every kernel vector lies in "
                "W intersect H2(K3,Q); multiplying by four makes it integral."
            ),
            "conjugation_invariance": (
                "If rank Lambda_b=1, its rational line is c*-stable and its "
                "generator has eigenvalue +1 or -1."
            ),
            "simple_Hodge_structure_lemma": (
                "T_Q is simple: a proper rational Hodge substructure would "
                "either miss H20 and be algebraic, or contain H20 and have "
                "an algebraic orthogonal complement."
            ),
            "reflection_argument": (
                "For a rational kernel generator v, its rational reflection "
                "s_v is anti-Hodge. If c(v)=v, s_v*c is Hodge and acts as "
                "-1 on H20, hence equals -Id_T and forces eigendimensions "
                "(T+,T-)=(1,19). If c(v)=-v, s_v*c acts as +1 on H20, hence "
                "equals Id_T and forces (T+,T-)=(19,1)."
            ),
            "rank_one_forced_pairs": [[1, 19], [19, 1]],
            "observed_possible_pairs": [
                [row["T_plus_dimension"], row["T_minus_dimension"]]
                for row in transcendental_pairs
            ],
            "allocation_independent_possible_pairs": [
                list(pair) for pair in allocation_independent_pairs
            ],
            "rank_one_excluded": True,
        },
        "large_gauge_immersion_kernel_rank": 0,
        "period_matrix_needed_for_kernel_rank": False,
        "period_matrix_still_needed_for": [
            "preferred coordinate normalization",
            "kinetic scale and decay constants",
            "explicit transcendental period values",
        ],
    }


def write_note(packet: dict) -> None:
    projection = packet["real_branch_projection_certificate"]
    real = packet["real_structure_and_kernel_certificate"]
    note = f"""# q79 K3 real structure and rank-zero b_K3 kernel

## Result

The selected q79 degree-two K3 has

`rho=2`, `NS(X_Qbar)=diag(2,-4)`, and `rank T(X)=20`.

The remaining global `b_K3` ambiguity was whether its large-gauge kernel had
rank zero or one. This packet proves

`rank Lambda_b=0`.

Thus the map from the two real `b_K3` parameters is injective, while its image
is dense and nonclosed in the compact transcendental `T20` already selected
by the Picard theorem.

## Exact real-sextic topology

Project the real branch sextic by `[x:y:z] -> [x:z]`. The projection center
is not on the curve. The exact critical-value resultant has degree
`{projection["critical_value_resultant"]["degree"]}`, is squarefree, and has
exactly `{projection["critical_value_resultant"]["total_real_root_count"]}`
real roots. Exact Sturm counts on the seven complementary intervals give

`{projection["fiber_count_pattern"]}`.

The fiber at infinity is squarefree and has exactly two real points. The two
bounded active bands form two ovals; the two tails and the two regular
infinity points form one further oval. Hence the real branch curve has
exactly three components.

For every possible nesting of three ovals and either outside sign,

`chi(R_plus) in {real["three_oval_nesting_exhaustion"]["possible_chi_R_plus"]}`,

so

`chi(X(R)) in {real["three_oval_nesting_exhaustion"]["possible_chi_X_real"]}`.

## Conjugation obstruction

The real Lefschetz formula gives the possible dimensions

`dim H2_+ in {real["real_lefschetz"]["possible_H2_plus_dimensions"]}`.

The real divisor classes `H` and `delta` lie in the minus eigenspace of the
antiholomorphic pullback, leaving the possible transcendental signatures

`{real["rank_one_resonance_obstruction"]["observed_possible_pairs"]}`.

If a rank-one `b_K3` kernel existed, its rational generator would be a
conjugation eigenvector. Reflection in that vector, composed with
conjugation, is a rational Hodge endomorphism of the simple transcendental
K3 Hodge structure. It would force the signature to be `(1,19)` or `(19,1)`.
Neither occurs. Rank one is impossible, and rank two was already excluded by
`rho=2`; therefore the kernel has rank zero.

## Consequence and boundary

Numerical periods are no longer required to decide the global kernel
topology. They remain necessary for preferred normalization, kinetic scales,
and explicit period values. This theorem does not construct the physical
non-pullback Hull-Strominger endpoint or the selected shared-circle upper
action, and it has no bearing on the separate eta9 object named `F0`.

## References

- D. Huybrechts, *Complex and real multiplication for K3 surfaces*:
  https://www.math.uni-bonn.de/people/huybrech/Transcent.pdf
- V. Kharlamov, *Overview of topological properties of real algebraic
  surfaces*: https://arxiv.org/abs/math/0502127
- V. Nikulin and S. Saito, *Real K3 surfaces with non-symplectic
  involutions and applications*: https://arxiv.org/abs/math/0312396
"""
    OUT_NOTE.write_text(note, encoding="utf-8")


def main() -> int:
    k3 = load(K3_BASE)
    picard = load(PICARD)
    global_bk3 = load(GLOBAL_BK3)
    f6 = branch_polynomial(k3)
    projection = exact_projection_certificate(f6)
    real_structure = real_structure_certificate(
        projection,
        picard,
        global_bk3,
    )

    packet = {
        "schema": "q79K3RealStructureBK3Kernel.v1",
        "status": "CLOSED_EXACT_BK3_LARGE_GAUGE_KERNEL_RANK_ZERO",
        "sources": {
            "selected_k3": source_record(
                K3_BASE,
                "mtt-protospinor-gr-response-proof",
                PROTO_ROOT,
            ),
            "exact_picard": source_record(
                PICARD,
                "mtt-mathematical-language-discovery-program",
                ROOT,
            ),
            "global_b_K3_cutset": source_record(
                GLOBAL_BK3,
                "mtt-mathematical-language-discovery-program",
                ROOT,
            ),
        },
        "real_branch_projection_certificate": projection,
        "real_structure_and_kernel_certificate": real_structure,
        "global_b_K3_conclusion": {
            "parameter_group": "R^2",
            "large_gauge_kernel": "{0}",
            "kernel_rank": 0,
            "map_type": "injective immersed homomorphism",
            "image": "dense nonclosed subgroup of compact T20",
            "closure": "compact transcendental T20",
            "new_fitted_continuous_parameters": 0,
        },
        "primary_references": {
            "transcendental_K3_Hodge_structure": (
                "https://www.math.uni-bonn.de/people/huybrech/Transcent.pdf"
            ),
            "real_algebraic_surface_topology": (
                "https://arxiv.org/abs/math/0502127"
            ),
            "real_K3_lattice_involutions": (
                "https://arxiv.org/abs/math/0312396"
            ),
        },
        "theorem": {
            "name": "q79K3RealStructureRankZeroBK3KernelTheorem",
            "statement": (
                "For the selected real q79 double-sextic K3, the exact "
                "three-oval branch topology bounds the complex-conjugation "
                "eigenspaces on the rank-20 transcendental lattice away from "
                "(1,19) and (19,1). Simplicity of the transcendental K3 Hodge "
                "structure and a rational-reflection argument show that any "
                "rank-one rational period resonance would force one of those "
                "two extreme signatures. Hence the b_K3 large-gauge kernel "
                "has rank zero."
            ),
            "tier": "CLOSED_EXACT_GLOBAL_TOPOLOGICAL_AND_HODGE_THEOREM",
            "does_not_claim": [
                "explicit numerical K3 periods",
                "a kinetic normalization or decay constant",
                "the physical non-pullback Hull-Strominger endpoint",
                "the selected shared-circle upper action",
                "any update to the unrelated eta9 F0 lift",
            ],
        },
        "frontier_delta": {
            "before": (
                "rho=2 and the b_K3 image was dense in T20, but its "
                "large-gauge kernel still had rank 0 or 1."
            ),
            "after": (
                "The large-gauge kernel has rank zero exactly; the b_K3 "
                "R2 parametrization is injective with dense nonclosed image "
                "in the compact transcendental T20."
            ),
            "next": (
                "Construct the selected shared-circle action intertwiner; "
                "period numerics are optional for normalization rather than "
                "needed for the kernel decision."
            ),
        },
    }
    OUT_PACKET.write_text(
        json.dumps(packet, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_note(packet)
    print("Q79_K3_REAL_STRUCTURE_BK3_KERNEL_BUILD_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
