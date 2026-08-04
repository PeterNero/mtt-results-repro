"""Schur-reduction formula for the retarded dyadic CKM lag.

This script verifies the algebraic coefficient extraction theorem used by the
retarded-lag proof.  It is not an evaluation of the MTT geometry.  Real MTT
input would be the selected closure Hessian blocks and the retarded overlap
force vector.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isclose


@dataclass(frozen=True)
class Coefficients:
    rho: float
    kappa: float
    epsilon: float


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def matvec(a: list[list[float]], x: list[float]) -> list[float]:
    return [dot(row, x) for row in a]


def solve(a: list[list[float]], b: list[float]) -> list[float]:
    n = len(b)
    aug = [row[:] + [rhs] for row, rhs in zip(a, b)]

    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(aug[row][col]))
        if abs(aug[pivot][col]) < 1e-14:
            raise ValueError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]

        pivot_value = aug[col][col]
        for j in range(col, n + 1):
            aug[col][j] /= pivot_value

        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            for j in range(col, n + 1):
                aug[row][j] -= factor * aug[col][j]

    return [aug[row][n] for row in range(n)]


def is_positive_definite(a: list[list[float]]) -> bool:
    """Sylvester criterion by leading principal determinants for small inputs."""

    for size in range(1, len(a) + 1):
        sub = [row[:size] for row in a[:size]]
        if determinant(sub) <= 0:
            return False
    return True


def determinant(a: list[list[float]]) -> float:
    n = len(a)
    if n == 1:
        return a[0][0]
    if n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    total = 0.0
    for col in range(n):
        minor = [
            [a[row][j] for j in range(n) if j != col]
            for row in range(1, n)
        ]
        total += ((-1.0) ** col) * a[0][col] * determinant(minor)
    return total


def schur_linear_retarded_coefficients(
    h_uu: float,
    h_u_eta: list[float],
    h_eta_eta: list[list[float]],
    r_u: float,
    r_eta: list[float],
) -> Coefficients:
    """Compute rho and kappa after minimizing nuisance directions.

    Closure strain:
        C(s,eta) = 1/2 h_uu s^2 + s h_u_eta eta
                   + 1/2 eta^T h_eta_eta eta.

    Retarded overlap force to first order:
        R(s,eta) = r_u s + r_eta eta.

    Eliminating eta gives:
        rho   = r_u - h_u_eta h_eta_eta^{-1} r_eta
        kappa = h_uu - h_u_eta h_eta_eta^{-1} h_eta_u.
    """

    inv_r_eta = solve(h_eta_eta, r_eta)
    inv_h_eta_u = solve(h_eta_eta, h_u_eta)
    rho = r_u - dot(h_u_eta, inv_r_eta)
    kappa = h_uu - dot(h_u_eta, inv_h_eta_u)
    return Coefficients(rho=rho, kappa=kappa, epsilon=rho / kappa)


def closure_cost(s: float, eta: list[float], h_uu: float, h_u_eta: list[float], h_eta_eta: list[list[float]]) -> float:
    return (
        0.5 * h_uu * s * s
        + s * dot(h_u_eta, eta)
        + 0.5 * dot(eta, matvec(h_eta_eta, eta))
    )


def retarded_force_cost(s: float, eta: list[float], r_u: float, r_eta: list[float]) -> float:
    return r_u * s + dot(r_eta, eta)


def minimized_cost(
    s: float,
    h_uu: float,
    h_u_eta: list[float],
    h_eta_eta: list[list[float]],
    r_u: float,
    r_eta: list[float],
) -> float:
    eta_star = [-value for value in solve(h_eta_eta, [h_u_eta[i] * s + r_eta[i] for i in range(len(r_eta))])]
    return closure_cost(s, eta_star, h_uu, h_u_eta, h_eta_eta) + retarded_force_cost(s, eta_star, r_u, r_eta)


def main() -> None:
    # Demonstration data only.  These are not selected MTT geometry values.
    h_uu = 5.0
    h_u_eta = [0.5, -0.25]
    h_eta_eta = [
        [4.0, 0.5],
        [0.5, 3.0],
    ]
    r_eta = [0.2, -0.1]
    r_u = 4.94

    coefficients = schur_linear_retarded_coefficients(
        h_uu=h_uu,
        h_u_eta=h_u_eta,
        h_eta_eta=h_eta_eta,
        r_u=r_u,
        r_eta=r_eta,
    )

    j_minus = minimized_cost(-1.0, h_uu, h_u_eta, h_eta_eta, r_u, r_eta)
    j_zero = minimized_cost(0.0, h_uu, h_u_eta, h_eta_eta, r_u, r_eta)
    j_plus = minimized_cost(1.0, h_uu, h_u_eta, h_eta_eta, r_u, r_eta)

    rho_from_values = 0.5 * (j_plus - j_minus)
    kappa_from_values = j_plus + j_minus - 2.0 * j_zero

    assert is_positive_definite(h_eta_eta)
    assert isclose(coefficients.rho, rho_from_values, rel_tol=0.0, abs_tol=1e-12)
    assert isclose(coefficients.kappa, kappa_from_values, rel_tol=0.0, abs_tol=1e-12)

    print("Retarded-lag Schur coefficient formula")
    print("======================================")
    print("Demonstration data only: not MTT geometry")
    print("h_eta_eta positive definite:", is_positive_definite(h_eta_eta))
    print("rho:", f"{coefficients.rho:.12f}")
    print("kappa:", f"{coefficients.kappa:.12f}")
    print("epsilon = rho/kappa:", f"{coefficients.epsilon:.12f}")
    print()

    print("Algebra checks")
    print("==============")
    gates = [
        ("Schur rho matches direct minimization", "PASS", f"{rho_from_values:.12f}"),
        ("Schur kappa matches direct minimization", "PASS", f"{kappa_from_values:.12f}"),
        ("positive nuisance Hessian", "PASS", "h_eta_eta > 0"),
        ("sample epsilon in retarded cell", "PASS" if 0.0 < coefficients.epsilon < 2.0 else "FAIL", "demonstration only"),
        ("actual selected MTT matrices supplied", "OPEN", "needs H_q and retarded kernel derivative"),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{width}s}  {status:{status_width}s}  {note}")


if __name__ == "__main__":
    main()
