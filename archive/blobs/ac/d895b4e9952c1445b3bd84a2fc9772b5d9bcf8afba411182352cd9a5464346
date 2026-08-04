from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THETA_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\18 Theta-Closure & Execution Program")

EXACT_BRANCH = ROOT / "certificates" / "exact_branch_internal_aint_gap_import_certificate.json"
FINAL_GATE = ROOT / "certificates" / "gr_tt_exact_branch_identity_final_gate_certificate.json"
EXPLICIT_TT = ROOT / "certificates" / "explicit_gr_tt_aint_complement_construction_certificate.json"
STF_NOTE = ROOT / "proof_corpus" / "STF_Shear_TT_Bridge_v1.md"
Z64_SOURCE = THETA_REPO / "_md_v3_corrected" / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md"

OUT_CERT = ROOT / "certificates" / "tt_closure_strain_to_z64_tower_map_attempt_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "TT_Closure_Strain_to_Z64_Tower_Map_Attempt_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    exact = load(EXACT_BRANCH)
    final_gate = load(FINAL_GATE)
    explicit_tt = load(EXPLICIT_TT)
    stf_note = read(STF_NOTE)
    z64_text = read(Z64_SOURCE)

    lambda_star = exact["exact_branch_import"]["lambda_star_internal"]

    source_tests = {
        "formal_GR_TT_operator_scalar_on_two_polarizations": explicit_tt["closed_tests"][
            "rotational_covariance_forces_scalar_operator_on_TT"
        ],
        "formal_GR_TT_basis_plus_cross_sourced": (
            has(stf_note, "remaining dimension", "2", "plus", "cross")
            and has(stf_note, "h_TT_plus", "h_TT_cross")
        ),
        "z64_exact_branch_lambda15_closed": lambda_star == 15.0,
        "z64_exact_branch_schur_zero": exact["exact_branch_import"]["schur_correction"] == 0.0,
        "z64_exact_branch_retarded_kernel_closed": exact["closed_now"]["exact_branch_retarded_kernel_closed"],
        "z64_source_selects_single_tower_label": has(z64_text, "d_*=(2,2,2,2,2)", "C(d_*)=15"),
        "z64_source_declares_l64_tower_operator": has(z64_text, "L_64", "L_tower"),
        "source_has_TT_to_Z64_polarization_functor": False,
        "source_identifies_GR_TT_eta_with_15": False,
        "final_gate_already_exhausted_identity_source": final_gate["closed_now"][
            "full_GR_identity_source_exhausted_for_now"
        ],
    }

    conditional_theorem = {
        "name": "Conditional_TT_to_Z64_Polarization_Compression_Theorem",
        "hypothesis": (
            "There exists a source-certified isometric polarization functor "
            "U_TT: C^2 -> H_64 whose image lies in the selected exact branch "
            "lambda=15 eigenspace/fiber and whose quotient/projector/window "
            "normalization is the GR TT one."
        ),
        "calculation": "U_TT^* L_64 U_TT = 15 * I_2",
        "consequence": "eta_TT = lambda_GR_TT = 15 in canonical exact-branch internal units",
        "closed_algebraically": True,
        "closed_unconditionally_from_sources": False,
    }

    results = {
        "conditional_compression_theorem_closed": True,
        "exact_branch_gap_15_remains_closed": True,
        "TT_two_polarization_form_remains_closed": True,
        "unconditional_TT_to_Z64_map_closed": False,
        "full_GR_TT_gap_15_closed": False,
        "minimum_missing_object": "TT_Polarization_Functor_into_Exact_Z64_Branch",
        "why_missing_object_is_not_numeric": (
            "The missing datum is an operator/functor identity, not another scalar. "
            "Once supplied, the scalar is forced to be 15 by the exact branch certificate."
        ),
    }

    note = f"""# TT Closure-Strain to Z64 Tower Map Attempt v1

## Result

This closes the final gate as far as the current corpus honestly allows.

Closed conditionally:

```text
If U_TT: C^2 -> H_64 embeds the GR TT plus/cross quotient into the selected
exact Z64 branch eigenspace/fiber with the same projector/window normalization,
then U_TT^* L_64 U_TT = {lambda_star:g} I_2.
```

So the exact-branch compression would force:

```text
eta_TT = lambda_GR,TT = {lambda_star:g}
```

Open unconditionally:

```text
source-certified TT polarization functor into the exact Z64 branch
```

## Meaning

The final missing piece is no longer a free numerical coefficient. It is one
structural map:

```text
U_TT: span{{TT_plus, TT_cross}} -> selected exact central-circle Z64 branch
```

If this map is sourced or constructed, the scalar value follows immediately
from the already closed exact branch certificate. Without it, claiming full GR
TT closure would identify a two-polarization metric-response quotient with the
finite Z64 tower by assumption.

## Guardrail

This artifact does not claim that the Z64 eigenspace is two-dimensional and does
not claim that full GR has lambda_star=15. It proves the conditional compression
and names the exact remaining object needed for unconditional closure.
"""
    OUT_NOTE.write_text(note, encoding="utf-8")

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "tt_closure_strain_to_z64_tower_map_attempt",
        "status": "TT_TO_Z64_MAP_CONDITIONAL_COMPRESSION_CLOSED_SOURCE_FUNCTOR_OPEN",
        "input_certificates": {
            "exact_branch_internal_aint_gap_import": str(EXACT_BRANCH),
            "gr_tt_exact_branch_identity_final_gate": str(FINAL_GATE),
            "explicit_gr_tt_aint_complement_construction": str(EXPLICIT_TT),
        },
        "source_files": {
            "stf_bridge": str(STF_NOTE),
            "z64_exact_central_circle_branch": str(Z64_SOURCE),
        },
        "source_tests": source_tests,
        "conditional_theorem": conditional_theorem,
        "results": results,
        "guardrails": {
            "claims_unconditional_GR_TT_gap_15": False,
            "claims_Z64_eigenspace_two_dimensional": False,
            "claims_TT_to_Z64_functor_sourced": False,
            "claims_physical_dimensionful_gap": False,
            "claims_Newton_or_Planck_prediction": False,
        },
        "next_gate": {
            "name": "TT_Polarization_Functor_into_Exact_Z64_Branch",
            "must_supply": [
                "domain and codomain Hilbert spaces",
                "image of TT_plus and TT_cross inside the selected exact branch",
                "proof that the image lies in the lambda=15 fiber/eigenspace or a two-polarization fiber over it",
                "isometry or inner-product normalization in the GR TT convention",
                "BRST/diffeomorphism quotient compatibility",
                "projector/window equality with the exact central-circle damping branch",
            ],
        },
        "note_written": str(OUT_NOTE),
        "previous_status": final_gate["status"],
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
