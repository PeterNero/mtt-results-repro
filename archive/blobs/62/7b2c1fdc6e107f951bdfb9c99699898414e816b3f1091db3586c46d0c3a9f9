"""Build CONST-EW-02 B31 clause-proof and row-packet frontier.

B31 imports the clause-level progress after B30's two-exit reduction: finite
Weyl trace measure and formal sector/Hessian assembly close as a subclaim, but
the strict source-promotion validator still rejects current support.  The
remaining payload is now minimal and explicit.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b31_clauseproof_and_rowpacket_frontier"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TRACE = BASE / "trace_assembly_subclause_import.packet.json"
PROMOTION = BASE / "strict_promotion_rejection_import.packet.json"
ROWPACKET = BASE / "honest_rowpacket_template_import.packet.json"
BOUNDARY = BASE / "weak_mixing_b31_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B31_ClauseProofAndRowPacketFrontier_v1.md"

STATUS = "MTT_CONST_EW_02_B31_CLAUSEPROOF_AND_ROWPACKET_FRONTIER_BUILT"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b30_path = DATA / "const_ew_02_weak_mixing_b30_source_identity_two_exit_reduction.candidate.json"
    b30_boundary_path = DATA / "const_ew_02_weak_mixing_b30_source_identity_two_exit_reduction" / "weak_mixing_b30_boundary.packet.json"
    b30_two_exit_path = DATA / "const_ew_02_weak_mixing_b30_source_identity_two_exit_reduction" / "two_exit_noncycle_frontier.packet.json"

    clause_candidate_path = SM / "candidate_data" / "selected_finitec1sourceidentityclauseproof_or_independentrowdataemission.candidate.json"
    trace_proof_path = SM / "candidate_data" / "selected_finitec1sourceidentityclauseproof_or_independentrowdataemission" / "finite_weyl_trace_assembly_clause_proof.packet.json"
    updated_gate_path = SM / "candidate_data" / "selected_finitec1sourceidentityclauseproof_or_independentrowdataemission" / "updated_source_identity_clause_gate.packet.json"
    clause_decision_path = SM / "candidate_data" / "selected_finitec1sourceidentityclauseproof_or_independentrowdataemission" / "clause_proof_or_row_data_decision.packet.json"
    independent_attempt_path = SM / "candidate_data" / "selected_finitec1sourceidentityclauseproof_or_independentrowdataemission" / "independent_row_data_emission_attempt.packet.json"

    promotion_candidate_path = SM / "candidate_data" / "selected_physicalsourcepromotionclauseproof_or_newindependentrowpacketfill.candidate.json"
    promotion_attempt_path = SM / "candidate_data" / "selected_physicalsourcepromotionclauseproof_or_newindependentrowpacketfill" / "physical_source_promotion_clause_attempt.packet.json"
    promotion_decision_path = SM / "candidate_data" / "selected_physicalsourcepromotionclauseproof_or_newindependentrowpacketfill" / "promotion_clause_or_new_rows_decision.packet.json"
    strict_validator_path = SM / "candidate_data" / "selected_physicalsourcepromotionclauseproof_or_newindependentrowpacketfill" / "strict_final_source_validator_result.packet.json"
    rowpacket_template_path = SM / "candidate_data" / "selected_physicalsourcepromotionclauseproof_or_newindependentrowpacketfill" / "new_independent_row_packet_fill_template.packet.json"

    b30 = load(b30_path)
    b30_boundary = load(b30_boundary_path)
    b30_two_exit = load(b30_two_exit_path)
    clause_candidate = load(clause_candidate_path)
    trace_proof = load(trace_proof_path)
    updated_gate = load(updated_gate_path)
    clause_decision = load(clause_decision_path)
    independent_attempt = load(independent_attempt_path)
    promotion_candidate = load(promotion_candidate_path)
    promotion_attempt = load(promotion_attempt_path)
    promotion_decision = load(promotion_decision_path)
    strict_validator = load(strict_validator_path)
    rowpacket_template = load(rowpacket_template_path)

    trace_packet = {
        "schema": "MTTConstEW02B31TraceAssemblySubclauseImport.v1",
        "status": "TRACE_ASSEMBLY_SUBCLAUSE_IMPORTED_CLOSED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B31-SOURCE-IDENTITY-CLAUSE-PROOF",
        "inputs": {
            "clause_candidate": rel(clause_candidate_path),
            "trace_proof": rel(trace_proof_path),
            "updated_gate": rel(updated_gate_path),
            "clause_decision": rel(clause_decision_path),
        },
        "closed_subclaim": trace_proof["proved_subclaim"],
        "not_closed_subclaim": trace_proof["not_proved_subclaim"],
        "updated_gate_status": updated_gate["status"],
        "clause_progress": clause_decision["clause_progress"],
        "source_identity_theorem_proved": clause_decision["source_identity_theorem_proved"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    promotion_packet = {
        "schema": "MTTConstEW02B31StrictPromotionRejectionImport.v1",
        "status": "STRICT_PROMOTION_REJECTED_AFTER_TRACE_ASSEMBLY",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B31-SOURCE-PROMOTION-VALIDATOR",
        "inputs": {
            "promotion_candidate": rel(promotion_candidate_path),
            "promotion_attempt": rel(promotion_attempt_path),
            "promotion_decision": rel(promotion_decision_path),
            "strict_final_source_validator_result": rel(strict_validator_path),
        },
        "what_closes_now": promotion_candidate["what_closes_now"],
        "strict_validator_ok": promotion_decision["strict_validator_ok"],
        "source_identity_theorem_proved": promotion_decision["source_identity_theorem_proved"],
        "new_independent_row_packet_emitted": promotion_decision["new_independent_row_packet_emitted"],
        "route_A_current": promotion_attempt["route_A_phifinc1_source_emission"],
        "route_B_current": promotion_attempt["route_B_independent_hessian_quadrature_source"],
        "remaining_minimal_payload": promotion_decision["remaining_minimal_payload"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    rowpacket = {
        "schema": "MTTConstEW02B31HonestRowPacketTemplateImport.v1",
        "status": "HONEST_ROWPACKET_TEMPLATE_IMPORTED_SOURCE_FIELDS_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B31-HONEST-KERNEL-EXPORT",
        "inputs": {
            "independent_attempt": rel(independent_attempt_path),
            "rowpacket_template": rel(rowpacket_template_path),
        },
        "current_postcheck_support": {
            "primitive_rows_available": independent_attempt["primitive_rows_available"],
            "primitive_values_exact": independent_attempt["primitive_values_exact"],
            "sector_rows_available_formally": independent_attempt["sector_rows_available_formally"],
            "hessian_rows_available_formally": independent_attempt["hessian_rows_available_formally"],
            "basis_source_certificate_available": independent_attempt["basis_source_certificate_available"],
        },
        "template_fields": rowpacket_template,
        "missing_for_export": {
            "primitive_source_integral_or_formula_independent": not rowpacket_template["primitive_rows"]["source_integral_or_formula_independent"],
            "same_source_b_selected_derivation": not rowpacket_template["hessian_source_rows"]["same_source_b_selected_derivation"],
            "residual_projector_replay_excluded_as_source": rowpacket_template["independence_certificate"]["residual_projector_replay_excluded_as_source"],
            "selected_source_identity_emitted": rowpacket_template["selected_source_identity"]["selected_emitted"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B31Boundary.v1",
        "status": "B31_TRACE_SUBCLAUSE_CLOSED_PROMOTION_AND_EXPORT_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B31-BOUNDARY",
        "previous_B30": {
            "candidate": b30["candidate"],
            "status": b30["status"],
            "two_exit_status": b30_two_exit["status"],
            "still_open": b30_boundary["still_open"],
        },
        "closed_or_sharpened_now": {
            "finite_trace_measure_equals_normalized_trace": trace_proof["proved_subclaim"]["finite_measure_equals_normalized_trace"],
            "formal_110_rows_executed": trace_proof["proved_subclaim"]["formal_110_rows_executed"],
            "sector_rows_assembled_formally": trace_proof["proved_subclaim"]["sector_rows_assembled_formally"],
            "hessian_source_rows_assembled_formally": trace_proof["proved_subclaim"]["hessian_source_rows_assembled_formally"],
            "strict_validator_rerun_after_trace_assembly": promotion_candidate["what_closes_now"]["strict_validator_rerun"],
            "new_row_packet_template_created": promotion_candidate["what_closes_now"]["new_row_packet_fill_template_created"],
        },
        "still_open": {
            "same_branch_phifin_c1_source_emission": True,
            "same_source_b_selected_emission": True,
            "source_independent_of_residual_projector_replay": True,
            "new_independent_selected_row_packet": True,
            "SelectedFiniteC1SourceIdentityTheorem_unpatched": True,
            "K_phys_or_f_ab": True,
            "mu_match": True,
            "RG_threshold_scheme": True,
            "physical_weak_angle_closure": True,
            "strict_full_no_knob_closure": True,
        },
        "anti_cycle_delta_from_B30": {
            "B30": "locked source identity or honest kernel export as the two exits",
            "B31": "closes the finite trace/assembly subclause and proves current promotion/export support still lacks source fields",
            "not_repeated": [
                "not another conditional validator pass",
                "not another B27-B29 row replay",
                "not a weak-angle target fit",
            ],
        },
        "allowed_claim": "B31 closes trace-measure/formal-assembly as a source-identity subclause and narrows remaining work to same-source Phi_fin/b emission or a genuinely independent row packet.",
        "forbidden_claim": "strict source promotion, independent row export, unpatched source identity, or physical weak-angle closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B31NextWork.v1",
        "status": "NEXT_WORKORDER_SAMESOURCE_EMISSION_OR_ACTUAL_ROWPACKET",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B32-SAMESOURCE-EMISSION-OR-ACTUAL-ROWPACKET",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B32-SAMESOURCE-PHIFIN-B-EMISSION",
            "task": "Prove same-branch physical Phi_fin^C1 source emission plus same-source b_selected/Hessian counterterm emission before residual replay.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B32-ACTUAL-INDEPENDENT-ROWPACKET",
            "task": "Fill the independent row-packet template with source integrals/formulae, source ids, exactness/error certificates, and an independence certificate excluding residual-projector replay.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB31ClauseProofAndRowPacketFrontier",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B31-SOURCE-IDENTITY-CLAUSE-PROOF-AND-HONEST-KERNEL-EXPORT",
        "output_packets": {
            "trace_assembly_subclause_import": rel(TRACE),
            "strict_promotion_rejection_import": rel(PROMOTION),
            "honest_rowpacket_template_import": rel(ROWPACKET),
            "weak_mixing_b31_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B31TraceAssemblySubclauseAndMinimalPayloadTheorem",
            "proved": True,
            "statement": (
                "The finite Weyl trace measure and formal 36 sector plus 2 Hessian/source row assembly are closed as a source-identity subclause. After importing this subclaim, the strict final-source validator still rejects current support and no independent row packet is emitted. Therefore the remaining weak-mixing C1 payload is minimal: same-source Phi_fin^C1/b_selected emission or an actual independent finite C1 row packet."
            ),
        },
        "trace_assembly_subclause_closed": True,
        "strict_promotion_validator_ok": False,
        "source_identity_theorem_proved_now": False,
        "new_independent_row_packet_emitted_now": False,
        "minimal_remaining_payload_locked": True,
        "anti_cycle_confirmed": True,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B31_ClauseProofAndRowPacketFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "trace_assembly_subclause_closed": True,
        "strict_promotion_validator_ok": False,
        "source_identity_theorem_proved_now": False,
        "new_independent_row_packet_emitted_now": False,
        "minimal_remaining_payload_locked": True,
        "anti_cycle_confirmed": True,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B31 Clause Proof And Row Packet Frontier v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B31-SOURCE-IDENTITY-CLAUSE-PROOF-AND-HONEST-KERNEL-EXPORT`

## Closed Now

```text
finite trace measure = normalized trace/Frobenius pairing  True
formal 110 rows executed                                      True
36 sector rows assembled formally                             True
2 Hessian/source rows assembled formally                       True
```

## Still Rejected

The strict final-source validator still rejects current support after this
subclaim is imported. The reason is no longer numerical exactness. It is source
provenance:

```text
same-branch Phi_fin^C1 source emission          open
same-source b_selected/Hessian emission         open
residual-projector replay excluded as source    open
actual independent row packet                   open
```

## Not A Cycle

B31 does not replay B27-B30. It closes one source-identity subclause and turns
the remaining problem into a minimal payload:

1. same-source `Phi_fin^C1` / `b_selected` emission, or
2. actual independent finite C1 row packet.

## Next

`CONST-EW-02 / WEAK-MIXING / B32-SAMESOURCE-EMISSION-OR-ACTUAL-ROWPACKET`
"""

    for path, payload in [
        (TRACE, trace_packet),
        (PROMOTION, promotion_packet),
        (ROWPACKET, rowpacket),
        (BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
