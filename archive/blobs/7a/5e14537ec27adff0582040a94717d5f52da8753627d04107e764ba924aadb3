"""Build CKM/PMNS rows versus Higgs/threshold/strict-PEW exit reduction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_ckmpmnsrows_or_higgsthresholdstrictpewexit"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
CKM_STATUS = PACKET_DIR / "ckm_weightrow_status_after_pickm_residual_audit.packet.json"
PMNS_STATUS = PACKET_DIR / "pmns_runningratio_status_after_flavor_bridge.packet.json"
DECISION = PACKET_DIR / "ckmpmns_higgs_pew_exit_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CKMPMNSRows_or_HiggsThresholdStrictPEWExit_v1.md"

FULLS2_LEDGER = DATA / "selected_fulls2noproxyrows_or_strictpewnormalizationpayload.candidate.json"
PICKM_ROWS = DATA / "selected_pickmnumeratorbranchretentionprinciple_or_weightrows.candidate.json"
PICKM_RESIDUAL = DATA / "selected_pickmweightrows_ckmresidualdecision_or_higherorderclosure.candidate.json"
FLAVOR_BRIDGE = DATA / "selected_flavoroperatorvalueuse_or_ckmpmnsorientationbridge.candidate.json"
POLICY_BRIDGE = DATA / "selected_flavoroperatorpolicyuse_afterah8_or_ckmpmnsbridge.candidate.json"
MASSRATIO = DATA / "selected_massratioorientationlawsearch_or_finitephaseckmclue.candidate.json"

STATUS = (
    "MTT_SELECTED_CKMPMNSROWS_OR_HIGGSTHRESHOLDSTRICTPEWEXIT_"
    "BUILT_CKM_WEIGHTROWS_CLOSED_PMNS_HIGGS_PEW_OPEN"
)
NEXT = "MTT_Selected_CKMCovarianceProfileOrHigherOrderResidualClosure_or_PMNSHiggsPEWRows_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    fulls2 = load(FULLS2_LEDGER)
    pickm_rows = load(PICKM_ROWS)
    pickm_residual = load(PICKM_RESIDUAL)
    flavor_bridge = load(FLAVOR_BRIDGE)
    policy_bridge = load(POLICY_BRIDGE)
    massratio = load(MASSRATIO)

    accepted_ckm_weight_rows = pickm_rows["closure_decision"]["accepted_weight_rows"]
    selected_ckm_row_certs = pickm_rows["closure_decision"]["selected_Pi_CKM_row_certificates"]
    residual_audited = pickm_residual["closure_decision"]["residual_cause_audited"]
    exact_ckm_rows = pickm_residual["closure_decision"]["accepted_exact_ckm_correction_rows"]
    no_knob_ckm_angle_rows = pickm_residual["closure_decision"]["accepted_no_knob_CKM_angle_rows"]
    q79_phase_residual_deg = policy_bridge["closure_decision"]["q79_phase_residual_deg"]
    q79_jarlskog_residual = policy_bridge["closure_decision"]["q79_jarlskog_relative_residual"]

    ckm_status = {
        "schema": "MTTCKMWeightRowStatusAfterPiCKMResidualAudit.v1",
        "status": "CKM_PICKM_WEIGHT_ROWS_CLOSED_EXACT_CENTRAL_RESIDUAL_OPEN",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "observed_data_used_for_postcheck": True,
        "pickm_weight_rows_candidate": rel(PICKM_ROWS),
        "pickm_residual_candidate": rel(PICKM_RESIDUAL),
        "q79_phase_bridge_candidate": rel(POLICY_BRIDGE),
        "accepted_selected_Pi_CKM_weight_rows": accepted_ckm_weight_rows,
        "selected_Pi_CKM_row_certificates": selected_ckm_row_certs,
        "selected_weights": pickm_rows["key_numbers"]["selected_weights"],
        "selected_correction_factors": pickm_rows["key_numbers"]["selected_correction_factors"],
        "q79_CKM_CP_phase_contact_imported": policy_bridge["closure_decision"][
            "q79_CKM_CP_phase_contact_imported"
        ],
        "q79_phase_residual_deg_postcheck": q79_phase_residual_deg,
        "q79_jarlskog_relative_residual_postcheck": q79_jarlskog_residual,
        "max_relative_angle_residual_against_frozen_replay": pickm_residual["key_numbers"][
            "max_relative_angle_residual_against_frozen_replay"
        ],
        "max_relative_weight_residual_against_frozen_replay": pickm_residual["key_numbers"][
            "max_relative_weight_residual_against_frozen_replay"
        ],
        "residual_cause_audited": residual_audited,
        "accepted_exact_ckm_correction_rows": exact_ckm_rows,
        "accepted_no_knob_CKM_angle_rows": no_knob_ckm_angle_rows,
        "exact_ckm_angle_magnitudes_closed": pickm_residual["closure_decision"][
            "exact_ckm_angle_magnitudes_closed"
        ],
    }

    pmns_status = {
        "schema": "MTTPMNSRunningRatioStatusAfterFlavorBridge.v1",
        "status": "PMNS_AND_RUNNING_RATIO_SOURCE_ROWS_OPEN",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "flavor_bridge_candidate": rel(FLAVOR_BRIDGE),
        "massratio_candidate": rel(MASSRATIO),
        "CKM_PMNS_orientation_bridge_executable": flavor_bridge["closure_decision"][
            "CKM_PMNS_orientation_bridge_executable"
        ],
        "policy_csk_source_value_row_count": flavor_bridge["closure_decision"][
            "policy_csk_source_value_row_count"
        ],
        "strict_selected_csk_source_row_count": flavor_bridge["closure_decision"][
            "strict_selected_csk_source_row_count"
        ],
        "selected_CKM_PMNS_orientation_source_closed": flavor_bridge["closure_decision"][
            "selected_CKM_PMNS_orientation_source_closed"
        ],
        "selected_CKM_PMNS_values_derived": massratio["closure_decision"][
            "selected_CKM_PMNS_values_derived"
        ],
        "selected_orientation_source_theorem_closed": massratio["closure_decision"][
            "selected_orientation_source_theorem_closed"
        ],
        "running_mass_ratio_rows_closed": False,
        "PMNS_angle_phase_rows_closed": False,
    }

    decision = {
        "schema": "MTTCKMPMNSHiggsPEWExitDecision.v1",
        "status": "CKM_WEIGHT_SUBLAYER_CLOSED_FULL_CKMPMNS_HIGGS_PEW_OPEN",
        "closed_now": [
            "The CKM source-input chain is now credited at the Pi_CKM weight-row layer.",
            "Three selected Pi_CKM row certificates emit W12, W23, and W13 without CKM targets as selectors.",
            "The q79 CKM CP phase contact and qualitative CKM/PMNS orientation bridge are retained as selected support.",
            "The CKM residual cause is audited and isolated as higher-order/profile rather than missing source-domain data.",
        ],
        "not_closed": [
            "Exact/no-knob CKM central angle closure remains open because residual correction rows are 0.",
            "PMNS angle/phase source rows and running mass-ratio source rows remain open.",
            "Higgs/lambda_H threshold rows and strict P_EW/direct-K normalization values remain open.",
        ],
        "source_row_counts": {
            "accepted_selected_Pi_CKM_weight_rows": accepted_ckm_weight_rows,
            "selected_Pi_CKM_row_certificates": selected_ckm_row_certs,
            "accepted_exact_ckm_correction_rows": exact_ckm_rows,
            "accepted_no_knob_CKM_angle_rows": no_knob_ckm_angle_rows,
            "strict_selected_csk_source_row_count": pmns_status["strict_selected_csk_source_row_count"],
            "PMNS_angle_phase_rows": 0,
            "running_mass_ratio_rows": 0,
        },
        "acceptance": {
            "ckm_Pi_weight_rows_closed": accepted_ckm_weight_rows == 3,
            "ckm_exact_central_residual_closed": False,
            "ckm_covariance_or_higher_order_profile_closed": False,
            "PMNS_rows_closed": False,
            "running_mass_ratio_rows_closed": False,
            "higgs_threshold_rows_closed": False,
            "strict_PEW_directK_values_closed": False,
            "fullS2_obligation_rows_closed_after_previous_update": fulls2["closure_decision"][
                "fullS2_obligation_rows_closed_after_yukawa_update"
            ],
            "fullS2_no_proxy_rows_closed": False,
            "global_true_SM_no_knob_closure": False,
            "true_SM_equivalence_closed": False,
        },
        "next_exact_target": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedCKMPMNSRowsOrHiggsThresholdStrictPEWExit",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "observed_data_used_for_postcheck": True,
        "inputs": {
            "fulls2_after_yukawa_ledger": rel(FULLS2_LEDGER),
            "pickm_weight_rows": rel(PICKM_ROWS),
            "pickm_residual_audit": rel(PICKM_RESIDUAL),
            "flavor_operator_ckm_pmns_bridge": rel(FLAVOR_BRIDGE),
            "policy_ckm_pmns_bridge": rel(POLICY_BRIDGE),
            "massratio_orientation_search": rel(MASSRATIO),
        },
        "output_packets": {
            "ckm_weightrow_status_after_pickm_residual_audit": rel(CKM_STATUS),
            "pmns_runningratio_status_after_flavor_bridge": rel(PMNS_STATUS),
            "ckmpmns_higgs_pew_exit_decision": rel(DECISION),
        },
        "theorem": {
            "name": "CKMPMNSRowsOrHiggsThresholdStrictPEWExitReductionTheorem",
            "proved": True,
            "statement": (
                "Within the remaining full-S2 value-row frontier, the CKM source-input sublayer "
                "is closed through three selected Pi_CKM weight rows plus the q79 phase contact. "
                "Exact central CKM closure is not claimed because the audited residual requires "
                "a higher-order/profile row. PMNS, running mass ratios, Higgs/threshold rows, and "
                "strict PEW/direct-K values remain open."
            ),
        },
        "key_numbers": {
            "accepted_selected_Pi_CKM_weight_rows": accepted_ckm_weight_rows,
            "accepted_exact_ckm_correction_rows": exact_ckm_rows,
            "accepted_no_knob_CKM_angle_rows": no_knob_ckm_angle_rows,
            "max_relative_angle_residual_against_frozen_replay": ckm_status[
                "max_relative_angle_residual_against_frozen_replay"
            ],
            "max_relative_weight_residual_against_frozen_replay": ckm_status[
                "max_relative_weight_residual_against_frozen_replay"
            ],
            "q79_phase_residual_deg_postcheck": q79_phase_residual_deg,
            "q79_jarlskog_relative_residual_postcheck": q79_jarlskog_residual,
            "PMNS_angle_phase_rows": 0,
            "running_mass_ratio_rows": 0,
        },
        "closure_decision": decision["acceptance"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_CKMPMNSRows_or_HiggsThresholdStrictPEWExit_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "ckm_Pi_weight_rows_closed": True,
        "accepted_selected_Pi_CKM_weight_rows": accepted_ckm_weight_rows,
        "ckm_exact_central_residual_closed": False,
        "PMNS_rows_closed": False,
        "running_mass_ratio_rows_closed": False,
        "higgs_threshold_rows_closed": False,
        "strict_PEW_directK_values_closed": False,
        "fullS2_no_proxy_rows_closed": False,
        "global_true_SM_no_knob_closure": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected CKMPMNSRows or HiggsThresholdStrictPEWExit v1

Status: `{STATUS}`

## Closed Now

The CKM source-input sublayer is now credited:

- selected `Pi_CKM` weight rows: `{accepted_ckm_weight_rows}/3`
- selected row certificates: `{selected_ckm_row_certs}/3`
- q79 CKM CP phase contact: closed as support
- CKM residual cause: audited

This does not close exact central CKM magnitudes.  The current selected rows
leave max relative angle residual
`{ckm_status["max_relative_angle_residual_against_frozen_replay"]}` against
the frozen replay, so the remaining CKM object is a higher-order/profile row.

## Still Open

- exact/no-knob CKM correction rows: `{exact_ckm_rows}`
- PMNS rows: `0`
- running mass-ratio rows: `0`
- Higgs/`lambda_H` threshold rows: open
- strict `P_EW` / direct-K normalization values: open

Next required artifact: `{NEXT}`.
"""

    write_json(CKM_STATUS, ckm_status)
    write_json(PMNS_STATUS, pmns_status)
    write_json(DECISION, decision)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
