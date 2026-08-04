"""Audit alpha1 source-normalization / End0-sector-routing value-fill attempt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_alpha1_source_normalization_or_end0_sector_routing_value_fill.candidate.json"
CERT = ROOT / "certificates" / "selected_alpha1_source_normalization_or_end0_sector_routing_value_fill_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Alpha1_SourceNormalization_or_End0SectorRouting_Value_Fill_v1.md"

STATUS = "MTT_SELECTED_ALPHA1_VALUE_FILL_ATTEMPTED_SOURCE_NORMALIZATION_NOGO_SECTOR_ROUTING_VALUES_OPEN"
NEXT = "MTT_Selected_End0_to_SectorFunctor_Source_and_Value_Packet_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    route_a = data["route_A_source_normalization"]
    route_b = data["route_B_end0_to_sector_routing"]
    decision = data["decision"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "closed tangent reused only as support",
            data["numerical_tangent_reused"]["residual_l2"] < 1e-12
            and data["numerical_tangent_reused"]["h_l2"] > 0
            and data["numerical_tangent_reused"]["h_mean_abs"] < 1e-14,
            data["numerical_tangent_reused"],
        ),
        check(
            "route A no-go",
            route_a["closed"] is True
            and route_a["topological_support_present"] is True
            and "does not vary the Chern class" in route_a["reason"]
            and "dotD_alpha1 := dotD[h_ext]" in route_a["forbidden_identification"],
            route_a,
        ),
        check(
            "route B reduced but not closed",
            route_b["closed"] is False
            and route_b["End0_row_response_available"] is True
            and route_b["sector_projector_dotd_matrices_exist_conditionally"] is True
            and route_b["honest_bn_validator_fails_only_by_source_flags"] is True
            and route_b["conditional_weyl_transfer_exact"] is True
            and route_b["values_promoted"] is False,
            route_b,
        ),
        check(
            "selected values still absent",
            route_b["selected_sector_routing_closed"] is False
            and route_b["selected_transfer_normalization_closed"] is False
            and route_b["q79_sector_charge_closed"] is False
            and route_b["constants_repo_transfer_normalization_closed"] is False,
            route_b,
        ),
        check(
            "decision honest",
            decision["source_normalization_route_retired_for_naive_scale_tangent"] is True
            and decision["sector_routing_route_remains_primary"] is True
            and decision["physical_dotD_alpha1_payload_extracted"] is False
            and decision["selected_End0_to_sector_routing_values_extracted"] is False
            and decision["best_next_object"] == NEXT,
            decision,
        ),
        check(
            "no closure or target fitting",
            data["closure_claimed"] is False
            and data["target_fitting_used"] is False
            and cert["closure_claimed"] is False
            and cert["target_fitting_used"] is False,
            {"closure": data["closure_claimed"], "target_fitting": data["target_fitting_used"]},
        ),
        check(
            "remaining gate precise",
            data["what_remains_open"]["selected_End0_to_sector_functor_values"] is True
            and data["what_remains_open"]["selected_transfer_normalization"] is True
            and data["what_remains_open"]["sector_dotD_alpha1_matrices"] is True,
            data["what_remains_open"],
        ),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records no-go and next",
            "Route A Result: Source-Normalization No-Go" in note
            and "change the integral Chern class" in note
            and "Route B Result: Sector-Routing Values Still Missing" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected alpha1 value-fill audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
