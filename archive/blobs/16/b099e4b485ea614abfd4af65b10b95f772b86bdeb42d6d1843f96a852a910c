from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_hym_value_solve_attempt_certificate.json"
STATUS = "SELECTED_HYM_VALUE_SOLVE_ATTEMPT_BLOCKED_COEFFICIENTS_AND_RANK2_SECTOR_FUNCTOR_OPEN"
NEXT = "MTT_Selected_HYM_NewtonGalerkin_FirstSolve_or_Rank2SectorFunctor_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected value-solve status")
    require(cert["theorem"]["name"] == "SelectedHYMValueSolveAttemptNoGo", "wrong theorem")
    require(cert["theorem"]["proved"] is True, "value-solve no-go theorem should be proved")
    require(cert["theorem"]["closure_claimed"] is False, "must not claim closure")
    require(all(cert["checks"].values()), "all checks should pass")
    require(all(cert["what_closes_now"].values()), "all current closure flags should be true")
    require(all(cert["what_remains_open"].values()), "remaining blockers should be explicit")
    require(all(cert["guardrails"].values()), "all guardrails should hold")
    require(cert["legal_value_solve_closed"] is False, "legal value solve must remain open")
    require(cert["next_required_artifact"] == NEXT, "wrong next artifact")

    routes = cert["attempted_routes"]
    require(routes["direct_selected_hym_connection"]["closed"] is False, "direct HYM route must be open")
    require(routes["finite_newton_galerkin"]["closed"] is False, "finite Newton route must be open")
    require(routes["finite_newton_galerkin"]["values_emitted"] is False, "values must not be emitted")
    require(routes["route_c_residual_bypass"]["formal_lift_rejected"] is True, "formal lift must be rejected")
    require(routes["phifin_alpha1_payload"]["closed"] is False, "Phi_fin alpha1 must remain open")
    require(routes["rank2_to_sector_transfer"]["closed"] is False, "rank2-to-sector functor must remain open")

    require(packet["gauge_fixed_problem"]["rank"] == 2, "HYM source should be rank 2")
    require(packet["finite_newton_galerkin_contract"]["basis_dimension"] == 27, "expected 27-mode scaffold")
    require(packet["source_alpha1_reduction"]["repair_object"] == "SelectedPhiFinAlpha1Payload", "wrong repair object")
    require("The value solve was attempted" in note, "note must record attempt")
    require("Formal lifted flags and smoke" in note, "note must reject forbidden proof")
    require(STATUS in note and NEXT in note, "note must record status and next artifact")

    print("AUDIT_PASS: selected HYM value solve attempted; selected coefficients and rank2-sector functor remain open")


if __name__ == "__main__":
    main()
