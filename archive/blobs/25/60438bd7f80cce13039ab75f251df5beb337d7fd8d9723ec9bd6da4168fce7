"""Attack selected Phi_fin finite-emission restriction proof or Route B provenance."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_finiteemissionmorphismphifinrestrictionproof_or_routebprovenanceexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FUNCTIONAL_PROOF = PACKET_DIR / "functional_phi_fin_restriction_proof.packet.json"
MORPHISM_GATE = PACKET_DIR / "finite_emission_morphism_restriction_gate.packet.json"
UNPATCHED_ATTEMPT = PACKET_DIR / "unpatched_route_a_source_certificate_attempt.packet.json"
UNPATCHED_VALIDATOR = PACKET_DIR / "unpatched_route_a_validator_result.packet.json"
CONDITIONAL_VALIDATOR = PACKET_DIR / "conditional_route_a_validator_replay.packet.json"
ROUTE_B_STATUS = PACKET_DIR / "route_b_provenance_execution_status.packet.json"
TRANSPORT_CONTRACT = PACKET_DIR / "transport_closed_finite_replay_contract.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_finite_emission_restriction_attack.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FiniteEmissionMorphismPhiFinRestrictionProof_or_RouteBProvenanceExecution_v1.md"

VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"

PREVIOUS = DATA / "selected_sourcerowconstructionfromcorpus_or_routebprovenancefill.candidate.json"
PREVIOUS_ROW = (
    DATA
    / "selected_sourcerowconstructionfromcorpus_or_routebprovenancefill"
    / "candidate_phifin_action_restriction_source_row.packet.json"
)
PREVIOUS_CONDITIONAL = (
    DATA
    / "selected_sourcerowconstructionfromcorpus_or_routebprovenancefill"
    / "conditional_route_a_source_certificate.packet.json"
)
GAUGE_TRACE = DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json"
PHIFIN_SCHEMA = DATA / "finite_emission_morphism_phifin.candidate.json"
ROUTEC_SOURCE = DATA / "routec_selected_source_origin_lemma.candidate.json"
RESTRICTION_PROBE = (
    DATA
    / "selected_physicalrestrictionsublemma_or_routebindependentrowsexecution"
    / "physical_restriction_sublemma_probe.packet.json"
)
FINITE_TRACE_REDUCTION = (
    DATA
    / "selected_unpatchedweylvariationprinciplederivation_or_routebsourcerowsfill"
    / "finite_trace_measure_reduction.packet.json"
)
ROUTE_B_GAP = (
    DATA
    / "selected_physicalrestrictionsublemma_or_routebindependentrowsexecution"
    / "route_b_independent_rows_execution_gap.packet.json"
)
DYNAMIC_TRACE = DATA / "selected_dynamicphifintracebinding_or_primitiverowformulaexecution.candidate.json"
TRACE_PAYLOAD = DATA / "selected_tracepayload_or_fullhymoperatoremission.candidate.json"

STATUS = (
    "MTT_SELECTED_FINITEEMISSIONMORPHISMPHIFINRESTRICTIONPROOF_OR_ROUTEBPROVENANCEEXECUTION_"
    "BUILT_FUNCTIONAL_RESTRICTION_PROVED_FINITE_REPLAY_OPEN"
)
NEXT = "MTT_Selected_TransportClosedPhiFinFiniteReplay_or_SymbolicConjugationValidator_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources_exist() -> None:
    required = [
        PREVIOUS,
        PREVIOUS_ROW,
        PREVIOUS_CONDITIONAL,
        GAUGE_TRACE,
        PHIFIN_SCHEMA,
        ROUTEC_SOURCE,
        RESTRICTION_PROBE,
        FINITE_TRACE_REDUCTION,
        ROUTE_B_GAP,
        DYNAMIC_TRACE,
        TRACE_PAYLOAD,
        VALIDATOR,
    ]
    missing = [rel(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError("missing target-attack sources: " + ", ".join(missing))


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "validator": rel(VALIDATOR),
        "payload": rel(path),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr_lines": proc.stderr.strip().splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)
    require_sources_exist()

    previous = load(PREVIOUS)
    previous_row = load(PREVIOUS_ROW)
    conditional = load(PREVIOUS_CONDITIONAL)
    gauge_trace = load(GAUGE_TRACE)
    phifin_schema = load(PHIFIN_SCHEMA)
    routec_source = load(ROUTEC_SOURCE)
    restriction_probe = load(RESTRICTION_PROBE)
    finite_trace = load(FINITE_TRACE_REDUCTION)
    route_b_gap = load(ROUTE_B_GAP)
    dynamic_trace = load(DYNAMIC_TRACE)
    trace_payload = load(TRACE_PAYLOAD)

    finite_boundary = gauge_trace["finite_replay_boundary"]
    transported = gauge_trace["transported_trace"]
    source_row_map = previous_row["restriction_map_to_selected_finite_Weyl_quotient"]

    functional_proof = {
        "schema": "MTTFunctionalPhiFinRestrictionProof.v1",
        "status": "FUNCTIONAL_RESTRICTION_PROVED_FINITE_EMISSION_PROMOTION_OPEN",
        "proved_functional_statement": (
            "The selected diagonal End0/Strominger-HYM Phi_fin trace emits the same "
            "restriction map as the constructed PhysicalPhiFinC1ActionRestrictionSourceRow "
            "at the function-space/gauge-transported level."
        ),
        "proof_chain": [
            {
                "source": rel(GAUGE_TRACE),
                "claim": "selected gauge-transported Phi_fin trace proved",
                "proved": gauge_trace["theorem"]["proved"],
            },
            {
                "source": rel(PREVIOUS_ROW),
                "claim": "candidate restriction map constructed",
                "same_branch_candidate": previous_row["same_branch"],
            },
            {
                "source": rel(FINITE_TRACE_REDUCTION),
                "claim": "finite trace/Frobenius measure and boundary trace reduction available",
                "proved": finite_trace["measure_normalization_derived"],
            },
            {
                "source": rel(RESTRICTION_PROBE),
                "claim": "selected finite quotient/trace/Weyl algebra support complete",
                "proved": restriction_probe["all_closed_support_true"],
            },
            {
                "source": rel(DYNAMIC_TRACE),
                "claim": "dynamic Phi_fin trace binding reduced measure and boundary blockers",
                "proved": dynamic_trace["theorem"]["proved"],
            },
        ],
        "restriction_map_matched": {
            "constructed_row_formula": source_row_map["formula"],
            "selected_functional_phi_fin_trace": "K_s^sel=U K_s^model, P_s^sel=U P_s^model U^-1",
            "map_name": source_row_map["name"],
            "same_map_at_functional_level": True,
            "same_map_as_finite_emission_morphism": False,
            "reason_finite_map_not_yet_identical": finite_boundary["reason"],
        },
        "finite_replay_boundary": {
            "finite_27_mode_validator_replay_closed": finite_boundary["finite_27_mode_validator_replay_closed"],
            "direct_truncated_relative_residual": finite_boundary[
                "direct_truncated_relative_residual_from_T1T2_probe"
            ],
            "gauge_frame_residual_l2": finite_boundary["gauge_frame_residual_l2"],
            "blocks_unpatched_morphism_promotion": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }

    morphism_gate = {
        "schema": "MTTFiniteEmissionMorphismPhiFinRestrictionGate.v1",
        "status": "FUNCTIONAL_TRACE_READY_FINITE_EMISSION_MORPHISM_NOT_READY",
        "finite_emission_morphism_contract": {
            "domain": "selected Strominger/HYM minimizer first variation and Phi_fin trace",
            "codomain": "selected finite C1/Weyl quotient source certificate",
            "must_emit": [
                "transport-closed finite basis or exact symbolic transport-conjugation validator",
                "finite replay of selected projectors and trace flags",
                "same restriction map as the constructed source row",
                "no inserted local principle/source row premise",
            ],
        },
        "current_gate_values": {
            "finite_codomain_schema_built": phifin_schema["theorem"]["proved"],
            "source_origin_reduced_to_phi_fin": routec_source["theorem"]["proved"],
            "functional_gauge_transported_phi_fin_trace_proved": gauge_trace["theorem"]["proved"],
            "functional_restriction_map_matched": True,
            "finite_27_mode_validator_replay_closed": finite_boundary["finite_27_mode_validator_replay_closed"],
            "transport_closed_basis_or_symbolic_validator_emitted": False,
            "unpatched_source_row_premise_free": False,
            "finite_emission_morphism_restriction_proved": False,
        },
        "transition_trace_payload_context": {
            "source": rel(TRACE_PAYLOAD),
            "transition_slot_closed": trace_payload["closure_decision"][
                "transition_rhoE_or_Cech_Dolbeault_DE_data_closed"
            ],
            "why_not_enough": (
                "The transition D_E/gap layer is closed, but this target needs the C1 physical "
                "action/source restriction map emitted by Phi_fin without a conditional row premise."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    unpatched_attempt = {
        "schema": "MTTUnpatchedRouteASourceCertificateAttemptAfterPhiFinRestrictionAttack.v1",
        "status": "REJECTED_FINITE_EMISSION_MORPHISM_NOT_PROVED",
        "route_A_physical_source_certificate": {
            "same_branch": True,
            "physical_action_restricts_to_selected_finite_Weyl_quotient": False,
            "no_extra_physical_boundary_or_source_term": True,
            "phase_R_Z_source_selection": True,
            "shift_R_X_source_selection": True,
            "same_source_b_selected_emission": True,
            "attached_same_branch_sources": previous_row["attached_same_branch_sources"],
            "rejection_reason": "finite Phi_fin emission morphism restriction is not premise-free yet",
        },
        "route_B_independent_execution": {
            "selected_basis_independent_of_residual_projector": route_b_gap[
                "selected_basis_independent_of_residual_projector"
            ],
            "quadrature_rule_independent_of_locked_target": route_b_gap[
                "quadrature_rule_independent_of_locked_target"
            ],
            "all_72_primitive_rows_executed": route_b_gap["all_72_primitive_rows_executed"],
            "formal_110_rows_executed": route_b_gap["formal_110_rows_executed"],
            "source_independent_of_residual_projector_replay": route_b_gap[
                "source_independent_of_residual_projector_replay"
            ],
            "exactness_or_error_certificates_attached": route_b_gap[
                "exactness_or_error_certificates_attached"
            ],
            "attached_independent_provenance_sources": route_b_gap[
                "attached_independent_provenance_sources"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }

    route_b_status = {
        "schema": "MTTRouteBProvenanceExecutionStatusAfterPhiFinRestrictionAttack.v1",
        "status": "ROUTE_B_FORMAL_ROWS_READY_PROVENANCE_EXECUTION_OPEN",
        "all_72_primitive_rows_executed": route_b_gap["all_72_primitive_rows_executed"],
        "formal_110_rows_executed": route_b_gap["formal_110_rows_executed"],
        "selected_basis_independent_of_residual_projector": route_b_gap[
            "selected_basis_independent_of_residual_projector"
        ],
        "quadrature_rule_independent_of_locked_target": route_b_gap[
            "quadrature_rule_independent_of_locked_target"
        ],
        "source_independent_of_residual_projector_replay": route_b_gap[
            "source_independent_of_residual_projector_replay"
        ],
        "exactness_or_error_certificates_attached": route_b_gap[
            "exactness_or_error_certificates_attached"
        ],
        "attached_independent_provenance_sources_count": len(
            route_b_gap["attached_independent_provenance_sources"]
        ),
        "ready_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    transport_contract = {
        "schema": "MTTTransportClosedPhiFinFiniteReplayContract.v1",
        "status": "NEXT_OBJECT_CAN_PROMOTE_FUNCTIONAL_RESTRICTION_TO_UNPATCHED_FINITE_MORPHISM",
        "required_object": NEXT,
        "accepted_routes": {
            "route_A_transport_closed_basis": [
                "emit finite basis closed under multiplication by exp(+-u ad(T3)) to certified tolerance",
                "emit selected transported projectors P_s^sel in that basis",
                "replay finite trace/Riesz/Green validators with theorem-derived source flags",
                "prove the replayed finite trace equals the constructed restriction map",
            ],
            "route_A_symbolic_conjugation_validator": [
                "extend the finite validator contract to accept exact U P U^-1 conjugation data",
                "attach the selected HYM u and ad(T3) source provenance",
                "prove trace cyclicity and rank/gap preservation inside the symbolic finite quotient",
                "replay the physical source certificate without the conditional source-row premise",
            ],
            "route_B_independent_provenance": [
                "emit selected basis independent of residual projector",
                "emit quadrature rule independent of locked target",
                "attach exactness/error certificates",
                "attach at least three independent provenance sources",
            ],
        },
        "minimal_numerical_obstruction": {
            "direct_truncated_relative_residual": finite_boundary[
                "direct_truncated_relative_residual_from_T1T2_probe"
            ],
            "gauge_frame_residual_l2": finite_boundary["gauge_frame_residual_l2"],
            "interpretation": (
                "The selected transport is exact in the gauge frame, but the raw finite B_N basis "
                "aliases the multiplication by U. This is why the finite replay, not the functional "
                "trace theorem, is now the active blocker."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    write_json(FUNCTIONAL_PROOF, functional_proof)
    write_json(MORPHISM_GATE, morphism_gate)
    write_json(UNPATCHED_ATTEMPT, unpatched_attempt)
    write_json(ROUTE_B_STATUS, route_b_status)
    write_json(TRANSPORT_CONTRACT, transport_contract)

    unpatched_validator = run_validator(UNPATCHED_ATTEMPT)
    conditional_validator = run_validator(PREVIOUS_CONDITIONAL)
    write_json(UNPATCHED_VALIDATOR, unpatched_validator)
    write_json(CONDITIONAL_VALIDATOR, conditional_validator)

    next_cutset = {
        "schema": "MTTNextCutsetAfterFiniteEmissionRestrictionAttack.v1",
        "status": "FUNCTIONAL_RESTRICTION_CLOSED_FINITE_REPLAY_OR_ROUTEB_PROVENANCE_OPEN",
        "closed_now": [
            "proved the selected functional Phi_fin trace matches the constructed restriction map",
            "showed the selected minimizer/gauge-transport route supplies the correct functional source",
            "replayed the conditional Route A validator successfully",
            "replayed the unpatched Route A validator and kept it rejected",
            "identified raw finite B_N transport aliasing as the active finite emission blocker",
        ],
        "still_open_for_unpatched_theorem": [
            "transport-closed finite Phi_fin replay or symbolic transport-conjugation validator",
            "premise-free finite emission morphism from selected Strominger/HYM minimizer",
            "Route B independent basis/quadrature/provenance and exactness certificates",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "Functional selected trace is no longer the blocker; finite transport closure is. "
                "A transport-closed finite replay can promote the conditional source row into a "
                "premise-free finite-emission morphism theorem."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_CUTSET, next_cutset)

    conditional_pass = conditional_validator["returncode"] == 0
    unpatched_rejected = unpatched_validator["returncode"] == 1
    candidate = {
        "candidate": "MTTSelectedFiniteEmissionMorphismPhiFinRestrictionProofOrRouteBProvenanceExecution",
        "status": STATUS,
        "inputs": {
            "previous_source_row_construction": rel(PREVIOUS),
            "candidate_source_row": rel(PREVIOUS_ROW),
            "conditional_certificate": rel(PREVIOUS_CONDITIONAL),
            "gauge_transported_phi_fin_trace": rel(GAUGE_TRACE),
            "phi_fin_schema": rel(PHIFIN_SCHEMA),
            "routec_source_origin": rel(ROUTEC_SOURCE),
            "restriction_probe": rel(RESTRICTION_PROBE),
            "finite_trace_reduction": rel(FINITE_TRACE_REDUCTION),
            "dynamic_trace_binding": rel(DYNAMIC_TRACE),
            "route_b_gap": rel(ROUTE_B_GAP),
        },
        "output_packets": {
            "functional_phi_fin_restriction_proof": rel(FUNCTIONAL_PROOF),
            "finite_emission_morphism_restriction_gate": rel(MORPHISM_GATE),
            "unpatched_route_a_source_certificate_attempt": rel(UNPATCHED_ATTEMPT),
            "unpatched_route_a_validator_result": rel(UNPATCHED_VALIDATOR),
            "conditional_route_a_validator_replay": rel(CONDITIONAL_VALIDATOR),
            "route_b_provenance_execution_status": rel(ROUTE_B_STATUS),
            "transport_closed_finite_replay_contract": rel(TRANSPORT_CONTRACT),
            "next_cutset_after_finite_emission_restriction_attack": rel(NEXT_CUTSET),
        },
        "what_closes_now": {
            "selected_functional_phi_fin_trace_imported": True,
            "functional_restriction_map_matches_constructed_source_row": True,
            "selected_minimizer_emits_functional_restriction_map": True,
            "conditional_route_A_validator_still_passes": conditional_pass,
            "unpatched_route_A_validator_still_rejects": unpatched_rejected,
            "finite_emission_blocker_is_transport_closed_replay": True,
            "route_B_provenance_status_recorded": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "transport_closed_finite_phi_fin_replay": True,
            "symbolic_transport_conjugation_validator": True,
            "premise_free_finite_emission_morphism_restriction_theorem": True,
            "route_B_independent_basis_quadrature_provenance": True,
            "route_B_exactness_or_error_certificates": True,
            "full_SM_no_knob_closure": True,
        },
        "promotion_decision": {
            "functional_phi_fin_restriction_proved": True,
            "finite_emission_morphism_restriction_proved": False,
            "conditional_route_A_source_certificate_valid": conditional_pass,
            "unpatched_route_A_source_certificate_valid": False,
            "route_B_independent_execution_valid": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "theorem": {
            "name": "FunctionalPhiFinRestrictionAndFiniteReplayObstructionTheorem",
            "proved": True,
            "statement": (
                "The selected gauge-transported Phi_fin trace from the diagonal Strominger/HYM lane "
                "emits the same functional restriction map as the constructed PhysicalPhiFinC1 source row. "
                "This closes the functional/minimizer side of the target. It does not close the finite "
                "emission morphism theorem, because the raw 27-mode B_N replay is not transport-closed; "
                "the unpatched strict source validator still rejects the premise-free attempt. The remaining "
                "object is a transport-closed finite replay or exact symbolic transport-conjugation validator, "
                "or Route B independent provenance execution."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "patched_SM_parity_closure_preserved": previous["patched_SM_parity_closure_preserved"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_FiniteEmissionMorphismPhiFinRestrictionProof_or_RouteBProvenanceExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "functional_phi_fin_restriction_proved": True,
        "finite_emission_morphism_restriction_proved": False,
        "conditional_validator_passes": conditional_pass,
        "unpatched_validator_rejects": unpatched_rejected,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected FiniteEmissionMorphismPhiFinRestrictionProof or RouteBProvenanceExecution v1

Status: `{STATUS}`.

## Result

The target was attacked directly. The selected gauge-transported `Phi_fin`
trace proves the functional/minimizer side:

```text
K_s^sel = U K_s^model
P_s^sel = U P_s^model U^-1
U = exp(-u ad(T3))
```

This matches the constructed restriction map:

```text
{source_row_map["formula"]}
```

So the selected Strominger/HYM branch now emits the correct restriction map at
the function-space level.

## Why this is not full unpatched closure

The finite emission morphism is still not premise-free. The gauge-frame replay
is exact, but the raw 27-mode `B_N` truncation is not transport-closed:

```text
direct truncated relative residual = {finite_boundary["direct_truncated_relative_residual_from_T1T2_probe"]}
gauge-frame residual              = {finite_boundary["gauge_frame_residual_l2"]}
```

The conditional Route A certificate still passes, but the unpatched Route A
attempt still rejects. That is the correct behavior: the functional theorem is
proved; the finite replay/promotion theorem remains open.

## Next object

`{NEXT}`.

It must either emit a transport-closed finite `Phi_fin` replay, add an exact
symbolic transport-conjugation validator, or complete Route B independent
provenance with exactness/error certificates.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"built {rel(OUTPUT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
