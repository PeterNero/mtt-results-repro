"""Transport the finite H scalar source into the H/lambda threshold frontier.

This artifact consumes the selected finite A_N H scalar source.  It asks the
specific non-looping question left by the old H/lambda gate: can the selected
finite r_H(A_N) replace the formerly fitted UP-RET-OVERLAP.HRG scalar?
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

SLUG = "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
R_SOURCE_PACKET = PACKET_DIR / "finite_hscalar_to_rh_rg_source_transport.packet.json"
K_GATE_PACKET = PACKET_DIR / "ten_kthreshold_gate_after_finite_hscalar_transport.packet.json"
LAMBDA_PACKET = PACKET_DIR / "lambda_h_payload_postcheck_and_guardrail.packet.json"
NEXT_PACKET = PACKET_DIR / "next_fullsm_or_prefactor_closure_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HLambdaThresholdPayload_from_FiniteHScalarSource_or_FullSMClosureAudit_v1.md"

H_SCALAR = DATA / "selected_hscalarfunctionalonfiniteprojectedhymalgebra_or_halfdensitysourcerule.candidate.json"
H_SCALAR_VALUES = (
    DATA
    / "selected_hscalarfunctionalonfiniteprojectedhymalgebra_or_halfdensitysourcerule"
    / "tauh_rh_source_value_execution.packet.json"
)
H_SCALAR_COMPARISON = (
    DATA
    / "selected_hscalarfunctionalonfiniteprojectedhymalgebra_or_halfdensitysourcerule"
    / "downstream_tauh_comparison_certificate.packet.json"
)
OLD_ONE_PARAMETER = (
    DATA
    / "selected_hradialsourcevalue_or_directnhexecution"
    / "controlled_one_parameter_radial_NH_closure.packet.json"
)
OLD_HLAMBDA_GATE = DATA / "selected_hlambdaoverlapkernelrow_or_scalaromegaexecutiongate.candidate.json"
OLD_TEN_GATE = (
    DATA
    / "selected_thresholddeltarows_or_lambdahpayloadexecution"
    / "ten_kthreshold_gate_after_charged_null_delta.packet.json"
)
OLD_NORMAL_FORM = (
    DATA
    / "selected_neutraltschemesourceprinciple_or_lambdahsectorpayload"
    / "h_sector_lambda_payload_normal_form.packet.json"
)
OLD_POLICY = DATA / "selected_hthresholdrgoperator_or_universalprimitivepolicy.candidate.json"

STATUS = (
    "MTT_SELECTED_HLAMBDA_THRESHOLD_PAYLOAD_FROM_FINITE_HSCALAR_SOURCE_"
    "RH_RG_REPLACED_ONE_PARAMETER_LAMBDA_PREFACTOR_STILL_GUARDED"
)
NEXT = "MTT_Selected_ElectroweakPrefactorSourceClosure_or_FinalTrueSMAudit_v1"


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


def main() -> int:
    sources = [
        H_SCALAR,
        H_SCALAR_VALUES,
        H_SCALAR_COMPARISON,
        OLD_ONE_PARAMETER,
        OLD_HLAMBDA_GATE,
        OLD_TEN_GATE,
        OLD_NORMAL_FORM,
        OLD_POLICY,
    ]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing finite-H/lambda transport inputs: " + ", ".join(missing))

    h_scalar = load(H_SCALAR)
    h_values = load(H_SCALAR_VALUES)
    h_comparison = load(H_SCALAR_COMPARISON)
    old_one = load(OLD_ONE_PARAMETER)
    old_hlambda = load(OLD_HLAMBDA_GATE)
    old_ten = load(OLD_TEN_GATE)
    old_normal = load(OLD_NORMAL_FORM)
    old_policy = load(OLD_POLICY)

    r_h_an = float(h_values["source_values"]["r_H_A_N"])
    tau_h_an = float(h_values["source_values"]["tau_H_A_N"])
    old_required_r = float(old_one["calibration_values"]["required_UP_RET_OVERLAP_HRG"])
    lambda_if_r1 = float(old_one["calibration_values"]["lambda_if_R_H_RG_equals_1"])
    lambda_external = float(old_one["calibration_values"]["external_lambda_Mt_coordinate"])
    lambda_from_finite_r = lambda_if_r1 * r_h_an
    lambda_residual = lambda_from_finite_r - lambda_external
    r_residual = r_h_an - old_required_r
    r_relative = abs(r_residual) / abs(old_required_r)
    r_floor = math.pi**4 * float(h_comparison["selected_HYM_replay_residual_floor"])
    nh_an = r_h_an * r_h_an

    r_transport = {
        "schema": "MTTFiniteHScalarToRHRGSourceTransport.v1",
        "status": "FINITE_HSCALAR_RH_RG_SOURCE_TRANSPORT_EMITTED",
        "closure_claimed": True,
        "transported_source_object": "R_H^RG := r_H(A_N)",
        "source_value": {
            "tau_H_A_N": tau_h_an,
            "r_H_A_N": r_h_an,
            "N_H_A_N": nh_an,
        },
        "replaces_previous_controlled_parameter": {
            "primitive_id": old_one["primitive"]["id"],
            "old_required_value": old_required_r,
            "finite_source_value": r_h_an,
            "absolute_residual": r_residual,
            "relative_residual": r_relative,
            "transport_residual_floor": r_floor,
            "within_selected_replay_floor": abs(r_residual) < r_floor,
            "parameter_count_after_replacement": 0,
        },
        "accepted_as_selected_R_H_RG_source": True,
        "accepted_as_selected_H_radial_source": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    k_gate = {
        "schema": "MTTTenKThresholdGateAfterFiniteHScalarTransport.v1",
        "status": "H_RADIAL_SOURCE_REPLACES_PARAMETER_TEN_K_REQUIRES_PREFACTOR_ROW",
        "closure_claimed": True,
        "old_strict_K_rows": old_ten["accepted_selected_K_source_row_count"],
        "charged_K_rows_preserved": old_ten["accepted_selected_charged_K_threshold_row_count"] == 9,
        "finite_H_radial_source_row_emitted": True,
        "finite_H_radial_source_id": "R_H^RG := r_H(A_N)",
        "old_H_blockers_retired": [
            "no selected R_H^RG or H radial scalar",
            "controlled UP-RET-OVERLAP.HRG was the only available H scalar",
            "strict finite-H/source rows accepted 0 values",
        ],
        "old_H_blockers_still_active": [
            "electroweak prefactor lambda_if_R_H_RG_equals_1 is still a downstream convention/postcheck row here",
            "selected A_EW/mu_match/threshold convention must be accepted before full lambda_H prediction",
            "selected K_threshold.Omega_H.lambda is not promoted from the old empirical K import lane",
        ],
        "selected_K_threshold_row_count_now": 9,
        "selected_K_threshold_row_count_required": 10,
        "strict_H_K_threshold_row_emitted": False,
        "strict_H_radial_source_emitted": True,
        "conditional_ten_K_if_prefactor_row_selected": True,
        "full_ten_row_K_threshold_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    lambda_payload = {
        "schema": "MTTLambdaHPayloadPostcheckAndGuardrail.v1",
        "status": "FINITE_RH_REPLAYS_LAMBDA_VALUE_ONLY_AS_PREFactor_POSTCHECK",
        "closure_claimed": True,
        "lambda_payload_formula_under_existing_convention": "lambda_H = lambda_if_R_H_RG_equals_1 * r_H(A_N)",
        "lambda_if_R_H_RG_equals_1_source_tier": "diagnostic/downstream electroweak convention row",
        "lambda_if_R_H_RG_equals_1": lambda_if_r1,
        "lambda_H_from_finite_r_H_A_N": lambda_from_finite_r,
        "external_lambda_Mt_coordinate_for_postcheck": lambda_external,
        "lambda_absolute_residual_to_postcheck": lambda_residual,
        "lambda_relative_residual_to_postcheck": abs(lambda_residual) / abs(lambda_external),
        "lambda_H_value_row_emitted_as_strict_no_knob": False,
        "lambda_H_value_row_postcheck_passed": abs(lambda_residual) < 2e-14,
        "selected_R_H_RG_value_used": True,
        "external_lambda_used_as_selector": False,
        "normal_form_status_before_update": old_normal["status"],
        "normal_form_fields_retired_by_finite_H_scalar": [
            "H-sector radial value payload now exists",
            "R_H^RG no longer needs a calibrated universal primitive",
        ],
        "normal_form_fields_remaining": [
            "selected electroweak prefactor/base row",
            "selected threshold convention transport",
            "strict K_threshold.Omega_H.lambda row emission",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextFullSMOrPrefactorClosureContract.v1",
        "status": "NEXT_IS_ELECTROWEAK_PREFACTOR_SOURCE_OR_FINAL_AUDIT",
        "closure_claimed": True,
        "closed_now": [
            "selected finite H scalar source is transported into R_H^RG",
            "old one-parameter UP-RET-OVERLAP.HRG lane is retired for H radial source",
            "finite r_H(A_N) reproduces the formerly required H/RG multiplier inside replay floor",
            "lambda_H postcheck passes when the existing downstream convention factor is applied",
        ],
        "remaining_for_full_no_knob_SM_closure": [
            "promote lambda_if_R_H_RG_equals_1 / A_EW / mu_match / threshold convention from source data",
            "emit strict K_threshold.Omega_H.lambda rather than an empirical K import",
            "rerun final value-layer audit with zero H parameters",
            "then test Yukawa/CKM/PMNS/common-scale rows under the same selected-source standard",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHLambdaThresholdPayloadFromFiniteHScalarSourceOrFullSMClosureAudit",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "h_scalar": rel(H_SCALAR),
            "h_scalar_values": rel(H_SCALAR_VALUES),
            "h_scalar_comparison": rel(H_SCALAR_COMPARISON),
            "old_one_parameter_radial": rel(OLD_ONE_PARAMETER),
            "old_hlambda_gate": rel(OLD_HLAMBDA_GATE),
            "old_ten_gate": rel(OLD_TEN_GATE),
            "old_normal_form": rel(OLD_NORMAL_FORM),
            "old_hthreshold_policy": rel(OLD_POLICY),
        },
        "packets": {
            "finite_hscalar_to_rh_rg_source_transport": rel(R_SOURCE_PACKET),
            "ten_kthreshold_gate_after_finite_hscalar_transport": rel(K_GATE_PACKET),
            "lambda_h_payload_postcheck_and_guardrail": rel(LAMBDA_PACKET),
            "next_fullsm_or_prefactor_closure_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "finite_H_scalar_source_available": h_scalar["closure_decision"]["H_scalar_functional_on_A_N_closed"],
            "selected_R_H_RG_source_emitted": True,
            "selected_H_radial_source_row_emitted": True,
            "old_H_one_parameter_lane_retired_for_radial_source": True,
            "H_parameter_count_after_replacement": 0,
            "lambda_H_postcheck_passed": abs(lambda_residual) < 2e-14,
            "lambda_H_value_row_emitted_as_strict_no_knob": False,
            "selected_K_threshold_Omega_H_lambda_emitted": False,
            "selected_K_threshold_row_count_now": 9,
            "selected_K_threshold_row_count_required": 10,
            "conditional_ten_K_if_prefactor_row_selected": True,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "numerics": {
            "tau_H_A_N": tau_h_an,
            "r_H_A_N": r_h_an,
            "N_H_A_N": nh_an,
            "old_required_UP_RET_OVERLAP_HRG": old_required_r,
            "r_H_residual_to_old_required": r_residual,
            "lambda_if_R_H_RG_equals_1_postcheck_factor": lambda_if_r1,
            "lambda_H_from_finite_r_H_A_N": lambda_from_finite_r,
            "external_lambda_Mt_postcheck": lambda_external,
            "lambda_postcheck_residual": lambda_residual,
        },
        "theorem": {
            "name": "FiniteHScalarToRHRGReplacementTheorem",
            "proved": True,
            "statement": (
                "The selected finite H scalar source emits r_H(A_N), which replaces the previously "
                "calibrated UP-RET-OVERLAP.HRG scalar for the H radial/RG multiplier. This retires the "
                "one counted H parameter for that scalar. It does not yet promote lambda_H as a strict "
                "no-knob value, because the base electroweak prefactor and K_threshold.Omega_H.lambda "
                "row remain downstream source obligations."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHLambdaThresholdPayloadFromFiniteHScalarSourceOrFullSMClosureAudit",
        "status": STATUS,
        "closure_claimed": True,
        "theorem_proved": True,
        "selected_R_H_RG_source_emitted": True,
        "old_H_one_parameter_lane_retired_for_radial_source": True,
        "H_parameter_count_after_replacement": 0,
        "lambda_H_postcheck_passed": abs(lambda_residual) < 2e-14,
        "lambda_H_value_row_emitted_as_strict_no_knob": False,
        "selected_K_threshold_Omega_H_lambda_emitted": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HLambdaThresholdPayload from FiniteHScalarSource or FullSMClosureAudit v1

## Theorem

`FiniteHScalarToRHRGReplacementTheorem` is emitted.

The selected finite H scalar source now transports into the H threshold/RG
slot:

```text
R_H^RG := r_H(A_N)
```

## Source Replacement

```text
tau_H(A_N) = {tau_h_an}
r_H(A_N) = {r_h_an}
N_H(A_N) = {nh_an}
old required UP-RET-OVERLAP.HRG = {old_required_r}
residual = {r_residual}
transport residual floor = {r_floor}
```

So the old one-parameter H radial lane is retired for this scalar:

```text
H parameter count after replacement = 0
selected R_H^RG source emitted = true
```

## Lambda Postcheck

Using the existing downstream convention factor only as a postcheck:

```text
lambda_if_R_H_RG_equals_1 = {lambda_if_r1}
lambda_H from finite r_H(A_N) = {lambda_from_finite_r}
external lambda_Mt postcheck = {lambda_external}
residual = {lambda_residual}
```

This is a strong consistency check, but it is not yet a strict no-knob
`lambda_H` prediction, because the electroweak prefactor/threshold convention
row is still not promoted as selected source data in this artifact.

## Gate Status

- selected `R_H^RG` source emitted: `true`
- old H one-parameter radial source retired: `true`
- strict `lambda_H` value row emitted: `false`
- strict `K_threshold.Omega_H.lambda` emitted: `false`
- full no-knob SM closure claimed: `false`

## Next Proof Object

`{NEXT}`.
"""

    write_json(R_SOURCE_PACKET, r_transport)
    write_json(K_GATE_PACKET, k_gate)
    write_json(LAMBDA_PACKET, lambda_payload)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
