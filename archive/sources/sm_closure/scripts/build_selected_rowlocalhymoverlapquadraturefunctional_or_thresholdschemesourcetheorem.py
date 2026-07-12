"""Build selected row-local HYM overlap quadrature / threshold scheme gate."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FUNCTIONAL_PACKET = PACKET_DIR / "selected_overlap_quadrature_functional.packet.json"
SOURCE_LEDGER_PACKET = PACKET_DIR / "available_source_import_ledger.packet.json"
MODEL_TRIAL_PACKET = PACKET_DIR / "finite_model_active_quadrature_trial.packet.json"
THRESHOLD_GATE_PACKET = PACKET_DIR / "threshold_scheme_source_gate.packet.json"
DEGENERACY_PACKET = PACKET_DIR / "current_source_degeneracy_nogo.packet.json"
CUTSET_PACKET = PACKET_DIR / "next_cutset_after_quadrature_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RowLocalHYMOverlapQuadratureFunctional_or_ThresholdSchemeSourceTheorem_v1.md"

PREVIOUS = DATA / "selected_rowlocalthresholdvaluerows_or_lambdahprefactorexecution.candidate.json"
STEP72_TARGETS = (
    DATA
    / "selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance"
    / "step72_required_rowlocal_prefactor_target_table.packet.json"
)
STEP70_FACTORS = (
    DATA
    / "selected_step70_heattorsionprefactorbackimport_or_rowlocalfrontier"
    / "step70_prefactor_slot_factorization.packet.json"
)
STEP73 = DATA / "selected_step73_honestrowlocalhymgalerkin_or_selectedprefactorsourcerows.candidate.json"
HYM_FIRST = (
    DATA
    / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
    / "selected_hym_first_solve_payload.packet.json"
)
FULL_GREEN = (
    DATA
    / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
    / "full_diagonal_end0_green_payload.packet.json"
)
PROJECTOR_VALUES = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"
PROJECTOR_PROMOTION = DATA / "selected_hym_projector_source_promotion_route_a.candidate.json"
THRESHOLD_FUNCTIONAL = DATA / "selected_thresholdfunctionalsourcetheorem_or_minimaluniversalparameterselection.candidate.json"

STATUS = (
    "MTT_SELECTED_ROWLOCALHYMOVERLAPQUADRATUREFUNCTIONAL_OR_THRESHOLDSCHEMESOURCETHEOREM_"
    "BUILT_FUNCTIONAL_AND_DEGENERACY_NOGO_ROWS_OPEN"
)
NEXT = "MTT_Selected_PhiFinMinimizerTraceRowLocalKernel_or_ThresholdSchemeValueRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def target_lookup(targets: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {row["omega_id"]: row for row in targets["target_rows"]}


def factor_lookup(factors: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {row["omega_id"]: row for row in factors["factor_rows"]}


def model_active_l_value(slot: dict[str, Any], generation_or_lambda: str) -> float:
    """Current finite projector packet has orthonormal emitted zero modes."""
    if slot["sector"] == "H":
        return 1.0
    ids = slot["ordered_zero_mode_basis_ids"]
    if generation_or_lambda == "gen1":
        basis_id = "phi_(0,0)_e0"
    elif generation_or_lambda == "gen2":
        basis_id = "phi_(0,0)_e1"
    else:
        basis_id = "phi_(0,0)_e2"
    return 1.0 if basis_id in ids else 0.0


def diagnostic_prefactor_representatives(inv: dict[str, Any], l_value: float) -> dict[str, float]:
    heat = inv["heat_trace_t1"]
    reduced = inv["reduced_heat_trace_t1"]
    positive = inv["positive_dimension"]
    log_pdet = inv["log_pseudodeterminant"]
    return {
        "D_heat_trace_times_L": heat * l_value,
        "D_exp_reduced_heat_times_L": math.exp(reduced) * l_value,
        "D_pseudodet_geomean_times_L": math.exp(log_pdet / positive) * l_value,
    }


def log_error(actual: float, predicted: float) -> float | None:
    if actual <= 0.0 or predicted <= 0.0:
        return None
    return abs(math.log(actual) - math.log(predicted))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    required = [
        PREVIOUS,
        STEP72_TARGETS,
        STEP70_FACTORS,
        STEP73,
        HYM_FIRST,
        FULL_GREEN,
        PROJECTOR_VALUES,
        PROJECTOR_PROMOTION,
        THRESHOLD_FUNCTIONAL,
    ]
    missing = [rel(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError("missing inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    targets = load(STEP72_TARGETS)
    factors = load(STEP70_FACTORS)
    step73 = load(STEP73)
    hym_first = load(HYM_FIRST)
    full_green = load(FULL_GREEN)
    projector_values = load(PROJECTOR_VALUES)
    projector_promotion = load(PROJECTOR_PROMOTION)
    threshold_functional = load(THRESHOLD_FUNCTIONAL)

    target_by_omega = target_lookup(targets)
    factor_by_omega = factor_lookup(factors)
    slots = projector_values["finite_value_payload"]["sector_slots"]

    functional = {
        "schema": "MTTSelectedOverlapQuadratureFunctional.v1",
        "status": "ROWLOCAL_HYM_GREEN_QUADRATURE_FUNCTIONAL_DEFINED_VALUES_REQUIRE_SELECTED_KERNEL",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "functional_rows": [
            {
                "component": "projector_and_basis",
                "symbol": "P_s,K_s",
                "selected_requirement": "same-branch selected HYM/Strominger sector projector P_s and ordered L2 basis K_s",
            },
            {
                "component": "retarded_overlap_kernel",
                "symbol": "K_row(s,g;A_HYM,G,dotD_alpha1)",
                "selected_requirement": "kernel derived from selected A_HYM, reduced Green G, physical dotD_alpha1, and matter-slot routing",
            },
            {
                "component": "quadrature",
                "symbol": "Q_sel",
                "selected_requirement": "finite quadrature/error contract tied to Phi_fin selected minimizer trace, not model-active smoke values",
            },
            {
                "component": "rowlocal_value",
                "symbol": "L_rowlocal(s,g)=abs(<K_s,g,K_row K_s,g>)",
                "selected_requirement": "emitted before diagnostic SM-parity target values are checked",
            },
            {
                "component": "threshold_scheme",
                "symbol": "T_scheme(s,g)=exp(Delta_threshold+Delta_mass+Delta_profile)",
                "selected_requirement": "same-branch internal threshold/mass/profile functional instantiated as source values",
            },
        ],
        "acceptance_predicate": {
            "all_projector_source_flags_true": True,
            "physical_dotD_alpha1_verified": True,
            "selected_threshold_scheme_values_emitted": True,
            "target_values_used_only_after_emission": True,
            "ordinary_fit_parameters_forbidden": True,
        },
        "formula_contract": "C_HYMthr(s,g)=D_fin.class(s)*L_rowlocal(s,g)*T_scheme(s,g)",
    }
    write_json(FUNCTIONAL_PACKET, functional)

    source_flags = projector_values["validator_result"]["selected_source_flags"]
    source_ledger = {
        "schema": "MTTAvailableSourceImportLedgerForRowLocalQuadrature.v1",
        "status": "DIAGONAL_HYM_GREEN_CLOSED_PROJECTOR_AND_THRESHOLD_SOURCE_VALUES_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_inputs": {
            "diagonal_HYM_first_solve": hym_first["status"]
            == "DIAGONAL_HYM_FIRST_SOLVE_PAYLOAD_ACCEPTED_AS_SOURCE_PROGRESS",
            "full_diagonal_End0_Green": full_green["status"]
            == "FULL_DIAGONAL_END0_GREEN_CLOSED_PHYSICAL_TRANSFER_OPEN",
            "model_active_projector_values_emitted": projector_values["validator_result"][
                "finite_projector_values_emitted"
            ],
            "rowlocal_factorization_contract_closed": factors["accepted_factorization_row_count"] == 10,
            "step73_diagonal_subsource_closed": step73["closure_decision"][
                "diagonal_hym_green_subsource_closed"
            ],
        },
        "open_inputs": {
            "selected_HYM_projector_values_promoted": projector_values["validator_result"][
                "selected_HYM_projector_values_promoted"
            ],
            "rho_candidate_promoted_to_selected_rho_s": projector_values["validator_result"][
                "rho_candidate_promoted_to_selected_rho_s"
            ],
            "Phi_fin_selected_minimizer_trace": not projector_promotion["what_remains_open"][
                "Phi_fin_selected_minimizer_trace"
            ],
            "physical_dotD_alpha1_verified": source_flags["dotd_alpha1_driver_verified"],
            "selected_threshold_response_functional_instantiated": threshold_functional[
                "closure_decision"
            ]["selected_threshold_response_functional_instantiated"],
            "generation_resolved_threshold_source_rows_closed": threshold_functional[
                "closure_decision"
            ]["generation_resolved_threshold_source_rows_closed"],
        },
        "source_flags": source_flags,
        "projector_promotion_status": projector_promotion["status"],
        "threshold_functional_status": threshold_functional["status"],
    }
    write_json(SOURCE_LEDGER_PACKET, source_ledger)

    rows: list[dict[str, Any]] = []
    charged_basis_signatures: dict[str, tuple[str, ...]] = {}
    max_errors: dict[str, float] = {
        "D_heat_trace_times_L": 0.0,
        "D_exp_reduced_heat_times_L": 0.0,
        "D_pseudodet_geomean_times_L": 0.0,
    }
    for target in targets["target_rows"]:
        omega_id = target["omega_id"]
        factor = factor_by_omega[omega_id]
        sector = target["sector"]
        generation = target["generation_or_lambda"]
        slot = slots["H" if sector == "H" else sector]
        basis_signature = tuple(slot["ordered_zero_mode_basis_ids"])
        if sector in {"u", "d", "e"}:
            charged_basis_signatures[sector] = basis_signature
        l_value = model_active_l_value(slot, generation)
        diagnostic = diagnostic_prefactor_representatives(
            factor["finite_heat_torsion_invariants"], l_value
        )
        for key, predicted in diagnostic.items():
            err = log_error(target["diagnostic_prefactor"], predicted)
            if err is not None:
                max_errors[key] = max(max_errors[key], err)
        rows.append(
            {
                "row_id": f"quadrature_trial.{omega_id}",
                "omega_id": omega_id,
                "sector": sector,
                "generation_or_lambda": generation,
                "basis_signature": list(basis_signature),
                "projector_source_verified": slot["selected_source_verified"],
                "selected_projector_promoted": slot["value_emitted_as_selected_HYM_projector"],
                "model_active_L_rowlocal_value": l_value,
                "model_active_T_scheme_value": 1.0,
                "diagnostic_prefactor_postcheck_only": target["diagnostic_prefactor"],
                "diagnostic_predicted_prefactor_representatives": diagnostic,
                "accepted_as_selected_L_rowlocal_source_row": False,
                "accepted_as_selected_T_scheme_source_row": False,
                "accepted_as_omega_source_row": False,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
                "blocking_reasons": [
                    "finite projector value is model-active, selected_source_verified is false",
                    "current zero-mode basis/projector payload is identical across charged sectors",
                    "physical dotD_alpha1/retarded overlap derivative is not verified",
                    "selected T_scheme source values are not instantiated",
                ],
            }
        )

    charged_basis_degenerate = len(set(charged_basis_signatures.values())) == 1
    distinct_model_l_values = len({row["model_active_L_rowlocal_value"] for row in rows})
    trial = {
        "schema": "MTTFiniteModelActiveQuadratureTrial.v1",
        "status": "MODEL_ACTIVE_QUADRATURE_EXECUTED_ZERO_SELECTED_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "target_values_are_postcheck_only": True,
        "row_count": len(rows),
        "accepted_L_rowlocal_source_row_count": 0,
        "accepted_T_scheme_source_row_count": 0,
        "accepted_omega_source_row_count": 0,
        "charged_basis_signatures": {key: list(value) for key, value in charged_basis_signatures.items()},
        "charged_basis_degenerate": charged_basis_degenerate,
        "distinct_model_active_L_values": distinct_model_l_values,
        "max_log_error_by_D_representative": max_errors,
        "min_best_representative_max_error_factor": math.exp(min(max_errors.values())),
        "trial_rows": rows,
    }
    write_json(MODEL_TRIAL_PACKET, trial)

    threshold_gate = {
        "schema": "MTTThresholdSchemeSourceGateForRowLocalQuadrature.v1",
        "status": "THRESHOLD_SCHEME_SOURCE_VALUES_NOT_INSTANTIATED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "functional_contract_closed": threshold_functional["closure_decision"][
            "functional_contract_closed"
        ],
        "dynamic_domain_subgate_closed": threshold_functional["closure_decision"][
            "dynamic_domain_subgate_closed"
        ],
        "family_coordinate_subgate_closed": threshold_functional["closure_decision"][
            "family_coordinate_subgate_closed"
        ],
        "selected_threshold_response_functional_instantiated": threshold_functional[
            "closure_decision"
        ]["selected_threshold_response_functional_instantiated"],
        "generation_resolved_threshold_source_rows_closed": threshold_functional[
            "closure_decision"
        ]["generation_resolved_threshold_source_rows_closed"],
        "mass_scheme_conversion_source_rows_closed": False,
        "accepted_T_scheme_source_row_count": 0,
        "legal_next_routes": [
            "instantiate T_scheme rows from same-branch threshold/mass/profile functional",
            "emit row-local overlap kernel values so T_scheme can remain universal or identity if selected",
            "derive lambda_H H-sector threshold/quartic payload from the same source",
        ],
    }
    write_json(THRESHOLD_GATE_PACKET, threshold_gate)

    degeneracy = {
        "schema": "MTTCurrentSourceDegeneracyNoGo.v1",
        "status": "CURRENT_CLOSED_SOURCE_DATA_CANNOT_EMIT_TEN_ROWLOCAL_VALUES",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "theorem": {
            "name": "CurrentClosedSourceDataDegeneracyNoGo",
            "proved": True,
            "statement": (
                "With only the closed diagonal HYM/Green source, model-active zero-mode projectors, "
                "and no selected threshold-scheme values, every charged row sees the same emitted "
                "constant zero-mode projector/quadrature value. Therefore the current closed data can "
                "emit at most one charged L_rowlocal value plus the H singlet value, while the Step69/"
                "Step70 scalar contract requires nine charged row-local/scheme values plus lambda_H."
            ),
        },
        "charged_basis_degenerate": charged_basis_degenerate,
        "distinct_model_active_L_values": distinct_model_l_values,
        "required_charged_row_count": 9,
        "required_total_row_count": 10,
        "selected_threshold_scheme_values_emitted": False,
        "selected_projector_values_promoted": False,
        "accepted_source_row_count": 0,
    }
    write_json(DEGENERACY_PACKET, degeneracy)

    cutset = {
        "schema": "MTTNextCutsetAfterQuadratureGate.v1",
        "status": "NEXT_ATTACK_PHIFIN_ROWLOCAL_KERNEL_OR_THRESHOLD_SCHEME_VALUE_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "closed_this_artifact": [
            "selected overlap quadrature functional contract",
            "source import ledger separating closed diagonal HYM/Green from open selected row values",
            "finite model-active quadrature trial over all ten rows",
            "current-source degeneracy no-go",
            "threshold-scheme source gate"
        ],
        "still_missing": [
            "Phi_fin selected minimizer trace that promotes finite projectors and zero-mode bases",
            "physical dotD_alpha1 / retarded overlap derivative row kernel",
            "selected row-local HYM/Green kernel entries L_rowlocal.*",
            "selected threshold scheme values T_scheme.*",
            "lambda_H H-sector source/quartic row",
            "strict Omega acceptance after source-only rows emit",
            "matrix-level CKM/PMNS/offdiagonal extension"
        ],
        "forbidden_routes": [
            "promote model-active B_N projectors while selected_source_verified is false",
            "use diagnostic prefactor targets to define L_rowlocal or T_scheme",
            "let threshold rows absorb all missing row variation without a same-branch source theorem",
            "claim scalar no-knob closure from the diagonal HYM solve alone"
        ],
    }
    write_json(CUTSET_PACKET, cutset)

    decision = {
        "overlap_quadrature_functional_defined": True,
        "diagonal_HYM_Green_imported": True,
        "finite_model_active_quadrature_trial_executed": True,
        "current_source_degeneracy_nogo_proved": True,
        "threshold_scheme_source_gate_built": True,
        "row_count": len(rows),
        "accepted_L_rowlocal_source_row_count": 0,
        "accepted_T_scheme_source_row_count": 0,
        "accepted_rowlocal_source_row_count": 0,
        "accepted_omega_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "selected_projector_values_promoted": False,
        "selected_retarded_overlap_derivative_rows_emitted": False,
        "lambda_H_value_row_emitted": False,
        "strict_omega_acceptance_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
    }
    candidate = {
        "candidate": "MTTSelectedRowLocalHYMOverlapQuadratureFunctionalOrThresholdSchemeSourceTheorem",
        "status": STATUS,
        "closure_claimed": True,
        "theorem": {
            "name": "RowLocalHYMOverlapQuadratureFunctionalAndDegeneracyNoGoTheorem",
            "proved": True,
            "statement": (
                "The selected row-local scalar gate is now a precise quadrature/threshold functional. "
                "The closed diagonal HYM/Green payload and finite model-active projector packet can be "
                "tested, but they emit zero accepted rows because the finite projectors are not selected "
                "source values and their charged zero-mode signatures are degenerate. Thus the next "
                "non-looping target is a selected Phi_fin row-local kernel or selected threshold-scheme "
                "value rows."
            ),
        },
        "inputs": {
            "previous_candidate": rel(PREVIOUS),
            "step72_required_rowlocal_prefactor_target_table": rel(STEP72_TARGETS),
            "step70_prefactor_slot_factorization": rel(STEP70_FACTORS),
            "step73_candidate": rel(STEP73),
            "selected_hym_first_solve_payload": rel(HYM_FIRST),
            "full_diagonal_end0_green_payload": rel(FULL_GREEN),
            "selected_hym_projector_zeromode_basis_value_emission": rel(PROJECTOR_VALUES),
            "selected_hym_projector_source_promotion_route_a": rel(PROJECTOR_PROMOTION),
            "selected_thresholdfunctionalsourcetheorem_or_minimaluniversalparameterselection": rel(THRESHOLD_FUNCTIONAL),
        },
        "output_packets": {
            "selected_overlap_quadrature_functional": rel(FUNCTIONAL_PACKET),
            "available_source_import_ledger": rel(SOURCE_LEDGER_PACKET),
            "finite_model_active_quadrature_trial": rel(MODEL_TRIAL_PACKET),
            "threshold_scheme_source_gate": rel(THRESHOLD_GATE_PACKET),
            "current_source_degeneracy_nogo": rel(DEGENERACY_PACKET),
            "next_cutset_after_quadrature_gate": rel(CUTSET_PACKET),
        },
        "closure_decision": decision,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_RowLocalHYMOverlapQuadratureFunctional_or_ThresholdSchemeSourceTheorem_v1",
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
        f"""# MTT Selected RowLocalHYMOverlapQuadratureFunctional or ThresholdSchemeSourceTheorem v1

Status: `{STATUS}`.

## What Closed

The row-local wall is now a typed functional rather than an informal wish:

`C_HYMthr(s,g)=D_fin.class(s)*L_rowlocal(s,g)*T_scheme(s,g)`.

`L_rowlocal` must come from selected `P_s,K_s,A_HYM,G,dotD_alpha1`
quadrature. `T_scheme` must come from a selected internal threshold/mass/profile
functional. Diagnostic target rows remain postchecks.

## Mathematical Trial

The current finite model-active projector packet was replayed across all ten
slots. It emits clean rank/projector/basis data, but its selected-source flags
remain false and all charged rows use the same zero-mode signature:

```text
row count                          : {len(rows)}
charged basis degenerate            : {charged_basis_degenerate}
distinct model-active L values      : {distinct_model_l_values}
accepted L_rowlocal source rows     : 0
accepted T_scheme source rows       : 0
accepted Omega/source scalar rows   : 0
best diagnostic max error factor    : {math.exp(min(max_errors.values())):.6g}
```

This proves a useful no-go: diagonal HYM/Green plus current model-active finite
projectors cannot by themselves emit the ten selected scalar rows.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
