"""Build HYM mu-selection or full-DeltaA spectrum theorem."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "payload_reduction": DATA / "selected_heterotic_strominger_analytic_torsion_or_threshold_operator_payload.candidate.json",
    "hym_block": DATA / "selected_heterotic_hym_delta_a_invariant_block_computation.candidate.json",
    "torsional_ou_attempt": DATA / "selected_heterotic_torsional_endomorphism_or_ou_mode_weights.candidate.json",
    "threshold_template": DATA / "selected_heterotic_strominger_threshold_operator_or_torsion_source.template.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_hym_mu_selection_or_full_deltaa_spectrum.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_hym_mu_selection_or_full_deltaa_spectrum_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_HYM_Mu_Selection_or_Full_DeltaA_Spectrum_v1.md"

STATUS = "HETEROTIC_HYM_MU_SELECTION_NO_EXTREMUM_FULL_DELTAA_SPECTRUM_OPEN"
NEXT = "Selected_Heterotic_HYM_FullQuotientSpectrum_or_OUHessianScale_SourcePacket_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def positive_det(mu: float) -> float:
    return 12.0 * mu**9 * (1.0 + mu) * (2.0 + mu) * (1.0 + 2.0 * mu)


def dlogdet(mu: float) -> float:
    return 9.0 / mu + 1.0 / (1.0 + mu) + 1.0 / (2.0 + mu) + 2.0 / (1.0 + 2.0 * mu)


def main() -> dict[str, Any]:
    payload = load(INPUTS["payload_reduction"])
    hym_block = load(INPUTS["hym_block"])
    torsional = load(INPUTS["torsional_ou_attempt"])
    template = load(INPUTS["threshold_template"])

    samples = {
        "mu_0.25": {"det_prime": positive_det(0.25), "d_logdet": dlogdet(0.25)},
        "mu_1": {"det_prime": positive_det(1.0), "d_logdet": dlogdet(1.0)},
        "mu_4": {"det_prime": positive_det(4.0), "d_logdet": dlogdet(4.0)},
    }

    monotonicity_proof = {
        "logdet": hym_block["computation"]["positive_logdet_prime"],
        "derivative": "d/dmu log det' = 9/mu + 1/(1+mu) + 1/(2+mu) + 2/(1+2*mu)",
        "domain": "mu > 0",
        "all_terms_positive_on_domain": True,
        "strictly_increasing": True,
        "stationary_point_exists_on_mu_positive": False,
        "extremal_mu_selected_by_invariant_block": False,
        "samples": samples,
    }

    source_tests = {
        "invariant_block_extremum": {
            "can_select_mu": False,
            "reason": "The exact determinant-prime is strictly increasing for mu>0.",
        },
        "internal_mu_equals_one": {
            "can_select_physical_mu": False,
            "reason": "mu=1 is allowed only in already closed internal determinant units, not as a physical heterotic threshold scale.",
        },
        "torsional_OU_attempt": {
            "can_select_mu": torsional["decision"]["mu_selected"],
            "OU_weights_computed": torsional["decision"]["OU_weights_computed"],
            "Weitzenbock_E_computed": torsional["decision"]["Weitzenbock_E_computed"],
            "reason": "The torsional/OU packet fills geometry support but no source-derived OU weights or Weitzenbock E_Qa.",
        },
        "local_system_torsion_exit": {
            "can_select_threshold_now": False,
            "reason": "No selected compact Nil/Iwasawa character, acyclicity policy, or torsion finite part is emitted.",
        },
        "full_deltaA_spectrum_exit": {
            "can_select_threshold_now": False,
            "reason": "The invariant End(C^3) block is computed, but the full quotient domain, BRST/zero-mode policy, trace weights, and physical threshold convention remain open.",
        },
    }

    decision = {
        "mu_selected": False,
        "invariant_block_mu_extremum_refuted": True,
        "full_deltaA_spectrum_computed": False,
        "local_system_torsion_computed": False,
        "threshold_payload_closed": False,
        "measured_electroweak_closure": False,
        "best_next_source_packet": "full quotient spectrum or OU/Hessian scale selector",
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticHYMMuSelectionOrFullDeltaASpectrum",
        "status": STATUS,
        "inputs": {name: rel(path) for name, path in INPUTS.items()},
        "input_statuses": {
            "payload_reduction": payload["status"],
            "hym_block": hym_block["status"],
            "torsional_ou_attempt": torsional["status"],
            "threshold_template": template["status"],
        },
        "monotonicity_proof": monotonicity_proof,
        "source_tests": source_tests,
        "decision": decision,
        "closed_now": {
            "exact_logdet_derivative": True,
            "no_invariant_block_mu_extremum": True,
            "mu_equals_one_physical_promotion_rejected": True,
            "next_source_packet_identified": True,
        },
        "still_open": {
            "source_selected_mu_or_moduli": True,
            "full_DeltaA_quotient_domain": True,
            "BRST_zero_mode_policy": True,
            "trace_weights_for_Qa_Qc_SU2": True,
            "heat_zeta_torsion_finite_part": True,
            "physical_threshold_convention": True,
            "mu_match_and_RG_scheme": True,
        },
        "guardrails": {
            "does_not_choose_mu_by_convenience": True,
            "does_not_import_internal_mu1_as_physical": True,
            "does_not_use_observed_electroweak_data": True,
            "does_not_promote_invariant_block_to_full_threshold": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "HYMInvariantBlockMuNoExtremumTheorem",
            "proved": True,
            "statement": (
                "For the exact source-computed invariant HYM block, det'(M_inv(mu)) "
                "equals 12*mu^9*(1+mu)*(2+mu)*(1+2*mu). Hence d/dmu log det' "
                "is 9/mu + 1/(1+mu) + 1/(2+mu) + 2/(1+2*mu), strictly positive "
                "for every mu>0. Therefore this invariant block cannot select mu "
                "by an extremum or stationary condition. Physical threshold closure "
                "requires a new same-source object: the full quotient Delta_A "
                "spectrum/finite part, or an OU/Strominger Hessian scale selector, "
                "plus trace weights and RG/matching convention."
            ),
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "derivative_positive_for_mu_gt_0": True,
        "mu_selected": False,
        "full_deltaA_spectrum_computed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic HYM Mu Selection or Full DeltaA Spectrum v1

## Result

```text
status = {STATUS}
det'(M_inv(mu)) = 12*mu^9*(1+mu)*(2+mu)*(1+2*mu)
d/dmu log det' > 0 for mu > 0
mu_selected = false
full_deltaA_spectrum_computed = false
next_required_artifact = {NEXT}
```

## What Closed

The invariant HYM block cannot select `mu` by an internal stationary principle.
Its log determinant is strictly increasing:

```text
d/dmu log det' = 9/mu + 1/(1+mu) + 1/(2+mu) + 2/(1+2*mu)
```

Every summand is positive for `mu > 0`.

## What Remains

The next object must supply one of:

- a full quotient `Delta_A` spectrum with BRST/zero-mode policy and trace weights;
- an OU/Strominger Hessian scale selector for `mu`;
- a selected local-system torsion finite part.

Internal `mu=1` remains valid only inside the already closed internal determinant
accounting, not as a physical heterotic threshold selector.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(result["status"])
