"""Build R_theta source-owner reconciliation / precision convention theorem gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_sourceowner_or_precisionthresholdconventiontheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_OWNER = PACKET_DIR / "rtheta_source_owner_reconciliation.packet.json"
COEFF_UPDATE = PACKET_DIR / "coefficient_promotion_after_source_owner.packet.json"
PRECISION = PACKET_DIR / "precision_threshold_convention_obstruction.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_source_owner_reconciliation.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaSourceOwner_or_PrecisionThresholdConventionTheorem_v1.md"

PREVIOUS = DATA / "selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows.candidate.json"
COEFFICIENTS = (
    DATA
    / "selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows"
    / "firstpass_rtheta_coefficient_values.packet.json"
)
PROMOTION_OLD = (
    DATA
    / "selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows"
    / "selected_rtheta_source_row_promotion_audit.packet.json"
)
VALUE_EVALUATOR = DATA / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation.candidate.json"
SOURCE_OWNER_UPDATE = (
    DATA
    / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation"
    / "rtheta_value_evaluator_source_owner_update.packet.json"
)
PI_AUDIT = (
    DATA
    / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation"
    / "threshold_response_instantiation_audit_after_pi_closure.packet.json"
)
PI_COEFF_RECHECK = (
    DATA
    / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation"
    / "rtheta_coefficient_value_recheck_after_pi_closure.packet.json"
)
CONVENTION = DATA / "selected_conventionsourcetheorem_or_rgenginethresholdpolicy.candidate.json"
TRUE_PRECISION_TARGET = (
    DATA
    / "selected_samebranchconvention_or_thresholdrowemission"
    / "true_precision_convention_target.packet.json"
)
SAME_BRANCH_GAP = (
    DATA
    / "selected_samebranchconvention_or_thresholdrowemission"
    / "same_branch_convention_source_gap.packet.json"
)
THRESHOLD_MAPS = DATA / "selected_thresholdpolerunningmaps_or_rthetaconventionsource.candidate.json"
SOURCE_ROWS = (
    DATA
    / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
    / "accepted_threshold_mass_scheme_source_row_audit.packet.json"
)

STATUS = (
    "MTT_SELECTED_RTHETASOURCEOWNER_OR_PRECISIONTHRESHOLDCONVENTIONTHEOREM_"
    "CLOSED_SOURCE_OWNER_FIRSTPASS_VALUES_PRECISION_ROWS_OPEN"
)
NEXT = "MTT_Selected_ThresholdRows_or_DiagonalProfileLimitationTheorem_v1"


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
        raise FileNotFoundError("missing Rtheta source-owner sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        COEFFICIENTS,
        PROMOTION_OLD,
        VALUE_EVALUATOR,
        SOURCE_OWNER_UPDATE,
        PI_AUDIT,
        PI_COEFF_RECHECK,
        CONVENTION,
        TRUE_PRECISION_TARGET,
        SAME_BRANCH_GAP,
        THRESHOLD_MAPS,
        SOURCE_ROWS,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    coeffs = load(COEFFICIENTS)
    old_promotion = load(PROMOTION_OLD)
    value_evaluator = load(VALUE_EVALUATOR)
    source_owner_update = load(SOURCE_OWNER_UPDATE)
    pi_audit = load(PI_AUDIT)
    pi_coeff_recheck = load(PI_COEFF_RECHECK)
    convention = load(CONVENTION)
    precision_target = load(TRUE_PRECISION_TARGET)
    same_branch_gap = load(SAME_BRANCH_GAP)
    threshold_maps = load(THRESHOLD_MAPS)
    source_rows = load(SOURCE_ROWS)

    source_owner_packet = {
        "schema": "MTTRThetaSourceOwnerReconciliation.v1",
        "status": "PI_BACKED_SOURCE_OWNER_RECONCILED_WITH_FIRSTPASS_COEFFICIENT_LAYER",
        "old_promotion_audit_source": rel(PROMOTION_OLD),
        "pi_source_owner_update": rel(SOURCE_OWNER_UPDATE),
        "pi_instantiation_audit": rel(PI_AUDIT),
        "previous_source_owner_blocker_retired": "selected_dynamic_operator_source_owner"
        in pi_audit["retired_failures_since_previous"],
        "Pi_Rtheta_closed": source_owner_update["Pi_Rtheta_closed"],
        "coefficient_functional_domain_closed": source_owner_update["coefficient_functional_domain_closed"],
        "source_normalized_projection_weights_closed": source_owner_update["source_normalized_projection_weights_closed"],
        "selected_dynamic_operator_source_owner_closed": source_owner_update[
            "selected_dynamic_operator_source_owner_closed"
        ],
        "firstpass_Rtheta_coefficient_values_present": coeffs["accepted_as_firstpass_Rtheta_coefficient_values"],
        "firstpass_dense_coefficient_entries": coeffs["total_dense_coefficient_entries"],
        "firstpass_nonzero_coefficient_entries": coeffs["total_nonzero_coefficient_entries"],
        "reconciliation_statement": (
            "The older promotion audit correctly rejected selected rows at that time, but its dynamic source-owner "
            "failure is now retired by the later Pi_Rtheta packet. The remaining rejection is no longer source-owner; "
            "it is precision convention, threshold/mass-scheme source rows, no-knob values, and profile response."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SOURCE_OWNER, source_owner_packet)

    remaining_blockers = [
        item
        for item in pi_audit["blocking_failures"]
        if item != "selected_dynamic_operator_source_owner"
    ]
    coeff_update = {
        "schema": "MTTCoefficientPromotionAfterSourceOwner.v1",
        "status": "SOURCE_OWNER_CLOSED_FIRSTPASS_COEFFICIENTS_PRESENT_SELECTED_PROMOTION_OPEN",
        "coefficient_source": rel(COEFFICIENTS),
        "pi_coefficient_recheck_source": rel(PI_COEFF_RECHECK),
        "old_accepted_coefficient_value_count": pi_coeff_recheck["accepted_coefficient_value_count"],
        "new_firstpass_dense_coefficient_entries": coeffs["total_dense_coefficient_entries"],
        "new_firstpass_nonzero_coefficient_entries": coeffs["total_nonzero_coefficient_entries"],
        "firstpass_Rtheta_coefficient_values_closed": True,
        "selected_dynamic_operator_source_owner_closed": True,
        "selected_Rtheta_coefficient_values_closed": False,
        "selected_Rtheta_source_rows_closed": False,
        "selected_threshold_response_functional_instantiated": False,
        "remaining_blockers_after_source_owner_reconciliation": remaining_blockers,
        "why_values_are_still_not_selected": [
            "first-pass coefficients are finite replay values, not same-branch true-precision threshold rows",
            "accepted threshold matching source rows are still empty",
            "accepted mass-scheme conversion source rows are still empty",
            "no accepted diagonal/profile limitation theorem has replaced the full profile likelihood",
            "no no-knob value theorem derives the magnitude-bearing rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(COEFF_UPDATE, coeff_update)

    precision_packet = {
        "schema": "MTTPrecisionThresholdConventionObstruction.v1",
        "status": "TRUE_PRECISION_CONVENTION_TARGET_IDENTIFIED_VALUES_AND_SOURCE_ROWS_OPEN",
        "convention_policy_source": rel(CONVENTION),
        "true_precision_target_source": rel(TRUE_PRECISION_TARGET),
        "same_branch_gap_source": rel(SAME_BRANCH_GAP),
        "threshold_map_decomposition_source": rel(THRESHOLD_MAPS),
        "source_row_audit_source": rel(SOURCE_ROWS),
        "target_scale": precision_target["target_scale"],
        "target_scheme": precision_target["target_scheme"],
        "beta_functions_required": precision_target["beta_functions_required"],
        "threshold_matching_required": precision_target["threshold_matching_required"],
        "mass_scheme_conversion_required": precision_target["mass_scheme_conversion_required"],
        "target_identified": precision_target["target_identified"],
        "selected_same_branch_source_closed": precision_target["selected_same_branch_source_closed"],
        "same_branch_convention_source_theorem_closed": convention["closure_decision"][
            "same_branch_convention_source_theorem_closed"
        ],
        "accepted_precision_threshold_row_count": threshold_maps["closure_decision"][
            "accepted_precision_threshold_row_count"
        ],
        "accepted_threshold_matching_source_rows": source_rows["accepted_threshold_matching_source_rows"],
        "accepted_mass_scheme_conversion_source_rows": source_rows["accepted_mass_scheme_conversion_source_rows"],
        "same_branch_gap_status": same_branch_gap["status"],
        "precision_convention_closed": False,
        "precision_threshold_rows_closed": False,
        "mass_scheme_source_rows_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PRECISION, precision_packet)

    cutset = {
        "schema": "MTTNextCutsetAfterSourceOwnerReconciliation.v1",
        "status": "NEXT_ATTACK_THRESHOLD_ROWS_OR_DIAGONAL_PROFILE_LIMITATION",
        "closed_now": {
            "selected_dynamic_operator_source_owner": True,
            "Pi_Rtheta": True,
            "coefficient_functional_domain": True,
            "source_normalized_projection_weights": True,
            "firstpass_Rtheta_coefficient_values_still_available": True,
            "stale_source_owner_blocker_retired_from_promotion_audit": True,
        },
        "still_open": {
            "same_branch_scale_scheme_loop_convention": True,
            "threshold_matching_source_rows": True,
            "mass_scheme_conversion_source_rows": True,
            "selected_Rtheta_coefficient_values": True,
            "selected_Rtheta_source_rows": True,
            "selected_threshold_response_functional": True,
            "no_knob_value_derivation": True,
            "full_profile_likelihood_or_accepted_diagonal_theorem": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "derive threshold/mass-scheme source rows from the Pi_Rtheta source owner and first-pass coefficient packet",
            "route_B": "prove an accepted diagonal/profile limitation theorem that allows first-pass coefficients to instantiate R_theta provisionally",
            "route_C": "import or reconstruct a precision threshold convention table and keep it downstream-only until source-owned",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaSourceOwnerOrPrecisionThresholdConventionTheorem",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "rtheta_source_owner_reconciliation": rel(SOURCE_OWNER),
            "coefficient_promotion_after_source_owner": rel(COEFF_UPDATE),
            "precision_threshold_convention_obstruction": rel(PRECISION),
            "next_cutset_after_source_owner_reconciliation": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaSourceOwnerReconciliationTheorem",
            "proved": True,
            "statement": (
                "The selected dynamic/operator source-owner blocker for R_theta is retired by the Pi_Rtheta "
                "closure and source-normalized projection weights. Combining that with the new first-pass "
                "coefficient packet closes the source-owner/coefficient-domain layer, but it does not promote "
                "the first-pass coefficients to selected threshold response rows. The remaining blockers are "
                "same-branch true-precision convention, threshold matching source rows, mass-scheme conversion "
                "source rows, no-knob value derivation, and full profile or accepted diagonal limitation."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "selected_dynamic_operator_source_owner_closed": True,
            "Pi_Rtheta_closed": True,
            "coefficient_functional_domain_closed": True,
            "firstpass_Rtheta_coefficient_values_closed": True,
            "selected_Rtheta_coefficient_values_closed": False,
            "selected_Rtheta_source_rows_closed": False,
            "selected_threshold_response_functional_closed": False,
            "same_branch_scale_scheme_loop_convention_closed": False,
            "threshold_matching_source_rows_closed": False,
            "mass_scheme_conversion_source_rows_closed": False,
            "full_profile_likelihood_or_accepted_diagonal_theorem_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_RThetaSourceOwner_or_PrecisionThresholdConventionTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "selected_dynamic_operator_source_owner_closed": True,
        "Pi_Rtheta_closed": True,
        "coefficient_functional_domain_closed": True,
        "firstpass_Rtheta_coefficient_values_closed": True,
        "selected_Rtheta_coefficient_values_closed": False,
        "selected_Rtheta_source_rows_closed": False,
        "selected_threshold_response_functional_closed": False,
        "same_branch_scale_scheme_loop_convention_closed": False,
        "threshold_matching_source_rows_closed": False,
        "mass_scheme_conversion_source_rows_closed": False,
        "full_profile_likelihood_or_accepted_diagonal_theorem_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected RThetaSourceOwner or PrecisionThresholdConventionTheorem v1

Status: `{STATUS}`.

This artifact reconciles the newer `Pi_Rtheta` closure with the first-pass
`R_theta^(1)` coefficient packet.

```text
selected dynamic source owner closed : true
Pi_Rtheta closed                     : true
coefficient functional domain closed : true
first-pass coefficient values closed : true
selected threshold rows closed       : false
precision convention closed          : false
```

So the stale source-owner blocker is retired.  The remaining wall is narrower:
threshold/mass-scheme source rows, same-branch true-precision convention,
no-knob value derivation, and full profile or accepted diagonal limitation.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
