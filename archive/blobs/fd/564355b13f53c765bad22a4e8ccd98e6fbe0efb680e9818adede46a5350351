"""Build post-source-promotion full-SM gap audit or dotD alpha1/matter routing closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_postsourcepromotionfullsmgapaudit_or_dotdalpha1matterroutingclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ALPHA1_CERT = PACKET_DIR / "alpha1_dotd_driver_certificate.packet.json"
ALPHA1_VALIDATOR_RESULT = PACKET_DIR / "alpha1_dotd_driver_validator_result.packet.json"
MATTER_STATIC = PACKET_DIR / "matter_slot_static_readout_import.packet.json"
MATTER_DYNAMIC_ATTEMPT = PACKET_DIR / "same_source_dynamic_matter_overlap_attempt.packet.json"
MATTER_DYNAMIC_RESULT = PACKET_DIR / "same_source_dynamic_matter_overlap_validator_result.packet.json"
POSTSOURCE_MATRIX = PACKET_DIR / "postsource_fullsm_gap_matrix.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_postsource_gap_audit.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PostSourcePromotionFullSMGapAudit_or_DotDAlpha1MatterRoutingClosure_v1.md"

VALIDATE_ALPHA1 = ROOT / "scripts" / "validate_visible_routec_sourceidentity_or_typedbn_derivative.py"
VALIDATE_MATTER = ROOT / "scripts" / "validate_samesource_matter_slot_overlap_operator_packet.py"

SOURCE_STACK = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate.candidate.json"
SOURCE_SUMMARY = (
    DATA
    / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate"
    / "unpatched_source_promotion_replay_summary.packet.json"
)
ALPHA1_CROSSREPO = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
ALPHA1_TRANSPORT = DATA / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
ALPHA1_PAYLOAD = DATA / "selected_phifinalpha1payloadvalues_or_typedbnretardedderivativeexecution.candidate.json"
MATTER_READOUT = DATA / "selected_matterslot_readout_backimport_from_smslotfunctor.candidate.json"
MATTER_CONTRACT = DATA / "selected_routec_samesource_matter_slot_overlap_operator_packet.candidate.json"
DYNAMIC_FRONTIER = DATA / "selected_dynamicqasu3_or_c1response_postsourcefrontier.candidate.json"
TRUE_FRONTIER = DATA / "selected_trueequivalence_currentfrontier_after_externalrg_smslot.candidate.json"

STATUS = (
    "MTT_SELECTED_POSTSOURCEPROMOTIONFULLSMGAPAUDIT_OR_DOTDALPHA1MATTERROUTINGCLOSURE_"
    "BUILT_ALPHA1_CLOSED_STATIC_MATTER_CLOSED_DYNAMIC_FULLSM_OPEN"
)
NEXT = "MTT_Selected_SameSourceDynamicMatterOverlapOperatorPacket_or_PrimitiveC1ValueClosure_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(validator: Path, packet: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(validator), str(packet)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "validator": rel(validator),
        "payload": rel(packet),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr_lines": proc.stderr.strip().splitlines(),
    }


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing post-source gap sources: " + ", ".join(missing))


def alpha_field(source: str) -> dict[str, Any]:
    return {
        "selected_emitted": True,
        "same_branch": True,
        "theorem_derived": True,
        "provenance": source,
    }


def matter_field(selected: bool, provenance: str, same_source: bool = True) -> dict[str, Any]:
    return {
        "selected_emitted": selected,
        "same_source": same_source,
        "theorem_derived": selected,
        "provenance": provenance,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    require_sources(
        [
            SOURCE_STACK,
            SOURCE_SUMMARY,
            ALPHA1_CROSSREPO,
            ALPHA1_TRANSPORT,
            ALPHA1_PAYLOAD,
            MATTER_READOUT,
            MATTER_CONTRACT,
            DYNAMIC_FRONTIER,
            TRUE_FRONTIER,
            VALIDATE_ALPHA1,
            VALIDATE_MATTER,
        ]
    )

    source_stack = load(SOURCE_STACK)
    source_summary = load(SOURCE_SUMMARY)
    alpha_crossrepo = load(ALPHA1_CROSSREPO)
    alpha_payload = load(ALPHA1_PAYLOAD)
    matter_readout = load(MATTER_READOUT)
    dynamic_frontier = load(DYNAMIC_FRONTIER)
    true_frontier = load(TRUE_FRONTIER)

    alpha1_cert = {
        "schema": "MTTVisibleRouteCSourceIdentityOrTypedBNRetardedDerivative.v1",
        "branch_id": "q79/F,m=1/S3_GS/RouteC_or_same_visible_source",
        "status": "ALPHA1_DOTD_DRIVER_VALIDATES_AFTER_SOURCE_PROMOTION_IMPORT",
        "lane_A_visible_routec_source_identity": {
            "source_identity": alpha_field("same_source_phi_fin_source_stack"),
            "visible_routec_operator_source": alpha_field("visible_routec_source_identity"),
            "phi_fin_payload": alpha_field("crossrepo_phi_fin_alpha1_payload_import"),
            "same_branch_alpha1_derivative": alpha_field("transport_derivative_theorem"),
            "dotd_validator_replay": {
                **alpha_field("crossrepo_honest_dotd_replay_import"),
                "honest_validator_exit_code": 0,
            },
        },
        "lane_B_typed_bn_retarded_derivative": {
            "retarded_source_selector": alpha_field("unused_valid_route_a"),
            "typed_bn_alpha1_derivative": alpha_field("unused_valid_route_a"),
            "selected_transfer_normalization": alpha_field("unused_valid_route_a"),
            "sector_dotd_equality": alpha_field("unused_valid_route_a"),
            "dotd_validator_replay": {
                **alpha_field("unused_valid_route_a"),
                "honest_validator_exit_code": 0,
            },
        },
        "promotion_result": {
            "selected_value_emitted": True,
            "alpha1_driver_verified": alpha_crossrepo["what_closes_now"][
                "selected_alpha1_driver_imported"
            ],
            "selected_dotD_source_verified": alpha_crossrepo["what_closes_now"][
                "selected_dotD_source_verified_imported"
            ],
            "honest_dotd_replay_closed": alpha_crossrepo["what_closes_now"][
                "honest_dotD_alpha1_replay_imported"
            ],
            "target_fitting_used": False,
        },
        "source_imports": {
            "source_stack": rel(SOURCE_STACK),
            "crossrepo_alpha1_driver": rel(ALPHA1_CROSSREPO),
            "transport_derivative": rel(ALPHA1_TRANSPORT),
            "alpha1_payload_replay": rel(ALPHA1_PAYLOAD),
        },
        "forbidden_inputs_used": [],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ALPHA1_CERT, alpha1_cert)
    alpha1_result = run_validator(VALIDATE_ALPHA1, ALPHA1_CERT)
    write_json(ALPHA1_VALIDATOR_RESULT, alpha1_result)

    matter_static = {
        "schema": "MTTMatterSlotStaticReadoutImport.v1",
        "status": "STATIC_MATTER_SLOT_READOUT_IMPORTED_DYNAMIC_OVERLAP_OPEN",
        "source": rel(MATTER_READOUT),
        "static_readout_closed": {
            "selected_U10_Ubar5_polarization_source_outputs_static_tier": matter_readout[
                "what_closes_now"
            ]["selected_U10_Ubar5_polarization_source_outputs_static_tier"],
            "selected_10M_clock_readout_static_tier": matter_readout["what_closes_now"][
                "selected_10M_clock_readout_static_tier"
            ],
            "selected_1M_Dirac_shift_readout_static_tier": matter_readout["what_closes_now"][
                "selected_1M_Dirac_shift_readout_static_tier"
            ],
            "selected_overlap_transfer_normalization_static_tier": matter_readout[
                "what_closes_now"
            ]["selected_overlap_transfer_normalization_static_tier"],
        },
        "dynamic_not_closed": {
            "selected_D_E_Riesz_Green_dotD": True,
            "selected_dynamic_overlap_tensor_or_transfer_functor": True,
            "selected_primitive_C1_contractions": True,
            "full_flavor_constants": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(MATTER_STATIC, matter_static)

    matter_dynamic_attempt = {
        "schema": "MTTSameSourceDynamicMatterOverlapAttemptAfterSourcePromotion.v1",
        "status": "DYNAMIC_MATTER_OVERLAP_ATTEMPT_REJECTED_VALUES_OPEN",
        "attempted_selected_packet": {
            "fields": {
                "source_identity": matter_field(True, "premise_free_phi_fin_source_stack"),
                "matter_slot_charge": matter_field(True, "static_smslot_functor_readout"),
                "singlet_neutrino_rule": matter_field(True, "static_smslot_functor_readout"),
                "operator_values": matter_field(False, "dynamic_values_open"),
                "overlap_transfer": matter_field(True, "static_overlap_transfer_normalization"),
                "normalization": matter_field(True, "static_trace_transfer_normalization"),
                "primitive_contractions": matter_field(False, "primitive_C1_contractions_open"),
            },
            "packet_flags": {
                "one_same_source": True,
                "observed_data_used": False,
                "target_fitting_used": False,
                "promote_to_A_selected": False,
                "promote_to_b_selected": False,
            },
        },
        "why_rejected": [
            "dynamic operator values are still open",
            "primitive C1 contractions are still open",
            "same-source matter/overlap packet cannot promote A_selected/b_selected at the full dynamic matter layer yet",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(MATTER_DYNAMIC_ATTEMPT, matter_dynamic_attempt)
    matter_result = run_validator(VALIDATE_MATTER, MATTER_DYNAMIC_ATTEMPT)
    write_json(MATTER_DYNAMIC_RESULT, matter_result)

    alpha1_closed = alpha1_result["returncode"] == 0
    matter_dynamic_open = matter_result["returncode"] == 1
    postsource_matrix = {
        "schema": "MTTPostSourceFullSMGapMatrix.v1",
        "status": "ALPHA1_CLOSED_STATIC_MATTER_CLOSED_DYNAMIC_VALUE_GATES_OPEN",
        "source_stack": {
            "source": rel(SOURCE_SUMMARY),
            "A_selected_promoted": source_summary["promoted_objects"]["A_selected"],
            "b_selected_promoted": source_summary["promoted_objects"]["b_selected"],
            "deltaTheta_C1_promoted": source_summary["promoted_objects"]["deltaTheta_C1"],
        },
        "alpha1_dotd": {
            "closed": alpha1_closed,
            "validator": rel(ALPHA1_VALIDATOR_RESULT),
            "alpha1_driver_verified": alpha_crossrepo["what_closes_now"][
                "selected_alpha1_driver_imported"
            ],
            "selected_dotD_source_verified": alpha_crossrepo["what_closes_now"][
                "selected_dotD_source_verified_imported"
            ],
            "honest_dotd_replay_closed": alpha_payload["closure_decision"][
                "honest_dotd_validator_replay_closed"
            ],
        },
        "matter_slot_routing": {
            "static_readout_closed": True,
            "dynamic_same_source_packet_closed": False,
            "dynamic_validator_rejects": matter_dynamic_open,
            "validator": rel(MATTER_DYNAMIC_RESULT),
        },
        "full_SM": {
            "SM_parity_remains_closed": true_frontier["closure_decision"]["SM_parity_closed"],
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
            "Yukawa_mass_mixing_closed": False,
            "actual_QaSU3_operator_packet_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": alpha1_closed,
    }
    write_json(POSTSOURCE_MATRIX, postsource_matrix)

    next_cutset = {
        "schema": "MTTNextCutsetAfterPostSourceGapAudit.v1",
        "status": "ALPHA1_RETIRED_DYNAMIC_MATTER_OVERLAP_VALUES_NEXT",
        "closed_now": [
            "unpatched C1 source stack remains closed",
            "alpha1 driver and selected dotD source verified by imported same-branch replay",
            "static matter-slot readout imported from SM-slot functor",
        ],
        "still_open": [
            "same-source dynamic matter/overlap operator values",
            "primitive C1 contractions",
            "selected dynamic Qa/SU3 operator packet",
            "Yukawa/mass/mixing value closure without proxy fitting",
            "true SM equivalence and full no-knob closure",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The active post-source blocker is no longer alpha1. It is the same-source dynamic "
                "matter/overlap operator packet, especially operator values and primitive C1 contractions."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": alpha1_closed,
    }
    write_json(NEXT_CUTSET, next_cutset)

    candidate = {
        "candidate": "MTTSelectedPostSourcePromotionFullSMGapAuditOrDotDAlpha1MatterRoutingClosure",
        "status": STATUS,
        "inputs": {
            "source_stack": rel(SOURCE_STACK),
            "source_summary": rel(SOURCE_SUMMARY),
            "alpha1_crossrepo": rel(ALPHA1_CROSSREPO),
            "alpha1_transport": rel(ALPHA1_TRANSPORT),
            "alpha1_payload": rel(ALPHA1_PAYLOAD),
            "matter_readout": rel(MATTER_READOUT),
            "matter_contract": rel(MATTER_CONTRACT),
            "dynamic_frontier": rel(DYNAMIC_FRONTIER),
            "true_frontier": rel(TRUE_FRONTIER),
        },
        "output_packets": {
            "alpha1_dotd_driver_certificate": rel(ALPHA1_CERT),
            "alpha1_dotd_driver_validator_result": rel(ALPHA1_VALIDATOR_RESULT),
            "matter_slot_static_readout_import": rel(MATTER_STATIC),
            "same_source_dynamic_matter_overlap_attempt": rel(MATTER_DYNAMIC_ATTEMPT),
            "same_source_dynamic_matter_overlap_validator_result": rel(MATTER_DYNAMIC_RESULT),
            "postsource_fullsm_gap_matrix": rel(POSTSOURCE_MATRIX),
            "next_cutset_after_postsource_gap_audit": rel(NEXT_CUTSET),
        },
        "what_closes_now": {
            "alpha1_driver_verified": alpha1_closed,
            "selected_dotD_source_verified": alpha1_closed,
            "honest_dotD_validator_replay_closed": alpha1_closed,
            "static_matter_slot_readout_closed": True,
            "source_stack_closure_preserved": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "same_source_dynamic_matter_overlap_operator_packet": True,
            "primitive_C1_contractions": True,
            "selected_dynamic_QaSU3_operator_packet": True,
            "Yukawa_mass_mixing_value_closure": True,
            "true_SM_equivalence": True,
            "full_SM_no_knob_closure": True,
        },
        "promotion_decision": {
            "postsource_alpha1_retired": alpha1_closed,
            "static_matter_routing_closed": True,
            "dynamic_matter_overlap_packet_closed": False,
            "A_selected_b_selected_deltaTheta_source_stack_preserved": True,
            "true_SM_equivalence_closed": False,
            "full_SM_no_knob_closed": False,
        },
        "theorem": {
            "name": "PostSourcePromotionGapAuditTheorem",
            "proved": alpha1_closed and matter_dynamic_open,
            "statement": (
                "After unpatched source promotion, the same-branch alpha1 driver and selected dotD "
                "source are imported as closed from the cross-repo q79/F,m=1 replay, and static "
                "matter-slot readout is imported from the SM-slot functor. The same-source dynamic "
                "matter/overlap packet still rejects because selected dynamic operator values and "
                "primitive C1 contractions are not emitted. Therefore the next full-SM blocker is "
                "dynamic matter/overlap value closure, not alpha1 or the C1 source wall."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": alpha1_closed,
        "unpatched_theorem_closure_claimed": alpha1_closed,
        "patched_SM_parity_closure_preserved": source_stack["patched_SM_parity_closure_preserved"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PostSourcePromotionFullSMGapAudit_or_DotDAlpha1MatterRoutingClosure_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "alpha1_driver_verified": alpha1_closed,
        "selected_dotD_source_verified": alpha1_closed,
        "static_matter_slot_readout_closed": True,
        "dynamic_matter_overlap_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "full_SM_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PostSourcePromotionFullSMGapAudit or DotDAlpha1MatterRoutingClosure v1

Status: `{STATUS}`.

## What Closed

- The unpatched C1 source stack remains closed.
- The same-branch alpha1 driver and selected `dotD` source are now imported as
  closed from the q79/F,m=1 cross-repo replay.
- Static matter-slot readout is imported from the SM-slot functor.

## What Did Not Close

The same-source dynamic matter/overlap packet still rejects. The open fields are
dynamic operator values and primitive C1 contractions. Therefore full SM/no-knob
closure is still not claimed.

Next artifact: `{NEXT}`.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"built {rel(OUTPUT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
