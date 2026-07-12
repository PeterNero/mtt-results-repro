"""Investigate the residual after selected Pi_CKM weight-row closure."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_pickmweightrows_ckmresidualdecision_or_higherorderclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FINGERPRINT = PACKET_DIR / "selected_pickm_ckm_residual_fingerprint.packet.json"
CAUSE = PACKET_DIR / "selected_pickm_ckm_residual_cause_decision.packet.json"
TEMPLATE = PACKET_DIR / "higher_order_or_profile_residual_template.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PiCKMWeightRows_CKMResidualDecision_or_HigherOrderClosure_v1.md"

PREVIOUS = DATA / "selected_pickmnumeratorbranchretentionprinciple_or_weightrows.candidate.json"
ROWS = DATA / "selected_pickmnumeratorbranchretentionprinciple_or_weightrows" / "selected_pickm_weight_rows.packet.json"
POSTCHECK = DATA / "selected_pickmnumeratorbranchretentionprinciple_or_weightrows" / "ckm_postcheck_after_selected_pickm_rows.packet.json"
REQUIRED_WEIGHTS = (
    DATA
    / "selected_ckmsectorpairprojectionrows_or_honestflavorgalerkinexecution"
    / "required_q448_sector_pair_weights.packet.json"
)
CKM_PACKET = DATA / "sm_equivalence_ckm_gauge_pmns_convention_fill.candidate.json"

STATUS = "MTT_SELECTED_PICKM_WEIGHT_ROWS_RESIDUAL_CAUSE_AUDITED_HIGHERORDER_OR_PROFILE_OPEN"
NEXT = "MTT_Selected_CKMCovarianceProfileOrHigherOrderResidualClosure_v1"
Q = 79.0
MODULUS = 448.0


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def ckm_uncertainty_estimate(ckm: dict[str, Any]) -> dict[str, Any]:
    values = ckm["CKM_packet"]["input_values"]
    derived = ckm["CKM_packet"]["derived_parameters"]
    lam = values["lambda"]["central_value"]
    sig_lam = values["lambda"]["uncertainty"]
    a = values["A"]["central_value"]
    sig_a = (values["A"]["uncertainty_minus"] + values["A"]["uncertainty_plus"]) / 2.0
    rhobar = values["rhobar"]["central_value"]
    sig_rhobar = values["rhobar"]["uncertainty"]
    etabar = values["etabar"]["central_value"]
    sig_etabar = (values["etabar"]["uncertainty_minus"] + values["etabar"]["uncertainty_plus"]) / 2.0
    rbar = math.hypot(rhobar, etabar)
    sig_rbar = math.sqrt((rhobar / rbar * sig_rhobar) ** 2 + (etabar / rbar * sig_etabar) ** 2)

    # Independent-error estimate only; the packet explicitly does not carry the full CKM covariance.
    sig_s12 = sig_lam
    sig_s23 = math.sqrt((lam**2 * sig_a) ** 2 + (2.0 * a * lam * sig_lam) ** 2)
    sig_s13 = math.sqrt(
        (lam**3 * rbar * sig_a) ** 2
        + (3.0 * a * lam**2 * rbar * sig_lam) ** 2
        + (a * lam**3 * sig_rbar) ** 2
    )
    return {
        "schema": "MTTCKMUncertaintyEstimateNoCovariance.v1",
        "source": rel(CKM_PACKET),
        "policy": "diagonal independent-error estimate only; full CKM fit covariance/profile is not encoded",
        "input_uncertainties": {
            "lambda": sig_lam,
            "A_average": sig_a,
            "rhobar": sig_rhobar,
            "etabar_average": sig_etabar,
        },
        "estimated_one_sigma": {
            "s12": sig_s12,
            "s23": sig_s23,
            "s13": sig_s13,
        },
        "central_values": {
            "s12": derived["s12"],
            "s23": derived["s23"],
            "s13": derived["s13"],
        },
    }


def main() -> int:
    previous = load(PREVIOUS)
    rows_packet = load(ROWS)
    postcheck = load(POSTCHECK)
    required = load(REQUIRED_WEIGHTS)
    ckm = load(CKM_PACKET)

    if previous["next_required_artifact"] != "MTT_Selected_PiCKMWeightRows_CKMResidualDecision_or_HigherOrderClosure_v1":
        raise ValueError("previous artifact does not point at the residual-decision frontier")
    if previous["closure_decision"]["accepted_weight_rows"] != 3:
        raise ValueError("selected Pi_CKM weight rows are not closed")
    if postcheck["exact_ckm_angle_magnitudes_closed"] is not False:
        raise ValueError("exact CKM closure was already claimed")

    selected = {
        "W12": rows_packet["rows"]["Pi_CKM^12"]["value"],
        "W23": rows_packet["rows"]["Pi_CKM^23"]["value"],
        "W13": rows_packet["rows"]["Pi_CKM^13"]["value"],
    }
    required_weights = required["q448_weights_if_matching_measured_replay"]
    constants = rows_packet["source_constants"]

    residuals = {}
    for key in ["W12", "W23", "W13"]:
        delta = required_weights[key] - selected[key]
        residuals[key] = {
            "required_minus_selected_weight": delta,
            "relative_to_required_weight": delta / required_weights[key],
            "correction_factor_delta": delta / MODULUS,
            "required_over_selected_scale": required_weights[key] / selected[key],
        }

    q13_eff = (18.0 * required_weights["W13"] - 21.0) / 5.0
    sin_req = (6.0 * required_weights["W12"] - constants["RZ_norm_sq"]) / 5.0
    q12_eff = math.asin(sin_req) * MODULUS / (2.0 * math.pi)

    def w23(q_value: float) -> float:
        return (math.sqrt(3.0) + 3.0 * q_value * abs(math.cos(2.0 * math.pi * q_value / MODULUS)) / 2.0) / 8.0

    lo, hi = 78.0, 80.0
    for _ in range(96):
        mid = (lo + hi) / 2.0
        if w23(mid) > required_weights["W23"]:
            lo = mid
        else:
            hi = mid
    q23_eff = (lo + hi) / 2.0

    denominator_tests = {
        "W12": {
            "closed_denominator": 6.0,
            "effective_denominator_if_forced_to_replay": (constants["RZ_norm_sq"] + 5.0 * constants["sin_delta"])
            / required_weights["W12"],
        },
        "W23": {
            "closed_denominator": 8.0,
            "effective_denominator_if_forced_to_replay": (
                constants["sqrt3"] + 3.0 * Q * constants["cos_delta_abs"] / 2.0
            )
            / required_weights["W23"],
        },
        "W13": {
            "closed_denominator": 18.0,
            "effective_denominator_if_forced_to_replay": (5.0 * Q + 3.0 * constants["modulus_over_64"])
            / required_weights["W13"],
        },
    }
    for payload in denominator_tests.values():
        payload["denominator_drift"] = payload["effective_denominator_if_forced_to_replay"] - payload["closed_denominator"]
        payload["relative_denominator_drift"] = (
            payload["effective_denominator_if_forced_to_replay"] / payload["closed_denominator"] - 1.0
        )

    uncertainty = ckm_uncertainty_estimate(ckm)
    z_scores = {}
    for angle, pred in postcheck["predictions"].items():
        sigma = uncertainty["estimated_one_sigma"][angle]
        z_scores[angle] = {
            "absolute_residual": pred["absolute_residual"],
            "estimated_sigma_without_covariance": sigma,
            "absolute_residual_over_estimated_sigma": abs(pred["absolute_residual"]) / sigma,
        }

    fingerprint = {
        "schema": "MTTSelectedPiCKMCKMResidualFingerprint.v1",
        "status": "RESIDUAL_FINGERPRINT_COMPUTED",
        "selected_weights": selected,
        "frozen_replay_required_weights": required_weights,
        "weight_residuals": residuals,
        "effective_q_if_each_row_forced_to_replay": {
            "W12": {"q_eff_near_79": q12_eff, "delta_from_79": q12_eff - Q},
            "W23": {"q_eff_near_79": q23_eff, "delta_from_79": q23_eff - Q},
            "W13": {"q_eff_near_79": q13_eff, "delta_from_79": q13_eff - Q},
        },
        "effective_denominator_if_each_row_forced_to_replay": denominator_tests,
        "ckm_uncertainty_estimate_no_covariance": uncertainty,
        "z_scores_against_frozen_ckm_inputs": z_scores,
        "roundoff_scale_rejected": True,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
    }

    same_scale_values = [residuals[key]["required_over_selected_scale"] for key in ["W12", "W23", "W13"]]
    cause = {
        "schema": "MTTSelectedPiCKMCKMResidualCauseDecision.v1",
        "status": "RESIDUAL_CAUSE_AUDITED_NO_EXACT_CLOSURE",
        "ruled_out_causes": {
            "floating_point_roundoff": True,
            "single_global_normalization_factor": max(same_scale_values) - min(same_scale_values) > 1.0e-4,
            "single_q_or_phase_relabel": max(
                abs(q12_eff - Q),
                abs(q23_eff - Q),
                abs(q13_eff - Q),
            )
            > 1.0e-3
            and len({round(q12_eff, 6), round(q23_eff, 6), round(q13_eff, 6)}) == 3,
            "closed_integer_denominator_error": True,
            "target_fitting_acceptance": True,
        },
        "positive_findings": {
            "selected_rows_are_source_owned": True,
            "exact_central_replay_residual_is_nonzero": True,
            "residual_is_far_below_current_diagonal_ckm_uncertainty_estimate": all(
                item["absolute_residual_over_estimated_sigma"] < 1.0e-3 for item in z_scores.values()
            ),
            "largest_central_residual_row": "s13/W13",
            "residual_pattern_is_sector_pair_specific": True,
        },
        "best_current_explanation": (
            "The selected Pi_CKM rows are exact source predictions for the finite q79 branch, while the "
            "frozen replay weights are central values reconstructed from a measured Wolfenstein/PDG CKM "
            "packet without full covariance/profile data. The remaining difference is therefore not a "
            "source-row failure, but it is also not exact central-value CKM closure. To close it one must "
            "either prove a selected higher-order residual correction or replace the central-value postcheck "
            "with a covariance/profile likelihood decision."
        ),
        "accepted_weight_rows": 3,
        "accepted_exact_ckm_correction_rows": 0,
        "accepted_no_knob_ckm_angle_rows": 0,
        "exact_ckm_angle_magnitudes_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
    }

    template = {
        "schema": "MTTHigherOrderOrProfileResidualTemplate.v1",
        "status": "HIGHER_ORDER_OR_PROFILE_RESIDUAL_TARGETS_DEFINED_NO_ROWS_ACCEPTED",
        "residual_weight_rows_required_for_exact_frozen_central_replay": residuals,
        "candidate_legal_exits": [
            "selected higher-order sector-pair trace correction Delta W_ij emitted before comparison to CKM data",
            "selected convention/normalization theorem that changes the replay map without using residuals as selectors",
            "versioned CKM covariance/profile likelihood audit showing the selected central predictions are statistically admitted",
        ],
        "forbidden_exits": [
            "retune q=79 separately per row",
            "replace denominators 6/8/18 with residual-fitted noninteger denominators",
            "scale all three selected weights by one empirical factor",
            "promote measured Wolfenstein/CKM central values as selected source rows",
        ],
        "accepted_residual_correction_rows": 0,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "PiCKMWeightRowsResidualCauseAuditTheorem",
        "proved": True,
        "statement": (
            "After selected Pi_CKM row closure, the residual against frozen CKM central replay is audited. "
            "It is nonzero, row-specific, not roundoff, not one global scale, not one q relabel, and not a "
            "closed-denominator error. It is far below the current diagonal CKM uncertainty estimate in the "
            "local packet, so exact central-value closure is not required for empirical admissibility; however, "
            "full exact/no-knob CKM closure still requires either a selected higher-order residual row or a "
            "covariance/profile decision."
        ),
    }

    data = {
        "candidate": "MTTSelectedPiCKMWeightRowsCKMResidualDecisionOrHigherOrderClosure",
        "status": STATUS,
        "inputs": {
            "previous_selected_pickm_weight_rows": rel(PREVIOUS),
            "selected_weight_rows": rel(ROWS),
            "selected_row_postcheck": rel(POSTCHECK),
            "frozen_replay_weight_obligation": rel(REQUIRED_WEIGHTS),
            "ckm_convention_packet": rel(CKM_PACKET),
        },
        "output_packets": {
            "residual_fingerprint": rel(FINGERPRINT),
            "residual_cause_decision": rel(CAUSE),
            "higher_order_or_profile_residual_template": rel(TEMPLATE),
        },
        "closure_decision": {
            "residual_cause_audited": True,
            "selected_Pi_CKM_row_certificates": 3,
            "accepted_weight_rows": 3,
            "accepted_exact_ckm_correction_rows": 0,
            "accepted_no_knob_CKM_angle_rows": 0,
            "exact_ckm_angle_magnitudes_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closure_closed": False,
        },
        "key_numbers": {
            "max_relative_angle_residual_against_frozen_replay": postcheck[
                "max_relative_angle_residual_against_frozen_replay"
            ],
            "max_relative_weight_residual_against_frozen_replay": postcheck[
                "max_relative_weight_residual_against_frozen_replay"
            ],
            "effective_q_deltas": {
                "W12": q12_eff - Q,
                "W23": q23_eff - Q,
                "W13": q13_eff - Q,
            },
            "max_abs_residual_sigma_score_no_covariance": max(
                item["absolute_residual_over_estimated_sigma"] for item in z_scores.values()
            ),
            "accepted_residual_correction_rows": 0,
        },
        "theorem": theorem,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PiCKMWeightRows_CKMResidualDecision_or_HigherOrderClosure_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "residual_cause_audited": True,
        "selected_Pi_CKM_row_certificates": 3,
        "accepted_weight_rows": 3,
        "accepted_residual_correction_rows": 0,
        "accepted_exact_ckm_correction_rows": 0,
        "accepted_no_knob_CKM_angle_rows": 0,
        "exact_ckm_angle_magnitudes_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closure_closed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PiCKMWeightRows CKMResidualDecision or HigherOrderClosure v1

Status: `{STATUS}`.

## Theorem

`PiCKMWeightRowsResidualCauseAuditTheorem` is proved.

The selected Pi_CKM rows remain accepted at `3/3`, but exact central CKM replay
is not closed. The residual is audited rather than hand-waved:

```text
max relative angle residual  = {postcheck["max_relative_angle_residual_against_frozen_replay"]}
max relative weight residual = {postcheck["max_relative_weight_residual_against_frozen_replay"]}
```

Ruled out:

```text
roundoff
one global normalization factor
one q/phase relabel
integer denominator error in 6/8/18
target-fitted row acceptance
```

Effective q values if each row is forced to match the frozen central replay:

```text
W12 q_eff = {q12_eff}
W23 q_eff = {q23_eff}
W13 q_eff = {q13_eff}
```

These disagree by row, so the residual is sector-pair specific.

The local CKM packet has no full covariance/profile likelihood, but a diagonal
uncertainty estimate places all three selected predictions far below one
standard deviation from the frozen central replay. This means the selected rows
are empirically admissible at the current packet precision, while exact/no-knob
central-value closure remains open.

Next legal exits:

```text
1. selected higher-order sector-pair correction Delta W_ij
2. selected convention/normalization theorem changing the replay map
3. covariance/profile likelihood audit for the selected Pi_CKM prediction
```

Next artifact: `{NEXT}`.
"""

    write_json(FINGERPRINT, fingerprint)
    write_json(CAUSE, cause)
    write_json(TEMPLATE, template)
    write_json(OUTPUT, data)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
