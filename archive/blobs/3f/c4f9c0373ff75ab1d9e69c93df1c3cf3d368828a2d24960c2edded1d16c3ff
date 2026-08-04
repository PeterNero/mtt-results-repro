from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "q79_shared_circle_spinc_determinant_bridge_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    checks = cert["checks"]
    finite = cert["finite_data"]
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]

    require(all(checks.values()), "one or more determinant-bridge checks failed")
    require(
        cert["status"]
        == "Q79_SPINC_DETERMINANT_SHARED_Z64_TWO_TORSION_BRIDGE_CLOSED_ROOT_INDEPENDENT_SAME_SOURCE_HYM_OPEN",
        "determinant-bridge status changed",
    )
    require(
        finite["hom_generator_images"] == [0, 32],
        "Hom(Z6,Z64) generator images changed",
    )
    require(
        finite["root_restriction_phase_exponents_mod64"]["1"]
        == finite["branch_sign_phase_exponents_mod64"],
        "chi1 no longer restricts to branch sign",
    )
    require(
        finite["root_restriction_phase_exponents_mod64"]["33"]
        == finite["branch_sign_phase_exponents_mod64"],
        "chi33 no longer restricts to branch sign",
    )
    require(
        finite["TT_restriction_phase_exponents_mod64"] == [0] * 6,
        "TT weight two is no longer trivial on the central image",
    )
    require(
        tiers["SpinC_determinant_shared_line_flat_connection_identification"]
        == "CLOSED_FOR_THE_UNIQUE_NONTRIVIAL_CENTRAL_MAP",
        "flat determinant/shared-line bridge was lost",
    )
    require(
        tiers["chi1_vs_chi33_selection_needed_for_determinant"] == "NO",
        "a spurious root selector was introduced",
    )
    require(tiers["MTT_same_source_emission_of_central_map"] == "OPEN", "same-source overclaim")
    require(
        guards["claims_physical_transverse_line_identified"] is False,
        "external transverse line was overclaimed",
    )
    require(
        guards["claims_final_integral_branch_selected"] is False,
        "final integral branch was overclaimed",
    )

    print(
        "AUDIT_PASS: the SpinC determinant is the root-independent shared-Z64 "
        "central restriction; same-source, transverse, and HYM promotion remain open"
    )


if __name__ == "__main__":
    main()
