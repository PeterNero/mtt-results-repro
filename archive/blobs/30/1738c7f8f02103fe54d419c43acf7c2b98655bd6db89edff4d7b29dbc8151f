"""Audit the selected U1/Y Route-C same-source operator-packet fill/no-go gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_samesource_operatorpacket_fill_or_nogo.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_samesource_operatorpacket_fill_or_nogo.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_samesource_operatorpacket_fill_or_nogo_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1.md"


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
    fields = data["attempted_selected_packet"]["fields"]

    check(
        "status exact",
        data["status"] == "U1Y_ROUTEC_SAMESOURCE_OPERATORPACKET_FILL_NOGO_CURRENT_SCAFFOLDS_SUPPORT_ONLY",
        data["status"],
    )
    check(
        "fill counts exact",
        data["fill_summary"]["required_fields"] == 7
        and data["fill_summary"]["support_present"] == 6
        and data["fill_summary"]["selected_emitted"] == 0
        and cert["selected_emitted"] == 0,
        data["fill_summary"],
    )
    check(
        "validator fails honestly",
        data["validator_report"]["exit_code"] == 1
        and data["validator_report"]["ok"] is False
        and cert["validator_ok"] is False,
        data["validator_report"],
    )
    check(
        "all attempted fields remain unselected",
        all(row["selected_emitted"] is False for row in fields.values())
        and all(row["same_source"] is False for row in fields.values())
        and all(row["theorem_derived"] is False for row in fields.values()),
        fields,
    )
    check(
        "forbidden provenance is retained as blocker evidence",
        fields["source_identity"]["provenance"] == "support_shape_only"
        and fields["singlet_neutrino_rule"]["provenance"] == "support_shape_only"
        and fields["overlap_transfer"]["provenance"] == "locked_target_selection"
        and fields["normalization"]["provenance"] == "locked_target_selection",
        {key: fields[key]["provenance"] for key in fields},
    )
    check(
        "q79 valpha/s3 remains open and imported only as support",
        data["u1y_binding"]["q79_valpha_s3_status"]
        == "SELECTED_QA_SU3_SAME_SOURCE_VALPHA_S3_OPERATOR_PACKET_ATTEMPT_OPEN"
        and data["u1y_binding"]["q79_valpha_s3_open_item_count"] >= 20,
        data["u1y_binding"],
    )
    check(
        "current scaffold no-go scoped",
        data["current_source_nogo"]["current_scaffold_nogo_proved"] is True
        and data["current_source_nogo"]["mathematical_impossibility_claimed"] is False
        and cert["mathematical_impossibility_claimed"] is False,
        data["current_source_nogo"],
    )
    check(
        "next minimal packet exact",
        data["next_required_artifact"] == "Selected_U1Y_RouteC_SourceEmission_MinimalSubpacket_AttackPlan_v1"
        and cert["next_required_artifact"] == "Selected_U1Y_RouteC_SourceEmission_MinimalSubpacket_AttackPlan_v1",
        cert,
    )
    check(
        "guardrails hold",
        data["guardrails"]["target_fitting_used"] is False
        and data["guardrails"]["locked_target_selector_used"] is False
        and data["guardrails"]["fixture_promoted"] is False
        and data["guardrails"]["claims_lambda12"] is False
        and cert["lambda_12_closed"] is False,
        data["guardrails"],
    )
    check(
        "note records no-go and next artifact without lambda claim",
        "current_scaffold_nogo_proved = true" in note
        and "Selected_U1Y_RouteC_SourceEmission_MinimalSubpacket_AttackPlan_v1" in note
        and "`lambda_12`, and full closure remain open" in note,
        NOTE,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
