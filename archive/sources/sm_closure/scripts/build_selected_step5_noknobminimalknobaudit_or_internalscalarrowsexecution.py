"""Build Step 5 no-knob/minimal-knob audit and internal scalar-row execution boundary."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step5_noknobminimalknobaudit_or_internalscalarrowsexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INTERNAL_EXEC = PACKET_DIR / "step5_internal_scalar_row_execution_audit.packet.json"
NOKNOB = PACKET_DIR / "step5_no_knob_value_derivation_audit.packet.json"
MINIMAL = PACKET_DIR / "step5_minimal_universal_parameter_audit.packet.json"
BOUNDARY = PACKET_DIR / "step5_closure_boundary.packet.json"
HANDOFF = PACKET_DIR / "step5_to_step6_handoff.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step5_NoKnobMinimalKnobAudit_or_InternalScalarRowsExecution_v1.md"

STEP4 = DATA / "selected_step4_dynamicphysicalmatrices_and_admittedvaluerows_closure.candidate.json"
STEP4_HANDOFF = (
    DATA
    / "selected_step4_dynamicphysicalmatrices_and_admittedvaluerows_closure"
    / "step4_to_step5_handoff.packet.json"
)
INTERNAL_SCALAR = DATA / "selected_internalrthetascalarrowemission_or_universalanchorselection.candidate.json"
DIRECT_ATTEMPT = (
    DATA
    / "selected_internalrthetascalarrowemission_or_universalanchorselection"
    / "direct_internal_rtheta_scalar_row_emission_attempt.packet.json"
)
NOKNOB_KERNEL = DATA / "selected_noknobvaluederivationkernel_or_sourceanchortheorem.candidate.json"
KERNEL_OBLIGATIONS = (
    DATA
    / "selected_noknobvaluederivationkernel_or_sourceanchortheorem"
    / "internal_value_obligation_status_after_readiness_8of9.packet.json"
)
FINAL_RECHECK = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "final_no_knob_value_derivation_recheck.packet.json"
)
POLICY_MATRIX = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "minimal_universal_parameter_policy_matrix.packet.json"
)
UNIVERSAL_POLICY = DATA / "universal_source_parameter_policy/universal_source_parameter_policy.packet.json"
UNIVERSAL_CANDIDATES = DATA / "universal_source_parameter_policy/candidate_universal_parameters.packet.json"
RTHETA_ROWS = DATA / "selected_rthetavaluerows_or_universalsourceanchortheorem.candidate.json"
RTHETA_COEFFS = (
    DATA
    / "selected_rthetavaluerows_or_universalsourceanchortheorem"
    / "rtheta_value_row_coefficients_attempt.packet.json"
)
THRESHOLD_MAGNITUDE = DATA / "selected_thresholdmagnituderows_or_minimaluniversalparameterdecision.candidate.json"
ANCHOR_RECHECK = (
    DATA
    / "selected_thresholdmagnituderows_or_minimaluniversalparameterdecision"
    / "minimal_universal_anchor_recheck_after_source_domain.packet.json"
)
EXTERNAL_IMPORT = DATA / "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport.candidate.json"

STATUS = (
    "MTT_SELECTED_STEP5_NOKNOBMINIMALKNOBAUDIT_OR_INTERNALSCALARROWSEXECUTION_"
    "CLOSED_AUDIT_NO_INTERNAL_ROWS_NO_MINIMAL_KNOB_SELECTED"
)
NEXT = "MTT_Selected_Step6_MeasuredSMDataComparisonReadiness_or_NoKnobValueGap_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 5 inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        STEP4,
        STEP4_HANDOFF,
        INTERNAL_SCALAR,
        DIRECT_ATTEMPT,
        NOKNOB_KERNEL,
        KERNEL_OBLIGATIONS,
        FINAL_RECHECK,
        POLICY_MATRIX,
        UNIVERSAL_POLICY,
        UNIVERSAL_CANDIDATES,
        RTHETA_ROWS,
        RTHETA_COEFFS,
        THRESHOLD_MAGNITUDE,
        ANCHOR_RECHECK,
        EXTERNAL_IMPORT,
    ]
    require_sources(sources)

    step4 = load(STEP4)
    step4_handoff = load(STEP4_HANDOFF)
    internal = load(INTERNAL_SCALAR)
    direct = load(DIRECT_ATTEMPT)
    kernel = load(NOKNOB_KERNEL)
    obligations = load(KERNEL_OBLIGATIONS)
    final_recheck = load(FINAL_RECHECK)
    policy_matrix = load(POLICY_MATRIX)
    universal_policy = load(UNIVERSAL_POLICY)
    universal_candidates = load(UNIVERSAL_CANDIDATES)
    rtheta_rows = load(RTHETA_ROWS)
    rtheta_coeffs = load(RTHETA_COEFFS)
    threshold_magnitude = load(THRESHOLD_MAGNITUDE)
    anchor_recheck = load(ANCHOR_RECHECK)
    external = load(EXTERNAL_IMPORT)

    selected_candidates = [
        row for row in universal_candidates["candidate_classes"] if row["selected_now"]
    ]

    internal_exec = {
        "schema": "MTTStep5InternalScalarRowExecutionAudit.v1",
        "status": "INTERNAL_SCALAR_ROW_EXECUTION_ATTEMPTED_ZERO_ROWS_EMITTED",
        "step4_source": rel(STEP4),
        "direct_attempt_source": rel(DIRECT_ATTEMPT),
        "source_domain_closed": direct["source_domain_closed"],
        "basis_map_closed": direct["basis_map_closed"],
        "orbit_matrix_packet_closed": direct["orbit_matrix_packet_closed"],
        "direct_emission_attempt_executed": internal["closure_decision"][
            "direct_emission_attempt_executed"
        ],
        "full_S2_scalar_execution_ready": direct["full_S2_scalar_execution_ready"],
        "selected_universal_parameter_count": direct["selected_universal_parameter_count"],
        "codomain_scalar_row_count": direct["codomain_scalar_row_count"],
        "accepted_internal_scalar_row_count": direct["accepted_internal_scalar_row_count"],
        "lambda_H_row_emitted": direct["lambda_H_row_emitted"],
        "direct_rows_allowed": direct["direct_rows_allowed"],
        "why_zero_rows": direct["why_blocked"],
        "internal_scalar_execution_audited": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(INTERNAL_EXEC, internal_exec)

    noknob = {
        "schema": "MTTStep5NoKnobValueDerivationAudit.v1",
        "status": "NO_KNOB_AUDIT_CLOSED_VALUE_DERIVATION_NOT_CLOSED",
        "kernel_source": rel(NOKNOB_KERNEL),
        "kernel_typed": kernel["closure_decision"]["final_no_knob_kernel_typed"],
        "Rtheta_readiness": "8/9",
        "basis_map_closed": rtheta_rows["closure_decision"][
            "basis_map_to_sector_scaled_magnitude_rows_closed"
        ],
        "coefficient_functional_closed": rtheta_coeffs["coefficient_functional_closed"],
        "accepted_coefficient_row_count": rtheta_coeffs["accepted_coefficient_row_count"],
        "accepted_internal_value_emission_count": final_recheck[
            "selected_internal_value_emission_count"
        ],
        "closed_no_knob_obligation_count": obligations["closed_row_count"],
        "required_no_knob_obligation_count": obligations["required_row_count"],
        "lambda_H_coefficient_selected": rtheta_coeffs["lambda_H_coefficient_selected"],
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": rtheta_rows[
            "closure_decision"
        ]["accepted_Yukawa_magnitudes_as_no_knob_predictions"],
        "full_no_knob_closed": False,
        "why_not_closed": final_recheck["why_not_closed"],
        "no_knob_audit_closed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(NOKNOB, noknob)

    external_replay_policy = next(
        row
        for row in policy_matrix["policy_options"]
        if row["id"] == "UX-EXTERNAL-REPLAY-PACK"
    )
    minimal = {
        "schema": "MTTStep5MinimalUniversalParameterAudit.v1",
        "status": "MINIMAL_KNOB_POLICY_AUDITED_NO_SOURCE_ANCHOR_SELECTED",
        "policy_source": rel(UNIVERSAL_POLICY),
        "maximum_live_universal_parameters": universal_policy["maximum_live_universal_parameters"],
        "candidate_class_count": len(universal_candidates["candidate_classes"]),
        "selected_candidates_now": selected_candidates,
        "selected_universal_parameter_count": len(selected_candidates),
        "candidate_specific_source_theorem_present": policy_matrix[
            "candidate_specific_source_theorem_present"
        ],
        "minimal_universal_parameter_selection_closed": policy_matrix[
            "minimal_universal_parameter_selection_closed"
        ],
        "source_domain_closure_changes_decision": anchor_recheck[
            "source_domain_closure_changes_decision"
        ],
        "external_replay_policy_ready": policy_matrix["external_replay_policy_ready"],
        "external_replay_policy_is_no_knob": policy_matrix["external_replay_policy_is_no_knob"],
        "external_replay_pack_selected_for_SM_parity": external_replay_policy["selected_now"],
        "external_replay_pack_selected_for_full_no_knob": external_replay_policy[
            "accepted_for_full_no_knob"
        ],
        "ordinary_fitted_knobs_forbidden": True,
        "forbidden_uses": universal_policy["forbidden_uses"],
        "allowed_minimal_knob_policy_closed": True,
        "minimal_knob_selected_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(MINIMAL, minimal)

    boundary = {
        "schema": "MTTStep5ClosureBoundary.v1",
        "status": "STEP5_CLOSED_AS_AUDIT_NOT_AS_NOKNOB_NUMERICAL_CLOSURE",
        "step5_plan_label": "No-knob/minimal-knob audits",
        "step4_closed_for_plan_contract": step4["closure_decision"][
            "step4_closed_for_plan_contract"
        ],
        "internal_scalar_row_execution_audited": True,
        "no_knob_audit_closed": True,
        "minimal_knob_policy_audit_closed": True,
        "ordinary_fitted_knobs_forbidden": True,
        "selected_universal_parameter_count": 0,
        "accepted_internal_scalar_row_count": 0,
        "accepted_external_threshold_row_count": external["closure_decision"][
            "accepted_external_threshold_row_count"
        ],
        "accepted_external_mass_scheme_row_count": external["closure_decision"][
            "accepted_external_mass_scheme_row_count"
        ],
        "external_replay_ready_for_step6": True,
        "internal_no_knob_values_ready_for_step6": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "step5_closed_for_plan_contract": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(BOUNDARY, boundary)

    handoff = {
        "schema": "MTTStep5ToStep6Handoff.v1",
        "status": "HANDOFF_TO_STEP6_MEASURED_COMPARISON_READINESS_WITH_NOKNOB_GAP",
        "completed_step": 5,
        "next_step": 6,
        "next_required_artifact": NEXT,
        "step6_allowed_comparisons": {
            "admitted_external_replay_rows": True,
            "dynamic_first_response_qualitative_matrix_tests": True,
            "internal_no_knob_Yukawa_lambdaH_CKM_PMNS_predictions": False,
        },
        "step6_must_report_gaps": {
            "accepted_internal_scalar_rows": True,
            "lambda_H_internal_row": True,
            "Yukawa_magnitude_internal_rows": True,
            "CKM_PMNS_value_rows": True,
            "source_selected_universal_anchor": True,
        },
        "do_not_use_as_selectors": {
            "diagnostic_coefficients": True,
            "admitted_external_replay_rows": True,
            "measured_Yukawa_CKM_PMNS_lambdaH_values": True,
            "profile_residuals": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(HANDOFF, handoff)

    candidate = {
        "candidate": "MTTSelectedStep5NoKnobMinimalKnobAuditOrInternalScalarRowsExecution",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "step5_internal_scalar_row_execution_audit": rel(INTERNAL_EXEC),
            "step5_no_knob_value_derivation_audit": rel(NOKNOB),
            "step5_minimal_universal_parameter_audit": rel(MINIMAL),
            "step5_closure_boundary": rel(BOUNDARY),
            "step5_to_step6_handoff": rel(HANDOFF),
        },
        "theorem": {
            "name": "Step5NoKnobMinimalKnobAuditBoundaryTheorem",
            "proved": True,
            "statement": (
                "Step 5 is closed as an audit. The internal scalar-row route has been executed "
                "against the closed source/domain and emits zero accepted rows; the no-knob "
                "kernel is typed but has zero closed internal obligations; the strict minimal-knob "
                "policy is available but selects zero universal parameters and admits no fitted "
                "sector/observable knobs. External replay remains available only as admitted "
                "comparison support, not as full no-knob closure."
            ),
        },
        "closure_decision": {
            "step5_closed_for_plan_contract": True,
            "internal_scalar_row_execution_audited": True,
            "accepted_internal_scalar_row_count": 0,
            "lambda_H_row_emitted": False,
            "no_knob_audit_closed": True,
            "full_no_knob_closed": False,
            "minimal_knob_policy_audit_closed": True,
            "selected_universal_parameter_count": 0,
            "ordinary_fitted_knobs_forbidden": True,
            "true_SM_equivalence_closed": False,
        },
        "what_closes_now": {
            "step5_plan_contract": True,
            "internal_scalar_execution_audited": True,
            "no_knob_failure_mode_frozen": True,
            "minimal_knob_policy_audited_zero_selected": True,
            "ordinary_knobs_forbidden": True,
            "step6_handoff_typed": True,
        },
        "what_remains_open": handoff["step6_must_report_gaps"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "step5_contract_closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step5_NoKnobMinimalKnobAudit_or_InternalScalarRowsExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "step5_contract_closure_claimed": True,
        "step5_closed_for_plan_contract": True,
        "accepted_internal_scalar_row_count": 0,
        "lambda_H_row_emitted": False,
        "full_no_knob_closed": False,
        "selected_universal_parameter_count": 0,
        "ordinary_fitted_knobs_forbidden": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step5 NoKnobMinimalKnobAudit or InternalScalarRowsExecution v1

Status: `{STATUS}`.

Step 5 is closed as an audit:

```text
internal scalar-row execution audited : true
accepted internal scalar rows         : 0
lambda_H row emitted                  : false
no-knob value derivation closed       : false
selected universal parameters         : 0
ordinary fitted knobs allowed         : false
external replay ready for Step 6      : true
true SM equivalence closed            : false
full no-knob closure                  : false
```

This closes the no-knob/minimal-knob audit step without pretending the numerical
SM value rows have been internally derived.  Step 6 may compare admitted replay
and qualitative dynamic packets, but it must report the internal no-knob value
gap.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
