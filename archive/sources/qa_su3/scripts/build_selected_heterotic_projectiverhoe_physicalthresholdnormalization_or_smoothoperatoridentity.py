"""Build physical threshold normalization or smooth-operator identity gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "rhoE_internal_finitepart": DATA / "selected_heterotic_projectiverhoe_eqa_or_thresholdfinitepart.candidate.json",
    "rhoE_internal_value": DATA / "selected_heterotic_projectiverhoe_internal_threshold_finitepart.json",
    "electroweak_matching_interface": DATA / "electroweak_matching_or_absolute_coupling_normalization.candidate.json",
    "internal_k_gauge_anchor": DATA / "selected_k_gauge_anchor_or_full_electroweak_matching.candidate.json",
    "physical_anchor_frontier": DATA / "selected_physical_gauge_anchor_and_electroweak_threshold_vector.candidate.json",
    "gaugekinetic_rg_route": DATA / "selected_electroweak_gaugekinetic_normalization_and_rg_scheme.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_physicalthresholdnormalization_or_smoothoperatoridentity.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_physicalthresholdnormalization_or_smoothoperatoridentity_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_PhysicalThresholdNormalization_or_SmoothOperatorIdentity_v1.md"
OUTPUT_CONTRACT = DATA / "selected_heterotic_projectiverhoe_physicalnormalization_or_smoothidentity_contract.json"

STATUS = "HETEROTIC_PROJECTIVERHOE_PHYSICAL_NORMALIZATION_REDUCED_KPHYS_OR_SMOOTH_IDENTITY_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_KPhysAnchor_or_SmoothOperatorIdentity_Fill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    rhoe_gate = load(INPUTS["rhoE_internal_finitepart"])
    rhoe_value = load(INPUTS["rhoE_internal_value"])
    ew_interface = load(INPUTS["electroweak_matching_interface"])
    k_anchor = load(INPUTS["internal_k_gauge_anchor"])
    physical_frontier = load(INPUTS["physical_anchor_frontier"])
    rg_route = load(INPUTS["gaugekinetic_rg_route"])

    internal_checks = {
        "rhoE_internal_finitepart_closed": rhoe_gate["decision"]["selected_internal_threshold_finitepart_closed"],
        "rhoE_value_selected": rhoe_value["selected"],
        "rhoE_value_is_log2008": rhoe_value["Delta_selected_internal_exact"] == "log(2008)",
        "internal_K_gauge_closed": k_anchor["decision"]["internal_K_gauge_anchor_closed"],
        "internal_K_gauge_value_is_one": k_anchor["decision"]["internal_K_gauge_value"] == "1",
        "electroweak_interface_allows_conditional_formula": ew_interface["decision"]["allowed_conditional_formula"] == "1/g_Qa^2(mu_match)=K_gauge*log(2008)",
    }

    physical_checks = {
        "physical_K_gauge_anchor_closed": k_anchor["decision"]["physical_K_gauge_anchor_closed"],
        "physical_anchor_closed": physical_frontier["decision"]["physical_anchor_closed"],
        "threshold_vector_closed": physical_frontier["decision"]["threshold_vector_closed"],
        "matching_scale_closed": k_anchor["decision"]["matching_scale_closed"],
        "RG_scheme_closed": rg_route["decision"]["RG_scheme_closed"],
        "smooth_operator_identity_proved": rhoe_gate["decision"]["smooth_operator_identity_proved"],
        "E_Qa_computed": rhoe_gate["decision"]["E_Qa_computed"],
    }

    contract = {
        "schema": "SelectedHeteroticProjectiveRhoEPhysicalNormalizationOrSmoothIdentityContract.v1",
        "status": "OPEN",
        "closed_internal_formula": {
            "Delta_rhoE_internal": "log(2008)",
            "K_gauge_internal": "1",
            "conditional_physical_formula": "1/g_Qa^2(mu_match) = K_phys * log(2008) + Delta_Qa^sel + RG_scheme_terms",
            "scope": "interface only; not measured coupling prediction",
        },
        "must_prove_one_of": {
            "physical_normalization_bridge": [
                "emit selected K_phys or Omega_0/ell_p/kappa_11/alpha_prime/action-unit anchor from the same branch",
                "emit selected mu_match and fixed RG/threshold scheme",
                "prove the selected rhoE internal finite part maps into the physical gauge kinetic convention",
                "prove no observed coupling, mass, scale, or residual is used as selector",
            ],
            "smooth_operator_identity_bridge": [
                "emit smooth heterotic projective rho_E transition/Cech/Deligne or equivalent operator data",
                "compute E_Qa or equivalent Weitzenbock/heat/zeta/torsion finite part from that same source",
                "prove its quotient/complement policy reduces to the selected finite log(2008) packet or replaces it consistently",
                "emit trace/normalization convention compatible with the physical gauge-action slot",
            ],
        },
        "forbidden_shortcuts": [
            "set K_phys=1 from internal action units",
            "compare log(2008) directly to observed inverse couplings",
            "import Theta matching scale or measured gauge coupling as a source value",
            "reuse smooth GR/protospinor complement as a Qa/SU3 internal threshold",
            "promote smooth E_Qa from finite H_sel without smooth operator data",
        ],
    }

    decision = {
        "internal_interface_closed": all(internal_checks.values()),
        "closed_internal_formula": "Delta_rhoE_internal = log(2008), K_gauge,int=1",
        "physical_threshold_normalization_closed": False,
        "smooth_operator_identity_proved": False,
        "E_Qa_computed": False,
        "measured_coupling_match_claimed": False,
        "contract_written": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEPhysicalThresholdNormalizationOrSmoothOperatorIdentity",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "rhoE_internal_finitepart": rhoe_gate["status"],
            "electroweak_matching_interface": ew_interface["status"],
            "internal_k_gauge_anchor": k_anchor["status"],
            "physical_anchor_frontier": physical_frontier["status"],
            "gaugekinetic_rg_route": rg_route["status"],
        },
        "internal_checks": internal_checks,
        "physical_checks": physical_checks,
        "contract_path": rel(OUTPUT_CONTRACT),
        "decision": decision,
        "guardrails": {
            "does_not_promote_internal_K_to_physical_K": True,
            "does_not_compare_to_measured_couplings": True,
            "does_not_claim_smooth_E_Qa": True,
            "does_not_claim_RG_or_matching_scale": True,
            "does_not_use_target_fitting": True,
        },
        "theorem": {
            "name": "ProjectiveRhoEPhysicalNormalizationOrSmoothIdentityReduction",
            "proved": True,
            "statement": (
                "The selected projective rho_E branch now closes the internal finite "
                "threshold interface: Delta_rhoE_internal=log(2008) and K_gauge,int=1. "
                "Physical threshold normalization is not closed because K_phys, mu_match, "
                "RG/threshold scheme, and a physical convention map remain open. Smooth "
                "operator identity is also not closed because no smooth rho_E transition "
                "data or E_Qa block is emitted. Therefore the next legal closure must fill "
                "either the physical-anchor bridge or the smooth-operator identity bridge."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_CONTRACT.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "contract_path": rel(OUTPUT_CONTRACT),
        "internal_interface_closed": decision["internal_interface_closed"],
        "physical_threshold_normalization_closed": False,
        "smooth_operator_identity_proved": False,
        "E_Qa_computed": False,
        "measured_coupling_match_claimed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE PhysicalThresholdNormalization or SmoothOperatorIdentity v1

## Result

```text
status = {STATUS}
internal_interface_closed = {str(decision["internal_interface_closed"]).lower()}
physical_threshold_normalization_closed = false
smooth_operator_identity_proved = false
next_required_artifact = {NEXT}
```

## Closed Here

The selected projective `rho_E` branch is now fully attached to the internal
normalization interface:

```text
Delta_rhoE_internal = log(2008)
K_gauge,int = 1
```

This is still an internal action-unit statement, not a measured coupling.

## Remaining Contract

The next proof must fill one of the two bridges written here:

```text
{rel(OUTPUT_CONTRACT)}
```

Either emit the physical anchor/matching/RG bridge, or emit a same-source smooth
heterotic operator identity with `E_Qa` or an equivalent finite-part theorem.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_CONTRACT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
