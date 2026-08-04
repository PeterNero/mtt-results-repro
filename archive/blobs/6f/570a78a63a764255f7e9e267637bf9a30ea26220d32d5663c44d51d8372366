"""Import the SM-slot functor downstream operator-payload ledger."""

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

PREVIOUS = CERTS / "smslotfunctor_overlapkernel_source_emission_import_certificate.json"
SM_PACKET = SM / "candidate_data" / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"
SM_CERT = SM / "certificates" / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger_certificate.json"

OUTPUT_PACKET = DATA / "smslotfunctor_downstream_operator_payload_ledger_import.candidate.json"
OUTPUT_CERT = CERTS / "smslotfunctor_downstream_operator_payload_ledger_import_certificate.json"
OUTPUT_NOTE = CORPUS / "SMSlotFunctor_DownstreamOperatorPayload_Ledger_Import_v1.md"

STATUS = "SMSLOTFUNCTOR_DOWNSTREAM_LEDGER_IMPORTED_STATIC_PROMOTED_DYNAMIC_OPEN"
PREVIOUS_STATUS = "SMSLOTFUNCTOR_OVERLAPKERNEL_SOURCE_PACKET_IMPORTED_DOWNSTREAM_OPERATOR_PAYLOADS_OPEN"
SM_STATUS = "MTT_SELECTED_SMSLOTFUNCTOR_DOWNSTREAM_PAYLOAD_LEDGER_BUILT_STATIC_FIELDS_PROMOTED_DYNAMIC_C1_OPEN"
NEXT = "Selected_U1Y_RouteC_DynamicOverlapKernel_or_C1Primitive_SourceEmission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    sm_packet = load(SM_PACKET)
    sm_cert = load(SM_CERT)
    tiers = sm_packet["payload_tiers"]
    reclass = sm_packet["old_contract_reclassification"]
    weyl = sm_packet["weylpair_consequence"]
    remains = sm_packet["what_remains_open"]

    checks = {
        "G0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "G1_upstream_ledger_proved": sm_cert["status"] == SM_STATUS
        and sm_cert["theorem_proved"] is True
        and sm_cert["selected_static_payloads_claimed"] is True
        and sm_cert["dynamic_operator_payloads_claimed"] is False,
        "G2_static_tier_closed_dynamic_tier_open": tiers["static_sm_slot_tier"]["closed"] is True
        and tiers["dynamic_operator_c1_tier"]["closed"] is False,
        "G3_static_sector_route_promoted": reclass["matter_slot_charge"]["static_selected_emitted"] is True
        and reclass["singlet_neutrino_rule"]["static_selected_emitted"] is True
        and reclass["overlap_transfer"]["static_finite_transfer_selected"] is True
        and reclass["normalization"]["static_trace_innerproduct_normalization_selected"] is True,
        "G4_dynamic_fields_not_promoted": reclass["operator_values"]["dynamic_selected_emitted"] is False
        and reclass["primitive_contractions"]["dynamic_selected_emitted"] is False
        and reclass["overlap_transfer"]["dynamic_source_to_C1_transfer_functor_selected"] is False
        and reclass["normalization"]["dynamic_hessian_or_b_selected_normalization_selected"] is False,
        "G5_weylpair_static_route_exact_no_A_selected": weyl["selected_static_sector_route_now_closed"] is True
        and weyl["phase_route"] == ["u", "e"]
        and weyl["shift_route"] == ["d", "nuD"]
        and weyl["conditional_A_weylpair_exact"] is True
        and weyl["promote_conditional_A_to_A_selected"] is False,
        "G6_remaining_dynamic_blockers_explicit": remains["selected_D_E_Riesz_Green_dotD"] is True
        and remains["physical_alpha1_driver"] is True
        and remains["selected_dynamic_overlap_tensor_or_transfer_functor"] is True
        and remains["selected_primitive_C1_contractions"] is True
        and remains["selected_b_selected_and_Hessian_normalization"] is True,
        "G7_no_target_or_closure_overclaim": sm_packet["closure_claimed"] is False
        and sm_packet["A_selected_claimed"] is False
        and sm_packet["b_selected_claimed"] is False
        and sm_packet["observed_data_used"] is False
        and sm_packet["target_fitting_used"] is False,
    }

    return {
        "packet": "SMSlotFunctor_DownstreamOperatorPayload_Ledger_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "sm_downstream_ledger_packet": str(SM_PACKET),
            "sm_downstream_ledger_certificate": str(SM_CERT),
        },
        "theorem": {
            "name": "SMSlotFunctorDownstreamLedgerImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected SM-slot functor discharges the static routing and "
                "finite trace-normalization blockers: Z/clock routes to u,e and "
                "X/shift routes to d,nuD, with the 1_M Dirac-neutrino rule selected "
                "at the static tier. This still does not promote the conditional "
                "Weyl-pair C1 operator to A_selected, because the dynamic operator "
                "tier lacks selected D_E/Riesz/Green/dotD, physical alpha1 driver, "
                "dynamic overlap tensor, primitive C1 contractions, and b_selected."
            ),
        },
        "checks": checks,
        "static_payloads_now_closed": sm_packet["what_closes_now"],
        "static_sector_route": {
            "phase_route": weyl["phase_route"],
            "shift_route": weyl["shift_route"],
            "conditional_A_weylpair_exact": weyl["conditional_A_weylpair_exact"],
            "promote_conditional_A_to_A_selected": weyl["promote_conditional_A_to_A_selected"],
        },
        "dynamic_payloads_still_open": {
            "dynamic_visible_routec_operator_source_identity": remains[
                "dynamic_visible_routec_operator_source_identity"
            ],
            "selected_D_E_Riesz_Green_dotD": remains["selected_D_E_Riesz_Green_dotD"],
            "physical_alpha1_driver": remains["physical_alpha1_driver"],
            "selected_dynamic_overlap_tensor_or_transfer_functor": remains[
                "selected_dynamic_overlap_tensor_or_transfer_functor"
            ],
            "selected_primitive_C1_contractions": remains["selected_primitive_C1_contractions"],
            "selected_b_selected_and_Hessian_normalization": remains[
                "selected_b_selected_and_Hessian_normalization"
            ],
            "promote_conditional_A_to_A_selected": remains["promote_conditional_A_to_A_selected"],
            "Yukawa_CKM_PMNS_masses_Higgs_RG": remains["Yukawa_CKM_PMNS_masses_Higgs_RG"],
            "full_SM_or_no_knob_closure": remains["full_SM_or_no_knob_closure"],
        },
        "frontier_update": {
            "old_next": previous["next_required_artifact"],
            "current_next": NEXT,
            "why": (
                "The static SM parity side is now clean enough that the next "
                "artifact can attack only the dynamic C1/operator layer."
            ),
        },
        "guardrails": {
            "selected_static_payloads_claimed": True,
            "dynamic_operator_payloads_claimed": False,
            "A_selected_claimed": False,
            "b_selected_claimed": False,
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SMSlotFunctorDownstreamOperatorPayloadLedgerImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "static_sector_route": packet["static_sector_route"],
        "dynamic_payloads_still_open": packet["dynamic_payloads_still_open"],
        "frontier_update": packet["frontier_update"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# SM Slot Functor DownstreamOperatorPayload Ledger Import v1

Status: `{cert["status"]}`.

## Result

The static SM-slot tier is promoted:

```text
Z / clock -> u,e
X / shift -> d,nuD
```

The selected `1_M=N^c` Dirac-neutrino rule and finite trace normalization are
now static source-tier data. The conditional Weyl-pair route is exact at that
tier, but `A_selected` is not promoted.

## Dynamic Frontier

```json
{json.dumps(packet["dynamic_payloads_still_open"], indent=2, sort_keys=True)}
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
