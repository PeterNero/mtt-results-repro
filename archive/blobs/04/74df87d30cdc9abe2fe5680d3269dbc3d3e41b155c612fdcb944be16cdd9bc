"""Audit CONST-EW-02 B17 operator tables or physical matching frontier."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b17_operator_tables_or_physical_matching"
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
    phifin = load(BASE / "finite_internal_phifin_source_lift_import.packet.json")
    tables = load(BASE / "routec_projective_operator_tables_import.packet.json")
    matching = load(BASE / "physical_matching_lane_import.packet.json")
    boundary = load(BASE / "weak_mixing_b17_boundary.packet.json")
    cert = load(CERT)

    for name, packet in [
        ("candidate", candidate),
        ("phifin", phifin),
        ("tables", tables),
        ("matching", matching),
        ("boundary", boundary),
        ("cert", cert),
    ]:
        require(packet["observed_data_used_as_selector"] is False, f"{name} used observed selector")
        require(packet["target_fitting_used"] is False, f"{name} used target fitting")
        require(packet["closure_claimed"] is False, f"{name} claimed closure")

    require(candidate["theorem"]["proved"] is True, "B17 theorem did not prove")
    require(candidate["strict_xL_emitted_now"] is False, "xL incorrectly emitted")
    require(candidate["selected_operator_values_emitted"] is False, "selected operator values overclaimed")
    require(candidate["physical_matching_closed"] is False, "physical matching overclaimed")
    require(cert["physical_weak_angle_closure"] is False, "weak angle overclaimed")

    require(phifin["imported_internal_closure"]["finite_internal_branch_closed"] is True, "finite internal branch not imported")
    require(phifin["not_promoted"]["same_source_PhiFin_identity_proved"] is False, "PhiFin identity overpromoted")
    require(phifin["not_promoted"]["explicit_bundle_connection_solved"] is False, "bundle connection overpromoted")
    require(phifin["not_promoted"]["smooth_operator_identity_closed"] is False, "smooth identity overpromoted")

    constructed = tables["constructed_tables"]
    require(constructed["routec_conditional_A_table_constructed"] is True, "Route-C conditional table missing")
    require(constructed["routec_rank_solve_exact"] is True, "Route-C exact solve missing")
    require(constructed["projective_rhoE_mesh_validator_imported"] is True, "projective validator missing")
    require(tables["not_promoted"]["selected_operator_tables_emitted"] is False, "operator tables overpromoted")
    require(tables["not_promoted"]["selected_finite_part_found"] is False, "finite part overpromoted")
    require(tables["open_selected_fields"]["finite_part_or_spectrum"] is True, "finite part not left open")
    require(tables["open_selected_fields"]["lambda_12"] is True, "lambda_12 not left open")

    require(matching["selected_route"]["strict_primary_route_selected"] == "B_flux_strominger_threshold", "wrong strict route")
    require(matching["open_physical_matching"]["gaugekinetic_normalization_closed"] is False, "gauge normalization overclosed")
    require(matching["open_physical_matching"]["matching_scale_closed"] is False, "matching scale overclosed")
    require(matching["open_physical_matching"]["RG_scheme_closed"] is False, "RG scheme overclosed")
    require(matching["one_primitive_lane"]["strict_no_knob"] is False, "one primitive mislabeled")

    require(boundary["closed_now"]["finite_internal_projective_packet_for_internal_scope"] is True, "finite internal boundary missing")
    require(boundary["closed_now"]["routec_conditional_operator_constructed"] is True, "conditional routec boundary missing")
    require(boundary["still_open"]["same_source_PhiFin_identity"] is True, "PhiFin not left open")
    require(boundary["still_open"]["selected_DE_dotD_Riesz_Green_values"] is True, "DE/dotD not left open")
    require(boundary["still_open"]["actual_xL_source_emission"] is True, "xL not left open")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "weak angle not left open")

    print("CONST-EW-02 B17 operator tables/physical matching audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
