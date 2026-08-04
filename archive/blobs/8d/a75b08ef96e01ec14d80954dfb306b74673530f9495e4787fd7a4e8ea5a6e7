"""Audit the selected HYM adjoint-transfer functor artifact."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_hym_adjoint_transfer_functor.candidate.json"
CERT = ROOT / "certificates" / "selected_hym_adjoint_transfer_functor_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_HYM_Adjoint_Transfer_Functor_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_HYM_ADJOINT_TRANSFER_FUNCTOR_BUILT_FINITE_IDENTIFICATION_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim full closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    require(data["straight_path"]["rank2_source"]["rank"] == 2, "source must be rank 2")
    require(data["straight_path"]["functor"]["rank"] == 3, "adjoint carrier must be rank 3")
    require(data["straight_path"]["functor"]["continuous_parameters_added"] == 0, "functor must add no knobs")
    require(data["straight_path"]["functor"]["gauge_functorial"] is True, "functoriality missing")
    require(
        data["what_closes_now"]["abstract_rank2_to_rank3_transfer_functor"] is True,
        "abstract transfer should close",
    )
    require(
        data["what_remains_open"]["End0_finite_basis_identification_with_qutrit_BN"] is True,
        "finite basis identification must remain open",
    )
    require(data["finite_galerkin_layout"]["rank2_Hermitian_endomorphism_unknowns_at_BN_level"] == 81, "wrong H unknown dimension")
    require(data["finite_galerkin_layout"]["rank2_connection_correction_unknowns_six_real_directions"] == 486, "wrong connection dimension")
    require(data["finite_galerkin_layout"]["first_solve_coefficients_emitted"] is False, "must not emit coefficients")
    require(cert["abstract_rank2_to_rank3_transfer_functor"] is True, "certificate should close abstract functor")
    require(cert["finite_basis_identification_closed"] is False, "certificate must keep finite basis open")
    require("This adds no continuous parameter" in proof, "proof must state no knob")
    require("finite basis/isomorphism problem" in proof, "proof must state remaining finite problem")

    print("PASS selected HYM adjoint-transfer functor audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
