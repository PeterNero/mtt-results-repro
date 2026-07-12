"""Audit alpha1 source-strength value gate reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import_alpha1_sourcestrength_value_gate_reduction.py"
PACKET = ROOT / "candidate_data" / "alpha1_sourcestrength_value_gate_reduction.candidate.json"
CERT = ROOT / "certificates" / "alpha1_sourcestrength_value_gate_reduction_certificate.json"
NOTE = ROOT / "proof_corpus" / "Alpha1_SourceStrength_Value_Gate_Reduction_v1.md"
STATUS = "ALPHA1_SOURCESTRENGTH_VALUE_GATE_REDUCED_TO_PHIFIN_DERIVATIVE_FILL_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    print(f"{'PASS' if condition else 'FAIL'}: {label} -- {detail}")
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

    check("status", cert["status"] == STATUS, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem agrees", packet["theorem"] == cert["theorem"], cert["theorem"])
    check("reduction theorem proved", cert["theorem"]["proved"] is True, cert["theorem"])
    check("all checks pass", all(packet["checks"].values()), packet["checks"])

    unit = packet["unit_candidate"]
    check(
        "unit candidate isolated not selected",
        unit["lambda_alpha1_candidate"] == 1.0
        and unit["selected_value_emitted"] is False
        and unit["alpha1_driver_verified"] is False,
        unit,
    )

    source = packet["source_identity_state"]
    check(
        "source identity closed but derivative open",
        source["same_source_identity_selected"]
        and source["visible_routec_operator_source_closed"]
        and source["typed_BN_derivative_closed"] is False
        and "same_branch_alpha1_derivative" in source["visible_remaining_lane_A_blockers"],
        source,
    )

    c1 = packet["c1_state"]
    check(
        "C1 engine not selected response",
        c1["primitive_C1_contraction_engine_built"]
        and c1["canonical_tensor_zero_response_result_proved_finitely"]
        and c1["selected_noninvariant_C1_primitive_or_vertex_open"]
        and c1["nonzero_C1_response_matrices_open"],
        c1,
    )

    update = packet["frontier_update"]
    check(
        "frontier moved to PhiFin derivative fill",
        update["current_next"] == "MTT_Visible_RouteC_PhiFinAlpha1Derivative_Fill_v1",
        update,
    )
    check("guardrails retained", all(v is True for v in cert["guardrails"].values()), cert["guardrails"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "lambda_alpha1 = 1",
        "N_alpha1(h_ext)=1",
        "same-branch `Phi_fin` alpha1 derivative",
        "C1 State",
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nAlpha1 source-strength value gate reduction audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
