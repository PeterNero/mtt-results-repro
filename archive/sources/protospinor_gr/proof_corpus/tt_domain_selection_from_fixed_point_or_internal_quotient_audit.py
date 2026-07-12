from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "tt_domain_selection_from_fixed_point_or_internal_quotient_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(
        cert["status"] == "TT_DOMAIN_SELECTION_REDUCED_TO_FIXED_POINT_EXTERNALIZATION_MAP",
        "unexpected status",
    )

    source = cert["source_tests"]
    closed = cert["closed_now"]
    result = cert["selection_result"]
    routes = {row["route"]: row for row in cert["route_table"]}
    guards = cert["guardrails"]

    require(source["strominger_selects_unique_internal_fixed_point"] is True, "internal fixed point not sourced")
    require(source["strominger_fuyau_torus_bundle_source"] is True, "Fu-Yau torus source not detected")
    require(source["mtheory_fixed_point_topological_scales"] is True, "M-theory scale/topology source missing")
    require(source["qg_external_domain_class_sourced"] is True, "QG external class not sourced")
    require(source["qg_selects_external_TT_domain"] is False, "QG must not be marked as selecting unique TT domain")
    require(source["flavor_selects_finite_internal_quotient"] is True, "finite internal quotient source missing")
    require(
        source["flavor_quotient_identified_with_TT_external_domain"] is False,
        "internal quotient must not be identified with external TT domain",
    )
    require(all(closed.values()), "closed_now fields should be true")

    require(routes["internal_flux_fixed_point"]["closed"] is True, "internal fixed-point route should close")
    require(routes["constructive_qg_external_domain"]["closed"] is True, "QG class route should close")
    require(routes["fixed_point_to_TT_externalization_map"]["closed"] is False, "externalization map must remain open")
    require(result["selected_external_TT_domain_closed"] is False, "selected external TT domain must remain open")
    require(result["fixed_point_to_external_TT_map_closed"] is False, "externalization map must remain open")
    require(result["selected_TT_lambda_closed"] is False, "lambda must remain open")

    required = packet["required_fields"]
    require(required["external_TT_domain_functor"] is None, "packet must not fill functor")
    require(required["external_spatial_topology"] is None, "packet must not select topology")
    require(required["lowest_positive_eigenvalue"] is None, "packet must not select eigenvalue")
    require("Fixed_Point_to_TT_Domain_Externalization_Theorem" in note, "note lost next theorem")

    require(guards["claims_periodic_T3_selected"] is False, "must not select periodic T3")
    require(guards["claims_Z64_is_external_TT_domain"] is False, "must not identify Z64 with TT domain")
    require(guards["claims_lambda_TT_numeric_selected"] is False, "must not claim numeric lambda")
    require(guards["claims_full_GR_response_closed"] is False, "must not claim full GR closure")

    print("AUDIT_PASS: TT domain selection reduced to fixed-point externalization map")


if __name__ == "__main__":
    main()
