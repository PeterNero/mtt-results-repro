"""Audit the selected U1/Y Route-C matter-slot overlap normalization source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_matter_slot_overlap_normalization_source.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_matter_slot_overlap_normalization_source.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_matter_slot_overlap_normalization_source_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_MatterSlot_Overlap_Normalization_Source_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> None:
    if condition:
        print(f"PASS: {name} -- {detail}")
        return
    print(f"FAIL: {name} -- {detail}")
    raise SystemExit(1)


def clause(data: dict, name: str) -> dict:
    for item in data["theorem_clauses"]:
        if item["clause"] == name:
            return item
    raise KeyError(name)


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout)
    check("builder exits cleanly", proc.returncode == 0, proc.returncode)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    check(
        "status exact",
        data["status"] == "U1Y_ROUTEC_MATTERSLOT_OVERLAP_THEOREM_ATTEMPTED_REDUCED_TO_HYBRID_GALERKIN_SOURCE_PACKET",
        data["status"],
    )
    check(
        "theorem attempted but not closed",
        data["decision"]["theorem_closed"] is False
        and cert["theorem_closed"] is False
        and data["decision"]["conditional_route_exact"] is True,
        data["decision"],
    )
    check(
        "structural partition retained but not selected",
        data["decision"]["structural_partition_matches"] is True
        and data["decision"]["selected_source_independently_derives_route"] is False
        and data["structural_candidate"]["matches_required_partition"] is True,
        data["structural_candidate"],
    )
    check(
        "Z route remains source open",
        clause(data, "Z_to_u_e")["closed"] is False
        and clause(data, "Z_to_u_e")["evidence"]["matches_conditional_route"] is True
        and clause(data, "Z_to_u_e")["evidence"]["selected_source_independently_derives_route"] is False,
        clause(data, "Z_to_u_e"),
    )
    check(
        "X route blocked by nuD singlet rule",
        clause(data, "X_to_d_nuD")["closed"] is False
        and clause(data, "X_to_d_nuD")["evidence"]["matches_conditional_route"] is True
        and clause(data, "X_to_d_nuD")["evidence"]["selected_singlet_rule_closed"] is False,
        clause(data, "X_to_d_nuD"),
    )
    check(
        "normalization and overlap still open",
        clause(data, "selected_transfer_normalization")["closed"] is False
        and clause(data, "selected_overlap_transfer_functor")["closed"] is False
        and data["what_remains_open"]["selected_transfer_normalization"] is True,
        data["what_remains_open"],
    )
    check(
        "next hybrid packet named",
        data["decision"]["best_next_artifact"] == "Selected_U1Y_RouteC_Hybrid_Galerkin_Overlap_Source_Packet_v1"
        and cert["next_artifact"] == "Selected_U1Y_RouteC_Hybrid_Galerkin_Overlap_Source_Packet_v1",
        cert,
    )
    check(
        "guardrails hold",
        data["guardrails"]["uses_locked_target_columns_as_selector"] is False
        and data["guardrails"]["claims_A_selected"] is False
        and cert["lambda_12_closed"] is False
        and data["target_fitting_used"] is False,
        data["guardrails"],
    )
    check(
        "note records next packet and no closure",
        "Selected_U1Y_RouteC_Hybrid_Galerkin_Overlap_Source_Packet_v1" in note
        and "theorem_closed = false" in note
        and "Do not use locked target columns" in note,
        NOTE,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
