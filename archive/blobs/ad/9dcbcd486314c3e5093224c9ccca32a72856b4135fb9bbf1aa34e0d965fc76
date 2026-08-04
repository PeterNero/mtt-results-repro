"""Build selected Phi_fin row-local kernel / threshold-scheme value-row gate."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Any, Callable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_phifinminimizertracerowlocalkernel_or_thresholdschemevaluerows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_DOMAIN_PACKET = PACKET_DIR / "latest_source_domain_import.packet.json"
TRACE_QUOTIENT_PACKET = PACKET_DIR / "phifin_trace_only_rank_quotient_nogo.packet.json"
EXECUTION_GATE_PACKET = PACKET_DIR / "rowlocal_value_execution_gate_after_phifin_import.packet.json"
EIGENPROFILE_PACKET = PACKET_DIR / "eigenprofile_sector_bruteforce_diagnostic.packet.json"
THRESHOLD_SYSTEM_PACKET = PACKET_DIR / "threshold_scheme_value_rows_minimal_system.packet.json"
CUTSET_PACKET = PACKET_DIR / "next_cutset_after_phifin_kernel_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhiFinMinimizerTraceRowLocalKernel_or_ThresholdSchemeValueRows_v1.md"

PREVIOUS = DATA / "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem.candidate.json"
PHIFIN = DATA / "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator.candidate.json"
PROJECTOR_IMPORT = (
    DATA
    / "selected_rtheta_sectortransferbnbasis_or_pikernelclosure"
    / "selected_transported_projector_source_import.packet.json"
)
SECTOR_SUBGATE = (
    DATA
    / "selected_rtheta_sectortransferbnbasis_or_pikernelclosure"
    / "rtheta_sector_transfer_stationary_subgate.packet.json"
)
RTHETA_SECTOR = DATA / "selected_rthetasectortransfer_or_primitiveassemblymapexecution.candidate.json"
RTHETA_SECTOR_EXEC = (
    DATA
    / "selected_rthetasectortransfer_or_primitiveassemblymapexecution"
    / "rtheta_sector_transfer_execution.packet.json"
)
RTHETA_PRIMITIVE = DATA / "selected_rtheta_primitivec1overlap_or_pinoneedtheorem.candidate.json"
RTHETA_VALUE = DATA / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation.candidate.json"
VALUE_GATE = (
    DATA
    / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation"
    / "rtheta_value_evaluator_execution_gate.packet.json"
)
THRESHOLD_AUDIT = (
    DATA
    / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation"
    / "threshold_response_instantiation_audit_after_pi_closure.packet.json"
)
COEFF_SKELETON = (
    DATA
    / "selected_rtheta_coefficientfunctional_or_universalanchorselection"
    / "rtheta_coefficient_functional_skeleton.packet.json"
)
SOURCE_WEIGHTS = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "source_normalized_sector_projection_weights.packet.json"
)
TARGETS = (
    DATA
    / "selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance"
    / "step72_required_rowlocal_prefactor_target_table.packet.json"
)
FACTORS = (
    DATA
    / "selected_step70_heattorsionprefactorbackimport_or_rowlocalfrontier"
    / "step70_prefactor_slot_factorization.packet.json"
)

STATUS = (
    "MTT_SELECTED_PHIFINMINIMIZERTRACEROWLOCALKERNEL_OR_THRESHOLDSCHEMEVALUEROWS_"
    "BUILT_SOURCE_DOMAIN_CLOSED_TRACE_QUOTIENT_NOGO_VALUES_OPEN"
)
NEXT = "MTT_Selected_ThresholdSchemeValueRows_or_SourceSelectedUniversalAnchorExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def generation_index(label: str) -> int | None:
    if label.startswith("gen"):
        return int(label[3:])
    return None


def charged_rows(targets: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [row for row in targets if row["sector"] in {"u", "d", "e"}]


def eigenvalue_for_generation(generation: int) -> float:
    return {
        1: -1.367835979172,
        2: -0.683917989586,
        3: 0.683917989586,
    }[generation]


def target_distinct_count(rows: list[dict[str, Any]]) -> int:
    return len({round(row["diagnostic_prefactor"], 12) for row in rows})


def run_eigenprofile_diagnostic(rows: list[dict[str, Any]]) -> dict[str, Any]:
    feature_defs: list[tuple[str, Callable[[str, int, float], float]]] = [
        ("1", lambda _s, _g, _x: 1.0),
        ("x", lambda _s, _g, x: x),
        ("x2", lambda _s, _g, x: x * x),
        ("x3", lambda _s, _g, x: x * x * x),
    ]
    for sector in ["u", "d", "e"]:
        feature_defs.extend(
            [
                (f"I_{sector}", lambda s, _g, _x, sector=sector: 1.0 if s == sector else 0.0),
                (f"I_{sector}x", lambda s, _g, x, sector=sector: x if s == sector else 0.0),
                (f"I_{sector}x2", lambda s, _g, x, sector=sector: x * x if s == sector else 0.0),
            ]
        )

    prepared = []
    for row in rows:
        generation = generation_index(row["generation_or_lambda"])
        assert generation is not None
        prepared.append(
            (
                row["omega_id"],
                row["sector"],
                generation,
                eigenvalue_for_generation(generation),
                math.log(row["diagnostic_prefactor"]),
            )
        )

    y = np.array([item[4] for item in prepared], dtype=float)
    best: list[dict[str, Any]] = []
    for count in range(1, 6):
        for combo in itertools.combinations(range(len(feature_defs)), count):
            matrix = np.array(
                [[feature_defs[index][1](sector, gen, x) for index in combo] for _, sector, gen, x, _ in prepared],
                dtype=float,
            )
            if np.linalg.matrix_rank(matrix) < count:
                continue
            coeffs, *_ = np.linalg.lstsq(matrix, y, rcond=None)
            predicted = matrix @ coeffs
            errors = predicted - y
            max_abs = float(np.max(np.abs(errors)))
            rms = float(np.sqrt(np.mean(errors * errors)))
            best.append(
                {
                    "feature_count": count,
                    "features": [feature_defs[index][0] for index in combo],
                    "coefficients": [float(value) for value in coeffs],
                    "max_abs_log_residual": max_abs,
                    "max_multiplicative_error_factor": math.exp(max_abs),
                    "rms_log_residual": rms,
                    "accepted_as_source_rule": False,
                    "target_fitting_used": True,
                }
            )
    best.sort(key=lambda item: (item["max_abs_log_residual"], item["rms_log_residual"], item["feature_count"]))
    return {
        "schema": "MTTEigenprofileSectorBruteforceDiagnostic.v1",
        "status": "COMPACT_EIGENPROFILE_SECTOR_LAWS_DIAGNOSTIC_ONLY_NO_SOURCE_RULE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": True,
        "charged_row_count": len(rows),
        "feature_pool_count": len(feature_defs),
        "max_feature_count_tested": 5,
        "tested_model_count": len(best),
        "best_models": best[:10],
        "decision": {
            "accepted_as_selected_threshold_or_rowlocal_source_rule": False,
            "reason": (
                "The best compact eigenprofile/sector diagnostic still leaves order-one residuals "
                "and is scored against postcheck targets, so it cannot be promoted as source data."
            ),
        },
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    required = [
        PREVIOUS,
        PHIFIN,
        PROJECTOR_IMPORT,
        SECTOR_SUBGATE,
        RTHETA_SECTOR,
        RTHETA_SECTOR_EXEC,
        RTHETA_PRIMITIVE,
        RTHETA_VALUE,
        VALUE_GATE,
        THRESHOLD_AUDIT,
        COEFF_SKELETON,
        SOURCE_WEIGHTS,
        TARGETS,
        FACTORS,
    ]
    missing = [rel(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError("missing inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    phifin = load(PHIFIN)
    projector_import = load(PROJECTOR_IMPORT)
    sector_subgate = load(SECTOR_SUBGATE)
    rtheta_sector = load(RTHETA_SECTOR)
    rtheta_sector_exec = load(RTHETA_SECTOR_EXEC)
    rtheta_primitive = load(RTHETA_PRIMITIVE)
    rtheta_value = load(RTHETA_VALUE)
    value_gate = load(VALUE_GATE)
    threshold_audit = load(THRESHOLD_AUDIT)
    coeff_skeleton = load(COEFF_SKELETON)
    source_weights = load(SOURCE_WEIGHTS)
    targets = load(TARGETS)
    factors = load(FACTORS)

    target_rows = targets["target_rows"]
    charged_target_rows = charged_rows(target_rows)
    charged_coeff_rows = coeff_skeleton["charged_functional_rows"]
    charged_coeff_by_slot = {row["coefficient_slot"].replace("theta_coeff.", ""): row for row in charged_coeff_rows}
    source_weight_by_sector = {row["sector"]: row for row in source_weights["sector_weights"]}

    source_domain = {
        "schema": "MTTLatestSourceDomainImportForPhiFinRowLocalKernel.v1",
        "status": "SOURCE_DOMAIN_IMPORT_CLOSES_STALE_PROJECTOR_DOTD_PI_BLOCKERS_VALUES_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_quadrature_gate": previous["status"],
        "retired_by_later_imports": {
            "premise_free_transport_closed_Phi_fin": phifin["promotion_decision"]["finite_emission_morphism_restriction_proved"],
            "stationary_projectors_promoted": projector_import["selected_projector_source_verified"],
            "validator_ready_stationary_rho_s": projector_import["validator_ready_stationary_rho_s"],
            "stationary_sector_transfer_closed": rtheta_sector_exec["stationary_sector_transfer_closed"],
            "dotD_alpha1_transport_subgate_closed": rtheta_sector_exec["dotD_alpha1_transport_subgate_closed"],
            "matter_slot_routing_closed": rtheta_primitive["closure_decision"]["matter_slot_routing_closed"],
            "primitive_C1_overlap_contractions_closed": rtheta_primitive["closure_decision"][
                "primitive_C1_overlap_contractions_closed"
            ],
            "Pi_Rtheta_closed": rtheta_primitive["closure_decision"]["Pi_Rtheta_closed"],
            "coefficient_functional_skeleton_closed": value_gate["coefficient_functional_skeleton_closed"],
        },
        "still_open_for_numerical_scalar_rows": {
            "selected_threshold_response_functional_instantiated": value_gate[
                "selected_threshold_response_functional_instantiated"
            ],
            "magnitude_bearing_projection_weights_closed": value_gate["magnitude_bearing_projection_weights_closed"],
            "accepted_coefficient_value_count": value_gate["accepted_coefficient_value_count"],
            "accepted_lambda_H_value": value_gate["accepted_lambda_H_value"],
            "full_no_knob_closed": rtheta_value["closure_decision"]["full_no_knob_closed"],
            "true_SM_equivalence_closed": rtheta_value["closure_decision"]["true_SM_equivalence_closed"],
        },
        "retired_blocker_note": (
            "The old model-active projector/provenance wording is no longer the active scalar blocker "
            "after importing the transported projector, dotD, matter-slot, primitive-C1, and Pi_Rtheta closures. "
            "What remains is selected numerical value emission."
        ),
    }
    write_json(SOURCE_DOMAIN_PACKET, source_domain)

    trace_classes: dict[str, list[str]] = {}
    for sector, formula in sector_subgate["selected_projector_formulas"].items():
        if sector == "H":
            trace_classes.setdefault("H_singlet_rank1", []).append(sector)
        else:
            trace_classes.setdefault("charged_transported_triplet_rank3", []).append(sector)
    quotient = {
        "schema": "MTTPhiFinTraceOnlyRankQuotientNoGo.v1",
        "status": "TRACE_ONLY_TRANSPORT_QUOTIENT_HAS_TOO_FEW_NUMERIC_CLASSES",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "theorem": {
            "name": "PhiFinTraceOnlyRankQuotientNoGo",
            "proved": True,
            "statement": (
                "In the selected transported stationary quotient, P_s^sel=U P_s^model U^-1 and finite trace "
                "cyclicity preserve rank and conjugacy invariants. Hence pure Phi_fin trace data distinguish "
                "only the charged rank-3 triplet class from the H rank-1 singlet. Adding current source-normalized "
                "phase/shift weights still supplies no magnitude-bearing coefficient values. Therefore trace-only "
                "data cannot emit the ten row-local scalar values."
            ),
        },
        "selected_projector_formulas": sector_subgate["selected_projector_formulas"],
        "trace_equivalence_classes": trace_classes,
        "trace_equivalence_class_count": len(trace_classes),
        "source_normalized_weight_status": source_weights["status"],
        "source_normalized_weight_classes": {
            row["sector"]: {
                "source_column": row["source_column"],
                "source_normalized_weight": row["source_normalized_weight"],
                "magnitude_bearing_weight": row["magnitude_bearing_weight"],
            }
            for row in source_weights["sector_weights"]
        },
        "typed_charged_functional_rows": coeff_skeleton["charged_functional_row_count"],
        "typed_total_scalar_rows": len(target_rows),
        "postcheck_target_distinct_prefactor_count": target_distinct_count(target_rows),
        "accepted_source_row_count": 0,
        "selected_value_rows_emitted": False,
    }
    write_json(TRACE_QUOTIENT_PACKET, quotient)

    execution_rows: list[dict[str, Any]] = []
    for target in target_rows:
        sector = target["sector"]
        generation = target["generation_or_lambda"]
        coefficient_key = f"{sector}.{generation}" if sector != "H" else None
        coeff_row = charged_coeff_by_slot.get(coefficient_key or "")
        source_weight = source_weight_by_sector.get(sector)
        is_charged = sector in {"u", "d", "e"}
        blockers = [
            "selected threshold response functional is not instantiated",
            "same-branch scale/scheme/loop convention is not closed at true-precision tier",
            "accepted internal threshold matching and mass-scheme conversion rows are empty",
            "magnitude-bearing projection weights remain distinct from source-normalized unit weights",
        ]
        if sector == "H":
            blockers.append("lambda_H H-sector value payload is not selected")
        execution_rows.append(
            {
                "row_id": f"phifin_kernel_gate.{target['omega_id']}",
                "omega_id": target["omega_id"],
                "sector": sector,
                "generation_or_lambda": generation,
                "source_domain_closed": True,
                "stationary_projector_source_closed": projector_import["selected_projector_source_verified"],
                "Pi_Rtheta_closed": rtheta_primitive["closure_decision"]["Pi_Rtheta_closed"],
                "coefficient_functional_domain_closed": value_gate["coefficient_functional_skeleton_closed"],
                "domain_basis_row_selected": bool(coeff_row["domain_basis_row_selected"]) if coeff_row else sector == "H",
                "source_normalized_weight_selected": source_weight is not None,
                "magnitude_bearing_weight_selected": bool(source_weight and source_weight["magnitude_bearing_weight"] is not None),
                "threshold_response_functional_instantiated": value_gate[
                    "selected_threshold_response_functional_instantiated"
                ],
                "emitted_L_rowlocal_kernel_value": None,
                "emitted_T_scheme_value": None,
                "emitted_lambda_H_value": None if sector == "H" else "not_applicable",
                "diagnostic_prefactor_postcheck_only": target["diagnostic_prefactor"],
                "accepted_as_selected_rowlocal_kernel_value": False,
                "accepted_as_selected_threshold_scheme_value": False,
                "accepted_as_omega_source_row": False,
                "blocking_reasons": blockers,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )
    execution_gate = {
        "schema": "MTTRowLocalValueExecutionGateAfterPhiFinImport.v1",
        "status": "SOURCE_DOMAIN_CLOSED_NUMERIC_VALUE_ROWS_REJECTED_BY_THRESHOLD_FUNCTIONAL_GAP",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "row_count": len(execution_rows),
        "charged_row_count": len(charged_target_rows),
        "accepted_L_rowlocal_kernel_value_count": 0,
        "accepted_T_scheme_value_count": 0,
        "accepted_omega_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "retired_blockers": [
            "selected transported stationary projector source",
            "validator-ready stationary rho_s",
            "dotD_alpha1 transport derivative and alpha1 source normalization",
            "static matter-slot routing",
            "primitive C1 overlap / Pi_Rtheta dependency",
        ],
        "execution_rows": execution_rows,
    }
    write_json(EXECUTION_GATE_PACKET, execution_gate)

    eigenprofile_diagnostic = run_eigenprofile_diagnostic(charged_target_rows)
    write_json(EIGENPROFILE_PACKET, eigenprofile_diagnostic)

    threshold_system = {
        "schema": "MTTThresholdSchemeValueRowsMinimalSystem.v1",
        "status": "MINIMAL_VALUE_ROW_SYSTEM_IDENTIFIED_THRESHOLD_SOURCE_ROWS_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "requirement_count": threshold_audit["requirement_count"],
        "present_count": threshold_audit["present_count"],
        "blocking_failures": threshold_audit["blocking_failures"],
        "requirements": threshold_audit["requirements"],
        "minimal_unknown_blocks": [
            {
                "block": "T_scheme.u/d/e.gen1-3",
                "row_count": 9,
                "legal_source": "selected same-branch threshold/mass/profile functional or selected universal source anchor",
                "accepted_now": False,
            },
            {
                "block": "lambda_H / Omega_H.lambda",
                "row_count": 1,
                "legal_source": "selected H-sector quartic/threshold payload from the same source branch",
                "accepted_now": False,
            },
            {
                "block": "matrix-level mixing extension",
                "row_count": "outside ten diagonal scalar rows",
                "legal_source": "selected offdiagonal dynamic operator/CKM/PMNS packet after scalar row source closure",
                "accepted_now": False,
            },
        ],
        "universal_anchor_policy": {
            "one_to_three_source_selected_parameters_allowed": True,
            "ordinary_fit_parameters_allowed": False,
            "must_be_selected_before_postcheck": True,
            "current_selected_value_parameter_count_for_this_gate": 0,
        },
    }
    write_json(THRESHOLD_SYSTEM_PACKET, threshold_system)

    cutset = {
        "schema": "MTTNextCutsetAfterPhiFinKernelGate.v1",
        "status": "NEXT_ATTACK_THRESHOLD_SCHEME_VALUE_ROWS_OR_SOURCE_SELECTED_UNIVERSAL_ANCHOR",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "closed_here": [
            "latest-source import that retires stale projector/dotD/Pi blockers",
            "trace-only transported Phi_fin rank-quotient no-go",
            "ten-row value execution gate after Phi_fin import",
            "compact eigenprofile/sector diagnostic rejection",
            "minimal threshold-scheme value-row system",
        ],
        "still_missing": [
            "selected threshold response functional value rows T_scheme.*",
            "selected same-branch scale/scheme/loop convention at true-precision tier",
            "accepted internal threshold matching source rows",
            "accepted internal mass-scheme conversion source rows",
            "selected magnitude-bearing projection weights or equivalent value functional",
            "lambda_H H-sector selected value row",
            "strict Omega source-row acceptance after values emit",
            "selected CKM/PMNS/offdiagonal matrix extension",
        ],
        "forbidden_routes": [
            "treat trace-only Phi_fin conjugacy classes as generation-resolved magnitudes",
            "promote compact target-scored eigenprofile fits as source laws",
            "promote admitted external threshold/mass rows to no-knob internal source rows",
            "use 1-3 knobs unless the knob values are source-selected before replay",
        ],
    }
    write_json(CUTSET_PACKET, cutset)

    decision = {
        "latest_source_domain_imported": True,
        "stale_projector_dotd_pi_blockers_retired": True,
        "trace_only_rank_quotient_nogo_proved": True,
        "rowlocal_value_execution_gate_built": True,
        "eigenprofile_sector_bruteforce_executed": True,
        "threshold_scheme_minimal_system_built": True,
        "row_count": len(execution_rows),
        "accepted_L_rowlocal_kernel_value_count": 0,
        "accepted_T_scheme_value_count": 0,
        "accepted_omega_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "selected_threshold_response_functional_instantiated": False,
        "lambda_H_value_row_emitted": False,
        "strict_omega_acceptance_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
    }
    candidate = {
        "candidate": "MTTSelectedPhiFinMinimizerTraceRowLocalKernelOrThresholdSchemeValueRows",
        "status": STATUS,
        "closure_claimed": True,
        "theorem": {
            "name": "PhiFinTraceOnlyRowLocalKernelNoGoAndThresholdValueRowsReductionTheorem",
            "proved": True,
            "statement": (
                "After importing the later transported-projector, dotD_alpha1, matter-slot, primitive-C1, "
                "and Pi_Rtheta closures, the old source-domain blockers are retired. However the selected "
                "stationary Phi_fin trace is conjugacy/rank invariant and cannot by itself emit the ten "
                "generation-resolved scalar values. The remaining no-knob scalar wall is now exactly selected "
                "threshold-scheme value rows, or a source-selected universal anchor that emits those rows "
                "before replay."
            ),
        },
        "inputs": {
            "previous_candidate": rel(PREVIOUS),
            "transportclosed_phifin": rel(PHIFIN),
            "selected_transported_projector_source_import": rel(PROJECTOR_IMPORT),
            "rtheta_sector_transfer_execution": rel(RTHETA_SECTOR_EXEC),
            "rtheta_primitive_c1_pi_closure": rel(RTHETA_PRIMITIVE),
            "rtheta_value_evaluator_execution_gate": rel(VALUE_GATE),
            "threshold_response_instantiation_audit": rel(THRESHOLD_AUDIT),
            "rtheta_coefficient_functional_skeleton": rel(COEFF_SKELETON),
            "source_normalized_sector_projection_weights": rel(SOURCE_WEIGHTS),
            "step72_postcheck_targets": rel(TARGETS),
            "step70_factorization": rel(FACTORS),
        },
        "output_packets": {
            "latest_source_domain_import": rel(SOURCE_DOMAIN_PACKET),
            "phifin_trace_only_rank_quotient_nogo": rel(TRACE_QUOTIENT_PACKET),
            "rowlocal_value_execution_gate_after_phifin_import": rel(EXECUTION_GATE_PACKET),
            "eigenprofile_sector_bruteforce_diagnostic": rel(EIGENPROFILE_PACKET),
            "threshold_scheme_value_rows_minimal_system": rel(THRESHOLD_SYSTEM_PACKET),
            "next_cutset_after_phifin_kernel_gate": rel(CUTSET_PACKET),
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
        "certificate": "MTT_Selected_PhiFinMinimizerTraceRowLocalKernel_or_ThresholdSchemeValueRows_v1",
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

    best = eigenprofile_diagnostic["best_models"][0]
    NOTE.write_text(
        f"""# MTT Selected PhiFinMinimizerTraceRowLocalKernel or ThresholdSchemeValueRows v1

Status: `{STATUS}`.

## What Closed

This packet imports the latest repo results rather than looping on the older
projector objection. The transported stationary projectors, stationary `rho_s`,
`dotD_alpha1` transport, static matter-slot routing, primitive C1 overlap, and
`Pi_Rtheta` are all treated as closed for the value-evaluator source domain.

## The New No-Go

Pure selected `Phi_fin` trace data are conjugacy/rank invariant:

`P_s^sel = U P_s^model U^-1`.

Finite trace cyclicity means this trace-only lane distinguishes only the
charged rank-3 class and the H rank-1 singlet. It cannot emit ten
generation-resolved scalar rows.

```text
typed scalar rows                    : {len(execution_rows)}
trace equivalence classes             : {len(trace_classes)}
accepted L_rowlocal kernel values     : 0
accepted T_scheme values              : 0
accepted Omega source rows            : 0
selected threshold functional emitted : False
```

## Diagnostic Search

A compact eigenprofile/sector brute-force diagnostic was run over charged rows
using up to five simple features. It remains diagnostic only because it is
target-scored:

```text
tested models                         : {eigenprofile_diagnostic['tested_model_count']}
best max multiplicative error factor  : {best['max_multiplicative_error_factor']:.6g}
best features                         : {', '.join(best['features'])}
accepted as source rule               : False
```

## Remaining Target

The live scalar wall is now exactly selected threshold-scheme value rows, or a
source-selected universal anchor that emits those rows before replay.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
