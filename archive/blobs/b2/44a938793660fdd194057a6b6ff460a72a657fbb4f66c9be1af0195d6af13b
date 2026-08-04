"""Import the selected SM-slot functor overlap-kernel source emission."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = CERTS / "operatorlevel_rhoe_bn_fill_cutset_matter_overlap_import_certificate.json"
SM_PACKET = SM / "candidate_data" / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"
SM_CERT = SM / "certificates" / "selected_smslotfunctor_overlapkernel_source_emission_certificate.json"

OUTPUT_PACKET = DATA / "smslotfunctor_overlapkernel_source_emission_import.candidate.json"
OUTPUT_CERT = CERTS / "smslotfunctor_overlapkernel_source_emission_import_certificate.json"
OUTPUT_NOTE = CORPUS / "SMSlotFunctor_OverlapKernel_SourceEmission_Import_v1.md"

STATUS = "SMSLOTFUNCTOR_OVERLAPKERNEL_SOURCE_PACKET_IMPORTED_DOWNSTREAM_OPERATOR_PAYLOADS_OPEN"
PREVIOUS_STATUS = "OPERATORLEVEL_RHOE_BN_FILL_REDUCED_MATTERSLOT_OVERLAP_SOURCE_OPEN"
SM_STATUS = "MTT_SELECTED_SMSLOTFUNCTOR_ALL_SIX_ARROWS_EMITTED_OPERATOR_PAYLOADS_OPEN"
NEXT = "Selected_U1Y_RouteC_Downstream_OperatorPayload_Ledger_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    sm_packet = load(SM_PACKET)
    sm_cert = load(SM_CERT)
    kernel = sm_packet["selected_overlap_kernel"]
    same_source = sm_packet["same_source_consistency"]
    arrow_status = sm_packet["arrow_status"]
    remains = sm_packet["what_remains_open"]

    checks = {
        "G0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "G1_upstream_certificate_proves_source_packet": sm_cert["status"] == SM_STATUS
        and sm_cert["theorem_proved"] is True
        and sm_cert["selected_SMSlotFunctor_all_six_arrows_claimed"] is True,
        "G2_all_six_source_arrows_closed": arrow_status["all_six_closed"] is True
        and arrow_status["closed_count"] == 6
        and arrow_status["open_count"] == 0,
        "G3_overlap_kernel_selected": kernel["status"] == "EMITTED_SOURCE_ARROW"
        and kernel["selected"] is True
        and kernel["preconditions"]["first_four_arrows_closed"] is True
        and kernel["preconditions"]["all_matter_projectors_selected"] is True
        and kernel["preconditions"]["selected_ext_unit_row_closed"] is True,
        "G4_same_source_consistency_selected": same_source["status"] == "EMITTED_SOURCE_ARROW"
        and same_source["selected_same_source_consistency_map"] is True
        and all(same_source["closed_parts"].values()),
        "G5_no_downstream_operator_or_flavor_closure": sm_packet[
            "downstream_operator_or_flavor_closure_claimed"
        ]
        is False
        and sm_cert["downstream_operator_or_flavor_closure_claimed"] is False
        and remains["same_source_D_E_Riesz_Green_dotD"] is True
        and remains["primitive_C1_overlap_contractions"] is True
        and remains["physical_alpha1_driver"] is True
        and remains["Yukawa_CKM_PMNS_masses"] is True,
        "G6_no_target_fitting_or_observed_data": sm_packet["observed_data_used"] is False
        and sm_packet["target_fitting_used"] is False
        and sm_cert["observed_data_used"] is False
        and sm_cert["target_fitting_used"] is False,
        "G7_boundary_preserves_full_closure_open": sm_packet["closure_claimed"] is False
        and sm_cert["closure_claimed"] is False
        and remains["full_SM_or_no_knob_closure"] is True,
    }

    closed_source_fields = {
        "selected_terminal_to_SU5_E6_slot_packet": True,
        "selected_10M_clock_readout": True,
        "selected_bar5M_shift_readout": True,
        "selected_1M_Dirac_shift_readout": True,
        "selected_U10_Ubar5_source_outputs": True,
        "selected_overlap_transfer_normalization": True,
        "same_source_consistency_map": True,
    }

    return {
        "packet": "SMSlotFunctor_OverlapKernel_SourceEmission_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_frontier": str(PREVIOUS.relative_to(ROOT)),
            "sm_slot_functor_packet": str(SM_PACKET),
            "sm_slot_functor_certificate": str(SM_CERT),
        },
        "theorem": {
            "name": "SMSlotFunctorOverlapKernelSourceEmissionImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The upstream SM parity repo now emits the complete selected "
                "SM-slot functor source packet: A1-A3 terminal section-ring slot "
                "arrows, A4 q79 polarization outputs, A5 selected overlap/transfer "
                "kernel, and A6 same-source consistency. Therefore the earlier "
                "local matter-slot overlap source gap is closed at the source-functor "
                "level. The remaining non-SM/SM-closure gate is downstream operator "
                "payload emission: same-source D_E/Riesz/Green/dotD, primitive C1 "
                "overlap contractions, physical alpha1 driver, and flavor/mass data."
            ),
        },
        "checks": checks,
        "closed_source_fields": closed_source_fields,
        "imported_overlap_kernel": {
            "definition": kernel["kernel_definition"],
            "source": kernel["source"],
            "normalization_values": kernel["normalization_values"],
            "preconditions": kernel["preconditions"],
        },
        "imported_same_source_consistency": same_source,
        "downstream_open_fields": {
            "same_source_D_E_Riesz_Green_dotD": True,
            "primitive_C1_overlap_contractions": True,
            "operator_layer_Pic0_recheck": True,
            "physical_alpha1_driver": True,
            "Yukawa_CKM_PMNS_masses": True,
            "full_SM_or_no_knob_closure": True,
        },
        "frontier_update": {
            "old_next": previous["verdict"]["next_required_artifact"],
            "current_next": NEXT,
            "why": (
                "Matter-slot routing and selected overlap normalization no longer "
                "need to be treated as open source-side blockers. The next ledger "
                "must replay downstream operator payloads against the emitted "
                "SM-slot functor and decide which fields are computable rather "
                "than structurally selected."
            ),
        },
        "guardrails": {
            "does_not_claim_downstream_operator_payloads": True,
            "does_not_claim_C1_response_or_full_response_matrix": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_physical_alpha1": True,
            "does_not_claim_Yukawa_CKM_PMNS_masses_or_full_SM": True,
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SMSlotFunctorOverlapKernelSourceEmissionImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "closed_source_fields": packet["closed_source_fields"],
        "downstream_open_fields": packet["downstream_open_fields"],
        "frontier_update": packet["frontier_update"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# SM Slot Functor OverlapKernel SourceEmission Import v1

Status: `{cert["status"]}`.

## Result

The source-side matter-slot blocker has moved. Upstream now emits all six
selected SM-slot functor arrows, including the selected overlap/transfer kernel:

```text
{packet["imported_overlap_kernel"]["definition"]}
```

This imports selected `10_M`, `bar5_M`, `1_M=N^c`, q79 polarization
`U_10=I_3`, `U_bar5=F`, selected overlap normalization, and same-source
consistency at the functor/source level.

## Boundary

This does not close downstream operator payloads, primitive C1 contractions,
physical alpha1, Yukawa/CKM/PMNS/masses, or full SM/no-knob closure.

```json
{json.dumps(packet["downstream_open_fields"], indent=2, sort_keys=True)}
```

Next artifact: `{packet["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
