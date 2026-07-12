from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "actual_shape_map_factorization_reduction_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    qg = cert["qg_sources"]
    checks = cert["finite_checks"]
    theorem = cert["reduction_theorem"]
    remaining = cert["remaining"]
    residuals = cert["finite_residuals"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "DRESSED_SHAPE_MAP_REDUCED_TO_CORE_B0_SAME_ANGLE_FACTORISATION",
        "unexpected status",
    )
    require(qg["B_defined_as_DG_Pi_coh"] is True, "B definition source missing")
    require(qg["B_factorization_sourced"] is True, "B factorization source missing")
    require(qg["B0_bounded_sourced"] is True, "B0 bounded source missing")
    require(qg["E_Aint_commute_sourced"] is True, "E/Aint commutation source missing")
    require(qg["Aint_gap_sourced"] is True, "Aint gap source missing")
    require(qg["central_finite_subgroup_sourced"] is True, "central finite subgroup source missing")
    require(all(checks.values()), "finite checks must pass")
    require(theorem["proved_conditionally"] is True, "conditional reduction theorem should close")
    require("B0^*P_TT" in theorem["what_closes"], "must reduce to B0 core")
    require(residuals["projection_residual"] < 1e-12, "projection residual too large")
    require(residuals["det_core_C"] != 0, "core C should be invertible in model")

    require(remaining["source_status"] == "CORE_B0_SAME_ANGLE_FACTORISATION_OPEN", "B0 source gate should remain")
    require("B0^*P_TT=U_TT C" in remaining["minimal_remaining_statement"], "minimal remaining statement wrong")
    packet = remaining["direct_computation_packet"]
    require(packet["test_1"] == "rank(U_TT^* B0^*P_TT)=2", "rank test missing")
    require(packet["test_2"] == "(I-Pi_exact64)B0^*P_TT=0", "projection test missing")
    require(packet["test_3"] == "central shift intertwining residual is zero", "intertwining test missing")

    require(guards["claims_B0_factorization_sourced"] is False, "must not claim B0 factorization sourced")
    require(guards["claims_unconditional_final_support"] is False, "must not claim final support")
    require(guards["uses_observed_GR_data"] is False, "must not use observed data")
    require(guards["adds_numeric_knob"] is False, "must not add knob")
    require(guards["lets_SPT_dressing_select_support"] is False, "SPT dressing must not select support")

    require("retarded kernel, SPT damping" in note, "note should explain what is no longer mysterious")
    print("AUDIT_PASS: dressed shape map reduced to core B0 same-angle factorization")


if __name__ == "__main__":
    main()
