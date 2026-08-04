"""Import primitive-C1 / Weyl-pair sector-routing source-emission boundary."""

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

PREVIOUS = CERTS / "primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission_import_certificate.json"
SM_PACKET = SM / "candidate_data" / "selected_primitivec1_or_weylpair_sectorrouting_sourceemission.candidate.json"
SM_CERT = SM / "certificates" / "selected_primitivec1_or_weylpair_sectorrouting_sourceemission_certificate.json"

OUTPUT_PACKET = DATA / "primitivec1_or_weylpair_sectorrouting_sourceemission_import.candidate.json"
OUTPUT_CERT = CERTS / "primitivec1_or_weylpair_sectorrouting_sourceemission_import_certificate.json"
OUTPUT_NOTE = CORPUS / "PrimitiveC1_or_WeylPair_SectorRouting_SourceEmission_Import_v1.md"

STATUS = "PRIMITIVEC1_OR_WEYLPAIR_ROUTING_IMPORTED_STATIC_ROUTE_CLOSED_DYNAMIC_CONTRACTIONS_OPEN"
PREVIOUS_STATUS = "PRIMITIVECLASS_C1OBSERVABLE_IMPORTED_HIGHERORDER_FULLRESPONSE_VALUES_OPEN"
SM_STATUS = "MTT_SELECTED_PRIMITIVEC1_OR_WEYLPAIR_SECTORROUTING_SOURCEEMISSION_STATIC_ROUTING_CLOSED_DYNAMIC_CONTRACTIONS_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveC1Contractions_or_DynamicOverlapTensor_SourceEmission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    sm_packet = load(SM_PACKET)
    sm_cert = load(SM_CERT)
    static = sm_packet["static_routing_source_emission"]
    retired = static["retired_sector_routing"]
    transfer = sm_packet["conditional_transfer_reclassification"]
    dynamic = sm_packet["dynamic_blockers"]
    boundary = sm_packet["proof_boundary"]

    checks = {
        "G0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "G1_upstream_theorem_proved": sm_cert["status"] == SM_STATUS
        and sm_cert["theorem_proved"] is True
        and sm_packet["theorem"]["proved"] is True,
        "G2_static_routing_source_emitted": static["proved"] is True
        and retired["selected_static_sector_route_Z_to_u_e_X_to_d_nuD"] is True
        and retired["phase_route"] == ["u", "e"]
        and retired["shift_route"] == ["d", "nuD"],
        "G3_static_neutrino_and_trace_rules_emitted": retired[
            "selected_static_1M_Dirac_neutrino_shift_rule"
        ]
        is True
        and retired["selected_static_finite_trace_transfer_normalization"] is True
        and retired["all_six_static_sm_slot_arrows_closed"] is True
        and retired["source_level_ZX_carrier_closed"] is True,
        "G4_old_sector_charge_blocker_reclassified": retired[
            "sector_charge_old_artifact_still_open_but_superseded_at_static_tier"
        ]
        is True
        and sm_packet["what_closes_now"]["old_sector_charge_blocker_reclassified_static_closed_dynamic_open"]
        is True,
        "G5_conditional_weyl_transfer_not_promoted": transfer["conditional_weyl_transfer_exact"]
        is True
        and transfer["static_sector_route_now_selected"] is True
        and transfer["conditional_A_promoted_to_A_selected"] is False,
        "G6_dynamic_contraction_blockers_still_open": dynamic[
            "dynamic_visible_routec_operator_source_identity"
        ]
        is True
        and dynamic["selected_D_E_Riesz_Green_dotD"] is True
        and dynamic["selected_dynamic_overlap_tensor_or_transfer_functor"] is True
        and dynamic["selected_primitive_C1_contractions"] is True
        and dynamic["selected_b_selected_and_Hessian_normalization"] is True
        and dynamic["selected_A_selected"] is True
        and dynamic["selected_sector_response_matrices"] is True,
        "G7_proof_boundary_no_dynamic_values_emitted": boundary[
            "static_routing_not_enough_for_A_selected"
        ]
        is True
        and boundary["dynamic_overlap_tensor_not_emitted"] is True
        and boundary["primitive_C1_contractions_not_emitted"] is True
        and boundary["full_SM_closure_claimed"] is False,
        "G8_no_target_or_closure_overclaim": sm_packet["closure_claimed"] is False
        and sm_packet["A_selected_claimed"] is False
        and sm_packet["b_selected_claimed"] is False
        and sm_packet["observed_data_used"] is False
        and sm_packet["target_fitting_used"] is False
        and boundary["observed_data_used"] is False
        and boundary["target_fitting_used"] is False,
    }

    return {
        "packet": "PrimitiveC1_or_WeylPair_SectorRouting_SourceEmission_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "sm_sectorrouting_packet": str(SM_PACKET),
            "sm_sectorrouting_certificate": str(SM_CERT),
        },
        "theorem": {
            "name": "PrimitiveC1OrWeylPairSectorRoutingImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected SM-slot functor ledger source-emits the static "
                "Weyl-pair route Z/clock/phase -> {u,e} and "
                "X/shift/translation -> {d,nuD}, including the 1_M=N^c "
                "Dirac-neutrino shift rule and finite trace normalization. "
                "This retires sector-routing as a static blocker only. The "
                "conditional Weyl transfer remains unpromoted because A_selected "
                "still requires selected dynamic overlap tensors, primitive C1 "
                "contractions, b/Hessian normalization, and sector response "
                "matrices from the same branch."
            ),
        },
        "checks": checks,
        "static_routing_source_emission": static,
        "conditional_transfer_reclassification": transfer,
        "dynamic_blockers": dynamic,
        "proof_boundary": boundary,
        "what_closes_now": sm_packet["what_closes_now"],
        "what_remains_open": sm_packet["what_remains_open"],
        "frontier_update": {
            "old_next": previous["next_required_artifact"],
            "current_next": NEXT,
            "why": (
                "Static sector routing is no longer a blocker. The next artifact "
                "must emit selected primitive C1 contractions or the selected "
                "dynamic overlap tensor/transfer functor that can promote the "
                "conditional Weyl transfer into A_selected."
            ),
        },
        "guardrails": {
            "static_weyl_sector_route_emitted": True,
            "conditional_weyl_transfer_exact": True,
            "conditional_transfer_promoted_to_A_selected": False,
            "dynamic_overlap_tensor_emitted": False,
            "primitive_C1_contractions_emitted": False,
            "A_selected_claimed": False,
            "b_selected_claimed": False,
            "observed_data_used": False,
            "target_fitting_used": False,
            "full_SM_closure_claimed": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "PrimitiveC1OrWeylPairSectorRoutingSourceEmissionImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "frontier_update": packet["frontier_update"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# PrimitiveC1 or WeylPair SectorRouting SourceEmission Import v1

Status: `{cert["status"]}`.

## Result

The selected SM-slot functor ledger closes the static Weyl-pair sector route:

```text
Z / clock / phase -> u, e
X / shift / translation -> d, nuD
1_M = N^c remains on the shift / Dirac-neutrino side
finite trace transfer normalization selected
```

This is source-tier routing data, not a fit to the locked C1 target.

## Boundary

The conditional Weyl-pair C1 transfer is exact only conditionally. It is still
not `A_selected`, because the selected dynamic overlap tensor, primitive C1
contractions, `b_selected` / Hessian normalization, and sector response matrices
have not been emitted from the same branch.

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
