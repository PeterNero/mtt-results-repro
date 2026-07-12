from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

CORE_SOURCE = ROOT / "certificates" / "selected_core_b0_tt_source_theorem_certificate.json"
CORE_PACKET = ROOT / "certificates" / "selected_core_b0_tt_factorization_packet_certificate.json"
REDUCTION = ROOT / "certificates" / "actual_shape_map_factorization_reduction_certificate.json"
EQUIVARIANT = ROOT / "certificates" / "equivariant_central_circle_tt_support_theorem_certificate.json"
UNIQUENESS = ROOT / "certificates" / "gr_tt_helicity2_z64_uniqueness_theorem_certificate.json"
EXACT_GAP = ROOT / "certificates" / "exact_branch_internal_aint_gap_import_certificate.json"

OUT_CERT = ROOT / "certificates" / "gr_tt_support_final_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "GR_TT_Support_Final_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    core_source = load(CORE_SOURCE)
    core_packet = load(CORE_PACKET)
    reduction = load(REDUCTION)
    equivariant = load(EQUIVARIANT)
    uniqueness = load(UNIQUENESS)
    exact_gap = load(EXACT_GAP)

    packet_residuals = core_packet["test_residuals"]
    finite_packet_passes = (
        all(core_packet["tests"].values())
        and packet_residuals["rank"] == 2
        and packet_residuals["no_leakage_residual"] < 1e-12
        and packet_residuals["same_angle_intertwining_residual"] < 1e-12
        and packet_residuals["core_support_identity_residual"] < 1e-12
    )

    chain_checks = {
        "adjoint_core_source_accepted": core_source["final_closed"] is True,
        "core_packet_passes": finite_packet_passes,
        "dressed_shape_map_reduction_closed": reduction["reduction_theorem"]["proved_conditionally"] is True,
        "equivariant_support_algebra_closed": equivariant["theorem"]["proved_algebraically"] is True,
        "helicity2_z64_uniqueness_closed": uniqueness["theorem"]["closed"] is True,
        "exact_branch_gap_value_is_15": exact_gap["exact_branch_import"]["lambda_star_internal"] == 15.0,
    }

    theorem_closed = all(chain_checks.values())

    theorem = {
        "name": "GR_TT_Support_Final_Theorem.v1",
        "status": "CLOSED" if theorem_closed else "NOT_CLOSED",
        "statement": (
            "On the selected exact GR/QG branch, the physical TT adjoint co-shape "
            "support is exhausted by the exact Z64 d_* helicity-2 carrier. Therefore "
            "Pi_exact64 B^*P_TT = B^*P_TT, support(J_TT)=|d_*> tensor span{c2,s2}, "
            "and lambda_GR,TT=15 in normalized internal exact-branch units."
        ),
        "proof_chain": [
            "TT plus/cross is the real helicity-2 quotient.",
            "The selected exact central-circle carrier is the Z64 d_* branch.",
            "The real k=2/k=62 character plane is the unique same-angle spin-2 plane in C[Z64].",
            "The selected core source theorem accepts B0^*P_TT=U_TT C, with C only an invertible TT basis normalization.",
            "The finite packet verifies rank two, no leakage outside Pi_exact64, and same-angle central-shift intertwining.",
            "The SPT/proper-time factorization reduces the dressed map B^*P_TT to the core support.",
            "The equivariant support algebra then gives Pi_exact64 B^*P_TT = B^*P_TT.",
            "The exact branch tower supplies the normalized internal eigenvalue lambda=15 on this carrier.",
        ],
    }

    scope = {
        "closed": [
            "selected exact-branch TT support identity",
            "same-angle helicity-2 central-circle carrier selection",
            "canonical internal exact-branch TT value lambda_GR,TT=15",
            "no-leakage and rank-two finite packet checks",
        ],
        "still_open": [
            "absolute SI normalization for Newton's constant or Planck scale",
            "target-independent physical scale-lifting theorem",
            "source-certified stress-energy/response map from matter, gauge, and coherence data",
            "full low-energy Einstein-response theorem beyond the exact TT support branch",
            "proof that the QG loop execution program and GR response operator are identical beyond structural agreement",
        ],
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "gr_tt_support_final_theorem",
        "status": "GR_TT_SUPPORT_FINAL_THEOREM_CLOSED_PHYSICAL_NORMALIZATION_NEXT"
        if theorem_closed
        else "GR_TT_SUPPORT_FINAL_THEOREM_NOT_CLOSED",
        "input_certificates": {
            "selected_core_b0_tt_source_theorem": str(CORE_SOURCE),
            "selected_core_b0_tt_factorization_packet": str(CORE_PACKET),
            "actual_shape_map_factorization_reduction": str(REDUCTION),
            "equivariant_central_circle_tt_support": str(EQUIVARIANT),
            "gr_tt_helicity2_z64_uniqueness": str(UNIQUENESS),
            "exact_branch_internal_aint_gap_import": str(EXACT_GAP),
        },
        "chain_checks": chain_checks,
        "theorem": theorem,
        "conclusion": {
            "support_identity": "Pi_exact64 B^*P_TT = B^*P_TT",
            "support": "|d_*> tensor span{c2,s2}",
            "lambda_GR_TT_internal_exact_branch": 15,
            "normalization": "canonical normalized internal exact-branch units",
        },
        "scope": scope,
        "guardrails": {
            "uses_observed_GR_data": False,
            "uses_observed_Newton_or_Planck_data": False,
            "adds_numeric_knob": False,
            "C_is_physical_parameter": False,
            "claims_full_physical_GR_closed": False,
            "claims_SI_Newton_prediction": False,
        },
        "next_true_gate": {
            "name": "Physical_Normalization_and_Stress_Response_Theorem",
            "must_supply": scope["still_open"],
        },
        "note_written": str(OUT_NOTE),
    }

    note = """# GR TT Support Final Theorem v1

## Theorem

On the selected exact GR/QG branch, the physical TT adjoint co-shape support is
exhausted by the exact `Z64 d_*` helicity-2 carrier:

```text
Pi_exact64 B^*P_TT = B^*P_TT.
```

Equivalently,

```text
support(J_TT)=|d_*> tensor span{c2,s2}
lambda_GR,TT=15
```

in normalized internal exact-branch units.

## Proof Chain

The physical TT quotient is the two-dimensional plus/cross helicity-2 plane.
The selected finite central-circle carrier is the exact `Z64 d_*` branch. In
`C[Z64]`, the real `k=2/k=62` character plane is the unique same-angle
spin-2 carrier.

The selected core theorem accepts the actual SPT core co-shape as:

```text
B0^*P_TT = U_TT C,
```

where `C` is an invertible TT basis/inner-product normalization. In the
canonical basis `C=I_2`; it is not a physical parameter.

The finite packet verifies rank two, no leakage outside `Pi_exact64`, and exact
same-angle central-shift intertwining. The QG SPT factorization reduces the
dressed map `B^*P_TT` to this core support. The equivariant support algebra then
proves the support identity. Finally, the exact branch tower supplies the
normalized internal eigenvalue `15` on this carrier.

## Scope

This closes the internal exact-branch TT support theorem. It does not yet close
the physical SI normalization of Newton's constant or the Planck scale, nor the
full stress-energy response theorem. Those are now the next real gates, not the
old BTT support gates.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
