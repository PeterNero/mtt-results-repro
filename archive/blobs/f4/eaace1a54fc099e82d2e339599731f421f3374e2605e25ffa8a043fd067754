"""Audit the selected HYM gauge-fixed representative / Galerkin solve gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_hym_gaugefixed_connection_or_galerkin_solve.candidate.json"
CERT = ROOT / "certificates" / "selected_hym_gaugefixed_connection_or_galerkin_solve_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_HYM_GaugeFixed_Connection_Representative_or_Galerkin_Solve_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_HYM_GAUGEFIXED_CONNECTION_OR_GALERKIN_SOLVE_SPEC_BUILT_SOLVE_VALUES_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    require(data["gauge_fixed_hym_problem"]["formulated"] is True, "gauge-fixed HYM problem not formulated")
    require(data["gauge_fixed_hym_problem"]["rank"] == 2, "straight HYM object should be rank 2")
    require(data["gauge_fixed_hym_problem"]["analytic_representative_emitted"] is False, "analytic representative must remain open")
    require(data["finite_newton_galerkin_contract"]["built"] is True, "finite solve contract not built")
    require(data["finite_newton_galerkin_contract"]["basis_dimension"] == 27, "expected 27-mode support scaffold")
    require(data["finite_newton_galerkin_contract"]["values_emitted"] is False, "must not emit solve values")
    require(data["first_solve_attempt"]["attempted"] is True, "first solve attempt missing")
    require(data["first_solve_attempt"]["closed"] is False, "first solve must not close")
    require(data["first_solve_attempt"]["blocked_before_numeric_values"] is True, "numeric blocker not recorded")
    require(
        data["what_remains_open"]["rank2_HYM_to_rank3_sector_operator_functor"] is True,
        "rank2-to-sector functor should remain open",
    )
    require(data["what_closes_now"]["rank2_vs_rank3_type_mismatch_exposed"] is True, "type mismatch not exposed")
    require(
        data["next_required_artifact"] == "MTT_Selected_HYM_NewtonGalerkin_FirstSolve_or_Rank2SectorFunctor_v1",
        "wrong next artifact",
    )
    require(cert["first_solve_closed"] is False, "certificate must keep solve open")
    require(cert["rank2_to_sector_functor_emitted"] is False, "certificate must keep transfer functor open")
    require("No selected finite operator values are promoted" in proof, "proof must state no promotion")
    require("rank-2-to-sector transfer functor" in proof, "proof must name type-transfer gate")

    print("PASS selected HYM gauge-fixed connection / Galerkin solve audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
