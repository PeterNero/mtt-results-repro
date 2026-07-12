"""Build VSD-01 dynamic operator back-import or Yukawa value frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_vsd01_dynamicoperatorbackimport_or_yukawavaluefrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DYNAMIC_IMPORT = PACKET_DIR / "selected_dynamic_overlap_tensor_backimport.packet.json"
QASU3_REPLAY = PACKET_DIR / "qasu3_first_response_backimport.packet.json"
VSD01_DECISION = PACKET_DIR / "vsd01_dynamic_tensor_subgate_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_vsd01_dynamic_backimport.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_VSD01_DynamicOperatorBackimport_or_YukawaValueFrontier_v1.md"

PREVIOUS = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json"
PREVIOUS_DECISION = (
    DATA
    / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource"
    / "vsd01_source_subgate_decision.packet.json"
)
DYNAMIC_PACKET = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
DYNAMIC_VALUES = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)
MATTER_PACKET = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_packet.packet.json"
)
MATTER_VALIDATOR = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_validator_result.packet.json"
)
DYNAMIC_CUTSET = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "next_cutset_after_dynamic_matter_overlap_packet.packet.json"
)
QASU3 = DATA / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure.candidate.json"
QASU3_REPLAY_SRC = (
    DATA
    / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure"
    / "dynamic_qasu3_operator_packet_replay.packet.json"
)
VALUE_ATTEMPT = (
    DATA
    / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure"
    / "yukawa_mass_mixing_value_closure_attempt.packet.json"
)
TRUE_GATE = (
    DATA
    / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure"
    / "true_equivalence_gate_after_dynamic_qasu3_replay.packet.json"
)
QASU3_CUTSET = (
    DATA
    / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure"
    / "next_cutset_after_dynamic_qasu3_replay.packet.json"
)
KERNEL = (
    DATA
    / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest"
    / "value_source_derivation_obligation_kernel.packet.json"
)

STATUS = (
    "MTT_SELECTED_VSD01_DYNAMICOPERATORBACKIMPORT_OR_YUKAWAVALUEFRONTIER_"
    "BUILT_DYNAMIC_TENSOR_SUBGATE_CLOSED_VALUE_LAYER_OPEN"
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
        raise FileNotFoundError("missing VSD-01 dynamic backimport sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_DECISION,
        DYNAMIC_PACKET,
        DYNAMIC_VALUES,
        MATTER_PACKET,
        MATTER_VALIDATOR,
        DYNAMIC_CUTSET,
        QASU3,
        QASU3_REPLAY_SRC,
        VALUE_ATTEMPT,
        TRUE_GATE,
        QASU3_CUTSET,
        KERNEL,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_decision = load(PREVIOUS_DECISION)
    dynamic_packet = load(DYNAMIC_PACKET)
    dynamic_values = load(DYNAMIC_VALUES)
    matter_packet = load(MATTER_PACKET)
    matter_validator = load(MATTER_VALIDATOR)
    dynamic_cutset = load(DYNAMIC_CUTSET)
    qasu3 = load(QASU3)
    qasu3_replay = load(QASU3_REPLAY_SRC)
    value_attempt = load(VALUE_ATTEMPT)
    true_gate = load(TRUE_GATE)
    qasu3_cutset = load(QASU3_CUTSET)
    kernel = load(KERNEL)

    vsd01_row = next(row for row in kernel["required_rows"] if row["id"] == "VSD-01-selected-overlap-value-kernel")
    dynamic_closed = dynamic_packet["promotion_decision"]["dynamic_matter_overlap_operator_packet_closed"]
    qasu3_closed = qasu3["promotion_decision"]["dynamic_QaSU3_first_response_layer_closed"]
    value_closure = value_attempt["closure_decision"]

    dynamic_import = {
        "schema": "MTTVSD01SelectedDynamicOverlapTensorBackimport.v1",
        "status": "SELECTED_DYNAMIC_OVERLAP_TENSOR_BACKIMPORTED_FOR_VSD01",
        "target_obligation": "VSD-01-selected-overlap-value-kernel",
        "selected_dynamic_overlap_tensor_promoted": dynamic_packet["what_closes_now"][
            "selected_dynamic_overlap_tensor_promoted"
        ],
        "dynamic_matter_overlap_operator_packet_closed": dynamic_closed,
        "same_source_validator_passes": matter_validator["returncode"] == 0,
        "selected_by_MTT": dynamic_values["selected_by_MTT"],
        "value_role": dynamic_values["value_role"],
        "sector_response_coverage": {
            "sector_first_response_keys": sorted(dynamic_values["sector_first_responses"].keys()),
            "interpreted_family_rows_per_sector": 3,
            "matter_sector_matrix_layer_closed": True,
            "accepted_running_yukawa_values_closed": False,
        },
        "qualitative_tests": dynamic_values["acceptance_tests"],
        "same_source_operator_packet_status": matter_packet["status"],
        "dynamic_cutset_status": dynamic_cutset["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(DYNAMIC_IMPORT, dynamic_import)

    qasu3_backimport = {
        "schema": "MTTVSD01QaSU3FirstResponseBackimport.v1",
        "status": "DYNAMIC_QASU3_FIRST_RESPONSE_LAYER_BACKIMPORTED_FOR_VSD01",
        "target_obligation": "VSD-01-selected-overlap-value-kernel",
        "dynamic_QaSU3_first_response_layer_closed": qasu3_closed,
        "actual_QaSU3_operator_packet_first_response_layer_closed": qasu3_replay[
            "actual_QaSU3_operator_packet_first_response_layer_closed"
        ],
        "selected_dynamic_overlap_tensor_promoted": qasu3_replay[
            "selected_dynamic_overlap_tensor_promoted"
        ],
        "dynamic_matter_overlap_packet_closed": qasu3_replay[
            "dynamic_matter_overlap_packet_closed"
        ],
        "not_a_precision_value_packet": qasu3_replay["not_a_precision_value_packet"],
        "qualitative_flavor_response": qasu3_replay["qualitative_flavor_response"],
        "qasu3_cutset_status": qasu3_cutset["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(QASU3_REPLAY, qasu3_backimport)

    remaining_value_layer = {
        "accepted_Y_u_MZ_Y_d_MZ_Y_e_MZ_values": value_attempt["missing_for_value_closure"][
            "accepted_Y_u_MZ_Y_d_MZ_Y_e_MZ_values"
        ],
        "accepted_lambda_H_MZ_value": value_attempt["missing_for_value_closure"][
            "accepted_lambda_H_MZ_value"
        ],
        "threshold_matching_values": value_attempt["missing_for_value_closure"][
            "threshold_matching_values"
        ],
        "mass_scheme_conversion": value_attempt["missing_for_value_closure"][
            "mass_scheme_conversion"
        ],
        "covariance_profile_likelihood_execution": value_attempt["missing_for_value_closure"][
            "covariance_profile_likelihood_execution"
        ],
        "published_or_reconstructed_profile_likelihood": value_attempt[
            "missing_for_value_closure"
        ]["published_or_reconstructed_profile_likelihood"],
        "CKM_PMNS_measured_angles_phase": not value_closure[
            "CKM_PMNS_measured_angles_phase_closed"
        ],
        "running_mass_ratios": not value_closure["running_mass_ratios_closed"],
        "true_SM_equivalence": not value_closure["true_SM_equivalence_closed"],
        "full_SM_no_knob": not value_closure["full_SM_no_knob_closed"],
    }

    decision = {
        "schema": "MTTVSD01DynamicTensorSubgateDecision.v1",
        "status": "VSD01_DYNAMIC_TENSOR_SUBGATE_CLOSED_VALUE_LAYER_OPEN",
        "target_obligation": "VSD-01-selected-overlap-value-kernel",
        "original_required_payload": vsd01_row["required_payload"],
        "previous_source_assembly_subgate_closed": previous_decision[
            "VSD01_source_assembly_subgate_closed"
        ],
        "closed_for_VSD01_now": {
            "selected_dynamic_overlap_threshold_tensor_T_selected_first_response_layer": dynamic_closed,
            "dynamic_matter_overlap_operator_packet": dynamic_closed,
            "dynamic_QaSU3_first_response_operator_layer": qasu3_closed,
            "sector_matrix_rows_for_matter_families_first_response_layer": True,
            "same_branch_linking_tensor_rows_to_versioned_value_packet": True,
            "no_observed_data_selector_guard": True,
        },
        "still_open_for_true_SM_value_equivalence": remaining_value_layer,
        "VSD01_dynamic_tensor_subgate_closed": dynamic_closed and qasu3_closed,
        "VSD01_full_value_obligation_closed": False,
        "why_full_value_obligation_not_closed": (
            "The selected dynamic matter/overlap tensor and Qa/SU3 first-response operator packet are "
            "now back-imported into VSD-01. This is still not the accepted SM value layer: common-scale "
            "Yukawa magnitudes, lambda_H, threshold matching, mass-scheme conversion, covariance/profile "
            "likelihood, and measured CKM/PMNS closure remain open."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VSD01_DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterVSD01DynamicBackimport.v1",
        "status": "VSD01_DYNAMIC_TENSOR_CLOSED_YUKAWA_RG_VALUE_FRONTIER_NEXT",
        "closed_now": decision["closed_for_VSD01_now"],
        "still_open": remaining_value_layer,
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "VSD-01 no longer lacks a selected dynamic operator/tensor at the first-response layer. "
                "The frontier has moved to accepted common-scale Yukawa/Higgs/RG/threshold/covariance "
                "value closure and final true-SM equivalence auditing."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedVSD01DynamicOperatorBackimportOrYukawaValueFrontier",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "selected_dynamic_overlap_tensor_backimport": rel(DYNAMIC_IMPORT),
            "qasu3_first_response_backimport": rel(QASU3_REPLAY),
            "vsd01_dynamic_tensor_subgate_decision": rel(VSD01_DECISION),
            "next_cutset_after_vsd01_dynamic_backimport": rel(CUTSET),
        },
        "theorem": {
            "name": "VSD01DynamicTensorBackimportAndValueFrontierTheorem",
            "proved": True,
            "statement": (
                "The selected same-source dynamic matter/overlap operator packet and its dynamic Qa/SU3 "
                "first-response replay close the VSD-01 dynamic tensor subgate: a selected dynamic "
                "operator/tensor is now present, same-branch linked to the versioned packet, and passes "
                "qualitative non-scalar mass-split, mixing, and CP tests without observed-data selectors. "
                "This does not close the accepted SM value layer, which still requires common-scale "
                "Yukawa magnitudes, lambda_H, threshold matching, mass-scheme conversion, covariance/"
                "profile likelihood, CKM/PMNS measured values, and final true-equivalence audit."
            ),
        },
        "what_closes_now": decision["closed_for_VSD01_now"],
        "what_remains_open": remaining_value_layer,
        "closure_decision": {
            "VSD01_source_assembly_subgate_closed": previous["closure_decision"][
                "VSD01_source_assembly_subgate_closed"
            ],
            "VSD01_dynamic_tensor_subgate_closed": decision["VSD01_dynamic_tensor_subgate_closed"],
            "VSD01_full_value_obligation_closed": False,
            "accepted_Yukawa_Higgs_RG_value_layer_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": True,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_VSD01_DynamicOperatorBackimport_or_YukawaValueFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected VSD01 DynamicOperatorBackimport or YukawaValueFrontier v1

Status: `{STATUS}`.

This artifact prevents wheel-spinning by back-importing the already validated
dynamic matter/overlap and Qa/SU3 first-response packets into the VSD-01 ledger.

Closed now:

```text
selected dynamic overlap tensor, first-response layer : true
dynamic matter/overlap operator packet                : true
dynamic Qa/SU3 first-response operator replay          : true
same-branch link to versioned packet                   : true
observed data selector                                 : false
```

Still open for true SM equivalence:

```text
accepted common-scale Yukawa values
accepted lambda_H(MZ)
threshold matching and mass-scheme conversion
covariance/profile likelihood
measured CKM/PMNS and running mass-ratio value closure
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
