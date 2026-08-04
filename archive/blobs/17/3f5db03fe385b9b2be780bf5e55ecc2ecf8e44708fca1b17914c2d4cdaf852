from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_dotd_source_end0_routing_reduction_certificate.json"
STATUS = "POST_ALPHA_DOTD_SOURCE_REDUCED_END0_ROUTING_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_End0_to_SectorFunctor_Source_and_Value_Packet_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["dotD_alpha1_source_closed"] is False, "dotD source should remain open")
    require(
        cert["selected_End0_to_sector_functor_values_extracted"] is False,
        "End0 functor values should remain open",
    )
    require(all(cert["checks"].values()), "all certificate checks should pass")

    contract = packet["contract"]
    require(contract["status"] == "OPEN_SELECTED_END0_TO_SECTOR_FUNCTOR_VALUES_REQUIRED", "contract should be open")
    require(contract["branch"]["q"] == 79, "wrong q")
    require(contract["domain"]["basis"] == ["T1", "T2", "T3"], "wrong domain basis")
    require(contract["domain"]["current_supported_lane"] == "T3", "wrong supported lane")
    require(contract["codomain"]["sector_slots"] == ["Q", "u", "d", "L", "e", "N", "H"], "wrong sectors")
    require(all(value is None for value in contract["values"].values()), "contract values should be empty")
    require(len(contract["required_fields"]) == 7, "wrong required-field count")

    route_a = packet["route_A_source_normalization_nogo"]
    require(route_a["closed_as_nogo"] is True, "route A no-go should close")
    require(route_a["does_not_vary_integral_c2_alpha1"] is True, "integral source row should not vary")
    require(route_a["central_shared_circle_retained"] is True, "shared circle guardrail missing")
    require(route_a["visible_rank2_support"]["central_shared_circle_trivial"] is True, "shared circle should be trivial")

    route_b = packet["route_B_end0_to_sector_routing"]
    require(route_b["closed"] is False, "route B should remain open")
    require(route_b["same_basis_dotD_matrices_exist"] is True, "same-basis dotD support missing")
    require(route_b["conditional_weyl_transfer_exact"] is True, "Weyl transfer support missing")
    require(route_b["selected_End0_to_sector_functor_values_extracted"] is False, "functor values must be open")
    require(route_b["selected_transfer_normalization_closed"] is False, "normalization must be open")
    require(route_b["values_promoted"] is False, "values should not be promoted")
    require(route_b["projector_ranks"]["H"] == 1.0, "wrong H projector rank")
    require(route_b["projector_ranks"]["Q"] == 3.0, "wrong Q projector rank")

    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "shared circle remains degree-zero" in note, "note missing essentials")

    print("AUDIT_PASS: dotD source reduced to End0-sector routing values; naive normalization rejected")


if __name__ == "__main__":
    main()
