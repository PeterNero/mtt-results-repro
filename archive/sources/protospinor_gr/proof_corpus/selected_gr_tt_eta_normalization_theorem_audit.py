from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_gr_tt_eta_normalization_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "ETA_NORMALIZATION_DECISION_CLOSED_SELECTED_VALUE_OPEN",
        "unexpected status",
    )

    decision = cert["closed_decision"]
    routes = cert["route_decisions"]
    lessons = cert["cross_encoding_lessons"]
    source = cert["source_tests"]
    shortcuts = cert["no_go_for_shortcuts"]
    remaining = cert["remaining_exact_gate"]
    guards = cert["guardrails"]

    require(decision["eta_TT_is_the_only_remaining_dimensionless_GR_TT_modal_gap_scalar"] is True, "eta should be only scalar")
    require(decision["eta_TT_cannot_be_selected_by_convention"] is True, "eta convention choice should be forbidden")
    require(routes["closure_metric_eta_1"]["closes_modal_gap"] is False, "unit route must not close")
    require(routes["action_hessian_eta_kappa_STF"]["closes_modal_gap"] is False, "kappa route must not close")
    require(routes["branch_window_eta_c_kappa_STF"]["closes_modal_gap"] is False, "window route must remain open")
    require(lessons["canonical_internal_action_units_closed"] is True, "internal action units should be closed")
    require(lessons["physical_absolute_no_go"] is True, "physical no-go should remain")
    require(lessons["coefficient_row_metric_can_close_when_source_selects_inner_product"] is True, "cross-encoding lesson expected")
    require(source["Aint_operator_shape_closed"] is True, "Aint shape should be closed")
    require(source["selected_projector_window_chi_tau_open"] is True, "projector/window should be open")
    require(source["selected_kappa_n_open"] is True, "selected kappa should be open")
    require(source["selected_fiber_lambda_open"] is True, "selected fiber lambda should be open")
    require(all(shortcuts.values()), "all shortcuts should be blocked")
    require(remaining["name"] == "Selected_TT_Projector_Window_Normalization_Lemma", "wrong remaining lemma")
    require(guards["claims_eta_TT_numeric_selected"] is False, "must not claim selected eta")
    require(guards["claims_GR_TT_modal_gap_closed"] is False, "must not claim GR TT gap closed")
    require(guards["claims_physical_modal_gap_closed"] is False, "must not claim physical gap")

    print("AUDIT_PASS: eta normalization decision closed; selected eta value remains open")


if __name__ == "__main__":
    main()
