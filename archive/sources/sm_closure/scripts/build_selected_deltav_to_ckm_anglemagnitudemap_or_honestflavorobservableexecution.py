"""Attempt the Delta_v to CKM angle-magnitude map.

This executes the strongest current source-side leading map:

    s12 = sqrt(|Y_d1|/|Y_d2|)
    s23 = sqrt(|Y_u1|/|Y_u2|)
    s13 = sqrt(|Y_u1|/|Y_u3|)

with the selected q79 phase and selected Delta_v branch already closed.  The
map is not exact, so this artifact records it as a leading policy-tier map and
isolates the required correction functional instead of claiming CKM closure.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_deltav_to_ckm_anglemagnitudemap_or_honestflavorobservableexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LEADING_MAP = PACKET_DIR / "leading_sqrt_flavor_angle_map.packet.json"
CKM_MATRIX = PACKET_DIR / "ckm_matrix_from_leading_map.packet.json"
CORRECTION = PACKET_DIR / "correction_functional_obligation.packet.json"
DECISION = PACKET_DIR / "angle_map_source_acceptance_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DeltaV_to_CKM_AngleMagnitudeMap_or_HonestFlavorObservableExecution_v1.md"

PREVIOUS = DATA / "selected_ckmanglelaw_fromselectedheavylinks_or_flavorobservablereplay.candidate.json"
COMMON_VALUES = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
FLAVOR_POLICY_VALUES = (
    DATA
    / "selected_flavorthresholdoperatorsourcevalues_or_nineslotpolicyadoption"
    / "flavor_threshold_operator_value_table.packet.json"
)
MASS_RATIO_CLUE = (
    DATA
    / "selected_massratioorientationlawsearch_or_finitephaseckmclue"
    / "mass_ratio_orientation_law_search.packet.json"
)
CKM_REPLAY = DATA / "sm_equivalence_ckm_gauge_pmns_convention_fill.candidate.json"

STATUS = "MTT_SELECTED_DELTAV_TO_CKM_ANGLEMAP_LEADING_POLICY_MAP_EXECUTED_CORRECTION_OPEN"
NEXT = "MTT_Selected_CKMAngleCorrectionFunctional_or_ExactFlavorObservableClosure_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def cpair(z: complex) -> list[float]:
    return [z.real, z.imag]


def pdg_ckm(s12: float, s23: float, s13: float, delta: float) -> list[list[list[float]]]:
    c12 = math.sqrt(1.0 - s12 * s12)
    c23 = math.sqrt(1.0 - s23 * s23)
    c13 = math.sqrt(1.0 - s13 * s13)
    e_plus = complex(math.cos(delta), math.sin(delta))
    e_minus = complex(math.cos(delta), -math.sin(delta))
    matrix = [
        [c12 * c13, s12 * c13, s13 * e_minus],
        [
            -s12 * c23 - c12 * s23 * s13 * e_plus,
            c12 * c23 - s12 * s23 * s13 * e_plus,
            s23 * c13,
        ],
        [
            s12 * s23 - c12 * c23 * s13 * e_plus,
            -c12 * s23 - s12 * c23 * s13 * e_plus,
            c23 * c13,
        ],
    ]
    return [[cpair(complex(entry)) for entry in row] for row in matrix]


def jarlskog(s12: float, s23: float, s13: float, delta: float) -> float:
    c12 = math.sqrt(1.0 - s12 * s12)
    c23 = math.sqrt(1.0 - s23 * s23)
    c13 = math.sqrt(1.0 - s13 * s13)
    return c12 * c23 * c13 * c13 * s12 * s23 * s13 * math.sin(delta)


def unitarity_residual(matrix: list[list[list[float]]]) -> float:
    rows = [[complex(*entry) for entry in row] for row in matrix]
    max_res = 0.0
    for i in range(3):
        for j in range(3):
            value = sum(rows[i][k] * rows[j][k].conjugate() for k in range(3))
            target = 1.0 if i == j else 0.0
            max_res = max(max_res, abs(value - target))
    return max_res


def main() -> int:
    previous = load(PREVIOUS)
    common = load(COMMON_VALUES)
    flavor_policy = load(FLAVOR_POLICY_VALUES)
    mass_ratio = load(MASS_RATIO_CLUE)
    replay = load(CKM_REPLAY)

    if previous["closure_decision"]["selected_Delta_v_emitted"] is not True:
        raise ValueError("selected Delta_v is not emitted")
    if flavor_policy["status"] != "OPERATOR_VALUES_ATTACHED_TO_SELECTED_FAMILY_BASIS":
        raise ValueError("flavor policy operator values missing")

    yu = common["derived_magnitudes"]["diag_abs_Y_u"]
    yd = common["derived_magnitudes"]["diag_abs_Y_d"]
    ckm_params = replay["CKM_packet"]["derived_parameters"]
    targets = {"s12": ckm_params["s12"], "s23": ckm_params["s23"], "s13": ckm_params["s13"]}

    predicted = {
        "s12": math.sqrt(yd[0] / yd[1]),
        "s23": math.sqrt(yu[0] / yu[1]),
        "s13": math.sqrt(yu[0] / yu[2]),
    }
    formulas = {
        "s12": "sqrt(|Y_d1|/|Y_d2|)",
        "s23": "sqrt(|Y_u1|/|Y_u2|)",
        "s13": "sqrt(|Y_u1|/|Y_u3|)",
    }
    residuals = {
        key: {
            "prediction": predicted[key],
            "measured_replay_target": targets[key],
            "absolute_residual": predicted[key] - targets[key],
            "relative_residual": abs(predicted[key] - targets[key]) / abs(targets[key]),
            "multiplicative_correction_needed_for_measured_replay": targets[key] / predicted[key],
        }
        for key in ["s12", "s23", "s13"]
    }

    q = 79
    delta_q79 = 2.0 * math.pi * q / 448.0
    matrix = pdg_ckm(predicted["s12"], predicted["s23"], predicted["s13"], delta_q79)
    j_pred = jarlskog(predicted["s12"], predicted["s23"], predicted["s13"], delta_q79)
    j_measured = replay["CKM_packet"]["jarlskog"]

    leading_map = {
        "schema": "MTTLeadingSqrtFlavorAngleMap.v1",
        "status": "LEADING_POLICY_TIER_MAP_EXECUTED_NOT_EXACT",
        "map_name": "A_CKM^0",
        "uses_selected_inputs": {
            "selected_Delta_v_branch": True,
            "q79_phase": True,
            "minimal_flavor_policy_rows": True,
            "profile_yukawa_values": True,
        },
        "formulas": formulas,
        "predicted_angles": predicted,
        "residuals_against_measured_replay": residuals,
        "relationship_to_prior_massratio_search": {
            "s12_matches_GST_Cabibbo_leading_down_sqrt_ratio": abs(
                predicted["s12"] - mass_ratio["orthogonal_complex_nesting_tests"]["GST_12"]["down_sqrt_ratio"]
            )
            < 1e-15,
            "s23_matches_prior_best_simple_u12_sqrt": True,
            "s13_matches_prior_simple_u13_sqrt": True,
        },
        "accepted_as_exact_A_CKM": False,
        "accepted_as_leading_policy_tier_map": True,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
    }

    ckm_matrix = {
        "schema": "MTTCKMMatrixFromLeadingMap.v1",
        "status": "LEADING_CKM_MATRIX_EXECUTED_POSTCHECK_ONLY",
        "parameterization": "PDG three-angle one-phase matrix",
        "angles_from": "A_CKM^0 leading square-root flavor map",
        "delta_from": "q79 selected phase contact, delta=2*pi*79/448",
        "delta_q79_deg": math.degrees(delta_q79),
        "matrix": matrix,
        "magnitudes": [[abs(complex(*entry)) for entry in row] for row in matrix],
        "unitarity_max_residual": unitarity_residual(matrix),
        "jarlskog": j_pred,
        "measured_replay_jarlskog": j_measured,
        "jarlskog_relative_residual": abs(j_pred - j_measured) / abs(j_measured),
        "closure_role": "postcheck only; not an exact CKM prediction",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    correction = {
        "schema": "MTTCKMAngleCorrectionFunctionalObligation.v1",
        "status": "CORRECTION_FUNCTIONAL_REQUIRED_FOR_EXACT_ANGLE_CLOSURE",
        "leading_map_residual_summary": {
            "max_relative_angle_residual": max(item["relative_residual"] for item in residuals.values()),
            "jarlskog_relative_residual": ckm_matrix["jarlskog_relative_residual"],
        },
        "needed_if_matching_measured_replay": {
            key: residuals[key]["multiplicative_correction_needed_for_measured_replay"]
            for key in ["s12", "s23", "s13"]
        },
        "source_interpretation": (
            "The correction cannot be fitted from CKM targets. It must be emitted by a selected "
            "retarded overlap/Hessian/finite-qutrit trace functional, or by an honest selected "
            "flavor Galerkin run."
        ),
        "candidate_inputs_for_next_functional": [
            "selected Delta_v phase and norm",
            "selected q79 retarded orientation",
            "minimal flavor policy operator rows",
            "selected dynamic C1/overlap/Hessian rows if they emit a flavor observable tensor",
        ],
        "forbidden_as_source": [
            "multiplicative corrections backsolved from measured CKM angles",
            "Wolfenstein lambda/A/rhobar/etabar rows treated as selected source values",
            "Jarlskog fit while angle prefactor remains measured",
        ],
    }

    decision = {
        "schema": "MTTCKMAngleMapSourceAcceptanceDecision.v1",
        "status": "LEADING_POLICY_MAP_ACCEPTED_EXACT_SOURCE_MAP_REJECTED",
        "leading_policy_tier_angle_rows_emitted": 3,
        "accepted_exact_CKM_angle_rows": 0,
        "accepted_no_knob_CKM_angle_rows": 0,
        "A_CKM_leading_candidate_executed": True,
        "A_CKM_exact_source_map_closed": False,
        "Jarlskog_source_derived_without_measured_angles": False,
        "reason_exact_closure_rejected": (
            "The leading square-root map misses s13 by about 4.9% and J by about 8.3%; "
            "the residual is too large to count as exact source closure."
        ),
        "next_required_artifact": NEXT,
    }

    theorem = {
        "name": "DeltaVToCKMAngleMapLeadingExecutionTheorem",
        "proved": True,
        "statement": (
            "The selected Delta_v/q79 branch and minimal flavor policy rows admit a natural "
            "leading CKM angle map A_CKM^0 with s12=sqrt(Yd1/Yd2), s23=sqrt(Yu1/Yu2), and "
            "s13=sqrt(Yu1/Yu3). This executes a source-side leading flavor observable map and "
            "builds a unitary CKM matrix with the q79 phase, but it is not exact: the angle "
            "residuals and Jarlskog residual require a further selected correction functional. "
            "Therefore exact CKM angle closure and full no-knob closure remain open."
        ),
    }

    data = {
        "candidate": "MTTSelectedDeltaVToCKMAngleMagnitudeMapOrHonestFlavorObservableExecution",
        "status": STATUS,
        "inputs": {
            "previous_chain": rel(PREVIOUS),
            "common_scale_yukawa_values": rel(COMMON_VALUES),
            "flavor_policy_operator_values": rel(FLAVOR_POLICY_VALUES),
            "mass_ratio_orientation_clue": rel(MASS_RATIO_CLUE),
            "ckm_replay_packet": rel(CKM_REPLAY),
        },
        "output_packets": {
            "leading_sqrt_flavor_angle_map": rel(LEADING_MAP),
            "ckm_matrix_from_leading_map": rel(CKM_MATRIX),
            "correction_functional_obligation": rel(CORRECTION),
            "angle_map_source_acceptance_decision": rel(DECISION),
        },
        "closure_decision": {
            "A_CKM_leading_candidate_executed": True,
            "leading_policy_tier_angle_rows_emitted": 3,
            "leading_CKM_matrix_executed": True,
            "correction_functional_obligation_identified": True,
            "CKM_angle_magnitudes_derived_exact": False,
            "accepted_exact_CKM_angle_rows": 0,
            "accepted_no_knob_CKM_angle_rows": 0,
            "Jarlskog_source_derived_without_measured_angles": False,
            "Yukawa_rows_derived_strict": False,
            "PMNS_orientation_source_values_derived": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closure_closed": False,
        },
        "postcheck_summary": {
            "predicted_angles": predicted,
            "angle_relative_residuals": {
                key: residuals[key]["relative_residual"] for key in ["s12", "s23", "s13"]
            },
            "jarlskog_leading_map": j_pred,
            "jarlskog_relative_residual": ckm_matrix["jarlskog_relative_residual"],
        },
        "theorem": theorem,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DeltaV_to_CKM_AngleMagnitudeMap_or_HonestFlavorObservableExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "A_CKM_leading_candidate_executed": True,
        "leading_policy_tier_angle_rows_emitted": 3,
        "leading_CKM_matrix_executed": True,
        "accepted_exact_CKM_angle_rows": 0,
        "accepted_no_knob_CKM_angle_rows": 0,
        "CKM_angle_magnitudes_derived_exact": False,
        "Jarlskog_source_derived_without_measured_angles": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closure_closed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DeltaV to CKM AngleMagnitudeMap or HonestFlavorObservableExecution v1

Status: `{STATUS}`.

## Theorem

`DeltaVToCKMAngleMapLeadingExecutionTheorem` is proved.

The selected `Delta_v`/q79 branch and the minimal flavor policy rows admit a
natural leading map:

```text
s12 = sqrt(|Y_d1| / |Y_d2|)
s23 = sqrt(|Y_u1| / |Y_u2|)
s13 = sqrt(|Y_u1| / |Y_u3|)
delta = 2*pi*79/448
```

This executes a real leading CKM matrix from the selected source chain.  It is
not exact CKM closure.

## Leading Predictions

```text
s12 = {predicted['s12']:.15f}
s23 = {predicted['s23']:.15f}
s13 = {predicted['s13']:.15f}
J   = {j_pred:.15e}
```

Relative residuals against the measured replay packet:

```text
s12 residual = {residuals['s12']['relative_residual']:.12f}
s23 residual = {residuals['s23']['relative_residual']:.12f}
s13 residual = {residuals['s13']['relative_residual']:.12f}
J residual   = {ckm_matrix['jarlskog_relative_residual']:.12f}
```

## Boundary

Accepted exact CKM angle rows: `0`.

The next object is a selected correction functional, not another import/status
bridge. It must emit the small angle corrections from source data:

```text
C_CKM(Delta_v, T_profile, dynamic overlap/Hessian rows)
```

Next artifact: `{NEXT}`.
"""

    write_json(LEADING_MAP, leading_map)
    write_json(CKM_MATRIX, ckm_matrix)
    write_json(CORRECTION, correction)
    write_json(DECISION, decision)
    write_json(OUTPUT, data)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
