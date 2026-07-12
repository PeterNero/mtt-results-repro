from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "tt_closure_strain_to_z64_tower_map_attempt_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(
        cert["status"] == "TT_TO_Z64_MAP_CONDITIONAL_COMPRESSION_CLOSED_SOURCE_FUNCTOR_OPEN",
        "unexpected status",
    )

    source = cert["source_tests"]
    theorem = cert["conditional_theorem"]
    results = cert["results"]
    guards = cert["guardrails"]

    require(source["formal_GR_TT_operator_scalar_on_two_polarizations"] is True, "TT scalar form not closed")
    require(source["formal_GR_TT_basis_plus_cross_sourced"] is True, "TT plus/cross basis not sourced")
    require(source["z64_exact_branch_lambda15_closed"] is True, "Z64 lambda=15 not closed")
    require(source["z64_exact_branch_schur_zero"] is True, "Z64 Schur leakage not zero")
    require(source["z64_exact_branch_retarded_kernel_closed"] is True, "Z64 retarded kernel not closed")
    require(source["z64_source_selects_single_tower_label"] is True, "selected tower label not detected")
    require(source["z64_source_declares_l64_tower_operator"] is True, "L64 tower operator not detected")
    require(source["source_has_TT_to_Z64_polarization_functor"] is False, "TT-to-Z64 functor unexpectedly sourced")
    require(source["source_identifies_GR_TT_eta_with_15"] is False, "eta=15 unexpectedly sourced")
    require(source["final_gate_already_exhausted_identity_source"] is True, "final identity gate not exhausted")

    require(theorem["closed_algebraically"] is True, "conditional algebra should close")
    require(theorem["closed_unconditionally_from_sources"] is False, "unconditional closure must remain open")
    require("15 * I_2" in theorem["calculation"], "conditional compression lost 15 I2")

    require(results["conditional_compression_theorem_closed"] is True, "conditional compression not closed")
    require(results["exact_branch_gap_15_remains_closed"] is True, "exact branch gap should remain closed")
    require(results["TT_two_polarization_form_remains_closed"] is True, "TT two-polarization form should remain closed")
    require(results["unconditional_TT_to_Z64_map_closed"] is False, "unconditional TT/Z64 map must remain open")
    require(results["full_GR_TT_gap_15_closed"] is False, "full GR TT gap must remain open")
    require(
        results["minimum_missing_object"] == "TT_Polarization_Functor_into_Exact_Z64_Branch",
        "wrong missing object",
    )
    require("not another scalar" in results["why_missing_object_is_not_numeric"], "missing-object diagnosis weakened")

    require("U_TT^* L_64 U_TT = 15 I_2" in note, "note lost conditional compression formula")
    require("full GR has lambda_star=15" in note, "note lost guardrail")

    require(guards["claims_unconditional_GR_TT_gap_15"] is False, "must not claim full GR gap")
    require(guards["claims_Z64_eigenspace_two_dimensional"] is False, "must not claim Z64 degeneracy")
    require(guards["claims_TT_to_Z64_functor_sourced"] is False, "must not claim functor is sourced")
    require(guards["claims_physical_dimensionful_gap"] is False, "must not claim physical gap")
    require(guards["claims_Newton_or_Planck_prediction"] is False, "must not claim Newton/Planck")

    print("AUDIT_PASS: conditional TT-to-Z64 compression closed; source functor remains open")


if __name__ == "__main__":
    main()
