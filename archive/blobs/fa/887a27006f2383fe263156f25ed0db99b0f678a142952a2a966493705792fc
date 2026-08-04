"""Audit the constants-repo m1 Chern-Weil source-route import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "constants_m1_cw_source_route_import_certificate.json"
CANDIDATE = REPO / "candidate_data" / "constants_m1_cw_source_route_import.candidate.json"
NOTE = REPO / "proof_corpus" / "Constants_M1_CW_Source_Route_Import_v1.md"
SCRIPT = REPO / "scripts" / "import_constants_m1_cw_source_route.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")

    statuses = cert["input_statuses"]
    target = cert["target_alignment"]
    h1 = cert["h1_bridge"]
    payload = cert["payload_alignment"]
    closed = cert["closed_now"]
    still_open = cert["still_open"]
    guardrails = cert["guardrails"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "CONSTANTS_M1_CW_SOURCE_ROUTE_IMPORTED_H1_COMPATIBLE_SOURCE_OPEN",
            cert["status"],
        ),
        check(
            "script recomputes certificate",
            computed["target_alignment"] == target
            and computed["h1_bridge"] == h1
            and computed["payload_alignment"] == payload,
            computed["status"],
        ),
        check(
            "constants source route imported",
            statuses["constants_cw_attempt"]
            == "QA_SU3_M1_CW_OPERATOR_SOURCE_ATTEMPT_RANK2_EXT_H1_DATA_OPEN"
            and target["constants_primary_route"] == "non_split_rank2_V_alpha_extension"
            and target["constants_primary_route_status"] == "PRIMARY_LIVE_SOURCE_ROUTE",
            statuses,
        ),
        check(
            "target matches q79 V_alpha route",
            target["targets_match"] is True
            and target["constants_target"] == target["q79_target"]
            and target["q79_target"]["l_vector_abc"] == [1, -2, 0]
            and target["q79_target"]["c2_extension_alpha_coeffs"] == [4, 0, 0],
            target,
        ),
        check(
            "h1 bridge compatible",
            h1["original_h1"] == 8
            and h1["conditional_promoted_h1"] == 8
            and h1["original_promotes_selected_data"] is False
            and h1["conditional_promoted_selected_data"] is True
            and h1["compatible_with_constants_h1_template"] is True,
            h1,
        ),
        check(
            "payload starts at source certificate",
            payload["first_unfilled_payload_item"] == "selected_source_certificate"
            and payload["q79_parity_rule_available"] is True
            and payload["common_payload_order"][0] == "selected_source_certificate",
            payload,
        ),
        check(
            "closed and open sets honest",
            all(closed.values())
            and still_open["selected_source_certificate"] is True
            and still_open["same_source_D_E_dotD_Riesz_Green"] is True
            and still_open["full_SM_closure"] is True,
            {"closed": closed, "open": still_open},
        ),
        check(
            "no promotion overclaim",
            guardrails["claims_constants_source_promotes_q79_flags"] is False
            and guardrails["claims_h1_fixture_is_selected_now"] is False
            and guardrails["claims_selected_D_E_dotD_constructed"] is False
            and guardrails["claims_full_sm_closure"] is False,
            guardrails,
        ),
        check(
            "note records alignment",
            "non_split_rank2_V_alpha_extension" in note
            and "h1(X,L^2) = 8" in note
            and "does not promote selected-source flags" in note,
            NOTE,
        ),
        check(
            "candidate matches certificate",
            candidate["target_alignment"] == cert["target_alignment"]
            and candidate["verdict"] == cert["verdict"],
            candidate["status"],
        ),
    ]

    print("\nConstants m1 Chern-Weil source-route import audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
