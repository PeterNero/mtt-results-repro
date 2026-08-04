from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "q79_trial_branch_irreducibility_and_spin_decision_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    witness = cert["exact_witness"]
    decision = cert["decision"]
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]

    require(all(cert["checks"].values()), "one or more trial branch checks failed")
    require(witness["norm_degree"] == 36, "elliptic norm degree changed")
    require(
        witness["norm_factorization_over_Q"]["factors"]
        == [{"degree": 36, "multiplicity": 1}],
        "elliptic norm is no longer irreducible",
    )
    require(witness["squarefree_gcd_degree"] == 0, "elliptic norm is not square-free")
    require(
        decision["trial_identity_alignment"]["strict_Spin"] == "NO_GO",
        "trial strict-Spin decision changed",
    )
    require(
        tiers["selected_alignment_in_irreducible_locus"] == "OPEN",
        "trial result was silently promoted to the selected alignment",
    )
    require(
        guards["promotes_trial_alignment_to_selected"] is False,
        "trial alignment was promoted",
    )
    require(
        guards["claims_selected_q79_strict_Spin_no_go"] is False,
        "selected strict-Spin no-go was overclaimed",
    )

    print(
        "AUDIT_PASS: the identity-alignment branch is exactly irreducible with "
        "strict Spin obstructed, while selected-alignment membership remains open"
    )


if __name__ == "__main__":
    main()
