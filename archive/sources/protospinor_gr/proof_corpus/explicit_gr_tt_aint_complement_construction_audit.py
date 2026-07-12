from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "explicit_gr_tt_aint_complement_construction_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    require(
        cert["status"] == "FORMAL_GR_TT_AINT_COMPLEMENT_CONSTRUCTED_SELECTED_NORMALIZATION_OPEN",
        "unexpected status",
    )

    closed = cert["closed_tests"]
    open_tests = cert["open_tests"]
    conventions = cert["normalization_conventions"]
    relation = cert["relation_to_previous_blocker"]
    guards = cert["guardrails"]

    require(all(closed.values()), "formal construction should close all formal tests")
    require(all(open_tests.values()), "selection tests should remain open")
    require(len(cert["computed_rows"]) >= 3, "expected computed rows")
    require(
        all(row["closure_metric_normalized_lambda"] == 1.0 for row in cert["computed_rows"]),
        "closure metric normalized rows should be unit",
    )
    require(
        all(row["action_hessian_normalized_lambda"] > 0 for row in cert["computed_rows"]),
        "action hessian rows should be positive",
    )
    require(conventions["closure_metric_normalized"]["closed_as_MTT_selected_modal_gap"] is False, "unit convention must not close gap")
    require(conventions["action_hessian_normalized"]["closed_as_MTT_selected_modal_gap"] is False, "hessian convention must not close gap")
    require(conventions["branch_window_normalized"]["requires_source_for_c_window"] is True, "window factor needs source")
    require(relation["resolves_distinct_A_route_as_formal_family"] is True, "distinct route should be formalized")
    require(relation["resolves_selected_GR_TT_modal_gap"] is False, "selected modal gap must remain open")
    require(packet["open_selection_fields"]["selected_normalization_convention"] is None, "packet must not select convention")
    require(guards["claims_selected_eta_TT"] is False, "must not claim selected eta")
    require(guards["claims_lambda_GR_TT_equals_1"] is False, "must not claim unit gap")
    require(guards["claims_lambda_GR_TT_equals_kappa_STF"] is False, "must not claim kappa gap")
    require(guards["claims_lambda_GR_TT_equals_z64"] is False, "must not claim Z64 gap")

    print("AUDIT_PASS: formal GR TT Aint complement constructed; selected normalization remains open")


if __name__ == "__main__":
    main()
