"""Build the central-cocycle map source-augmentation request for Qa/SU3."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

PROMOTION_FILL = DATA / "twisted_source_promotion_packet_fill_attempt.candidate.json"
PROMOTION_CERT = CERTS / "twisted_source_promotion_packet_fill_attempt_certificate.json"

OUTPUT_DATA = DATA / "central_cocycle_map_source_augmentation_request.candidate.json"
OUTPUT_CERT = CERTS / "central_cocycle_map_source_augmentation_request_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Central_Cocycle_Map_Source_Augmentation_Request_v1.md"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def build() -> tuple[dict[str, object], dict[str, object], str]:
    fill = load(PROMOTION_FILL)
    cert = load(PROMOTION_CERT)
    required_packet = {
        "source_identity": [
            "MTT selection rule for this exact Qa/SU3 branch",
            "source text or theorem naming the selected Deligne/Cech, B-field, finite quotient, or smooth representative",
            "statement that observed constants, residuals, masses, and mixings are not inputs",
        ],
        "representative": [
            "Cech cover or finite quotient used by the selected source",
            "local B_i potentials or Deligne cochains, or finite holonomy table",
            "period denominator, smooth unit, or exact normalization convention",
            "gauge-equivalence rule and invariant class",
        ],
        "central_cocycle_map": [
            "explicit map from representative/holonomy to the c-twist label",
            "cocycle law on overlaps or group multiplication",
            "orientation/complex-polarization convention matching the primitive slants",
            "proof that F_i and G_i carry opposite twists and P is untwisted",
        ],
        "admissibility": [
            "Green-Schwarz/Bianchi check for the mapped module",
            "Freed-Witten or anomaly-cancellation check for the twisted module",
            "HYM/stability/local-freeness policy for the exact source",
            "projector retention and zero-mode policy",
        ],
        "response_payload": [
            "projective rho_E generator matrices or smooth D_E/dotD blocks",
            "metric/unitarity compatibility",
            "Riesz/Green/heat/zeta/torsion finite part from the same source",
            "trace normalization and sector maps",
            "same-source bridge to monad g*f=0 if the monad route is used",
        ],
    }
    forbidden_shortcuts = [
        "direct q79/S3 finite tables without a same-branch Qa/SU3 map",
        "primitive slants without period denominator or smooth unit",
        "global gerbe existence without the central-cocycle action",
        "projective rho_E validator pass without selected rho_E entries",
        "Bianchi/HYM context without mapped Freed-Witten and projector checks",
        "fitting to observed constants, residuals, masses, or mixings",
    ]
    acceptance_tests = {
        "source_selected": False,
        "representative_supplied": False,
        "central_cocycle_map_verified": False,
        "period_or_smooth_unit_selected": False,
        "admissibility_mapped": False,
        "response_payload_supplied": False,
        "monad_bridge_checked_if_used": False,
        "qa_su3_packet_closed": False,
    }
    candidate = {
        "candidate": "SelectedQaSU3CentralCocycleMapSourceAugmentationRequest",
        "status": "QA_SU3_CENTRAL_COCYCLE_MAP_SOURCE_AUGMENTATION_REQUEST_BUILT_VALUES_OPEN",
        "input_status": {
            "promotion_fill_attempt": fill["status"],
            "promotion_certificate": cert["status"],
        },
        "problem_statement": cert["blocker"]["clean_statement"],
        "required_packet": required_packet,
        "forbidden_shortcuts": forbidden_shortcuts,
        "acceptance_tests": acceptance_tests,
        "minimal_success_criterion": "A selected representative plus a verified map to the central c-twist action, followed by at least one same-source projective rho_E or D_E/dotD finite response.",
        "route_split": {
            "source_augmentation_lane": "Ask the corpus/source to print the representative, period unit, cocycle map, admissibility checks, and response payload.",
            "derivation_lane": "Derive the same objects from the selected Hessian blocks and retarded overlap kernel, then prove the map is the selected source rather than a fitted response.",
        },
        "current_result": {
            "request_built": True,
            "values_filled": False,
            "closure_claimed": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": "Selected_Qa_SU3_Central_Cocycle_Map_Source_Search_or_Derivation_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": candidate["candidate"],
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "central_cocycle_gap_named": True,
            "required_source_packet_specified": True,
            "forbidden_shortcuts_specified": True,
            "source_augmentation_and_derivation_lanes_split": True,
        },
        "what_remains_open": acceptance_tests,
        "minimal_success_criterion": candidate["minimal_success_criterion"],
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = f"""# Selected Qa/SU3 Central Cocycle Map Source Augmentation Request v1

## Purpose

The previous promotion fill attempt located the true missing object:

```text
{candidate["problem_statement"]}
```

So this artifact narrows the next source request. We do not need another broad
gerbe search. We need the exact map from the selected representative to the
central c-twist action, plus one same-source response payload.

## Required Packet

```text
1. selected source identity and branch rule
2. Deligne/Cech, B-field, finite quotient, or smooth representative
3. period denominator or smooth unit
4. verified representative -> central cocycle/action map
5. Bianchi, Freed-Witten, HYM/stability, projector, and zero-mode checks
6. projective rho_E matrices or D_E/dotD blocks
7. finite heat, zeta, torsion, Green, or Riesz response from the same source
8. same-source bridge to g*f=0 if the monad route is used
```

## Forbidden

```text
q79/S3 values as direct Qa/SU3 proof,
primitive slants without the selected period unit,
global gerbe existence without the module action,
validator pass without selected entries,
Bianchi/HYM context without mapped anomaly/projector checks,
target fitting to observed constants.
```

## Two Live Lanes

```text
source-augmentation lane:
  print the representative, period unit, central map, admissibility checks,
  and response payload.

derivation lane:
  derive the same packet from selected Hessian blocks and retarded overlap
  kernel, then prove this derivation is source-selected.
```

Next artifact:

```text
{candidate["next_required_artifact"]}
```

closure claimed: no
target fitting used: no
"""
    return candidate, certificate, note


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
