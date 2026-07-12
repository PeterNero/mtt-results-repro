import math


def distance(epsilon):
    return math.sqrt(-math.log(epsilon))


def main():
    targets = {
        "CKM s12": 0.2250,
        "CKM s23": 0.0411,
        "CKM s13": 0.0036,
        "PMNS s12": math.sin(math.radians(33.4)),
        "PMNS s23": math.sin(math.radians(46.8)),
        "PMNS s13": math.sin(math.radians(8.6)),
        "y_u/y_t": 1.2e-5 / 0.53,
        "y_c/y_t": 1.6e-3 / 0.53,
        "y_d/y_b": 2.2e-4 / 0.11,
        "y_s/y_b": 5.5e-3 / 0.11,
        "y_e/y_tau": 2.8e-4 / 0.10,
        "y_mu/y_tau": 6.0e-3 / 0.10,
        "m1/m3": 0.0025 / 0.050,
        "m2/m3": 0.0087 / 0.050,
    }

    print(f"{'quantity':<14} {'magnitude':>14} {'D':>10}")
    print("-" * 42)
    for name, eps in targets.items():
        print(f"{name:<14} {eps:14.6e} {distance(eps):10.3f}")


if __name__ == "__main__":
    main()
