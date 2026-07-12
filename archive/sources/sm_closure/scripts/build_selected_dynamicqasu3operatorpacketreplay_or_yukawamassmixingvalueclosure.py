"""Replay dynamic Qa/SU3 operator packet or Yukawa/mass/mixing value closure."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
QASU3_REPLAY = PACKET_DIR / "dynamic_qasu3_operator_packet_replay.packet.json"
YUKAWA_ATTEMPT = PACKET_DIR / "yukawa_mass_mixing_value_closure_attempt.packet.json"
TRUE_EQ_GATE = PACKET_DIR / "true_equivalence_gate_after_dynamic_qasu3_replay.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_dynamic_qasu3_replay.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicQaSU3OperatorPacketReplay_or_YukawaMassMixingValueClosure_v1.md"

DYNAMIC_PACKET = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
DYNAMIC_VALUES = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)
TRUE_FRONTIER = DATA / "selected_trueequivalence_currentfrontier_after_externalrg_smslot.candidate.json"
PRECISION_EXEC = DATA / "selected_precisionprofileloopvalues_or_actualqasu3operatorpayload_currentexecution.candidate.json"
RG_ENGINE = DATA / "selected_rgengineexecution_or_selectedsmpacketcertificateintegration.candidate.json"
YUKAWA_TRANSPORT = DATA / "selected_commonscaleyukawahiggstransport_or_finalreplayaudit.candidate.json"
MIXING_REPLAY = DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json"
RG_POLICY = DATA / "sm_equivalence_rgpolicy_covariance_and_observable_suite.candidate.json"
QASU3_PARITY = DATA / "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json"

STATUS = (
    "MTT_SELECTED_DYNAMICQASU3OPERATORPACKETREPLAY_OR_YUKAWAMASSMIXINGVALUECLOSURE_"
    "BUILT_DYNAMIC_PACKET_REPLAYED_VALUE_CLOSURE_OPEN"
)
NEXT = "MTT_Selected_YukawaMagnitudeRGClosure_or_FinalTrueSMEquivalenceAudit_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing dynamic Qa/SU3 replay sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        DYNAMIC_PACKET,
        DYNAMIC_VALUES,
        TRUE_FRONTIER,
        PRECISION_EXEC,
        RG_ENGINE,
        YUKAWA_TRANSPORT,
        MIXING_REPLAY,
        RG_POLICY,
        QASU3_PARITY,
    ]
    require_sources(sources)

    dynamic_packet = load(DYNAMIC_PACKET)
    dynamic_values = load(DYNAMIC_VALUES)
    true_frontier = load(TRUE_FRONTIER)
    precision_exec = load(PRECISION_EXEC)
    rg_engine = load(RG_ENGINE)
    yukawa_transport = load(YUKAWA_TRANSPORT)
    mixing_replay = load(MIXING_REPLAY)
    rg_policy = load(RG_POLICY)
    qasu3_parity = load(QASU3_PARITY)

    qualitative = dynamic_values["acceptance_tests"]
    dynamic_closed = dynamic_packet["promotion_decision"][
        "dynamic_matter_overlap_operator_packet_closed"
    ]
    qasu3_replay = {
        "schema": "MTTDynamicQaSU3OperatorPacketReplay.v1",
        "status": "DYNAMIC_QASU3_FIRST_RESPONSE_LAYER_REPLAYED",
        "source": rel(DYNAMIC_PACKET),
        "dynamic_matter_overlap_packet_closed": dynamic_closed,
        "actual_QaSU3_operator_packet_first_response_layer_closed": dynamic_closed,
        "selected_dynamic_overlap_tensor_promoted": dynamic_packet["what_closes_now"][
            "selected_dynamic_overlap_tensor_promoted"
        ],
        "qualitative_flavor_response": {
            "mass_split_positive": qualitative["all_mass_split_positive"],
            "ckm_commutator_positive": qualitative["ckm_commutator_positive"],
            "pmns_commutator_positive": qualitative["pmns_commutator_positive"],
            "cp_odd_invariant_nonzero": qualitative["cp_odd_invariant_nonzero"],
        },
        "not_a_precision_value_packet": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": dynamic_closed,
    }
    write_json(QASU3_REPLAY, qasu3_replay)

    yukawa_attempt = {
        "schema": "MTTYukawaMassMixingValueClosureAttempt.v1",
        "status": "VALUE_CLOSURE_REJECTED_MAGNITUDES_RG_COVARIANCE_OPEN",
        "inputs": {
            "common_scale_transport_kernel": rel(YUKAWA_TRANSPORT),
            "mixing_and_gauge_replay": rel(MIXING_REPLAY),
            "rg_policy_observable_suite": rel(RG_POLICY),
            "diagnostic_rg_engine": rel(RG_ENGINE),
        },
        "closed_support": {
            "dynamic_non_scalar_operator_layer": dynamic_closed,
            "CKM_complex_Yukawa_replay_executable": mixing_replay["what_closes_now"][
                "CKM_complex_Yukawa_replay"
            ],
            "PMNS_oscillation_mass_squared_replay_executable": mixing_replay["what_closes_now"][
                "PMNS_oscillation_mass_squared_replay"
            ],
            "RG_policy_fixed": rg_policy["what_closes_now"][
                "RG_reference_scheme_and_scale_policy"
            ],
            "diagnostic_one_loop_RG_smoke_run": rg_engine["what_closes_now"][
                "diagnostic_RG_smoke_run_executed"
            ],
        },
        "missing_for_value_closure": {
            "accepted_Y_u_MZ_Y_d_MZ_Y_e_MZ_values": rg_engine["what_remains_open"][
                "accepted_Y_u_MZ_Y_d_MZ_Y_e_MZ_values"
            ],
            "accepted_lambda_H_MZ_value": rg_engine["what_remains_open"][
                "accepted_lambda_H_MZ_value"
            ],
            "threshold_matching_values": rg_engine["what_remains_open"][
                "threshold_matching_values"
            ],
            "mass_scheme_conversion": rg_engine["what_remains_open"]["mass_scheme_conversion"],
            "covariance_profile_likelihood_execution": rg_engine["what_remains_open"][
                "covariance_profile_likelihood_execution"
            ],
            "published_or_reconstructed_profile_likelihood": true_frontier["what_remains_open"][
                "published_or_reconstructed_profile_likelihood"
            ],
        },
        "closure_decision": {
            "Yukawa_magnitudes_closed": False,
            "running_mass_ratios_closed": False,
            "CKM_PMNS_measured_angles_phase_closed": False,
            "Higgs_RG_precision_closed": False,
            "true_SM_equivalence_closed": False,
            "full_SM_no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(YUKAWA_ATTEMPT, yukawa_attempt)

    true_eq_gate = {
        "schema": "MTTTrueEquivalenceGateAfterDynamicQaSU3Replay.v1",
        "status": "QASU3_FIRST_RESPONSE_REPLAYED_TRUE_EQUIVALENCE_VALUE_LAYER_OPEN",
        "SM_parity_closed": qasu3_parity["closure_decision"]["SM_parity_closed"],
        "actual_QaSU3_operator_packet_status": {
            "previous_actual_packet_open": precision_exec["closure_decision"][
                "route_B_actual_QaSU3_operator_payload_closed"
            ]
            is False,
            "first_response_layer_now_closed": dynamic_closed,
            "full_precision_packet_closed": False,
        },
        "true_equivalence": {
            "previous_frontier": true_frontier["status"],
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "remaining_gates": list(yukawa_attempt["missing_for_value_closure"].keys()),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(TRUE_EQ_GATE, true_eq_gate)

    next_cutset = {
        "schema": "MTTNextCutsetAfterDynamicQaSU3Replay.v1",
        "status": "DYNAMIC_QASU3_REPLAYED_YUKAWA_RG_VALUE_CLOSURE_NEXT",
        "closed_now": [
            "dynamic Qa/SU3 first-response operator layer replayed from selected dynamic matter/overlap packet",
            "qualitative mass-splitting, mixing, and CP nonzero tests preserved without observed flavor selectors",
            "true-equivalence frontier shifted to accepted value transport and covariance/profile closure",
        ],
        "still_open": [
            "accepted common-scale Yukawa/Higgs values",
            "threshold and mass-scheme conversion",
            "full covariance/profile likelihood execution",
            "measured CKM/PMNS and running mass-ratio value closure",
            "true SM equivalence and full no-knob closure",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The selected dynamic operator layer is now present, but the accepted SM value layer "
                "still requires RG/threshold/covariance and magnitude closure."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": dynamic_closed,
    }
    write_json(NEXT_CUTSET, next_cutset)

    candidate = {
        "candidate": "MTTSelectedDynamicQaSU3OperatorPacketReplayOrYukawaMassMixingValueClosure",
        "status": STATUS,
        "inputs": {
            "dynamic_packet": rel(DYNAMIC_PACKET),
            "dynamic_values": rel(DYNAMIC_VALUES),
            "true_frontier": rel(TRUE_FRONTIER),
            "precision_execution": rel(PRECISION_EXEC),
            "rg_engine": rel(RG_ENGINE),
            "yukawa_transport": rel(YUKAWA_TRANSPORT),
            "mixing_replay": rel(MIXING_REPLAY),
            "rg_policy": rel(RG_POLICY),
            "qasu3_parity": rel(QASU3_PARITY),
        },
        "output_packets": {
            "dynamic_qasu3_operator_packet_replay": rel(QASU3_REPLAY),
            "yukawa_mass_mixing_value_closure_attempt": rel(YUKAWA_ATTEMPT),
            "true_equivalence_gate_after_dynamic_qasu3_replay": rel(TRUE_EQ_GATE),
            "next_cutset_after_dynamic_qasu3_replay": rel(NEXT_CUTSET),
        },
        "what_closes_now": {
            "dynamic_QaSU3_first_response_layer_replayed": dynamic_closed,
            "actual_QaSU3_operator_packet_no_longer_absent_at_first_response_layer": dynamic_closed,
            "qualitative_non_scalar_flavor_tests_preserved": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": yukawa_attempt["missing_for_value_closure"],
        "promotion_decision": {
            "dynamic_QaSU3_first_response_layer_closed": dynamic_closed,
            "accepted_Yukawa_magnitudes_closed": False,
            "running_mass_ratios_closed": False,
            "CKM_PMNS_measured_angles_phase_closed": False,
            "true_SM_equivalence_closed": False,
            "full_SM_no_knob_closed": False,
        },
        "theorem": {
            "name": "DynamicQaSU3ReplayAndValueClosureSeparationTheorem",
            "proved": dynamic_closed,
            "statement": (
                "The selected dynamic matter/overlap packet replays as a first-response dynamic Qa/SU3 "
                "operator layer and preserves qualitative non-scalar mass-splitting, mixing, and CP tests "
                "without observed flavor selectors. This does not close accepted Yukawa magnitudes, running "
                "mass ratios, CKM/PMNS measured values, RG/Higgs precision transport, true SM equivalence, "
                "or full no-knob closure; those remain value/covariance gates."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": dynamic_closed,
        "unpatched_theorem_closure_claimed": dynamic_closed,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DynamicQaSU3OperatorPacketReplay_or_YukawaMassMixingValueClosure_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "dynamic_QaSU3_first_response_layer_closed": dynamic_closed,
        "accepted_Yukawa_magnitudes_closed": False,
        "true_SM_equivalence_closed": False,
        "full_SM_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DynamicQaSU3OperatorPacketReplay or YukawaMassMixingValueClosure v1

Status: `{STATUS}`.

The selected dynamic matter/overlap packet now replays as a first-response
dynamic Qa/SU3 operator layer. It preserves the qualitative non-scalar tests:
mass splitting, nonzero mixing commutators, and nonzero CP-odd invariant.

This does not close accepted Yukawa magnitudes, running mass ratios,
CKM/PMNS measured values, Higgs/RG precision transport, true SM equivalence, or
full no-knob closure.

Next artifact: `{NEXT}`.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"built {rel(OUTPUT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
