"""Audit the selected U1/Y Route-C finite cochain source construct."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_finite_cochain_source_construct.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_finite_cochain_source_construct.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_finite_cochain_source_construct_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_Finite_Cochain_Source_Construct_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> None:
    if condition:
        print(f"PASS: {name} -- {detail}")
        return
    print(f"FAIL: {name} -- {detail}")
    raise SystemExit(1)


def by_name(data: dict, name: str) -> dict:
    for item in data["construct_checks"]:
        if item["name"] == name:
            return item
    raise KeyError(name)


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout)
    check("builder exits cleanly", proc.returncode == 0, proc.returncode)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    packet = data["construct_packet"]

    check(
        "status exact",
        data["status"] == "U1Y_ROUTEC_FINITE_COHCHAIN_CONSTRUCT_BUILT_REDUCED_TO_MATTERSLOT_OVERLAP_SOURCE",
        data["status"],
    )
    check(
        "finite construct executed but source not closed",
        data["decision"]["finite_construct_executed"] is True
        and data["decision"]["finite_cochain_source_closed"] is False
        and cert["finite_cochain_source_closed"] is False,
        data["decision"],
    )
    check(
        "conditional Weyl-pair algebra closes",
        by_name(data, "weylpair_conditional_operator")["closed"] is True
        and packet["routec_weylpair_operator"]["shape"] == [72, 2]
        and packet["routec_weylpair_operator"]["rank"] == 2
        and packet["routec_weylpair_operator"]["is_A_selected"] is False,
        packet["routec_weylpair_operator"],
    )
    check(
        "source level carrier closed but operator promotion open",
        by_name(data, "source_level_weyl_carrier")["closed"] is True
        and packet["source_level_carrier"]["source_level_projective_class_selected"] is True
        and packet["source_level_carrier"]["operator_level_projective_rhoE_promoted"] is False,
        packet["source_level_carrier"],
    )
    check(
        "matter slot overlap theorem is first source gap",
        by_name(data, "sector_charge_and_overlap_normalization")["closed"] is False
        and data["decision"]["best_next_artifact"] == "Selected_U1Y_RouteC_MatterSlot_Overlap_Normalization_Source_v1"
        and "selected transfer normalization" in " ".join(packet["matter_slot_overlap_gap"]["must_prove"]),
        packet["matter_slot_overlap_gap"],
    )
    check(
        "same-source promotion still refuses honest packet",
        by_name(data, "same_source_operator_promotion")["closed"] is False
        and "selected_by_mtt must be true" in by_name(data, "same_source_operator_promotion")["evidence"]["honest_current_open_items"],
        by_name(data, "same_source_operator_promotion")["evidence"],
    )
    check(
        "lambda and target fitting forbidden",
        cert["lambda_12_closed"] is False
        and data["target_fitting_used"] is False
        and data["guardrails"]["do_not_use_locked_target_columns_as_source_selector"] is True,
        data["guardrails"],
    )
    check(
        "note records next object",
        "Selected_U1Y_RouteC_MatterSlot_Overlap_Normalization_Source_v1" in note
        and "finite_cochain_source_closed = false" in note
        and "Do not promote hypothetical selected flags" in note,
        NOTE,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
