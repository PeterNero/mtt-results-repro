"""Audit the U1/Y Gauduchon chamber or selected residual source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_gauduchon_chamber_or_selected_residual_source.py"
DATA = REPO / "candidate_data" / "selected_u1y_gauduchon_chamber_or_selected_residual_source.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_gauduchon_chamber_or_selected_residual_source_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_Gauduchon_Chamber_or_SelectedResidual_Source_v1.md"


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
    principle = data["principle_status"]
    stability = data["gauduchon_or_stability"]
    residual = data["residual_values"]
    operator = data["operator_payload"]
    decision = data["decision"]

    check(
        "status exact",
        data["status"] == "U1Y_GAUDUCHON_OR_SELECTED_RESIDUAL_GATE_ATTEMPTED_VISIBLE_SOURCE_SOLVE_REQUIRED",
        data["status"],
    )
    check(
        "principle axiom-ready but not unconditional",
        principle["corpus_support"] is True
        and principle["axiom_ready_not_unconditional"] is True
        and principle["literal_unconditional_statement_found"] is False
        and decision["terminal_principle_unconditional"] is False,
        principle,
    )
    check(
        "stability partial only",
        stability["non_split_extension_input"] is True
        and stability["selected_h1_8_nonzero_ext"] is True
        and stability["closed"] is False,
        stability,
    )
    check(
        "formal lift rejected",
        residual["honest_residual_zero"] is True
        and residual["honest_selected_source_verified"] is False
        and residual["formal_lift_selected_source_verified"] is True
        and residual["formal_lift_accepted_as_proof"] is False,
        residual,
    )
    check(
        "operator payload not closed",
        operator["promotion_gate_formulated"] is True
        and operator["orientation_packets_reach_validator_layer"] is True
        and operator["selected_source_origin_constructed"] is False
        and decision["same_source_operator_payload_closed"] is False,
        operator,
    )
    check(
        "certificate agrees",
        cert["gauduchon_chamber_or_hym_closed"] is False
        and cert["selected_routec_residual_values_closed"] is False
        and cert["lambda_12_closed"] is False,
        cert,
    )
    check(
        "note records next source solve",
        "Selected_U1Y_Visible_Bundle_or_RouteC_Source_Solve_v1" in note
        and "formal_lift_accepted_as_proof = false" in note
        and "terminal_principle_unconditional = false" in note,
        NOTE,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
