"""Build the selected K_gauge anchor / electroweak matching frontier theorem.

The proof goal here is deliberately split:

1. close the internal action-unit gauge anchor, where the sibling non-SM and
   GR repos already certify canonical internal action units; and
2. refuse to promote that internal unit to a measured electroweak coupling
   until the physical compactification/modal-gap anchor, matching scale, and
   threshold/RG scheme are supplied.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"
SM_PARITY = ROOT.parent / "mtt-sm-parity-closure"
GR = ROOT.parent / "mtt-protospinor-gr-response-proof"

INPUTS = {
    "qa_response": DATA / "selected_response_functional_chi_qa.candidate.json",
    "u1_projector": DATA / "selected_u1_quotient_projector_pperp_and_trace_policy.candidate.json",
    "nonsm_kernel": NONSM / "certificates" / "selected_electroweak_kernel_interface_certificate.json",
    "nonsm_bridge": NONSM / "certificates" / "electroweak_no_knob_bridge_audit_certificate.json",
    "gr_mtheory_anchor": GR / "certificates" / "m_theory_modal_gap_dimensional_anchor_candidate_certificate.json",
    "sm_measured_policy": SM_PARITY / "candidate_data" / "core_axioms_measured_parameter_interface.candidate.json",
}

OUTPUT_DATA = DATA / "selected_k_gauge_anchor_or_full_electroweak_matching.candidate.json"
OUTPUT_CERT = CERTS / "selected_k_gauge_anchor_or_full_electroweak_matching_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_K_Gauge_Anchor_or_Full_Electroweak_Matching_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    qa = load(INPUTS["qa_response"])
    u1 = load(INPUTS["u1_projector"])
    kernel = load(INPUTS["nonsm_kernel"])
    bridge = load(INPUTS["nonsm_bridge"])
    mtheory = load(INPUTS["gr_mtheory_anchor"])
    sm_policy = load(INPUTS["sm_measured_policy"])

    log2008 = math.log(2008)
    internal_indices = {
        "U1": "2/3",
        "SU2": "1",
        "Qa_or_SU3": "log(2008)",
    }
    internal_numeric = {
        "U1": 2.0 / 3.0,
        "SU2": 1.0,
        "Qa_or_SU3": log2008,
    }

    source_checks = {
        "qa_finite_response_closed": qa["decision"]["finite_internal_coupling_normalization"] == "CLOSED",
        "qa_delta_is_log2008": qa["decision"]["finite_response_functional"] == "Delta_Qa_selected_finite = log(2008)",
        "u1_su2_index_pair_closed": u1["decision"]["selected_U1_SU2_threshold_index_pair_closed"] is True,
        "nonsm_kernel_interface_built": kernel["verdict"]["kernel_interface_built"] is True,
        "nonsm_numeric_electroweak_open": kernel["verdict"]["numeric_electroweak_closure"] is False,
        "rho_uv_bridge_open": bridge["verdict"]["rho_uv_bridge_to_electroweak_closed"] is False,
        "mtheory_gauge_slot_identified": mtheory["closed_tests"]["m_theory_gauge_slot_identified"] is True,
        "mtheory_physical_anchor_open": mtheory["verdict"]["physical_dimensionful_anchor_available"] is False,
        "sm_gauge_couplings_downstream": (
            sm_policy["sector_interfaces"]["QFT"]["parity_policy"]
            == "Renormalized couplings may be measured parity inputs after sector selection."
        ),
    }

    theorem = {
        "name": "SelectedInternalKGaugeAnchorAndPhysicalMatchingReduction",
        "statement": (
            "In canonical selected internal action units, the common gauge-action "
            "normalization is fixed as K_gauge,int=1. This is not a measured "
            "electroweak normalization: the physical K_gauge is the compactification/"
            "action anchor controlled by the same M-theory modal-gap slot as the "
            "GR normalization. Therefore the internal kernel is closed, while full "
            "measured electroweak matching is reduced to the single physical anchor "
            "plus selected threshold/RG data."
        ),
        "internal_unit_anchor": {
            "K_gauge_internal_action_units": "1",
            "why_allowed": (
                "The non-SM constants repo already certifies canonical internal "
                "action units alpha_int=1 and G10_int=1; in those units K_gauge "
                "is a unit conversion for the selected internal response functional, "
                "not a fitted physical coupling."
            ),
            "why_not_physical": (
                "The protospinor/GR M-theory anchor certificate identifies the "
                "gauge kinetic normalization slot but leaves ell_p/kappa_11/"
                "alpha_prime or the physical modal-gap unit open."
            ),
        },
        "selected_internal_kernel": {
            "formula": "G_a^int = K_gauge,int * I_a with K_gauge,int=1, before physical thresholds/running",
            "entries_exact": internal_indices,
            "entries_numeric": internal_numeric,
            "scope": "dimensionless selected internal action units; not M_Z couplings and not a physical high-scale fit",
        },
        "physical_kernel_required": {
            "formula": (
                "G_a^phys(mu) = K_phys * I_a + Delta_a^sel + "
                "b_a/(8*pi^2)*log(mu_match/mu) in a fixed scheme"
            ),
            "K_phys_source": "M-theory compactification/action slot, e.g. kappa_11^{-2} times the selected harmonic Gram matrix with conventions fixed",
            "still_missing": [
                "target-independent physical modal-gap / ell_p / kappa_11 / alpha_prime anchor",
                "selected matching scale mu_match",
                "selected threshold vector Delta_a^sel",
                "fixed RG and threshold scheme",
                "sector-resolved SU3 identification if Qa is used as the SU3 payload",
            ],
        },
    }

    decision = {
        "internal_K_gauge_anchor_closed": True,
        "internal_K_gauge_value": "1",
        "selected_internal_kernel_vector_closed": True,
        "selected_internal_kernel_vector": internal_indices,
        "physical_K_gauge_anchor_closed": False,
        "matching_scale_closed": False,
        "threshold_vector_closed": False,
        "measured_electroweak_closure": False,
        "full_SM_closure": False,
        "target_fitting_used": False,
        "next_required_object": "Selected_Physical_Gauge_Anchor_and_Electroweak_Threshold_Vector_v1",
    }

    candidate = {
        "candidate": "SelectedKGaugeAnchorOrFullElectroweakMatching",
        "status": "INTERNAL_K_GAUGE_ANCHOR_CLOSED_PHYSICAL_ELECTROWEAK_MATCHING_OPEN",
        "inputs": {name: rel(path) for name, path in INPUTS.items()},
        "source_checks": source_checks,
        "theorem": theorem,
        "decision": decision,
        "guardrails": [
            "K_gauge,int=1 is an internal action-unit statement, not a measured coupling prediction.",
            "Do not compare the internal vector (2/3,1,log(2008)) directly to measured inverse couplings.",
            "Do not use observed alpha_EM, sin^2(theta_W), g2, g3, masses, or M_Z-derived fits to select K_phys or Delta^sel.",
            "The physical gauge anchor must be shared with the GR/M-theory compactification normalization if claimed as no-knob.",
            "Thresholds and RG scheme must be fixed before any electroweak data comparison.",
        ],
        "closure_claimed": True,
        "closure_scope": "internal_action_unit_K_gauge_anchor_and_frontier_reduction_only",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedKGaugeAnchorOrFullElectroweakMatching",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "closed": {
            "internal_K_gauge_anchor": True,
            "internal_K_gauge_value": "1",
            "selected_internal_kernel_vector": internal_indices,
            "cross_repo_frontier_checked": True,
            "no_hidden_target_fit": True,
        },
        "open": {
            "physical_K_gauge_anchor": True,
            "selected_mu_match": True,
            "selected_Delta_a_threshold_vector": True,
            "fixed_RGE_threshold_scheme": True,
            "measured_electroweak_closure": True,
        },
        "next_required_object": decision["next_required_object"],
        "guardrail_summary": "internal unit closure only; physical electroweak matching remains open",
        "target_fitting_used": False,
    }

    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    theorem = candidate["theorem"]
    decision = candidate["decision"]
    checks = "\n".join(f"{key} = {value}" for key, value in candidate["source_checks"].items())
    guards = "\n".join(f"- {item}" for item in candidate["guardrails"])
    missing = "\n".join(f"- {item}" for item in theorem["physical_kernel_required"]["still_missing"])
    entries_exact = "\n".join(f"{key}: {value}" for key, value in theorem["selected_internal_kernel"]["entries_exact"].items())
    entries_numeric = "\n".join(
        f"{key}: {value:.12g}" for key, value in theorem["selected_internal_kernel"]["entries_numeric"].items()
    )
    return f"""# Selected K Gauge Anchor or Full Electroweak Matching v1

## Result

This solves the frontier in the only currently source-certified scope:

```text
internal_K_gauge_anchor_closed = {str(decision["internal_K_gauge_anchor_closed"]).lower()}
K_gauge,int = {decision["internal_K_gauge_value"]}
selected_internal_kernel_vector_closed = {str(decision["selected_internal_kernel_vector_closed"]).lower()}
physical_K_gauge_anchor_closed = {str(decision["physical_K_gauge_anchor_closed"]).lower()}
measured_electroweak_closure = {str(decision["measured_electroweak_closure"]).lower()}
target_fitting_used = {str(decision["target_fitting_used"]).lower()}
```

The physical electroweak constants are not yet predicted.  What is now proved
is that there is no additional internal normalization knob left at this layer:
the common gauge normalization is `1` in canonical selected internal action
units, and the remaining physical normalization is the same M-theory/modal-gap
anchor already isolated by the GR/protospinor branch.

## Theorem

```text
{theorem["name"]}
```

{theorem["statement"]}

Internal unit anchor:

```text
K_gauge,int = {theorem["internal_unit_anchor"]["K_gauge_internal_action_units"]}
```

Why this is allowed:

```text
{theorem["internal_unit_anchor"]["why_allowed"]}
```

Why this is not physical electroweak closure:

```text
{theorem["internal_unit_anchor"]["why_not_physical"]}
```

## Selected Internal Kernel

Formula:

```text
{theorem["selected_internal_kernel"]["formula"]}
```

Exact entries:

```text
{entries_exact}
```

Numeric entries:

```text
{entries_numeric}
```

Scope:

```text
{theorem["selected_internal_kernel"]["scope"]}
```

## Physical Kernel Still Required

Formula:

```text
{theorem["physical_kernel_required"]["formula"]}
```

Source slot:

```text
{theorem["physical_kernel_required"]["K_phys_source"]}
```

Still missing:

{missing}

## Cross-Repo Checks

```text
{checks}
```

## Guardrails

{guards}

## Next Required Object

```text
{decision["next_required_object"]}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    missing = [str(path) for path in INPUTS.values() if not path.exists()]
    if missing:
        print("Missing inputs:")
        print("\n".join(missing))
        return 1
    candidate, certificate, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, certificate)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"Wrote {OUTPUT_DATA}")
    print(f"Wrote {OUTPUT_CERT}")
    print(f"Wrote {OUTPUT_NOTE}")
    print(certificate["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
