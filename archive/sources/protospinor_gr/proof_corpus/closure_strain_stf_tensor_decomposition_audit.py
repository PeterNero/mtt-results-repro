from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "closure_strain_stf_tensor_decomposition_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "CLOSURE_STRAIN_STF_TENSOR_DECOMPOSITION_CLOSED_SELECTED_HESSIAN_OPEN",
        "unexpected status",
    )
    decomp = cert["decomposition"]
    tt = cert["tt_reduction"]
    guardrails = cert["guardrails"]

    require(decomp["full_decomposition_rank"] == 9, "strain decomposition should span 9D strain space")
    require(decomp["decomposition_closed"] is True, "decomposition should be closed")
    require(tt["constraint_rank"] == 7, "physical TT constraints should have rank 7")
    require(tt["physical_dimension"] == 2, "TT physical sector should be two-dimensional")
    require(tt["plus_satisfies_constraints"] is True, "plus mode should satisfy constraints")
    require(tt["cross_satisfies_constraints"] is True, "cross mode should satisfy constraints")
    require(tt["plus_cross_independent"] is True, "plus/cross should be independent")
    require(tt["tt_basis_closed"] is True, "TT basis should be closed")
    require(guardrails["claims_selected_MTT_Hessian"] is False, "must not claim selected Hessian")
    require(guardrails["claims_full_GR_closed"] is False, "must not claim full GR closure")

    print("AUDIT_PASS: closure-strain tensor decomposition closes the STF/TT algebraic route")


if __name__ == "__main__":
    main()
