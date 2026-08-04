from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_modal_gap_physical_anchor_gate_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "SELECTED_MODAL_GAP_PHYSICAL_ANCHOR_NOT_CLOSED_TEV_CALIBRATION_FORBIDDEN",
        "unexpected status",
    )
    source = cert["source_tests"]
    closed = cert["closed_tests"]
    blocked = cert["blocked_shortcuts"]
    open_tests = cert["open_tests"]
    guards = cert["guardrails"]
    rows = {row["id"]: row for row in cert["candidate_classification"]}

    require(source["theta_i_has_lambda_star_value"] is True, "Theta I should contain lambda_star")
    require(
        source["theta_i_declares_tev_scale_calibration_assumption"] is True,
        "Theta I should declare TeV calibration assumption",
    )
    require(
        source["theta_i_says_formalism_does_not_fix_identification"] is True,
        "Theta I should say formalism does not fix TeV identification",
    )
    require(closed["internal_lambda_star_identified"] is True, "internal lambda_star should be identified")
    require(blocked["use_mu_theta_5TeV_as_prediction"] is True, "5 TeV shortcut must be blocked")
    require(blocked["use_tensor_bound_to_infer_planck_scale"] is True, "Planck tensor shortcut must be blocked")
    require(rows["theta_mu_5_TeV"]["classification"] == "FORBIDDEN_AS_NO_KNOB_ANCHOR_CALIBRATION_ASSUMPTION", "TeV row should be forbidden")
    require(open_tests["selected_modal_gap_in_eV_or_inverse_meters_computed"] is False, "physical modal gap should remain open")
    require(guards["claims_mu_theta_5TeV_derived"] is False, "must not claim 5 TeV derived")
    require(guards["forbids_calibration_as_prediction"] is True, "calibration guard required")

    print("AUDIT_PASS: selected modal-gap physical anchor remains open; 5 TeV calibration forbidden as prediction")


if __name__ == "__main__":
    main()
