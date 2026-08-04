from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ALPHA_THEOREM = ROOT / "certificates" / "selected_physical_alpha_or_action_unit_theorem_certificate.json"
ANCHOR_CANDIDATES = ROOT / "certificates" / "target_independent_dimensional_anchor_candidates_certificate.json"
M_THEORY_ANCHOR = ROOT / "certificates" / "m_theory_modal_gap_dimensional_anchor_candidate_certificate.json"
MODAL_GATE = ROOT / "certificates" / "selected_modal_gap_physical_anchor_gate_certificate.json"
ANCHOR_HUNT = ROOT / "certificates" / "selected_physical_anchor_source_hunt_certificate.json"

OUT_CERT = ROOT / "certificates" / "target_independent_dimensional_anchor_search_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Target_Independent_Dimensional_Anchor_Search_v1.md"
OUT_PACKET = ROOT / "candidate_data" / "selected_dimensional_anchor_packet.template.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    alpha = load(ALPHA_THEOREM)
    candidates = load(ANCHOR_CANDIDATES)
    m_anchor = load(M_THEORY_ANCHOR)
    modal_gate = load(MODAL_GATE)
    anchor_hunt = load(ANCHOR_HUNT)

    route_table = {
        "m_theory_modal_gap_planck_anchor": {
            "classification": "BEST_STRUCTURAL_ROUTE_PACKET_REQUIRED",
            "closed": [
                "M-theory Planck/kappa11 slot identified",
                "same compactification data controls GR and gauge normalizations",
                "exact internal gap and rho_UV branch available",
            ],
            "blocker": "no selected physical modal-gap value or ell_p/kappa11/alpha_prime value independent of targets",
            "next_packet_fields": [
                "selected physical inverse-length unit",
                "map to ell_p/kappa11/alpha_prime",
                "proof no Newton/Planck/mass/cosmology/TeV target is used",
            ],
        },
        "theta_matching_scale": {
            "classification": "REJECTED_AS_NO_KNOB_ANCHOR",
            "closed": ["Theta matching framework present"],
            "blocker": "5 TeV is calibration/benchmark, not derived no-knob scale",
        },
        "proper_time_tau": {
            "classification": "PROMISING_SLOT_VALUE_OPEN",
            "closed": ["finite kernels and damping formulas use tau"],
            "blocker": "no selected tau in physical units",
        },
        "flux_bianchi_alpha_prime": {
            "classification": "PROMISING_STRING_SLOT_VALUE_OPEN",
            "closed": ["flux/Bianchi ratios and internal alpha-prime-one units available"],
            "blocker": "alpha_prime/string length remains an external dimensional anchor unless selected elsewhere",
        },
        "coherence_capacity": {
            "classification": "STRUCTURAL_RELATION_NORMALIZATION_OPEN",
            "closed": ["corpus relates effective gravity to coherence capacity"],
            "blocker": "no canonical physical normalization of capacity C_MTT",
        },
        "observed_target_backsolve": {
            "classification": "FORBIDDEN",
            "blocker": "uses the value being predicted",
        },
        "unit_convention": {
            "classification": "FORBIDDEN_AS_PHYSICAL_PREDICTION",
            "blocker": "changing units cannot select a dimensionful observable",
        },
    }

    closed_inputs = {
        "alpha_reduced_to_single_anchor": alpha["status"]
        == "ALPHA_PHYS_REDUCED_TO_SINGLE_EXTERNAL_DIMENSIONFUL_ANCHOR",
        "candidate_table_available": candidates["verdict"]["internal_scale_lift_available"],
        "candidate_table_has_no_physical_anchor": candidates["verdict"]["physical_dimensionful_anchor_available"] is False,
        "m_theory_route_identifies_slot": m_anchor["closed_tests"]["m_theory_planck_slot_identified"],
        "m_theory_route_lacks_dimensionful_gap": m_anchor["open_tests"]["dimensionful_modal_gap_value_computed"] is False,
        "modal_gate_forbids_5TeV_prediction": modal_gate["blocked_shortcuts"]["use_mu_theta_5TeV_as_prediction"],
        "anchor_hunt_direct_anchor_not_found": anchor_hunt["hard_negative"]["direct_physical_anchor_found_in_current_sources"] is False,
    }

    packet_template = {
        "packet": "SelectedDimensionalAnchorPacket",
        "status": "TEMPLATE_UNFILLED",
        "candidate_id": None,
        "source_branch": None,
        "dimensionful_quantity": {
            "symbol": None,
            "units": None,
            "physical_meaning": None,
            "value": None,
            "uncertainty_or_exactness": None,
        },
        "source_certification": {
            "selected_by_mtt": False,
            "source_files": [],
            "source_certificates": [],
            "same_branch_as_rho_uv_and_z448": False,
            "computed_before_target_comparison": False,
        },
        "forbidden_inputs_absent": {
            "observed_Newton_or_Planck": None,
            "observed_Omega0_H0_rhoDE": None,
            "observed_particle_masses_or_TeV_calibration": None,
            "unit_convention_only": None,
        },
        "map_to_alpha_phys": {
            "formula": None,
            "alpha_phys_value": None,
            "dimensional_analysis_checked": False,
            "convention_factors_declared": False,
        },
        "downstream_predictions_allowed_after_acceptance": [
            "Omega0 physical value",
            "omega_gap_phys physical value",
            "Lambda_gap_phys physical value",
            "G_eff/kappa_STF physical normalization if M/string map is supplied",
        ],
    }

    guardrails = {
        "claims_alpha_phys_closed_now": False,
        "claims_physical_Newton_or_Planck_now": False,
        "uses_target_backsolve": False,
        "uses_Theta_5TeV_as_prediction": False,
        "uses_unit_convention_as_prediction": False,
    }

    ready = all(closed_inputs.values())
    status = "DIMENSIONAL_ANCHOR_SEARCH_EXHAUSTED_PACKET_GATE_READY" if ready else "DIMENSIONAL_ANCHOR_SEARCH_INPUTS_NOT_READY"

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "target_independent_dimensional_anchor_search",
        "status": status,
        "input_certificates": {
            "selected_physical_alpha_or_action_unit_theorem": str(ALPHA_THEOREM),
            "target_independent_dimensional_anchor_candidates": str(ANCHOR_CANDIDATES),
            "m_theory_modal_gap_dimensional_anchor_candidate": str(M_THEORY_ANCHOR),
            "selected_modal_gap_physical_anchor_gate": str(MODAL_GATE),
            "selected_physical_anchor_source_hunt": str(ANCHOR_HUNT),
        },
        "closed_inputs": closed_inputs,
        "route_table": route_table,
        "verdict": {
            "current_corpus_closes_alpha_phys": False,
            "best_route": "m_theory_modal_gap_planck_anchor",
            "best_route_status": "structural slot identified; selected dimensionful value open",
            "next_required_object": str(OUT_PACKET),
            "honest_claim": (
                "All dimensionless exact-branch data are closed; physical numeric closure "
                "requires filling and validating a SelectedDimensionalAnchorPacket."
            ),
        },
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = """# Target Independent Dimensional Anchor Search v1

## Result

The search for a current target-independent dimensional anchor is exhausted
against the existing certificates.

Current status:

```text
alpha_phys is not numerically closed by the present corpus.
```

The best route remains:

```text
m_theory_modal_gap_planck_anchor
```

because it identifies the correct physical slot: a single length/action scale
would fix `ell_p`, `kappa_11`, the 4D gravitational normalization, and the TT
response scale together. But the route still lacks a selected physical modal-gap
value independent of Newton, Planck, cosmology, mass, or TeV calibration data.

## Route Classification

```text
M-theory/modal gap     best structural route; packet required
Theta 5 TeV            forbidden as no-knob anchor; calibration only
proper time tau        promising slot; physical value open
flux/Bianchi alpha'    promising string slot; string length open
coherence capacity     structural relation; normalization open
target backsolve       forbidden
unit convention        forbidden as physical prediction
```

## Next Executable Object

The verifier now writes:

```text
candidate_data/selected_dimensional_anchor_packet.template.json
```

Any claimed dimensional closure must fill that packet with:

```text
selected dimensionful quantity
source branch and source certificates
proof it is computed before target comparison
proof forbidden observed inputs are absent
formula mapping it to alpha_phys
declared convention factors and dimensional analysis
```

Until such a packet is filled and audited, the rigorous endpoint remains:

```text
Omega0 = sqrt(alpha_phys) * sqrt(15/log(448)).
```
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_PACKET.write_text(json.dumps(packet_template, indent=2), encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
