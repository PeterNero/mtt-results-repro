import numpy as np


Yu = np.diag([1.2e-5, 1.6e-3, 0.53])
Yd = np.array(
    [
        [2.14e-4, 1.24e-3, 3.96e-4],
        [-4.95e-5, 5.35e-3, 4.52e-3],
        [1.26e-6, -2.25e-4, 1.099e-1],
    ]
)

Ye = np.diag([2.8e-4, 6.0e-3, 0.10])
Ynu = np.array(
    [
        [1.462e-2, -8.287e-3, 5.594e-3],
        [1.799e-2, 1.690e-2, -2.197e-2],
        [1.185e-2, 5.710e-2, 5.362e-2],
    ]
)
MR = np.diag([3.8e12, 3.8e12, 3.8e12])
vu = 174.0


def left_rotation(y):
    vals, vecs = np.linalg.eigh(y @ y.T)
    order = np.argsort(vals)
    return vecs[:, order], np.sqrt(np.maximum(vals[order], 0))


def main():
    uu, mu = left_rotation(Yu)
    ud, md = left_rotation(Yd)
    vckm = uu.T @ ud

    ue, me = left_rotation(Ye)
    mnu = Ynu.T @ np.linalg.inv(MR) @ Ynu * vu**2 * 1e9
    mn, unu = np.linalg.eigh(mnu)
    order = np.argsort(mn)
    mn = mn[order]
    unu = unu[:, order]
    upmns = ue.T @ unu

    print("up singular values:", mu)
    print("down singular values:", md)
    print("|V_CKM|:")
    print(np.round(np.abs(vckm), 4))
    print("charged-lepton singular values:", me)
    print("neutrino masses [eV]:", mn)
    print("|U_PMNS|:")
    print(np.round(np.abs(upmns), 3))
    print("J_CKM for printed real benchmark: 0")


if __name__ == "__main__":
    main()
