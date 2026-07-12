from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "minimal_cln_gr_hessian_candidate_certificate.json"
DATA = ROOT / "candidate_data" / "minimal_cln_gr_hessian_candidate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))

    require(
        cert["status"] == "MINIMAL_CLN_GR_HESSIAN_FORMAL_CANDIDATE_PASSES_SOURCE_OPEN",
        "unexpected status",
    )
    checks = cert["checks"]
    for key in [
        "source_theorem_target_closed_source_open",
        "h_anchor_symmetric",
        "h_anchor_positive",
        "k_gr_symmetric",
        "tt_block_positive",
        "gauge_block_null",
        "no_tt_mixing",
        "retarded_atom_positive",
    ]:
        require(checks[key] is True, f"failed check: {key}")

    require(cert["formal_result"]["K_GR_rank"] == 2, "candidate rank should be 2")
    require(cert["formal_result"]["gauge_nullity"] == 4, "candidate gauge nullity should be 4")
    require(
        cert["formal_result"]["candidate_matches_required_rank_pattern"] is True,
        "candidate should match TT/gauge rank pattern",
    )
    require(data["K_GR"]["matrix"][0][0] == 1.0, "plus TT eigenvalue mismatch")
    require(data["K_GR"]["matrix"][1][1] == 1.0, "cross TT eigenvalue mismatch")
    require(all(value == 0.0 for value in data["K_GR"]["gauge_eigenvalues"]), "gauge eigenvalues not zero")

    status = cert["scientific_status"]
    require(status["is_selected_MTT_GR_Hessian"] is False, "must not claim selected Hessian")
    require(status["is_formal_minimal_candidate"] is True, "must remain formal candidate")
    guardrails = cert["guardrails"]
    require(guardrails["claims_full_GR_closure"] is False, "must not claim full GR")
    require(guardrails["claims_selected_H_anchor"] is False, "must not claim selected H")
    require(guardrails["claims_selected_P_GR"] is False, "must not claim selected P")

    print("AUDIT_PASS: minimal CLN GR Hessian candidate passes formal rank tests and remains source-open")


if __name__ == "__main__":
    main()

