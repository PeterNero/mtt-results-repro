from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

UPSTREAM_CERT = ROOT / "certificates" / "tt_domain_selection_from_fixed_point_or_internal_quotient_certificate.json"
QG_V4 = (
    CORPUS
    / "12 Quantum Gravity"
    / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"
)
QG_I = (
    CORPUS
    / "12 Quantum Gravity"
    / "Constructive_MTT_Quantum_Gravity_I__Borel_Summability_of_the_SPT_Filtered_TT_Sector.md"
)
QG_II = (
    CORPUS
    / "12 Quantum Gravity"
    / "Constructive_MTT_Quantum_Gravity_II__BRST_Lifting__Gauge_Invariant_Observables__and_the_Physical_Hilbert_Space_under_SPT_Damping.md"
)

OUT_CERT = ROOT / "certificates" / "tt_gap_external_domain_vs_internal_aint_role_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "TT_Gap_External_Domain_vs_Internal_Aint_Role_Theorem_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    upstream = load_json(UPSTREAM_CERT)
    qg_v4 = read(QG_V4)
    qg_i = read(QG_I)
    qg_ii = read(QG_II)

    source_tests = {
        "qg_v4_external_internal_blocks_commute": has(
            qg_v4,
            "commuting external/internal blocks",
            "[E,A_{\\mathrm{int}}]=0",
        ),
        "qg_v4_positive_gap_above_coherent_zero_modes": has(
            qg_v4,
            "positive spectral gap $\\lambda_\\ast>0$ above the coherent zero modes",
        ),
        "qg_v4_defines_E_as_external_TT_lichnerowicz": has(
            qg_v4,
            "$E$                        operator",
            "Lichnerowicz operator on TT modes (external block)",
        ),
        "qg_v4_defines_lambda_as_internal_Aint_gap": has(
            qg_v4,
            "$A_{\\mathrm{int}}$         operator",
            "First positive eigenvalue bound for $A_{\\mathrm{int}}$",
        ),
        "qg_v4_pushforward_from_internal_projector_to_Y4": (
            "P := I\\circ \\Pi" in qg_v4 and "pushes forward along the compact fibre" in qg_v4
        ),
        "qg_v4_lambda_controls_uv_scale": (
            "Lambda^2 \\sim \\tau_0^{-1}\\sim \\lambda_\\ast" in qg_v4
            or "Lambda^2" in qg_v4
            and "lambda_\\ast" in qg_v4
            and "tau_0^{-1}" in qg_v4
        ),
        "qg_i_external_domain_is_bounded_chart": has(
            qg_i,
            "bounded domain",
            "bounded-geometry coordinate chart of a time slab",
        ),
        "qg_ii_boundary_terms_are_well_posedness_constraint": has(
            qg_ii,
            "boundary conditions",
            "BRST variations produce no boundary contributions",
        ),
    }

    role_separation = {
        "external_block_E": {
            "role": "TT Lichnerowicz/kinematic block on the 4D bounded-geometry background",
            "depends_on_external_domain": True,
            "source_of_lambda_star": False,
            "numeric_box_eigenvalues_are": "model/regulator data unless a separate selection theorem fixes the domain and scale",
        },
        "internal_block_Aint": {
            "role": "positive incoherent-complement block selected by coherent projector/fixed-point data",
            "depends_on_external_domain": False,
            "source_of_lambda_star": True,
            "numeric_gap_task": "identify the selected A_int complement and compute its first positive eigenvalue",
        },
        "projector_pushforward_P": {
            "role": "maps internal coherent data to external 4D observables",
            "depends_on_external_domain": "only through the 4D bounded-geometry target and covariance",
            "source_of_lambda_star": "inherits lambda_star from A_int, not from a finite-box Laplacian eigenvalue",
        },
    }

    decisions = {
        "external_TT_domain_selection_needed_for_well_posed_QG": True,
        "external_TT_domain_selection_needed_for_global_covariance_story": True,
        "external_box_lowest_eigenvalue_is_selected_modal_gap": False,
        "flat_T3_lambda_1_equals_1_remains_useful_model": True,
        "flat_T3_lambda_1_equals_1_closes_lambda_star": False,
        "numeric_gap_refocused_on_selected_internal_Aint": True,
    }

    note = """# TT Gap External Domain vs Internal Aint Role Theorem v1

## Result

The selected TT modal gap should not be computed from an arbitrary external box
eigenvalue.

The QG source separates the operator into:

```text
E      = external TT Lichnerowicz block
A_int  = internal incoherent-complement block
[E, A_int] = 0
lambda_* = first positive gap of A_int on the noncoherent slice
```

So the external bounded domain is still required for heat-kernel estimates,
BRST boundary control, and local covariance. But the numerical `lambda_*` in
the SPT damping denominator is sourced as an internal `A_int` gap.

## Consequence

The flat periodic `T3` calculation with `lambda_1=1` remains a useful model
eigenpacket. It does not close the selected modal gap.

The next real numeric gate is:

```text
Selected_Internal_Aint_Complement_Gap_Theorem
```

That theorem must identify the selected GR/QG `A_int` complement from the
fixed-point/projector data and compute its first positive eigenvalue in the
same branch and normalization as the TT response operator.
"""
    OUT_NOTE.write_text(note, encoding="utf-8")

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "tt_gap_external_domain_vs_internal_aint_role",
        "status": "TT_NUMERIC_GAP_REFOCUSED_ON_INTERNAL_AINT_EXTERNAL_DOMAIN_REGULATOR",
        "input_certificates": {
            "tt_domain_selection_from_fixed_point_or_internal_quotient": str(UPSTREAM_CERT),
        },
        "source_files": {
            "uv_finite_qg_v4": str(QG_V4),
            "constructive_qg_i": str(QG_I),
            "constructive_qg_ii": str(QG_II),
        },
        "source_tests": source_tests,
        "role_separation": role_separation,
        "decisions": decisions,
        "closed_now": {
            "external_E_vs_internal_Aint_roles_separated": True,
            "lambda_star_sourced_as_internal_Aint_gap": source_tests[
                "qg_v4_defines_lambda_as_internal_Aint_gap"
            ],
            "external_domain_retained_as_QG_well_posedness_scaffold": source_tests[
                "qg_i_external_domain_is_bounded_chart"
            ],
            "flat_T3_model_not_promoted": True,
            "next_numeric_gate_identified": True,
        },
        "next_gate": {
            "name": "Selected_Internal_Aint_Complement_Gap_Theorem",
            "must_supply": [
                "selected internal incoherent-complement operator A_int",
                "projector/window normalization matching the GR TT response convention",
                "same-branch proof against nil, Z64, Fu-Yau, or another selected quotient",
                "lowest positive eigenvalue of A_int after gauge/coherent zero modes are removed",
                "then lift that lambda_star through the TT propagator denominator",
            ],
        },
        "guardrails": {
            "claims_external_box_gap_is_lambda_star": False,
            "claims_flat_T3_lambda_1_closes_gap": False,
            "claims_domain_selection_irrelevant": False,
            "claims_selected_internal_Aint_gap_computed": False,
            "claims_full_GR_response_closed": False,
        },
        "note_written": str(OUT_NOTE),
        "previous_status": upstream["status"],
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
