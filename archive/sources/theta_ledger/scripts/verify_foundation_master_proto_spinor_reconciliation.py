#!/usr/bin/env python3
"""Verify the 2026-07-15 Foundation/master/proto-spinor revision pass."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DOWNLOADS = TEXPAPERS.parent
FOUNDATION = TEXPAPERS / "3 Core Foundations" / "revised_tex_vnext"
PROTO = TEXPAPERS / "10 ProtoSpinor" / "revised_tex_vnext"
MASTER = DOWNLOADS / "MTT_Master_Corrigendum_and_Revision_Plan.md"

FILES = {
    "foundation": FOUNDATION / "Modal_Triplet_Theory__Foundation_v8" / "main.tex",
    "signature": FOUNDATION
    / "Lorentzian_Base_Compatibility_and_Signature_Stability_in_the_MTT_Fixed_Point_Realization_v2"
    / "main.tex",
    "kinematics": FOUNDATION / "Coherent_Kinematics_in_Modal_Triplet_Theory_v2" / "main.tex",
    "atlas": FOUNDATION / "Modal_Triplet_Theory__A_Typed_Relationship_Atlas_v3" / "main.tex",
    "projection": FOUNDATION
    / "The_Projection__Admissibility_Principle__Descent__Recovery__and_Structural_Constraints_v2"
    / "main.tex",
    "scales": FOUNDATION / "Baseline_Scales_and_Phenomenological_Consistency_in_Modal_Triplet_Theory_v2" / "main.tex",
    "proto": PROTO
    / "The_Proto_Spinor__Conditional_Spinorial_Closure_and_q79_Interface_v6"
    / "main.tex",
    "world": PROTO
    / "World_in_World_Genesis__Local_Comparison_Geometry_and_Globalization_Program_v5"
    / "main.tex",
    "strain": PROTO
    / "Closure_Strain_Geometry__Local_Normal_Forms_and_Conditional_Matter_Encodings_v7"
    / "main.tex",
    "worldsheet": PROTO
    / "Proto_Spinor_Closure_and_Worldsheet_Encoding_in_Modal_Triplet_Theory_v4"
    / "main.tex",
    "action": PROTO
    / "Closure_Geometry_and_a_Regime_Local_Ten_Dimensional_Action_Ansatz_v4"
    / "main.tex",
}


def fail(message: str) -> None:
    raise AssertionError(message)


def uncommented(text: str) -> str:
    rows = []
    for line in text.splitlines():
        out = []
        escaped = False
        for char in line:
            if char == "%" and not escaped:
                break
            out.append(char)
            if char == "\\":
                escaped = not escaped
            else:
                escaped = False
        rows.append("".join(out))
    return "\n".join(rows)


def verify_tex_structure(path: Path) -> None:
    text = uncommented(path.read_text(encoding="utf-8"))
    if "\\begin{document}" not in text or "\\end{document}" not in text:
        fail(f"missing document boundary: {path}")

    stack: list[str] = []
    for match in re.finditer(r"\\(begin|end)\{([^{}]+)\}", text):
        kind, env = match.groups()
        if kind == "begin":
            stack.append(env)
        elif not stack or stack.pop() != env:
            fail(f"environment mismatch near {match.start()} in {path}")
    if stack:
        fail(f"unclosed environments {stack} in {path}")

    depth = 0
    escaped = False
    for char in text:
        if char == "\\":
            escaped = not escaped
            continue
        if char == "{" and not escaped:
            depth += 1
        elif char == "}" and not escaped:
            depth -= 1
            if depth < 0:
                fail(f"extra closing brace in {path}")
        escaped = False
    if depth != 0:
        fail(f"brace balance {depth} in {path}")


def require(name: str, *needles: str) -> None:
    text = FILES[name].read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            fail(f"{name}: required text absent: {needle}")


def reject(name: str, *needles: str) -> None:
    text = FILES[name].read_text(encoding="utf-8")
    for needle in needles:
        if needle in text:
            fail(f"{name}: retired text remains: {needle}")


Matrix = list[list[Fraction]]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0)) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matsum(*items: Matrix) -> Matrix:
    return [
        [sum((item[i][j] for item in items), Fraction(0)) for j in range(len(items[0][0]))]
        for i in range(len(items[0]))
    ]


def eye(n: int) -> Matrix:
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def rank(a: Matrix) -> int:
    m = [row[:] for row in a]
    rows, cols = len(m), len(m[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        scale = m[r][c]
        m[r] = [x / scale for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c]:
                factor = m[i][c]
                m[i] = [m[i][j] - factor * m[r][j] for j in range(cols)]
        r += 1
    return r


def verify_strain_projectors() -> None:
    z = Fraction(0)
    third = Fraction(1, 3)
    p1: Matrix = [[z for _ in range(6)] for _ in range(6)]
    for i in range(3):
        for j in range(3):
            p1[i][j] = third
    p2: Matrix = [[z for _ in range(6)] for _ in range(6)]
    for i in range(3):
        p2[i][i] = 1
    p2 = [[p2[i][j] - p1[i][j] for j in range(6)] for i in range(6)]
    p3: Matrix = [[z for _ in range(6)] for _ in range(6)]
    for i in range(3, 6):
        p3[i][i] = 1

    projectors = [p1, p2, p3]
    if [rank(p) for p in projectors] != [1, 2, 3]:
        fail("strain projector ranks are not 1,2,3")
    if matsum(*projectors) != eye(6):
        fail("strain projectors do not sum to identity")
    for i, p in enumerate(projectors):
        if matmul(p, p) != p:
            fail(f"strain projector {i} is not idempotent")
        for j, q in enumerate(projectors):
            if i != j and matmul(p, q) != [[z] * 6 for _ in range(6)]:
                fail(f"strain projectors {i},{j} are not orthogonal")


def perm_sign(p: tuple[int, ...]) -> int:
    inversions = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


def perm_matrix(p: tuple[int, ...]) -> list[list[int]]:
    m = [[0] * 3 for _ in range(3)]
    for j in range(3):
        m[p[j]][j] = 1
    return m


def imatmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def det3(m: list[list[int]]) -> int:
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def rho(p: tuple[int, ...]) -> list[list[int]]:
    sign = perm_sign(p)
    return [[sign * x for x in row] for row in perm_matrix(p)]


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[i]] for i in range(3))


def verify_signed_sheet_representation() -> None:
    group = list(permutations(range(3)))
    for p in group:
        if det3(rho(p)) != 1:
            fail(f"signed permutation is not in SO(3): {p}")
        for q in group:
            if imatmul(rho(p), rho(q)) != rho(compose(p, q)):
                fail(f"signed sheet map is not a homomorphism: {p}, {q}")


Q2 = tuple[Fraction, Fraction]  # a + b*sqrt(2)
Quaternion = tuple[Q2, Q2, Q2, Q2]


def q2_add(x: Q2, y: Q2) -> Q2:
    return (x[0] + y[0], x[1] + y[1])


def q2_neg(x: Q2) -> Q2:
    return (-x[0], -x[1])


def q2_mul(x: Q2, y: Q2) -> Q2:
    return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def quat_mul(a: Quaternion, b: Quaternion) -> Quaternion:
    w, x, y, z = a
    W, X, Y, Z = b
    terms = (
        (q2_mul(w, W), q2_neg(q2_mul(x, X)), q2_neg(q2_mul(y, Y)), q2_neg(q2_mul(z, Z))),
        (q2_mul(w, X), q2_mul(x, W), q2_mul(y, Z), q2_neg(q2_mul(z, Y))),
        (q2_mul(w, Y), q2_neg(q2_mul(x, Z)), q2_mul(y, W), q2_mul(z, X)),
        (q2_mul(w, Z), q2_mul(x, Y), q2_neg(q2_mul(y, X)), q2_mul(z, W)),
    )
    return tuple(q2_add(q2_add(row[0], row[1]), q2_add(row[2], row[3])) for row in terms)  # type: ignore[return-value]


def quat_pow(q: Quaternion, n: int) -> Quaternion:
    one: Quaternion = ((Fraction(1), Fraction(0)),) + (((Fraction(0), Fraction(0)),) * 3)  # type: ignore[assignment]
    result = one
    for _ in range(n):
        result = quat_mul(result, q)
    return result


def verify_binary_dihedral_lifts() -> None:
    zero: Q2 = (Fraction(0), Fraction(0))
    a: Q2 = (Fraction(0), Fraction(1, 2))  # sqrt(2)/2
    minus_a = q2_neg(a)
    one: Quaternion = ((Fraction(1), Fraction(0)), zero, zero, zero)
    minus_one: Quaternion = ((Fraction(-1), Fraction(0)), zero, zero, zero)
    q1: Quaternion = (zero, a, minus_a, zero)
    q2: Quaternion = (zero, zero, a, minus_a)
    if quat_mul(q1, q1) != minus_one or quat_mul(q2, q2) != minus_one:
        fail("half-turn lifts do not square to -1")
    if quat_mul(quat_mul(q1, q2), q1) != quat_mul(quat_mul(q2, q1), q2):
        fail("lifted braid relation does not close")
    if quat_pow(quat_mul(q1, q2), 3) != minus_one:
        fail("(q1 q2)^3 is not -1")

    generated = {one}
    frontier = [one]
    while frontier:
        current = frontier.pop()
        for generator in (q1, q2):
            nxt = quat_mul(current, generator)
            if nxt not in generated:
                generated.add(nxt)
                frontier.append(nxt)
    if len(generated) != 12:
        fail(f"lifted group has order {len(generated)}, expected 12")


def main() -> int:
    missing = [str(path) for path in [*FILES.values(), MASTER] if not path.is_file()]
    if missing:
        fail("missing revised files:\n" + "\n".join(missing))

    for path in FILES.values():
        verify_tex_structure(path)

    require(
        "foundation",
        "Local comparison carrier and selected q79 interface",
        "1+3\\times3=(1+3)+(1+2+3)=4+6=10",
        "same-source",
    )
    require("signature", "counts components of an ordering scalar", "does not claim universal signature")
    require("kinematics", "A compact shared $U(1)$ circle", "\\mathbb R\\to S^1")
    require("atlas", "local binary-dihedral spin lift", "Fu--Yau branch")
    require("proto", "Conditional double-cover necessity", "Local binary-dihedral lift", "Strict global Spin")
    require("world", "Bundle dimension versus comparison components", "Selected world-in-world/q79 intertwiner")
    require("strain", "Closure-strain projector theorem", "What a positive strain Hessian proves")
    require("worldsheet", "Conditional quadratic bridge", "\\|u\\|_{\\rm ps}^3")
    require("action", "Pole-mass promotion", "Conditional coherent reduction", "Regime-local action statement")

    reject("proto", "Internal dimension must be three for minimal discrete return obstruction")
    reject("world", "Uniqueness of bookkeeping time", "Dimensional rigidity and proto-spinorial lift")
    reject("strain", "Triadic completeness (structural)", "No second Higgs")
    reject("action", "Mass Theorem", "Nil Quantization Theorem", "most general ten-dimensional")

    master = MASTER.read_text(encoding="utf-8")
    for needle in (
        'version: "1.1"',
        "Foundational-geometry reconciliation authority",
        "World-in-world comparison carrier",
        "same-source world-in-world/strain-to-q79",
        "Every `3 x 3` count",
    ):
        if needle not in master:
            fail(f"master: required text absent: {needle}")
    if "M_{10}\\simeq\\mathbb R_t\\times W_1^3\\times W_2^3\\times W_3^3" in master:
        fail("master retains obsolete three-spatial-leg product")

    verify_strain_projectors()
    verify_signed_sheet_representation()
    verify_binary_dihedral_lifts()

    print("PASS: 11 revised TeX papers have balanced source structure")
    print("PASS: Foundation/master carry the corrected comparison and q79 boundary")
    print("PASS: exact strain projector ranks are 1+2+3")
    print("PASS: signed S3 sheet action is an SO(3) representation")
    print("PASS: exact quaternion lifts generate Dic_3 of order 12")
    print("PASS: retired central proto-spinor claims are absent from successor papers")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
