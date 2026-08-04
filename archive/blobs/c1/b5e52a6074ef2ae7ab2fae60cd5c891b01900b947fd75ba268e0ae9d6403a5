from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

BN_IMPORT = ROOT / "certificates" / "routec_smooth_bn_galerkin_lift_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_de_action_on_smooth_bn_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_de_action_on_smooth_bn.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_de_action_on_smooth_bn_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_de_action_on_smooth_bn_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_DE_Action_on_Smooth_BN_Import_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    bn_import = load(BN_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)
    validation = src["validation"]
    matrix = validation["matrix_consistency"]
    straight = src["superset_mode"]["straight_path"]

    honest_text = "\n".join(validation["honest"]["output"])
    diagnostic_text = "\n".join(validation["diagnostic_source_lift"]["output"])

    closed_now = {
        "previous_smooth_BN_scaffold_imported": bn_import["theorem"]["proved"],
        "D_E_matrix_on_27_mode_BN_emitted": src_cert["what_closes"]["D_E_matrix_on_27_mode_BN_emitted"],
        "diagnostic_source_lift_passes_existing_q79_validator": src_cert["what_closes"]["diagnostic_source_lift_passes_existing_q79_validator"],
        "family_kernel_dimension_three_emitted": src_cert["what_closes"]["family_kernel_dimension_three_emitted"],
        "higgs_kernel_dimension_one_emitted": src_cert["what_closes"]["higgs_kernel_dimension_one_emitted"],
        "stiffness_equals_DstarD": src_cert["what_closes"]["stiffness_equals_DstarD"],
        "zero_mode_bases_ordered": src_cert["what_closes"]["zero_mode_bases_ordered"],
        "target_fitting_excluded": src_cert["what_closes"]["target_fitting_excluded"],
    }

    validator_checks = {
        "diagnostic_validator_passes": (
            validation["diagnostic_source_lift"]["exit_code"] == 0
            and "D_E action validation PASS" in diagnostic_text
            and straight["diagnostic_lift_passes"] is True
        ),
        "honest_validator_does_not_promote": (
            validation["honest"]["exit_code"] == 1
            and "selected_source_verified is not true" in honest_text
            and straight["honest_validator_promotes"] is False
        ),
        "domain_dimension_27": matrix["domain_dimension"] == 27,
        "family_kernel_dimension_3": matrix["family_kernel_dimension"] == 3,
        "family_range_dimension_24": matrix["family_range_dimension"] == 24,
        "higgs_kernel_dimension_1": matrix["higgs_kernel_dimension"] == 1,
        "higgs_range_dimension_26": matrix["higgs_range_dimension"] == 26,
        "honest_fails_only_by_selected_source_flags": matrix["honest_validator_fails_only_by_selected_source_flags"] is True,
    }

    still_open_checks = {
        "selected_D_E_source_promotion_open": src["what_remains_open"]["selected_D_E_source_promotion"] is True,
        "full_iwasawa_strominger_DE_action_open": src["what_remains_open"]["full_iwasawa_strominger_DE_action_not_only_model_active"] is True,
        "full_iwasawa_truncation_error_open": src["what_remains_open"]["full_iwasawa_truncation_error_certificate"] is True,
        "sector_projectors_open": src["what_remains_open"]["sector_projectors"] is True,
        "dotD_alpha1_open": src["what_remains_open"]["dotD_alpha1_in_same_basis"] is True,
        "R6_replay_open": src["what_remains_open"]["R6_replay_without_lifted_flags"] is True,
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
    }

    theorem = {
        "name": "RouteCDEActionOnSmoothBNImportTheorem",
        "proved": all(closed_now.values()) and all(validator_checks.values()) and all(still_open_checks.values()),
        "statement": (
            "A finite D_E matrix realization on the 27-mode smooth B_N scaffold "
            "has been emitted. The diagnostic source-lift packet passes the "
            "existing q79 validator, closing matrix, Gram, stiffness, and "
            "zero-mode consistency. The honest packet remains unpromoted because "
            "selected_source_verified is not theorem-derived and the operator is "
            "still the model active D_E rather than the full selected "
            "Iwasawa/Strominger action."
        ),
    }

    verdict = {
        "D_E_matrix_on_27_mode_BN_built": True,
        "diagnostic_validator_passes": True,
        "honest_source_promotes": False,
        "full_selected_DE_action_closed": False,
        "sector_projectors_closed": False,
        "dotD_alpha1_closed": False,
        "R6_honest_replay_ready": False,
        "next_required_artifact": src["next_required_artifact"],
    }

    packet = {
        "theorem": theorem,
        "source_status": src["status"],
        "payloads": src["payloads"],
        "validation": validation,
        "closed_now": closed_now,
        "validator_checks": validator_checks,
        "still_open_checks": still_open_checks,
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C D_E Action on Smooth B_N Import v1

## Result

The finite `D_E` action on the 27-mode smooth `B_N` scaffold has been imported.

Closed at the matrix-consistency level:

```text
domain dimension = 27
family kernel dimension = 3
family range dimension = 24
Higgs kernel dimension = 1
Higgs range dimension = 26
stiffness = D_E^* D_E
zero-mode bases ordered
diagnostic q79 validator passes
```

## Boundary

The honest packet still does not promote. Its validator fails because
`selected_source_verified` is not theorem-derived for the sectors. The current
operator is also still the model active `D_E`, not yet the full selected
Iwasawa/Strominger action with truncation-error certificate.

Still open:

```text
selected D_E source promotion
full Iwasawa/Strominger D_E action
full truncation-error certificate
sector projectors
dotD_alpha1 in the same basis
honest R6 replay without lifted flags
```

## Status

```text
ROUTEC_DE_ACTION_ON_SMOOTH_BN_IMPORTED_SOURCE_PROMOTION_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_Sector_Projectors_and_DotD_on_Smooth_BN_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_de_action_on_smooth_bn_import",
                "status": "ROUTEC_DE_ACTION_ON_SMOOTH_BN_IMPORTED_SOURCE_PROMOTION_OPEN",
                "input_certificates": {
                    "routec_smooth_bn_galerkin_lift_import": str(BN_IMPORT),
                    "selected_routec_de_action_on_smooth_bn": str(SRC_CERT),
                },
                "theorem": theorem,
                "closed_now": closed_now,
                "validator_checks": validator_checks,
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
    print("STATUS: ROUTEC_DE_ACTION_ON_SMOOTH_BN_IMPORTED_SOURCE_PROMOTION_OPEN")


if __name__ == "__main__":
    main()
