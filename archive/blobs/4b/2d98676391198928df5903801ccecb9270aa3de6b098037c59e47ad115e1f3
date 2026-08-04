"""Audit the alpha1 source-strength normalization theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_alpha1_source_strength_normalization_theorem.py"
CANDIDATE = ROOT / "candidate_data" / "selected_alpha1_source_strength_normalization_theorem.candidate.json"
CERT = ROOT / "certificates" / "selected_alpha1_source_strength_normalization_theorem_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Alpha1_SourceStrength_Normalization_Theorem_v1.md"

STATUS = "MTT_SELECTED_ALPHA1_SOURCE_STRENGTH_NORMALIZATION_THEOREM_BUILT_VALUE_OPEN"
NEXT = "MTT_Selected_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1"


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
    theorem = data["theorem"]
    evidence = data["current_evidence"]
    status = data["current_status"]
    criterion = data["acceptance_criterion"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check("certificate path", cert["candidate_path"].endswith(CANDIDATE.name), cert),
        check(
            "theorem built",
            theorem["proved"] is True
            and theorem["closure_claimed"] is False
            and "same-branch source-strength normalization" in theorem["statement"],
            theorem,
        ),
        check(
            "criterion complete",
            criterion["necessary_and_sufficient_for_current_branch"] is True
            and len(criterion["must_emit"]) >= 5
            and "renaming the continuous Ext-density scale as alpha1" in criterion["forbidden_shortcuts"],
            criterion,
        ),
        check(
            "support evidence correct",
            evidence["selected_projector_riesz_green_source_replay_closed"] is True
            and evidence["transport_dotd_source_formula_closed"] is True
            and evidence["dotd_matrices_pass_if_driver_theorem_supplied"] is True
            and evidence["naive_continuous_scale_identification_rejected"] is True,
            evidence,
        ),
        check(
            "driver still not promoted",
            status["alpha1_driver_verified_now"] is False
            and status["honest_dotd_validator_closed_now"] is False
            and cert["alpha1_driver_verified"] is False
            and cert["honest_dotd_validator_closed"] is False,
            status,
        ),
        check(
            "no target fitting or closure",
            data["target_fitting_used"] is False
            and data["closure_claimed"] is False
            and cert["target_fitting_used"] is False
            and cert["closure_claimed"] is False,
            cert,
        ),
        check(
            "next gate recorded",
            data["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note
            and "normalization value is not emitted yet" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected alpha1 source-strength normalization theorem audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
