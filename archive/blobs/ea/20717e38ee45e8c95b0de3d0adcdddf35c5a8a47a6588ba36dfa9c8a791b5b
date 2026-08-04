"""Audit PMNS/running-mass rows versus Higgs-threshold/strict-PEW exit reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_pmnsrunningmassrows_or_higgsthresholdstrictpewexit"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PMNS_STATUS = PACKET_DIR / "pmns_policy_and_source_status.packet.json"
RUNNING_STATUS = PACKET_DIR / "running_mass_threshold_status.packet.json"
DECISION = PACKET_DIR / "pmns_running_higgs_pew_exit_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PMNSRunningMassRows_or_HiggsThresholdStrictPEWExit_v1.md"

STATUS = (
    "MTT_SELECTED_PMNSRUNNINGMASSROWS_OR_HIGGSTHRESHOLDSTRICTPEWEXIT_"
    "BUILT_PMNS_POLICY_RUNNING_PROXY_CLOSED_SOURCE_ROWS_OPEN"
)
NEXT = "MTT_Selected_HiggsThresholdStrictPEWExit_or_SelectedSourceRows_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    pmns = load(PMNS_STATUS)
    running = load(RUNNING_STATUS)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["closure_claimed"] is False, "candidate overclosed")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["target_fitting_used"] is False, "candidate target fitting")

    require(pmns["status"] == "PMNS_MINIMAL_OSCILLATION_POLICY_CLOSED_SOURCE_VALUES_OPEN", "PMNS status")
    require(pmns["observed_data_used_as_selector"] is False, "PMNS observed selector")
    require(pmns["target_fitting_used"] is False, "PMNS target fitting")
    require(pmns["minimal_PMNS_oscillation_policy_closed"] is True, "PMNS policy")
    require(pmns["PMNS_matrix_ready_for_replay"] is True, "PMNS replay")
    require(pmns["PMNS_oscillation_mass_squared_replay_ready"] is True, "PMNS mass replay")
    require(pmns["PMNS_unitarity_max_residual"] < 1e-12, "PMNS unitarity")
    require(pmns["PMNS_diagonalization_max_residual_eV2"] < 1e-15, "PMNS diagonalization")
    require(pmns["absolute_neutrino_mass_closed"] is False, "absolute mass overclosed")
    require(pmns["Dirac_neutrino_yukawa_magnitudes_closed"] is False, "Dirac overclosed")
    require(pmns["Majorana_policy_selected"] is False, "Majorana overclosed")
    require(pmns["Majorana_phases_closed"] is False, "Majorana phases overclosed")
    require(pmns["PMNS_angle_phase_source_rows_closed"] is False, "PMNS source overclosed")
    require(pmns["selected_PMNS_no_knob_rows_closed"] is False, "PMNS no-knob overclosed")

    require(
        running["status"] == "RUNNING_PROXY_AND_THRESHOLD_READINESS_CLOSED_SOURCE_ROWS_OPEN",
        "running status",
    )
    require(running["observed_data_used_as_selector"] is False, "running observed selector")
    require(running["target_fitting_used"] is False, "running target fitting")
    require(running["running_mass_proxy_layer_closed"] is True, "running proxy")
    require(running["full_precision_Higgs_widths_closed"] is False, "precision widths overclosed")
    require(running["one_loop_gauge_bridge_policy_validation_closed"] is True, "gauge bridge")
    require(running["top_higgs_threshold_map_targets_extracted"] is True, "top/Higgs targets")
    require(running["threshold_mass_scheme_row_readiness_matrix_closed"] is True, "readiness")
    require(running["external_top_higgs_rows_integrated"] is True, "top/Higgs external")
    require(running["external_WZH_coordinate_rows_integrated"] is True, "WZH external")
    require(running["BCT_residual_rows_attached"] is True, "BCT residuals")
    require(running["accepted_BCT_map_row_count"] == 3, "BCT accepted row count")
    require(running["BCT_profile_95pct_closure_closed"] is False, "BCT profile overclosed")
    require(running["selected_threshold_matching_source_rows_closed"] is False, "threshold source")
    require(running["selected_mass_scheme_conversion_source_rows_closed"] is False, "mass scheme source")
    require(running["selected_Rtheta_source_rows_closed"] is False, "Rtheta source")

    require(
        decision["status"] == "PMNS_POLICY_RUNNING_PROXY_CLOSED_HIGGS_PEW_SOURCE_ROWS_OPEN",
        "decision status",
    )
    require(len(decision["closed_now"]) == 3, "closed count")
    require(len(decision["not_closed"]) == 3, "not closed count")
    counts = decision["source_row_counts"]
    require(counts["accepted_PMNS_policy_rows"] == 1, "PMNS policy count")
    require(counts["accepted_PMNS_source_rows"] == 0, "PMNS source count")
    require(counts["accepted_absolute_neutrino_mass_rows"] == 0, "absolute mass count")
    require(counts["accepted_running_mass_proxy_layers"] == 1, "running proxy count")
    require(counts["accepted_precision_running_mass_source_rows"] == 0, "running source count")
    require(counts["accepted_external_top_higgs_coordinate_rows"] == 2, "top/Higgs count")
    require(counts["accepted_external_WZH_coordinate_rows"] == 5, "WZH count")
    require(counts["accepted_BCT_map_rows"] == 3, "BCT count")
    require(counts["accepted_selected_threshold_source_rows"] == 0, "threshold source count")
    acceptance = decision["acceptance"]
    require(acceptance["PMNS_minimal_oscillation_policy_closed"] is True, "accept PMNS policy")
    require(acceptance["PMNS_replay_ready"] is True, "accept PMNS replay")
    require(acceptance["PMNS_source_rows_closed"] is False, "accept PMNS source")
    require(acceptance["absolute_neutrino_mass_closed"] is False, "accept absolute")
    require(acceptance["running_mass_proxy_layer_closed"] is True, "accept running proxy")
    require(acceptance["precision_running_mass_source_rows_closed"] is False, "accept running source")
    require(acceptance["threshold_mass_scheme_readiness_closed"] is True, "accept readiness")
    require(acceptance["selected_threshold_matching_source_rows_closed"] is False, "accept threshold")
    require(acceptance["higgs_threshold_rows_closed"] is False, "Higgs overclosed")
    require(acceptance["strict_PEW_directK_values_closed"] is False, "PEW overclosed")
    require(acceptance["fullS2_no_proxy_rows_closed"] is False, "fullS2 overclosed")
    require(acceptance["global_true_SM_no_knob_closure"] is False, "global overclosed")
    require(acceptance["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["next_exact_target"] == NEXT, "decision next")

    require(
        data["theorem"]["name"] == "PMNSRunningMassRowsOrHiggsThresholdStrictPEWExitReductionTheorem",
        "theorem",
    )
    require(data["theorem"]["proved"] is True, "theorem proved")
    key = data["key_numbers"]
    require(key["accepted_PMNS_policy_rows"] == 1, "key PMNS")
    require(key["accepted_PMNS_source_rows"] == 0, "key PMNS source")
    require(key["accepted_running_mass_proxy_layers"] == 1, "key running")
    require(key["accepted_external_top_higgs_coordinate_rows"] == 2, "key top/Higgs")
    require(key["accepted_external_WZH_coordinate_rows"] == 5, "key WZH")
    require(key["accepted_BCT_map_rows"] == 3, "key BCT")
    require(key["accepted_selected_threshold_source_rows"] == 0, "key threshold")

    require(cert["PMNS_minimal_oscillation_policy_closed"] is True, "cert PMNS")
    require(cert["PMNS_replay_ready"] is True, "cert replay")
    require(cert["PMNS_source_rows_closed"] is False, "cert PMNS source")
    require(cert["absolute_neutrino_mass_closed"] is False, "cert absolute")
    require(cert["running_mass_proxy_layer_closed"] is True, "cert running")
    require(cert["precision_running_mass_source_rows_closed"] is False, "cert running source")
    require(cert["threshold_mass_scheme_readiness_closed"] is True, "cert readiness")
    require(cert["selected_threshold_matching_source_rows_closed"] is False, "cert threshold")
    require(cert["higgs_threshold_rows_closed"] is False, "cert Higgs")
    require(cert["strict_PEW_directK_values_closed"] is False, "cert PEW")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    for phrase in [
        "PMNS minimal oscillation policy: closed",
        "selected PMNS source rows: `0`",
        "precision running mass-ratio/source rows: `0`",
        "external top/Higgs coordinate rows in readiness harness: `2`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
