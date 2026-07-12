"""Build common-scale Yukawa/Higgs transport kernel scaffold / final replay audit gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_commonscaleyukawahiggstransport_or_finalreplayaudit"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
KERNEL = PACKET_DIR / "yukawa_higgs_common_scale_transport_kernel.packet.json"
AUDIT_PLAN = PACKET_DIR / "final_empirical_replay_audit_plan.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CommonScaleYukawaHiggsTransport_or_FinalReplayAudit_v1.md"

STATUS = "MTT_SELECTED_COMMONSCALEYUKAWAHIGGSTRANSPORT_OR_FINALREPLAYAUDIT_BUILT_TRANSPORT_KERNEL_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RGEngineExecution_or_SelectedSMPacketCertificateIntegration_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    final_gap = load(DATA / "selected_finalsmparitygapmatrix_or_closureattempt.candidate.json")
    reference = load(DATA / "sm_equivalence_reference_data_values_fill.candidate.json")
    tree = load(DATA / "sm_equivalence_tree_level_replay_seed.candidate.json")
    common = load(DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json")
    mixing = load(DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json")

    native = common["common_scale_packet"]["native_values_carried_but_not_common_scale"]
    masses = tree["tree_level_replay"]["input_masses_GeV"]
    higgs = tree["tree_level_replay"]["higgs_tree"]
    gauge = common["common_scale_packet"]["closed_values"]

    transport_kernel = {
        "schema": "MTTYukawaHiggsCommonScaleTransportKernel.v1",
        "status": "TRANSPORT_KERNEL_SPEC_BUILT_VALUES_NOT_EMITTED",
        "target_scale": "M_Z",
        "target_scheme": "MSbar",
        "available_common_scale_inputs": {
            "alpha_1_GUT_MZ": gauge["alpha_1_GUT_MZ"],
            "alpha_2_MZ": gauge["alpha_2_MZ"],
            "alpha_3_MZ": gauge["alpha_3_MZ"],
            "g_1_GUT_MZ": gauge["g_1_GUT_MZ"],
            "g_2_MZ": gauge["g_2_MZ"],
            "g_3_MZ": gauge["g_3_MZ"],
        },
        "native_values_to_transport": {
            "Y_u_native": native["Y_u_native"],
            "Y_d_native_complex_up_diagonal_convention": native["Y_d_native_complex_up_diagonal_convention"],
            "Y_e_native": native["Y_e_native"],
            "lambda_H_tree_native": native["lambda_H_tree_native"],
            "input_masses_GeV": masses,
            "higgs_tree": higgs,
        },
        "required_engine_inputs": {
            "renormalization_scheme": "MSbar",
            "loop_order": "declare 1-loop minimum; 2-loop preferred for parity-grade audit",
            "threshold_policy": "top, bottom, charm, tau, W/Z/H threshold matching policy required",
            "mass_scheme_policy": "pole/rest/direct masses must be mapped to running masses before M_Z Yukawas are claimed",
            "covariance_policy": "propagate supplied measurement uncertainties; correlations remain explicit open data if absent",
            "beta_functions_required": [
                "gauge beta functions",
                "Y_u/Y_d/Y_e beta functions",
                "Higgs lambda beta function",
                "top/Higgs/electroweak matching terms",
            ],
        },
        "emitted_values": {
            "Y_u_MZ": None,
            "Y_d_MZ": None,
            "Y_e_MZ": None,
            "lambda_H_MZ": None,
        },
        "why_values_not_emitted": (
            "The repo has native measured seeds and M_Z gauge values, but no selected/versioned RG engine "
            "with loop order, thresholds, pole-to-running conversions, and covariance propagation. Emitting "
            "M_Z Yukawa/Higgs values here would be an unverified transport shortcut."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    audit_plan = {
        "schema": "MTTFinalEmpiricalReplayAuditPlan.v1",
        "status": "FINAL_REPLAY_AUDIT_PLAN_BUILT_WAITING_FOR_TRANSPORT_VALUES_AND_PACKET_CERT",
        "audit_blocks": [
            {
                "block": "gauge_MZ",
                "input_status": "closed",
                "comparison": "alpha1_GUT, alpha2, alpha3 at M_Z",
                "can_run_now": True,
            },
            {
                "block": "charged_yukawa_MZ",
                "input_status": "open_transport_values",
                "comparison": "Y_u, Y_d, Y_e at M_Z with uncertainty policy",
                "can_run_now": False,
            },
            {
                "block": "higgs_lambda_MZ",
                "input_status": "open_transport_values",
                "comparison": "lambda_H(M_Z) under declared potential and matching convention",
                "can_run_now": False,
            },
            {
                "block": "CKM_PMNS_native",
                "input_status": "native_replay_available_covariance_open",
                "comparison": "unitarity, convention, phase, and uncertainty profile",
                "can_run_now": False,
            },
            {
                "block": "selected_SM_packet_certificate",
                "input_status": "open_Qa_SU3_packet_integration",
                "comparison": "source-side packet attached before final SM-parity claim",
                "can_run_now": False,
            },
        ],
        "minimum_to_close_SM_parity_after_this": [
            "execute RG transport engine for Yukawa/Higgs values",
            "attach selected SM packet certificate, especially Qa/SU3 color/operator packet",
            "run final empirical replay audit over frozen observed packets",
        ],
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "MTTSelectedCommonScaleYukawaHiggsTransportOrFinalReplayAudit",
        "status": STATUS,
        "inputs": {
            "final_gap_matrix": rel(DATA / "selected_finalsmparitygapmatrix_or_closureattempt.candidate.json"),
            "reference_values": rel(DATA / "sm_equivalence_reference_data_values_fill.candidate.json"),
            "tree_level_replay_seed": rel(DATA / "sm_equivalence_tree_level_replay_seed.candidate.json"),
            "common_scale_packet": rel(DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json"),
            "mixing_and_gauge_replay": rel(DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json"),
        },
        "output_packets": {
            "yukawa_higgs_common_scale_transport_kernel": rel(KERNEL),
            "final_empirical_replay_audit_plan": rel(AUDIT_PLAN),
        },
        "theorem": {
            "name": "CommonScaleYukawaHiggsTransportKernelTheorem",
            "proved": True,
            "statement": (
                "The repo now contains all native measured Yukawa/Higgs seeds and the M_Z gauge triplet "
                "needed to define a common-scale transport kernel. It does not yet emit Y_u(M_Z), Y_d(M_Z), "
                "Y_e(M_Z), or lambda_H(M_Z), because that requires a selected/versioned RG engine with "
                "loop order, thresholds, mass-scheme conversion, and covariance policy."
            ),
        },
        "what_closes_now": {
            "common_scale_yukawa_higgs_transport_kernel_specified": True,
            "native_values_to_transport_bound_into_one_packet": True,
            "final_empirical_replay_audit_plan_built": True,
            "transport_shortcut_rejected": True,
            "superset_strategy_remains_locked_to_downstream_replay": True,
        },
        "what_remains_open": {
            "RG_engine_execution": True,
            "Y_u_MZ_Y_d_MZ_Y_e_MZ_values": True,
            "lambda_H_MZ_value": True,
            "threshold_matching_values": True,
            "covariance_profile_likelihood_execution": True,
            "selected_SM_packet_certificate_integration": True,
            "final_integrated_empirical_replay_audit": True,
            "SM_parity_closure": True,
        },
        "closure_decision": {
            "patched_SM_parity_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_blocker_sets": final_gap["blocker_sets"],
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "source_boundary_preserved": reference["source_boundary_preserved"] and mixing["source_boundary_preserved"],
    }

    cert = {
        "certificate": "MTT_Selected_CommonScaleYukawaHiggsTransport_or_FinalReplayAudit_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT_ARTIFACT,
    }

    note = f"""# MTT Selected CommonScaleYukawaHiggsTransport or FinalReplayAudit v1

Status: `{STATUS}`.

This builds the common-scale transport kernel scaffold for the remaining
Yukawa/Higgs SM-parity blocker. It binds native measured seeds and the M_Z
gauge triplet into one replay target, but deliberately does not emit transported
values without a versioned RG engine.

```text
Y_u(M_Z), Y_d(M_Z), Y_e(M_Z) = OPEN
lambda_H(M_Z)                = OPEN
final empirical replay audit = PLANNED, not run
SM-parity closure            = False
```

The next required artifact is `{NEXT_ARTIFACT}`.
"""

    KERNEL.write_text(json.dumps(transport_kernel, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    AUDIT_PLAN.write_text(json.dumps(audit_plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
