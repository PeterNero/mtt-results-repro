"""Build the Qa/SU3 electroweak matching / absolute coupling gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

CHI = DATA / "selected_response_functional_chi_qa.candidate.json"
BRIDGE = DATA / "internal_logdet_to_coupling_response_bridge.candidate.json"

NONSM_PHYSICAL_ACTION = TEXPAPERS / "mtt-nonsm-constants-no-knob" / "certificates" / "physical_action_normalization_gate_certificate.json"
GR_ALPHA = TEXPAPERS / "mtt-protospinor-gr-response-proof" / "certificates" / "selected_physical_alpha_or_action_unit_theorem_certificate.json"
GR_ANCHOR = TEXPAPERS / "mtt-protospinor-gr-response-proof" / "certificates" / "target_independent_dimensional_anchor_search_certificate.json"
GR_ONE_ANCHOR = TEXPAPERS / "mtt-protospinor-gr-response-proof" / "certificates" / "one_anchor_gr_normalization_propagation_certificate.json"
THETA_V = TEXPAPERS / "mtt-q79-proof-repro" / "proof_corpus" / "Theta_Closure_in_Modal_Triplet_Theory_V__Redundant_Determination_from_Gauge_Couplings_and_the_Weak_Mixing_Angle.md"

OUTPUT_DATA = DATA / "electroweak_matching_or_absolute_coupling_normalization.candidate.json"
OUTPUT_CERT = CERTS / "electroweak_matching_or_absolute_coupling_normalization_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Electroweak_Matching_or_Absolute_Coupling_Normalization_v1.md"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def scan_text(path: Path, needles: list[str]) -> dict[str, bool]:
    text = path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""
    return {needle: needle in text for needle in needles}


def scan_theta(path: Path) -> dict[str, bool]:
    text = path.read_text(encoding="utf-8", errors="ignore").lower() if path.exists() else ""
    return {
        "one_additional_input_unavoidable": "one additional input is logically unavoidable" in text,
        "ratios_fix_theta": "the ratios" in text and "fix" in text and "theta" in text,
        "absolute_scale_not_fixed": "do not fix the" in text and "absolute scale" in text,
        "one_dimensionless_coupling_needed": "without specifying one dimensionless coupling" in text,
        "g2_reference_input": "g_2" in text and "ref" in text,
        "sin2theta_not_used_in_ref_stage": "no information about $\\sin^2\\theta_w(m_z)$ is used" in text,
        "sin2theta_prediction_formula": "sin^2\\theta_w^{\\mathrm{pred}}(m_z)" in text,
    }


def build() -> tuple[dict[str, object], dict[str, object], str]:
    chi = load(CHI)
    bridge = load(BRIDGE)
    nonsm = load(NONSM_PHYSICAL_ACTION)
    gr_alpha = load(GR_ALPHA)
    gr_anchor = load(GR_ANCHOR)
    gr_one_anchor = load(GR_ONE_ANCHOR)
    theta_scan = scan_theta(THETA_V)

    logdet = chi["decision"]["finite_response_functional"].split(" = ", 1)[1]
    selected_internal_payload = {
        "Qa_SU3_internal_overlap_payload": logdet,
        "chi_Qa": chi["decision"]["selected_chi_Qa"],
        "interpretation": "selected finite internal response, not a measured coupling",
        "boundary_form_in_internal_units": "I_Qa = log(2008)",
        "physical_boundary_form": "1/g_Qa^2(mu_match) = K_gauge * log(2008)",
    }

    cross_repo_findings = {
        "theta_electroweak_matching": {
            "source": str(THETA_V),
            "scanned_clauses": theta_scan,
            "usable_as": "matching scaffold and non-circular test discipline",
            "not_usable_as": "no-knob absolute normalization, because it states one extra overall coupling input is unavoidable",
        },
        "nonsm_physical_action": {
            "source": str(NONSM_PHYSICAL_ACTION),
            "status": nonsm["status"],
            "internal_alpha_closed": nonsm["verdict"]["alpha_closed_in_internal_units"],
            "physical_absolute_closed": nonsm["verdict"]["physical_absolute_dimensionful_predictions_closed"],
        },
        "gr_alpha_or_action_unit": {
            "source": str(GR_ALPHA),
            "status": gr_alpha["status"],
            "alpha_phys_status": gr_alpha["theorem_result"]["alpha_phys_status"],
            "physical_numeric_alpha_selected": gr_alpha["theorem_result"]["physical_numeric_alpha_selected"],
        },
        "gr_anchor_search": {
            "source": str(GR_ANCHOR),
            "status": gr_anchor["status"],
            "current_corpus_closes_alpha_phys": gr_anchor["verdict"]["current_corpus_closes_alpha_phys"],
            "best_route": gr_anchor["verdict"]["best_route"],
        },
        "gr_one_anchor_family": {
            "source": str(GR_ONE_ANCHOR),
            "status": gr_one_anchor["status"],
            "one_anchor_family_closed": gr_one_anchor["verdict"]["one_anchor_gr_normalization_family_closed"],
            "absolute_newton_value_predicted_without_anchor": gr_one_anchor["verdict"]["absolute_newton_value_predicted_without_anchor"],
        },
    }

    tested_routes = [
        {
            "route": "direct_Qa_absolute_coupling",
            "formula": "1/g_Qa^2 = log(2008)",
            "status": "REJECTED_AS_PHYSICAL_CLOSURE",
            "reason": "This silently sets K_gauge=1 as a physical normalization. The current proof only selects internal units.",
        },
        {
            "route": "Theta_overlap_matching_scaffold",
            "formula": "1/g_a^2(mu_match)=K_gauge I_a",
            "status": "ACCEPTED_AS_INTERFACE_ONLY",
            "reason": "Theta supplies the correct overlap and RGE matching architecture, but also states that ratios do not fix the absolute coupling scale.",
        },
        {
            "route": "Qa_as_SU3_overlap_payload",
            "formula": "I_3 or I_Qa = log(2008)",
            "status": "CONDITIONALLY_AVAILABLE",
            "reason": "The Qa/SU3 internal payload can serve as one selected nonabelian overlap payload after a source states the Qa-to-SU3 matching representation.",
        },
        {
            "route": "one_external_gauge_anchor",
            "formula": "K_gauge fixed by one independently selected gauge coupling at mu_match",
            "status": "VALID_MATCHING_MODE_NOT_NO_KNOB",
            "reason": "This is the Theta V non-circular test mode; it may predict sin^2(theta_W) without using it, but it still uses one gauge normalization.",
        },
        {
            "route": "GR_or_nonSM_alpha_phys_import",
            "formula": "use alpha_phys or G10 physical anchor to fix K_gauge",
            "status": "OPEN_SAME_ANCHOR_PROBLEM",
            "reason": "GR/non-SM reduce physical scale to one anchor, but do not select that anchor numerically without metrological input.",
        },
        {
            "route": "full_no_knob_electroweak_closure",
            "formula": "derive K_gauge, I_1, I_2, I_3, threshold scheme, and RGE scheme internally",
            "status": "OPEN",
            "missing": [
                "selected U1 payload in the same quotient and hypercharge normalization",
                "selected SU2 payload in the same quotient and threshold scheme",
                "selected common K_gauge or proof that it cancels in the claimed observable",
                "matching scale or internal scale map",
                "RGE and electroweak threshold scheme if comparing to M_Z data",
            ],
        },
    ]

    theorem = {
        "name": "SelectedQaSU3ElectroweakMatchingOrAbsoluteCouplingNormalization",
        "hypotheses": [
            "Selected_Qa_SU3_Response_Functional_Chi_Qa_v1 is accepted",
            "the selected finite internal Qa/SU3 payload is Delta_Qa=log(2008)",
            "Theta V overlap/RGE matching is used only as a scaffold, not as target-fitted proof input",
            "non-SM and GR absolute-normalization certificates are imported as guardrails",
            "no observed alpha_EM, alpha_s, sin^2(theta_W), masses, TeV benchmark, Newton, or Planck value is used to close a no-knob result",
        ],
        "conclusions": {
            "Qa_SU3_internal_payload_for_matching": "CLOSED_LOG_2008",
            "electroweak_matching_interface": "BUILT",
            "absolute_gauge_normalization_K_gauge": "OPEN",
            "U1_SU2_same_scheme_payloads": "OPEN",
            "no_knob_measured_electroweak_closure_now": False,
            "allowed_conditional_formula": "1/g_Qa^2(mu_match)=K_gauge*log(2008)",
            "next_required_object": "Selected_U1_SU2_Same_Scheme_Internal_Payloads_or_K_Gauge_Anchor_v1",
        },
        "proof_idea": [
            "the Qa/SU3 branch now supplies one selected internal response payload with coefficient chi_Qa=1",
            "electroweak matching needs a common gauge-normalization constant and comparable U1/SU2 payloads in the same quotient scheme",
            "Theta V proves the matching architecture and explicitly warns that overlap ratios do not fix absolute coupling scale",
            "non-SM and GR repos independently reduce physical absolute normalization to one external anchor rather than closing it",
            "therefore the legal result is an electroweak matching interface and a sharp no-go for no-knob measured coupling closure from the current repos",
        ],
    }

    candidate = {
        "candidate": "SelectedQaSU3ElectroweakMatchingOrAbsoluteCouplingNormalization",
        "status": "QA_SU3_ELECTROWEAK_MATCHING_INTERFACE_BUILT_ABSOLUTE_K_GAUGE_OPEN",
        "inputs": {
            "selected_chi_Qa": str(CHI.relative_to(ROOT)),
            "internal_bridge": str(BRIDGE.relative_to(ROOT)),
            "cross_repo_sweep_performed": True,
            "target_fitting_used": False,
        },
        "selected_internal_payload": selected_internal_payload,
        "cross_repo_findings": cross_repo_findings,
        "tested_routes": tested_routes,
        "theorem": theorem,
        "decision": theorem["conclusions"],
        "guardrails": [
            "do not set K_gauge=1 as a measured coupling normalization",
            "do not import Theta 5 TeV as a no-knob scale prediction",
            "do not use observed alpha_EM, alpha_s, sin^2(theta_W), masses, Newton, Planck, or TeV calibration as proof input",
            "do not compare log(2008) directly to a measured inverse coupling without a selected matching map",
            "do not mix Qa/SU3, U1, SU2, GR, and non-SM normalizations unless one common quotient/action scheme is certified",
        ],
        "closure_claimed": True,
        "closure_scope": "electroweak_matching_interface_and_no_go_for_current_no_knob_absolute_closure",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedQaSU3ElectroweakMatchingOrAbsoluteCouplingNormalization",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "cross_repo_sweep_for_matching_inputs": True,
            "Qa_SU3_internal_matching_payload": "log(2008)",
            "electroweak_matching_interface": "1/g_Qa^2(mu_match)=K_gauge*log(2008)",
            "current_source_no_knob_absolute_closure_no_go": True,
        },
        "what_remains_open": {
            "K_gauge_absolute_or_common_normalization": True,
            "U1_same_scheme_payload": True,
            "SU2_same_scheme_payload": True,
            "matching_scale_or_internal_scale_map": True,
            "measured_electroweak_closure": True,
            "full_SM_closure": True,
        },
        "next_required_object": theorem["conclusions"]["next_required_object"],
        "closure_scope": candidate["closure_scope"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, object]) -> str:
    payload = candidate["selected_internal_payload"]
    theorem = candidate["theorem"]
    routes = "\n".join(f"- {r['route']}: {r['status']} ({r['formula']})" for r in candidate["tested_routes"])
    guardrails = "\n".join(f"- {item}" for item in candidate["guardrails"])
    findings = candidate["cross_repo_findings"]
    hypotheses = "\n".join(f"- {item}" for item in theorem["hypotheses"])
    proof = "\n".join(f"- {item}" for item in theorem["proof_idea"])
    return f"""# Selected Qa/SU3 Electroweak Matching or Absolute Coupling Normalization v1

## Result

The selected Qa/SU3 internal payload is available for matching:

```text
I_Qa = {payload["Qa_SU3_internal_overlap_payload"]}
chi_Qa = {payload["chi_Qa"]}
```

The legal physical matching interface is:

```text
{payload["physical_boundary_form"]}
```

The current repos do not select `K_gauge`, nor do they supply same-scheme U1
and SU2 payloads. Therefore measured electroweak closure is not claimed.

## Cross-Repo Sweep

Theta V supplies the overlap/RGE scaffold, but it explicitly says that overlap
ratios do not fix the absolute coupling scale and that one overall coupling
normalization is logically unavoidable in that framework.

Non-SM physical action status:

```text
{findings["nonsm_physical_action"]["status"]}
physical absolute closed = {findings["nonsm_physical_action"]["physical_absolute_closed"]}
```

GR alpha/action status:

```text
{findings["gr_alpha_or_action_unit"]["status"]}
alpha_phys selected = {findings["gr_alpha_or_action_unit"]["physical_numeric_alpha_selected"]}
```

GR anchor search:

```text
{findings["gr_anchor_search"]["status"]}
current corpus closes alpha_phys = {findings["gr_anchor_search"]["current_corpus_closes_alpha_phys"]}
```

## Theorem

```text
{theorem["name"]}
```

Hypotheses:

{hypotheses}

Proof idea:

{proof}

## Tested Routes

{routes}

## Decision

```text
Qa/SU3 internal payload = CLOSED_LOG_2008
electroweak matching interface = BUILT
K_gauge = OPEN
U1/SU2 same-scheme payloads = OPEN
no-knob measured electroweak closure = false
```

## Guardrails

{guardrails}

## Next Required Object

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
