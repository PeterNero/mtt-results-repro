"""Audit the U1/Y Route-C source-emission minimal subpacket attack plan."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_sourceemission_minimal_subpacket_attack_plan.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_sourceemission_minimal_subpacket_attack_plan.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_sourceemission_minimal_subpacket_attack_plan_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_SourceEmission_MinimalSubpacket_AttackPlan_v1.md"

STATUS = "U1Y_ROUTEC_SOURCEEMISSION_MINIMAL_SUBPACKET_ATTACK_PLAN_BUILT"
NEXT = "Selected_U1Y_RouteC_OperatorSourceIdentity_Bridge_Subpacket_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> None:
    if condition:
        print(f"PASS: {name} -- {detail}")
        return
    print(f"FAIL: {name} -- {detail}")
    raise SystemExit(1)


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout)
    check("builder exits cleanly", proc.returncode == 0, proc.returncode)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    order = data["strategy"]["dependency_order"]
    contract = data["acceptance_contract"]

    check("status exact", data["status"] == STATUS and cert["status"] == STATUS, data["status"])
    check(
        "four ordered source-emission subpackets",
        [item["priority"] for item in order] == [1, 2, 3, 4]
        and [item["id"] for item in order]
        == [
            "S1_source_identity_bridge",
            "S2_operator_values_payload",
            "S3_matter_overlap_payload",
            "S4_primitive_contractions_payload",
        ],
        order,
    )
    check(
        "first subpacket exact",
        data["next_required_artifact"] == NEXT
        and cert["next_required_artifact"] == NEXT
        and order[0]["next_artifact"] == NEXT,
        cert,
    )
    check(
        "q79 update retained",
        order[0]["retired_old_blockers"]["selected_valpha_attempt_no_longer_blocks_on_ordered_source_validator"] is True
        and order[0]["current_blockers"]["selected_valpha_open_items"] >= 20,
        order[0],
    )
    check(
        "operator source before overlap",
        "operator-source identity" in order[0]["reason"].lower()
        and "D_E" in " ".join(order[1]["must_emit"])
        and "matter-slot" in order[2]["reason"].lower()
        and order[3]["id"] == "S4_primitive_contractions_payload",
        [item["reason"] for item in order],
    )
    check(
        "same-source validator acceptance explicit",
        contract["must_make_same_source_validator_pass"] is True
        and contract["required_field_flags"]["selected_emitted"] is True
        and contract["required_field_flags"]["same_source"] is True
        and contract["required_field_flags"]["theorem_derived"] is True
        and contract["packet_flags"]["observed_data_used"] is False
        and contract["packet_flags"]["target_fitting_used"] is False,
        contract,
    )
    check(
        "forbidden provenance list strict",
        {"support_shape_only", "locked_target_selection", "unselected_fixture", "lifted_flag"}.issubset(
            set(contract["forbidden_provenance"])
        ),
        contract["forbidden_provenance"],
    )
    check(
        "guarded no closure",
        data["closure_claimed"] is False
        and data["target_fitting_used"] is False
        and cert["closure_claimed"] is False
        and cert["lambda_12_closed"] is False,
        cert,
    )
    check(
        "note records next gate and acceptance",
        NEXT in note
        and "selected_emitted = true" in note
        and "operator-source identity bridge" in note,
        NOTE,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
