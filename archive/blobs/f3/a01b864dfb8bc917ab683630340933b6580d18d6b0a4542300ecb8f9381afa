"""Build the complement-spectrum or smooth-operator source gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

SMOOTH_GATE = DATA / "smooth_determinant_spectral_table_or_source_operator.candidate.json"
FINITE_PACKET = DATA / "hessian_kernel_central_cocycle_finite_galerkin_candidate.packet.json"

OUTPUT_DATA = DATA / "complement_spectrum_or_smooth_operator_source.candidate.json"
OUTPUT_CERT = CERTS / "complement_spectrum_or_smooth_operator_source_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Complement_Spectrum_or_Smooth_Operator_Source_v1.md"


def build() -> tuple[dict[str, object], dict[str, object], str]:
    smooth_gate = json.loads(SMOOTH_GATE.read_text(encoding="utf-8"))
    finite_packet = json.loads(FINITE_PACKET.read_text(encoding="utf-8"))

    routes = {
        "coherent_sector_quotient": {
            "claim": "Use only the selected coherent/projected Galerkin sector in the determinant.",
            "positive_evidence": [
                "finite packet has a projector-retention policy",
                "finite packet removes coefficient-gauge zero modes before the three-coordinate Gram block",
                "MTT corpus uses coherent-sector projectors and internal spectral gaps",
            ],
            "blocking_condition": "No current source states that every smooth complement mode cancels or is excluded from the Qa/SU3 threshold determinant.",
            "status": "PARTIAL_NOT_CLOSED",
        },
        "gap_suppression": {
            "claim": "Use spectral gaps to neglect complement modes.",
            "positive_evidence": [
                "fixed-point and Theta/Nil corpus provide positive gap and lower-bound language",
            ],
            "blocking_condition": "A positive gap gives control/decay, not an exact zeta determinant or exact cancellation.",
            "status": "REJECT_AS_EXACT_CLOSURE",
        },
        "same_source_smooth_operator": {
            "claim": "Supply a same-source smooth Qa/SU3 Nil/Iwasawa threshold operator.",
            "positive_evidence": [
                "Strominger/HYM and typed monad machinery supply compatible templates",
                "finite H_sel/G_ret/tau packet gives the required projected validator",
            ],
            "blocking_condition": "The current corpus still does not print the selected smooth operator, complement spectrum, heat table, analytic torsion, or Reidemeister torsion.",
            "status": "OPEN_PRIMARY",
        },
    }

    reduced_determinant_conditional = {
        "name": "ReducedCoherentSectorDeterminant",
        "conditional_statement": "If the selected Qa/SU3 determinant prescription is the coherent-sector projected determinant and the complement is quotiented/cancels by the BRST/coherent-sector policy, then the determinant is log(2008).",
        "value": "log(2008)",
        "conditions_needed": [
            "selected determinant domain is exactly the finite projected H_sel sector",
            "smooth complement determinant cancels, is quotiented, or is source-declared outside the threshold response",
            "no local FP/BRST or gauge quotient determinant is double-counted",
        ],
        "conditions_met_now": {
            "finite_projected_H_sel_sector": True,
            "complement_cancellation_or_quotient": False,
            "no_double_count_proof": False,
        },
        "status": "CONDITIONAL_NOT_PROMOTED",
    }

    no_go = {
        "name": "ComplementSpectrumRemainingSourceTheorem",
        "proof": [
            "The finite determinant gate closed log(2008) only for the projected H_sel block.",
            "The complement-spectrum test showed that adding a positive complement mode changes the determinant without changing H_sel.",
            "The current coherent-sector/projector language does not prove exact complement cancellation or quotienting for the Qa/SU3 threshold determinant.",
            "The current spectral-gap language does not determine zeta finite parts.",
            "Therefore no no-knob smooth determinant can be computed from the current source data beyond the conditional reduced determinant.",
        ],
        "verdict": "CURRENT_SOURCE_EXHAUSTED_AT_CONDITIONAL_REDUCED_DETERMINANT",
    }

    candidate = {
        "candidate": "SelectedQaSU3ComplementSpectrumOrSmoothOperatorSource",
        "status": "QA_SU3_COMPLEMENT_SPECTRUM_GATE_CURRENT_SOURCE_EXHAUSTED_REDUCED_DETERMINANT_CONDITIONAL",
        "input_smooth_gate": str(SMOOTH_GATE.relative_to(ROOT)),
        "input_finite_packet": str(FINITE_PACKET.relative_to(ROOT)),
        "route_tests": routes,
        "reduced_determinant_conditional": reduced_determinant_conditional,
        "no_go": no_go,
        "decision": {
            "reduced_coherent_sector_determinant": "CONDITIONAL_LOG_2008",
            "smooth_complement_policy": "OPEN",
            "same_source_smooth_operator": "OPEN",
            "full_Qa_SU3_threshold_closure_now": False,
            "next_required_artifact": "Selected_Qa_SU3_Source_Amendment_Complement_Quotient_or_Smooth_Spectrum_v1",
        },
        "what_this_closes": [
            "all current-source routes for the complement are tested",
            "reduced coherent-sector determinant value is isolated as log(2008)",
            "exact condition for promoting log(2008) is stated",
        ],
        "what_remains_open": [
            "source amendment or theorem that quotients/cancels the smooth complement",
            "or a selected smooth operator spectrum/heat/zeta/torsion table",
            "full Qa/SU3 threshold determinant",
        ],
        "closure_claimed": False,
        "target_fitting_used": False,
        "finite_packet_projector_policy": finite_packet["admissibility"]["projector_retention_checked"],
        "finite_packet_zero_mode_policy": finite_packet["admissibility"]["zero_mode_policy"],
        "prior_finite_determinant": smooth_gate["finite_hessian_determinant"],
    }

    certificate = {
        "certificate": "SelectedQaSU3ComplementSpectrumOrSmoothOperatorSource",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "complement_routes_tested": True,
            "conditional_reduced_determinant_is_log2008": True,
            "current_source_exhausted_for_smooth_determinant": True,
        },
        "what_remains_open": {
            "complement_quotient_or_cancellation_source": True,
            "same_source_smooth_operator_spectrum": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["decision"]["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, object]) -> str:
    reduced = candidate["reduced_determinant_conditional"]
    return f"""# Selected Qa/SU3 Complement Spectrum or Smooth Operator Source v1

## Result

The reduced determinant is isolated, but not promoted.

```text
conditional reduced coherent-sector determinant = {reduced["value"]}
```

This becomes the full Qa/SU3 threshold determinant only if the selected source
proves that the smooth complement is quotiented, cancels, or lies outside the
threshold response.

## Route Tests

```text
coherent-sector quotient: {candidate["route_tests"]["coherent_sector_quotient"]["status"]}
gap suppression: {candidate["route_tests"]["gap_suppression"]["status"]}
same-source smooth operator: {candidate["route_tests"]["same_source_smooth_operator"]["status"]}
```

The current source data support projectors and gaps, but not exact complement
cancellation and not a full smooth spectrum.

## Hard Verdict

The current source is exhausted for the smooth determinant.  The next move must
be a genuine source amendment or located source packet:

```text
{candidate["decision"]["next_required_artifact"]}
```

No target fitting was used, and full Qa/SU3 closure is not claimed.
"""


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
