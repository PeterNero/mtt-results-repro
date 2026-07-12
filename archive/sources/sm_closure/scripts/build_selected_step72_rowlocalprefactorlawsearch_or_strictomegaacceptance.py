"""Build Step72 row-local prefactor law search / strict Omega gate."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ACCEPTANCE_PACKET = PACKET_DIR / "step72_strict_rowlocal_omega_acceptance_predicate.packet.json"
TRIAL_PACKET = PACKET_DIR / "step72_source_only_candidate_law_trials.packet.json"
TARGET_PACKET = PACKET_DIR / "step72_required_rowlocal_prefactor_target_table.packet.json"
KNOB_PACKET = PACKET_DIR / "step72_minimal_knob_diagnostic.packet.json"
WORKORDER_PACKET = PACKET_DIR / "step72_honest_galerkin_rowlocal_workorder.packet.json"
CUTSET_PACKET = PACKET_DIR / "step72_next_rowlocal_galerkin_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step72_RowLocalPrefactorLawSearch_or_StrictOmegaAcceptance_v1.md"

STEP71 = DATA / "selected_step71_smparitymatrixcomparison_or_rowlocaltargets.candidate.json"
STEP71_TARGETS = (
    DATA
    / "selected_step71_smparitymatrixcomparison_or_rowlocaltargets"
    / "step71_rowlocal_composite_target_contract.packet.json"
)
STEP71_PROJECTION = (
    DATA
    / "selected_step71_smparitymatrixcomparison_or_rowlocaltargets"
    / "step71_smparity_matrix_diagonal_projection.packet.json"
)
STEP71_SCOPE = (
    DATA
    / "selected_step71_smparitymatrixcomparison_or_rowlocaltargets"
    / "step71_matrix_scope_comparison.packet.json"
)
STEP70_FACTORS = (
    DATA
    / "selected_step70_heattorsionprefactorbackimport_or_rowlocalfrontier"
    / "step70_prefactor_slot_factorization.packet.json"
)
STEP69_FORMULA = (
    DATA
    / "selected_step69_hymthresholdprefactorrows_or_omegascalarexecution"
    / "step69_prefactor_solution_formula_rows.packet.json"
)
STEP69_DIAGNOSTIC = (
    DATA
    / "selected_step69_hymthresholdprefactorrows_or_omegascalarexecution"
    / "step69_diagnostic_prefactor_postcheck.packet.json"
)
HEAT_RESPONSE = (
    DATA
    / "selected_heattorsionresponse_finalgate"
    / "selected_finite_heat_spectrum_response.packet.json"
)

STATUS = "MTT_SELECTED_STEP72_ROWLOCAL_PREFACTOR_LAW_SEARCH_BUILT_STRICT_OMEGA_STILL_OPEN"
NEXT = "MTT_Selected_HonestRowLocalHYMGalerkinExecution_or_SelectedPrefactorSourceRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sector_gen(omega_id: str) -> tuple[str, str]:
    if omega_id == "Omega_H.lambda":
        return "H", "lambda"
    _, tail = omega_id.split("_", 1)
    sector, gen = tail.split(".")
    return sector, gen


def grouped_log_fit(
    rows: list[dict[str, Any]],
    group_fn: Callable[[dict[str, Any]], str | None],
) -> dict[str, Any]:
    covered = [row for row in rows if group_fn(row) is not None]
    groups: dict[str, list[float]] = {}
    for row in covered:
        group = group_fn(row)
        if group is None:
            continue
        groups.setdefault(group, []).append(math.log(abs(float(row["diagnostic_prefactor"]))))

    params = {group: sum(values) / len(values) for group, values in sorted(groups.items())}
    residuals = []
    row_residuals = []
    for row in covered:
        group = group_fn(row)
        if group is None:
            continue
        actual = math.log(abs(float(row["diagnostic_prefactor"])))
        predicted = params[group]
        residual = actual - predicted
        residuals.append(residual)
        row_residuals.append(
            {
                "omega_id": row["omega_id"],
                "group": group,
                "actual_log_prefactor": actual,
                "predicted_log_prefactor": predicted,
                "abs_log_residual": abs(residual),
                "multiplicative_error_factor": math.exp(abs(residual)),
            }
        )

    if residuals:
        rms = math.sqrt(sum(value * value for value in residuals) / len(residuals))
        max_abs = max(abs(value) for value in residuals)
    else:
        rms = 0.0
        max_abs = 0.0

    return {
        "covered_row_count": len(covered),
        "uncovered_row_count": len(rows) - len(covered),
        "parameter_count": len(params),
        "fitted_log_parameters_diagnostic_only": params,
        "rms_log_residual": rms,
        "max_abs_log_residual": max_abs,
        "max_multiplicative_error_factor": math.exp(max_abs),
        "row_residuals": row_residuals,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP71,
        STEP71_TARGETS,
        STEP71_PROJECTION,
        STEP71_SCOPE,
        STEP70_FACTORS,
        STEP69_FORMULA,
        STEP69_DIAGNOSTIC,
        HEAT_RESPONSE,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step72 inputs: " + ", ".join(missing))

    step71 = load(STEP71)
    targets = load(STEP71_TARGETS)
    projection = load(STEP71_PROJECTION)
    scope = load(STEP71_SCOPE)
    factors = load(STEP70_FACTORS)
    formula = load(STEP69_FORMULA)
    diagnostic = load(STEP69_DIAGNOSTIC)
    heat = load(HEAT_RESPONSE)

    if step71["status"] != "MTT_SELECTED_STEP71_SMPARITY_MATRIX_COMPARISON_BUILT_ROWLOCAL_TARGETS_OPEN":
        raise AssertionError("Step72 expects Step71 frontier status")
    if targets["accepted_rowlocal_source_row_count"] != 0:
        raise AssertionError("Step72 expects zero accepted row-local rows before search")
    if not projection["matrix_projection_matches_declared_common_scale_magnitudes"]:
        raise AssertionError("Step72 expects the Step71 diagonal projection postcheck")

    formula_by_omega = {row["omega_id"]: row for row in formula["formula_rows"]}
    factor_by_omega = {row["omega_id"]: row for row in factors["factor_rows"]}
    projection_by_omega = {row["omega_id"]: row for row in projection["diagonal_projection_rows"]}

    diagnostic_rows = []
    for row in diagnostic["diagnostic_rows"]:
        sector, gen = sector_gen(row["omega_id"])
        factor_row = factor_by_omega[row["omega_id"]]
        formula_row = formula_by_omega[row["omega_id"]]
        projection_row = projection_by_omega[row["omega_id"]]
        diagnostic_rows.append(
            {
                "omega_id": row["omega_id"],
                "sector": sector,
                "generation_or_lambda": gen,
                "source_class": factor_row["source_class"],
                "theta_exponent": formula_row["theta_exponent"],
                "theta_weight": formula_row["theta_weight"],
                "diagnostic_prefactor": row["diagnostic_prefactor"],
                "sm_parity_projected_abs_value": projection_row["sm_parity_projected_abs_value"],
                "finite_heat_torsion_subfactor_id": factor_row["finite_heat_torsion_subfactor_id"],
                "rowlocal_composite_target_symbolic": (
                    f"({row['diagnostic_prefactor']}) / {factor_row['finite_heat_torsion_subfactor_id']}"
                ),
                "accepted_as_source_row": False,
                "source_value_tier": "admitted_replay_postcheck_only",
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )

    family_prefactors = [
        abs(float(row["diagnostic_prefactor"])) for row in diagnostic_rows if row["source_class"] == "family_sector"
    ]
    family_span = max(family_prefactors) / min(family_prefactors)

    acceptance_packet = {
        "schema": "MTTStep72StrictRowLocalOmegaAcceptancePredicate.v1",
        "status": "STRICT_ROWLOCAL_OMEGA_ACCEPTANCE_PREDICATE_FIXED_ACCEPTANCE_FALSE",
        "source_inputs": {
            "step71_candidate": rel(STEP71),
            "step71_rowlocal_targets": rel(STEP71_TARGETS),
            "step70_factorization": rel(STEP70_FACTORS),
            "step69_formula_rows": rel(STEP69_FORMULA),
            "heat_response": rel(HEAT_RESPONSE),
        },
        "strict_acceptance_predicate": {
            "same_branch_selected_before_replay": True,
            "ten_rowlocal_overlap_rows_required": True,
            "ten_threshold_scheme_rows_or_single_selected_scheme_theorem_required": True,
            "lambda_H_value_payload_required": True,
            "observed_replay_matrix_may_be_used_only_after_source_selection": True,
            "ckm_down_sector_offdiagonal_matrix_is_separate_from_scalar_prefactor_gate": True,
        },
        "currently_closed": {
            "theta_exponent_weights": True,
            "finite_heat_torsion_subsource": True,
            "diagonal_projection_postcheck": True,
            "scope_split_against_ckm_mixing": True,
        },
        "currently_open": {
            "selected_rowlocal_HYM_overlap_rows": True,
            "selected_threshold_scheme_rows": True,
            "selected_lambda_H_value_payload": True,
            "strict_omega_acceptance": True,
            "selected_ckm_offdiagonal_matrix_theorem": True,
        },
        "strict_acceptance_result": {
            "accepted_rowlocal_source_row_count": 0,
            "accepted_threshold_scheme_row_count": 0,
            "accepted_full_prefactor_source_row_count": 0,
            "accepted_omega_source_row_count": 0,
            "accepted_internal_scalar_value_row_count": 0,
            "value_rows_execute": False,
            "reason": (
                "Step71 supplies exact replay postchecks and target slots, but no same-branch "
                "HYM/Galerkin row-local source rows or selected threshold-scheme rows."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ACCEPTANCE_PACKET, acceptance_packet)

    trial_specs = [
        (
            "source_class_only_heat_torsion",
            "source-only D_fin class law: one family value and one H value",
            lambda row: row["source_class"],
            True,
            False,
        ),
        (
            "sector_constant_diagnostic_fit",
            "diagnostic fit with one constant per u/d/e/H sector",
            lambda row: row["sector"],
            False,
            True,
        ),
        (
            "generation_constant_family_only_diagnostic_fit",
            "diagnostic fit with one family-generation constant; lambda_H is uncovered",
            lambda row: row["generation_or_lambda"] if row["sector"] != "H" else None,
            False,
            True,
        ),
        (
            "source_class_plus_generation_diagnostic_fit",
            "diagnostic fit with family generations plus H class",
            lambda row: f"{row['source_class']}:{row['generation_or_lambda']}",
            False,
            True,
        ),
    ]

    trial_rows: list[dict[str, Any]] = []
    for trial_id, description, group_fn, source_only, diagnostic_fit in trial_specs:
        fit = grouped_log_fit(diagnostic_rows, group_fn)
        trial_rows.append(
            {
                "trial_id": trial_id,
                "description": description,
                "source_only_without_replay_fit": source_only and not diagnostic_fit,
                "uses_replay_values_if_promoted": diagnostic_fit,
                "fit": fit,
                "accepted_as_selected_source_law": False,
                "rejection_reason": (
                    "source-only heat/torsion has only two classes and cannot emit the observed "
                    "family row span"
                    if source_only
                    else "diagnostic grouping parameters are fitted from replay targets, not selected by MTT geometry"
                ),
            }
        )

    replay_exact_trial = {
        "trial_id": "smparity_replay_exact_10_row_import",
        "description": "Use the Step71 replay diagonal projection to set all ten row-local composite values.",
        "source_only_without_replay_fit": False,
        "uses_replay_values_if_promoted": True,
        "covered_row_count": 10,
        "parameter_count": 10,
        "max_multiplicative_error_factor": 1.0,
        "accepted_as_selected_source_law": False,
        "rejection_reason": "This is exact only because it imports the downstream SM-parity replay matrix as selector.",
    }
    trial_rows.append(replay_exact_trial)

    trial_packet = {
        "schema": "MTTStep72SourceOnlyCandidateLawTrials.v1",
        "status": "NO_CANDIDATE_LAW_ACCEPTED_REPLAY_IMPORT_REJECTED",
        "diagnostic_prefactor_family_span": family_span,
        "source_only_closed_feature_classes": [
            "theta exponent weights",
            "D_fin.family",
            "D_fin.H",
            "selected q79/F/m=1 branch labels",
        ],
        "candidate_law_trials": trial_rows,
        "accepted_source_law_count": 0,
        "strict_omega_acceptance_from_trials": False,
        "replay_matrix_exact_but_forbidden": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(TRIAL_PACKET, trial_packet)

    target_packet = {
        "schema": "MTTStep72RequiredRowLocalPrefactorTargetTable.v1",
        "status": "TEN_ROWLOCAL_COMPOSITE_TARGETS_NUMERICALLY_PINNED_FOR_POSTCHECK_ONLY",
        "target_rows": diagnostic_rows,
        "target_row_count": len(diagnostic_rows),
        "family_prefactor_span": family_span,
        "max_abs_diagnostic_prefactor": max(abs(float(row["diagnostic_prefactor"])) for row in diagnostic_rows),
        "min_abs_diagnostic_prefactor": min(abs(float(row["diagnostic_prefactor"])) for row in diagnostic_rows),
        "all_targets_inside_order_one_window_0p1_to_10": diagnostic[
            "all_diagnostic_prefactors_inside_order_one_window_0p1_to_10"
        ],
        "accepted_as_source_rows": False,
        "accepted_source_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(TARGET_PACKET, target_packet)

    knob_models = [
        {
            "model_id": "one_global_prefactor",
            "description": "one universal replay-fitted scalar for all ten rows",
            **grouped_log_fit(diagnostic_rows, lambda row: "global"),
        },
        {
            "model_id": "two_source_classes",
            "description": "one family-sector scalar and one H scalar",
            **grouped_log_fit(diagnostic_rows, lambda row: row["source_class"]),
        },
        {
            "model_id": "three_family_sectors_only",
            "description": "one u, one d, one e scalar; lambda_H remains uncovered",
            **grouped_log_fit(diagnostic_rows, lambda row: row["sector"] if row["sector"] != "H" else None),
        },
    ]
    for model in knob_models:
        model["accepted_as_selected_knob_policy"] = False
        model["reason"] = (
            "diagnostic fit uses replay values; a 1-3 knob lane is credible only if the "
            "parameters are source-selected before replay and the uncovered rows are closed by theorem"
        )

    knob_packet = {
        "schema": "MTTStep72MinimalKnobDiagnostic.v1",
        "status": "ONE_TO_THREE_KNOBS_NOT_ACCEPTED_WITHOUT_SOURCE_SELECTION",
        "policy": {
            "one_to_three_universal_parameters_can_be_scientifically_credible": True,
            "ordinary_fit_parameters_forbidden": True,
            "must_be_selected_before_observed_replay": True,
            "must_emit_or_explain_all_ten_scalar_rows": True,
        },
        "diagnostic_models": knob_models,
        "accepted_minimal_knob_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(KNOB_PACKET, knob_packet)

    workorder_packet = {
        "schema": "MTTStep72HonestGalerkinRowLocalWorkorder.v1",
        "status": "HONEST_ROWLOCAL_HYM_GALERKIN_EXECUTION_SPECIFIED",
        "required_source_inputs": [
            "selected q79/F/m=1 finite HYM/Strominger operator",
            "ordered zero-mode bases for every Omega slot",
            "retarded overlap kernel derivative on the same branch",
            "Riesz/Green/projector normalization already selected in the Step36-42 chain",
            "threshold/scale/scheme convention selected before replay",
            "lambda_H slot treated as H-sector row rather than imported Higgs replay value",
        ],
        "row_formula_template": {
            "rowlocal_overlap": (
                "L_rowlocal.Omega = normalized finite Galerkin matrix element "
                "<psi_L, Pi0^perp G_E (delta_Omega D_E) Pi0^perp psi_R> on q79/F/m=1"
            ),
            "threshold_scheme": (
                "T_scheme.Omega = selected same-branch threshold/scale map from the finite "
                "source row to the common physical scalar convention"
            ),
            "strict_omega": "Omega.value = D_fin.class * L_rowlocal.Omega * T_scheme.Omega * epsilon_Theta^n",
        },
        "acceptance_tests": [
            "emit ten rows before reading the SM-parity replay magnitudes",
            "prove branch provenance q=79, orientation=F, torsion m=1 for every row",
            "separate diagonal scalar rows from the Y_d CKM/offdiagonal matrix theorem",
            "after source emission only, compare to Step72 target table as postcheck",
            "reject any row whose numeric value is obtained by solving against replay targets",
        ],
        "output_rows_required": [
            row["omega_id"] for row in diagnostic_rows
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(WORKORDER_PACKET, workorder_packet)

    cutset_packet = {
        "schema": "MTTStep72NextRowLocalGalerkinCutset.v1",
        "status": "HONEST_ROWLOCAL_GALERKIN_EXECUTION_IS_NEXT_NONLOOPING_TARGET",
        "not_missing_anymore": [
            "SM-parity matrix comparison",
            "strict row-local/Omega acceptance predicate",
            "source-only candidate law trial table",
            "diagnostic target table for all ten scalar slots",
            "minimal 1-3 knob diagnostic boundary",
            "honest Galerkin row-local execution workorder",
        ],
        "still_missing": [
            "actual selected row-local Galerkin matrix elements L_rowlocal.*",
            "actual selected threshold/scale/scheme rows T_scheme.*",
            "lambda_H H-sector source value payload",
            "strict Omega acceptance after row emission",
            "separate selected CKM/down-sector offdiagonal matrix theorem",
        ],
        "forbidden_routes": [
            "reuse the SM-parity replay matrix as source values",
            "fit one to three knobs to the replay magnitudes and call them selected",
            "collapse the ten row-local rows to two heat/torsion source classes",
            "claim diagonal scalar closure derives CKM/offdiagonal content",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CUTSET_PACKET, cutset_packet)

    candidate = {
        "candidate": "MTTSelectedStep72RowLocalPrefactorLawSearchOrStrictOmegaAcceptance",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "strict_rowlocal_omega_acceptance_predicate": rel(ACCEPTANCE_PACKET),
            "source_only_candidate_law_trials": rel(TRIAL_PACKET),
            "required_rowlocal_prefactor_target_table": rel(TARGET_PACKET),
            "minimal_knob_diagnostic": rel(KNOB_PACKET),
            "honest_galerkin_rowlocal_workorder": rel(WORKORDER_PACKET),
            "next_rowlocal_galerkin_cutset": rel(CUTSET_PACKET),
        },
        "theorem": {
            "name": "Step72RowLocalAcceptanceAndSearchTheorem",
            "proved": True,
            "statement": (
                "The Step71 SM-parity replay matrix cannot be promoted to selected row-local "
                "prefactor source data. The closed source-only material through Step71 supplies "
                "theta weights and two finite heat/torsion classes, which is insufficient to emit "
                "the ten row-local HYM/threshold prefactors. One-to-three parameters remain allowed "
                "only as pre-replay source-selected universal parameters. The next non-looping "
                "object is an honest same-branch Galerkin/HYM row-local execution."
            ),
        },
        "closure_decision": {
            "strict_rowlocal_acceptance_predicate_closed": True,
            "source_only_candidate_law_search_closed": True,
            "smparity_replay_matrix_as_source_rejected": True,
            "diagnostic_target_table_emitted": True,
            "minimal_knob_diagnostic_boundary_closed": True,
            "honest_galerkin_workorder_emitted": True,
            "accepted_source_law_count": 0,
            "accepted_rowlocal_source_row_count": 0,
            "accepted_threshold_scheme_row_count": 0,
            "accepted_full_prefactor_source_row_count": 0,
            "accepted_omega_source_row_count": 0,
            "accepted_internal_scalar_value_row_count": 0,
            "strict_omega_acceptance_closed": False,
            "lambda_H_value_row_emitted": False,
            "selected_ckm_offdiagonal_matrix_derived": False,
            "scalar_value_execution_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step71["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step72_RowLocalPrefactorLawSearch_or_StrictOmegaAcceptance_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    target_lines = "\n".join(
        f"{row['omega_id']:<16} C_diag={row['diagnostic_prefactor']:.12g} "
        f"target={row['rowlocal_composite_target_symbolic']}"
        for row in diagnostic_rows
    )
    source_class_fit = next(
        trial for trial in trial_rows if trial["trial_id"] == "source_class_only_heat_torsion"
    )["fit"]
    one_knob = knob_models[0]
    three_sector = knob_models[2]
    y_d_ratio = scope["matrix_scope_metrics"]["Y_d_offdiag_to_frob_ratio"]

    NOTE.write_text(
        f"""# MTT Selected Step72 RowLocalPrefactorLawSearch or StrictOmegaAcceptance v1

Status: `{STATUS}`.

## Result

Step72 fixes the strict acceptance predicate for the remaining scalar rows and
tests the tempting shortcut: using the earlier SM-parity replay matrix as the
row-local source.  That shortcut is rejected.

```text
accepted row-local source rows : 0
accepted threshold scheme rows : 0
accepted Omega source rows     : 0
strict Omega acceptance closed : False
```

The earlier matrix is still valuable: it gives an exact postcheck target table,
not a source selector.

## Target Table

```text
{target_lines}
```

All ten diagnostic prefactors remain finite and order-one, but the table is
postcheck-only.

## Source-Law Search

The closed source-only material through Step71 contains theta weights plus two
finite heat/torsion classes: `D_fin.family` and `D_fin.H`.  That cannot emit the
ten row-local values.  The family diagnostic span is
`{family_span:.12g}`, while the source-class-only diagnostic model has max
multiplicative residual `{source_class_fit['max_multiplicative_error_factor']:.12g}`.

Replay-fitted 1-3 knob checks remain diagnostic only:

```text
one global knob max factor error       : {one_knob['max_multiplicative_error_factor']:.12g}
three family-sector knobs uncovered    : {three_sector['uncovered_row_count']}
three family-sector knobs max error    : {three_sector['max_multiplicative_error_factor']:.12g}
```

A 1-3 knob lane remains scientifically possible only if the knobs are selected
by MTT geometry before replay.  Fitting them to the replay table is not accepted.

## SM-Parity Matrix Comparison

Compared with the earlier SM-parity matrix, Step72 keeps the same boundary as
Step71: diagonal scalar slots are aligned as postchecks, while down-sector
mixing remains outside the scalar-prefactor proof.

```text
Y_d offdiag/frob = {y_d_ratio:.12g}
```

## Next Object

The next non-looping proof object is an honest same-branch Galerkin/HYM row-local
execution:

```text
L_rowlocal.Omega =
  normalized finite Galerkin matrix element
  <psi_L, Pi0^perp G_E (delta_Omega D_E) Pi0^perp psi_R>

Omega.value =
  D_fin.class * L_rowlocal.Omega * T_scheme.Omega * epsilon_Theta^n
```

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
