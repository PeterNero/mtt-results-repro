import math


def character_order(k, n):
    return n // math.gcd(k, n)


def main():
    # Same CKM benchmark convention as complex_holonomy_benchmark_check.py.
    s12_q, s23_q, s13_q = 0.2250, 0.0411, 0.0036
    c12_q = math.sqrt(1.0 - s12_q * s12_q)
    c23_q = math.sqrt(1.0 - s23_q * s23_q)
    c13_q = math.sqrt(1.0 - s13_q * s13_q)
    target_j = 2.9e-5
    prefactor = c12_q * c23_q * c13_q**2 * s12_q * s23_q * s13_q
    delta_q = math.asin(target_j / prefactor)

    rows = []
    for m in range(1, 65):
        n = 64 * m
        k = round(delta_q * n / (2.0 * math.pi)) % n
        delta = 2.0 * math.pi * k / n
        j = prefactor * math.sin(delta)
        phase_error = abs(delta - delta_q)
        j_error = abs(j - target_j)
        order = character_order(k, n)
        rows.append((phase_error, j_error, m, n, k, order, delta))

    print("Top candidates for N = 64*m, ranked by CKM phase error")
    print("m  N     k    char_order  phase_error    J_error")
    for phase_error, j_error, m, n, k, order, _ in sorted(rows)[:20]:
        print(
            f"{m:2d} {n:5d} {k:4d} {order:10d} "
            f"{phase_error:12.3e} {j_error:10.3e}"
        )

    print()
    print("Small odd/even companions m <= 14")
    print("m  N     k    char_order  phase_error    J_error")
    for phase_error, j_error, m, n, k, order, _ in rows:
        if m <= 14:
            print(
                f"{m:2d} {n:5d} {k:4d} {order:10d} "
                f"{phase_error:12.3e} {j_error:10.3e}"
            )

    print()
    print("Multiples of seven in the scan")
    print("m  N     k    gcd(k,N)  char_order")
    for phase_error, j_error, m, n, k, order, _ in rows:
        if m % 7 == 0:
            print(f"{m:2d} {n:5d} {k:4d} {math.gcd(k, n):8d} {order:10d}")


if __name__ == "__main__":
    main()
