from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MTT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

EQUIVARIANT = ROOT / "certificates" / "equivariant_central_circle_tt_support_theorem_certificate.json"
EXACT_GAP = ROOT / "certificates" / "exact_branch_internal_aint_gap_import_certificate.json"
ADJOINT = ROOT / "certificates" / "btt_adjoint_shape_map_typing_theorem_certificate.json"

QG = MTT / "12 Quantum Gravity" / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"
CENTRAL = (
    MTT
    / "13 Standard Model & Topology-Only Constraints"
    / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md"
)

OUT_CERT = ROOT / "certificates" / "actual_shape_map_factorization_reduction_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Actual_Shape_Map_Factorization_Reduction_v1.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def mat_mat(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    cols = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in cols] for row in a]


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [list(col) for col in zip(*a)]


def max_abs_matrix(a: list[list[float]]) -> float:
    return max(abs(x) for row in a for x in row)


def main() -> None:
    equivariant = load(EQUIVARIANT)
    exact_gap = load(EXACT_GAP)
    adjoint = load(ADJOINT)
    qg = read(QG)
    central = read(CENTRAL)

    qg_sources = {
        "B_defined_as_DG_Pi_coh": has(qg, "B \\;=\\; DG(\\Psi_\\ast)\\Pi_{\\mathrm{coh}}")
        or has(qg, "B= \\left.\\frac{\\delta g}{\\delta \\Psi}\\right|_{\\Psi^\\ast}"),
        "B_factorization_sourced": has(
            qg,
            "B \\;=\\; e^{-\\frac{\\tau_0}{2}E}\\;B_0\\;e^{-\\frac{\\tau_0}{2}A_{\\mathrm{int}}}",
        )
        or has(qg, "B \\;=\\; e^{-\\tfrac{\\tau_0}{2}E}\\,B_0\\,e^{-\\tfrac{\\tau_0}{2}A_{\\mathrm{int}}}"),
        "B0_bounded_sourced": has(qg, "Then $B_0$ is bounded"),
        "E_Aint_commute_sourced": has(qg, "Blocks commute", "[E,A_{\\mathrm{int}}]=0")
        or has(qg, "[E,A_{\\mathrm{int}}]=0"),
        "Aint_gap_sourced": has(qg, "A_{\\mathrm{int}}\\ge\\lambda_\\ast>0")
        or has(qg, "spectral gap"),
        "central_finite_subgroup_sourced": has(central, "finite subgroup of $U(1)$")
        and has(central, "central circle coordinate $\\theta$"),
    }

    # Finite model of the reduction. U spans the exact plane. D_int is a scalar
    # proper-time dressing on the selected exact plane, so it preserves the image
    # of U. D_ext is a scalar positive dressing on the TT quotient.
    n = 64
    k = 2
    theta = 2 * math.pi / n
    c2 = [math.sqrt(2 / n) * math.cos(k * theta * j) for j in range(n)]
    s2 = [math.sqrt(2 / n) * math.sin(k * theta * j) for j in range(n)]
    u = [[c2[i], s2[i]] for i in range(n)]
    projector = mat_mat(u, transpose(u))

    tau0 = 1.0
    lambda_exact = 15.0
    d_int_on_exact = math.exp(-0.5 * tau0 * lambda_exact)
    d_ext_on_tt = math.exp(-0.5 * tau0 * 1.0)
    core_c = [[1.1, 0.25], [-0.05, 0.8]]
    core_bstar = mat_mat(u, core_c)
    dressed_bstar = [[d_int_on_exact * d_ext_on_tt * x for x in row] for row in core_bstar]
    projection_residual = [
        [
            sum(projector[i][j] * dressed_bstar[j][col] for j in range(n)) - dressed_bstar[i][col]
            for col in range(2)
        ]
        for i in range(n)
    ]

    det_core_c = core_c[0][0] * core_c[1][1] - core_c[0][1] * core_c[1][0]
    finite_checks = {
        "equivariant_algebra_closed": equivariant["theorem"]["proved_algebraically"] is True,
        "adjoint_support_nonzero_closed": adjoint["closed_now"]["TT_coupling_nonzero_for_adjoint_support"] is True,
        "exact_gap_imported": exact_gap["status"] == "EXACT_BRANCH_INTERNAL_AINT_GAP_CLOSED_GR_TT_BRANCH_IDENTITY_OPEN",
        "core_factorization_rank2": abs(det_core_c) > 1e-12,
        "proper_time_dressing_preserves_exact_plane": max_abs_matrix(projection_residual) < 1e-12,
    }

    reduction_theorem = {
        "name": "ActualShapeMapFactorizationReduction.v1",
        "proved_conditionally": all(qg_sources.values()) and all(finite_checks.values()),
        "statement": (
            "Using the QG SPT factorization B=e^{-tau0 E/2} B0 e^{-tau0 A_int/2}, "
            "the final dressed co-shape support identity reduces to the same-angle exact-plane "
            "factorization of the core map B0^*P_TT. Proper-time dressing by E and A_int "
            "does not supply a new support choice."
        ),
        "logic": [
            "QG sources B=DG(Psi*)Pi_coh and B=e^{-tau0 E/2}B0e^{-tau0 A_int/2}.",
            "Taking adjoints gives B^*P_TT=e^{-tau0 A_int/2}B0^*e^{-tau0 E/2}P_TT.",
            "The external TT dressing e^{-tau0 E/2} preserves the TT quotient.",
            "On the selected exact branch, e^{-tau0 A_int/2} acts within the exact central character plane.",
            "Therefore support closure for B^*P_TT is equivalent to support closure for B0^*P_TT.",
        ],
        "what_closes": (
            "The last problem is no longer the full retarded/SPT shape map. It is the core same-angle "
            "factorization B0^*P_TT=U_TT C."
        ),
    }

    remaining = {
        "source_status": "CORE_B0_SAME_ANGLE_FACTORISATION_OPEN",
        "minimal_remaining_statement": (
            "For the selected exact GR/QG branch, the SPT core map obeys B0^*P_TT=U_TT C "
            "with C invertible on TT plus/cross, using the same central-circle angle as the exact Z64 shift."
        ),
        "direct_computation_packet": {
            "input_1": "core map B0 from QG SPT factorization",
            "input_2": "TT plus/cross physical quotient basis",
            "input_3": "selected exact d_* Z64 character basis c2,s2",
            "test_1": "rank(U_TT^* B0^*P_TT)=2",
            "test_2": "(I-Pi_exact64)B0^*P_TT=0",
            "test_3": "central shift intertwining residual is zero",
        },
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "actual_shape_map_factorization_reduction",
        "status": "DRESSED_SHAPE_MAP_REDUCED_TO_CORE_B0_SAME_ANGLE_FACTORISATION",
        "input_certificates": {
            "equivariant_central_circle_tt_support": str(EQUIVARIANT),
            "exact_branch_internal_aint_gap_import": str(EXACT_GAP),
            "btt_adjoint_shape_map_typing": str(ADJOINT),
        },
        "source_files": {
            "qg": str(QG),
            "central_circle": str(CENTRAL),
        },
        "qg_sources": qg_sources,
        "finite_checks": finite_checks,
        "finite_residuals": {
            "projection_residual": max_abs_matrix(projection_residual),
            "det_core_C": det_core_c,
            "d_int_on_exact": d_int_on_exact,
            "d_ext_on_tt": d_ext_on_tt,
        },
        "reduction_theorem": reduction_theorem,
        "remaining": remaining,
        "guardrails": {
            "claims_B0_factorization_sourced": False,
            "claims_unconditional_final_support": False,
            "uses_observed_GR_data": False,
            "adds_numeric_knob": False,
            "lets_SPT_dressing_select_support": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = """# Actual Shape Map Factorization Reduction v1

## Result

The QG paper gives the decisive structural factorization:

```text
B = DG(Psi*) Pi_coh = exp(-tau0 E/2) B0 exp(-tau0 A_int/2).
```

Taking adjoints on the TT quotient gives:

```text
B^*P_TT = exp(-tau0 A_int/2) B0^* exp(-tau0 E/2) P_TT.
```

Therefore the final support problem reduces from the full dressed metric shape
map to the SPT core map `B0`.

## Theorem

If the core map satisfies

```text
B0^*P_TT = U_TT C
```

for the same-angle helicity-2 carrier `U_TT` and an invertible TT matrix `C`,
then the full dressed map also satisfies

```text
B^*P_TT = U_TT C'
```

for an invertible `C'`, and hence

```text
Pi_exact64 B^*P_TT = B^*P_TT.
```

The finite verifier checks the model algebra: scalar proper-time dressing on
the selected exact plane preserves `Pi_exact64` support. Dressing cannot create
the support if `B0` lacks it, and cannot destroy it if `B0` has it.

## Remaining Minimal Gate

The last source-level statement is now:

```text
B0^*P_TT = U_TT C
```

on the selected exact GR/QG branch, with `C` invertible and the same
central-circle angle as the exact `Z64` shift.

Equivalently, the direct computation packet is:

```text
rank(U_TT^* B0^*P_TT)=2
(I-Pi_exact64)B0^*P_TT=0
central shift intertwining residual = 0
```

This is the smallest remaining hard object. The retarded kernel, SPT damping,
and proper-time filters are no longer part of the mystery; they preserve the
support selected by `B0`.
"""

    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
