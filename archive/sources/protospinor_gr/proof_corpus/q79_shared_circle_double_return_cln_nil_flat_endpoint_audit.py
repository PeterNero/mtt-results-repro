from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "q79_shared_circle_double_return_cln_nil_flat_endpoint_certificate.json"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(CERT.read_text(encoding="utf-8"))
    require(all(data["checks"].values()), "a double-return/flat-endpoint check failed")
    require(
        data["finite_data"]["unique_nontrivial_central_halfturn"] == 32,
        "the selected half-turn changed",
    )
    require(
        data["finite_data"]["odd_root_character_sequences"]
        == {"1": [1, -1, 1], "33": [1, -1, 1]},
        "the root-independent double return changed",
    )
    require(
        data["finite_data"]["metric_character_sequence"] == [1, 1, 1],
        "metric blindness changed",
    )
    require(
        data["finite_data"]["folded_nil_cohomology_dimension"] == 0
        and data["finite_data"]["folded_nil_differential_rank"] == 2,
        "the canonical C2 Nil complex is no longer acyclic",
    )
    require(
        data["claim_tiers"]["same_source_CLN_operator_roles"]
        == "CLOSED_EXACT_AT_FINITE_OPERATOR_TIER",
        "the finite CLN role theorem changed",
    )
    require(
        data["claim_tiers"]["double_return_alone_forces_zero_metric_strain"]
        == "CLOSED_NO_GO",
        "double return was silently promoted to a flatness selector",
    )
    require(
        data["finite_data"]["metric_counterexample"]
        == [[4, 0, 0], [0, "1/4", 0], [0, 0, 1]],
        "the nonzero invariant metric witness changed",
    )
    require(
        data["claim_tiers"]["canonical_zero_defect_Minkowski_coframe"]
        == "CLOSED_EXACT"
        and data["finite_data"]["teleparallel_torsion_nonzero_components"] == 0
        and data["finite_data"]["Levi_Civita_Riemann_nonzero_components"] == 0,
        "the exact flat zero-defect endpoint changed",
    )
    require(
        data["claim_tiers"]["Lambda_eff_zero"] == "OPEN"
        and data["claim_tiers"]["double_return_dynamically_selects_zero_defect"]
        == "OPEN",
        "an open physical-selection boundary was overpromoted",
    )
    require(
        not data["guardrails"]["claims_flat_spacetime_has_no_time_or_space"]
        and not data["guardrails"]["claims_double_return_forces_Q_WW_identity"],
        "flat spacetime or double return was misinterpreted",
    )
    print("Q79_SHARED_CIRCLE_DOUBLE_RETURN_CLN_NIL_FLAT_ENDPOINT_AUDIT_PASS")


if __name__ == "__main__":
    main()
