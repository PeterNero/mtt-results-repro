from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from decimal import Decimal, localcontext
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2criticalvalueandnodeisolation"
STATUS = "MTT_U6_Q79_90_CRITICAL_VALUES_AND_NODAL_POINTS_CERTIFIED_MONODROMY_PATHS_OPEN"
NEXT = "MTT_Selected_q79GenusTwoPicardLefschetzMonodromyExecution_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79GenusTwoCriticalValueAndNodeIsolation_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")],
        cwd=ROOT,
        check=True,
    )
    candidate = load(CANDIDATE)
    certificate = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    roots = outputs["certified_root_disks"]
    nodes = outputs["critical_and_node_lifts"]
    monodromy = outputs["monodromy_execution_open"]
    frontier = outputs["U6_frontier"]

    require(candidate["status"] == certificate["status"] == STATUS, "A112 status changed")
    require(candidate["next_required_artifact"] == certificate["next_required_artifact"] == NEXT, "A112 next changed")
    require(all(candidate["checks"].values()), "one or more A112 checks failed")
    require(sp.__version__ == "1.14.0", "unlocked SymPy version")

    solver = roots["solver"]
    require(solver["name"] == "MPSolve", "wrong root solver")
    require(solver["version"] == "MPSolve 3.2.3", "unlocked MPSolve version")
    require(solver["goal"] == "isolate", "wrong MPSolve goal")
    require(solver["threads"] == 1, "nondeterministic MPSolve thread count")

    root_disks = roots["root_disks"]
    require(len(root_disks) == 90, "root disk count")
    require(len({root["root_id"] for root in root_disks}) == 90, "root ids not unique")
    require(all(root["status"] == "Status: Isolated, None, In" for root in root_disks), "nonisolated root")

    minimum_margin = None
    pair_count = 0
    with localcontext() as context:
        context.prec = 100
        for left_index, left in enumerate(root_disks):
            left_real = Decimal(left["center_real"])
            left_imaginary = Decimal(left["center_imaginary"])
            left_radius = Decimal(left["radius"])
            for right in root_disks[left_index + 1 :]:
                right_real = Decimal(right["center_real"])
                right_imaginary = Decimal(right["center_imaginary"])
                right_radius = Decimal(right["radius"])
                margin = (left_real - right_real) ** 2 + (
                    left_imaginary - right_imaginary
                ) ** 2 - (left_radius + right_radius) ** 2
                require(margin > 0, "overlapping root disks")
                minimum_margin = margin if minimum_margin is None else min(minimum_margin, margin)
                pair_count += 1
    checks = roots["disk_checks"]
    require(pair_count == checks["pair_count"] == 4005, "disk pair count")
    require(str(minimum_margin) == checks["minimum_squared_separation_margin"], "disk margin mismatch")
    require(checks["real_axis_disk_count"] == 8, "real disk count")
    require(checks["nonreal_disk_count"] == 82, "nonreal disk count")
    require(checks["conjugate_pair_count"] == 41, "conjugate count")
    require(len(roots["exact_real_root_intervals"]) == 8, "Sturm interval count")
    require(all(item["multiplicity"] == 1 for item in roots["exact_real_root_intervals"]), "real multiplicity")

    input_path = ROOT / roots["input"]["path"]
    raw_path = ROOT / roots["raw_output"]["path"]
    require(hashlib.sha256(input_path.read_bytes()).hexdigest() == roots["input"]["sha256"], "MPSolve input hash")
    require(hashlib.sha256(raw_path.read_bytes()).hexdigest() == roots["raw_output"]["sha256"], "MPSolve output hash")
    lines = input_path.read_text(encoding="ascii").splitlines()
    require(lines[:3] == ["dri", "0", "90"], "MPSolve input preamble")
    coefficients_ascending = [int(value) for value in lines[3:]]
    require(len(coefficients_ascending) == 91, "MPSolve coefficient count")

    a111_discriminant = load(
        ROOT
        / "candidate_data"
        / "selected_q79genus2lefschetzperiodreduction"
        / "degree90_nodal_discriminant_certificate.packet.json"
    )
    coefficients_descending = a111_discriminant["norm_certificate"]["coefficients_descending"]
    require(coefficients_ascending == list(reversed(coefficients_descending)), "N90 input mismatch")
    a = sp.symbols("a")
    n90 = sp.Poly.from_list(coefficients_descending, gens=a, domain=sp.ZZ)
    require(n90.degree() == 90, "N90 degree")
    require(sp.gcd(n90, n90.diff()).as_expr() == 1, "N90 not square-free")

    lift = nodes["critical_value_lift"]
    require(lift["critical_value_count"] == 90, "critical lift count")
    require(lift["unique_lift_per_a_root"], "elliptic lift not unique")
    require(nodes["nodal_point_lift"]["node_count"] == 90, "node lift count")
    require(nodes["nodal_point_lift"]["c1_nonzero_at_every_critical_value"], "subresultant degenerates")
    require(len(nodes["exact_objects"]) == 90, "exact node table count")
    require(all(item["u"] == 0 for item in nodes["exact_objects"]), "node u coordinate")

    a111_fibration = load(
        ROOT
        / "candidate_data"
        / "selected_q79genus2lefschetzperiodreduction"
        / "explicit_genus2_fibration.packet.json"
    )
    b, t = sp.symbols("b t")
    f_ab = sp.sympify(
        a111_fibration["fiber_chart"]["equation"].split("=", 1)[1],
        locals={"a": a, "b": b, "t": t},
    )
    subresultants = sp.subresultants(f_ab, sp.diff(f_ab, t), t)
    require([sp.degree(item, t) for item in subresultants] == [6, 5, 4, 3, 2, 1, 0], "subresultant degrees")
    s1 = sp.Poly(subresultants[-2], t)
    elliptic = sp.Poly(b**2 - a**3 + a, b, domain=sp.QQ[a])
    reduce_on_e = lambda expression: sp.rem(
        sp.Poly(sp.expand(expression), b, domain=sp.QQ[a]), elliptic
    ).as_expr()
    c1 = sp.expand(reduce_on_e(s1.coeff_monomial(t)))
    c0 = sp.expand(reduce_on_e(s1.coeff_monomial(1)))
    s1_packet = nodes["degree_one_subresultant"]
    require(hashlib.sha256(str(c1).encode("ascii")).hexdigest() == s1_packet["c1_sha256"], "c1 hash")
    require(hashlib.sha256(str(c0).encode("ascii")).hexdigest() == s1_packet["c0_sha256"], "c0 hash")
    require(s1_packet["gcd_N90_c1_on_critical_numerator"] == "1", "c1 critical gcd")
    require(nodes["theorem"]["proved"], "node theorem missing")

    require(all(value is None for value in monodromy["open"].values()), "monodromy field invented")
    require(not any(monodromy["acceptance"].values()), "monodromy/beta decision invented")
    require(frontier["critical_values_closed"] == 90, "frontier critical count")
    require(frontier["nodal_points_closed"] == 90, "frontier node count")
    require(frontier["monodromy_matrices_closed"] == 0, "monodromy invented")
    require(frontier["beta_C_period_rows_emitted"] == 0, "beta rows invented")
    require(not frontier["actual_exact_gerbe_zero"], "gerbe zero invented")
    require(frontier["strict_MTT_source_moduli_removed"] == 0, "source moduli removed")
    require(not frontier["U6_strong_CP_closed"], "U6 overclosed")

    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A112 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"authority hash mismatch: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in [
        "Certified critical values",
        "All `4005` disk pairs are disjoint",
        "Exact lift to the elliptic base",
        "Exact nodal points",
        "gcd(N90,N90')",
        "No monodromy matrix or beta period is inferred",
        "zero strict source moduli are removed",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print("A112 q79 critical-value and nodal-point isolation audit: PASS")
    print(f"status={STATUS}")
    print("N90: 90 guaranteed disjoint root disks, 8 real roots, 41 conjugate pairs")
    print("critical lifts: 90/90 on E_i; exact subresultant nodes: 90/90")
    print("paths, Sp4Z monodromy, H2 basis, beta periods, selection and U6 remain open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
