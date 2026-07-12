"""Audit selected sector zero-mode adjoint-triplet realization theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_sector_zero_mode_adjointtriplet_realization_theorem.py"
CANDIDATE = ROOT / "candidate_data" / "selected_sector_zero_mode_adjointtriplet_realization_theorem.candidate.json"
CERT = ROOT / "certificates" / "selected_sector_zero_mode_adjointtriplet_realization_theorem_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SectorZeroMode_AdjointTriplet_Realization_Theorem_v1.md"

STATUS = "MTT_SELECTED_SECTOR_ZEROMODE_ADJOINT_TRIPLET_THEOREM_PROVED_SOURCE_ACTION_OPEN"
NEXT = "MTT_Selected_SectorZeroMode_End0Action_Matrix_or_MatterSlotRouting_Value_Fill_v1"


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
    model = data["checked_adjoint_model"]
    hypotheses = data["hypotheses_still_to_emit"]
    boundary = data["conclusion_boundary"]

    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "theorem proved",
            data["theorem"]["proved"] is True
            and cert["theorem_proved"] is True
            and cert["conditional_representation_choice_closed"] is True,
            data["theorem"],
        ),
        check(
            "su2 bracket model",
            all(model["lie_checks"].values()) and all(model["skew_checks"].values()),
            model,
        ),
        check(
            "adjoint generator ranks",
            all(row["rank"] == 2 and row["frob2"] == 2 for row in model["rank_checks"].values()),
            model["rank_checks"],
        ),
        check(
            "source action honestly open",
            hypotheses["selected_End0_action_source_map_rho_s"] is False
            and hypotheses["rho_s_bracket_preserving"] is False
            and hypotheses["rho_s_irreducible_or_rank_two_nonabelian"] is False
            and cert["selected_source_action_open"] is True,
            hypotheses,
        ),
        check(
            "conditional closes only representation choice",
            boundary["adjoint_triplet_representation_choice_closed_conditionally"] is True
            and boundary["Higgs_singlet_representation_choice_closed_conditionally"] is True
            and boundary["selected_zero_mode_packet_emitted"] is False
            and boundary["physical_dotD_alpha1_payload_extracted"] is False,
            boundary,
        ),
        check(
            "superset path constrained not fitted",
            data["superset_combined_path"]["uses_observed_constants"] is False
            and data["superset_combined_path"]["locked_or_constrained_target"] == "rank pattern 6*3+1 and End0 adjoint/singlet representation class",
            data["superset_combined_path"],
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
            "next artifact",
            data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT,
            data["next_required_artifact"],
        ),
        check(
            "note records theorem boundary",
            "The representation-choice freedom is removed" in note
            and "What Remains Open" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected sector zero-mode adjoint-triplet realization theorem audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
