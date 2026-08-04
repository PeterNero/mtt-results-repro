from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "q79_s3_strain_intertwiner_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    sources = cert["source_tests"]
    checks = cert["exact_checks"]
    scope = cert["scope"]
    guards = cert["guardrails"]

    require(all(sources.values()), "one or more corpus source tests failed")
    require(all(checks.values()), "one or more exact intertwiner checks failed")
    require(cert["projector_ranks"] == [1, 2, 3], "lane ranks are not 1+2+3")
    require(len(cert["equivariance_table"]) == 6, "not all S3 elements were checked")
    require(
        all(row["intertwining_residual_exactly_zero"] for row in cert["equivariance_table"]),
        "an S3 equivariance identity failed",
    )
    require(
        cert["theorem"]["computed_derivative"] == "DG(0)[delta f]=2 J(delta f)",
        "metric derivative formula changed",
    )
    require(
        "extension through the q79 branch locus" in scope["still_open"],
        "branch-locus boundary was lost",
    )
    require(guards["claims_global_HYM_intertwiner_closed"] is False, "HYM overclaim")
    require(guards["claims_physical_spacetime_metric_derived"] is False, "physical metric overclaim")
    require(guards["adds_fitted_numeric_parameter"] is False, "unexpected fitted parameter")

    print("AUDIT_PASS: q79 S3 strain intertwiner and local Q source are exact on the unbranched carrier")


if __name__ == "__main__":
    main()
