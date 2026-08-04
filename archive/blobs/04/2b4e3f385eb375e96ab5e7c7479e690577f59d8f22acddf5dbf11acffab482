from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

DE_IMPORT = ROOT / "certificates" / "routec_de_action_on_smooth_bn_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_sector_projectors_dotd_on_smooth_bn_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_sector_projectors_dotd_on_smooth_bn_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_sector_projectors_dotd_on_smooth_bn_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_Sector_Projectors_DotD_on_Smooth_BN_Import_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    de_import = load(DE_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)
    validation = src["validation"]
    residuals = validation["projector_residuals"]
    straight = src["superset_mode"]["straight_path"]

    closed_now = {
        "previous_DE_action_imported": de_import["theorem"]["proved"],
        "sector_projectors_on_27_mode_BN_emitted": src_cert["what_closes"]["sector_projectors_on_27_mode_BN_emitted"],
        "dotD_alpha1_matrix_in_same_basis_emitted": src_cert["what_closes"]["dotD_alpha1_matrix_in_same_basis_emitted"],
        "horizontal_response_equation_passes_diagnostic_validator": src_cert["what_closes"]["horizontal_response_equation_passes_diagnostic_validator"],
        "projectors_are_idempotent_and_hermitian": src_cert["what_closes"]["projectors_are_idempotent_and_hermitian"],
        "family_kernel_dimension_three_retained": src_cert["what_closes"]["family_kernel_dimension_three_retained"],
        "higgs_kernel_dimension_one_retained": src_cert["what_closes"]["higgs_kernel_dimension_one_retained"],
        "target_fitting_excluded": src_cert["what_closes"]["target_fitting_excluded"],
    }

    algebra_checks = {
        "diagnostic_dotD_validator_passes": (
            validation["diagnostic_lift_validator_passes"] is True
            and validation["diagnostic_source_lift"]["exit_code"] == 0
        ),
        "honest_validator_does_not_promote": (
            validation["honest"]["exit_code"] == 1
            and validation["honest_validator_fails_only_by_source_driver_flags"] is True
        ),
        "projectors_exact": all(
            item["idempotence_residual"] == 0.0 and item["hermitian_residual"] == 0.0
            for item in residuals.values()
        ),
        "family_sector_ranks_three": all(residuals[sector]["rank_trace"] == 3.0 for sector in ("Q", "u", "d", "L", "e", "N")),
        "higgs_sector_rank_one": residuals["H"]["rank_trace"] == 1.0,
        "same_basis_dotD_emitted": straight["dotD_alpha1_matrix_emitted"] is True,
        "sector_projectors_emitted": straight["sector_projectors_on_BN_emitted"] is True,
    }

    still_open_checks = {
        "selected_dotD_source_verified_open": src["what_remains_open"]["selected_dotD_source_verified"] is True,
        "alpha1_driver_verified_open": src["what_remains_open"]["alpha1_driver_verified"] is True,
        "primitive_C1_overlap_contractions_open": src["what_remains_open"]["primitive_C1_overlap_contractions"] is True,
        "selected_source_flags_promoted_open": src["what_remains_open"]["selected_source_flags_promoted"] is True,
        "full_iwasawa_strominger_DE_open": src["what_remains_open"]["full_iwasawa_strominger_DE_not_only_model_active"] is True,
        "full_iwasawa_truncation_error_open": src["what_remains_open"]["full_iwasawa_truncation_error_certificate"] is True,
        "honest_replay_not_ready": src["what_remains_open"]["honest_replay_without_lifted_flags"] is True and straight["honest_replay_ready"] is False,
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
    }

    theorem = {
        "name": "RouteCSectorProjectorsDotDOnSmoothBNImportTheorem",
        "proved": all(closed_now.values()) and all(algebra_checks.values()) and all(still_open_checks.values()),
        "statement": (
            "On the same 27-mode smooth B_N scaffold, sector projectors and a "
            "finite dotD_alpha1 response packet are emitted. The diagnostic "
            "source-lift replay passes the q79 dotD response validator, proving "
            "finite horizontal-response consistency. Selected dotD source, "
            "alpha1 driver, primitive C1 contractions, and honest replay remain "
            "open."
        ),
    }

    verdict = {
        "sector_projectors_built": True,
        "dotD_alpha1_on_same_basis_built": True,
        "finite_horizontal_response_algebra_closed_conditionally": True,
        "selected_dotD_source_promotes": False,
        "alpha1_driver_promotes": False,
        "primitive_C1_overlap_contractions_closed": False,
        "R6_honest_replay_ready": False,
        "next_required_artifact": src["next_required_artifact"],
    }

    packet = {
        "theorem": theorem,
        "source_status": src["status"],
        "payloads": src["payloads"],
        "projector_residuals": residuals,
        "validation": validation,
        "closed_now": closed_now,
        "algebra_checks": algebra_checks,
        "still_open_checks": still_open_checks,
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C Sector Projectors and dotD on Smooth B_N Import v1

## Result

Sector projectors and `dotD_alpha1` response slots on the same 27-mode smooth
`B_N` basis have been imported.

Closed at the finite horizontal-response algebra level:

```text
Q,u,d,L,e,N projector rank = 3
H projector rank = 1
projectors are Hermitian and idempotent
dotPsi_i = -R Q dotD Psi_i passes diagnostic validation
diagnostic q79 dotD validator passes
```

## Boundary

The honest packet remains unpromoted. The source-critical flags are still not
theorem-derived:

```text
selected_dotD_source_verified
alpha1_driver_verified
primitive C1 overlap contractions
full Iwasawa/Strominger D_E rather than model active D_E
full truncation-error certificate
honest replay without lifted flags
```

## Status

```text
ROUTEC_SECTOR_PROJECTORS_DOTD_ON_SMOOTH_BN_IMPORTED_SOURCE_PROMOTION_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_C1_Primitive_Response_or_Selected_Source_Proof_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_sector_projectors_dotd_on_smooth_bn_import",
                "status": "ROUTEC_SECTOR_PROJECTORS_DOTD_ON_SMOOTH_BN_IMPORTED_SOURCE_PROMOTION_OPEN",
                "input_certificates": {
                    "routec_de_action_on_smooth_bn_import": str(DE_IMPORT),
                    "selected_routec_sector_projectors_dotd_on_smooth_bn": str(SRC_CERT),
                },
                "theorem": theorem,
                "closed_now": closed_now,
                "algebra_checks": algebra_checks,
                "still_open_checks": still_open_checks,
                "verdict": verdict,
                "packet_written": str(OUT_PACKET),
                "note_written": str(OUT_NOTE),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print("STATUS: ROUTEC_SECTOR_PROJECTORS_DOTD_ON_SMOOTH_BN_IMPORTED_SOURCE_PROMOTION_OPEN")


if __name__ == "__main__":
    main()
