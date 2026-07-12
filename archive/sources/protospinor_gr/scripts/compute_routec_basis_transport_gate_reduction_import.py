from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PHIFIN_SCAFFOLD = ROOT / "certificates" / "phifin_operator_payload_scaffold_import_certificate.json"
NONINV_CERT = SM / "certificates" / "selected_routec_noninvariant_c1_primitive_search_certificate.json"
NONINV_DATA = SM / "candidate_data" / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
SOURCE_AUDIT_CERT = SM / "certificates" / "selected_routec_primitive_source_selection_audit_certificate.json"
SOURCE_AUDIT_DATA = SM / "candidate_data" / "selected_routec_primitive_source_selection_audit.candidate.json"
FIBER_CERT = SM / "certificates" / "selected_routec_fiberclass_observable_invariance_or_gaugefix_certificate.json"
FIBER_DATA = SM / "candidate_data" / "selected_routec_fiberclass_observable_invariance_or_gaugefix.candidate.json"
BASIS_SLOT_CERT = SM / "certificates" / "selected_routec_basis_transport_primitive_source_theorem_certificate.json"
BASIS_SLOT_DATA = SM / "candidate_data" / "selected_routec_basis_transport_primitive_source_theorem.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_basis_transport_gate_reduction_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_basis_transport_gate_reduction_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_BasisTransport_Gate_Reduction_Import_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    phifin = load(PHIFIN_SCAFFOLD)
    noninv_cert = load(NONINV_CERT)
    noninv = load(NONINV_DATA)
    source_cert = load(SOURCE_AUDIT_CERT)
    source = load(SOURCE_AUDIT_DATA)
    fiber_cert = load(FIBER_CERT)
    fiber = load(FIBER_DATA)
    basis_cert = load(BASIS_SLOT_CERT)
    basis = load(BASIS_SLOT_DATA)

    fixed_fiber = source["fiber_class_theorem"]["fixed_fiber_shifts"]
    fixed_shifts = sorted(fixed_fiber["ranks"].keys())
    sectors = ["d", "e", "nuD", "u"]
    active_shift = source["active_shift_theorem"]["enumeration"]["nonzero_active_shifts"]

    closed_now = {
        "Phi_fin_operator_scaffold_available": phifin["verdict"]["phi_fin_finite_operator_scaffold_imported"],
        "canonical_zero_repaired_at_candidate_level": noninv_cert["what_closes"]["canonical_zero_repaired_at_candidate_level"],
        "active_shift_1_1_unique_and_forced": (
            source["active_shift_theorem"]["proved"] is True
            and active_shift == [[1, 1]]
            and source_cert["what_closes"]["active_shift_1_1_forced_by_finite_support"] is True
        ),
        "fixed_fiber_shifts_reduced_to_one_qutrit_gauge_class": source_cert["what_closes"]["fixed_fiber_shifts_reduced_to_one_qutrit_gauge_class"],
        "all_fiber_envelope_retired_as_fixed_single_charge_candidate": source_cert["what_closes"]["all_fiber_envelope_retired_as_fixed_single_charge_candidate"],
        "current_spectral_observables_invariant_under_fixed_fiber_class": fiber_cert["what_closes"]["observable_invariance_under_fixed_fiber_class_for_current_C1_spectrum"],
        "canonical_shift0_computation_gauge_allowed": fiber_cert["what_closes"]["canonical_shift0_computation_gauge_allowed"],
        "named_basis_transport_source_theorem_slot_exists": basis_cert["what_closes"]["named_theorem_slot_added"],
        "target_fitting_excluded": (
            noninv_cert["what_closes"]["target_fitting_excluded"] is True
            and source_cert["what_closes"]["no_observed_flavor_data_used"] is True
            and fiber_cert["what_closes"]["no_observed_flavor_data_used"] is True
            and basis_cert["what_closes"]["target_fitting_excluded"] is True
        ),
    }

    still_open = {
        "selected_basis_transport_or_vertex_source": basis_cert["what_remains_open"]["prove_selected_basis_transport_or_vertex_source"],
        "selected_noninvariant_C1_primitive_or_vertex_source": fiber_cert["what_remains_open"]["selected_noninvariant_C1_primitive_or_vertex_source"],
        "operator_level_basis_transport": fiber_cert["what_remains_open"]["operator_level_basis_transport"],
        "alpha1_driver_verified": fiber_cert["what_remains_open"]["alpha1_driver_verified"],
        "selected_dotD_source_verified": fiber_cert["what_remains_open"]["selected_dotD_source_verified"],
        "emit_A_selected_and_b_selected": basis_cert["what_remains_open"]["emit_A_selected_and_b_selected"],
        "solve_or_reject_splitter_equation": basis_cert["what_remains_open"]["solve_or_reject_splitter_equation"],
        "honest_replay_without_lifted_flags": fiber_cert["what_remains_open"]["honest_replay_without_lifted_flags"],
        "full_SM_or_no_knob_closure": fiber_cert["what_remains_open"]["full_SM_or_no_knob_closure"],
    }

    reduction = {
        "active_shift": active_shift[0],
        "fixed_qutrit_fiber_shifts": fixed_shifts,
        "fixed_fiber_rank_by_sector": fixed_fiber["ranks"],
        "fixed_fiber_frobenius_norm_by_sector": fixed_fiber["frobenius_norms"],
        "spectral_invariants_scope": fiber["path_A_observable_invariance"]["scope"],
        "canonical_computation_gauge": fiber["path_B_absolute_gauge_fix"]["canonical_computation_gauge"],
        "current_layer_limitation": fiber["path_A_observable_invariance"]["why_not_physical_flavor_closure"],
    }

    theorem = {
        "name": "RouteCBasisTransportGateReductionImportTheorem",
        "proved": all(closed_now.values()),
        "statement": (
            "The finite Route-C C1 gate is reduced to a source-emission theorem: "
            "finite support forces active shift (1,1), the fixed qutrit fiber "
            "shifts 0,1,2 form one current-layer spectral gauge class, and shift "
            "0 may be used as a computation gauge for the current spectral "
            "invariants. This does not prove selected basis transport or nonzero "
            "physical flavor closure."
        ),
    }

    verdict = {
        "basis_transport_gate_reduced": theorem["proved"],
        "fiber_choice_ambiguity_removed_for_current_spectral_invariants": True,
        "selected_basis_transport_source_proved": False,
        "selected_C1_primitive_promoted": False,
        "nondegenerate_yukawa_or_CKM_PMNS_closed": False,
        "next_required_artifact": "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Proof_or_Counterexample_v1",
    }

    guardrails = {
        "does_not_claim_selected_basis_transport": True,
        "does_not_claim_selected_C1_promotion": True,
        "does_not_claim_flavor_closure": True,
        "does_not_use_observed_or_benchmark_inputs": True,
        "does_not_lift_flags_by_hand": True,
    }

    packet = {
        "theorem": theorem,
        "reduction": reduction,
        "basis_transport_theorem_slot": basis["theorem_slot"],
        "closed_now": closed_now,
        "still_open": still_open,
        "verdict": verdict,
    }

    note = """# Route-C BasisTransport Gate Reduction Import v1

## Result

The next `Phi_fin`/Route-C C1 gate is reduced but not closed.

Finite support proves that the only nonzero active deck shift for the current
one-response C1 primitive class is:

```text
(1,1)
```

The fixed qutrit fiber shifts `0`, `1`, and `2` form one current-layer spectral
gauge class. For the present finite C1 layer, `YY*` is scalar identity in each
fixed-fiber sector, so rank, determinant magnitude, trace invariants, and
singular spectra are invariant under the fixed-fiber shift. Therefore shift `0`
may be used as a computation gauge for these current spectral invariants.

## Boundary

This does not prove operator-level basis transport, selected non-invariant C1
source emission, `A_selected`, `b_selected`, the locked `DeltaTheta_C1` solve,
or nondegenerate flavor/CKM/PMNS closure. The current layer is still degenerate;
the source theorem or a higher-order/full-response splitting is still required.

## Status

```text
ROUTEC_BASISTRANSPORT_GATE_REDUCED_SOURCE_PROOF_OPEN
```
"""

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "routec_basis_transport_gate_reduction_import",
        "status": "ROUTEC_BASISTRANSPORT_GATE_REDUCED_SOURCE_PROOF_OPEN",
        "input_certificates": {
            "phifin_operator_payload_scaffold_import": str(PHIFIN_SCAFFOLD),
            "selected_routec_noninvariant_c1_primitive_search": str(NONINV_CERT),
            "selected_routec_primitive_source_selection_audit": str(SOURCE_AUDIT_CERT),
            "selected_routec_fiberclass_observable_invariance_or_gaugefix": str(FIBER_CERT),
            "selected_routec_basis_transport_primitive_source_theorem": str(BASIS_SLOT_CERT),
        },
        "theorem": theorem,
        "reduction": reduction,
        "closed_now": closed_now,
        "still_open": still_open,
        "verdict": verdict,
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print("STATUS: ROUTEC_BASISTRANSPORT_GATE_REDUCED_SOURCE_PROOF_OPEN")


if __name__ == "__main__":
    main()
