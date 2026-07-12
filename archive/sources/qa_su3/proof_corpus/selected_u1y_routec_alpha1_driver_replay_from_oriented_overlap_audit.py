"""Audit the U1/Y Route-C alpha1 driver replay from oriented overlap gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_alpha1_driver_replay_from_oriented_overlap.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_alpha1_driver_replay_from_oriented_overlap.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_alpha1_driver_replay_from_oriented_overlap_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_Alpha1_Driver_Replay_from_OrientedOverlap_v1.md"

STATUS = "U1Y_ROUTEC_ALPHA1_DRIVER_REPLAY_CLOSED_PRIMITIVE_C1_LAMBDA_OPEN"
NEXT = "Selected_U1Y_RouteC_Primitive_C1_Contractions_or_Lambda12_Gate_v1"


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
    note = NOTE.read_text(encoding="utf-8")
    reqs = data["alpha_requirements"]
    value = data["promoted_value"]
    replay = data["honest_dotd_replay"]
    guards = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("all alpha requirements", all(reqs.values()), reqs),
        check("value promoted", cert["selected_N_alpha1_h_ext_value"] is True and value["N_alpha1_h_ext"] == 1.0 and value["du_dalpha1"] == "h_ext", value),
        check("alpha closed", cert["du_dalpha1_equals_h_ext"] is True and cert["alpha1_driver_verified"] is True, cert),
        check("honest replay closed", cert["honest_dotD_validator_closed"] is True and replay["honest_dotD_validator_closed"] is True, replay),
        check("not lifted flags", "not diagnostic flags" in replay["why_not_lifted_flags"], replay["why_not_lifted_flags"]),
        check("remaining gates open", cert["primitive_C1_contractions_closed"] is False and cert["lambda_12_closed"] is False, cert),
        check("guardrails hold", guards["claims_lambda12"] is False and guards["uses_observed_data"] is False and data["target_fitting_used"] is False, guards),
        check("note records boundary", "not primitive C1 contractions" in note and "Operator-layer Pic0" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C alpha1 driver replay from oriented overlap audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
