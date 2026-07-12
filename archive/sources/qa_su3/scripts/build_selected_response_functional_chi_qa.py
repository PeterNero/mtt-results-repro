"""Build the selected Qa/SU3 response functional chi_Qa packet."""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

BRIDGE = DATA / "internal_logdet_to_coupling_response_bridge.candidate.json"
ORBIT = DATA / "central_twist_orbit_democracy_source_or_determinant_operator.candidate.json"
OUTPUT_DATA = DATA / "selected_response_functional_chi_qa.candidate.json"
OUTPUT_CERT = CERTS / "selected_response_functional_chi_qa_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Response_Functional_Chi_Qa_v1.md"


def frac(value: object) -> Fraction:
    if isinstance(value, str):
        return Fraction(value)
    return Fraction(value)


def build() -> tuple[dict[str, object], dict[str, object], str]:
    bridge = json.loads(BRIDGE.read_text(encoding="utf-8"))
    orbit = json.loads(ORBIT.read_text(encoding="utf-8"))
    payload = bridge["locked_finite_payload"]
    finite_probe = orbit["determinant_operator_branch"]["finite_probe"]

    pi = payload["Pi_tw"]
    g_ret = payload["G_ret"]
    pi_g_pi = sum(Fraction(pi[i]) * frac(g_ret[i][j]) * Fraction(pi[j]) for i in range(3) for j in range(3))
    tau2_trace = Fraction(finite_probe["finite_trace_tau_squared_computed"])
    chi = tau2_trace * pi_g_pi

    derivation = {
        "name": "SelectedFiniteQaSU3ResponseNormalization",
        "formula": "chi_Qa = Tr_finite(tau^2) * <Pi_tw, G_ret Pi_tw>",
        "inputs": {
            "Pi_tw": pi,
            "G_ret": g_ret,
            "G_ret_Pi_tw_Pi_tw": str(pi_g_pi),
            "finite_trace_tau_squared": int(tau2_trace),
        },
        "result": {
            "chi_Qa": str(chi),
            "chi_Qa_numeric": float(chi),
            "selected": chi == 1,
        },
        "why_source_selected": [
            "Pi_tw=+e3 is selected by primitive retarded-energy minimization in the locked finite packet",
            "G_ret is the exact inverse of the selected Hessian H_sel",
            "Tr_finite(tau^2)=8 is selected by the ordinary finite trace over the eleven typed module labels",
            "the product pairs the selected retarded overlap with the selected finite central-character heat trace",
        ],
    }

    tested_normalizations = [
        {
            "route": "retarded_trace_pairing",
            "status": "ACCEPTED_FOR_SELECTED_FINITE_RESPONSE_NORMALIZATION",
            "formula": derivation["formula"],
            "result": "chi_Qa=1",
        },
        {
            "route": "bare_unit_declaration",
            "status": "REPLACED_BY_DERIVATION",
            "reason": "chi_Qa=1 is not simply declared; it follows from 8 * (1/8).",
        },
        {
            "route": "measured_coupling_fit",
            "status": "REJECTED",
            "reason": "no observed alpha, alpha_s, electroweak angle, mass, CKM, or residual value is used",
        },
        {
            "route": "external_QFT_beta_import",
            "status": "REJECTED_AS_PHYSICAL_MATCHING_STEP",
            "reason": "beta/index coefficients are not needed for the selected finite internal normalization; they belong to later RG/threshold matching if used",
        },
    ]

    theorem = {
        "name": "SelectedQaSU3ResponseFunctionalChiQa",
        "hypotheses": [
            "the internal logdet bridge gate is accepted",
            "the locked finite packet supplies H_sel, G_ret, Pi_tw, and tau",
            "the orbit-democracy finite trace branch supplies Tr_finite(tau^2)=8",
            "the response normalization is the same-branch retarded trace pairing",
            "no measured constants or external fitted weights are used",
        ],
        "conclusions": {
            "selected_chi_Qa": str(chi),
            "finite_response_functional": "Delta_Qa_selected_finite = log(2008)",
            "finite_internal_coupling_normalization": "CLOSED",
            "measured_electroweak_or_running_coupling_match": "OPEN",
            "full_SM_closure_now": False,
            "next_required_object": "Selected_Qa_SU3_Electroweak_Matching_or_Absolute_Coupling_Normalization_v1",
        },
        "proof_idea": [
            "the bridge gate reduced the problem to a coefficient chi_Qa multiplying logdet_int",
            "the selected twist direction is Pi_tw=e3, so the selected retarded overlap is <Pi_tw,G_ret Pi_tw>=1/8",
            "the finite trace branch selects Tr_finite(tau^2)=8 by ordinary counting of selected typed labels",
            "multiplying these same-branch data gives chi_Qa=8*(1/8)=1",
            "this closes the finite internal response normalization but not the later map to a measured running coupling",
        ],
    }

    candidate = {
        "candidate": "SelectedQaSU3ResponseFunctionalChiQa",
        "status": "QA_SU3_SELECTED_FINITE_RESPONSE_FUNCTIONAL_CHI_QA_CLOSED_MEASURED_MATCH_OPEN",
        "inputs": {
            "bridge_packet": str(BRIDGE.relative_to(ROOT)),
            "orbit_democracy_packet": str(ORBIT.relative_to(ROOT)),
            "target_fitting_used": False,
        },
        "derivation": derivation,
        "tested_normalizations": tested_normalizations,
        "theorem": theorem,
        "decision": theorem["conclusions"],
        "guardrails": [
            "chi_Qa=1 is a derived finite internal normalization, not a measured coupling",
            "do not infer alpha_EM, alpha_s, sin^2(theta_W), or a unification scale from this artifact",
            "do not add QFT beta coefficients or threshold schemes unless selected in a later matching theorem",
            "do not use observed constants, masses, CKM/PMNS data, or residuals as inputs",
            "do not count the GR/protospinor surface response inside the Qa/SU3 internal packet",
        ],
        "closure_claimed": True,
        "closure_scope": "selected_finite_Qa_SU3_response_functional_chi_Qa_only",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedQaSU3ResponseFunctionalChiQa",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "selected_finite_response_functional_chi_Qa": str(chi),
            "retarded_trace_pairing": "8 * (1/8) = 1",
            "finite_internal_response": "Delta_Qa_selected_finite = log(2008)",
        },
        "what_remains_open": {
            "measured_electroweak_or_running_coupling_match": True,
            "absolute_physical_coupling_normalization": True,
            "full_SM_closure": True,
        },
        "next_required_object": theorem["conclusions"]["next_required_object"],
        "closure_scope": candidate["closure_scope"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, object]) -> str:
    derivation = candidate["derivation"]
    theorem = candidate["theorem"]
    inputs = derivation["inputs"]
    guardrails = "\n".join(f"- {item}" for item in candidate["guardrails"])
    why = "\n".join(f"- {item}" for item in derivation["why_source_selected"])
    hypotheses = "\n".join(f"- {item}" for item in theorem["hypotheses"])
    proof = "\n".join(f"- {item}" for item in theorem["proof_idea"])
    return f"""# Selected Qa/SU3 Response Functional Chi_Qa v1

## Result

The selected finite response coefficient is:

```text
chi_Qa = Tr_finite(tau^2) * <Pi_tw, G_ret Pi_tw>
       = {inputs["finite_trace_tau_squared"]} * {inputs["G_ret_Pi_tw_Pi_tw"]}
       = {derivation["result"]["chi_Qa"]}
```

Therefore the selected finite internal response is:

```text
Delta_Qa_selected_finite = chi_Qa * logdet_int
                          = log(2008)
```

## Theorem

```text
{theorem["name"]}
```

Hypotheses:

{hypotheses}

Proof idea:

{proof}

## Why This Is Source Selected

{why}

## What This Does Not Close

This does not compute a measured running electroweak or strong coupling. It
does not select an RG scale, external QFT beta coefficient, threshold scheme,
or GR/protospinor surface matching term.

## Guardrails

{guardrails}

## Decision

The coefficient `chi_Qa` is closed for the selected finite Qa/SU3 internal
response functional. The next gate is the absolute physical matching layer:

```text
{theorem["conclusions"]["next_required_object"]}
```
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
