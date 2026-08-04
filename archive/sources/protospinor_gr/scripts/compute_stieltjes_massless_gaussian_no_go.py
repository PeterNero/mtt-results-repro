from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

MASSLESS_GAP_NOGO = ROOT / "certificates" / "massless_tt_pole_internal_gap_no_go_certificate.json"
QG_SOURCE = (
    ROOT.parent
    / "12 Quantum Gravity"
    / "_work"
    / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4"
    / "main.tex"
)

OUT_CERT = ROOT / "certificates" / "stieltjes_massless_gaussian_no_go_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Stieltjes_Massless_Pole_Gaussian_Damping_NoGo_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    massless = load(MASSLESS_GAP_NOGO)
    qg_text = QG_SOURCE.read_text(encoding="utf-8")

    # A finite numerical witness is not the proof, but it makes the asymptotic
    # contradiction executable. For any C,r0,tau>0, choose x beyond the exact
    # crossing log(C/r0)/tau. We test several scales and constants.
    examples = []
    for r0, C, tau in [
        (1.0, 1.0, 0.1),
        (1.0, 100.0, 0.1),
        (0.25, 1.0e6, 0.01),
        (1.0, 1.0, math.log(448.0) / 15.0),
    ]:
        threshold = max(0.0, math.log(C / r0) / tau)
        x = threshold + 10.0 / tau
        lower = r0 / x
        gaussian_upper = C * math.exp(-tau * x) / x
        examples.append(
            {
                "r0": r0,
                "C": C,
                "tau": tau,
                "crossing_threshold": threshold,
                "witness_x": x,
                "stieltjes_massless_lower": lower,
                "gaussian_upper": gaussian_upper,
                "lower_exceeds_upper": lower > gaussian_upper,
            }
        )

    checks = {
        "massless_zero_atom_is_required": (
            massless["claim_tiers"]["zero_internal_atom_required_for_massless_pole"]
            == "CLOSED"
        ),
        "all_numeric_crossing_witnesses_pass": all(
            row["lower_exceeds_upper"] for row in examples
        ),
        "QG_paper_claims_positive_Stieltjes_representation": (
            "positive operator measure" in qg_text
            and "Stieltjes" in qg_text
        ),
        "QG_paper_claims_massless_IR_residue": (
            "F(0)=1" in qg_text and r"\Dprop=F(E)\,E^{-1}" in qg_text
        ),
        "QG_paper_claims_permanent_Gaussian_propagator_damping": (
            "This dressing is present" in qg_text
            and "at $k=0$" in qg_text
            and r"e^{-\tau_0 k^2}" in qg_text
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    theorem = {
        "name": "PositiveStieltjesMasslessPoleGaussianDampingNoGoTheorem",
        "assumptions": {
            "positive_spectral_representation": (
                "Delta(x)=r0/x + integral_[0,infinity) (x+s)^(-1) rho(ds), "
                "with rho positive and r0>0"
            ),
            "massless_pole": "r0>0",
            "strict_Gaussian_bound": "Delta(x)<=C exp(-tau x)/(x+lambda), with C,tau>0 and lambda>=0",
        },
        "proof": [
            "Positivity gives Delta(x)>=r0/x for every x>0.",
            "Since x+lambda>=x, the Gaussian hypothesis gives Delta(x)<=C exp(-tau x)/x.",
            "Choose x>tau^(-1) log(C/r0). Then C exp(-tau x)<r0, contradicting both inequalities.",
        ],
        "conclusion": (
            "No nonzero positive-spectral massless propagator can have uniform "
            "permanent exponential suppression on the positive Euclidean axis."
        ),
        "independence": (
            "The contradiction is independent of the value lambda=15, the detailed "
            "spectral density, loop order, and field normalization."
        ),
    }

    resolution_routes = {
        "route_A_physical_positive_spectrum": {
            "keep": ["massless pole", "positive Kallen-Lehmann/Stieltjes density", "standard causal unitary interpretation"],
            "must_drop_or_weaken": "permanent Gaussian damping of the physical propagator",
            "consequence": (
                "Use the proper-time factor only as a removable regulator/coarse-graining "
                "device, or accept non-exponential physical UV behavior. The current "
                "all-loop-finiteness proof no longer follows."
            ),
            "recommended": True,
        },
        "route_B_physical_entire_damping": {
            "keep": ["massless pole", "permanent Gaussian/entire damping"],
            "must_drop_or_replace": "positive Stieltjes/Kallen-Lehmann proof",
            "consequence": (
                "Unitarity and causality require a different nonlocal analysis; OS "
                "positivity cannot be inferred from the claimed positive measure."
            ),
            "recommended": False,
        },
        "route_C_positive_gapped_theory": {
            "keep": ["positive Stieltjes density", "positive internal gap"],
            "must_drop": "massless graviton / GR infrared limit",
            "consequence": "This is not the intended gravity branch.",
            "recommended": False,
        },
        "route_D_cancellations": {
            "keep": ["improved ultraviolet decay"],
            "must_drop": "positive spectral density",
            "consequence": "Negative residues or an indefinite state space reintroduce a unitarity burden.",
            "recommended": False,
        },
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "stieltjes_massless_gaussian_no_go",
        "date": "2026-07-15",
        "status": "POSITIVE_STIELTJES_MASSLESS_POLE_AND_PERMANENT_GAUSSIAN_PROPAGATOR_DAMPING_CLOSED_INCOMPATIBLE",
        "inputs": {
            "massless_tt_pole_internal_gap_no_go": str(MASSLESS_GAP_NOGO),
            "qg_paper_source": str(QG_SOURCE),
        },
        "checks": checks,
        "numeric_witnesses": examples,
        "theorem": theorem,
        "resolution_routes": resolution_routes,
        "paper_impact": {
            "qg_main_three_claim_conjunction": "CLOSED_NO_GO",
            "claims_that_cannot_stand_together": [
                "positive Stieltjes/Kallen-Lehmann TT propagator",
                "normalized massless pole F(0)=1",
                "permanent Gaussian damping on every physical graviton propagator",
            ],
            "all_loop_finiteness_status": (
                "NOT_ESTABLISHED on the recommended positive-spectrum massless route; "
                "the existing domination proof uses the incompatible permanent Gaussian bound"
            ),
            "unitarity_status_on_entire_route": (
                "NOT_ESTABLISHED by the existing Stieltjes argument if permanent Gaussian damping is retained"
            ),
        },
        "claim_tiers": {
            "three_way_incompatibility": "CLOSED",
            "positive_spectrum_massless_GR_route": "AVAILABLE_GAUSSIAN_PHYSICAL_DAMPING_MUST_BE_RETIRED",
            "permanent_entire_damping_route": "AVAILABLE_POSITIVE_SPECTRAL_UNITARITY_PROOF_MUST_BE_RETIRED",
            "all_loop_UV_finiteness_with_positive_massless_spectrum": "OPEN_NOT_PROVED",
            "full_unitary_causal_UV_finite_QG": "OPEN",
        },
        "guardrails": {
            "claims_all_loop_finiteness_survives_unchanged": False,
            "claims_positive_Stieltjes_and_physical_Gaussian_are_compatible": False,
            "claims_full_QG_closed": False,
            "uses_observed_physics_data": False,
            "adds_fitted_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# Stieltjes Massless Pole and Gaussian Damping No-Go v1

Date: 2026-07-15

## The theorem

Assume a Euclidean TT propagator has a positive spectral representation and a
massless residue:

```text
Delta(x) = r0/x + integral_0^infinity (x+s)^(-1) rho(ds),
rho >= 0,
r0 > 0.
```

Positivity immediately gives

```text
Delta(x) >= r0/x.
```

Suppose at the same time that the physical propagator has permanent Gaussian
suppression,

```text
Delta(x) <= C exp(-tau x)/(x+lambda),
C,tau>0,
lambda>=0.
```

Then `Delta(x)<=C exp(-tau x)/x`.  For

```text
x > log(C/r0)/tau
```

the upper bound is strictly smaller than the positive-spectral lower bound.
This is a contradiction.

## Consequence for the QG paper

The current QG paper claims all three of the following:

1. a positive Stieltjes/Kallen-Lehmann TT propagator;
2. a normalized massless pole `Delta=F(E)E^-1`, `F(0)=1`; and
3. permanent Gaussian damping on every physical graviton propagator.

The theorem proves that this conjunction is impossible.  This is not a missing
numerical coefficient and is not repaired by changing `lambda=15`.

## Correct routes

The conservative route is to retain the positive spectral representation and
massless GR pole, and treat proper-time damping as a removable regulator or
coarse-graining device rather than a permanent physical form factor.  Then the
existing all-loop Gaussian domination proof must be withdrawn or replaced.

Alternatively one may retain a permanent entire form factor, but then the
Stieltjes/OS positivity argument cannot prove unitarity; a different nonlocal
unitarity and causality theorem is required.  Negative-residue cancellations
can improve UV decay but also abandon positive spectral density.

This no-go sharply separates the viable low-energy GR construction from the
still-open UV-completion problem.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
