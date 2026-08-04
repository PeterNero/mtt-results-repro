from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
from decimal import Decimal, localcontext
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2criticalvalueandnodeisolation"
STATUS = "MTT_U6_Q79_90_CRITICAL_VALUES_AND_NODAL_POINTS_CERTIFIED_MONODROMY_PATHS_OPEN"
NEXT = "MTT_Selected_q79GenusTwoPicardLefschetzMonodromyExecution_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79GenusTwoCriticalValueAndNodeIsolation_v1.md"

MPS_INPUT = OUT / "N90_exact_integer.mpsolve.pol"
MPS_RAW = OUT / "N90_mpsolve_isolated.full.txt"
ROOTS = OUT / "N90_certified_root_disks.packet.json"
NODES = OUT / "exact_critical_value_and_nodal_point_lifts.packet.json"
MONODROMY = OUT / "Picard_Lefschetz_monodromy_execution.open.json"
FRONTIER = OUT / "U6_frontier_after_A112.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def windows_to_wsl(path: Path) -> str:
    absolute = path.resolve()
    drive = absolute.drive.rstrip(":").lower()
    tail = str(absolute)[len(absolute.drive) :].lstrip("\\/").replace("\\", "/")
    return f"/mnt/{drive}/{tail}"


def run_mpsolve(input_path: Path) -> tuple[str, str, str, list[str]]:
    native = shutil.which("mpsolve")
    if native:
        version_command = [native, "-v"]
        command = [native, "-G", "i", "-o", "30", "-Of", "-j", "1", str(input_path)]
        mode = "native"
    else:
        wsl = shutil.which("wsl")
        if not wsl:
            raise RuntimeError(
                "MPSolve is required for A112. Install mpsolve 3.2.3 natively or in WSL."
            )
        version_command = [wsl, "mpsolve", "-v"]
        command = [
            wsl,
            "mpsolve",
            "-G",
            "i",
            "-o",
            "30",
            "-Of",
            "-j",
            "1",
            windows_to_wsl(input_path),
        ]
        mode = "wsl"

    version = subprocess.run(
        version_command, capture_output=True, text=True, check=True
    ).stdout.strip()
    completed = subprocess.run(command, capture_output=True, text=True, check=True)
    if completed.stderr.strip():
        raise RuntimeError(f"MPSolve stderr was nonempty: {completed.stderr}")
    return mode, version, completed.stdout, command


def parse_mpsolve_full(output: str) -> list[dict]:
    lines = [line.strip() for line in output.splitlines() if line.strip()]
    if len(lines) % 3:
        raise ValueError("unexpected MPSolve full-output block count")

    roots = []
    center_pattern = re.compile(r"\(([^,]+),\s*([^\)]+)\)")
    for offset in range(0, len(lines), 3):
        center_match = center_pattern.fullmatch(lines[offset])
        if not center_match:
            raise ValueError(f"invalid MPSolve center: {lines[offset]}")
        radius_mantissa, radius_exponent = lines[offset + 1].split("x")
        radius = Decimal(radius_mantissa) * (Decimal(10) ** int(radius_exponent))
        real = Decimal(center_match.group(1))
        imaginary = Decimal(center_match.group(2))
        status = lines[offset + 2]
        roots.append(
            {
                "center_real": str(real),
                "center_imaginary": str(imaginary),
                "radius": str(radius),
                "status": status,
                "intersects_real_axis": abs(imaginary) <= radius,
            }
        )

    roots.sort(key=lambda item: (Decimal(item["center_real"]), Decimal(item["center_imaginary"])))
    for index, root in enumerate(roots, start=1):
        root["root_id"] = f"a{index:02d}"
    return roots


def pairwise_disk_certificate(roots: list[dict]) -> dict:
    minimum_margin = None
    pair_count = 0
    with localcontext() as context:
        context.prec = 100
        for left_index, left in enumerate(roots):
            left_real = Decimal(left["center_real"])
            left_imaginary = Decimal(left["center_imaginary"])
            left_radius = Decimal(left["radius"])
            for right in roots[left_index + 1 :]:
                right_real = Decimal(right["center_real"])
                right_imaginary = Decimal(right["center_imaginary"])
                right_radius = Decimal(right["radius"])
                distance_squared = (left_real - right_real) ** 2 + (
                    left_imaginary - right_imaginary
                ) ** 2
                radius_squared = (left_radius + right_radius) ** 2
                margin = distance_squared - radius_squared
                if margin <= 0:
                    raise AssertionError("MPSolve inclusion disks overlap")
                minimum_margin = margin if minimum_margin is None else min(minimum_margin, margin)
                pair_count += 1

    conjugate_matched = 0
    for root in roots:
        real = Decimal(root["center_real"])
        imaginary = Decimal(root["center_imaginary"])
        radius = Decimal(root["radius"])
        if root["intersects_real_axis"]:
            continue
        for other in roots:
            if other is root:
                continue
            other_real = Decimal(other["center_real"])
            other_imaginary = Decimal(other["center_imaginary"])
            other_radius = Decimal(other["radius"])
            tolerance = radius + other_radius
            if abs(real - other_real) <= tolerance and abs(imaginary + other_imaginary) <= tolerance:
                conjugate_matched += 1
                break

    return {
        "pair_count": pair_count,
        "all_pairwise_disjoint": True,
        "minimum_squared_separation_margin": str(minimum_margin),
        "real_axis_disk_count": sum(item["intersects_real_axis"] for item in roots),
        "nonreal_disk_count": sum(not item["intersects_real_axis"] for item in roots),
        "nonreal_disks_with_conjugate_match": conjugate_matched,
        "conjugate_pair_count": conjugate_matched // 2,
        "maximum_radius": str(max(Decimal(item["radius"]) for item in roots)),
    }


def main() -> int:
    paths = {
        "A106_period": ROOT
        / "candidate_data"
        / "selected_q79pgl3toprymgerbejacobianexecution"
        / "residue_period_Jacobian_formula.packet.json",
        "A111_fibration": ROOT
        / "candidate_data"
        / "selected_q79genus2lefschetzperiodreduction"
        / "explicit_genus2_fibration.packet.json",
        "A111_discriminant": ROOT
        / "candidate_data"
        / "selected_q79genus2lefschetzperiodreduction"
        / "degree90_nodal_discriminant_certificate.packet.json",
        "A111_prym": ROOT
        / "candidate_data"
        / "selected_q79genus2lefschetzperiodreduction"
        / "explicit_prym_residues_and_delta_normal_function.packet.json",
        "A111_frontier": ROOT
        / "candidate_data"
        / "selected_q79genus2lefschetzperiodreduction"
        / "U6_frontier_after_A111.packet.json",
    }
    for path in paths.values():
        assert path.exists(), path

    period106 = load(paths["A106_period"])
    fibration111 = load(paths["A111_fibration"])
    discriminant111 = load(paths["A111_discriminant"])
    prym111 = load(paths["A111_prym"])
    frontier111 = load(paths["A111_frontier"])

    assert discriminant111["consequences"]["distinct_discriminant_points_on_E"] == 90
    assert discriminant111["norm_certificate"]["gcd_N90_derivative"] == "1"
    assert prym111["residue_forms"]["trace_free_form_count"] == 8
    assert frontier111["beta_C_period_rows_emitted"] == 0

    coefficients_descending = discriminant111["norm_certificate"][
        "coefficients_descending"
    ]
    assert len(coefficients_descending) == 91
    input_text = "dri\n0\n90\n" + "\n".join(
        str(coefficient) for coefficient in reversed(coefficients_descending)
    ) + "\n"
    MPS_INPUT.parent.mkdir(parents=True, exist_ok=True)
    MPS_INPUT.write_text(input_text, encoding="ascii")
    solver_mode, solver_version, raw_output, solver_command = run_mpsolve(MPS_INPUT)
    MPS_RAW.write_text(raw_output, encoding="ascii")

    roots = parse_mpsolve_full(raw_output)
    disk_checks = pairwise_disk_certificate(roots)
    assert len(roots) == 90
    assert all(root["status"] == "Status: Isolated, None, In" for root in roots)
    assert disk_checks["pair_count"] == 4005
    assert disk_checks["real_axis_disk_count"] == 8
    assert disk_checks["nonreal_disk_count"] == 82
    assert disk_checks["conjugate_pair_count"] == 41

    a, b, t = sp.symbols("a b t")
    n90 = sp.Poly.from_list(coefficients_descending, gens=a, domain=sp.ZZ)
    real_intervals = n90.intervals(eps=sp.Rational(1, 10**12))
    assert len(real_intervals) == 8
    assert all(multiplicity == 1 for _interval, multiplicity in real_intervals)

    root_packet = {
        "schema": "MTTQ79N90CertifiedRootDisks.v1",
        "status": "ALL_90_N90_ROOTS_ISOLATED_WITH_GUARANTEED_DISJOINT_INCLUSION_DISKS",
        "solver": {
            "name": "MPSolve",
            "version": solver_version,
            "execution_mode": solver_mode,
            "goal": "isolate",
            "requested_output_digits": 30,
            "threads": 1,
            "command_shape": [
                Path(solver_command[0]).name,
                "mpsolve" if solver_mode == "wsl" else "-G",
                "-G i -o 30 -Of -j 1",
                str(MPS_INPUT.relative_to(ROOT)).replace("\\", "/"),
            ],
            "official_semantics": "For exact integer input and goal isolate, each Status: Isolated output disk contains one root; the displayed error bound is its guaranteed inclusion radius.",
        },
        "input": {
            "degree": 90,
            "coefficient_count": len(coefficients_descending),
            "format": "dense real integer, coefficients in increasing degree",
            "path": str(MPS_INPUT.relative_to(ROOT)).replace("\\", "/"),
            "sha256": sha256(MPS_INPUT),
            "A111_N90_expression_sha256": discriminant111["norm_certificate"][
                "sha256_of_expanded_expression"
            ],
        },
        "raw_output": {
            "path": str(MPS_RAW.relative_to(ROOT)).replace("\\", "/"),
            "sha256": sha256(MPS_RAW),
        },
        "root_disks": roots,
        "disk_checks": disk_checks,
        "exact_real_root_intervals": [
            {
                "left": str(interval[0]),
                "right": str(interval[1]),
                "multiplicity": multiplicity,
            }
            for interval, multiplicity in real_intervals
        ],
        "theorem": {
            "name": "Q79N90CertifiedCriticalValueIsolationTheorem",
            "proved": True,
            "statement": "MPSolve isolates all 90 roots of the exact square-free integer N90 in pairwise disjoint guaranteed disks. Eight disks meet the real axis and exact Sturm intervals certify the eight simple real roots; the remaining 82 disks form 41 conjugate pairs.",
        },
    }

    f_ab = sp.sympify(
        fibration111["fiber_chart"]["equation"].split("=", 1)[1],
        locals={"a": a, "b": b, "t": t},
    )
    subresultants = sp.subresultants(f_ab, sp.diff(f_ab, t), t)
    assert [sp.degree(item, t) for item in subresultants] == [6, 5, 4, 3, 2, 1, 0]
    s1 = sp.Poly(subresultants[-2], t)
    elliptic_polynomial = sp.Poly(b**2 - a**3 + a, b, domain=sp.QQ[a])

    def reduce_on_e(expression: sp.Expr) -> sp.Expr:
        return sp.rem(
            sp.Poly(sp.expand(expression), b, domain=sp.QQ[a]), elliptic_polynomial
        ).as_expr()

    c1 = sp.expand(reduce_on_e(s1.coeff_monomial(t)))
    c0 = sp.expand(reduce_on_e(s1.coeff_monomial(1)))
    assert sp.degree(c1, b) == sp.degree(c0, b) == 1

    p45 = sp.sympify(discriminant111["discriminant_on_E"]["P45"], locals={"a": a})
    q43 = sp.sympify(discriminant111["discriminant_on_E"]["Q43"], locals={"a": a})
    c1_poly_b = sp.Poly(c1, b)
    c1_constant = c1_poly_b.coeff_monomial(1)
    c1_b = c1_poly_b.coeff_monomial(b)
    c1_on_critical_numerator = sp.expand(c1_constant * q43 - c1_b * p45)
    c1_nonzero_gcd = sp.gcd(n90, sp.Poly(c1_on_critical_numerator, a, domain=sp.QQ))
    assert c1_nonzero_gcd.as_expr() == 1

    node_packet = {
        "schema": "MTTQ79ExactCriticalValueAndNodalPointLifts.v1",
        "status": "ALL_90_ELLIPTIC_CRITICAL_VALUES_AND_FIBER_NODES_ALGEBRAICALLY_LIFTED",
        "critical_value_lift": {
            "a_j": "the unique N90 root in certified disk D_j",
            "b_j": "-P45(a_j)/Q43(a_j)",
            "Q43_nonzero_reason": "gcd(P45,Q43)=1 and N90(a_j)=0, so Q43(a_j)=0 would force P45(a_j)=0, impossible",
            "elliptic_equation": "b_j^2=a_j^3-a_j follows from N90(a_j)=0",
            "discriminant_equation": "P45(a_j)+b_j*Q43(a_j)=0",
            "unique_lift_per_a_root": True,
            "critical_value_count": 90,
        },
        "degree_one_subresultant": {
            "formula": "S1_red(a,b,t)=c1(a,b)*t+c0(a,b)",
            "c1": str(c1),
            "c0": str(c0),
            "c1_term_count": len(sp.Poly(c1, a, b).terms()),
            "c0_term_count": len(sp.Poly(c0, a, b).terms()),
            "c1_sha256": hashlib.sha256(str(c1).encode("ascii")).hexdigest(),
            "c0_sha256": hashlib.sha256(str(c0).encode("ascii")).hexdigest(),
            "c1_on_critical_numerator_degree": int(
                sp.degree(c1_on_critical_numerator, a)
            ),
            "c1_on_critical_numerator_sha256": hashlib.sha256(
                str(c1_on_critical_numerator).encode("ascii")
            ).hexdigest(),
            "gcd_N90_c1_on_critical_numerator": str(c1_nonzero_gcd.as_expr()),
        },
        "nodal_point_lift": {
            "t_j": "-c0(a_j,b_j)/c1(a_j,b_j)",
            "u_j": 0,
            "c1_nonzero_at_every_critical_value": True,
            "subresultant_reason": "At a simple discriminant point gcd(f_ab,d_t f_ab) has degree one and is generated by S1_red; therefore t_j is the unique double root.",
            "node_count": 90,
        },
        "exact_objects": [
            {
                "root_id": root["root_id"],
                "a": f"RootOf(N90,{root['root_id']}_disk)",
                "b": f"-P45(a)/Q43(a) at {root['root_id']}",
                "t": f"-c0(a,b)/c1(a,b) at {root['root_id']}",
                "u": 0,
            }
            for root in roots
        ],
        "theorem": {
            "name": "Q79ExactCriticalValueAndNodeLiftTheorem",
            "proved": True,
            "statement": "Every isolated N90 root has one and only one lift to the elliptic discriminant. The reduced degree-one subresultant has nonzero leading coefficient at all 90 lifts, so it gives the unique double root and hence the exact nodal point (a_j,b_j,t_j,0) on each singular fiber.",
        },
    }

    monodromy_open = {
        "schema": "MTTQ79PicardLefschetzMonodromyExecutionInput.v1",
        "status": "OPEN_CERTIFIED_PATHS_VANISHING_CYCLES_AND_INTEGRAL_MONODROMY",
        "closed_input": {
            "critical_value_disks": str(ROOTS.relative_to(ROOT)).replace("\\", "/"),
            "exact_critical_and_node_lifts": str(NODES.relative_to(ROOT)).replace("\\", "/"),
            "critical_values": 90,
            "nodes": 90,
            "fiber_H1_rank": 4,
            "surface_H2_target_rank": 92,
            "Prym_residue_rows": 8,
        },
        "open": {
            "regular_basepoint_e0": None,
            "six_ordered_branch_points_of_f_e0": None,
            "symplectic_H1_basis": None,
            "certified_nonintersecting_base_paths_to_90_disks": None,
            "colliding_branch_pair_per_path": None,
            "90_integral_vanishing_cycles_in_Z4": None,
            "90_Picard_Lefschetz_transvections_Sp4Z": None,
            "two_elliptic_base_monodromies": None,
            "integral_H2_basis_rank92": None,
        },
        "acceptance": {
            "integral_monodromy_closed": False,
            "H2_basis_closed": False,
            "beta_C_period_rows_emitted": 0,
            "beta_C_zero_proved": False,
            "beta_C_nonzero_proved": False,
        },
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA112.v1",
        "status": STATUS,
        "closed_now": [
            "exact MPSolve integer input for N90",
            "90 guaranteed pairwise-disjoint isolated root disks",
            "8 exact real-root intervals and 41 nonreal conjugate pairs",
            "unique algebraic lift of every a root to E_i",
            "reduced degree-one subresultant for every fiber double root",
            "90 exact nodal points (a_j,b_j,t_j,0)",
        ],
        "critical_values_closed": 90,
        "nodal_points_closed": 90,
        "monodromy_matrices_closed": 0,
        "beta_C_period_rows_emitted": 0,
        "actual_exact_gerbe_zero": False,
        "trial_tau_i_and_identity_alignment_selected": False,
        "strict_MTT_source_moduli_removed": 0,
        "observed_or_fitted_physics_parameters_added": 0,
        "U6_strong_CP_closed": False,
        "next_exact_target": "Choose a regular fiber and certified path tree in E_i minus the 90 disks, identify each colliding branch pair, and emit the 90 integral Sp4(Z) Picard-Lefschetz transvections.",
        "next_required_artifact": NEXT,
    }

    outputs = {
        "certified_root_disks": str(ROOTS.relative_to(ROOT)).replace("\\", "/"),
        "critical_and_node_lifts": str(NODES.relative_to(ROOT)).replace("\\", "/"),
        "monodromy_execution_open": str(MONODROMY.relative_to(ROOT)).replace("\\", "/"),
        "U6_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    for path, payload in [
        (ROOTS, root_packet),
        (NODES, node_packet),
        (MONODROMY, monodromy_open),
        (FRONTIER, frontier),
    ]:
        dump(path, payload)

    checks = {
        "mpsolve_exact_integer_input": root_packet["input"]["degree"] == 90,
        "all_90_roots_isolated": len(roots) == 90
        and all(root["status"] == "Status: Isolated, None, In" for root in roots),
        "all_disks_pairwise_disjoint": disk_checks["all_pairwise_disjoint"],
        "real_and_conjugate_counts": disk_checks["real_axis_disk_count"] == 8
        and disk_checks["conjugate_pair_count"] == 41,
        "exact_real_intervals": len(real_intervals) == 8,
        "unique_elliptic_lifts": node_packet["critical_value_lift"]["unique_lift_per_a_root"],
        "subresultant_linear": sp.degree(c1 * t + c0, t) == 1,
        "subresultant_leading_nonzero_on_all_nodes": c1_nonzero_gcd.as_expr() == 1,
        "all_90_nodes_lifted": len(node_packet["exact_objects"]) == 90,
        "monodromy_not_invented": frontier["monodromy_matrices_closed"] == 0,
        "beta_rows_not_invented": frontier["beta_C_period_rows_emitted"] == 0,
        "trial_not_selected": not frontier["trial_tau_i_and_identity_alignment_selected"],
        "no_observed_fit": frontier["observed_or_fitted_physics_parameters_added"] == 0,
    }
    assert all(checks.values())

    results = {
        "N90_critical_value_disks_closed": 90,
        "exact_real_roots": 8,
        "nonreal_conjugate_pairs": 41,
        "elliptic_critical_value_lifts_closed": 90,
        "fiber_nodal_point_lifts_closed": 90,
        "integral_monodromy_matrices_closed": 0,
        "beta_C_period_rows_emitted": 0,
        "actual_exact_gerbe_zero": False,
        "strict_MTT_source_moduli_removed": 0,
        "observed_or_fitted_physics_parameters_added": 0,
        "U6_strong_CP_closed": False,
    }
    authority_hashes = [{"path": str(path), "sha256": sha256(path)} for path in paths.values()]
    candidate = {
        "schema": "MTTSelectedQ79GenusTwoCriticalValueAndNodeIsolation.v1",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "outputs": outputs,
        "checks": checks,
        "results": results,
        "authority_hashes": authority_hashes,
    }
    certificate = {
        "certificate": "MTT_Selected_q79GenusTwoCriticalValueAndNodeIsolation_v1",
        "candidate": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "proof_artifact": str(NOTE.relative_to(ROOT)).replace("\\", "/"),
        "status": STATUS,
        "next_required_artifact": NEXT,
        "checks": checks,
        "results": results,
    }
    dump(CANDIDATE, candidate)
    dump(CERT, certificate)

    note = f"""# MTT Selected q79 Genus-Two Critical-Value and Node Isolation v1

Status: `{STATUS}`

## Certified critical values

A112 feeds A111's exact degree-90 integer polynomial `N90` to MPSolve 3.2.3
with the isolation goal and exact integer input. The full output contains `90`
entries, each with status

```text
Status: Isolated, None, In
```

and a guaranteed inclusion radius. All `4005` disk pairs are disjoint by an
exact decimal-rational squared-distance check. Eight disks meet the real axis;
independent Sturm isolation gives eight simple rational real intervals. The
other 82 disks form 41 conjugate pairs. Thus every discriminant root now has a
machine-checkable individual carrier rather than only a square-free count.

The exact integer discriminant is square-free:

```text
gcd(N90,N90') = 1.
```

Thus no certified disk can hide a repeated critical value.

## Exact lift to the elliptic base

For the unique root `a_j` in disk `D_j`, define

```text
b_j=-P45(a_j)/Q43(a_j).
```

The A111 coprimality certificate proves `Q43(a_j)!=0`. The equation
`N90(a_j)=0` then gives `b_j^2=a_j^3-a_j`, while construction gives
`P45(a_j)+b_j Q43(a_j)=0`. Therefore every `a_j` has exactly one lift to a
critical point of the genus-two family on `E_i`.

## Exact nodal points

The subresultant sequence of `f_ab` and `d_t f_ab` has degrees

```text
6,5,4,3,2,1,0.
```

Reduce the degree-one member modulo `b^2-a^3+a`:

```text
S1_red=c1(a,b)t+c0(a,b).
```

After substituting `b=-P45/Q43`, the numerator of `c1` is coprime to `N90`.
Hence `c1` is nonzero at all 90 critical values and

```text
t_j=-c0(a_j,b_j)/c1(a_j,b_j),  u_j=0
```

is the unique double root and the exact node of the singular fiber. A112 thus
closes all 90 critical values and all 90 nodal points algebraically.

## What remains

No monodromy matrix or beta period is inferred from root isolation. The next
execution must choose a regular genus-two fiber and certified path tree on the
punctured elliptic base, track the colliding branch pair along every path, and
emit the 90 integral Picard-Lefschetz transvections in `Sp(4,Z)`. Only then can
the rank-92 surface homology and A106 beta periods be assembled.

The trial carrier remains unselected, zero strict source moduli are removed,
and U6 is not declared closed.

## Solver semantics

MPSolve's official polynomial-file and output documentation defines exact
integer input, the isolate goal, full output error bounds, and `Isolated`
status. The raw input and output are retained and hashed in the packet.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps(certificate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
