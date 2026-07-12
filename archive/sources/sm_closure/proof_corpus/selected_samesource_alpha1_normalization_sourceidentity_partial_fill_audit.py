"""Audit source-identity partial fill for same-source alpha1 normalization."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_samesource_alpha1_normalization_sourceidentity_partial_fill.py"
CANDIDATE = ROOT / "candidate_data" / "selected_samesource_alpha1_normalization_packet.sourceidentity_partial_fill.json"
CERT = ROOT / "certificates" / "selected_samesource_alpha1_normalization_sourceidentity_partial_fill_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SameSourceAlpha1_Normalization_SourceIdentityPartialFill_v1.md"

STATUS = "MTT_SELECTED_SAMESOURCE_ALPHA1_NORMALIZATION_SOURCEIDENTITY_PARTIAL_FILL_DRIVER_OPEN"
NEXT = "MTT_Selected_Alpha1_SourceStrengthCoordinate_or_TransferNormalization_Fill_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    source = data["source_identity"]
    result = data["partial_fill_result"]
    validation = data["validation"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "source identity selected",
            source["selected_emitted"] is True
            and source["same_source"] is True
            and source["theorem_derived"] is True
            and source["provenance"] == "symbolic_transport_conjugation_theorem",
            source,
        ),
        check(
            "remaining fields not promoted",
            result["source_strength_coordinate_selected"] is False
            and result["normalization_functional_selected"] is False
            and result["tangent_equality_selected"] is False
            and result["sector_dotd_equality_selected"] is False
            and cert["alpha1_driver_verified"] is False,
            result,
        ),
        check(
            "validator still fails on real blockers",
            validation["ok"] is False
            and validation["exit_code"] == 1
            and "source_identity: selected_emitted is not true" not in validation["errors"]
            and any("source_strength_coordinate" in e for e in validation["errors"])
            and any("normalization_functional" in e for e in validation["errors"])
            and any("sector_dotd_equality" in e for e in validation["errors"]),
            validation,
        ),
        check(
            "no closure or target fitting",
            data["closure_claimed"] is False
            and data["target_fitting_used"] is False
            and cert["closure_claimed"] is False
            and cert["target_fitting_used"] is False,
            cert,
        ),
        check(
            "next gate recorded",
            data["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note
            and "`source_strength_coordinate`" in note,
            NOTE,
        ),
    ]

    print("\nMTT same-source alpha1 normalization source-identity partial fill audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
