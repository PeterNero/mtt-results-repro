from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

METRIC_SOURCE = ROOT / "certificates" / "world_in_world_z64_metric_source_map_certificate.json"
GLOBAL_DG = ROOT / "certificates" / "global_covariant_helicity2_dg_bundle_certificate.json"
GLOBAL_HESSIAN = ROOT / "certificates" / "global_tt_hessian_action_uniqueness_reduction_certificate.json"
OLD_TT_SUPPORT = ROOT / "certificates" / "gr_tt_support_final_theorem_certificate.json"
QG_SOURCE = (
    ROOT.parent
    / "12 Quantum Gravity"
    / "_work"
    / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4"
    / "main.tex"
)

OUT_CERT = ROOT / "certificates" / "massless_tt_pole_internal_gap_no_go_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Massless_TT_Pole_vs_Positive_Internal_Gap_NoGo_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def max_matrix_residual(matrix: list[list[float]], target: Fraction) -> float:
    target_float = float(target)
    return max(
        abs(matrix[0][0] - target_float),
        abs(matrix[1][1] - target_float),
        abs(matrix[0][1]),
        abs(matrix[1][0]),
    )


def main() -> None:
    metric = load(METRIC_SOURCE)
    global_dg = load(GLOBAL_DG)
    global_hessian = load(GLOBAL_HESSIAN)
    old_support = load(OLD_TT_SUPPORT)
    qg_text = QG_SOURCE.read_text(encoding="utf-8")

    lambda_gap = Fraction(int(metric["finite_data"]["lambda_star_internal"]), 1)
    metric_map_scale = Fraction(2, 1)
    strain_map_scale = Fraction(1, 1)
    metric_zero_value = metric_map_scale**2 / lambda_gap
    strain_zero_value = strain_map_scale**2 / lambda_gap

    metric_matrix = metric["finite_data"]["metric_B_Ainv_Bstar"]
    strain_matrix = metric["finite_data"]["log_strain_B_Ainv_Bstar"]
    metric_residual = max_matrix_residual(metric_matrix, metric_zero_value)
    strain_residual = max_matrix_residual(strain_matrix, strain_zero_value)

    # For Delta_c(E)=c^2/(E+lambda), the massless-pole residue is
    # lim_{E->0} E Delta_c(E)=0 whenever lambda>0.
    probe_values = [Fraction(1, 10**power) for power in range(1, 8)]
    metric_residue_probes = [
        float(E * metric_map_scale**2 / (E + lambda_gap)) for E in probe_values
    ]
    strain_residue_probes = [
        float(E * strain_map_scale**2 / (E + lambda_gap)) for E in probe_values
    ]

    checks = {
        "computed_internal_value_is_lambda15": lambda_gap == 15,
        "metric_DG_scale_is_two": metric["checks"]["metric_shape_C_is_2I"] is True,
        "strain_DG_scale_is_one": metric["checks"]["log_strain_C_is_I"] is True,
        "computed_metric_zero_value_is_exactly_4_over_15": metric_residual < 1.0e-14,
        "computed_strain_zero_value_is_exactly_1_over_15": strain_residual < 1.0e-14,
        "pure_positive_gap_metric_residue_tends_to_zero": (
            metric_residue_probes[-1] < metric_residue_probes[0]
            and metric_residue_probes[-1] < 1.0e-7
        ),
        "pure_positive_gap_strain_residue_tends_to_zero": (
            strain_residue_probes[-1] < strain_residue_probes[0]
            and strain_residue_probes[-1] < 1.0e-8
        ),
        "global_DG_current_internal_factor_is_dstar": (
            "|d_*>" in global_dg["theorem"]["exact_support"]
        ),
        "closed_action_reduction_requires_massless_operator_under_gauge_identity": (
            global_hessian["claim_tiers"]["massless_quadratic_operator"]
            == "CLOSED_CONDITIONAL_ON_LINEARIZED_DIFF_GAUGE_INVARIANCE"
        ),
        "old_support_packet_called_lambda15_GR_TT": (
            old_support["conclusion"]["lambda_GR_TT_internal_exact_branch"] == 15
        ),
        "QG_paper_claims_massless_IR_pole_normalization": (
            "F(0)=1" in qg_text and r"\Dprop=F(E)\,E^{-1}" in qg_text
        ),
        "QG_paper_separately_calls_lambda_internal_complement_gap": (
            r"First positive eigenvalue bound for $A_{\mathrm{int}}$ on the non" in qg_text
            and "coherent slice" in qg_text
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    theorem = {
        "name": "MasslessTTPolePositiveInternalGapNoGoAndZeroModeRepairTheorem",
        "pure_gap_no_go": {
            "assumptions": [
                "A_int is nonnegative",
                "B^*P_TT is supported entirely in spectral values s>=lambda_gap>0",
                "the projected propagator is a positive Stieltjes compression B(E+A_int)^(-1)B^*",
            ],
            "statement": (
                "The compressed propagator is bounded at E=0 and has zero massless "
                "residue: lim_{E->0} E Delta_TT(E)=0. Therefore it cannot equal "
                "F(E)E^(-1) with F(0)>0."
            ),
            "proof": (
                "For every s>=lambda_gap, 0<=E/(E+s)<=E/lambda_gap. "
                "Integrating against the finite positive compressed spectral measure "
                "and taking E->0 gives zero by domination."
            ),
            "executed_lambda15_values": {
                "metric_Delta_at_E0": "4/15 Id_E",
                "half_log_strain_Delta_at_E0": "1/15 Id_E",
                "metric_massless_residue": 0,
                "half_log_strain_massless_residue": 0,
            },
        },
        "zero_mode_necessity": {
            "statement": (
                "A positive Stieltjes TT propagator has a nonzero 1/E pole if and only "
                "if its compressed spectral measure has a nonzero atom at s=0."
            ),
            "decomposition": "nu_TT = r0 delta_0 + nu_gap, with r0>0",
            "propagator": "Delta_TT(E)=r0/E + integral_[lambda_gap,infinity) (E+s)^(-1) nu_gap(ds)",
            "normalized_residue": "F(0)=1 fixes r0=1 in normalized field units",
        },
        "corrected_carrier": {
            "physical_massless_channel": "E_TT tensor |0_int>, with A_int|0_int>=0 and in fact A_int|0_int>=0 selected as the coherent zero mode",
            "gapped_channel": "E_TT tensor |d_*>, with A_int|d_*>=15|d_*>",
            "role_of_lambda15": (
                "lambda=15 is a noncoherent suppression/correction scale. It cannot be "
                "the location of the physical graviton pole."
            ),
            "role_of_external_helicity": (
                "The nontrivial helicity topology is carried by the external associated "
                "bundle E_TT, so the internal coherent factor may be the trivial zero "
                "mode without erasing helicity two."
            ),
            "retained_result": (
                "The exact d_* rows, their lambda=15 eigenvalue, and their fiberwise "
                "support theorem remain valid for the gapped component."
            ),
            "new_source_gate": (
                "Compute and select the coherent-zero-mode TT source row and its residue; "
                "the full physical B^*P_TT cannot be exhausted by Pi_exact64 d_* support."
            ),
        },
        "parameter_count": {
            "new_fitted_parameters": 0,
            "residue_comment": (
                "The zero-mode residue is fixed by canonical TT normalization once "
                "kappa_h is selected; its source row is a theorem obligation, not a fit."
            ),
        },
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "massless_tt_pole_internal_gap_no_go",
        "date": "2026-07-15",
        "status": "PURE_LAMBDA15_PHYSICAL_TT_CARRIER_CLOSED_NOGO_COHERENT_ZERO_MODE_POLE_CHANNEL_REQUIRED",
        "inputs": {
            "world_in_world_z64_metric_source_map": str(METRIC_SOURCE),
            "global_covariant_helicity2_dg_bundle": str(GLOBAL_DG),
            "global_tt_hessian_action_uniqueness_reduction": str(GLOBAL_HESSIAN),
            "old_gr_tt_support_final_theorem": str(OLD_TT_SUPPORT),
            "qg_paper_source": str(QG_SOURCE),
        },
        "checks": checks,
        "numerics": {
            "lambda_gap": int(lambda_gap),
            "metric_zero_value_exact": str(metric_zero_value),
            "strain_zero_value_exact": str(strain_zero_value),
            "metric_zero_value_matrix_residual": metric_residual,
            "strain_zero_value_matrix_residual": strain_residual,
            "E_probe_values": [float(value) for value in probe_values],
            "metric_E_times_Delta_probes": metric_residue_probes,
            "strain_E_times_Delta_probes": strain_residue_probes,
        },
        "theorem": theorem,
        "supersession": {
            "old_claim": "lambda_GR,TT=15 is the physical exact-branch graviton pole value",
            "status": "SUPERSEDED_AS_PHYSICAL_POLE_IDENTIFICATION",
            "retained": (
                "lambda=15 remains exact on the selected d_* tower and may control the "
                "gapped correction/suppression channel."
            ),
            "reason": (
                "A strictly positive internal spectral value yields a finite E=0 "
                "compressed propagator and cannot produce the massless 1/E pole."
            ),
        },
        "claim_tiers": {
            "pure_lambda15_carrier_as_massless_graviton": "CLOSED_NO_GO",
            "lambda15_as_gapped_internal_suppression_channel": "CLOSED_CONSISTENT",
            "zero_internal_atom_required_for_massless_pole": "CLOSED",
            "external_helicity_bundle_allows_trivial_internal_zero_factor": "CLOSED_STRUCTURAL",
            "coherent_zero_mode_TT_source_row": "OPEN",
            "normalized_massless_residue_source": "OPEN",
            "selected_Lorentzian_action": "OPEN",
            "full_GR_or_QG": "OPEN",
        },
        "guardrails": {
            "claims_lambda15_is_physical_graviton_mass_or_pole": False,
            "claims_zero_mode_source_row_computed": False,
            "claims_selected_action_closed": False,
            "claims_full_GR_or_QG_closed": False,
            "uses_observed_GR_data": False,
            "adds_fitted_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# Massless TT Pole versus Positive Internal Gap: No-Go v1

Date: 2026-07-15

## Exact contradiction

The explicit metric source calculation has

```text
lambda_gap = 15,
DG_metric = 2 I,
DG_strain = I.
```

Consequently, at zero external momentum,

```text
Delta_metric(0) = 4/15 I,
Delta_strain(0) = 1/15 I.
```

Those are exactly the matrices already emitted by the metric-source packet.
They are finite.  In contrast, a normalized massless graviton propagator has

```text
Delta_TT(E) = F(E)/E,
F(0)=1,
```

and hence a nonzero `1/E` pole.

## General no-go theorem

Let the compressed positive Stieltjes measure be supported in
`[lambda_gap,infinity)` with `lambda_gap>0`. Then

```text
0 <= E/(E+s) <= E/lambda_gap.
```

After integration,

```text
lim_(E->0) E Delta_TT(E) = 0.
```

Therefore no bounded source map supported only on the positive `lambda=15`
eigenspace can produce a massless graviton pole.  This is independent of basis
normalization and does not depend on a numerical approximation.

## Necessary repair

A positive Stieltjes propagator has a massless pole precisely when its
compressed measure contains a zero atom:

```text
nu_TT = r0 delta_0 + nu_gap,
Delta_TT(E) = r0/E + integral (E+s)^(-1) nu_gap(ds).
```

Canonical normalized fields set `r0=1`.  The corrected carrier is therefore

```text
massless channel: E_TT tensor |0_int>,
gapped channel:   E_TT tensor |d_*>,  lambda(d_*)=15.
```

The external associated bundle `E_TT` carries helicity two and its Chern
class.  The internal factor of the massless channel can consequently be the
trivial coherent zero mode; helicity no longer has to be encoded by an internal
positive-gap character.

## What survives

The `d_*` Fourier rows, exact `Z64` support, and `lambda=15` calculation remain
correct. Their physical role changes: they describe a gapped correction or
suppression channel, not the location of the graviton pole.  The old statement
`lambda_GR,TT=15` is superseded only as a physical pole identification.

The next executable object is now unambiguous: compute the coherent-zero-mode
TT source row and its normalized residue from the same selected action.  The
full physical source cannot obey the old exhaustion statement
`Pi_exact64 B^*P_TT=B^*P_TT`; that identity remains valid only for its gapped
`d_*` component.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
