"""Build RG policy, covariance policy, and observable suite for SM equivalence."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "sm_equivalence_common_rg_and_empirical_audit.candidate.json"
MIXING = DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json"
TREE = DATA / "sm_equivalence_tree_level_replay_seed.candidate.json"
SM_PACKET = DATA / "actual_selected_sm_packet_anomaly_audit.candidate.json"

OUTPUT = DATA / "sm_equivalence_rgpolicy_covariance_and_observable_suite.candidate.json"
CERT = CERTS / "sm_equivalence_rgpolicy_covariance_and_observable_suite_certificate.json"
NOTE = CORPUS / "MTT_SM_Equivalence_RGPolicy_Covariance_and_ObservableSuite_v1.md"

STATUS = "MTT_SM_EQUIVALENCE_RGPOLICY_COVARIANCE_AND_OBSERVABLESUITE_BUILT_TRANSPORT_VALUES_OPEN"
NEXT = "MTT_SM_Equivalence_CommonScale_ValueTransport_and_FinalPacketCertificate_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    previous = load(PREVIOUS)
    mixing = load(MIXING)
    tree = load(TREE)
    sm_packet = load(SM_PACKET)

    rg_policy = {
        "status": "POLICY_DECLARED_TRANSPORT_VALUES_OPEN",
        "reference_scale": "M_Z",
        "scheme": "MSbar",
        "gauge_normalization": {
            "U1": "GUT-normalized alpha_1=(5/3) alpha_Y",
            "SU2": "alpha_2",
            "SU3": "alpha_3",
        },
        "first_pass_loop_order": {
            "classification": "CENTRAL_VALUE_REPLAY_POLICY",
            "rule": (
                "Use published central values in their declared schemes as inputs; common-scale "
                "transport must later declare beta functions, matching thresholds, and pole-to-running maps."
            ),
            "one_loop_scaffold_declared": True,
            "higher_loop_precision_required_for_precision_claim": True,
        },
        "threshold_policy": {
            "status": "DECLARED_OPEN_VALUES",
            "must_handle": ["u,d,s,c,b,t quark thresholds", "W/Z/H/top pole-to-running conversion", "alpha_em(M_Z) electroweak fit convention", "neutrino absolute-sector convention"],
            "not_allowed": ["choosing thresholds from residual minimization", "using measured targets to select source/operator data"],
        },
        "transport_outputs_required": {
            "Y_u_MZ": True,
            "Y_d_MZ": True,
            "Y_e_MZ": True,
            "lambda_H_MZ": True,
            "alpha_1_MZ": False,
            "alpha_2_MZ": False,
            "alpha_3_MZ": False,
            "CKM_MZ_or_declared_scale_independence": True,
            "PMNS_MZ_or_declared_low_energy_policy": True,
        },
        "already_at_reference_scale": {
            "gauge_triplet_MZ": True,
            "alpha_1_MZ": mixing["gauge_replay_MZ"]["numeric_triplet"]["alpha_1_GUT"],
            "alpha_2_MZ": mixing["gauge_replay_MZ"]["numeric_triplet"]["alpha_2"],
            "alpha_3_MZ": mixing["gauge_replay_MZ"]["numeric_triplet"]["alpha_3"],
        },
    }

    covariance_policy = {
        "status": "CENTRAL_VALUE_BASELINE_DECLARED_FULL_COVARIANCE_OPEN",
        "baseline": "central-value parity certificate with uncertainty sidecars",
        "meaning": (
            "The first true-equivalence audit may compare central values with declared residual tolerances. "
            "It cannot claim precision-global-fit equivalence until covariance/profile likelihood data are encoded."
        ),
        "sidecar_uncertainties_required": {
            "masses": True,
            "CKM": True,
            "PMNS": True,
            "gauge": True,
            "Higgs": True,
        },
        "full_covariance_open": {
            "PDG_CKM_global_fit": True,
            "NuFIT_PMNS_profile": True,
            "electroweak_fit_correlations": True,
            "mass_correlations_and_scheme_correlations": True,
        },
        "acceptance_tiers": {
            "tier_0_central_replay": "exact algebraic replay from admitted central values",
            "tier_1_uncertainty_sidecar": "central values plus uncorrelated first-order uncertainty propagation where available",
            "tier_2_profile_likelihood": "full fit covariance/profile replay; open",
        },
    }

    neutrino_policy = {
        "status": "MINIMAL_OSCILLATION_PARITY_DECLARED_ABSOLUTE_SCALE_OPEN",
        "first_pass_policy": "normal ordering with m1^2=0 representative for oscillation mass-squared replay",
        "what_this_closes": {
            "PMNS_angles_delta_and_mass_splittings_replay": mixing["replay_tests"]["PMNS_mass_splittings_replayed"],
            "Dirac_neutrino_1M_route_kept_as_MTT_extension_slot": True,
        },
        "what_remains_open": {
            "absolute_neutrino_mass_scale": True,
            "Dirac_Yukawa_magnitudes": True,
            "Majorana_vs_Dirac_external_empirical_policy": True,
        },
        "not_allowed": ["using neutrino mass scale to choose MTT source branch", "calling oscillation-only replay full neutrino-sector closure"],
    }

    observable_suite = {
        "status": "SUITE_DECLARED_VALUES_PARTIAL",
        "rows": {
            "source_packet": {
                "observable_or_check": "SU3 x SU2 x U1 carrier, chiral representation table, three families, Higgs carrier, anomaly checks",
                "current_status": "INTERFACE_PARTIAL_FINAL_CERTIFICATE_OPEN",
                "evidence": rel(SM_PACKET),
                "tolerance": "boolean exact certificate",
                "blocks_true_equivalence": True,
            },
            "charged_masses": {
                "observable_or_check": "charged leptons and quark mass seeds replayed from admitted slots",
                "current_status": "NATIVE_REPLAY_CLOSED_COMMON_SCALE_VALUES_OPEN",
                "evidence": rel(TREE),
                "tolerance": "central residual zero at native replay; common-scale residual pending",
                "blocks_true_equivalence": True,
            },
            "higgs_tree": {
                "observable_or_check": "lambda=m_H^2/(2v^2), v from G_F",
                "current_status": "TREE_SEED_CLOSED_RUNNING_LAMBDA_OPEN",
                "evidence": rel(TREE),
                "tolerance": "central residual zero at tree seed",
                "blocks_true_equivalence": True,
            },
            "CKM": {
                "observable_or_check": "unitary CKM matrix, Jarlskog, complex Y_d replay",
                "current_status": "NATIVE_REPLAY_CLOSED_COVARIANCE_RG_OPEN",
                "evidence": rel(MIXING),
                "tolerance": "unitarity residual < 1e-12; profile tolerance open",
                "blocks_true_equivalence": True,
            },
            "PMNS": {
                "observable_or_check": "unitary PMNS matrix and normal-ordering mass-squared differences",
                "current_status": "OSCILLATION_REPLAY_CLOSED_ABSOLUTE_POLICY_OPEN",
                "evidence": rel(MIXING),
                "tolerance": "unitarity residual < 1e-12; mass-splitting residual < 1e-18 eV^2",
                "blocks_true_equivalence": True,
            },
            "gauge_MZ": {
                "observable_or_check": "alpha_1, alpha_2, alpha_3 at M_Z",
                "current_status": "MZ_VALUES_CLOSED_CORRELATIONS_OPEN",
                "evidence": rel(MIXING),
                "tolerance": "formula residual < 1e-15",
                "blocks_true_equivalence": False,
            },
            "local_QFT_observables": {
                "observable_or_check": "declared correlator/S-matrix or low-energy observable functor",
                "current_status": "OPEN",
                "evidence": "candidate_data/empirical_equivalence_ledger.candidate.json",
                "tolerance": "not yet declared",
                "blocks_true_equivalence": True,
            },
        },
    }

    final_packet_policy = {
        "status": "FINAL_SELECTED_SM_PACKET_CERTIFICATE_OPEN",
        "current_interface_support": sm_packet["gate_results"]["topology_only_sm_structure_supported"],
        "sm_parity_interface_components_supported": all(
            row["closed_for_sm_parity_interface"]
            for row in sm_packet["packet_components"]
            if row["id"] != "qa_su3_color_operator_packet"
        ),
        "critical_open_source_component": "qa_su3_color_operator_packet",
        "required_certificate_fields": [
            "selected gauge carrier maps",
            "selected chiral representation table",
            "three-family selector",
            "Higgs carrier and trilinear slots",
            "machine-checkable anomaly table",
            "Qa/SU3 color/operator packet or parity-accepted interface replacement",
        ],
    }

    candidate = {
        "candidate": "MTTSMEquivalenceRGPolicyCovarianceAndObservableSuite",
        "status": STATUS,
        "inputs": {
            "common_rg_and_empirical_audit": rel(PREVIOUS),
            "mixing_and_gauge_replay": rel(MIXING),
            "tree_level_replay_seed": rel(TREE),
            "actual_selected_sm_packet_anomaly_audit": rel(SM_PACKET),
        },
        "rg_policy": rg_policy,
        "covariance_policy": covariance_policy,
        "neutrino_policy": neutrino_policy,
        "observable_suite": observable_suite,
        "final_packet_policy": final_packet_policy,
        "cutset_progress": {
            "C1_common_RG_policy": "POLICY_DECLARED_VALUES_OPEN",
            "C2_covariance_profile_policy": "CENTRAL_VALUE_BASELINE_DECLARED_FULL_COVARIANCE_OPEN",
            "C3_neutrino_absolute_policy": "MINIMAL_OSCILLATION_PARITY_DECLARED_ABSOLUTE_SCALE_OPEN",
            "C4_observable_suite": "SUITE_DECLARED_LOCAL_QFT_AND_COMMON_SCALE_VALUES_OPEN",
            "C5_selected_SM_packet_certificate": "OPEN",
        },
        "what_closes_now": {
            "RG_reference_scheme_and_scale_policy": True,
            "central_value_covariance_tier_policy": True,
            "minimal_neutrino_oscillation_policy": True,
            "observable_suite_manifest": True,
            "next_value_transport_contract": True,
            "source_selection_guardrails_preserved": True,
        },
        "what_remains_open": {
            "common_scale_Yukawa_Higgs_transport_values": True,
            "loop_threshold_beta_function_implementation": True,
            "full_covariance_profile_likelihood": True,
            "absolute_neutrino_mass_or_external_policy_upgrade": True,
            "local_QFT_observable_functor_values": True,
            "selected_SM_packet_final_certificate": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_closure": True,
        },
        "closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "native_replay_closure_claimed": previous["native_replay_closure_claimed"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_boundary_preserved": True,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "RGPolicyCovarianceObservableSuiteTheorem",
            "proved": True,
            "statement": (
                "The first true-SM-equivalence audit standard is now fixed: MSbar at M_Z "
                "with GUT-normalized U1, central-value parity with uncertainty sidecars, "
                "minimal normal-ordering oscillation neutrino replay, and a sector-by-sector "
                "observable suite.  This closes the policy ambiguity but not the actual "
                "common-scale transport values, full covariance/profile likelihood, local QFT "
                "observable functor, final selected SM packet certificate, or no-knob derivation."
            ),
        },
    }

    cert = {
        "certificate": "MTT_SM_Equivalence_RGPolicy_Covariance_and_ObservableSuite_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "native_replay_closure_claimed": previous["native_replay_closure_claimed"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_boundary_preserved": True,
        "theorem_proved": True,
        "cutset_progress": candidate["cutset_progress"],
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT SM Equivalence RGPolicy Covariance and ObservableSuite v1

Status: `{STATUS}`.

Policy now fixed for the first true-equivalence attempt:

```text
reference scale: M_Z
scheme: MSbar
U1 normalization: alpha_1=(5/3) alpha_Y
comparison tier: central-value parity with uncertainty sidecars
neutrino first pass: normal-ordering oscillation replay, m1^2=0 representative
```

This closes ambiguity, not the remaining numerical transport.

Cutset progress:

```text
C1 common RG policy: declared, transport values open
C2 covariance/profile policy: central-value baseline declared, full covariance open
C3 neutrino policy: minimal oscillation parity declared, absolute scale open
C4 observable suite: manifest declared, local QFT/common-scale values open
C5 selected SM packet certificate: open
```

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
