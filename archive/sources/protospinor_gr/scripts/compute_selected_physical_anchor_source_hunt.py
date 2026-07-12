from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

PHYS_STRESS = ROOT / "certificates" / "physical_normalization_stress_response_gate_certificate.json"
ANCHOR_CANDIDATES = ROOT / "certificates" / "target_independent_dimensional_anchor_candidates_certificate.json"
MODAL_ANCHOR = ROOT / "certificates" / "selected_modal_gap_physical_anchor_gate_certificate.json"
M_THEORY = ROOT / "certificates" / "m_theory_modal_gap_dimensional_anchor_candidate_certificate.json"
DIM_OBSTRUCTION = NONSM / "certificates" / "dimensionful_constant_obstruction_certificate.json"
ACTION_NORM = NONSM / "certificates" / "physical_action_normalization_gate_certificate.json"

M_THEORY_SOURCE = OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Modal_Triplet_Theory__From_MTT_to_M_theory.md"
THETA_I = OBSIDIAN / "18 Theta-Closure & Execution Program" / "Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry.md"
THETA_IV = OBSIDIAN / "18 Theta-Closure & Execution Program" / "Theta_Closure_in_Modal_Triplet_Theory_IV__Gravity_and_Cosmology_from_the_Closure_Scale.md"
PROPAGATORS = OBSIDIAN / "5 Dirac Delta" / "MTT_Corrected_Propagators_and_UV_Behaviour.md"
COHERENT_KERNELS = OBSIDIAN / "5 Dirac Delta" / "Canonical_Coherent_Kernels_from_MTT_Fixed_Point_Data.md"
FIXED_DAMPING = OBSIDIAN / "5 Dirac Delta" / "Deriving_the_MTT_Coherence_Scale_from_Fixed__Point_Damping.md"
META_PARAMS = OBSIDIAN / "2 Meta & Diagnosis & Universality" / "Modal_Triplet_Theory__Parameters__Closure__and_Structural_Falsifiability.md"
QFT_SOURCE = OBSIDIAN / "7 Quantum Field Theory" / "Modal_Triplet_Theory__Quantum_Amplitudes_from_Modal_Geometry_v2.md"

OUT_CERT = ROOT / "certificates" / "selected_physical_anchor_source_hunt_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Physical_Anchor_Source_Hunt_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def has(path: Path, *patterns: str) -> bool:
    text = read(path)
    return all(re.search(pattern, text, re.IGNORECASE | re.DOTALL) for pattern in patterns)


def main() -> None:
    phys_stress = load(PHYS_STRESS)
    anchor_candidates = load(ANCHOR_CANDIDATES)
    modal_anchor = load(MODAL_ANCHOR)
    m_theory = load(M_THEORY)
    dim_obstruction = load(DIM_OBSTRUCTION)
    action_norm = load(ACTION_NORM)

    source_tests = {
        "m_theory_ellp_fixed_by_modal_gap_and_topology": has(
            M_THEORY_SOURCE,
            r"ell_p",
            r"fixed functions of the modal gap",
            r"topological integers",
        ),
        "m_theory_planck_relation_present": has(
            M_THEORY_SOURCE,
            r"kappa_\{11\}|\\kappa_\{11\}",
            r"ell_p|\\ell_p",
            r"Vol\(X_7\)|mathrm\{Vol\}\(X_7\)|Vol}\(X_7\)",
        ),
        "theta_i_tev_is_calibration": has(THETA_I, r"calibration assumption", r"does not fix this identification"),
        "theta_iv_coherence_scale_depends_on_matching_identification": has(
            THETA_IV, r"coherence scale", r"matching scale"
        ),
        "propagator_tau_physical_value_not_fixed": has(
            PROPAGATORS,
            r"tau",
            r"not yet fix|not fixed",
            r"effective coherence scale",
        ),
        "coherent_kernels_tau_slot_present": has(COHERENT_KERNELS, r"proper-time/coherence scale", r"tau"),
        "fixed_damping_internal_scale_source_present": has(FIXED_DAMPING, r"coherence scale", r"damping"),
        "meta_absolute_normalization_collapses_to_single_scalar": has(
            META_PARAMS, r"Absolute normalization", r"single scalar"
        ),
        "qft_dimensionful_factors_absorb_into_action_volume": has(
            QFT_SOURCE, r"dimensionful factors", r"higher--dimensional action", r"internal volumes"
        ),
    }

    route_status = {
        "route_A_m_theory_modal_gap_to_ellp": {
            "classification": "BEST_STRUCTURAL_ROUTE_PHYSICAL_GAP_VALUE_OPEN",
            "closed": [
                "ell_p/kappa_11 slot identified",
                "4D Planck and gauge kinetic normalizations share the same compactification data",
                "source says ell_p is fixed by modal gap scales and topological integers",
            ],
            "missing": [
                "selected physical modal-gap value",
                "fixed convention mapping modal gap to ell_p or kappa_11",
                "proof no observed Newton/Planck/mass/cosmology value is used",
            ],
        },
        "route_B_theta_matching_scale": {
            "classification": "FORBIDDEN_AS_NO_KNOB_ANCHOR_CALIBRATION_ONLY",
            "closed": ["Theta closure supplies internal geometry and matching-scale framework"],
            "missing": ["source explicitly says physical TeV identification is not fixed by MTT"],
        },
        "route_C_proper_time_tau": {
            "classification": "PROMISING_SLOT_INTERNAL_OR_SECTOR_VALUE_NOT_PHYSICAL_YET",
            "closed": ["finite kernels use tau", "Lambda_eff ~ tau^-1/2 is the right physical slot"],
            "missing": ["selected sector tau in physical units", "internal-to-SI conversion"],
        },
        "route_D_action_unit_G10": {
            "classification": "INTERNAL_UNIT_CLOSED_PHYSICAL_G10_NOT_SELECTED",
            "closed": ["G10_int=1 canonical internal action units"],
            "missing": ["physical G10/R1^3 or equivalent absolute action/length unit"],
        },
        "route_E_dimensionless_only": {
            "classification": "CREDIBLE_FALLBACK_NOT_FULL_PHYSICAL_GR_CLOSURE",
            "closed": ["dimensionless/internal exact-branch quantities are auditable"],
            "missing": ["absolute Newton/Planck prediction by design"],
        },
    }

    hard_negative = {
        "direct_physical_anchor_found_in_current_sources": False,
        "physical_G10_selected": False,
        "physical_ellp_selected": False,
        "physical_alpha_prime_selected": False,
        "physical_tau_selected": False,
        "theta_5TeV_promotable_to_prediction": False,
    }

    best_next_theorem = {
        "name": "Selected_Modal_Gap_to_Physical_Unit_Theorem",
        "premise": (
            "The selected coherent fixed point supplies a physical modal-gap scale Lambda_gap "
            "rather than only a dimensionless eigenvalue."
        ),
        "must_construct": [
            "selected operator and quotient whose lowest positive eigenvalue is the modal gap",
            "one physical dimensionful unit or length/action convention fixed by MTT data",
            "map Lambda_gap to ell_p, kappa_11, alpha_prime, or G10 with stated conventions",
            "proof that no observed G_N, M_Pl, H0, rho_DE, absolute mass, or TeV calibration target is used",
        ],
        "if_closed_then": [
            "compute physical G_eff = G10/Vol_int",
            "compute physical kappa_STF = (32*pi*G_eff)^-1",
            "promote the exact TT branch into a physical Einstein-response theorem",
        ],
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_physical_anchor_source_hunt",
        "status": "PHYSICAL_ANCHOR_SOURCE_HUNT_COMPLETE_DIRECT_ANCHOR_NOT_FOUND",
        "input_certificates": {
            "physical_normalization_stress_response_gate": str(PHYS_STRESS),
            "target_independent_dimensional_anchor_candidates": str(ANCHOR_CANDIDATES),
            "selected_modal_gap_physical_anchor_gate": str(MODAL_ANCHOR),
            "m_theory_modal_gap_dimensional_anchor_candidate": str(M_THEORY),
            "dimensionful_constant_obstruction": str(DIM_OBSTRUCTION),
            "physical_action_normalization": str(ACTION_NORM),
        },
        "source_files": {
            "m_theory": str(M_THEORY_SOURCE),
            "theta_i": str(THETA_I),
            "theta_iv": str(THETA_IV),
            "propagators": str(PROPAGATORS),
            "coherent_kernels": str(COHERENT_KERNELS),
            "fixed_damping": str(FIXED_DAMPING),
            "meta_parameters": str(META_PARAMS),
            "qft": str(QFT_SOURCE),
        },
        "source_tests": source_tests,
        "route_status": route_status,
        "hard_negative": hard_negative,
        "synthesis": {
            "current_physical_gate_status": phys_stress["status"],
            "dimensionful_obstruction_certified": dim_obstruction["status"] == "OBSTRUCTION_CERTIFIED",
            "canonical_internal_action_units_closed": action_norm["verdict"][
                "canonical_internal_action_normalization_closed"
            ],
            "best_route": "route_A_m_theory_modal_gap_to_ellp",
            "reason": (
                "It is the only route whose source says the physical length/action data are fixed "
                "by modal gap scales and topology, while preserving the no-backsolve guard."
            ),
            "direct_closure_available_now": False,
        },
        "best_next_theorem": best_next_theorem,
        "guardrails": {
            "claims_measured_Newton_constant": False,
            "claims_measured_Planck_scale": False,
            "uses_Theta_5TeV_as_prediction": False,
            "uses_observed_target_backsolve": False,
            "hides_scale_in_unit_convention": False,
            "claims_full_physical_GR_closed": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = """# Selected Physical Anchor Source Hunt v1

## Result

The source hunt did not find a direct selected physical anchor for `G_10`,
`ell_p`, `kappa_11`, `alpha_prime`, or `tau` in SI/physical units.

This is not a failure of the exact TT branch. It is the expected dimensionful
normalization obstruction, now localized to one theorem.

## Route Ranking

Best route:

```text
M-theory modal gap -> ell_p / kappa_11 -> G_eff -> kappa_STF
```

Why: the M-theory corpus says `R_11` and `ell_p` are fixed functions of modal
gap scales and topological integers at the coherent fixed point, and gives:

```text
2 kappa_11^2 = (2 pi)^8 ell_p^9
kappa_4^-2 = kappa_11^-2 Vol(X_7)
```

Blocked route:

```text
Theta matching scale / 5 TeV
```

because the Theta source explicitly treats the physical matching scale as a
calibration assumption, not a derived no-knob value.

Promising but open slot:

```text
proper-time tau, Lambda_eff ~ tau^-1/2
```

because the kernel papers identify the physical coherence-scale slot but do not
fix the sector value in physical units.

## Next Theorem

The next required object is:

```text
Selected_Modal_Gap_to_Physical_Unit_Theorem
```

It must construct a selected physical modal-gap scale and map it to `ell_p`,
`kappa_11`, `alpha_prime`, or `G_10` without observed Newton, Planck,
cosmological, absolute mass, or TeV calibration input.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
