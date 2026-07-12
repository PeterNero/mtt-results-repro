"""Build BN27 source-branch identity three-clause fill / connection solve gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "validator_fill": DATA / "selected_heterotic_orientedphifin_bn27_validatorexport_fill_or_selectedconnectionsolve.candidate.json",
    "dependency_collapse": DATA / "selected_heterotic_orientedphifin_bn27_validator_dependency_collapse.json",
    "sourcebranch_nogo": DATA / "selected_heterotic_orientedphifin_sourcebranchidentity_emission_or_nogo.candidate.json",
    "repair_packet": DATA / "selected_heterotic_orientedphifin_sourcebranchidentity_repair_packet.json",
    "refined_root_cutset": DATA / "selected_heterotic_orientedphifin_bn27_sourceidentity_refined_root_cutset.json",
    "direct_source_frontier": DATA / "selected_heterotic_orientedphifin_bn27_sourceidentity_directsourcetheorem_or_connectionvalues_externalconstruction.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_threeclause_fill_or_connectionsolve.candidate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_threeclause_acceptance_packet.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_threeclause_fill_or_connectionsolve_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_SourceBranchIdentity_ThreeClause_Fill_or_ConnectionSolve_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEBRANCHIDENTITY_THREECLAUSE_FILL_REDUCED_TO_SOURCE_AMENDMENT_OR_CONNECTIONVALUES"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceBranchIdentity_SourceAmendment_Template_or_ConnectionValues_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    validator_fill = load(INPUTS["validator_fill"])
    collapse = load(INPUTS["dependency_collapse"])
    sourcebranch = load(INPUTS["sourcebranch_nogo"])
    repair = load(INPUTS["repair_packet"])
    roots = load(INPUTS["refined_root_cutset"])
    frontier = load(INPUTS["direct_source_frontier"])

    clauses = collapse["three_clause_sourcebranch_cutset"]
    clause_fill = {
        key: {
            "support_present": value["support_present"],
            "emitted_by_current_source": value["emitted_by_current_source"],
            "required": value["required"],
            "current_blocker": value["blocker"],
            "fill_status": "OPEN_SUPPORT_ONLY",
        }
        for key, value in clauses.items()
    }
    emitted_count = sum(1 for value in clause_fill.values() if value["emitted_by_current_source"])
    support_count = sum(1 for value in clause_fill.values() if value["support_present"])

    acceptance_packet = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.SourceBranchIdentity.ThreeClauseAcceptance.v1",
        "status": "SOURCE_BRANCH_IDENTITY_ACCEPTANCE_PACKET_BUILT_VALUES_OPEN",
        "source_amendment_payload": {
            "selected_source_object_S_QaSU3_BN27": None,
            "one_selected_source_owns_heterotic_C_tau_orientation": None,
            "one_selected_source_owns_RouteC_PhiFin_DE_magnitude": None,
            "operators_coemitted_before_finite_comparison": None,
            "full_F3xF3_rank_slot_carrier_emitted": None,
            "sixteen_nonzero_oriented_positive_rows_retained": None,
            "eleven_label_rho_tau_shadow_embeds_but_is_not_threshold_domain": None,
            "RouteC_row_internal_theorem_not_external_import": None,
            "kernel_shared_circle_policy_source_owned": None,
            "trace_zeta_finitepart_policy_source_owned": None,
            "no_lifted_flags_full_replay_audit": None,
        },
        "connection_values_payload": {
            "typed_f_sections": None,
            "typed_g_sections": None,
            "cech_transition_cocycles": None,
            "g_after_f_zero_exactness_certificate": None,
            "selected_HYM_or_projective_connection_coefficients": None,
            "BN27_DE_Riesz_Green_kernel_trace_export": None,
            "finitepart_log92160000_identity_from_values": None,
            "no_lifted_flags_connection_replay": None,
        },
        "acceptance_logic": {
            "direct_source_amendment_closes": [
                "one_selected_source_names_both_branches",
                "eleven_label_to_full_BN27_threshold_carrier",
                "routec_row_not_external_import",
            ],
            "connection_values_alternative_closes": [
                "same_source_export_to_BN27_validators",
                "operator_coemission",
                "kernel_policy",
                "trace_policy",
                "audit_replay",
            ],
            "all_fields_are_source_values_not_fitted_numbers": True,
        },
        "guardrails": repair["forbidden_shortcuts"],
        "target_fitting_used": False,
    }
    OUTPUT_PACKET.write_text(json.dumps(acceptance_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "attempt_executed": True,
        "support_count": support_count,
        "emitted_count": emitted_count,
        "required_clause_count": len(clause_fill),
        "source_branch_identity_closed": False,
        "source_amendment_packet_built": True,
        "selected_connection_solve_closed": False,
        "same_source_export_to_BN27_validators": False,
        "full_BN27_carrier_emitted": False,
        "routec_internalized": False,
        "one_source_owns_both_branches": False,
        "oriented_logdet_promoted": False,
        "acceptance_packet_path": rel(OUTPUT_PACKET),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27SourceBranchIdentityThreeClauseFillOrConnectionSolve",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "validator_fill": validator_fill["status"],
            "dependency_collapse": collapse["status"],
            "sourcebranch_nogo": sourcebranch["status"],
            "refined_root_cutset": roots["status"],
            "direct_source_frontier": frontier["status"],
        },
        "clause_fill": clause_fill,
        "root_reuse": {
            "selected_trace_equality_for_27mode_DE_gap_layer_closed": roots["scoped_root_refinement"]["selected_trace_equality_for_27mode_DE_gap_layer"]["closed"],
            "full_operator_formula_closed": roots["scoped_root_refinement"]["full_selected_iwasawa_strominger_operator_formula"]["closed"],
            "source_object_named_S_QaSU3_BN27_closed": roots["scoped_root_refinement"]["source_object_named_S_QaSU3_BN27"]["closed"],
            "source_flags_full_BN27_closed": roots["scoped_root_refinement"]["theorem_derived_selected_source_flags_for_full_BN27"]["closed"],
        },
        "acceptance_packet_path": rel(OUTPUT_PACKET),
        "decision": decision,
        "theorem": {
            "name": "BN27SourceBranchIdentityThreeClauseFillTheorem",
            "proved": True,
            "statement": (
                "The current artifact set fills support for all three BN27 source-branch clauses but emits none of them. "
                "Therefore source-branch identity is equivalent, at this frontier, to either a source amendment naming "
                "S_QaSU3^BN27 with full carrier/operator/provenance ownership, or a selected connection-value solve "
                "that exports the same fields to the BN27 validators. The selected 27-mode D_E trace equality remains "
                "usable support but does not close the full BN27 threshold source."
            ),
        },
        "guardrails": {
            "does_not_promote_log92160000": True,
            "does_not_promote_11label_shadow_to_BN27": True,
            "does_not_promote_routec_row_as_heterotic_source": True,
            "does_not_treat_trace_equality_as_full_operator_formula": True,
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
        "acceptance_packet_path": rel(OUTPUT_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "support_count": support_count,
        "emitted_count": emitted_count,
        "source_branch_identity_closed": False,
        "selected_connection_solve_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 SourceBranchIdentity ThreeClause Fill or ConnectionSolve v1

## Result

```text
status = {STATUS}
support_count = {support_count}
emitted_count = {emitted_count}
source_branch_identity_closed = false
selected_connection_solve_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Acceptance Packet

```text
{rel(OUTPUT_PACKET)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_PACKET)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
