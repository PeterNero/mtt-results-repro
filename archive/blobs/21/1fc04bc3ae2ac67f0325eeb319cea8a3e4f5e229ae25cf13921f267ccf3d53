"""Build L_rowlocal/T_scheme/lambda_H source execution or controlled import.

The previous packet fixed the internal-vs-external decision boundary.  This
one presses the constructive lane by reducing the scalar execution problem to
the product rows that actually enter the Omega formula:

    K_i = L_rowlocal_i * T_scheme_i

The split between L_rowlocal and T_scheme remains important provenance, but the
ten scalar rows need only the selected product K_i once D_fin and theta weights
are closed.  Current source data do not select K_i, so the controlled empirical
K import is recorded as a non-no-knob fallback.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_lrowlocaltschemelambdah_sourceexecution_or_controlledempiricalimport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PRODUCT_CONTRACT = PACKET_DIR / "combined_threshold_kernel_k_row_contract.packet.json"
SOURCE_ATTEMPT = PACKET_DIR / "source_selected_k_row_execution_attempt.packet.json"
EMPIRICAL_IMPORT = PACKET_DIR / "controlled_empirical_k_import_contract.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_k_product_reduction.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LRowlocalTSchemeLambdaH_SourceExecution_or_ControlledEmpiricalImport_v1.md"

PREVIOUS = DATA / "selected_internalthresholdresponsefunctionalvaluerows_or_externalsourceimportdecision.candidate.json"
ROW_LEDGER = (
    DATA
    / "selected_internalthresholdresponsefunctionalvaluerows_or_externalsourceimportdecision"
    / "ten_row_internal_external_source_decision_ledger.packet.json"
)
WORKORDER = (
    DATA
    / "selected_internalthresholdresponsefunctionalvaluerows_or_externalsourceimportdecision"
    / "source_selected_threshold_functional_execution_workorder.packet.json"
)
EXTERNAL_DECISION = (
    DATA
    / "selected_internalthresholdresponsefunctionalvaluerows_or_externalsourceimportdecision"
    / "controlled_external_source_import_decision.packet.json"
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
ROWLOCAL_SEARCH = DATA / "selected_rowlocalthresholdvaluerows_or_lambdahprefactorexecution.candidate.json"

STATUS = (
    "MTT_SELECTED_LROWLOCALTSCHEMELAMBDAH_SOURCEEXECUTION_OR_CONTROLLEDEMPIRICALIMPORT_"
    "BUILT_PRODUCT_REDUCTION_SOURCE_K_ROWS_OPEN"
)
NEXT = "MTT_Selected_CombinedThresholdKernelKRows_SourceTheorem_v1"


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
        raise FileNotFoundError("missing K-product reduction inputs: " + ", ".join(missing))


def by_omega(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {row["omega_id"]: row for row in rows}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        ROW_LEDGER,
        WORKORDER,
        EXTERNAL_DECISION,
        TARGETS,
        FORMULAS,
        FACTORS,
        ROWLOCAL_SEARCH,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    row_ledger = load(ROW_LEDGER)
    workorder = load(WORKORDER)
    external_decision = load(EXTERNAL_DECISION)
    targets = load(TARGETS)
    formulas = load(FORMULAS)
    factors = load(FACTORS)
    rowlocal_search = load(ROWLOCAL_SEARCH)

    formula_by_omega = by_omega(formulas["formula_rows"])
    factor_by_omega = by_omega(factors["factor_rows"])

    k_rows: list[dict[str, Any]] = []
    empirical_rows: list[dict[str, Any]] = []
    for target in targets["target_rows"]:
        omega_id = target["omega_id"]
        factor = factor_by_omega[omega_id]
        formula = formula_by_omega[omega_id]
        k_id = "K_threshold." + omega_id
        k_definition = (
            f"{k_id} = {factor['row_local_overlap_threshold_factor_id']} * "
            f"{factor['scale_scheme_factor_id']}"
        )
        empirical_symbolic = target["rowlocal_composite_target_symbolic"]
        k_rows.append(
            {
                "omega_id": omega_id,
                "combined_kernel_row_id": k_id,
                "definition": k_definition,
                "sector": target["sector"],
                "generation_or_lambda": target["generation_or_lambda"],
                "finite_heat_torsion_subfactor_id": factor["finite_heat_torsion_subfactor_id"],
                "theta_exponent": target["theta_exponent"],
                "omega_formula": formula["formula"],
                "product_sufficient_for_scalar_execution": True,
                "split_L_T_required_before_scalar_execution": False,
                "split_L_T_required_for_provenance_refinement": True,
                "internal_selected_K_row_accepted": False,
                "empirical_K_import_available": True,
                "empirical_K_import_symbolic": empirical_symbolic,
                "source_theorem_required": (
                    "same-branch source theorem emits this combined K row before observed "
                    "Yukawa/Higgs replay values enter"
                ),
                "why_open": [
                    "no selected source functional currently emits K_i",
                    "available exact replay is target-pinned postcheck data",
                    "row-local and threshold-scheme factors have not been source-selected",
                ],
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )
        empirical_rows.append(
            {
                "omega_id": omega_id,
                "combined_kernel_row_id": k_id,
                "empirical_K_import_symbolic": empirical_symbolic,
                "source_value_tier": target["source_value_tier"],
                "selected_for_no_knob": False,
                "selected_for_true_SM_equivalence": False,
                "allowed_use": "controlled empirical replay/import only",
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )

    product_contract = {
        "schema": "MTTCombinedThresholdKernelKRowContract.v1",
        "status": "TEN_COMBINED_K_ROWS_DEFINED_SOURCE_SELECTION_OPEN",
        "row_formula_before_reduction": workorder["functional_contract"]["row_formula"],
        "reduced_row_formula": "Omega_i = D_fin[class(i)] * K_threshold_i * exp(-2*pi*n_i)",
        "combined_kernel_definition": "K_threshold_i = L_rowlocal_i * T_scheme_i",
        "row_count": len(k_rows),
        "combined_kernel_rows": k_rows,
        "accepted_combined_K_source_row_count": 0,
        "product_reduction_closed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(PRODUCT_CONTRACT, product_contract)

    source_attempt = {
        "schema": "MTTSourceSelectedKRowExecutionAttempt.v1",
        "status": "SOURCE_SELECTED_K_ROWS_NOT_EMITTED",
        "closed_support": {
            "theta_exponents_closed": True,
            "finite_heat_torsion_D_fin_closed": True,
            "omega_formula_skeleton_closed": formulas["accepted_formula_skeleton_row_count"] == 10,
            "internal_external_decision_boundary_closed": previous["closure_decision"][
                "ten_row_decision_ledger_built"
            ],
            "product_reduction_closed": True,
        },
        "accepted_combined_K_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "lambda_H_value_row_emitted": False,
        "best_prior_target_scored_search_error_factor": rowlocal_search[
            "best_rational_diagnostic_candidate"
        ]["max_multiplicative_error_factor"],
        "why_not_emitted": [
            "current source data select D_fin and theta exponents, not K_threshold_i",
            "prior brute-force laws are target-scored diagnostics and remain forbidden",
            "controlled empirical K rows are import data, not source-selected rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SOURCE_ATTEMPT, source_attempt)

    empirical_import = {
        "schema": "MTTControlledEmpiricalKImportContract.v1",
        "status": "EMPIRICAL_K_ROWS_AVAILABLE_NOT_NOKNOB",
        "external_import_lane_available": external_decision["external_import_lane_available"],
        "empirical_K_row_count": len(empirical_rows),
        "empirical_K_rows": empirical_rows,
        "can_replay_ten_scalar_slots_under_empirical_layer": True,
        "selected_for_no_knob_closure": False,
        "selected_for_true_SM_equivalence": False,
        "empirical_layer_label": "controlled K-row import",
        "guardrail": (
            "Choosing this lane makes the result an empirical/parity-layer replay. It must not be "
            "reported as selected no-knob MTT value derivation."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(EMPIRICAL_IMPORT, empirical_import)

    cutset = {
        "schema": "MTTNextCutsetAfterKProductReduction.v1",
        "status": "NEXT_ATTACK_SOURCE_THEOREM_FOR_COMBINED_K_ROWS",
        "next_required_artifact": NEXT,
        "closed_here": [
            "L_rowlocal/T_scheme split reduced to combined K_threshold rows for scalar execution",
            "ten empirical K rows typed as controlled import data",
            "source-selected K execution attempted with zero accepted source rows",
            "target-scored row laws remain quarantined",
        ],
        "still_open": [
            "selected source theorem for ten K_threshold rows",
            "selected H-sector K row emitting lambda_H",
            "strict Omega acceptance after K rows emit",
            "matrix-level CKM/offdiagonal mixing extension",
            "full no-knob SM closure",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CUTSET, cutset)

    decision = {
        "product_reduction_closed": True,
        "combined_K_row_contract_built": True,
        "source_selected_K_execution_attempted": True,
        "accepted_combined_K_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "lambda_H_value_row_emitted": False,
        "controlled_empirical_K_import_available": True,
        "controlled_empirical_K_import_selected_for_no_knob": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
    }
    candidate = {
        "candidate": "MTTSelectedLRowlocalTSchemeLambdaHSourceExecutionOrControlledEmpiricalImport",
        "status": STATUS,
        "closure_claimed": True,
        "theorem": {
            "name": "CombinedThresholdKernelProductReductionTheorem",
            "proved": True,
            "statement": (
                "For scalar Omega execution, the separate L_rowlocal and T_scheme factors can be "
                "reduced to combined source rows K_threshold_i = L_rowlocal_i*T_scheme_i. Current "
                "selected source data do not emit any K_threshold row, while empirical K rows can be "
                "typed only as a controlled import layer. Therefore no-knob closure is reduced to a "
                "source theorem for the ten combined K rows."
            ),
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "combined_threshold_kernel_k_row_contract": rel(PRODUCT_CONTRACT),
            "source_selected_k_row_execution_attempt": rel(SOURCE_ATTEMPT),
            "controlled_empirical_k_import_contract": rel(EMPIRICAL_IMPORT),
            "next_cutset_after_k_product_reduction": rel(CUTSET),
        },
        "closure_decision": decision,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_LRowlocalTSchemeLambdaH_SourceExecution_or_ControlledEmpiricalImport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        **decision,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected LRowlocalTSchemeLambdaH SourceExecution or ControlledEmpiricalImport v1

Status: `{STATUS}`.

The scalar value problem has been reduced:

```text
before : Omega_i = D_fin[class(i)] * L_rowlocal_i * T_scheme_i * exp(-2*pi*n_i)
after  : Omega_i = D_fin[class(i)] * K_threshold_i * exp(-2*pi*n_i)
where  : K_threshold_i = L_rowlocal_i * T_scheme_i
```

This closes a useful simplification, but not no-knob values.

```text
combined K source rows accepted : 0
internal scalar rows accepted    : 0
empirical K import available     : true
empirical K selected for no-knob  : false
```

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
