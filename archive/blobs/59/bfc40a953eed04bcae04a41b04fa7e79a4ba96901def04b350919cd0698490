"""Audit typed/Cech End(E) basis or projective rho_E fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_typedcechende_basis_or_projectiverhoe_fill_attempt.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_typedcechende_basis_or_projectiverhoe_fill_attempt.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_typedcechende_basis_or_projectiverhoe_fill_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_TypedCechEndE_Basis_or_ProjectiveRhoE_FillAttempt_v1.md"

STATUS = "HETEROTIC_TYPEDCECHENDE_BASIS_OR_PROJECTIVERHOE_FILL_ATTEMPT_BLOCKED_VALUES_OPEN"


def check(label: str, condition: bool, detail: object) -> None:
    if not condition:
        print(f"FAIL: {label} -- {detail}")
        sys.exit(1)
    print(f"PASS: {label} -- {detail}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    check("script reruns", proc.returncode == 0, proc.stdout + proc.stderr)

    data = load(DATA)
    cert = load(CERT)
    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("fill executed open", data["decision"]["fill_attempt_executed"] is True and data["closure_claimed"] is False, data["decision"])
    check("lane counts zero", data["counts"]["lane_a_filled"] == 0 and data["counts"]["lane_b_filled"] == 0, data["counts"])

    lane_a = data["lane_a_typed_cech"]
    lane_b = data["lane_b_projective_rhoE"]
    check("typed lane blocked", lane_a["verdict"] == "BLOCKED_TYPED_MAPS_AND_CECH_DATA_NOT_EMITTED" and lane_a["blockers"]["typed_f_g_maps"].startswith("FAIL"), lane_a)
    check("projective lane blocked", lane_b["verdict"] == "BLOCKED_SELECTED_REPRESENTATIVE_AND_PROJECTIVE_RHOE_TABLES_NOT_EMITTED" and lane_b["blockers"]["projective_rhoE_tables"] is False, lane_b)
    check("support not values", lane_a["support"]["topological_monad_data"] == "PASS_SOURCE_PRINTED" and lane_b["support"]["projective_validator_pattern_available"] is True, (lane_a["support"], lane_b["support"]))
    check("response absent", lane_b["blockers"]["response_payload"] is False and lane_b["blockers"]["finite_response"] is False, lane_b["blockers"])
    check("no downstream closure", data["decision"]["E_Qa_computed"] is False and data["decision"]["same_source_identity_proved"] is False and data["decision"]["computed_threshold_value"] is False, data["decision"])
    check("guardrails", not any(data["guardrails"].values()), data["guardrails"])
    check("note records request", cert["next_required_artifact"] in NOTE.read_text(encoding="utf-8"), NOTE)

    print("\nSelected heterotic typed/Cech End(E) basis or projective rho_E fill attempt audit")


if __name__ == "__main__":
    main()
