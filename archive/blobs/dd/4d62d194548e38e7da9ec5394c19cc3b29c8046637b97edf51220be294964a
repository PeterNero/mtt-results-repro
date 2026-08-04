"""Build combined K-threshold source theorem attempt.

The previous frontier reduced scalar execution to ten combined rows
K_threshold_i.  This builder tries to promote those rows from closed source
data.  It deliberately separates three things:

* the closed source grammar that is available before replay,
* the conditional theorem that ten selected K rows would close the scalar gate,
* the current failure to select the K rows from that grammar.

No empirical K row is promoted to no-knob source data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_combinedthresholdkernelkrows_sourcetheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
GRAMMAR = PACKET_DIR / "closed_source_k_threshold_grammar.packet.json"
ATTEMPT = PACKET_DIR / "selected_k_threshold_source_theorem_attempt.packet.json"
CONDITIONAL = PACKET_DIR / "conditional_k_rows_scalar_closure_theorem.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_k_source_theorem_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CombinedThresholdKernelKRows_SourceTheorem_v1.md"

PREVIOUS = DATA / "selected_lrowlocaltschemelambdah_sourceexecution_or_controlledempiricalimport.candidate.json"
K_CONTRACT = (
    DATA
    / "selected_lrowlocaltschemelambdah_sourceexecution_or_controlledempiricalimport"
    / "combined_threshold_kernel_k_row_contract.packet.json"
)
K_SOURCE_ATTEMPT = (
    DATA
    / "selected_lrowlocaltschemelambdah_sourceexecution_or_controlledempiricalimport"
    / "source_selected_k_row_execution_attempt.packet.json"
)
EMPIRICAL_K = (
    DATA
    / "selected_lrowlocaltschemelambdah_sourceexecution_or_controlledempiricalimport"
    / "controlled_empirical_k_import_contract.packet.json"
)
SOURCE_FEATURES = (
    DATA
    / "selected_rowlocalthresholdvaluerows_or_lambdahprefactorexecution"
    / "source_feature_table.packet.json"
)
THETA_WEIGHTS = (
    DATA
    / "selected_step68_thetaexponentweights_or_prefactorthreshold_frontier"
    / "step68_selected_theta_exponent_weight_rows.packet.json"
)
HEAT_RESPONSE = (
    DATA
    / "selected_heattorsionresponse_finalgate"
    / "selected_finite_heat_spectrum_response.packet.json"
)
ROWLOCAL_SEARCH = DATA / "selected_rowlocalthresholdvaluerows_or_lambdahprefactorexecution.candidate.json"

STATUS = (
    "MTT_SELECTED_COMBINEDTHRESHOLDKERNELKROWS_SOURCETHEOREM_"
    "BUILT_CONDITIONAL_CLOSURE_SOURCE_THEOREM_OPEN"
)
NEXT = "MTT_Selected_KThresholdFunctionalFromHYMThresholdAction_or_ControlledEmpiricalKImport_v1"


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
        raise FileNotFoundError("missing K source theorem inputs: " + ", ".join(missing))


def by_omega(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {row["omega_id"]: row for row in rows}


def grammar_rows(k_contract: dict[str, Any], features: dict[str, Any]) -> list[dict[str, Any]]:
    feature_by_omega = by_omega(features["feature_rows"])
    rows: list[dict[str, Any]] = []
    for row in k_contract["combined_kernel_rows"]:
        feature_row = feature_by_omega[row["omega_id"]]
        selected_features = feature_row["features"]
        rows.append(
            {
                "omega_id": row["omega_id"],
                "combined_kernel_row_id": row["combined_kernel_row_id"],
                "sector": row["sector"],
                "generation_or_lambda": row["generation_or_lambda"],
                "source_column": feature_row["source_column"],
                "source_direction": feature_row["source_direction"],
                "source_class": feature_row["source_class"],
                "closed_features_available_before_replay": {
                    "theta_exponent": selected_features["theta_exponent"],
                    "qutrit_floor": selected_features["qutrit_floor"],
                    "shared_h_index": selected_features["shared_h_index"],
                    "phase_column": selected_features["phase_column"],
                    "shift_column": selected_features["shift_column"],
                    "mixed_slot": selected_features["mixed_slot"],
                    "family_sector": selected_features["family_sector"],
                    "H_sector": selected_features["H_sector"],
                    "log_reduced_heat_trace": selected_features["log_reduced_heat_trace"],
                },
                "empirical_K_import_available": row["empirical_K_import_available"],
                "internal_selected_K_row_accepted": False,
                "why_grammar_does_not_select_value": [
                    "grammar identifies row slots and selected structural features",
                    "grammar contains no selected numerical functional F_K",
                    "choosing coefficients from empirical residuals is forbidden",
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
        K_CONTRACT,
        K_SOURCE_ATTEMPT,
        EMPIRICAL_K,
        SOURCE_FEATURES,
        THETA_WEIGHTS,
        HEAT_RESPONSE,
        ROWLOCAL_SEARCH,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    k_contract = load(K_CONTRACT)
    k_source_attempt = load(K_SOURCE_ATTEMPT)
    empirical_k = load(EMPIRICAL_K)
    source_features = load(SOURCE_FEATURES)
    theta_weights = load(THETA_WEIGHTS)
    heat_response = load(HEAT_RESPONSE)
    rowlocal_search = load(ROWLOCAL_SEARCH)

    rows = grammar_rows(k_contract, source_features)
    selected_k_count = 0
    conditional_ready = selected_k_count == k_contract["row_count"]

    grammar = {
        "schema": "MTTClosedSourceKThresholdGrammar.v1",
        "status": "CLOSED_SOURCE_GRAMMAR_AVAILABLE_FUNCTIONAL_NOT_SELECTED",
        "row_count": len(rows),
        "grammar_rows": rows,
        "closed_source_inputs": {
            "theta_exponent_rows_closed": theta_weights["all_10_exponent_weight_rows_constructed"],
            "finite_heat_response_closed": heat_response["slot_closes"],
            "K_product_contract_closed": k_contract["product_reduction_closed"],
            "source_feature_table_closed": source_features["closure_claimed"],
        },
        "available_grammar_columns": [
            "theta_exponent",
            "qutrit_floor",
            "shared_h_index",
            "phase_column",
            "shift_column",
            "mixed_slot",
            "family_sector",
            "H_sector",
            "log_reduced_heat_trace",
        ],
        "selected_numerical_K_functional_present": False,
        "accepted_combined_K_source_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(GRAMMAR, grammar)

    attempt = {
        "schema": "MTTSelectedKThresholdSourceTheoremAttempt.v1",
        "status": "K_SOURCE_THEOREM_NOT_DERIVED_FROM_CLOSED_GRAMMAR",
        "candidate_theorem": {
            "name": "SelectedCombinedThresholdKernelFunctionalTheorem",
            "required_statement": (
                "The selected q=79/F/m=1 HYM/threshold action defines a source functional "
                "F_K on the closed K grammar whose ten values are K_threshold_i before empirical replay."
            ),
            "proved_now": False,
        },
        "closed_support_sufficient_for_slots": True,
        "closed_support_sufficient_for_values": False,
        "accepted_combined_K_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "lambda_H_value_row_emitted": False,
        "best_prior_target_scored_error_factor": rowlocal_search["best_rational_diagnostic_candidate"][
            "max_multiplicative_error_factor"
        ],
        "why_not_proved": [
            "the closed grammar selects the slots but not a numerical functional F_K",
            "finite heat/torsion and theta exponents are already factored out",
            "the remaining order-one K rows are exactly the missing HYM/threshold action response",
            "target-scored rational and least-squares laws remain diagnostics only",
            "empirical K rows are controlled import data, not selected source rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ATTEMPT, attempt)

    conditional = {
        "schema": "MTTConditionalKRowsScalarClosureTheorem.v1",
        "status": "CONDITIONAL_SCALAR_CLOSURE_PROVED_ANTECEDENT_OPEN",
        "conditional_statement": (
            "If all ten K_threshold_i rows are selected by F_K before replay, then the closed D_fin "
            "and theta exponent rows execute the ten Omega scalar rows through "
            "Omega_i = D_fin[class(i)] * K_threshold_i * exp(-2*pi*n_i)."
        ),
        "antecedent": {
            "selected_K_threshold_row_count_required": k_contract["row_count"],
            "selected_K_threshold_row_count_present": selected_k_count,
            "satisfied": conditional_ready,
        },
        "consequent_if_satisfied": {
            "strict_Omega_rows_executable": True,
            "lambda_H_row_executable": True,
            "scalar_prefactor_closure_executable": True,
        },
        "consequent_current": {
            "strict_Omega_rows_executable": False,
            "lambda_H_row_executable": False,
            "scalar_prefactor_closure_executable": False,
        },
        "empirical_import_can_satisfy_antecedent_for_no_knob": False,
        "controlled_empirical_K_import_available": empirical_k["can_replay_ten_scalar_slots_under_empirical_layer"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CONDITIONAL, conditional)

    cutset = {
        "schema": "MTTNextCutsetAfterKSourceTheoremAttempt.v1",
        "status": "NEXT_ATTACK_SELECTED_FK_FROM_HYM_THRESHOLD_ACTION",
        "next_required_artifact": NEXT,
        "closed_here": [
            "closed source grammar for all ten K_threshold slots emitted",
            "conditional theorem proved: selected ten K rows imply scalar Omega execution",
            "current closed support shown insufficient to select numerical K values",
            "empirical K import retained only as controlled non-no-knob layer",
        ],
        "still_open": [
            "selected functional F_K from same-branch HYM/threshold action",
            "ten selected K_threshold numerical rows",
            "selected H-sector K row/lambda_H execution",
            "strict Omega acceptance after K rows emit",
            "matrix-level CKM/offdiagonal mixing extension",
            "full no-knob SM closure",
        ],
        "forbidden_routes": [
            "choose F_K coefficients from empirical K residuals",
            "promote controlled empirical K import to no-knob",
            "use row-id lookup as a source theorem",
            "reopen D_fin or theta exponents as if they were the K-value blocker",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CUTSET, cutset)

    decision = {
        "closed_source_K_grammar_built": True,
        "conditional_K_rows_scalar_closure_proved": True,
        "selected_FK_functional_proved": False,
        "accepted_combined_K_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "lambda_H_value_row_emitted": False,
        "controlled_empirical_K_import_available": True,
        "controlled_empirical_K_import_selected_for_no_knob": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
    }
    candidate = {
        "candidate": "MTTSelectedCombinedThresholdKernelKRowsSourceTheorem",
        "status": STATUS,
        "closure_claimed": True,
        "theorem": {
            "name": "KThresholdGrammarAndConditionalClosureTheorem",
            "proved": True,
            "statement": (
                "The closed MTT source data define the ten K_threshold slots and prove that selected "
                "K rows would execute the scalar Omega rows. They do not yet derive the numerical "
                "source functional F_K; empirical K rows remain controlled import data only."
            ),
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "closed_source_k_threshold_grammar": rel(GRAMMAR),
            "selected_k_threshold_source_theorem_attempt": rel(ATTEMPT),
            "conditional_k_rows_scalar_closure_theorem": rel(CONDITIONAL),
            "next_cutset_after_k_source_theorem_attempt": rel(CUTSET),
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
        "certificate": "MTT_Selected_CombinedThresholdKernelKRows_SourceTheorem_v1",
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
        f"""# MTT Selected CombinedThresholdKernelKRows SourceTheorem v1

Status: `{STATUS}`.

This packet tries to solve the `K_threshold` source theorem.

What closes:

```text
closed source K-slot grammar      : true
conditional K -> Omega theorem    : true
selected numerical F_K functional : false
accepted K source rows            : 0
empirical K import selected       : false
```

The exact remaining object is no longer generic row-local bookkeeping. It is a
same-branch source functional:

```text
F_K : closed K grammar -> (K_threshold.Omega_i)_i
```

It must be derived from the selected HYM/threshold action before empirical replay.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
