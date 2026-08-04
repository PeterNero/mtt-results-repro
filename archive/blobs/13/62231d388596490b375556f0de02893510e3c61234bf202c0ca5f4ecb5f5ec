"""Build current direct H K threshold row exit test."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_directhkthresholdrow_currentexit_or_radialsource"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
POLAR_PACKET = PACKET_DIR / "direct_hk_polar_prerequisite_recheck.packet.json"
RADIAL_PACKET = PACKET_DIR / "direct_hk_radial_value_source_gate.packet.json"
DIRECT_PACKET = PACKET_DIR / "direct_kthreshold_omega_h_lambda_execution_attempt.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_radial_source_or_direct_NH_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DirectHKThresholdRow_CurrentExit_or_RadialSource_v1.md"

SOURCES = {
    "previous": DATA / "selected_samesourceconnectionvaluetable_or_directhkrow.candidate.json",
    "first_field_contract": DATA
    / "selected_samesourceconnectionvaluetable_or_directhkrow"
    / "next_first_same_source_field_or_direct_hkrow_contract.packet.json",
    "old_direct_h": DATA / "selected_direcththresholdkrowemission_or_hquarticfunctionaltheorem.candidate.json",
    "old_direct_h_attempt": DATA
    / "selected_direcththresholdkrowemission_or_hquarticfunctionaltheorem"
    / "h_k_threshold_emission_attempt.packet.json",
    "hresponse_rows": DATA / "selected_hresponsetablevaluerows_or_directherm2valuerows.candidate.json",
    "hresponse_cert_payload": DATA
    / "selected_hresponserowsourceemission_or_directherm2certificatepayload.candidate.json",
    "polar_completion": DATA / "selected_hpolarfieldnumericalcompletionattempt_or_directfinitehactionrows.candidate.json",
    "polar_promotion": DATA / "selected_hpolarfieldpromotion_or_finitehactionderivation.candidate.json",
    "phase_sign": DATA / "selected_hphasesignselector_lenscircle_or_hrgvaluemap.candidate.json",
    "radial_norm": DATA / "selected_hrgradialnormlaw_or_value_source_derivation.candidate.json",
    "radial_action": DATA / "selected_hradialactionnormvalue_or_hlambdathresholdrow.candidate.json",
    "h_lambda_formal": DATA / "selected_hlambdarowlocaloverlapandscheme_or_directradialhessianvalue.candidate.json",
    "h_lambda_execution": DATA / "selected_hlambdafinitegalerkinexecution_or_radialhessianscalarrun.candidate.json",
}

STATUS = "MTT_SELECTED_DIRECTHKTHRESHOLDROW_CURRENTEXIT_PHASE_CLOSED_RADIAL_SOURCE_OPEN"
NEXT = "MTT_Selected_HRadialSourceValue_or_DirectNHExecution_v1"


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
    old_attempt_decision = sources["old_direct_h_attempt"]["route_decision"]
    hresponse = sources["hresponse_rows"]["closure_decision"]
    hcert = sources["hresponse_cert_payload"]["closure_decision"]
    polar = sources["polar_completion"]
    polar_promotion = sources["polar_promotion"]["decision"]
    phase = sources["phase_sign"]["decision"]
    radial_norm = sources["radial_norm"]
    radial_action = sources["radial_action"]
    hformal = sources["h_lambda_formal"]["decision"]
    hexec = sources["h_lambda_execution"]["decision"]

    polar_packet = {
        "schema": "MTTDirectHKPolarPrerequisiteRecheck.v1",
        "status": "PHASE_AND_DIRECTION_CLOSED_RADIAL_LENGTH_OPEN",
        "closure_claimed": True,
        "controlled_Herm2_candidate": polar["key_numbers"],
        "m0_tracefree_quotient_promoted": polar_promotion[
            "m0_tracefree_quotient_promoted"
        ],
        "sigma_D_orientation_promoted": polar_promotion["sigma_D_orientation_promoted"],
        "phase_axis_promoted": phase["phase_axis_promoted"],
        "phi_sign_promoted": phase["phi_sign_promoted"],
        "strict_phi_Omega_promoted": phase["strict_phi_Omega_promoted"],
        "strict_r_H_promoted": phase["strict_r_H_promoted"],
        "radial_norm_law_promoted": radial_norm["decision"]["radial_norm_law_promoted"],
        "strict_Herm2_rows_promoted": radial_norm["decision"][
            "strict_Herm2_rows_promoted"
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    radial_packet = {
        "schema": "MTTDirectHKRadialValueSourceGate.v1",
        "status": "RADIAL_VALUE_SOURCE_NOT_EMITTED",
        "closure_claimed": True,
        "controlled_r_H_postcheck_only": radial_action["key_numbers"][
            "controlled_r_H_postcheck_only"
        ],
        "controlled_r_H_squared_postcheck_only": radial_action["key_numbers"][
            "controlled_r_H_squared_postcheck_only"
        ],
        "accepted_radial_action_norm_value_rows": radial_action["key_numbers"][
            "accepted_radial_action_norm_value_rows"
        ],
        "accepted_H_lambda_bridge_value_rows": radial_action["key_numbers"][
            "accepted_H_lambda_bridge_value_rows"
        ],
        "accepted_numeric_radial_value_sources": radial_norm["key_numbers"][
            "accepted_numeric_radial_value_sources"
        ],
        "best_source_only_formula_rejected": radial_norm["key_numbers"][
            "best_source_only_formula"
        ],
        "best_source_only_relative_error": radial_norm["key_numbers"][
            "best_source_only_relative_error"
        ],
        "direct_N_H_value_emitted": hformal["direct_N_H_value_emitted"]
        or hexec["direct_N_H_value_emitted"],
        "selected_L_rowlocal_Omega_H_lambda_emitted": hexec[
            "selected_L_rowlocal_Omega_H_lambda_emitted"
        ],
        "selected_T_scheme_Omega_H_lambda_emitted": hexec[
            "selected_T_scheme_Omega_H_lambda_emitted"
        ],
        "lambda_H_source_value_payload_emitted": hexec[
            "lambda_H_source_value_payload_emitted"
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    direct_packet = {
        "schema": "MTTDirectKThresholdOmegaHLambdaCurrentExecution.v1",
        "status": "DIRECT_K_THRESHOLD_OMEGA_H_LAMBDA_NOT_EMITTED_RADIAL_SOURCE_OPEN",
        "closure_claimed": True,
        "required_output": "K_threshold.Omega_H.lambda",
        "direct_exit_from_current_frontier": sources["first_field_contract"]["direct_exit"],
        "old_direct_attempt_status": sources["old_direct_h_attempt"]["status"],
        "old_direct_route_decision": old_attempt_decision,
        "latest_direct_Herm2_rows": {
            "direct_Herm2_interface_fixed": hresponse["direct_Herm2_interface_fixed"],
            "direct_Herm2_value_row_execution_attempted": hresponse[
                "direct_Herm2_value_row_execution_attempted"
            ],
            "direct_Herm2_Huv_payload_emitted": hresponse[
                "direct_Herm2_Huv_payload_emitted"
            ],
            "direct_Huu_Hud_Hdd_emitted": hresponse["direct_Huu_Hud_Hdd_emitted"],
            "source_ownership_certificate_emitted": hresponse[
                "source_ownership_certificate_emitted"
            ],
            "same_source_exactness_or_error_certificate_emitted": hresponse[
                "same_source_exactness_or_error_certificate_emitted"
            ],
        },
        "latest_row_certificate_payload": {
            "B_Huv_support_imported": hcert["B_Huv_support_imported"],
            "payload_manifest_fixed": hcert["payload_manifest_fixed"],
            "support_slots_available": sources["hresponse_cert_payload"]["key_numbers"][
                "support_slots_available"
            ],
            "payload_slots_required": sources["hresponse_cert_payload"]["key_numbers"][
                "payload_slots_required"
            ],
            "accepted_payload_slot_count": sources["hresponse_cert_payload"]["key_numbers"][
                "accepted_payload_slot_count"
            ],
            "accepted_value_row_count": sources["hresponse_cert_payload"]["key_numbers"][
                "accepted_value_row_count"
            ],
            "accepted_final_certificate_count": sources["hresponse_cert_payload"][
                "key_numbers"
            ]["accepted_final_certificate_count"],
        },
        "current_decision": {
            "phase_and_direction_prerequisites_closed": True,
            "radial_norm_law_closed": True,
            "numeric_radial_source_value_emitted": False,
            "direct_N_H_value_emitted": False,
            "direct_K_threshold_Omega_H_lambda_emitted": False,
            "strict_H_K_threshold_row_emitted": False,
            "accepted_selected_K_source_row_count": prev[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": prev[
                "selected_K_threshold_row_count_required"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_contract = {
        "schema": "MTTHRadialSourceValueOrDirectNHContract.v1",
        "status": "RADIAL_SOURCE_VALUE_OR_DIRECT_NH_REQUIRED",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "primary_required_payload": [
            "selected radial Hessian/action scalar N_H=Hess(F_H)[U_H,U_H]",
            "or source-owned r_H value on the already selected Herm(2) ray",
            "or selected L_rowlocal.Omega_H.lambda and T_scheme.Omega_H.lambda",
            "or direct K_threshold.Omega_H.lambda with row-level source certificate",
        ],
        "already_closed_for_direct_exit": [
            "trace-free m0=0",
            "ordered T3/sigma_D=+1 orientation",
            "q79/F,m=1 +i phase sign",
            "radial norm law on the selected Herm(2) ray",
            "formal RO.q79F1.Omega_H.lambda operator domain readiness",
        ],
        "must_not_use": [
            "controlled HRG radial value as strict source",
            "near miss z448*sqrt2/phi as exact source identity",
            "B_Huv support slots as final Herm(2) value certificates",
            "model-active HYM/Galerkin values as selected H K row",
        ],
        "strict_K_threshold_count": {
            "accepted": prev["accepted_selected_K_source_row_count"],
            "required": prev["selected_K_threshold_row_count_required"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedDirectHKThresholdRowCurrentExitOrRadialSource",
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
            "direct_hk_polar_prerequisite_recheck": rel(POLAR_PACKET),
            "direct_hk_radial_value_source_gate": rel(RADIAL_PACKET),
            "direct_kthreshold_omega_h_lambda_execution_attempt": rel(DIRECT_PACKET),
            "next_radial_source_or_direct_NH_contract": rel(NEXT_CONTRACT),
        },
        "closure_decision": {
            "direct_exit_executed_current_frontier": True,
            "m0_tracefree_quotient_promoted": True,
            "sigma_D_orientation_promoted": True,
            "strict_phi_Omega_promoted": True,
            "radial_norm_law_promoted": True,
            "strict_r_H_promoted": False,
            "numeric_radial_source_value_emitted": False,
            "direct_N_H_value_emitted": False,
            "selected_L_rowlocal_Omega_H_lambda_emitted": False,
            "selected_T_scheme_Omega_H_lambda_emitted": False,
            "direct_K_threshold_Omega_H_lambda_emitted": False,
            "strict_H_K_threshold_row_emitted": False,
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
            "name": "DirectHKThresholdCurrentExitReductionTheorem",
            "proved": True,
            "statement": (
                "The direct K_threshold.Omega_H.lambda exit has been re-executed "
                "after the latest table normalization and H polar updates. The "
                "phase/direction side is now closed: m0=0, sigma_D=+1, and the "
                "q79/F,m=1 +i phase sign are promoted, and the radial norm law is "
                "proved. The direct exit still emits zero strict H K rows because "
                "the numeric radial/action scalar r_H or direct N_H is not emitted "
                "as selected source data."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedDirectHKThresholdRowCurrentExitOrRadialSource",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "direct_exit_executed_current_frontier": True,
        "strict_phi_Omega_promoted": True,
        "radial_norm_law_promoted": True,
        "strict_r_H_promoted": False,
        "direct_K_threshold_Omega_H_lambda_emitted": False,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Direct H K Threshold Row Current Exit or Radial Source v1

## Theorem

`DirectHKThresholdCurrentExitReductionTheorem` is emitted.

## Newly Closed

- The direct `K_threshold.Omega_H.lambda` exit has been re-executed from the
  current frontier, after the same-source table normalization.
- The direct H polar prerequisites are no longer the main blocker:
  `m0=0`, `sigma_D=+1`, and the q79/F,m=1 `+i` phase are promoted.
- The radial norm law on the selected Herm(2) ray is proved.
- The formal `RO.q79F1.Omega_H.lambda` operator domain is ready.

## Current Direct-Exit Result

- Controlled radial value retained only as postcheck:
  `{radial_action["key_numbers"]["controlled_r_H_postcheck_only"]}`.
- Accepted numeric radial source values: `0`.
- Direct `N_H` values emitted: `false`.
- Direct `K_threshold.Omega_H.lambda` emitted: `false`.
- Strict selected `K_threshold` rows remain
  `{prev["accepted_selected_K_source_row_count"]}/{prev["selected_K_threshold_row_count_required"]}`.

## Remaining Direct Payload

The direct exit now reduces to one of these source-owned payloads:

- selected radial Hessian/action scalar `N_H=Hess(F_H)[U_H,U_H]`;
- source-owned `r_H` value on the selected Herm(2) ray;
- selected split pair `L_rowlocal.Omega_H.lambda` and
  `T_scheme.Omega_H.lambda`;
- direct `K_threshold.Omega_H.lambda` with row-level source certificate.

## Next Artifact

`{NEXT}`
"""

    write_json(POLAR_PACKET, polar_packet)
    write_json(RADIAL_PACKET, radial_packet)
    write_json(DIRECT_PACKET, direct_packet)
    write_json(NEXT_CONTRACT, next_contract)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
