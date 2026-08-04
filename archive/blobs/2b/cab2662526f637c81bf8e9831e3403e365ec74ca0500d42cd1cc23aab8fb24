"""Audit Q79_VAlpha_Source_Frontier_Import_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "q79_valpha_source_frontier_import_certificate.json"
SCRIPT = REPO / "scripts" / "import_q79_valpha_source_frontier.py"
NOTE = REPO / "proof_corpus" / "Q79_VAlpha_Source_Frontier_Import_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return condition


def main() -> int:
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    script_cert = json.loads(proc.stdout)
    closed = cert["closed_now"]
    not_closed = cert["not_closed"]
    guards = cert["guardrails"]
    next_gate = cert["updated_next_gate"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "Q79_VALPHA_SOURCE_FRONTIER_IMPORTED_FINITE_EMISSION_BRIDGE_NEXT",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "frontier import agrees with local gate",
        closed["q79_frontier_imported"] is True
        and closed["q79_yoneda_promoted_to_AH_conditional"] is True
        and closed["direct_pic0_shortcut_not_available"] is True
        and closed["same_source_blocker_identified"] is True
        and closed["local_cross_repo_frontier_agrees"] is True,
        closed,
    )
    ok &= check(
        "next gate is q79-facing bridge",
        next_gate["name"] == "Q79_VAlpha_Source_Origin_and_Finite_Emission_Bridge_v1"
        and "Selected_Source_Certificate_or_BN_Basis_PhiFin_Payload_Fill_v1"
        in next_gate["relation_to_local_frontier"],
        next_gate,
    )
    ok &= check(
        "real closure remains open",
        not_closed["selected_visible_valpha_source"] is True
        and not_closed["selected_Pic0_rule"] is True
        and not_closed["selected_D_E_dotD_Riesz_Green"] is True
        and not_closed["primitive_C1_contractions"] is True,
        not_closed,
    )
    ok &= check(
        "guardrails prevent promotion",
        guards["claims_selected_visible_valpha_source"] is False
        and guards["claims_selected_Pic0_rule"] is False
        and guards["claims_selected_D_E_dotD"] is False
        and guards["claims_full_SM_closure"] is False
        and guards["uses_observed_flavor_data"] is False,
        guards,
    )
    ok &= check(
        "note records bridge",
        "Q79_VAlpha_Source_Origin_and_Finite_Emission_Bridge_v1" in note
        and "does not promote the selected source" in note,
        NOTE,
    )

    print("\nQ79 VAlpha source frontier import audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
