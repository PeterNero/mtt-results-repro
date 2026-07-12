"""Audit RG policy, covariance policy, and observable suite artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "sm_equivalence_rgpolicy_covariance_and_observable_suite.candidate.json"
CERT = ROOT / "certificates" / "sm_equivalence_rgpolicy_covariance_and_observable_suite_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_SM_Equivalence_RGPolicy_Covariance_and_ObservableSuite_v1.md"
BUILDER = ROOT / "scripts" / "build_sm_equivalence_rgpolicy_covariance_and_observable_suite.py"

STATUS = "MTT_SM_EQUIVALENCE_RGPOLICY_COVARIANCE_AND_OBSERVABLESUITE_BUILT_TRANSPORT_VALUES_OPEN"
NEXT = "MTT_SM_Equivalence_CommonScale_ValueTransport_and_FinalPacketCertificate_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    rg = data["rg_policy"]
    require(rg["status"] == "POLICY_DECLARED_TRANSPORT_VALUES_OPEN", "RG status mismatch")
    require(rg["reference_scale"] == "M_Z", "reference scale mismatch")
    require(rg["scheme"] == "MSbar", "scheme mismatch")
    require(rg["gauge_normalization"]["U1"] == "GUT-normalized alpha_1=(5/3) alpha_Y", "U1 normalization mismatch")
    require(rg["first_pass_loop_order"]["one_loop_scaffold_declared"] is True, "one-loop scaffold missing")
    require(rg["first_pass_loop_order"]["higher_loop_precision_required_for_precision_claim"] is True, "precision guard missing")
    require("choosing thresholds from residual minimization" in rg["threshold_policy"]["not_allowed"], "threshold guard missing")
    for key in ["Y_u_MZ", "Y_d_MZ", "Y_e_MZ", "lambda_H_MZ"]:
        require(rg["transport_outputs_required"][key] is True, f"transport output not required: {key}")
    for key in ["alpha_1_MZ", "alpha_2_MZ", "alpha_3_MZ"]:
        require(rg["transport_outputs_required"][key] is False, f"gauge value wrongly marked as needing transport: {key}")
        require(rg["already_at_reference_scale"][key]["central_value"] > 0.0, f"{key} missing MZ value")
    require(rg["already_at_reference_scale"]["gauge_triplet_MZ"] is True, "gauge triplet not at MZ")

    cov = data["covariance_policy"]
    require(cov["status"] == "CENTRAL_VALUE_BASELINE_DECLARED_FULL_COVARIANCE_OPEN", "covariance status mismatch")
    require(cov["baseline"] == "central-value parity certificate with uncertainty sidecars", "covariance baseline mismatch")
    for key in ["masses", "CKM", "PMNS", "gauge", "Higgs"]:
        require(cov["sidecar_uncertainties_required"][key] is True, f"uncertainty sidecar missing: {key}")
    for key in ["PDG_CKM_global_fit", "NuFIT_PMNS_profile", "electroweak_fit_correlations", "mass_correlations_and_scheme_correlations"]:
        require(cov["full_covariance_open"][key] is True, f"full covariance not open: {key}")

    nu = data["neutrino_policy"]
    require(nu["status"] == "MINIMAL_OSCILLATION_PARITY_DECLARED_ABSOLUTE_SCALE_OPEN", "neutrino status mismatch")
    require(nu["what_this_closes"]["PMNS_angles_delta_and_mass_splittings_replay"] is True, "PMNS replay not closed")
    require(nu["what_this_closes"]["Dirac_neutrino_1M_route_kept_as_MTT_extension_slot"] is True, "1M route missing")
    for key in ["absolute_neutrino_mass_scale", "Dirac_Yukawa_magnitudes", "Majorana_vs_Dirac_external_empirical_policy"]:
        require(nu["what_remains_open"][key] is True, f"neutrino gate not open: {key}")

    suite = data["observable_suite"]
    require(suite["status"] == "SUITE_DECLARED_VALUES_PARTIAL", "suite status mismatch")
    rows = suite["rows"]
    for key in ["source_packet", "charged_masses", "higgs_tree", "CKM", "PMNS", "gauge_MZ", "local_QFT_observables"]:
        require(key in rows, f"observable row missing: {key}")
        require("tolerance" in rows[key], f"observable row missing tolerance: {key}")
    require(rows["gauge_MZ"]["blocks_true_equivalence"] is False, "MZ gauge should not block by itself")
    for key in ["source_packet", "charged_masses", "higgs_tree", "CKM", "PMNS", "local_QFT_observables"]:
        require(rows[key]["blocks_true_equivalence"] is True, f"row should block true equivalence: {key}")

    final_packet = data["final_packet_policy"]
    require(final_packet["status"] == "FINAL_SELECTED_SM_PACKET_CERTIFICATE_OPEN", "final packet status mismatch")
    require(final_packet["current_interface_support"] is True, "interface support missing")
    require(final_packet["sm_parity_interface_components_supported"] is True, "SM parity components not supported")
    require(final_packet["critical_open_source_component"] == "qa_su3_color_operator_packet", "critical open component mismatch")
    require(len(final_packet["required_certificate_fields"]) == 6, "certificate field count mismatch")

    progress = data["cutset_progress"]
    require(progress == {
        "C1_common_RG_policy": "POLICY_DECLARED_VALUES_OPEN",
        "C2_covariance_profile_policy": "CENTRAL_VALUE_BASELINE_DECLARED_FULL_COVARIANCE_OPEN",
        "C3_neutrino_absolute_policy": "MINIMAL_OSCILLATION_PARITY_DECLARED_ABSOLUTE_SCALE_OPEN",
        "C4_observable_suite": "SUITE_DECLARED_LOCAL_QFT_AND_COMMON_SCALE_VALUES_OPEN",
        "C5_selected_SM_packet_certificate": "OPEN",
    }, "cutset progress mismatch")

    closes = data["what_closes_now"]
    for key in [
        "RG_reference_scheme_and_scale_policy",
        "central_value_covariance_tier_policy",
        "minimal_neutrino_oscillation_policy",
        "observable_suite_manifest",
        "next_value_transport_contract",
        "source_selection_guardrails_preserved",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "common_scale_Yukawa_Higgs_transport_values",
        "loop_threshold_beta_function_implementation",
        "full_covariance_profile_likelihood",
        "absolute_neutrino_mass_or_external_policy_upgrade",
        "local_QFT_observable_functor_values",
        "selected_SM_packet_final_certificate",
        "true_SM_equivalence_closure",
        "full_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining gate missing: {key}")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM equivalence overclaimed")
    require(data["no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["native_replay_closure_claimed"] is True, "native replay closure lost")
    require(data["observed_data_used_as_selector"] is False, "observed data used as selector")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["source_boundary_preserved"] is True, "source boundary not preserved")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("reference scale: M_Z" in note, "note missing RG policy")
    require("C5 selected SM packet certificate: open" in note, "note missing packet gate")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
