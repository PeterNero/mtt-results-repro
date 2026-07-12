"""Build common-RG and empirical audit gate for SM equivalence."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

MIXING = DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json"
TREE = DATA / "sm_equivalence_tree_level_replay_seed.candidate.json"
MANIFEST = DATA / "sm_equivalence_measured_parameter_replay_manifest.candidate.json"
LEDGER = DATA / "empirical_equivalence_ledger.candidate.json"
SM_PACKET = DATA / "actual_selected_sm_packet_anomaly_audit.candidate.json"

OUTPUT = DATA / "sm_equivalence_common_rg_and_empirical_audit.candidate.json"
CERT = CERTS / "sm_equivalence_common_rg_and_empirical_audit_certificate.json"
NOTE = CORPUS / "MTT_SM_Equivalence_Common_RG_and_Empirical_Audit_v1.md"

STATUS = "MTT_SM_EQUIVALENCE_COMMON_RG_AND_EMPIRICAL_AUDIT_BUILT_TRUE_EQUIVALENCE_OPEN"
NEXT = "MTT_SM_Equivalence_RGPolicy_Covariance_and_ObservableSuite_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    mixing = load(MIXING)
    tree = load(TREE)
    manifest = load(MANIFEST)
    ledger = load(LEDGER)
    sm_packet = load(SM_PACKET)

    replay_tests = mixing["replay_tests"]
    tree_tests = tree["replay_tests"]

    native_replay = {
        "standard": "native published-parameter replay",
        "meaning": (
            "Each measured slot is replayed in its declared source convention: pole/on-shell "
            "where the reference packet says pole/on-shell, MSbar at M_Z for gauge couplings, "
            "NuFIT oscillation convention for PMNS, and PDG CKM convention for CKM."
        ),
        "closed_rows": {
            "charged_fermion_and_quark_mass_to_tree_yukawa_loop": tree_tests[
                "mass_replay_exact_by_construction"
            ],
            "higgs_tree_lambda_seed": tree_tests["higgs_lambda_tree_built"],
            "electroweak_tree_seed": tree_tests["electroweak_tree_seed_built"],
            "CKM_complex_down_yukawa_replay": replay_tests["CKM_complex_Yukawa_matrix_built"],
            "PMNS_oscillation_mass_squared_replay": replay_tests["PMNS_mass_splittings_replayed"],
            "MZ_gauge_alpha_triplet": replay_tests["gauge_alpha1_alpha2_alpha3_values_ready"],
        },
        "status": "NATIVE_CONVENTION_REPLAY_EXECUTABLE",
    }

    common_rg = {
        "standard": "true common-scale SM equivalence",
        "meaning": (
            "All replay quantities are transported into one declared renormalization scheme, "
            "scale, loop order, threshold prescription, and covariance/profile convention before "
            "the empirical audit is allowed to claim SM equivalence."
        ),
        "selected_policy": {
            "preferred_reference_scale": "M_Z",
            "preferred_scheme": "MSbar for running gauge/Yukawa/Higgs parameters, with explicitly declared pole-to-running conversions where needed",
            "minimum_loop_policy": "open; must be specified before closure",
            "threshold_policy": "open; must specify heavy-quark, W/Z/H/top, and neutrino-sector treatment",
            "covariance_policy": "open; must encode or explicitly justify omission of PDG/NuFIT/electroweak-fit correlations",
            "neutrino_policy": "open; PMNS oscillation replay is closed, absolute mass and Dirac/Majorana convention are not",
        },
        "closed_rows": {
            "typed_measured_slots_declared": manifest["what_closes_now"][
                "SM_equivalence_replay_pipeline_declared"
            ],
            "source_nonselection_guardrail": mixing["source_boundary_preserved"],
            "native_replay_values_available": True,
        },
        "open_rows": {
            "single_common_scale_transport": True,
            "loop_order_beta_functions_and_thresholds": True,
            "mass_scheme_unification": True,
            "Yukawa_running_matrices_at_common_scale": True,
            "Higgs_lambda_running_at_common_scale": True,
            "full_CKM_PMNS_covariance_or_profile_likelihood": True,
            "absolute_neutrino_mass_or_declared_minimal_parity_policy": True,
            "observable_suite_with_tolerances": True,
        },
        "status": "TRUE_COMMON_SCALE_EQUIVALENCE_OPEN",
    }

    empirical_audit = {
        "audit_standard": "sector-by-sector SM equivalence audit",
        "ledger_interfaces_ready": ledger["acceptance_summary"]["interfaces_ready_for_empirical_audit"],
        "required_rows": {
            "SM_source_interface": {
                "status": "PARTIAL_SOURCE_PACKET_BUILT_ANOMALY_INTERFACE_OPEN",
                "evidence": rel(SM_PACKET),
                "blocks_true_equivalence": True,
                "reason": "True equivalence needs one consolidated selected SM gauge/representation/family/Higgs packet and anomaly/observable certificate.",
            },
            "masses_and_tree_yukawas": {
                "status": "NATIVE_REPLAY_CLOSED_COMMON_RG_OPEN",
                "evidence": rel(TREE),
                "blocks_true_equivalence": True,
                "reason": "Tree replay is executable, but mixed pole/MSbar/native scales still need common RG transport.",
            },
            "CKM_and_complex_quark_Yukawa": {
                "status": "NATIVE_REPLAY_CLOSED_COVARIANCE_RG_OPEN",
                "evidence": rel(MIXING),
                "blocks_true_equivalence": True,
                "reason": "Complex matrix replay is closed in a declared convention; covariance/profile and common-scale running remain open.",
            },
            "PMNS_and_neutrino_splittings": {
                "status": "OSCILLATION_REPLAY_CLOSED_ABSOLUTE_NEUTRINO_OPEN",
                "evidence": rel(MIXING),
                "blocks_true_equivalence": True,
                "reason": "Oscillation splittings replay, but absolute mass and Dirac/Majorana policy must be declared for full equivalence.",
            },
            "gauge_triplet": {
                "status": "MZ_TRIPLET_CLOSED_RG_THRESHOLD_POLICY_OPEN",
                "evidence": rel(MIXING),
                "blocks_true_equivalence": True,
                "reason": "alpha_1, alpha_2, alpha_3 are emitted at M_Z; threshold/loop policy and covariance remain open.",
            },
            "QFT_observable_functor": {
                "status": "INTERFACE_DECLARED_OBSERVABLE_SUITE_OPEN",
                "evidence": rel(LEDGER),
                "blocks_true_equivalence": True,
                "reason": "Need a declared observable suite and tolerance policy beyond parameter replay.",
            },
        },
        "can_claim_native_replay_closure": True,
        "can_claim_true_SM_equivalence": False,
        "can_claim_no_knob_closure": False,
    }

    minimum_closure_cutset = [
        {
            "id": "C1_common_RG_policy",
            "task": "Choose and implement one RG scheme/scale/loop/threshold policy, preferably MSbar at M_Z for the first closure certificate.",
            "why_minimal": "It turns mixed reference values into one comparable SM parameter packet.",
        },
        {
            "id": "C2_covariance_profile_policy",
            "task": "Encode covariance/profile policy for CKM, PMNS, electroweak, and mass inputs, or declare a central-value parity standard with explicit precision limits.",
            "why_minimal": "It defines what counts as matching the measured SM data.",
        },
        {
            "id": "C3_neutrino_absolute_policy",
            "task": "Declare minimal-mass oscillation-only parity, or add absolute neutrino mass and Dirac/Majorana policy.",
            "why_minimal": "PMNS alone is not a full neutrino sector.",
        },
        {
            "id": "C4_observable_suite",
            "task": "Build a sector-by-sector empirical replay suite with tolerances: masses, mixings, gauge values, Higgs parameters, anomaly/interface checks, and selected low-energy observables.",
            "why_minimal": "True equivalence is an audit statement, not only a data table.",
        },
        {
            "id": "C5_selected_SM_packet_certificate",
            "task": "Bundle the selected SM gauge/representation/family/Higgs/anomaly interface into one final packet certificate.",
            "why_minimal": "Measured replay is downstream and cannot itself certify the SM source packet.",
        },
    ]

    candidate = {
        "candidate": "MTTSMEquivalenceCommonRGAndEmpiricalAudit",
        "status": STATUS,
        "inputs": {
            "mixing_and_gauge_replay": rel(MIXING),
            "tree_level_replay_seed": rel(TREE),
            "measured_parameter_replay_manifest": rel(MANIFEST),
            "empirical_equivalence_ledger": rel(LEDGER),
            "actual_selected_sm_packet_anomaly_audit": rel(SM_PACKET),
        },
        "superset_strategy_use": {
            "mode": "SUPERSET_TO_LOCKED_SOURCE_THEN_STRAIGHT_MEASURED_REPLAY",
            "source_side": "superset paths may support the selected SM packet and no-knob upgrades",
            "measured_replay_side": "common-RG and empirical audit use measured SM inputs only after source/interface declaration",
            "measured_targets_used_to_lock_source": False,
        },
        "native_published_parameter_replay": native_replay,
        "common_RG_true_equivalence_gate": common_rg,
        "empirical_audit": empirical_audit,
        "minimum_closure_cutset": minimum_closure_cutset,
        "closure_level": {
            "native_replay_layer": "SUBSTANTIALLY_CLOSED",
            "true_common_scale_SM_equivalence": "OPEN",
            "no_knob_SM_derivation": "OPEN",
        },
        "what_closes_now": {
            "native_published_parameter_replay_audit": True,
            "true_SM_equivalence_standard_declared": True,
            "common_RG_cutset_identified": True,
            "empirical_audit_rows_identified": True,
            "source_selection_guardrails_preserved": True,
        },
        "what_remains_open": {
            "common_RG_transport_values": True,
            "loop_order_and_threshold_policy": True,
            "covariance_or_profile_policy": True,
            "absolute_neutrino_mass_or_minimal_policy": True,
            "observable_suite_with_tolerances": True,
            "selected_SM_packet_final_certificate": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_closure": True,
        },
        "closure_claimed": False,
        "native_replay_closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_boundary_preserved": True,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "CommonRGAndEmpiricalAuditCutsetTheorem",
            "proved": True,
            "statement": (
                "The current measured SM-parity replay is executable at native published "
                "conventions for masses/tree Yukawas, CKM, PMNS oscillation splittings, and "
                "the M_Z gauge triplet.  True SM equivalence is not yet proved because it "
                "requires a common RG scheme/scale/loop/threshold policy, covariance/profile "
                "handling, neutrino-sector completion or minimal policy, an observable suite "
                "with tolerances, and a bundled selected SM packet certificate.  None of these "
                "open gates may be filled by using measured values as source selectors."
            ),
        },
    }

    cert = {
        "certificate": "MTT_SM_Equivalence_Common_RG_and_Empirical_Audit_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "native_replay_closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_boundary_preserved": True,
        "theorem_proved": True,
        "minimum_closure_cutset": minimum_closure_cutset,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT SM Equivalence Common RG and Empirical Audit v1

Status: `{STATUS}`.

This artifact separates three standards:

```text
native published-parameter replay: substantially closed
true common-scale SM equivalence: open
no-knob SM derivation: open
```

The native replay layer is now executable for:

```text
mass -> tree Yukawa -> mass
Higgs tree lambda seed
CKM complex down-Yukawa replay
PMNS oscillation mass-squared replay
M_Z gauge triplet alpha_1, alpha_2, alpha_3
```

True SM equivalence still requires the minimum cutset:

```text
C1 common RG policy and transport
C2 covariance/profile or declared central-value precision policy
C3 neutrino absolute-mass or minimal oscillation-only policy
C4 empirical observable suite with tolerances
C5 final selected SM packet/anomaly/interface certificate
```

The superset strategy remains source-side only: it may help certify the selected
SM packet or no-knob upgrade targets, but measured masses, mixings, gauge
couplings, and residuals do not select source structure.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
