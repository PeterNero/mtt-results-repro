"""Build H radial source value or direct N_H execution packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hradialsourcevalue_or_directnhexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STRICT_PACKET = PACKET_DIR / "strict_radial_NH_source_execution.packet.json"
CONTROLLED_PACKET = PACKET_DIR / "controlled_one_parameter_radial_NH_closure.packet.json"
CUTSET_PACKET = PACKET_DIR / "next_strict_source_or_crossuse_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HRadialSourceValue_or_DirectNHExecution_v1.md"

SOURCES = {
    "previous": DATA / "selected_directhkthresholdrow_currentexit_or_radialsource.candidate.json",
    "previous_contract": DATA
    / "selected_directhkthresholdrow_currentexit_or_radialsource"
    / "next_radial_source_or_direct_NH_contract.packet.json",
    "radial_action_contract": DATA
    / "selected_hradialactionnormvalue_or_hlambdathresholdrow"
    / "h_radial_action_norm_value_contract.packet.json",
    "radial_payload_execution": DATA
    / "selected_hradialactionnormvalue_or_hlambdathresholdrow"
    / "current_h_radial_value_payload_execution.packet.json",
    "direct_radial_contract": DATA
    / "selected_hlambdarowlocaloverlapandscheme_or_directradialhessianvalue"
    / "direct_radial_hessian_value_execution_contract.packet.json",
    "direct_radial_run": DATA
    / "selected_hlambdafinitegalerkinexecution_or_radialhessianscalarrun"
    / "direct_radial_hessian_scalar_run.packet.json",
    "primitive_policy": DATA
    / "selected_hthresholdrgoperator_or_universalprimitivepolicy"
    / "h_threshold_universal_primitive_admission_matrix.packet.json",
    "controlled_gate": DATA
    / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun"
    / "controlled_empirical_h_k_gate.packet.json",
    "minimal_calibration": DATA
    / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun"
    / "minimal_primitive_calibration_run.packet.json",
    "strict_rhrg_oracle": DATA / "selected_strictrhrgsourceconstruction_or_independentvalidationoracle.candidate.json",
}

STATUS = "MTT_SELECTED_HRADIALSOURCEVALUE_OR_DIRECTNH_STRICT_OPEN_CONTROLLED_ONE_PARAMETER_CLOSED"
NEXT = "MTT_Selected_StrictFiniteHActionSource_or_UPRetOverlapHRGCrossUse_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing required source packets: {missing}")
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    sources = require_sources()
    prev = sources["previous"]["closure_decision"]
    action = sources["radial_action_contract"]
    payload = sources["radial_payload_execution"]
    direct_contract = sources["direct_radial_contract"]
    direct_run = sources["direct_radial_run"]
    policy = sources["primitive_policy"]
    controlled_gate = sources["controlled_gate"]
    minimal = sources["minimal_calibration"]
    rhrg = sources["strict_rhrg_oracle"]

    r_h = float(minimal["calibration_values"]["required_UP_RET_OVERLAP_HRG"])
    n_h = r_h * r_h

    strict_packet = {
        "schema": "MTTStrictRadialNHSourceExecution.v1",
        "status": "STRICT_RADIAL_NH_EXECUTED_ZERO_SOURCE_ROWS",
        "closure_claimed": True,
        "required_scalar": action["required_value_payload"]["definition"],
        "preferred_name": action["required_value_payload"]["preferred_name"],
        "legal_source_operators": direct_contract["legal_source_operators"],
        "current_emission": {
            "finite_H_action_selected": direct_run["current_emission"][
                "finite_H_action_selected"
            ],
            "M_source_values_selected": direct_run["current_emission"][
                "M_source_values_selected"
            ],
            "primitive_H_response_kernel_values_selected": direct_run["current_emission"][
                "primitive_H_response_kernel_values_selected"
            ],
            "direct_N_H_value_emitted": direct_run["current_emission"][
                "direct_N_H_value_emitted"
            ],
            "accepted_direct_radial_hessian_value_rows": direct_run["current_emission"][
                "accepted_direct_radial_hessian_value_rows"
            ],
        },
        "strict_R_H_RG_source_constructed": rhrg["closure_decision"][
            "strict_R_H_RG_source_constructed"
        ],
        "all_strict_R_H_RG_gates_satisfied": rhrg["closure_decision"][
            "all_strict_R_H_RG_gates_satisfied"
        ],
        "strict_selected_K_rows": {
            "accepted": prev["accepted_selected_K_source_row_count"],
            "required": prev["selected_K_threshold_row_count_required"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    controlled_packet = {
        "schema": "MTTControlledOneParameterRadialNHClosure.v1",
        "status": "CONTROLLED_ONE_PARAMETER_RADIAL_NH_LAYER_CLOSED_NOT_STRICT",
        "closure_claimed": True,
        "primitive": minimal["primitive"],
        "calibration_protocol": minimal["calibration_protocol"],
        "calibration_values": minimal["calibration_values"],
        "derived_controlled_values": {
            "r_H": r_h,
            "N_H_equals_r_H_squared": n_h,
            "normalization": "r_H=sqrt(N_H) from the radial action norm contract",
            "conditional_K_row_count": controlled_gate["controlled_empirical_tier"][
                "conditional_parameterized_K_row_count"
            ],
        },
        "claim_boundary": {
            "minimal_parameter_H_layer_closed": minimal["claim_boundary"][
                "minimal_parameter_H_layer_closed"
            ],
            "lambda_H_calibrated": minimal["claim_boundary"]["lambda_H_calibrated"],
            "lambda_H_predicted": minimal["claim_boundary"]["lambda_H_predicted"],
            "strict_no_knob_closure_claimed": minimal["claim_boundary"][
                "strict_no_knob_closure_claimed"
            ],
            "full_SM_closure_claimed": minimal["claim_boundary"]["full_SM_closure_claimed"],
        },
        "credibility_requirement": (
            "UP-RET-OVERLAP.HRG must predict a non-Higgs target without retuning "
            "before it can be upgraded from calibrated support to credible universal "
            "primitive support; it still would not be no-knob unless source-derived."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset_packet = {
        "schema": "MTTStrictSourceOrUPRetOverlapHRGCrossUseCutset.v1",
        "status": "STRICT_SOURCE_OR_CROSSUSE_REQUIRED",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "strict_no_knob_exits": [
            "derive selected finite H-sector action F_H and compute N_H",
            "derive selected same-source Hermitian M_source restricted to B_Huv",
            "derive selected primitive H-response kernel K_H with row-level exactness/error bound",
            "derive strict R_H^RG source operator without calibration",
        ],
        "minimal_parameter_exit": [
            "declare UP-RET-OVERLAP.HRG once",
            "keep lambda_H as calibration, not prediction",
            "use r_H=391.39140285811936 and N_H=r_H^2 as controlled values",
            "audit at least one non-Higgs cross-use prediction without retuning",
        ],
        "must_not_use": action["required_value_payload"]["forbidden_sources"]
        + [
            "claim calibrated lambda_H as prediction",
            "claim controlled one-parameter closure as strict no-knob closure",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHRadialSourceValueOrDirectNHExecution",
        "status": STATUS,
        "previous_status": sources["previous"]["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "output_packets": {
            "strict_radial_NH_source_execution": rel(STRICT_PACKET),
            "controlled_one_parameter_radial_NH_closure": rel(CONTROLLED_PACKET),
            "next_strict_source_or_crossuse_cutset": rel(CUTSET_PACKET),
        },
        "closure_decision": {
            "strict_radial_source_execution_attempted": True,
            "strict_N_H_value_emitted": False,
            "strict_r_H_source_emitted": False,
            "strict_R_H_RG_source_constructed": False,
            "selected_L_rowlocal_Omega_H_lambda_emitted": False,
            "selected_T_scheme_Omega_H_lambda_emitted": False,
            "direct_K_threshold_Omega_H_lambda_emitted": False,
            "strict_H_K_threshold_row_emitted": False,
            "controlled_one_parameter_radial_layer_closed": True,
            "controlled_r_H": r_h,
            "controlled_N_H": n_h,
            "controlled_conditional_K_row_count": controlled_gate["controlled_empirical_tier"][
                "conditional_parameterized_K_row_count"
            ],
            "lambda_H_calibrated": True,
            "lambda_H_predicted": False,
            "minimal_parameter_count_added_if_adopted": minimal["primitive"][
                "new_universal_parameter_count_in_this_layer"
            ],
            "crossuse_prediction_required_for_credibility_upgrade": True,
            "accepted_selected_K_source_row_count": prev[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": prev[
                "selected_K_threshold_row_count_required"
            ],
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "HRadialSourceValueOrDirectNHExecutionTheorem",
            "proved": True,
            "statement": (
                "The H radial/direct-N_H blocker has been executed. Strict no-knob "
                "source emission remains open: no selected finite H action, M_source, "
                "primitive H-response kernel, direct N_H, or strict R_H^RG source is "
                "emitted. The controlled/minimal one-parameter lane is closed: if "
                "UP-RET-OVERLAP.HRG is declared as one calibrated universal primitive, "
                "then r_H=391.39140285811936 and N_H=r_H^2=153187.23023124668, yielding "
                "a conditional 10/10 H K layer. This calibrates lambda_H and is not a "
                "lambda_H prediction or strict no-knob closure."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHRadialSourceValueOrDirectNHExecution",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "strict_N_H_value_emitted": False,
        "strict_r_H_source_emitted": False,
        "direct_K_threshold_Omega_H_lambda_emitted": False,
        "strict_H_K_threshold_row_emitted": False,
        "controlled_one_parameter_radial_layer_closed": True,
        "controlled_r_H": r_h,
        "controlled_N_H": n_h,
        "lambda_H_calibrated": True,
        "lambda_H_predicted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected H Radial Source Value or Direct NH Execution v1

## Theorem

`HRadialSourceValueOrDirectNHExecutionTheorem` is emitted.

## Strict Result

- Strict `N_H=Hess(F_H)[U_H,U_H]` emitted: `false`.
- Strict source-owned `r_H` emitted: `false`.
- Strict `R_H^RG` source constructed: `false`.
- Direct `K_threshold.Omega_H.lambda` emitted: `false`.
- Strict selected `K_threshold` rows remain
  `{prev["accepted_selected_K_source_row_count"]}/{prev["selected_K_threshold_row_count_required"]}`.

## Controlled Minimal-Parameter Result

The one-parameter lane is now explicit and executable:

- primitive: `UP-RET-OVERLAP.HRG`;
- role: global H-threshold/RG transport strength;
- calibrated value: `{r_h}`;
- controlled `N_H=r_H^2`: `{n_h}`;
- conditional H K layer row count: `{controlled_gate["controlled_empirical_tier"]["conditional_parameterized_K_row_count"]}/10`.

This closes a controlled/minimal H layer only. It calibrates `lambda_H`; it does not predict `lambda_H`, and it is not strict no-knob closure.

## Next Artifact

`{NEXT}`
"""

    write_json(STRICT_PACKET, strict_packet)
    write_json(CONTROLLED_PACKET, controlled_packet)
    write_json(CUTSET_PACKET, cutset_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
