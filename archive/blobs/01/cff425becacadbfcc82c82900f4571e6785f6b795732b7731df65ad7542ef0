import math
import numpy as np


def mixing_matrix(s12, s23, s13, delta):
    c12 = math.sqrt(1.0 - s12 * s12)
    c23 = math.sqrt(1.0 - s23 * s23)
    c13 = math.sqrt(1.0 - s13 * s13)
    e_pos = complex(math.cos(delta), math.sin(delta))
    e_neg = e_pos.conjugate()
    return np.array(
        [
            [c12 * c13, s12 * c13, s13 * e_neg],
            [
                -s12 * c23 - c12 * s23 * s13 * e_pos,
                c12 * c23 - s12 * s23 * s13 * e_pos,
                s23 * c13,
            ],
            [
                s12 * s23 - c12 * c23 * s13 * e_pos,
                -c12 * s23 - s12 * c23 * s13 * e_pos,
                c23 * c13,
            ],
        ],
        dtype=complex,
    )


def jarlskog(u):
    return float(np.imag(u[0, 0] * u[1, 1] * np.conj(u[0, 1]) * np.conj(u[1, 0])))


def main():
    s12_q, s23_q, s13_q = 0.2250, 0.0411, 0.0036
    c12_q = math.sqrt(1.0 - s12_q * s12_q)
    c23_q = math.sqrt(1.0 - s23_q * s23_q)
    c13_q = math.sqrt(1.0 - s13_q * s13_q)
    target_j = 2.9e-5
    prefactor = c12_q * c23_q * c13_q**2 * s12_q * s23_q * s13_q
    delta_q = math.asin(target_j / prefactor)
    v_ckm = mixing_matrix(s12_q, s23_q, s13_q, delta_q)

    theta12_l = math.radians(33.4)
    theta23_l = math.radians(46.8)
    theta13_l = math.radians(8.6)
    delta_l = -math.pi / 2.0
    u_pmns = mixing_matrix(
        math.sin(theta12_l), math.sin(theta23_l), math.sin(theta13_l), delta_l
    )

    phi_12 = delta_q
    phi_23 = delta_l
    phi_31 = -(phi_12 + phi_23)
    phase_sum = phi_12 + phi_23 + phi_31

    yd_singular = np.diag([2.2e-4, 5.5e-3, 0.11])
    yd = v_ckm @ yd_singular
    check = yd @ yd.conj().T
    eigvals, eigvecs = np.linalg.eigh(check)
    order = np.argsort(eigvals)
    singular_values = np.sqrt(np.maximum(eigvals[order], 0))

    print(f"delta_q = {delta_q:.8f} rad")
    print(f"J_CKM = {jarlskog(v_ckm):.8e}")
    print("|V_CKM| =")
    print(np.round(np.abs(v_ckm), 4))
    print("down singular values from complex Yd =", singular_values)
    print(f"delta_l = {delta_l:.8f} rad")
    print(f"J_PMNS = {jarlskog(u_pmns):.8e}")
    print("|U_PMNS| =")
    print(np.round(np.abs(u_pmns), 3))
    print("holonomy phases =", (phi_12, phi_23, phi_31))
    print(f"phase sum = {phase_sum:.3e}")


if __name__ == "__main__":
    main()
