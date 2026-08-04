from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "absolute_normalization_bridge_from_nonsm_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "INTERNAL_GR_NORMALIZATION_CARRIED_HOME_PHYSICAL_ABSOLUTE_ANCHOR_OPEN",
        "unexpected status",
    )
    internal = cert["closed_internal_units"]
    physical = cert["physical_absolute_status"]
    current = cert["relation_to_current_GR_branch"]
    guards = cert["guardrails"]

    require(internal["G10_int"] == 1.0, "canonical internal G10 should be 1")
    require(internal["alpha_int"] == 1.0, "canonical internal alpha should be 1")
    require(len(internal["computed_rows"]) >= 3, "expected internal tested rows")
    require(all(row["kappa_STF_int"] > 0 for row in internal["computed_rows"]), "kappa_STF_int should be positive")
    require(physical["physical_absolute_dimensionful_predictions_closed"] is False, "physical absolute closure must remain open")
    require(physical["no_go_without_external_dimensional_anchor"] is True, "no-go should be active")
    require(current["kappa_not_independent"] is True, "kappa should not be independent")
    require(current["absolute_GR_gate_is_same_as_nonsm_gate"] is True, "gate should match non-SM gate")
    require(current["new_GR_specific_free_parameter_introduced"] is False, "must not introduce a new GR free parameter")
    require(guards["claims_measured_Newton_constant"] is False, "must not claim measured Newton constant")
    require(guards["claims_physical_absolute_dimensionful_closure"] is False, "must not claim physical absolute closure")
    require(guards["claims_internal_dimensionless_normalization_closure"] is True, "internal closure should be claimed")

    print("AUDIT_PASS: internal GR normalization closes; physical absolute anchor remains open")


if __name__ == "__main__":
    main()
