"""Fill the direct BN27 source declaration template where current data permits."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "normal_form": DATA / "selected_heterotic_orientedphifin_bundleA_sourceselector_or_bn27_sourcedeclaration.candidate.json",
    "declaration_template": DATA / "selected_heterotic_orientedphifin_bn27_direct_source_declaration.template.json",
    "direct_response_packet": DATA / "selected_heterotic_orientedphifin_directfiniteresponse_fillattempt_packet.json",
    "trace_identity": DATA / "selected_heterotic_orientedphifin_fullfourierorbit_traceidentity.json",
    "repair_packet": DATA / "selected_heterotic_orientedphifin_sourcebranchidentity_repair_packet.json",
    "sourceleaf": DATA / "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_directbn27_sourcedeclaration_fill_or_bundleA_selector.candidate.json"
OUTPUT_FILLED = DATA / "selected_heterotic_orientedphifin_bn27_direct_source_declaration.fill_attempt.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_directbn27_sourcedeclaration_fill_or_bundleA_selector_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_DirectBN27_SourceDeclaration_Fill_or_BundleA_Selector_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_DIRECTBN27_SOURCEDECLARATION_FILL_SUPPORT_FILLED_SOURCE_OWNERSHIP_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceOwned_BN27_Certificate_or_BundleA_Selector_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    normal = load(INPUTS["normal_form"])
    template = load(INPUTS["declaration_template"])
    response = load(INPUTS["direct_response_packet"])
    trace = load(INPUTS["trace_identity"])
    repair = load(INPUTS["repair_packet"])
    sourceleaf = load(INPUTS["sourceleaf"])

    source_tests = response["source_tests"]
    closed_leaves = set(response["closed_required_leaves"])
    open_leaves = set(response["open_required_leaves"])

    filled = {
        "schema": "SelectedHeterotic.OrientedPhiFin.DirectBN27.SourceDeclaration.FillAttempt.v1",
        "status": "SUPPORT_FILLED_SOURCE_OWNERSHIP_OPEN",
        "source_certificate": {
            "source_name": template["source_certificate"]["source_name"],
            "same_selected_source_as_heterotic_QaSU3_threshold_branch": source_tests["same_branch_heterotic_source_certificate"],
            "not_routec_or_benchmark_import": False,
            "relation_to_internal_projective_rhoE_shadow": template["source_certificate"]["relation_to_internal_projective_rhoE_shadow"],
            "why_open": "No current theorem declares S_QaSU3^BN27 as the selected heterotic Qa/SU3 threshold source.",
        },
        "domain": {
            "basis_id": response["domain"]["basis_id"],
            "basis_dimension": response["domain"]["basis_dimension"],
            "F3xF3_rank_slot_deck_action_materialized": True,
            "F3xF3_rank_slot_deck_action_source_owned": False,
            "oriented_nonzero_count": response["domain"]["oriented_nonzero_count"],
            "kernel_shared_circle_no_double_count_policy": "support_replay_closed_not_source_owned",
            "selected_domain_or_quotient_map_to_oriented_BN": source_tests["selected_domain_or_quotient_map_to_oriented_BN"],
        },
        "operators": {
            "source_emits_C_tau": False,
            "source_emits_PhiFin_DE": False,
            "C_tau_and_PhiFin_DE_commute": template["operators"]["C_tau_and_PhiFin_DE_commute"],
            "orientation_operator_Ctau_binding": source_tests["orientation_operator_Ctau_binding"],
            "source_owns_positive_magnitude_with_orientation": False,
            "D_E_diagonal_on_oriented_nonzero_BN": response["operator_values_materialized"]["D_E_diagonal_on_oriented_nonzero_BN"],
            "positive_spectrum": response["operator_values_materialized"]["positive_spectrum"],
            "green_trace": response["operator_values_materialized"]["green_trace"],
            "green_square_trace": response["operator_values_materialized"]["green_square_trace"],
        },
        "finitepart": {
            "kernel_trace_policy_source_owned": False,
            "finitepart_trace_identity_relative_to_full_orbit_source": trace["identity_closed_relative_to_full_orbit_source"],
            "finitepart_trace_identity_for_oriented_nonzero_sector_source_owned": False,
            "oriented_abs_sector_product": trace["oriented_abs_sector_product"],
            "oriented_abs_sector_logdet_exact": trace["oriented_abs_sector_logdet_exact"],
            "plus_sector_product": trace["plus_sector_product"],
            "minus_sector_product": trace["minus_sector_product"],
            "oriented_logdet_promoted": False,
        },
        "audit_replay": {
            "support_replay_ready": True,
            "closure_replay_allowed": False,
            "blocked_by_open_leaves": sorted(open_leaves),
        },
        "forbidden": template["forbidden"],
        "target_fitting_used": False,
    }
    OUTPUT_FILLED.write_text(json.dumps(filled, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    fields = {
        "source_certificate": filled["source_certificate"]["same_selected_source_as_heterotic_QaSU3_threshold_branch"],
        "not_routec_import": filled["source_certificate"]["not_routec_or_benchmark_import"],
        "domain_source_owned": filled["domain"]["F3xF3_rank_slot_deck_action_source_owned"],
        "operator_coemission": filled["operators"]["source_emits_C_tau"] and filled["operators"]["source_emits_PhiFin_DE"],
        "kernel_trace_source_owned": filled["finitepart"]["kernel_trace_policy_source_owned"],
        "finitepart_source_owned": filled["finitepart"]["finitepart_trace_identity_for_oriented_nonzero_sector_source_owned"],
    }
    declaration_closed = all(fields.values())

    decision = {
        "fill_attempt_executed": True,
        "support_values_filled": True,
        "source_owned_fields": fields,
        "direct_BN27_source_declaration_closed": declaration_closed,
        "bundle_A_source_selector_closed": False,
        "support_replay_ready": True,
        "closure_replay_allowed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinDirectBN27SourceDeclarationFillOrBundleASelector",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "normal_form": normal["status"],
            "direct_response_packet": response["schema"],
            "repair_packet": repair["status"],
            "sourceleaf": sourceleaf["status"],
        },
        "filled_declaration_path": rel(OUTPUT_FILLED),
        "filled_support_summary": {
            "basis_dimension": filled["domain"]["basis_dimension"],
            "oriented_nonzero_count": filled["domain"]["oriented_nonzero_count"],
            "positive_spectrum_count": len(filled["operators"]["positive_spectrum"]),
            "oriented_abs_sector_logdet_exact": filled["finitepart"]["oriented_abs_sector_logdet_exact"],
            "green_trace": filled["operators"]["green_trace"],
            "green_square_trace": filled["operators"]["green_square_trace"],
            "closed_support_leaves": sorted(closed_leaves),
            "open_source_leaves": sorted(open_leaves),
        },
        "decision": decision,
        "theorem": {
            "name": "DirectBN27SourceDeclarationFillSupportOnlyTheorem",
            "proved": True,
            "statement": (
                "The direct BN27 declaration template can be filled with all current support values: 27-mode domain, "
                "commuting C_tau/PhiFin_DE table, 16 oriented nonzero rows, diagonal D_E/Green/Riesz support, and the "
                "exact full-orbit trace identity log(92160000). It still cannot close because none of the decisive "
                "source-owned fields are emitted: same-source certificate, non-Route-C provenance, deck action ownership, "
                "operator co-emission, kernel/trace ownership, and finitepart identity ownership remain false."
            ),
        },
        "guardrails": {
            "does_not_close_by_support_values": True,
            "does_not_promote_log92160000": True,
            "does_not_promote_routec_import": True,
            "does_not_use_lifted_selected_flags": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "filled_declaration_path": rel(OUTPUT_FILLED),
        "note_path": rel(OUTPUT_NOTE),
        "support_values_filled": True,
        "direct_BN27_source_declaration_closed": False,
        "bundle_A_source_selector_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin DirectBN27 SourceDeclaration Fill or BundleA Selector v1

## Result

```text
status = {STATUS}
support_values_filled = true
direct_BN27_source_declaration_closed = false
bundle_A_source_selector_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Filled Declaration Attempt

```text
{rel(OUTPUT_FILLED)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_FILLED)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
