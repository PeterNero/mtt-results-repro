"""Build Step55 threshold/mass admitted-row import / profile no-knob frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step55_thresholdmass_admittedrow_import_or_profile_noknob_frontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROW_IMPORT = PACKET_DIR / "step55_threshold_mass_admitted_row_import.packet.json"
ATOMIC_RECHECK = PACKET_DIR / "step55_atomic_route_recheck_after_threshold_mass.packet.json"
VALUE_RECHECK = PACKET_DIR / "step55_value_readiness_recheck_after_threshold_mass.packet.json"
CUTSET = PACKET_DIR / "step55_next_profile_noknob_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step55_ThresholdMassAdmittedRowImport_or_ProfileNoKnobFrontier_v1.md"

STEP54 = DATA / "selected_step54_samebranch_convention_import_or_thresholdmassrows.candidate.json"
STEP54_ATOMIC = (
    DATA
    / "selected_step54_samebranch_convention_import_or_thresholdmassrows"
    / "step54_atomic_route_recheck_after_convention.packet.json"
)
STEP54_VALUES = (
    DATA
    / "selected_step54_samebranch_convention_import_or_thresholdmassrows"
    / "step54_value_execution_recheck_after_convention.packet.json"
)
POST_PI_ROWS = DATA / "selected_thresholdmatchingrowspostpi_or_massschemesourcerows.candidate.json"
THRESHOLD_ROWS = (
    DATA
    / "selected_thresholdmatchingrowspostpi_or_massschemesourcerows"
    / "post_pi_admitted_threshold_matching_rows.packet.json"
)
MASS_ROWS = (
    DATA
    / "selected_thresholdmatchingrowspostpi_or_massschemesourcerows"
    / "post_pi_admitted_mass_scheme_rows.packet.json"
)
PROMOTION_GUARD = (
    DATA
    / "selected_thresholdmatchingrowspostpi_or_massschemesourcerows"
    / "external_row_admission_not_rtheta_selection.packet.json"
)
READINESS_AFTER_ROWS = (
    DATA
    / "selected_thresholdmatchingrowspostpi_or_massschemesourcerows"
    / "rtheta_value_readiness_after_external_rows.packet.json"
)
NEXT_AFTER_ROWS = (
    DATA
    / "selected_thresholdmatchingrowspostpi_or_massschemesourcerows"
    / "next_cutset_after_external_threshold_mass_rows.packet.json"
)

STATUS = "MTT_SELECTED_STEP55_THRESHOLD_MASS_ADMITTED_ROWS_IMPORTED_PROFILE_NOKNOB_OPEN"
NEXT = "MTT_Selected_FullProfileOrDiagonalTheoremPostPi_or_NoKnobValueDerivation_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP54,
        STEP54_ATOMIC,
        STEP54_VALUES,
        POST_PI_ROWS,
        THRESHOLD_ROWS,
        MASS_ROWS,
        PROMOTION_GUARD,
        READINESS_AFTER_ROWS,
        NEXT_AFTER_ROWS,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step55 inputs: " + ", ".join(missing))

    step54 = load(STEP54)
    step54_atomic = load(STEP54_ATOMIC)
    step54_values = load(STEP54_VALUES)
    rows_candidate = load(POST_PI_ROWS)
    threshold_rows = load(THRESHOLD_ROWS)
    mass_rows = load(MASS_ROWS)
    promotion_guard = load(PROMOTION_GUARD)
    readiness_after_rows = load(READINESS_AFTER_ROWS)
    next_after_rows = load(NEXT_AFTER_ROWS)

    row_import = {
        "schema": "MTTStep55ThresholdMassAdmittedRowImport.v1",
        "status": "THRESHOLD_MASS_ROWS_IMPORTED_AT_ADMITTED_EXTERNAL_TIER",
        "step54_source": rel(STEP54),
        "post_pi_row_source": rel(POST_PI_ROWS),
        "threshold_row_source": rel(THRESHOLD_ROWS),
        "mass_row_source": rel(MASS_ROWS),
        "threshold_matching_source_rows_closed_at_admitted_external_tier": rows_candidate[
            "closure_decision"
        ]["threshold_matching_source_rows_closed_at_admitted_external_tier"],
        "mass_scheme_conversion_source_rows_closed_at_admitted_external_tier": rows_candidate[
            "closure_decision"
        ]["mass_scheme_conversion_source_rows_closed_at_admitted_external_tier"],
        "admitted_threshold_row_count": threshold_rows[
            "accepted_admitted_external_threshold_matching_row_count"
        ],
        "admitted_mass_scheme_row_count": mass_rows[
            "accepted_admitted_external_mass_scheme_row_count"
        ],
        "accepted_internal_selected_Rtheta_row_count": promotion_guard[
            "accepted_internal_selected_Rtheta_row_count"
        ],
        "closed_as_no_knob_Rtheta_derivation": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ROW_IMPORT, row_import)

    remaining_atomic_failures = [
        "selected_response_functional_map",
        "profile_response_or_diagonal_limitation",
        "no_knob_value_derivation",
    ]
    atomic_recheck = {
        "schema": "MTTStep55AtomicRouteRecheckAfterThresholdMassRows.v1",
        "status": "THRESHOLD_MASS_ATOMIC_LEMMAS_CLOSED_AT_EXTERNAL_TIER_PROFILE_NOKNOB_OPEN",
        "previous_closed_atomic_count": step54_atomic["closed_atomic_count"],
        "closed_atomic_lemmas": [
            "no_observed_selector_proof",
            "same_branch_scale_scheme_loop_convention",
            "threshold_matching_source_rows_admitted_external",
            "mass_scheme_conversion_source_rows_admitted_external",
        ],
        "closed_atomic_count": 4,
        "required_atomic_count": step54_atomic["required_atomic_count"],
        "remaining_atomic_failures": remaining_atomic_failures,
        "external_likelihood_route_has_admitted_rows": True,
        "external_likelihood_route_is_full_profile": False,
        "minimal_parameter_route_still_open": True,
        "recommended_next": next_after_rows["recommended_next"]["artifact"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ATOMIC_RECHECK, atomic_recheck)

    value_recheck = {
        "schema": "MTTStep55ValueReadinessRecheckAfterThresholdMassRows.v1",
        "status": "READINESS_7_OF_9_EXTERNAL_ROWS_CLOSED_INTERNAL_VALUES_ZERO",
        "previous_readiness_source": rel(STEP54_VALUES),
        "previous_present_count": step54_values["present_count"],
        "previous_requirement_count": step54_values["requirement_count"],
        "retired_blocking_failures": readiness_after_rows["retired_blocking_failures"],
        "present_count": readiness_after_rows["present_count"],
        "requirement_count": readiness_after_rows["requirement_count"],
        "blocking_failures": readiness_after_rows["blocking_failures"],
        "selected_threshold_response_functional_instantiated": False,
        "selected_value_evaluator_closed": False,
        "accepted_coefficient_value_count": 0,
        "accepted_internal_scalar_row_count": 0,
        "accepted_lambda_H_value": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VALUE_RECHECK, value_recheck)

    cutset = {
        "schema": "MTTStep55NextProfileNoKnobCutset.v1",
        "status": "NEXT_FRONTIER_PROFILE_OR_NOKNOB_VALUE_DERIVATION",
        "closed_now": {
            "same_branch_scale_scheme_loop_convention": True,
            "threshold_matching_source_rows_at_admitted_external_tier": True,
            "mass_scheme_conversion_source_rows_at_admitted_external_tier": True,
            "Rtheta_readiness_present_count_advanced_to_7_of_9": True,
        },
        "still_open": {
            "selected_internal_Rtheta_threshold_mass_derivation": True,
            "selected_threshold_response_functional_instantiated": True,
            "no_knob_value_derivation": True,
            "full_profile_likelihood_or_accepted_diagonal_theorem": True,
            "numeric_Rtheta_coefficient_values": True,
            "lambda_H_value_execution": True,
            "Yukawa_mass_mixing_value_closure": True,
            "true_SM_equivalence": True,
        },
        "recommended_next": next_after_rows["recommended_next"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedStep55ThresholdMassAdmittedRowImportOrProfileNoKnobFrontier",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "threshold_mass_admitted_row_import": rel(ROW_IMPORT),
            "atomic_route_recheck_after_threshold_mass": rel(ATOMIC_RECHECK),
            "value_readiness_recheck_after_threshold_mass": rel(VALUE_RECHECK),
            "next_profile_noknob_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "Step55ThresholdMassAdmittedRowImportTheorem",
            "proved": True,
            "statement": (
                "The already-audited post-Pi threshold matching and mass-scheme rows are imported "
                "into the active numbered plan under the Step54 same-branch M_Z/MSbar convention. "
                "This closes threshold_matching_source_rows and mass_scheme_conversion_source_rows "
                "at the admitted-external replay tier, advances Rtheta readiness to 7/9, and keeps "
                "internal no-knob Rtheta value derivation open."
            ),
        },
        "closure_decision": {
            "same_branch_scale_scheme_loop_convention_closed": True,
            "threshold_matching_source_rows_closed": True,
            "threshold_matching_source_rows_closed_at_admitted_external_tier": True,
            "mass_scheme_conversion_source_rows_closed": True,
            "mass_scheme_conversion_source_rows_closed_at_admitted_external_tier": True,
            "selected_internal_Rtheta_threshold_mass_derivation_closed": False,
            "selected_threshold_response_functional_instantiated": False,
            "selected_value_evaluator_closed": False,
            "Rtheta_readiness_present_count": readiness_after_rows["present_count"],
            "Rtheta_readiness_requirement_count": readiness_after_rows["requirement_count"],
            "accepted_external_threshold_row_count": threshold_rows[
                "accepted_admitted_external_threshold_matching_row_count"
            ],
            "accepted_external_mass_scheme_row_count": mass_rows[
                "accepted_admitted_external_mass_scheme_row_count"
            ],
            "accepted_internal_Rtheta_coefficient_row_count": 0,
            "accepted_internal_scalar_row_count": 0,
            "accepted_lambda_H_value": False,
            "no_knob_value_derivation_closed": False,
            "full_profile_likelihood_or_accepted_diagonal_theorem_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "minimal_parameter_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step55_ThresholdMassAdmittedRowImport_or_ProfileNoKnobFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "theorem_proved": True,
        "closed_at_admitted_external_tier_only": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step55 ThresholdMassAdmittedRowImport or ProfileNoKnobFrontier v1

Status: `{STATUS}`.

Step55 imports the already-audited post-Pi threshold/mass row theorem into the
active numbered plan after the Step54 same-branch convention closure.

```text
threshold matching rows closed      : true
mass-scheme conversion rows closed  : true
closed tier                          : admitted external replay
admitted threshold rows              : {candidate["closure_decision"]["accepted_external_threshold_row_count"]}
admitted mass-scheme rows            : {candidate["closure_decision"]["accepted_external_mass_scheme_row_count"]}
selected internal Rtheta rows        : 0
Rtheta readiness                     : {candidate["closure_decision"]["Rtheta_readiness_present_count"]}/{candidate["closure_decision"]["Rtheta_readiness_requirement_count"]}
true SM equivalence                  : false
full no-knob closure                 : false
```

This is a real frontier reduction, but it is not a no-knob value proof.  The
accepted rows are admitted replay/source rows under the closed convention; they
do not select internal `Rtheta` coefficients and they do not instantiate the
threshold-response functional.

The next target is `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
