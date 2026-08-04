"""Partially fill same-source alpha1 normalization using the proved source identity."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

BASE = DATA / "selected_samesource_alpha1_normalization_packet.fill_attempt.json"
VISIBLE_FILL = DATA / "visible_routec_sourceidentity_or_typedbn_derivative.partial_fill.json"
DOTD = DATA / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
VALIDATOR = ROOT / "scripts" / "validate_samesource_alpha1_normalization_packet.py"

OUTPUT = DATA / "selected_samesource_alpha1_normalization_packet.sourceidentity_partial_fill.json"
CERT = CERTS / "selected_samesource_alpha1_normalization_sourceidentity_partial_fill_certificate.json"
NOTE = CORPUS / "MTT_Selected_SameSourceAlpha1_Normalization_SourceIdentityPartialFill_v1.md"

STATUS = "MTT_SELECTED_SAMESOURCE_ALPHA1_NORMALIZATION_SOURCEIDENTITY_PARTIAL_FILL_DRIVER_OPEN"
NEXT = "MTT_Selected_Alpha1_SourceStrengthCoordinate_or_TransferNormalization_Fill_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    try:
        parsed = json.loads(proc.stdout)
    except json.JSONDecodeError:
        parsed = {"raw_output": proc.stdout}
    parsed["exit_code"] = proc.returncode
    return parsed


def build_note(data: dict[str, Any]) -> str:
    return f"""# MTT Selected Same-Source Alpha1 Normalization Source-Identity Partial Fill v1

Status: `{STATUS}`

Next artifact: `{NEXT}`

## Result

The same-source alpha1 normalization packet now imports the theorem-derived
source identity from the visible Route-C partial fill. This closes the
`source_identity` field for the normalization packet without using observed
constants, benchmark entries, or lifted flags.

The packet still does not validate. That is intentional and important: the
remaining fields require an actual selected source-strength coordinate or a
typed transfer normalization, not the coordinate convention
`N(f)=<f,h_ext>/||h_ext||^2`.

## Remaining Fields

- `source_strength_coordinate`: still not selected; `lambda_alpha1=1` remains a
  unit candidate until the source emits the coordinate.
- `normalization_functional`: still not selected; the current dual functional
  is canonical once `h_ext` is chosen, but it is not an MTT-selected
  normalization.
- `tangent_equality`: numerically exact for the candidate `h_ext`, but not a
  selected equality until `h_selected_alpha1` is emitted.
- `sector_dotd_equality`: the source-only validator still fails exactly by
  `alpha1_driver_verified`.

## Validator

```json
{json.dumps(data["validation"], indent=2, sort_keys=True)}
```
"""


def main() -> int:
    base = load(BASE)
    visible = load(VISIBLE_FILL)
    dotd = load(DOTD)

    packet = copy.deepcopy(base)
    packet["status"] = STATUS
    packet["next_required_artifact"] = NEXT
    packet["closure_claimed"] = False
    packet["target_fitting_used"] = False

    source_identity = visible["lane_A_visible_routec_source_identity"]["source_identity"]
    if not (
        source_identity["selected_emitted"] is True
        and source_identity["same_branch"] is True
        and source_identity["theorem_derived"] is True
    ):
        raise RuntimeError("visible source identity is not theorem-promoted")

    packet["source_identity"] = {
        "selected_emitted": True,
        "same_source": True,
        "theorem_derived": True,
        "provenance": "symbolic_transport_conjugation_theorem",
        "certificate_path": source_identity["certificate_path"],
        "support_present": True,
        "support_source": source_identity["support_source"],
        "theorem": source_identity["theorem"],
        "selected_flags": {
            "source_identity": True,
            "visible_routec_operator_source": True,
            "selected_by_mtt": True,
        },
        "reason_selected": "The symbolic transport-conjugation theorem promotes the stationary visible/Route-C source identity on the locked q79/F,m=1 branch.",
    }

    packet["source_strength_coordinate"]["same_source"] = True
    packet["source_strength_coordinate"]["support_present"] = True
    packet["source_strength_coordinate"]["reason_not_selected"] = (
        "The source identity is now selected, but the source-strength coordinate itself is still not emitted by the selected branch."
    )
    packet["normalization_functional"]["same_source"] = True
    packet["normalization_functional"]["reason_not_selected"] = (
        "The canonical L2 dual is compatible with the selected source identity, but remains a coordinate functional unless selected transfer normalization is emitted."
    )
    packet["tangent_equality"]["same_source"] = True
    packet["tangent_equality"]["theorem_derived"] = True
    packet["tangent_equality"]["reason_not_selected"] = (
        "The transport derivative formula and h_ext solve are theorem-derived, but the selected physical alpha1 tangent has not been emitted."
    )
    packet["sector_dotd_equality"]["same_source"] = True
    packet["sector_dotd_equality"]["source_only_fails_only_by_alpha1_driver"] = dotd["validator_boundary"][
        "source_only_fails_only_by_alpha1_driver"
    ]

    packet["partial_fill_result"] = {
        "source_identity_selected": True,
        "source_strength_coordinate_selected": False,
        "normalization_functional_selected": False,
        "tangent_equality_selected": False,
        "sector_dotd_equality_selected": False,
        "alpha1_driver_verified": False,
    }
    packet["promotion_result"] = {
        "selected_value_emitted": False,
        "alpha1_driver_verified": False,
        "honest_dotd_validator_closed": False,
        "target_fitting_used": False,
    }

    packet["validation"] = {"ok": False, "errors": ["validation pending"]}
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    packet["validation"] = run_validator(OUTPUT)
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": "MTTSelectedSameSourceAlpha1NormalizationSourceIdentityPartialFill",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "validator_path": rel(VALIDATOR),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "source_identity_selected": True,
        "remaining_fields": [
            "source_strength_coordinate",
            "normalization_functional",
            "tangent_equality",
            "sector_dotd_equality",
        ],
        "alpha1_driver_verified": False,
        "validator_ok": packet["validation"]["ok"],
        "validator_exit_code": packet["validation"]["exit_code"],
    }
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(build_note(packet), encoding="utf-8")
    print(json.dumps({"status": STATUS, "candidate": rel(OUTPUT), "certificate": rel(CERT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
