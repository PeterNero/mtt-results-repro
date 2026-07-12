from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "physical_alpha1_normalization_nogo_end0_sector_reduction_certificate.json"
STATUS = "PHYSICAL_ALPHA1_NAIVE_NORMALIZATION_NOGO_REDUCED_TO_END0_SECTOR_FUNCTOR_VALUES"
NEXT = "MTT_Selected_SectorZeroMode_Realization_Functor_or_End0TensorProduct_Construction_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(all(cert["checks"].values()), "all checks should pass")
    require(packet["route_A_naive_source_normalization_nogo"]["closed_as_nogo"] is True, "route A no-go missing")
    require(
        packet["route_A_naive_source_normalization_nogo"]["does_not_vary_integral_c2_alpha1"] is True,
        "integral row guardrail missing",
    )
    require(packet["route_B_end0_to_sector_reduction"]["closed"] is False, "route B must remain open")
    require(packet["route_B_end0_to_sector_reduction"]["selected_End0_to_sector_functor_values_extracted"] is False, "must not extract functor values")
    require(all(packet["what_closes_now"].values()), "closure flags should be true")
    require(all(packet["what_remains_open"].values()), "open flags should be true")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "c2(V_alpha)=4 alpha1" in note, "note missing essentials")
    print("AUDIT_PASS: physical alpha1 naive normalization no-go; reduced to End0-sector functor values")


if __name__ == "__main__":
    main()
