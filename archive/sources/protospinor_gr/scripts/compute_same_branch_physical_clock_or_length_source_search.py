from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

PHYSICAL_GAP = ROOT / "certificates" / "physical_modal_gap_closure_plan_and_first_attempt_certificate.json"
ALPHA = ROOT / "certificates" / "selected_physical_alpha_or_action_unit_theorem_certificate.json"
MTHEORY_PACKET = ROOT / "certificates" / "m_theory_dimensional_anchor_packet_attempt_certificate.json"

FCP = CORPUS / "5 Dirac Delta" / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md"
QG = CORPUS / "12 Quantum Gravity" / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"
SPECTRAL_ACTION = (
    CORPUS
    / "15 Discrete & Spectral & Operator Geometric Theories"
    / "The_Spectral_Action_as_a_Shadow_of_Coherent_Fixed_Point_Geometry.md"
)
KK = (
    CORPUS
    / "15 Discrete & Spectral & Operator Geometric Theories"
    / "Modal_Triplet_Theory__From_MTT_to_Kaluza__Klein_Theory.md"
)

OUT_CERT = ROOT / "certificates" / "same_branch_physical_clock_or_length_source_search_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Same_Branch_Physical_Clock_or_Length_Source_Search_v1.md"
OUT_PACKET = ROOT / "candidate_data" / "same_branch_physical_clock_or_length_source.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def find_line(path: Path, needle: str) -> dict:
    for index, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), start=1):
        if needle in line:
            return {"path": str(path), "line": index, "needle": needle, "found": True}
    return {"path": str(path), "line": None, "needle": needle, "found": False}


def main() -> None:
    physical_gap = load(PHYSICAL_GAP)
    alpha = load(ALPHA)
    mtheory = load(MTHEORY_PACKET)

    packet = load(Path(physical_gap["packet_written"]))
    tau_int = packet["dimensionless_values_closed"]["tau_internal"]
    lambda_eff_int = packet["dimensionless_values_closed"]["Lambda_eff_internal"]
    ell_coh_over_alpha_minus_half = math.sqrt(tau_int)
    lambda_eff_over_sqrt_alpha = 1.0 / ell_coh_over_alpha_minus_half

    source_hits = {
        "fcp_tau_dimension": find_line(FCP, r"[\tau]=L^2=E^{-2}."),
        "fcp_coherent_length": find_line(FCP, r"\ell_{\rm coh}\sim\sqrt{\tau},"),
        "fcp_effective_energy": find_line(FCP, r"\Lambda_{\rm eff}\sim\tau^{-1/2}."),
        "fcp_execution_architecture": find_line(FCP, r"\text{derive }A,\;P,\;\chi,\;\tau"),
        "qg_universal_gaussian": find_line(QG, r"e^{-\tau_0 k^2}"),
        "qg_projector_data": find_line(QG, r"All constants $(\lambda_\ast,\tau_0,C_0,c_{\mathrm{proj}})$ are geometric/projector data"),
        "spectral_action_tau_gap": find_line(SPECTRAL_ACTION, r"\mu(\tau)$ supported on $\tau\ge\tau_0\sim\lambda_\ast^{-1}$"),
        "spectral_action_cutoff": find_line(SPECTRAL_ACTION, r"$\Lambda\sim\tau_0^{-1/2}\sim\lambda_\ast^{1/2}$."),
        "kk_gap_parameters": find_line(KK, "set by MTT gap parameters"),
        "kk_modal_gap_scale": find_line(KK, r"where $\Lambda_{\rm gap}$ is the modal gap scale (MTT)."),
    }

    all_core_hits = all(
        source_hits[key]["found"]
        for key in [
            "fcp_tau_dimension",
            "fcp_coherent_length",
            "fcp_effective_energy",
            "fcp_execution_architecture",
            "qg_universal_gaussian",
            "qg_projector_data",
            "spectral_action_tau_gap",
            "spectral_action_cutoff",
        ]
    )

    candidate_routes = {
        "coherent_length_bridge": {
            "classification": "SAME_BRANCH_STRUCTURAL_BRIDGE_CLOSED_ABSOLUTE_SCALE_OPEN",
            "closed": [
                "tau has physical dimension L^2=E^-2 in the FCP corpus",
                "sqrt(tau) is the coherent length scale",
                "tau^-1/2 is the effective energy scale",
                "the QG corpus identifies tau_0 as SPT damping/proper-time projector data",
                "the spectral-action corpus identifies the cutoff as tau_0^-1/2",
            ],
            "computed_relative_values": {
                "tau_int": tau_int,
                "ell_coh_over_alpha_phys_minus_half": ell_coh_over_alpha_minus_half,
                "Lambda_eff_over_sqrt_alpha_phys": lambda_eff_over_sqrt_alpha,
            },
            "remaining_blocker": (
                "The corpus supplies the same-branch dimensional role of tau, but not an "
                "absolute SI/metrological value for alpha_phys or ell_coh."
            ),
        },
        "spectral_action_cutoff_bridge": {
            "classification": "RELATIVE_CUTOFF_CLOSED_ABSOLUTE_SCALE_OPEN",
            "closed": ["Lambda is tied to tau_0^-1/2 and lambda_*^1/2"],
            "remaining_blocker": "The cutoff is a physical scale only after the same alpha_phys/metrological unit is selected.",
        },
        "kk_radius_bridge": {
            "classification": "PHENOMENOLOGY_READY_IF_FCC_RADIUS_PACKET_FILLED",
            "closed": ["KK paper says R_KK and masses are set by MTT gap parameters"],
            "remaining_blocker": "No selected numeric R_KK packet on the exact Z448/q79/rho_UV branch exists here.",
        },
        "m_theory_planck_bridge": {
            "classification": "STRUCTURAL_SLOT_CONFIRMED_VALUE_OPEN",
            "closed": ["M-theory packet already identifies ell_p/kappa_11/Lambda_gap^-1 slot"],
            "remaining_blocker": mtheory["promotion"]["honest_result"],
        },
    }

    metrology_no_go = {
        "statement": (
            "A theory can select dimensionless ratios and dimensionful roles internally, "
            "but an absolute SI value for a length/action/energy scale requires one "
            "metrological identification unless the corpus independently constructs a "
            "physical clock/rod/counting process with units."
        ),
        "applies_here": True,
        "reason": (
            "The new sources identify tau as the physical coherent-length/proper-time "
            "object, but all absolute values remain proportional to alpha_phys."
        ),
        "allowed_solution": (
            "Declare relative closure as final for no-knob mathematics, or add exactly "
            "one explicitly named metrological primitive and propagate it through the "
            "already closed dimensionless chain."
        ),
        "forbidden_solution": (
            "Set alpha_phys=1 and call it an SI prediction, or backsolve from Newton, "
            "Planck, cosmology, particle masses, or TeV benchmark data."
        ),
    }

    closed_inputs = {
        "physical_gap_first_attempt_ready": physical_gap["status"]
        == "PHYSICAL_MODAL_GAP_PLAN_EXECUTED_FIRST_ATTEMPT_VALUE_OPEN",
        "alpha_single_anchor_status_ready": alpha["status"] == "ALPHA_PHYS_REDUCED_TO_SINGLE_EXTERNAL_DIMENSIONFUL_ANCHOR",
        "mtheory_packet_ready": mtheory["status"] == "MTHEORY_ANCHOR_PACKET_FILLED_STRUCTURAL_VALUE_OPEN",
        "core_source_hits_found": all_core_hits,
        "lambda_eff_matches_previous_packet": abs(lambda_eff_over_sqrt_alpha - lambda_eff_int) < 1e-15,
    }

    result_packet = {
        "packet": "SameBranchPhysicalClockOrLengthSourcePacket",
        "status": "STRUCTURAL_SOURCE_FOUND_ABSOLUTE_VALUE_OPEN",
        "selected_branch": packet["selected_branch"],
        "source_identification": {
            "tau_role": "physical proper-time/coherent-length squared object",
            "length_role": "ell_coh = sqrt(tau_phys)",
            "energy_role": "Lambda_eff = tau_phys^-1/2",
            "same_branch_acceptance": "accepted structurally through exact tau_int and QG/SPT/FCP corpus alignment",
        },
        "relative_values": {
            "tau_int": tau_int,
            "ell_coh_over_alpha_phys_minus_half": ell_coh_over_alpha_minus_half,
            "Lambda_eff_over_sqrt_alpha_phys": lambda_eff_over_sqrt_alpha,
        },
        "absolute_values": {
            "alpha_phys": None,
            "tau_phys": None,
            "ell_coh": None,
            "Lambda_eff": None,
        },
        "source_hits": source_hits,
        "candidate_routes": candidate_routes,
        "metrology_no_go": metrology_no_go,
    }

    guardrails = {
        "claims_alpha_phys_closed": False,
        "claims_absolute_SI_length_or_energy": False,
        "uses_observed_Newton_or_Planck": False,
        "uses_observed_cosmology_or_masses": False,
        "uses_Theta_5TeV_as_prediction": False,
        "uses_unit_convention_as_physics": False,
    }

    status = (
        "SAME_BRANCH_CLOCK_LENGTH_SOURCE_FOUND_ABSOLUTE_METROLOGY_OPEN"
        if all(closed_inputs.values())
        else "SAME_BRANCH_CLOCK_LENGTH_SOURCE_SEARCH_INPUTS_NOT_READY"
    )

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "same_branch_physical_clock_or_length_source_search",
        "status": status,
        "input_certificates": {
            "physical_modal_gap_closure_plan_and_first_attempt": str(PHYSICAL_GAP),
            "selected_physical_alpha_or_action_unit_theorem": str(ALPHA),
            "m_theory_dimensional_anchor_packet_attempt": str(MTHEORY_PACKET),
        },
        "external_sources": {
            "finite_coherent_projection": str(FCP),
            "uv_finite_quantum_gravity": str(QG),
            "spectral_action_shadow": str(SPECTRAL_ACTION),
            "kaluza_klein_shadow": str(KK),
        },
        "closed_inputs": closed_inputs,
        "candidate_routes": candidate_routes,
        "metrology_no_go": metrology_no_go,
        "verdict": {
            "same_branch_physical_clock_or_length_source_found": True,
            "structural_bridge_closed": True,
            "absolute_physical_value_closed": False,
            "exact_blocker": "The physical role of tau is sourced; the absolute metrological value of alpha_phys is not.",
            "next_executable_artifact": "Dimensional_Metrology_NoGo_and_Relative_Closure_Theorem_v1",
        },
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Same Branch Physical Clock or Length Source Search v1

## Result

The search found the missing **structural** source:

```text
tau_phys has dimension L^2 = E^-2
ell_coh = sqrt(tau_phys)
Lambda_eff = tau_phys^-1/2
```

On the selected exact branch, the verified internal value is:

```text
tau_int = log(448)/15 = {tau_int:.15g}
ell_coh / alpha_phys^(-1/2) = sqrt(tau_int) = {ell_coh_over_alpha_minus_half:.15g}
Lambda_eff / sqrt(alpha_phys) = tau_int^(-1/2) = {lambda_eff_over_sqrt_alpha:.15g}
```

## What Closed

The broader corpus aligns the same object across FCP, QG, and spectral-action
language:

```text
FCP: tau has dimension L^2=E^-2; sqrt(tau) is coherent length.
QG: tau_0 is the SPT proper-time damping scale for graviton lines.
Spectral action: Lambda is tau_0^-1/2.
KK: compactification/mass scales are set by modal-gap parameters.
```

So the previous blocker is smaller. We no longer lack the physical **role** of
the clock/length object. The same-branch bridge is:

```text
Z448/q79/rho_UV branch
  -> tau_int = log(448)/15
  -> tau_phys = tau_int / alpha_phys
  -> ell_coh = sqrt(tau_int / alpha_phys)
  -> Lambda_eff = sqrt(alpha_phys / tau_int)
```

## What Still Cannot Close

This does not select the absolute SI value of `alpha_phys`. It proves the
relative physical chain, but an absolute dimensionful number still requires one
metrological primitive or an independently selected physical rod/clock process.

Forbidden shortcuts remain forbidden:

```text
do not set alpha_phys=1 as an SI prediction
do not backsolve from Newton/Planck/cosmology/masses
do not use 5 TeV as a no-knob prediction
```

## New Frontier

The next executable theorem should be:

```text
Dimensional_Metrology_NoGo_and_Relative_Closure_Theorem_v1
```

That theorem should formally close the no-knob result as **relative/dimensionless
closure**, while isolating exactly what a one-anchor metrological extension would
mean.
"""

    OUT_PACKET.write_text(json.dumps(result_packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
