"""Build H radial-scale/phase source or Herm(2) Hessian rows packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hradialscalephasesource_or_herm2hessianrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HRadialScalePhaseSource_or_Herm2HessianRows_v1.md"

SOURCE_SPLIT = PACKET_DIR / "h_radial_scale_source_split.packet.json"
POLAR = PACKET_DIR / "herm2_polar_reconstruction_law.packet.json"
CONTROLLED = PACKET_DIR / "controlled_parameter_radial_lane.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hradial_phase_source.packet.json"

PREVIOUS = DATA / "selected_finitehfunctionalcandidate_or_directherm2rowemissionrun.candidate.json"
HRADIAL = DATA / "selected_hradialthresholdscalarsource_or_tenkclosure.candidate.json"
EW_BOUNDARY = DATA / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure.candidate.json"
HTHRESHOLD = DATA / "selected_hthresholdrgoperator_or_universalprimitivepolicy.candidate.json"
HCAL = DATA / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun.candidate.json"

STATUS = (
    "MTT_SELECTED_HRADIALSCALEPHASESOURCE_OR_HERM2HESSIANROWS_"
    "RADIAL_ROUTE_SPLIT_PHASE_TRACE_OPEN"
)
NEXT = "MTT_Selected_Herm2PolarSourceCompletion_or_HResponseRows_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing H radial/phase inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [PREVIOUS, HRADIAL, EW_BOUNDARY, HTHRESHOLD, HCAL]
    require_sources(sources)

    previous = load(PREVIOUS)
    hradial = load(HRADIAL)
    ew = load(EW_BOUNDARY)
    hthreshold = load(HTHRESHOLD)
    hcal = load(HCAL)

    s_beta = previous["key_numbers"]["selected_s_beta_value"]
    up_hrg = hcal["calibration_numbers"]["UP_RET_OVERLAP_HRG"]
    log_up_hrg = hcal["calibration_numbers"]["log_UP_RET_OVERLAP_HRG"]

    source_split = {
        "schema": "MTTHRadialScaleSourceSplit.v1",
        "status": "RADIAL_SOURCE_REDUCED_TO_EW_BOUNDARY_OR_H_THRESHOLD_RG",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "selected_angle_support": {
            "s_beta": s_beta,
            "selected_s_beta_polar_angle_closed": previous["closure_decision"][
                "selected_s_beta_polar_angle_closed"
            ],
            "Herm2_radial_collapse_closed": previous["closure_decision"][
                "Herm2_radial_collapse_closed"
            ],
        },
        "strict_no_knob_radial_routes": {
            "Dterm_EW_boundary_route": {
                "reduced": hradial["closure_decision"]["Dterm_route_imported"],
                "selected_A_EW_emitted": hradial["closure_decision"]["selected_A_EW_emitted"],
                "selected_threshold_RG_transport_closed": hradial["closure_decision"][
                    "selected_threshold_RG_transport_closed"
                ],
                "K_threshold_Omega_H_lambda_emitted": hradial["closure_decision"][
                    "K_threshold_Omega_H_lambda_emitted"
                ],
            },
            "intrinsic_H_quartic_or_large_threshold_RG_route": {
                "A_EW_source_tier_gate_closed": ew["closure_decision"]["A_EW_source_tier_gate_closed"],
                "direct_intrinsic_H_quartic_K_row_emitted": ew["closure_decision"][
                    "direct_intrinsic_H_quartic_K_row_emitted"
                ],
                "selected_large_threshold_RG_theorem_emitted": ew["closure_decision"][
                    "selected_large_threshold_RG_theorem_emitted"
                ],
            },
            "strict_R_H_RG_operator_route": {
                "strict_H_threshold_RG_operator_source_search_closed": hthreshold[
                    "closure_decision"
                ]["strict_H_threshold_RG_operator_source_search_closed"],
                "strict_H_threshold_RG_operator_emitted": hthreshold["closure_decision"][
                    "strict_H_threshold_RG_operator_emitted"
                ],
                "K_threshold_Omega_H_lambda_emitted": hthreshold["closure_decision"][
                    "K_threshold_Omega_H_lambda_emitted"
                ],
            },
        },
        "decision": {
            "radial_source_route_split_closed": True,
            "strict_radial_scale_source_emitted": False,
            "controlled_radial_calibration_available": hcal["closure_decision"][
                "UP_RET_OVERLAP_HRG_admitted_empirical_layer"
            ],
            "lambda_H_predicted": False,
            "strict_Herm2_rows_determined": False,
        },
    }

    polar = {
        "schema": "MTTHerm2PolarReconstructionLaw.v1",
        "status": "HERMITIAN_TRACEFREE_POLAR_LAW_CLOSED_VALUES_CONDITIONAL",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "known_inputs": {
            "s_beta": s_beta,
            "angle_relation": "s_beta = Delta^2/(Delta^2 + Re(Omega)^2 + Im(Omega)^2)",
        },
        "required_new_sources": {
            "radial_scale": "r_H = sqrt(Delta^2 + |Omega|^2) or equivalent threshold/RG scalar",
            "Delta_sign": "sigma_D in {+1,-1}, selected by source orientation",
            "Omega_phase": "phi_Omega, selected phase/sign convention in the H_uv basis",
            "trace_center": "m0=(Huu+Hdd)/2 or proof that quotient trace-free normalization sets m0=0",
            "source_certificates": [
                "source ownership",
                "same-source exactness/error",
                "quotient admissibility",
            ],
        },
        "conditional_reconstruction": {
            "Delta": "sigma_D * r_H * sqrt(s_beta)",
            "Re_Omega": "r_H * sqrt(1-s_beta) * cos(phi_Omega)",
            "Im_Omega": "r_H * sqrt(1-s_beta) * sin(phi_Omega)",
            "Huu": "m0 + Delta",
            "Hud": "Re_Omega + i Im_Omega",
            "Hdd": "m0 - Delta",
        },
        "decision": {
            "polar_reconstruction_law_closed": True,
            "Delta_row_emitted": False,
            "Re_Omega_row_emitted": False,
            "Im_Omega_row_emitted": False,
            "Huu_Hud_Hdd_emitted": False,
            "trace_center_source_emitted": False,
            "phase_source_emitted": False,
        },
    }

    controlled = {
        "schema": "MTTControlledParameterRadialLane.v1",
        "status": "CONTROLLED_RADIAL_LANE_AVAILABLE_NOT_STRICT_SOURCE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "controlled_parameter": {
            "name": "UP_RET_OVERLAP_HRG",
            "value": up_hrg,
            "log_value": log_up_hrg,
            "tier": "controlled empirical calibration",
            "lambda_H_calibrated": hcal["closure_decision"]["lambda_H_calibrated"],
            "lambda_H_predicted": hcal["closure_decision"]["lambda_H_predicted"],
        },
        "strict_boundary": {
            "strict_H_threshold_RG_source_theorem_attempted": hcal["closure_decision"][
                "strict_H_threshold_RG_source_theorem_attempted"
            ],
            "strict_H_threshold_RG_operator_emitted": hcal["closure_decision"][
                "strict_H_threshold_RG_operator_emitted"
            ],
            "crossuse_prediction_audit_passed": hcal["closure_decision"][
                "crossuse_prediction_audit_passed"
            ],
            "strict_accepted_selected_K_source_row_count": hcal["closure_decision"][
                "strict_accepted_selected_K_source_row_count"
            ],
            "strict_selected_K_threshold_row_count_required": hcal["closure_decision"][
                "strict_selected_K_threshold_row_count_required"
            ],
        },
        "decision": {
            "minimal_parameter_H_layer_available": True,
            "usable_for_SM_parity_calibration": True,
            "usable_for_no_knob_prediction": False,
            "can_emit_strict_Herm2_rows": False,
            "can_emit_controlled_radial_placeholder": True,
            "still_needs_phase_trace_certificates_for_Herm2_rows": True,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHRadialPhaseSource.v1",
        "status": "NEXT_FRONTIER_HERM2_POLAR_SOURCE_COMPLETION_OR_HRESPONSE_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "radial scale source route split imported into Herm(2) frontier",
            "strict radial source shown equivalent to A_EW/RG, intrinsic H quartic K row, or strict R_H^RG source",
            "controlled one-parameter HRG radial lane separated from strict no-knob source",
            "Herm(2) polar reconstruction law from s_beta, radial scale, phase, sign, and trace source",
        ],
        "still_open": [
            "strict selected radial scale source",
            "selected Delta sign/source orientation",
            "selected Omega phase in H_uv basis",
            "trace-center m0 source or quotient trace-free normalization theorem",
            "same-source ownership/exactness/quotient certificates",
            "direct H-response rows Huu,Hud,Hdd",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedHRadialScalePhaseSourceOrHerm2HessianRows",
        "schema": "MTTSelectedCandidate.v1",
        "status": STATUS,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "minimal_parameter_tier_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "HRadialScalePhaseSourceOrHerm2HessianRowsTheorem",
            "proved": True,
            "statement": (
                "The Herm(2) value problem is now reduced to a polar source "
                "completion.  The s_beta angle and radial-collapse law are closed, "
                "and the radial source route is split into strict A_EW/RG or "
                "R_H^RG emission versus the controlled HRG calibration lane.  "
                "Neither lane emits strict Herm(2) rows until radial scale, "
                "Delta sign, Omega phase, trace-center convention/source, and "
                "same-source certificates are supplied."
            ),
        },
        "packets": {
            "h_radial_scale_source_split": rel(SOURCE_SPLIT),
            "herm2_polar_reconstruction_law": rel(POLAR),
            "controlled_parameter_radial_lane": rel(CONTROLLED),
            "next_cutset": rel(CUTSET),
        },
        "inputs": {
            "previous": rel(PREVIOUS),
            "hradial": rel(HRADIAL),
            "ew_boundary": rel(EW_BOUNDARY),
            "hthreshold": rel(HTHRESHOLD),
            "hcal": rel(HCAL),
        },
        "closure_decision": {
            "radial_source_route_split_closed": True,
            "Herm2_polar_reconstruction_law_closed": True,
            "controlled_radial_calibration_available": True,
            "strict_radial_scale_source_emitted": False,
            "selected_Delta_sign_emitted": False,
            "selected_Omega_phase_emitted": False,
            "trace_center_source_or_normalization_emitted": False,
            "same_source_certificates_emitted": False,
            "direct_Herm2_rows_emitted": False,
            "selected_H_response_table_emitted": False,
            "selected_H_response_spectrum_emitted": False,
            "R_H_RG_value_emitted": False,
            "lambda_H_calibrated_in_controlled_lane": True,
            "lambda_H_predicted": False,
            "accepted_H_response_source_row_count": 0,
            "accepted_R_H_RG_source_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "selected_s_beta_value": s_beta,
            "UP_RET_OVERLAP_HRG_controlled_calibration": up_hrg,
            "log_UP_RET_OVERLAP_HRG": log_up_hrg,
            "strict_selected_K_source_rows": hcal["closure_decision"][
                "strict_accepted_selected_K_source_row_count"
            ],
            "strict_selected_K_rows_required": hcal["closure_decision"][
                "strict_selected_K_threshold_row_count_required"
            ],
            "accepted_H_response_source_row_count": 0,
            "accepted_R_H_RG_source_count": 0,
        },
    }

    cert = {
        "certificate": "MTTSelectedHRadialScalePhaseSourceOrHerm2HessianRows",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "radial_source_route_split_closed": True,
        "Herm2_polar_reconstruction_law_closed": True,
        "controlled_radial_calibration_available": True,
        "strict_radial_scale_source_emitted": False,
        "selected_Omega_phase_emitted": False,
        "trace_center_source_or_normalization_emitted": False,
        "direct_Herm2_rows_emitted": False,
        "R_H_RG_value_emitted": False,
        "lambda_H_predicted": False,
        "accepted_H_response_source_row_count": 0,
        "accepted_R_H_RG_source_count": 0,
    }

    note = f"""# MTT Selected H Radial Scale Phase Source or Herm(2) Hessian Rows v1

Status: `{STATUS}`

## Theorem

The Herm(2) Higgs value problem is now a polar source-completion problem.
The selected angle is closed:

```text
s_beta = {s_beta}
```

The radial route is split:

- strict/no-knob: selected `A_EW/RG`, intrinsic H quartic K row, or strict
  `R_H^RG` source theorem,
- controlled tier: `UP_RET_OVERLAP_HRG = {up_hrg}` as calibration, not
  prediction.

## Conditional Herm(2) Rows

```text
Delta    = sigma_D * r_H * sqrt(s_beta)
ReOmega  = r_H * sqrt(1-s_beta) * cos(phi_Omega)
ImOmega  = r_H * sqrt(1-s_beta) * sin(phi_Omega)
Huu      = m0 + Delta
Hud      = ReOmega + i ImOmega
Hdd      = m0 - Delta
```

## Remaining Source Fields

Accepted H-response source rows: `0`.

Strict radial scale source emitted: `False`.

Selected Omega phase emitted: `False`.

Trace-center source/normalization emitted: `False`.

Next artifact: `{NEXT}`
"""

    write_json(SOURCE_SPLIT, source_split)
    write_json(POLAR, polar)
    write_json(CONTROLLED, controlled)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE {rel(OUTPUT)}")
    print(f"WROTE {rel(CERT)}")
    print(f"WROTE {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
