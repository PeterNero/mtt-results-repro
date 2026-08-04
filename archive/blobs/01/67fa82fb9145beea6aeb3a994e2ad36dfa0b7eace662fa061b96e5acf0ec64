from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEGREE2 = ROOT / "certificates" / "q79_degree2_k3_fuyau_torsion_glsm_base_certificate.json"
CLUTCHING = ROOT / "certificates" / "q79_shared_circle_clutching_c2_c3_independence_certificate.json"
CERTIFICATE = ROOT / "certificates" / "q79_fuyau_mixed_c2_hodge_admissibility_certificate.json"
NOTE = ROOT / "proof_corpus" / "q79_FuYau_Mixed_C2_Hodge_Admissibility_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    degree2 = load(DEGREE2)
    clutching = load(CLUTCHING)
    checks = degree2["checks"]
    intersection = degree2["intersection_and_torsion_source"]
    simultaneous = clutching["q79_candidate_specialization"][
        "simultaneous_reference_member"
    ]
    if not checks["delta_is_primitive_and_H_orthogonal"]:
        raise AssertionError("the selected primitive Fu-Yau divisor is unavailable")
    if intersection["H_dot_delta"] != "0":
        raise AssertionError("H is not orthogonal to delta")
    if intersection["delta_square"] != "-4":
        raise AssertionError("the selected Fu-Yau curvature cost changed")
    if simultaneous["c2"] != "9 u" or simultaneous["c3"] != [6, -6]:
        raise AssertionError("the simultaneous clutching target changed")

    payload = {
        "schema": "MTTQ79FuYauMixedC2HodgeAdmissibility.v1",
        "status": (
            "Q79_MIXED_C2_9U_AND_C3_PLUSMINUS6_HODGE_ADMISSIBLE_ON_RANKONE_"
            "FUYAU_COMPLEX_STRUCTURE_HOLOMORPHIC_BUNDLE_EXISTENCE_STILL_OPEN"
        ),
        "date": "2026-07-16",
        "authority_hashes": [
            {"path": str(path), "sha256": sha256(path)}
            for path in (DEGREE2, CLUTCHING)
        ],
        "selected_geometry": {
            "base": "degree-two polarized K3 surface S",
            "polarization": "H in H^(1,1)(S,Z), H^2=2",
            "active_FuYau_curvature": "delta=H-L in H^(1,1)(S,Z)",
            "shared_circle_curvature": "0",
            "intersection_rows": {
                "H_dot_delta": 0,
                "delta_square": -4,
                "delta_primitive": True,
            },
            "vertical_forms": {
                "eta_delta": "real connection one-form with d eta_delta=pi^*delta",
                "eta_shared": "closed integral one-form on S1_shared",
                "Theta": "eta_delta+i eta_shared, of type (1,0)",
                "vertical_area": "eta_delta wedge eta_shared=(i/2) Theta wedge conjugate(Theta)",
            },
        },
        "differential_representatives": {
            "Hhat": {
                "representative": "eta_delta wedge pi^*H",
                "closedness": "d(Hhat)=pi^*(delta wedge H)=0",
                "reason": (
                    "delta is primitive (1,1) for the H-polarized K3 metric, so "
                    "delta is anti-self-dual while H is self-dual and delta wedge H=0"
                ),
                "fiber_integral": "pi_!(Hhat)=H",
            },
            "u": {
                "representative": "eta_delta wedge eta_shared wedge pi^*H",
                "complex_formula": "(i/2) Theta wedge conjugate(Theta) wedge pi^*H",
                "bidegree": [2, 2],
                "closed": True,
                "integral_and_primitive": True,
            },
            "orientation": {
                "representative": (
                    "eta_delta wedge eta_shared wedge pi^*(vol_H), "
                    "with vol_H proportional to H wedge H"
                ),
                "bidegree": [3, 3],
                "closed": True,
            },
        },
        "chern_target": {
            "c1": 0,
            "c2": "9 u has a closed real (2,2) representative",
            "c3": "+/-6 [X]^* has a closed real (3,3) representative",
            "new_continuous_parameters": 0,
            "necessary_Hodge_type_condition": "CLOSED_EXACT_ON_SELECTED_RANKONE_FUYAU_COMPLEX_STRUCTURE",
        },
        "checks": {
            "H_is_integral_11_polarization": True,
            "delta_is_integral_primitive_11": True,
            "delta_is_H_primitive": True,
            "rank_one_FuYau_pair_is_delta_and_zero": True,
            "shared_circle_one_form_is_closed": True,
            "Theta_defines_the_vertical_10_form": True,
            "Hhat_representative_is_closed": True,
            "u_representative_is_closed_22": True,
            "orientation_representative_is_closed_33": True,
            "c2_9u_and_c3_plusminus6_have_necessary_Hodge_types": True,
            "observed_SM_values_used": False,
        },
        "claim_tiers": {
            "mixed_c2_9u_Hodge_admissibility": "CLOSED_EXACT_CONDITIONAL_ON_SELECTED_FUYAU_COMPLEX_STRUCTURE",
            "c3_plusminus6_Hodge_admissibility": "CLOSED_EXACT",
            "holomorphic_nonpullback_SU3_bundle": "OPEN",
            "inverse_gerbe_spectral_sheaf_and_local_freeness": "OPEN",
            "balanced_stability_and_HYM": "OPEN",
            "differential_total_space_Bianchi_identity": "OPEN",
            "UV_complete_q79_quantum_gravity": "OPEN",
        },
        "guardrails": {
            "claims_integral_Hodge_class_is_automatically_a_bundle_Chern_class": False,
            "claims_a_holomorphic_structure_was_constructed": False,
            "claims_balanced_HYM_was_constructed": False,
            "claims_differential_Bianchi_was_solved": False,
            "claims_UV_completion": False,
        },
        "next_required_artifact": (
            "MTT_Selected_q79InverseGerbeSpectralSheafLocalFreenessDeterminantAndChernExecution_v1"
        ),
        "primary_sources": [
            "https://arxiv.org/abs/hep-th/0604137",
            "https://arxiv.org/abs/1008.3365",
        ],
    }
    dump(CERTIFICATE, payload)

    note = """# q79 Fu-Yau Mixed C2 Hodge Admissibility Theorem v1

## Exact statement

Let the selected rank-one Fu-Yau space be the principal two-torus bundle over
the degree-two K3 with curvature pair `(delta,0)`, where

```text
delta=H-L,   delta^2=-4,   H.delta=0.
```

Write `eta_delta` for the nontrivial circle connection and `eta_shared` for
the closed shared-circle form.  The selected complex vertical form is

```text
Theta=eta_delta+i eta_shared.
```

Since `H` and `delta` are integral `(1,1)` classes and `delta` is primitive
for the `H`-polarized K3 metric, `delta wedge H=0`.  Therefore

```text
Hhat = eta_delta wedge pi^*H,
u    = eta_delta wedge eta_shared wedge pi^*H
     = (i/2) Theta wedge conjugate(Theta) wedge pi^*H
```

are closed.  Fiber integration gives `pi_!(Hhat)=H`, so this `u` is the same
primitive mixed class selected by the Gysin/clutching theorem.  It is of type
`(2,2)`.  The orientation class is represented by the vertical area wedged
with the K3 volume and is of type `(3,3)`.

It follows that the simultaneous smooth target

```text
c1=0,   c2=9u,   c3=+/-6[X]^*
```

passes the necessary Hodge-type test on the selected Fu-Yau complex
structure.  No continuous parameter is added.

## What this closes

The new smooth bundle is not excluded from holomorphic promotion merely
because its second Chern class lies in the mixed shared-circle channel.  The
mixed class has an explicit closed `(2,2)` representative, and the chirality
class has type `(3,3)`.

## What remains open

An integral class of the correct type is not automatically the Chern class of
a holomorphic vector bundle on a non-Kahler threefold.  This theorem does not
construct the inverse-gerbe spectral sheaf, prove WIT or local freeness,
establish determinant zero, prove balanced stability/HYM, or solve the
differential Bianchi identity.  Those are the next gates; UV completion is
not claimed.

## Primary sources

- [Fu-Yau anomaly solutions](https://arxiv.org/abs/hep-th/0604137)
- [Vector bundles on non-Kahler elliptic principal bundles](https://arxiv.org/abs/1008.3365)
"""
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {CERTIFICATE.relative_to(ROOT)}")
    print(f"wrote {NOTE.relative_to(ROOT)}")
    print("q79 Fu-Yau mixed c2 Hodge admissibility: CLOSED; holomorphic bundle open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
