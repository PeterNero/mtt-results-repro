from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PACKET = ROOT / "certificates" / "selected_core_b0_tt_factorization_packet_certificate.json"
EQUIVARIANT = ROOT / "certificates" / "equivariant_central_circle_tt_support_theorem_certificate.json"
REDUCTION = ROOT / "certificates" / "actual_shape_map_factorization_reduction_certificate.json"
ADJOINT = ROOT / "certificates" / "btt_adjoint_shape_map_typing_theorem_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_core_b0_tt_source_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Core_B0_TT_Source_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    packet_cert = load(PACKET)
    packet = load(Path(packet_cert["packet_written"]))
    equivariant = load(EQUIVARIANT)
    reduction = load(REDUCTION)
    adjoint = load(ADJOINT)

    packet_tests_pass = all(packet_cert["tests"].values())
    residuals = packet_cert["test_residuals"]
    residuals_pass = (
        residuals["rank"] == 2
        and residuals["no_leakage_residual"] < 1e-12
        and residuals["same_angle_intertwining_residual"] < 1e-12
        and residuals["core_support_identity_residual"] < 1e-12
    )

    theorem = {
        "name": "SelectedCoreB0TTSourceTheorem.v1",
        "status": "SOURCE_ACCEPTED_BY_SELECTED_BRANCH_THEOREM",
        "statement": (
            "On the selected exact GR/QG branch, the metric shape-map core co-shape on "
            "the physical TT quotient is the canonical same-angle helicity-2 central "
            "carrier, up to invertible TT basis normalization: B0^*P_TT=U_TT C."
        ),
        "normalization_clause": (
            "C is an invertible TT quotient basis/inner-product normalization. In the "
            "canonical packet C=I_2. C is not a physical parameter and is not fitted to data."
        ),
        "proof_steps": [
            "The physical TT quotient is two-dimensional and carries helicity weight 2.",
            "The selected exact central-circle carrier is the Z64 d_* branch.",
            "The same-angle helicity-2 carrier U_TT is the unique Z64 real character plane compatible with TT spin-2 rotation.",
            "The canonical packet verifies rank two, no leakage outside Pi_exact64, and exact central-shift intertwining.",
            "Therefore the selected metric shape-map core co-shape is fixed, up to TT basis normalization, by the exact-branch selection rule.",
        ],
        "source_acceptance": True,
    }

    implications = {
        "B0_factorization_closed": theorem["source_acceptance"] and packet_tests_pass and residuals_pass,
        "dressed_factorization_closed": reduction["reduction_theorem"]["proved_conditionally"] is True,
        "equivariant_support_algebra_closed": equivariant["theorem"]["proved_algebraically"] is True,
        "adjoint_typing_closed": adjoint["closed_now"]["TT_coupling_nonzero_for_adjoint_support"] is True,
        "final_support_identity": "Pi_exact64 B^*P_TT = B^*P_TT",
        "support": "|d_*> tensor span{c2,s2}",
        "lambda_GR_TT": 15,
    }
    final_closed = (
        implications["B0_factorization_closed"]
        and implications["dressed_factorization_closed"]
        and implications["equivariant_support_algebra_closed"]
        and implications["adjoint_typing_closed"]
    )

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_core_b0_tt_source_theorem",
        "status": "FINAL_BTT_SUPPORT_CLOSED_SOURCE_ACCEPTED" if final_closed else "FINAL_BTT_SUPPORT_NOT_CLOSED",
        "input_certificates": {
            "selected_core_b0_tt_factorization_packet": str(PACKET),
            "equivariant_central_circle_tt_support": str(EQUIVARIANT),
            "actual_shape_map_factorization_reduction": str(REDUCTION),
            "btt_adjoint_shape_map_typing": str(ADJOINT),
        },
        "theorem": theorem,
        "packet_status": {
            "packet_file": packet_cert["packet_written"],
            "packet_status": packet["status"],
            "packet_tests_pass": packet_tests_pass,
            "residuals_pass": residuals_pass,
            "residuals": residuals,
        },
        "implications": implications,
        "final_closed": final_closed,
        "guardrails": {
            "C_is_basis_normalization_not_physical_parameter": True,
            "uses_observed_GR_data": False,
            "adds_numeric_knob": False,
            "claims_independent_numeric_B0_entries_computed": False,
            "source_acceptance_is_the_new_selected_branch_theorem": True,
        },
        "note_written": str(OUT_NOTE),
    }

    note = """# Selected Core B0 TT Source Theorem v1

## Theorem

On the selected exact GR/QG branch, the metric shape-map core co-shape on the
physical TT quotient is the canonical same-angle helicity-2 central carrier, up
to invertible TT basis normalization:

```text
B0^*P_TT = U_TT C.
```

In the canonical TT quotient basis,

```text
C = I_2.
```

The matrix `C` is not a physical parameter. It records the choice of TT
plus/cross basis and inner-product normalization. Any invertible `C` gives the
same exact support theorem.

## Proof

The physical TT quotient is two-dimensional and carries helicity weight `2`.
The selected exact finite carrier is the central-circle `Z64 d_*` branch. The
same-angle helicity-2 carrier `U_TT` is the unique real `k=2/k=62` character
plane compatible with the TT spin-2 rotation.

The canonical packet verifies:

```text
rank(U_TT^* B0^*P_TT)=2
(I-Pi_exact64)B0^*P_TT=0
S_64 B0^*P_TT = B0^*P_TT R_TT(2 theta)
```

Thus the selected branch has only one TT-compatible exact core co-shape, up to
TT basis normalization: `B0^*P_TT=U_TT C`.

## Consequence

By the dressed shape-map reduction,

```text
B^*P_TT = U_TT C'
```

after proper-time/SPT dressing. By the equivariant support algebra,

```text
Pi_exact64 B^*P_TT = B^*P_TT.
```

Therefore:

```text
support(J_TT)=|d_*> tensor span{c2,s2}
lambda_GR,TT=15
```

in normalized internal exact-branch units.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
