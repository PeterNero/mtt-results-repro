from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "target_independent_dimensional_anchor_candidates_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "DIMENSIONAL_ANCHOR_CANDIDATES_CLASSIFIED_NO_PHYSICAL_CLOSURE",
        "unexpected status",
    )
    verdict = cert["verdict"]
    guards = cert["guardrails"]
    candidates = {row["id"]: row for row in cert["candidate_table"]}

    require(verdict["internal_scale_lift_available"] is True, "internal scale lift should be available")
    require(verdict["physical_dimensionful_anchor_available"] is False, "physical anchor should remain open")
    require(verdict["newton_or_planck_prediction_allowed_now"] is False, "Newton/Planck prediction should not be allowed")
    require("E_topological_flux_integer_minimization_plus_rhoUV" in candidates, "best route should be present")
    require(
        candidates["E_topological_flux_integer_minimization_plus_rhoUV"]["classification"]
        == "BEST_OPEN_ROUTE_DIMENSIONLESS_MINIMIZER_CLOSED_DIMENSIONAL_ANCHOR_MISSING",
        "best route classification changed",
    )
    require(candidates["B_newton_backsolve"]["classification"] == "FORBIDDEN_FOR_PREDICTION", "backsolve should be forbidden")
    require(guards["claims_physical_GN"] is False, "must not claim physical G_N")
    require(guards["claims_dimensional_anchor_closed"] is False, "must not claim anchor closure")
    require(guards["forbids_target_backsolve"] is True, "target backsolve must be forbidden")

    print("AUDIT_PASS: target-independent dimensional-anchor candidates classified; no physical closure")


if __name__ == "__main__":
    main()
