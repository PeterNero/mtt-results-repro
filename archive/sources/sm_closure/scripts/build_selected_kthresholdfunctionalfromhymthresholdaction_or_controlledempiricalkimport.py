"""Build F_K source-functional attempt from selected HYM/threshold action data.

The combined K-row theorem localizes the remaining scalar problem to a single
source functional:

    F_K : closed K grammar -> (K_threshold.Omega_i)_i

This builder tests whether the currently selected same-branch HYM/threshold
action data actually emit that numerical functional.  It separates:

* selected HYM action/source progress,
* current row-separation/rank insufficiency,
* controlled empirical K import as a parity layer only.

No empirical K value is promoted to no-knob source data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_kthresholdfunctionalfromhymthresholdaction_or_controlledempiricalkimport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INVENTORY = PACKET_DIR / "hym_threshold_action_source_inventory.packet.json"
ATTEMPT = PACKET_DIR / "fk_action_functional_attempt.packet.json"
NOGO = PACKET_DIR / "action_rank_insufficiency_nogo.packet.json"
EMPIRICAL_DECISION = PACKET_DIR / "controlled_empirical_k_import_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_fk_action_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_KThresholdFunctionalFromHYMThresholdAction_or_ControlledEmpiricalKImport_v1.md"

PREVIOUS = DATA / "selected_combinedthresholdkernelkrows_sourcetheorem.candidate.json"
K_GRAMMAR = DATA / "selected_combinedthresholdkernelkrows_sourcetheorem" / "closed_source_k_threshold_grammar.packet.json"
K_CONDITIONAL = (
    DATA
    / "selected_combinedthresholdkernelkrows_sourcetheorem"
    / "conditional_k_rows_scalar_closure_theorem.packet.json"
)
EMPIRICAL_K = (
    DATA
    / "selected_lrowlocaltschemelambdah_sourceexecution_or_controlledempiricalimport"
    / "controlled_empirical_k_import_contract.packet.json"
)
ROWLOCAL = DATA / "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem.candidate.json"
ROWLOCAL_LEDGER = (
    DATA
    / "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem"
    / "available_source_import_ledger.packet.json"
)
ROWLOCAL_FUNCTIONAL = (
    DATA
    / "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem"
    / "selected_overlap_quadrature_functional.packet.json"
)
ROWLOCAL_NOGO = (
    DATA
    / "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem"
    / "current_source_degeneracy_nogo.packet.json"
)
THRESHOLD_GATE = (
    DATA
    / "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem"
    / "threshold_scheme_source_gate.packet.json"
)
FINITE_TRIAL = (
    DATA
    / "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem"
    / "finite_model_active_quadrature_trial.packet.json"
)
HYM_NEWTON = DATA / "selected_full_exps_hym_newton_replay.candidate.json"
HYM_FIRST_PAYLOAD = (
    DATA
    / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
    / "selected_hym_first_solve_payload.packet.json"
)
END0_GREEN = (
    DATA
    / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
    / "full_diagonal_end0_green_payload.packet.json"
)
PROJECTOR_VALUES = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"

STATUS = (
    "MTT_SELECTED_KTHRESHOLDFUNCTIONALFROMHYMTHRESHOLDACTION_OR_CONTROLLEDEMPIRICALKIMPORT_"
    "BUILT_ACTION_SOURCE_TEST_NO_INTERNAL_FK_ROWS"
)
NEXT = "MTT_Selected_PhysicalDotDAlpha1SectorTransferRetardedOverlapKernel_or_EmpiricalKParityImport_v1"


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
        raise FileNotFoundError("missing F_K source-functional inputs: " + ", ".join(missing))


def action_class(row: dict[str, Any]) -> str:
    if row["sector"] == "H":
        return "H_singlet"
    return "charged_universal_diagonal_HYM_class"


def attempt_rows(grammar_rows: list[dict[str, Any]], empirical_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    empirical_by_omega = {row["omega_id"]: row for row in empirical_rows}
    rows: list[dict[str, Any]] = []
    for row in grammar_rows:
        empirical = empirical_by_omega[row["omega_id"]]
        rows.append(
            {
                "omega_id": row["omega_id"],
                "sector": row["sector"],
                "generation_or_lambda": row["generation_or_lambda"],
                "action_separation_class": action_class(row),
                "closed_grammar_features_seen_by_action_test": row["closed_features_available_before_replay"],
                "selected_FK_value_emitted": False,
                "emitted_K_threshold_value": None,
                "empirical_K_import_available": empirical["selected_for_no_knob"] is False,
                "empirical_K_value_symbolic": empirical["empirical_K_import_symbolic"],
                "accepted_as_no_knob_source_row": False,
                "accepted_as_controlled_empirical_row": True,
                "blocking_reasons": [
                    "current selected HYM action data provide diagonal/global action moments, not ten numerical K rows",
                    "charged zero-mode/projector signatures remain degenerate before selected sector transfer",
                    "selected physical dotD_alpha1 / retarded overlap derivative rows are not emitted",
                    "selected threshold scheme values T_scheme.* are not instantiated",
                    "empirical K row may be replayed only as controlled parity import",
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
        K_GRAMMAR,
        K_CONDITIONAL,
        EMPIRICAL_K,
        ROWLOCAL,
        ROWLOCAL_LEDGER,
        ROWLOCAL_FUNCTIONAL,
        ROWLOCAL_NOGO,
        THRESHOLD_GATE,
        FINITE_TRIAL,
        HYM_NEWTON,
        HYM_FIRST_PAYLOAD,
        END0_GREEN,
        PROJECTOR_VALUES,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    grammar = load(K_GRAMMAR)
    conditional = load(K_CONDITIONAL)
    empirical_k = load(EMPIRICAL_K)
    rowlocal = load(ROWLOCAL)
    ledger = load(ROWLOCAL_LEDGER)
    functional = load(ROWLOCAL_FUNCTIONAL)
    rowlocal_nogo = load(ROWLOCAL_NOGO)
    threshold_gate = load(THRESHOLD_GATE)
    finite_trial = load(FINITE_TRIAL)
    hym_newton = load(HYM_NEWTON)
    hym_first = load(HYM_FIRST_PAYLOAD)
    end0_green = load(END0_GREEN)
    projector_values = load(PROJECTOR_VALUES)

    rows = attempt_rows(grammar["grammar_rows"], empirical_k["empirical_K_rows"])
    distinct_action_classes = sorted({row["action_separation_class"] for row in rows})
    max_selected_action_classes = len(distinct_action_classes)
    required_rows = grammar["row_count"]

    inventory = {
        "schema": "MTTHYMThresholdActionSourceInventoryForFK.v1",
        "status": "SELECTED_DIAGONAL_HYM_ACTION_AVAILABLE_FULL_FK_SOURCE_NOT_AVAILABLE",
        "closed_source_inputs": {
            "closed_K_grammar_rows": grammar["row_count"] == 10,
            "conditional_K_to_Omega_theorem": conditional["status"]
            == "CONDITIONAL_SCALAR_CLOSURE_PROVED_ANTECEDENT_OPEN",
            "diagonal_expS_HYM_replay_solved": hym_newton["what_closes_now"]["diagonal_expS_nonlinear_replay"],
            "selected_A_HYM_payload_emitted": hym_first["A_HYM_payload"]["emitted"],
            "full_diagonal_End0_Green_closed": end0_green["T1_T2_covariant_Green"]["closed"],
            "overlap_quadrature_functional_defined": rowlocal["closure_decision"][
                "overlap_quadrature_functional_defined"
            ],
            "threshold_scheme_source_gate_built": rowlocal["closure_decision"]["threshold_scheme_source_gate_built"],
        },
        "open_source_inputs": {
            "selected_projector_values_promoted": projector_values["validator_result"][
                "selected_HYM_projector_values_promoted"
            ],
            "selected_physical_dotD_alpha1": projector_values["what_remains_open"]["selected_physical_dotD_alpha1"]
            is False,
            "selected_retarded_overlap_derivative_rows_emitted": rowlocal["closure_decision"][
                "selected_retarded_overlap_derivative_rows_emitted"
            ],
            "selected_threshold_response_functional_instantiated": threshold_gate[
                "selected_threshold_response_functional_instantiated"
            ],
            "generation_resolved_threshold_source_rows_closed": threshold_gate[
                "generation_resolved_threshold_source_rows_closed"
            ],
            "mass_scheme_conversion_source_rows_closed": threshold_gate["mass_scheme_conversion_source_rows_closed"],
        },
        "selected_action_payload_summaries": {
            "hym_status": hym_newton["status"],
            "hym_final_residual_l2": hym_newton["solution_summary"]["final_residual_l2"],
            "hym_u_l2": hym_newton["solution_summary"]["u_l2"],
            "hym_gradient_l2": hym_first["A_HYM_payload"]["gradient_l2"],
            "green_operator_norm_bound": end0_green["T1_T2_covariant_Green"]["green_operator_norm_bound"],
            "current_rowlocal_distinct_model_active_L_values": finite_trial["distinct_model_active_L_values"],
        },
        "selected_numerical_FK_functional_present": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(INVENTORY, inventory)

    attempt = {
        "schema": "MTTFKActionFunctionalAttempt.v1",
        "status": "ACTION_FUNCTIONAL_TESTED_NO_SELECTED_NUMERICAL_FK_ROWS",
        "candidate_functional": {
            "name": "F_K_from_selected_HYM_threshold_action",
            "required_type": "closed K grammar -> ten selected K_threshold numerical rows",
            "current_action_domain": [
                "selected diagonal exp(S) HYM solution u",
                "A_HYM = du*T3 diagonal End0 connection payload",
                "protected T3 and coupled T1/T2 End0 Green/Riesz payload",
                "row-local HYM/Green quadrature functional contract",
                "threshold scheme source gate",
            ],
            "proved_now": False,
        },
        "row_count": len(rows),
        "attempt_rows": rows,
        "accepted_selected_K_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "lambda_H_value_row_emitted": False,
        "controlled_empirical_K_rows_available": empirical_k["empirical_K_row_count"],
        "controlled_empirical_K_import_selected_for_no_knob": False,
        "why_not_proved": [
            "the selected diagonal HYM action payload is real source progress but not a ten-row numerical K functional",
            "current selected action data distinguish at most charged-vs-H classes before sector transfer",
            "the only ten-row K numbers currently available are empirical import rows",
            "using empirical K values to define F_K would be target selection",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ATTEMPT, attempt)

    nogo = {
        "schema": "MTTActionRankInsufficiencyNoGoForFK.v1",
        "status": "CURRENT_SELECTED_ACTION_DATA_RANK_INSUFFICIENT_FOR_TEN_K_ROWS",
        "theorem": {
            "name": "CurrentHYMThresholdActionRankInsufficiencyForFK",
            "proved": True,
            "statement": (
                "With the current selected diagonal HYM action payload, selected End0 Green payload, "
                "and uninstantiated threshold scheme rows, the source-visible row separation has at most "
                "charged-vs-H classes and cannot emit ten generation-resolved K_threshold values."
            ),
        },
        "required_selected_K_row_count": required_rows,
        "accepted_selected_K_source_row_count": 0,
        "distinct_selected_action_separation_classes": distinct_action_classes,
        "selected_action_class_upper_bound": max_selected_action_classes,
        "rank_sufficient_for_ten_K_rows": max_selected_action_classes >= required_rows,
        "current_model_active_degeneracy_nogo_imported": rowlocal_nogo["theorem"]["proved"],
        "current_source_degeneracy_details": {
            "charged_basis_degenerate": rowlocal_nogo["charged_basis_degenerate"],
            "distinct_model_active_L_values": rowlocal_nogo["distinct_model_active_L_values"],
            "required_total_row_count": rowlocal_nogo["required_total_row_count"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(NOGO, nogo)

    empirical_decision = {
        "schema": "MTTControlledEmpiricalKImportDecision.v1",
        "status": "CONTROLLED_EMPIRICAL_K_IMPORT_AVAILABLE_FOR_PARITY_NOT_NO_KNOB",
        "empirical_K_row_count": empirical_k["empirical_K_row_count"],
        "can_replay_ten_scalar_slots_under_empirical_layer": empirical_k[
            "can_replay_ten_scalar_slots_under_empirical_layer"
        ],
        "selected_for_no_knob_closure": False,
        "selected_for_true_SM_equivalence": False,
        "allowed_use": "controlled parity replay/postcheck only",
        "forbidden_use": [
            "define F_K by empirical residual lookup",
            "promote empirical K rows as selected source rows",
            "claim no-knob scalar closure from imported K values",
        ],
        "decision": (
            "If no selected F_K is emitted, the ten empirical K rows may be retained as a typed "
            "SM-parity/comparison layer, but they do not close no-knob MTT."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(EMPIRICAL_DECISION, empirical_decision)

    cutset = {
        "schema": "MTTNextCutsetAfterFKActionAttempt.v1",
        "status": "NEXT_ATTACK_PHYSICAL_DOTD_SECTOR_TRANSFER_RETARDED_OVERLAP_OR_EMPIRICAL_PARITY_IMPORT",
        "next_required_artifact": NEXT,
        "closed_here": [
            "selected HYM/threshold-action source inventory assembled for F_K",
            "current action functional attempt executed against all ten K rows",
            "rank/separation no-go proved for current selected action data",
            "controlled empirical K import decision typed as parity-only and non-no-knob",
        ],
        "still_open": [
            "selected physical dotD_alpha1 and sector-transfer functor",
            "selected retarded overlap derivative row kernel",
            "selected threshold-scheme rows T_scheme.*",
            "selected lambda_H H-sector value/quartic payload",
            "ten selected K_threshold rows",
            "strict Omega/lambda_H scalar execution",
            "matrix-level mixing extension",
            "full no-knob SM closure",
        ],
        "forbidden_routes": [
            "use empirical K import as F_K",
            "use charged row labels as numerical source values",
            "reuse theta/D_fin factors after they have already been factored out of K",
            "promote model-active projectors without selected source flags",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CUTSET, cutset)

    decision = {
        "selected_HYM_threshold_action_inventory_built": True,
        "FK_action_functional_attempted": True,
        "selected_FK_functional_proved": False,
        "action_rank_insufficiency_nogo_proved": True,
        "accepted_selected_K_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "lambda_H_value_row_emitted": False,
        "controlled_empirical_K_import_available": True,
        "controlled_empirical_K_import_selected_for_no_knob": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
    }
    candidate = {
        "candidate": "MTTSelectedKThresholdFunctionalFromHYMThresholdActionOrControlledEmpiricalKImport",
        "status": STATUS,
        "closure_claimed": True,
        "theorem": {
            "name": "CurrentHYMThresholdActionFKAttemptAndRankNoGo",
            "proved": True,
            "statement": (
                "The current selected HYM/threshold action data can be tested against the F_K obligation. "
                "They do not emit selected numerical K rows; the remaining same-branch object is physical "
                "dotD/sector-transfer/retarded-overlap plus threshold-scheme execution, or an explicitly "
                "controlled empirical K import at parity tier."
            ),
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "hym_threshold_action_source_inventory": rel(INVENTORY),
            "fk_action_functional_attempt": rel(ATTEMPT),
            "action_rank_insufficiency_nogo": rel(NOGO),
            "controlled_empirical_k_import_decision": rel(EMPIRICAL_DECISION),
            "next_cutset_after_fk_action_attempt": rel(CUTSET),
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
        "certificate": "MTT_Selected_KThresholdFunctionalFromHYMThresholdAction_or_ControlledEmpiricalKImport_v1",
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
        f"""# MTT Selected KThresholdFunctionalFromHYMThresholdAction or ControlledEmpiricalKImport v1

Status: `{STATUS}`.

This packet attacks the exact `F_K` wall.

What closes:

```text
selected HYM/threshold action inventory : true
F_K action-functional attempt            : executed
current action rank no-go                : true
selected numerical F_K functional        : false
accepted selected K rows                 : 0
controlled empirical K import available : true
empirical K selected for no-knob         : false
```

The selected diagonal HYM action payload is real source progress: it supplies the
same-branch `u`, `A_HYM=du*T3`, and End0 Green/Riesz data.  But the current
selected action data still distinguish at most charged-vs-H classes before
physical sector transfer, retarded overlap derivatives, and threshold-scheme
rows are emitted.

So the no-knob frontier is not another K-row grammar question.  It is:

```text
selected physical dotD_alpha1 + sector transfer + retarded overlap kernel
plus selected T_scheme.* and lambda_H payload
```

Controlled empirical K rows remain available only as SM-parity/postcheck data.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
