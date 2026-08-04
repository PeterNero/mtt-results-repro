"""Audit q79 selected visible operator or primitive C1 target import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
SCRIPT = ROOT / "scripts" / "import_q79_selected_visible_operator_or_primitive_c1_target.py"
PACKET = DATA / "q79_selected_visible_operator_or_primitive_c1_target_import.candidate.json"
CERT = CERTS / "q79_selected_visible_operator_or_primitive_c1_target_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_Selected_Visible_Operator_or_Primitive_C1_Target_Import_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load(PACKET)
    cert = load(CERT)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("script runs", proc.returncode == 0, proc.stdout)
    script_cert = json.loads(proc.stdout)

    expected = "Q79_SELECTED_VISIBLE_OPERATOR_OR_PRIMITIVE_C1_TARGET_IMPORTED"
    check("certificate status", cert["status"] == expected, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem imported", cert["theorem"]["proved"] is True, cert["theorem"])
    check("all import checks pass", all(packet["import_checks"].values()), packet["import_checks"])

    source = packet["source_lane"]
    check(
        "source lane open at selected source",
        source["validator_exit_code"] == 2
        and "selected_by_mtt must be true" in source["open_items"]
        and "source_certificate missing" in source["open_items"]
        and source["ordered_source_passes"]
        and source["s3_class_passes"],
        source,
    )

    c1 = packet["primitive_c1_lane"]
    check(
        "primitive C1 atoms fully enumerated and missing",
        c1["contract_atom_count"] == 24
        and c1["missing_atom_count"] == 24
        and len(c1["missing_atoms"]) == 24,
        c1,
    )

    scan = packet["missing_data_scan"]
    check(
        "missing scan blocks at selected operator source",
        scan["first_blocking_layer"] == "selected_operator_source"
        and scan["can_compute_now"]["actual_selected_C1_matrices"] is False
        and scan["can_compute_now"]["full_SM_closure"] is False,
        scan,
    )

    check(
        "next gate exact",
        cert["verdict"]["next_required_artifact"]
        == "Q79_Selected_DE_Green_DotD_Source_for_Primitive_C1_v1"
        and packet["decision"]["selected_DE_rhoE_Riesz_Green_dotD_not_closed"],
        packet["decision"],
    )
    check(
        "guardrails retained",
        cert["guardrails"]["does_not_claim_selected_operator_source_constructed"]
        and cert["guardrails"]["does_not_claim_primitive_C1_values_computed"]
        and cert["guardrails"]["does_not_claim_selected_C1_response_matrices"]
        and cert["guardrails"]["does_not_claim_full_SM_closure"]
        and cert["guardrails"]["does_not_use_observed_or_benchmark_inputs"],
        cert["guardrails"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check("note records 24 primitive matrices", "24 selected" in note, NOTE)

    print("\nQ79 selected visible operator or primitive C1 target import audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
