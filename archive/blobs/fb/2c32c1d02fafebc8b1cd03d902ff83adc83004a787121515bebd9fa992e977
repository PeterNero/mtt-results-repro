from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "stieltjes_massless_gaussian_no_go_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    tiers = cert["claim_tiers"]
    impact = cert["paper_impact"]
    guards = cert["guardrails"]

    require(all(cert["checks"].values()), "one or more three-way no-go checks failed")
    require(
        cert["status"]
        == "POSITIVE_STIELTJES_MASSLESS_POLE_AND_PERMANENT_GAUSSIAN_PROPAGATOR_DAMPING_CLOSED_INCOMPATIBLE",
        "three-way no-go status changed",
    )
    require(all(row["lower_exceeds_upper"] for row in cert["numeric_witnesses"]), "crossing witness failed")
    require(tiers["three_way_incompatibility"] == "CLOSED", "three-way no-go lost")
    require(impact["qg_main_three_claim_conjunction"] == "CLOSED_NO_GO", "paper impact lost")
    require(tiers["all_loop_UV_finiteness_with_positive_massless_spectrum"] == "OPEN_NOT_PROVED", "UV claim overpromoted")
    require(guards["claims_all_loop_finiteness_survives_unchanged"] is False, "all-loop overclaim")
    require(guards["claims_full_QG_closed"] is False, "full QG overclaim")

    print(
        "AUDIT_PASS: positive spectral density, a massless pole, and permanent "
        "Gaussian propagator damping cannot all hold"
    )


if __name__ == "__main__":
    main()
