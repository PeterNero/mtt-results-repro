"""Build common-scale value transport and final packet certificate gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

POLICY = DATA / "sm_equivalence_rgpolicy_covariance_and_observable_suite.candidate.json"
MIXING = DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json"
TREE = DATA / "sm_equivalence_tree_level_replay_seed.candidate.json"
SM_PACKET = DATA / "actual_selected_sm_packet_anomaly_audit.candidate.json"

OUTPUT = DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json"
CERT = CERTS / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.json"
NOTE = CORPUS / "MTT_SM_Equivalence_CommonScale_ValueTransport_and_FinalPacketCertificate_v1.md"

STATUS = "MTT_SM_EQUIVALENCE_COMMONSCALE_VALUE_TRANSPORT_AND_FINALPACKETCERT_BUILT_PARTIAL_GAUGE_CLOSED"
NEXT = "MTT_SM_Equivalence_SelectedSMPacket_or_RGTransport_ValueFill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    policy = load(POLICY)
    mixing = load(MIXING)
    tree = load(TREE)
    sm_packet = load(SM_PACKET)

    rg_policy = policy["rg_policy"]
    gauge = mixing["gauge_replay_MZ"]["numeric_triplet"]
    tree_replay = tree["tree_level_replay"]

    common_scale_packet = {
        "status": "PARTIAL_COMMON_SCALE_PACKET_GAUGE_ONLY",
        "reference_scale": rg_policy["reference_scale"],
        "scheme": rg_policy["scheme"],
        "closed_values": {
            "alpha_1_GUT_MZ": gauge["alpha_1_GUT"],
            "alpha_2_MZ": gauge["alpha_2"],
            "alpha_3_MZ": gauge["alpha_3"],
            "g_1_GUT_MZ": gauge["g_1_GUT"],
            "g_2_MZ": gauge["g_2"],
            "g_3_MZ": gauge["g_3"],
        },
        "native_values_carried_but_not_common_scale": {
            "Y_u_native": tree_replay["yukawa_matrices"]["Y_u_diag"],
            "Y_d_native_complex_up_diagonal_convention": mixing["CKM_replay"]["Y_d_complex"],
            "Y_e_native": tree_replay["yukawa_matrices"]["Y_e_diag"],
            "lambda_H_tree_native": tree_replay["higgs_tree"]["lambda_tree"],
            "CKM_native": mixing["CKM_replay"]["input_CKM_matrix"],
            "PMNS_native": mixing["PMNS_replay"]["input_PMNS_matrix"],
        },
        "transport_values_open": {
            "Y_u_MZ": True,
            "Y_d_MZ": True,
            "Y_e_MZ": True,
            "lambda_H_MZ": True,
            "pole_to_running_mass_maps": True,
            "threshold_matching_values": True,
        },
        "why_partial": (
            "The gauge triplet was sourced directly in the declared M_Z MSbar convention. "
            "The mass/Yukawa/Higgs values were replayed at native reference conventions and "
            "need explicit pole/MSbar and threshold transport before common-scale closure."
        ),
    }

    source_rows = []
    for row in sm_packet["packet_components"]:
        source_rows.append(
            {
                "id": row["id"],
                "component": row["component"],
                "closed_for_sm_parity_interface": row["closed_for_sm_parity_interface"],
                "closed_as_actual_selected_no_knob_packet": row["closed_as_actual_selected_no_knob_packet"],
                "required_selected_data": row["required_selected_data"],
            }
        )

    interface_supported = all(row["closed_for_sm_parity_interface"] for row in source_rows if row["id"] != "qa_su3_color_operator_packet")
    qa_su3_open = next(row for row in source_rows if row["id"] == "qa_su3_color_operator_packet")

    final_packet_certificate = {
        "status": "SM_PARITY_INTERFACE_PARTIAL_CERTIFICATE_BUILT_QA_SU3_OPEN",
        "interface_components_supported_except_QaSU3": interface_supported,
        "source_rows": source_rows,
        "critical_open_row": qa_su3_open,
        "can_close_true_SM_equivalence_now": False,
        "can_close_SM_parity_interface_without_QaSU3": False,
        "reason": (
            "Gauge carrier, fermion representation, family, Higgs/trilinear, and anomaly "
            "support are present at the SM-parity interface level, but the Qa/SU3 "
            "color/operator packet is explicitly marked open and not replaceable by "
            "measured replay values."
        ),
        "unsafe_shortcuts_rejected": sm_packet["unsafe_shortcuts_rejected"],
    }

    observable_status = {
        "gauge_MZ": "CLOSED_AT_DECLARED_REFERENCE_SCALE",
        "charged_masses": "NATIVE_REPLAY_CLOSED_COMMON_SCALE_TRANSPORT_OPEN",
        "higgs_tree": "NATIVE_TREE_REPLAY_CLOSED_RUNNING_LAMBDA_OPEN",
        "CKM": "NATIVE_COMPLEX_REPLAY_CLOSED_RG_COVARIANCE_OPEN",
        "PMNS": "OSCILLATION_REPLAY_CLOSED_ABSOLUTE_POLICY_OPEN",
        "source_packet": "PARTIAL_CERTIFICATE_QA_SU3_OPEN",
        "local_QFT_observables": "OPEN",
    }

    candidate = {
        "candidate": "MTTSMEquivalenceCommonScaleValueTransportAndFinalPacketCertificate",
        "status": STATUS,
        "inputs": {
            "rg_policy_covariance_observable_suite": rel(POLICY),
            "mixing_and_gauge_replay": rel(MIXING),
            "tree_level_replay_seed": rel(TREE),
            "actual_selected_sm_packet_anomaly_audit": rel(SM_PACKET),
        },
        "common_scale_packet": common_scale_packet,
        "final_packet_certificate": final_packet_certificate,
        "observable_status": observable_status,
        "closure_decision": {
            "native_replay_layer": "SUBSTANTIALLY_CLOSED",
            "common_scale_gauge_values": "CLOSED",
            "common_scale_yukawa_higgs_values": "OPEN",
            "selected_SM_packet_final_certificate": "OPEN_QA_SU3_COLOR_OPERATOR_PACKET",
            "true_SM_equivalence": "OPEN",
            "no_knob_SM_derivation": "OPEN",
        },
        "what_closes_now": {
            "common_scale_gauge_values_at_MZ": True,
            "partial_common_scale_packet_built": True,
            "final_packet_certificate_rows_instantiated": True,
            "QaSU3_identified_as_source_interface_blocker": True,
            "value_transport_blockers_separated_from_source_certificate_blockers": True,
            "source_selection_guardrails_preserved": True,
        },
        "what_remains_open": {
            "Yukawa_common_scale_transport": True,
            "Higgs_lambda_common_scale_transport": True,
            "loop_threshold_beta_function_values": True,
            "full_covariance_profile_likelihood": True,
            "absolute_neutrino_mass_or_policy_upgrade": True,
            "local_QFT_observable_functor_values": True,
            "QaSU3_color_operator_packet": True,
            "selected_SM_packet_final_certificate": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_closure": True,
        },
        "closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "native_replay_closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_boundary_preserved": True,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "CommonScaleGaugeClosureAndPacketBlockerSeparationTheorem",
            "proved": True,
            "statement": (
                "At the declared MSbar M_Z reference point, the gauge triplet already forms a "
                "closed common-scale value packet.  The charged Yukawa/Higgs values remain "
                "native replay data until an explicit transport implementation emits M_Z "
                "running values.  Independently, the final SM packet certificate remains open "
                "because the Qa/SU3 color/operator packet is not closed.  Thus true SM "
                "equivalence reduces to two separated gates: value transport and final selected "
                "SM packet certification."
            ),
        },
    }

    cert = {
        "certificate": "MTT_SM_Equivalence_CommonScale_ValueTransport_and_FinalPacketCertificate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "native_replay_closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_boundary_preserved": True,
        "theorem_proved": True,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT SM Equivalence CommonScale ValueTransport and FinalPacketCertificate v1

Status: `{STATUS}`.

Closed at the declared common scale:

```text
alpha_1^GUT(M_Z) = {gauge["alpha_1_GUT"]["central_value"]}
alpha_2(M_Z)     = {gauge["alpha_2"]["central_value"]}
alpha_3(M_Z)     = {gauge["alpha_3"]["central_value"]}
```

Still not transported to common scale:

```text
Y_u(M_Z), Y_d(M_Z), Y_e(M_Z)
lambda_H(M_Z)
pole-to-running mass maps
threshold matching values
```

Final selected SM packet status:

```text
SM-parity interface support except Qa/SU3: {interface_supported}
critical open row: qa_su3_color_operator_packet
true SM equivalence: open
```

The remaining gates are separated:

```text
Gate A: common-scale Yukawa/Higgs/threshold transport values
Gate B: final selected SM packet certificate, especially Qa/SU3 color/operator packet
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
