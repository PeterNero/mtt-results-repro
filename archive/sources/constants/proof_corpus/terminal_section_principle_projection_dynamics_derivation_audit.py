"""Audit terminal section principle derivation from projection dynamics."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "derive_terminal_section_principle_from_projection_dynamics.py"
PACKET = ROOT / "candidate_data" / "terminal_section_principle_projection_dynamics_derivation.candidate.json"
CERT = ROOT / "certificates" / "terminal_section_principle_projection_dynamics_derivation_certificate.json"
NOTE = ROOT / "proof_corpus" / "Terminal_Section_Principle_from_Projection_Dynamics_v1.md"

STATUS = "TERMINAL_SECTION_PRINCIPLE_DERIVED_AT_REDUCED_FINITE_PROJECTION_LEVEL_RAW_NMTT_OPEN"


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
    script_packet = json.loads(proc.stdout)

    check("packet and cert match", packet == cert, {"packet": PACKET, "cert": CERT})
    check("script agrees", script_packet["status"] == packet["status"], script_packet["status"])
    check("status", packet["status"] == STATUS, packet["status"])
    check(
        "projection contract checks pass",
        all(packet["projection_contract_checks"].values()),
        packet["projection_contract_checks"],
    )
    check(
        "reduced selector checks pass",
        all(packet["reduced_selector_checks"].values()),
        packet["reduced_selector_checks"],
    )
    check(
        "derivation theorem proved in reduced scope",
        packet["theorem"]["proved"] is True
        and packet["theorem"]["scope"] == "reduced finite terminal survivor projection"
        and packet["theorem"]["raw_operator_constructed"] is False,
        packet["theorem"],
    )
    q79 = packet["q79_reduced_projection_evaluation"]
    check(
        "unique survivor is L3-K2",
        q79["finite_survivors"] == ["L3-K2"]
        and q79["selected_survivor"] == "L3-K2"
        and q79["selected_L"] == [1, -2, 0],
        q79,
    )
    check(
        "raw and downstream gates retained",
        packet["what_remains_open"]["construct_raw_N_MTT_terminal_source_operator"] is True
        and packet["what_remains_open"]["derive_smooth_finite_width_terminal_kernel_not_only_sharp_limit"] is True
        and packet["what_remains_open"]["selected_dotD_alpha1_first_variation"] is True,
        packet["what_remains_open"],
    )
    check(
        "guardrails all negative",
        all(v is False for v in packet["guardrails"].values()),
        packet["guardrails"],
    )
    check(
        "verdict distinguishes reduced from raw closure",
        packet["verdict"]["deeper_task_closed_at_reduced_level"] is True
        and packet["verdict"]["full_raw_projection_dynamics_closed"] is False
        and packet["verdict"]["q79_L3_K2_no_longer_axiom_only"] is True,
        packet["verdict"],
    )

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "finite projection level",
        "`L3-K2`",
        "`N_MTT`",
        "sharp-survivor limit",
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nTerminal section principle projection-dynamics derivation audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
