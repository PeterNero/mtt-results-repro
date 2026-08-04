"""Attempt to fill the BN27 orbit-closure source request."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "orbitclosure_request": DATA / "selected_heterotic_orientedphifin_bn27_orbitclosure_source_request.json",
    "bn27_bridge_gate": DATA / "selected_heterotic_orientedphifin_bn27_sourcedomainbridge_or_smootheqa_quotient.candidate.json",
    "routec_selected_trace": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
    "routec_finite_trace_source": DATA / "selected_u1y_routec_selected_finite_trace_source_or_nogo.candidate.json",
    "routec_phifin_subpacket": DATA / "selected_u1y_routec_finite_emission_morphism_phifin_subpacket.candidate.json",
    "routec_source_certificate": DATA / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction.candidate.json",
    "simultaneous_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
    "trace_identity": DATA / "selected_heterotic_orientedphifin_fullfourierorbit_traceidentity.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_orbitclosure_sourcefill.candidate.json"
OUTPUT_REPORT = DATA / "selected_heterotic_orientedphifin_bn27_orbitclosure_sourcefill_report.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_orbitclosure_sourcefill_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_OrbitClosure_SourceFill_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_ORBITCLOSURE_FILL_ATTEMPT_SUPPORT_ONLY_SOURCE_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_HeteroticRouteC_SourceIdentity_or_SelectedConnectionWitness_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    request = load(INPUTS["orbitclosure_request"])
    bridge = load(INPUTS["bn27_bridge_gate"])
    routec_trace = load(INPUTS["routec_selected_trace"])
    routec_finite = load(INPUTS["routec_finite_trace_source"])
    phifin_subpacket = load(INPUTS["routec_phifin_subpacket"])
    routec_source = load(INPUTS["routec_source_certificate"])
    table = load(INPUTS["simultaneous_table"])
    trace_identity = load(INPUTS["trace_identity"])

    routec_support = {
        "selected_deck_action_support": {
            "present": routec_trace["finite_trace_route"]["proof_steps"]["canonical_active_metric_normalization_source"]["proved"],
            "source": "Route-C selected finite trace theorem",
            "reason": routec_trace["finite_trace_route"]["proof_steps"]["canonical_active_metric_normalization_source"]["reason"],
        },
        "uniform_trace_weight_support": {
            "present": routec_trace["finite_trace_route"]["proof_steps"]["canonical_active_metric_normalization_source"]["proved"],
            "source": "Route-C selected finite trace theorem",
            "reason": "identity Gram/quadrature on the uniform F3xF3 Fourier deck",
        },
        "projective_deck_action_support": {
            "present": routec_trace["finite_trace_route"]["proof_steps"]["projective_flat_connection_to_DE_source"]["proved"],
            "source": "Route-C selected finite trace theorem",
            "reason": routec_trace["finite_trace_route"]["proof_steps"]["projective_flat_connection_to_DE_source"]["reason"],
        },
        "BN27_basis_support": {
            "present": table["basis_dimension"] == 27,
            "basis_id": table["basis_id"],
            "basis_dimension": table["basis_dimension"],
        },
    }

    fill_status = {
        "selected_deck_action": {
            "filled": False,
            "support": routec_support["selected_deck_action_support"],
            "blocker": "deck action is selected on Route-C/q79 support, not yet emitted by the heterotic Qa/SU3 source branch",
        },
        "rank_slot_completion": {
            "filled": False,
            "support": {
                "full_C_tau_spectrum": table["counts"]["C_tau_spectrum"],
                "all_rank_slots_present_per_deck_point": True,
                "rank_slot_count": 3,
            },
            "blocker": "rank-slot completion is table-materialized, but no heterotic source theorem says the threshold carrier retains all rank slots",
        },
        "orbit_closure_rule": {
            "filled": False,
            "support": {
                "full_oriented_rows_count": table["counts"]["oriented_nonzero_Ctau_positive_magnitude_count"],
                "routec_full_positive_orbit_selected_at_gap_scope": bridge["decision"]["embedding_support_insufficient"],
            },
            "blocker": "no selected heterotic orbit-retention axiom or connection witness converts sparse shadow support to the full orbit",
        },
        "kernel_policy": {
            "filled": False,
            "support": {
                "PhiFin_kernel_count": table["counts"]["PhiFin_kernel_count"],
                "C_tau_zero_rank_count": table["counts"]["C_tau_spectrum"]["0"],
                "relative_trace_identity_closed": trace_identity["identity_closed_relative_to_full_orbit_source"],
            },
            "blocker": "kernel policy is algebraic/relative; source ownership still depends on BN27 domain emission",
        },
        "trace_weight_policy": {
            "filled": False,
            "support": routec_support["uniform_trace_weight_support"],
            "blocker": "uniform weights are Route-C trace support, not same-source heterotic threshold weights",
        },
        "compatibility": {
            "filled": True,
            "support": {
                "rho_shadow_projection_compatible": bridge["orbit_completion_test"]["embedded_11_shadow"]["rho_intertwines"],
                "determinant_not_identified": True,
                "embedding_support_insufficient_recorded": bridge["decision"]["embedding_support_insufficient"],
            },
            "blocker": None,
        },
        "audit_replay": {
            "filled": True,
            "support": {
                "oriented_nonzero_positive_rows": table["counts"]["oriented_nonzero_Ctau_positive_magnitude_count"],
                "oriented_abs_sector_product": trace_identity["oriented_abs_sector_product"],
                "oriented_abs_sector_logdet_exact": trace_identity["oriented_abs_sector_logdet_exact"],
                "target_fitting_used": False,
            },
            "blocker": None,
        },
    }
    filled_count = sum(1 for item in fill_status.values() if item["filled"])

    source_identity_cutset = {
        "schema": "SelectedHeterotic.OrientedPhiFin.HeteroticRouteCSourceIdentityCutset.v1",
        "status": "SELECTED_CONNECTION_WITNESS_REQUIRED",
        "why_current_fill_fails": [
            "Route-C/q79 selects the 27-mode deck trace and D_E gap layer at its own source scope.",
            "The heterotic Qa/SU3 source record currently selects the 11-label finite physical quotient and C_tau shadow/intertwiner.",
            "No theorem identifies these as one selected source branch or emits a selected connection witness exporting the BN27 deck action into heterotic threshold ownership.",
        ],
        "minimal_closing_payload": {
            "same_source_identity": "heterotic Qa/SU3 source = Route-C/q79 finite trace source for this BN27 threshold row",
            "selected_connection_witness": "typed Cech/HYM/finite connection values with theorem-derived selected-source flags",
            "BN27_export": "selected deck action, rank-slot completion, kernel and uniform trace policy emitted by that witness",
            "honest_replay": "rerun D_E/Riesz/Green, C_tau, oriented finitepart, and no-double-count audits without lifted flags",
        },
        "support_available_but_not_enough": routec_support,
    }

    report = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27OrbitClosureSourceFillAttempt.v1",
        "status": "SUPPORT_ONLY_SOURCE_IDENTITY_OPEN",
        "filled_count": filled_count,
        "required_count": len(fill_status),
        "fill_status": fill_status,
        "source_identity_cutset": source_identity_cutset,
        "routec_source_state": {
            "routec_trace_status": routec_trace["status"],
            "finite_trace_source_status": routec_finite["status"],
            "phifin_subpacket_status": phifin_subpacket["status"],
            "routec_source_certificate_status": routec_source["status"],
            "selected_basis_B_N_emitted_in_old_subpacket": phifin_subpacket["decision"]["selected_basis_B_N_emitted"],
            "selected_routec_source_certificate_closed": routec_source["decision"]["selected_routec_source_certificate_closed"],
            "typed_DE_construction_closed": routec_source["decision"]["typed_DE_construction_closed"],
        },
        "guardrails": {
            "does_not_promote_routec_support_to_heterotic_source": True,
            "does_not_promote_orbitclosure_without_connection_witness": True,
            "does_not_promote_log92160000": True,
            "does_not_use_lifted_selected_flags": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
    }
    OUTPUT_REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "BN27_orbitclosure_fill_attempted": True,
        "filled_count": filled_count,
        "required_count": len(fill_status),
        "compatibility_closed": True,
        "audit_replay_closed": True,
        "selected_deck_action_closed_for_heterotic_source": False,
        "rank_slot_completion_closed_for_heterotic_source": False,
        "orbit_closure_rule_closed_for_heterotic_source": False,
        "kernel_trace_policy_source_owned": False,
        "BN27_orbitclosure_source_bridge_closed": False,
        "branch_identity_closed": False,
        "oriented_logdet_promoted": False,
        "minimal_next_leaf": "heterotic_routec_same_source_identity_or_selected_connection_witness",
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27OrbitClosureSourceFill",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "bn27_bridge_gate": bridge["status"],
            "routec_selected_trace": routec_trace["status"],
            "routec_finite_trace_source": routec_finite["status"],
            "routec_phifin_subpacket": phifin_subpacket["status"],
            "routec_source_certificate": routec_source["status"],
        },
        "fill_attempt_report_path": rel(OUTPUT_REPORT),
        "decision": decision,
        "theorem": {
            "name": "BN27OrbitClosureSourceFillSupportOnlyTheorem",
            "proved": True,
            "statement": (
                "The existing Route-C/q79 finite trace theorem supplies strong support for "
                "the uniform F3xF3 Fourier deck, projective deck action, and BN27 D_E gap "
                "layer. The oriented table and trace identity replay the full 16-row oriented "
                "positive sector and product log(92160000). However, those facts are not yet "
                "emitted by the heterotic Qa/SU3 source branch. The BN27 orbit-closure request "
                "therefore fills only compatibility and audit replay. Closure requires a "
                "same-source heterotic/Route-C identity theorem or an explicit selected "
                "connection witness exporting the BN27 deck action into heterotic threshold "
                "ownership."
            ),
        },
        "guardrails": report["guardrails"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "fill_attempt_report_path": rel(OUTPUT_REPORT),
        "note_path": rel(OUTPUT_NOTE),
        "BN27_orbitclosure_fill_attempted": True,
        "filled_count": filled_count,
        "required_count": len(fill_status),
        "BN27_orbitclosure_source_bridge_closed": False,
        "branch_identity_closed": False,
        "oriented_logdet_promoted": False,
        "minimal_next_leaf": decision["minimal_next_leaf"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 OrbitClosure SourceFill v1

## Result

```text
status = {STATUS}
filled_count = {filled_count}
required_count = {len(fill_status)}
BN27_orbitclosure_source_bridge_closed = false
branch_identity_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

Report:

```text
{rel(OUTPUT_REPORT)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_REPORT)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
