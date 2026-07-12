"""Build the U1/SU2 internal payload template or K_gauge source fill attempt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

PREVIOUS = DATA / "u1_su2_same_scheme_payloads_or_k_gauge_anchor.candidate.json"
SM_REPO = TEXPAPERS / "mtt-sm-parity-closure"
SM_DATA = SM_REPO / "candidate_data"

SM_SECTOR = SM_DATA / "sm_sector_embedding_interface.candidate.json"
SM_PACKET = SM_DATA / "actual_selected_sm_packet_anomaly_audit.candidate.json"
INVERSE_SPEC = SM_DATA / "inverse_superset_search_spec.candidate.json"
INVERSE_RECON = SM_DATA / "inverse_superset_reconstruction.candidate.json"

OUTPUT_DATA = DATA / "u1_su2_internal_overlap_payload_template_or_k_gauge_source_fill.candidate.json"
OUTPUT_CERT = CERTS / "u1_su2_internal_overlap_payload_template_or_k_gauge_source_fill_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1_SU2_Internal_Overlap_Payload_Template_or_K_Gauge_Source_Fill_v1.md"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def find_domain(spec: dict[str, object], domain_id: str) -> dict[str, object]:
    return next(item for item in spec["search_domains"] if item["id"] == domain_id)


def build() -> tuple[dict[str, object], dict[str, object], str]:
    previous = load(PREVIOUS)
    sm_sector = load(SM_SECTOR)
    sm_packet = load(SM_PACKET)
    inverse_spec = load(INVERSE_SPEC)
    inverse_recon = load(INVERSE_RECON)
    threshold_domain = find_domain(inverse_spec, "theta_gauge_threshold_packet")
    topology_domain = find_domain(inverse_spec, "finite_topology_packet")

    payload_template = {
        "common_scheme": {
            "quotient_action_measure": "must be the same finite/internal action measure used by I_Qa=log(2008)",
            "trace_policy": "must declare representation trace weights before computing I_1 or I_2",
            "response_policy": "must compute chi_1 and chi_2 from selected finite response functionals, not from measured couplings",
            "normalization_policy": "must select U1 hypercharge normalization from source data; 3/5 may be a candidate but is not assumed",
        },
        "I_1_template": "I_1 = chi_1 * Delta_U1_selected_finite",
        "I_2_template": "I_2 = chi_2 * Delta_SU2_selected_finite",
        "matching_template": "1/g_a^2(mu_match) = K_gauge * I_a for a in {1,2,Qa}",
        "allowed_ratio_test_if_K_cancels": "g_i^{-2}/g_j^{-2} = I_i/I_j only after same K_gauge and same mu_match are certified",
    }

    candidate_routes = [
        {
            "id": "topology_hypercharge_line_bundle_route",
            "kind": "U1_payload_candidate",
            "source_support": [
                "SM packet audit says topology-only constraints state exact SM hypercharges and anomaly cancellation from triplet line-bundle difference charges.",
                "Inverse spec exposes line_bundle_charge_packet as a finite-topology variable.",
            ],
            "candidate_payload_field": "I_1",
            "current_status": "PARTIAL_STRUCTURAL_NOT_PROMOTED",
            "fills": {
                "carrier_hint": "U1/hypercharge line-bundle charge packet",
                "anomaly_context": True,
            },
            "blocks": [
                "actual selected representation table with hypercharges and source maps is absent",
                "source-selected hypercharge normalization is absent",
                "same-scheme finite response functional chi_1 is absent",
                "Delta_U1_selected_finite spectrum/determinant/torsion payload is absent",
            ],
        },
        {
            "id": "weak_su2_carrier_route",
            "kind": "SU2_payload_candidate",
            "source_support": [
                "SM sector interface declares SU3 x SU2 x U1 as source data required before measured couplings enter.",
                "SM packet audit requires color/weak reps and SU2 global anomaly checks on the selected representation packet.",
            ],
            "candidate_payload_field": "I_2",
            "current_status": "PARTIAL_STRUCTURAL_NOT_PROMOTED",
            "fills": {
                "carrier_hint": "SU2 weak carrier",
                "global_anomaly_context": True,
            },
            "blocks": [
                "actual selected weak representation table is absent",
                "same-source SU2 operator or finite response packet is absent",
                "trace/action normalization relative to Qa/SU3 is absent",
                "Delta_SU2_selected_finite spectrum/determinant/torsion payload is absent",
            ],
        },
        {
            "id": "inverse_normalization_index_route",
            "kind": "K_gauge_or_embedding_normalization_candidate",
            "source_support": [
                "Inverse spec exposes normalization_index over U1/SU2/SU3 embedding-normalization candidates.",
                "Inverse reconstruction permits gauge coupling targets only as discovery data and bars promotion without forward replay.",
            ],
            "candidate_payload_field": "K_gauge or relative embedding normalization",
            "current_status": "DISCOVERY_ONLY_NOT_PROMOTED",
            "fills": {
                "candidate_variable": "normalization_index",
                "discrete_or_rational_domain": True,
            },
            "blocks": [
                "no numeric inverse run has selected a compact normalization candidate",
                "any inverse hit would still require corpus alignment and forward replay",
                "K_gauge absolute normalization is not fixed by embedding index alone",
                "matching scale and RGE/threshold scheme are absent",
            ],
        },
    ]

    promotion_tests = [
        "The route must fill I_1 and I_2 from selected source data, or fill K_gauge from a target-independent action normalization.",
        "The route must use the same quotient/action measure as I_Qa=log(2008).",
        "The route must provide hypercharge normalization before any U1 comparison.",
        "The route must declare mu_match and RGE/threshold scheme before comparison to M_Z or other measured data.",
        "The route must replay forward with alpha_em, sin2_theta_w, alpha_s, masses, CKM, and PMNS removed from selectors.",
    ]

    theorem = {
        "name": "SelectedU1SU2InternalPayloadTemplateOrKGaugeSourceFill",
        "hypotheses": [
            "Selected_U1_SU2_Same_Scheme_Internal_Payloads_or_K_Gauge_Anchor_v1 is accepted",
            "SM parity structural packet and inverse-search spec are accepted as discovery scaffolds",
            "I_Qa=log(2008) is the only closed same-scheme internal gauge payload",
            "observed gauge couplings are not used as source selectors",
        ],
        "conclusions": {
            "payload_template_built": True,
            "topology_hypercharge_route": "LIVE_PARTIAL_STRUCTURAL",
            "weak_su2_route": "LIVE_PARTIAL_STRUCTURAL",
            "inverse_normalization_index_route": "LIVE_DISCOVERY_ONLY",
            "I_1_filled": False,
            "I_2_filled": False,
            "K_gauge_filled": False,
            "measured_electroweak_closure": False,
            "next_required_object": "Selected_U1_SU2_Source_Response_or_Normalization_Index_Run_v1",
        },
    }

    candidate = {
        "candidate": "SelectedU1SU2InternalOverlapPayloadTemplateOrKGaugeSourceFill",
        "status": "U1_SU2_K_GAUGE_FILL_ATTEMPT_TEMPLATE_BUILT_CURRENT_SOURCE_PARTIAL_ONLY",
        "inputs": {
            "previous_gate": str(PREVIOUS.relative_to(ROOT)),
            "sm_sector_status": sm_sector["status"],
            "sm_packet_status": sm_packet["status"],
            "inverse_spec_status": inverse_spec["status"],
            "inverse_reconstruction_status": inverse_recon["status"],
            "target_fitting_used": False,
        },
        "source_extracted_handles": {
            "finite_topology_variables": topology_domain["variables"],
            "theta_gauge_threshold_variables": threshold_domain["variables"],
            "gauge_couplings_allowed_use": next(
                item for item in inverse_recon["measured_targets"] if item["id"] == "gauge_couplings"
            )["allowed_use"],
            "sm_gauge_coupling_slot_status": sm_sector["sm_required_components"]["gauge_couplings"]["status"],
            "actual_selected_representation_packet_supplied": sm_packet["gate_results"]["actual_selected_representation_packet_supplied"],
            "qa_su3_operator_packet_supplied": sm_packet["gate_results"]["qa_su3_operator_packet_supplied"],
        },
        "payload_template": payload_template,
        "candidate_routes": candidate_routes,
        "promotion_tests": promotion_tests,
        "theorem": theorem,
        "decision": theorem["conclusions"],
        "closure_claimed": True,
        "closure_scope": "payload_template_and_current_source_fill_attempt_no_go",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedU1SU2InternalOverlapPayloadTemplateOrKGaugeSourceFill",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "I1_I2_Kgauge_fill_template": True,
            "three_candidate_routes_ranked": True,
            "inverse_normalization_index_handle_identified": True,
            "current_source_partial_fill_no_go": True,
        },
        "what_remains_open": {
            "I1_U1_payload": True,
            "I2_SU2_payload": True,
            "K_gauge_anchor": True,
            "selected_hypercharge_normalization": True,
            "same_scheme_SU2_operator_response": True,
            "normalization_index_numeric_run": True,
            "forward_replay_without_gauge_targets": True,
            "measured_electroweak_closure": True,
        },
        "next_required_object": theorem["conclusions"]["next_required_object"],
        "closure_scope": candidate["closure_scope"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, object]) -> str:
    template = candidate["payload_template"]
    routes = "\n".join(
        f"### {route['id']}\n\n"
        f"- Kind: `{route['kind']}`\n"
        f"- Status: `{route['current_status']}`\n"
        f"- Candidate field: `{route['candidate_payload_field']}`\n"
        f"- Source support: {'; '.join(route['source_support'])}\n"
        f"- Blocks: {'; '.join(route['blocks'])}\n"
        for route in candidate["candidate_routes"]
    )
    tests = "\n".join(f"- {item}" for item in candidate["promotion_tests"])
    decision = candidate["decision"]
    handles = candidate["source_extracted_handles"]
    return f"""# Selected U1/SU2 Internal Overlap Payload Template or K_gauge Source Fill v1

## Result

This is the first constructive fill attempt after the same-scheme gate.  It
builds the U1/SU2/K-gauge payload template and tests the current SM parity
source against it.

The current source partially fills structural carrier information, but it does
not yet fill `I_1`, `I_2`, or `K_gauge`.

## Extracted Handles

```text
SM gauge-coupling slot status = {handles["sm_gauge_coupling_slot_status"]}
gauge couplings allowed use in inverse reconstruction = {handles["gauge_couplings_allowed_use"]}
actual selected representation packet supplied = {handles["actual_selected_representation_packet_supplied"]}
Qa/SU3 operator packet supplied = {handles["qa_su3_operator_packet_supplied"]}
```

The important live handle is the inverse-search variable:

```text
normalization_index: U1/SU2/SU3 embedding normalization candidates
```

It is discovery-only until compressed, source-aligned, and replayed forward.

## Payload Template

```text
{template["I_1_template"]}
{template["I_2_template"]}
{template["matching_template"]}
{template["allowed_ratio_test_if_K_cancels"]}
```

Common scheme requirements:

```text
quotient/action measure = {template["common_scheme"]["quotient_action_measure"]}
trace policy = {template["common_scheme"]["trace_policy"]}
response policy = {template["common_scheme"]["response_policy"]}
normalization policy = {template["common_scheme"]["normalization_policy"]}
```

## Candidate Routes

{routes}

## Promotion Tests

{tests}

## Decision

```text
payload_template_built = {decision["payload_template_built"]}
topology_hypercharge_route = {decision["topology_hypercharge_route"]}
weak_su2_route = {decision["weak_su2_route"]}
inverse_normalization_index_route = {decision["inverse_normalization_index_route"]}
I_1_filled = {str(decision["I_1_filled"]).lower()}
I_2_filled = {str(decision["I_2_filled"]).lower()}
K_gauge_filled = {str(decision["K_gauge_filled"]).lower()}
measured_electroweak_closure = {str(decision["measured_electroweak_closure"]).lower()}
```

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
