"""Build the U1/SU2 same-scheme payload or K_gauge anchor gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

EW_GATE = DATA / "electroweak_matching_or_absolute_coupling_normalization.candidate.json"
SM_REPO = TEXPAPERS / "mtt-sm-parity-closure"
SM_CERTS = SM_REPO / "certificates"

SM_SECTOR = SM_CERTS / "sm_sector_embedding_interface_certificate.json"
SM_PACKET = SM_CERTS / "actual_selected_sm_packet_anomaly_audit_certificate.json"
SM_CORE = SM_CERTS / "core_axioms_measured_parameter_interface_certificate.json"
SM_BACKLOG = SM_CERTS / "no_knob_upgrade_backlog_certificate.json"

OUTPUT_DATA = DATA / "u1_su2_same_scheme_payloads_or_k_gauge_anchor.candidate.json"
OUTPUT_CERT = CERTS / "u1_su2_same_scheme_payloads_or_k_gauge_anchor_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1_SU2_Same_Scheme_Internal_Payloads_or_K_Gauge_Anchor_v1.md"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def scan_repo_for_payloads() -> dict[str, object]:
    files = list(SM_REPO.rglob("*")) if SM_REPO.exists() else []
    names = [path.name.lower() for path in files if path.is_file()]
    joined = "\n".join(str(path.relative_to(SM_REPO)).lower() for path in files if path.is_file())
    text_parts = []
    for path in files:
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".py", ".txt"}:
            text_parts.append(path.read_text(encoding="utf-8", errors="ignore").lower())
    content = "\n".join(text_parts)
    exact_old_payloads = {
        "u1_su2_operator_weight_candidate_gate": any("u1_su2_operator_weight_candidate_gate" in name for name in names),
        "u1_threshold": "u1" in joined and "threshold" in joined,
        "su2_threshold": "su2" in joined and "threshold" in joined,
        "same_scheme_payload": "same-scheme" in joined or "same_scheme" in joined,
        "k_gauge_anchor": "k_gauge" in joined,
        "stack_determinant": "stack_determinant" in joined or "stack determinant" in joined,
    }
    structural_terms = {
        "hypercharge": "hypercharge" in content or "hypercharge" in joined,
        "anomaly": "anomaly" in content or "anomaly" in joined,
        "line_bundle_charge_packet": "line_bundle_charge_packet" in content or "line_bundle_charge_packet" in joined,
        "gauge_coupling_measured_parameter_policy": "gauge coupling" in content or "gauge_coupling" in content,
    }
    return {
        "repo": str(SM_REPO),
        "file_count": len([path for path in files if path.is_file()]),
        "exact_payload_artifacts_found": exact_old_payloads,
        "structural_terms_found": structural_terms,
        "same_scheme_payloads_present": any(exact_old_payloads.values()),
    }


def build() -> tuple[dict[str, object], dict[str, object], str]:
    ew_gate = load(EW_GATE)
    sm_sector = load(SM_SECTOR)
    sm_packet = load(SM_PACKET)
    sm_core = load(SM_CORE)
    sm_backlog = load(SM_BACKLOG)
    repo_scan = scan_repo_for_payloads()

    acceptance_contract = [
        {
            "field": "I_Qa",
            "required_content": "selected Qa/SU3 internal payload in internal determinant units",
            "current_status": "CLOSED",
            "current_value": "log(2008)",
        },
        {
            "field": "I_1",
            "required_content": "selected U1/hypercharge payload in the same quotient/action scheme",
            "current_status": "OPEN",
            "current_value": None,
        },
        {
            "field": "I_2",
            "required_content": "selected SU2 payload in the same quotient/action scheme",
            "current_status": "OPEN",
            "current_value": None,
        },
        {
            "field": "hypercharge_normalization_policy",
            "required_content": "source-selected U1 normalization, e.g. a derived 3/5 policy if GUT-normalized hypercharge is used",
            "current_status": "OPEN",
            "current_value": None,
        },
        {
            "field": "K_gauge",
            "required_content": "target-independent common gauge normalization, or a proof it cancels in the claimed observable",
            "current_status": "OPEN",
            "current_value": None,
        },
        {
            "field": "mu_match",
            "required_content": "selected matching scale or internal scale map",
            "current_status": "OPEN",
            "current_value": None,
        },
        {
            "field": "RGE_threshold_scheme",
            "required_content": "same renormalization and threshold scheme if comparing to M_Z data",
            "current_status": "OPEN",
            "current_value": None,
        },
        {
            "field": "no_target_fitting",
            "required_content": "declaration and audit that observed couplings/masses/mixings were not used to select entries",
            "current_status": "CLOSED_FOR_THIS_GATE",
            "current_value": True,
        },
    ]

    current_sources = {
        "Qa_SU3_electroweak_gate": {
            "source": str(EW_GATE.relative_to(ROOT)),
            "status": ew_gate["status"],
            "available_payload": ew_gate["selected_internal_payload"]["Qa_SU3_internal_overlap_payload"],
            "next_required_object": ew_gate["decision"]["next_required_object"],
        },
        "sm_sector_embedding_interface": {
            "source": str(SM_SECTOR),
            "status": sm_sector["status"],
            "structural_support": sm_sector["what_closes"],
            "open_items": sm_sector["what_remains_open"],
        },
        "actual_selected_sm_packet_audit": {
            "source": str(SM_PACKET),
            "status": sm_packet["status"],
            "structural_support": sm_packet["what_closes"],
            "open_items": sm_packet["what_remains_open"],
        },
        "core_axioms_measured_parameter_interface": {
            "source": str(SM_CORE),
            "status": sm_core["status"],
            "policy_support": sm_core["what_closes"],
            "open_items": sm_core["what_remains_open"],
        },
        "no_knob_upgrade_backlog": {
            "source": str(SM_BACKLOG),
            "status": sm_backlog["status"],
            "open_items": sm_backlog["what_remains_open"],
        },
        "repo_scan": repo_scan,
    }

    no_go_reasons = [
        "The current SM parity repo has hypercharge/anomaly/embedding scaffolds, not same-scheme U1 and SU2 determinant payloads.",
        "The measured-parameter interface explicitly keeps gauge couplings as parameter slots unless upgraded by source-selected no-knob data.",
        "The Qa/SU3 branch supplies I_Qa=log(2008), but one internal payload cannot determine U1, SU2, K_gauge, mu_match, and thresholds.",
        "A direct K_gauge=1 convention would be an unselected physical normalization, not a theorem.",
        "GUT-like hypercharge normalization may be a good candidate, but it must be selected by the source packet, not assumed for numerical success.",
    ]

    next_fill_templates = {
        "Selected_U1_Internal_Overlap_Payload_v1": {
            "must_supply": [
                "selected U1 carrier or hypercharge line-bundle/section-ring packet",
                "normalization policy for Y, including whether 3/5 is source-selected",
                "same finite quotient/action measure used by Qa/SU3",
                "finite response functional chi_1 and internal payload I_1",
            ]
        },
        "Selected_SU2_Internal_Overlap_Payload_v1": {
            "must_supply": [
                "selected SU2 weak carrier packet",
                "same quotient/action measure used by Qa/SU3",
                "finite response functional chi_2 and internal payload I_2",
                "operator/trace policy compatible with the Qa/SU3 trace policy",
            ]
        },
        "Selected_K_Gauge_Anchor_Packet_v1": {
            "must_supply": [
                "target-independent common gauge action normalization",
                "proof that it is shared by U1, SU2, and Qa/SU3",
                "matching-scale map or proof of cancellation for the claimed observable",
                "audit that no observed electroweak data were used to choose it",
            ]
        },
    }

    decision = {
        "Qa_SU3_payload": "CLOSED_LOG_2008",
        "SM_embedding_and_hypercharge_support": "PARTIAL_STRUCTURAL",
        "U1_same_scheme_payload": "OPEN",
        "SU2_same_scheme_payload": "OPEN",
        "K_gauge_anchor": "OPEN",
        "same_scheme_payloads_or_anchor": "OPEN",
        "measured_electroweak_closure": False,
        "full_SM_closure": False,
        "next_required_object": "Selected_U1_SU2_Internal_Overlap_Payload_Template_or_K_Gauge_Source_Fill_v1",
    }

    candidate = {
        "candidate": "SelectedU1SU2SameSchemePayloadsOrKGaugeAnchor",
        "status": "U1_SU2_SAME_SCHEME_ACCEPTANCE_CONTRACT_BUILT_PAYLOADS_AND_K_GAUGE_OPEN",
        "inputs": {
            "electroweak_gate": str(EW_GATE.relative_to(ROOT)),
            "sm_parity_repo": str(SM_REPO),
            "target_fitting_used": False,
        },
        "acceptance_contract": acceptance_contract,
        "current_sources": current_sources,
        "no_go_reasons": no_go_reasons,
        "next_fill_templates": next_fill_templates,
        "decision": decision,
        "closure_claimed": True,
        "closure_scope": "same_scheme_acceptance_contract_and_current_source_no_go",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedU1SU2SameSchemePayloadsOrKGaugeAnchor",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "same_scheme_acceptance_contract": True,
            "cross_repo_sm_parity_sweep": True,
            "Qa_SU3_payload_carried_forward": "log(2008)",
            "current_source_no_hidden_U1_SU2_or_K_gauge_closure": True,
        },
        "what_remains_open": {
            "U1_same_scheme_payload": True,
            "SU2_same_scheme_payload": True,
            "K_gauge_anchor": True,
            "hypercharge_normalization_policy": True,
            "matching_scale_or_internal_scale_map": True,
            "RGE_threshold_scheme": True,
            "measured_electroweak_closure": True,
            "full_SM_closure": True,
        },
        "next_required_object": decision["next_required_object"],
        "closure_scope": candidate["closure_scope"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, object]) -> str:
    decision = candidate["decision"]
    contract = "\n".join(
        f"- `{item['field']}`: {item['current_status']} - {item['required_content']}"
        for item in candidate["acceptance_contract"]
    )
    no_go = "\n".join(f"- {item}" for item in candidate["no_go_reasons"])
    templates = "\n".join(
        f"- `{name}`: " + "; ".join(data["must_supply"])
        for name, data in candidate["next_fill_templates"].items()
    )
    sources = candidate["current_sources"]
    scan = sources["repo_scan"]
    return f"""# Selected U1/SU2 Same-Scheme Internal Payloads or K_gauge Anchor v1

## Result

This gate carries forward the selected Qa/SU3 internal payload:

```text
I_Qa = log(2008)
```

It does not close measured electroweak coupling prediction. The current
SM-parity source supplies structural SM scaffolding, but it does not currently
emit selected U1 and SU2 internal payloads in the same scheme, nor a
target-independent common `K_gauge` anchor.

## Acceptance Contract

{contract}

## Current Source Sweep

SM sector embedding:

```text
{sources["sm_sector_embedding_interface"]["status"]}
```

Actual selected SM packet/anomaly audit:

```text
{sources["actual_selected_sm_packet_audit"]["status"]}
```

Measured-parameter interface:

```text
{sources["core_axioms_measured_parameter_interface"]["status"]}
```

Repository payload scan:

```text
same_scheme_payloads_present = {scan["same_scheme_payloads_present"]}
exact_payload_artifacts_found = {scan["exact_payload_artifacts_found"]}
structural_terms_found = {scan["structural_terms_found"]}
```

## No-Go For Current Source

{no_go}

## Decision

```text
Qa_SU3_payload = {decision["Qa_SU3_payload"]}
SM_embedding_and_hypercharge_support = {decision["SM_embedding_and_hypercharge_support"]}
U1_same_scheme_payload = {decision["U1_same_scheme_payload"]}
SU2_same_scheme_payload = {decision["SU2_same_scheme_payload"]}
K_gauge_anchor = {decision["K_gauge_anchor"]}
measured_electroweak_closure = {str(decision["measured_electroweak_closure"]).lower()}
full_SM_closure = {str(decision["full_SM_closure"]).lower()}
```

## Next Fill Templates

{templates}

## Next Required Object

```text
{decision["next_required_object"]}
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
