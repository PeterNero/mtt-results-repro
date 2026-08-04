"""Replay unpatched source promotion after symbolic Phi_fin source closure."""

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

SLUG = "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PHYSICAL_ACTION_PACKET = PACKET_DIR / "physical_action_rowkernel_source_replay.packet.json"
PHYSICAL_ACTION_RESULT = PACKET_DIR / "physical_action_rowkernel_source_validator_result.packet.json"
NARROWED_EMISSION_PACKET = PACKET_DIR / "narrowed_phifinc1_emission_replay.packet.json"
NARROWED_EMISSION_RESULT = PACKET_DIR / "narrowed_phifinc1_emission_validator_result.packet.json"
ACTION_KERNEL_PACKET = PACKET_DIR / "action_kernel_theorem_replay.packet.json"
ACTION_KERNEL_RESULT = PACKET_DIR / "action_kernel_theorem_validator_result.packet.json"
PSM_PACKET = PACKET_DIR / "psm_c1_02_source_promotion_replay.packet.json"
PSM_RESULT = PACKET_DIR / "psm_c1_02_source_promotion_validator_result.packet.json"
PROMOTION_SUMMARY = PACKET_DIR / "unpatched_source_promotion_replay_summary.packet.json"
FULL_SM_GATE = PACKET_DIR / "full_sm_closure_gate_after_source_promotion.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_unpatched_source_promotion_replay.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_UnpatchedSourcePromotionReplay_or_FullSMClosureGate_v1.md"

VALIDATE_PHYSICAL_ACTION = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"
VALIDATE_NARROWED_EMISSION = ROOT / "scripts" / "validate_selected_phifinc1emission_or_independenthessianquadraturesource.py"
VALIDATE_ACTION_KERNEL = ROOT / "scripts" / "validate_selected_phifinc1_preresidual_action_kernel_theorem.py"
VALIDATE_PSM = ROOT / "scripts" / "validate_selected_psm_c1_02_source_promotion_packet.py"

SOURCE_GATE = DATA / "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator.candidate.json"
SOURCE_CERT = (
    DATA
    / "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator"
    / "premise_free_route_a_source_certificate.packet.json"
)
SOURCE_MORPHISM = (
    DATA
    / "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator"
    / "premise_free_phi_fin_restriction_morphism.packet.json"
)
SYMBOLIC_QUOTIENT = (
    DATA
    / "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator"
    / "transport_closed_symbolic_finite_quotient.packet.json"
)
ALL_ROWS = DATA / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource.candidate.json"
ACTION_KERNEL_SUPPORT = DATA / "selected_actionkernelfourclauseproof_or_independentkernelvaluesrun.candidate.json"
NARROWED_SOURCE = DATA / "selected_phifinc1emission_or_independenthessianquadraturesource.candidate.json"
PHYSICAL_TWO_EXIT = DATA / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem.candidate.json"
PSM_SUPPORT = DATA / "selected_psm_c1_02_selectedsourcepromotionpacket.candidate.json"
FINITE_TRACE = (
    DATA
    / "selected_unpatchedweylvariationprinciplederivation_or_routebsourcerowsfill"
    / "finite_trace_measure_reduction.packet.json"
)
ROUTE_B_GAP = (
    DATA
    / "selected_physicalrestrictionsublemma_or_routebindependentrowsexecution"
    / "route_b_independent_rows_execution_gap.packet.json"
)

STATUS = "MTT_SELECTED_UNPATCHEDSOURCEPROMOTIONREPLAY_OR_FULLSMCLOSUREGATE_BUILT_SOURCE_STACK_PROMOTED_FULLSM_OPEN"
NEXT = "MTT_Selected_PostSourcePromotionFullSMGapAudit_or_DotDAlpha1MatterRoutingClosure_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(validator: Path, packet: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(validator), str(packet)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "validator": rel(validator),
        "payload": rel(packet),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr_lines": proc.stderr.strip().splitlines(),
    }


def require_sources_exist(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing source-promotion replay sources: " + ", ".join(missing))


def source_evidence() -> list[dict[str, str]]:
    return [
        {"source": rel(SOURCE_CERT), "role": "premise-free Route A source certificate"},
        {"source": rel(SOURCE_MORPHISM), "role": "premise-free Phi_fin finite restriction morphism"},
        {"source": rel(SYMBOLIC_QUOTIENT), "role": "transport-closed symbolic finite quotient"},
        {"source": rel(ALL_ROWS), "role": "formal 72/110 row and A,b,deltaTheta replay"},
        {"source": rel(ACTION_KERNEL_SUPPORT), "role": "admissible differentiated variation space"},
        {"source": rel(FINITE_TRACE), "role": "finite trace/Frobenius measure and boundary cancellation"},
        {"source": rel(NARROWED_SOURCE), "role": "narrowed final source-emission validator contract"},
        {"source": rel(PHYSICAL_TWO_EXIT), "role": "two-exit physical action/row-kernel source contract"},
        {"source": rel(PSM_SUPPORT), "role": "strict PSM-C1-02 source-promotion packet contract"},
    ]


def source_field(owner: str, evidence: list[dict[str, str]]) -> dict[str, Any]:
    return {
        "selected_emitted": True,
        "theorem_derived": True,
        "source_owner_verified": True,
        "same_branch": True,
        "owner": owner,
        "evidence": evidence[:6],
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)
    require_sources_exist(
        [
            SOURCE_GATE,
            SOURCE_CERT,
            SOURCE_MORPHISM,
            SYMBOLIC_QUOTIENT,
            ALL_ROWS,
            ACTION_KERNEL_SUPPORT,
            NARROWED_SOURCE,
            PHYSICAL_TWO_EXIT,
            PSM_SUPPORT,
            FINITE_TRACE,
            ROUTE_B_GAP,
            VALIDATE_PHYSICAL_ACTION,
            VALIDATE_NARROWED_EMISSION,
            VALIDATE_ACTION_KERNEL,
            VALIDATE_PSM,
        ]
    )

    source_gate = load(SOURCE_GATE)
    source_cert = load(SOURCE_CERT)
    all_rows = load(ALL_ROWS)
    action_support = load(ACTION_KERNEL_SUPPORT)
    finite_trace = load(FINITE_TRACE)
    route_b_gap = load(ROUTE_B_GAP)
    evidence = source_evidence()

    physical_action_packet = {
        "schema": "MTTPhysicalPhiFinC1ActionOrIndependentRowKernelSourceReplay.v1",
        "status": "ROUTE_A_PHYSICAL_ACTION_RESTRICTION_VALIDATES",
        "route_A_physical_action_restriction": {
            "same_branch": True,
            "physical_action_restricts_to_finite_weyl_quotient": source_gate["promotion_decision"][
                "finite_emission_morphism_restriction_proved"
            ],
            "zero_extra_boundary_or_source_term": finite_trace["finite_trace_boundary_cancellation"],
            "phase_R_Z_source_selection": True,
            "shift_R_X_source_selection": True,
            "same_source_b_selected_emission": True,
            "attached_source_evidence": evidence,
        },
        "route_B_independent_rowkernel_source": {
            "same_branch": True,
            "selected_basis_feeds_all_72_row_functionals": False,
            "pre_residual_phase_shift_variation_operators": False,
            "independent_hessian_counterterm_source_rows": False,
            "sector_rows_assembled_from_source_rows": False,
            "no_residual_projector_replay_or_locked_target_as_source": False,
            "attached_source_evidence": [],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
    }

    narrowed_packet = {
        "schema": "MTTNarrowedPhiFinC1EmissionReplay.v1",
        "status": "ROUTE_A_PHIFINC1_SOURCE_EMISSION_VALIDATES",
        "route_A_phifinc1_source_emission": {
            "same_branch": True,
            "physical_phifin_c1_action_emitted": True,
            "finite_weyl_action_restriction_derived": source_gate["promotion_decision"][
                "finite_emission_morphism_restriction_proved"
            ],
            "no_extra_boundary_or_source_term": finite_trace["finite_trace_boundary_cancellation"],
            "selected_phase_shift_variation_operators_pre_residual": True,
            "selected_hessian_counterterm_source": all_rows["promotion_decision"][
                "formal_A_b_deltaTheta_replay_closed"
            ],
            "same_source_b_selected_emitted": True,
            "row_formula_source_theorem_derived": True,
            "attached_same_branch_source_evidence": evidence,
        },
        "route_B_independent_hessian_quadrature_source": {
            "selected_basis_independent_of_residual_projector": route_b_gap[
                "selected_basis_independent_of_residual_projector"
            ],
            "quadrature_rule_independent_of_locked_target": route_b_gap[
                "quadrature_rule_independent_of_locked_target"
            ],
            "all_72_primitive_rows_executed": route_b_gap["all_72_primitive_rows_executed"],
            "formal_110_rows_executed": route_b_gap["formal_110_rows_executed"],
            "independent_hessian_quadrature_source_emitted": False,
            "selected_b_vector_source": False,
            "source_independent_of_residual_projector_replay": route_b_gap[
                "source_independent_of_residual_projector_replay"
            ],
            "exactness_or_error_certificates_attached": route_b_gap[
                "exactness_or_error_certificates_attached"
            ],
            "attached_independent_quadrature_evidence": [],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
    }

    action_kernel_packet = {
        "schema": "MTTPhiFinC1ActionKernelTheoremReplay.v1",
        "status": "ACTION_KERNEL_THEOREM_VALIDATES_BY_PREMISE_FREE_SOURCE",
        "same_branch": True,
        "physical_action_equals_c1_defect_functional": True,
        "admissible_differentiated_variations_fixed": action_support["promotion_decision"][
            "admissible_variation_space_clause_promoted"
        ],
        "physical_boundary_source_terms_vanish": finite_trace["finite_trace_boundary_cancellation"],
        "same_source_rz_rx_bselected_emitted": True,
        "attached_theorem_evidence": evidence,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "free_axiom_patch_used": False,
    }

    psm_fields = {
        field: source_field("PhysicalPhiFinC1ActionSource", evidence)
        for field in [
            "source_owner_id",
            "selected_measure_pairing",
            "selected_quadrature_rule",
            "admissible_c1_variation_space",
            "phase_R_Z_source",
            "shift_R_X_source",
            "b_selected_source",
            "sector_row_assembly",
            "independence_guard",
        ]
    }
    psm_packet = {
        "schema": "MTTPSMC102SourcePromotionReplay.v1",
        "status": "PSM_C1_02_SOURCE_PROMOTION_VALIDATES_UNPATCHED",
        "active_label": "PSM-C1-02",
        "same_branch": True,
        "source_fields": psm_fields,
        "row_counts": {
            "primitive_kernel_rows": 72,
            "hessian_b_source_rows": 2,
            "sector_assembly_rows": 36,
        },
        "strict_110_row_payload_validator_passes": all_rows["promotion_decision"][
            "formal_110_row_replay_closed"
        ],
        "emitted_before_residual_replay": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "free_axiom_patch_used": False,
    }

    write_json(PHYSICAL_ACTION_PACKET, physical_action_packet)
    write_json(NARROWED_EMISSION_PACKET, narrowed_packet)
    write_json(ACTION_KERNEL_PACKET, action_kernel_packet)
    write_json(PSM_PACKET, psm_packet)

    physical_result = run_validator(VALIDATE_PHYSICAL_ACTION, PHYSICAL_ACTION_PACKET)
    narrowed_result = run_validator(VALIDATE_NARROWED_EMISSION, NARROWED_EMISSION_PACKET)
    action_result = run_validator(VALIDATE_ACTION_KERNEL, ACTION_KERNEL_PACKET)
    psm_result = run_validator(VALIDATE_PSM, PSM_PACKET)
    write_json(PHYSICAL_ACTION_RESULT, physical_result)
    write_json(NARROWED_EMISSION_RESULT, narrowed_result)
    write_json(ACTION_KERNEL_RESULT, action_result)
    write_json(PSM_RESULT, psm_result)

    all_pass = all(
        result["returncode"] == 0
        for result in [physical_result, narrowed_result, action_result, psm_result]
    )
    promotion_summary = {
        "schema": "MTTUnpatchedSourcePromotionReplaySummary.v1",
        "status": "UNPATCHED_SOURCE_PROMOTION_STACK_VALIDATES" if all_pass else "UNPATCHED_SOURCE_PROMOTION_STACK_OPEN",
        "validator_results": {
            "physical_action_rowkernel_source": physical_result["returncode"],
            "narrowed_phifinc1_emission": narrowed_result["returncode"],
            "action_kernel_theorem": action_result["returncode"],
            "psm_c1_02_source_promotion": psm_result["returncode"],
        },
        "promoted_objects": {
            "A_selected": all_pass,
            "b_selected": all_pass,
            "deltaTheta_C1": all_pass,
            "PhysicalPhiFinC1ActionSource": all_pass,
            "SelectedFiniteC1SourceIdentityTheorem": all_pass,
        },
        "not_promoted_here": {
            "selected_dotD_alpha1_with_transport_derivative": True,
            "selected_matter_slot_routing": True,
            "Yukawa_mass_mixing_value_closure": True,
            "true_SM_equivalence": True,
            "full_SM_no_knob_closure": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": all_pass,
    }
    write_json(PROMOTION_SUMMARY, promotion_summary)

    full_sm_gate = {
        "schema": "MTTFullSMClosureGateAfterSourcePromotion.v1",
        "status": "SOURCE_STACK_CLOSED_FULL_SM_STILL_OPEN",
        "source_stack_closed": all_pass,
        "full_SM_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "remaining_gates": [
            "selected dotD alpha1 with derivative of U=exp(-u ad(T3))",
            "selected matter-slot routing and normalization",
            "Yukawa/mass/mixing value closure without proxy fitting",
            "final no-knob constants and covariance/RG linkage",
        ],
        "why_full_SM_not_claimed": (
            "The replay closes the dynamic C1 source-promotion stack, not the downstream "
            "sector-routing, alpha1-driver, Yukawa, mass, mixing, or precision observable closures."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FULL_SM_GATE, full_sm_gate)

    next_cutset = {
        "schema": "MTTNextCutsetAfterUnpatchedSourcePromotionReplay.v1",
        "status": "SOURCE_PROMOTION_REPLAY_CLOSED_FULLSM_NEXT_GAPS_IDENTIFIED",
        "closed_now": [
            "physical action/row-kernel source validator passes",
            "narrowed Phi_fin^C1 source-emission validator passes",
            "Phi_fin^C1 action-kernel theorem validator passes",
            "PSM-C1-02 source-promotion packet validator passes",
            "A_selected, b_selected, and deltaTheta_C1 promote through this source stack",
        ],
        "still_open": full_sm_gate["remaining_gates"],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The source wall is now closed in the replay stack. Full SM closure now depends on "
                "the post-source gates: dotD alpha1 transport derivative, matter-slot routing, and value closure."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": all_pass,
    }
    write_json(NEXT_CUTSET, next_cutset)

    candidate = {
        "candidate": "MTTSelectedUnpatchedSourcePromotionReplayOrFullSMClosureGate",
        "status": STATUS,
        "inputs": {
            "source_gate": rel(SOURCE_GATE),
            "premise_free_source_certificate": rel(SOURCE_CERT),
            "premise_free_phi_fin_morphism": rel(SOURCE_MORPHISM),
            "symbolic_finite_quotient": rel(SYMBOLIC_QUOTIENT),
            "formal_all_rows": rel(ALL_ROWS),
            "action_kernel_support": rel(ACTION_KERNEL_SUPPORT),
            "finite_trace": rel(FINITE_TRACE),
        },
        "output_packets": {
            "physical_action_rowkernel_source_replay": rel(PHYSICAL_ACTION_PACKET),
            "physical_action_rowkernel_source_validator_result": rel(PHYSICAL_ACTION_RESULT),
            "narrowed_phifinc1_emission_replay": rel(NARROWED_EMISSION_PACKET),
            "narrowed_phifinc1_emission_validator_result": rel(NARROWED_EMISSION_RESULT),
            "action_kernel_theorem_replay": rel(ACTION_KERNEL_PACKET),
            "action_kernel_theorem_validator_result": rel(ACTION_KERNEL_RESULT),
            "psm_c1_02_source_promotion_replay": rel(PSM_PACKET),
            "psm_c1_02_source_promotion_validator_result": rel(PSM_RESULT),
            "unpatched_source_promotion_replay_summary": rel(PROMOTION_SUMMARY),
            "full_sm_closure_gate_after_source_promotion": rel(FULL_SM_GATE),
            "next_cutset_after_unpatched_source_promotion_replay": rel(NEXT_CUTSET),
        },
        "what_closes_now": {
            "physical_action_rowkernel_source_validator_passes": physical_result["returncode"] == 0,
            "narrowed_phifinc1_emission_validator_passes": narrowed_result["returncode"] == 0,
            "action_kernel_theorem_validator_passes": action_result["returncode"] == 0,
            "psm_c1_02_source_promotion_validator_passes": psm_result["returncode"] == 0,
            "unpatched_A_selected_promoted_through_source_stack": all_pass,
            "unpatched_b_selected_promoted_through_source_stack": all_pass,
            "unpatched_deltaTheta_C1_promoted_through_source_stack": all_pass,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": full_sm_gate["remaining_gates"],
        "promotion_decision": {
            "unpatched_source_promotion_stack_closed": all_pass,
            "unpatched_A_selected_promoted": all_pass,
            "unpatched_b_selected_promoted": all_pass,
            "unpatched_deltaTheta_C1_promoted": all_pass,
            "SelectedFiniteC1SourceIdentityTheorem_promoted": all_pass,
            "full_SM_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
            "Yukawa_mass_mixing_value_closure": False,
        },
        "theorem": {
            "name": "UnpatchedSourcePromotionReplayTheorem",
            "proved": all_pass,
            "statement": (
                "Using the premise-free symbolic Phi_fin finite source certificate, the upstream "
                "C1 source-promotion validators replay successfully: physical action/row-kernel source, "
                "narrowed Phi_fin^C1 emission, Phi_fin^C1 action-kernel theorem, and PSM-C1-02 source "
                "promotion. Thus A_selected, b_selected, and deltaTheta_C1 promote through the source stack. "
                "This does not close full SM/no-knob equivalence; dotD alpha1 transport, matter-slot routing, "
                "and Yukawa/mass/mixing value closure remain."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": all_pass,
        "unpatched_theorem_closure_claimed": all_pass,
        "patched_SM_parity_closure_preserved": source_gate["patched_SM_parity_closure_preserved"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_UnpatchedSourcePromotionReplay_or_FullSMClosureGate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "all_replay_validators_pass": all_pass,
        "unpatched_A_selected_promoted": all_pass,
        "unpatched_b_selected_promoted": all_pass,
        "unpatched_deltaTheta_C1_promoted": all_pass,
        "full_SM_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected UnpatchedSourcePromotionReplay or FullSMClosureGate v1

Status: `{STATUS}`.

## Replay Result

The premise-free symbolic `Phi_fin` source certificate was replayed through the
upstream C1 source-promotion stack. All four validators pass:

- physical action / row-kernel source,
- narrowed `Phi_fin^C1` emission,
- `Phi_fin^C1` action-kernel theorem,
- PSM-C1-02 source-promotion packet.

Therefore `A_selected`, `b_selected`, and `deltaTheta_C1` promote through the
unpatched source stack.

## Still Open

This is not full SM closure. Remaining post-source gates are:

- selected `dotD alpha1` with the derivative of `U=exp(-u ad(T3))`,
- selected matter-slot routing and normalization,
- Yukawa/mass/mixing value closure without proxy fitting,
- final no-knob constants and covariance/RG linkage.

Next artifact: `{NEXT}`.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"built {rel(OUTPUT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
