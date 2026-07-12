"""Attempt to fill the oriented Phi_fin selected-connection witness export."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "export_request": DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_request.json",
    "sourceidentity_gate": DATA / "selected_heterotic_orientedphifin_heterotic_routec_sourceidentity_or_selectedconnectionwitness.candidate.json",
    "u1y_witness_contract": DATA / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.candidate.json",
    "u1y_finite_hym_partial": DATA / "selected_u1y_routec_finite_hym_connection_solve_or_typed_cech_payload.candidate.json",
    "routec_trace": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
    "simultaneous_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
    "trace_identity": DATA / "selected_heterotic_orientedphifin_fullfourierorbit_traceidentity.json",
    "bn27_orbitclosure_report": DATA / "selected_heterotic_orientedphifin_bn27_orbitclosure_sourcefill_report.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_fill.candidate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_minimal_source_values_packet.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_fill_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_SelectedConnectionWitness_Export_Fill_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SELECTEDCONNECTIONWITNESS_EXPORT_FILL_SUPPORT_READY_SOURCE_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceIdentityTransport_or_ConnectionValues_MinimalPacket_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    request = load(INPUTS["export_request"])
    gate = load(INPUTS["sourceidentity_gate"])
    witness = load(INPUTS["u1y_witness_contract"])
    finite_hym = load(INPUTS["u1y_finite_hym_partial"])
    routec_trace = load(INPUTS["routec_trace"])
    table = load(INPUTS["simultaneous_table"])
    trace_identity = load(INPUTS["trace_identity"])
    orbit_report = load(INPUTS["bn27_orbitclosure_report"])

    support = {
        "basis_id": table["basis_id"],
        "basis_dimension": table["basis_dimension"],
        "rank_slots": [0, 1, 2],
        "deck": "F3xF3",
        "C_tau_spectrum": table["counts"]["C_tau_spectrum"],
        "PhiFin_kernel_count": table["counts"]["PhiFin_kernel_count"],
        "PhiFin_positive_count": table["counts"]["PhiFin_positive_count"],
        "oriented_nonzero_positive_count": table["counts"]["oriented_nonzero_Ctau_positive_magnitude_count"],
        "oriented_abs_sector_product": trace_identity["oriented_abs_sector_product"],
        "oriented_abs_sector_logdet_exact": trace_identity["oriented_abs_sector_logdet_exact"],
        "full_positive_product_including_Ctau0": trace_identity["full_positive_product_including_Ctau0"],
        "commutation_closed": table["commutation"]["commutator_zero"],
        "relative_trace_identity_closed": trace_identity["identity_closed_relative_to_full_orbit_source"],
        "routec_DE_gap_layer_closed": finite_hym["decision"]["DE_action_closed_for_gap_layer"],
        "routec_Riesz_Green_gap_layer_closed": finite_hym["decision"]["Riesz_Green_gap_layer_closed"],
        "routec_trace_support_status": routec_trace["status"],
        "orbit_audit_replay_closed": orbit_report["fill_status"]["audit_replay"]["filled"],
        "orbit_compatibility_closed": orbit_report["fill_status"]["compatibility"]["filled"],
    }

    export_fields = {
        "source_identity": {
            "support_present": True,
            "selected_source_owned": False,
            "filled_for_export": False,
            "value": None,
            "blocker": "no theorem transports heterotic Qa/SU3 source ownership to the Route-C/q79 BN27 finite trace row",
        },
        "BN27_deck_action": {
            "support_present": support["basis_dimension"] == 27 and support["deck"] == "F3xF3",
            "selected_source_owned": False,
            "filled_for_export": False,
            "value": {
                "basis_id": support["basis_id"],
                "deck": support["deck"],
                "rank_slots": support["rank_slots"],
            },
            "blocker": "deck action is table/Route-C replayable, but not emitted by the heterotic source witness",
        },
        "operators": {
            "support_present": support["commutation_closed"] and support["routec_DE_gap_layer_closed"],
            "selected_source_owned": False,
            "filled_for_export": False,
            "value": {
                "C_tau": table["operators"]["C_tau"],
                "PhiFin_DE": table["operators"]["PhiFin_DE"],
                "commutator_zero": support["commutation_closed"],
            },
            "blocker": "C_tau and PhiFin_DE commute on BN27, but one source algebra owning both is not proved",
        },
        "kernel_policy": {
            "support_present": True,
            "selected_source_owned": False,
            "filled_for_export": False,
            "value": {
                "C_tau_zero_rank_count": support["C_tau_spectrum"]["0"],
                "PhiFin_kernel_count": support["PhiFin_kernel_count"],
                "positive_policy": trace_identity["positive_oriented_policy"],
            },
            "blocker": "kernel/no-double-count policy is algebraically replayed, not source-exported by a selected connection",
        },
        "trace_policy": {
            "support_present": support["relative_trace_identity_closed"],
            "selected_source_owned": False,
            "filled_for_export": False,
            "value": {
                "plus_sector_product": trace_identity["plus_sector_product"],
                "minus_sector_product": trace_identity["minus_sector_product"],
                "oriented_abs_sector_product": support["oriented_abs_sector_product"],
                "oriented_abs_sector_logdet_exact": support["oriented_abs_sector_logdet_exact"],
            },
            "blocker": "finitepart identity is exact relative to full-orbit source ownership, which is still the missing witness",
        },
        "audit_replay": {
            "support_present": True,
            "selected_source_owned": True,
            "filled_for_export": True,
            "value": {
                "oriented_rows": support["oriented_nonzero_positive_count"],
                "orbit_audit_replay_closed": support["orbit_audit_replay_closed"],
                "target_fitting_used": False,
            },
            "blocker": None,
        },
    }

    family_fill = {
        "typed_monad_cech": {
            "closed": witness["decision"]["typed_monad_cech_values_present"],
            "missing_count": witness["payload_counts"]["typed_monad_cech_missing"],
            "first_missing": "typed f_i/g_i sections plus Cech transitions and g o f certificate",
        },
        "direct_hym": {
            "closed": witness["decision"]["direct_hym_values_present"],
            "missing_count": witness["payload_counts"]["direct_hym_missing"],
            "first_missing": "selected A/F_A or equivalent HYM connection coefficients with residual certificate",
        },
        "finite_routec_solve": {
            "closed": witness["decision"]["finite_routec_solve_values_present"],
            "missing_count": witness["payload_counts"]["finite_routec_solve_missing"],
            "partial_promotions": {
                "DE_gap_layer": finite_hym["decision"]["DE_action_closed_for_gap_layer"],
                "Riesz_Green_gap_layer": finite_hym["decision"]["Riesz_Green_gap_layer_closed"],
                "analytic_alpha1_kernel_formula": finite_hym["decision"]["analytic_alpha1_kernel_formula_proved"],
            },
            "first_missing": "same-source source identity plus connection/residual/export values beyond the D_E gap layer",
        },
        "smooth_EQa_quotient": {
            "closed": gate["route_status"]["smooth_bundle_EQa_witness"]["closed"],
            "missing_count": 4,
            "first_missing": "selected smooth bundle connection A/F_A and representation trace producing E_Qa",
        },
    }

    support_ready_count = sum(1 for item in export_fields.values() if item["support_present"])
    export_filled_count = sum(1 for item in export_fields.values() if item["filled_for_export"])

    minimal_packet = {
        "schema": "SelectedHeterotic.OrientedPhiFin.SelectedConnectionWitnessMinimalSourceValuesPacket.v1",
        "status": "MINIMAL_SOURCE_VALUES_REQUIRED",
        "why_this_is_the_smallest_remaining_leaf": (
            "All six export fields are either algebraically replayable or explicitly blocked by the same missing "
            "source-ownership transport. The only field filled as an export is audit replay. Source identity must "
            "be supplied before BN27 deck action, operators, kernel policy, and trace policy can be promoted."
        ),
        "acceptable_minimal_values": {
            "source_identity_transport": [
                "same-source theorem: heterotic Qa/SU3 branch emits Route-C/q79 BN27 finite trace row",
                "proof that C_tau orientation and PhiFin_DE magnitude are co-emitted before finite comparison",
                "no lifted selected flags; rerun current audits from emitted source theorem",
            ],
            "typed_connection_values": [
                "typed f_i/g_i representatives and Cech transitions",
                "g o f = 0 and exactness/local-freeness certificate",
                "Hermitian metric/trace and BN27 export map",
            ],
            "direct_connection_values": [
                "selected A/F_A or projective rho_E transition matrices",
                "HYM/Strominger/Bianchi residual certificate",
                "finite D_E/E_Qa action and zeta finitepart rule",
            ],
        },
        "must_not_use": request["forbidden_shortcuts"],
    }
    OUTPUT_PACKET.write_text(json.dumps(minimal_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "fill_attempt_executed": True,
        "support_ready_count": support_ready_count,
        "export_required_count": len(export_fields),
        "export_filled_count": export_filled_count,
        "audit_replay_export_filled": export_fields["audit_replay"]["filled_for_export"],
        "source_identity_export_filled": export_fields["source_identity"]["filled_for_export"],
        "BN27_deck_action_export_filled": export_fields["BN27_deck_action"]["filled_for_export"],
        "operators_export_filled": export_fields["operators"]["filled_for_export"],
        "kernel_policy_export_filled": export_fields["kernel_policy"]["filled_for_export"],
        "trace_policy_export_filled": export_fields["trace_policy"]["filled_for_export"],
        "selected_connection_witness_export_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinSelectedConnectionWitnessExportFill",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "sourceidentity_gate": gate["status"],
            "u1y_witness_contract": witness["status"],
            "u1y_finite_hym_partial": finite_hym["status"],
            "routec_trace": routec_trace["status"],
            "bn27_orbitclosure_report": orbit_report["status"],
        },
        "support": support,
        "export_fields": export_fields,
        "family_fill": family_fill,
        "minimal_source_values_packet_path": rel(OUTPUT_PACKET),
        "decision": decision,
        "theorem": {
            "name": "SelectedConnectionWitnessExportFillSupportReadySourceOpenTheorem",
            "proved": True,
            "statement": (
                "The selected-connection export request can be filled only at the audit-replay level from the "
                "current corpus. The BN27 deck, commuting C_tau/PhiFin_DE operator table, kernel policy, and "
                "exact log(92160000) trace identity are all replayable support, but none is source-owned by a "
                "selected heterotic connection witness. Therefore the remaining proof is not a numerical "
                "calculation; it is a minimal source-values packet giving either source-identity transport, "
                "typed Cech/monad connection values, or direct HYM/projective rho_E connection values."
            ),
        },
        "guardrails": {
            "does_not_promote_routec_support_to_source_identity": True,
            "does_not_promote_log92160000": True,
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
        "minimal_source_values_packet_path": rel(OUTPUT_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "support_ready_count": support_ready_count,
        "export_filled_count": export_filled_count,
        "export_required_count": len(export_fields),
        "selected_connection_witness_export_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin SelectedConnectionWitness Export Fill v1

## Result

```text
status = {STATUS}
support_ready_count = {support_ready_count}
export_filled_count = {export_filled_count}
export_required_count = {len(export_fields)}
selected_connection_witness_export_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

Minimal source-values packet:

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
