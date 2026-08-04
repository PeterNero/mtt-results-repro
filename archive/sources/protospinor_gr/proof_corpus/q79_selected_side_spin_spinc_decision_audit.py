from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "q79_selected_side_spin_spinc_decision_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    checks = cert["checks"]
    interval = cert["interval_result"]
    theorem = cert["SpinC_theorem"]
    decision = cert["decision"]
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]

    require(all(checks.values()), "one or more selected-side Spin/SpinC checks failed")
    require(
        cert["status"]
        == "EXECUTED_SELECTED_SIDE_STRICT_SPIN_NOGO_AND_SPINC_LIFT_CLOSED_SHARED_LINE_HYM_OPEN",
        "selected-side status changed",
    )
    require(interval["norm_degree"] == 36, "selected-side elliptic norm degree changed")
    require(
        checks["selected_side_norm_resultant_excludes_zero"] is True,
        "the interval resultant no longer excludes zero",
    )
    require(
        checks["selected_side_norm_avoids_finite_flex_points"] is True
        and checks["selected_side_pullback_avoids_flex_at_infinity"] is True,
        "the selected branch no longer avoids all nine flex points",
    )
    require(
        decision["current_executed_selected_side"]["strict_Spin"] == "NO_GO",
        "selected-side strict-Spin decision changed",
    )
    require(
        decision["current_executed_selected_side"]["SpinC_representation_lift"]
        == "CLOSED",
        "selected-side SpinC lift was lost",
    )
    require(theorem["generated_image_order"] == 6, "SpinC image is not S3-sized")
    require(
        theorem["determinant_character"] == "z^2=sign(sheet permutation)",
        "SpinC determinant character changed",
    )
    require(
        tiers["SpinC_determinant_equals_selected_shared_circle_line"] == "OPEN",
        "the shared-circle determinant identification was silently promoted",
    )
    require(
        tiers["branch_locus_HYM_extension"] == "OPEN",
        "the branch-locus HYM extension was silently promoted",
    )
    require(
        guards["claims_integral_gerbe_branch_selected"] is False,
        "the final integral branch was overclaimed",
    )
    require(
        guards["claims_SpinC_determinant_already_selected_by_MTT"] is False,
        "the SpinC determinant line was overclaimed as MTT-selected",
    )

    print(
        "AUDIT_PASS: the executed selected-side interval has strict Spin "
        "obstructed and an exact SpinC lift, while shared-line and HYM "
        "selection remain open"
    )


if __name__ == "__main__":
    main()
