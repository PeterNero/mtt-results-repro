"""Build internal threshold response value rows or external source import decision.

This packet closes the ambiguity left after the threshold-anchor search.  It
does not claim no-knob closure.  It classifies every scalar row into the only
three honest lanes currently available:

1. selected internal source row,
2. admitted external replay/import row,
3. forbidden target-fitted replay row.

The result fixes the next constructive object: source-selected
L_rowlocal/T_scheme/lambda_H execution, with external rows kept as a controlled
empirical layer only.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_internalthresholdresponsefunctionalvaluerows_or_externalsourceimportdecision"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INTERNAL_GATE = PACKET_DIR / "internal_threshold_response_value_row_gate.packet.json"
ROW_LEDGER = PACKET_DIR / "ten_row_internal_external_source_decision_ledger.packet.json"
EXTERNAL_DECISION = PACKET_DIR / "controlled_external_source_import_decision.packet.json"
WORKORDER = PACKET_DIR / "source_selected_threshold_functional_execution_workorder.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_internal_external_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_InternalThresholdResponseFunctionalValueRows_or_ExternalSourceImportDecision_v1.md"

PREVIOUS = DATA / "selected_thresholdschemevaluerows_or_sourceselecteduniversalanchorexecution.candidate.json"
STEP74 = DATA / "selected_step74_pivsd01backimport_or_rowlocalthresholdvaluefrontier.candidate.json"
ROWLOCAL = DATA / "selected_rowlocalthresholdvaluerows_or_lambdahprefactorexecution.candidate.json"
QUADRATURE = DATA / "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem.candidate.json"
PHIFIN_KERNEL = DATA / "selected_phifinminimizertracerowlocalkernel_or_thresholdschemevaluerows.candidate.json"
THRESHOLD_IMPORT = DATA / "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport.candidate.json"
NOKNOB_KERNEL = DATA / "selected_noknobvaluederivationkernel_or_sourceanchortheorem.candidate.json"
INTERNAL_RTHETA = DATA / "selected_internalrthetascalarrowemission_or_universalanchorselection.candidate.json"
READINESS = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "rtheta_readiness_final_frontier.packet.json"
)
FINAL_RECHECK = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "final_no_knob_value_derivation_recheck.packet.json"
)
EXTERNAL_BOUNDARY = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "post_pi_external_replay_boundary.packet.json"
)
TARGETS = (
    DATA
    / "selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance"
    / "step72_required_rowlocal_prefactor_target_table.packet.json"
)
FORMULAS = (
    DATA
    / "selected_step69_hymthresholdprefactorrows_or_omegascalarexecution"
    / "step69_prefactor_solution_formula_rows.packet.json"
)
FACTORS = (
    DATA
    / "selected_step70_heattorsionprefactorbackimport_or_rowlocalfrontier"
    / "step70_prefactor_slot_factorization.packet.json"
)

STATUS = (
    "MTT_SELECTED_INTERNALTHRESHOLDRESPONSEFUNCTIONALVALUEROWS_OR_EXTERNALSOURCEIMPORTDECISION_"
    "BUILT_DECISION_BOUNDARY_INTERNAL_ROWS_OPEN"
)
NEXT = "MTT_Selected_LRowlocalTSchemeLambdaH_SourceExecution_or_ControlledEmpiricalImport_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing internal/external decision inputs: " + ", ".join(missing))


def by_omega(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {row["omega_id"]: row for row in rows}


def build_row_decisions(
    targets: dict[str, Any],
    formulas: dict[str, Any],
    factors: dict[str, Any],
) -> list[dict[str, Any]]:
    formula_by_omega = by_omega(formulas["formula_rows"])
    factor_by_omega = by_omega(factors["factor_rows"])
    rows: list[dict[str, Any]] = []
    for target in targets["target_rows"]:
        omega_id = target["omega_id"]
        formula = formula_by_omega[omega_id]
        factor = factor_by_omega[omega_id]
        is_higgs = target["sector"] == "H"
        missing_internal_sources = [
            factor["row_local_overlap_threshold_factor_id"],
            factor["scale_scheme_factor_id"],
            "strict_omega_acceptance_for_" + omega_id,
        ]
        if is_higgs:
            missing_internal_sources.append("selected_lambda_H_payload_row")
        else:
            missing_internal_sources.append("selected_charged_threshold_value_row_for_" + omega_id)
        rows.append(
            {
                "omega_id": omega_id,
                "sector": target["sector"],
                "generation_or_lambda": target["generation_or_lambda"],
                "theta_exponent": target["theta_exponent"],
                "theta_weight": target["theta_weight"],
                "formula": formula["formula"],
                "finite_heat_torsion_subfactor_id": factor["finite_heat_torsion_subfactor_id"],
                "closed_source_subfields": {
                    "theta_exponent_weight": factor["closed_subsources"]["theta_exponent_weight"],
                    "finite_heat_torsion_response": factor["closed_subsources"]["finite_heat_torsion_response"],
                    "prefactor_formula_contract": formula["accepted_formula_skeleton"],
                },
                "open_internal_source_subfields": missing_internal_sources,
                "internal_selected_value_row_accepted": False,
                "admitted_external_replay_row_available": target["source_value_tier"]
                == "admitted_replay_postcheck_only",
                "forbidden_target_fit_row_available": True,
                "accepted_decision": "controlled_external_replay_only",
                "why_internal_not_accepted": [
                    "L_rowlocal and T_scheme are not selected source rows",
                    "strict Omega acceptance is still false",
                    "row is currently pinned only as admitted replay/postcheck data",
                    "target-scored coefficients are forbidden as source selectors",
                ],
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )
    return rows


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        STEP74,
        ROWLOCAL,
        QUADRATURE,
        PHIFIN_KERNEL,
        THRESHOLD_IMPORT,
        NOKNOB_KERNEL,
        INTERNAL_RTHETA,
        READINESS,
        FINAL_RECHECK,
        EXTERNAL_BOUNDARY,
        TARGETS,
        FORMULAS,
        FACTORS,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    step74 = load(STEP74)
    rowlocal = load(ROWLOCAL)
    quadrature = load(QUADRATURE)
    phifin_kernel = load(PHIFIN_KERNEL)
    threshold_import = load(THRESHOLD_IMPORT)
    noknob_kernel = load(NOKNOB_KERNEL)
    internal_rtheta = load(INTERNAL_RTHETA)
    readiness = load(READINESS)
    final_recheck = load(FINAL_RECHECK)
    external_boundary = load(EXTERNAL_BOUNDARY)
    targets = load(TARGETS)
    formulas = load(FORMULAS)
    factors = load(FACTORS)

    row_decisions = build_row_decisions(targets, formulas, factors)
    internal_accepted_count = sum(1 for row in row_decisions if row["internal_selected_value_row_accepted"])
    external_available_count = sum(1 for row in row_decisions if row["admitted_external_replay_row_available"])

    internal_gate = {
        "schema": "MTTInternalThresholdResponseFunctionalValueRowGate.v1",
        "status": "INTERNAL_THRESHOLD_RESPONSE_VALUE_ROWS_NOT_EMITTED",
        "readiness_fraction": readiness["readiness_fraction"],
        "only_remaining_readiness_blocker": readiness["only_remaining_readiness_blocker"],
        "present_count": readiness["present_count"],
        "requirement_count": readiness["requirement_count"],
        "accepted_internal_scalar_value_row_count": internal_accepted_count,
        "accepted_threshold_scheme_value_row_count": previous["closure_decision"][
            "accepted_threshold_scheme_value_row_count"
        ],
        "accepted_omega_source_row_count": previous["closure_decision"]["accepted_omega_source_row_count"],
        "lambda_H_value_row_emitted": final_recheck["lambda_H_coefficient_selected"],
        "selected_threshold_response_functional_instantiated": final_recheck[
            "selected_threshold_response_functional_instantiated"
        ],
        "basis_map_to_sector_scaled_magnitude_rows_closed": final_recheck[
            "basis_map_to_sector_scaled_magnitude_rows_closed"
        ],
        "support_retired_as_blocker": {
            "operator_domain_side_closed_after_backimport": step74["closure_decision"][
                "operator_domain_side_closed_after_backimport"
            ],
            "latest_source_domain_imported": phifin_kernel["closure_decision"][
                "latest_source_domain_imported"
            ],
            "overlap_quadrature_functional_defined": quadrature["closure_decision"][
                "overlap_quadrature_functional_defined"
            ],
            "advanced_attack_plan_built": rowlocal["closure_decision"]["advanced_attack_plan_built"],
        },
        "blocking_value_sources": [
            "selected_L_rowlocal source rows",
            "selected_T_scheme source rows",
            "selected lambda_H payload row",
            "strict Omega acceptance",
            "selected matrix-level mixing extension after scalar rows",
        ],
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(INTERNAL_GATE, internal_gate)

    row_ledger = {
        "schema": "MTTTenRowInternalExternalSourceDecisionLedger.v1",
        "status": "TEN_ROWS_CLASSIFIED_INTERNAL_OPEN_EXTERNAL_REPLAY_ONLY",
        "row_count": len(row_decisions),
        "internal_selected_value_row_count": internal_accepted_count,
        "admitted_external_replay_row_count": external_available_count,
        "forbidden_target_fit_row_count": len(row_decisions),
        "row_decisions": row_decisions,
        "decision_rule": (
            "A row may close no-knob only if L_rowlocal, T_scheme, and any lambda_H payload are "
            "selected before replay. Admitted replay rows are comparison/import data only."
        ),
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(ROW_LEDGER, row_ledger)

    external_decision = {
        "schema": "MTTControlledExternalSourceImportDecision.v1",
        "status": "EXTERNAL_SOURCE_IMPORT_AVAILABLE_AS_CONTROLLED_EMPIRICAL_LAYER_ONLY",
        "external_import_lane_available": threshold_import["closure_decision"][
            "external_import_lane_closed_at_admitted_replay_tier"
        ],
        "accepted_external_threshold_row_count": external_boundary["threshold_rows_at_admitted_external_tier"],
        "accepted_external_mass_scheme_row_count": external_boundary["mass_scheme_rows_at_admitted_external_tier"],
        "accepted_diagonal_profile_theorem_closed": external_boundary[
            "accepted_diagonal_profile_theorem_closed"
        ],
        "ten_row_postcheck_target_count": targets["target_row_count"],
        "ten_row_postcheck_targets_available": external_available_count == targets["target_row_count"],
        "selected_for_no_knob_closure": False,
        "selected_for_true_SM_equivalence": False,
        "allowed_use": [
            "SM-parity/admitted-replay comparison",
            "controlled empirical layer if the project explicitly accepts source import",
            "postcheck after internal source-row emission",
        ],
        "forbidden_use": [
            "branch/source/operator selection",
            "no-knob value derivation",
            "promotion of fitted row coefficients to source rows",
            "hiding empirical constants inside L_rowlocal or T_scheme",
        ],
        "external_rows_used_as_branch_selector": external_boundary["external_rows_used_as_branch_selector"],
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(EXTERNAL_DECISION, external_decision)

    workorder = {
        "schema": "MTTSourceSelectedThresholdFunctionalExecutionWorkorder.v1",
        "status": "NEXT_EXECUTE_SOURCE_SELECTED_LROWLOCAL_TSCHEME_LAMBDAH_ROWS",
        "functional_contract": {
            "row_formula": "Omega_i = D_fin[class(i)] * L_rowlocal_i * T_scheme_i * exp(-2*pi*n_i)",
            "charged_rows": 9,
            "higgs_rows": 1,
            "source_selected_inputs_already_closed": [
                "epsilon_Theta = exp(-2*pi)",
                "theta exponent rows",
                "D_fin.family and D_fin.H heat/torsion subfactors",
                "Rtheta/Pi/source-domain ownership",
                "post-Pi admitted replay boundary for comparison only",
            ],
            "source_selected_inputs_to_execute": [
                "L_rowlocal_i from same-branch HYM/overlap derivative rows",
                "T_scheme_i from same-branch threshold/mass/profile functional rows",
                "lambda_H H-sector payload",
                "strict Omega acceptance after rows are emitted",
            ],
        },
        "acceptance_tests": [
            "no observed or benchmark SM values enter before row emission",
            "row values have source provenance independent of target residuals",
            "all ten rows emit before postcheck comparison",
            "external replay rows remain quarantined as comparison/import data",
            "matrix-level mixing extension is attempted only after scalar rows close",
        ],
        "route_A": "derive L_rowlocal and T_scheme from selected same-branch HYM/threshold functional rows",
        "route_B": "derive an equivalent source-selected universal anchor that emits the same ten-row codomain before replay",
        "route_C": "declare controlled empirical import and stop calling the result no-knob",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(WORKORDER, workorder)

    cutset = {
        "schema": "MTTNextCutsetAfterInternalExternalDecision.v1",
        "status": "NEXT_ATTACK_SOURCE_SELECTED_TEN_ROW_FUNCTIONAL_EXECUTION",
        "next_required_artifact": NEXT,
        "closed_here": [
            "ten scalar rows classified by source tier",
            "internal value-row gate rebuilt with readiness 8/9 and zero accepted rows",
            "external import lane admitted only as controlled empirical layer",
            "forbidden fitted-row lane quarantined",
            "source-selected L_rowlocal/T_scheme/lambda_H workorder emitted",
        ],
        "still_open": [
            "selected L_rowlocal rows",
            "selected T_scheme rows",
            "selected lambda_H payload row",
            "strict Omega acceptance",
            "matrix-level CKM/offdiagonal mixing extension",
            "full no-knob SM closure",
        ],
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CUTSET, cutset)

    decision = {
        "internal_threshold_response_value_rows_emitted": False,
        "accepted_internal_scalar_value_row_count": internal_accepted_count,
        "accepted_threshold_scheme_value_row_count": 0,
        "accepted_omega_source_row_count": 0,
        "lambda_H_value_row_emitted": False,
        "external_source_import_available_at_admitted_replay_tier": True,
        "external_source_import_selected_for_no_knob": False,
        "controlled_empirical_layer_policy_built": True,
        "ten_row_decision_ledger_built": True,
        "source_selected_execution_workorder_built": True,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
    }
    candidate = {
        "candidate": "MTTSelectedInternalThresholdResponseFunctionalValueRowsOrExternalSourceImportDecision",
        "status": STATUS,
        "closure_claimed": True,
        "theorem": {
            "name": "InternalExternalValueRowDecisionBoundaryTheorem",
            "proved": True,
            "statement": (
                "Given the closed Rtheta/source-domain support, admitted post-Pi external replay rows, "
                "and the failed current source-anchor/replay-fit lanes, the ten scalar rows split into "
                "zero internal selected value rows and ten controlled admitted-replay rows. External "
                "import is available only as an empirical layer, not as no-knob closure. The next "
                "constructive proof object is source-selected L_rowlocal/T_scheme/lambda_H execution."
            ),
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "internal_threshold_response_value_row_gate": rel(INTERNAL_GATE),
            "ten_row_internal_external_source_decision_ledger": rel(ROW_LEDGER),
            "controlled_external_source_import_decision": rel(EXTERNAL_DECISION),
            "source_selected_threshold_functional_execution_workorder": rel(WORKORDER),
            "next_cutset_after_internal_external_decision": rel(CUTSET),
        },
        "closure_decision": decision,
        "previous_status": previous["status"],
        "readiness_fraction": readiness["readiness_fraction"],
        "only_remaining_readiness_blocker": readiness["only_remaining_readiness_blocker"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "supporting_kernel_status": noknob_kernel["status"],
        "direct_internal_rtheta_status": internal_rtheta["status"],
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_InternalThresholdResponseFunctionalValueRows_or_ExternalSourceImportDecision_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        **decision,
        "readiness_fraction": readiness["readiness_fraction"],
        "only_remaining_readiness_blocker": readiness["only_remaining_readiness_blocker"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected InternalThresholdResponseFunctionalValueRows or ExternalSourceImportDecision v1

Status: `{STATUS}`.

This packet closes the row-tier decision boundary after the threshold-anchor
search.

```text
Rtheta readiness                         : {readiness["readiness_fraction"]}
only readiness blocker                   : {readiness["only_remaining_readiness_blocker"]}
internal selected scalar rows             : {internal_accepted_count}
admitted replay/postcheck rows            : {external_available_count}
external import selected for no-knob      : false
full no-knob closure                      : false
```

The external lane is available only as a controlled empirical layer. It may be
used for SM-parity/admitted-replay comparison or as an explicit empirical import
standard, but it cannot select the source branch and cannot prove no-knob value
derivation.

The next constructive target is:

`{NEXT}`

That target must execute source-selected `L_rowlocal.*`, `T_scheme.*`, and
`lambda_H` rows before observed values enter as postchecks.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
