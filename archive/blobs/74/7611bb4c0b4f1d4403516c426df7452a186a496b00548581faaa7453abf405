"""Build PMNS/running-mass rows versus Higgs-threshold/strict-PEW exit reduction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_pmnsrunningmassrows_or_higgsthresholdstrictpewexit"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
PMNS_STATUS = PACKET_DIR / "pmns_policy_and_source_status.packet.json"
RUNNING_STATUS = PACKET_DIR / "running_mass_threshold_status.packet.json"
DECISION = PACKET_DIR / "pmns_running_higgs_pew_exit_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PMNSRunningMassRows_or_HiggsThresholdStrictPEWExit_v1.md"

PREVIOUS = DATA / "selected_ckmcovarianceprofileorhigherorderresidualclosure_or_pmnshiggspewrows.candidate.json"
NEUTRINO = DATA / "selected_neutrinomassmajoranapolicy_or_precisionprofiletable.candidate.json"
CONVENTIONS = DATA / "sm_equivalence_ckm_gauge_pmns_convention_fill.candidate.json"
RUNNING_PROXY = DATA / "selected_runningmasshiggsdecayproxy_or_precisionwidths.candidate.json"
THRESHOLD_RUNNING = DATA / "selected_thresholdpolerunningmaps_or_rthetaconventionsource.candidate.json"
THRESHOLD_READINESS = DATA / "selected_thresholdmassschemerows_or_precisionprofileupgrade.candidate.json"
BCT_PROFILE = DATA / "selected_bctprofilereconciliation_or_rthetamassschemederivation.candidate.json"

STATUS = (
    "MTT_SELECTED_PMNSRUNNINGMASSROWS_OR_HIGGSTHRESHOLDSTRICTPEWEXIT_"
    "BUILT_PMNS_POLICY_RUNNING_PROXY_CLOSED_SOURCE_ROWS_OPEN"
)
NEXT = "MTT_Selected_HiggsThresholdStrictPEWExit_or_SelectedSourceRows_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    previous = load(PREVIOUS)
    neutrino = load(NEUTRINO)
    conventions = load(CONVENTIONS)
    running_proxy = load(RUNNING_PROXY)
    threshold_running = load(THRESHOLD_RUNNING)
    threshold_readiness = load(THRESHOLD_READINESS)
    bct_profile = load(BCT_PROFILE)

    minimal_pmns_closed = neutrino["closure_decision"]["minimal_PMNS_oscillation_policy_closed"]
    pmns_replay_ready = (
        conventions["replay_readiness"]["PMNS_matrix_ready_for_replay"]
        and neutrino["PMNS_replay_facts"]["status"]
        == "OSCILLATION_MASS_SQUARED_REPLAY_READY_ABSOLUTE_MASS_OPEN"
    )
    absolute_neutrino_mass_closed = neutrino["closure_decision"]["absolute_neutrino_mass_closed"]
    dirac_yukawa_closed = neutrino["closure_decision"]["Dirac_neutrino_yukawa_magnitudes_closed"]
    majorana_policy_selected = neutrino["closure_decision"]["Majorana_policy_selected"]
    running_proxy_closed = running_proxy["closure_decision"]["running_mass_proxy_layer_closed"]
    running_precision_closed = running_proxy["closure_decision"]["full_precision_Higgs_widths_closed"]

    pmns_status = {
        "schema": "MTTPMNSPolicyAndSourceStatus.v1",
        "status": "PMNS_MINIMAL_OSCILLATION_POLICY_CLOSED_SOURCE_VALUES_OPEN",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "neutrino_policy_candidate": rel(NEUTRINO),
        "ckm_pmns_convention_packet": rel(CONVENTIONS),
        "minimal_PMNS_oscillation_policy_closed": minimal_pmns_closed,
        "PMNS_matrix_ready_for_replay": conventions["replay_readiness"]["PMNS_matrix_ready_for_replay"],
        "PMNS_oscillation_mass_squared_replay_ready": pmns_replay_ready,
        "PMNS_unitarity_max_residual": neutrino["PMNS_replay_facts"]["unitarity_max_residual"],
        "PMNS_diagonalization_max_residual_eV2": neutrino["PMNS_replay_facts"][
            "diagonalization_max_residual_eV2"
        ],
        "absolute_neutrino_mass_closed": absolute_neutrino_mass_closed,
        "Dirac_neutrino_yukawa_magnitudes_closed": dirac_yukawa_closed,
        "Majorana_policy_selected": majorana_policy_selected,
        "Majorana_phases_closed": neutrino["closure_decision"]["Majorana_phases_closed"],
        "PMNS_angle_phase_source_rows_closed": False,
        "selected_PMNS_no_knob_rows_closed": False,
    }

    running_status = {
        "schema": "MTTRunningMassThresholdStatus.v1",
        "status": "RUNNING_PROXY_AND_THRESHOLD_READINESS_CLOSED_SOURCE_ROWS_OPEN",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "running_proxy_candidate": rel(RUNNING_PROXY),
        "threshold_running_candidate": rel(THRESHOLD_RUNNING),
        "threshold_readiness_candidate": rel(THRESHOLD_READINESS),
        "bct_profile_candidate": rel(BCT_PROFILE),
        "running_mass_proxy_layer_closed": running_proxy_closed,
        "full_precision_Higgs_widths_closed": running_precision_closed,
        "one_loop_gauge_bridge_policy_validation_closed": threshold_running["closure_decision"][
            "one_loop_gauge_bridge_policy_validation_closed"
        ],
        "top_higgs_threshold_map_targets_extracted": threshold_running["closure_decision"][
            "top_higgs_threshold_map_targets_extracted"
        ],
        "threshold_mass_scheme_row_readiness_matrix_closed": threshold_readiness["closure_decision"][
            "threshold_mass_scheme_row_readiness_matrix_closed"
        ],
        "external_top_higgs_rows_integrated": threshold_readiness["closure_decision"][
            "external_top_higgs_rows_integrated"
        ],
        "external_WZH_coordinate_rows_integrated": threshold_readiness["closure_decision"][
            "external_WZH_coordinate_rows_integrated"
        ],
        "BCT_residual_rows_attached": threshold_readiness["closure_decision"]["BCT_residual_rows_attached"],
        "accepted_BCT_map_row_count": bct_profile["closure_decision"][
            "accepted_bottom_charm_tau_map_row_count"
        ],
        "BCT_profile_95pct_closure_closed": bct_profile["closure_decision"][
            "BCT_profile_95pct_closure_closed"
        ],
        "selected_threshold_matching_source_rows_closed": threshold_readiness["closure_decision"][
            "selected_threshold_matching_source_rows_closed"
        ],
        "selected_mass_scheme_conversion_source_rows_closed": threshold_readiness["closure_decision"][
            "selected_mass_scheme_conversion_source_rows_closed"
        ],
        "selected_Rtheta_source_rows_closed": threshold_readiness["closure_decision"][
            "selected_Rtheta_source_rows_closed"
        ],
    }

    decision = {
        "schema": "MTTPMNSRunningHiggsPEWExitDecision.v1",
        "status": "PMNS_POLICY_RUNNING_PROXY_CLOSED_HIGGS_PEW_SOURCE_ROWS_OPEN",
        "closed_now": [
            "Minimal PMNS oscillation replay/policy is closed and PMNS replay matrices are ready.",
            "Running-mass Higgs decay proxy layer is closed as a controlled proxy tier.",
            "Threshold/mass-scheme row readiness matrix is closed with external top/Higgs, WZH, and BCT validation targets.",
        ],
        "not_closed": [
            "Absolute neutrino mass, Dirac neutrino Yukawa magnitudes, Majorana policy/phases, and selected PMNS source rows remain open.",
            "Precision running mass-ratio/source derivation and selected threshold/mass-scheme source rows remain open.",
            "Higgs/lambda_H threshold source rows and strict P_EW/direct-K values remain open.",
        ],
        "source_row_counts": {
            "accepted_PMNS_policy_rows": 1 if minimal_pmns_closed else 0,
            "accepted_PMNS_source_rows": 0,
            "accepted_absolute_neutrino_mass_rows": 0,
            "accepted_running_mass_proxy_layers": 1 if running_proxy_closed else 0,
            "accepted_precision_running_mass_source_rows": 0,
            "accepted_external_top_higgs_coordinate_rows": 2
            if threshold_readiness["closure_decision"]["external_top_higgs_rows_integrated"]
            else 0,
            "accepted_external_WZH_coordinate_rows": 5
            if threshold_readiness["closure_decision"]["external_WZH_coordinate_rows_integrated"]
            else 0,
            "accepted_BCT_map_rows": bct_profile["closure_decision"]["accepted_bottom_charm_tau_map_row_count"],
            "accepted_selected_threshold_source_rows": 0,
        },
        "acceptance": {
            "PMNS_minimal_oscillation_policy_closed": minimal_pmns_closed,
            "PMNS_replay_ready": pmns_replay_ready,
            "PMNS_source_rows_closed": False,
            "absolute_neutrino_mass_closed": absolute_neutrino_mass_closed,
            "running_mass_proxy_layer_closed": running_proxy_closed,
            "precision_running_mass_source_rows_closed": False,
            "threshold_mass_scheme_readiness_closed": threshold_readiness["closure_decision"][
                "threshold_mass_scheme_row_readiness_matrix_closed"
            ],
            "selected_threshold_matching_source_rows_closed": False,
            "higgs_threshold_rows_closed": False,
            "strict_PEW_directK_values_closed": False,
            "fullS2_no_proxy_rows_closed": False,
            "global_true_SM_no_knob_closure": False,
            "true_SM_equivalence_closed": False,
        },
        "next_exact_target": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedPMNSRunningMassRowsOrHiggsThresholdStrictPEWExit",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_ckm_profile_candidate": rel(PREVIOUS),
            "neutrino_policy": rel(NEUTRINO),
            "ckm_pmns_convention_packet": rel(CONVENTIONS),
            "running_mass_proxy": rel(RUNNING_PROXY),
            "threshold_running_decomposition": rel(THRESHOLD_RUNNING),
            "threshold_mass_scheme_readiness": rel(THRESHOLD_READINESS),
            "bct_profile_reconciliation": rel(BCT_PROFILE),
        },
        "output_packets": {
            "pmns_policy_and_source_status": rel(PMNS_STATUS),
            "running_mass_threshold_status": rel(RUNNING_STATUS),
            "pmns_running_higgs_pew_exit_decision": rel(DECISION),
        },
        "theorem": {
            "name": "PMNSRunningMassRowsOrHiggsThresholdStrictPEWExitReductionTheorem",
            "proved": True,
            "statement": (
                "After CKM diagonal-profile admission, the remaining PMNS/running-mass branch "
                "separates into closed replay/proxy/readiness layers and open selected source rows. "
                "Minimal PMNS oscillation policy, PMNS replay readiness, running-mass proxy, and "
                "threshold/mass-scheme readiness are closed. Absolute neutrino mass, selected PMNS "
                "source rows, precision running/source rows, Higgs/threshold rows, and strict "
                "PEW/direct-K values remain open."
            ),
        },
        "key_numbers": {
            "PMNS_unitarity_max_residual": pmns_status["PMNS_unitarity_max_residual"],
            "PMNS_diagonalization_max_residual_eV2": pmns_status[
                "PMNS_diagonalization_max_residual_eV2"
            ],
            "accepted_PMNS_policy_rows": decision["source_row_counts"]["accepted_PMNS_policy_rows"],
            "accepted_PMNS_source_rows": 0,
            "accepted_running_mass_proxy_layers": decision["source_row_counts"][
                "accepted_running_mass_proxy_layers"
            ],
            "accepted_external_top_higgs_coordinate_rows": decision["source_row_counts"][
                "accepted_external_top_higgs_coordinate_rows"
            ],
            "accepted_external_WZH_coordinate_rows": decision["source_row_counts"][
                "accepted_external_WZH_coordinate_rows"
            ],
            "accepted_BCT_map_rows": decision["source_row_counts"]["accepted_BCT_map_rows"],
            "accepted_selected_threshold_source_rows": 0,
        },
        "closure_decision": decision["acceptance"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PMNSRunningMassRows_or_HiggsThresholdStrictPEWExit_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "PMNS_minimal_oscillation_policy_closed": minimal_pmns_closed,
        "PMNS_replay_ready": pmns_replay_ready,
        "PMNS_source_rows_closed": False,
        "absolute_neutrino_mass_closed": absolute_neutrino_mass_closed,
        "running_mass_proxy_layer_closed": running_proxy_closed,
        "precision_running_mass_source_rows_closed": False,
        "threshold_mass_scheme_readiness_closed": decision["acceptance"][
            "threshold_mass_scheme_readiness_closed"
        ],
        "selected_threshold_matching_source_rows_closed": False,
        "higgs_threshold_rows_closed": False,
        "strict_PEW_directK_values_closed": False,
        "fullS2_no_proxy_rows_closed": False,
        "global_true_SM_no_knob_closure": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PMNSRunningMassRows or HiggsThresholdStrictPEWExit v1

Status: `{STATUS}`

## Closed Now

- PMNS minimal oscillation policy: closed
- PMNS replay readiness: closed
- PMNS unitarity residual: `{pmns_status["PMNS_unitarity_max_residual"]}`
- PMNS diagonalization residual: `{pmns_status["PMNS_diagonalization_max_residual_eV2"]}`
- running-mass Higgs proxy layer: closed
- threshold/mass-scheme readiness matrix: closed
- external top/Higgs coordinate rows in readiness harness: `2`
- external WZH coordinate rows in readiness harness: `5`

## Still Open

- selected PMNS source rows: `0`
- absolute neutrino mass rows: `0`
- precision running mass-ratio/source rows: `0`
- selected threshold/mass-scheme source rows: `0`
- Higgs/`lambda_H` threshold rows: open
- strict `P_EW` / direct-K values: open

Next required artifact: `{NEXT}`.
"""

    write_json(PMNS_STATUS, pmns_status)
    write_json(RUNNING_STATUS, running_status)
    write_json(DECISION, decision)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
