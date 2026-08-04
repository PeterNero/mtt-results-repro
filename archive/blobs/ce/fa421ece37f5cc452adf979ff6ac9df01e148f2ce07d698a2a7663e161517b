from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "world_in_world_z64_metric_source_map_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    checks = cert["checks"]
    construction = cert["construction"]
    uniqueness = cert["uniqueness"]
    scope = cert["scope"]
    guards = cert["guardrails"]

    require(all(checks.values()), "one or more metric-source checks failed")
    require(
        cert["status"]
        == "EXPLICIT_DG_AND_EXACT_SUPPORT_CLOSED_FOR_CONSTRUCTED_REALIZATION_UNIQUE_MTT_SELECTION_OPEN",
        "metric-source status changed",
    )
    require(
        construction["support_identity"]
        == "Pi_exact64 DG(0)^*P_TT=DG(0)^*P_TT",
        "support identity missing",
    )
    metric_c = construction["core_factorization_matrix_C_for_metric_g"]
    require(abs(metric_c[0][0] - 2.0) < 1.0e-12, "metric normalization mismatch")
    require(abs(metric_c[1][1] - 2.0) < 1.0e-12, "metric normalization mismatch")
    require(abs(metric_c[0][1]) < 1.0e-12, "metric normalization is not diagonal")
    require(abs(metric_c[1][0]) < 1.0e-12, "metric normalization is not diagonal")
    strain_c = construction["core_factorization_matrix_C_for_log_strain"]
    require(abs(strain_c[0][0] - 1.0) < 1.0e-12, "strain normalization mismatch")
    require(abs(strain_c[1][1] - 1.0) < 1.0e-12, "strain normalization mismatch")
    require(
        uniqueness["computed_real_dimension_before_normalization"] == 2,
        "intertwiner uniqueness dimension mismatch",
    )
    require(
        len(scope["not_yet_an_unconditional_MTT_selection_theorem"]) == 4,
        "selection boundary was lost",
    )
    require(guards["claims_all_MTT_realizations_must_use_this_G"] is False, "selection overclaim")
    require(guards["claims_dimensionful_GR_gap_or_Newton_constant"] is False, "metrology overclaim")
    require(guards["adds_fitted_numeric_parameter"] is False, "unexpected fitted parameter")

    print("AUDIT_PASS: actual DG and exact TT support are computed for the explicit Z64 world-in-world realization")


if __name__ == "__main__":
    main()
