"""Import Weyl-pair dynamic-overlap promotion / honest Galerkin C1 cutset."""

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

PREVIOUS = CERTS / "nonscalardynamicoverlap_or_fullresponsecorrection_valueemission_import_certificate.json"
SM_PACKET = SM / "candidate_data" / "selected_weylpairdynamicoverlap_sourcepromotion_or_honestgalerkinc1_valuefill.candidate.json"
SM_CERT = SM / "certificates" / "selected_weylpairdynamicoverlap_sourcepromotion_or_honestgalerkinc1_valuefill_certificate.json"

OUTPUT_PACKET = DATA / "weylpairdynamicoverlap_sourcepromotion_or_honestgalerkinc1_valuefill_import.candidate.json"
OUTPUT_CERT = CERTS / "weylpairdynamicoverlap_sourcepromotion_or_honestgalerkinc1_valuefill_import_certificate.json"
OUTPUT_NOTE = CORPUS / "WeylPairDynamicOverlap_SourcePromotion_or_HonestGalerkinC1_ValueFill_Import_v1.md"

STATUS = "WEYLPAIR_DYNAMIC_OVERLAP_PROMOTION_CUTSET_IMPORTED_OPEN"
PREVIOUS_STATUS = "NONSCALAR_DYNAMIC_OVERLAP_CONDITIONAL_VALUES_IMPORTED_SOURCE_OPEN"
SM_STATUS = (
    "MTT_SELECTED_WEYLPAIRDYNAMICOVERLAP_SOURCEPROMOTION_OR_HONESTGALERKINC1_"
    "VALUEFILL_BUILT_PROMOTION_CUTSET_OPEN"
)
NEXT = "Selected_U1Y_RouteC_DynamicTransferHessian_bSelected_or_HonestGalerkinC1_ValueFill_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    sm_packet = load(SM_PACKET)
    sm_cert = load(SM_CERT)
    lane_a = sm_packet["lane_A_dynamic_source_promotion"]
    lane_b = sm_packet["lane_B_honest_Galerkin_C1_value_fill"]
    cutset = sm_packet["minimum_cutset"]
    decision = sm_packet["promotion_decision"]

    checks = {
        "G0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "G1_upstream_theorem_proved": sm_cert["status"] == SM_STATUS
        and sm_cert["theorem_proved"] is True
        and sm_packet["theorem"]["proved"] is True,
        "G2_static_source_tier_closed": all(sm_packet["closed_static_source_tier"].values()),
        "G3_lane_A_conditional_transfer_exact_but_unpromoted": lane_a["conditional_transfer_exact"]
        is True
        and lane_a["conditional_transfer_formula"]["phase_column"] == "T(Z) = sector_route(u,e; I + Z)"
        and lane_a["conditional_transfer_formula"]["shift_column"] == "T(X) = sector_route(d,nuD; I + X)"
        and lane_a["conditional_transfer_residuals"]["phase_residual"] == 0.0
        and lane_a["conditional_transfer_residuals"]["shift_residual"] == 0.0
        and lane_a["static_source_route_reclassified_closed"] is True
        and all(lane_a["conditional_packet_tests_pass"].values())
        and lane_a["promoted"] is False
        and all(value is False for value in lane_a["selected_promotion_fields"].values()),
        "G4_lane_B_honest_galerkin_contract_open": lane_b["manifest_status"]
        == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING"
        and lane_b["selected_source_verified"] is False
        and lane_b["promoted"] is False
        and all(value is False for value in lane_b["required_outputs_present"].values()),
        "G5_minimum_cutset_exact": cutset["static_routing_no_longer_in_cutset"] is True
        and cutset["observed_flavor_data_forbidden_as_selector"] is True
        and "selected_b_selected" in cutset["lane_A_fill_all"]
        and "linear_response_matrices" in cutset["lane_B_fill_all"],
        "G6_promotion_decision_blocks_selected_claims": decision["static_source_route_retired_as_blocker"]
        is True
        and decision["conditional_non_scalar_packet_available"] is True
        and decision["dynamic_promotion_cutset_open"] is True
        and decision["selected_dynamic_overlap_promoted"] is False
        and decision["selected_full_response_promoted"] is False
        and decision["selected_A_selected_promoted"] is False
        and decision["selected_b_selected_promoted"] is False
        and decision["selected_Galerkin_C1_contractions_promoted"] is False,
        "G7_no_target_or_closure_overclaim": sm_packet["closure_claimed"] is False
        and sm_packet["selected_dynamic_overlap_tensor_claimed"] is False
        and sm_packet["selected_full_response_claimed"] is False
        and sm_packet["A_selected_claimed"] is False
        and sm_packet["b_selected_claimed"] is False
        and sm_packet["Galerkin_C1_contractions_claimed"] is False
        and sm_packet["observed_data_used"] is False
        and sm_packet["target_fitting_used"] is False,
    }

    return {
        "packet": "WeylPairDynamicOverlap_SourcePromotion_or_HonestGalerkinC1_ValueFill_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "sm_weylpair_promotion_packet": str(SM_PACKET),
            "sm_weylpair_promotion_certificate": str(SM_CERT),
        },
        "theorem": {
            "name": "WeylPairDynamicOverlapPromotionCutsetImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected static source tier emits the Weyl carrier, active "
                "shift, Z->u,e and X->d,nuD routing, 1_M=N^c shift rule, and "
                "trace normalization. The conditional I+Z/I+X transfer is exact "
                "and passes the qualitative non-scalar flavor tests. Promotion "
                "is still blocked by a precise two-lane cutset: selected dynamic "
                "transfer/Hessian/A_selected/b_selected/sector response values, "
                "or honest selected Galerkin C1 zero-mode bases, contractions, "
                "linear responses, and rank tests."
            ),
        },
        "checks": checks,
        "closed_static_source_tier": sm_packet["closed_static_source_tier"],
        "lane_A_dynamic_source_promotion": lane_a,
        "lane_B_honest_Galerkin_C1_value_fill": lane_b,
        "minimum_cutset": cutset,
        "promotion_decision": decision,
        "what_closes_now": sm_packet["what_closes_now"],
        "what_remains_open": sm_packet["what_remains_open"],
        "frontier_update": {
            "old_next": previous["next_required_artifact"],
            "current_next": NEXT,
            "why": (
                "The conditional non-scalar packet is tied to selected static "
                "routing, but selected dynamic promotion is still exactly the "
                "two-lane value-fill cutset."
            ),
        },
        "guardrails": {
            "static_source_tier_closed": True,
            "conditional_non_scalar_transfer_exact": True,
            "selected_dynamic_overlap_tensor_claimed": False,
            "selected_full_response_claimed": False,
            "selected_A_selected_claimed": False,
            "selected_b_selected_claimed": False,
            "honest_Galerkin_C1_contractions_claimed": False,
            "observed_data_used": False,
            "target_fitting_used": False,
            "full_SM_closure_claimed": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "WeylPairDynamicOverlapSourcePromotionOrHonestGalerkinC1ValueFillImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "frontier_update": packet["frontier_update"],
        "minimum_cutset": packet["minimum_cutset"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    cutset = packet["minimum_cutset"]
    return f"""# WeylPairDynamicOverlap SourcePromotion or HonestGalerkinC1 ValueFill Import v1

Status: `{cert["status"]}`.

## Closed Tier

The selected static/source tier now includes the Weyl carrier, active shift
`(1,1)`, `Z -> u,e`, `X -> d,nuD`, `1_M=N^c` on the shift side, and trace
transfer normalization.

The conditional transfer is exact:

```text
T(Z) = sector_route(u,e; I + Z)
T(X) = sector_route(d,nuD; I + X)
```

## Remaining Cutset

Lane A:
```text
{cutset["lane_A_fill_all"]}
```

Lane B:
```text
{cutset["lane_B_fill_all"]}
```

No observed masses, CKM/PMNS values, CP phase, or benchmark entries are used as
selectors.

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
