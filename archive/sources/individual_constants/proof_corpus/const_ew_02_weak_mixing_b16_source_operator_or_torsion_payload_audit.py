"""Audit CONST-EW-02 B16 source operator/torsion payload."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b16_source_operator_or_torsion_payload"
DATA = ROOT / "candidate_data"
BASE = DATA / SLUG
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(DATA / f"{SLUG}.candidate.json")
    projector = load(BASE / "pperp_projector_and_index_import.packet.json")
    finitepart = load(BASE / "internal_finitepart_policy_import.packet.json")
    hym = load(BASE / "hym_operator_payload_status.packet.json")
    torsion = load(BASE / "torsion_route_status.packet.json")
    boundary = load(BASE / "weak_mixing_b16_boundary.packet.json")
    cert = load(CERT)

    for name, packet in [
        ("candidate", candidate),
        ("projector", projector),
        ("finitepart", finitepart),
        ("hym", hym),
        ("torsion", torsion),
        ("boundary", boundary),
        ("cert", cert),
    ]:
        require(packet["observed_data_used_as_selector"] is False, f"{name} used observed selector")
        require(packet["target_fitting_used"] is False, f"{name} used target fitting")
        require(packet["closure_claimed"] is False, f"{name} claimed closure")

    require(candidate["theorem"]["proved"] is True, "B16 theorem did not prove")
    require(candidate["strict_xL_emitted_now"] is False, "xL incorrectly emitted")
    require(candidate["operator_payload_closed"] is False, "operator payload incorrectly closed")
    require(cert["strict_xL_emitted_now"] is False, "certificate overclaims xL")
    require(cert["physical_weak_angle_closure"] is False, "certificate overclaims weak angle")

    imported = projector["imported_projector"]
    require(imported["P_perp"][0] == ["2/3", "-1/3", "-1/3"], "wrong P_perp row")
    require(imported["rank_P_perp"] == 2, "wrong P_perp rank")
    require(imported["normalized_trace"] == "2/3", "wrong normalized trace")
    require(imported["selected_U1_SU2_threshold_index_pair"] is True, "index pair not imported")
    require("K_gauge physical anchor" in projector["what_it_does_not_close"], "K_gauge guard missing")

    p_expected = 8.0 * math.log((2.0 * math.pi / 3.0) ** 2) + 8.0 * math.log(2.0 * (2.0 * math.pi / 3.0) ** 2)
    row = finitepart["imported_internal_row"]
    require(row["selected_p_a_internal_promoted"] is True, "internal p_a not promoted")
    require(math.isclose(row["selected_p_a_internal_value"], p_expected, rel_tol=0.0, abs_tol=1e-12), "internal p_a mismatch")
    require(finitepart["lambda_12_closed"] is False, "lambda_12 incorrectly closed")
    require(finitepart["measured_electroweak_closure"] is False, "EW closure incorrectly closed")

    require(hym["closed_support"]["P_perp_projector_compatibility_available"] is True, "Pperp support missing in HYM")
    require(hym["closed_support"]["HYM_mu_stationary_selection_rejected"] is True, "mu no-extremum theorem missing")
    require(hym["open_payload_leaves"]["selected_operator_tables"] is True, "operator tables not left open")
    require(hym["open_payload_leaves"]["selected_positive_spectrum_or_zeta_heat_torsion"] is True, "finite part not left open")
    require(hym["operator_payload_closed"] is False, "HYM operator payload overclosed")

    require(torsion["closed_negative"]["ordinary_rank_one_torsion_route_closed_negative_for_q64"] is True, "ordinary q64 torsion not rejected")
    require(torsion["still_open"]["q64_projective_route_open_auxiliary"] is True, "projective route not left open")
    require(torsion["torsion_payload_closed"] is False, "torsion payload overclosed")

    require(boundary["closed_now"]["P_perp_projector_and_trace_policy"] is True, "Pperp not closed in boundary")
    require(boundary["closed_now"]["internal_Qa_stack_finitepart_policy"] is True, "internal finite part not closed in boundary")
    require(boundary["still_open"]["actual_xL_source_emission"] is True, "xL not left open")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "weak angle not left open")

    print("CONST-EW-02 B16 source operator/torsion payload audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
