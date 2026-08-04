from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "exact_branch_internal_aint_gap_import_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(
        cert["status"] == "EXACT_BRANCH_INTERNAL_AINT_GAP_CLOSED_GR_TT_BRANCH_IDENTITY_OPEN",
        "unexpected status",
    )

    source = cert["source_tests"]
    imported = cert["exact_branch_import"]
    scope = cert["scope"]
    guards = cert["guardrails"]

    require(source["fixed_point_damping_theorem_defines_A_gap_on_Q"] is True, "fixed-point A gap missing")
    require(source["fixed_point_damping_kernel_uses_same_A"] is True, "fixed-point kernel/A relation missing")
    require(source["qg_Aint_gap_is_internal_noncoherent_gap"] is True, "QG Aint role missing")
    require(source["z64_exact_branch_hessian_kernel_certified"] is True, "Z64 exact Hessian not certified")
    require(source["z64_exact_branch_has_lambda15"] is True, "lambda 15 missing")
    require(source["z64_exact_branch_schur_leakage_zero"] is True, "Schur leakage should be zero")
    require(source["physical_action_internal_alpha_closed"] is True, "internal alpha should be closed")
    require(source["physical_absolute_normalization_closed"] is False, "physical absolutes must remain open")

    require(imported["lambda_star_internal"] == 15.0, "internal lambda mismatch")
    require(abs(imported["sqrt_lambda_star_internal"] - math.sqrt(15.0)) < 1e-15, "sqrt lambda mismatch")
    require(abs(imported["tau0_if_saturated"] - (1.0 / 15.0)) < 1e-15, "tau mismatch")
    require(imported["schur_correction"] == 0.0, "Schur correction should vanish")

    require(scope["can_use_as_exact_branch_internal_Aint_gap"] is True, "exact branch should be usable")
    require(scope["can_use_as_unconditional_GR_TT_gap"] is False, "GR TT gap must not be unconditional")
    require(scope["can_use_as_physical_dimensionful_gap"] is False, "physical gap must not close")
    require(cert["not_closed"]["unconditional_GR_TT_Aint_identity"] is True, "GR identity must remain open")
    require("lambda_star = 15" in note, "note lost exact branch value")

    require(guards["claims_unconditional_GR_TT_gap_15"] is False, "must not claim unconditional GR gap")
    require(guards["claims_physical_dimensionful_gap"] is False, "must not claim physical gap")
    require(guards["claims_Newton_or_Planck_prediction"] is False, "must not claim Newton/Planck")
    require(guards["claims_full_GR_response_closed"] is False, "must not claim full GR closure")

    print("AUDIT_PASS: exact-branch internal Aint gap closed; GR TT branch identity remains open")


if __name__ == "__main__":
    main()
