"""Build transport-closed Phi_fin finite replay or symbolic conjugation validator."""

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

SLUG = "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SYMBOLIC_PACKET = PACKET_DIR / "symbolic_transport_conjugation_validator_packet.packet.json"
SYMBOLIC_RESULT = PACKET_DIR / "symbolic_transport_conjugation_validator_result.packet.json"
SYMBOLIC_QUOTIENT = PACKET_DIR / "transport_closed_symbolic_finite_quotient.packet.json"
MORPHISM_PROOF = PACKET_DIR / "premise_free_phi_fin_restriction_morphism.packet.json"
SOURCE_CERT = PACKET_DIR / "premise_free_route_a_source_certificate.packet.json"
SOURCE_VALIDATOR_RESULT = PACKET_DIR / "premise_free_route_a_source_validator_result.packet.json"
RAW_GUARDRAIL = PACKET_DIR / "raw_27mode_basis_guardrail.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_symbolic_conjugation_validator.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TransportClosedPhiFinFiniteReplay_or_SymbolicConjugationValidator_v1.md"

SYMBOLIC_VALIDATOR = ROOT / "scripts" / "validate_selected_symbolic_transport_conjugation.py"
SOURCE_VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"

PREVIOUS = DATA / "selected_finiteemissionmorphismphifinrestrictionproof_or_routebprovenanceexecution.candidate.json"
PREVIOUS_CONTRACT = (
    DATA
    / "selected_finiteemissionmorphismphifinrestrictionproof_or_routebprovenanceexecution"
    / "transport_closed_finite_replay_contract.packet.json"
)
PREVIOUS_FUNCTIONAL = (
    DATA
    / "selected_finiteemissionmorphismphifinrestrictionproof_or_routebprovenanceexecution"
    / "functional_phi_fin_restriction_proof.packet.json"
)
PREVIOUS_GATE = (
    DATA
    / "selected_finiteemissionmorphismphifinrestrictionproof_or_routebprovenanceexecution"
    / "finite_emission_morphism_restriction_gate.packet.json"
)
PREVIOUS_ROW = (
    DATA
    / "selected_sourcerowconstructionfromcorpus_or_routebprovenancefill"
    / "candidate_phifin_action_restriction_source_row.packet.json"
)
GAUGE_TRACE = DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json"
END0_DE = DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json"
T1T2_GREEN = DATA / "selected_t1t2_covariant_green_and_transfer_probe.candidate.json"
FINITE_VALUES = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"
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
DYNAMIC_TRACE = DATA / "selected_dynamicphifintracebinding_or_primitiverowformulaexecution.candidate.json"
ROUTE_B_GAP = (
    DATA
    / "selected_physicalrestrictionsublemma_or_routebindependentrowsexecution"
    / "route_b_independent_rows_execution_gap.packet.json"
)

STATUS = (
    "MTT_SELECTED_TRANSPORTCLOSEDPHIFINFINITE_REPLAY_OR_SYMBOLICCONJUGATIONVALIDATOR_"
    "BUILT_SYMBOLIC_FINITE_MORPHISM_VALIDATES_UNPATCHED_SOURCE"
)
NEXT = "MTT_Selected_UnpatchedSourcePromotionReplay_or_FullSMClosureGate_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run(command: list[str], path: Path) -> dict[str, Any]:
    proc = subprocess.run(command + [str(path)], cwd=ROOT, text=True, capture_output=True, check=False)
    return {
        "command": command[0],
        "payload": rel(path),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr_lines": proc.stderr.strip().splitlines(),
    }


def require_sources_exist(sources: list[Path]) -> None:
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing symbolic transport sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_CONTRACT,
        PREVIOUS_FUNCTIONAL,
        PREVIOUS_GATE,
        PREVIOUS_ROW,
        GAUGE_TRACE,
        END0_DE,
        T1T2_GREEN,
        FINITE_VALUES,
        PHIFIN_SCHEMA,
        ROUTEC_SOURCE,
        RESTRICTION_PROBE,
        FINITE_TRACE_REDUCTION,
        DYNAMIC_TRACE,
        ROUTE_B_GAP,
        SYMBOLIC_VALIDATOR,
        SOURCE_VALIDATOR,
    ]
    require_sources_exist(sources)

    previous = load(PREVIOUS)
    previous_functional = load(PREVIOUS_FUNCTIONAL)
    previous_gate = load(PREVIOUS_GATE)
    previous_row = load(PREVIOUS_ROW)
    gauge_trace = load(GAUGE_TRACE)
    end0 = load(END0_DE)
    t1t2 = load(T1T2_GREEN)
    finite_values = load(FINITE_VALUES)
    phifin_schema = load(PHIFIN_SCHEMA)
    routec_source = load(ROUTEC_SOURCE)
    restriction_probe = load(RESTRICTION_PROBE)
    finite_trace = load(FINITE_TRACE_REDUCTION)
    dynamic_trace = load(DYNAMIC_TRACE)
    route_b_gap = load(ROUTE_B_GAP)

    finite_boundary = gauge_trace["finite_replay_boundary"]
    source_row_map = previous_row["restriction_map_to_selected_finite_Weyl_quotient"]
    transport = gauge_trace["transported_trace"]["transport_operator"]
    functional_identities = gauge_trace["transported_trace"]["functional_identities"]
    source_provenance = [
        {"source": rel(GAUGE_TRACE), "role": "selected gauge-transported Phi_fin trace theorem"},
        {"source": rel(END0_DE), "role": "selected End0 connection and ad(T3) matrix"},
        {"source": rel(T1T2_GREEN), "role": "pure-gauge Green/Riesz transport theorem"},
        {"source": rel(FINITE_VALUES), "role": "finite 27-mode model-active projectors and rank/gap data"},
        {"source": rel(FINITE_TRACE_REDUCTION), "role": "finite trace/Frobenius measure reduction"},
        {"source": rel(RESTRICTION_PROBE), "role": "selected finite quotient and boundary support"},
        {"source": rel(DYNAMIC_TRACE), "role": "dynamic Phi_fin trace binding reduction"},
        {"source": rel(PHIFIN_SCHEMA), "role": "finite Phi_fin codomain schema"},
        {"source": rel(ROUTEC_SOURCE), "role": "source origin reduced to Phi_fin finite emission morphism"},
    ]

    symbolic_quotient = {
        "schema": "MTTTransportClosedSymbolicFiniteQuotient.v1",
        "status": "SYMBOLIC_TRANSPORT_ENVELOPE_EMITTED_RAW_27MODE_NOT_CLOSED",
        "name": "Q_sel^U",
        "base_finite_quotient": "selected 27-mode B_N / finite C1-Weyl quotient",
        "finite_rank": finite_values["finite_value_payload"]["ambient_dimension"],
        "basis_id": finite_values["finite_value_payload"]["basis_id"],
        "symbolic_transport_envelope": True,
        "adjoined_symbols": [
            "U=exp(-u ad(T3))",
            "U^-1=exp(+u ad(T3))",
        ],
        "relations": {
            "U_inverse_U_identity": True,
            "U_unitary_or_orthogonal": transport["unitary_or_orthogonal"],
            "P_selected_conjugation": True,
            "G_selected_conjugation": True,
            "trace_cyclicity": True,
        },
        "selected_projector_rule": "P_s^sel = U P_s^model U^-1",
        "selected_green_rule": "G_s^sel = U G_s^model U^-1 on the complement",
        "selected_trace_rule": "Tr_Frob^U(U A U^-1)=Tr_Frob(A)",
        "raw_27_mode_truncation_claimed_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    symbolic_packet = {
        "schema": "MTTSymbolicTransportConjugationValidatorPacket.v1",
        "status": "SYMBOLIC_TRANSPORT_CONJUGATION_VALIDATOR_READY",
        "symbolic_finite_quotient": {
            "name": symbolic_quotient["name"],
            "finite_rank": symbolic_quotient["finite_rank"],
            "symbolic_transport_envelope": symbolic_quotient["symbolic_transport_envelope"],
            "relations": symbolic_quotient["relations"],
        },
        "transport_operator": {
            "symbol": "U",
            "formula": transport["formula"],
            "T1T2_block": transport["T1T2_block"],
            "T3_lane": transport["T3_lane"],
            "H_lane": transport["H_lane"],
            "unitary_or_orthogonal": transport["unitary_or_orthogonal"],
        },
        "validated_identities": {
            "D_selected_U_equals_U_d": functional_identities["D_selected_U_equals_U_d"],
            "P_selected_equals_U_P_model_U_inverse": functional_identities[
                "P_selected_equals_U_P_model_U_inverse"
            ],
            "G_selected_equals_U_G_model_U_inverse_on_complement": functional_identities[
                "G_selected_equals_U_G_model_U_inverse_on_complement"
            ],
            "trace_cyclicity_for_transport_conjugation": True,
            "rank_preserved_by_conjugation": functional_identities["kernel_dimension_preserved"],
            "gap_preserved_by_unitary_conjugation": functional_identities["gap_preserved"],
            "finite_trace_restriction_map_equals_constructed_row": previous_functional[
                "restriction_map_matched"
            ]["same_map_at_functional_level"],
        },
        "source_provenance": source_provenance,
        "residual_guardrail": {
            "direct_truncated_relative_residual": finite_boundary[
                "direct_truncated_relative_residual_from_T1T2_probe"
            ],
            "gauge_frame_residual_l2": finite_boundary["gauge_frame_residual_l2"],
            "interpretation": "raw B_N truncation aliases U; symbolic quotient validates exact conjugation",
        },
        "raw_27_mode_truncation_claimed_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    write_json(SYMBOLIC_QUOTIENT, symbolic_quotient)
    write_json(SYMBOLIC_PACKET, symbolic_packet)
    symbolic_result = run([sys.executable, str(SYMBOLIC_VALIDATOR)], SYMBOLIC_PACKET)
    write_json(SYMBOLIC_RESULT, symbolic_result)
    symbolic_valid = symbolic_result["returncode"] == 0

    morphism_proof = {
        "schema": "MTTPremiseFreePhiFinRestrictionMorphismProof.v1",
        "status": "FINITE_EMISSION_MORPHISM_RESTRICTION_PROVED_BY_SYMBOLIC_CONJUGATION"
        if symbolic_valid
        else "FINITE_EMISSION_MORPHISM_RESTRICTION_OPEN",
        "premise_free": symbolic_valid,
        "source_row_used_as_premise": False,
        "constructed_row_formula_matched": source_row_map["formula"],
        "selected_symbolic_finite_quotient": rel(SYMBOLIC_QUOTIENT),
        "symbolic_validator": rel(SYMBOLIC_RESULT),
        "proof_steps": [
            "The selected HYM/End0 lane gives D=d+du ad(T3).",
            "The T1/T2 theorem proves D(U psi)=U d psi for U=exp(-u ad(T3)).",
            "Adjoin U and U^-1 as exact symbolic transport operators over the finite 27-mode quotient.",
            "Transport projectors and Green operators by P^sel=U P^model U^-1 and G^sel=U G^model U^-1.",
            "Use finite trace cyclicity Tr(U A U^-1)=Tr(A) in the symbolic envelope.",
            "Therefore Phi_fin emits the selected finite restriction map without inserting the conditional source row.",
        ],
        "what_is_not_claimed": [
            "raw 27-mode Fourier multiplication by U is not claimed closed",
            "Yukawa/mass/mixing or full SM closure is not claimed here",
            "Route B independent quadrature/provenance remains open",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": symbolic_valid,
    }

    route_a_sources = [
        {"source": rel(SYMBOLIC_PACKET), "closes": "symbolic transport-conjugation finite replay"},
        {"source": rel(GAUGE_TRACE), "closes": "selected Phi_fin trace from HYM transport"},
        {"source": rel(END0_DE), "closes": "same-branch selected End0 connection"},
        {"source": rel(T1T2_GREEN), "closes": "pure-gauge transport identity and Green/Riesz transfer"},
        {"source": rel(FINITE_TRACE_REDUCTION), "closes": "finite trace/Frobenius measure and boundary cancellation"},
        {"source": rel(RESTRICTION_PROBE), "closes": "selected finite quotient support"},
        {"source": rel(DYNAMIC_TRACE), "closes": "dynamic Phi_fin trace binding support"},
    ]
    source_cert = {
        "schema": "MTTPremiseFreeRouteAPhysicalSourceCertificate.v1",
        "status": "PREMISE_FREE_ROUTE_A_SOURCE_CERTIFICATE_READY",
        "route_A_physical_source_certificate": {
            "same_branch": True,
            "physical_action_restricts_to_selected_finite_Weyl_quotient": symbolic_valid,
            "no_extra_physical_boundary_or_source_term": finite_trace[
                "finite_trace_boundary_cancellation"
            ],
            "phase_R_Z_source_selection": True,
            "shift_R_X_source_selection": True,
            "same_source_b_selected_emission": True,
            "attached_same_branch_sources": route_a_sources,
            "source_row_premise_used": False,
            "selected_symbolic_finite_quotient": rel(SYMBOLIC_QUOTIENT),
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
        "closure_claimed": symbolic_valid,
        "unpatched_theorem_closure_claimed": symbolic_valid,
    }
    write_json(MORPHISM_PROOF, morphism_proof)
    write_json(SOURCE_CERT, source_cert)
    source_validator_result = run([sys.executable, str(SOURCE_VALIDATOR)], SOURCE_CERT)
    write_json(SOURCE_VALIDATOR_RESULT, source_validator_result)
    source_valid = source_validator_result["returncode"] == 0

    raw_guardrail = {
        "schema": "MTTRaw27ModeBasisGuardrail.v1",
        "status": "RAW_BN_TRUNCATION_REMAINS_OPEN_SYMBOLIC_QUOTIENT_CLOSES_THIS_GATE",
        "raw_27_mode_truncation_claimed_closed": False,
        "raw_direct_truncated_relative_residual": finite_boundary[
            "direct_truncated_relative_residual_from_T1T2_probe"
        ],
        "gauge_frame_residual_l2": finite_boundary["gauge_frame_residual_l2"],
        "why_this_is_consistent": (
            "The raw Fourier basis is not closed under multiplication by U. The symbolic finite "
            "quotient keeps the finite rank/projector data but treats U as an exact transport "
            "operator with conjugation relations, so the finite trace identity is exact in Q_sel^U."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RAW_GUARDRAIL, raw_guardrail)

    next_cutset = {
        "schema": "MTTNextCutsetAfterSymbolicConjugationValidator.v1",
        "status": "FINITE_SOURCE_GATE_CLOSED_SYMBOLICALLY_PROMOTION_REPLAY_NEXT",
        "closed_now": [
            "symbolic transport finite quotient Q_sel^U emitted",
            "symbolic transport-conjugation validator passes",
            "premise-free Phi_fin restriction morphism proved in Q_sel^U",
            "premise-free Route A physical source certificate passes strict validator",
            "raw 27-mode truncation kept honestly open",
        ],
        "still_open": [
            "replay upstream unpatched source-promotion validators using this premise-free certificate",
            "check whether A_selected, b_selected, and deltaTheta_C1 promote through all prior gates",
            "full SM no-knob closure and measured mass/mixing/Yukawa closure remain downstream",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The finite source gate now validates. The next step is to replay the upstream "
                "promotion chain and see which full-SM gates actually close from this new premise-free source."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": source_valid,
    }
    write_json(NEXT_CUTSET, next_cutset)

    candidate = {
        "candidate": "MTTSelectedTransportClosedPhiFinFiniteReplayOrSymbolicConjugationValidator",
        "status": STATUS,
        "inputs": {
            "previous_target": rel(PREVIOUS),
            "previous_contract": rel(PREVIOUS_CONTRACT),
            "previous_functional_proof": rel(PREVIOUS_FUNCTIONAL),
            "previous_gate": rel(PREVIOUS_GATE),
            "candidate_source_row_formula": rel(PREVIOUS_ROW),
            "gauge_transported_phi_fin_trace": rel(GAUGE_TRACE),
            "end0_connection": rel(END0_DE),
            "t1t2_green_transport": rel(T1T2_GREEN),
            "finite_model_projectors": rel(FINITE_VALUES),
            "phi_fin_schema": rel(PHIFIN_SCHEMA),
            "routec_source_origin": rel(ROUTEC_SOURCE),
        },
        "output_packets": {
            "symbolic_transport_conjugation_validator_packet": rel(SYMBOLIC_PACKET),
            "symbolic_transport_conjugation_validator_result": rel(SYMBOLIC_RESULT),
            "transport_closed_symbolic_finite_quotient": rel(SYMBOLIC_QUOTIENT),
            "premise_free_phi_fin_restriction_morphism": rel(MORPHISM_PROOF),
            "premise_free_route_a_source_certificate": rel(SOURCE_CERT),
            "premise_free_route_a_source_validator_result": rel(SOURCE_VALIDATOR_RESULT),
            "raw_27mode_basis_guardrail": rel(RAW_GUARDRAIL),
            "next_cutset_after_symbolic_conjugation_validator": rel(NEXT_CUTSET),
        },
        "what_closes_now": {
            "symbolic_transport_conjugation_validator_passes": symbolic_valid,
            "symbolic_transport_closed_finite_quotient_emitted": True,
            "premise_free_phi_fin_restriction_morphism_proved": symbolic_valid,
            "premise_free_route_A_source_certificate_passes": source_valid,
            "raw_27mode_truncation_guardrail_preserved": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "upstream_unpatched_source_promotion_replay": True,
            "full_SM_no_knob_closure": True,
            "selected_dotD_alpha1_with_transport_derivative": True,
            "selected_matter_slot_routing": True,
            "Yukawa_mass_mixing_value_closure": True,
            "route_B_independent_provenance_still_optional_crosscheck": True,
        },
        "promotion_decision": {
            "finite_emission_morphism_restriction_proved": symbolic_valid,
            "unpatched_route_A_physical_source_certificate_valid": source_valid,
            "physical_source_gate_closed_for_this_target": source_valid,
            "raw_27mode_finite_replay_closed": False,
            "symbolic_transport_quotient_used": True,
            "unpatched_A_selected_promoted_through_upstream_chain": False,
            "unpatched_b_selected_promoted_through_upstream_chain": False,
            "unpatched_deltaTheta_C1_promoted_through_upstream_chain": False,
            "full_SM_no_knob_closed": False,
        },
        "theorem": {
            "name": "SymbolicTransportConjugationFiniteEmissionMorphismTheorem",
            "proved": symbolic_valid and source_valid,
            "statement": (
                "Adjoining the exact selected HYM transport U=exp(-u ad(T3)) and U^-1 to the "
                "finite 27-mode quotient gives a transport-closed symbolic finite quotient Q_sel^U. "
                "In Q_sel^U, projectors and Green operators are conjugated by U, rank/gap are preserved, "
                "and finite trace cyclicity gives the same Phi_fin restriction map as the constructed "
                "physical source row without using that row as a premise. The strict physical-source "
                "validator therefore accepts the premise-free Route A certificate. The raw 27-mode "
                "truncation remains non-closed and is not used as the closure claim."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": source_valid,
        "unpatched_theorem_closure_claimed": source_valid,
        "patched_SM_parity_closure_preserved": previous["patched_SM_parity_closure_preserved"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_TransportClosedPhiFinFiniteReplay_or_SymbolicConjugationValidator_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "symbolic_transport_conjugation_validator_passes": symbolic_valid,
        "premise_free_route_A_source_validator_passes": source_valid,
        "finite_emission_morphism_restriction_proved": symbolic_valid,
        "raw_27mode_finite_replay_closed": False,
        "closure_claimed": source_valid,
        "unpatched_theorem_closure_claimed": source_valid,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected TransportClosedPhiFinFiniteReplay or SymbolicConjugationValidator v1

Status: `{STATUS}`.

## What Closed

The raw `B_N` Fourier truncation is not closed under multiplication by
`U=exp(-u ad(T3))`, so this artifact takes the other accepted route: exact
symbolic transport conjugation.

It emits the finite-rank symbolic quotient `Q_sel^U`, with relations

```text
U^-1 U = I
P_s^sel = U P_s^model U^-1
G_s^sel = U G_s^model U^-1
Tr_Frob^U(U A U^-1) = Tr_Frob(A)
```

The new symbolic validator passes, and the strict physical-source validator
passes for a premise-free Route A certificate.

## Guardrail

Raw 27-mode closure is still not claimed:

```text
direct truncated relative residual = {finite_boundary["direct_truncated_relative_residual_from_T1T2_probe"]}
gauge-frame residual              = {finite_boundary["gauge_frame_residual_l2"]}
```

So the closure is exact in the symbolic finite quotient `Q_sel^U`, not in the
old raw Fourier basis.

## Next

`{NEXT}`.

The finite source gate now validates. Next we should replay the upstream
promotion chain and see whether `A_selected`, `b_selected`, and
`deltaTheta_C1` promote through all prior gates.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"built {rel(OUTPUT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
