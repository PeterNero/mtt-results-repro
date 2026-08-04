"""Audit the electroweak two-key fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_electroweak_two_key_fill_attempt.py"
DATA = REPO / "candidate_data" / "selected_electroweak_two_key_fill_attempt.candidate.json"
CERT = REPO / "certificates" / "selected_electroweak_two_key_fill_attempt_certificate.json"
U1_FILL = REPO / "candidate_data" / "selected_electroweak_u1y_local_determinant_key.fill_attempt.json"
ALPHA_FILL = REPO / "candidate_data" / "selected_electroweak_physical_action_anchor_key.fill_attempt.json"
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_Two_Key_FillAttempt_v1.md"

STATUS = "ELECTROWEAK_TWO_KEY_FILL_ATTEMPT_CURRENT_CORPUS_KEYS_OPEN"
NEXT = "Selected_Electroweak_U1Y_OperatorRow_or_DimensionalAnchor_SourceAugmentation_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    u1 = json.loads(U1_FILL.read_text(encoding="utf-8"))
    alpha = json.loads(ALPHA_FILL.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")

    decision = data["decision"]
    u1_attempt = data["u1y_local_determinant_key_attempt"]
    alpha_attempt = data["physical_action_anchor_key_attempt"]
    guardrails = data["guardrails"]

    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 5, proc.stdout),
        check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("u1 support partial", u1_attempt["filled_support"]["P_perp_policy"] is True and u1_attempt["filled_support"]["bad_shortcuts_rejected"] is True, u1_attempt["filled_support"]),
        check("u1 blocks exact source rows", "u1y_operator_row.operator_identity" in u1_attempt["blocking_fields"] and "spectrum_or_finite_part.positive_eigenvalues" in u1_attempt["blocking_fields"], u1_attempt["blocking_fields"]),
        check("u1 not promoted", u1_attempt["promotes"] is False and u1["status"].startswith("FILL_ATTEMPT"), (u1_attempt["promotes"], u1["status"])),
        check("alpha support partial", alpha_attempt["filled_support"]["m_theory_slot_identified"] is True and "Omega0_formula" in alpha_attempt["filled_support"], alpha_attempt["filled_support"]),
        check("alpha blocks dimensionful value", "dimensionful_quantity.value" in alpha_attempt["blocking_fields"] and "map_to_alpha_phys.alpha_phys_value" in alpha_attempt["blocking_fields"], alpha_attempt["blocking_fields"]),
        check("alpha not promoted", alpha_attempt["promotes"] is False and alpha["status"].startswith("FILL_ATTEMPT"), (alpha_attempt["promotes"], alpha["status"])),
        check("guardrails forbid fitting", all(value is False for value in guardrails.values()), guardrails),
        check("no closure", cert["closure_claimed"] is False and decision["measured_electroweak_closure"] is False and data["closure_claimed"] is False, decision),
        check("source augmentation note", "source-augmentation problem" in note and "dimensionful action anchor" in note, NOTE),
    ]
    print("\nSelected electroweak two-key fill attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
