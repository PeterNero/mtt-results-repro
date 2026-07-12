import math


def ckm_prefactor():
    s12, s23, s13 = 0.2250, 0.0411, 0.0036
    c12 = math.sqrt(1.0 - s12 * s12)
    c23 = math.sqrt(1.0 - s23 * s23)
    c13 = math.sqrt(1.0 - s13 * s13)
    return c12 * c23 * c13**2 * s12 * s23 * s13


def main():
    target_j = 2.9e-5
    pref = ckm_prefactor()
    target_delta = math.asin(target_j / pref)

    n = 448
    k12 = 79
    k23 = -112
    k31 = 33

    assert (k12 + k23 + k31) % n == 0

    phi12 = 2 * math.pi * k12 / n
    phi23 = 2 * math.pi * k23 / n
    phi31 = 2 * math.pi * k31 / n
    j_ckm = pref * math.sin(phi12)

    theta12_l = math.radians(33.4)
    theta23_l = math.radians(46.8)
    theta13_l = math.radians(8.6)
    s12_l, s23_l, s13_l = math.sin(theta12_l), math.sin(theta23_l), math.sin(theta13_l)
    c12_l, c23_l, c13_l = math.cos(theta12_l), math.cos(theta23_l), math.cos(theta13_l)
    j_pmns = c12_l * c23_l * c13_l**2 * s12_l * s23_l * s13_l * math.sin(phi23)

    print(f"N = {n}")
    print(f"(k12, k23, k31) = ({k12}, {k23}, {k31})")
    print(f"sum mod N = {(k12 + k23 + k31) % n}")
    print(f"target delta_q = {target_delta:.12f}")
    print(f"finite delta_q = {phi12:.12f}")
    print(f"delta error = {abs(phi12 - target_delta):.3e}")
    print(f"J_CKM finite = {j_ckm:.12e}")
    print(f"J_CKM target error = {abs(j_ckm - target_j):.3e}")
    print(f"delta_l finite = {phi23:.12f}")
    print(f"J_PMNS finite = {j_pmns:.12e}")
    print(f"phi31 = {phi31:.12f}")
    print(f"phase sum = {phi12 + phi23 + phi31:.3e}")

    print("\nBest N divisible by 4 up to 512:")
    best = None
    for cand_n in range(4, 513, 4):
        cand_k = round(cand_n * target_delta / (2 * math.pi))
        cand_phi = 2 * math.pi * cand_k / cand_n
        cand_j = pref * math.sin(cand_phi)
        err = abs(cand_j - target_j)
        if best is None or err < best[0]:
            best = (err, cand_n, cand_k, cand_phi, cand_j)
    err, cand_n, cand_k, cand_phi, cand_j = best
    print(f"N={cand_n}, k={cand_k}, delta={cand_phi:.12f}, J={cand_j:.12e}, err={err:.3e}")


if __name__ == "__main__":
    main()
