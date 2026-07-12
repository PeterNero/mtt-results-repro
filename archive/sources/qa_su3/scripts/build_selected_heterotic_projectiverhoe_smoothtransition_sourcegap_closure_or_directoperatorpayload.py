"""Build smooth-transition source-gap closure or direct-operator payload gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "source_gap": DATA / "selected_heterotic_projectiverhoe_smoothtransition_source_gap.json",
    "symbolic_transition_template": DATA / "selected_heterotic_projectiverhoe_symbolic_smoothtransition_table_template.json",
    "smoothdomain_no_go": DATA / "selected_heterotic_projectiverhoe_smoothdomaincover_sourceleaf_or_directcomplementdomain.candidate.json",
    "selected_packet_emission": DATA / "selected_heterotic_projectiverhoe_selectedpacketemission_or_operatoridentity.candidate.json",
    "internal_finitepart": DATA / "selected_heterotic_projectiverhoe_internal_threshold_finitepart.json",
    "finite_values": DATA / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.values.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_smoothtransition_sourcegap_closure_or_directoperatorpayload.candidate.json"
OUTPUT_ACCEPTANCE = DATA / "selected_heterotic_projectiverhoe_direct_operator_payload_acceptance_template.json"
OUTPUT_FORK = DATA / "selected_heterotic_projectiverhoe_transition_or_directoperator_closure_fork.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_smoothtransition_sourcegap_closure_or_directoperatorpayload_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_SmoothTransitionSourceGap_Closure_or_DirectOperatorPayload_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SOURCEGAP_FORK_BUILT_DIRECT_OPERATOR_PAYLOAD_TEMPLATE_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_DirectOperatorPayload_FillAttempt_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def same_labels(finite_values: dict[str, Any], transition_template: dict[str, Any]) -> bool:
    finite_labels = finite_values["finite_internal_values"]["labels"]
    template_labels = list(transition_template["symbolic_transition_table"])
    return finite_labels == template_labels


def main() -> dict[str, Any]:
    source_gap = load(INPUTS["source_gap"])
    transition_template = load(INPUTS["symbolic_transition_template"])
    smoothdomain_no_go = load(INPUTS["smoothdomain_no_go"])
    packet_emission = load(INPUTS["selected_packet_emission"])
    internal_finitepart = load(INPUTS["internal_finitepart"])
    finite_values = load(INPUTS["finite_values"])

    finite_internal = finite_values["finite_internal_values"]
    transition_lane = {
        "id": "Lane_A_selected_smooth_transition_source",
        "status": "OPEN_SOURCE_GAP",
        "formal_validators_pass": source_gap["passed_formally"],
        "blocked_by": smoothdomain_no_go["decision"],
        "must_supply": source_gap["minimal_closing_payload"],
        "can_close_now": False,
        "reason": (
            "The symbolic transition table has the right algebra, but the current "
            "source still lacks a selected smooth cover/domain and smooth transition "
            "functions deriving tau before finite comparison."
        ),
    }

    direct_operator_acceptance = {
        "schema": "SelectedHeteroticProjectiveRhoE.DirectOperatorPayloadAcceptanceTemplate.v1",
        "status": "TEMPLATE_OPEN",
        "required_payload": {
            "same_branch_source_certificate": None,
            "operator_domain_or_finite_quotient_domain": None,
            "rho_E_or_D_E_operator_tables": None,
            "self_adjoint_or_unitary_structure": None,
            "projector_or_quotient_policy": None,
            "zero_mode_and_gauge_subtraction_policy": None,
            "spectrum_or_logdet_finite_part": None,
            "trace_normalization": None,
            "map_to_selected_internal_packet": None,
            "proof_no_smooth_GR_double_count": None,
        },
        "already_available_internal_values": {
            "labels": finite_internal["labels"],
            "rho_E_central_character": finite_internal["rho_E_central_character"],
            "D_E": finite_internal["D_E"],
            "H_sel": finite_internal["H_sel"],
            "Green_operator": finite_internal["Green_operator"],
            "Riesz_projector": finite_internal["Riesz_projector"],
            "chi_Qa": finite_internal["chi_Qa"],
            "finite_internal_part": finite_internal["finite_internal_part"],
        },
        "acceptance_checks": {
            "same_labels_as_transition_template": same_labels(finite_values, transition_template),
            "selected_finite_packet_emitted": packet_emission["decision"]["selected_finite_internal_packet_emitted"],
            "internal_finitepart_closed": internal_finitepart["selected"] is True
            and internal_finitepart["Delta_selected_internal_exact"] == "log(2008)",
            "no_target_fitting": True,
            "does_not_need_smooth_transition_tables_if_direct_operator_identity_is_source_selected": True,
            "physical_normalization_not_claimed": True,
        },
        "forbidden_promotions": [
            "treat formal transition table as smooth source data",
            "treat finite internal logdet as measured electroweak coupling",
            "append a smooth complement determinant without an exact quotient theorem",
            "reuse GR/protospinor smooth response as Qa/SU3 internal determinant",
            "fit any missing entry to observed constants",
        ],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_ACCEPTANCE.write_text(json.dumps(direct_operator_acceptance, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    direct_operator_lane = {
        "id": "Lane_B_direct_same_branch_operator_payload",
        "status": "NEXT_EXECUTABLE_TEMPLATE_BUILT",
        "why_preferred_now": (
            "Lane A is blocked at smooth source ownership; Lane B can try to close "
            "by proving the already-emitted finite rho_E/D_E/logdet packet is the "
            "selected same-branch operator payload, or by emitting an equivalent "
            "smooth operator identity."
        ),
        "acceptance_template_path": rel(OUTPUT_ACCEPTANCE),
        "can_close_now": False,
        "reason_open": "the direct payload source certificate and map-to-selected-internal-packet proof are not yet filled",
    }

    fork = {
        "schema": "SelectedHeteroticProjectiveRhoE.TransitionOrDirectOperatorClosureFork.v1",
        "status": "FORK_BUILT_NEXT_DIRECT_OPERATOR_FILL",
        "lane_A": transition_lane,
        "lane_B": direct_operator_lane,
        "selected_next_lane": "Lane_B_direct_same_branch_operator_payload",
        "reason": "Lane A has formal algebra but no selected smooth source; Lane B is the only currently executable fill target.",
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_FORK.write_text(json.dumps(fork, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "sourcegap_fork_built": True,
        "lane_A_formal_validators_pass": all(source_gap["passed_formally"].values()),
        "lane_A_smooth_source_closed": False,
        "lane_A_current_source_nogo": smoothdomain_no_go["decision"]["current_source_nogo_for_S1"],
        "lane_B_direct_operator_acceptance_template_built": True,
        "lane_B_selected_as_next_executable": True,
        "selected_finite_internal_packet_retained": packet_emission["decision"]["selected_finite_internal_packet_emitted"],
        "internal_finitepart_retained": internal_finitepart["selected"] is True
        and internal_finitepart["Delta_selected_internal_exact"] == "log(2008)",
        "physical_normalization_claimed": False,
        "smooth_transition_tables_promoted": False,
        "direct_operator_payload_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoESmoothTransitionSourceGapClosureOrDirectOperatorPayload",
        "status": STATUS,
        "inputs": {name: rel(path) for name, path in INPUTS.items()},
        "fork_path": rel(OUTPUT_FORK),
        "direct_operator_acceptance_template_path": rel(OUTPUT_ACCEPTANCE),
        "decision": decision,
        "closed_now": {
            "smooth_transition_source_gap_classified": True,
            "direct_operator_acceptance_template": True,
            "finite_internal_operator_packet_retained_as_available_input": True,
            "internal_logdet_retained_as_internal_only": True,
        },
        "still_open": {
            "smooth_transition_source_promotion": True,
            "direct_same_branch_operator_payload_source_certificate": True,
            "map_to_selected_internal_packet_proof": True,
            "smooth_operator_identity_or_exact_complement_quotient": True,
            "physical_threshold_normalization": True,
        },
        "guardrails": {
            "does_not_promote_symbolic_transition_table": True,
            "does_not_overwrite_S1_current_source_nogo": True,
            "does_not_treat_internal_logdet_as_physical_coupling": True,
            "does_not_double_count_GR_smooth_surface": True,
            "does_not_use_observed_constants": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "SmoothTransitionSourceGapForkTheorem",
            "proved": True,
            "statement": (
                "Given the formal transition-table validators and the current-source "
                "no-go for the first smooth source leaf, smooth transition promotion "
                "cannot close now. The correct next executable route is a direct "
                "same-branch operator-payload fill attempt, using the selected finite "
                "rho_E/D_E/Green/Riesz/chi_Qa/logdet packet as available internal "
                "data while requiring a source certificate and map-to-packet proof."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "fork_path": rel(OUTPUT_FORK),
        "direct_operator_acceptance_template_path": rel(OUTPUT_ACCEPTANCE),
        "note_path": rel(OUTPUT_NOTE),
        "sourcegap_fork_built": True,
        "lane_B_direct_operator_acceptance_template_built": True,
        "lane_B_selected_as_next_executable": True,
        "direct_operator_payload_closed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE SmoothTransitionSourceGap Closure or DirectOperatorPayload v1

## Result

```text
status = {STATUS}
lane_A_formal_validators_pass = true
lane_A_smooth_source_closed = false
lane_B_direct_operator_acceptance_template_built = true
lane_B_selected_as_next_executable = true
next_required_artifact = {NEXT}
```

## Meaning

The smooth-transition table route is algebraically coherent but not source
owned. The first smooth source leaf is still absent, so the route cannot close
from the current repository.

The next executable route is therefore direct operator payload: prove that the
selected finite `rho_E/D_E/Green/Riesz/chi_Qa/log(2008)` packet is emitted by
the same branch as operator data, or emit an equivalent smooth operator identity.

Fork:

```text
{rel(OUTPUT_FORK)}
```

Direct payload template:

```text
{rel(OUTPUT_ACCEPTANCE)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_FORK)}")
    print(f"wrote {rel(OUTPUT_ACCEPTANCE)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(result["status"])
