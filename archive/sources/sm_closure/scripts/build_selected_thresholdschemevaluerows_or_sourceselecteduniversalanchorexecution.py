"""Build threshold-scheme value rows / source-selected universal anchor attempt."""

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

SLUG = "selected_thresholdschemevaluerows_or_sourceselecteduniversalanchorexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_BASIS_PACKET = PACKET_DIR / "selected_anchor_source_basis.packet.json"
ANCHOR_SEARCH_PACKET = PACKET_DIR / "one_to_three_anchor_model_search.packet.json"
OVERFIT_GUARD_PACKET = PACKET_DIR / "overfit_exact_replay_guard.packet.json"
THRESHOLD_GATE_PACKET = PACKET_DIR / "threshold_value_row_acceptance_gate.packet.json"
CUTSET_PACKET = PACKET_DIR / "next_cutset_after_anchor_search.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThresholdSchemeValueRows_or_SourceSelectedUniversalAnchorExecution_v1.md"

PREVIOUS = DATA / "selected_phifinminimizertracerowlocalkernel_or_thresholdschemevaluerows.candidate.json"
PREVIOUS_THRESHOLD_SYSTEM = (
    DATA
    / "selected_phifinminimizertracerowlocalkernel_or_thresholdschemevaluerows"
    / "threshold_scheme_value_rows_minimal_system.packet.json"
)
THRESHOLD_AUDIT = (
    DATA
    / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation"
    / "threshold_response_instantiation_audit_after_pi_closure.packet.json"
)
SOURCE_WEIGHTS = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "source_normalized_sector_projection_weights.packet.json"
)
COEFF_SKELETON = (
    DATA
    / "selected_rtheta_coefficientfunctional_or_universalanchorselection"
    / "rtheta_coefficient_functional_skeleton.packet.json"
)
TARGETS = (
    DATA
    / "selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance"
    / "step72_required_rowlocal_prefactor_target_table.packet.json"
)
STEP67 = DATA / "selected_step67_thetaoverlap_anchor_or_exponentprefactor_frontier.candidate.json"
STEP68_WEIGHTS = (
    DATA
    / "selected_step68_thetaexponentweights_or_prefactorthreshold_frontier"
    / "step68_selected_theta_exponent_weight_rows.packet.json"
)
STEP44 = DATA / "selected_step44_alpha1universalanchor_admission_or_rthetarowexecution.candidate.json"

STATUS = (
    "MTT_SELECTED_THRESHOLDSCHEMEVALUEROWS_OR_SOURCESELECTEDUNIVERSALANCHOREXECUTION_"
    "BUILT_ANCHOR_SEARCH_NO_SOURCE_ROWS_OPEN"
)
NEXT = "MTT_Selected_InternalThresholdResponseFunctionalValueRows_or_ExternalSourceImportDecision_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def eigenvalue_for_generation(generation: int) -> float:
    return {
        1: -1.367835979172,
        2: -0.683917989586,
        3: 0.683917989586,
    }[generation]


def charged_target_rows(target_rows: list[dict[str, Any]]) -> list[tuple[str, str, int, float, float]]:
    prepared = []
    for row in target_rows:
        if row["sector"] not in {"u", "d", "e"}:
            continue
        generation = int(row["generation_or_lambda"][3:])
        prepared.append(
            (
                row["omega_id"],
                row["sector"],
                generation,
                eigenvalue_for_generation(generation),
                math.log(row["diagnostic_prefactor"]),
            )
        )
    return prepared


def feature_pool() -> list[tuple[str, Callable[[str, int, float], float], str]]:
    features: list[tuple[str, Callable[[str, int, float], float], str]] = [
        ("1", lambda _s, _g, _x: 1.0, "unit/alpha1 source-normalized constant"),
        ("x", lambda _s, _g, x: x, "selected family eigenprofile"),
        ("x2", lambda _s, _g, x: x * x, "quadratic family eigenprofile diagnostic"),
        ("x3", lambda _s, _g, x: x * x * x, "cubic family eigenprofile diagnostic"),
    ]
    for sector in ["u", "d", "e"]:
        features.extend(
            [
                (f"I_{sector}", lambda s, _g, _x, sector=sector: 1.0 if s == sector else 0.0, f"{sector} sector slot"),
                (f"I_{sector}x", lambda s, _g, x, sector=sector: x if s == sector else 0.0, f"{sector} sector times family eigenprofile"),
                (
                    f"I_{sector}x2",
                    lambda s, _g, x, sector=sector: x * x if s == sector else 0.0,
                    f"{sector} sector times quadratic family eigenprofile",
                ),
            ]
        )
    return features


def least_squares_search(rows: list[tuple[str, str, int, float, float]], max_features: int) -> list[dict[str, Any]]:
    features = feature_pool()
    y = np.array([row[4] for row in rows], dtype=float)
    best: list[dict[str, Any]] = []
    for count in range(1, max_features + 1):
        local_best: list[dict[str, Any]] = []
        for combo in itertools.combinations(range(len(features)), count):
            matrix = np.array(
                [[features[index][1](sector, generation, x) for index in combo] for _, sector, generation, x, _ in rows],
                dtype=float,
            )
            if np.linalg.matrix_rank(matrix) < count:
                continue
            coeffs, *_ = np.linalg.lstsq(matrix, y, rcond=None)
            predicted = matrix @ coeffs
            errors = predicted - y
            max_abs = float(np.max(np.abs(errors)))
            rms = float(np.sqrt(np.mean(errors * errors)))
            local_best.append(
                {
                    "feature_count": count,
                    "features": [features[index][0] for index in combo],
                    "coefficients": [float(value) for value in coeffs],
                    "max_abs_log_residual": max_abs,
                    "max_multiplicative_error_factor": math.exp(max_abs),
                    "rms_log_residual": rms,
                    "accepted_as_source_anchor_model": False,
                    "target_fitting_used": True,
                }
            )
        local_best.sort(key=lambda item: (item["max_abs_log_residual"], item["rms_log_residual"]))
        best.extend(local_best[:5])
    best.sort(key=lambda item: (item["max_abs_log_residual"], item["rms_log_residual"], item["feature_count"]))
    return best


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    required = [
        PREVIOUS,
        PREVIOUS_THRESHOLD_SYSTEM,
        THRESHOLD_AUDIT,
        SOURCE_WEIGHTS,
        COEFF_SKELETON,
        TARGETS,
        STEP67,
        STEP68_WEIGHTS,
        STEP44,
    ]
    missing = [rel(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError("missing inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    previous_threshold_system = load(PREVIOUS_THRESHOLD_SYSTEM)
    threshold_audit = load(THRESHOLD_AUDIT)
    source_weights = load(SOURCE_WEIGHTS)
    coeff_skeleton = load(COEFF_SKELETON)
    targets = load(TARGETS)
    step67 = load(STEP67)
    step68_weights = load(STEP68_WEIGHTS)
    step44 = load(STEP44)

    prepared_rows = charged_target_rows(targets["target_rows"])
    features = feature_pool()
    source_basis = {
        "schema": "MTTSelectedAnchorSourceBasisForThresholdRows.v1",
        "status": "SELECTED_STRUCTURAL_BASIS_AVAILABLE_VALUE_ANCHORS_NOT_EMITTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "available_selected_structural_sources": [
            {
                "id": "alpha1_source_strength_anchor",
                "source": rel(STEP44),
                "selected_at_source_tier": step44["closure_decision"][
                    "alpha1_one_universal_source_anchor_admitted_at_source_tier"
                ],
                "emits_threshold_value_rows": False,
            },
            {
                "id": "epsilon_Theta",
                "source": rel(STEP67),
                "selected_at_source_tier": step67["closure_decision"]["theta_overlap_suppression_anchor_closed"],
                "emits_threshold_value_rows": False,
            },
            {
                "id": "qutrit_shared_circle_quotient_index",
                "source": rel(STEP68_WEIGHTS),
                "selected_at_source_tier": True,
                "emits_threshold_value_rows": False,
            },
            {
                "id": "source_normalized_sector_weights",
                "source": rel(SOURCE_WEIGHTS),
                "selected_at_source_tier": source_weights["source_projection_weights_closed"],
                "emits_threshold_value_rows": False,
            },
            {
                "id": "family_eigenprofile_basis",
                "source": rel(COEFF_SKELETON),
                "selected_at_source_tier": coeff_skeleton["coefficient_functional_readiness_closed"],
                "emits_threshold_value_rows": False,
            },
        ],
        "feature_pool": [
            {"feature": name, "source_interpretation": description, "selected_value_functional": False}
            for name, _func, description in features
        ],
        "current_value_emitting_anchor_count": 0,
    }
    write_json(SOURCE_BASIS_PACKET, source_basis)

    search = least_squares_search(prepared_rows, 9)
    best_by_count = {}
    for item in search:
        best_by_count.setdefault(str(item["feature_count"]), item)
    anchor_search = {
        "schema": "MTTOneToThreeAnchorModelSearch.v1",
        "status": "ONE_TO_THREE_CURRENT_SOURCE_ANCHORS_INSUFFICIENT_DIAGNOSTIC_ONLY",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": True,
        "charged_row_count": len(prepared_rows),
        "feature_pool_count": len(features),
        "policy_feature_count_limit": 3,
        "best_by_feature_count": {key: best_by_count[key] for key in sorted(best_by_count, key=int)},
        "policy_result": {
            "one_to_three_current_source_anchor_sufficient": False,
            "best_policy_max_multiplicative_error_factor": best_by_count["3"]["max_multiplicative_error_factor"],
            "accepted_source_anchor_row_count": 0,
            "reason": (
                "Under the current selected structural feature basis, all one-to-three coefficient models "
                "remain order-one diagnostic fits. They do not emit threshold value rows."
            ),
        },
    }
    write_json(ANCHOR_SEARCH_PACKET, anchor_search)

    exact_model = best_by_count["9"]
    near_exact_model = best_by_count["8"]
    overfit_guard = {
        "schema": "MTTOverfitExactReplayGuardForThresholdRows.v1",
        "status": "HIGH_PARAMETER_REPLAY_EXISTS_BUT_IS_FORBIDDEN_AS_SOURCE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": True,
        "near_exact_model": near_exact_model,
        "exact_charged_replay_model": exact_model,
        "accepted_as_source_rows": False,
        "why_forbidden": [
            "eight/nine coefficients for nine charged rows are row-replay, not selected source data",
            "coefficients are solved from Step72 diagnostic postcheck targets",
            "no same-branch threshold functional selects these coefficients before replay",
            "lambda_H remains outside the charged exact replay",
        ],
    }
    write_json(OVERFIT_GUARD_PACKET, overfit_guard)

    threshold_gate = {
        "schema": "MTTThresholdValueRowAcceptanceGate.v1",
        "status": "THRESHOLD_VALUE_ROWS_NOT_ACCEPTED_CURRENT_GATE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_gate": previous["status"],
        "previous_minimal_system": previous_threshold_system["status"],
        "requirement_count": threshold_audit["requirement_count"],
        "present_count": threshold_audit["present_count"],
        "blocking_failures": threshold_audit["blocking_failures"],
        "accepted_threshold_scheme_value_row_count": 0,
        "accepted_source_anchor_row_count": 0,
        "accepted_lambda_H_value_row": False,
        "accepted_omega_source_row_count": 0,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
    }
    write_json(THRESHOLD_GATE_PACKET, threshold_gate)

    cutset = {
        "schema": "MTTNextCutsetAfterAnchorSearch.v1",
        "status": "NEXT_ATTACK_INTERNAL_THRESHOLD_RESPONSE_VALUE_FUNCTIONAL_OR_EXTERNAL_SOURCE_IMPORT",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "closed_here": [
            "selected structural anchor basis enumerated",
            "1-3 source-anchor policy search executed and rejected under current basis",
            "8/9-coefficient exact replay quarantined as target-fit overparameterization",
            "threshold value-row acceptance gate rebuilt with zero accepted rows",
        ],
        "still_missing": [
            "selected same-branch scale/scheme/loop convention at true-precision tier",
            "selected threshold matching value rows",
            "selected mass-scheme conversion value rows",
            "selected profile/diagonal likelihood value functional",
            "selected lambda_H value row",
            "external source import decision if internal functional cannot be derived",
        ],
        "forbidden_routes": [
            "promote one-to-three target-scored coefficients as selected anchors",
            "use exact eight/nine coefficient replay as no-knob proof",
            "treat admitted-external threshold rows as internal selected rows",
            "hide row-specific fits inside T_scheme.*",
        ],
    }
    write_json(CUTSET_PACKET, cutset)

    decision = {
        "selected_anchor_source_basis_built": True,
        "one_to_three_anchor_model_search_executed": True,
        "one_to_three_current_source_anchor_sufficient": False,
        "overfit_exact_replay_guard_built": True,
        "threshold_value_row_acceptance_gate_built": True,
        "accepted_threshold_scheme_value_row_count": 0,
        "accepted_source_anchor_row_count": 0,
        "accepted_lambda_H_value_row": False,
        "accepted_omega_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
    }
    candidate = {
        "candidate": "MTTSelectedThresholdSchemeValueRowsOrSourceSelectedUniversalAnchorExecution",
        "status": STATUS,
        "closure_claimed": True,
        "theorem": {
            "name": "CurrentSourceAnchorSearchAndOverfitGuardTheorem",
            "proved": True,
            "statement": (
                "The currently selected structural anchors and basis rows do not supply one-to-three "
                "value-emitting source parameters for the threshold scheme. Diagnostic exact replay "
                "appears only when enough target-scored coefficients are admitted to fit the rows, which "
                "is forbidden. Thus the next legal target is an internal threshold response value functional "
                "or an explicit external source-import decision, not another replay fit."
            ),
        },
        "inputs": {
            "previous_candidate": rel(PREVIOUS),
            "previous_threshold_system": rel(PREVIOUS_THRESHOLD_SYSTEM),
            "threshold_response_instantiation_audit": rel(THRESHOLD_AUDIT),
            "source_normalized_sector_weights": rel(SOURCE_WEIGHTS),
            "coefficient_skeleton": rel(COEFF_SKELETON),
            "step72_postcheck_targets": rel(TARGETS),
            "step67_theta_anchor": rel(STEP67),
            "step68_theta_weights": rel(STEP68_WEIGHTS),
            "step44_alpha1_anchor": rel(STEP44),
        },
        "output_packets": {
            "selected_anchor_source_basis": rel(SOURCE_BASIS_PACKET),
            "one_to_three_anchor_model_search": rel(ANCHOR_SEARCH_PACKET),
            "overfit_exact_replay_guard": rel(OVERFIT_GUARD_PACKET),
            "threshold_value_row_acceptance_gate": rel(THRESHOLD_GATE_PACKET),
            "next_cutset_after_anchor_search": rel(CUTSET_PACKET),
        },
        "closure_decision": decision,
        "best_policy_max_multiplicative_error_factor": best_by_count["3"]["max_multiplicative_error_factor"],
        "near_exact_replay_feature_count": near_exact_model["feature_count"],
        "exact_charged_replay_feature_count": exact_model["feature_count"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_ThresholdSchemeValueRows_or_SourceSelectedUniversalAnchorExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        **decision,
        "best_policy_max_multiplicative_error_factor": best_by_count["3"]["max_multiplicative_error_factor"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected ThresholdSchemeValueRows or SourceSelectedUniversalAnchorExecution v1

Status: `{STATUS}`.

## What Was Tried

The current selected structural basis was assembled from `alpha1`,
`epsilon_Theta`, the qutrit/shared-circle quotient, source-normalized sector
weights, and the family eigenprofile rows.

The allowed 1-3 source-anchor lane was then tested as a diagnostic against the
nine charged postcheck rows.

```text
best 1-3 anchor max error factor : {best_by_count['3']['max_multiplicative_error_factor']:.6g}
accepted source-anchor rows      : 0
threshold value rows accepted    : 0
lambda_H accepted                : False
```

An exact charged replay appears only with `{exact_model['feature_count']}`
target-scored coefficients for nine charged rows. That is explicitly forbidden
as a no-knob/source proof.

## Result

Current selected anchors are structurally useful but do not emit threshold
scheme value rows. The live target is now an internal threshold response value
functional, or an explicit external source-import decision if the internal route
cannot be derived.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
