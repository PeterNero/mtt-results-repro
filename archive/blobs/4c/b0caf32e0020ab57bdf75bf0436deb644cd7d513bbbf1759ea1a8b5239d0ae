from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MTT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

REDUCTION = ROOT / "certificates" / "actual_shape_map_factorization_reduction_certificate.json"
EQUIVARIANT = ROOT / "certificates" / "equivariant_central_circle_tt_support_theorem_certificate.json"

QG = MTT / "12 Quantum Gravity" / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"
CENTRAL = (
    MTT
    / "13 Standard Model & Topology-Only Constraints"
    / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md"
)

OUT_CERT = ROOT / "certificates" / "core_b0_factorization_final_gate_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Core_B0_Factorization_Final_Gate_v1.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    reduction = load(REDUCTION)
    equivariant = load(EQUIVARIANT)
    qg = read(QG)
    central = read(CENTRAL)

    source_tests = {
        "shape_map_core_B0_exists": has(qg, "B_0", "Metric shape map", "DG(\\Psi_\\ast)")
        or has(qg, "B_0", "DG(\\Psi_\\ast)"),
        "shape_map_core_B0_formula_sourced": has(
            qg,
            "B_0 \\;:=\\; \\int",
            "S_t",
            "DG(\\Psi_\\ast)",
            "A_{\\mathrm{int}}",
        ),
        "spectral_filter_B0_positive_commuting_exists": has(
            qg,
            "B_0 := \\int_0^\\infty e^{-sL}",
            "bounded positive operator commuting with $L$",
        ),
        "spectral_filter_B0_is_not_shape_map_core": has(qg, "Define the bounded operator", "$$B := f(L)$$"),
        "central_circle_shared_gravity_sourced": has(
            central,
            "Gravity, by contrast, operates on the shared circle itself",
        )
        or has(central, "Gravity, by contrast, operates on the shared coherence channel"),
        "central_circle_finite_holonomy_sourced": has(central, "finite subgroup of $U(1)$"),
        "literal_B0_to_UTT_factorization_absent": "B0^*P_TT = U_TT C" not in qg
        and "B_0^*P_TT = U_TT C" not in qg,
        "literal_same_angle_B0_absent": "same-angle" not in qg and "same central-circle angle" not in qg,
    }

    false_closure_routes = {
        "use_filter_B0_commuting_with_L": {
            "tempting": source_tests["spectral_filter_B0_positive_commuting_exists"],
            "valid_for_final_shape_support": False,
            "reason": (
                "This B0 is introduced after defining B=f(L), a spectral filter. It is not the metric "
                "shape-map core in B=DG(Psi*)Pi_coh, so its positivity/commutation cannot identify "
                "B0^*P_TT with the exact central helicity plane."
            ),
        },
        "use_central_circle_gravity_text_directly": {
            "tempting": source_tests["central_circle_shared_gravity_sourced"],
            "valid_for_final_shape_support": False,
            "reason": (
                "The central-circle text identifies the physical channel, but does not compute or state the "
                "core co-shape matrix B0^*P_TT=U_TT C."
            ),
        },
        "use_spt_dressing_to_select_support": {
            "tempting": reduction["status"] == "DRESSED_SHAPE_MAP_REDUCED_TO_CORE_B0_SAME_ANGLE_FACTORISATION",
            "valid_for_final_shape_support": False,
            "reason": (
                "The reduction theorem proves SPT dressing preserves support selected by B0; it does not "
                "select that support on behalf of B0."
            ),
        },
    }

    final_packet = {
        "name": "SelectedCoreB0TTFactorizationPacket.v1",
        "operator_to_compute": "B0^*P_TT",
        "required_basis_data": [
            "TT plus/cross physical quotient basis",
            "selected exact d_* Z64 real character basis U_TT=(c2,s2)",
            "inner products defining the adjoint of the metric shape-map core B0",
        ],
        "closing_tests": {
            "rank_test": "rank(U_TT^* B0^*P_TT)=2",
            "no_leakage_test": "(I-Pi_exact64)B0^*P_TT=0",
            "same_angle_test": "S_64 B0^*P_TT = B0^*P_TT R_TT(2 theta) up to the selected convention",
        },
        "if_passes": [
            "B0^*P_TT=U_TT C with C invertible",
            "B^*P_TT=U_TT C' after SPT dressing",
            "Pi_exact64 B^*P_TT=B^*P_TT",
            "support(J_TT)=|d_*> tensor span{c2,s2}",
            "lambda_GR,TT=15 in normalized internal exact-branch units",
        ],
    }

    decision = {
        "final_support_closed_now": False,
        "why": (
            "The corpus supplies B's SPT factorization and central-circle physical motivation, but not the "
            "actual metric shape-map core matrix or a theorem that it factors through U_TT."
        ),
        "minimal_remaining_work": "compute or source SelectedCoreB0TTFactorizationPacket.v1",
        "honest_status": "FINAL_GATE_IS_EXPLICIT_CORE_B0_PACKET_NOT_YET_FILLED",
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "core_b0_factorization_final_gate",
        "status": "FINAL_B0_FACTORISATION_GATE_EXPLICIT_NOT_CLOSED",
        "input_certificates": {
            "actual_shape_map_factorization_reduction": str(REDUCTION),
            "equivariant_central_circle_tt_support": str(EQUIVARIANT),
        },
        "source_files": {
            "qg": str(QG),
            "central_circle": str(CENTRAL),
        },
        "source_tests": source_tests,
        "false_closure_routes": false_closure_routes,
        "final_packet": final_packet,
        "decision": decision,
        "guardrails": {
            "claims_final_support_closed": False,
            "uses_filter_B0_as_shape_B0": False,
            "uses_central_circle_interpretation_as_matrix_proof": False,
            "uses_observed_GR_data": False,
            "adds_numeric_knob": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = """# Core B0 Factorization Final Gate v1

## Decision

The final exact-support theorem is not honestly closed yet.

We have reduced it to the smallest remaining object:

```text
B0^*P_TT = U_TT C
```

where `B0` is the metric shape-map core from the QG SPT factorization,
`U_TT` is the same-angle helicity-2 carrier into the exact `Z64 d_*` branch, and
`C` must be invertible on the TT plus/cross quotient.

## What Does Not Close It

The QG paper also introduces a spectral-filter object with a similar name:

```text
B := f(L),
B0 := integral e^{-sL} ...
```

and proves that this filter-core is positive and commutes with `L`. That is
useful for damping and filter independence, but it is not the same object as
the metric shape-map core in

```text
B = DG(Psi*)Pi_coh = exp(-tau0 E/2) B0 exp(-tau0 A_int/2).
```

Therefore we must not use the spectral-filter `B0` as a proof of the metric
co-shape support.

The central-circle paper also gives the right physical channel: gravity operates
on the shared circle/coherence channel. But it does not compute the matrix
`B0^*P_TT`, so it cannot close the final support identity by itself.

## Final Packet

To finish the theorem, fill:

```text
SelectedCoreB0TTFactorizationPacket.v1
```

with these checks:

```text
rank(U_TT^* B0^*P_TT)=2
(I-Pi_exact64)B0^*P_TT=0
S_64 B0^*P_TT = B0^*P_TT R_TT(2 theta)
```

If those pass, then all remaining implications are already verified:

```text
B0^*P_TT=U_TT C
B^*P_TT=U_TT C'
Pi_exact64 B^*P_TT=B^*P_TT
support(J_TT)=|d_*> tensor span{c2,s2}
lambda_GR,TT=15
```

## Status

This is a good kind of open problem: the theorem is no longer vague. It is a
specific finite core-map packet. The next genuine progress must supply the
metric shape-map core entries or a source theorem proving the same three packet
checks.
"""

    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
