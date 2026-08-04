import math


def distance(epsilon):
    return math.sqrt(-math.log(epsilon))


def triangle_margins(d12, d23, d13):
    return (
        d12 + d23 - d13,
        d12 + d13 - d23,
        d23 + d13 - d12,
    )


def embed_triangle(d12, d23, d13):
    # Place p1=(0,0), p2=(d12,0), solve for p3.
    x = (d12**2 + d13**2 - d23**2) / (2 * d12)
    y2 = d13**2 - x**2
    if y2 < -1e-12:
        return None
    return (0.0, 0.0), (d12, 0.0), (x, math.sqrt(max(0.0, y2)))


def report(name, d12, d23, d13):
    print(name)
    print(f"  D12={d12:.6f}, D23={d23:.6f}, D13={d13:.6f}")
    margins = triangle_margins(d12, d23, d13)
    print("  margins:", tuple(round(x, 6) for x in margins))
    ok = all(m >= -1e-12 for m in margins)
    print("  triangle ok:", ok)
    if ok:
        print("  embedding:", embed_triangle(d12, d23, d13))
    else:
        deficit = max(-m for m in margins)
        scale = d13 / (d12 + d23)
        print(f"  deficit={deficit:.6f}")
        print(f"  scale short sides to restore D12+D23>=D13: {scale:.6f}")


def main():
    ckm = (
        distance(0.2250),
        distance(0.0411),
        distance(0.0036),
    )
    pmns = (
        distance(math.sin(math.radians(33.4))),
        distance(math.sin(math.radians(46.8))),
        distance(math.sin(math.radians(8.6))),
    )
    report("CKM", *ckm)
    report("PMNS", *pmns)


if __name__ == "__main__":
    main()
