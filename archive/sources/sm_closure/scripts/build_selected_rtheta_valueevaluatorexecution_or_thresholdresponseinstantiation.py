"""Build R_theta value evaluator execution or threshold-response instantiation packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_OWNER = PACKET_DIR / "rtheta_value_evaluator_source_owner_update.packet.json"
INSTANTIATION_AUDIT = PACKET_DIR / "threshold_response_instantiation_audit_after_pi_closure.packet.json"
EXECUTION_GATE = PACKET_DIR / "rtheta_value_evaluator_execution_gate.packet.json"
VALUE_RECHECK = PACKET_DIR / "rtheta_coefficient_value_recheck_after_pi_closure.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_value_evaluator_recheck.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaValueEvaluatorExecution_or_ThresholdResponseInstantiation_v1.md"

PI_CLOSURE = DATA / "selected_rtheta_primitivec1overlap_or_pinoneedtheorem.candidate.json"
PI_RECHECK = (
    DATA
    / "selected_rtheta_primitivec1overlap_or_pinoneedtheorem"
    / "pi_rtheta_recheck_after_primitive_c1_import.packet.json"
)
COEFFICIENT_SKELETON = (
    DATA
    / "selected_rtheta_coefficientfunctional_or_universalanchorselection"
    / "rtheta_coefficient_functional_skeleton.packet.json"
)
THRESHOLD_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
OLD_INSTANTIATION_AUDIT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "current_repo_functional_instantiation_audit.packet.json"
)
THRESHOLD_SOURCE_THEOREM = DATA / "selected_thresholdfunctionalsourcetheorem_or_minimaluniversalparameterselection.candidate.json"
SOURCE_WEIGHTS = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "source_normalized_sector_projection_weights.packet.json"
)
THRESHOLD_ROWS_RECHECK = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "threshold_response_rows_recheck.packet.json"
)
GENERATION_SUPPORT = (
    DATA
    / "selected_generationresolvedthresholdsourcerows_or_profileconventionclosure"
    / "generation_source_support_recheck.packet.json"
)
PROFILE_CONVENTION = (
    DATA
    / "selected_generationresolvedthresholdsourcerows_or_profileconventionclosure"
    / "profile_convention_closure_recheck.packet.json"
)

STATUS = (
    "MTT_SELECTED_RTHETA_VALUEEVALUATOREXECUTION_OR_THRESHOLDRESPONSEINSTANTIATION_"
    "CLOSED_PI_SOURCE_OWNER_THRESHOLD_ROWS_OPEN"
)
NEXT = "MTT_Selected_RThetaThresholdRows_or_ProfileConventionSourceClosure_v1"


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
        raise FileNotFoundError("missing R_theta value-evaluator sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PI_CLOSURE,
        PI_RECHECK,
        COEFFICIENT_SKELETON,
        THRESHOLD_CONTRACT,
        OLD_INSTANTIATION_AUDIT,
        THRESHOLD_SOURCE_THEOREM,
        SOURCE_WEIGHTS,
        THRESHOLD_ROWS_RECHECK,
        GENERATION_SUPPORT,
        PROFILE_CONVENTION,
    ]
    require_sources(sources)

    pi_closure = load(PI_CLOSURE)
    pi_recheck = load(PI_RECHECK)
    skeleton = load(COEFFICIENT_SKELETON)
    contract = load(THRESHOLD_CONTRACT)
    old_audit = load(OLD_INSTANTIATION_AUDIT)
    source_theorem = load(THRESHOLD_SOURCE_THEOREM)
    weights = load(SOURCE_WEIGHTS)
    rows = load(THRESHOLD_ROWS_RECHECK)
    generation = load(GENERATION_SUPPORT)
    profile = load(PROFILE_CONVENTION)

    pi_closed = pi_closure["closure_decision"]["Pi_Rtheta_closed"] is True and pi_recheck["Pi_Rtheta_closed"] is True
    source_owner_closed = (
        pi_closed
        and source_theorem["closure_decision"]["dynamic_domain_subgate_closed"] is True
        and source_theorem["closure_decision"]["family_coordinate_subgate_closed"] is True
        and weights["source_projection_weights_closed"] is True
        and generation["generation_support_closed"] is True
    )
    coefficient_domain_closed = (
        skeleton["coefficient_functional_readiness_closed"] is True
        and skeleton["charged_functional_row_count"] == skeleton["required_charged_functional_row_count"]
    )
    threshold_contract_closed = contract["status"] == "SELECTED_THRESHOLD_RESPONSE_FUNCTIONAL_CONTRACT_EMITTED"
    threshold_rows_closed = rows["threshold_response_rows_closed"] is True
    mass_scheme_rows_closed = rows["mass_scheme_conversion_rows_closed"] is True
    scale_scheme_closed = profile["same_branch_scale_scheme_loop_convention_closed"] is True
    profile_response_closed = profile["full_profile_likelihood_closed"] is True
    no_knob_derivation_closed = source_theorem["closure_decision"][
        "minimal_parameter_yukawa_closure_closed"
    ] is True

    source_owner_update = {
        "schema": "MTTRThetaValueEvaluatorSourceOwnerUpdate.v1",
        "status": "PI_BACKED_DYNAMIC_SOURCE_OWNER_CLOSED",
        "pi_closure_source": rel(PI_CLOSURE),
        "threshold_source_theorem": rel(THRESHOLD_SOURCE_THEOREM),
        "source_projection_weights_source": rel(SOURCE_WEIGHTS),
        "generation_support_source": rel(GENERATION_SUPPORT),
        "Pi_Rtheta_closed": pi_closed,
        "selected_dynamic_operator_source_owner_closed": source_owner_closed,
        "coefficient_functional_domain_closed": coefficient_domain_closed,
        "source_normalized_projection_weights_closed": weights["source_projection_weights_closed"],
        "magnitude_bearing_projection_weights_closed": weights["magnitude_bearing_projection_weights_closed"],
        "retired_old_failure": "selected_dynamic_operator_source_owner",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": source_owner_closed,
    }
    write_json(SOURCE_OWNER, source_owner_update)

    requirements = [
        {
            "id": "selected_dynamic_operator_source_owner",
            "present": source_owner_closed,
            "source": rel(SOURCE_OWNER),
            "missing_for_acceptance": [],
        },
        {
            "id": "Pi_Rtheta_projection_kernel",
            "present": pi_closed,
            "source": rel(PI_CLOSURE),
            "missing_for_acceptance": [],
        },
        {
            "id": "coefficient_functional_skeleton",
            "present": coefficient_domain_closed,
            "source": rel(COEFFICIENT_SKELETON),
            "missing_for_acceptance": [],
        },
        {
            "id": "source_normalized_sector_projection_weights",
            "present": weights["source_projection_weights_closed"],
            "source": rel(SOURCE_WEIGHTS),
            "missing_for_acceptance": [],
        },
        {
            "id": "same_branch_scale_scheme_loop_convention",
            "present": scale_scheme_closed,
            "source": rel(PROFILE_CONVENTION),
            "missing_for_acceptance": [
                "available profile convention is explicitly first-pass/parity, not true precision source convention"
            ],
        },
        {
            "id": "threshold_matching_source_rows",
            "present": threshold_rows_closed,
            "source": rel(THRESHOLD_ROWS_RECHECK),
            "missing_for_acceptance": rows["accepted_threshold_matching_source_rows"] or [
                "accepted threshold matching source rows are empty"
            ],
        },
        {
            "id": "mass_scheme_conversion_source_rows",
            "present": mass_scheme_rows_closed,
            "source": rel(THRESHOLD_ROWS_RECHECK),
            "missing_for_acceptance": rows["accepted_mass_scheme_conversion_source_rows"] or [
                "accepted mass-scheme conversion source rows are empty"
            ],
        },
        {
            "id": "no_knob_value_derivation",
            "present": no_knob_derivation_closed,
            "source": rel(THRESHOLD_SOURCE_THEOREM),
            "missing_for_acceptance": [
                "no theorem derives magnitude-bearing rows from selected source data without a universal parameter or external source rows"
            ],
        },
        {
            "id": "full_profile_likelihood_or_accepted_diagonal_theorem",
            "present": profile_response_closed,
            "source": rel(PROFILE_CONVENTION),
            "missing_for_acceptance": [
                "full profile likelihood is not closed; first-pass diagonal/profile replay is not true precision equivalence"
            ],
        },
    ]
    present_count = sum(1 for item in requirements if item["present"])
    blocking_failures = [item["id"] for item in requirements if not item["present"]]
    threshold_response_instantiated = (
        threshold_contract_closed
        and source_owner_closed
        and pi_closed
        and coefficient_domain_closed
        and threshold_rows_closed
        and mass_scheme_rows_closed
        and scale_scheme_closed
        and profile_response_closed
        and no_knob_derivation_closed
    )

    instantiation_audit = {
        "schema": "MTTThresholdResponseInstantiationAuditAfterPiClosure.v1",
        "status": "PI_SOURCE_OWNER_CLOSED_THRESHOLD_RESPONSE_NOT_INSTANTIATED",
        "previous_audit": rel(OLD_INSTANTIATION_AUDIT),
        "functional_contract": rel(THRESHOLD_CONTRACT),
        "accepted_threshold_response_functional_instantiated": threshold_response_instantiated,
        "present_count": present_count,
        "requirement_count": len(requirements),
        "requirements": requirements,
        "retired_failures_since_previous": ["selected_dynamic_operator_source_owner"],
        "blocking_failures": blocking_failures,
        "old_blocking_failures": old_audit["blocking_failures"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(INSTANTIATION_AUDIT, instantiation_audit)

    execution_gate = {
        "schema": "MTTRThetaValueEvaluatorExecutionGate.v1",
        "status": "VALUE_EVALUATOR_DOMAIN_CLOSED_EXECUTION_BLOCKED_BY_THRESHOLD_ROWS",
        "Pi_Rtheta_closed": pi_closed,
        "selected_dynamic_operator_source_owner_closed": source_owner_closed,
        "coefficient_functional_skeleton_closed": coefficient_domain_closed,
        "threshold_response_contract_closed": threshold_contract_closed,
        "source_normalized_projection_weights_closed": weights["source_projection_weights_closed"],
        "magnitude_bearing_projection_weights_closed": weights["magnitude_bearing_projection_weights_closed"],
        "selected_threshold_response_functional_instantiated": threshold_response_instantiated,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "why_execution_blocked": blocking_failures,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(EXECUTION_GATE, execution_gate)

    value_recheck = {
        "schema": "MTTRThetaCoefficientValueRecheckAfterPiClosure.v1",
        "status": "PI_CLOSED_COEFFICIENT_VALUES_STILL_REJECTED",
        "charged_functional_row_count": skeleton["charged_functional_row_count"],
        "Pi_Rtheta_closed": pi_closed,
        "selected_value_evaluator_closed": False,
        "accepted_coefficient_value_count": 0,
        "rejected_value_reasons": [
            "threshold response functional is not instantiated",
            "same-branch scale/scheme/loop convention is not closed at true-precision level",
            "accepted threshold matching and mass-scheme conversion source rows are empty",
            "magnitude-bearing weights remain distinct from source-normalized unit weights",
        ],
        "lambda_H_value_selected": False,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VALUE_RECHECK, value_recheck)

    cutset = {
        "schema": "MTTNextCutsetAfterRThetaValueEvaluatorRecheck.v1",
        "status": "NEXT_ATTACK_THRESHOLD_ROWS_OR_PROFILE_CONVENTION_SOURCE_CLOSURE",
        "closed_now": {
            "Pi_Rtheta": pi_closed,
            "selected_dynamic_operator_source_owner": source_owner_closed,
            "coefficient_functional_domain": coefficient_domain_closed,
            "source_normalized_projection_weights": weights["source_projection_weights_closed"],
        },
        "still_open": blocking_failures,
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "derive same-branch scale/scheme/loop convention and threshold/mass-scheme source rows from selected branch",
            "route_B": "prove an accepted diagonal/profile limitation theorem strong enough to instantiate R_theta without full external likelihood",
            "route_C": "if no-knob is impossible, introduce the minimal universal parameter policy explicitly and rerun coefficient rows",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaValueEvaluatorExecutionOrThresholdResponseInstantiation",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "rtheta_value_evaluator_source_owner_update": rel(SOURCE_OWNER),
            "threshold_response_instantiation_audit_after_pi_closure": rel(INSTANTIATION_AUDIT),
            "rtheta_value_evaluator_execution_gate": rel(EXECUTION_GATE),
            "rtheta_coefficient_value_recheck_after_pi_closure": rel(VALUE_RECHECK),
            "next_cutset_after_value_evaluator_recheck": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaPiClosureRetiresDynamicSourceOwnerButNotThresholdRowsTheorem",
            "proved": True,
            "statement": (
                "Closing Pi_Rtheta supplies the selected physical projection kernel and retires the old "
                "selected_dynamic_operator_source_owner failure in the R_theta value-evaluator contract. "
                "The value evaluator still cannot emit numeric coefficients because true scale/scheme "
                "convention, threshold matching rows, mass-scheme conversion rows, no-knob value derivation, "
                "and profile/diagonal response remain unselected."
            ),
        },
        "closure_decision": {
            "Pi_Rtheta_closed": pi_closed,
            "selected_dynamic_operator_source_owner_closed": source_owner_closed,
            "coefficient_functional_domain_closed": coefficient_domain_closed,
            "source_normalized_projection_weights_closed": weights["source_projection_weights_closed"],
            "selected_threshold_response_functional_instantiated": threshold_response_instantiated,
            "selected_value_evaluator_closed": False,
            "accepted_coefficient_value_count": 0,
            "accepted_lambda_H_value": False,
            "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTTSelectedRThetaValueEvaluatorExecutionOrThresholdResponseInstantiation",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "Pi_Rtheta_closed": pi_closed,
        "selected_dynamic_operator_source_owner_closed": source_owner_closed,
        "selected_threshold_response_functional_instantiated": threshold_response_instantiated,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected RThetaValueEvaluatorExecution or ThresholdResponseInstantiation v1

Status: `{STATUS}`.

This artifact rechecks the `R_theta` value evaluator after `Pi_Rtheta` closure.

```text
Pi_Rtheta closed                              : {str(pi_closed).lower()}
selected dynamic operator source owner closed: {str(source_owner_closed).lower()}
coefficient functional domain closed         : {str(coefficient_domain_closed).lower()}
source-normalized projection weights closed  : {str(weights['source_projection_weights_closed']).lower()}
threshold response instantiated              : {str(threshold_response_instantiated).lower()}
accepted coefficient values                   : 0
lambda_H value accepted                       : false
```

The old threshold-contract failure `selected_dynamic_operator_source_owner` is
retired.  The value evaluator still cannot execute numeric rows because the
remaining open items are:

{chr(10).join(f'- `{item}`' for item in blocking_failures)}

No measured masses, Yukawas, CKM/PMNS values, or Higgs values are used as
selectors.  First-pass/profile replay packets remain validation support, not
source rows for true precision equivalence.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
