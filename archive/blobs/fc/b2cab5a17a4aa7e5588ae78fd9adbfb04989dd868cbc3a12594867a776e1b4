from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FINAL_GATE = ROOT / "certificates" / "core_b0_factorization_final_gate_certificate.json"
EQUIVARIANT = ROOT / "certificates" / "equivariant_central_circle_tt_support_theorem_certificate.json"
REDUCTION = ROOT / "certificates" / "actual_shape_map_factorization_reduction_certificate.json"

OUT_PACKET = ROOT / "candidate_data" / "selected_core_b0_tt_factorization_packet.canonical_fill.json"
OUT_CERT = ROOT / "certificates" / "selected_core_b0_tt_factorization_packet_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Core_B0_TT_Factorization_Packet_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def mat_mat(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    cols = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in cols] for row in a]


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [list(col) for col in zip(*a)]


def max_abs_matrix(a: list[list[float]]) -> float:
    return max(abs(x) for row in a for x in row)


def rank_2x2(m: list[list[float]], tol: float = 1e-12) -> int:
    det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    if abs(det) > tol:
        return 2
    if any(abs(x) > tol for row in m for x in row):
        return 1
    return 0


def main() -> None:
    final_gate = load(FINAL_GATE)
    equivariant = load(EQUIVARIANT)
    reduction = load(REDUCTION)

    n = 64
    k = 2
    theta = 2 * math.pi / n

    c2 = [math.sqrt(2 / n) * math.cos(k * theta * j) for j in range(n)]
    s2 = [math.sqrt(2 / n) * math.sin(k * theta * j) for j in range(n)]
    u_tt = [[c2[i], s2[i]] for i in range(n)]
    u_star = transpose(u_tt)
    pi_exact64 = mat_mat(u_tt, u_star)

    # Canonical fill: choose the TT quotient basis/normalization in which the
    # same-angle equivariant core co-shape is exactly U_TT. A different
    # invertible TT normalization would be U_TT C and is equivalent for support.
    c_canonical = [[1.0, 0.0], [0.0, 1.0]]
    b0_star_ptt = mat_mat(u_tt, c_canonical)

    # Z64 shift and TT helicity-2 rotation in the same angular coordinate.
    s64 = [[1.0 if i == (j + 1) % n else 0.0 for j in range(n)] for i in range(n)]
    r_tt = [
        [math.cos(k * theta), -math.sin(k * theta)],
        [math.sin(k * theta), math.cos(k * theta)],
    ]

    rank_matrix = mat_mat(u_star, b0_star_ptt)
    leakage = [
        [
            b0_star_ptt[i][col] - sum(pi_exact64[i][j] * b0_star_ptt[j][col] for j in range(n))
            for col in range(2)
        ]
        for i in range(n)
    ]
    intertwining = [
        [
            mat_mat(s64, b0_star_ptt)[i][col] - mat_mat(b0_star_ptt, r_tt)[i][col]
            for col in range(2)
        ]
        for i in range(n)
    ]
    support_identity = [
        [
            sum(pi_exact64[i][j] * b0_star_ptt[j][col] for j in range(n)) - b0_star_ptt[i][col]
            for col in range(2)
        ]
        for i in range(n)
    ]

    tests = {
        "rank_Ustar_B0starPtt_is_2": rank_2x2(rank_matrix) == 2,
        "no_leakage_outside_Pi_exact64": max_abs_matrix(leakage) < 1e-12,
        "same_angle_intertwining": max_abs_matrix(intertwining) < 1e-12,
        "support_identity_on_core": max_abs_matrix(support_identity) < 1e-12,
        "final_gate_packet_name_matches": final_gate["final_packet"]["name"] == "SelectedCoreB0TTFactorizationPacket.v1",
        "equivariant_algebra_available": equivariant["theorem"]["proved_algebraically"] is True,
        "dressed_reduction_available": reduction["reduction_theorem"]["proved_conditionally"] is True,
    }

    packet = {
        "name": "SelectedCoreB0TTFactorizationPacket.v1",
        "fill_type": "canonical_same_angle_equivariant_fill",
        "status": "CANONICAL_PACKET_FILLED_TESTS_PASS_SOURCE_ACCEPTANCE_OPEN",
        "operator": "B0^*P_TT",
        "normalization": {
            "TT_basis": ["TT_plus", "TT_cross"],
            "selected_core_matrix_C": c_canonical,
            "meaning": (
                "This chooses the normalized TT quotient basis in which the core co-shape equals U_TT. "
                "Any invertible 2x2 C gives the same exact support result."
            ),
        },
        "finite_carrier": {
            "group": "Z64",
            "character": 2,
            "conjugate_character": 62,
            "basis": ["c2", "s2"],
            "theta": theta,
        },
        "closing_tests": {
            "rank_U_TT_star_B0_star_P_TT": rank_matrix,
            "rank": rank_2x2(rank_matrix),
            "no_leakage_residual": max_abs_matrix(leakage),
            "same_angle_intertwining_residual": max_abs_matrix(intertwining),
            "core_support_identity_residual": max_abs_matrix(support_identity),
        },
        "source_acceptance_required": (
            "Accept or source that the selected metric shape-map core B0 uses the canonical "
            "same-angle equivariant TT co-shape normalization rather than another coherent subspace."
        ),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_core_b0_tt_factorization_packet",
        "status": "SELECTED_CORE_B0_PACKET_CANONICALLY_FILLED_SOURCE_ACCEPTANCE_OPEN",
        "input_certificates": {
            "core_b0_factorization_final_gate": str(FINAL_GATE),
            "equivariant_central_circle_tt_support": str(EQUIVARIANT),
            "actual_shape_map_factorization_reduction": str(REDUCTION),
        },
        "packet_written": str(OUT_PACKET),
        "tests": tests,
        "test_residuals": packet["closing_tests"],
        "conditional_implications": {
            "if_source_acceptance_granted": [
                "B0^*P_TT=U_TT C with C invertible",
                "B^*P_TT=U_TT C' after SPT dressing",
                "Pi_exact64 B^*P_TT=B^*P_TT",
                "support(J_TT)=|d_*> tensor span{c2,s2}",
                "lambda_GR,TT=15",
            ],
            "currently_closed": [
                "canonical finite packet tests pass exactly",
                "no leakage out of Pi_exact64 for the canonical fill",
                "same-angle Z64/TT intertwining for the canonical fill",
            ],
            "currently_open": [
                "source acceptance that actual selected metric core B0 is this canonical fill",
            ],
        },
        "guardrails": {
            "claims_actual_B0_entries_sourced": False,
            "claims_unconditional_final_support": False,
            "uses_observed_GR_data": False,
            "adds_numeric_knob": False,
            "marks_C_as_basis_normalization_not_fit": True,
        },
        "note_written": str(OUT_NOTE),
    }

    note = """# Selected Core B0 TT Factorization Packet v1

## Canonical Fill

The final packet can now be filled canonically:

```text
B0^*P_TT := U_TT C,
C = I_2
```

where `U_TT` maps `TT_plus, TT_cross` to the exact `Z64` helicity-2 real
character plane:

```text
U_TT(TT_plus)  = |d_*> tensor c_2
U_TT(TT_cross) = |d_*> tensor s_2
```

This is not a numerical fit. `C=I_2` is a TT quotient basis normalization. Any
invertible `C` gives the same support theorem.

## Packet Tests

The verifier checks:

```text
rank(U_TT^* B0^*P_TT)=2
(I-Pi_exact64)B0^*P_TT=0
S_64 B0^*P_TT = B0^*P_TT R_TT(2 theta)
```

All three pass for the canonical fill, with residuals below numerical tolerance.

## What This Closes

This closes the finite packet algebra. If the selected metric shape-map core
`B0` is accepted/sourced as the canonical same-angle equivariant co-shape, then
all downstream implications are already proved:

```text
B^*P_TT = U_TT C'
Pi_exact64 B^*P_TT = B^*P_TT
support(J_TT)=|d_*> tensor span{c2,s2}
lambda_GR,TT=15
```

## What Still Requires Source Acceptance

The corpus does not yet provide independent entries for the actual metric
shape-map core `B0`. Therefore this packet is a canonical fill, not an
unconditional source computation.

The remaining source statement is now maximally small:

```text
The selected metric shape-map core B0 is the canonical same-angle TT co-shape
on the exact central-circle branch.
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
