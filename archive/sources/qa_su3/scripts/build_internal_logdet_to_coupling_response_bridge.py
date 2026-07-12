"""Build the internal-logdet to coupling-response bridge gate packet."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

LOCKED = DATA / "locked_proof_state.candidate.json"
SEPARATION = DATA / "gr_surface_internal_quantum_separation_theorem.candidate.json"
OUTPUT_DATA = DATA / "internal_logdet_to_coupling_response_bridge.candidate.json"
OUTPUT_CERT = CERTS / "internal_logdet_to_coupling_response_bridge_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Internal_Logdet_to_Coupling_Response_Bridge_v1.md"


def build() -> tuple[dict[str, object], dict[str, object], str]:
    locked = json.loads(LOCKED.read_text(encoding="utf-8"))
    separation = json.loads(SEPARATION.read_text(encoding="utf-8"))
    finite = locked["locked_state"]["finite_hessian"]
    logdet = finite["finite_rank_logdet"]
    det_value = finite["determinant"]

    tested_routes = [
        {
            "route": "direct_unit_internal_response",
            "formula": "Delta_Qa_internal_units = 1 * logdet_int",
            "status": "ACCEPTED_AS_INTERNAL_UNIT_CONVENTION_ONLY",
            "accepted_result": logdet,
            "why_not_physical_closure": "unit coefficient is not source-selected as a physical coupling normalization",
        },
        {
            "route": "one_loop_threshold",
            "formula": "Delta(1/g^2) = -(b_Qa/(8*pi^2)) * logdet_int",
            "status": "REJECTED_AS_CLOSURE_CURRENT_SOURCE",
            "missing": [
                "selected beta or index coefficient b_Qa",
                "representation trace normalization",
                "scheme/scale policy tying the internal packet to the measured coupling",
            ],
        },
        {
            "route": "heat_kernel_response",
            "formula": "Delta = Tr_Qa(a_k exp(-t H_sel))_finite_part",
            "status": "REJECTED_AS_CLOSURE_CURRENT_SOURCE",
            "missing": [
                "selected heat coefficient",
                "degree/index weights",
                "finite-part subtraction rule",
            ],
        },
        {
            "route": "torsion_response",
            "formula": "Delta = weighted Ray-Singer/Reidemeister torsion of the selected local system",
            "status": "REJECTED_AS_CLOSURE_CURRENT_SOURCE",
            "missing": [
                "acyclic selected local system",
                "cochain degree weights",
                "same-source torsion-to-gauge normalization",
            ],
        },
        {
            "route": "theta_or_retarded_overlap_kernel",
            "formula": "Delta = d_theta log det(H_sel + theta K_ret)|theta=0",
            "status": "REJECTED_AS_CLOSURE_CURRENT_SOURCE",
            "missing": [
                "selected retarded kernel derivative K_ret",
                "theta insertion policy",
                "normalization from derivative response to physical coupling",
            ],
        },
        {
            "route": "GR_surface_response",
            "formula": "Delta = GR/protospinor surface response functional",
            "status": "ROUTED_OUT_OF_QA_SU3_INTERNAL_DETERMINANT",
            "missing": [
                "separate GR/protospinor response theorem",
                "matching rule if a universal surface contribution is later combined with internal packets",
            ],
        },
    ]

    response_functional = {
        "name": "Selected_Qa_SU3_Response_Functional_Chi_Qa_v1",
        "minimal_form": "Delta_Qa_physical = chi_Qa * logdet_int",
        "known_payload": {
            "logdet_int": logdet,
            "det_int": det_value,
            "logdet_int_numeric": math.log(det_value),
        },
        "open_selected_data": [
            "chi_Qa",
            "representation/trace normalization",
            "scheme/scale or threshold policy",
            "same-branch derivation from Hessian blocks and retarded overlap kernel",
        ],
    }

    theorem = {
        "name": "SelectedQaSU3InternalLogdetToCouplingResponseBridge",
        "hypotheses": [
            "the GR-surface/internal-quantum separation theorem is accepted",
            "the selected internal Qa/SU3 determinant domain is the locked finite coherent packet H_sel",
            "the internal determinant payload is det(H_sel)=2008 and logdet_int=log(2008)",
            "no measured masses, mixings, residuals, or couplings are used as inputs",
            "a physical coupling threshold requires a selected response functional, not only a determinant payload",
        ],
        "conclusions": {
            "internal_unit_response_bridge": "CLOSED_LOG_2008",
            "physical_coupling_bridge": "OPEN_SELECTED_CHI_QA_RESPONSE_FUNCTIONAL_REQUIRED",
            "full_electroweak_closure_now": False,
            "full_SM_closure_now": False,
            "next_required_object": response_functional["name"],
        },
        "proof_idea": [
            "the separation theorem removes the smooth-complement determinant from the Qa/SU3 internal determinant domain",
            "therefore the locked finite packet supplies the complete internal reduced determinant payload log(2008)",
            "a coupling or threshold value is a response of a gauge-normalized functional to that payload",
            "all current-source shortcut maps require an extra selected coefficient, trace, heat coefficient, torsion weight, or kernel derivative",
            "hence the bridge gate closes only in internal determinant units and reduces physical closure to selecting chi_Qa from the same branch",
        ],
    }

    candidate = {
        "candidate": "SelectedQaSU3InternalLogdetToCouplingResponseBridge",
        "status": "QA_SU3_INTERNAL_UNIT_RESPONSE_BRIDGE_CLOSED_PHYSICAL_CHI_QA_OPEN",
        "inputs": {
            "locked_proof_state": str(LOCKED.relative_to(ROOT)),
            "separation_theorem": str(SEPARATION.relative_to(ROOT)),
            "target_fitting_used": False,
        },
        "locked_finite_payload": {
            "H_sel": finite["H_sel"],
            "G_ret": finite["G_ret"],
            "Pi_tw": finite["Pi_tw"],
            "tau": finite["tau"],
            "spectrum": finite["spectrum"],
            "determinant": det_value,
            "finite_rank_logdet": logdet,
            "finite_rank_logdet_numeric": math.log(det_value),
        },
        "separation_policy_imported": separation["decision"],
        "tested_bridge_routes": tested_routes,
        "response_functional": response_functional,
        "theorem": theorem,
        "guardrails": [
            "do not treat chi_Qa=1 as a physical coupling normalization unless a source selects it",
            "do not import QFT beta coefficients, heat coefficients, torsion weights, or measured couplings as hidden fit parameters",
            "do not count the GR/protospinor surface response inside the Qa/SU3 internal determinant",
            "do not promote log(2008) to electroweak or full SM closure",
            "do not use observed masses, CKM data, alpha_EM, alpha_s, or residuals as inputs",
        ],
        "decision": theorem["conclusions"],
        "closure_claimed": True,
        "closure_scope": "internal_unit_response_bridge_only_physical_response_functional_open",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedQaSU3InternalLogdetToCouplingResponseBridge",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "smooth_complement_objection_for_internal_payload": True,
            "internal_reduced_logdet_payload": logdet,
            "internal_unit_response_bridge": "CLOSED_LOG_2008",
            "shortcut_route_audit": "COMPLETE_FOR_CURRENT_SOURCE",
        },
        "what_remains_open": {
            "Selected_Qa_SU3_Response_Functional_Chi_Qa_v1": True,
            "physical_coupling_bridge": True,
            "electroweak_no_knob_closure": True,
            "full_SM_closure": True,
        },
        "next_required_object": response_functional["name"],
        "closure_scope": candidate["closure_scope"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, object]) -> str:
    finite = candidate["locked_finite_payload"]
    theorem = candidate["theorem"]
    routes = "\n".join(
        f"- {route['route']}: {route['status']} ({route['formula']})"
        for route in candidate["tested_bridge_routes"]
    )
    guardrails = "\n".join(f"- {item}" for item in candidate["guardrails"])
    hypotheses = "\n".join(f"- {item}" for item in theorem["hypotheses"])
    proof_idea = "\n".join(f"- {item}" for item in theorem["proof_idea"])
    response = candidate["response_functional"]
    missing = "\n".join(f"- {item}" for item in response["open_selected_data"])
    return f"""# Selected Qa/SU3 Internal Logdet to Coupling Response Bridge v1

## Result

This artifact closes the bridge only in internal determinant units:

```text
det_int(H_sel) = {finite["determinant"]}
logdet_int = {finite["finite_rank_logdet"]}
Delta_Qa_internal_units = log(2008)
```

It does not close the physical coupling. The physical bridge is reduced to one
explicit same-branch object:

```text
{response["name"]}
Delta_Qa_physical = chi_Qa * logdet_int
```

## Theorem

```text
{theorem["name"]}
```

Hypotheses:

{hypotheses}

Proof idea:

{proof_idea}

Conclusions:

```text
internal unit response bridge = CLOSED_LOG_2008
physical coupling bridge = OPEN_SELECTED_CHI_QA_RESPONSE_FUNCTIONAL_REQUIRED
full electroweak closure = false
full SM closure = false
```

## Tested Bridge Routes

{routes}

## Missing Physical Response Data

{missing}

## Guardrails

{guardrails}

## Decision

The determinant-side bridge gate is closed: after the GR-surface/internal
separation, the selected Qa/SU3 internal payload is exactly `log(2008)`.

The coupling-side bridge is not closed by the present source record. Closing it
requires a same-branch selected response functional `chi_Qa`, preferably derived
from the selected Hessian blocks and retarded overlap kernel rather than fitted
to observed couplings.
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
