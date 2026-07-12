"""Audit Cross_Repo_Update_Chain_and_Next_Gate_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "cross_repo_update_chain_and_next_gate_certificate.json"
SCRIPT = REPO / "scripts" / "import_cross_repo_update_chain_and_next_gate.py"
NOTE = REPO / "proof_corpus" / "Cross_Repo_Update_Chain_and_Next_Gate_v1.md"


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
    caveat = cert["external_update_caveat"]
    frontier = cert["updated_local_frontier"]
    not_closed = cert["not_closed"]
    guards = cert["guardrails"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "CROSS_REPO_UPDATES_IMPORTED_SOURCE_PROMOTION_AND_DOTD_C1_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "all repos scanned and local state known",
        closed["all_five_repos_scanned"] is True
        and closed["local_repo_state_captured_at_scan"] is True
        and len(cert["repo_states"]) == 5,
        cert["repo_states"],
    )
    ok &= check(
        "external dirty caveat recorded",
        caveat["sm_parity_closure_has_uncommitted_update_batch"] is True
        and "provisional" in caveat["import_status"],
        caveat,
    )
    ok &= check(
        "SM-parity chain imported as reduction",
        closed["sm_parity_same_source_chain_imported_as_reduction"] is True
        and closed["sm_parity_routec_de_matrix_on_bn_available_as_unpromoted_artifact"] is True,
        closed,
    )
    ok &= check(
        "local next gate sharpened",
        frontier["old_frontier"] == "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1"
        and frontier["new_frontier"] == "Selected_Source_Certificate_or_BN_Basis_PhiFin_Payload_Fill_v1",
        frontier,
    )
    ok &= check(
        "real closure remains open",
        not_closed["source_promotion_without_lifted_flags"] is True
        and not_closed["same_branch_dotD_alpha1_in_same_basis"] is True
        and not_closed["selected_C1_response"] is True
        and not_closed["full_SM_closure"] is True,
        not_closed,
    )
    ok &= check(
        "guardrails prevent overclaim",
        guards["claims_external_dirty_artifacts_are_final"] is False
        and guards["claims_selected_source_promotion_now"] is False
        and guards["claims_dotD_C1_yukawa_closure"] is False
        and guards["claims_full_SM_closure"] is False
        and guards["uses_observed_cp_sign_or_masses"] is False,
        guards,
    )
    ok &= check(
        "note records chain and boundary",
        "Selected_Source_Certificate_or_BN_Basis_PhiFin_Payload_Fill_v1" in note
        and "27-mode BN D_E matrix" in note
        and "does not treat external dirty artifacts as final baselines" in note,
        NOTE,
    )

    print("\nCross-repo update chain and next gate audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
