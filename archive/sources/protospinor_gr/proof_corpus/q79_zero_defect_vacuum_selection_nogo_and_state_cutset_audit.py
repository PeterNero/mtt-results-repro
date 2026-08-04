from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "q79_zero_defect_vacuum_selection_nogo_and_state_cutset_certificate.json"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(CERT.read_text(encoding="utf-8"))
    require(all(data["checks"].values()), "a vacuum-selection no-go check failed")
    require(
        data["finite_data"]["metric_determinant"] == -1
        and data["finite_data"]["Ricci_tensor"]
        == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        "the exact Ricci-flat wave witness changed",
    )
    require(
        data["finite_data"]["representative_plus_curvature"]
        == {"R_uxux": -1, "R_uyuy": 1}
        and data["finite_data"]["nonzero_Riemann_component_count"] > 0,
        "the curved vacuum witness became flat",
    )
    require(
        data["claim_tiers"]["zero_stress_Lambda_zero_Einstein_equations_force_flatness"]
        == "CLOSED_NO_GO"
        and data["claim_tiers"]["double_return_plus_Lambda_zero_force_flatness"]
        == "CLOSED_NO_GO",
        "vacuum equations or double return were promoted to flatness selection",
    )
    require(
        data["finite_data"]["state_boundary_rows_available"] == 0
        and data["finite_data"]["state_boundary_rows_required"] == 5
        and data["claim_tiers"]["selected_zero_defect_state_or_boundary_rule"]
        == "OPEN_5_ROW_CONTRACT_0_AVAILABLE",
        "the state/boundary cutset changed",
    )
    require(
        not data["guardrails"]["claims_Lambda_eff_zero_selects_Minkowski"]
        and not data["guardrails"]["claims_double_return_excludes_gravitational_waves"],
        "a flat-vacuum guardrail changed",
    )
    print("Q79_ZERO_DEFECT_VACUUM_SELECTION_NOGO_STATE_CUTSET_AUDIT_PASS")


if __name__ == "__main__":
    main()
