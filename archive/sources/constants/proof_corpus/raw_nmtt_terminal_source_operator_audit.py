"""Audit the finite raw N_MTT terminal source operator."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "construct_raw_nmtt_terminal_source_operator.py"
PACKET = ROOT / "candidate_data" / "raw_nmtt_terminal_source_operator.candidate.json"
CERT = ROOT / "certificates" / "raw_nmtt_terminal_source_operator_certificate.json"
NOTE = ROOT / "proof_corpus" / "Raw_N_MTT_Terminal_Source_Operator_v1.md"

STATUS = "RAW_NMTT_TERMINAL_SOURCE_OPERATOR_CONSTRUCTED_FINITE_MODEL_SMOOTH_RAW_OPEN"


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
    check("operator checks pass", all(packet["operator_checks"].values()), packet["operator_checks"])

    op = packet["operator_definition"]
    check(
        "operator has unique L3-K2 kernel",
        op["kernel_basis"] == ["L3-K2"]
        and op["spectral_gap"] > 0
        and op["basis"][2] == "L3-K2",
        op,
    )
    check(
        "matrix is diagonal nonnegative",
        all(
            op["matrix"][i][j] == (op["eigenvalues"][i] if i == j else 0.0)
            for i in range(len(op["matrix"]))
            for j in range(len(op["matrix"]))
        )
        and all(ev >= 0 for ev in op["eigenvalues"]),
        op["matrix"],
    )
    kernel = packet["finite_width_terminal_kernel"]
    w1 = kernel["weights_by_beta"]["1.0"]["selected_weight"]
    w4 = kernel["weights_by_beta"]["4.0"]["selected_weight"]
    w16 = kernel["weights_by_beta"]["16.0"]["selected_weight"]
    e1 = kernel["projection_error_bounds"]["1.0"]
    e4 = kernel["projection_error_bounds"]["4.0"]
    e16 = kernel["projection_error_bounds"]["16.0"]
    check(
        "finite heat kernel selects L3-K2 and contracts the complement",
        w1 < w16 and w1 <= w4 <= w16 and e1 > e4 > e16,
        {"selected_weights": (w1, w4, w16), "projection_error_bounds": (e1, e4, e16)},
    )
    check(
        "finite model closed but smooth raw open",
        packet["theorem"]["proved"] is True
        and packet["theorem"]["smooth_raw_operator_constructed"] is False
        and packet["verdict"]["finite_terminal_raw_operator_closed"] is True
        and packet["verdict"]["smooth_full_raw_N_MTT_closed"] is False,
        packet["theorem"],
    )
    check(
        "downstream gates retained",
        packet["what_remains_open"]["smooth_continuum_raw_N_MTT_operator"] is True
        and packet["what_remains_open"]["selected_dotD_alpha1_first_variation"] is True
        and packet["what_remains_open"]["primitive_C1_response_matrices"] is True,
        packet["what_remains_open"],
    )
    check(
        "guardrails all negative",
        all(v is False for v in packet["guardrails"].values()),
        packet["guardrails"],
    )

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "finite raw terminal `N_MTT`",
        "`L3-K2`",
        "exp(-beta N_MTT_terminal_q79)",
        "smooth continuum `N_MTT`",
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nRaw N_MTT terminal source operator audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
